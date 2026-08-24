"""
track2_housing.py -- Track 2 of the median-adult lifestyle cost: HOUSING.

The carried-forward labour Track 1 misses. A home's construction labour was spent
years ago, so it never appears in this year's PCE (Track 1). Under Aequitas it is
front-loaded and holding-time-split (Foundations Sec.6.2b), so the right per-year
figure is the home's total build labour ANNUALISED over its service life.

WHY THIS IS THE BILL-OF-MATERIALS LABOUR, done via IO:
The BLS Employment Requirements Matrix "Construction" column is a TOTAL requirement
-- it already includes the labour to produce the lumber, concrete, steel, windows,
plumbing, wiring and mechanicals as INDIRECT requirements (that is what "total"
means). Applied to a home's CONSTRUCTION COST (the structure -- not land, not
finance, not the mortgage), it back-traces every material's production labour plus
on-site assembly, in one measured coefficient. So we avoid (a) applying a labour
multiplier to land/finance dollars, and (b) inventing per-material labour rates.

NO DOUBLE-COUNT with Track 1: residential construction is INVESTMENT in the national
accounts, not PCE, so none of this is in Track 1's PCE. Track 1's "owner-occupied
dwellings" line is the imputed-rent SERVICE flow (a return on capital), not the build.

    build_hours   = structure_cost($M) x construction_jobs_per_$M x hours_per_job
    per_year      = build_hours / service_life
    + maintenance = annual home improvement/repair $ x same multiplier (already /yr)

Reuses the ERM loader and hours/job from track1_labour.

Run:  python track2_housing.py
      python track2_housing.py --test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

from track1_labour import load_erm, Params as T1Params

CONSTRUCTION_SECTOR = 15   # BLS sector 15 = Construction (verified title)


@dataclass(frozen=True)
class HouseParams:
    # The home a median adult actually lives in = existing stock, not a new build.
    median_home_sqft: float = 2_000.0       # US existing single-family ~1,800-2,100
    construction_cost_per_sqft: float = 160.0  # structure only, excl land (RSMeans/NAHB ~$150-165)
    service_life_years: float = 60.0        # homes last 60-100+ yr; 60 = conservative (more h/yr)
    persons_per_home: float = 2.5           # US avg household size (Census)
    adults_per_home: float = 2.0
    # Ongoing improvement/repair (owner improvements are investment, not PCE, so also
    # missing from Track 1). ~$3,500/home/yr (Harvard JCHS / Census C30). Flagged.
    home_improvement_per_year: float = 3_500.0
    hours_per_job: float = 1_750.0          # shared with Track 1


def construction_multiplier():
    """Total (direct+indirect) jobs per $1M final demand for Construction."""
    sector_ids, jobs_per_M = load_erm()
    idx = sector_ids.index(CONSTRUCTION_SECTOR)
    return jobs_per_M[idx]


def compute(h: HouseParams | None = None):
    h = h or HouseParams()
    mult = construction_multiplier()                      # jobs per $1M

    structure_cost = h.median_home_sqft * h.construction_cost_per_sqft   # $
    build_jobs = (structure_cost / 1e6) * mult
    build_hours = build_jobs * h.hours_per_job            # total labour to build
    build_per_year = build_hours / h.service_life_years   # annualised (Sec.6.2b)

    maint_jobs = (h.home_improvement_per_year / 1e6) * mult
    maint_hours = maint_jobs * h.hours_per_job            # already per year

    per_home_year = build_per_year + maint_hours
    per_adult = per_home_year / h.adults_per_home
    per_person = per_home_year / h.persons_per_home

    return dict(
        params=h, mult=mult, structure_cost=structure_cost,
        build_hours=build_hours, build_per_year=build_per_year,
        maint_hours=maint_hours, per_home_year=per_home_year,
        per_adult=per_adult, per_person=per_person,
    )


def report(h: HouseParams | None = None):
    h = h or HouseParams()
    r = compute(h)
    W = 78
    print("=" * W)
    print("TRACK 2 -- housing construction labour (annualised), per median adult")
    print("=" * W)
    print(f"Construction multiplier (BLS ERM sector 15): {r['mult']:.1f} jobs/$1M")
    print(f"  (already includes lumber/steel/concrete/windows/plumbing/electrical")
    print(f"   production labour as INDIRECT requirements)")
    print("-" * W)
    print(f"median home                 : {h.median_home_sqft:,.0f} sqft "
          f"@ ${h.construction_cost_per_sqft:.0f}/sqft (structure, excl land)")
    print(f"structure cost              : ${r['structure_cost']:,.0f}")
    print(f"TOTAL build labour          : {r['build_hours']:,.0f} hours "
          f"(~{r['build_hours']/1750:.1f} person-years)")
    print(f"annualised over {h.service_life_years:.0f} yr life : "
          f"{r['build_per_year']:,.0f} h/yr per home")
    print(f"+ improvement/repair        : {r['maint_hours']:,.0f} h/yr per home "
          f"(${h.home_improvement_per_year:,.0f}/yr)")
    print(f"= housing labour per home   : {r['per_home_year']:,.0f} h/yr")
    print("-" * W)
    print(f"  per ADULT ({h.adults_per_home:.0f}/home)      : "
          f"{r['per_adult']:6.0f} h/yr")
    print(f"  per person ({h.persons_per_home:.1f}/home)   : "
          f"{r['per_person']:6.0f} h/yr")
    print("-" * W)
    # sensitivity
    big = compute(HouseParams(median_home_sqft=2400, construction_cost_per_sqft=180,
                              service_life_years=50))
    small = compute(HouseParams(median_home_sqft=1600, construction_cost_per_sqft=140,
                                service_life_years=80))
    print(f"sensitivity (small 1600sqft/80yr .. big 2400sqft/50yr): "
          f"per-adult {small['per_adult']:.0f}-{big['per_adult']:.0f} h/yr")
    print("=" * W)
    print("Cleanly ADDITIVE to Track 1 (construction is investment, not PCE). This is")
    print("the durable carried-forward labour Track 1 structurally misses.")
    print("=" * W)
    return r


def test_multiplier_is_construction():
    m = construction_multiplier()
    assert 4.0 < m < 8.0, f"construction multiplier {m:.1f} off (expected ~5.8)"
    print(f"[ok] construction multiplier {m:.1f} jobs/$1M")


def test_build_hours_plausible():
    r = compute()
    py = r["build_hours"] / 1750
    assert 1.0 < py < 4.0, f"build {py:.1f} person-years implausible for a house"
    print(f"[ok] total build labour {r['build_hours']:,.0f} h (~{py:.1f} person-years)")


def test_per_adult_range():
    r = compute()
    assert 10 < r["per_adult"] < 120, f"per-adult housing {r['per_adult']:.0f} off"
    print(f"[ok] housing per-adult {r['per_adult']:.0f} h/yr in sane range")


def run_tests():
    test_multiplier_is_construction()
    test_build_hours_plausible()
    test_per_adult_range()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
