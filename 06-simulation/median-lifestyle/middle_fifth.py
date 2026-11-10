"""
middle_fifth.py -- hours behind the middle fifth's consumption, not the average's.

WHY
  q6_payers.py reports the hours behind each country's consumption PER PERSON, which is
  an average. An average is pulled up by whoever consumes most. This script reads the
  middle fifth of households by income (the 40th to 60th percentile), which sits close
  to the median, and asks how far below the average it is in each country.

METHOD (ratio method)
  For each COICOP division d (the 12 standard spending divisions) and country c:
    r_cd = middle-fifth spending on d / all-household average spending on d
           -- both read from the SAME national survey, so currency and units cancel
    H_cd = hours per person behind household purchases in division d (EXIOBASE 3, 2022,
           the same m-vector and household column as q6_payers.py). Wholesale and retail
           trade (products 154, 155) are shared out to goods divisions by goods spending,
           as essentials-basket/essentials.py does.
  middle-fifth household hours = sum_d r_cd * H_cd
  Government individual services and non-profits (q6_payers.py GOV_IND, NPISH) are held at
  the national average: care and schooling are used about equally across income fifths.

SURVEYS (downloaded 2026-11-09 into 06-simulation/data/, which is never committed)
  EU   Eurostat Household Budget Survey: hbs_exp_t133 (spending per adult equivalent by
       income fifth) and hbs_str_t223 (per-mille share of spending by COICOP division and
       income fifth). Waves 2015 and 2020.
       https://ec.europa.eu/eurostat/statistics-explained/index.php/Household_budget_survey_-_statistics_on_consumption_expenditure
  US   BLS Consumer Expenditure Survey, Table 1101, 2023, quintiles of income before taxes.
       bls.gov refuses scripted downloads (HTTP 403); the copy is from the Internet Archive:
       https://web.archive.org/web/2025/https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-quintiles-before-taxes-2023.xlsx

Run:  python middle_fifth.py            # about 3 minutes, writes middle_fifth_result.json
      python middle_fifth.py --show     # from the cache
      python middle_fifth.py --test     # self-tests, from the cache and the survey files
"""
from __future__ import annotations

import argparse
import json
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
ZIP = os.path.join(DATA, "exiobase", "IOT_2022_pxp.zip")
T133 = os.path.join(DATA, "hbs", "hbs_exp_t133.tsv")
T223 = os.path.join(DATA, "hbs", "hbs_str_t223.tsv")
CEX = os.path.join(DATA, "cex", "cu-income-quintiles-before-taxes-2023.xlsx")
CACHE = os.path.join(HERE, "middle_fifth_result.json")
Q6 = os.path.join(HERE, "q6_payers_result.json")

# 2022 population, millions -- the table in q6_payers.py
POP_M = {"US": 333.3, "DE": 83.8, "FR": 68.0, "SE": 10.5, "NL": 17.7, "DK": 5.9,
         "NO": 5.5, "BE": 11.6, "GB": 67.0, "AT": 9.0, "FI": 5.55}
HBS_GEO = {"GB": "UK"}                      # EXIOBASE code -> Eurostat code
DIVS = [f"CP{i:02d}" for i in range(1, 13)]
Q = ["QU1", "QU2", "QU3", "QU4", "QU5"]

# EXIOBASE product (1-based, order of unit.txt) -> COICOP division. Unlisted -> CP12.
R = lambda a, b: list(range(a, b + 1))
PROD_DIV: dict[int, str] = {}
for div, prods in {
    "CP01": R(1, 14) + [19] + R(43, 51) + [53],
    "CP02": [52, 54],                              # beverages (mostly alcohol by value), tobacco
    "CP03": [55, 56, 57],
    "CP04": [18] + R(20, 27) + [71, 75, 91] + R(128, 149) + [150, 168] + R(176, 195),
    "CP05": [58, 62, 90, 96, 97, 99, 117, 118, 120, 125, 199],
    "CP06": [122, 175],
    "CP07": [67, 68, 72, 93, 94, 123, 124, 152, 153] + R(157, 163),
    "CP08": [164],
    "CP09": [63, 119, 121, 170, 197],
    "CP10": [174],
    "CP11": [156],
}.items():
    for p in prods:
        PROD_DIV[p] = div
