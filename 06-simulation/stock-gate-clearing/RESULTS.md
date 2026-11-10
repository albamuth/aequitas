# Stock-gate clearing rate after a −30% capacity year

## 1. The question (quoted)

> Stock-gate clearing rate after a capacity shock. Population, wants and capacity as rho_sweep_anchor.py (N, seed, CAP 0.85, sigma 0.45, kappa 1380/365), ages from stable_band_cumulative.py's pyramid. Build each ledger in steady state at rho0 = 0.33, F = 10: C = c*365*age, D = 365*age*min(wants*kappa, rho0*c). Then one year at -30% capacity through gate.py's stock room(). Report: rho at which that year's admitted demand equals capacity; admitted demand by age band and by credit decile against baseline; share of people admitting zero; the next year's demand with rho restored to 0.33. Three arms: gate on all demand; gate only on demand above E = 826 h/yr; D excluding ages under 14. Also F = 2 and 14. Print the flow rho* (0.19) beside it.

## 2. Outcomes declared before the first run (README.md)

| # | Statement | Kind | Result (F=10, rho0=0.33) | Held? |
|---|---|---|---|---|
| 1 | Flow rho* at −30% reads 0.19 ± 0.02 on this code | LEVEL | **0.186** | Yes |
| 2 | Arm A stock rho_s is in [0.21, 0.33) | LEVEL | **0.323** | Yes, 0.007 below the top |
| 3 | More than 5% of people admit zero at rho_s | LEVEL | **13.4%** (16.2% of people aged 14+) | Yes |
| 4 | Year 2 at rho 0.33 admits more than 1% above the baseline year | CHANGE | **+13.0%** | Yes |
| 5 | Arm B: the ungated part alone is at least 90% of shocked capacity | LEVEL | **88.6%** | **No**, by 1.4 points. A clearing rho exists (0.251) |
| 6 | Arm C moves rho_s by more than 0.02 from arm A | CHANGE | 0.189 vs 0.323 | Yes, but see §4: arm C's own baseline no longer clears |

## 3. The numbers

Population 200,000, seed 7. Ages: seeds 11 to 15. Capacity in "want units" (1 unit = 1,380 h): full = 0.85 × 221,652 = **188,404**; shocked (−30%) = **131,883**. The five age seeds agree to within 0.002 in rho_s, so the spread comes from ages only. The population was drawn once.

### Headline, F = 10, rho0 = 0.33

| | Flow gate (published) | **Stock, arm A** (all demand) | Arm B (gate above E = 826 h) | Arm C (D excl. ages < 14) |
|---|--:|--:|--:|--:|
| rho that makes the shocked year's admitted demand = capacity | **0.186** (0.19) | **0.323** (0.323 – 0.323) | **0.251** (B2: 0.240) | 0.189 (C2: 0.190) |
| People admitting zero, all / aged 14+ | n/a | 13.4% / 16.2% | 0.0% / 0.0% | 30.5% / 36.7% |
| Next year at rho 0.33, units (× full capacity) | n/a | 213,067 (**1.131**) | 209,781 (1.113) | 221,652 (1.176) |
| Baseline year at rho 0.33, units (× full capacity) | 188,531 (1.001) | 188,531 (1.001) | same ledger | **221,652 (1.176)**, ungated |

**Reading arm A.** The stock rho_s is 0.323, which is 1.74 times the flow 0.186. A stock gate that clears the −30% year sits 0.010 below the 0.33 that clears the normal year. The shock moves the stock rho by 0.010; it moves the flow rho by 0.144.

**Why.** People who did not bind in the past carry stored room. A non-binder with age 40 holds `0.33 × c × 365 × 41 − D` of room, far more than one year's request. Cutting rho from 0.33 to 0.19 barely trims them. The cut falls on people already bound (those whose want exceeds 0.33·c/κ), who have no stored room.

**Admitted demand against the same ledger's baseline year (arm A, F=10, mean of 5 age seeds).**

| Age band | 0–18 | 18–35 | 35–50 | 50–65 | 65–85 |
|---|--:|--:|--:|--:|--:|
| Shock year, units | 37,831 | 33,184 | 22,408 | 20,272 | 18,189 |
| Baseline year, units | 41,391 | 43,499 | 35,868 | 35,681 | 32,092 |
| Ratio | **0.914** | 0.763 | 0.625 | 0.568 | **0.567** |

| Credit decile (low to high C) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Shock, units | 17,353 | 15,799 | 14,241 | 13,036 | 11,755 | 10,737 | 10,512 | 10,676 | 12,603 | 15,173 |
| Baseline, units | 18,282 | 18,242 | 18,161 | 18,258 | 18,370 | 18,333 | 18,476 | 18,715 | 20,069 | 21,624 |
| Ratio | **0.949** | 0.866 | 0.784 | 0.714 | 0.640 | 0.586 | **0.569** | 0.570 | 0.628 | 0.702 |

