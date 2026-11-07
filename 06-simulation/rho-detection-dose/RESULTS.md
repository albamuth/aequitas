# Detection-dose curve for ρ\* — results

> **Version:** 0.1
> **Date:** 2026-11-06
> **Status:** run. 8 self-tests pass. Raw output: [`RUN.txt`](RUN.txt). Declared first: [`DECLARED.md`](DECLARED.md) (sha256 prefix `18bb535a718d3592`).

## 1. The question

> *"Produce a detection-dose curve for rho*: for each of three declared debit dispersions, report the smallest number of fabricated floor accounts at which the PAIRED move in rho* clears k paired standard deviations, with k fixed before running and seeds paired between clean and faulted arms. Population N = 200,000. Report the curve, not a verdict."*

## 2. Outcomes declared before running

Full text in [`DECLARED.md`](DECLARED.md). Fixed: **k = 2**, σ (spread of ln appetite per credit-hour) = **0.25, 0.50, 1.00**, 30 seeds per block, two blocks (seeds 1–30 and 101–130), F = 10, N = 200,000. The request does not say what appetite a fabricated account has, so three arms were declared: **P** zero recorded appetite, **T** typical appetite, both with capacity tied to recorded credit, and **Q** typical appetite with capacity held at the true physical value.

| # | Declared | Result |
|---|---|---|
| L1 | Clean ρ\* at σ = 0.50 in [1.10, 1.30] | **Held.** 1.2472 (block A), 1.2470 (B) |
| L2 | Clean ρ\* at σ = 0.25 in [1.15, 1.45]; at σ = 1.00 in [1.30, 1.70] | **Held.** 1.1626 and 1.4674 |
| L3 | Arm P, σ = 0.50, move at 10,000 accounts in [+0.03, +0.10] | **Held.** +0.0602 |
| L4 | Arm P, σ = 0.50, dose clearing the unpaired bar in [500, 6,000] | **Failed.** 300 (interpolated 250 in block A, 280 in block B). The level was about half the declared lower end |
| D1 | Arm T never clears the paired bar, any σ, either block | **Held.** Highest ratio 1.91 (σ = 0.25, block B, dose 1, one account, a single-seed fluke beside ratios of 0.0–0.3 at every other dose) |
| D2 | Paired ratio flat in dose for arms P and Q (within 3× between 100 and 10,000 accounts) | **Held for P** (σ = 0.5: 599 at 100, 566 at 10,000). **Failed for Q** (82 → 405, a factor of 5; σ = 0.25 3.5×; σ = 1.0 5.1×). Q still clears at every dose, so the crossing is unchanged |
| D3 | Unpaired dose at least 10× the paired dose for arm P, every σ | **Held**, but only as a lower bound: the paired dose is the lowest dose tried (1), so the true factor is at least 100, 300 and 1,000 |
| D4 | P loosens ρ\*, Q tightens it, every σ, every dose ≥ 100 | **Held** |
| D5 | Block B reproduces block A's unpaired dose within 2× | **Held.** 77 / 68, 250 / 280, 567 / 655 (interpolated) |

## 3. The numbers

**Clean ρ\*** (exact solver, mean over 30 seeds, block A). The spread is the draw-to-draw standard deviation of ρ\* across seeds, which is the noise an observer without the clean arm faces.

| σ | Clean ρ\* | sd across seeds |
|--:|--:|--:|
| 0.25 | 1.1626 | 0.00012 |
| 0.50 | 1.2472 | 0.00052 |
| 1.00 | 1.4674 | 0.00152 |

**The curve.** Smallest grid dose at which the mean move clears k = 2 under each bar. Both blocks agree on every cell. Interpolated crossing for the unpaired bar in brackets (log-log, block A).

| σ | Arm | Paired bar (B1, as asked) | Unpaired bar (B3) | B3 dose as % of N |
|--:|---|--:|--:|--:|
| 0.25 | P, phantom | **1** (lowest tried) | **100** [77] | 0.05% |
| 0.25 | Q, K physical | **1** (lowest tried) | **100** [77] | 0.05% |
| 0.25 | T, typical, K tied | **none up to 100,000** | **none up to 100,000** | — |
| 0.50 | P | **1** (lowest tried) | **300** [250] | 0.15% |
| 0.50 | Q | **1** (lowest tried) | **300** [251] | 0.15% |
| 0.50 | T | none | none | — |
| 1.00 | P | **1** (lowest tried) | **1,000** [567] | 0.5% |
| 1.00 | Q | **1** (lowest tried) | **1,000** [570] | 0.5% |
| 1.00 | T | none | none | — |

