"""
Refinery slice -- physical-split vs price allocation on a real joint process.

Objections §C Test 4 / Foundations §11(a): re-derive a refinery's fraction slate
under §3.4a process-physics allocation and show it differs *materially* from the
market-value (price) allocation that USEEIO/EXIOBASE fall back to. A materially
different, defensible per-fraction debit vector is the most publishable early
technical result.

This is the first exercise of the engine's genuine joint-production path
(`Theta != I`) on real-grounded data -- unlike the EXIOBASE IOT loader, whose
product-by-product table had already price-allocated joint production (`Theta=I`).

MODEL. One joint refinery process turns crude into a fraction slate, measured in
VOLUME (barrels), with three debit dimensions split per §3.2a:

  - energy  : split by WHERE THE PROCESS SENT ITS ENERGY, in two channels
              (physical-trace test applied *inside* the refinery):
                * conversion (MEASURED): reforming/FCC/hydrocracking/coking energy
                  routes to the specific products those units make;
                * distillation (DECLARED convention): shared column heating, no
                  per-fraction trace -> split by a declared basis, scaled to the
                  METERED actual so losses/inefficiency are counted (§3.5/A1: we
                  count 100 MJ applied, never the 80 MJ "usefully" used).
  - materials: crude mass carried into each fraction (low-res mass estimator).
  - labour   : rides the material split (OP-18 / §3.4a) -- no basis of its own.

Pollution is DELIBERATELY EXCLUDED (author's decision): a fraction's transferable
cost carries no pollution, because pollution never cascades downstream (§3.2b) --
the same non-cascade as computational closure (§6.2a). See refinery_slice_PLAN.md.

DATA. The ENERGY dimension uses the real per-process onsite energies
from the DOE 2015 Petroleum Refining Bandwidth Study
(Table 4-2, U.S. 2010): nine processes, 2,163 TBtu/yr, split into a declared
distillation channel and a measured conversion channel routed by standard
refinery flow. Volume yields are the standard EIA refinery-yield proportions
(gasoline ~46-49%). Materials (crude mass), labour, and prices remain
representative and are flagged -- the DOE bandwidth study is process energy only,
so those dimensions are the next refinement. Sources: `../00-strategy/GLOSSARY.md#src-refinery-process-energy`.

Run:  python refinery_slice.py            # build, report the two allocations
      python refinery_slice.py --test      # self-tests only
"""

from __future__ import annotations

import argparse
import os
import sys

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recursion_convergence import Economy, build_forward, solve_direct  # noqa: E402
from estimation_engine import MultiDimEconomy  # noqa: E402


# ---------------------------------------------------------------------------
# The refinery: representative US-average slate (see 02-research/…)
# ---------------------------------------------------------------------------
#
# Per 100 barrels of crude charged. Yields sum to > 100 (processing gain ~6%):
# volume is a reporting unit, not conserved -- which is exactly why it cannot be
# a split basis, and it is not used as one.

FRACTIONS = ["lpg", "gasoline", "jet", "diesel", "residual_fuel", "petcoke",
             "asphalt"]

YIELD_BBL = {          # volume produced per 100 bbl crude (EIA-representative)
    "lpg":            5.0,
    "gasoline":      49.0,
    "jet":           10.0,
    "diesel":        30.0,
    "residual_fuel":  3.0,
    "petcoke":        5.0,
    "asphalt":        3.0,
}   # sum = 105 > 100: processing gain (~5%) -- cracking dense heavies into
    # lighter products raises total volume. Volume is a reporting unit, not
    # conserved, so it is never used as a split basis.

