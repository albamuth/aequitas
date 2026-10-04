"""
health_peer.py -- how many hours of health services a person uses in countries
where everyone is covered, against the US.

WHY
  health_share.py found care services are ~180 of the 1,380 h anchor. That is
  the US population average, which mixes under-served people, over-treatment,
  and insurance paperwork. The author asked for a figure for a person who is
  adequately provided for. Proxy: countries with universal coverage.

DATA  EXIOBASE 3, 2022, pxp (as track6_country_labour.py).

METHOD
  m = e (I - A)^-1 : total hours, anywhere on Earth, per M-EUR of final demand.
  For country c, health demand y_c = product 'Health and social work services'
  bought by ALL THREE final-consumption columns: households, non-profits, and
  government. Government must be included: in most universal systems the state
  pays, so household spending alone would miss most of the care.
  hours per person = m . y_c / population_c

LIMIT  The product is 'health AND social work', so it also holds childcare,
  elderly care and social services. Same definition in every country.
  Drugs are not in it (they sit inside 'Chemicals nec').

Run:  python health_peer.py [--show]
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ZIP = os.path.join(os.path.dirname(HERE), "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "health_peer_result.json")
FC = "Final consumption expenditure"

# 2022 population, millions -- same table as track6_country_labour.py
POP_M = {
    "US": 333.3, "DE": 83.8, "FR": 68.0, "GB": 67.0, "IT": 59.0, "ES": 47.8,
    "SE": 10.5, "NL": 17.7, "DK": 5.9, "NO": 5.5, "FI": 5.55, "CH": 8.8,
    "AT": 9.0, "BE": 11.6, "IE": 5.1, "PT": 10.3, "PL": 37.7, "CA": 38.9,
    "AU": 26.0, "JP": 125.0, "KR": 51.6, "CZ": 10.5, "GR": 10.4,
}
NAMED = ["DE", "JP", "SE", "FR", "ES"]     # the author's five


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

    products = np.array([p for _, p in idx])
    health = np.array(["health" in p.lower() for p in products])
    Y = exio.Y
    out = {}
    for c, pop_m in POP_M.items():
        cols = [col for col in Y.columns if col[0] == c and str(col[1]).startswith(FC)]
        if not cols:
            continue
        pop = pop_m * 1e6
        by_payer = {}
        for col in cols:
            y = np.where(health, Y[col].values.astype(np.float64), 0.0)
            by_payer[col[1]] = float(m @ y) * 1e6 / pop
        out[c] = dict(health_h_per_capita=sum(by_payer.values()), by_payer=by_payer,
                      population_m=pop_m)
        print(f"  {c}: {out[c]['health_h_per_capita']:.0f} h/cap")
    json.dump(out, open(CACHE, "w"), indent=1)
    return out


def show(out: dict):
    us = out["US"]["health_h_per_capita"]
    peers = {c: v["health_h_per_capita"] for c, v in out.items() if c != "US"}
    named = [peers[c] for c in NAMED if c in peers]
    W = 70
    print("=" * W)
    print("HEALTH AND SOCIAL WORK SERVICES -- hours per person per year, 2022")
    print("  (all payers: households + non-profits + government; worked anywhere)")
    print("=" * W)
    for c, v in sorted(out.items(), key=lambda kv: -kv[1]["health_h_per_capita"]):
        hh = sum(h for k, h in v["by_payer"].items() if "households" in k)
        gov = sum(h for k, h in v["by_payer"].items() if "government" in k.lower())
        tag = "  <- US" if c == "US" else ("  *" if c in NAMED else "")
        print(f"  {c}  {v['health_h_per_capita']:6.1f} h   "
              f"(households {hh:5.1f}, government {gov:5.1f}){tag}")
    print("-" * W)
    print(f"  US                          {us:6.1f} h")
    print(f"  median of the five named *  {np.median(named):6.1f} h  = {np.median(named) / us:.2f} x US")
    print(f"  median of all {len(peers)} peers       {np.median(list(peers.values())):6.1f} h"
          f"  = {np.median(list(peers.values())) / us:.2f} x US")
    print(f"  range of the five named     {min(named):6.1f} - {max(named):.1f} h")
    print("=" * W)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true", help="print the cached result")
    a = ap.parse_args()
    out = json.load(open(CACHE)) if a.show else compute()
    show(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
