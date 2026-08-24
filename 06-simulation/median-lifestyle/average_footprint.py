"""
average_footprint.py -- environmental footprint of the AVERAGE US person's
consumption, from EXIOBASE 3 (2022), the same L @ Y_us_households machinery used
for the labour footprint (track3_exiobase.py) -- just different satellites.

Reports the consumption-based footprint of US HOUSEHOLD final demand, per capita,
for CO2, materials, land, water, and energy, split domestic vs foreign.

Note on Aequitas: this is the FULL footprint a person's consumption DRIVES. Under
§3.2b most embodied pollution stays on producers; the consumer bears only their own
direct emissions (Track 4). Both views are useful -- this is "impact of the lifestyle."

Run:  python average_footprint.py <path-to-IOT_2022_pxp.zip>
"""
import sys
import warnings

import numpy as np
import pymrio

warnings.filterwarnings("ignore")
US_POP = 335e6

# extension -> list of stressor-row substrings to sum, and a friendly unit scale
WANT = {
    "air_emissions": (["CO2"], "CO2 (all sources)"),
    "material":      (["Domestic Extraction Used"], "material extraction"),
    "land":          ([""], "land use"),                 # [""] sums all land rows
    "water":         (["Water Consumption"], "water consumption"),
    "energy":        (["Energy use - Net"], "energy (net use)"),
}


def main(zip_path):
    print("parsing EXIOBASE...", flush=True)
    exio = pymrio.parse_exiobase3(path=zip_path)
    print("computing Leontief inverse...", flush=True)
    exio.calc_all()
    L = exio.L.values

    Y = exio.Y
    ycol = [c for c in Y.columns if c[0] == "US" and "households" in c[1].lower()][0]
    Y_us_hh = Y[ycol].values
    x_driven = L @ Y_us_hh
    regions = Y.index.get_level_values(0).values
    is_us = regions == "US"

    print("=" * 72)
    print("ENVIRONMENTAL FOOTPRINT of the AVERAGE US person's consumption (2022)")
    print("=" * 72)
    for ext_name, (subs, label) in WANT.items():
        try:
            ext = getattr(exio, ext_name)
        except AttributeError:
            continue
        S = ext.S
        rows = [r for r in S.index if any(s.lower() in str(r).lower() for s in subs)]
        if not rows:
            print(f"  [{label}] no rows matched {subs}")
            continue
        S_sum = S.loc[rows].sum(axis=0).values
        by_sector = S_sum * x_driven
        total = by_sector.sum()
        foreign = by_sector[~is_us].sum()
        dom = by_sector[is_us].sum()
        unit = str(ext.unit.loc[rows[0]].iloc[0]) if hasattr(ext, "unit") else "?"
        pc = total / US_POP
        print(f"  {label:<22} total {total:12.3e} {unit:<8} "
              f"per person {pc:10.3e} {unit}  (foreign {100*foreign/total:.0f}%)")
    print("=" * 72)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "IOT_2022_pxp.zip"
    main(path)
