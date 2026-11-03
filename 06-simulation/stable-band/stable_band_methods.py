#!/usr/bin/env python3
"""
stable_band_methods.py -- stable_band_kappa.py at the German/Japanese and Spanish methods.

Request sr-20261028-re-run-stable-band-kappa-py-at-the-german-ja (filed 2026-10-28).
Extends stable_band_kappa.py. Inputs are declared in METHODS_DECLARED.md.

    kappa(method) = yearly median demand / 365   (883 / 759 h/yr, 1,380 for the US control)
    R_max(method) = 88,196 / 102,629 real units  (US control: 0.85 x wants = 56,446)

Because wants (66,407) < R_max for both efficient methods, the test
"admitted <= R_max" cannot fail, so the upper edge does not exist. This script
reports that, and ALSO measures rho_sat: the lowest rho at which >= 99.9% of
wants are admitted (the gate stops binding on people). rho_sat can fail.

Run:  python stable_band_methods.py [--test]
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import stable_band as sb                                    # noqa: E402
import stable_band_cumulative as sc                         # noqa: E402

FLOORS = sc.FLOORS_ASKED
SAT = 0.999                                                 # share of wants "satisfied"
US_H = 1380.0
# name -> (yearly median demand h, capacity real units or None = 0.85 x wants)
METHODS = {
    "US (control)": (US_H, None),
    "German/Japanese": (883.0, 88_196.0),
    "Spanish": (759.0, 102_629.0),
}
NARROW = (516.0, 655.0)
BROAD = (826.0, 965.0)


def kappa_of(h_yr):
    return h_yr / 365.0


def baskets(h_yr):
    """ASSUMPTION A: scale the US essentials baskets by the method ratio."""
    r = h_yr / US_H
    return (NARROW[0] * r, NARROW[1] * r), (BROAD[0] * r, BROAD[1] * r)


def lower_edge(E, F, rho_unit=1.0):
    return E / (365.0 * F)


def sat_one_day(w, x, F, kappa):
    """Lowest rho at which one-day admitted >= SAT x wants. (value, flag)."""
    tgt = SAT * x.sum()
    e, fl = sc.bisect_edge(lambda r: sc.one_day(w, x, F, r, kappa) < tgt)
    return e, fl


def sat_cum(w, x, ages, F, kappa):
    """Lowest rho at which EVERY yearly period 1..M admits >= SAT x wants.
    The path is non-increasing, so the last period decides."""
    tgt = SAT * x.sum()
    past = kappa * 365.0                              # past debit = flow, as RESULTS_KAPPA
    e, fl = sc.bisect_edge(
        lambda r: sc.run_path(w, x, ages, F, r, kappa, sc.M_PRIMARY, past_rate=past)[-1] < tgt)
    return e, fl


def open_state(lower_top, upper, flag):
    if flag == "censored":
        return "open (no upper edge)"
    return "open" if lower_top < upper else "CLOSED"


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def _small(n=6000, seed=3):
    w, x = sb.build_people(n, seed=seed)
    return w, x, 0.85 * x.sum()


def test_us_control_reproduces_published_edges():
    w, x = sb.build_people()
    R = 0.85 * x.sum()
    for F, pub in ((2.0, 1.017), (10.0, 0.330), (14.0, 0.253)):
        e, fl = sc.edge_one_day(w, x, F, kappa_of(US_H), R)
        assert fl == "" and abs(e - pub) <= 0.01, (F, e, pub)
    print("[ok] US control at kappa 1,380 reproduces 1.017 / 0.330 / 0.253")


def test_capacity_above_wants_cannot_bind():
    """With R above total wants, admitted <= R at the top of the grid."""
    w, x, _ = _small()
    for h, R in ((883.0, 1.33 * x.sum()), (759.0, 1.55 * x.sum())):
        for F in FLOORS:
            top = sc.one_day(w, x, F, sc.RHO_HI, kappa_of(h))
            assert top <= x.sum() * (1 + 1e-9) < R, (h, F, top, R)
        e, fl = sc.edge_one_day(w, x, 10.0, kappa_of(h), R)
        assert fl == "censored", (h, e, fl)
    print("[ok] R above wants: admitted <= wants < R, edge censored (no upper edge)")


def test_capacity_below_wants_can_bind():
    """Same code, R below wants (0.85): the edge is a real number. Proves the
    'censored' result above comes from capacity, not from the code."""
    w, x, R = _small()
    e, fl = sc.edge_one_day(w, x, 10.0, kappa_of(883.0), R)
    assert fl == "" and 0.05 < e < 3.9, (e, fl)
    print(f"[ok] at R = 0.85 x wants the German-kappa edge is a number ({e:.3f})")


def test_sat_scales_with_kappa():
    w, x, _ = _small()
    a, fa = sat_one_day(w, x, 10.0, kappa_of(US_H))
    b, fb = sat_one_day(w, x, 10.0, kappa_of(883.0))
    assert fa == fb == "" and abs(b - a * 883.0 / US_H) < 0.01 * a + 2e-3, (a, b)
    print(f"[ok] rho_sat scales with kappa: {a:.3f} x 0.640 = {a*883/US_H:.3f} vs {b:.3f}")


def test_sat_can_fail_the_other_way():
    """At rho 0.01 the gate must hold people back; at rho 4 it must not."""
    w, x, _ = _small()
    k = kappa_of(883.0)
    assert sc.one_day(w, x, 10.0, 0.01, k) < SAT * x.sum()
    assert sc.one_day(w, x, 10.0, 4.0, k) >= SAT * x.sum()
    print("[ok] the satiation test fails at rho 0.01 and passes at rho 4")


def test_baskets_scale():
    n, b = baskets(883.0)
    assert abs(b[1] - 965 * 883 / 1380) < 1e-9 and abs(n[0] - 516 * 883 / 1380) < 1e-9
    print(f"[ok] broad basket German = {b[0]:.0f}-{b[1]:.0f} h")


def run_tests():
    for fn in (test_us_control_reproduces_published_edges,
               test_capacity_above_wants_cannot_bind,
               test_capacity_below_wants_can_bind,
               test_sat_scales_with_kappa,
               test_sat_can_fail_the_other_way,
               test_baskets_scale):
        fn()
    print("\nAll self-tests passed.")


# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    if ap.parse_args().test:
        run_tests()
        return

    w, x = sb.build_people()
    n, W = len(w), x.sum()
    print(f"N={n:,} seed={sb.RNG_SEED} total wants {W:,.0f} real units, age seeds {sc.AGE_SEEDS}, M={sc.M_PRIMARY}")
    ages = {s: sc.draw_ages(n, s) for s in sc.AGE_SEEDS}
    for name, (h, Rm) in METHODS.items():
        R = 0.85 * W if Rm is None else Rm
        kap = kappa_of(h)
        nar, bro = baskets(h)
        print(f"\n===== {name}: kappa {kap:.4f} ({h:.0f} h/yr), R_max {R:,.0f} "
              f"({R/W:.3f} x wants) =====")
        print(f"narrow basket {nar[0]:.0f}-{nar[1]:.0f} h, broad {bro[0]:.0f}-{bro[1]:.0f} h "
              f"(assumption A: US baskets x {h/US_H:.4f})")
        for F in FLOORS:
            od, fo = sc.edge_one_day(w, x, F, kap, R)
            cum = [sc.edge_cumulative(w, x, ages[s], F, kap, R, past_rate=kap * 365.0)
                   for s in sc.AGE_SEEDS]
            cv = np.array([c[0] for c in cum]); cf = sorted({c[1] for c in cum})
            top = sc.one_day(w, x, F, sc.RHO_HI, kap)
            be = h / (365.0 * F)
            ln_t, ln_b = lower_edge(nar[1], F), lower_edge(bro[1], F)
            ln_t0, ln_b0 = lower_edge(nar[0], F), lower_edge(bro[0], F)
            s1, sf1 = sat_one_day(w, x, F, kap)
            sv = [sat_cum(w, x, ages[s], F, kap) for s in sc.AGE_SEEDS]
            svv = np.array([v[0] for v in sv]); svf = sorted({v[1] for v in sv})
            print(f"\nF={F:g}  break-even {be:.4f}  admitted at rho=4.0: {top:,.0f} (R_max {R:,.0f})")
            print(f"  upper edge one-day: {sc.fmt(od, fo)}   cumulative: mean {cv.mean():.3f} "
                  f"sd {cv.std():.4f} flags {cf}")
            print(f"  rho_sat one-day: {sc.fmt(s1, sf1)}   cumulative: mean {svv.mean():.3f} "
                  f"sd {svv.std():.4f} min {svv.min():.3f} max {svv.max():.3f} flags {svf}"
                  f"   cum/one-day {svv.mean()/s1:.3f}")
            print(f"  lower edge narrow {ln_t0:.3f}-{ln_t:.3f}  broad {ln_b0:.3f}-{ln_b:.3f}")
            print(f"  band narrow: {open_state(ln_t, od, fo)} | broad: {open_state(ln_b, od, fo)}")
            if Rm is not None:
                print(f"  (if capacity were 0.85 x wants = {0.85*W:,.0f}, one-day edge would be "
                      f"{sc.edge_one_day(w, x, F, kap, 0.85*W)[0]:.3f})")
        print("\n  share of people held below wants, one-day, F=10:")
        for rho in (0.1, 0.25, 0.5, 1.0, 1.2):
            _, fr = sb.admitted_total(w, x, 10.0, rho, kap)
            print(f"    rho {rho:<4g} held back {fr:6.1%}")


if __name__ == "__main__":
    main()
