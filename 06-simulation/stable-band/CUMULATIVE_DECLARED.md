# Declared before the full run (2026-10-26)

Written after the six self-tests passed and before `python stable_band_cumulative.py` was run in full.
Inputs are in the header of `stable_band_cumulative.py`. Outcomes:

| # | Kind | Declaration | It fails if |
|---|---|---|---|
| O1 | **Level** | rho*_L at F = 10 lies in **[0.30, 0.90]** (one-day: 1.20) | it is >= 1.10, or < 0.30 |
| O2 | Direction | rho*_L < one-day rho* at F = 2, 10 and 14 | any of the three is >= its one-day value |
| O3 | **Level** | The F = 2 edge falls LEAST in absolute terms is NOT assumed. Declared: the fall in rho (one-day minus L) at F = 2 is **larger than 1.0** (one-day is 3.70) | the F = 2 fall is <= 1.0 |
| O4 | Return time | At F = 10, rho = 1.2, admitted demand does **not** come back within 1.01 x the one-day level inside M = 100 periods | it returns at t <= 100 |
| O5 | Instrument | At age 0 the edge equals the one-day edge (+/- 0.02) | it differs by more than 0.02 |

Reasoning, stated so it can be wrong: a joiner of age a arrives with room (rho*F*365 - 1,380)*a already on the books. At F = 10, rho = 1.2 that is 3,000 h a year of age, which a year of demand (~5,000 h) takes a long time to use. At F = 2 the room is negative for rho < 1.89, so the F = 2 edge should fall by less in relative terms than the F = 14 edge.
