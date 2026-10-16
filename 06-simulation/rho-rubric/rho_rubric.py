"""
rho_rubric.py -- score claim 2 of disparity_ceiling_sim.py (the clearing rate rho*)
on the sensitivity / specificity / coverage rubric.

The artifact under test is IMPORTED, not reimplemented: draw_population and
clearing_rho come from 06-simulation/disparity-ceiling/disparity_ceiling_sim.py.
The only new code is (a) an exact solver for rho* (the file's own solver snaps to
a 200-point grid, step 0.0176, which would put a floor under every move), (b) the
faults, and (c) the paired-seed statistics.

Model of claim 2, unchanged:  a_i = max(0.1, c_i * LogNormal(ln 1.6, 0.5)),
K = 1.15 * sum(c),  rho* solves  sum_i min(a_i, rho * c_i) = K.

Run:  python rho_rubric.py            # full run, 30 seeds, N = 200,000
      python rho_rubric.py --test     # self-tests only
      python rho_rubric.py --seeds 5 --n 20000   # quick look
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "disparity-ceiling"))
import disparity_ceiling_sim as dcs  # noqa: E402

PROD = 1.15                 # productivity in claim2_market_and_shocks
FAULT_STREAM = 10_000_000   # fault RNG = seed + this, so the base draw is shared
N_DEFAULT = 200_000
SEEDS_DEFAULT = 30
GRID = np.linspace(0.5, 4.0, 200)   # the file's own search grid


# ---------------------------------------------------------------------------
# population (same draws as claim2_market_and_shocks, per seed)
# ---------------------------------------------------------------------------

def r_draw(rng, n):
    return rng.lognormal(mean=np.log(1.6), sigma=0.5, size=n)


def draw_base(seed, n):
    rng = np.random.default_rng(seed)
    c = dcs.draw_population(n, rng)
    a = np.maximum(0.1, c * r_draw(rng, n))
    return c, a, PROD * c.sum()


# ---------------------------------------------------------------------------
# exact demand curve and exact rho*
# ---------------------------------------------------------------------------

class Curve:
    """demand(rho) = sum_i min(a_i, rho c_i), exactly, from sorted thresholds."""

    def __init__(self, c, a):
        t = a / c
        o = np.argsort(t, kind="stable")
        self.ts = t[o]
        self.A = np.cumsum(a[o])
        self.C = np.cumsum(c[o])
        self.Ctot = float(self.C[-1])
        self.Atot = float(self.A[-1])
        self.bp = self.A + self.ts * (self.Ctot - self.C)   # demand at each breakpoint

    def demand(self, rho):
        rho = np.asarray(rho, float)
        k = np.searchsorted(self.ts, rho, side="right")
        Ak = np.where(k > 0, self.A[np.maximum(k - 1, 0)], 0.0)
        Ck = np.where(k > 0, self.C[np.maximum(k - 1, 0)], 0.0)
        return Ak + rho * (self.Ctot - Ck)

    def rho_star(self, K):
        """Exact clearing rho; nan if demand never reaches K (post-scarcity)."""
        if self.Atot < K:
            return float("nan")
        idx = int(np.searchsorted(self.bp, K, side="left"))
        if idx == 0:
            return K / self.Ctot
        rest = self.Ctot - self.C[idx - 1]
        return float((K - self.A[idx - 1]) / rest)

    def grid_rho(self, K):
        """What the file's clearing_rho returns: nearest grid point to capacity."""
        if self.demand(GRID[-1]) < K:
            return float("nan")
        return float(GRID[np.argmin(np.abs(self.demand(GRID) - K))])


def rho_star(c, a, K):
    return Curve(c, a).rho_star(K)


# ---------------------------------------------------------------------------
# faults.  Each takes (c, a, K, rng) and returns (c', a', K').
# K' is what the faulted BOOKS say capacity is.  Capacity in claim 2 is defined as
# 1.15 * (recorded credit), so a fault that adds recorded credit adds capacity
# unless the physical variant (K held at the true value) is asked for.
# ---------------------------------------------------------------------------

