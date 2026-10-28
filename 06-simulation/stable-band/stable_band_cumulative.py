#!/usr/bin/env python3
"""
stable_band_cumulative.py -- the upper edge rho*(F) on a CUMULATIVE ledger.

Request sr-20261023-re-run-stable-band-py-s-upper-edge-rho-on-a-
(filed 2026-10-23). Extends stable_band.py; it does not replace it.

THE QUESTION
    stable_band.py opens every cell at C = D = 0, accrues ONE day and consumes
    once. Foundations 5.5.6 makes the gate cumulative (C and D only ever rise)
    and 4.4 rebuilds a joiner's life back to birth. So a joiner of age a arrives
    with credit and debit already on the books. How far does that move rho*?

DECLARED BEFORE RUNNING (the inputs; outcomes are in RESULTS.md)
    population   the SAME 60,000 people as stable_band.py (seed 7): work_h, wants.
    kappa, R_max the SAME fixed calibration as stable_band.py (F_REF = 10).
    ages         drawn once per age-seed from a 5-band US-like pyramid,
                 uniform inside each band (AGE_BANDS below), independent of
                 work_h and wants. Age seeds 11..15.
    credit at joining   C0 = F * 365 * age       (floor only; past work is NOT
                 credited -- the conservative end, 4.4 condition 2).
    debit at joining    D0 = 1,380 * age         (cohort consumption, US method,
                 the same for everyone).
    joining      everyone joins on day one (period 0).
    period       one year = 365 days. Each period: accrue 365 days of credit at
                 rate F + work_h, then request wants * kappa * 365 debit-hours
                 and let the gate decide -- the one-day cell, scaled by 365.
    M            100 yearly periods (the primary horizon). No deaths, no births.
    rationing    a period RATIONS iff admitted real units <= R_max.
                 rho*_L = the highest rho at which EVERY period 1..M rations.
    return time  first period t with admitted_t <= 1.01 * (one-day admitted at
                 the same F and rho).

Run:  python stable_band_cumulative.py [--test]
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import stable_band as sb                                      # noqa: E402
from gate import Kernel, Dials, Conformance                   # noqa: E402

AGE_SEEDS = (11, 12, 13, 14, 15)
# (share of people, age from, age to), uniform within the band. US-like pyramid.
AGE_BANDS = ((0.22, 0, 18), (0.23, 18, 35), (0.19, 35, 50),
             (0.19, 50, 65), (0.17, 65, 85))
PAST_RATE = 1380.0               # h/yr, cohort consumption at the US method
M_PRIMARY = 100
M_LONG = 400                     # exploratory only, for the return period
RHO_LO, RHO_HI, TOL = 0.005, 4.0, 3e-4
FLOORS_ASKED = (2.0, 10.0, 14.0)
RETURN_TOL = 1.01


def draw_ages(n, seed):
    rng = np.random.default_rng(seed)
    shares = np.array([b[0] for b in AGE_BANDS])
    band = rng.choice(len(AGE_BANDS), size=n, p=shares / shares.sum())
    lo = np.array([b[1] for b in AGE_BANDS], float)[band]
    hi = np.array([b[2] for b in AGE_BANDS], float)[band]
    return lo + rng.random(n) * (hi - lo)


def run_path(work_h, wants, ages, F, rho, kappa, M,
             past_rate=PAST_RATE, past_work=False, check_gate=True):
    """Admitted real units in each of M yearly periods, through the kernel."""
    n = len(work_h)
    k = Kernel(n, sb.credit_rate(work_h, F), Dials(rho=float(rho), floor_h=float(F)))
    k.C = F * 365.0 * ages                                   # floor, every day lived
    if past_work:                                            # sensitivity only
        k.C = k.C + work_h * 365.0 * np.maximum(ages - 18.0, 0.0)
    k.D = past_rate * ages                                   # rebuilt consumption
    out = np.empty(M)
    req = wants * kappa * 365.0
    for t in range(M):
        k.accrue(days=365.0)
        room_before = np.maximum(k.room(), 0.0)
        admitted, _ = k.consume(req)
        if check_gate and np.any(admitted > room_before + 1e-6):
            raise AssertionError("admitted more than the gate allowed")
        # the kernel's other invariants. gate_was_respected is NOT run: a joiner
        # may arrive past the gate (acts before joining were never gated, 4.4).
        Conformance.ic7_day_is_24_hours(k)
        Conformance.credit_only_rises(k)
        Conformance.debit_only_rises(k)
        Conformance.pledged_room_is_backed(k)
        out[t] = admitted.sum() / (kappa * 365.0)
    return out


def one_day(work_h, wants, F, rho, kappa):
    return sb.admitted_total(work_h, wants, F, rho, kappa)[0]


def bisect_edge(ok):
    """Highest rho with ok(rho) True, ok monotone (True then False).
    Returns (value, flag): flag '' | 'below' (even RHO_LO fails) | 'censored'."""
    if not ok(RHO_LO):
        return RHO_LO, "below"
    if ok(RHO_HI):
        return RHO_HI, "censored"
    lo, hi = RHO_LO, RHO_HI
    while hi - lo > TOL:
        mid = 0.5 * (lo + hi)
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo, ""


def edge_one_day(work_h, wants, F, kappa, R_max):
    return bisect_edge(lambda r: one_day(work_h, wants, F, r, kappa) <= R_max)


def edge_cumulative(work_h, wants, ages, F, kappa, R_max, M=M_PRIMARY, **kw):
    return bisect_edge(
        lambda r: run_path(work_h, wants, ages, F, r, kappa, M, **kw).max() <= R_max)


def edge_at_period(work_h, wants, ages, F, kappa, R_max, M, **kw):
    """rho at which period M alone rations (the settled, late-life edge)."""
    return bisect_edge(
        lambda r: run_path(work_h, wants, ages, F, r, kappa, M, **kw)[-1] <= R_max)


def return_period(path, level):
    """First 1-based period with path <= RETURN_TOL*level, or None."""
    hit = np.flatnonzero(path <= RETURN_TOL * level)
    return int(hit[0]) + 1 if hit.size else None


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def _small(n=6000, seed=3):
    w, x = sb.build_people(n, seed=seed)
    kappa, B = sb.calibrate(w, x)
    return w, x, kappa, B / kappa


def test_age_zero_reproduces_the_one_day_cell():
    """Born-on-joining: period 1 must equal stable_band's one-day admitted."""
    w, x, kappa, _ = _small()
    zero = np.zeros(len(w))
    for F, rho in ((10.0, 1.2), (2.0, 1.0), (14.0, 0.9)):
        a = run_path(w, x, zero, F, rho, kappa, 1)[0]
        b = one_day(w, x, F, rho, kappa)
        assert abs(a - b) < 1e-6 * max(b, 1.0), (F, rho, a, b)
    print("[ok] age 0 on joining reproduces the one-day cell exactly")


