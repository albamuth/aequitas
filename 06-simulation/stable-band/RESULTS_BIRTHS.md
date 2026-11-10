# The births arm of the cumulative upper edge ρ\* — result

> **Version:** 0.1
> **Date:** 2026-11-08

> **Run:** `python stable_band_births.py` · **Self-tests:** `python stable_band_births.py --test`, 8 pass
> **Transcript:** [`BIRTHS_RUN.txt`](BIRTHS_RUN.txt) · **Tests:** [`BIRTHS_TEST.txt`](BIRTHS_TEST.txt) · **Declared first:** [`BIRTHS_DECLARED.md`](BIRTHS_DECLARED.md)
> **Request:** `sr-20261102-births-arm-of-stable-band-cumulative-py-kapp`

---

## 1. The question

> Births arm of stable_band_cumulative.py (kappa-tied, US method, F = 2, 10, 14). Add births and deaths over the 100 years; the runner DECLARES the birth rate and the death schedule and prints both. Children follow Pledges.md ruling 7: no debit, floor credit from birth, no requests below the consent age (runner declares it). Report rho* with and without births at each F, and the change, as three separate columns. Declared before running: cell 1, rho*(births) < rho*(fixed) at every F; cell 2, it is >= at some F; cell 3 (level), rho*(births) at F = 2 is below 0.90, the top of the narrow-basket lower edge.

**Terms.** `F` is the floor, in hours a day. ρ is the debit tolerance in the gate `D ≤ ρ·(C + P)`. ρ\* is the highest ρ at which admitted demand still fits inside capacity in every one of 100 yearly periods. The **consent age** is the age below which a person makes no requests.

## 2. Declared before running

**Inputs, printed by the runner.** Death schedule (chance of dying in a year, by age): 0–18 0.0004 · 18–35 0.0010 · 35–50 0.0025 · 50–65 0.0080 · 65–85 0.0350 · 85–100 0.1500 · all die at 100. This gives a life expectancy at birth of **76.5 years**. Birth rate **0.012** per living person per year. Consent age **18**. Both the schedule and the rate are illustrative, not sourced. Starting people, wants, κ = 1,380 ÷ 365 and starting capacity 56,446 units are those of `stable_band_kappa.py`.

| # | Kind | Declared | Result |
|---|---|---|---|
| **O0** | **Level, instrument** | Arm A reproduces 1.017 / 0.330 / 0.253 within 0.01 | **Held.** 1.017 / 0.330 / 0.253 |
| **O1** | Direction (cell 1) | ρ\*(births) < ρ\*(fixed) at every F | **Held** at all three |
| **O2** | Direction (cell 2) | ρ\*(births) ≥ ρ\*(fixed) at some F | **Did not hold** |
| **O3** | **Level (cell 3)** | ρ\*(births) at F = 2 is below 0.90 | **Held.** 0.866 |
| **O4** | **Level** | ρ\*(births) at F = 10 lies in [0.15, 0.33) | **Held.** 0.262 |

O1 and O2 exclude each other, so one of them had to fail. O3 and O4 could each have failed: the fixed-population control at F = 2 sits at 0.994, which is above 0.90.

## 3. The numbers

**Absolute figures.** Capacity at the start is 56,446 real units for 60,000 people. Their wants total 66,407 units. In the births arm, capacity each year is 0.85 × the wants of the people who request that year (44,005 units in year 1, 37,485 in year 100).

**Demography actually drawn (age seed 11).** Realised crude death rate 0.0136, crude birth rate 0.0120. Population 60,000 in year 1, 59,050 in year 25, 56,178 in year 50, 51,015 in year 100. In 100 years: 67,242 births, 76,335 deaths. **The population shrinks by 15%: the declared birth rate is a little below replacement for this age pyramid.**

### 3.1 The three columns asked for

| `F` (h/day) | ρ\* **without births** (A) | ρ\* **with births** (B) | **Change, B − A** |
|--:|--:|--:|--:|
| 2 | 1.017 (sd 0.000) | 0.866 (sd 0.004) | **−0.152** (−15%) |
| 10 | 0.330 (sd 0.000) | 0.262 (sd 0.000) | **−0.068** (−21%) |
| 14 | 0.253 (sd 0.000) | 0.192 (sd 0.000) | **−0.061** (−24%) |

Spread: five age seeds, each with its own birth and death draw. Per-seed B at F = 2: 0.867, 0.863, 0.864, 0.862, 0.872.

### 3.2 Where the change comes from

Arm A is the published model. **A change in B − A mixes two things**, so two controls separate them.

| `F` | A: fixed, published children | **C: fixed, ruling 7 children** | D: births, published children | B: births, ruling 7 |
|--:|--:|--:|--:|--:|
| 2 | 1.017 | 0.994 | 1.017 | 0.866 |
| 10 | 0.330 | 0.266 | 0.330 | 0.262 |
| 14 | 0.253 | 0.194 | 0.252 | 0.192 |

