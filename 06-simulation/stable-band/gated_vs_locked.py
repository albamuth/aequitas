#!/usr/bin/env python3
"""
gated_vs_locked.py -- at the one-day rho* of stable_band_kappa.py, how many people
does the gate hold back (a), and how many have a yearly request above rho x 8,760 (b)?

Request sr-20261111-in-stable-band-kappa-py-s-own-population-60-
(objection obj-20261111-gradient-dissent-edge-from-other-population).

(a) share held below what they wanted: stable_band.admitted_total's 2nd return,
    run through the kernel's own gate, kappa = 1,380/365, R_max as in stable_band_kappa.
(b) share whose yearly request  wants * kappa * 365  exceeds rho * 8,760
    (the q4 lock line T(rho) = rho * 24 * 365), counted in THIS population.
Beside (b): q4_locked_ledgers' closed form, lognormal sigma 0.80 at median 1,380:
    share = 1 - Phi( ln(T / 1380) / 0.80 )      (body only, no Pareto tail, no billionaires)
    and q4's own sampled population (body + tail) re-anchored at median 1,380.

Run:  python gated_vs_locked.py [--test]
"""
from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "scenario-suite"))

import stable_band as sb                                    # noqa: E402
import stable_band_cumulative as sc                         # noqa: E402
import stable_band_kappa as sk                              # noqa: E402

MEDIAN_H = 1380.0
MAX_CREDIT = 24.0 * 365.0
Q4_SIGMA = 0.80
FLOORS = (2.0, 10.0, 14.0)
EXTRA_RHO = 1.5


def phi_sf(z):
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def q4_closed_form_pct(rho, median=MEDIAN_H, sigma=Q4_SIGMA):
    return 100.0 * phi_sf(math.log(rho * MAX_CREDIT / median) / sigma)


def share_above_line(wants, rho, kappa=sk.KAPPA_ANCHOR):
    """(b): yearly request wants*kappa*365 > rho*8,760."""
    return float(np.mean(wants * kappa * 365.0 > rho * MAX_CREDIT))


def held_below(w, x, F, rho, kappa=sk.KAPPA_ANCHOR):
    """(a): admitted_total's second return."""
    return sb.admitted_total(w, x, F, rho, kappa)


def q4_sampled_pct(rho, median=MEDIAN_H):
    import q4_locked_ledgers as q4
    q4.MEDIAN_FOOTPRINT_H = median
    q4.RNG = np.random.default_rng(7)
    f = q4.build_us_footprints(n=2_000_000, rng=q4.RNG)
    return q4.pct_locked(f, rho)


# ------------------------------------------------------------------ tests
def test_closed_form_matches_the_quoted_numbers():
    for rho, quoted in ((1.017, 0.99), (0.330, 17.77), (0.253, 27.69)):
        got = q4_closed_form_pct(rho)
        assert abs(got - quoted) < 0.05, (rho, got, quoted)
    print("[ok] closed form reproduces the quoted 0.99 / 17.77 / 27.69")


def test_a_can_fail_and_b_can_fail():
    w, x, _, R = sk.setup(6000, 3)
    lo = held_below(w, x, 10.0, 0.05)[1]
    hi = held_below(w, x, 10.0, 4.0)[1]
    assert lo > 0.5 and hi < 0.05, (lo, hi)     # tight gate holds many, loose holds few
    assert share_above_line(x, 0.05) > share_above_line(x, 4.0)
    print(f"[ok] (a) {lo:.2f} at rho .05 vs {hi:.4f} at rho 4; (b) also falls with rho")


def test_edge_reproduces_request_values():
    w, x, _, R = sk.setup()
    for F, quoted in ((2.0, 1.017), (10.0, 0.330), (14.0, 0.253)):
        got, flag = sc.edge_one_day(w, x, F, sk.KAPPA_ANCHOR, R)
        assert flag == "" and abs(got - quoted) < 0.002, (F, got, quoted)
    print("[ok] one-day rho* = 1.017 / 0.330 / 0.253 reproduced")


def run_tests():
    test_closed_form_matches_the_quoted_numbers()
    test_a_can_fail_and_b_can_fail()
    test_edge_reproduces_request_values()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    if ap.parse_args().test:
        run_tests()
        return
    w, x, kappa_old, R = sk.setup()
    print(f"N={len(w):,} seed={sb.RNG_SEED} kappa={sk.KAPPA_ANCHOR:.4f} R_max={R:,.0f} "
          f"wants_total={x.sum():,.0f}")
    lx = np.log(x)
    print(f"wants: median {np.median(x):.3f} mean {x.mean():.3f} max {x.max():.2f} "
          f"max yearly request {x.max()*MEDIAN_H:,.0f} h; log-sd {lx.std():.3f}")
    print(f"T(rho)=rho*8,760 h/yr; q4 sampled population re-anchored at median {MEDIAN_H:.0f}\n")
    print(f"{'F':>3} {'rho':>7} {'which':>6} | {'(a) held %':>10} {'(a) n':>7} | "
          f"{'(b) >line %':>11} {'(b) n':>6} | {'q4 closed %':>11} {'q4 sampled %':>12} | "
          f"{'admitted':>9}")
    for F in FLOORS:
        edge, flag = sc.edge_one_day(w, x, F, sk.KAPPA_ANCHOR, R)
        for tag, rho in (("rho*", edge), ("1.5", EXTRA_RHO)):
            tot, fr = held_below(w, x, F, rho)
            b = share_above_line(x, rho)
            print(f"{F:>3g} {rho:>7.3f} {tag:>6} | {fr*100:>10.2f} {int(round(fr*len(w))):>7,} | "
                  f"{b*100:>11.4f} {int(round(b*len(w))):>6,} | "
                  f"{q4_closed_form_pct(rho):>11.2f} {q4_sampled_pct(rho):>12.2f} | "
                  f"{tot:>9,.0f}")
    print("\nSubset check (locked must be <= gated): see (b) vs (a) per row.")


if __name__ == "__main__":
    main()