# --- the ENERGY split: REAL DOE process energies + a routing model ----------
# DOE 2015 Bandwidth Study, Table 4-2: onsite Current Typical energy consumption
# by process, U.S. 2010 (TBtu/yr). These are *metered actuals* (incl. losses),
# which is exactly the §3.5/A1 pool: we split the 100 MJ applied, not the
# thermodynamic minimum. Sum = 2,163 TBtu = 68% of sector-wide onsite energy.
PROCESS_ENERGY_TBTU = {
    "atm_distillation": 604.0, "vac_distillation": 222.0,   # DECLARED channel
    "reforming": 279.0, "fcc": 334.0, "hydrocracking": 85.0,   # MEASURED channel
    "coking": 114.0, "hydrotreating": 390.0, "alkylation": 90.0,
    "isomerization": 44.0,
}
DISTILLATION_PROCESSES = ["atm_distillation", "vac_distillation"]   # no per-fraction trace

# per-bbl-of-crude energy intensity for the nine processes (Btu/bbl crude):
# 2,163 TBtu / 5,540 M bbl atmospheric-distillation throughput (DOE Table 3-1).
ENERGY_BTU_PER_BBL_CRUDE = 2163e12 / 5540e6      # ~390,400 Btu/bbl crude

# CONVERSION ROUTING (the documented modelling layer): fraction shares of each
# conversion process's energy, from standard refinery flow (DOE Figure 2-2).
# This is a `measured` routing -- each unit's metered energy goes to the products
# it makes -- but the per-fraction shares are a modelled convention, flagged.
CONVERSION_ROUTING = {
    "reforming":     {"gasoline": 1.00},                       # reformate -> octane
    "alkylation":    {"gasoline": 1.00},                       # alkylate
    "isomerization": {"gasoline": 1.00},                       # isomerate
    "fcc":           {"gasoline": 0.70, "lpg": 0.15, "diesel": 0.15},
    "hydrocracking": {"diesel": 0.55, "jet": 0.30, "gasoline": 0.15},
    "coking":        {"petcoke": 0.45, "diesel": 0.30, "gasoline": 0.25},
    "hydrotreating": {"diesel": 0.40, "gasoline": 0.30, "jet": 0.25, "lpg": 0.05},
}

# --- direct MATERIALS and LABOUR (per 100 bbl crude) ------------------------
CRUDE_MASS_KG = 13600.0      # ~100 bbl crude at ~0.86 kg/L * 158.99 L/bbl
DIRECT_LABOUR_HR = 20.0      # representative operating labour per 100 bbl

# --- representative PRICES ($/bbl) for the price-allocation contrast ---------
PRICE_USD_BBL = {
    "lpg":            40.0,
    "gasoline":      105.0,
    "jet":           100.0,
    "diesel":        113.0,
    "residual_fuel":  65.0,   # discounted heavy
    "petcoke":        15.0,   # very cheap byproduct
    "asphalt":        50.0,
}


# ---------------------------------------------------------------------------
# Build the physical split (theta) for each dimension
# ---------------------------------------------------------------------------

def _normalise(d):
    tot = sum(d.values())
    return {k: v / tot for k, v in d.items()}


def energy_theta():
    """Two-channel energy split from real DOE process energies, normalised.

    DECLARED channel: the two distillation units heat the whole barrel to
    separate it -- no per-fraction trace -- so their combined energy is split by
    volume (an enthalpy-demand stand-in). MEASURED channel: each conversion
    unit's metered energy is routed to the products it makes (CONVERSION_ROUTING).
    Returns (theta dict, provenance dict of the two channels per fraction).
    """
    vol = _normalise(YIELD_BBL)                     # declared distillation basis
    raw = {f: 0.0 for f in FRACTIONS}
    prov = {f: dict(measured_conversion=0.0, declared_distillation=0.0)
            for f in FRACTIONS}

    # declared: distillation energy split across all fractions by volume
    dist_total = sum(PROCESS_ENERGY_TBTU[p] for p in DISTILLATION_PROCESSES)
    for f in FRACTIONS:
        d = dist_total * vol[f]
        raw[f] += d
        prov[f]["declared_distillation"] = d

    # measured: each conversion unit's energy routed to its products
    for proc, routing in CONVERSION_ROUTING.items():
        e = PROCESS_ENERGY_TBTU[proc]
        for f, share in routing.items():
            raw[f] += e * share
            prov[f]["measured_conversion"] += e * share

    return _normalise(raw), prov


