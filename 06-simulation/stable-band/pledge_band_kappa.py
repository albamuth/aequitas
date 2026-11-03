#!/usr/bin/env python3
"""
pledge_band_kappa.py -- pledge_band.py's pledge term on the kappa-tied ledger.

Request sr-20261028-run-pledge-band-py-s-pledge-term-on-the-kapp (filed 2026-10-28).
Extends stable_band_kappa.py. Declared in PLEDGE_KAPPA_DECLARED.md.

pledge_band.py does not run a kernel: it divides rho*(F) by (1 + p). This script
puts P into the kernel (`Kernel.P`, the gate's own term) and re-finds the edge,
so the rule is tested instead of assumed.

Three arms for the cumulative ledger, plus the one-day row:
    A  P = p * C at every period          (the rule should be exact)
    B  P = p * C_at_joining, never topped up
    C  concentrated: backed people get P = C_at_joining, sized so sum P = p sum C

Run:  python pledge_band_kappa.py [--test]
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
import stable_band_kappa as sk                              # noqa: E402
from gate import Kernel, Dials, Conformance, ConformanceError  # noqa: E402

KAPPA = sk.KAPPA_ANCHOR
FLOORS = (2.0, 10.0, 14.0)
PS = (0.0, 0.25, 0.5, 0.75, 1.0)
AGE_SEEDS = (11, 12)
ARMS = ("A", "B", "C")


def backed_set(c0, p, seed=99):
    """Random set of people whose joining credit sums to p * total, P = c0 there."""
    n = len(c0)
    if p >= 1.0:
        return np.ones(n, bool)
    order = np.random.default_rng(seed).permutation(n)
    cum = np.cumsum(c0[order])
    take = order[cum <= p * c0.sum()]
    m = np.zeros(n, bool)
    m[take] = True
    return m


def set_pledges(k, arm, p, c0, mask):
    if arm == "A":
        k.P = p * k.C
    # B and C are set once, before the loop


def one_day_pledged(w, x, F, rho, p):
    """One day, P = p * C. Through the kernel, with the conformance checks."""
    k = Kernel(len(w), sb.credit_rate(w, F), Dials(rho=float(rho), floor_h=float(F)))
    k.accrue(days=1.0)
    k.P = p * k.C
    adm, _ = k.consume(x * KAPPA)
    Conformance.run_all(k)
    return float(adm.sum() / KAPPA)


def path(w, x, ages, F, rho, p, arm, M=sc.M_PRIMARY):
    n = len(w)
    k = Kernel(n, sb.credit_rate(w, F), Dials(rho=float(rho), floor_h=float(F)))
    c0 = F * 365.0 * ages
    k.C = c0.copy()
    k.D = sc.PAST_RATE * ages
    mask = None
    if arm == "B":
        k.P = p * c0
    elif arm == "C":
        mask = backed_set(c0, p)
        k.P = np.where(mask, c0, 0.0)
    out = np.empty(M)
    req = x * KAPPA * 365.0
    for t in range(M):
        k.accrue(days=365.0)
        set_pledges(k, arm, p, c0, mask)
        room_before = np.maximum(k.room(), 0.0)
        adm, _ = k.consume(req)
        if np.any(adm > room_before + 1e-6):
            raise AssertionError("admitted more than the gate allowed")
        Conformance.ic7_day_is_24_hours(k)
        Conformance.credit_only_rises(k)
        Conformance.debit_only_rises(k)
        Conformance.pledged_room_is_backed(k)
        out[t] = adm.sum() / (KAPPA * 365.0)
    return out


def edge_one_day(w, x, F, p, R):
    return sc.bisect_edge(lambda r: one_day_pledged(w, x, F, r, p) <= R)


def edge_cum(w, x, ages, F, p, arm, R, M=sc.M_PRIMARY):
    return sc.bisect_edge(lambda r: path(w, x, ages, F, r, p, arm, M).max() <= R)


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def _small():
    return sk.setup(6000, 3)


def test_p_zero_reproduces_the_kappa_edges():
    w, x, _, R = _small()
    ages = sc.draw_ages(len(w), 11)
    for F in FLOORS:
        a, _ = edge_one_day(w, x, F, 0.0, R)
        b, _ = sc.edge_one_day(w, x, F, KAPPA, R)
        assert abs(a - b) < 1e-3, (F, a, b)
        c, _ = edge_cum(w, x, ages, F, 0.0, "A", R, M=20)
        d, _ = sc.edge_cumulative(w, x, ages, F, KAPPA, R, M=20)
        assert abs(c - d) < 1e-3, (F, c, d)
    print("[ok] p = 0 reproduces stable_band_kappa's one-day and cumulative edges")


def test_one_day_edge_is_rho_star_over_one_plus_p():
    w, x, _, R = _small()
    for F in FLOORS:
        r0, _ = edge_one_day(w, x, F, 0.0, R)
        for p in (0.5, 1.0):
            r, _ = edge_one_day(w, x, F, p, R)
            assert abs(r - r0 / (1 + p)) < 2e-3, (F, p, r, r0 / (1 + p))
    print("[ok] one-day kernel edge = rho*/(1+p) at p = 0.5, 1")


def test_arm_a_is_the_rule():
    w, x, _, R = _small()
    ages = sc.draw_ages(len(w), 11)
    r0, _ = edge_cum(w, x, ages, 10.0, 0.0, "A", R, M=20)
    r1, _ = edge_cum(w, x, ages, 10.0, 1.0, "A", R, M=20)
    assert abs(r1 - r0 / 2) < 2e-3, (r0, r1)
    print(f"[ok] arm A: {r1:.3f} = {r0:.3f}/2")


def test_the_frozen_arm_can_break_the_rule():
    """If B equalled A, the arm would be decoration."""
    w, x, _, R = _small()
    ages = sc.draw_ages(len(w), 11)
    a, _ = edge_cum(w, x, ages, 10.0, 1.0, "A", R, M=100)
    b, _ = edge_cum(w, x, ages, 10.0, 1.0, "B", R, M=100)
    assert abs(a - b) > 0.01, (a, b)
    print(f"[ok] frozen pledges move the edge: A {a:.3f} vs B {b:.3f}")


def test_ic8_check_fires_and_concentrated_set_obeys_it():
    k = Kernel(3, np.array([10.0, 10.0, 10.0]), Dials(rho=1.0, floor_h=10.0))
    k.accrue(days=1.0)
    k.P = 2.0 * k.C                                  # P_total = 2 C_total
    try:
        Conformance.pledged_room_is_backed(k)
    except ConformanceError:
        pass
    else:
        raise AssertionError("IC-8 did not fire on P > C")
    c0 = np.random.default_rng(1).uniform(1, 3, 5000)
    for p in (0.25, 0.5, 0.75):
        m = backed_set(c0, p)
        share = c0[m].sum() / c0.sum()
        assert share <= p + 1e-9 and share > p - 0.01, (p, share)
    print("[ok] IC-8 fires on P > C; concentrated set sums to p of total credit")


def test_edge_is_monotone_in_p():
    w, x, _, R = _small()
    ages = sc.draw_ages(len(w), 11)
    for arm in ARMS:
        v = [edge_cum(w, x, ages, 10.0, p, arm, R, M=30)[0] for p in (0.0, 0.5, 1.0)]
        assert v[0] >= v[1] - 1e-6 and v[1] >= v[2] - 1e-6, (arm, v)
    print("[ok] edge never rises with p, all three arms")


def run_tests():
    for fn in (test_p_zero_reproduces_the_kappa_edges,
               test_one_day_edge_is_rho_star_over_one_plus_p,
               test_arm_a_is_the_rule,
               test_the_frozen_arm_can_break_the_rule,
               test_ic8_check_fires_and_concentrated_set_obeys_it,
               test_edge_is_monotone_in_p):
        fn()
    print("\nAll self-tests passed.")


# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    if ap.parse_args().test:
        run_tests()
        return
    w, x, kappa_old, R = sk.setup()
    n = len(w)
    print(f"N={n:,} seed={sb.RNG_SEED} kappa={KAPPA:.4f} R_max={R:,.0f} "
          f"wants={x.sum():,.0f} M={sc.M_PRIMARY} age seeds {AGE_SEEDS}")
    print()

    star = {}
    print("== 1. ONE-DAY publishable edge, kernel with P = p*C, beside rule rho*/(1+p) and break-even 3.78/F ==")
    print(f"{'F':>4} {'break-even':>10} | " + " | ".join(f"p={p:<4g} kern/rule" for p in PS))
    for F in FLOORS:
        row = []
        for p in PS:
            r, fl = edge_one_day(w, x, F, p, R)
            if p == 0.0:
                star[F] = r
            row.append(f"{r:.3f}/{star[F]/(1+p):.3f}{'*' if fl else ''}")
        print(f"{F:>4g} {KAPPA/F:>10.3f} | " + " | ".join(f"{c:>13}" for c in row))
    print()

    print("== 2. CUMULATIVE publishable edge (mean of age seeds; sd in brackets), by arm ==")
    cum = {}
    for arm in ARMS:
        print(f"-- arm {arm}")
        print(f"{'F':>4} {'break-even':>10} | " + " | ".join(f"p={p:<4g}" .rjust(15) for p in PS))
        for F in FLOORS:
            cells = []
            for p in PS:
                v = [edge_cum(w, x, sc.draw_ages(n, s), F, p, arm, R) for s in AGE_SEEDS]
                vals = np.array([a for a, _ in v])
                flags = sorted({f for _, f in v if f})
                cum[(arm, F, p)] = vals.mean()
                cells.append(f"{vals.mean():.3f}({vals.std():.4f}){'*' if flags else ''}".rjust(15))
            print(f"{F:>4g} {KAPPA/F:>10.3f} | " + " | ".join(cells))
    print()

    print("== 3. cumulative edge ÷ rule rho*/(1+p)   (1.000 = rule holds) ==")
    for arm in ARMS:
        print(f"-- arm {arm}")
        for F in FLOORS:
            print(f"{F:>4g} | " + " | ".join(
                f"p={p:<4g}{cum[(arm, F, p)] / (star[F]/(1+p)):>7.3f}" for p in PS))
    print()

    print("== 4. publishable edge ÷ break-even 3.78/F (arm A = rule) ==")
    for F in FLOORS:
        print(f"{F:>4g} | " + " | ".join(
            f"p={p:<4g}{star[F]/(1+p)/(KAPPA/F):>7.3f}" for p in PS))
    print()
    print("== 5. documented rho = 1.2 against the publishable edge at F=10 ==")
    for p in PS:
        print(f"p={p:<4g} edge {star[10.0]/(1+p):.3f}  1.2 is {1.2/(star[10.0]/(1+p)):.1f}x the edge")
    print("\n(* = bisection flag: edge at grid floor or censored)")


if __name__ == "__main__":
    main()
