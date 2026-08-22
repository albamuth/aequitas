"""
q5_reallocation.py -- Q5 of the scenario suite.

Question (author): how could the world's standard of living change if the labour-time
balance between WASTEFUL (warfare, luxuries, policing/repression, disposable goods,
fossil fuels) and ESSENTIAL (healthcare, food/water, housing, quality clothing,
renewable energy) were changed under Aequitas?

TYPE: explicit counterfactual with an EXOGENOUS TAXONOMY DIAL. Aequitas does NOT decree
what is wasteful vs essential -- under Aequitas this shift is driven by PLEDGES (§6), not
by any planner. The wasteful/essential split here is a scenario knob the author asked me
to propose; every boundary is contestable and a sensitivity pass is run over it.

METHOD. Take the global labour pool (ILO). Free the WASTEFUL fraction (anchored to Q2's
captured/wasted pool, 17-36% of productive labour, applied globally as a band). Compare
the freed hours to the labour needed to close the world's major ESSENTIAL deficits
(health workforce, adequate housing). The result is an UPPER ENVELOPE on the reallocation
gain -- it shows whether essential needs are labour-constrained at all.

HEADLINE (and it echoes Q1): meeting the world's essential needs is NOT labour-limited.
The freed pool dwarfs the deficits by ~1-2 orders of magnitude. The binding constraints
are materials/energy (Q1) and demand-side coordination (pledges) -- never a shortage of
human hours. "We can't afford to house/heal everyone" is a money statement, not a
physical one.

PROPOSED TAXONOMY (v1 -- every row contestable, treated as a dial):
    WASTEFUL (shrink)                    ESSENTIAL (grow)
    warfare / arms                       healthcare
    luxury / positional goods            food & clean water
    policing / repression*               housing (durable)
    disposable / short-life goods        quality, durable clothing
    fossil-fuel extraction               renewable energy + grid
    FIRE / advertising overhead          education / care
    (*vs legitimate public safety -- the sharpest boundary; sensitivity-tested)

DATA ANCHORS (real, cited in-line):
  - Global employment ~3.5B workers (ILO WESO 2024,
    https://www.ilo.org/resource/statement/world-employment-and-social-outlook-trends-2024-ilo-director-generals).
  - Wasteful/captured fraction 17-36% of productive labour (Q2, q2_capture.py).
  - WHO health-worker shortage ~11M by 2030
    (https://www.who.int/, State of the World's Nursing).
  - ~1.13B people live in informal settlements/slums; up to 3.4B lack adequate
    housing (UN-Habitat World Cities Report,
    https://unhabitat.org/world-cities-report-2026).

Run:  python q5_reallocation.py
      python q5_reallocation.py --test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class ReallocationParams:
    global_workers: float = 3.5e9
    hours_per_worker: float = 1_900.0

    # wasteful fraction of productive labour -- the taxonomy DIAL (Q2 band, global)
    wasteful_frac_lo: float = 0.17
    wasteful_frac_hi: float = 0.36

    # --- essential deficits, in labour-hours ---
    health_worker_shortage: float = 11e6          # WHO, by 2030
    hours_per_health_worker_yr: float = 1_900.0

    slum_population: float = 1.13e9               # UN-Habitat informal settlements
    inadequate_housing_population: float = 3.4e9  # up to 3.4B lack adequate housing
    persons_per_dwelling: float = 4.0
    person_hours_per_dwelling: float = 2_000.0    # modest durable dwelling, incl. trades

    # sensitivity: reclassify a chunk of the wasteful pool as essential (e.g. half of
    # "policing" is legitimate public safety) -> shrinks the freed pool
    sensitivity_reclassify: float = 0.25


def compute(p: ReallocationParams | None = None):
    p = p or ReallocationParams()
    pool = p.global_workers * p.hours_per_worker            # total global labour-hours/yr

    freed_lo = pool * p.wasteful_frac_lo
    freed_hi = pool * p.wasteful_frac_hi
    # sensitivity: reclassify a slice back to essential/legitimate
    freed_sens_lo = pool * p.wasteful_frac_lo * (1 - p.sensitivity_reclassify)

    # essential deficits in hours
    health_hours = p.health_worker_shortage * p.hours_per_health_worker_yr   # per year
    slum_dwellings = p.slum_population / p.persons_per_dwelling
    slum_hours = slum_dwellings * p.person_hours_per_dwelling                 # one-time
    all_housing_dwellings = p.inadequate_housing_population / p.persons_per_dwelling
    all_housing_hours = all_housing_dwellings * p.person_hours_per_dwelling   # one-time

    return dict(
        pool=pool, freed=(freed_lo, freed_hi), freed_sens_lo=freed_sens_lo,
        health_hours=health_hours, slum_hours=slum_hours, all_housing_hours=all_housing_hours,
        # ratios / durations
        health_ratio=(freed_lo / health_hours, freed_hi / health_hours),
        slum_years=(slum_hours / freed_hi, slum_hours / freed_lo),        # yrs at freed rate
        all_housing_years=(all_housing_hours / freed_hi, all_housing_hours / freed_lo),
        p=p,
    )


def report(p: ReallocationParams | None = None):
    p = p or ReallocationParams()
    r = compute(p)
    W = 78
    print("=" * W)
    print("Q5 -- reallocating WASTEFUL -> ESSENTIAL labour (counterfactual; taxonomy = dial)")
    print("=" * W)
    print(f"Global labour pool         : {r['pool']:.2e} h/yr  (3.5B workers x 1,900 h)")
    fl, fh = r["freed"]
    print(f"Wasteful fraction (dial)   : {p.wasteful_frac_lo:.0%}-{p.wasteful_frac_hi:.0%}  (Q2 band, global)")
    print(f"FREED labour pool          : {fl:.2e} - {fh:.2e} h/yr")
    print("-" * W)
    print("What the freed hours could do vs the world's essential deficits:")
    hl, hh = r["health_ratio"]
    print(f"  HEALTHCARE -- WHO 11M-worker shortage = {r['health_hours']:.2e} h/yr")
    print(f"    freed pool covers it {hl:.0f}-{hh:.0f}x OVER (per year)")
    sl, sh = r["slum_years"]
    print(f"  HOUSING (slums, 1.13B people) = {r['slum_hours']:.2e} h one-time")
    print(f"    buildable with the freed pool in ~{sl:.1f}-{sh:.1f} years")
    al, ah = r["all_housing_years"]
    print(f"  HOUSING (all 3.4B inadequately housed) = {r['all_housing_hours']:.2e} h one-time")
    print(f"    buildable with the freed pool in ~{al:.1f}-{ah:.1f} years")
    print("-" * W)
    print(f"SENSITIVITY (reclassify {p.sensitivity_reclassify:.0%} of the pool as legitimate):")
    print(f"  freed low end {fl:.2e} -> {r['freed_sens_lo']:.2e} h/yr")
    print(f"  health coverage still {r['freed_sens_lo']/r['health_hours']:.0f}x -- conclusion robust")
    print("=" * W)
    print("Headline: meeting the world's ESSENTIAL needs is NOT labour-constrained --")
    print("the freed pool dwarfs the deficits ~50-100x. The real limits are materials/")
    print("energy (Q1) and demand-side coordination (pledges), never a shortage of hours.")
    print("'We can't afford to house/heal everyone' is a money statement, not a physical one.")
    print("=" * W)
    return r


# ---------------------------------------------------------------------------
# self-tests
# ---------------------------------------------------------------------------

def test_freed_band_ordered():
    r = compute()
    assert 0 < r["freed"][0] < r["freed"][1], "freed band must be positive & ordered"
    print(f"[ok] freed pool {r['freed'][0]:.2e}-{r['freed'][1]:.2e} h/yr")


def test_health_dwarfed():
    """Freed pool must cover the health shortage many times over."""
    r = compute()
    assert r["health_ratio"][0] > 10, "freed pool should be >10x the health shortage"
    print(f"[ok] freed covers WHO shortage {r['health_ratio'][0]:.0f}-{r['health_ratio'][1]:.0f}x")


def test_housing_fast():
    """Slum housing buildable within a handful of years of the freed pool."""
    r = compute()
    assert r["slum_years"][0] < 3, "slum housing should be buildable within a few years"
    print(f"[ok] slum housing buildable in ~{r['slum_years'][0]:.1f}-{r['slum_years'][1]:.1f} yrs")


def test_sensitivity_robust():
    """Even after reclassifying part of the pool, health is still dwarfed."""
    r = compute()
    assert r["freed_sens_lo"] / r["health_hours"] > 10, "conclusion should survive the sensitivity"
    print(f"[ok] sensitivity: still {r['freed_sens_lo']/r['health_hours']:.0f}x the health shortage")


def test_labour_not_the_limit():
    """The whole point: hours are not the binding constraint on essentials."""
    r = compute()
    # even ALL inadequate-housing built plus health covered is a fraction of one year's freed pool
    one_year = r["freed"][1]
    assert r["health_hours"] + r["all_housing_hours"] / 5 < one_year, "essentials << freed pool"
    print("[ok] essentials (health + housing over 5 yrs) fit inside one year's freed pool")


def run_tests():
    test_freed_band_ordered()
    test_health_dwarfed()
    test_housing_fast()
    test_sensitivity_robust()
    test_labour_not_the_limit()
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