TRADE = [154, 155]
GOODS = set(R(1, 149))
PUBLIC_ADMIN = 173


# ---------------------------------------------------------------- surveys
def read_tsv(path: str) -> dict:
    rows = {}
    with open(path, encoding="utf-8") as f:
        years = [h.strip() for h in f.readline().rstrip("\n").split("\t")[1:]]
        for line in f:
            parts = line.rstrip("\n").split("\t")
            vals = {}
            for y, v in zip(years, parts[1:]):
                mt = re.match(r"\s*([0-9.]+)", v)          # drops flags such as 'e', and ':'
                if mt:
                    vals[y] = float(mt.group(1))
            rows[tuple(parts[0].split(","))] = vals
    return rows


def hbs_ratios(t133: dict, t223: dict, geo: str, year: str):
    try:
        ae = {q: t133[("A", q, "PPS_AE", geo)][year] for q in Q + ["TOTAL"]}
        hh = {q: t133[("A", q, "PPS_HH", geo)][year] for q in Q + ["TOTAL"]}
        sh = {(q, d): t223[("A", q, d, "PM", geo)][year] for q in Q for d in DIVS}
    except KeyError:
        return None
    # t223 has no all-household row: average the five fifths' structures, weighted by spending
    avg_struct = {d: sum(hh[q] * sh[(q, d)] for q in Q) / sum(hh[q] for q in Q) for d in DIVS}
    r = {d: (ae["QU3"] * sh[("QU3", d)]) / (ae["TOTAL"] * avg_struct[d]) for d in DIVS}
    return dict(r=r, overall=ae["QU3"] / ae["TOTAL"],
                weight_check=(sum(hh[q] for q in Q) / 5) / hh["TOTAL"],
                spend_ae={q: ae[q] for q in Q + ["TOTAL"]})


def cex_ratios() -> dict:
    import openpyxl
    rows = list(openpyxl.load_workbook(CEX, read_only=True, data_only=True).worksheets[0]
                .iter_rows(values_only=True))
    num = lambda v: float(v) if re.match(r"^[0-9.]+$", str(v)) else 0.0

    def mean_of(label):
        for i, row in enumerate(rows):
            if row[0] and str(row[0]).strip().lower().startswith(label.lower()):
                for j in range(i + 1, i + 4):
                    if rows[j][0] and str(rows[j][0]).strip() == "Mean":
                        return num(rows[j][1]), num(rows[j][4])       # all units, third fifth
        raise KeyError(label)

    g = {k: mean_of(k) for k in [
        "Food at home", "Food away from home", "Alcoholic beverages", "Shelter",
        "Utilities, fuels", "Telephone services", "Household operations",
        "Housekeeping supplies", "Household furnishings", "Apparel and services",
        "Transportation", "Healthcare", "Entertainment", "Personal care", "Reading",
        "Education", "Tobacco", "Miscellaneous", "Average annual expenditures"]}
    people = next(r for r in rows if r[0] and str(r[0]).strip() == "People")
    g["People"] = (num(people[1]), num(people[4]))                # values on the same row
    add = lambda *ks: tuple(sum(g[k][i] for k in ks) for i in (0, 1))
    sub = lambda a, b: (a[0] - b[0], a[1] - b[1])
    div = {"CP01": add("Food at home"), "CP02": add("Alcoholic beverages", "Tobacco"),
           "CP03": add("Apparel and services"),
           "CP04": sub(add("Shelter", "Utilities, fuels"), add("Telephone services")),
           "CP05": add("Household operations", "Housekeeping supplies", "Household furnishings"),
           "CP06": add("Healthcare"), "CP07": add("Transportation"),
           "CP08": add("Telephone services"), "CP09": add("Entertainment", "Reading"),
           "CP10": add("Education"), "CP11": add("Food away from home"),
           "CP12": add("Personal care", "Miscellaneous")}
    people_all, people_mid = g["People"]
    per_person = people_all / people_mid            # 2.5 / 2.5 in 2023
    tot = g["Average annual expenditures"]
    return dict(r={d: v[1] / v[0] * per_person for d, v in div.items()},
                overall=tot[1] / tot[0] * per_person, weight_check=None,
                spend_cu={"all": tot[0], "third": tot[1]}, people=(people_all, people_mid))


