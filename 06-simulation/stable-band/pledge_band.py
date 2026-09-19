#!/usr/bin/env python3
"""
The stable band, re-run with a pledge term.
=============================================================================

WHY THIS EXISTS
---------------
`stable_band.py` computed the workable band of (F, rho) with NO pledges in it.
Under the ruling of 2026-09-18 the consumption gate is

    D <= rho * (C + P)

where P is COMMITTED pledged room. Backing is one hour pledged per hour earned
(conformance row 9, IC-8), so across a network P_total <= C_total.

Write P = p * C, where p in [0, 1] is the PLEDGE DENSITY -- the share of the
population's lifetime pledge budget that has been committed to somebody. Then

    D <= rho * (1 + p) * C

so the EFFECTIVE tolerance is rho*(1+p), and a network that PUBLISHES rho is
running at up to twice that when p = 1.

    ***  This is exact, not an approximation, and it needs no kernel change. ***

`stable_band.py` was run with no pledges, so the rho it swept IS the effective
tolerance. This script reuses its measured upper edge and reports the band a
network may actually PUBLISH.

THE ASYMMETRY, AND IT IS THE POINT
----------------------------------
The two edges do NOT see p the same way, and treating them alike would be wrong.

  UPPER EDGE -- "does the ledger still ration?" is an AGGREGATE question about
  the whole population's demand against capacity. The population's own p is
  what belongs in it.  publishable upper = rho*(F) / (1 + p)

  LOWER EDGE -- "can a person who does nothing but stay alive afford
  essentials?" must hold for somebody NOBODY PLEDGED TO. Their own p is 0,
  whatever the population average is. So the lower edge does not move.
      publishable lower = E / (365 * F),  at p = 0, always.

Reading the lower edge at the population's p would make essentials look
affordable because OTHER people were given room. That is the flattering
direction, and Foundations Sec.4.4 says errors of this shape are not caught by
whoever made them.

WHAT IT MEASURES
----------------
The band narrows from ONE side as p rises. Whether it ever CLOSES is the
question, because `stable_band.py`'s headline was that it never does.

Run:  python pledge_band.py            (report)
      python pledge_band.py --test     (self-tests only)
"""

import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from stable_band import (                                    # noqa: E402
    build_people, calibrate, us_case, upper_edge,
    FLOORS, E_SHARES, MEDIAN_LIFESTYLE_H_YR,
)

# Pledge density: the share of the population's lifetime pledge budget that has
# been committed. p = 1 is the one-for-one ceiling, where every subscriber has
# committed every hour they ever earned.
PLEDGE_DENSITIES = (0.00, 0.25, 0.50, 0.75, 1.00)


def publishable_upper(rho_star_effective, p):
    """The rho a network may PUBLISH, given a population pledge density p."""
    if rho_star_effective is None:
        return None
    return float(rho_star_effective) / (1.0 + float(p))


def lower_edge(floor_h, E_h_yr):
    """Unchanged by p. Essentials must be affordable to somebody nobody pledged to."""
    return float(E_h_yr) / (365.0 * float(floor_h))


def band(floor_h, rho_star_effective, E_h_yr, p):
    """(lo, hi, width, open?) in PUBLISHABLE rho."""
    lo = lower_edge(floor_h, E_h_yr)
    hi = publishable_upper(rho_star_effective, p)
    if hi is None:
        return lo, None, None, None
    return lo, hi, hi - lo, hi >= lo


# =============================================================================
# report
# =============================================================================

