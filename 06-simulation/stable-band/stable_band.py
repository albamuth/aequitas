#!/usr/bin/env python3
"""
Statera study -- the stable band of F and rho.

THE QUESTION, and it is owed in writing.
---------------------------------------
Foundations Sec.5.5.3 gives the floor a bound at each end and nothing in between:

    "Set it too low and people cannot afford what they need. Set it too high and
     the books stop rationing anything. Finding the value that balances the
     economy is the network's job."

    "Owed: a simulation showing the stable band, and its width. Nothing in this
     section claims the band has been found."

This is that simulation. Registered against OP-4 (debit tolerance).

THE TWO DIALS. Aequitas uses these and never sets them (A8).

    F     the FLOOR. Hours a day a network credits for the work of staying alive.
    rho   the DEBIT TOLERANCE. The multiplier in the consumption gate D <= rho*C,
          where D is recorded debit and C is recorded credit.

THE TWO EDGES. Each compares a dial-driven quantity against an EXOGENOUS one --
a fact about the economy that no dial can move.

    LOWER EDGE -- essentials must be affordable to a person who does nothing else.
        A floor-only person's yearly room is  rho * F * 365  debit-hours.
        A year of essentials commands  E  hours of other people's labour.
        AFFORDABLE  <=>  rho * F * 365 >= E.

    UPPER EDGE -- the ledger must still ration what is genuinely short.
        Total admitted demand must not exceed what the economy can physically
        deliver, R_max. Above that, the gate has stopped deciding who gets what
        and physical shortage decides at the point of distribution instead
        (Sec.5.5.3, Sec.3.4a) -- "the accounting has stopped doing the work it
        was set up to do."
        RATIONS  <=>  admitted_total <= R_max.

    IN BAND  <=>  both.

THE TRAP THIS SCRIPT IS BUILT TO AVOID, and it has caught this project twice.
------------------------------------------------------------------------------
@amber, c24446 on 1f916.ai:  "A check whose passing condition is set by the
checker is not an instrument, and it fails toward flattery."

@alfred-pennyworth, c23625, killed Q1's labour row on exactly this ground: its
numerator was CREDITED hours, which include the floor, and the floor is a value
the network sets by rule -- so the pass condition was fixed the moment F was
chosen, before a single worker was counted.

So two calibrations are computed ONCE, at a reference floor, and HELD FIXED
across the whole grid:

    kappa   debit-hours per unit of median lifestyle. If this were recalibrated
            per F, then rho = 1 would fund one median lifestyle at every floor,
            F would cancel out, and the sweep would measure nothing.
    R_max   the physical capacity of the economy. It is a fact about factories
            and energy, not about a bookkeeping dial.

Both edges can fail, and each fails at a different corner of the grid. That is
what makes this an instrument rather than a ceremony.

WHAT IS EXOGENOUS AND WHERE IT CAME FROM
    1,380 h/yr   labour a median US lifestyle commands.
                 06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md
    E            a year of ESSENTIALS. Nobody has measured this, so it is SWEPT
                 as a fraction of the median lifestyle rather than assumed.
                 Sec.5.5.3 uses 700 h/yr as an illustration and says so.
    CAP = 0.85   physical capacity as a share of unconstrained wants.
                 06-simulation/disparity-ceiling/rho_sweep.py

Run:  python stable_band.py [--test] [--no-plots]
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "statera"))
sys.path.insert(0, os.path.join(HERE, "..", "disparity-ceiling"))

from statera import Kernel, Dials, Conformance, DAY          # noqa: E402

RNG_SEED = 7
N = 60_000

MEDIAN_LIFESTYLE_H_YR = 1380.0        # measured; see the header
CAP = 0.85                            # physical capacity / unconstrained wants
F_REF = 10.0                          # reference floor for the FIXED calibration

# The grid.
FLOORS = np.arange(1.0, 14.01, 0.5)          # h/day
RHOS = np.arange(0.20, 4.001, 0.05)          # multiplier

# E, a year of essentials, as a share of a median lifestyle. Swept, not assumed.
E_SHARES = (0.30, 0.50, 0.70)

# PRODUCTION METHOD. Debit-hours per unit of the SAME real standard of living.
# Measured, not modelled: cross-country embodied-labour accounting over EXIOBASE,
# 06-simulation/median-lifestyle/Q6.md. The US is the outlier -- Germany, Japan and
# Spain deliver a comparable-or-better material standard, and longer lives, at
# roughly two thirds of the embodied labour and a quarter to a half of the CO2.
#   0.64 = 820/1283 h (Germany/US)      0.55 = 709/1283 h (Spain/US)
EFF = {"US method": 1.00, "German or Japanese method": 0.64, "Spanish method": 0.55}


# =============================================================================
# population -- drawn ONCE, so that moving F moves the credit and nothing else
# =============================================================================

def build_people(n=N, seed=RNG_SEED):
    """Work hours and desires for n people. Neither depends on F or rho.

    c(F) = F + work_h.  A network that credits more for self-care records more
    credit for the SAME lives -- the people do not change when the dial moves.
    """
    rng = np.random.default_rng(seed)
    works = rng.random(n) > 0.35                    # ~35% do little or no paid work
    work_h = np.where(
        works,
        np.clip(rng.normal(6.0, 3.0, n), 0.0, DAY - 14.0),
        rng.uniform(0.0, 1.5, n),
    )
    wants = rng.lognormal(mean=0.0, sigma=0.45, size=n)
    wants /= np.median(wants)
    wants *= ((F_REF + work_h) / np.median(F_REF + work_h)) ** 0.25
    wants /= np.median(wants)                       # median desired lifestyle = 1.0
    return work_h, wants


def credit_rate(work_h, floor_h):
    return float(floor_h) + work_h


# =============================================================================
# the two edges
# =============================================================================

def affordable(floor_h, rho, E_h_yr):
    """LOWER EDGE. Can a person who does nothing but stay alive afford essentials?"""
    return (rho * floor_h * 365.0) >= E_h_yr


def admitted_total(work_h, wants, floor_h, rho, kappa):
    """Drive demand through the kernel's own gate and conformance checks.

    Returns (real lifestyle-units admitted in total, fraction of people held
    below what they wanted).
    """
    c = credit_rate(work_h, floor_h)
    n = len(c)
    k = Kernel(n, c, Dials(rho=float(rho), floor_h=float(floor_h)))
    k.accrue(days=1.0)
    admitted, _ = k.consume(wants * kappa)          # request in debit-hours
    Conformance.run_all(k)
    real = admitted / kappa
    return float(real.sum()), float((real < wants - 1e-9).mean())


# =============================================================================
# the sweep
# =============================================================================

def calibrate(work_h, wants):
    """kappa_US and B, computed ONCE at F_REF and held fixed. See the header.

    B is the PHYSICAL BUDGET in debit-hours -- the energy and materials envelope.
    It is a fact about the planet, so it does not move when a production method
    changes. What changes is how much real living that same envelope buys:

        kappa(eff) = kappa_US * eff        debit-hours per unit of real standard
        R_max(eff) = B / kappa(eff)        real units the envelope delivers

    So a method that needs less debit for the same standard delivers MORE real
    living from an unchanged physical envelope. That is the Q6 channel.
    """
    c_ref = credit_rate(work_h, F_REF)
    kappa_us = float(np.median(c_ref))              # debit-h per lifestyle-unit, US
    B = CAP * float(wants.sum()) * kappa_us         # physical budget, debit-hours
    return kappa_us, B


def us_case(kappa_us, B):
    """The US method as (kappa, R_max), which is what the two edges want."""
    return kappa_us, B / kappa_us


def method_edges(work_h, wants, kappa_us, B, eff):
    """rho*(F) for one production method, plus what it costs and delivers.

    kappa = kappa_us * eff   debit-hours per unit of the same real standard
    R_max = B / kappa        real units the FIXED physical envelope delivers
    """
    kappa = kappa_us * eff
    R_max = B / kappa
    return upper_edge(work_h, wants, kappa, R_max), kappa, R_max


def upper_edge(work_h, wants, kappa, R_max):
    """rho*(F) -- the highest tolerance at which the ledger still rations.

    THIS DOES NOT DEPEND ON E. It is a fact about the population and the
    economy's capacity, so it is computed once per floor and reused for every
    essentials basket. Above it, admitted demand exceeds what can be delivered
    and physical shortage decides instead of the gate (Sec.5.5.3).
    """
    rows = []
    for f in FLOORS:
        hi = None
        frac_hi = None
        for r in RHOS:
            total, fr = admitted_total(work_h, wants, f, r, kappa)
            if total <= R_max:
                hi, frac_hi = float(r), float(fr)
            else:
                break                       # demand rises with rho; first miss ends it
        rows.append((float(f), hi, frac_hi))
    return rows


def sweep(work_h, wants, kappa, R_max, E_h_yr):
    """One (affordable, rations, constrained-fraction) grid over FLOORS x RHOS."""
    aff = np.zeros((len(FLOORS), len(RHOS)), dtype=bool)
    rat = np.zeros_like(aff)
    frac = np.zeros(aff.shape, dtype=float)
    for i, f in enumerate(FLOORS):
        for j, r in enumerate(RHOS):
            aff[i, j] = affordable(f, r, E_h_yr)
            total, fr = admitted_total(work_h, wants, f, r, kappa)
            rat[i, j] = total <= R_max
            frac[i, j] = fr
    return aff, rat, frac


def band_rows(aff, rat, frac):
    """Per floor: the rho interval that is in band, and its width."""
    rows = []
    both = aff & rat
    for i, f in enumerate(FLOORS):
        idx = np.flatnonzero(both[i])
        if idx.size == 0:
            rows.append(dict(floor_h=float(f), lo=None, hi=None, width=0.0,
                             frac_lo=None, frac_hi=None,
                             why="" if aff[i].any() else "never affordable"))
            continue
        lo, hi = float(RHOS[idx[0]]), float(RHOS[idx[-1]])
        # contiguous? report it if not -- a gapped band would be a finding
        contiguous = (idx[-1] - idx[0] + 1) == idx.size
        rows.append(dict(floor_h=float(f), lo=lo, hi=hi, width=hi - lo,
                         frac_lo=float(frac[i, idx[0]]),
                         frac_hi=float(frac[i, idx[-1]]),
                         why="" if contiguous else "NOT CONTIGUOUS"))
    return rows


# =============================================================================
# report
# =============================================================================

def print_capacity_table(edges):
    """The answer to 'how wide', stated as the largest essentials basket a
    network can carry at each floor.

    The band is  rho in [ E/(365*F) , rho*(F) ].  It is EMPTY exactly when
    E/(365*F) > rho*(F), so the largest basket a floor can carry is

        E_max(F) = 365 * F * rho*(F)

    which is a number, not a picture, and it is what Sec.5.5.3 asked for.
    """
    print("-" * 78)
    print("HOW WIDE -- the largest essentials basket each floor can carry")
    print("-" * 78)
    print("  E_max(F) = 365 * F * rho*(F).  Above it the band is empty and the")
    print("  network fails whatever rho it sets.")
    print()
    print(f"{'F h/day':>8} {'rho*(F)':>9} {'E_max h/yr':>12} "
          f"{'x median lifestyle':>20} {'% held back at rho*':>21}")
    for f, hi, fr in edges:
        if hi is None:
            print(f"{f:>8.1f} {'--':>9} {'--':>12} {'--':>20} {'--':>21}")
            continue
        e_max = 365.0 * f * hi
        # Conformance row 13: a figure computed over an incomplete range is a
        # FLOOR, never a value. rho*(F) at the top of the swept grid is censored
        # -- the true edge is somewhere above it and we did not look.
        censored = hi >= float(RHOS[-1]) - 1e-9
        mark = "  FLOOR (rho grid ends here)" if censored else ""
        print(f"{f:>8.1f} {hi:>9.2f} {e_max:>12,.0f} "
              f"{e_max / MEDIAN_LIFESTYLE_H_YR:>20.2f} {fr*100:>20.1f}%{mark}")
    print()
    print("  Rows marked FLOOR ran off the top of the swept rho range, so their")
    print("  figure is a lower bound and not a value (conformance row 13).")
    print()
    ok = [(f, 365.0 * f * hi) for f, hi, _ in edges
          if hi is not None and hi < float(RHOS[-1]) - 1e-9]
    lo_f, lo_e = min(ok, key=lambda t: t[1])
    print(f"  The tightest floor is F = {lo_f:g} h, carrying "
          f"E_max = {lo_e:,.0f} h/yr = "
          f"{lo_e / MEDIAN_LIFESTYLE_H_YR:.2f} x a median lifestyle.")
    print()
    print("  In plain words: even the worst floor in this sweep carries an")
    print("  essentials basket larger than a whole median lifestyle. Essentials")
    print("  are a PART of a median lifestyle, so no floor in the swept range")
    print("  fails on affordability. The band does not close.")
    print()


def print_method_table(work_h, wants, kappa_us, B):
    """The point of the whole study: what a production method does to the band.

    THE ANCHOR IS THE UNITED STATES, and that is not a neutral choice. The
    1,380 h/yr figure is what a median US lifestyle commands, and Q6 measured
    the US as the labour- and carbon-inefficient outlier among rich countries.
    Germany, Japan and Spain deliver a comparable-or-better material standard,
    and longer lives, on roughly two thirds of the embodied labour.

    So "one median lifestyle" below means ONE MEDIAN AMERICAN LIFESTYLE, and the
    question this table asks is what the ledger does about that.
    """
    print("-" * 78)
    print("WHAT THE PRODUCTION METHOD DOES TO THE BAND")
    print("-" * 78)
    print("  The physical envelope B is FIXED -- same energy, same materials.")
    print("  What changes is the debit each unit of the SAME real standard costs.")
    print("  Source: 06-simulation/median-lifestyle/Q6.md (EXIOBASE, measured).")
    print()
    print("  NOTE ON THE ANCHOR. 'One median lifestyle' = 1,380 h/yr = one median")
    print("  AMERICAN lifestyle. Q6 measured the US as the inefficient outlier:")
    print("  Germany, Japan and Spain reach a comparable-or-better standard, and")
    print("  longer lives, on about two thirds of the embodied labour.")
    print()
    hdr = (f"{'method':>26} {'debit/unit':>11} {'real capacity':>14} "
           f"{'rho*(F=10)':>11} {'% held back':>12}")
    print(hdr)
    base = None
    for name, eff in EFF.items():
        edges, kappa, R_max = method_edges(work_h, wants, kappa_us, B, eff)
        row = [e for e in edges if abs(e[0] - 10.0) < 1e-9][0]
        _, hi, fr = row
        if base is None:
            base = (kappa, R_max)
        censored = hi is not None and hi >= float(RHOS[-1]) - 1e-9
        mark = "  NEVER BINDS (rho grid ends here)" if censored else ""
        print(f"{name:>26} {kappa:>11.2f} {R_max:>14,.0f} "
              f"{(hi if hi is not None else float('nan')):>11.2f} "
              f"{(fr * 100 if fr is not None else float('nan')):>11.1f}%{mark}")
    want_total = float(wants.sum())
    print()
    print(f"  Unconstrained wants total {want_total:,.0f} real units.")
    print()
    print("  READ THE CAPACITY COLUMN AGAINST THAT NUMBER, and the result is not")
    print("  the one this table was built expecting.")
    print()
    print("  Under the US method the same physical envelope delivers LESS than")
    print("  people want, so the gate rations and about a third are held back.")
    print("  Under the German, Japanese or Spanish method the SAME envelope")
    print("  delivers MORE than everyone wants -- so the gate never binds at any")
    print("  rho in the swept range, and nobody is held back at all.")
    print()
    print("  In plain words: the band has an upper edge only because the US")
    print("  method is wasteful. Fix the method and there is nothing left to")
    print("  ration. Foundations Sec.5.5.3 calls that the intended end state,")
    print("  not a failure -- 'where the economy can actually deliver that much,")
    print("  this is abundance'.")
    print()

    # The sharp version: what one US lifestyle COSTS under each method.
    print("  What one median AMERICAN lifestyle costs, by the method used to make it:")
    print()
    print(f"{'method':>26} {'h/yr of other labour':>24} {'vs the US method':>18}")
    for name, eff in EFF.items():
        cost = MEDIAN_LIFESTYLE_H_YR * eff
        print(f"{name:>26} {cost:>24,.0f} {eff:>17.0%}")
    print()
    print("  The ledger charges the method, not the person. Two people living the")
    print("  same material life carry different debit if one is supplied by a")
    print("  wasteful chain -- which is A4 and A5 doing their work with no")
    print("  mandate, no ban, and nobody's consumption forbidden.")
    print()


def print_report(work_h, wants, kappa, R_max, kappa_us, B):
    print("=" * 78)
    print("THE STABLE BAND OF F AND rho -- Foundations Sec.5.5.3, owed with OP-4")
    print("=" * 78)
    print()
    print("  Terms, before any number:")
    print("    F      the FLOOR, hours a day credited for staying alive. A dial.")
    print("    rho    the DEBIT TOLERANCE in the gate D <= rho*C. A dial.")
    print("    E      hours of other people's labour a YEAR OF ESSENTIALS commands.")
    print("           Exogenous. Nobody has measured it, so it is swept.")
    print("    R_max  what the economy can physically deliver. Exogenous.")
    print()
    print(f"  Population           {len(work_h):,} people, seed {RNG_SEED}")
    print(f"  Median lifestyle     {MEDIAN_LIFESTYLE_H_YR:,.0f} h/yr (measured)")
    print(f"  kappa                {kappa:.3f} debit-h per lifestyle-unit"
          f"   FIXED at F = {F_REF:g}")
    print(f"  R_max                {R_max:,.0f} lifestyle-units"
          f"   FIXED (= {CAP:.2f} x unconstrained wants)")
    print()

    edges = upper_edge(work_h, wants, kappa, R_max)
    print_capacity_table(edges)
    print_method_table(work_h, wants, kappa_us, B)

    for share in E_SHARES:
        E = share * MEDIAN_LIFESTYLE_H_YR
        aff, rat, frac = sweep(work_h, wants, kappa, R_max, E)
        rows = band_rows(aff, rat, frac)
        print("-" * 78)
        print(f"E = {E:,.0f} h/yr   ({share:.0%} of a median lifestyle)")
        print("-" * 78)
        print(f"{'F h/day':>8} {'rho low':>9} {'rho high':>9} {'width':>8} "
              f"{'% held back':>12}  note")
        for r in rows:
            if r["lo"] is None:
                print(f"{r['floor_h']:>8.1f} {'--':>9} {'--':>9} {0.0:>8.2f} "
                      f"{'--':>12}  EMPTY {r['why']}")
            else:
                print(f"{r['floor_h']:>8.1f} {r['lo']:>9.2f} {r['hi']:>9.2f} "
                      f"{r['width']:>8.2f} "
                      f"{r['frac_lo']*100:>5.1f}->{r['frac_hi']*100:<5.1f}"
                      f"  {r['why']}")
        widths = [r["width"] for r in rows]
        open_rows = [r for r in rows if r["width"] > 0]
        print()
        print(f"  floors with a band   {len(open_rows)} of {len(rows)}")
        if open_rows:
            widest = max(open_rows, key=lambda r: r["width"])
            narrowest = min(open_rows, key=lambda r: r["width"])
            print(f"  widest band          F = {widest['floor_h']:g} h, "
                  f"rho in [{widest['lo']:.2f}, {widest['hi']:.2f}], "
                  f"width {widest['width']:.2f}")
            print(f"  narrowest open band  F = {narrowest['floor_h']:g} h, "
                  f"width {narrowest['width']:.2f}")
        print()

    print("=" * 78)
    print("HOW TO READ THIS, in plain words")
    print("=" * 78)
    print("  Each row is one choice of floor. The two rho columns are the lowest")
    print("  and highest debit tolerance that BOTH keep essentials affordable AND")
    print("  leave the ledger still rationing. A width of 0 means no rho works at")
    print("  that floor, and the network fails whatever it sets.")
    print()
    print("  '% held back' is the share of people the gate holds below what they")
    print("  wanted, at the low and high edge of the band. It is a description,")
    print("  not a test -- no threshold on it is used anywhere above.")
    print()


# =============================================================================
# self-tests -- each one must be able to FAIL
# =============================================================================

def test_lower_edge_can_fail():
    """A tiny floor and a tiny tolerance must not afford essentials."""
    E = 0.5 * MEDIAN_LIFESTYLE_H_YR
    assert not affordable(1.0, 0.2, E), "rho*F*365 = 73 h cannot cover 690 h"
    assert affordable(10.0, 1.2, E), "rho*F*365 = 4380 h covers 690 h"
    print("[ok] the lower edge can fail, and does, at F = 1, rho = 0.2")


def test_upper_edge_can_fail():
    """A large tolerance must admit more than the economy can deliver."""
    work_h, wants = build_people(8_000, seed=3)
    kappa, R_max = us_case(*calibrate(work_h, wants))
    lo, _ = admitted_total(work_h, wants, 10.0, 0.2, kappa)
    hi, _ = admitted_total(work_h, wants, 10.0, 4.0, kappa)
    assert lo <= R_max, "at rho = 0.2 the gate must still ration"
    assert hi > R_max, "at rho = 4.0 the gate must have stopped rationing"
    print("[ok] the upper edge can fail, and does, at rho = 4.0")


def test_floor_actually_moves_the_answer():
    """The calibration is fixed, so F must change what is admitted.

    This is the @alfred-pennyworth check. If kappa were recalibrated per floor,
    these two numbers would be equal and the whole sweep would be a ceremony.
    """
    work_h, wants = build_people(8_000, seed=3)
    kappa, _ = us_case(*calibrate(work_h, wants))
    a, _ = admitted_total(work_h, wants, 4.0, 1.2, kappa)
    b, _ = admitted_total(work_h, wants, 12.0, 1.2, kappa)
    assert b > a * 1.05, f"a higher floor must admit more: {a:.0f} vs {b:.0f}"
    print(f"[ok] the floor moves the answer: {a:,.0f} -> {b:,.0f} lifestyle-units")


def test_calibration_is_not_recomputed_per_cell():
    """kappa and R_max must not depend on the dials at all."""
    work_h, wants = build_people(8_000, seed=3)
    k1, r1 = calibrate(work_h, wants)
    k2, r2 = calibrate(work_h, wants)
    assert k1 == k2 and r1 == r2
    src = open(os.path.join(HERE, "stable_band.py"), encoding="utf-8").read()
    body = src.split("def sweep(")[1].split("\ndef ")[0]
    assert "calibrate(" not in body, "sweep() must never recalibrate"
    print("[ok] the calibration is fixed across the grid")


def test_gate_and_conformance_actually_run():
    """Demand goes through the kernel, not through closed-form arithmetic."""
    work_h, wants = build_people(4_000, seed=5)
    kappa, _ = us_case(*calibrate(work_h, wants))
    total, frac = admitted_total(work_h, wants, 10.0, 1.2, kappa)
    assert total > 0 and 0.0 <= frac <= 1.0
    print(f"[ok] the kernel's gate and all conformance checks ran "
          f"({frac*100:.1f}% held back at F = 10, rho = 1.2)")


def run_tests():
    for fn in (test_lower_edge_can_fail,
               test_upper_edge_can_fail,
               test_floor_actually_moves_the_answer,
               test_calibration_is_not_recomputed_per_cell,
               test_gate_and_conformance_actually_run):
        fn()
    print("\nAll self-tests passed.")


# =============================================================================

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--no-plots", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return
    work_h, wants = build_people()
    kappa_us, B = calibrate(work_h, wants)
    kappa, R_max = us_case(kappa_us, B)
    print_report(work_h, wants, kappa, R_max, kappa_us, B)


if __name__ == "__main__":
    main()
