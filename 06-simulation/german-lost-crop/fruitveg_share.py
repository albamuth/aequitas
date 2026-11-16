#!/usr/bin/env python3
"""
fruitveg_share.py -- hours of work behind US household demand for fresh fruit and vegetables,
as a share of all US consumption hours. Same method and data as essentials-basket/essentials.py
(EXIOBASE 3, 2022, pxp; hours = m . y, trade margin shared by goods spending).

LINE DEFINITION. EXIOBASE product 4 = "Vegetables, fruit, nuts" (raw produce bought by households).
Processed fruit and vegetables sit inside product 51 "Food products nec" and cannot be separated,
so they are NOT in this line. This understates the line; the run sweeps the share to cover that.

Self-test: the same code must reproduce essentials-basket's "Food eaten at home" = 131.0 h and
"all US consumption" = 1398 h to within 1 h, or the script refuses to write a result.

Run: python fruitveg_share.py     (~2-3 min, reads data/exiobase in place, writes fruitveg_result.json)
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
ZIP = os.path.join(SIM, "data", "exiobase", "IOT_2022_pxp.zip")
OUT = os.path.join(HERE, "fruitveg_result.json")
FC = "Final consumption expenditure"
POP = 333.3e6
R = lambda a, b: list(range(a, b + 1))   # noqa: E731
FOOD = R(1, 14) + [19] + R(43, 53)
FRUITVEG = [4]
TRADE = [154, 155]
GOODS = set(R(1, 149))


def main():
    import pymrio
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
    m = np.linalg.solve((np.eye(A.shape[0]) - A).T, e)
    n_prod = A.shape[0] // len(set(r for r, _ in idx))
    pnum = np.array([i % n_prod + 1 for i in range(A.shape[0])])
    Y = exio.Y
    cols = [c for c in Y.columns if c[0] == "US" and str(c[1]).startswith(FC)]
    y = Y[cols].sum(axis=1).values.astype(np.float64)
    h_of = lambda prods: float(m @ np.where(np.isin(pnum, prods), y, 0.0)) * 1e6 / POP   # noqa: E731
    eur_of = lambda prods: float(np.where(np.isin(pnum, prods), y, 0.0).sum())           # noqa: E731
    trade_h = h_of(TRADE)
    goods_eur = eur_of(sorted(GOODS))

    def line(prods):
        g = [p for p in prods if p in GOODS]
        return h_of(prods) + trade_h * (eur_of(g) / goods_eur if g else 0.0)

    food_h, fv_h, all_h = line(FOOD), line(FRUITVEG), h_of(list(range(1, 201)))
    assert abs(food_h - 131.0) < 1.0, f"does not reproduce essentials-basket food (131.0): {food_h:.1f}"
    assert abs(all_h - 1398.0) < 1.0, f"does not reproduce essentials-basket total (1398): {all_h:.1f}"
    assert fv_h < food_h, "fruit and vegetables must be part of food"
    res = dict(food_at_home_h=food_h, fruitveg_h=fv_h, all_consumption_h=all_h,
               fruitveg_share_of_food=fv_h / food_h, fruitveg_share_of_all=fv_h / all_h,
               fruitveg_eur_m=eur_of(FRUITVEG) / 1.0, food_eur_m=eur_of(FOOD))
    json.dump(res, open(OUT, "w"), indent=1)
    print(json.dumps(res, indent=1))
    print("[ok] reproduces food 131.0 h and all 1398 h")


if __name__ == "__main__":
    sys.exit(main())
