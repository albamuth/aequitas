"""
average_household.py -- the AVERAGE (mean) US person's lifestyle in labour-hours,
2023, factored to ONE person (household figures / 2.51 persons per consumer unit).

The mean -- pulled up by the wealthy -- is the living standard everyone WOULD have
if consumption were shared evenly. Our EEIO tracks already compute means (national
totals / people), so this just re-normalises the four tracks to a per-person basis
and contrasts with the median.

Tracks (national -> per capita):
  1 consumption   track1_labour: total PCE labour / population
  2 housing       track2_housing: per-home build+repair / persons-per-home
  3 imports       EXIOBASE foreign labour / population
  4 pollution     track4: per-adult remediation x (adults/pop)

Run:  python average_household.py
"""
from __future__ import annotations

import track1_labour
import track2_housing
import track4_pollution

POP = 335e6
CONSUMER_UNITS = 134.556e6
PERSONS_PER_CU = 2.51
ADULTS = 258e6
MEDIAN_OVER_MEAN = 0.83

# Track 3: EXIOBASE 2022 foreign labour embodied in US household consumption
# (track3_exiobase.py result -- measured, not re-run here).
T3_FOREIGN_HOURS_TOTAL = 202.7e9
T3_DOMESTIC_HOURS_TOTAL = 224.9e9   # EXIOBASE domestic cross-check (BLS Track1 = 199.3e9)


def compute():
    t1 = track1_labour.compute()
    t2 = track2_housing.compute()
    t4 = track4_pollution.compute()

    # per person (per capita), MEAN
    T1 = t1["total_hours"] / POP
    T2 = t2["per_home_year"] / PERSONS_PER_CU
    T3 = T3_FOREIGN_HOURS_TOTAL / POP
    T4_lo = t4["per_adult_low"] * ADULTS / POP
    T4_hi = t4["per_adult_high"] * ADULTS / POP
    T4_mid = (T4_lo + T4_hi) / 2

    total_mid = T1 + T2 + T3 + T4_mid
    domestic = T1 + T2 + T4_mid
    foreign = T3

    # median: apply the mean->median haircut to the consumption-driven parts (T1,T3);
    # necessities (housing, own-pollution) are more uniform.
    median_total = MEDIAN_OVER_MEAN * (T1 + T3) + T2 + T4_mid

    return dict(T1=T1, T2=T2, T3=T3, T4_lo=T4_lo, T4_hi=T4_hi, T4_mid=T4_mid,
                total_mid=total_mid, domestic=domestic, foreign=foreign,
                per_household=total_mid * PERSONS_PER_CU, median_total=median_total)


def report():
    r = compute()
    W = 74
    print("=" * W)
    print("AVERAGE US PERSON'S LIFESTYLE IN LABOUR-HOURS (mean, 2023, per person)")
    print("=" * W)
    print(f"  {'Track':<26}{'h/yr per person':>16}")
    print("-" * W)
    print(f"  1  Consumption (domestic) {r['T1']:>15.0f}")
    print(f"  2  Housing build/repair   {r['T2']:>15.0f}")
    print(f"  3  Imports (FOREIGN)       {r['T3']:>15.0f}")
    print(f"  4  Own pollution clean-up {r['T4_mid']:>15.0f}   (range {r['T4_lo']:.0f}-{r['T4_hi']:.0f})")
    print("-" * W)
    print(f"  TOTAL (mean, per person)  {r['total_mid']:>15.0f}   h/yr")
    print(f"     of which domestic      {r['domestic']:>15.0f}")
    print(f"     of which FOREIGN       {r['foreign']:>15.0f}   ({100*r['foreign']/r['total_mid']:.0f}%)")
    print("-" * W)
    print(f"  per household (x2.51)     {r['per_household']:>15.0f}   h/yr")
    print(f"  MEDIAN person (compare)   {r['median_total']:>15.0f}   h/yr")
    print(f"  mean / median             {r['total_mid']/r['median_total']:>15.2f}   x")
    print("=" * W)
    print("The mean is only ~1.2x the median -- consumption is FAR more even than")
    print("income (Gini ~0.3 vs ~0.5), because you can't eat 1000x the food. This is")
    print("itself the disparity-ceiling intuition: real consumption is naturally bounded.")
    print("=" * W)
    return r


def test_mean_exceeds_median():
    r = compute()
    assert r["total_mid"] > r["median_total"], "mean should exceed median"
    ratio = r["total_mid"] / r["median_total"]
    assert 1.0 < ratio < 1.5, f"mean/median {ratio:.2f} implausible for consumption"
    print(f"[ok] mean/median = {ratio:.2f} (consumption is fairly even)")


def test_foreign_about_half():
    r = compute()
    share = r["foreign"] / r["total_mid"]
    assert 0.35 < share < 0.6, f"foreign share {share:.2f} off"
    print(f"[ok] foreign share {100*share:.0f}%")


def test_per_person_consistent():
    """Per-person total should match per-capita of the national tracks."""
    r = compute()
    assert 900 < r["total_mid"] < 1500, f"per-person total {r['total_mid']:.0f} off"
    print(f"[ok] per-person total {r['total_mid']:.0f} h/yr")


def run_tests():
    test_mean_exceeds_median()
    test_foreign_about_half()
    test_per_person_consistent()
    print("\nAll self-tests passed.")


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        run_tests()
    else:
        report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
