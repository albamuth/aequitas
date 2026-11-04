# ρ-sweep, anchor-tied — the clearing rate re-measured

> **Version:** 0.1
> **Date:** 2026-11-04
> **Script:** [`rho_sweep_anchor.py`](rho_sweep_anchor.py) · 5 self-tests green
> **Answers:** sim request `sr-20261104-re-run-rho-sweep-py-s-clearing-rate-with-dem`
> **Supersedes the ρ\* levels in** [`RHO_SWEEP.md`](RHO_SWEEP.md) (banner-marked 2026-11-04)

## What was wrong, and what this run fixes

**Terms.** **ρ** ("rho") is a network's debit tolerance: the gate is `D ≤ ρ·C` here (`P` = 0 throughout). **ρ\*** is the clearing rate — the ρ at which admitted demand equals physical capacity; above it the gate stops rationing. **κ** ("kappa") is the model's cost of one median lifestyle, in debit-hours per day. The **anchor** is 1,380 h/yr = 3.7808 h/day, the labour a median US lifestyle commands (Foundations §3.5). A **shock** is a cut to physical capacity. The **lower edge** for an essentials basket `E` is `E ÷ (365·F)`: the ρ below which a floor-only person cannot afford that basket (Foundations §5.5.3).

`rho_sweep.py` set κ to the median credit rate, 13.797 h/day, instead of the anchor. The two differ by 13.797 ÷ 3.7808 = **3.65**, so every published ρ\* was 3.65× too high. The same defect was found and fixed in the stable-band instrument on 2026-10-27 (`../stable-band/RESULTS_KAPPA.md`). This run fixes it here: κ = 3.7808, and the ρ grid runs 0.01 to 4.00 in steps of 0.01 so no deep-shock cell is censored.

## Configuration

| | |
|---|---|
| κ | 1380 ÷ 365 = **3.7808** debit-h/day per median-lifestyle unit |
| CAP | **0.85** — capacity = 85% of unconstrained wants at no shock |
| wants | lognormal, sigma **0.45**, median-normalised, mild credit link (exponent 0.25) |
| N | **200,000** · seed **7** · population `c_i ∈ [F, 24]` from `disparity_ceiling_sim.py` |
| grid | ρ from 0.01 to 4.00, step 0.01 · `P` = 0 |

## ρ\* per cell

Capacity in a cell is `0.85 × Σwants × (1 + shock)`. No cell was censored; every cell binds.

| shock | `F` = 2 | `F` = 10 | `F` = 14 |
|--:|--:|--:|--:|
| 0% | **0.92** | **0.33** | **0.25** |
| −5% | 0.80 | 0.29 | 0.23 |
| −10% | 0.70 | 0.27 | 0.21 |
| −15% | 0.63 | 0.24 | 0.19 |
| −20% | 0.56 | 0.22 | 0.17 |
| −25% | 0.51 | 0.20 | 0.16 |
| −30% | 0.46 | **0.19** | 0.14 |
| −35% | 0.41 | 0.17 | 0.13 |
| −40% | 0.37 | 0.16 | 0.12 |
| −45% | 0.33 | 0.14 | 0.11 |
| −50% | 0.30 | 0.13 | 0.10 |

**In plain words: at the US method the gate's clearing rate at `F` = 10 is 0.33, not 1.2, and a −30% disaster moves it to 0.19, not 0.68.** The old figures were the same measurements in the wrong unit.

## The cross-check that matters

Two independent instruments now read the same quantity:

| `F` | This run, baseline ρ\* | Stable-band edge ρ\*(F), Foundations §5.5.3 |
|--:|--:|--:|
| 2 | 0.92 | 1.017 |
| 10 | **0.33** | **0.330** |
| 14 | **0.25** | **0.253** |

**In plain words: at `F` = 10 and 14 the two instruments agree to the grid step.** At `F` = 2 this run reads about 9% lower; the two use different population kernels, and the spread is an instrument-level reading, not a contradiction. The agent's rescale prediction (1.2 ÷ 3.65 = 0.329) and the −30% prediction (0.68 ÷ 3.65 = 0.186) both land on the measured cells (0.33, 0.19).

## When a shock closes the band

A cell where ρ\* falls below a basket's lower edge means **no ρ both rations and keeps that basket affordable for a floor-only person** — the band of §5.5.3 is closed, and shortage handling moves to the §5.5.4 backstop and the distribution point.

First shock step where ρ\* drops below `E ÷ (365·F)`:

| Basket `E` (h/yr) | `F` = 2 | `F` = 10 | `F` = 14 |
|--:|--:|--:|--:|
| 516 (narrow, low) | −10% | −45% | −50% |
| 655 (narrow, high) | −5% | −35% | −40% |
| 826 (broad, low) | **already at 0%** | −20% | −25% |
| 965 (broad, high) | **already at 0%** | −15% | −20% |

**In plain words: at `F` = 10 the US-method economy absorbs a capacity shock of about 10–15% before the broad essentials basket stops fitting inside the band; at `F` = 14 about 15–20%; at `F` = 2 the broad basket never fit, which is what §5.5.3 already measured.** The narrow basket survives much deeper shocks everywhere.

### Worked example, with the digits

At `F` = 10, broad basket at 826 h/yr: the lower edge is 826 ÷ (365 × 10) = **0.226**. At a −15% shock the gate clears at ρ\* = 0.24, still above 0.226 — open. At −20% it clears at 0.22, below 0.226 — closed. So the first closing step for that basket is **−20%**.

## Limits

- κ is OP-10-dependent like every weighting figure; the anchor itself carries the unaudited BEA secondary-product convention (Foundations §3.4a).
- CAP = 0.85 is the Q1 illustrative capacity share; ρ\* levels scale with it.
- `P` = 0: committed pledges can double a network's effective gate (§4.6), and the pledge term is not in this run.
- One population kernel, one seed. The `F` = 2 spread against the stable band (0.92 vs 1.017) is unexplained beyond kernel difference and is left as a reading.
