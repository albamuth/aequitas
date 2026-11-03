# Stable band at the every-payer peer ratios — results

Request `sr-20261029-re-run-stable-band-methods-py-the-kappa-tied`, run 2026-10-30. Code: `stable_band_payers.py` (reuses `stable_band_methods.py`). Declared inputs and outcomes, written before the full run: `PAYERS_DECLARED.md`. Raw output: `PAYERS_RUN.txt`.

## 1. The question (quoted from the request)

> Re-run stable_band_methods.py (the kappa-tied band at another production method) at the every-payer peer ratios of 06-simulation/median-lifestyle/Q6_PAYERS_RUN.txt: peers at 0.836 (Germany, Japan), 0.858 (France) and 0.873 (Sweden) of the US yearly demand of 1,380 h, so kappa = 1,153.7 / 1,184.0 / 1,204.7 h/yr, with capacity = 778,955 h divided by (kappa / 100) units (US capacity 56,446 units at 13.80 h a unit) against wants of 66,407. Report at F = 2, 10, 14 the one-day and cumulative rho* where a capacity edge exists (say 'none' where it does not) and rho_sat, beside break-even kappa/(365*F). Scale both essentials baskets by the same ratio and declare that scaling as an assumption. Say whether the band is open on each basket. Leave Spain out (data gap). Keep the US control.

## 2. Outcomes declared before running, and how each came out

| # | Kind | Declared | Result |
|---|---|---|---|
| O1 | Level | Germany/Japan: every edge is "none" | **HELD.** All 6 cells censored. Admitted at rho = 4.0 is 66,381 (F=2) and 66,407 (F=10, 14) against capacity 67,519 |
| O2 | Level | France and Sweden: an edge exists everywhere | **HELD.** All 12 cells are numbers |
| O3 | Level | One-day edge at F = 10: France [0.55, 0.85], Sweden [0.40, 0.65] | **HELD.** 0.612 and 0.496 |
| O4 | Level | One-day edge at F = 2: France [1.3, 2.6], Sweden [1.0, 2.2] | **HELD.** 2.365 and 1.823 |
| O5 | Level | Break-even arithmetic (Sweden F=10 0.330, France F=2 1.622) | **HELD** |
| O6 | Level | Broad basket open at F = 10, 14 for all three; at F = 2 for 0.836 and 0.858 | **HELD.** Also open for Sweden at F = 2 |
| O7 | Instrument | US control 1.017 / 0.330 / 0.253 within 0.01 | **HELD.** Exact |
| O8 | Relation | Edge per unit of ratio is lower for the tighter capacity (Sweden) than France | **HELD.** F=2: 2.757 vs 2.088; F=10: 0.713 vs 0.568; F=14: 0.535 vs 0.428 |
| O9 | Level | Cumulative edge within 5% of one-day edge | **FAILED, by a lot.** Cumulative is 9% to 46% below one-day (table 3a) |

Note on capacity: the code computes 778,955 / (h/100) from h = 1,380 x ratio, giving 67,519 / 65,788 / 64,658. The declared file said 67,515 / 65,790 (rounded h). The difference is below 0.01% and moves no result.

## 3. The numbers

60,000 people, seed 7. Total wants 66,407 real units. Cumulative: 5 age seeds (11-15), 100 yearly periods, a joiner's past debit = the method's own yearly figure, floor-only past credit. Spread = standard deviation over the 5 age seeds. rho* = highest rho at which admitted real units <= capacity.

### 3a. Upper edge rho* (capacity edge)

