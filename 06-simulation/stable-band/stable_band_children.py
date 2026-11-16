#!/usr/bin/env python3
"""
stable_band_children.py -- stable_band_cumulative.py, kappa-tied, with children.

Request sr-20261031-re-run-stable-band-cumulative-py-kappa-tied-  (filed 2026-10-31).
Extends stable_band_cumulative.py and stable_band_kappa.py; replaces neither.

Three arms (declared in CHILDREN_DECLARED.md before the first run):
  0  control   past debit = 1,380 * age                      (the published run)
  1  child debit  past debit = 1,380 * max(0, age - 18); everything else as arm 0
  2  household    arm 1, and every person under 18 requests nothing under their
                  own gate; their requests are split in equal shares across the
                  adults (age >= 18) and added to each adult's request.

Pledges.md ruling 7: a child carries no debit; goods stay with the guardian.

Run:  python stable_band_children.py [--test] [--arm N] [--seeds 11,12,...]
"""
from __future__ import annotations

import argparse
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import stable_band as sb                                      # noqa: E402
import stable_band_cumulative as sc                           # noqa: E402
import stable_band_kappa as skp                               # noqa: E402
from gate import Kernel, Dials, Conformance                   # noqa: E402

KAPPA = skp.KAPPA_ANCHOR            # 1,380 / 365
ADULT_AGE = 18.0
FLOORS = sc.FLOORS_ASKED
PUBLISHED = {2.0: 1.017, 10.0: 0.330, 14.0: 0.253}


def past_debit(ages, arm, rate=sc.PAST_RATE):
    if arm == 0:
        return rate * ages
    return rate * np.maximum(ages - ADULT_AGE, 0.0)


def requests(wants, ages, arm, kappa=KAPPA):
    """Yearly request in debit-hours, per person."""
    req = wants * kappa * 365.0
    if arm < 2:
        return req
    child = ages < ADULT_AGE
    adult = ~child
    out = np.where(child, 0.0, req)
    share = req[child].sum() / max(int(adult.sum()), 1)
    return out + np.where(adult, share, 0.0)


def run_path(work_h, wants, ages, F, rho, M, arm, kappa=KAPPA):
    n = len(work_h)
    k = Kernel(n, sb.credit_rate(work_h, F), Dials(rho=float(rho), floor_h=float(F)))
    k.C = F * 365.0 * ages
    k.D = past_debit(ages, arm)
    req = requests(wants, ages, arm, kappa)
    out = np.empty(M)
    for t in range(M):
        k.accrue(days=365.0)
        admitted, _ = k.consume(req)
        Conformance.ic7_day_is_24_hours(k)
        Conformance.credit_only_rises(k)
        Conformance.debit_only_rises(k)
        out[t] = admitted.sum() / (kappa * 365.0)
    return out


def edge(work_h, wants, ages, F, R, M, arm):
    return sc.bisect_edge(lambda r: run_path(work_h, wants, ages, F, r, M, arm).max() <= R)


def setting_period(work_h, wants, ages, F, rho_star, M, arm):
    """Period of the worst admitted demand at the first rho that fails."""
    p = run_path(work_h, wants, ages, F, rho_star + 2 * sc.TOL, M, arm)
    return int(np.argmax(p)) + 1, float(p.max())


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def _small(n=6000, seed=3):
    w, x, _, R = skp.setup(n, seed)
    return w, x, R


def test_arm0_equals_the_published_script():
    w, x, _ = _small()
    ag = sc.draw_ages(len(w), 11)
    for F, rho in ((10.0, 0.3), (2.0, 1.0), (14.0, 0.25)):
        a = run_path(w, x, ag, F, rho, 5, 0)
        b = sc.run_path(w, x, ag, F, rho, KAPPA, 5)
        assert np.allclose(a, b, rtol=1e-9), (F, a, b)
    print("[ok] arm 0 reproduces stable_band_cumulative.run_path exactly")


def test_arm1_debit_is_zero_for_children():
    ag = np.array([0.0, 9.0, 17.99, 18.0, 40.0])
    d = past_debit(ag, 1)
    assert np.all(d[:3] == 0.0) and d[3] == 0.0 and abs(d[4] - 1380 * 22) < 1e-9, d
    assert abs(past_debit(ag, 0)[4] - 1380 * 40) < 1e-9
    print("[ok] arm 1 books no past debit under 18, 1,380 x (age-18) after")


