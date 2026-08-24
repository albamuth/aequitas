"""
median_lifestyle.py -- What does the median US standard of living COST in Aequitas
credit (i.e. embodied human labour-hours)?  The real-world anchor for the
disparity-ceiling proof (queue #8, Part 3).

WHY THIS QUANTITY.  Aequitas credit is human time (A2).  So "the cost of a
lifestyle" is the number of person-hours of labour that lifestyle *commands* --
the hours embodied in everything a person consumes.  This is directly comparable
to what a person can supply (<= 24 h/day, A3) and therefore situates a real
lifestyle inside the disparity band [floor, 24/F * floor].

WHAT COUNTS (locked with the author, 2026-08-09; see three-bucket rule below):
  Bucket 1 -- EMBODIED LABOUR + MATERIAL of everything held/consumed, INCLUDING
              electricity's generation-labour, grid, and fuel-as-material.
              *** This is the headline: pure hours, the credit comparison. ***
  Bucket 2 -- the consumer's OWN combustion + waste only: vehicle fuel, on-site
              gas (furnace/stove), garbage.  Reported in physical units; the
              hours conversion is a mitigation-cost weighting choice (OP-10), so
              it is NOT folded into the bucket-1 headline.
  Bucket 3 -- ALL upstream production pollution (power-plant emissions, farm
              runoff, mine tailings, factory emissions) -- EXCLUDED.  Under
              Foundations Sec.3.2b it is permanent on each *producer*, never on
              the consumer.  Electricity delivered to the home carries only its
              material + labour, not its generation pollution.

METHOD (bucket 1), top-down and deliberately transparent:
  total US labour-hours/yr  x  (share going to household consumption)
      -> mean embodied consumption-hours per capita (DOMESTIC labour only)
  x  import-labour uplift   -> add the foreign hours embodied in imports
  x  median/mean ratio      -> the MEDIAN bundle (consumption < income in spread)

Every input is a named constant with a source and is easy to override.  The point
is not a precise number -- it is the ORDER OF MAGNITUDE and how it sits against
today's income spread (10^4-10^5 x) versus the Aequitas ceiling (~10^1 x).

HONESTY.  The import-labour uplift is the biggest uncertainty and is exactly what
a real EXIOBASE multi-region solve would pin down (foreign labour-hours per unit
final demand).  `exiobase_loader.py` already reaches that structure; the employ-
ment satellite is the one-call swap when full EXIOBASE is downloaded.  Until then
this reports a RANGE (domestic-only lower bound -> import-adjusted central).

Run:  python median_lifestyle.py
      python median_lifestyle.py --test
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Inputs -- each a documented, overridable constant with a source
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Inputs:
    # --- US macro (headline, bucket 1) ---
    population: float = 335e6            # US resident pop ~2023 (Census, ~334.9M)
    employed: float = 161e6             # employed persons ~2023 (BLS CPS, ~161M)
    avg_annual_hours: float = 1_800.0   # avg annual hours / worker (OECD US ~1,811)
    pce_share_of_labour: float = 0.68   # PCE ~= 68% of GDP; used as labour share
                                        #   flowing to household consumption
    # Imports embody FOREIGN hours at a higher hours/$ than domestic output
    # (lower-wage, more labour-intensive).  Uplift multiplies domestic-consumption
    # hours to approximate total (domestic + import) embodied labour.
    #   1.00 = domestic-only hard lower bound
    #   1.4-1.7 = plausible central band (large US import content, high hours/$)
    import_uplift_lo: float = 1.00
    import_uplift_hi: float = 1.60

    # Consumption is LESS unequal than income (consumption Gini ~0.3-0.4 vs income
    # ~0.48).  Median household expenditure ~= 0.8 x mean (BLS CE Survey shape).
    median_over_mean: float = 0.80

    # --- Aequitas disparity band (for situating the result) ---
    self_care_floor_h_day: float = 10.0  # F: credited self-care service, h/day
                                         #   (~8 h sleep + hygiene/food; Sec.6.1b)
    rho: float = 1.5                     # tolerance ratio D <= rho*C (exogenous
                                         #   "prime-rate" dial; Aequitas is agnostic)

    # --- Bucket 2: the consumer's OWN combustion + waste (physical units) ---
    own_vehicle_co2_t: float = 4.6       # avg passenger vehicle, t CO2/yr (EPA)
    own_home_fuel_co2_t: float = 1.5     # on-site gas heating/stove, t CO2/capita
                                         #   (EIA residential direct fuel, approx)
    own_msw_kg: float = 811.0            # municipal solid waste, kg/person/yr
                                         #   (EPA ~4.9 lb/person/day)

    # --- Representative physical footprints (the material/energy DISPARITY the
    #     rho*C cap compresses).  Illustrative multipliers, flagged as such. ---
    primary_energy_gj: float = 290.0     # US primary energy/capita, GJ/yr
                                         #   (EIA ~93 quads / 335M ~ 290 GJ)
    material_footprint_t: float = 22.0   # raw material consumption/capita, t/yr
                                         #   (OECD/UNEP, US high end)
    toptail_footprint_mult: float = 30.0 # a high-net-worth lifestyle (multiple
                                         #   estates, jet, yacht, staff) embodies
                                         #   ~10-100x median energy+materials;
                                         #   30x is a mid illustrative point


# ---------------------------------------------------------------------------
# Bucket 1 -- embodied labour-hours in the median consumption bundle
# ---------------------------------------------------------------------------

def total_labour_hours(x: Inputs) -> float:
    """Total US labour-hours supplied per year (domestic)."""
    return x.employed * x.avg_annual_hours


def mean_consumption_hours_domestic(x: Inputs) -> float:
    """Mean embodied DOMESTIC labour-hours per capita, household consumption."""
    consumption_hours = total_labour_hours(x) * x.pce_share_of_labour
    return consumption_hours / x.population


def median_bundle_hours(x: Inputs) -> tuple[float, float]:
    """(lower-bound, central) embodied labour-hours for the MEDIAN US bundle/yr.

    lower = domestic labour only (import_uplift = lo)
    central = import-adjusted (import_uplift = hi)
    Both scaled from mean to median by `median_over_mean`.
    """
    mean_dom = mean_consumption_hours_domestic(x)
    lo = mean_dom * x.import_uplift_lo * x.median_over_mean
    hi = mean_dom * x.import_uplift_hi * x.median_over_mean
    return lo, hi


# ---------------------------------------------------------------------------
# Aequitas disparity band -- where does the median sit?
# ---------------------------------------------------------------------------

def self_care_credit_per_capita(x: Inputs) -> float:
    """Credit each living human earns for self-care alone, h/yr (F * 365)."""
    return x.self_care_floor_h_day * 365.0


def total_self_care_credit(x: Inputs) -> float:
    """Whole-population self-care credit, h/yr."""
    return x.population * self_care_credit_per_capita(x)


def accrual_ceiling_ratio(x: Inputs) -> float:
    """The disparity ceiling on credit ACCRUAL RATE, 24/F -- rho-INDEPENDENT.

    This bounds the rate at which any two people accrue credit (max worker 24 h/day
    vs min-liver's self-care floor F).  It is a labour-TIME result and is clean.
    The disparity in full-vector *consumption* is a separate question that needs
    the material/energy dimensions (see note in report()).
    """
    return 24.0 / x.self_care_floor_h_day


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def report(x: Inputs | None = None) -> dict:
    x = x or Inputs()

    tot = total_labour_hours(x)
    per_cap_worked = tot / x.population
    mean_dom = mean_consumption_hours_domestic(x)
    med_lo, med_hi = median_bundle_hours(x)
    sc_pc = self_care_credit_per_capita(x)
    sc_tot = total_self_care_credit(x)
    sc_over_prod = sc_tot / tot
    ratio = accrual_ceiling_ratio(x)
    # median LABOUR bundle as a fraction of self-care credit alone
    med_frac_lo = med_lo / sc_pc
    med_frac_hi = med_hi / sc_pc

    W = 76
    print("=" * W)
    print("MEDIAN US STANDARD OF LIVING, IN AEQUITAS CREDIT (embodied labour-hours)")
    print("=" * W)
    print("Bucket 1 -- embodied LABOUR a lifestyle commands (the clean credit figure)")
    print("-" * W)
    print(f"  US total labour supplied      : {tot/1e9:6.1f} billion h/yr")
    print(f"  ... per capita (whole pop)    : {per_cap_worked:6.0f} h/person/yr worked")
    print(f"  mean consumption, domestic    : {mean_dom:6.0f} h/person/yr")
    print(f"  MEDIAN bundle, domestic (LB)  : {med_lo:6.0f} h/person/yr")
    print(f"  MEDIAN bundle, import-adj     : {med_hi:6.0f} h/person/yr")
    print(f"  => a median lifestyle commands ~{med_lo:.0f}-{med_hi:.0f} h/yr of others' LABOUR")
    print()
    print(">>> THE FINDING: labour is ABUNDANT relative to what lifestyles command")
    print("-" * W)
    print(f"  self-care credit, per capita  : {sc_pc:6.0f} h/yr   (F * 365, every human)")
    print(f"  self-care credit, US total    : {sc_tot/1e9:6.0f} billion h/yr")
    print(f"  productive labour, US total   : {tot/1e9:6.0f} billion h/yr")
    print(f"  self-care / productive        : {sc_over_prod:6.1f} x")
    print(f"  median labour bundle / self-care credit : {med_frac_lo:.2f}-{med_frac_hi:.2f}")
    print( "  -> Self-care credit alone (~10 h/day for EVERY human) is ~4x ALL the")
    print( "     productive labour in the economy, and ~4-8x the labour a median")
    print( "     lifestyle commands. So the LABOUR dimension never binds a consumption")
    print( "     ceiling. What binds -- and where the rich diverge -- is the MATERIAL /")
    print( "     ENERGY / land dimensions of the debit vector, not labour-time.")
    print()
    print("Bucket 2 -- the consumer's OWN combustion + waste (physical; needs the")
    print("            material dims + a mitigation weight to enter the hours ceiling)")
    print("-" * W)
    print(f"  vehicle fuel        : {x.own_vehicle_co2_t:4.1f} t CO2/yr")
    print(f"  on-site home fuel   : {x.own_home_fuel_co2_t:4.1f} t CO2/yr")
    print(f"  garbage (MSW)       : {x.own_msw_kg:4.0f} kg/yr")
    print()
    print("Bucket 3 -- upstream production pollution : EXCLUDED (Sec.3.2b, on producers)")
    print()
    print("The physical footprint disparity the rho*C cap COMPRESSES")
    print("-" * W)
    print(f"  median energy footprint     : {x.primary_energy_gj:6.0f} GJ/yr"
          f"   material : {x.material_footprint_t:.0f} t/yr")
    print(f"  a top-tail lifestyle (~{x.toptail_footprint_mult:.0f}x) : "
          f"{x.primary_energy_gj*x.toptail_footprint_mult:6.0f} GJ/yr"
          f"   material : {x.material_footprint_t*x.toptail_footprint_mult:.0f} t/yr")
    print( "  Physically, footprints span ~10-100x median. That is where the rich")
    print( "  actually diverge -- in materials & energy, not in labour-hours.")
    print()
    print("The clean disparity result (rho-independent, weighting-independent)")
    print("-" * W)
    print(f"  self-care floor F           : {x.self_care_floor_h_day:.0f} h/day")
    print(f"  CEILING 24/F                : {ratio:6.1f} x   (max credit 24h vs floor F)")
    print( "  Argument: total consumption D <= rho*C; credit C is bounded to [F,24]*365")
    print(f"  -> a {ratio:.1f}x spread; so D_max/D_min <= {ratio:.1f}x WHATEVER the collapse")
    print( "  weights (they set WHAT you consume, never the TOTAL cap). Sec.3.5 (debit >")
    print( "  credit in aggregate) guarantees the gate is ACTIVE, so it binds.")
    print()
    print( "  Today, for comparison       : top incomes run 10,000-100,000 x the median;")
    print(f"  physical footprints ~10-100x. Aequitas caps the spread at ~{ratio:.0f}x")
    print( "  (3-4 orders of magnitude of compression), and it does NOT depend on OP-10.")
    print()
    print("  NEXT: the rho-sweep sim -- heterogeneous agents, does a pickable rho keep")
    print("  committed-debit ~= productive capacity across growth / decline / disaster?")
    print("=" * W)

    return dict(
        total_labour_hours=tot,
        per_capita_worked=per_cap_worked,
        mean_consumption_hours_domestic=mean_dom,
        median_bundle_lo=med_lo,
        median_bundle_hi=med_hi,
        self_care_credit_per_capita=sc_pc,
        self_care_over_productive=sc_over_prod,
        accrual_ceiling_ratio=ratio,
    )


# ---------------------------------------------------------------------------
# Self-tests -- sanity, not precision
# ---------------------------------------------------------------------------

def test_domestic_is_lower_bound():
    x = Inputs()
    lo, hi = median_bundle_hours(x)
    assert lo <= hi, "domestic-only must be <= import-adjusted"
    print(f"[ok] domestic LB ({lo:.0f}) <= import-adjusted ({hi:.0f})")


def test_labour_is_abundant():
    """The finding: median LABOUR bundle is a small fraction of self-care credit."""
    x = Inputs()
    lo, hi = median_bundle_hours(x)
    sc = self_care_credit_per_capita(x)
    assert hi < sc, (
        f"median labour bundle {hi:.0f} should be < self-care credit {sc:.0f} "
        f"(labour abundance)")
    print(f"[ok] median labour bundle {lo:.0f}-{hi:.0f} h/yr < self-care credit "
          f"{sc:.0f} h/yr (labour abundant)")


def test_self_care_dwarfs_production():
    """Self-care credit (every human) must exceed total productive labour."""
    x = Inputs()
    r = total_self_care_credit(x) / total_labour_hours(x)
    assert r > 1.0, f"self-care/productive = {r:.1f} should exceed 1"
    print(f"[ok] self-care credit = {r:.1f}x total productive labour")


def test_ceiling_rho_independent():
    """24/F must not depend on rho (the whole point of the reframe)."""
    a = accrual_ceiling_ratio(Inputs(rho=1.2))
    b = accrual_ceiling_ratio(Inputs(rho=3.0))
    assert abs(a - b) < 1e-12, "accrual ceiling must be rho-independent"
    print(f"[ok] accrual ceiling rho-independent (24/F = {a:.1f}x at any rho)")


def test_per_capita_sane():
    """Per-capita hours worked must be < full-time (pop includes non-workers)."""
    x = Inputs()
    pc = total_labour_hours(x) / x.population
    assert 500 < pc < x.avg_annual_hours, f"per-capita worked {pc:.0f} implausible"
    print(f"[ok] per-capita hours worked {pc:.0f} < full-time {x.avg_annual_hours:.0f}")


def run_tests():
    test_domestic_is_lower_bound()
    test_labour_is_abundant()
    test_self_care_dwarfs_production()
    test_ceiling_rho_independent()
    test_per_capita_sane()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true", help="run self-tests only")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
