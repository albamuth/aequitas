# Declared before running — rho-rubric

> **Date:** 2026-10-15. Written before the first run. `rho_rubric.py` prints this file's SHA-256 prefix at the top of every run.

**Request:** `sr-20260901-score-claim-2-of-disparity-ceiling-sim-py-th`. Score the clearing rate ρ\* on sensitivity, specificity and coverage.

## The model under test

Claim 2 of `06-simulation/disparity-ceiling/disparity_ceiling_sim.py`, unchanged: credit rate `c` from `draw_population`, appetite `a = max(0.1, c · LogNormal(ln 1.6, 0.5))`, capacity `K = 1.15 · Σc`, and ρ\* the ρ where `Σ min(a, ρ·c) = K`. N = 200,000, F = 10, 30 seeds.

## Rules fixed in advance

- **Paired.** The faulted arm re-uses the clean arm's seed. The fault draws from its own stream (seed + 10,000,000), so the base population is identical in both arms.
- **Noise bar.** σ of the 30 paired differences. A challenge **fires** if |mean move| ≥ 2 × that σ.
- **Solver.** ρ\* is solved exactly (sorted thresholds), not on the file's 200-point grid. The grid version is reported beside it.

## Outcomes, each stated before the run

| # | Statement | Kind |
|---|---|---|
| **L1** | Clean ρ\* lies in **[1.10, 1.30]**, reproducing the published ≈ 1.2 | **Level** |
| **L2** | S1 (capacity −30%) lands in **[0.60, 0.76]**, reproducing the published ≈ 0.68. If it lands outside, the published 0.68 does not come from this file | **Level** |
| **L3** | S3 (every appetite +25%) lands in **[0.90, 1.10]**, reproducing the published ≈ 1.0 | **Level** |
| **L4** | Clean-arm paired-difference σ for S1 is **below 0.01**, so a move of 0.05 is ten times the noise | **Level (size of the noise)** |
| **D1** | S1, S2, S3 fire in the expected direction (S1 down, S2 up, S3 down) | Change |
| **D2** | **S4 (20,000 fabricated floor accounts with typical appetite) does NOT fire.** Reason I expect: `a = c · r`, so demand is `Σ c · min(r, ρ)` and `K` is `1.15 Σc`. Any inserted account whose `r` is typical changes both sides in the same proportion | Change |
| **D3** | S5 (omit 20% of real consumption from the books) **fires, upward**, and the same ρ\* can be reproduced by a pure capacity rise, so ρ\* cannot tell under-recording from real spare capacity | Change |
| **D4** | S6a (shuffle appetite between accounts, total fixed) **moves ρ\***, against the brief's expected 0.00, because `min(a, ρc)` is not linear in `a` | Change |
| **D5** | Leg 2 controls (reorder accounts, rescale units) move ρ\* by less than 1e-9 | Change |

## What would change my mind

- D2 false (S4 fires): ρ\* sees fabricated accounts, which is a finding for the brief's prior.
- L2 false: the 0.68 in Foundations §5.5.7 was not produced by this model; the fold needs a source.
- D3 false (S5 does not fire): ρ\* cannot see under-recording at all.

## Leg 3

Unavailable on a generator. Not scored.