def f_none(c, a, K, rng):
    return c, a, K


def f_cap(m):
    return lambda c, a, K, rng: (c, a, K * m)


def f_appetite(m):
    return lambda c, a, K, rng: (c, a * m, K)


def f_fab(count, appetite="typical", tied=True):
    """Insert `count` fabricated accounts at the floor F."""
    def f(c, a, K, rng):
        cf = np.full(count, dcs.F)
        if appetite == "typical":
            af = np.maximum(0.1, cf * r_draw(rng, count))
        elif appetite == "zero":
            af = np.zeros(count)
        else:
            raise ValueError(appetite)
        c2, a2 = np.concatenate([c, cf]), np.concatenate([a, af])
        return c2, a2, (PROD * c2.sum() if tied else K)
    return f


def f_omit_accounts(frac):
    """A random `frac` of accounts have their consumption left out of the books."""
    def f(c, a, K, rng):
        a2 = a.copy()
        a2[rng.random(len(a)) < frac] = 0.0
        return c, a2, K
    return f


def f_shuffle_all(c, a, K, rng):
    return c, a[rng.permutation(len(a))], K


def f_shuffle_decile(c, a, K, rng):
    """Move appetite between accounts of similar credit (same decile of c)."""
    o = np.argsort(c, kind="stable")
    a2 = a.copy()
    for blk in np.array_split(o, 10):
        a2[blk] = a[blk][rng.permutation(len(blk))]
    return c, a2, K


def f_reorder(c, a, K, rng):
    p = rng.permutation(len(c))
    return c[p], a[p], K


def f_rescale(k):
    return lambda c, a, K, rng: (c * k, a * k, K * k)


# (id, kind, label, fault, expected direction: -1 down, +1 up, 0 none)
LEG1 = [
    ("S1",  "sens", "capacity -30%",                       f_cap(0.70),            -1),
    ("S2",  "sens", "capacity +25%",                       f_cap(1.25),            +1),
    ("S3",  "sens", "every appetite +25% (re-weighting)",  f_appetite(1.25),       -1),
    ("S4a", "sens", "+20,000 fabricated floor accts, typical appetite, K tied to credit", f_fab(20_000, "typical", True), 0),
    ("S4b", "sens", "+20,000 fabricated floor accts, typical appetite, K physical",       f_fab(20_000, "typical", False), -1),
    ("S4c", "sens", "+20,000 phantom floor accts, zero appetite, K tied to credit",       f_fab(20_000, "zero", True), +1),
    ("S5a", "sens", "20% of accounts' consumption omitted", f_omit_accounts(0.20), +1),
    ("S5b", "sens", "every account's consumption x0.8",     f_appetite(0.80),       +1),
    ("S6a", "sens", "shuffle appetite across ALL accounts, total fixed",       f_shuffle_all,    0),
    ("S6b", "sens", "shuffle appetite within credit deciles, total fixed",     f_shuffle_decile, 0),
]
LEG2 = [
    ("U0", "spec", "no fault (null)",                     f_none,      0),
    ("U1", "spec", "reorder the accounts",                f_reorder,   0),
    ("U2", "spec", "rescale every unit x2 (c, a, K)",     f_rescale(2.0), 0),
]
SWEEP_CAP = [0.999, 0.995, 0.99, 0.98, 0.95, 0.90]       # smallest capacity shift seen
SWEEP_FAB = [2_000, 5_000, 20_000, 50_000]


# ---------------------------------------------------------------------------
# paired run
# ---------------------------------------------------------------------------

