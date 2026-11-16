# German-method prime-rate sweep, arm 2: demand at Germany's middle fifth

Request `sr-20261110-second-arm-of-sr-20261109-prime-rate-sweep-a`. Run 2026-11-12.
Code: `german_arm2.py` (6 self-tests, imports arm 1's `german_prime_sweep.py`). Raw output: `RESULTS_ARM2_RAW.txt`. Declared outcomes: `DECLARED_ARM2.md`. Arm 1's file is `RESULTS.md`.

## 1. The question

> Second arm of sr-20261109-prime-rate-sweep-at-the-german-method-on-the, with demand set to Germany's own middle fifth. Same population, gate, essentials rule, service rule, joiner pasts, capacity steps and floors as that request. Change two inputs only. (1) Demand level: Germany's middle fifth of households, 1,048 h per person per year, every payer, EXIOBASE 2022 (MIDDLE_FIFTH.md), with care, schooling, land transport services and post/telecoms hours removed before building D; print kappa before and after. Note the basis: per person, all ages, not per median adult. (2) Output basis: baseline capacity = 100% of that demand, declared, because it is the lifestyle Germany's economy actually delivered; sweep +20% to -40% from it. Report the same cells as the first arm, and print each clearing rho beside the first arm's at the same F and step, with their ratio.

## 2. Declared before running (full text in `DECLARED_ARM2.md`)

| # | Statement | Kind | Result |
|---|---|---|---|
| 1 | Arm 1 reproduced inside the new code: rho 0.221 +/- 0.005 at F=10, -20%, E=437.2 | level | **Held**: 0.2205 |
| 2 | No clearing rho at +20%, +10%, 0, any F | level of the cell | **Held.** Set by the input (capacity = demand), not a finding |
| 3 | F=10, -20%, E=437.2: arm-2 rho in [0.10, 0.30] | level | **Held**: 0.170 |
| 4 | Same cell: ratio arm2/arm1 in [0.55, 0.95] | level on the ratio | **Held**: 0.771 |
| 5 | Ratio below the pure-scaling value 0.87 at F=10, -10% and -20% | change | **Held**: 0.791 and 0.771 |
| 6 | F=10, E=437.2, -30%: "none, ungated part alone exceeds capacity" | level of the cell | **FAILED**: rho 0.089. The ungated part is 0.992 of capacity, so the cell clears by a 0.8% margin (see 3) |
| 7 | F=10, -20%, E=437.2: share admitting nothing above E above arm 1's 26.08% | change | **Held**: 38.01% |
| 8 | Year 2 at rho 1.2 within 1% of the unshocked baseline year | change | **Held, mostly cannot fail.** At F=10 and F=14 rho 1.2 does not bind in either year (221,652 = 221,652). At F=2 it binds slightly: 219,178 against 218,738 (+0.2%) |

## 3. The numbers

**kappa (debit-hours per person per year for one unit of lifestyle).**

| | Arm 1 (US anchor x 0.836) | Arm 2 (Germany's middle fifth) |
|---|--:|--:|
| Before services come off | 1,380 x 0.836 = **1,153.7 h/yr** (3.1608 h/day) | **1,048.0 h/yr** (2.8712 h/day) |
| Services removed | 412 x 0.836 = 344.4 h | 344.4 h (same) |
| After | **809.2 h/yr** (2.2171 h/day) | **703.6 h/yr** (1.9276 h/day) |
| Services as share of a request, s | 0.2986 | 0.3287 |
| Capacity base against wants | 101.7% | 100.0% |

Basis: 1,048 h is per person, all ages, every payer (households, non-profits, government care and schooling), EXIOBASE 2022. Arm 1's 1,380 h is per median adult. Both are applied to each person's want w the same way, so a "unit" is one middle-fifth German lifestyle-year in arm 2 and one median German lifestyle-year in arm 1. The 344.4 h is arm 1's own service hours (US method) times 0.836. No German per-service hours exist in the project tables.

**Population.** Same draw as arm 1. Wants: F=10 221,652 units; F=2 223,868; F=14 221,470. Arm-2 capacity at 0 shock equals wants, so at -20% it is 177,322 units at F=10 (arm 1: 225,420 x 0.8 = 180,336).

**Clearing rho, arm 1 | arm 2 | ratio.** Mean of 5 age seeds. Format: E = 437.2 h / E = 462.3 h. "none-U" = none, ungated part alone exceeds capacity. +20%, +10%, 0 are "none, gate never binds below rho = 4.0" in both arms at every F, and -40% is none-U in both arms at every F.

| F | Shock | Arm 1 | Arm 2 | Ratio arm2/arm1 |
|--:|--:|---|---|---|
| 2 | -10% | 0.866 / 0.853 | 0.635 / 0.617 | 0.733 / 0.723 |
| 2 | -20% | 0.511 / 0.493 | 0.361 / 0.343 | 0.707 / 0.696 |
| 2 | -30% | 0.323 / 0.304 | 0.176 / none-U | 0.545 / n.a. |
| 10 | -10% | 0.309 / 0.307 | 0.244 / 0.242 | 0.791 / 0.788 |
| 10 | -20% | 0.221 / 0.217 | **0.170 / 0.165** | **0.771 / 0.761** |
| 10 | -30% | 0.158 / 0.151 | 0.089 / none-U | 0.563 / n.a. |
| 14 | -10% | 0.237 / 0.236 | 0.189 / 0.187 | 0.794 / 0.792 |
| 14 | -20% | 0.172 / 0.169 | 0.134 / 0.130 | 0.778 / 0.769 |
| 14 | -30% | 0.125 / 0.120 | 0.073 / none-U | 0.584 / n.a. |

Spread across the 5 age seeds: not printed per cell by this script (the means are what is shown). Arm 1 reported 0.001 or less. The population draw is one (seed 7), so population noise is not in either arm's spread.

**Why the ratio is 0.77 and not 0.87.** Pure scaling gives 703.6 / 809.2 = 0.8694. Self-test 3 confirms it exactly when E = 0 and s = 0 (ratio 0.8694). The remaining gap at -10% and -20% comes from two inputs that did not scale: E is the same 437 or 462 h against a request that is now 13% smaller, so essentials are a larger part of it; and capacity is 1.000 of wants, not 1.017, so "-20%" is 1.7 points deeper against demand. The ratio falls to 0.55 to 0.58 at -30% because the ungated part is then 0.992 of capacity.

**Ungated demand against capacity.** Services plus essentials take, at F=10 and E=437.2: arm 1 0.635 of wants, arm 2 0.694. At E=462.3: 0.653 and 0.712. Arm 2 crosses capacity at a shock of **-30.6%** (E=437.2) and **-28.8%** (E=462.3). Arm 1 crossed at -37.5% and -35.8%. Computed from the F=10, age-seed-11 cell. So the range of shocks over which a clearing rho exists shrank from about 0 to -37% in arm 1 to about 0 to -30% in arm 2.

**Share of people admitting nothing above E** (of those whose request exceeds E). Arm 2 (arm 1), E = 437.2 / 462.3.

| F | -10% | -20% | -30% |
|--:|---|---|---|
| 2 | 23.89% / 26.46% (14.45% / 15.50%) | 54.02% / 56.78% (41.61% / 44.18%) | 89.95% / n.a. (66.25% / 69.81%) |
| 10 | 13.13% / 14.15% (8.51% / 8.95%) | 38.01% / 42.16% (26.08% / 27.87%) | 90.95% / n.a. (54.17% / 59.71%) |
| 14 | 12.38% / 13.30% (8.04% / 8.45%) | 35.94% / 39.72% (24.75% / 26.39%) | 90.31% / n.a. (51.89% / 57.04%) |

At +20%, +10%, 0: F=10 and 14 are 0.00% in both arms. F=2 is 3.04% / 3.16% (arm 1: 4.99% / 5.14%).

In absolute terms at F=10, -20%, E=437.2: 38.01% of 200,000 is **76,020 people** who receive essentials and services and no discretionary goods that year (arm 1: 52,160). The -30% figure of 90.95% sits 0.8% under the ungated line, so almost everyone is at the edge of the essentials-only state (see limit 4).

**Admitted units by age band, F=10, E=437.2** (ages 0-18 / 18-35 / 35-50 / 50-65 / 65-85; share of band wants). The script prints band lines for this cell only (F=10, E=437.2); other F values were not tabulated.

| Shock | 0-18 | 18-35 | 35-50 | 50-65 | 65-85 |
|---|---|---|---|---|---|
| 0 (rho 1.2) | 48,600 (1.000) | 51,112 (1.000) | 42,208 (1.000) | 41,975 (1.000) | 37,757 (1.000) |
| -10% | 44,217 (0.910) | 45,948 (0.899) | 37,839 (0.896) | 37,645 (0.897) | 33,837 (0.896) |
| -20% | 39,370 (0.810) | 40,819 (0.799) | 33,641 (0.797) | 33,432 (0.796) | 30,060 (0.796) |
| -30% | 34,098 (0.702) | 35,768 (0.700) | 29,514 (0.699) | 29,375 (0.699) | 26,402 (0.699) |

Children keep about 1 point more than adults at -10% and -20%, and 0.2 points at -30%. Arm 1's gap was 1 to 2 points. Cause not tested.

**Next year at rho 1.2, capacity restored.** F=10: 221,652 units (1.000 of full capacity) after every shock depth, equal to the unshocked year. F=14: 221,470, same. F=2: 219,138 after +20% to 0 and 219,178 to 219,277 after -10% to -30%, against an unshocked 218,738 (E=437.2). The gate does not bind at rho 1.2 for F=10 and F=14, so no shock left a mark. At F=2 the gate binds slightly and the year after a shock admits 0.2% more.

## 4. What this does not show

1. **The 100% capacity base is declared, not measured.** It says the 1,048 h lifestyle is exactly what the economy delivered. "No clearing rho at 0 and above" is the arithmetic of that choice. Only the scarcity rows carry information, as in arm 1.
2. **Arm 2's lower rho is mostly arithmetic, not a new finding about Germany.** A smaller request needs a smaller rho (ratio 0.87 by scaling, confirmed by self-test 3). The extra 0.1 of ratio (0.77 instead of 0.87) comes from E staying fixed and capacity being 1.7% lower, both inputs. If E were scaled with the demand level, the ratio would sit nearer 0.87.
3. **The 344.4 service hours are the arm-1 US-method figure times 0.836, not German middle-fifth service hours.** Nobody measured German care, schooling, land transport or post/telecoms hours for the middle fifth. The 1,048 h is per person, all ages, and arm 1's 412 h was also per person at the US method, so the two bases agree on that point only. With care at the covering-everyone level (144 h, not 253 h) services would be about 32% smaller (arm 1 limit 8). Not run.
4. **The -30% cells are fragile.** At F=10, E=437.2 the ungated part is 0.992 of capacity, so a 0.8% change in any input flips the cell from "rho 0.089" to "none". The failed outcome 6 is that fragility, not a model fault. The rho values at -30% (0.089, 0.176, 0.073) are readings next to a cliff and should not be quoted as levels.
5. **E was not rebuilt for a German middle-fifth basket.** It is arm 1's US broad basket times 0.836. Against a 703.6 h request, 437 to 462 h is 62% to 66% of it.
6. **One population draw and one capacity shape.** Wants and credit come from the project's synthetic model (seed 7). Only the age draw varies. The shock is spread evenly over all output. A shock that falls on food or care would hit the ungated line at a shallower depth.
7. **It does not show a network can find the clearing rho.** The run reads rho off a capacity figure it was handed.
8. **Year 2 at rho 1.2 is not a test at F=10 and F=14.** The gate does not bind there.
9. **Both arms are rationing figures at one rate for everyone.** Who the 76,020 people are, beyond age band, was not broken down.

## 5. Exact command and seed

```
python 06-simulation/german-prime-sweep/german_arm2.py --test
python 06-simulation/german-prime-sweep/german_arm2.py --raw
```
`--raw` writes `RESULTS_ARM2_RAW.txt` next to the script. Population seed 7 (N = 200,000, sigma 0.45); age seeds 11, 12, 13, 14, 15; baseline rho for year 2 = 1.2. Run time: a few minutes, including arm 1's re-run.
