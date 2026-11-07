"""
detection_dose.py -- detection-dose curve for the clearing rate rho*.

For each of three declared debit dispersions (sigma of ln r) and each of three
fabrication arms, find the smallest number of fabricated floor accounts at which
the PAIRED move in rho* clears k paired standard deviations.  k = 2, fixed in
DECLARED.md before the first run.  Seeds are paired between clean and faulted arms.

The model is IMPORTED from ../rho-rubric/rho_rubric.py (exact rho* solver, Curve,
population draw).  The only new code: a sigma parameter on the draw, the dose
sweep, and the two noise bars.

Run:  python detection_dose.py --test
      python detection_dose.py                  # full: N=200,000, 2 blocks x 30 seeds
      python detection_dose.py --n 20000 --seeds 6 --blocks 1   # quick look
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sys
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "rho-rubric"))
import rho_rubric as rr  # noqa: E402
dcs = rr.dcs

K_SD = 2.0
SIGMAS = (0.25, 0.50, 1.00)
DOSES = (1, 3, 10, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000)
ARMS = {  # name: (appetite, K tied to recorded credit?)
    "P": ("zero", True),
    "T": ("typical", True),
    "Q": ("typical", False),
}
BLOCKS = {"A": 1, "B": 101}   # first seed of each 30-seed block
N_DEFAULT = 200_000
SEEDS_DEFAULT = 30


def draw_base_sigma(seed, n, sigma):
    """Same draw order as rr.draw_base, with the appetite spread as a parameter."""
    rng = np.random.default_rng(seed)
    c = dcs.draw_population(n, rng)
    r = rng.lognormal(mean=np.log(1.6), sigma=sigma, size=n)
    a = np.maximum(0.1, c * r)
    return c, a, rr.PROD * c.sum()


def fault_arm(count, arm, sigma, c, a, K, seed):
    appetite, tied = ARMS[arm]
    rng = np.random.default_rng(seed + rr.FAULT_STREAM)
    cf = np.full(count, dcs.F)
    if appetite == "typical":
        af = np.maximum(0.1, cf * rng.lognormal(np.log(1.6), sigma, size=count))
    else:
        af = np.zeros(count)
    c2, a2 = np.concatenate([c, cf]), np.concatenate([a, af])
    return c2, a2, (rr.PROD * c2.sum() if tied else K)


def run_cell(job):
    """One (sigma, block): all arms, all doses, all seeds.  Returns arrays of rho*."""
    sigma, block, n, nseeds, doses = job
    s0 = BLOCKS[block]
    seeds = list(range(s0, s0 + nseeds))
    clean = np.empty(nseeds)
    out = {(arm, d): np.empty(nseeds) for arm in ARMS for d in doses}
    for i, s in enumerate(seeds):
        c, a, K = draw_base_sigma(s, n, sigma)
        clean[i] = rr.Curve(c, a).rho_star(K)
        for arm in ARMS:
            for d in doses:
                c2, a2, K2 = fault_arm(d, arm, sigma, c, a, K, s)
                out[(arm, d)][i] = rr.Curve(c2, a2).rho_star(K2)
    return sigma, block, clean, out


def stats(clean, faulted):
    d = faulted - clean
    ok = ~np.isnan(d)
    d, cl, fa = d[ok], clean[ok], faulted[ok]
    m = float(d.mean())
    sd_p = float(d.std(ddof=1))
    sd_u = float(np.hypot(cl.std(ddof=1), fa.std(ddof=1)))
    return dict(move=m, sd_p=sd_p, sd_u=sd_u, n_ok=int(ok.sum()),
                ratio_p=abs(m) / sd_p if sd_p > 0 else (0.0 if m == 0 else float("inf")),
                ratio_u=abs(m) / sd_u if sd_u > 0 else float("inf"))


def first_clearing(doses, ratios, k=K_SD):
    """Smallest grid dose with ratio >= k; plus a log-log interpolated crossing between the
    last failing and first passing grid points (None if no pass, or if the first dose passes)."""
    for j, (d, r) in enumerate(zip(doses, ratios)):
        if r >= k:
            if j == 0:
                return d, None
            r0, r1, d0 = ratios[j - 1], r, doses[j - 1]
            if r0 <= 0:
                return d, None
            t = (np.log(k) - np.log(r0)) / (np.log(r1) - np.log(r0))
            return d, float(np.exp(np.log(d0) + t * (np.log(d) - np.log(d0))))
    return None, None


# ---------------------------------------------------------------------------
# self-tests -- each can fail
# ---------------------------------------------------------------------------

def test_draw_matches_rubric_at_file_sigma():
    c, a, K = draw_base_sigma(7, 5_000, 0.5)
    c0, a0, K0 = rr.draw_base(7, 5_000)
    assert np.array_equal(c, c0) and np.array_equal(a, a0) and K == K0, "sigma draw differs from the rubric's"
    print("[ok] sigma-parameterised draw equals rho_rubric.draw_base at sigma = 0.5")


def test_sigma_changes_the_population():
    _, a1, _ = draw_base_sigma(3, 5_000, 0.25)
    _, a2, _ = draw_base_sigma(3, 5_000, 1.00)
    assert a2.std() > 2 * a1.std(), "sigma = 1.0 should spread appetite far more than 0.25"
    print("[ok] sigma = 1.0 spreads appetite more than twice as much as sigma = 0.25")


def test_zero_dose_moves_exactly_zero():
    c, a, K = draw_base_sigma(2, 5_000, 0.5)
    r0 = rr.Curve(c, a).rho_star(K)
    for arm in ARMS:
        c2, a2, K2 = fault_arm(0, arm, 0.5, c, a, K, 2)
        assert rr.Curve(c2, a2).rho_star(K2) == r0, f"arm {arm}: zero dose moved rho*"
    print("[ok] dose 0 moves rho* by exactly 0.0 in every arm")


def test_arm_signs_and_monotone_phantom():
    c, a, K = draw_base_sigma(4, 20_000, 0.5)
    r0 = rr.Curve(c, a).rho_star(K)
    last = 0.0
    for d in (100, 1_000, 5_000):
        p = rr.Curve(*fault_arm(d, "P", 0.5, c, a, K, 4)[:2]).rho_star(fault_arm(d, "P", 0.5, c, a, K, 4)[2]) - r0
        assert p > last, "phantom accounts must loosen rho* more as the dose grows"
        last = p
    q = rr.Curve(*fault_arm(5_000, "Q", 0.5, c, a, K, 4)[:2]).rho_star(fault_arm(5_000, "Q", 0.5, c, a, K, 4)[2]) - r0
    assert q < 0, "typical accounts with K physical must tighten rho*"
    print(f"[ok] P loosens monotonically (to {last:+.4f} at 5,000), Q tightens ({q:+.4f})")


def test_first_clearing_finds_a_known_crossing():
    ds = (1, 10, 100, 1000)
    d, interp = first_clearing(ds, [0.1, 0.5, 4.0, 40.0])
    assert d == 100 and 10 < interp < 100, (d, interp)
    d2, _ = first_clearing(ds, [0.1, 0.2, 0.3, 0.4])
    assert d2 is None, "a ratio that never reaches k must not report a dose"
    d3, i3 = first_clearing(ds, [5.0, 6.0, 7.0, 8.0])
    assert d3 == 1 and i3 is None
    print("[ok] first_clearing: finds 100, refuses when nothing clears, flags a clear at the lowest dose")


def test_criterion_can_fail_and_can_pass():
    rng = np.random.default_rng(0)
    clean = rng.normal(1.2, 0.01, 30)
    assert stats(clean, clean + rng.normal(0, 0.001, 30))["ratio_p"] < K_SD, "pure noise must not clear k"
    assert stats(clean, clean + 0.5 + rng.normal(0, 0.001, 30))["ratio_p"] > K_SD, "a big move must clear k"
    print("[ok] the k-sd criterion fails on pure noise and passes on a large move")


def test_typical_tied_is_neutral_small_scale():
    s = stats(*_pair(0.5, "T", 10_000, 8, 20_000))
    assert s["ratio_p"] < K_SD, f"arm T cleared k at 10,000 accounts (ratio {s['ratio_p']:.2f})"
    ph = stats(*_pair(0.5, "P", 10_000, 8, 20_000))
    assert ph["ratio_p"] > K_SD and ph["move"] > 0, "arm P at 10,000 accounts must clear -- else the test above is blind"
    print(f"[ok] arm T ratio {s['ratio_p']:.2f} < {K_SD}; arm P ratio {ph['ratio_p']:.1f} > {K_SD}")


def _pair(sigma, arm, d, nseeds, n):
    cl, fa = [], []
    for s in range(1, nseeds + 1):
        c, a, K = draw_base_sigma(s, n, sigma)
        cl.append(rr.Curve(c, a).rho_star(K))
        c2, a2, K2 = fault_arm(d, arm, sigma, c, a, K, s)
        fa.append(rr.Curve(c2, a2).rho_star(K2))
    return np.array(cl), np.array(fa)


def run_tests():
    rr.test_solver_matches_bruteforce()
    test_draw_matches_rubric_at_file_sigma()
    test_sigma_changes_the_population()
    test_zero_dose_moves_exactly_zero()
    test_arm_signs_and_monotone_phantom()
    test_first_clearing_finds_a_known_crossing()
    test_criterion_can_fail_and_can_pass()
    test_typical_tied_is_neutral_small_scale()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--n", type=int, default=N_DEFAULT)
    ap.add_argument("--seeds", type=int, default=SEEDS_DEFAULT)
    ap.add_argument("--blocks", type=int, default=2)
    ap.add_argument("--procs", type=int, default=6)
    a = ap.parse_args()
    if a.test:
        run_tests()
        return 0

    h = hashlib.sha256(open(os.path.join(HERE, "DECLARED.md"), "rb").read()).hexdigest()[:16]
    print(f"DECLARED.md sha256 prefix: {h}   (printed before any statistic is computed)")
    blocks = list(BLOCKS)[: a.blocks]
    print(f"N = {a.n:,}  seeds/block = {a.seeds}  blocks = {blocks} (first seeds {[BLOCKS[b] for b in blocks]})"
          f"  F = {dcs.F:g}  k = {K_SD:g}  fault stream = seed + {rr.FAULT_STREAM:,}")
    jobs = [(s, b, a.n, a.seeds, DOSES) for s in SIGMAS for b in blocks]
    with Pool(min(a.procs, len(jobs))) as pool:
        results = pool.map(run_cell, jobs)
    res = {(s, b): (cl, out) for s, b, cl, out in results}

    for b in blocks:
        print("\n" + "=" * 132)
        print(f"BLOCK {b}   (seeds {BLOCKS[b]}..{BLOCKS[b] + a.seeds - 1})")
        for s in SIGMAS:
            cl, out = res[(s, b)]
            print(f"\n  sigma = {s}   clean rho* mean {cl.mean():.4f}   sd across seeds {cl.std(ddof=1):.5f}")
            for arm in ARMS:
                print(f"   arm {arm}  ({ARMS[arm][0]} appetite, K {'tied' if ARMS[arm][1] else 'physical'})")
                print(f"   {'dose':>8}{'% of N':>9}{'mean move':>12}{'sd paired':>12}{'sd unpaired':>13}"
                      f"{'move/sd_p':>11}{'move/sd_u':>11}   B1  B3")
                rp, ru = [], []
                for d in DOSES:
                    st = stats(cl, out[(arm, d)])
                    rp.append(st["ratio_p"]); ru.append(st["ratio_u"])
                    print(f"   {d:>8,}{d / a.n * 100:>8.3f}%{st['move']:>+12.6f}{st['sd_p']:>12.7f}{st['sd_u']:>13.6f}"
                          f"{st['ratio_p']:>11.2f}{st['ratio_u']:>11.2f}   "
                          f"{'Y' if st['ratio_p'] >= K_SD else '.'}   {'Y' if st['ratio_u'] >= K_SD else '.'}")
                d1, i1 = first_clearing(DOSES, rp)
                d3, i3 = first_clearing(DOSES, ru)
                f = lambda d, i: "none in grid" if d is None else (f"{d:,} (lowest dose tried)" if i is None and d == DOSES[0]
                                                                  else f"{d:,}  (interpolated {i:,.0f})")
                print(f"   -> smallest dose clearing B1 (paired):   {f(d1, i1)}")
                print(f"   -> smallest dose clearing B3 (unpaired): {f(d3, i3)}")
    print("\nSUMMARY (block A unless stated): smallest grid dose clearing each bar")
    print(f"{'sigma':>6} {'arm':>4}" + "".join(f"{'B1 ' + b:>14}{'B3 ' + b:>14}" for b in blocks))
    for s in SIGMAS:
        for arm in ARMS:
            row = f"{s:>6} {arm:>4}"
            for b in blocks:
                cl, out = res[(s, b)]
                rp = [stats(cl, out[(arm, d)])["ratio_p"] for d in DOSES]
                ru = [stats(cl, out[(arm, d)])["ratio_u"] for d in DOSES]
                d1, _ = first_clearing(DOSES, rp); d3, _ = first_clearing(DOSES, ru)
                row += f"{('none' if d1 is None else format(d1, ',')):>14}{('none' if d3 is None else format(d3, ',')):>14}"
            print(row)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