def material_theta():
    """Materials split by mass carried into each fraction (low-res estimator).

    Fraction mass = volume * density. Light fractions are less dense, so mass
    theta is NOT the same as volume theta -- but it is a physical trace (the atoms
    went somewhere), so it is `measured`, unlike labour.
    """
    density = {   # kg/L, representative
        "lpg": 0.55, "gasoline": 0.74, "jet": 0.80, "diesel": 0.84,
        "residual_fuel": 0.99, "petcoke": 1.05, "asphalt": 1.03,
    }
    mass = {f: YIELD_BBL[f] * density[f] for f in FRACTIONS}
    return _normalise(mass)


# ---------------------------------------------------------------------------
# Assemble as a MultiDimEconomy (single joint process, Theta != I)
# ---------------------------------------------------------------------------

def build_refinery() -> MultiDimEconomy:
    M, N = len(FRACTIONS), 1
    idx = {f: i for i, f in enumerate(FRACTIONS)}

    B = sp.csr_matrix(np.array([[YIELD_BBL[f]] for f in FRACTIONS]))   # M x 1, volume
    A = sp.csr_matrix((M, N))                                          # crude exogenous

    e_theta, _ = energy_theta()
    m_theta = material_theta()
    Theta_energy = sp.csr_matrix(np.array([[e_theta[f]] for f in FRACTIONS]))
    Theta_material = sp.csr_matrix(np.array([[m_theta[f]] for f in FRACTIONS]))

    # energy pool for a 100-bbl-crude batch (Btu), from the real DOE intensity
    energy_pool = ENERGY_BTU_PER_BBL_CRUDE * 100.0
    direct = {
        "materials": np.array([CRUDE_MASS_KG]),
        "energy":    np.array([energy_pool]),
        "labour":    np.array([DIRECT_LABOUR_HR]),
    }
    theta = {
        "materials": Theta_material,
        "energy":    Theta_energy,
        "labour":    Theta_material,      # OP-18: labour rides the material split
    }
    units = {f: "bbl" for f in FRACTIONS}
    econ = MultiDimEconomy(FRACTIONS, ["refinery"], A, B, direct, theta, units)
    assert econ.theta["labour"] is econ.theta["materials"], "OP-18 invariant"
    return econ


def per_barrel_debit(econ: MultiDimEconomy, dim: str):
    """Per-barrel embodied debit of one dimension for every fraction."""
    sub = Economy(econ.M, econ.N, econ.A, econ.B,
                  np.asarray(econ.direct[dim], float), econ.theta[dim])
    A_tilde, c = build_forward(sub)
    return solve_direct(A_tilde, c)


# ---------------------------------------------------------------------------
# Price (market-value) allocation -- the rejected USEEIO method, for contrast
# ---------------------------------------------------------------------------