def test_history_moves_the_answer():
    """An older cohort must admit MORE at F=10, rho=1.2 than a newborn one.
    If the credit rebuild did nothing, this fails."""
    w, x, kappa, _ = _small()
    n = len(w)
    new = run_path(w, x, np.zeros(n), 10.0, 1.2, kappa, 1)[0]
    old = run_path(w, x, np.full(n, 40.0), 10.0, 1.2, kappa, 1)[0]
    assert old > new * 1.05, (new, old)
    print(f"[ok] 40-year-olds admit more than newborns: {new:,.0f} -> {old:,.0f}")


def test_edge_falls_with_age():
    w, x, kappa, R = _small()
    n = len(w)
    e0, _ = edge_cumulative(w, x, np.zeros(n), 10.0, kappa, R, M=5)
    e40, _ = edge_cumulative(w, x, np.full(n, 40.0), 10.0, kappa, R, M=5)
    assert e40 < e0 - 0.1, (e0, e40)
    print(f"[ok] rho* falls with age: {e0:.2f} (age 0) -> {e40:.2f} (age 40)")


def test_instrument_matches_published_one_day_edge():
    """The bisection must reproduce stable_band's own grid answers."""
    w, x = sb.build_people()
    kappa, B = sb.calibrate(w, x)
    R = B / kappa
    for F, pub in ((2.0, 3.70), (10.0, 1.20), (14.0, 0.90)):
        e, flag = edge_one_day(w, x, F, kappa, R)
        assert flag == "" and abs(e - pub) <= 0.05, (F, e, pub)
    print("[ok] one-day bisection reproduces the published 3.70 / 1.20 / 0.90")


def test_a_ceiling_can_fail():
    """A rho near 4 must fail rationing for old joiners, a tiny rho must pass."""
    w, x, kappa, R = _small()
    n = len(w)
    ages = np.full(n, 40.0)
    lo = run_path(w, x, ages, 10.0, 0.05, kappa, 3).max()
    hi = run_path(w, x, ages, 10.0, 4.0, kappa, 3).max()
    assert lo <= R < hi, (lo, R, hi)
    print("[ok] the rationing test can fail (rho 4.0) and can pass (rho 0.05)")


def test_admission_is_nonincreasing_over_periods():
    """Stored room only runs down for binders, so the path may not rise."""
    w, x, kappa, _ = _small()
    ages = draw_ages(len(w), 11)
    p = run_path(w, x, ages, 10.0, 1.2, kappa, 60)
    assert np.all(np.diff(p) <= 1e-6 * p.max()), "admitted demand rose"
    print("[ok] admitted demand never rises over the periods")


