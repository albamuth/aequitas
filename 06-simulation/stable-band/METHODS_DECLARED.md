# Declared before the run (2026-10-29) — request sr-20261028-re-run-stable-band-kappa-py-at-the-german-ja

Written before `stable_band_methods.py` was run in full.

## Inputs declared

| Input | German/Japanese | Spanish | US (control) |
|---|---|---|---|
| Yearly demand of the median person (kappa x 365) | **883 h/yr** | **759 h/yr** | 1,380 h/yr |
| kappa (debit-h per lifestyle-unit per day) | 883/365 = 2.4192 | 759/365 = 2.0795 | 3.7808 |
| Capacity R_max, real units (given in the request) | **88,196** | **102,629** | 56,446 (0.85 x wants) |
| Total wants | 66,407 | 66,407 | 66,407 |
| Past debit of a joiner (cumulative arm) | 883 h/yr | 759 h/yr | 1,380 h/yr |
| Break-even rho, (883 or 759)/(365 F) | per F | per F | 3.78/F |

- Population, ages, joining, M = 100, past credit (floor only): exactly as `stable_band_kappa.py` (60,000 people, seed 7, age seeds 11-15).
- **ASSUMPTION A (declared, not measured):** the essentials baskets scale by the method ratio. Narrow 516-655 h x 883/1,380 = 330-419 h (German) and x 759/1,380 = 284-360 h (Spanish). Broad 826-965 h x 0.6399 = 529-617 h (German) and x 0.55 = 454-531 h (Spanish). This treats the ratio for the whole median lifestyle as the ratio for the essentials share. Nobody measured the essentials basket under the German or Spanish method.
- Pass rule for "rations", as in the earlier runs: admitted real units <= R_max.
- Lower edge = E / (365 F). Band open on a basket iff the lower edge (using the **top** of the basket range, the hard case) is below the upper edge. Where there is no upper edge the band is open whenever the lower edge is a finite, reachable rho.

## Reasoning, stated so it can be wrong

- Total wants (66,407) is below capacity (88,196 and 102,629). Admitted units can never exceed wants. So "admitted <= R_max" is true at every rho. **The capacity test cannot fail. The upper edge does not exist** (bisection will end at the grid top, 4.0, flagged "censored"). Under the rule in the brief 4b this is a model-entailed result about the *edge*. It is reported as "no upper edge", not as a number.
- What can still be measured is where the gate stops binding on people: `rho_sat` = lowest rho at which at least 99.9% of the wants are admitted (one-day). That could fail (it could be above 4.0 or below the lower edge).
- One-day admitted depends on rho / kappa only. So rho_sat(method) = rho_sat(US kappa) x kappa_method / kappa_US. With kappa_US-edge values 1.017 / 0.330 / 0.253 for rho at admitted = 56,446, rho_sat for the full wants is larger than those; the scaling factor is 0.640 (German) and 0.550 (Spanish).

## Outcomes

| # | Kind | Declaration | It fails if |
|---|---|---|---|
| O1 | **Level** | Capacity never binds: at rho = 4.0, admitted real units at every F in {2, 10, 14} is **<= 66,407 (= total wants)** and so < both capacities, and the edge comes back flagged "censored" for both methods, one-day and cumulative | any edge comes back as a number below the grid top, or admitted > R_max |
| O2 | **Level** | German broad-basket lower edge at F = 2 lies in **[0.72, 0.85]** (Foundations inference: 529-618 h / 730) and the narrow one in **[0.45, 0.58]** | outside either range |
| O3 | **Level** | Spanish broad-basket lower edge at F = 2 lies in **[0.62, 0.73]** | outside |
| O4 | **Level** | At F = 2 the band is **open on both baskets, both methods** (no upper edge, lower edge < 1) | closed on any |
| O5 | **Level** | Break-even rho 883/(365 F) = 1.209 / 0.2419 / 0.1728 at F = 2 / 10 / 14 (German); 759/(365 F) = 1.040 / 0.2079 / 0.1485 (Spanish). Arithmetic check, to 3 decimals | any differs |
| O6 | **Level** | The gate-stops-binding rho_sat at F = 10 lies in **[0.25, 0.60]** (German) and **[0.20, 0.55]** (Spanish) | outside |
| O7 | Instrument | Control: the US row at kappa 1,380 reproduces the published one-day edges 1.017 / 0.330 / 0.253 within 0.01 | any gap > 0.01 |
| O8 | Relation | Cumulative rho_sat is within 5% of one-day rho_sat at all F (past debit = flow, as in RESULTS_KAPPA) | any gap > 5% |
