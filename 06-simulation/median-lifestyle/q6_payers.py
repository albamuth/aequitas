"""
q6_payers.py -- does Q6's comparison change when every payer is counted?

WHY
  Q6 (track6_country_labour.py) counts the hours behind what HOUSEHOLDS buy.
  But its standard-of-living measure, Actual Individual Consumption (AIC),
  includes the services a GOVERNMENT provides to individuals -- health care
  and schooling above all. In most peer countries the state pays for those;
  in the US households mostly do. So the peers' care and teaching hours were
  left out of the labour side and kept in the standard side. That flatters
  the peers.

READINGS, hours per person per year, all worked anywhere on Earth
  HH            households only -- what Q6 used
  NPISH         non-profit institutions serving households
  GOV_IND       government, except 'public administration and defence'
                (product 173) -- a stand-in for government INDIVIDUAL
                consumption: health, schooling, social services, culture
  GOV_COLL      government purchases of product 173 -- collective services
  AIC_HOURS     HH + NPISH + GOV_IND -- the labour that matches AIC

DATA  EXIOBASE 3, 2022, pxp, as track6_country_labour.py.

LIMIT  Splitting government by product is a stand-in. National accounts
  split individual from collective by function (COFOG), which EXIOBASE does
  not carry.

Run:  python q6_payers.py [--show] [--test]
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ZIP = os.path.join(os.path.dirname(HERE), "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "q6_payers_result.json")

# 2022 population, millions -- the table in track6_country_labour.py
POP_M = {
    "US": 333.3, "DE": 83.8, "FR": 68.0, "GB": 67.0, "IT": 59.0, "ES": 47.8,
    "SE": 10.5, "NL": 17.7, "DK": 5.9, "NO": 5.5, "FI": 5.55, "CH": 8.8,
    "AT": 9.0, "BE": 11.6, "IE": 5.1, "PT": 10.3, "PL": 37.7, "CA": 38.9,
    "AU": 26.0, "JP": 125.0, "KR": 51.6, "CZ": 10.5, "GR": 10.4,
}
PUBLIC_ADMIN = 173
DATA_GAPS = {"ES", "PL"}      # missing shop work: essentials-basket/logistics_chain.py --census
NAMED = ["DE", "SE", "FR", "JP"]


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

    regions = np.array([r for r, _ in idx])
    n_prod = len(regions) // len(set(regions))
    pnum = np.array([i % n_prod + 1 for i in range(len(regions))])
    is_admin = pnum == PUBLIC_ADMIN
    Y = exio.Y
    out = {}
    for c, pop_m in POP_M.items():
        per = lambda v: float(v) * 1e6 / (pop_m * 1e6)
        col = lambda test: Y[[k for k in Y.columns if k[0] == c and test(str(k[1]))]] \
            .sum(axis=1).values.astype(np.float64)
        # the NPISH column's name also contains 'households', so households is matched exactly
        hh = col(lambda s: s == "Final consumption expenditure by households")
        npish = col(lambda s: "non-profit" in s)
        gov = col(lambda s: "government" in s)
        r = dict(HH=per(m @ hh), NPISH=per(m @ npish),
                 GOV_IND=per(m @ np.where(is_admin, 0.0, gov)),
                 GOV_COLL=per(m @ np.where(is_admin, gov, 0.0)))
        r["AIC_HOURS"] = r["HH"] + r["NPISH"] + r["GOV_IND"]
        out[c] = r
        print(f"  {c}: HH {r['HH']:.0f}  AIC-matched {r['AIC_HOURS']:.0f}")
    json.dump(out, open(CACHE, "w"), indent=1)
    return out


def show(out: dict):
    us = out["US"]
    W = 84
    print("=" * W)
    print("Q6 WITH EVERY PAYER -- hours per person per year, 2022")
    print("=" * W)
    print(f"  {'':4}{'HH':>7}{'NPISH':>7}{'GOV ind':>9}{'GOV coll':>10}{'AIC-matched':>13}"
          f"{'US ÷ HH':>10}{'US ÷ AIC':>10}")
    for c, v in sorted(out.items(), key=lambda kv: -kv[1]["AIC_HOURS"]):
        flag = "  data gap" if c in DATA_GAPS else ""
        print(f"  {c:4}{v['HH']:7.0f}{v['NPISH']:7.0f}{v['GOV_IND']:9.0f}{v['GOV_COLL']:10.0f}"
              f"{v['AIC_HOURS']:13.0f}{us['HH'] / v['HH']:10.2f}{us['AIC_HOURS'] / v['AIC_HOURS']:10.2f}{flag}")
    print("-" * W)
    hh = [us["HH"] / out[c]["HH"] for c in NAMED]
    aic = [us["AIC_HOURS"] / out[c]["AIC_HOURS"] for c in NAMED]
    print(f"  US extra hours against Germany, Sweden, France, Japan:")
    print(f"    households only (as Q6)   {100 * (min(hh) - 1):.0f}% to {100 * (max(hh) - 1):.0f}% more")
    print(f"    every individual payer    {100 * (min(aic) - 1):.0f}% to {100 * (max(aic) - 1):.0f}% more")
    print(f"  peers' AIC-matched hours as a share of the US: "
          f"{min(1 / a for a in aic):.2f} - {max(1 / a for a in aic):.2f}"
          f"  (Q6 household-only: {min(1 / a for a in hh):.2f} - {max(1 / a for a in hh):.2f})")
    print("=" * W)


def run_tests():
    out = json.load(open(CACHE))
    t6 = json.load(open(os.path.join(HERE, "track6_country_result.json")))
    for c in ("US", "DE", "JP", "FR", "SE"):
        assert abs(out[c]["HH"] - t6[c]["hours_per_capita"]) < 1.0, (c, out[c]["HH"])
    print("[ok] the households-only column reproduces track6 (Q6) for US, DE, JP, FR, SE")
    for c, v in out.items():
        assert min(v.values()) >= 0, c
    print("[ok] every reading is non-negative")
    ess = json.load(open(os.path.join(os.path.dirname(HERE), "essentials-basket", "essentials_result.json")))
    for c in ess:
        allpay = out[c]["AIC_HOURS"] + out[c]["GOV_COLL"]
        assert abs(allpay - ess[c]["total"]) < 1.0, (c, allpay, ess[c]["total"])
    print("[ok] all payers together reproduce essentials.py's totals")
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return 0
    out = json.load(open(CACHE)) if a.show else compute()
    show(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
