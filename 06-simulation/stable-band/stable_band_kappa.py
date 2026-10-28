#!/usr/bin/env python3
"""
stable_band_kappa.py -- both rho* edges with kappa tied to the measured anchor.

Request sr-20261026-re-run-stable-band-py-with-kappa-tied-to-the
(filed 2026-10-26). Extends stable_band.py and stable_band_cumulative.py.

THE CHANGE
    Before: kappa = median daily credit at F = 10 = 13.797 debit-h per
            lifestyle-unit per day, so a year of demand was 5,037 h.
    Now:    kappa = 1,380 / 365 = 3.7808, so a year of demand is the measured
            1,380 h/yr (Foundations 3.5).

HELD FIXED (declared in KAPPA_DECLARED.md)
    population      60,000 people, seed 7
    R_max           0.85 * sum(wants) real units -- the SAME number as before
                    (the old R_max = B / kappa_old; here it is kept, not re-derived)
    ages, joining, M, past credit (floor only), past debit 1,380 h/yr:
                    exactly as in stable_band_cumulative.py

Run:  python stable_band_kappa.py [--test]
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

KAPPA_ANCHOR = sb.MEDIAN_LIFESTYLE_H_YR / 365.0             # 3.7808
FLOORS = sc.FLOORS_ASKED


def setup(n=sb.N, seed=sb.RNG_SEED):
    w, x = sb.build_people(n, seed=seed)
    kappa_old, B = sb.calibrate(w, x)
    R = B / kappa_old                                       # capacity, real units
    return w, x, kappa_old, R


def both_edges(w, x, R, F, kappa, seeds=sc.AGE_SEEDS):
    od, fo = sc.edge_one_day(w, x, F, kappa, R)
    cum = [sc.edge_cumulative(w, x, sc.draw_ages(len(w), s), F, kappa, R)
           for s in seeds]
    return od, fo, np.array([c[0] for c in cum]), sorted({c[1] for c in cum})


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def _small(n=6000, seed=3):
    return setup(n, seed)


def test_kappa_is_the_anchor_not_the_median_credit():
    w, x, kappa_old, _ = _small()
    assert abs(KAPPA_ANCHOR * 365.0 - 1380.0) < 1e-9
    assert abs(kappa_old - 13.8) < 0.5, kappa_old          # old value is what we replace
    assert KAPPA_ANCHOR < kappa_old / 3.0
    print(f"[ok] kappa = {KAPPA_ANCHOR:.4f} (year = 1,380 h), old = {kappa_old:.3f}")


def test_capacity_is_the_old_capacity():
    w, x, _, R = _small()
    assert abs(R - sb.CAP * x.sum()) < 1e-6 * R
    print(f"[ok] R_max = {R:,.0f} = 0.85 x wants ({x.sum():,.0f}), unchanged")


def test_one_day_edge_scales_with_kappa():
    """Requests scale with kappa, capacity is in real units, so the edge scales
    exactly with kappa. If the script secretly re-derived R_max it would not."""
    w, x, kappa_old, R = _small()
    for F in (2.0, 10.0, 14.0):
        old, _ = sc.edge_one_day(w, x, F, kappa_old, R)
        new, _ = sc.edge_one_day(w, x, F, KAPPA_ANCHOR, R)
        assert abs(new - old * KAPPA_ANCHOR / kappa_old) < 0.01 * max(old, 1), (F, old, new)
    print("[ok] one-day edge at the anchor = old edge x kappa ratio")


def test_capacity_binds_at_anchor():
    w, x, _, R = _small()
    hi = sc.one_day(w, x, 10.0, 4.0, KAPPA_ANCHOR)
    lo = sc.one_day(w, x, 10.0, 0.02, KAPPA_ANCHOR)
    assert lo <= R < hi, (lo, R, hi)
    print(f"[ok] capacity can bind: rho 0.02 admits {lo:,.0f} <= R {R:,.0f} < rho 4 admits {hi:,.0f}")


def test_cumulative_path_runs_through_kernel_and_falls():
    w, x, _, _ = _small()
    p = sc.run_path(w, x, sc.draw_ages(len(w), 11), 10.0, 0.5, KAPPA_ANCHOR, 30)
    assert np.all(np.diff(p) <= 1e-6 * p.max())
    assert p[0] > p[-1]
    print(f"[ok] admitted path non-increasing: {p[0]:,.0f} -> {p[-1]:,.0f}")


def test_a_wrong_past_debit_changes_the_cumulative_edge():
    """If past debit did nothing, this would fail."""
    w, x, _, R = _small()
    ag = sc.draw_ages(len(w), 11)
    a, _ = sc.edge_cumulative(w, x, ag, 10.0, KAPPA_ANCHOR, R, M=20)
    b, _ = sc.edge_cumulative(w, x, ag, 10.0, KAPPA_ANCHOR, R, M=20, past_rate=5037.0)
    assert abs(a - b) > 0.01, (a, b)
    print(f"[ok] past debit matters: edge {a:.3f} (1,380) vs {b:.3f} (5,037)")


def run_tests():
    for fn in (test_kappa_is_the_anchor_not_the_median_credit,
               test_capacity_is_the_old_capacity,
               test_one_day_edge_scales_with_kappa,
               test_capacity_binds_at_anchor,
               test_cumulative_path_runs_through_kernel_and_falls,
               test_a_wrong_past_debit_changes_the_cumulative_edge):
        fn()
    print("\nAll self-tests passed.")


# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return

    w, x, kappa_old, R = setup()
    n = len(w)
    print(f"N={n:,} seed={sb.RNG_SEED} kappa={KAPPA_ANCHOR:.4f} (old {kappa_old:.3f}) "
          f"R_max={R:,.0f} wants_total={x.sum():,.0f} M={sc.M_PRIMARY}")
    print(f"kappa*365 = {KAPPA_ANCHOR*365:.1f} h/yr; old kappa*365 = {kappa_old*365:,.0f} h/yr")
    print()

    print("== 1. both edges at kappa = 1,380/365, beside break-even 3.78/F ==")
    res = {}
    for F in FLOORS:
        od, fo, cv, cf = both_edges(w, x, R, F, KAPPA_ANCHOR)
        old_od, _ = sc.edge_one_day(w, x, F, kappa_old, R)
        be = KAPPA_ANCHOR / F
        res[F] = (od, fo, cv, cf, old_od)
        print(f"F={F:>4g}  break-even {be:.3f} | one-day {sc.fmt(od, fo)} "
              f"(old kappa {old_od:.3f}, scaled {old_od*KAPPA_ANCHOR/kappa_old:.3f}) | "
              f"cumulative rho*_L mean {cv.mean():.3f} sd {cv.std():.4f} "
              f"min {cv.min():.3f} max {cv.max():.3f} flags {cf} | "
              f"cum/one-day {cv.mean()/od:.3f} | one-day/break-even {od/be:.3f}, "
              f"cum/break-even {cv.mean()/be:.3f}")
    print()

    print("== 2. capacity: does it still bind at kappa = 1,380? ==")
    print(f"unconstrained wants {x.sum():,.0f} real units vs R_max {R:,.0f} "
          f"({R/x.sum():.0%})")
    for F in FLOORS:
        for rho in (0.05, 0.25, 1.0, 4.0):
            adm = sc.one_day(w, x, F, rho, KAPPA_ANCHOR)
            print(f"F={F:>4g} rho={rho:<5g} one-day admitted {adm:>9,.0f}  "
                  f"{'<= R_max (rations)' if adm <= R else '> R_max (capacity binds, gate does not)'}")
    print()

    print("== 3. admitted path at the one-day edge (age seed 11) ==")
    ag = sc.draw_ages(n, sc.AGE_SEEDS[0])
    for F in FLOORS:
        od = res[F][0]
        path = sc.run_path(w, x, ag, F, od, KAPPA_ANCHOR, sc.M_PRIMARY)
        lvl = sc.one_day(w, x, F, od, KAPPA_ANCHOR)
        print(f"F={F:>4g} rho={od:.3f} one-day {lvl:,.0f} | t=1 {path[0]:,.0f} "
              f"t=10 {path[9]:,.0f} t=50 {path[49]:,.0f} t=100 {path[99]:,.0f} "
              f"| return(M=100) {sc.return_period(path, lvl)}")
    print()

    print("== 4. sensitivity: cumulative rho*_L, age seed 11 ==")
    variants = [("declared (past debit 1,380)", dict()),
                ("past debit 5,037 (old model flow)", dict(past_rate=5037.0)),
                ("past work credited", dict(past_work=True)),
                ("all join at age 40", dict(ages=np.full(n, 40.0)))]
    for name, kw in variants:
        kw = dict(kw)
        ages = kw.pop("ages", ag)
        row = [sc.fmt(*sc.edge_cumulative(w, x, ages, F, KAPPA_ANCHOR, R, **kw))
               for F in FLOORS]
        print(f"{name:<38} F=2 {row[0]:>9}  F=10 {row[1]:>9}  F=14 {row[2]:>9}")


if __name__ == "__main__":
    main()
