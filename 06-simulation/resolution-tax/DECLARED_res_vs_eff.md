# Declared before the first run — 2026-10-25

Written before `res_vs_eff.py` was run for the first time.

| # | Outcome | Kind | Counts against it |
|---|---|---|---|
| E1 | Steer hide reads 12.50 coarse, 2.00 fine; packaged beef 2.00 both | Level | any other figure |
| E2 | Calibrated efficiency spread: mean max/min of 3 producers = 1.82 (SIG_A about 0.30 to 0.40) | Level (calibration, not a check) | SIG_A outside 0.2–0.6 |
| E3 | At the calibrated SIG_A, n=12, all goods, uniform exits: median RES p90/p10 lies **between 1.2 and 3.0**. (Earlier run, other statistic: median best-to-worst about 1.9 over all goods.) | Level | median under 1.2 or over 3.0 |
| E4 | EFF median p90/p10 at calibrated SIG_A = exp(2.563 × SIG_A), about 2.4 to 2.5 | Level | off by more than 8% |
| E5 | **RES does not dominate EFF at the calibrated SIG_A**: RES variance share of ln(figure) is below 50% | Change/size | share at or above 50% |
| E6 | RES variance share is **not** stable: it crosses 50% somewhere inside SIG_A in 0.1–1.0 | Change | share stays on one side across the whole sweep |
| E7 | A flat chain (sigma 0) with uniform exits does NOT return RES near 1.0 (brief section 7 says it does). Median RES p90/p10 above 1.3 | Level | median at or under 1.3 |
| E8 | Late-exit goods (last third of chain) have much smaller RES than uniform exits: median p90/p10 under 1.3 at sigma 0.8 | Level | at or above 1.3 |

Verdict rule, fixed now: **"RES dominates"** means RES variance share ≥ 50% at the calibrated SIG_A **and** RES median p90/p10 ≥ EFF median p90/p10. **"RES is noise"** means RES variance share < 20%. Anything between is **"same order, neither dominates"**.