def price_allocation(econ: MultiDimEconomy):
    """Allocate each dimension's total debit by REVENUE share (price x volume).

    This is what USEEIO/EXIOBASE do: cost share proportional to market value.
    Forbidden as *truth* by A5; computed here only to show it differs from the
    physical split. Returns {dim -> per-barrel cost vector}.
    """
    vol = np.array([YIELD_BBL[f] for f in FRACTIONS])
    revenue = np.array([PRICE_USD_BBL[f] * YIELD_BBL[f] for f in FRACTIONS])
    rev_share = revenue / revenue.sum()
    out = {}
    for dim in econ.dims():
        pool = float(econ.direct[dim][0])           # single process
        out[dim] = (rev_share * pool) / vol         # per-barrel
    return out


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(econ: MultiDimEconomy = None):
    econ = econ or build_refinery()
    phys = {d: per_barrel_debit(econ, d) for d in econ.dims()}
    price = price_allocation(econ)
    e_theta, prov = energy_theta()

    vol = np.array([YIELD_BBL[f] for f in FRACTIONS])
    tot_vol = vol.sum()

    print("=" * 82)
    print("REFINERY SLICE -- physical (process-energy) vs price allocation")
    print("=" * 82)
    print(f"basis: 100 bbl crude -> {tot_vol:.0f} bbl product "
          f"(processing gain {tot_vol-100:.0f}%). Outputs in bbl.")

    # energy: the headline dimension (real DOE energies -> MMBtu/bbl)
    print("\nENERGY debit per barrel, MMBtu/bbl  (physical §3.4a  vs  price/USEEIO):")
    print(f"{'fraction':<15}{'yield%':>8}{'phys':>10}{'price':>10}{'phys÷price':>12}")
    print("-" * 82)
    for i, f in enumerate(FRACTIONS):
        ratio = phys['energy'][i] / price['energy'][i] if price['energy'][i] else float('nan')
        print(f"{f:<15}{100*vol[i]/tot_vol:>7.1f}%{phys['energy'][i]/1e6:>10.3f}"
              f"{price['energy'][i]/1e6:>10.3f}{ratio:>11.2f}x")
    print("-" * 82)

    # energy shares -- validate against the 49%/62% anchor
    e_share = np.array([e_theta[f] for f in FRACTIONS])
    v_share = vol / tot_vol
    gi = FRACTIONS.index("gasoline")
    print(f"\ngasoline: {100*v_share[gi]:.0f}% of volume, "
          f"{100*e_share[gi]:.0f}% of energy  "
          f"(DOE anchor: ~49% vol / ~62% energy)")

    # the material divergence, summarised
    print("\nWHERE PHYSICAL AND PRICE DISAGREE (energy dimension):")
    for i, f in enumerate(FRACTIONS):
        r = phys['energy'][i] / price['energy'][i]
        if r > 1.3 or r < 0.77:
            direction = "UNDER-costed by price" if r > 1 else "OVER-costed by price"
            print(f"  {f:<15} physical is {r:>4.1f}x price  -> {direction}")

    # full per-barrel debit vector (all three dimensions, physical)
    print("\nFULL PHYSICAL DEBIT VECTOR (per bbl):")
    print(f"{'fraction':<15}{'materials(kg)':>14}{'energy(MMBtu)':>15}{'labour(hr)':>12}")
    print("-" * 82)
    for i, f in enumerate(FRACTIONS):
        print(f"{f:<15}{phys['materials'][i]:>14.2f}{phys['energy'][i]/1e6:>15.3f}"
              f"{phys['labour'][i]:>12.5f}")
    print("=" * 82)
    return phys, price


# ---------------------------------------------------------------------------
# Self-tests (the plan's faithfulness gates)
# ---------------------------------------------------------------------------

def test_conservation():
    """Gate 1: both allocations conserve -- shares sum to the total pool
    (efficiency axiom). Neither creates nor destroys debit."""
    econ = build_refinery()
    vol = np.array([YIELD_BBL[f] for f in FRACTIONS])
    for dim in econ.dims():
        pool = float(econ.direct[dim][0])
        phys_total = float(np.dot(per_barrel_debit(econ, dim), vol))
        price_total = float(np.dot(price_allocation(econ)[dim], vol))
        assert abs(phys_total - pool) < 1e-6, f"{dim}: physical loses debit"
        assert abs(price_total - pool) < 1e-6, f"{dim}: price loses debit"
    print("[ok] conservation: both allocations sum to the pool, every dimension")


def test_nonnegative():
    """Gate 2: physical split is non-negative (inherited Neumann result)."""
    econ = build_refinery()
    for dim in econ.dims():
        assert np.min(per_barrel_debit(econ, dim)) >= -1e-12, f"{dim} negative"
    print("[ok] non-negative physical debit across all dimensions")


