# German-method prime-rate sweep on the specified stock gate

Request `sr-20261109-prime-rate-sweep-at-the-german-method-on-the`. Run 2026-11-11.
Code: `german_prime_sweep.py` (6 self-tests). Raw output: `RESULTS_RAW.txt`. Declared outcomes: `DECLARED.md`.

## 1. The question

> Prime-rate sweep at the German method on the specified gate. Population, wants and age pyramid as stock_gate_clearing.py (N 200,000, seed 7, sigma 0.45). German every-payer ratio 0.836, capacity = 101.7% of wants. Gate: stock, D <= rho*(C+P), P = 0. Essentials never gated: the first E h/yr of each request is ungated, E = 437 to 462 h; report both ends. Services and enrichment off the receiver's D: remove care, schooling, land transport services and post/telecoms from kappa; print kappa before and after. Pasts: joiners rebuilt to birth (4.4), uncapped. Sweep capacity at +20%, +10%, 0, -10%, -20%, -30%, -40%, at F = 2, 10, 14. Per cell: the clearing rho or "none"; share admitting nothing above E; admitted demand by age band; next year's demand at the baseline rho.

## 2. Declared before running (full text in `DECLARED.md`)

| # | Statement | Kind | Result |
|---|---|---|---|
| 1 | At +20% and 0, no clearing rho exists, at every F | level of the cell | **Held** (all 3 F, both E, all 5 age seeds) |
| 2 | A clearing rho appears below some depth and falls as the shock deepens | change | **Held** at -10, -20, -30. It vanishes again at -40 (see 4) |
| 3 | F = 10, -20%: rho in [0.15, 0.35] | level | **Held**: 0.221 (E 437) and 0.217 (E 462) |
| 4 | F = 10, -40%: ungated part alone exceeds capacity, so no rho | level | **Held**: ungated 140,808 units against capacity 135,252 |
| 5 | F = 10, -20%: share admitting nothing above E is under 5% | level | **FAILED**: 26.08% (E 437), 27.87% (E 462) |
| 6 | Year 2 at rho 1.2 admits at least the baseline year | change | **Held, but could not fail**: rho 1.2 is above every edge, so the gate does not bind in either year. Not evidence |

## 3. The numbers

**kappa (debit-hours per person per year for one median lifestyle, German method).** Before services come off: 1,380 x 0.836 = **1,153.7 h/yr** (3.1608 h/day). After: (1,380 - 412) x 0.836 = **809.2 h/yr** (2.2171 h/day). The 412 h are care 253 + schooling 87 + land transport services 59 + post and telecoms 13 (US-method hours, `essentials-basket/RESULTS.md`). Services are 412 / 1,380 = **29.9%** of each request. They are never refused and still count against capacity.

**Population.** F = 10: wants 221,652 units, capacity at 0 shock 225,420 (101.7%). F = 2: 223,868 / 227,674. F = 14: 221,470 / 225,235. Unit = one median German lifestyle-year.

**Clearing rho, primary arm.** Cell values are the mean over 5 age seeds. The spread across age seeds was 0.001 or less in every cell. Format: E = 437.2 h / E = 462.3 h.

| Shock | F = 2 | F = 10 | F = 14 |
|---|---|---|---|
| +20% | none, gate never binds below rho = 4.0 | none (same) | none (same) |
| +10% | none (same) | none (same) | none (same) |
| 0 | none (same) | none (same) | none (same) |
| -10% | 0.866 / 0.853 | 0.309 / 0.307 | 0.237 / 0.236 |
| -20% | 0.511 / 0.493 | 0.221 / 0.217 | 0.172 / 0.169 |
| -30% | 0.323 / 0.304 | 0.158 / 0.151 | 0.125 / 0.120 |
| -40% | none, ungated part alone exceeds capacity | none (same) | none (same) |

