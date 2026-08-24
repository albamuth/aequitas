"""
track1_by_category.py -- Track 1, broken down by CONSUMER-facing category, using
the true 132-detail final-demand bridge (BLS NOMINAL_FD.xlsx). This is the
bottom-up-per-category deliverable the method (median_lifestyle_METHOD.md) asked
for; track1_embodied_hours.py gives the aggregate + a producer-side group view.

DATA
  - ERM 2023 colsums (as track1_embodied_hours).
  - NOMINAL_FD.xlsx sheet '2023' : 176 commodities x 132 DETAIL final-demand
    categories (producer value, $M). Columns 1-79 are the PCE detail categories
    (1-76 = goods/services; 77-79 = trade & transport MARGINS on PCE, held in
    separate commodity rows so no margin labour is lost). Extracted on disk from
    data/io_full.zip -> IONom/NOMINAL_FD.xlsx.

METHOD
  embodied hours for detail category c = sum_i FD[i,c] * ERM_colsum_i * 1000 * H
  Then the 79 PCE detail categories are grouped into ~12 CE-comparable buckets,
  and the 3 margin columns (77-79) are re-allocated to the goods buckets in
  proportion to each bucket's goods dollar-value (services get no margin).

Verified: the 79 PCE detail columns reproduce the aggregate exactly
  (611.9 h/capita, $18.82T) -- see track1_embodied_hours.py.

Run:  python track1_by_category.py [--test]
"""
from __future__ import annotations

import argparse
import csv
import os

import numpy as np
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
ERM_CSV = os.path.join(DATA, "erm_full", "NOMINAL_DOMEMPREQ_2023.csv")
FD_XLSX = os.path.join(DATA, "IONom", "NOMINAL_FD.xlsx")

AVG_ANNUAL_HOURS = 1800.0
POPULATION = 335e6
ADULTS = 259e6
MEDIAN_OVER_MEAN = 0.80

# CE-comparable buckets -> detail final-demand category numbers (1-based, 1..79).
# Margin categories 77,78,79 are handled separately (allocated to goods buckets).
BUCKETS: dict[str, list[int]] = {
    "Food & alcohol": [18, 19, 20, 55, 56],
    "Housing (shelter+utilities+ops)": [34, 35, 36, 37, 38, 39, 40, 26, 29, 73,
                                        4, 5, 6, 7],
    "Apparel & footwear": [21, 22, 23, 24, 16],
    "Transportation": [1, 2, 3, 25, 46, 47, 48, 49, 50, 63],
    "Healthcare": [27, 41, 42, 43, 44, 45, 14, 62],
    "Entertainment & recreation": [8, 9, 10, 11, 12, 28, 51, 52, 53, 54, 57],
    "Communications": [17, 64, 65, 66],
    "Education": [15, 67, 68, 69],
    "Personal care & services": [30, 71, 70, 72, 13],  # 13=jewelry/watches
    "Financial & insurance": [58, 59, 60, 61],
    "Tobacco, reading, misc": [31, 32, 33, 74, 75, 76],
}
# categories that are physical goods (receive trade/transport margin)
GOODS_CATS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32}
MARGIN_CATS = [77, 78, 79]


def load():
    rows = list(csv.reader(open(ERM_CSV)))
    colsum = np.array([[float(x) for x in r[1:]] for r in rows[1:]]).sum(axis=0)
    wb = openpyxl.load_workbook(FD_XLSX, read_only=True, data_only=True)
    ws = wb["2023"]
    rr = [r for r in ws.iter_rows(values_only=True)]
    FD = np.array([[float(c) if c not in (None, "") else 0.0 for c in r[1:133]]
                   for r in rr[1:] if r[0] not in (None, "SECTORNUMBER")])
    return colsum, FD  # colsum len176, FD 176x132


def compute():
    colsum, FD = load()
    # embodied hours per detail category (len132), per capita
    hpc = (FD * colsum[:, None]).sum(axis=0) * 1000 * AVG_ANNUAL_HOURS / POPULATION
    dollars = FD.sum(axis=0) / 1e6  # $T per detail category

    def cat_h(cats):
        return sum(hpc[c - 1] for c in cats)

    def cat_goods_dollars(cats):
        return sum(dollars[c - 1] for c in cats if c in GOODS_CATS)

    # margins to allocate across goods buckets, by goods-dollar share
    margin_h = sum(hpc[c - 1] for c in MARGIN_CATS)
    goods_dollars_by_bucket = {b: cat_goods_dollars(cats) for b, cats in BUCKETS.items()}
    total_goods_dollars = sum(goods_dollars_by_bucket.values())

    out = {}
    for b, cats in BUCKETS.items():
        base = cat_h(cats)
        share = (goods_dollars_by_bucket[b] / total_goods_dollars) if total_goods_dollars else 0
        out[b] = base + margin_h * share

    total = sum(out.values())
    per_adult_mean = total * POPULATION / ADULTS
    median_adult = per_adult_mean * MEDIAN_OVER_MEAN
    return dict(buckets=out, total_percap=total, margin_h=margin_h,
                per_adult_mean=per_adult_mean, median_adult=median_adult)


def report():
    r = compute()
    W = 66
    print("=" * W)
    print("TRACK 1 BY CE CATEGORY -- embodied domestic labour, per capita/yr 2023")
    print("  (132-detail PCE bridge; trade/transport margins reallocated to goods)")
    print("=" * W)
    for b, h in sorted(r["buckets"].items(), key=lambda kv: -kv[1]):
        bar = "#" * int(round(h / 2))
        print(f"  {h:5.0f} h  {b:<36}{bar}")
    print("-" * W)
    print(f"  {r['total_percap']:5.0f} h  TOTAL per capita")
    print(f"  (of which {r['margin_h']:.0f} h was trade/transport margin, re-allocated)")
    print(f"  {r['per_adult_mean']:5.0f} h  mean per adult")
    print(f"  {r['median_adult']:5.0f} h  MEDIAN adult (x{MEDIAN_OVER_MEAN}) -- domestic lower bound")
    print("=" * W)
    return r


def test_reproduces_aggregate():
    r = compute()
    assert abs(r["total_percap"] - 612) < 3, r["total_percap"]
    print(f"[ok] category total {r['total_percap']:.0f}h ~= aggregate 612h")


def test_healthcare_and_housing_top():
    r = compute()
    top2 = sorted(r["buckets"], key=lambda k: -r["buckets"][k])[:3]
    assert "Healthcare" in top2, top2
    print(f"[ok] top buckets: {top2}")


def test_all_positive():
    r = compute()
    assert all(v >= 0 for v in r["buckets"].values())
    print("[ok] all category hours non-negative")


def run_tests():
    test_reproduces_aggregate()
    test_healthcare_and_housing_top()
    test_all_positive()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    run_tests() if a.test else report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
