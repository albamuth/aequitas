#!/usr/bin/env python3
"""
german_arm2.py -- second arm of the German prime-rate sweep.
Request sr-20261110-second-arm-of-sr-20261109-prime-rate-sweep-a.

Changes TWO inputs against german_prime_sweep.py (arm 1), nothing else:
  (1) demand level: Germany's middle fifth, 1,048 h per person per year (MIDDLE_FIFTH.md), per person all ages,
      not per median adult. Services (344.4 h = 412 x 0.836, the arm-1 service hours) come off before D is built.
  (2) output basis: capacity base = 100% of wants (declared), not 101.7%.
Arm 1 is re-run inside this script with its own inputs, so each rho is printed beside arm 1's at the same
F, E and shock, with the ratio.

Run:  python german_arm2.py [--test]
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import german_prime_sweep as g                                       # noqa: E402  (arm 1)
import rho_sweep_anchor as rsa                                       # noqa: E402
from stable_band_cumulative import draw_ages                         # noqa: E402

MID_FIFTH_H = 1048.0                                   # h/person/yr, Germany middle fifth, EXIOBASE 2022
SERVICE_H_GER = g.SERVICE_TOTAL * g.GERMAN             # 344.4 h
KAPPA2_BEFORE = MID_FIFTH_H / 365.0
KAPPA2_AFTER = (MID_FIFTH_H - SERVICE_H_GER) / 365.0   # h/day per unit
S2 = SERVICE_H_GER / MID_FIFTH_H
CAP2 = 1.000

ARM1 = dict(name="arm1", kappa=g.KAPPA_AFTER, s=g.S_SHARE, cap_ratio=g.CAP_RATIO)
ARM2 = dict(name="arm2", kappa=KAPPA2_AFTER, s=S2, cap_ratio=CAP2)


def cell(arm, F, age_seed, shock, E, pop):
    c, w = pop
    ages = draw_ages(len(c), age_seed)
    kappa, s = arm["kappa"], arm["s"]
    C0 = c * 365.0 * ages
    D0 = w * kappa * 365.0 * ages
    cap_full = arm["cap_ratio"] * w.sum()
    cap = cap_full * (1.0 + shock)
    rho_s, flag = g.solve_rho(c, w, ages, F, C0, D0, E, cap, s=s, kappa=kappa)
    rho_year = g.RHO0 if rho_s is None else rho_s
    adm, u, D1, req = g.run_year(c, w, ages, F, rho_year, C0, D0, E, s=s, kappa=kappa)
    over = req > E + 1e-9
    above = adm - np.minimum(req, E)
    zero_above = float((above[over] <= 1e-6).mean()) if over.any() else 0.0
    C1 = C0 + c * 365.0
    _, u2, _, _ = g.run_year(c, w, ages + 1.0, F, g.RHO0, C1, D1, E, s=s, kappa=kappa)
    _, ub, _, _ = g.run_year(c, w, ages, F, g.RHO0, C0, D0, E, s=s, kappa=kappa)
    f0 = g.units(g.run_year(c, w, ages, F, 0.0, C0, D0, E, s=s, kappa=kappa)[1])     # ungated floor
    return dict(rho=rho_s, flag=flag, units=g.units(u), cap=cap, cap_full=cap_full, wants=float(w.sum()),
                zero_above=zero_above, band=g.by_band(w, u, ages), bandw=g.band_wants(w, ages),
                year2=g.units(u2), base=g.units(ub), ungated=f0)


# ------------------------------------------------------------------ self-tests (each can fail)
def _small(n=20000):
    c, w = rsa.build_population(10.0, n=n)
    return c, w, draw_ages(n, 11)


def test_inputs():
    assert abs(SERVICE_H_GER - 344.4) < 0.05, SERVICE_H_GER
    assert abs(KAPPA2_AFTER * 365 - (1048 - 412 * 0.836)) < 1e-9
    assert abs(S2 - 412 * 0.836 / 1048) < 1e-9 and CAP2 == 1.0
    print(f"[ok] 1. inputs: kappa {KAPPA2_BEFORE:.4f} -> {KAPPA2_AFTER:.4f} h/day ({KAPPA2_AFTER * 365:.1f} h/yr), s {S2:.4f}")


def test_arm1_reproduced():
    """Level check against arm 1's published figure: F=10, -20%, E=437.2 -> 0.221."""
    pop = rsa.build_population(10.0)
    x = cell(ARM1, 10.0, 11, -0.20, g.E_GER[0], pop)
    assert x["rho"] is not None and abs(x["rho"] - 0.221) < 0.005, x["rho"]
    print(f"[ok] 2. arm 1 reproduced inside this script: rho {x['rho']:.4f} (published 0.221)")


