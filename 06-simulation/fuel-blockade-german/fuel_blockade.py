#!/usr/bin/env python3
"""
fuel_blockade.py -- fuel blockade at the German method.
Request sr-20261111-fuel-blockade-at-the-german-method-same-popu.

Same population, gate and settings as ../german-prime-sweep/german_prime_sweep.py (imported, not copied):
stock gate, P = 0, essentials ungated at E = 437.2 and 462.3 h, services off the receiver, joiner pasts,
F = 2, 10, 14. What changes: the even capacity cut is replaced by a per-line cut.

  fossil energy input falls by CUT (10, 20, 30, 50%)
  a line's output falls by CUT x (fossil share of the line's input)        [shares.py, EXIOBASE Z and x]
  capacity is per line: services, essentials goods, non-essential goods each keep 1.017 x their own
  wants x (1 - own fall). Spare capacity in one line cannot serve another.

Per cell it prints: the fall of each essentials line, of services and of non-essentials; the clearing rho of the
gated part (non-essential units above E) against the non-essentials capacity; 'none below 4.0'; or
'none: ungated part exceeds capacity'; the share admitting nothing above E; and, beside it, the even-cut
clearing rho at the SAME overall output loss, solved with the sweep's own solver.

Run:  python fuel_blockade.py --test
      python fuel_blockade.py > RESULTS_RAW.txt
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(SIM, "german-prime-sweep"))
sys.path.insert(0, HERE)

import german_prime_sweep as gps          # noqa: E402
import shares as S                        # noqa: E402

rsa = gps.rsa
C = gps.CAP_RATIO
CUTS = (0.10, 0.20, 0.30, 0.50)
FLOORS = (10.0, 2.0, 14.0)
SEEDS = gps.AGE_SEEDS
RHO0, RHO_HI = gps.RHO0, gps.RHO_HI
NONE_HI = "none below 4.0"
NONE_UNG = "none: ungated part exceeds capacity"

# even-cut figures printed in german-prime-sweep/RESULTS.md (F -> {shock: (rho at E 437.2, rho at E 462.3)})
RESULTS_MD = {2.0: {-0.10: (0.866, 0.853), -0.20: (0.511, 0.493), -0.30: (0.323, 0.304)},
              10.0: {-0.10: (0.309, 0.307), -0.20: (0.221, 0.217), -0.30: (0.158, 0.151)},
              14.0: {-0.10: (0.237, 0.236), -0.20: (0.172, 0.169), -0.30: (0.125, 0.120)}}


# ------------------------------------------------------------------ line falls
def line_falls(cut, e_index, which="direct", data=None):
    """Return dict of per-line output fall (fraction) and the three group falls."""
    sh = S.all_line_shares(which, data)
    h = dict(S.ESS_HOURS)
    h["housing structure"] = 31.0 if e_index == 0 else 61.0
    ess_h = sum(h.values())
    f_e = sum(h[k] * cut * sh[k] for k in h) / ess_h
    srv_h = sum(S.SERV_HOURS.values())
    f_s = sum(S.SERV_HOURS[k] * cut * sh[k] for k in S.SERV_HOURS) / srv_h
    f_n = cut * sh["non-essentials"]
    lines = {k: cut * sh[k] for k in list(h) + list(S.SERV_HOURS)}
    return dict(lines=lines, f_e=f_e, f_s=f_s, f_n=f_n, ess_hours=ess_h)


# ------------------------------------------------------------------ cell machinery
class Cell:
    def __init__(self, F, seed, E, pop):
        self.F, self.E = F, E
        self.c, self.w = pop
        self.ages = gps.draw_ages(len(self.c), seed)
        self.C0, self.D0 = gps.joiner_ledger(self.c, self.w, self.ages, "wants", "full", F)
        self.W = float(self.w.sum())
        self.req = self.w * gps.KAPPA_AFTER * 365.0
        s = gps.S_SHARE
        self.ung_units = self.w * (s + (1 - s) * np.minimum(self.req, E) / self.req)
        self.U = float(self.ung_units.sum())
        self.N = self.W - self.U
        self.Sw = s * self.W
        self.Ew = self.U - self.Sw

    def run(self, rho):
        return gps.run_year(self.c, self.w, self.ages, self.F, rho, self.C0, self.D0, self.E)

    def gated(self, rho):
        return float(self.run(rho)[1].sum()) - self.U

    def solve_gated(self, target):
        if self.gated(RHO_HI) <= target + 1e-9:
            return None, NONE_HI
        lo, hi = 0.0, RHO_HI
        while hi - lo > 1e-5:
            m = 0.5 * (lo + hi)
            if self.gated(m) <= target:
                lo = m
            else:
                hi = m
        return 0.5 * (lo + hi), ""

    def zero_above(self, rho):
        adm, _, _, req = self.run(rho)
        over = req > self.E + 1e-9
        above = adm - np.minimum(req, self.E)
        return float((above[over] <= 1e-6).mean()) if over.any() else 0.0


def evaluate(cell, f_s, f_e, f_n):
    """One cell, per-line and even-cut at the same overall loss."""
    W, U, N, Sw, Ew = cell.W, cell.U, cell.N, cell.Sw, cell.Ew
    L = (Sw * f_s + Ew * f_e + N * f_n) / W
    cap_s, cap_e, cap_n = C * Sw * (1 - f_s), C * Ew * (1 - f_e), C * N * (1 - f_n)
    short_s, short_e = Sw > cap_s + 1e-9, Ew > cap_e + 1e-9
    if short_s or short_e:
        rho_h, flag_h = None, NONE_UNG
    else:
        rho_h, flag_h = cell.solve_gated(cap_n)
    # even cut at the same overall loss: the sweep's own solver on aggregate capacity
    cap_even = C * W * (1 - L)
    rho_e, flag_e = gps.solve_rho(cell.c, cell.w, cell.ages, cell.F, cell.C0, cell.D0, cell.E, cap_even)
    flag_e = {"none, gate never binds below rho = 4.0": NONE_HI,
              "none, ungated part alone exceeds capacity": NONE_UNG}.get(flag_e, flag_e)
    return dict(L=L, rho_h=rho_h, flag_h=flag_h, rho_e=rho_e, flag_e=flag_e, short_s=short_s, short_e=short_e,
                zero_h=cell.zero_above(RHO0 if rho_h is None else rho_h),
                zero_e=cell.zero_above(RHO0 if rho_e is None else rho_e),
                cap_n=cap_n, N=N, U=U, W=W)


def fmt(rhos, flags):
    v = [r for r in rhos if r is not None]
    fl = sorted(set(f for f in flags if f))
    if not v:
        return " / ".join(fl)
    t = f"{np.mean(v):.3f} (min {min(v):.3f}, max {max(v):.3f}; {len(v)}/{len(rhos)} seeds)"
    return t + (" + " + " / ".join(fl) if fl else "")


# ------------------------------------------------------------------ self-tests
def _cell(F=10.0, n=20000, e=0):
    pop = rsa.build_population(F, n=n)
    return Cell(F, 11, gps.E_GER[e], pop)


def test_zero_cut():
    cl = _cell()
    fl = line_falls(0.0, 0)
    assert fl["f_e"] == fl["f_s"] == fl["f_n"] == 0.0 and all(v == 0 for v in fl["lines"].values())
    r = evaluate(cl, 0.0, 0.0, 0.0)
    assert r["L"] == 0.0 and r["rho_h"] is None and r["flag_h"] == NONE_HI and r["flag_e"] == NONE_HI, r
    print("[ok] 1. zero cut: no fall, no clearing rho under either arm (as the sweep's 0-shock row)")


def test_reproduces_sweep():
    c = rsa.build_population(10.0)
    cl = Cell(10.0, 11, gps.E_GER[0], c)
    r, _ = gps.solve_rho(cl.c, cl.w, cl.ages, 10.0, cl.C0, cl.D0, cl.E, C * cl.W * 0.8)
    assert r is not None and abs(r - 0.221) < 0.004, r
    print(f"[ok] 2. even cut -20%, F=10, E=437.2 reproduces RESULTS.md 0.221 (got {r:.3f})")


def test_algebra():
    """The declared identity: per-line target minus even-cut target = U(C f_u - 0.017)."""
    rng = np.random.default_rng(3)
    cl = _cell()
    for _ in range(50):
        f_s, f_e, f_n = rng.uniform(0, 0.05, 3)
        L = (cl.Sw * f_s + cl.Ew * f_e + cl.N * f_n) / cl.W
        t_h = C * cl.N * (1 - f_n)
        t_e = C * cl.W * (1 - L) - cl.U
        f_u = (cl.Sw * f_s + cl.Ew * f_e) / cl.U
        assert abs((t_h - t_e) - cl.U * (C * f_u - (C - 1))) < 1e-6 * cl.W
    print("[ok] 3. per-line target - even target = U x (C x f_u - 0.017), 50 random draws")


def test_flag_can_fire_and_not_fire():
    cl = _cell()
    assert evaluate(cl, 0.0, 0.05, 0.0)["flag_h"] == NONE_UNG
    assert evaluate(cl, 0.0, 0.005, 0.20)["flag_h"] != NONE_UNG
    assert evaluate(cl, 0.05, 0.0, 0.0)["flag_h"] == NONE_UNG
    print("[ok] 4. 'ungated part exceeds capacity' fires at essentials fall 5% or services fall 5%, not at 0.5%")


def test_monotone():
    cl = _cell()
    prev, prev_L = None, -1
    for f_n in (0.02, 0.05, 0.08, 0.12):
        r = evaluate(cl, 0.0, 0.0, f_n)
        assert r["L"] > prev_L
        if r["rho_h"] is not None and prev is not None:
            assert r["rho_h"] <= prev + 1e-9, (r["rho_h"], prev)
        if r["rho_h"] is not None:
            prev = r["rho_h"]
        prev_L = r["L"]
    assert prev is not None
    print("[ok] 5. deeper non-essentials fall: loss rises, clearing rho never rises")


def test_hours_and_shares():
    for j, tot in ((0, 523.0), (1, 553.0)):
        assert abs(line_falls(0.5, j)["ess_hours"] - tot) < 1e-9
    a, b = line_falls(0.1, 0), line_falls(0.5, 0)
    assert abs(b["f_e"] / a["f_e"] - 5.0) < 1e-9
    print("[ok] 6. essentials hours sum to 523 / 553 (the sweep's E before x 0.836); fall is linear in the cut")


def test_utilities_most_exposed():
    fl = line_falls(0.5, 0)["lines"]
    assert fl["utilities"] == max(fl[k] for k in S.ESS_HOURS), fl
    print(f"[ok] 7. utilities is the most fossil-exposed essentials line (fall {fl['utilities']:.2%} at a 50% cut)")


def run_tests():
    S.run_tests()
    print()
    for fn in (test_zero_cut, test_reproduces_sweep, test_algebra, test_flag_can_fire_and_not_fire, test_monotone,
               test_hours_and_shares, test_utilities_most_exposed):
        fn()
    print("\nAll self-tests passed.")


# ------------------------------------------------------------------ the run
def main():
    data = S.load()
    print(f"FUEL BLOCKADE AT THE GERMAN METHOD  N={rsa.N:,} pop seed={rsa.SEED} age seeds={SEEDS} RHO0={RHO0} C={C}")
    print("fossil share source: EXIOBASE 3.10.2 pxp 2022 Z and x, German producers; energy extension on disk is all zero")
    for which in ("direct", "up"):
        sh = S.all_line_shares(which, data)
        print(f"\nLINE FOSSIL SHARES ({'direct purchases' if which == 'direct' else 'direct + domestic upstream, SENSITIVITY'})")
        for k, v in sh.items():
            print(f"  {k:28s} {v:7.4f}")
    for which in ("direct", "up"):
        print("\n" + "=" * 120)
        print("PRIMARY: direct fossil purchases" if which == "direct" else "SENSITIVITY: direct + domestic upstream fossil purchases")
        for F in FLOORS:
            if which == "up" and F != 10.0:
                continue
            pop = rsa.build_population(F)
            for ei, E in enumerate(gps.E_GER):
                cells = [Cell(F, s, E, pop) for s in SEEDS]
                print("-" * 120)
                print(f"F={F:g}  E={E:.1f} h/yr  wants={cells[0].W:,.0f}  ungated demand U={cells[0].U:,.0f} "
                      f"({cells[0].U / cells[0].W:.1%})  gated demand N={cells[0].N:,.0f}  capacity base {C * cells[0].W:,.0f}")
                for cut in CUTS:
                    fl = line_falls(cut, ei, which, data)
                    res = [evaluate(cl, fl["f_s"], fl["f_e"], fl["f_n"]) for cl in cells]
                    L = res[0]["L"]
                    print(f"  CUT {cut:.0%}: falls  essentials goods {fl['f_e']:.3%} | services {fl['f_s']:.3%} | "
                          f"non-essentials {fl['f_n']:.3%} | OVERALL loss {L:.3%} "
                          f"(= {L * cells[0].W:,.0f} of {cells[0].W:,.0f} units)")
                    if F == 10.0 and ei == 0:
                        print("      essentials lines: " + " | ".join(f"{k} {v:.3%}" for k, v in fl["lines"].items() if k in S.ESS_HOURS))
                        print("      service lines:    " + " | ".join(f"{k} {v:.3%}" for k, v in fl["lines"].items() if k in S.SERV_HOURS))
                    print(f"      per-line  rho: {fmt([r['rho_h'] for r in res], [r['flag_h'] for r in res])}"
                          f" | admit>E zero {np.mean([r['zero_h'] for r in res]):.2%}"
                          f" | services short {res[0]['short_s']} essentials short {res[0]['short_e']}")
                    print(f"      even-cut  rho (same loss {L:.3%}): {fmt([r['rho_e'] for r in res], [r['flag_e'] for r in res])}"
                          f" | admit>E zero {np.mean([r['zero_e'] for r in res]):.2%}")
                    near = {-0.10: 0, -0.20: 0, -0.30: 0}
                    if which == "direct":
                        print("      RESULTS.md even-cut grid at this F, E:", {f"{k:+.0%}": v[ei] for k, v in RESULTS_MD[F].items()})
    print("\nDone.")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        main()