def run_challenge(fault, seeds, n, grid=False):
    clean, faulted, gclean, gfault, equiv = [], [], [], [], []
    for s in seeds:
        c, a, K = draw_base(s, n)
        cu = Curve(c, a)
        r0 = cu.rho_star(K)
        c2, a2, K2 = fault(c, a, K, np.random.default_rng(s + FAULT_STREAM))
        f = Curve(c2, a2)
        r1 = f.rho_star(K2)
        clean.append(r0); faulted.append(r1)
        # capacity multiplier on the CLEAN books that reproduces the faulted rho*
        equiv.append(float(cu.demand(r1) / K) if np.isfinite(r1) else float("nan"))
        if grid:
            gclean.append(cu.grid_rho(K)); gfault.append(f.grid_rho(K2))
    clean, faulted, equiv = map(np.array, (clean, faulted, equiv))
    d = faulted - clean
    out = dict(clean=clean, faulted=faulted, d=d, equiv=equiv,
               n_nan=int(np.isnan(faulted).sum()))
    if grid:
        out["gd"] = np.array(gfault) - np.array(gclean)
        out["gclean"] = np.array(gclean)
    return out


def summarise(res, expect):
    d = res["d"]
    ok = ~np.isnan(d)
    d = d[ok]
    m, sd = float(d.mean()), float(d.std(ddof=1)) if len(d) > 1 else float("nan")
    cl, fa = res["clean"][ok], res["faulted"][ok]
    sc, sf = cl.std(ddof=1), fa.std(ddof=1)
    r = float(np.corrcoef(cl, fa)[0, 1]) if sc > 0 and sf > 0 else float("nan")
    z = m / (sd / np.sqrt(len(d))) if sd > 0 else (0.0 if m == 0 else float("inf"))
    fires = bool(abs(m) >= 2 * sd) if sd > 0 else bool(abs(m) > 1e-9)
    sign_ok = (expect == 0) or (np.sign(m) == expect)
    return dict(clean=float(cl.mean()), clean_sd=float(sc), faulted=float(fa.mean()),
                move=m, sd_paired=sd, sd_unpaired=float(np.hypot(sc, sf)), r=r, z=float(z),
                fires=fires, sign_ok=bool(sign_ok), equiv=float(np.nanmean(res["equiv"])))


# ---------------------------------------------------------------------------
# self-tests -- each can fail
# ---------------------------------------------------------------------------

def _brute_rho(c, a, K):
    lo, hi = 0.0, 1e6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if np.minimum(a, mid * c).sum() < K:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def test_solver_matches_bruteforce():
    for s in (1, 2, 3):
        c, a, K = draw_base(s, 5_000)
        assert abs(rho_star(c, a, K) - _brute_rho(c, a, K)) < 1e-8, "exact solver disagrees with bisection"
    print("[ok] exact solver matches 200-step bisection to 1e-8 on 3 populations")


def test_grid_matches_the_files_own_function():
    c, a, K = draw_base(1, 20_000)
    theirs, _, _ = dcs.clearing_rho(c, a, K)
    ours = Curve(c, a).grid_rho(K)
    assert abs(theirs - ours) < 1e-12, f"grid reimplementation {ours} != imported clearing_rho {theirs}"
    print(f"[ok] grid version equals the imported clearing_rho ({theirs:.4f})")


def test_capacity_direction():
    c, a, K = draw_base(1, 20_000)
    lo, mid, hi = rho_star(c, a, 0.5 * K), rho_star(c, a, K), rho_star(c, a, 2 * K)
    assert lo < mid < hi, f"capacity must loosen rho*: {lo} {mid} {hi}"
    print(f"[ok] halving capacity tightens ({lo:.3f}), doubling loosens ({hi:.3f}), base {mid:.3f}")


def test_zero_appetite_never_binds():
    c, _, K = draw_base(1, 5_000)
    assert np.isnan(rho_star(c, np.zeros_like(c), K)), "zero demand must read as 'never binds'"
    print("[ok] zero appetite everywhere -> never binds (nan), not an error")


def test_null_fault_moves_exactly_zero():
    res = run_challenge(f_none, [1, 2, 3], 5_000)
    assert np.all(res["d"] == 0.0), "null fault moved rho*: the pairing leaks"
    print("[ok] null fault moves rho* by exactly 0.0 over 3 seeds")