def test_arm2_children_request_nothing_and_total_is_kept():
    w, x, _ = _small()
    ag = sc.draw_ages(len(w), 11)
    r1, r2 = requests(x, ag, 1), requests(x, ag, 2)
    child = ag < ADULT_AGE
    assert np.all(r2[child] == 0.0)
    assert abs(r1.sum() - r2.sum()) < 1e-6 * r1.sum()
    assert np.all(r2[~child] > r1[~child])
    print(f"[ok] arm 2: children request 0, total request unchanged "
          f"({r1.sum():,.0f} h), adults +{(r2[~child]/r1[~child]-1).mean():.1%}")


def test_arm2_admits_nothing_to_children():
    w, x, _ = _small()
    ag = sc.draw_ages(len(w), 11)
    k = Kernel(len(w), sb.credit_rate(w, 10.0), Dials(rho=4.0, floor_h=10.0))
    k.C = 10.0 * 365.0 * ag
    k.D = past_debit(ag, 2)
    k.accrue(days=365.0)
    adm, _ = k.consume(requests(x, ag, 2))
    assert adm[ag < ADULT_AGE].sum() == 0.0
    tot = adm.sum() / (KAPPA * 365.0)
    assert abs(tot - x.sum()) < 1e-6 * x.sum(), (tot, x.sum())
    print(f"[ok] at rho 4 arm 2 admits the whole of wants to adults: {tot:,.0f}")


def test_arm1_moves_the_edge():
    w, x, R = _small()
    ag = sc.draw_ages(len(w), 11)
    e0, _ = edge(w, x, ag, 10.0, R, 5, 0)
    e1, _ = edge(w, x, ag, 10.0, R, 5, 1)
    assert e1 < e0 - 0.02, (e0, e1)
    print(f"[ok] child debit moves the edge: {e0:.3f} -> {e1:.3f} (F=10, M=5, n=6000)")


def test_a_ceiling_can_fail_in_every_arm():
    w, x, R = _small()
    ag = sc.draw_ages(len(w), 11)
    for arm in (0, 1, 2):
        lo = run_path(w, x, ag, 10.0, 0.02, 3, arm).max()
        hi = run_path(w, x, ag, 10.0, 4.0, 3, arm).max()
        assert lo <= R < hi, (arm, lo, R, hi)
    print("[ok] rationing test can pass (rho .02) and fail (rho 4) in all three arms")


def run_tests():
    for fn in (test_arm0_equals_the_published_script,
               test_arm1_debit_is_zero_for_children,
               test_arm2_children_request_nothing_and_total_is_kept,
               test_arm2_admits_nothing_to_children,
               test_arm1_moves_the_edge,
               test_a_ceiling_can_fail_in_every_arm):
        fn()
    print("\nAll self-tests passed.")


# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--arm", type=int, default=None)
    ap.add_argument("--seeds", default=",".join(map(str, sc.AGE_SEEDS)))
    ap.add_argument("--M", type=int, default=sc.M_PRIMARY)
    a = ap.parse_args()
    if a.test:
        run_tests()
        return
    seeds = [int(s) for s in a.seeds.split(",")]
    w, x, kappa_old, R = skp.setup()
    n = len(w)
    print(f"N={n:,} seed={sb.RNG_SEED} kappa={KAPPA:.4f} R_max={R:,.0f} "
          f"wants={x.sum():,.0f} M={a.M} age seeds {seeds}", flush=True)
    arms = [a.arm] if a.arm is not None else [0, 1, 2]
    for arm in arms:
        for F in FLOORS:
            t0 = time.time()
            vals, flags, sets = [], [], []
            for s in seeds:
                ag = sc.draw_ages(n, s)
                e, fl = edge(w, x, ag, F, R, a.M, arm)
                p, mx = setting_period(w, x, ag, F, e, a.M, arm)
                vals.append(e); flags.append(fl); sets.append((p, mx))
            v = np.array(vals)
            ag0 = sc.draw_ages(n, seeds[0])
            kids = float((ag0 < ADULT_AGE).mean())
            print(f"ARM {arm} F={F:>4g} rho*_L mean {v.mean():.3f} sd {v.std():.3f} "
                  f"min {v.min():.3f} max {v.max():.3f} flags {sorted(set(flags))} "
                  f"setting period {sorted(set(s[0] for s in sets))} "
                  f"max admitted at first failing rho {np.mean([s[1] for s in sets]):,.0f} "
                  f"(R_max {R:,.0f}) per-seed {[round(t,3) for t in vals]} "
                  f"under18 share {kids:.3f} [{time.time()-t0:.0f}s]", flush=True)


if __name__ == "__main__":
    main()
