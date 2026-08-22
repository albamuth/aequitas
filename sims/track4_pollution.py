"""
track4_pollution.py -- Track 4 of the median-adult lifestyle cost: the labour-
hours to REMEDIATE the pollution a US adult causes THEMSELVES (bucket-2 debit).

SCOPE (Foundations v0.15 sec.3.2b + sec.3.2b real-time-dispatch).
  The consumer carries only pollution THEY cause by their own action:
    - vehicle fuel they burn                (combustion, driver acts)
    - on-site home fuel they burn (gas)     (combustion, occupant acts)
    - ELECTRICITY they draw                 (real-time dispatch: non-storable,
                                             generated the instant drawn -> the
                                             END-USER's emission, sec.3.2b-realtime)
    - wastewater + solid waste they generate (treatment labour)
  EXCLUDED: all upstream PRODUCTION pollution (mine tailings, factory emissions,
  farm runoff) -- permanent on each producer under sec.3.2b, never the consumer.
  Track 1 already carries the *labour+material* of the goods; this track is only
  the consumer's OWN emissions -> remediation labour.

  *** AXIOM-vs-METHOD-DOC DISCREPANCY, FLAGGED (CLAUDE.md rule). ***
  median_lifestyle_METHOD.md (written against Foundations v0.9) says EXCLUDE
  electricity ("generation stays with the plant"). Foundations v0.15 sec.3.2b
  REVERSED this: real-time-dispatched electricity emissions follow the end-user.
  This script follows the CURRENT axiom and INCLUDES residential electricity.
  Set INCLUDE_ELECTRICITY=False to reproduce the stale-method-doc figure.

THE HARD PART -- the sec.3.3 remediation-basis question (an OPEN decision).
  Labour-hours per tonne CO2 depends entirely on WHICH remediation restores the
  sec.3.3 baseline:
    - NATURE-BASED (afforestation / soil carbon): cheap, ~$15-50/t.
    - ENGINEERED DIRECT AIR CAPTURE (DAC): expensive, ~$250-600/t today.
  We do NOT pick one -- we report the RANGE, as the method plan directs. Cost is
  bridged to labour with an economy-average intensity h_per_dollar (same Level-1
  ballpark as Q3 plastic, ~0.009 h/$ from the ERM: ~5 jobs/$1M x 1800 h). This
  counts embodied labour commanded by the remediation spend; flagged as a
  ballpark, and it is the ratio (nature vs DAC) that matters, not the absolute.

Run:  python track4_pollution.py [--test]
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

INCLUDE_ELECTRICITY = True  # Foundations v0.15 sec.3.2b-realtime; see header


@dataclass(frozen=True)
class Inputs:
    # --- the adult's OWN CO2 emissions, per capita, t/yr (2022-23) ---
    vehicle_co2_t: float = 3.0     # US light-duty vehicle CO2 ~1.0 Gt / 335M
    home_fuel_co2_t: float = 1.0   # residential on-site gas (heat/stove/water),
                                   #   ~0.27 Gt NG + oil; ~1.0 t/capita
    electricity_co2_t: float = 1.7  # residential electricity: US power-sector CO2
                                    #   ~1.5 Gt x ~38% residential / 335M ~ 1.7 t
                                    #   (real-time-dispatch: the consumer's, v0.15)

    # --- carbon remediation cost bracket ($/t CO2) -- the sec.3.3 open choice ---
    cost_nature_lo: float = 15.0   # afforestation / soil carbon, low
    cost_nature_hi: float = 50.0   # afforestation, high / degraded-land
    cost_dac_lo: float = 250.0     # engineered DAC, optimistic near-term
    cost_dac_hi: float = 600.0     # engineered DAC, current high end

    # --- cost -> labour bridge (economy-avg embodied labour intensity) ---
    h_per_dollar: float = 0.009    # ~5 jobs/$1M x 1800 h/job (ERM Level-1);
                                   #   matches Q3 plastic's 0.010 h/$ ballpark

    # --- wastewater + solid waste (TREATMENT labour; small) ---
    wastewater_kgal_yr: float = 30.0     # ~82 gal/person/day indoor -> 30 kgal/yr
    ww_h_per_kgal: float = 1.2e-5        # WWTP: ~25 staff per 10 MGD plant
                                         #   (25*1800h / 3.65e9 gal *1000)
    msw_kg_yr: float = 811.0             # EPA ~4.9 lb/person/day
    msw_h_per_kg: float = 2.8e-6         # ~450k US waste workers / 290 Mt MSW

    us_pop: float = 335e6
    us_adults: float = 259e6
    median_over_mean: float = 0.80


def own_co2(x: Inputs) -> float:
    t = x.vehicle_co2_t + x.home_fuel_co2_t
    if INCLUDE_ELECTRICITY:
        t += x.electricity_co2_t
    return t


def carbon_labour_range(x: Inputs) -> tuple[float, float]:
    """(nature-based low, DAC high) remediation labour-hours/yr for own CO2."""
    t = own_co2(x)
    lo = t * x.cost_nature_lo * x.h_per_dollar
    hi = t * x.cost_dac_hi * x.h_per_dollar
    return lo, hi


def carbon_labour_points(x: Inputs) -> dict:
    t = own_co2(x)
    b = lambda c: t * c * x.h_per_dollar
    return {
        "nature_lo": b(x.cost_nature_lo),
        "nature_hi": b(x.cost_nature_hi),
        "dac_lo": b(x.cost_dac_lo),
        "dac_hi": b(x.cost_dac_hi),
    }


def waste_labour(x: Inputs) -> float:
    return x.wastewater_kgal_yr * x.ww_h_per_kgal + x.msw_kg_yr * x.msw_h_per_kg


def totals(x: Inputs) -> dict:
    lo_c, hi_c = carbon_labour_range(x)
    w = waste_labour(x)
    lo, hi = lo_c + w, hi_c + w
    scale = (x.us_pop / x.us_adults) * x.median_over_mean  # per-cap -> median adult
    return dict(
        co2_t=own_co2(x),
        carbon_lo=lo_c, carbon_hi=hi_c, waste=w,
        total_percap_lo=lo, total_percap_hi=hi,
        median_adult_lo=lo * scale, median_adult_hi=hi * scale,
        points=carbon_labour_points(x),
    )


def report(x: Inputs | None = None) -> dict:
    x = x or Inputs()
    r = totals(x)
    W = 70
    print("=" * W)
    print("TRACK 4 -- LABOUR TO REMEDIATE THE ADULT'S OWN POLLUTION (per capita/yr)")
    print("=" * W)
    print(f"  Own CO2 (vehicle+home fuel"
          f"{'+electricity' if INCLUDE_ELECTRICITY else ''}) : {r['co2_t']:.1f} t/yr")
    print("    vehicle 3.0 + home-fuel 1.0"
          + ("  + electricity 1.7 (v0.15 sec.3.2b real-time dispatch)" if INCLUDE_ELECTRICITY else "  [electricity EXCLUDED]"))
    print("-" * W)
    print("  Carbon remediation labour depends on the sec.3.3 BASIS (open choice):")
    p = r["points"]
    print(f"    nature-based (afforestation)  : {p['nature_lo']:5.1f} - {p['nature_hi']:5.1f} h/yr")
    print(f"    engineered DAC                : {p['dac_lo']:5.1f} - {p['dac_hi']:5.1f} h/yr")
    print(f"  Wastewater + solid-waste treatment: {r['waste']:.3f} h/yr (negligible)")
    print("-" * W)
    print(f"  TRACK 4 RANGE, per capita     : {r['total_percap_lo']:5.1f} - {r['total_percap_hi']:5.1f} h/yr")
    print(f"  TRACK 4 RANGE, median adult   : {r['median_adult_lo']:5.1f} - {r['median_adult_hi']:5.1f} h/yr")
    print("=" * W)
    print("  CONTEXT: Tracks 1+3 = ~1,276 h/capita. Track 4 adds only")
    print(f"  ~{r['total_percap_lo']:.0f}-{r['total_percap_hi']:.0f} h -- own-pollution remediation is a SMALL labour")
    print("  add under nature-based restoration, modest under DAC. The big")
    print("  environmental debit is the near-PERMANENT stock kind (Q3 micro-")
    print("  plastics, landfill) that no scalable remediation retires -- not")
    print("  this flow-remediation. Carbon-basis choice swings it ~14x.")
    print("=" * W)
    return r


# --- self-tests --------------------------------------------------------------
def test_range_ordered():
    r = totals(Inputs())
    assert r["total_percap_lo"] < r["total_percap_hi"]
    print(f"[ok] range ordered {r['total_percap_lo']:.1f} < {r['total_percap_hi']:.1f}")


def test_dac_dearer_than_nature():
    p = totals(Inputs())["points"]
    assert p["dac_lo"] > p["nature_hi"], "DAC should exceed nature-based"
    print(f"[ok] DAC ({p['dac_lo']:.1f}+) dearer than nature ({p['nature_hi']:.1f})")


def test_waste_negligible():
    r = totals(Inputs())
    assert r["waste"] < 0.1, r["waste"]
    print(f"[ok] wastewater+MSW treatment labour {r['waste']:.3f} h negligible")


def test_small_vs_tracks13():
    """Track 4 must be small next to the ~1276 h of Tracks 1+3."""
    r = totals(Inputs())
    assert r["total_percap_hi"] < 100, r["total_percap_hi"]
    print(f"[ok] Track-4 high end {r['total_percap_hi']:.0f} h << 1276 h (Tracks 1+3)")


def test_electricity_toggle():
    """Including electricity must raise the CO2 and the labour."""
    global INCLUDE_ELECTRICITY
    INCLUDE_ELECTRICITY = True
    a = own_co2(Inputs())
    INCLUDE_ELECTRICITY = False
    b = own_co2(Inputs())
    INCLUDE_ELECTRICITY = True
    assert a > b, "electricity inclusion must raise own-CO2"
    print(f"[ok] electricity toggle: {a:.1f} t (v0.15) vs {b:.1f} t (stale method doc)")


def run_tests():
    test_range_ordered()
    test_dac_dearer_than_nature()
    test_waste_negligible()
    test_small_vs_tracks13()
    test_electricity_toggle()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    run_tests() if a.test else report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
