"""
track1_embodied_hours.py -- Track 1 of the median-adult lifestyle cost, done
RIGOROUSLY from measured supply chains (no blanket labour/$ ratio).

WHAT THIS COMPUTES
  The domestic human labour-hours embodied, per year, in the personal
  consumption of a median US adult -- the real-world anchor for the
  disparity-ceiling proof (Foundations Sec.7.5; the 24/F band).

  This SUPERSEDES the top-down `median_lifestyle.py`, which *assumed* the
  labour allocation (pce_share x blanket hours). Here the allocation is
  MEASURED: the BLS Employment Requirements Matrix (ERM) already carries the
  full direct+indirect domestic supply chain, and we apply it to the actual
  2023 producer-value composition of US personal consumption (PCE).

DATA (all on disk, 2023, one internally-consistent year; memory
      [[median-lifestyle-data-sources]]):
  1. ERM 2023 -- data/erm_full/NOMINAL_DOMEMPREQ_2023.csv (176x176).
     cell(i,j) = THOUSANDS of jobs (direct+indirect, DOMESTIC/import-adjusted)
     per $1M of final demand for commodity j. Column-sum_j = total embodied
     jobs per $1M of commodity j delivered to final demand.
  2. Final-demand aggregates 2023 -- data/io/NOMINAL_FDAGG.xlsx, sheet '2023'.
     Column 1 = PCE, a 176-vector of PRODUCER-value personal consumption in $M
     (sum = $18.82T = actual 2023 US PCE). Producer value already has trade &
     transport margins reallocated to the retail/wholesale/transport rows, so
     retail labour is counted where it physically occurs -- no margin is lost.
  3. Sector labels -- data/erm_sector_names.json (from SectorPlan2034.xlsx).

THE ARITHMETIC (per commodity i)
  jobs_i  = PCE_i[$M] * colsum_i[thousand-jobs/$M] * 1000
  hours_i = jobs_i * AVG_ANNUAL_HOURS
  per-capita_i = hours_i / POPULATION
  Sum over i -> total domestic embodied labour-hours per capita/yr.

WHY THIS IS A DOMESTIC LOWER BOUND
  The ERM is import-adjusted: it counts only labour performed *in the US*.
  The foreign hours embodied in imports (apparel, electronics) are Track 3 and
  ADD to this figure. So Track 1's number is a floor on total embodied labour.

Run:  python track1_embodied_hours.py
      python track1_embodied_hours.py --test
"""
from __future__ import annotations

import argparse
import csv
import json
import os

import numpy as np

try:
    import openpyxl
except ImportError:  # pragma: no cover
    openpyxl = None

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
ERM_CSV = os.path.join(DATA, "erm_full", "NOMINAL_DOMEMPREQ_2023.csv")
FDAGG = os.path.join(DATA, "io", "NOMINAL_FDAGG.xlsx")
NAMES_JSON = os.path.join(DATA, "erm_sector_names.json")

# --- documented constants (overridable) --------------------------------------
AVG_ANNUAL_HOURS = 1800.0   # hours per job-year (OECD US ~1,811; refine per
                            #   sector with BLS avg weekly hours -- flagged).
POPULATION = 335e6          # US resident pop ~2023 (Census ~334.9M).
ADULTS = 259e6              # US 18+ pop ~2023 (Census ~258.3M).
MEDIAN_OVER_MEAN = 0.80     # consumption median/mean (CE spread; less unequal
                            #   than income, Gini ~0.3-0.4). Refine from CE.


def load_erm_colsums() -> np.ndarray:
    """Return the 176-vector of embodied jobs per $1M FD (thousand-job units)."""
    rows = list(csv.reader(open(ERM_CSV)))
    M = np.array([[float(x) for x in r[1:]] for r in rows[1:]])
    assert M.shape == (176, 176), f"ERM not 176x176: {M.shape}"
    return M.sum(axis=0)


def load_pce_vector() -> np.ndarray:
    """Return the 176-vector of 2023 PCE producer-value in $M (FDAGG col 1)."""
    if openpyxl is None:
        raise RuntimeError("openpyxl required to read FDAGG")
    wb = openpyxl.load_workbook(FDAGG, read_only=True, data_only=True)
    ws = wb["2023"]
    rows = [r for r in ws.iter_rows(values_only=True)]
    pce = np.array([float(r[1]) for r in rows[1:]
                    if r[0] not in (None, "SECTORNUMBER")])
    assert len(pce) == 176, f"PCE not len-176: {len(pce)}"
    return pce


def load_names() -> dict[int, str]:
    raw = json.load(open(NAMES_JSON))
    return {int(k): v for k, v in raw.items()}


# --- readable groupings of the 176 commodities (sector-number ranges) --------
# Coarse consumption groups for the breakdown chart. Sector numbers per
# SectorPlan2034 "Industry Commodity Sectors".
GROUPS: dict[str, range | list] = {
    "Food & agriculture": list(range(1, 7)) + list(range(16, 27)),   # farms+food mfg+bev+tobacco
    "Apparel & leather (mfg)": [27, 28, 29, 30],
    "Energy & fuels": [7, 8, 12, 13, 37, 38, 40],                    # oil/gas/coal, elec, gas dist, petroleum, chem
    "Vehicles & transport equip": list(range(60, 66)),
    "Other manufacturing": list(range(31, 37)) + [39, 41, 42, 43]
        + list(range(44, 60)) + list(range(66, 80)),
    "Construction": [15],
    "Wholesale & retail trade": list(range(80, 90)),
    "Transport & warehousing": list(range(90, 100)),
    "Information & communications": list(range(100, 108)),
    "Finance, insurance, real estate": list(range(108, 116)),
    "Professional & business services": list(range(116, 133)),
    "Healthcare": list(range(133, 143)),
    "Education": list(range(143, 147)),
    "Arts, recreation, food service, hotels": list(range(147, 156)),
    "Other services & government": list(range(156, 177)),
}


