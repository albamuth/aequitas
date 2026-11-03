#!/usr/bin/env python3
"""
stable_band_payers.py -- stable_band_methods.py at the every-payer peer ratios.

Request sr-20261029-re-run-stable-band-methods-py-the-kappa-tied (filed 2026-10-29).
Replaces the household-only 0.64 / 0.55 ratios of stable_band_methods.py. Inputs are
declared in PAYERS_DECLARED.md.

    h(peer)     = 1,380 x ratio           (ratio 0.836 / 0.858 / 0.873, Q6_PAYERS_RUN.txt)
    kappa(peer) = h / 365
    capacity    = 778,955 / (h / 100)     (US: 56,446 units at 13.80 h a unit)

Reuses stable_band_methods (edges, rho_sat, basket scaling). Run: python stable_band_payers.py [--test]
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
import stable_band_methods as sm                            # noqa: E402

US_H = sm.US_H
ENVELOPE = 778_955.0                       # debit-hours of the physical envelope (request)
PEERS = (("Germany, Japan", 0.836), ("France", 0.858), ("Sweden", 0.873))
FLOORS = sc.FLOORS_ASKED


def h_of(ratio):
    return US_H * ratio


def capacity_of(h):
    return ENVELOPE / (h / 100.0)


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def test_capacity_formula_reproduces_us_and_request():
    assert abs(capacity_of(US_H) - 56_446) < 1.0, capacity_of(US_H)
    for ratio, k_req in ((0.836, 1153.7), (0.858, 1184.0), (0.873, 1204.7)):
        assert abs(h_of(ratio) - k_req) < 0.1, (ratio, h_of(ratio), k_req)
    print("[ok] 778,955/(13.80) = 56,446 and the three kappas match the request")


def test_capacity_vs_wants_sign():
    """Germany/Japan above wants, France and Sweden below. Can fail if ratios change."""
    W = 66_407.0
    assert capacity_of(h_of(0.836)) > W > capacity_of(h_of(0.858)) > capacity_of(h_of(0.873))
    print("[ok] capacity: DE/JP above wants; FR, SE below")


def test_above_wants_censored_below_wants_numeric():
    w, x = sb.build_people(6000, seed=3)
    W = x.sum()
    k = sm.kappa_of(h_of(0.836))
    e, fl = sc.edge_one_day(w, x, 10.0, k, 1.017 * W)
    assert fl == "censored", (e, fl)
    e2, fl2 = sc.edge_one_day(w, x, 10.0, k, 0.974 * W)
    assert fl2 == "" and 0.05 < e2 < 3.9, (e2, fl2)
    print(f"[ok] capacity 1.017 x wants: censored; 0.974 x wants: edge {e2:.3f}")


def test_edge_rises_with_capacity_share():
    w, x = sb.build_people(6000, seed=3)
    W = x.sum()
    k = sm.kappa_of(h_of(0.858))
    a, _ = sc.edge_one_day(w, x, 10.0, k, 0.95 * W)
    b, _ = sc.edge_one_day(w, x, 10.0, k, 0.99 * W)
    assert b > a, (a, b)
    print(f"[ok] more capacity, higher edge: {a:.3f} (95%) < {b:.3f} (99%)")


def test_us_control_reproduces_published_edges():
    sm.test_us_control_reproduces_published_edges()


def test_breakeven_arithmetic():
    assert abs(h_of(0.873) / (365 * 10) - 0.3301) < 5e-4
    assert abs(h_of(0.858) / (365 * 2) - 1.6220) < 5e-4
    print("[ok] break-even arithmetic")


def run_tests():
    for fn in (test_capacity_formula_reproduces_us_and_request,
               test_capacity_vs_wants_sign,
               test_above_wants_censored_below_wants_numeric,
               test_edge_rises_with_capacity_share,
               test_us_control_reproduces_published_edges,
               test_breakeven_arithmetic):
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
    rows = [("US (control)", 1.0)] + list(PEERS)
    for name, ratio in rows:
        h = h_of(ratio)
        R = capacity_of(h)
        kap = sm.kappa_of(h)
        nar, bro = sm.baskets(h)
        print(f"\n===== {name}: ratio {ratio:.3f}, h {h:.1f} h/yr, kappa {kap:.4f}, "
              f"capacity {R:,.0f} ({R/W:.3f} x wants) =====")
        print(f"narrow basket {nar[0]:.0f}-{nar[1]:.0f} h, broad {bro[0]:.0f}-{bro[1]:.0f} h "
              f"(assumption A: US baskets x {ratio:.3f})")
        for F in FLOORS:
            od, fo = sc.edge_one_day(w, x, F, kap, R)
            cum = [sc.edge_cumulative(w, x, ages[s], F, kap, R, past_rate=kap * 365.0)
                   for s in sc.AGE_SEEDS]
            cv = np.array([c[0] for c in cum]); cf = sorted({c[1] for c in cum})
            top = sc.one_day(w, x, F, sc.RHO_HI, kap)
            be = h / (365.0 * F)
            ln_t, ln_b = sm.lower_edge(nar[1], F), sm.lower_edge(bro[1], F)
            ln_t0, ln_b0 = sm.lower_edge(nar[0], F), sm.lower_edge(bro[0], F)
            s1, sf1 = sm.sat_one_day(w, x, F, kap)
            sv = [sm.sat_cum(w, x, ages[s], F, kap) for s in sc.AGE_SEEDS]
            svv = np.array([v[0] for v in sv]); svf = sorted({v[1] for v in sv})
            print(f"\nF={F:g}  break-even {be:.4f}  admitted at rho=4.0: {top:,.0f} (capacity {R:,.0f})")
            print(f"  upper edge one-day: {sc.fmt(od, fo)}   cumulative: mean {cv.mean():.3f} "
                  f"sd {cv.std():.4f} flags {cf}")
            print(f"  rho_sat one-day: {sc.fmt(s1, sf1)}   cumulative: mean {svv.mean():.3f} "
                  f"sd {svv.std():.4f} flags {svf}")
            print(f"  lower edge narrow {ln_t0:.3f}-{ln_t:.3f}  broad {ln_b0:.3f}-{ln_b:.3f}")
            print(f"  band narrow: {sm.open_state(ln_t, od, fo)} | broad: {sm.open_state(ln_b, od, fo)}")


if __name__ == "__main__":
    main()
