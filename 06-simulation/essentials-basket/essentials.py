"""
essentials.py -- measure E, the hours of other people's work a year of
essentials takes, for one person.

WHY
  Foundations 5.5.3 bounds the floor F from below by  rho * F * 365 >= E.
  E has only ever been illustrative (700 h) or swept (30-70% of a median
  lifestyle). This measures it.

WHAT COUNTS AS ESSENTIAL
  Each trust network decides. So two baskets are reported, and the gap
  between them is the network's choice:
    NARROW  food eaten at home, clothing, shelter services, household
            utilities, health and social care
    BROAD   NARROW + household supplies, furniture, public and hired land
            transport, post and telecoms, schooling

HOW MUCH COUNTS AS ADEQUATE
  Measured two ways, and the gap is reported rather than hidden:
    US      what the US population consumes now, per person
    PEERS   the median of Germany, Japan, Sweden, France and Spain --
            countries where everyone is covered
  PEERS mixes two things: a different quantity AND a more efficient method
  (Q6). For a US network the US figure is the one that does not flatter.

DATA  EXIOBASE 3, 2022, pxp. Every hour worked anywhere on Earth behind a
  country's consumption, whoever pays: households, non-profits, government.

METHOD
  m = e (I - A)^-1   total hours per M-EUR of final demand (one solve)
  hours in category k for country c = m . y_c[k] / population_c
  Wholesale and retail trade (products 154, 155) are purchased as separate
  products, so their hours are shared out to goods categories in proportion
  to each category's spending on goods -- as Track 1 does with margins.

Run:  python essentials.py [--show] [--test]
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
ZIP = os.path.join(SIM, "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "essentials_result.json")
FC = "Final consumption expenditure"

# 2022 population, millions -- same table as median-lifestyle/track6_country_labour.py
POP_M = {"US": 333.3, "DE": 83.8, "JP": 125.0, "SE": 10.5, "FR": 68.0, "ES": 47.8}
PEERS = ["DE", "JP", "SE", "FR", "ES"]

# EXIOBASE product numbers, 1-based, in the order of unit.txt
R = lambda a, b: list(range(a, b + 1))
CATS = {
    "Food eaten at home":        R(1, 14) + [19] + R(43, 53),
    "Clothing and footwear":     [55, 56, 57],
    "Shelter services":          [168],
    "Household utilities":       R(128, 141) + [147, 148, 149],
    "Health and social care":    [175],
    "Chemicals, paper, plastics (incl. drugs)": [62, 90, 96],
    "Furniture and other goods": [125],
    "Land transport services":   [157, 158],
    "Post and telecoms":         [164],
    "Schooling":                 [174],
}
NARROW = ["Food eaten at home", "Clothing and footwear", "Shelter services",
          "Household utilities", "Health and social care"]
BROAD = list(CATS)
TRADE = [154, 155]
GOODS = set(R(1, 149))            # physical products carry a trade margin


def compute() -> dict:
    import pymrio
    print("parsing EXIOBASE 3 (~2 min)...")
    exio = pymrio.parse_exiobase3(path=ZIP)
    x = exio.x["indout"].values.astype(np.float64)
    idx = exio.Z.index
    Z = exio.Z.values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        inv_x = np.where(x > 0, 1.0 / x, 0.0)
    A = Z * inv_x[np.newaxis, :]
    del Z
    F = exio.employment.F
    rows = [s for s in F.index if str(s).startswith("Employment hours")]
    hrs = F.loc[rows].sum(axis=0).values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        e = np.where(x > 0, hrs / x, 0.0)
    print("solving (I-A)^T m = e ...")
    m = np.linalg.solve((np.eye(A.shape[0]) - A).T, e)

    n_prod = A.shape[0] // len(set(r for r, _ in idx))
    pnum = np.array([i % n_prod + 1 for i in range(A.shape[0])])   # 1..200
    Y = exio.Y
    out = {}
    for c, pop_m in POP_M.items():
        cols = [col for col in Y.columns if col[0] == c and str(col[1]).startswith(FC)]
        y = Y[cols].sum(axis=1).values.astype(np.float64)
        pop = pop_m * 1e6
        h_of = lambda prods: float(m @ np.where(np.isin(pnum, prods), y, 0.0)) * 1e6 / pop
        eur_of = lambda prods: float(np.where(np.isin(pnum, prods), y, 0.0).sum())
        trade_h = h_of(TRADE)
        goods_eur = eur_of(sorted(GOODS))
        cats = {}
        for k, prods in CATS.items():
            g = [p for p in prods if p in GOODS]
            share = eur_of(g) / goods_eur if g else 0.0
            cats[k] = h_of(prods) + trade_h * share
        out[c] = dict(categories=cats, total=h_of(list(range(1, 201))),
                      trade=trade_h, population_m=pop_m)
        print(f"  {c}: narrow {sum(cats[k] for k in NARROW):.0f} h, "
              f"broad {sum(cats[k] for k in BROAD):.0f} h, all {out[c]['total']:.0f} h")
    json.dump(out, open(CACHE, "w"), indent=1)
    return out


# Two pieces EXIOBASE household demand does not carry, added from the
# median-lifestyle project and stated as such:
#  - DRUGS: EXIOBASE has no drug product (drugs sit in 'Chemicals nec', which
#    is in the BROAD basket only). The NARROW basket takes the US drug and
#    device figure from median-lifestyle/health_share.py, per capita.
#  - HOUSING STRUCTURE: building a home is investment, not consumption.
#    Track 2 annualises it at 31-61 h a year (MEDIAN_LIFESTYLE_RESULT.md).
HOUSING = (31.0, 61.0)


def drugs_per_capita() -> float:
    d = json.load(open(os.path.join(SIM, "median-lifestyle", "health_share_result.json")))
    return d["anchor"]["goods"] * 1276.18 / 1380.0     # median adult -> per capita


def summarise(out: dict) -> dict:
    us = out["US"]["categories"]
    peer = {k: float(np.median([out[c]["categories"][k] for c in PEERS])) for k in CATS}
    s = lambda d, ks: sum(d[k] for k in ks)
    dr = drugs_per_capita()
    lo, hi = HOUSING
    return dict(us=us, peer=peer, drugs=dr,
                narrow_us=s(us, NARROW), broad_us=s(us, BROAD),
                narrow_peer=s(peer, NARROW), broad_peer=s(peer, BROAD),
                E_narrow=(s(us, NARROW) + dr + lo, s(us, NARROW) + dr + hi),
                E_broad=(s(us, BROAD) + lo, s(us, BROAD) + hi),
                # care at the level of countries that cover everyone, the rest
                # at the US level (author ruling 2026-09-24: adequate care is E)
                care_cut=us["Health and social care"] - peer["Health and social care"],
                trade={c: v["trade"] for c, v in out.items()},
                us_total=out["US"]["total"])


def show(out: dict):
    r = summarise(out)
    W = 72
    print("=" * W)
    print("E -- hours of work behind a year of essentials, per person, 2022")
    print("  (EXIOBASE; worked anywhere; all payers)")
    print("=" * W)
    print(f"  {'category':<42}{'US':>8}{'peer median':>14}   basket")
    for k in CATS:
        tag = "narrow" if k in NARROW else "broad only"
        print(f"  {k:<42}{r['us'][k]:8.1f}{r['peer'][k]:14.1f}   {tag}")
    print("-" * W)
    print(f"  {'E, NARROW basket':<42}{r['narrow_us']:8.0f}{r['narrow_peer']:14.0f}")
    print(f"  {'E, BROAD basket':<42}{r['broad_us']:8.0f}{r['broad_peer']:14.0f}")
    print(f"  {'all US consumption':<42}{r['us_total']:8.0f}")
    print(f"  narrow is {100 * r['narrow_us'] / r['us_total']:.0f}% and broad "
          f"{100 * r['broad_us'] / r['us_total']:.0f}% of all US consumption hours")
    print("-" * W)
    print("E AT THE US LEVEL, with the two pieces EXIOBASE does not carry")
    print(f"  NARROW  = {r['narrow_us']:.0f} + drugs {r['drugs']:.0f} + housing structure 31-61"
          f"  = {r['E_narrow'][0]:.0f} - {r['E_narrow'][1]:.0f} h")
    print(f"  BROAD   = {r['broad_us']:.0f} + housing structure 31-61"
          f"  = {r['E_broad'][0]:.0f} - {r['E_broad'][1]:.0f} h   (drugs already inside)")
    c = r["care_cut"]
    print(f"  with care at the peer level (-{c:.0f} h):  NARROW {r['E_narrow'][0] - c:.0f} - "
          f"{r['E_narrow'][1] - c:.0f} h,  BROAD {r['E_broad'][0] - c:.0f} - {r['E_broad'][1] - c:.0f} h")
    for name, (lo, hi) in (("NARROW", (r["E_narrow"][0] - c, r["E_narrow"][1])),
                           ("BROAD", (r["E_broad"][0] - c, r["E_broad"][1]))):
        print(f"  lowest floor that affords {name} at rho = 1.2:  "
              f"{lo / (1.2 * 365):.2f} - {hi / (1.2 * 365):.2f} h/day")
    print("-" * W)
    print("  retail and wholesale hours households buy directly (shared out above):")
    print("   " + "  ".join(f"{c} {h:.0f}" for c, h in r["trade"].items()))
    print("=" * W)
    return r


def run_tests():
    out = json.load(open(CACHE))
    for c, v in out.items():
        assert all(h >= 0 for h in v["categories"].values()), c
        assert sum(v["categories"].values()) <= v["total"] + 1e-6, c
    print("[ok] every category is non-negative and the categories fit inside the total")
    r = summarise(out)
    assert r["narrow_us"] < r["broad_us"] < r["us_total"]
    print("[ok] narrow < broad < all consumption, for the US")
    peer_health = json.load(open(os.path.join(SIM, "median-lifestyle", "health_peer_result.json")))
    us_h = peer_health["US"]["health_h_per_capita"]
    assert abs(out["US"]["categories"]["Health and social care"] - us_h) < 1.0, us_h
    print(f"[ok] US health and social care reproduces health_peer.py ({us_h:.1f} h)")
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true", help="print the cached result")
    ap.add_argument("--test", action="store_true", help="self-tests on the cached result")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return 0
    out = json.load(open(CACHE)) if a.show else compute()
    show(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