def compute() -> dict:
    colsum = load_erm_colsums()
    pce = load_pce_vector()
    jobs = pce * colsum * 1000.0                    # jobs per commodity
    hours = jobs * AVG_ANNUAL_HOURS                 # hours per commodity
    h_percap = hours / POPULATION                   # per-capita hours/commodity

    total_jobs = jobs.sum()
    percap = h_percap.sum()                         # mean domestic embodied h/cap
    # per-adult: attribute all PCE labour to adults (children's consumption is
    #   part of the cost of supporting an adult household). mean per adult:
    per_adult_mean = hours.sum() / ADULTS
    median_adult = per_adult_mean * MEDIAN_OVER_MEAN

    names = load_names()
    order = np.argsort(h_percap)[::-1]
    top = [(names[j + 1], float(h_percap[j])) for j in order[:15]]

    groups = {}
    assigned = set()
    for label, secs in GROUPS.items():
        idx = [s - 1 for s in secs]
        assigned.update(secs)
        groups[label] = float(h_percap[idx].sum())
    # any sector not explicitly grouped (e.g. mining, water/sewage) -> catch-all
    leftover = [s - 1 for s in range(1, 177) if s not in assigned]
    if leftover:
        groups["Other services & government"] += float(h_percap[leftover].sum())

    return dict(
        total_pce_embodied_jobs=total_jobs,
        percap_mean_domestic=percap,
        per_adult_mean=per_adult_mean,
        median_adult_domestic=median_adult,
        top_commodities=top,
        groups=groups,
        pce_total_trillion=pce.sum() / 1e6,
    )


def report() -> dict:
    r = compute()
    W = 74
    print("=" * W)
    print("TRACK 1 -- DOMESTIC EMBODIED LABOUR IN US PERSONAL CONSUMPTION, 2023")
    print("  (measured supply chains: BLS ERM x actual PCE producer-value mix)")
    print("=" * W)
    print(f"  PCE total (check = $18.82T)     : ${r['pce_total_trillion']:.2f}T")
    print(f"  PCE-embodied jobs (dir+indir)   : {r['total_pce_embodied_jobs']/1e6:.1f} M")
    print("-" * W)
    print(f"  MEAN embodied h/capita/yr       : {r['percap_mean_domestic']:.0f} h")
    print(f"  MEAN embodied h per ADULT/yr    : {r['per_adult_mean']:.0f} h")
    print(f"  MEDIAN ADULT h/yr (x{MEDIAN_OVER_MEAN})       : {r['median_adult_domestic']:.0f} h"
          "   <-- Track-1 headline (domestic LOWER BOUND)")
    print("-" * W)
    print("  Where the hours sit (per-capita h/yr, by group):")
    for label, h in sorted(r["groups"].items(), key=lambda kv: -kv[1]):
        bar = "#" * int(round(h / 2))
        print(f"    {h:5.0f}  {label:<38} {bar}")
    print("-" * W)
    print("  Top commodities:")
    for name, h in r["top_commodities"]:
        print(f"    {h:5.1f} h  {name[:48]}")
    print("=" * W)
    print("  Domestic-only (ERM is import-adjusted): Track 3 adds foreign hours")
    print("  embodied in imports on top of this floor. Track 2 (durables) is")
    print("  already inside PCE here via producer value; the holding-time split")
    print("  (Foundations Sec.6.2b) re-annualises it and is a Track-2 refinement.")
    print("=" * W)
    return r


# --- self-tests --------------------------------------------------------------
def test_pce_total():
    r = compute()
    assert 18.0 < r["pce_total_trillion"] < 19.5, r["pce_total_trillion"]
    print(f"[ok] PCE total ${r['pce_total_trillion']:.2f}T ~= 2023 actual $18.8T")


def test_jobs_plausible():
    r = compute()
    j = r["total_pce_embodied_jobs"] / 1e6
    assert 90 < j < 140, f"PCE-embodied jobs {j:.0f}M implausible"
    print(f"[ok] PCE-embodied jobs {j:.0f}M (< US total ~161M, PCE ~68% GDP)")


def test_percap_range():
    r = compute()
    p = r["percap_mean_domestic"]
    assert 400 < p < 900, f"per-capita {p:.0f}h implausible"
    print(f"[ok] mean domestic embodied {p:.0f} h/capita/yr")


def test_groups_sum():
    r = compute()
    s = sum(r["groups"].values())
    assert abs(s - r["percap_mean_domestic"]) < 1.0, (s, r["percap_mean_domestic"])
    print(f"[ok] group breakdown sums to total ({s:.0f}h) -- partition covers all 176")


def test_services_dominate():
    """Labour concentrates in labour-intensive services, not fuels/materials."""
    r = compute()
    g = r["groups"]
    assert g["Healthcare"] > g["Energy & fuels"], "healthcare should out-labour fuels"
    print(f"[ok] healthcare {g['Healthcare']:.0f}h >> energy/fuels "
          f"{g['Energy & fuels']:.0f}h (labour is in services)")


def run_tests():
    test_pce_total()
    test_jobs_plausible()
    test_percap_range()
    test_groups_sum()
    test_services_dominate()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
    else:
        report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