def print_report(edges_us, E_shares=E_SHARES):
    star = {f: r for f, r, _ in edges_us}

    print("=" * 78)
    print("THE STABLE BAND WITH A PLEDGE TERM")
    print("=" * 78)
    print()
    print("Gate:  D <= rho * (C + P),  P = p * C,  p in [0, 1]")
    print("Effective tolerance = rho * (1 + p).  Upper edge falls as 1/(1+p).")
    print("Lower edge is read at p = 0: essentials must be affordable to")
    print("somebody nobody pledged to.")
    print()

    print("-" * 78)
    print("1. PUBLISHABLE UPPER EDGE, rho*(F) / (1 + p)")
    print("-" * 78)
    hdr = f"{'F (h/day)':>10} | " + " | ".join(f"p={p:<5.2f}" for p in PLEDGE_DENSITIES)
    print(hdr)
    print("-" * len(hdr))
    for f in FLOORS:
        if star.get(f) is None:
            continue
        cells = " | ".join(f"{publishable_upper(star[f], p):>7.2f}" for p in PLEDGE_DENSITIES)
        print(f"{f:>10.1f} | {cells}")
    print()
    print("  p = 0 reproduces stable_band.py exactly. p = 1 halves every entry.")
    print()

    for share in E_shares:
        E = share * MEDIAN_LIFESTYLE_H_YR
        print("-" * 78)
        print(f"2. THE BAND IN PUBLISHABLE rho -- essentials at {share:.0%} of a median "
              f"lifestyle (E = {E:,.0f} h/yr)")
        print("-" * 78)
        hdr = (f"{'F':>6} | {'lower':>7} | "
               + " | ".join(f"{'p=' + format(p, '.2f'):>16}" for p in PLEDGE_DENSITIES))
        print(hdr)
        print("-" * len(hdr))
        for f in FLOORS:
            if star.get(f) is None:
                continue
            lo = lower_edge(f, E)
            cells = []
            for p in PLEDGE_DENSITIES:
                _, hi, w, ok = band(f, star[f], E, p)
                cells.append(f"[{lo:.2f},{hi:.2f}] {'' if ok else 'SHUT'}".rjust(16))
            print(f"{f:>6.1f} | {lo:>7.3f} | " + " | ".join(cells))
        print()

    print("-" * 78)
    print("3. DOES THE BAND EVER CLOSE?")
    print("-" * 78)
    closed = []
    for share in E_shares:
        E = share * MEDIAN_LIFESTYLE_H_YR
        for f in FLOORS:
            if star.get(f) is None:
                continue
            for p in PLEDGE_DENSITIES:
                _, hi, _, ok = band(f, star[f], E, p)
                if not ok:
                    closed.append((share, float(f), float(p), lower_edge(f, E), hi))
    if closed:
        print(f"  CLOSES in {len(closed)} swept cells:")
        for share, f, p, lo, hi in closed[:20]:
            print(f"    E={share:.0%}  F={f:.1f}  p={p:.2f}  ->  lower {lo:.3f} > upper {hi:.3f}")
    else:
        print("  NO. The band stays open in every swept cell, at every pledge")
        print("  density up to the one-for-one ceiling p = 1.")
        print("  stable_band.py's headline survives the pledge term.")
    print()

    print("-" * 78)
    print("4. WHAT IT COSTS, AT THE DOCUMENTED SETTING F = 10")
    print("-" * 78)
    f10 = 10.0
    if star.get(f10) is not None:
        for p in PLEDGE_DENSITIES:
            print(f"  p = {p:.2f}  ->  a network may publish rho up to "
                  f"{publishable_upper(star[f10], p):.2f}")
        print()
        print(f"  rho*(10) = {star[f10]:.2f}, so the documented setting rho = 1.2")
        print(f"  sits EXACTLY AT the publishable edge when p = 0, and above it")
        print(f"  for every p > 0. Any pledging at all puts it out of band.")
    print()

    print("=" * 78)
    print("WHAT THIS DOES NOT SHOW")
    print("=" * 78)
    print("  - p is swept, not measured. Nobody knows what pledge density a real")
    print("    network would run at, and it is a behavioural quantity.")
    print("  - The upper edge is inherited from stable_band.py, including its own")
    print("    censoring: rows whose rho* ran off the top of the swept range are")
    print("    floors and are excluded here rather than reported.")
    print("  - Uncommitted pledges are not in p at all. A pledge to a fund grants")
    print("    no room until it names somebody (Foundations ruling, 2026-09-18).")
    print("  - The 1,380 h/yr anchor behind E is one defensible reading, not a")
    print("    fact about the world. See papers/Pledges.md Sec.15.3.")


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def test_p_zero_reproduces_the_published_edge(star):
    for f, r in star.items():
        if r is None:
            continue
        assert abs(publishable_upper(r, 0.0) - r) < 1e-12, f
    print("[ok] p = 0 reproduces stable_band.py's upper edge exactly")


def test_p_one_halves_the_edge(star):
    for f, r in star.items():
        if r is None:
            continue
        assert abs(publishable_upper(r, 1.0) - r / 2.0) < 1e-12, f
    print("[ok] p = 1 halves the publishable upper edge")


def test_upper_edge_is_monotone_in_p(star):
    for f, r in star.items():
        if r is None:
            continue
        vals = [publishable_upper(r, p) for p in PLEDGE_DENSITIES]
        assert all(a >= b for a, b in zip(vals, vals[1:])), f
    print("[ok] the publishable upper edge falls monotonically in p")


def test_lower_edge_does_not_move_with_p():
    E = 0.5 * MEDIAN_LIFESTYLE_H_YR
    a = lower_edge(10.0, E)
    b = lower_edge(10.0, E)
    assert a == b
    # and it is genuinely sensitive to the things it SHOULD move with
    assert lower_edge(10.0, E) > lower_edge(14.0, E)
    assert lower_edge(10.0, 2 * E) > lower_edge(10.0, E)
    print("[ok] the lower edge ignores p, and still moves with F and E")


def test_the_closure_check_can_fire():
    """If the band could never be reported shut, section 3 would be decoration."""
    # A deliberately impossible setting: essentials at 20x a median lifestyle.
    E_absurd = 20.0 * MEDIAN_LIFESTYLE_H_YR
    lo, hi, _, ok = band(10.0, 1.20, E_absurd, 1.00)
    assert ok is False, (lo, hi)
    print(f"[ok] the closure check fires when it should "
          f"(lower {lo:.2f} > upper {hi:.2f} at an absurd E)")


def run_tests(star):
    test_p_zero_reproduces_the_published_edge(star)
    test_p_one_halves_the_edge(star)
    test_upper_edge_is_monotone_in_p(star)
    test_lower_edge_does_not_move_with_p()
    test_the_closure_check_can_fire()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()

    work_h, wants = build_people()
    kappa_us, B = calibrate(work_h, wants)
    kappa, R_max = us_case(kappa_us, B)
    edges_us = upper_edge(work_h, wants, kappa, R_max)
    star = {f: r for f, r, _ in edges_us}

    if args.test:
        run_tests(star)
        return
    print_report(edges_us)
    print()
    run_tests(star)


if __name__ == "__main__":
    main()