def test_pairing_shares_the_base_population():
    c, a, K = draw_base(5, 5_000)
    c2, a2, K2 = draw_base(5, 5_000)
    assert np.array_equal(c, c2) and np.array_equal(a, a2) and K == K2
    c3, a3, _ = f_fab(100)(c, a, K, np.random.default_rng(5 + FAULT_STREAM))
    assert np.array_equal(c3[:5_000], c) and len(c3) == 5_100 and np.all(c3[5_000:] == dcs.F)
    print("[ok] same seed -> identical base; fabricated accounts are appended at exactly F")


def test_a_known_size_fault_fires_and_a_tiny_one_does_not():
    big = summarise(run_challenge(f_cap(0.70), range(1, 9), 20_000), -1)
    assert big["fires"] and big["move"] < 0, "a -30% capacity shock must fire"
    tiny = summarise(run_challenge(f_cap(1.0 + 1e-9), range(1, 9), 20_000), 0)
    assert not tiny["fires"] or abs(tiny["move"]) < 1e-6, "a 1e-9 capacity change should be below any bar"
    print(f"[ok] -30% capacity fires (move {big['move']:+.3f}, bar {2*big['sd_paired']:.4f}); 1e-9 does not")


def test_scale_invariance_is_exact():
    res = summarise(run_challenge(f_rescale(2.0), range(1, 5), 20_000), 0)
    assert abs(res["move"]) < 1e-9, f"rescaling units moved rho* by {res['move']}"
    print("[ok] rescaling every unit x2 leaves rho* unchanged (<1e-9)")


def test_typical_fabricated_accounts_are_neutral_by_identity():
    """a = c*r  =>  demand = sum c*min(r, rho).  An inserted account with typical r
    and K tied to credit changes both sides by the same share, so the move is noise."""
    res = summarise(run_challenge(f_fab(20_000, "typical", True), range(1, 11), 50_000), 0)
    assert abs(res["move"]) < 3 * res["sd_paired"] + 1e-4, "S4a moved by more than sampling noise"
    # and the same fault with a zero-appetite phantom must NOT be neutral, or the test is blind
    ph = summarise(run_challenge(f_fab(20_000, "zero", True), range(1, 11), 50_000), +1)
    assert ph["move"] > 10 * abs(res["move"]) and ph["move"] > 0.02, "phantom accounts should loosen rho*"
    print(f"[ok] typical fabricated accts move {res['move']:+.4f} (noise {res['sd_paired']:.4f}); "
          f"zero-appetite phantoms move {ph['move']:+.3f}")


def run_tests():
    test_solver_matches_bruteforce()
    test_grid_matches_the_files_own_function()
    test_capacity_direction()
    test_zero_appetite_never_binds()
    test_null_fault_moves_exactly_zero()
    test_pairing_shares_the_base_population()
    test_a_known_size_fault_fires_and_a_tiny_one_does_not()
    test_scale_invariance_is_exact()
    test_typical_fabricated_accounts_are_neutral_by_identity()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