def test_rho_scales_with_kappa():
    """With E=0 and s=0 the gate sees only rho/kappa, so clearing rho must scale exactly with kappa."""
    c, w, ages = _small()
    out = []
    for kap in (g.KAPPA_AFTER, KAPPA2_AFTER):
        C0, D0 = c * 365 * ages, w * kap * 365 * ages
        r, _ = g.solve_rho(c, w, ages, 10.0, C0, D0, 0.0, 0.8 * g.CAP_RATIO * w.sum(), s=0.0, kappa=kap)
        out.append(r)
    ratio = out[1] / out[0]
    assert abs(ratio - KAPPA2_AFTER / g.KAPPA_AFTER) < 0.002, (ratio, KAPPA2_AFTER / g.KAPPA_AFTER)
    print(f"[ok] 3. E=0, s=0: rho ratio {ratio:.4f} == kappa ratio {KAPPA2_AFTER / g.KAPPA_AFTER:.4f}")


def test_ungated_flag_fires():
    c, w, ages = _small()
    kap, s = KAPPA2_AFTER, S2
    C0, D0 = c * 365 * ages, w * kap * 365 * ages
    r, flag = g.solve_rho(c, w, ages, 10.0, C0, D0, g.E_GER[0], 0.5 * w.sum(), s=s, kappa=kap)
    assert r is None and "ungated" in flag, (r, flag)
    r2, flag2 = g.solve_rho(c, w, ages, 10.0, C0, D0, g.E_GER[0], 1.0 * w.sum(), s=s, kappa=kap)
    assert r2 is None and "never binds" in flag2, (r2, flag2)
    r3, _ = g.solve_rho(c, w, ages, 10.0, C0, D0, g.E_GER[0], 0.85 * w.sum(), s=s, kappa=kap)
    assert r3 is not None and 0 < r3 < g.RHO_HI, r3
    print(f"[ok] 4. both 'none' flags fire and a mid-capacity cell clears (rho {r3:.3f})")


def test_full_demand_admitted_at_high_rho():
    c, w, ages = _small()
    kap = KAPPA2_AFTER
    C0, D0 = c * 365 * ages, w * kap * 365 * ages
    _, u, _, _ = g.run_year(c, w, ages, 10.0, g.RHO_HI, C0, D0, g.E_GER[0], s=S2, kappa=kap)
    assert abs(g.units(u) - w.sum()) < 1e-6 * w.sum(), (g.units(u), w.sum())
    print("[ok] 5. at rho 4.0 arm 2 admits all of wants (capacity base 1.000 equals demand)")


def test_monotone_and_gate():
    c, w, ages = _small()
    kap = KAPPA2_AFTER
    C0, D0 = c * 365 * ages, w * kap * 365 * ages
    us = [g.units(g.run_year(c, w, ages, 10.0, r, C0, D0, g.E_GER[1], s=S2, kappa=kap)[1]) for r in np.linspace(0, 1.5, 16)]
    assert all(b >= a - 1e-9 for a, b in zip(us, us[1:]))
    adm, _, _, req = g.run_year(c, w, ages, 10.0, 0.2, C0, D0, g.E_GER[1], s=S2, kappa=kap)
    ess = np.minimum(req, g.E_GER[1])
    room = np.maximum(0.2 * (C0 + c * 365) - (D0 + ess), 0.0)
    assert np.all(adm - ess <= room + 1e-6)
    print("[ok] 6. arm 2 admitted units monotone in rho; nobody above E beyond rho*(C+P) - D")


def run_tests():
    for fn in (test_inputs, test_arm1_reproduced, test_rho_scales_with_kappa, test_ungated_flag_fires,
               test_full_demand_admitted_at_high_rho, test_monotone_and_gate):
        fn()
    print("\nAll self-tests passed.")


# ------------------------------------------------------------------ the run
def fmt(cells):
    v = [x["rho"] for x in cells if x["rho"] is not None]
    if not v:
        return sorted(set(x["flag"] for x in cells))[0] if len(set(x["flag"] for x in cells)) == 1 else "mixed flags"
    return f"{np.mean(v):.3f}" + ("" if len(v) == len(cells) else f" ({len(v)}/{len(cells)} seeds)")