| `F` | Ruling 7 alone, C − A | Births and deaths alone, D − A | Births and deaths with ruling 7 held, B − C |
|--:|--:|--:|--:|
| 2 | −0.023 | +0.000 | **−0.128** |
| 10 | **−0.064** | −0.000 | −0.004 |
| 14 | **−0.059** | −0.001 | −0.002 |

**In plain words.** Births and deaths with the published children change nothing (D − A is zero to three decimals), because a joiner's past debit then equals the yearly flow and nobody holds extra room. **What moves ρ\* at F = 10 and 14 is ruling 7: a person who is a child carries no debit, so at 18 they hold 18 years of floor credit and no debit.** At F = 10 that is 65,700 h of credit and 0 h of debit, against 65,700 h and 24,840 h in the published model. **At F = 2 ruling 7 alone moves little (−0.023), and births matter (−0.128):** the year-by-year stream of new 18-year-olds, each with stored room, is what sets the edge in a long run.

### 3.3 Which year sets the edge (age seed 11)

| `F` | Arm | ρ at its edge | Year where admitted ÷ capacity peaks |
|--:|---|--:|--:|
| 2 | B | 0.867 | 79 |
| 2 | C | 0.994 | 37 |
| 10 | B | 0.262 | 9 |
| 10 | C | 0.266 | 9 |
| 14 | B | 0.192 | 8 |
| 14 | C | 0.193 | 7 |

At F = 10 and 14 the edge is set within 10 years by the starting cohort of children coming of age, so births have no time to act. At F = 2 the peak is in year 79, so the long run decides it.

### 3.4 Sensitivities (age seed 11, arm B)

| Variation | F = 2 | F = 10 | F = 14 |
|---|--:|--:|--:|
| **Declared** (birth rate 0.012) | 0.866 | 0.262 | 0.192 |
| Birth rate 0.008 (population 24,406 in year 100) | 0.893 | 0.262 | 0.192 |
| Birth rate 0.016 (population 96,893 in year 100) | 0.845 | 0.262 | 0.191 |
| Past debit 1,000 h/yr | 0.867 | 0.203 | 0.146 |
| Past debit 2,000 h/yr | 0.867 | 0.271 | 0.206 |
| Capacity fixed at 56,446 | **excluded, entailed** | | |
| Capacity 0.85 × wants of everybody alive | **excluded, entailed** | | |

**The last two rows are excluded, not run.** With ruling 7 children make no requests, so the most the adults ever want is **52,467 units**, below 56,446. Rationing cannot fail under a fixed capacity at the starting value, whatever ρ is. The runner prints this check. This is the entailed fault of the brief (§4c): the verdict is set by the input, so the check is dropped rather than restated.

## 4. What this does not show

1. **It does not show what children's consumption does to the gate.** Ruling 7 puts a child's food, clothing and housing on the guardians (`Pledges.md` §13.1: about 552 h a year per child). This run does not move that debit to anyone. It vanishes from the books. That lowers every debit total, and so lowers ρ\*. Part of the −0.06 at F = 10 and 14 is that omission. The size is not measured here.
2. **Capacity is a declared convention, and the result depends on it.** Capacity is 0.85 × the wants of the people who request. Fixed or all-people capacity would make rationing impossible to fail (§3.4), so the only convention left that can fail is the one that scales capacity with the number of requesters. Whether an economy with fewer adult requesters really has proportionally less capacity is not shown.
3. **The population shrinks 15%, and the death schedule and the birth rate are illustrative.** The schedule is not a sourced life table. The rate is not a measured fertility. At F = 2 the answer moves from 0.893 to 0.845 across birth rates 0.008 to 0.016, so it is not flat in the rate. At F = 10 and 14 it does not move.
4. **Everyone still joins on day one with a rebuilt past, and the past is flat.** Past credit is floor only and past debit is 1,380 h a year for everyone from the consent age. The F = 10 and 14 edges move with that past debit (0.203 to 0.271 at F = 10); the F = 2 edge does not.
5. **The F = 2 rows carry the open defect in the README's "Known defects".** At F = 2 some accounts have negative room and the kernel refuses them in full, essentials included, which Foundations §5.5.4 does not allow. The F = 2 figures are a lower bound on what a corrected run would admit, so ρ\* there may be understated.
6. **Dead people take their stored room with them and nothing is inherited.** That matches Foundations §4.8 for credit. Their debit leaves the gate too. Neither is varied.
7. **Spread is across five age and demography draws only.** The population seed (7), the lognormal wants and CAP = 0.85 are fixed and marked illustrative.
8. **Nobody who is born works as a child, and new adults draw work and wants independently of their parents.** No households, no families, no migration.

## 5. Command and seed

```
python stable_band_births.py --test
python stable_band_births.py > BIRTHS_RUN.txt
```

Population seed 7 (`stable_band.RNG_SEED`), N = 60,000. Age seeds 11 to 15. Demography seed = age seed + 100. Newborn pool seed = demography seed + 1000. About 2 minutes on the author's machine. Python 3, numpy. Writes only the two transcripts.