| Peer | h/yr | kappa | Capacity (units, share of wants) | F | Break-even h/(365 F) | One-day rho* | Cumulative rho* (mean, sd) |
|---|--:|--:|--:|--:|--:|--:|--:|
| **Germany, Japan** (0.836) | 1,153.7 | 3.1608 | 67,519 (101.7%) | 2 | 1.580 | **none** | **none** |
| | | | | 10 | 0.316 | **none** | **none** |
| | | | | 14 | 0.226 | **none** | **none** |
| **France** (0.858) | 1,184.0 | 3.2439 | 65,788 (99.1%) | 2 | 1.622 | 2.365 | 1.653 (0.0007) |
| | | | | 10 | 0.324 | 0.612 | 0.342 (0.0005) |
| | | | | 14 | 0.232 | 0.459 | 0.246 (0.0005) |
| **Sweden** (0.873) | 1,204.7 | 3.3007 | 64,658 (97.4%) | 2 | 1.650 | 1.823 | 1.656 (0.0000) |
| | | | | 10 | 0.330 | 0.496 | 0.337 (0.0001) |
| | | | | 14 | 0.236 | 0.374 | 0.242 (0.0001) |
| US (control) | 1,380 | 3.7808 | 56,446 (85.0%) | 2 | 1.890 | 1.017 | 1.017 (0.000) |
| | | | | 10 | 0.378 | 0.330 | 0.330 (0.000) |
| | | | | 14 | 0.270 | 0.253 | 0.253 (0.000) |

"none" means admitted <= capacity at every rho from 0.005 to 4.0 (the swept range; nothing above 4.0 was looked at). For Germany and Japan this is **entailed by the input**: capacity 67,519 is above total wants 66,407 before any person is simulated (brief 4b). France and Sweden are the cells that could have failed, and the edge is a real number there only because capacity (65,788 / 64,658) is below wants.

**The cumulative edge sits just above break-even.** France: 1.653 / 0.342 / 0.246 against break-even 1.622 / 0.324 / 0.232 (1.9% / 5.5% / 6.0% above). Sweden: 1.656 / 0.337 / 0.242 against 1.650 / 0.330 / 0.236 (0.4% / 2.1% / 2.5% above). Above break-even a joiner's past and future both leave net room each year, so the capacity test fails late in life no matter what; the cumulative edge cannot go meaningfully above break-even at a capacity this close to wants.

### 3b. rho_sat: where the gate stops holding people back (>= 99.9% of wants admitted)

| Peer | F | One-day rho_sat | Cumulative rho_sat (mean, sd) | Break-even |
|---|--:|--:|--:|--:|
| Germany, Japan | 2 | 3.501 | 3.312 (0.0120) | 1.580 |
| | 10 | 0.855 | 0.796 (0.0034) | 0.316 |
| | 14 | 0.638 | 0.592 (0.0015) | 0.226 |
| France | 2 | 3.593 | 3.399 (0.0123) | 1.622 |
| | 10 | 0.878 | 0.817 (0.0034) | 0.324 |
| | 14 | 0.655 | 0.608 (0.0016) | 0.232 |
| Sweden | 2 | 3.655 | 3.459 (0.0126) | 1.650 |
| | 10 | 0.893 | 0.832 (0.0035) | 0.330 |
| | 14 | 0.666 | 0.618 (0.0016) | 0.236 |
| US (control) | 2 | >= 4.0 (censored) | 3.962 (0.0144) | 1.890 |
| | 10 | 1.023 | 0.952 (0.0041) | 0.378 |
| | 14 | 0.763 | 0.708 (0.0019) | 0.270 |

**Where an upper edge exists (France, Sweden), rho_sat is far above it.** France F=10: edge 0.612 (one-day), rho_sat 0.878. Between the two, the gate holds some people below their wants and total admitted is still above capacity: capacity is rationed by the gate in that range. Above rho_sat everyone is admitted and capacity (99.1% or 97.4% of wants) cannot cover it, so shortage is settled at distribution (Foundations 5.5.3).

### 3c. Is the band open? (Assumption A applied)

**ASSUMPTION A (declared, not measured): each essentials basket scales by the same ratio as the median lifestyle.** Narrow 516-655 h and broad 826-965 h become, at 0.836: 431-548 and 691-807 h; at 0.858: 443-562 and 709-828 h; at 0.873: 450-572 and 721-842 h. Nobody measured a peer's essentials basket.

Band = rho between lower edge E/(365 F) and the upper edge. Lower edge shown uses the top of each basket range (the hard case); the range is low-high.