def main():
    print(f"GERMAN PRIME-RATE SWEEP, ARM 2   N={rsa.N:,} pop seed={rsa.SEED} age seeds={g.AGE_SEEDS} RHO0={g.RHO0}")
    print(f"ARM 1 kappa before {g.KAPPA_BEFORE:.4f} h/day ({g.KAPPA_BEFORE * 365:.1f} h/yr)  after {g.KAPPA_AFTER:.4f} ({g.KAPPA_AFTER * 365:.1f} h/yr)  s={g.S_SHARE:.4f}  capacity base {g.CAP_RATIO}")
    print(f"ARM 2 kappa before {KAPPA2_BEFORE:.4f} h/day ({MID_FIFTH_H:.1f} h/yr)  after {KAPPA2_AFTER:.4f} ({KAPPA2_AFTER * 365:.1f} h/yr)  s={S2:.4f}  capacity base {CAP2}")
    print(f"services removed: {SERVICE_H_GER:.1f} h (412 x {g.GERMAN}); E = {g.E_GER[0]:.1f} and {g.E_GER[1]:.1f} h/yr (unchanged)\n")
    for F in (10.0, 2.0, 14.0):
        pop = rsa.build_population(F)
        for E in g.E_GER:
            print("-" * 118)
            print(f"F={F:g}  E={E:.1f}  wants={pop[1].sum():,.0f}  cap arm1={g.CAP_RATIO * pop[1].sum():,.0f} arm2={CAP2 * pop[1].sum():,.0f}")
            for shock in g.SHOCKS:
                c1 = [cell(ARM1, F, s_, shock, E, pop) for s_ in g.AGE_SEEDS]
                c2 = [cell(ARM2, F, s_, shock, E, pop) for s_ in g.AGE_SEEDS]
                r1 = [x["rho"] for x in c1]
                r2 = [x["rho"] for x in c2]
                ratio = ""
                if all(r is not None for r in r1 + r2):
                    ratio = f" | ratio arm2/arm1 = {np.mean(r2) / np.mean(r1):.3f}"
                m = lambda cs, f: np.mean([f(x) for x in cs])        # noqa: E731
                print(f"  shock {shock:+.0%}: ARM1 rho {fmt(c1)} || ARM2 rho {fmt(c2)}{ratio}")
                print(f"      arm2: cap {c2[0]['cap']:,.0f} units {m(c2, lambda x: x['units']):,.0f} ({m(c2, lambda x: x['units'] / x['cap']):.3f} x cap)"
                      f" | ungated {m(c2, lambda x: x['ungated']):,.0f} ({m(c2, lambda x: x['ungated'] / x['cap']):.3f} x cap)"
                      f" | admit>E zero {m(c2, lambda x: x['zero_above']):.2%} (arm1 {m(c1, lambda x: x['zero_above']):.2%})"
                      f" | yr2@{g.RHO0} {m(c2, lambda x: x['year2']):,.0f} ({m(c2, lambda x: x['year2'] / x['cap_full']):.3f} x full cap; unshocked yr {m(c2, lambda x: x['base'] / x['cap_full']):.3f})")
                if F == 10.0 and E == g.E_GER[0]:
                    bnd = np.mean([x["band"] for x in c2], 0)
                    bw = np.mean([x["bandw"] for x in c2], 0)
                    print("      arm2 units by age band", [f"{lo:g}-{hi:g}" for lo, hi in g.BAND_EDGES], ":",
                          " ".join(f"{v:,.0f}" for v in bnd), "| share of band wants:", " ".join(f"{v:.3f}" for v in bnd / bw))
    # ungated-line crossing, analytic from the F=10 cell
    pop = rsa.build_population(10.0)
    for E in g.E_GER:
        x = cell(ARM2, 10.0, 11, 0.0, E, pop)
        y = cell(ARM1, 10.0, 11, 0.0, E, pop)
        for nm, z in (("arm1", y), ("arm2", x)):
            line = z["ungated"] / z["wants"]
            cr = line / (ARM1["cap_ratio"] if nm == "arm1" else CAP2) - 1.0
            print(f"ungated line {nm} E={E:.1f}: {z['ungated']:,.0f} units = {line:.3f} of wants; ungated alone exceeds capacity at shock below {cr:+.1%}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    elif "--raw" in sys.argv:                      # write the transcript to RESULTS_ARM2_RAW.txt, next to this file
        with open(os.path.join(HERE, "RESULTS_ARM2_RAW.txt"), "w", encoding="utf-8") as fh:
            sys.stdout = fh
            main()
        sys.stdout = sys.__stdout__
    else:
        main()
