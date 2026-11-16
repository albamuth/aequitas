# Children in the cumulative stable band (kappa-tied)

Request `sr-20261031-re-run-stable-band-cumulative-py-kappa-tied-`, run 2026-11-16. Code: `stable_band_children.py` (6 self-tests, each able to fail). Declared outcomes: `CHILDREN_DECLARED.md`.

## 1. The question

> Re-run stable_band_cumulative.py (kappa-tied, kappa = 1,380/365) in two arms at F = 2, 10, 14, beside the published rho*_L 1.017 / 0.330 / 0.253. Arm 1: line 79 past debit = 1,380 x max(0, age - 18) instead of 1,380 x age; nothing else changed. Arm 2: arm 1, plus every person under 18 requests nothing under their own gate, and their wants are added to the adults' requests in equal shares (declared household rule). Report rho*_L, the period that sets it, and whether the F = 2 narrow band (lower edge 0.71-0.90) stays open.

Terms. `F` is the floor in hours a day. ρ is the debit tolerance in the gate `D ≤ ρ·(C + P)`. ρ*_L is the highest ρ at which every one of 100 yearly periods keeps admitted demand at or below capacity `R_max`.

## 2. Outcomes declared before running

| # | Statement | Result |
|---|---|---|
| L1 (level) | Arm 0 reproduces 1.017 / 0.330 / 0.253 within ±0.01 | **Held** |
| L2 (level) | Arm 1 at F = 10 is in 0.15–0.30 | **Held** (0.267) |
| L3 (level) | Arm 1 at F = 2 is in 0.55–0.95, and at F = 14 in 0.12–0.24 | **Failed at F = 2** (1.009). F = 14 held (0.194) |
| D1 | Arm 1 is below arm 0 by more than 0.02 at all three F | **Failed at F = 2** (drop 0.008). Held at 10 and 14 |
| D2 | Arm 2 ≥ arm 1 at all three F | **Held** |
| D3 | Period 1 sets ρ*_L in every arm | **Failed in every arm** (periods 4 to 74) |
| N1 | The F = 2 narrow band closes in arm 1 (ρ*_L < 0.71) | **Failed.** It stays open |

## 3. Numbers

`R_max` = 56,446 real units. People want 66,407 in total (85% capacity). 60,000 people, seed 7. Under-18s are 22.0% of people. Five age seeds (11–15). κ = 3.7808 h per unit per day, so a year of median demand is 1,380 h.

| F | Arm 0 (published) | Arm 1: child debit 0 | Arm 2: arm 1 + household | Period that sets it (arm 0 / 1 / 2) |
|--:|--:|--:|--:|---|
| 2 | **1.017** | **1.009** (−0.008) | **1.196** (sd 0.002; +0.179) | 74 / 40–41 / 17–19 |
| 10 | **0.330** | **0.267** (−0.063, −19%) | **0.277** (−0.053, −16%) | 14–15 / 6–7 / 4 |
| 14 | **0.253** | **0.194** (−0.059, −23%) | **0.199** (−0.054, −21%) | 7 / 6 / 4 |

Spread across the five age seeds is 0.000 in every cell except arm 2 at F = 2 (1.195–1.199).

Absolute figure at the first failing ρ (ρ*_L + 0.0006), for scale. Capacity is 56,446:

| F | Arm 0 | Arm 1 | Arm 2 |
|--:|--:|--:|--:|
| 2 | 56,455 | 56,455 | 56,455 |
| 10 | 56,482 | 56,622 | 56,720 |
| 14 | 56,498 | 56,712 | 56,818 |

**The F = 2 narrow band** (lower edge 0.71–0.90, from `E/(365·F)`): stays open in all three arms. The gap between the upper edge and the top of the lower range is 1.017 − 0.90 = 0.117 h-ratio units in arm 0, 1.009 − 0.90 = 0.109 in arm 1, and 1.196 − 0.90 = 0.296 in arm 2. The broad basket's lower edge (1.13–1.32) is above arm 0 and arm 1 (closed, as published) and **below the arm 2 value of 1.196 only for the lower half of its range** (1.13 to 1.196 open, 1.196 to 1.32 closed). That last line is arithmetic on two ranges, not a re-measured affordability.

## 4. What this does not show

1. **Nobody ages.** Ages are fixed at joining for 100 years. A child under 18 stays a child for the whole run, so arm 2's children never become adults and their requests never move to their own gate. A real network would age them in.
2. **Children still accrue credit in every arm** (floor plus `work_h`), as in the published script. In arm 2 that credit is stranded on accounts that request nothing. Nothing in the run says whether a network should credit it.
3. **The household rule is the request's, not a measurement.** Equal shares across all adults ignores who the guardians are. The extra load per adult is +34.8% on the 6,000-person test population, and refused amounts are lost, not re-offered.
4. **Past credit is still floor only** and past debit is flat at 1,380 for adults, so the F = 2 result inherits the published run's windfall assumption (RESULTS_CUMULATIVE.md).
5. **Capacity (0.85 of wants) and κ are held at one-day values**, with no births, deaths, or property held.
6. **The F = 2 arm 2 result is large (+0.179) and I did not isolate why.** It is probably the load shifting from always-admitted children to adults who are gated at F = 2, but no extra arm tested that.
7. **My declared period outcome was wrong.** I assumed period 1 sets the edge. It does not; the earlier test only showed admitted demand non-increasing at non-binding ρ. I have not investigated the rising path at binding ρ.

## 5. Command and seed

```
python 06-simulation/stable-band/stable_band_children.py --test
python 06-simulation/stable-band/stable_band_children.py --arm 0   # and 1, 2
```
Population seed 7 (`stable_band.RNG_SEED`), age seeds 11–15, M = 100. Raw lines: `CHILDREN_RUN.txt`.