**Absolute figures behind the unpaired column** (σ = 0.50, arm P, block A): 300 fabricated accounts move ρ\* from 1.2472 to 1.2490 (+0.00176). The bar is 2 × 0.000732 = 0.00146. At 100 accounts the move is +0.00059 against a bar of 0.00146, so it does not clear. **One account moves ρ\* by about 5.9 × 10⁻⁶** (σ = 0.5), 7.6 × 10⁻⁶ (σ = 1.0) and 4.5 × 10⁻⁶ (σ = 0.25), almost linearly up to about 5% of N.

**The paired column in absolute figures** (σ = 0.50, arm P): at 1 account the mean move is +0.000006 and the standard deviation of the paired differences is below 5 × 10⁻⁸, giving a ratio of 603. At 10,000 accounts the move is +0.060194 and the standard deviation is 0.000106, a ratio of 566. **The ratio does not depend on dose**, because the sd of the paired difference grows in proportion to the move.

**Arm T, in absolute figures.** At 100,000 fabricated accounts (50% of N) the mean move is −0.000106 (σ = 0.5, block A) and under 0.0002 in size at every σ and block. That is under 0.02% of ρ\*, against an unpaired noise of 0.0007 to 0.0025.

**Dispersion effect.** The unpaired dose rises roughly in step with the clean-arm noise (0.00012, 0.00052, 0.00152): 100 → 300 → 1,000 accounts. A factor of 4 in σ (0.25 to 1.0) costs a factor of about 10 in dose at the grid resolution, and a factor of 7 to 9 on the interpolated values (77 → 250 → 567).

## 4. What this does not show

1. **The paired bar is not an instrument for dose.** For arm P the ratio of the mean paired move to the standard deviation of the paired differences is 283 to 1,067 at every dose from 1 to 100,000 accounts. The standard deviation of a paired difference is small because both arms share the same population, and it shrinks in proportion to the move. **A bar whose verdict is the same at every dose could not have failed for a fault of any size, so the requested "smallest dose" is the smallest dose tried (1), which is a property of the pairing and not of ρ\*** (brief 4b, 4c: model-entailed). The paired column is reported because it was requested. **Nothing should be quoted from it.** The unpaired column carries the dose axis.
2. **The paired comparison needs the clean arm, and an auditor does not have one.** A paired move is measured against a clean counterfactual of the same population. On real books the clean population is exactly what is unknown. The unpaired bar is closer to what an outside reader of one published ρ\* faces, and it is still optimistic, because it takes the draw-to-draw noise of a **synthetic** population. Real populations differ from one another far more than 30 seeds of one generator do. The 100 to 1,000 accounts are therefore a floor on what would need to be fabricated, not an estimate of it.
3. **Arm T is neutral by identity, and the model is built so.** In this file appetite is `a = c·r`, so a fabricated account with typical `r` raises demand and capacity in the same proportion. The zero move is a consequence of the generator, and it says nothing about real fabricated accounts whose consumption is correlated with their credit differently. It does say that **a fabricator who gives each fake account an ordinary-looking appetite is invisible to ρ\* at any dose, including 50% of the population.**
4. **Arms P and Q are the two ends of one assumption.** P hides the fabricated accounts' consumption and ties capacity to the fake credit. Q gives them consumption but holds capacity at the true value. A real fabrication sits somewhere between. The two arms give the same dose here because the move per account is almost the same size and opposite in sign, which is itself a structural fact of this model.
5. **Two things the request left open were chosen here.** The fabricated accounts' appetite (three arms, all reported) and the meaning of "debit dispersion" (σ of ln appetite per credit-hour, three values). A different dispersion, such as a spread in credit `c`, or heavy tails in `r`, was not run. The 1.15 capacity multiple and the credit distribution are the file's.
6. **k = 2 is the rubric's bar and is not argued for.** The ratio columns in `RUN.txt` let a reader apply any k. At the unpaired bar a change from k = 2 to k = 3 raises the dose by about half, since the move is close to linear in dose.
7. **The 30-seed noise estimate has its own error.** The unpaired standard deviation from 30 seeds carries about ±13%, so the interpolated doses carry about the same. The two blocks agree to within 15%.
8. **This is ρ\* in this file's units (clean ≈ 1.25), not the anchor-tied ρ\* = 0.33 of Foundations §5.5.3 and §5.5.7.** The dose in accounts is scale-free, but the absolute moves are not comparable with the 0.33 figures.
9. **Leg 3 (coverage witness) is unavailable** on a generator, as `rho-rubric` says. Nothing here shows that ρ\* could be contradicted by a record made on a separate path.

## 5. Command and seed

```
python 06-simulation/rho-detection-dose/detection_dose.py --test
python 06-simulation/rho-detection-dose/detection_dose.py > 06-simulation/rho-detection-dose/RUN.txt
```

Seeds 1–30 (block A) and 101–130 (block B). Fault stream = seed + 10,000,000. N = 200,000, F = 10, k = 2. Do not run with `python -I` (it hides numpy on this machine). Ran in under five minutes, 6 processes, under 100 KB written.
