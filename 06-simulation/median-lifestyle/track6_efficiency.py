"""
track6_efficiency.py -- Q6, part B: who delivers the most MATERIAL BENEFIT per
HOUR of labour commanded? Divides a material-standard / wellbeing indicator by the
embodied labour-hours per capita from track6_country_labour.py.

Two numerators, deliberately (one physical outcome, one material-standard proxy):
  - LIFE EXPECTANCY at birth, 2022 (World Bank / OWID) -- a physical wellbeing
    outcome, money-free. Aequitas-clean.
  - ACTUAL INDIVIDUAL CONSUMPTION per capita, 2022, PPP index (Eurostat EU27=100;
    US via OECD PPPs) -- the standard "material welfare of households" measure.
    Monetary, so shown for reference; distorted by price levels.

EFFICIENCY = benefit / (embodied labour-hours per capita).
  hours_per_life_year = hours_per_capita / life_expectancy   (LOWER = better)
  aic_per_1000h       = AIC_index / (hours_per_capita/1000)   (HIGHER = better)

Denominator source: track6_country_result.json (EXIOBASE 3, 2022; embodied
labour-hours per capita in household consumption, domestic + imported).

Run:  python track6_efficiency.py [--test]
"""
from __future__ import annotations

import argparse
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.join(HERE, "track6_country_result.json")

# --- Numerator data (published 2022 figures; archived in Q6.md / research stub) --
# Life expectancy at birth 2022, years (World Bank / OWID).
LIFE_EXP = {
    "US": 77.4, "JP": 84.0, "ES": 83.2, "IT": 83.0, "FR": 82.3, "SE": 83.0,
    "DE": 80.6, "GB": 80.4, "NL": 81.7, "CH": 83.9, "NO": 83.2, "AU": 84.5,
    "KR": 82.7, "PL": 77.4, "FI": 81.0, "DK": 81.3, "CA": 82.6, "PT": 81.5,
    "AT": 81.1, "BE": 81.8, "GR": 80.7, "CZ": 79.1, "IE": 82.4,
}
# Actual Individual Consumption per capita 2022, PPP index (EU27=100; US via OECD).
AIC = {
    "US": 150, "LU": 138, "DE": 119, "AT": 118, "NL": 118, "BE": 116, "DK": 113,
    "FR": 113, "FI": 112, "SE": 111, "IT": 99, "IE": 96, "ES": 91, "GB": 113,
    "PT": 84, "PL": 84, "CZ": 84, "GR": 82, "NO": 131, "CH": 130, "JP": 108,
    "AU": 116, "KR": 100, "CA": 120,
}
# Small open trade-hubs whose EXIOBASE embodied-hours are inflated by transit /
# transfer-pricing (foreign share > 0.85). Flagged, shown separately.
TRADE_HUBS = {"IE", "NL", "BE", "LU", "CH", "DK"}


def load():
    return json.load(open(LAB))


def rows():
    d = load()
    out = []
    for c, v in d.items():
        h = v["hours_per_capita"]
        le = LIFE_EXP.get(c)
        aic = AIC.get(c)
        out.append(dict(
            country=c, hours=h, foreign=v["foreign_share"],
            life_exp=le, aic=aic,
            h_per_life_year=(h / le) if le else None,
            aic_per_1000h=(aic / (h / 1000)) if aic else None,
            hub=c in TRADE_HUBS,
        ))
    return out


def report():
    data = [r for r in rows() if not r["hub"]]
    hubs = [r for r in rows() if r["hub"]]
    W = 78
    print("=" * W)
    print("Q6 -- MATERIAL BENEFIT PER LABOUR-HOUR, first-world countries (2022)")
    print("  embodied labour-hours/capita (EXIOBASE) vs life-expectancy & AIC")
    print("=" * W)
    print(f"  {'ctry':<6}{'h/cap':>7}{'life':>7}{'AIC':>6}"
          f"{'h/life-yr':>11}{'AIC/1000h':>11}   {'':}")
    print(f"  {'':<6}{'':>7}{'exp':>7}{'idx':>6}{'(lower=better)':>11}{'(higher=better)':>11}")
    print("-" * W)
    for r in sorted(data, key=lambda r: r["h_per_life_year"] or 9e9):
        print(f"  {r['country']:<6}{r['hours']:>7.0f}{r['life_exp']:>7.1f}"
              f"{r['aic']:>6.0f}{r['h_per_life_year']:>11.1f}{r['aic_per_1000h']:>11.0f}")
    print("-" * W)
    print("  Trade-hub / transfer-pricing distorted (foreign share > 85%, flagged):")
    for r in sorted(hubs, key=lambda r: r["h_per_life_year"] or 9e9):
        print(f"  {r['country']:<6}{r['hours']:>7.0f}{r['life_exp']:>7.1f}"
              f"{r['aic']:>6.0f}{r['h_per_life_year']:>11.1f}{r['aic_per_1000h']:>11.0f}"
              f"   (foreign {r['foreign']*100:.0f}%)")
    print("=" * W)
    # headline
    best = min(data, key=lambda r: r["h_per_life_year"])
    us = next(r for r in data if r["country"] == "US")
    print(f"  MOST labour-efficient (wellbeing): {best['country']} "
          f"({best['h_per_life_year']:.1f} h per life-year)")
    print(f"  US: {us['h_per_life_year']:.1f} h/life-year -- "
          f"{us['h_per_life_year']/best['h_per_life_year']:.2f}x {best['country']}, "
          f"for a SHORTER life ({us['life_exp']} vs {best['life_exp']})")
    print("=" * W)
    return data


def test_us_least_efficient_wellbeing():
    data = [r for r in rows() if not r["hub"]]
    us = next(r for r in data if r["country"] == "US")
    worst = max(data, key=lambda r: r["h_per_life_year"])
    assert worst["country"] == "US", f"expected US worst, got {worst['country']}"
    print(f"[ok] US least wellbeing-efficient ({us['h_per_life_year']:.1f} h/life-yr)")


def test_spain_beats_us():
    data = {r["country"]: r for r in rows()}
    assert data["ES"]["hours"] < data["US"]["hours"]
    assert data["ES"]["life_exp"] > data["US"]["life_exp"]
    print(f"[ok] Spain: fewer hours ({data['ES']['hours']:.0f}<{data['US']['hours']:.0f}) "
          f"AND longer life ({data['ES']['life_exp']}>{data['US']['life_exp']})")


def test_us_aic_efficiency_below_median():
    data = [r for r in rows() if not r["hub"] and r["aic_per_1000h"]]
    vals = sorted(r["aic_per_1000h"] for r in data)
    med = vals[len(vals) // 2]
    us = next(r for r in data if r["country"] == "US")
    assert us["aic_per_1000h"] < med, (us["aic_per_1000h"], med)
    print(f"[ok] US material-consumption per hour ({us['aic_per_1000h']:.0f}) below median ({med:.0f})")


def run_tests():
    test_us_least_efficient_wellbeing()
    test_spain_beats_us()
    test_us_aic_efficiency_below_median()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    run_tests() if a.test else report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
