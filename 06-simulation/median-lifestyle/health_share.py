"""
health_share.py -- healthcare's share of the 1,380 h median-lifestyle anchor,
and the range of anchors a trust network can reach by how it attributes care.

WHY
  Foundations uses 1,380 h/yr (labour a median US adult's consumption commands)
  as the median debit. Who carries a service's labour is a network's own rule
  (Pledges.md ruling 10). So the anchor is one reading, and this script gives
  the range.

PART A -- domestic, by where the jobs sit (BLS ERM x PCE, as Track 1)
  For each healthcare PCE category, split its embodied hours by the industry
  the jobs are in: care providers, drug makers, advertising, R&D, trade, other.
  This is where drug marketing and drug research show up.

PART B -- domestic + foreign (EXIOBASE, as Track 3)
  Health services embodied hours at home and abroad. Pharmaceuticals are not a
  separate EXIOBASE product (they sit inside 'Chemicals nec'), so drugs are
  taken from Part A and scaled by the whole-economy foreign ratio -- stated,
  not hidden.

Run:  python health_share.py [--test] [--no-exio]
"""
from __future__ import annotations

import argparse
import csv
import json
import os

import numpy as np
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
ERM_CSV = os.path.join(DATA, "erm_full", "NOMINAL_DOMEMPREQ_2023.csv")
FD_XLSX = os.path.join(DATA, "IONom", "NOMINAL_FD.xlsx")
EXIO_ZIP = os.path.join(DATA, "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "health_share_result.json")

H = 1800.0                  # hours per job-year, as Track 1
POP = 335e6
ANCHOR = 1380.0             # h / median adult / yr, MEDIAN_LIFESTYLE_RESULT.md
TOTAL_PER_CAP = 1276.18     # Tracks 1+3 per capita (track3_result.json)

# PCE detail categories (1-based), labels from FDSectorPlan2034.xlsx
HEALTH = {
    14: "Therapeutic appliances and equipment",
    27: "Pharmaceutical and other medical products",
    41: "Physician services",
    42: "Dental services",
    43: "Paramedical services",
    44: "Hospitals",
    45: "Nursing homes",
    62: "Net health insurance",
}
CARE_SERVICES = [41, 42, 43, 44, 45]
GOODS_CATS = set(range(1, 33))      # as track1_by_category.py
MARGIN_CATS = [77, 78, 79]
PCE_CATS = range(1, 80)

# ERM industry rows (1-based), labels from erm_sector_names.json
IND = {
    "care providers": list(range(133, 143)) + [172],
    "drug manufacturing": [39],
    "medical equipment manufacturing": [77],
    "advertising and PR": [116],
    "marketing research and other professional": [119],
    "scientific R&D": [115],
    "insurance": [103, 104],
    "wholesale and retail trade": [80, 81, 82, 83, 84],
}


def load():
    rows = list(csv.reader(open(ERM_CSV)))
    E = np.array([[float(x) for x in r[1:]] for r in rows[1:]])  # jobs/$M: industry x commodity
    wb = openpyxl.load_workbook(FD_XLSX, read_only=True, data_only=True)
    rr = list(wb["2023"].iter_rows(values_only=True))
    FD = np.array([[float(c) if c not in (None, "") else 0.0 for c in r[1:133]]
                   for r in rr[1:] if r[0] not in (None, "SECTORNUMBER")])
    return E, FD


def part_a():
    E, FD = load()
    # hours per capita by (industry, FD category)
    jobs = E @ FD                                   # industry x FD-category, thousand jobs
    hrs = jobs * 1000 * H / POP                     # h / capita
    col_h = hrs.sum(axis=0)
    dollars = FD.sum(axis=0)

    # trade/transport margin hours go to goods categories by goods-dollar share
    margin_h = sum(col_h[c - 1] for c in MARGIN_CATS)
    goods_d = sum(dollars[c - 1] for c in GOODS_CATS)
    margin_of = {c: margin_h * dollars[c - 1] / goods_d for c in GOODS_CATS}

    pce_total = sum(col_h[c - 1] for c in PCE_CATS)
    cats = {}
    for c, name in HEALTH.items():
        by_ind = {k: float(sum(hrs[i - 1, c - 1] for i in v)) for k, v in IND.items()}
        own = float(col_h[c - 1])
        m = margin_of.get(c, 0.0)
        by_ind["wholesale and retail trade"] += m
        tot = own + m
        by_ind["everything else"] = tot - sum(by_ind.values())
        cats[c] = dict(name=name, hours=tot, by_industry=by_ind)
    return dict(pce_total=float(pce_total), categories=cats,
                health_total=sum(v["hours"] for v in cats.values()))


def part_b():
    import pymrio
    print("parsing EXIOBASE 3 (~1-3 min)...")
    exio = pymrio.parse_exiobase3(path=EXIO_ZIP)
    exio.calc_all()
    A = exio.A.values.astype(np.float64)
    x = exio.x["indout"].values.astype(np.float64)
    idx = exio.A.index
    F = exio.employment.F
    rows = [s for s in F.index if str(s).startswith("Employment hours")]
    hrs = F.loc[rows].sum(axis=0).values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        e = np.where(x > 0, hrs / x, 0.0)
    Y = exio.Y
    cols = [c for c in Y.columns if c[0] == "US"
            and c[1] == "Final consumption expenditure by households"]
    y = Y[cols].sum(axis=1).values.astype(np.float64)
    products = np.array([p for _, p in idx])
    regions = np.array([r for r, _ in idx])
    health = np.array(["health" in p.lower() for p in products])
    y_h = np.where(health, y, 0.0)
    L = np.eye(A.shape[0]) - A
    xs = np.linalg.solve(L, np.column_stack([y, y_h]))
    emb_all, emb_h = e * xs[:, 0], e * xs[:, 1]
    us = regions == "US"
    to_h = lambda v: float(v.sum() * 1e6 / POP)
    return dict(
        product_names=sorted(set(products[health])),
        all_dom=to_h(emb_all[us]), all_for=to_h(emb_all[~us]),
        health_dom=to_h(emb_h[us]), health_for=to_h(emb_h[~us]),
    )


def assemble(a, b):
    care = sum(a["categories"][c]["hours"] for c in CARE_SERVICES)
    goods = a["categories"][27]["hours"] + a["categories"][14]["hours"]
    ins = a["categories"][62]["hours"]
    # Part A is domestic only. Add foreign hours:
    #   care services: EXIOBASE health-services foreign ratio (for/dom)
    #   goods: the whole-economy foreign ratio (for/dom) -- pharma is not a
    #   separate EXIOBASE product, so this is the stated stand-in
    r_care = b["health_for"] / b["health_dom"] if b else 0.0
    r_goods = b["all_for"] / b["all_dom"] if b else 0.0
    care_t, goods_t, ins_t = care * (1 + r_care), goods * (1 + r_goods), ins
    scale = ANCHOR / TOTAL_PER_CAP                 # per capita -> median adult anchor
    care_a, goods_a, ins_a = care_t * scale, goods_t * scale, ins_t * scale
    health_a = care_a + goods_a + ins_a
    scen = [
        ("A: every treatment lands on the patient", ANCHOR),
        ("B: care services covered, drugs and devices on the patient", ANCHOR - care_a - ins_a),
        ("C: all healthcare covered", ANCHOR - health_a),
    ]
    # ADEQUATE PROVISION: scale care services to countries with universal
    # coverage (health_peer.py). Insurance paperwork has no Aequitas equivalent.
    peer = None
    pc = os.path.join(HERE, "health_peer_result.json")
    if os.path.exists(pc):
        d = json.load(open(pc))
        us = d["US"]["health_h_per_capita"]
        ratios = {c: d[c]["health_h_per_capita"] / us for c in ("DE", "JP", "SE", "FR", "ES")}
        med = float(np.median(list(ratios.values())))
        adequate = lambda r: ANCHOR - care_a - ins_a + care_a * r
        peer = dict(ratios=ratios, median_ratio=med,
                    anchor_median=adequate(med),
                    anchor_low=adequate(min(ratios.values())),
                    anchor_high=adequate(max(ratios.values())))
    return dict(care=care_a, goods=goods_a, insurance=ins_a, health=health_a,
                share=health_a / ANCHOR, r_care=r_care, r_goods=r_goods,
                scenarios=scen, peer=peer)


def report(use_exio=True):
    a = part_a()
    b = None
    if use_exio:
        b = part_b()
    elif os.path.exists(CACHE):
        b = json.load(open(CACHE)).get("part_b")
    s = assemble(a, b)
    json.dump(dict(part_a=a, part_b=b, anchor=s), open(CACHE, "w"), indent=1, default=str)

    W = 74
    print("=" * W)
    print("PART A -- domestic hours per capita/yr, by where the jobs sit (BLS 2023)")
    print("=" * W)
    for c, v in sorted(a["categories"].items(), key=lambda kv: -kv[1]["hours"]):
        print(f"  {v['hours']:6.1f} h  {v['name']}")
        if c in (27, 44):
            for k, h in sorted(v["by_industry"].items(), key=lambda kv: -kv[1]):
                if h >= 0.05 or c == 27:
                    print(f"             {h:6.2f} h  {k}")
    print(f"  {a['health_total']:6.1f} h  HEALTHCARE, of {a['pce_total']:.1f} h domestic "
          f"({100 * a['health_total'] / a['pce_total']:.1f}%)")
    if b:
        print("-" * W)
        print("PART B -- EXIOBASE, per capita/yr")
        print(f"  health services: {b['health_dom']:.1f} h domestic + {b['health_for']:.1f} h foreign")
        print(f"  all consumption: {b['all_dom']:.1f} h domestic + {b['all_for']:.1f} h foreign")
    print("-" * W)
    print(f"IN THE 1,380 h MEDIAN-ADULT ANCHOR")
    print(f"  care services {s['care']:6.0f} h   drugs+devices {s['goods']:5.0f} h   "
          f"insurance {s['insurance']:4.0f} h   = {s['health']:.0f} h ({100 * s['share']:.1f}%)")
    for name, v in s["scenarios"]:
        print(f"  {v:6.0f} h  {name}")
    if s["peer"]:
        p = s["peer"]
        print("-" * W)
        print("ADEQUATE PROVISION -- care at the level of countries with universal coverage")
        print(f"  care services x {p['median_ratio']:.2f} (median of DE JP SE FR ES), insurance removed")
        print(f"  {p['anchor_median']:6.0f} h  anchor, patient carries every treatment"
              f"  (range {p['anchor_low']:.0f} - {p['anchor_high']:.0f})")
    print("=" * W)
    return a, b, s


def run_tests():
    a = part_a()
    assert abs(a["pce_total"] - 612) < 3, a["pce_total"]
    print(f"[ok] PCE total {a['pce_total']:.1f} h reproduces Track 1's 612 h")
    ht = a["health_total"]
    assert abs(ht - 145) < 3, ht
    print(f"[ok] healthcare {ht:.1f} h reproduces track1_by_category's 145 h")
    for c, v in a["categories"].items():
        assert abs(sum(v["by_industry"].values()) - v["hours"]) < 1e-6
    print("[ok] every category's industry split adds back to its total")
    s = assemble(a, None)
    vals = [v for _, v in s["scenarios"]]
    assert vals[0] >= vals[1] >= vals[2] > 0, vals
    print("[ok] scenarios are ordered A >= B >= C > 0")
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--no-exio", action="store_true", help="skip EXIOBASE, reuse cache")
    a = ap.parse_args()
    run_tests() if a.test else report(use_exio=not a.no_exio)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
