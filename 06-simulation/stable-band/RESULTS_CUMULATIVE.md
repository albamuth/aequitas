# The upper edge ρ* on a cumulative ledger — result

> **Version:** 0.1
> **Date:** 2026-10-26

> **Run:** `python stable_band_cumulative.py` · **Self-tests:** `python stable_band_cumulative.py --test`, 6 pass
> **Transcript:** [`CUMULATIVE_RUN.txt`](CUMULATIVE_RUN.txt) · **Declared inputs and outcomes:** [`CUMULATIVE_DECLARED.md`](CUMULATIVE_DECLARED.md)
> **Request:** `sr-20261023-re-run-stable-band-py-s-upper-edge-rho-on-a-`

---

## 1. The question

> Re-run stable_band.py's upper edge rho* on a CUMULATIVE ledger: each agent joins with credit and debit rebuilt to birth (floor credit per day lived, cohort consumption 1,380 h/yr at the US method), ages drawn from a declared distribution, all joining on day one, then run M yearly periods. Report rho*_L at F = 2, 10, 14 beside the one-day rho*, and the period at which admitted demand returns to the one-day level. Declare ages, past consumption, joining schedule and M before running.

**Terms.** `F` is the floor, in hours a day. ρ is the debit tolerance in the gate `D ≤ ρ·(C + P)`. ρ\* is the highest ρ at which admitted demand still fits inside the economy's capacity `R_max`. **ρ\*_L** is that edge when every period from 1 to M must fit. **One-day ρ\*** is the published edge from `stable_band.py`.

## 2. Declared before running

Inputs (full list in the script header): same 60,000 people and same fixed calibration as `stable_band.py` (seed 7; κ = 13.797 debit-h per unit, `R_max` = 56,446 units). Ages from a five-band US-like pyramid, mean 39.8 (five age seeds, 11 to 15). Joiner credit `C0 = F × 365 × age` (floor only). Joiner debit `D0 = 1,380 × age`. Everyone joins in period 0. A period is 365 days. **M = 100.**

| # | Kind | Declared | Result |
|---|---|---|---|
| O1 | **Level** | ρ\*_L at F = 10 lies in **[0.30, 0.90]** | **0.416. Held.** |
| O2 | Direction | ρ\*_L is below the one-day edge at F = 2, 10, 14 | **Held** at all three |
| O3 | **Level** | The F = 2 edge falls by more than 1.0 (3.71 down to below 2.71) | **Fell by 1.73. Held.** |
| O4 | Return time | At F = 10, ρ = 1.2, admitted demand does not return to the one-day level within 100 periods | **Held.** It returns at period 150 |
| O5 | Instrument | At age 0 the edge equals the one-day edge, within 0.02 | **Held.** 3.712, 1.206, 0.922, both ways |

Every one of these could have failed: O1 had a band of 0.6 wide and a request that predicted "below 1.20" with size unknown; O4 would have failed if the stored room ran out inside a lifetime.

## 3. The numbers

**Capacity and demand, absolute.** `R_max` = 56,446 real units. People want 66,407 in total.

### 3.1 The edge

| `F` (h/day) | One-day ρ\* | **ρ\*_L (all of periods 1–100)** | Change | ρ\*_L at period 100 alone |
|--:|--:|--:|--:|--:|
| 2 | 3.712 | **1.982** | −1.73 (−47%) | 3.668 |
| 10 | 1.206 | **0.416** | −0.79 (−66%) | 1.155 |
| 14 | 0.922 | **0.299** | −0.62 (−68%) | 0.878 |

**Spread.** Five age seeds give the same ρ\*_L to three decimals at every F (sd 0.000, range under 0.001). The 60,000-person average leaves no room for age-draw noise. **That is a spread across age draws only.** The population seed (7) was not varied, and the result is not claimed to hold across it.

### 3.2 Why period 1 sets ρ\*_L

Admitted demand never rises from one period to the next (self-test 6), so period 1 is the worst case. At F = 10, ρ = 1.2, the people admit 66,318 units in period 1 against `R_max` of 56,446. The gate is not binding for almost anyone. The stored room of a joiner (ρ·F·365 − 1,380) × age is 3,000 h per year of age at these settings.

### 3.3 Return to the one-day level (age seed 11, return = within 1% of the one-day total)

