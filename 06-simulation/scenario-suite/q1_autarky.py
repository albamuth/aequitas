"""
q1_autarky.py -- Q1 of the scenario suite.

Question (author): what is the highest EGALITARIAN, PHYSICAL standard of living the
continental US can sustain using only local labour and resources -- no imports,
no exports?

METRIC (author's choice): the highest level EVERYONE can hold at once, in physical
services, bounded by the disparity ceiling -- NOT a dollar figure and NOT a top-tail
maximum.

TYPE: physical feasibility envelope. Method: for each binding input (labour, energy,
land, water, critical minerals) compute the autarkic per-capita ceiling and divide by
today's average-person footprint. The SMALLEST ratio is the binding constraint; the
egalitarian universal bundle is what that constraint permits, distributed under 24/F.

CORE FINDING (what the numbers say):
  - LABOUR is NOT binding. The credited-labour pool (productive + self-care) is ~2x
    what even a fully re-shored footprint needs. Hours are abundant (this project's
    standing result: self-care credit ~3-4x all productive labour).
  - WATER and FOOD are adequate. The US is a large net food exporter and has ~5x its
    water footprint in renewable supply.
  - ENERGY is the SWING constraint, and it is a BUILD-OUT question, not a resource one:
      * at today's sustainable build (renewables + nuclear ~16 quads) the ceiling is
        only ~1/5 of current per-capita energy -- a big cut;
      * at full renewable TECHNICAL POTENTIAL (NREL: solar+wind many x current use)
        energy is abundant -- but the build-out itself consumes land + critical minerals.
  - CRITICAL MINERALS are the genuine autarky loss: the US is >50% net-import-reliant
    for ~50 minerals (USGS). These must be substituted, recycled, or forgone.

So the honest headline: an autarkic US is NOT labour- or land- or water-limited; its
egalitarian physical ceiling is set by (a) completing the renewable energy transition
and (b) a short list of non-substitutable minerals. Complete the transition and the
sustainable universal standard sits around today's MEAN; leave energy at today's
sustainable build and per-capita energy drops to ~1/5. Physical consumption is
naturally bounded (mean/median ~1.2), so "egalitarian" costs little vs the average.

DATA ANCHORS (real, cited in-line):
  - Population ~335M; adults ~258M (Census 2023).
  - Primary energy 2023: production 102.8 / consumption 93.6 quads; renewables ~8
    quads, nuclear ~9% (~8.4 quads). EIA (https://www.eia.gov/todayinenergy/detail.php?id=62407).
  - Solar+wind technical potential >> current consumption. NREL 2023 supply-curve
    study (https://research-hub.nrel.gov/en/publications/
    solar-photovoltaics-and-land-based-wind-technical-potential-and-s).
  - Cropland ~135M ha (334M ac); total ag land incl. pasture/grazed forest ~478M ha.
    USDA ERS (https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/land-and-natural-resources).
  - Renewable freshwater supply ~2,800 km3/yr; withdrawals ~1,200. USGS.
  - Critical-mineral net import reliance >50% for ~50 commodities. USGS MCS 2024.
  - Average-person footprint (this project, median_lifestyle): ~279 GJ energy,
    2.2 ha land, 1,600 m3 water, ~1,600 embodied labour-h/yr.

Run:  python q1_autarky.py
      python q1_autarky.py --test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field

QUAD_TO_GJ = 1.055e9          # 1 quad = 1.055e18 J = 1.055e9 GJ


@dataclass(frozen=True)
class AutarkyParams:
    population: float = 335e6
    adults: float = 258e6

    # --- labour pool, h/yr ---
    jobs: float = 160e6
    hours_per_job: float = 1_750.0
    self_care_h_per_adult: float = 10.0 * 365.0    # F=10 h/day credited (A2/§6.1b)

    # --- energy, quads/yr ---
    energy_consumption_quads: float = 93.6
    renewable_quads: float = 8.0
    nuclear_quads: float = 8.4
    # full renewable technical potential as a MULTIPLE of current consumption
    # (NREL: solar+wind technical potential is many x current use; conservative 10x)
    renewable_potential_multiple: float = 10.0

    # --- land, hectares ---
    cropland_ha: float = 135e6
    total_ag_land_ha: float = 478e6                # cropland + pasture + grazed forest

    # --- water, m3/yr ---
    renewable_water_m3: float = 2.8e12             # ~2,800 km3/yr renewable supply

    # --- average-person footprint (this project, median_lifestyle) ---
    # NB: footprints must be on an AUTARKIC / domestically-producible basis (imports
    # are being removed). Land especially: the gross 2.2 ha/person footprint includes
    # foreign + non-food land; the domestic-DIET land need (incl. pasture for the
    # current heavy-meat US diet) is ~1.3 ha/person. The US is a net food EXPORTER,
    # so domestic land feeds the domestic diet with room -- but it is the tightest
    # resource, and a higher-meat diet makes it bind. Diet is the lever.
    fp_energy_GJ: float = 279.0                    # 93.6 quads / 335M (domestic-consumed)
    fp_land_ha: float = 1.3                        # domestic-diet land (incl. pasture)
    fp_water_m3: float = 1_600.0
    fp_labour_h: float = 1_600.0                   # ~half currently foreign -> re-shored here

    # physical consumption is naturally bounded (this project): mean/median ~1.2
    footprint_mean_over_median: float = 1.20

    # critical minerals: number of commodities with >50% US net import reliance (USGS)
    critical_minerals_import_reliant: int = 50


def compute(p: AutarkyParams | None = None):
    p = p or AutarkyParams()

    # --- per-capita availability ---
    labour_pool = p.jobs * p.hours_per_job + p.adults * p.self_care_h_per_adult
    avail = {
        "labour_h":  labour_pool / p.population,
        "energy_GJ_current_build":  (p.renewable_quads + p.nuclear_quads) * QUAD_TO_GJ / p.population,
        "energy_GJ_full_potential": p.renewable_potential_multiple * p.energy_consumption_quads
                                     * QUAD_TO_GJ / p.population,
        "land_ha":   p.total_ag_land_ha / p.population,
        "water_m3":  p.renewable_water_m3 / p.population,
    }
    footprint = {
        "labour_h":  p.fp_labour_h,
        "energy_GJ": p.fp_energy_GJ,
        "land_ha":   p.fp_land_ha,
        "water_m3":  p.fp_water_m3,
    }

    # --- binding ratios (available / footprint); <1 binds, >1 has room ---
    ratios = {
        "labour":                 avail["labour_h"] / footprint["labour_h"],
        "energy (current build)": avail["energy_GJ_current_build"] / footprint["energy_GJ"],
        "energy (full renewable potential)": avail["energy_GJ_full_potential"] / footprint["energy_GJ"],
        "land":                   avail["land_ha"] / footprint["land_ha"],
        "water":                  avail["water_m3"] / footprint["water_m3"],
    }

    # binding constraint under each energy scenario
    def binding(scenario_key):
        rs = {k: v for k, v in ratios.items()
              if k in ("labour", "land", "water", scenario_key)}
        k = min(rs, key=rs.get)
        return k, rs[k]

    bind_current = binding("energy (current build)")
    bind_potential = binding("energy (full renewable potential)")

    return dict(avail=avail, footprint=footprint, ratios=ratios,
                bind_current=bind_current, bind_potential=bind_potential, p=p)


def report(p: AutarkyParams | None = None):
    p = p or AutarkyParams()
    r = compute(p)
    W = 78
    print("=" * W)
    print("Q1 -- highest EGALITARIAN, PHYSICAL standard of living, autarkic (continental US)")
    print("=" * W)
    a, f, ratios = r["avail"], r["footprint"], r["ratios"]

    print("Per-capita availability vs today's average-person footprint:")
    print(f"  {'resource':<34}{'available':>14}{'footprint':>12}{'ratio':>8}")
    rows = [
        ("labour (h/yr)",              a["labour_h"],                f["labour_h"], ratios["labour"]),
        ("energy CURRENT build (GJ)",  a["energy_GJ_current_build"], f["energy_GJ"], ratios["energy (current build)"]),
        ("energy FULL potential (GJ)", a["energy_GJ_full_potential"],f["energy_GJ"], ratios["energy (full renewable potential)"]),
        ("land (ha)",                  a["land_ha"],                 f["land_ha"], ratios["land"]),
        ("water (m3/yr)",              a["water_m3"],                f["water_m3"], ratios["water"]),
    ]
    for name, av, fp, ra in rows:
        flag = "  BINDS" if ra < 1 else "  room"
        print(f"  {name:<34}{av:>14,.0f}{fp:>12,.0f}{ra:>8.2f}{flag}")

    print("-" * W)
    bc, bcr = r["bind_current"]
    bp, bpr = r["bind_potential"]
    print(f"BINDING CONSTRAINT, today's sustainable build : {bc}  (ceiling {bcr:.2f}x footprint)")
    print(f"BINDING CONSTRAINT, full renewable build-out  : {bp}  (ceiling {bpr:.2f}x footprint)")
    print(f"Critical minerals: US >50% net-import-reliant for ~{p.critical_minerals_import_reliant} "
          f"commodities (USGS)")
    print(f"                   -> the genuine autarky loss; substitute / recycle / forgo.")
    print("-" * W)
    print("EGALITARIAN UNIVERSAL BUNDLE (distributed under 24/F; consumption is")
    print(f"naturally bounded, mean/median ~{p.footprint_mean_over_median:.2f}):")
    print("  * labour, water        : ABUNDANT -- everyone at/above today's median easily")
    print("  * food / land          : ADEQUATE but the tightest resource (~1.1x); the US")
    print("                           is a net food exporter, so it feeds itself -- but a")
    print("                           higher-meat diet makes land bind. Diet is the lever.")
    print("  * energy               : the swing -- ~1/5 of today's per-capita at current")
    print("                           build; ~today's mean once the renewable build-out")
    print("                           is done (which itself needs land + minerals)")
    print("  * critical minerals    : a short forgone/substitute list -- the real bite")
    print("=" * W)
    print("Headline: autarkic America is NOT labour-, land-, water-, or food-limited.")
    print("Its egalitarian physical ceiling is set by the ENERGY TRANSITION and a handful")
    print("of critical minerals. Finish the transition -> a universal standard ~ today's")
    print("mean. Don't -> per-capita energy falls to ~1/5. Labour was never the limit.")
    print("=" * W)
    return r


# ---------------------------------------------------------------------------
# self-tests
# ---------------------------------------------------------------------------

def test_labour_not_binding():
    r = compute()
    assert r["ratios"]["labour"] > 1.5, "labour pool should dwarf the footprint"
    print(f"[ok] labour ratio {r['ratios']['labour']:.2f} (abundant -- self-care pool dominates)")


def test_water_food_room():
    r = compute()
    assert r["ratios"]["water"] > 2, "water should be abundant nationally"
    print(f"[ok] water ratio {r['ratios']['water']:.1f} (abundant)")


def test_energy_is_the_swing():
    """Energy binds hard at current build but is abundant at full potential."""
    r = compute()
    assert r["ratios"]["energy (current build)"] < 0.5, "current-build energy should bind hard"
    assert r["ratios"]["energy (full renewable potential)"] > 1.0, "potential should relieve it"
    print(f"[ok] energy: current build {r['ratios']['energy (current build)']:.2f}x (BINDS) -> "
          f"full potential {r['ratios']['energy (full renewable potential)']:.1f}x (room)")


def test_binding_switches_with_buildout():
    """The binding constraint at current build is energy; after build-out it isn't."""
    r = compute()
    assert "energy" in r["bind_current"][0], "energy should bind at current build"
    assert "energy" not in r["bind_potential"][0], "after build-out, energy shouldn't bind"
    print(f"[ok] binding switches: {r['bind_current'][0]} -> {r['bind_potential'][0]} after build-out")


def test_egalitarian_cheap():
    """Physical consumption is naturally bounded, so egalitarian ~ near the mean."""
    assert AutarkyParams().footprint_mean_over_median < 1.5
    print(f"[ok] mean/median {AutarkyParams().footprint_mean_over_median:.2f} -- egalitarian costs little")


def run_tests():
    test_labour_not_binding()
    test_water_food_room()
    test_energy_is_the_swing()
    test_binding_switches_with_buildout()
    test_egalitarian_cheap()
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
