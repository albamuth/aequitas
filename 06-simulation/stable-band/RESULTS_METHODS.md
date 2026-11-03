# Stable band at the German/Japanese and Spanish methods — results

Request `sr-20261028-re-run-stable-band-kappa-py-at-the-german-ja`, run 2026-10-29. Code: `stable_band_methods.py`. Declared inputs and outcomes, written before the full run: `METHODS_DECLARED.md`.

## 1. The question (quoted from the request)

> Re-run stable_band_kappa.py at the German/Japanese and the Spanish production methods. Tie each person's yearly demand to that method's median lifestyle (883 and 759 h/yr) and set capacity to what the same physical envelope delivers under that method (88,196 and 102,629 units against wants of 66,407). Report the one-day and cumulative upper edge rho* at F = 2, 10, 14 beside break-even (883 or 759)/(365F). Scale the narrow (516-655 h) and broad (826-965 h) essentials baskets by the method ratio, DECLARE that scaling as an assumption, and say at each F whether the band is open on each basket. Say plainly if the gate never binds, so that there is no upper edge.

## 2. Outcomes declared before running, and how each came out

| # | Kind | Declared | Result |
|---|---|---|---|
| O1 | Level | Capacity never binds; every upper edge censored at the grid top (4.0); admitted <= 66,407 | **HELD.** Admitted at rho = 4.0 is 66,404 (F=2) and 66,407 (F=10, 14), against capacity 88,196 / 102,629. All 12 edges (2 methods x 3 F x one-day/cumulative) came back "censored" |
| O2 | Level | German lower edge at F = 2: broad in [0.72, 0.85], narrow in [0.45, 0.58] | **HELD.** Broad 0.724-0.846, narrow 0.452-0.574 |
| O3 | Level | Spanish broad lower edge at F = 2 in [0.62, 0.73] | **HELD.** 0.622-0.727 |
| O4 | Level | Band open on both baskets, both methods, at F = 2 | **HELD** |
| O5 | Level | Break-even arithmetic to 3 decimals: German 1.209 / 0.2419 / 0.1728; Spanish 1.040 / 0.2079 / 0.1485 | **FAILED on one digit.** 883 / 730 = 1.2096, which rounds to 1.210, not the declared 1.209 (truncation error in the declaration). The other five match |
| O6 | Level | rho_sat at F = 10 in [0.25, 0.60] (German), [0.20, 0.55] (Spanish) | **FAILED, both.** German 0.655, Spanish 0.563. Both sit just above the declared range. The declared ranges were too low by about 10% |
| O7 | Instrument | US control at kappa 1,380 reproduces 1.017 / 0.330 / 0.253 within 0.01 | **HELD.** 1.017 / 0.330 / 0.253 exactly |
| O8 | Relation | Cumulative rho_sat within 5% of one-day rho_sat | **FAILED.** Cumulative is 5.4% to 7.2% lower at all six cells (ratio 0.928-0.946) |

## 3. The numbers

60,000 people, seed 7. Total wants 66,407 real units. Cumulative: 5 age seeds (11-15), 100 yearly periods, past debit of a joiner = the method's own yearly figure (883 or 759 h), floor-only past credit. Spread is the standard deviation over the 5 age seeds. `rho*` is the highest rho at which admitted real units <= capacity.

### 3a. The upper edge rho*

| Method | kappa (debit-h/unit/day) | Yearly median demand | Capacity (units) | F | Break-even (yr demand)/(365 F) | One-day rho* | Cumulative rho* |
|---|--:|--:|--:|--:|--:|---|---|
| **German/Japanese** | 2.4192 | 883 h | 88,196 | 2 | 1.2096 | **none** (>= 4.0, censored) | **none** (censored, sd 0) |
| | | | | 10 | 0.2419 | **none** | **none** |
| | | | | 14 | 0.1728 | **none** | **none** |
| **Spanish** | 2.0795 | 759 h | 102,629 | 2 | 1.0397 | **none** | **none** |
| | | | | 10 | 0.2079 | **none** | **none** |
| | | | | 14 | 0.1485 | **none** | **none** |
| US (control) | 3.7808 | 1,380 h | 56,446 | 2 | 1.8904 | 1.017 | 1.017 (sd 0.000) |
| | | | | 10 | 0.3781 | 0.330 | 0.330 (sd 0.000) |
| | | | | 14 | 0.2701 | 0.253 | 0.253 (sd 0.000) |