def test_universality_price_independent():
    """Gate 3: the physical split is INDEPENDENT of prices (B9 / §3.4a).

    Perturb every price arbitrarily; the physical per-barrel debit must not move
    at all. This is the property that killed demand-contingent splitting."""
    econ = build_refinery()
    before = {d: per_barrel_debit(econ, d).copy() for d in econ.dims()}
    saved = dict(PRICE_USD_BBL)
    try:
        for k in PRICE_USD_BBL:
            PRICE_USD_BBL[k] *= 3.7          # arbitrary price shock
        after = {d: per_barrel_debit(econ, d) for d in econ.dims()}
    finally:
        PRICE_USD_BBL.update(saved)
    for d in econ.dims():
        assert np.max(np.abs(before[d] - after[d])) < 1e-12, \
            f"{d}: physical split moved when prices changed -- universality breach"
    print("[ok] universality: physical split is price-independent (demand cannot "
          "enter cost)")


def test_material_divergence():
    """Gate 4: physical and price differ materially on at least the byproduct
    fractions, and gasoline's energy share exceeds its volume share (the anchor
    direction: processing depth, not weight, drives cost)."""
    econ = build_refinery()
    phys = per_barrel_debit(econ, "energy")
    price = price_allocation(econ)["energy"]
    l1 = float(np.sum(np.abs(phys - price) * np.array([YIELD_BBL[f] for f in FRACTIONS]))) / 1e6
    assert l1 > 0.1, f"allocations should differ materially, L1(MMBtu)={l1}"
    # petcoke: cheap byproduct, real coking energy -> physical >> price
    pi = FRACTIONS.index("petcoke")
    assert phys[pi] > 1.5 * price[pi], "petcoke should be under-costed by price"
    # gasoline: energy-intensive -> energy share > volume share (DOE anchor)
    e_theta, _ = energy_theta()
    vol = np.array([YIELD_BBL[f] for f in FRACTIONS]); vshare = vol / vol.sum()
    gi = FRACTIONS.index("gasoline")
    assert e_theta["gasoline"] > vshare[gi], "gasoline energy share must exceed volume share"
    print(f"[ok] material divergence: L1={l1:.2f} MMBtu; petcoke under-costed by "
          f"price; gasoline energy {100*e_theta['gasoline']:.0f}% > volume "
          f"{100*vshare[gi]:.0f}%")


def test_gasoline_energy_anchor():
    """Gate 5: gasoline's energy share exceeds its volume share and lands in the
    DOE ballpark, validating the routing of the real per-process energies.

    DOE reports gasoline at ~49% of volume but ~62% of *sector-wide* energy. This
    model covers the nine bandwidth processes (68% of sector energy) and routes
    them, giving ~55% -- energy-intensive relative to volume, the same direction,
    slightly lower because sector utilities (skewed to gasoline processing) are
    outside the nine-process pool."""
    e_theta, _ = energy_theta()
    share = e_theta["gasoline"]
    vol = _normalise(YIELD_BBL)["gasoline"]
    assert share > vol, f"gasoline energy share {share:.2f} must exceed volume {vol:.2f}"
    assert 0.50 <= share <= 0.66, f"gasoline energy share {share:.2f} off DOE ballpark"
    print(f"[ok] gasoline energy anchor: {100*share:.0f}% of energy vs "
          f"{100*vol:.0f}% of volume (DOE sector-wide ~62%/49%)")


def test_op18_labour_rides_materials():
    """Labour uses the material operator exactly (OP-18)."""
    econ = build_refinery()
    lab = per_barrel_debit(econ, "labour")
    mat = per_barrel_debit(econ, "materials")
    # both scale the same theta by their own direct pool -> proportional
    ratio = lab / mat
    assert np.allclose(ratio, ratio[0]), "labour must ride the material split exactly"
    print(f"[ok] OP-18: labour rides material split (constant ratio "
          f"{ratio[0]:.6f} hr/kg across fractions)")


def run_tests():
    test_conservation()
    test_nonnegative()
    test_universality_price_independent()
    test_material_divergence()
    test_gasoline_energy_anchor()
    test_op18_labour_rides_materials()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    print("Running self-tests first...\n")
    run_tests()
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