| `F` | ρ | One-day admitted | Period 1 | Period 10 | Period 50 | Period 100 | Period 400 | **Return period** |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 10 | 1.2 | 56,333 | 66,318 | 64,539 | 59,185 | 57,431 | 56,421 | **150** |
| 10 | 1.206 (one-day edge) | 56,446 | 66,319 | 64,571 | 59,297 | 57,545 | 56,532 | **150** |
| 14 | 1.2 | 61,699 | 66,387 | 65,854 | 63,842 | 62,741 | 61,808 | **144** |
| 14 | 0.922 (one-day edge) | 56,440 | 66,328 | 64,728 | 59,639 | 57,706 | 56,552 | **165** |
| 2 | 3.712 (one-day edge) | 56,445 | 66,200 | 62,353 | 57,214 | 56,663 | 56,459 | **60** |
| 2 | 1.2 | 30,201 | 1,272 | 22,691 | 30,201 | 30,201 | 30,201 | **never above** (starts below) |

Within M = 100 the return is not reached at F = 10 or 14. **150 years is a number from the model with no deaths, no births and no new joiners, so it is not a prediction about a society.** The model has no mortality.

### 3.4 Sensitivity of ρ\*_L (age seed 11, M = 100)

| Variation | F = 2 | F = 10 | F = 14 |
|---|--:|--:|--:|
| **Declared** | 1.982 | 0.416 | 0.299 |
| All join at age 0 | 3.712 | 1.206 | 0.922 |
| All join at age 20 | 2.039 | 0.430 | 0.309 |
| All join at age 40 | 1.968 | 0.405 | 0.290 |
| Past work credited to adults | 1.846 | 0.401 | 0.289 |
| Past debit 1,000 h/yr | 1.503 | 0.320 | 0.230 |
| Past debit 2,000 h/yr | 2.782 | 0.575 | 0.413 |
| **Past debit 5,037 h/yr (the model's own yearly flow, κ × 365)** | 3.712 | 1.206 | 0.922 |

**The result depends on one input, and it is the last row.** The windfall exists because the joiner's past debit (1,380 h/yr) is far below the model's yearly demand for a median-wants person (13.797 × 365 = 5,037 h/yr). Make the two equal and ρ\*_L returns exactly to the one-day edge. Age matters little once it is above about 20.

## 4. What this does not show

**1. It does not show that ρ = 1.2 is too high for a real network. It shows the one-day edge is not the cumulative edge, and that the size depends on a unit gap inside the model.** The model's yearly demand for a median-wants person is 5,037 h/yr. The measured US anchor is 1,380 h/yr. They differ by a factor of 3.65. `stable_band.py` calibrates κ to the median *daily credit* (so a median person demands about their daily credit) and never ties it to 1,380. The request asks for a past of 1,380 h/yr beside a flow of 5,037 h/yr, and the gap between those is what produces the windfall. Row 8 of the sensitivity table is the control: close the gap and the effect vanishes. **Which of the two is right for the flow is not decided here and it decides the size.**

**2. The F = 2 row is contaminated by the open defect 2 in README "Known defects".** At F = 2, a joiner has room `(ρ·730 − 1,380) × age`, which is negative for ρ below 1.89. `gate.py` `consume()` was called with `essential=False`, so those accounts are refused in full, essentials included, which Foundations §5.5.4 does not allow. I did not change `stable_band.py` or `gate.py`. The F = 2 number, and the t = 1 figure of 1,272 units at ρ = 1.2, are a lower bound on what a corrected run would admit. At F = 10 and 14 the same thing happens only for ρ below 0.38 and 0.27, and the reported edges (0.416, 0.299) sit just above those thresholds, so they are close to it but not inside it.

**3. It does not show a steady-state economy.** No one dies, is born, or joins after day one. `R_max` and κ are held at their one-day values for 100 years. Stored room that would have gone to the dead stays with the living here. A real network refills with newborns who join with no room, which pushes the edge back up.

**4. The "all join on day one" window is the largest windfall there is.** Foundations §4.4 says joining is a windfall for a median person. A network that grows by joiners over time has this windfall spread out. ρ\*_L here is the day-one edge for a network founded with a whole population present, and no more.

**5. Past credit is floor only, and past debit is flat at 1,380 for everyone.** That is the declared choice, not a measurement. Past work credit (one variant) lowers ρ\*_L by 0.01 to 0.14. Past debit that differs by person was not run.

**6. Spread is across age draws only.** Population seed 7 is fixed, as are `CAP` = 0.85 and the lognormal spread of wants, both marked illustrative in `rho_sweep.py`.

## 5. Command and seed

```
python stable_band_cumulative.py --test
python stable_band_cumulative.py > CUMULATIVE_RUN.txt
```

Population seed 7 (`stable_band.RNG_SEED`), N = 60,000. Age seeds 11, 12, 13, 14, 15. Runs in under two minutes on the author's machine. No files other than the transcript are written.
