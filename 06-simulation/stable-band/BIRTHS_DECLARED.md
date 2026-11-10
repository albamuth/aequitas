# Births arm of stable_band_cumulative.py — declared before running

> **Date:** 2026-11-08 · **Request:** `sr-20261102-births-arm-of-stable-band-cumulative-py-kapp`
> **Written before the first run of `stable_band_births.py`.**

## Inputs (all declared, all printed by the runner)

| Input | Value |
|---|---|
| Starting population, wants, work, capacity | Same as `stable_band_kappa.py`: 60,000 people, seed 7, κ = 1,380 ÷ 365 (US method), `R_max` = 0.85 × Σ wants = 56,446 |
| Starting ages | Same 5-band pyramid, age seeds 11–15 |
| Joiner past | Credit `F × 365 × age`. Debit `1,380 × age`, or `1,380 × (age − consent age)` in the ruling 7 arms |
| Period | 1 year, 100 periods |
| **Death schedule** (chance of dying in a year, by age at start of year) | 0–18: 0.0004 · 18–35: 0.0010 · 35–50: 0.0025 · 50–65: 0.0080 · 65–85: 0.0350 · 85–100: 0.1500 · everyone dies at 100. Illustrative bands, not a sourced life table |
| **Birth rate** | 0.012 births per living person per year (12 per 1,000). Illustrative. Sensitivity: 0.008 and 0.016 |
| **Consent age** | 18 |
| Children (ruling 7, `Pledges.md` §13.1) | Credit at the floor `F` from birth. No debit. No requests below the consent age. Their material use is **not** put on the guardians in the primary arm |
| New adults | Draw work and wants from the same distribution as the starting people |
| Capacity | Primary: `R_t` = 0.85 × Σ wants of the people who request in period `t`. Sensitivity: fixed 56,446, and 0.85 × Σ wants of everybody alive |
| Rationing | A period rations when admitted real units ≤ `R_t`. ρ\* = highest ρ at which all 100 periods ration |

## Arms

| Arm | Births and deaths | Children |
|---|---|---|
| **A. fixed** (the published model) | No | Request and carry debit as before |
| **B. births** (the arm asked for) | Yes | Ruling 7 |
| C. control: fixed + ruling 7 | No | Ruling 7 |
| D. control: births, children as in the published model | Yes | Request and carry debit |

C and D split the change in B into a ruling 7 part and a population-turnover part.

## Outcomes declared

| # | Kind | Statement | What would fail it |
|---|---|---|---|
| **O0** | **Level, instrument** | Arm A reproduces the published ρ\*: 1.017 / 0.330 / 0.253 at F = 2 / 10 / 14, within 0.01 | Any larger gap means the new code is not the old model |
| **O1** | Direction (cell 1) | ρ\*(B) < ρ\*(A) at every F | Any F where B ≥ A |
| **O2** | Direction (cell 2) | ρ\*(B) ≥ ρ\*(A) at some F | Cell 1 holding at all three F |
| **O3** | **Level (cell 3)** | ρ\*(B) at F = 2 is below **0.90** | ρ\*(B) at F = 2 of 0.90 or more |
| **O4** | **Level** | At F = 10, ρ\*(B) lies in **[0.15, 0.33)**: below the fixed edge and above half of it | A value outside that range |

O1 and O2 cannot both hold. I expect O1: a child arrives at 18 with 18 years of floor credit and no debit, which is more stored room than the fixed model's 18-year-old holds (that one has 24,840 h of debit), and every year brings a new cohort of them. I expect the F = 2 drop to be the largest in size, and O3 to hold. I have no declared expectation for how much of the drop is ruling 7 and how much is turnover.
