# Declared before running — rho* detection-dose curve

> **Written 2026-11-06, before the first run of `detection_dose.py`.** The run prints this file's sha256 prefix before it computes any statistic.

## Fixed in advance

| Choice | Value | Why |
|---|---|---|
| Population | N = 200,000, F = 10 h/day, appetite `a = max(0.1, c·r)`, `r ~ LogNormal(ln 1.6, σ)`, capacity `K = 1.15·Σc` | The model of claim 2 in `disparity_ceiling_sim.py`, imported through `rho-rubric/rho_rubric.py` |
| **Three declared debit dispersions** | **σ = 0.25, 0.50, 1.00** (σ is the spread of ln r, the appetite per hour of credit). 0.50 is the file's own value | Low, file, and high |
| **k, fixed now** | **k = 2** | The rubric's own bar (`fires` = move ≥ 2 sd) |
| Seeds | Block A = seeds 1–30. Block B = seeds 101–130, as a replication | Paired: the faulted arm re-uses the clean arm's seed |
| Fault | `count` fabricated accounts at credit exactly F, appended to the books | Request wording |
| Doses | 1, 3, 10, 30, 100, 300, 1,000, 3,000, 10,000, 30,000, 100,000 | One decade apart, half-decade steps |
| Fabricated accounts' appetite is not stated in the request, so **three arms are run and all three are reported** | **P** = phantom: zero recorded appetite, K tied to recorded credit. **T** = typical appetite, K tied to recorded credit. **Q** = typical appetite, K held at the true physical capacity | Rubric legs S4c, S4a, S4b |

## Noise bars (all computed on every cell and printed side by side)

| Bar | What it is |
|---|---|
| **B1 (the requested one)** | k × sd of the **paired differences** (faulted − clean, same seed) at that dose |
| **B3 (an observer without the clean arm)** | k × sd of the **unpaired** difference, hypot(sd of clean ρ\*, sd of faulted ρ\*) |

**The "smallest dose" under a bar is the smallest grid dose where |mean paired move| ≥ bar.** Between grid points, a log-log interpolation is printed and marked as interpolated.

## Outcomes, stated before the run

**Over a level (sizes of numbers):**

| # | Statement | Could it fail? |
|---|---|---|
| L1 | Clean ρ\* at σ = 0.50 is in **[1.10, 1.30]** | Yes. The rubric declared the same range for the same model |
| L2 | Clean ρ\* at σ = 0.25 in **[1.15, 1.45]** and at σ = 1.00 in **[1.30, 1.70]** | Yes |
| L3 | Arm P, σ = 0.50: the mean move at 10,000 fabricated accounts is in **[+0.03, +0.10]** | Yes. From shift ≈ 1.15·F·m ÷ (0.72·Σc), Σc ≈ 14.2 × 200,000 |
| L4 | Arm P, σ = 0.50: the dose that clears **B3** is in **[500, 6,000]** accounts | Yes |

**Over a change (structure):**

| # | Statement | Could it fail? |
|---|---|---|
| D1 | **Arm T never clears B1 at any dose, at any σ, in either block.** (Typical appetite plus K tied to credit is neutral by identity: `a = c·r` so an inserted account raises both sides in the same share.) | Yes. One clearing cell falsifies it |
| D2 | **B1 is flat in dose for arms P and Q**: move ÷ sd(paired) at 10,000 accounts is within a factor of 3 of the same ratio at 100 accounts. If so, B1's "smallest dose" is the smallest dose tried, and says nothing about dose | Yes |
| D3 | **B3's dose is at least 10× B1's dose** for arm P at every σ | Yes |
| D4 | Arm Q (K physical) moves ρ\* **down**, arm P moves it **up**, at every σ and every dose ≥ 100 | Yes |
| D5 | Block B reproduces block A's B3 doses to within a factor of 2 | Yes |

## What would make me say the curve is not usable

If D2 holds, the paired bar B1 does not depend on dose. A criterion that returns the same answer at every dose is **model-entailed** (brief 4c): the verdict is decided by the pairing, not by the fault. In that case B1's column is reported as asked, the entailment is named, and B3 carries the curve.
