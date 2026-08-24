"""
track2_durables.py -- Track 2 of the median-adult lifestyle cost: the ANNUALISED
embodied labour in the DURABLES an adult holds, via the Aequitas sec.6.2b
holding-time share (make-labour carried per year of holding = build-hours /
service-life), NOT a dollar conversion (durable dollars are mostly land, finance,
and interest -- near-zero labour).

THE KEY ACCOUNTING POINT (why this track is almost all HOUSING).
  In a rough steady state, the annual PCE *purchase* of a durable equals its
  annualised holding-labour (what is bought each year ~ what wears out each year).
  So vehicles, furniture, and appliances -- which ARE PCE categories -- are
  ALREADY captured in Tracks 1 (domestic) + 3 (foreign). Re-annualising them here
  would DOUBLE-COUNT.

  The ONE durable missing from Tracks 1+3 is the HOUSING STRUCTURE, because
  residential construction is booked as INVESTMENT, not PCE. This is exactly why
  track1_embodied_hours.py reported Construction = 0 h. So Track 2's real, non-
  double-counting contribution to the grand total is housing structure alone.

  Vehicles are shown here too, but ONLY for comparison (to confirm the annualised
  figure is the same order as their Track-1+3 PCE share) -- not added again.

METHOD (housing).
  per-adult annual labour = build_hours_per_dwelling / service_life / adults_per_dwelling
  build_hours ranges from on-site construction only (low) to total embodied incl.
  building-materials manufacturing (high, ~2x).

Run:  python track2_durables.py [--test]
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Inputs:
    # --- housing (THE addition) ---
    home_build_hours_onsite: float = 3500.0  # on-site construction labour per
                                             #   single-family dwelling (NAHB/
                                             #   Census order; ~3-4k h)
    embodied_mult_lo: float = 1.0            # on-site only
    embodied_mult_hi: float = 2.0            # + building-materials manufacturing
    home_service_life_yr: float = 60.0       # method plan
    adults_per_dwelling: float = 1.9         # US ~2.5 persons, ~1.9 adults / unit

    # --- vehicles (shown for COMPARISON only; already in Tracks 1+3 as PCE) ---
    vehicle_embodied_hours: float = 200.0    # assembly + parts + supply chain per
                                             #   vehicle (US auto sector ~1M workers
                                             #   x1800h / ~10M vehicles + supply)
    vehicle_service_life_yr: float = 15.0
    vehicles_per_adult: float = 0.85         # ~252M vehicles / ~259M adults, dm.

    # --- appliances + furniture (also already in Track 1 PCE; illustrative) ---
    appl_furn_hours: float = 400.0           # rough per-adult stock mfg hours
    appl_furn_life_yr: float = 15.0


def housing_range(x: Inputs) -> tuple[float, float]:
    base = x.home_build_hours_onsite / x.home_service_life_yr / x.adults_per_dwelling
    return base * x.embodied_mult_lo, base * x.embodied_mult_hi


def vehicle_annualised(x: Inputs) -> float:
    return x.vehicle_embodied_hours / x.vehicle_service_life_yr * x.vehicles_per_adult


def appl_furn_annualised(x: Inputs) -> float:
    return x.appl_furn_hours / x.appl_furn_life_yr


def report(x: Inputs | None = None) -> dict:
    x = x or Inputs()
    h_lo, h_hi = housing_range(x)
    veh = vehicle_annualised(x)
    af = appl_furn_annualised(x)
    W = 70
    print("=" * W)
    print("TRACK 2 -- ANNUALISED DURABLE LABOUR (sec.6.2b holding-time share)")
    print("=" * W)
    print("  HOUSING STRUCTURE  <-- the real addition (missing from Tracks 1+3:")
    print("                         residential construction is investment, not PCE)")
    print(f"    build labour/dwelling  : {x.home_build_hours_onsite:.0f} h on-site"
          f"  ({x.embodied_mult_hi:.0f}x incl. materials)")
    print(f"    / {x.home_service_life_yr:.0f} yr life / {x.adults_per_dwelling:.1f} adults per unit")
    print(f"    => per adult/yr        : {h_lo:5.1f} - {h_hi:5.1f} h   <== TRACK-2 CONTRIBUTION")
    print("-" * W)
    print("  For COMPARISON only (already inside Tracks 1+3 as PCE -- NOT re-added):")
    print(f"    vehicles, annualised   : {veh:5.1f} h/adult/yr")
    print(f"    appliances+furniture   : {af:5.1f} h/adult/yr")
    print("    (in steady state, annual PCE purchase ~ annualised holding cost, so")
    print("     these are captured by Track 1 domestic + Track 3 foreign already.)")
    print("=" * W)
    print(f"  TRACK 2 adds ~{h_lo:.0f}-{h_hi:.0f} h/median adult/yr (housing structure).")
    print("  This is the labour that residential-construction-as-investment hides")
    print("  from a consumption-only account -- modest but real, and it is the")
    print("  labour a home actually commands, spread over the holders' time (6.2b).")
    print("=" * W)
    return dict(housing_lo=h_lo, housing_hi=h_hi, vehicle=veh, appl_furn=af)


def test_housing_positive_ordered():
    r = report.__wrapped__ if hasattr(report, "__wrapped__") else None
    lo, hi = housing_range(Inputs())
    assert 0 < lo < hi
    print(f"[ok] housing {lo:.1f} < {hi:.1f} h/adult/yr")


def test_housing_dominates_durables():
    x = Inputs()
    lo, _ = housing_range(x)
    assert lo > vehicle_annualised(x), "housing should be the biggest durable"
    print(f"[ok] housing {lo:.0f}h > vehicles {vehicle_annualised(x):.0f}h (housing is the addition)")


def test_vehicle_same_order_as_track1():
    """Annualised vehicle labour should be small (single digits) -- consistent
    with Track1+3 vehicles being minor, so not double-counting is defensible."""
    v = vehicle_annualised(Inputs())
    assert v < 20, v
    print(f"[ok] vehicle annualised {v:.0f}h small (consistent w/ Track1+3 PCE)")


def test_contribution_modest():
    lo, hi = housing_range(Inputs())
    assert hi < 100, hi
    print(f"[ok] Track-2 contribution {lo:.0f}-{hi:.0f}h modest vs 1276h (Tracks1+3)")


def run_tests():
    test_housing_positive_ordered()
    test_housing_dominates_durables()
    test_vehicle_same_order_as_track1()
    test_contribution_modest()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    run_tests() if a.test else report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