def survey_ratios() -> dict:
    t133, t223 = read_tsv(T133), read_tsv(T223)
    out = {}
    for c in POP_M:
        if c == "US":
            out[c] = {"2023": cex_ratios()}
        else:
            geo = HBS_GEO.get(c, c)
            out[c] = {y: v for y in ("2015", "2020")
                      if (v := hbs_ratios(t133, t223, geo, y)) is not None}
    return out


# ---------------------------------------------------------------- EXIOBASE
def compute() -> dict:
    import pymrio
    from scipy.linalg import lu_factor, lu_solve
    ratios = survey_ratios()
    print("parsing EXIOBASE 3 (~2 min)...")
    exio = pymrio.parse_exiobase3(path=ZIP)
    x = exio.x["indout"].values.astype(np.float64)
    idx = exio.Z.index
    Z = exio.Z.values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        inv_x = np.where(x > 0, 1.0 / x, 0.0)
    IA = np.eye(len(x)) - Z * inv_x[np.newaxis, :]
    del Z
    F = exio.employment.F
    hrs = F.loc[[s for s in F.index if str(s).startswith("Employment hours")]] \
        .sum(axis=0).values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        e = np.where(x > 0, hrs / x, 0.0)
    print("factorising (I - A) ...")
    lu = lu_factor(IA, overwrite_a=True, check_finite=False)
    m = lu_solve(lu, e, trans=1, check_finite=False)            # (I-A)^T m = e, as q6_payers.py

    regions = np.array([str(r) for r, _ in idx])
    n_prod = len(regions) // len(set(regions))
    pnum = np.array([i % n_prod + 1 for i in range(len(regions))])
    div_of = np.array([PROD_DIV.get(int(p), "CP12") for p in pnum])
    is_admin = pnum == PUBLIC_ADMIN
    is_trade = np.isin(pnum, TRADE)
    goods = np.isin(pnum, sorted(GOODS))
    Y = exio.Y
    out = {}
    for c, pop_m in POP_M.items():
        col = lambda test: Y[[k for k in Y.columns if k[0] == c and test(str(k[1]))]] \
            .sum(axis=1).values.astype(np.float64)
        hh = col(lambda s: s == "Final consumption expenditure by households")
        npish = col(lambda s: "non-profit" in s)
        gov = col(lambda s: "government" in s)
        per = lambda v: float(v) / pop_m                          # q6_payers.py's per()
        trade_h = per(m @ np.where(is_trade, hh, 0.0))
        goods_eur = np.where(goods, hh, 0.0).sum()
        H = {d: per(m @ np.where((div_of == d) & ~is_trade, hh, 0.0))
                + trade_h * np.where(goods & (div_of == d), hh, 0.0).sum() / goods_eur
             for d in DIVS}
        hh_mean = per(m @ hh)
        public = per(m @ npish) + per(m @ np.where(is_admin, 0.0, gov))
        y_aic = hh + npish + np.where(is_admin, 0.0, gov)
        worked = e * lu_solve(lu, y_aic, check_finite=False)      # hours, by where they were worked
        home = per(worked[regions == c].sum())
        res = dict(HH_mean=hh_mean, public=public, AIC_mean=hh_mean + public,
                   home=home, abroad=per(worked.sum()) - home,
                   spend_eur=float(y_aic.sum()) / pop_m, H=H, by_year={})
        for y, rr in ratios[c].items():
            hh_mid = sum(rr["r"][d] * H[d] for d in DIVS)
            res["by_year"][y] = dict(HH_mid=hh_mid, AIC_mid=hh_mid + public, **rr)
        out[c] = res
        print(f"  {c}: average {res['AIC_mean']:.0f} h, middle fifth "
              + ", ".join(f"{y} {v['AIC_mid']:.0f} h" for y, v in res["by_year"].items()))
    json.dump(out, open(CACHE, "w"), indent=1)
    return out


