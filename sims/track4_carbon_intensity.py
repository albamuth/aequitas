"""
track4_carbon_intensity.py -- real EEIO labour intensity of carbon remediation,
replacing the economy-average 0.0105 h/$ shortcut in track4_pollution.py.

Carbon capture is not an average activity. Nature-based sequestration is forestry/
agriculture labour (labour-intensive). Engineered Direct Air Capture (DAC) is
dominated by ENERGY and CAPITAL, which are labour-LIGHT -- so a dollar of DAC
commands fewer human hours than an average dollar.

We build each method as a basket of spending across real BLS sectors and apply each
sector's TOTAL (direct+indirect) employment multiplier from the Employment
Requirements Matrix (2023). The cost shares are representative, from the DAC/NBS
cost literature (energy ~40-50%, capital ~30-40%, O&M/chemicals ~15-20% for DAC),
and are FLAGGED -- they are the remaining assumption; the multipliers are measured.

    intensity(h/$) = SUM_s [ share_s x jobs_per_$M(s) ] x hours_per_job / 1e6

Run:  python track4_carbon_intensity.py
"""
from __future__ import annotations

from track1_labour import load_erm

HOURS_PER_JOB = 1750.0

# (sector_id, cost_share) baskets. Sector titles for reference:
#   3 Forestry · 6 Support ag/forestry · 12 Electric power · 13 Nat-gas distribution
#   15 Construction · 38 Chemical mfg · 54 Machinery mfg · 79 misc mfg
#   88 Truck transport · 111 Architectural/engineering · 129 Waste mgmt & remediation
BASKETS = {
    "nature-based ($50/t afforestation)": {
        "cost_per_ton": 50.0,
        "mix": [(6, 0.50), (3, 0.15), (111, 0.15), (88, 0.10), (79, 0.10)],
        # planting/tending 50%, forestry 15%, MRV/monitoring 15%, transport 10%, materials 10%
    },
    "DAC ($500/t direct air capture)": {
        "cost_per_ton": 500.0,
        "mix": [(12, 0.40), (15, 0.20), (13, 0.10), (54, 0.10), (38, 0.10), (129, 0.10)],
        # electricity 40%, plant capital 20%, heat/gas 10%, machinery 10%,
        # sorbent chemicals 10%, O&M/remediation ops 10%
    },
}

SECTOR_TITLE = {
    3: "Forestry", 6: "Support activities ag/forestry", 12: "Electric power",
    13: "Natural gas distribution", 15: "Construction", 38: "Chemical mfg",
    54: "Machinery mfg", 79: "Other misc mfg", 88: "Truck transportation",
    111: "Architectural/engineering", 129: "Waste mgmt & remediation",
}


def main():
    sector_ids, jobs_per_M = load_erm()
    jpm = {sid: jobs_per_M[i] for i, sid in enumerate(sector_ids)}

    W = 74
    results = {}
    for name, spec in BASKETS.items():
        print("=" * W)
        print(name)
        print("-" * W)
        print(f"  {'sector':<34}{'share':>7}{'jobs/$M':>9}{'contrib':>9}")
        weighted = 0.0
        for sid, share in spec["mix"]:
            contrib = share * jpm[sid]
            weighted += contrib
            print(f"  {SECTOR_TITLE.get(sid, str(sid)):<34}"
                  f"{share*100:>6.0f}%{jpm[sid]:>9.1f}{contrib:>9.2f}")
        intensity = weighted * HOURS_PER_JOB / 1e6
        h_per_ton = spec["cost_per_ton"] * intensity
        results[name] = (weighted, intensity, h_per_ton)
        print("-" * W)
        print(f"  weighted jobs/$M           : {weighted:.2f}")
        print(f"  -> intensity               : {intensity:.5f} h/$  "
              f"(vs 0.01050 economy-avg shortcut)")
        print(f"  x ${spec['cost_per_ton']:.0f}/ton               : "
              f"{h_per_ton:.3f} h/ton CO2")
        print()

    # apply to Track 4's 8.3 t CO2 + 1.6 h wastewater
    CO2, WW = 8.3, 1.6
    print("=" * W)
    print("REVISED Track 4 (real carbon intensity)")
    print("-" * W)
    for name, (_, _, hpt) in results.items():
        carbon = CO2 * hpt
        print(f"  {name.split(' (')[0]:<14}: carbon {carbon:5.1f} + wastewater "
              f"{WW} = {carbon+WW:5.1f} h/adult")
    lo = CO2 * results["nature-based ($50/t afforestation)"][2] + WW
    hi = CO2 * results["DAC ($500/t direct air capture)"][2] + WW
    print("-" * W)
    print(f"  TRACK 4 range : {lo:.0f} - {hi:.0f} h/adult   (mid ~{(lo+hi)/2:.0f})")
    print(f"  was (shortcut): 6 - 45 h/adult (mid ~26)")
    print("=" * W)
    return lo, hi


if __name__ == "__main__":
    main()