**The gate never binds against capacity at either efficient method, so there is no upper edge.** Reason: people want 66,407 units in total and the envelope delivers 88,196 or 102,629. Admitted units cannot exceed wants, so "admitted <= capacity" is true at every rho from 0.005 to 4.0. (The 4.0 is the end of the swept range. Nothing above it was looked at, as in the earlier runs.)

**This result is entailed by the capacity figures the request supplies, not discovered by the simulation** (brief 4b). The capacity numbers are above total wants before any person is simulated. The control row (US, capacity 56,446 < wants) does produce numbers, and `test_capacity_below_wants_can_bind` shows the same code returns a real edge for the German kappa when capacity is set to 0.85 x wants (0.211 at F=10). So the "none" comes from the capacity input and not from the code.

### 3b. What can still fail: rho_sat, where the gate stops holding people back

`rho_sat` = lowest rho at which at least 99.9% of wants (66,341 of 66,407 units) are admitted. This is a different thing from the upper edge. It says where the gate stops being felt by anyone, whatever the capacity.

| Method | F | Lower edge, narrow (top of range) | Lower edge, broad (top of range) | One-day rho_sat | Cumulative rho_sat (mean, sd) | Cum / one-day |
|---|--:|--:|--:|--:|--:|--:|
| German/Japanese | 2 | 0.574 | 0.846 | 2.679 | 2.535 (0.009) | 0.946 |
| | 10 | 0.115 | 0.169 | 0.655 | 0.609 (0.003) | 0.931 |
| | 14 | 0.082 | 0.121 | 0.488 | 0.453 (0.001) | 0.928 |
| Spanish | 2 | 0.493 | 0.727 | 2.303 | 2.179 (0.008) | 0.946 |
| | 10 | 0.099 | 0.145 | 0.563 | 0.524 (0.002) | 0.931 |
| | 14 | 0.070 | 0.104 | 0.420 | 0.389 (0.001) | 0.928 |
| US (control) | 2 | 0.897 | 1.322 | >= 4.0 (censored) | 3.962 (0.014) | n/a |
| | 10 | 0.179 | 0.264 | 1.023 | 0.952 (0.004) | 0.931 |
| | 14 | 0.128 | 0.189 | 0.763 | 0.708 (0.002) | 0.928 |

Share of people held below their wants at F = 10 (one-day): at rho = 0.25, 57.8% (US), 23.5% (German), 14.9% (Spanish). At rho = 1.2, 0.1% (US) and 0.0% for the other two.

### 3c. Is the band open? (Assumption A applied)

**ASSUMPTION A (declared, not measured): each essentials basket scales by the method ratio.** Narrow 516-655 h becomes 330-419 h (German, x 0.6399) and 284-360 h (Spanish, x 0.5500). Broad 826-965 h becomes 529-617 h (German) and 454-531 h (Spanish). Nobody has measured the essentials basket under the German or Spanish method. The ratio is the ratio for the whole median lifestyle.

Lower edge = E / (365 F), using the top of each basket range (the hard case). Band is open when the lower edge is below the upper edge. With no upper edge it is open wherever the lower edge is a reachable rho.

| Method | F | Narrow basket | Broad basket |
|---|--:|---|---|
| German/Japanese | 2 | **Open**, no upper edge (lower 0.452-0.574) | **Open**, no upper edge (lower 0.724-0.846) |
| | 10 | **Open** (0.090-0.115) | **Open** (0.145-0.169) |
| | 14 | **Open** (0.065-0.082) | **Open** (0.103-0.121) |
| Spanish | 2 | **Open** (0.389-0.493) | **Open** (0.622-0.727) |
| | 10 | **Open** (0.078-0.099) | **Open** (0.124-0.145) |
| | 14 | **Open** (0.056-0.070) | **Open** (0.089-0.104) |