**Share of people admitting nothing above E** (among those whose request exceeds E, at the cell's rho). E = 437.2 / 462.3.

| Shock | F = 2 | F = 10 | F = 14 |
|---|---|---|---|
| +20%, +10%, 0 (rho held at 1.2) | 4.99% / 5.14% | 0.00% | 0.00% |
| -10% | 14.45% / 15.50% | 8.51% / 8.95% | 8.04% / 8.45% |
| -20% | 41.61% / 44.18% | 26.08% / 27.87% | 24.75% / 26.39% |
| -30% | 66.25% / 69.81% | 54.17% / 59.71% | 51.89% / 57.04% |

In absolute terms at F = 10, -20%, E = 437: 26.08% of 200,000 is **52,160 people** who receive essentials and services and no discretionary goods that year.

**Admitted units by age band at F = 10, E = 437.2** (units of lifestyle, ages 0-18 / 18-35 / 35-50 / 50-65 / 65-85; share of that band's wants in brackets). The other F values are in `RESULTS_RAW.txt`.

| Shock | 0-18 | 18-35 | 35-50 | 50-65 | 65-85 |
|---|---|---|---|---|---|
| 0 (no clearing rho, rho 1.2) | 48,600 (1.000) | 51,111 (1.000) | 42,207 (1.000) | 41,974 (1.000) | 37,756 (1.000) |
| -10% | 44,964 (0.925) | 46,725 (0.914) | 38,495 (0.912) | 38,293 (0.912) | 34,401 (0.911) |
| -20% | 40,197 (0.827) | 41,493 (0.812) | 34,156 (0.809) | 33,958 (0.809) | 30,532 (0.809) |
| -30% | 35,082 (0.722) | 36,313 (0.710) | 29,915 (0.709) | 29,740 (0.709) | 26,745 (0.708) |

Children (0-18) keep 1-2 points more than every adult band. The five bands are within 0.2 points of each other from age 18 up. Likely cause, not tested: the past debit grows with age, so the 0-18 band has the most room.

**Next year at rho 1.2, capacity restored.** F = 10: **221,648 units (0.983 of full capacity) after every shock depth**, identical to the unshocked year. F = 14: 221,470, identical. F = 2: 215,719 after 0 shock and 215,781 to 215,782 after -10% to -30%, about 0.03% higher. No shock left a mark that rho 1.2 does not erase. This is declared outcome 6, and see its caveat.

**Ungated demand against capacity.** Services plus essentials take 140,808 units at F = 10 (E = 437), which is 63.5% of wants and 104% of the -40% capacity of 135,252. The gate has room to work only while capacity stays above the ungated line. Worked: ungated is 140,808 / 221,652 = 0.635 of wants, capacity is 1.017 x (1 + shock) of wants, so they cross at 1 + shock = 0.625, a shock of about **-37.5%** (E = 437). At E = 462: 144,730 / 221,652 = 0.653, crossing at about **-35.8%**. Computed from the printed figures, not swept at those depths.

## 4. Sensitivities (F = 10 only; full tables in `RESULTS_RAW.txt`)

| Arm | -10% | -20% | -30% | Zero above E at -20% |
|---|---|---|---|---|
| Primary: past = each person's own want x kappa; credit = c x age | 0.309 | 0.221 | 0.158 | 26.08% |
| SENS-1: past = the median person's want x kappa for everyone (stable-band style) | 0.201 | 0.152 | 0.125 | 51.82% |
| SENS-2: past credit = floor only, F x 365 x age (4.4 condition 2, the conservative end) | 0.415 | 0.304 | 0.224 | 23.04% |

The level of rho moves by a factor of 2 across the three readings of "a joiner's past", at the same shock. The direction (none above 0, a rho that falls with depth, none at -40%) does not move.

## 5. What this does not show

1. **It does not show a network can find the clearing rho.** The run reads rho off a capacity figure it was handed. A network that must set rho from observed demand, with a lag, was not simulated.
2. **The upper-end claim ("plenty") is the input, not a finding.** Capacity is set at 101.7% of wants before anyone is simulated, so "no clearing rho at 0 and above" is the arithmetic of that number (Foundations 5.5.3 says the same of the German row). Only the scarcity half carries information.
3. **-40% is "none" for a reason that is not the gate.** Services plus essentials alone exceed capacity there, so the shortage is settled at distribution (5.5.4) and no rho could clear it. "A clearing rho falls as the shock deepens" holds only down to about -36% to -37.5% (section 3).
4. **The shock is spread evenly over all output.** A shock that falls on food or care (PLAN-2026-11-09 section 7) can exceed capacity with essentials alone at a much shallower depth. Not run.
5. **Declared outcome 5 failed and it matters.** At -20% and F = 10, over a quarter of people (52,160 of 200,000) admit nothing above E. This is the specified gate with essentials exempt, so nobody is without food, but the burden falls on one group. Who they are was not broken down beyond age band (person-level credit decile and want size were not tabulated).
6. **Year 2 at rho 1.2 cannot fail.** Rho 1.2 sits above every edge at the German method, so the gate does not bind in either year. A year-2 test at a rho that binds (for instance the shock-year rho kept in place) was not run.
7. **One population draw.** Seed 7 builds wants and credit once. Only the age draw varies (seeds 11-15), so the spreads above (0.001 or less) understate population noise. Credit and want are drawn from the project's synthetic model, not from German data.
8. **Hours basis mismatch.** The 412 service hours are per person of all ages at the US method. kappa (1,380) is per median adult. Subtracting one from the other mixes the two bases (`essentials-basket/RESULTS.md` says so). Care at the covering-everyone level is 144 h, not 253 h; with 144, services are 32% smaller. Not run.
9. **Services are modelled as never refused and as using capacity.** That is a reading of the author ruling (a service moves no debit). If services used no scarce capacity, the -40% result would change.
10. **E is scaled by 0.836 and nobody measured a German basket.**

## 6. Exact command and seed

```
python 06-simulation/german-prime-sweep/german_prime_sweep.py --test
python 06-simulation/german-prime-sweep/german_prime_sweep.py > 06-simulation/german-prime-sweep/RESULTS_RAW.txt
```
Population seed 7 (N = 200,000, sigma 0.45); age seeds 11, 12, 13, 14, 15; baseline rho for year 2 = 1.2. Run time: about 2 minutes.