The people with the least credit (youngest, largest ratio) lose 5%. The people with the most stored credit-per-debit in the middle deciles (older, long histories at a binding rho0) lose 43%. **Under the stock gate the burden falls on the old, which a flow gate cannot show.** Arm B spreads the cut almost evenly (ratios 0.68 to 0.73 across every decile and band).

### Other floors

| F | rho0 (primary) | Baseline year ÷ capacity | Flow rho* at −30% | **Stock rho_s, arm A** | Zero, aged 14+ | Next year ÷ full capacity |
|--:|--:|--:|--:|--:|--:|--:|
| 2 | 1.017 | 1.031 | 0.457 | **0.919** | 35.0% | 1.151 |
| 10 | 0.330 | 1.001 | 0.186 | **0.323** | 16.2% | 1.131 |
| 14 | 0.253 | 0.999 | 0.145 | **0.248** | 14.3% | 1.129 |

(Flow rho* at F = 2 and 14 here is this code's reading; the published 0.19 is for F = 10 only.)

**Sensitivity, rho0 = 0.33 at every F.** F = 14: baseline year is 1.092 × capacity, stock rho_s 0.280, 25.9% of adults admit zero. **F = 2: the baseline year admits only 0.543 × capacity, so the ledger never cleared capacity to begin with. That cell is not a clearing result.**

### Arm B (gate only above E = 826 h/yr)

The first 826 h of each request is ungated. At F=10 it sums to **88.6% of shocked capacity**; only 12.9% of people want less than 826 h a year in total. Stock rho_s is 0.251, and nobody admits zero. Because ungated demand takes 88.6% of capacity, the gate rations the last 11.4% and rho_s is set by who is above E.

### Arm C (D excludes ages under 14) — the arm as asked does not hold together

Removing under-14 debit from the past leaves every adult with credit for ages 0–14 that nothing was ever charged against. At rho0 = 0.33 the **baseline year already admits 1.176 × capacity, with nobody gated** (the "next year = 1.000 × own baseline" in the raw output is that: all demand admitted). The 0.189 in the table is therefore a clearing rho measured from a baseline that was not clearing. **Recalibrated** (`--armc`): rho0 solved so arm C's own unshocked year admits exactly capacity gives **rho0_C = 0.020 and stock rho_s = 0.017 at F = 10** (F=2: 0.055 → 0.046; F=14: 0.016 → 0.013). That is a rho an order of magnitude below the band. Whether children's credit should also be excluded was not asked and not run.

## 4. What this does not show

1. **One population draw, one capacity-binding rule.** Population seed 7, one draw. Age seeds vary rho_s by under 0.002, so nothing here says how the result moves with the population draw, with sigma 0.45, or with the (c/median)^0.25 want-credit link.
2. **Wants are independent of age.** A 5-year-old wants as much as a 40-year-old, and 22% of people are under 18. Arm A's 0.914 ratio for ages 0–18 and the whole age-band profile are driven by that. A real age profile of wants could reverse the band ordering.
3. **Steady state is built by formula, not grown.** D = 365·age·min(wants·κ, ρ0·c) says everyone has consumed their capped request every year of their life at today's wants. There are no births, deaths, changing wants or earlier shocks. The result that older people absorb the cut follows from that: they hold the largest stored room differences.
4. **Capacity −30% is applied to want-units uniformly.** No sector structure, no essentials priority; "capacity equals admitted demand" is one scalar match.
5. **Arm C is one reading of "D excluding ages under 14"** (past debit removed, current-year child consumption ungated, child credit kept). The recalibration shows this reading breaks the steady state. A reading that also drops child credit was not run.
6. **Year 2 assumes capacity fully restored.** Year 2 admits 1.131 × full capacity in arm A. That overshoot is a demand-side fact (restored rho releases people rationed in year 1); it says nothing about whether supply can respond.
7. **P = 0 and no pledges.** The pledge term (5.5.3) lowers the edge by 1/(1+p) on the flow gate; it was not applied to a stock gate here.
8. **Stock rho_s near 0.323 sits 0.010 under 0.33.** That near-equality is partly built in: at rho0 = 0.33 the non-binders have large stored room, so the gate has little to cut. A rho0 that does not clear capacity (F = 2, rho0 = 0.33) shows the number depends on the steady-state calibration.

## 5. Command and seed

```
cd 06-simulation/stock-gate-clearing
python stock_gate_clearing.py --test            # 7 self-tests
python stock_gate_clearing.py > RESULTS_RAW.txt # about 55 s, population seed 7, age seeds 11..15
python stock_gate_clearing.py --armc > RESULTS_ARMC_RAW.txt
```

Raw output: `RESULTS_RAW.txt`, `RESULTS_ARMC_RAW.txt`. Files written are under 100 KB in total.
