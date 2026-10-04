"""
logistics_chain.py -- do countries that cover everyone have shorter
logistics chains than the US, or do they only file shop work differently?

WHY
  essentials.py found US households buy 224 h a year of retail and wholesale
  work as a separate item, against 10-73 h in five peer countries. RESULTS.md
  called that a filing difference without testing it. The author asked the
  real question: is it a shorter chain -- more local production, less
  transport, warehousing and distribution work?

THREE READINGS, per person per year
  A  BOUGHT AS AN ITEM  hours behind the trade and transport products that
                        final consumers buy directly (what essentials.py saw)
  B  BEHIND CONSUMPTION hours worked IN trade and transport sectors, anywhere
                        on Earth, behind the country's whole final
                        consumption -- however the accounts file them
  C  WORKED AT HOME     hours worked in the country's own trade and transport
                        sectors, per resident, whatever those hours serve

  If A differs and B does not -> the gap was a filing difference.
  If B is lower in the peers  -> the peers' chains really are shorter.

DATA  EXIOBASE 3, 2022, pxp. Final consumption = households + non-profits +
  government, as essentials.py.

SECTORS (EXIOBASE product numbers, 1-based)
  trade      152 motor-vehicle trade and repair, 153 fuel retail,
             154 wholesale, 155 retail
  transport  157 rail, 158 other land (road freight, bus, taxi),
             159 pipelines, 160 sea, 161 inland water, 162 air,
             163 cargo handling, storage and warehousing, travel agencies

Run:  python logistics_chain.py [--show]
      python logistics_chain.py --census   # reading C for all 23 Q6 countries,
                                           # to find data sets missing shop work
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
ZIP = os.path.join(SIM, "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "logistics_chain_result.json")
FC = "Final consumption expenditure"

POP_M = {"US": 333.3, "DE": 83.8, "JP": 125.0, "SE": 10.5, "FR": 68.0, "ES": 47.8}
PEERS = ["DE", "JP", "SE", "FR", "ES"]

TRADE = [152, 153, 154, 155]
TRANSPORT = {
    "land": [157, 158, 159],
    "water": [160, 161],
    "air": [162],
    "storage and handling": [163],
}
ALL_TRANSPORT = sum(TRANSPORT.values(), [])


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
    hrs = F.loc[rows].sum(axis=0).values.astype(np.float64)      # M.hr worked, by sector
    with np.errstate(divide="ignore", invalid="ignore"):
        e = np.where(x > 0, hrs / x, 0.0)                         # M.hr per M-EUR output

    regions = np.array([r for r, _ in idx])
    n_prod = len(regions) // len(set(regions))
    pnum = np.array([i % n_prod + 1 for i in range(len(regions))])
    is_trade = np.isin(pnum, TRADE)
    is_tr = np.isin(pnum, ALL_TRANSPORT)

    Y = exio.Y
    cs = list(POP_M)
    cols = []
    for c in cs:                                  # whole final consumption
        cc = [col for col in Y.columns if col[0] == c and str(col[1]).startswith(FC)]
        cols.append(Y[cc].sum(axis=1).values.astype(np.float64))
    for k in range(len(cs)):                      # only trade + transport bought as items
        cols.append(np.where(is_trade | is_tr, cols[k], 0.0))
    Ymat = np.column_stack(cols)
    print(f"solving (I-A) X = Y for {Ymat.shape[1]} demand vectors...")
    X = np.linalg.solve(np.eye(A.shape[0]) - A, Ymat)
    H = e[:, None] * X                            # M.hr, by sector, per demand vector

    out = {}
    for k, c in enumerate(cs):
        pop = POP_M[c] * 1e6
        per = lambda v: float(v) * 1e6 / pop
        h, h_item = H[:, k], H[:, len(cs) + k]
        home = regions == c
        out[c] = dict(
            total_behind_consumption=per(h.sum()),
            A_bought_as_item=per(h_item.sum()),
            B_trade=per(h[is_trade].sum()),
            B_trade_home=per(h[is_trade & home].sum()),
            B_transport=per(h[is_tr].sum()),
            B_transport_home=per(h[is_tr & home].sum()),
            B_transport_modes={m: per(h[np.isin(pnum, p)].sum()) for m, p in TRANSPORT.items()},
            C_trade=per(hrs[is_trade & home].sum()),
            C_transport=per(hrs[is_tr & home].sum()),
            population_m=POP_M[c],
        )
        print(f"  {c}: B trade {out[c]['B_trade']:.0f} h, B transport {out[c]['B_transport']:.0f} h")
    json.dump(out, open(CACHE, "w"), indent=1)
    return out


# 2022 population, millions -- the table in median-lifestyle/track6_country_labour.py
Q6_POP_M = {
    "US": 333.3, "DE": 83.8, "FR": 68.0, "GB": 67.0, "IT": 59.0, "ES": 47.8,
    "SE": 10.5, "NL": 17.7, "DK": 5.9, "NO": 5.5, "FI": 5.55, "CH": 8.8,
    "AT": 9.0, "BE": 11.6, "IE": 5.1, "PT": 10.3, "PL": 37.7, "CA": 38.9,
    "AU": 26.0, "JP": 125.0, "KR": 51.6, "CZ": 10.5, "GR": 10.4,
}
CENSUS = os.path.join(HERE, "logistics_census_result.json")


def census() -> dict:
    """Reading C only: hours worked in each country's own shops, wholesale
    and transport, per resident. No solve, so it covers all 23 countries."""
    import pymrio
    print("parsing EXIOBASE 3 (~2 min)...")
    exio = pymrio.parse_exiobase3(path=ZIP)
    F = exio.employment.F
    rows = [s for s in F.index if str(s).startswith("Employment hours")]
    hrs = F.loc[rows].sum(axis=0)
    out = {}
    for c, pop_m in Q6_POP_M.items():
        h = hrs.loc[c].values.astype(np.float64)          # 200 products, in order
        pn = np.arange(1, len(h) + 1)
        per = lambda v: float(v) * 1e6 / (pop_m * 1e6)
        out[c] = dict(trade=per(h[np.isin(pn, TRADE)].sum()),
                      transport=per(h[np.isin(pn, ALL_TRANSPORT)].sum()),
                      all_work=per(h.sum()))
    json.dump(out, open(CENSUS, "w"), indent=1)
    W = 64
    print("=" * W)
    print("READING C -- hours worked at home per resident per year, 2022")
    print("=" * W)
    print(f"  {'':4}{'shops+wholesale':>17}{'transport':>11}{'all work':>10}{'shops share':>13}")
    for c, v in sorted(out.items(), key=lambda kv: kv[1]["trade"]):
        flag = "   <- missing?" if v["trade"] < 0.25 * np.median([w["trade"] for w in out.values()]) else ""
        print(f"  {c:4}{v['trade']:17.0f}{v['transport']:11.0f}{v['all_work']:10.0f}"
              f"{100 * v['trade'] / v['all_work']:12.1f}%{flag}")
    print("=" * W)
    return out


def show(out: dict):
    W = 86
    print("=" * W)
    print("LOGISTICS WORK PER PERSON PER YEAR -- trade (shops, wholesale) and transport")
    print("  A = bought as an item   B = worked in these sectors behind consumption   C = worked at home")
    print("=" * W)
    print(f"  {'':4}{'A item':>9}{'B trade':>10}{'B transp.':>11}{'B both':>9}"
          f"{'of all B':>10}{'C trade':>10}{'C transp.':>11}{'all hours':>11}")
    for c in ["US"] + PEERS:
        v = out[c]
        both = v["B_trade"] + v["B_transport"]
        print(f"  {c:4}{v['A_bought_as_item']:9.0f}{v['B_trade']:10.0f}{v['B_transport']:11.0f}"
              f"{both:9.0f}{100 * both / v['total_behind_consumption']:9.0f}%"
              f"{v['C_trade']:10.0f}{v['C_transport']:11.0f}{v['total_behind_consumption']:11.0f}")
    med = lambda key: float(np.median([out[c][key] for c in PEERS]))
    print("-" * W)
    print(f"  peer median   B trade {med('B_trade'):.0f} h (US {out['US']['B_trade']:.0f})   "
          f"B transport {med('B_transport'):.0f} h (US {out['US']['B_transport']:.0f})")
    print("-" * W)
    print("  B transport by mode, and the share worked at home")
    for c in ["US"] + PEERS:
        v = out[c]
        modes = "  ".join(f"{m} {h:.0f}" for m, h in v["B_transport_modes"].items())
        print(f"  {c:4}{modes}   | at home: trade {100 * v['B_trade_home'] / v['B_trade']:.0f}%"
              f", transport {100 * v['B_transport_home'] / v['B_transport']:.0f}%")
    print("=" * W)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true", help="print the cached result")
    ap.add_argument("--census", action="store_true", help="reading C for all 23 Q6 countries")
    a = ap.parse_args()
    if a.census:
        census()
        return 0
    out = json.load(open(CACHE)) if a.show else compute()
    show(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
