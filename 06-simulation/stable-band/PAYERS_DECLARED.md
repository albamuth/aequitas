# Declared before the run (2026-10-30) — request sr-20261029-re-run-stable-band-methods-py-the-kappa-tied

Written before `stable_band_payers.py` was run in full.

## Inputs

| Peer | Ratio to US | Yearly demand h = 1,380 x ratio | kappa = h/365 | Capacity = 778,955 / (h/100) | Capacity / wants (66,407) |
|---|--:|--:|--:|--:|--:|
| Germany, Japan | 0.836 | 1,153.7 | 3.1608 | 67,515 | 1.017 |
| France | 0.858 | 1,184.0 | 3.2438 | 65,790 | 0.991 |
| Sweden | 0.873 | 1,204.7 | 3.3007 | 64,658 | 0.974 |
| US control | 1.000 | 1,380 | 3.7808 | 56,446 | 0.850 |

- Spain left out (data gap), as requested. Population, ages, M = 100, floor-only past credit, past debit = the method's own yearly figure: as `stable_band_methods.py`.
- ASSUMPTION A (declared, not measured): both essentials baskets (narrow 516-655 h, broad 826-965 h) scale by the same ratio as the median lifestyle.
- Pass rule for "rations": admitted real units <= capacity. Upper edge = highest rho passing it. "none" = passes at every rho up to the grid top 4.0.
- rho_sat = lowest rho at which >= 99.9% of wants are admitted.

## Reasoning, stated so it can be wrong

- Admitted units cannot exceed wants (66,407). Germany/Japan capacity 67,515 is above wants, so the capacity test cannot fail there: no upper edge (model-entailed, brief 4b). France and Sweden capacity is below wants, so an edge can exist. Those are the cells that can fail.
- One-day admitted depends on rho/kappa only. So rho*(peer) = rho*_US-at-that-capacity-share x (ratio).

## Outcomes

| # | Kind | Declaration | It fails if |
|---|---|---|---|
| O1 | Level | Germany/Japan (0.836): every edge, one-day and cumulative, F = 2, 10, 14, is "none" (censored) | any edge is a number |
| O2 | Level | France (0.858) and Sweden (0.873): an edge exists (a number below 4.0) at every F, one-day and cumulative | any is censored |
| O3 | Level | One-day edge at F = 10: France in [0.55, 0.85]; Sweden in [0.40, 0.65] | outside either range |
| O4 | Level | One-day edge at F = 2: France in [1.3, 2.6]; Sweden in [1.0, 2.2] | outside either range |
| O5 | Level | Break-even arithmetic kappa/(365 F) = h/(365 F), 3 decimals; e.g. Sweden F = 10: 0.330, France F = 2: 1.622 | any differs |
| O6 | Level | Band open on the broad basket at F = 10 and 14 for all three peers; at F = 2, open for 0.836 and 0.858 | closed at any of those |
| O7 | Instrument | US control reproduces 1.017 / 0.330 / 0.253 within 0.01 | gap > 0.01 |
| O8 | Relation | Edge rises with capacity share: edge(Sweden) < edge(France) at the same F in rho units per ratio, i.e. edge/ratio is lower for the tighter capacity | order reversed |
| O9 | Level | Cumulative edge within 5% of one-day edge at every cell where both exist | gap > 5% |