The lower-edge range at F = 2 for the German broad basket, 0.724-0.846, matches the 0.72-0.85 that Foundations 5.5.3 inferred by the same scaling. That is expected: it is the same division, 529-617 / 730. What this run adds is the other half: at the German and Spanish capacity there is no upper edge for it to sit above.

## 4. What this does not show

1. **The "no upper edge" is a consequence of the capacity input.** Capacity (88,196 and 102,629) was set from the Q6 efficiency ratio applied to an envelope that is 85% of wants at the US method. If the envelope were smaller, or the efficient methods delivered less than Q6 says, an edge would appear. Run at capacity 0.85 x wants with the German kappa, the one-day edge is 0.651 / 0.211 / 0.162 at F = 2 / 10 / 14. At F = 2 the German broad basket (lower edge up to 0.846) would then be **closed**, because 0.846 is above 0.651. The narrow basket (up to 0.574) would stay open. So the opening of the broad basket at F = 2 depends on the capacity figure and on nothing else in this run.
2. **The baskets are scaled, not measured (Assumption A).** An essentials basket may not shrink by the same 0.64 or 0.55 as a whole median lifestyle. Food, shelter and care are the items an efficient economy may save least on. Lower edges at F = 2 run from 0.45 to 0.85. If the basket scaled by 0.80, the German broad lower edge at F = 2 would be 826-965 x 0.80 / 730 = 0.91-1.06, and it would still be open only because there is no upper edge.
3. **Open here means affordable and not rationed by capacity. It does not mean the gate is idle.** At F = 2, German method, rho_sat is 2.68. A tolerance below that holds some people below their wants. At rho = 1.2 and F = 2 the gate still binds on some people. Whether that is a defect depends on whether a network wants the gate to ration individuals.
4. **Demand tied to a yearly figure is a declared input.** Each person's yearly demand is wants x kappa x 365, with the median at 883 or 759 h. That reproduces the median lifestyle and spreads everyone else log-normally (sigma 0.45) around it. The spread is invented and shared with the earlier runs.
5. **The cumulative arm sets a joiner's past debit equal to the method's own yearly figure.** A joiner from a US past (1,380 h/yr) entering an efficient economy would carry more debit. That case is not run.
6. **Everyone joins on day one with no held property, nobody is born or dies in 100 years, and past credit is floor only.** Same limits as `RESULTS_KAPPA.md`.
7. **The 883 and 759 h figures are quoted from Foundations 5.5.3.** They do not appear as those digits in `median-lifestyle/Q6.md` (searched). The ratios 0.640 and 0.550 match the `EFF` constants in `stable_band.py`, which cite 820/1,283 and 709/1,283 h. 883/1,380 = 0.6399 and 759/1,380 = 0.5500 agree to 3 decimals.
8. **The pledge term is not run.** Pledges can double the effective tolerance (Foundations 4.6). With no upper edge the pledge halving has nothing to halve, but rho_sat would halve.
9. **The capacity numbers 88,196 / 102,629 are used as given.** They are 56,446 / 0.640 and 56,446 / 0.550 (88,197 and 102,629 on recomputation). Capacity does not depend on how many people hold the same envelope, or on trade.

## 5. Command and seed

```
python 06-simulation/stable-band/stable_band_methods.py --test     # 6 self-tests, ~1 min
python 06-simulation/stable-band/stable_band_methods.py            # full run, a few minutes
```

Population seed 7 (N = 60,000). Age seeds 11, 12, 13, 14, 15. M = 100. Grid: rho 0.005 to 4.0, bisection tolerance 3e-4. Python 3 with numpy 2.5.1. Raw output: `METHODS_RUN.txt`.