def run_tests():
    for fn in (test_age_zero_reproduces_the_one_day_cell,
               test_history_moves_the_answer,
               test_edge_falls_with_age,
               test_instrument_matches_published_one_day_edge,
               test_a_ceiling_can_fail,
               test_admission_is_nonincreasing_over_periods):
        fn()
    print("\nAll self-tests passed.")


# =============================================================================
# the run
# =============================================================================

def fmt(v, flag):
    s = f"{v:.3f}"
    return s + {"": "", "below": " (<)", "censored": " (>=)"}[flag]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return

    w, x = sb.build_people()
    kappa, B = sb.calibrate(w, x)
    R = B / kappa
    n = len(w)
    print(f"N={n:,}  seed={sb.RNG_SEED}  kappa={kappa:.3f}  R_max={R:,.0f}  "
          f"wants_total={x.sum():,.0f}  M={M_PRIMARY}")
    for s in AGE_SEEDS[:1]:
        ag = draw_ages(n, s)
        print(f"ages seed {s}: mean {ag.mean():.1f}  median {np.median(ag):.1f}")
    print()

    # ---- 1. headline: rho*_L at each F, five age seeds -----------------------
    print("== 1. rho*_L (every period 1..M rations) vs one-day rho* ==")
    head = {}
    for F in FLOORS_ASKED:
        od, fo = edge_one_day(w, x, F, kappa, R)
        per_seed = []
        late = []
        for s in AGE_SEEDS:
            ag = draw_ages(n, s)
            e, fl = edge_cumulative(w, x, ag, F, kappa, R)
            per_seed.append((e, fl))
            l, lf = edge_at_period(w, x, ag, F, kappa, R, M_PRIMARY)
            late.append((l, lf))
        vals = np.array([p[0] for p in per_seed])
        lv = np.array([p[0] for p in late])
        head[F] = (od, fo, vals, [p[1] for p in per_seed], lv, [p[1] for p in late])
        print(f"F={F:>4g}  one-day {fmt(od, fo)}   rho*_L {vals.mean():.3f} "
              f"(sd {vals.std():.3f}, min {vals.min():.3f}, max {vals.max():.3f}) "
              f"flags {sorted(set(p[1] for p in per_seed))}   "
              f"rho*_L at period {M_PRIMARY} only: {lv.mean():.3f} "
              f"flags {sorted(set(p[1] for p in late))}")
    print()

    # ---- 2. what the admitted path looks like, and when it returns ----------
    print("== 2. admitted demand by period, and the return to the one-day level ==")
    ag = draw_ages(n, AGE_SEEDS[0])
    for F in FLOORS_ASKED:
        od = head[F][0]
        for label, rho in (("rho=1.2", 1.2), ("rho=one-day rho*", od)):
            level = one_day(w, x, F, rho, kappa)
            path = run_path(w, x, ag, F, rho, kappa, M_LONG)
            rp100 = return_period(path[:M_PRIMARY], level)
            rp400 = return_period(path, level)
            print(f"F={F:>4g} {label:>17} (rho {rho:.3f}) one-day {level:>9,.0f} "
                  f"R_max {R:,.0f} | t=1 {path[0]:>9,.0f} t=10 {path[9]:>9,.0f} "
                  f"t=50 {path[49]:>9,.0f} t=100 {path[99]:>9,.0f} t=400 {path[-1]:>9,.0f} "
                  f"| return: M=100 {rp100}  M=400 {rp400}")
    print()

    # ---- 3. sensitivities (age seed 11, M=100) ------------------------------
    print("== 3. sensitivities of rho*_L (age seed 11) ==")
    ag = draw_ages(n, AGE_SEEDS[0])
    variants = [
        ("declared", dict()),
        ("all join at age 0", dict(ages=np.zeros(n))),
        ("all join at age 20", dict(ages=np.full(n, 20.0))),
        ("all join at age 40", dict(ages=np.full(n, 40.0))),
        ("past work credited (adults, at today's work_h)", dict(past_work=True)),
        ("past debit 1,000 h/yr", dict(past_rate=1000.0)),
        ("past debit 2,000 h/yr", dict(past_rate=2000.0)),
        ("past debit = model flow, 5,037 h/yr (kappa*365)",
         dict(past_rate=kappa * 365.0)),
    ]
    for name, kw in variants:
        kw = dict(kw)
        ages = kw.pop("ages", ag)
        row = []
        for F in FLOORS_ASKED:
            e, fl = edge_cumulative(w, x, ages, F, kappa, R, **kw)
            row.append(fmt(e, fl))
        print(f"{name:<50} F=2 {row[0]:>9}  F=10 {row[1]:>9}  F=14 {row[2]:>9}")
    print()
    print("(<) = even rho 0.005 fails to ration: value is a ceiling on the edge, "
          "not a value.  (>=) = grid ended: a floor, not a value.")


if __name__ == "__main__":
    main()