def fmt_row(cid, leg, label, s, expect):
    arrow = {-1: "down", 0: "none", 1: "up"}[expect]
    fires = "YES" if s["fires"] else "no"
    sign = "" if expect == 0 else ("" if s["sign_ok"] else "  WRONG WAY")
    return (f"{cid:<4}{leg:<5}{s['clean']:>8.4f}{s['faulted']:>9.4f}{s['move']:>+9.4f}"
            f"{s['sd_paired']:>9.5f}{2*s['sd_paired']:>9.5f}{s['sd_unpaired']:>9.5f}{s['r']:>7.3f}"
            f"{s['z']:>8.1f}  {fires:<4} (exp {arrow}){sign}  {label}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--seeds", type=int, default=SEEDS_DEFAULT)
    ap.add_argument("--n", type=int, default=N_DEFAULT)
    a = ap.parse_args()
    if a.test:
        run_tests()
        return 0

    decl = os.path.join(HERE, "DECLARED.md")
    h = hashlib.sha256(open(decl, "rb").read()).hexdigest()[:16]
    print(f"DECLARED.md sha256 prefix: {h}   (printed before any statistic is computed)")
    seeds = list(range(1, a.seeds + 1))
    print(f"N = {a.n:,}   seeds = 1..{a.seeds}   F = {dcs.F:g}   fault stream = seed + {FAULT_STREAM:,}")
    print("=" * 150)
    hdr = (f"{'id':<4}{'leg':<5}{'clean':>8}{'faulted':>9}{'move':>9}{'sd(pair)':>9}{'2*sd':>9}"
           f"{'sd(unp)':>9}{'r':>7}{'z':>8}  fires")
    print(hdr)
    print("-" * 150)
    rows = {}
    for cid, leg, label, fault, expect in LEG1 + LEG2:
        res = run_challenge(fault, seeds, a.n, grid=cid in ("U0", "S1", "S3", "S5a"))
        s = summarise(res, expect)
        rows[cid] = (res, s, label)
        print(fmt_row(cid, leg, label, s, expect))
        if res["n_nan"]:
            print(f"      ({res['n_nan']} seeds never bind after the fault; excluded from the mean)")
    print("=" * 150)

    print("\nCLEAN BASELINE (exact solver):  "
          f"mean {rows['U0'][1]['clean']:.4f}   sd across seeds {rows['U0'][1]['clean_sd']:.5f}")
    g = rows["U0"][0]["gclean"]
    print(f"CLEAN BASELINE (file's 200-point grid, step {GRID[1]-GRID[0]:.4f}):  "
          f"mean {g.mean():.4f}   sd across seeds {g.std(ddof=1):.5f}")

    print("\nGRID vs EXACT, paired move (the file's own solver snaps to a grid):")
    for cid in ("S1", "S3", "S5a"):
        res, s, _ = rows[cid]
        gd = res["gd"]
        print(f"  {cid}: exact move {s['move']:+.4f}   grid move {gd.mean():+.4f}   "
              f"grid sd(pair) {gd.std(ddof=1):.5f}")

    print("\nOBSERVATIONAL EQUIVALENCE: the capacity multiplier on clean books that reproduces "
          "each fault's rho* (mean over seeds)")
    for cid in ("S3", "S4b", "S4c", "S5a", "S5b", "S6a", "S6b"):
        res, s, label = rows[cid]
        print(f"  {cid:<4} capacity x{s['equiv']:.4f}  ({(s['equiv']-1)*100:+.2f}%)   {label}")

    print("\nSMALLEST CAPACITY SHIFT THAT FIRES (sensitivity floor in capacity terms):")
    for m in SWEEP_CAP:
        s = summarise(run_challenge(f_cap(m), seeds, a.n), -1)
        print(f"  capacity x{m:<6} move {s['move']:+.5f}  bar(2sd) {2*s['sd_paired']:.5f}  "
              f"{'fires' if s['fires'] else 'no'}")

    print("\nFABRICATION SWEEP (how many fabricated floor accounts before rho* moves past the bar):")
    for tag, appetite, tied in (("typical, K tied", "typical", True),
                                ("typical, K physical", "typical", False),
                                ("zero appetite, K tied", "zero", True)):
        for cnt in SWEEP_FAB:
            s = summarise(run_challenge(f_fab(cnt, appetite, tied), seeds, a.n), 0)
            print(f"  {tag:<22} +{cnt:>6,} accts ({cnt/a.n*100:4.1f}%)  move {s['move']:+.5f}  "
                  f"bar(2sd) {2*s['sd_paired']:.5f}  {'fires' if s['fires'] else 'no'}")

    print("\nPAIRING (brief 7a): S1 noise on the move, three ways")
    s = rows["S1"][1]
    print(f"  clean-arm sd {s['clean_sd']:.5f};  paired-difference sd {s['sd_paired']:.5f};  "
          f"unpaired sd {s['sd_unpaired']:.5f};  r(clean, faulted) = {s['r']:.4f}")
    print(f"  S4a move {rows['S4a'][1]['move']:+.5f} vs paired bar {2*rows['S4a'][1]['sd_paired']:.5f} "
          f"vs unpaired bar {2*rows['S4a'][1]['sd_unpaired']:.5f}")
    print("\nLEG 3 (coverage witness): UNAVAILABLE on a generator. rho* is computed from the "
          "population it describes; no outside total exists here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
