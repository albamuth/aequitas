"""
track3_exiobase.py -- Track 3 RIGOROUS: foreign labour-hours embodied in US
household consumption, from the EXIOBASE 3 global MRIO (2022, pxp).

Replaces the wide wage/margin ballpark in track3_imports.py with a measured figure
that has the actual foreign supply chains and country-of-origin wages baked in.

Method (standard consumption-based footprint, split by origin):
    x_driven      = L @ Y_us_households        # world output driven by US HH demand
    hours_sector  = S_emp * x_driven           # employment-hours by region-sector
    foreign_hours = sum(hours_sector where origin region != US)
    per_adult     = foreign_hours / US adults

Currency cancels (S_emp is hours per M.EUR, Y is M.EUR) so no EUR/USD conversion.
Cross-check: the US-origin part should be the same order as Track 1's ~199 B h.

Run:  python track3_exiobase.py <path-to-IOT_2022_pxp.zip>
"""
import sys
import warnings

import numpy as np
import pymrio

warnings.filterwarnings("ignore")

US_ADULTS = 258e6


def main(zip_path):
    print("parsing EXIOBASE...", flush=True)
    exio = pymrio.parse_exiobase3(path=zip_path)

    # gross output x, technical coefficients A, Leontief inverse L
    print("computing Leontief inverse (this is the slow part)...", flush=True)
    exio.calc_all()                      # populates x, A, L, and extension S/M/D
    L = exio.L.values                    # (n x n)

    emp = exio.employment
    S = emp.S                            # direct intensity per unit output
    hour_rows = [r for r in S.index if str(r).startswith("Employment hours")]
    S_emp = S.loc[hour_rows].sum(axis=0).values          # hours-intensity per M.EUR
    # unit of the HOURS rows specifically (not the persons rows)
    unit = str(emp.unit.loc[hour_rows[0]].iloc[0]) if hasattr(emp, "unit") else "?"
    print(f"employment-hours rows: {len(hour_rows)}  unit: {unit}", flush=True)

    # US household final demand vector over ALL region-products
    Y = exio.Y
    ycol = [c for c in Y.columns if c[0] == "US" and "households" in c[1].lower()][0]
    Y_us_hh = Y[ycol].values

    x_driven = L @ Y_us_hh                                # M.EUR output by region-sector
    hours_sector = S_emp * x_driven                       # emp-hours (in `unit`) by sector

    regions = Y.index.get_level_values(0).values
    is_us = regions == "US"
    domestic = hours_sector[is_us].sum()
    foreign = hours_sector[~is_us].sum()
    total = hours_sector.sum()

    # EXIOBASE employment-hours are in M.hr (millions of hours) -> x1e6 for hours
    scale = 1e6 if "hr" in str(unit).lower() else 1.0
    print(f"raw sums (unit {unit}): domestic={hours_sector[is_us].sum():,.0f} "
          f"foreign={hours_sector[~is_us].sum():,.0f}", flush=True)
    dom_h, for_h, tot_h = domestic * scale, foreign * scale, total * scale

    print("=" * 70)
    print("TRACK 3 (EXIOBASE 2022) -- labour embodied in US household consumption")
    print("=" * 70)
    print(f"  DOMESTIC (US) hours : {dom_h/1e9:8.1f} B h/yr   "
          f"(cross-check vs Track1 ~199B)")
    print(f"  FOREIGN hours       : {for_h/1e9:8.1f} B h/yr")
    print(f"  total footprint     : {tot_h/1e9:8.1f} B h/yr")
    print(f"  foreign share       : {100*for_h/tot_h:8.1f} %")
    print("-" * 70)
    print(f"  FOREIGN per US adult: {for_h/US_ADULTS:8.0f} h/yr   <- Track 3 rigorous")
    print(f"  domestic per adult  : {dom_h/US_ADULTS:8.0f} h/yr")
    print("=" * 70)

    # top foreign origin regions
    order = np.argsort(hours_sector)[::-1]
    seen, shown = {}, 0
    for idx in order:
        r = regions[idx]
        if r == "US":
            continue
        seen[r] = seen.get(r, 0) + hours_sector[idx]
    top = sorted(seen.items(), key=lambda kv: kv[1], reverse=True)[:8]
    print("top foreign origin regions (B h/yr):")
    for r, h in top:
        print(f"    {r}: {h*scale/1e9:.1f}")
    return for_h / US_ADULTS


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "IOT_2022_pxp.zip"
    main(path)
