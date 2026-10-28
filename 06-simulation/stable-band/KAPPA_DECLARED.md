# Declared before the run (2026-10-27) — request sr-20261026

Written before `stable_band_kappa.py` was run in full.

## Inputs declared

| Input | Value | Source |
|---|---|---|
| kappa | **1,380 / 365 = 3.7808 debit-h per lifestyle-unit per day** (1,380 h/yr per median person) | Foundations 3.5 anchor |
| old kappa | 13.797 (median daily credit at F = 10), kept only for comparison | `stable_band.calibrate` |
| capacity R_max | **unchanged: 0.85 x sum(wants)** in real lifestyle-units | same as sr-20261023 |
| population | same 60,000 people, seed 7 | `stable_band.build_people` |
| ages, joining, M, past credit, past debit | same as `stable_band_cumulative.py` (age seeds 11-15, M = 100, C0 = F*365*age, D0 = 1,380*age, everyone joins day one) | |

## Reasoning, stated so it can be wrong

- One-day gate: requests scale with kappa and capacity is in real units, so admitted real units depend on rho / kappa only. **The one-day edge should be the old edge x 3.7808 / 13.797 = 0.274 x old.** Old edges 3.70 / 1.20 / 0.90 give about **1.01 / 0.33 / 0.25** at F = 2 / 10 / 14.
- Break-even 3.78 / F is 1.89 / 0.378 / 0.270. So the one-day edge should sit **below** break-even at F = 2 and F = 10 and near it at F = 14.
- Past debit is now 1,380 h/yr = kappa x 365, the same rate as the yearly request. Per sr-20261023, that is the case where the cumulative edge equals the one-day edge.

## Outcomes

| # | Kind | Declaration | It fails if |
|---|---|---|---|
| O1 | **Level** | One-day rho* at F = 10 lies in **[0.28, 0.38]** | outside that range |
| O2 | **Level** | One-day rho* at F = 2 lies in **[0.85, 1.20]** and at F = 14 in **[0.20, 0.30]** | either is outside |
| O3 | **Level** | Cumulative rho*_L at F = 10 lies in **[0.28, 0.38]** (old kappa: 0.42) | outside that range |
| O4 | Relation | Cumulative rho*_L is within **5%** of one-day rho* at all three F | any gap > 5% |
| O5 | Instrument | Scaling check: new one-day edge = old edge x 0.274, within +/- 0.03 at each F | gap > 0.03 |
| O6 | Capacity | Capacity binds at kappa = 1,380: with rho = 4.0 admitted real units > R_max, and the edge is not censored or below-grid | edge flagged "below" or "censored" |