# ---------------------------------------------------------------- report
def latest(res: dict) -> tuple[str, dict]:
    y = max(res["by_year"])
    return y, res["by_year"][y]


def show(out: dict):
    W = 96
    print("=" * W)
    print("MIDDLE FIFTH AGAINST THE AVERAGE -- hours per person per year, every payer, EXIOBASE 2022")
    print("=" * W)
    print(f"  {'':4}{'average':>9}{'middle':>9}{'mid/avg':>9}{'survey':>8}{'spend mid/avg':>15}"
          f"{'abroad share':>14}{'h per kEUR':>12}")
    for c, v in sorted(out.items(), key=lambda kv: -kv[1]["AIC_mean"]):
        y, b = latest(v)
        print(f"  {c:4}{v['AIC_mean']:9.0f}{b['AIC_mid']:9.0f}{b['AIC_mid'] / v['AIC_mean']:9.2f}{y:>8}"
              f"{b['overall']:15.3f}{v['abroad'] / (v['home'] + v['abroad']):14.0%}"
              f"{v['AIC_mean'] / v['spend_eur'] * 1000:12.1f}")
    print("-" * W)
    for c in ("DK", "NO", "AT", "FI", "DE", "NL", "BE", "FR"):
        if len(out[c]["by_year"]) == 2:
            a, b = out[c]["by_year"]["2015"], out[c]["by_year"]["2020"]
            print(f"  {c} survey wave check: 2015 {a['AIC_mid']:.0f} h, 2020 {b['AIC_mid']:.0f} h")
    print("=" * W)


def run_tests():
    out = json.load(open(CACHE))
    q6 = json.load(open(Q6))
    for c, v in out.items():
        assert abs(v["AIC_mean"] - q6[c]["AIC_HOURS"]) < 1.0, (c, v["AIC_mean"], q6[c]["AIC_HOURS"])
    print("[ok] the average column reproduces q6_payers.py (AIC-matched hours) for all 11 countries")
    for c, v in out.items():
        assert abs(sum(v["H"].values()) - v["HH_mean"]) < 1.0, c
        assert abs(v["home"] + v["abroad"] - v["AIC_mean"]) < 1.0, c
    print("[ok] the 12 divisions add up to all household hours; home + abroad add up to the total")
    ratios = survey_ratios()
    for c, ys in ratios.items():
        for y, rr in ys.items():
            if rr["weight_check"] is not None:
                assert abs(rr["weight_check"] - 1) < 0.005, (c, y, rr["weight_check"])
            assert all(0 < r < 5 for r in rr["r"].values()), (c, y)
    print("[ok] each income fifth holds a fifth of households (to 0.5%); every ratio is positive and finite")
    us = ratios["US"]["2023"]
    assert us["spend_cu"] == {"all": 77280.0, "third": 65487.0} and us["people"] == (2.5, 2.5), us
    print("[ok] the BLS table reads $77,280 for all households and $65,487 for the middle fifth, 2.5 people each")
    de = ratios["DE"]["2020"]["spend_ae"]
    assert abs(sum(de[q] for q in Q) / 5 - de["TOTAL"]) < 1.0, de
    print("[ok] Germany 2020: the all-household figure equals the mean of the five fifths (22,074 PPS)")
    flat = {d: 1.0 for d in DIVS}
    v = out["DE"]
    assert abs(sum(flat[d] * v["H"][d] for d in DIVS) - v["HH_mean"]) < 1.0
    print("[ok] a middle fifth that spends exactly like the average returns the average")
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--show", action="store_true")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return 0
    show(json.load(open(CACHE)) if a.show else compute())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