| Peer | F | Narrow lower edge | Broad lower edge | Upper edge (one-day / cumulative) | Narrow | Broad |
|---|--:|--:|--:|---|---|---|
| Germany, Japan | 2 | 0.591-0.750 | 0.946-1.105 | none / none | Open (no upper edge) | Open (no upper edge) |
| | 10 | 0.118-0.150 | 0.189-0.221 | none / none | Open | Open |
| | 14 | 0.084-0.107 | 0.135-0.158 | none / none | Open | Open |
| France | 2 | 0.606-0.770 | 0.971-1.134 | 2.365 / 1.653 | Open | Open |
| | 10 | 0.121-0.154 | 0.194-0.227 | 0.612 / 0.342 | Open | Open |
| | 14 | 0.087-0.110 | 0.139-0.162 | 0.459 / 0.246 | Open | Open |
| Sweden | 2 | 0.617-0.783 | 0.988-1.154 | 1.823 / 1.656 | Open | Open |
| | 10 | 0.123-0.157 | 0.198-0.231 | 0.496 / 0.337 | Open | Open |
| | 14 | 0.088-0.112 | 0.141-0.165 | 0.374 / 0.242 | Open | Open |

The band is open on both baskets in all 9 peer cells, on both the one-day and the cumulative edge. The narrowest margin is Sweden at F = 2, broad basket, cumulative edge: lower edge up to 1.154, upper edge 1.656 (gap 0.50). At the US method the same F = 2 broad cell is closed (1.132-1.322 against 1.017).

## 4. What this does not show

1. **"None" for Germany and Japan is a consequence of the capacity input.** Capacity 67,519 is 101.7% of wants. Foundations 5.5.3 says the true figure lies between 97% and 102% and that which side is not determined. This run shows both sides: at 101.7% there is no edge, at 99.1% the edge is 0.612 (F=10), at 97.4% it is 0.496. Whether the German and Japanese envelope delivers 101.7% or something below 100% decides whether an edge exists. The 778,955 h envelope is supplied by the request and not re-derived here.
2. **The baskets are scaled, not measured (Assumption A).** An essentials basket may not shrink with the whole lifestyle; food, shelter and care are the items an efficient economy may save least on. If the broad basket did not scale at all (826-965 h) the F = 2 lower edge would be 1.13-1.32 and the band would still be open on every peer, because the smallest F = 2 upper edge is 1.653 (France, cumulative). The band only closes at F = 2 if the broad basket exceeds 1.653 x 730 = 1,207 h, which is 87% of the US yearly figure. That is the margin Assumption A has to survive.
3. **The cumulative edge is built from a declared joiner past.** A joiner's past debit equals the peer's own yearly figure (1,153.7 / 1,184.0 / 1,204.7 h). A joiner arriving from a US past (1,380 h/yr) would carry more debit and the cumulative edge would fall. That case is not run. The cumulative edge sitting within 0.4% to 6% of break-even is a property of past rate = flow rate (as in RESULTS_KAPPA) and not a measurement of a real economy.
4. **Open means affordable and not rationed by capacity. It does not mean the gate is idle.** rho_sat at F = 10 is 0.86 to 0.89 (one-day) for the peers. A tolerance below that holds some people below their wants.
5. **Demand per person is a declared input.** Each person's yearly demand is wants x kappa x 365, median at the peer's h, log-normal spread sigma 0.45 shared with earlier runs. The spread is invented.
6. **Everyone joins on day one with no held property, nobody is born or dies in 100 years, past credit is floor only.** Same limits as `RESULTS_KAPPA.md`.
7. **The pledge term is not run.** Pledges can double effective tolerance (Foundations 4.6); the upper edges would halve in published rho.
8. **The peer ratios are every-payer labour-hour ratios from EXIOBASE for 2022** (`Q6_PAYERS_RUN.txt`, AIC-matched column). Their accuracy is not tested here. Spain and Poland are excluded for data gaps.
9. **Capacity does not depend on how many people hold the same envelope, or on trade.** It is a single number per method.

## 5. Command and seed

```
python 06-simulation/stable-band/stable_band_payers.py --test     # 6 self-tests, under 1 min
python 06-simulation/stable-band/stable_band_payers.py            # full run, about 2 minutes
```

Population seed 7 (N = 60,000). Age seeds 11, 12, 13, 14, 15. M = 100. Grid: rho 0.005 to 4.0, bisection tolerance 3e-4. Python 3 with numpy. Raw output: `PAYERS_RUN.txt`.
