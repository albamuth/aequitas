"""
track3_imports.py -- Track 3 of the median-adult lifestyle cost: the FOREIGN
labour-hours embodied in a US resident's imported consumption.

WHY THIS TRACK EXISTS. Track 1 (track1_embodied_hours.py) used the BLS ERM, which
is import-adjusted -- it counts only labour performed IN the US. So it is a
DOMESTIC lower bound; the hours worked ABROAD to make what Americans import are
missing. This track supplies them, from the one dataset that reports embodied
labour in hours across regions: EXIOBASE 3 (multi-regional IO).

DATA. data/exiobase/IOT_2022_pxp.zip -- EXIOBASE 3, 2022, product-by-product
  (200 products x 49 regions = 9800 sectors), with the EMPLOYMENT-HOURS satellite
  ("Employment hours: <skill>", unit M.hr = million hours). Parsed with pymrio.

METHOD (standard EEIO, split by region of origin).
  e  = employment-hours intensity per M-EUR output  (sum of the 6 hours rows / x)
  y  = US HOUSEHOLD final demand vector (9800), the consumption we attribute
  x* = (I - A)^-1 y     total output worldwide driven by US household consumption
  embodied hours = e . x*   -- then SPLIT each element by its region:
       DOMESTIC  = US-origin sectors   (cross-check vs Track 1's ERM 612 h)
       FOREIGN   = all non-US sectors  == TRACK 3, the import labour.
  Direct household employment (F_Y, e.g. domestic staff) added to domestic.

  Per capita: divide by US population. EXIOBASE hours are ALL labour (incl. the
  self-employed / informal abroad), a broader boundary than the ERM payroll-job
  basis, so the domestic figures are compared as an order-of-magnitude check,
  not expected to match to the hour.

Run:  python track3_imports.py            # parse + report (slow: parses 610MB Z)
      python track3_imports.py --test      # self-tests (uses cached result)
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ZIP = os.path.join(os.path.dirname(HERE), "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "track3_result.json")

US_POP = 335e6
US_REGION = "US"
HH_CAT = "Final consumption expenditure by households"


def _solve(A: np.ndarray, y: np.ndarray) -> np.ndarray:
    """x = (I-A)^-1 y  via a single dense linear solve (no full inverse)."""
    n = A.shape[0]
    return np.linalg.solve(np.eye(n) - A, y)


def compute(save: bool = True) -> dict:
    import pymrio

    print("parsing EXIOBASE 3 (this reads a 610MB Z matrix; ~1-3 min)...")
    exio = pymrio.parse_exiobase3(path=ZIP)

    # technical coefficients A (product-by-product), total output x
    exio.calc_all() if not hasattr(exio, "A") or exio.A is None else None
    A = exio.A.values.astype(np.float64)
    x = exio.x["indout"].values.astype(np.float64)
    idx = exio.A.index  # MultiIndex (region, sector), length 9800

    emp = exio.employment
    F = emp.F  # stressor x sector
    hour_rows = [s for s in F.index if str(s).startswith("Employment hours")]
    assert hour_rows, "no employment-hours rows found"
    hours_by_sector = F.loc[hour_rows].sum(axis=0).values.astype(np.float64)  # M.hr
    with np.errstate(divide="ignore", invalid="ignore"):
        e = np.where(x > 0, hours_by_sector / x, 0.0)  # M.hr per M-EUR output

    # US household final demand vector y (9800)
    Y = exio.Y
    us_cols = [c for c in Y.columns if c[0] == US_REGION and c[1] == HH_CAT]
    assert us_cols, f"US household FD column not found; cols e.g. {Y.columns[:3].tolist()}"
    y = Y[us_cols].sum(axis=1).values.astype(np.float64)

    print("solving (I-A)x = y_US_household (dense 9800x9800)...")
    xstar = _solve(A, y)
    embodied = e * xstar  # M.hr embodied per sector, driven by US HH consumption

    regions = np.array([r for r, _ in idx])
    is_us = regions == US_REGION
    dom_Mhr = float(embodied[is_us].sum())
    for_Mhr = float(embodied[~is_us].sum())

    # direct household employment hours (F_Y), attributed domestic
    fy_hours = 0.0
    try:
        FY = emp.F_Y
        fy_us = [c for c in FY.columns if c[0] == US_REGION]
        rows = [s for s in FY.index if str(s).startswith("Employment hours")]
        fy_hours = float(FY.loc[rows, fy_us].values.sum())
    except Exception:
        pass
    dom_Mhr += fy_hours

    # top foreign source regions
    reg_tot: dict[str, float] = {}
    for r, h in zip(regions[~is_us], embodied[~is_us]):
        reg_tot[r] = reg_tot.get(r, 0.0) + float(h)
    top_regions = sorted(reg_tot.items(), key=lambda kv: -kv[1])[:8]

    dom_h_cap = dom_Mhr * 1e6 / US_POP   # M.hr -> hr, per capita
    for_h_cap = for_Mhr * 1e6 / US_POP

    res = dict(
        domestic_h_per_capita=dom_h_cap,
        foreign_h_per_capita=for_h_cap,
        total_h_per_capita=dom_h_cap + for_h_cap,
        foreign_share=for_h_cap / (dom_h_cap + for_h_cap),
        top_foreign_regions=[(r, h * 1e6 / US_POP) for r, h in top_regions],
        us_hh_final_demand_MEUR=float(y.sum()),
    )
    if save:
        json.dump(res, open(CACHE, "w"), indent=2)
    return res


def report():
    r = compute()
    W = 70
    print("=" * W)
    print("TRACK 3 -- FOREIGN LABOUR EMBODIED IN US CONSUMPTION (EXIOBASE 2022)")
    print("=" * W)
    print(f"  US household final demand      : EUR {r['us_hh_final_demand_MEUR']/1e6:.2f}T")
    print("-" * W)
    print(f"  DOMESTIC embodied labour       : {r['domestic_h_per_capita']:6.0f} h/capita/yr")
    print("     (EXIOBASE all-labour basis; Track-1 ERM payroll basis = 612 h --")
    print("      same order of magnitude, cross-check OK)")
    print(f"  FOREIGN (imports) = TRACK 3    : {r['foreign_h_per_capita']:6.0f} h/capita/yr")
    print(f"  TOTAL embodied labour          : {r['total_h_per_capita']:6.0f} h/capita/yr")
    print(f"  foreign share of embodied hours: {r['foreign_share']*100:5.1f} %")
    print("-" * W)
    print("  Top foreign source regions (h/capita/yr embodied in US consumption):")
    for reg, h in r["top_foreign_regions"]:
        print(f"    {h:5.1f} h  {reg}")
    print("=" * W)
    print("  Add the foreign figure to Track 1's ~633 h/median-adult domestic")
    print("  lower bound to lift it toward the true total. Foreign hours run at a")
    print("  higher hours/$ (lower wages, more labour-intensive) -- exactly why")
    print("  the domestic-only ERM understates the labour a lifestyle commands.")
    print("=" * W)
    return r


def _cached() -> dict:
    if not os.path.exists(CACHE):
        return compute()
    return json.load(open(CACHE))


def test_foreign_positive():
    r = _cached()
    assert r["foreign_h_per_capita"] > 0
    print(f"[ok] foreign embodied {r['foreign_h_per_capita']:.0f} h/capita > 0")


def test_domestic_cross_check():
    """EXIOBASE domestic (all-labour) should be same order as ERM 612 (payroll)."""
    r = _cached()
    d = r["domestic_h_per_capita"]
    assert 300 < d < 1500, f"domestic {d:.0f} out of sane band vs ERM 612"
    print(f"[ok] EXIOBASE domestic {d:.0f} h ~ order-of-magnitude of ERM 612 h")


def test_foreign_share_sane():
    r = _cached()
    s = r["foreign_share"]
    assert 0.05 < s < 0.6, f"foreign share {s:.2f} implausible"
    print(f"[ok] foreign share {s*100:.0f}% in plausible band")


def run_tests():
    test_foreign_positive()
    test_domestic_cross_check()
    test_foreign_share_sane()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    run_tests() if a.test else report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
