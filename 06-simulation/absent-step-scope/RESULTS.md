# Absent-step scope: results

Request `sr-20260910-over-a-real-multi-step-process-flow-sheet-ho` (hemei, c50095, objection `obj-20260910-hemei-expected-actual-passage-row`). Run 2026-10-28.

## 1. The question

> Over a real multi-step process flow sheet, how often does an absent step divide into enumerated-and-absent versus never-looked-at, and what is the debit-hours-per-kg error when a reader cannot tell them apart?

Terms. A **passage claim** (Foundations 3.4a) is the set of steps a product went through. An **absent** step is one not in that set. **Enumerated-and-absent (E)**: the plant looked and recorded "not passed". **Never-looked-at (N)**: no record. A sheet with no scope line shows E and N the same way.

## 2. Outcomes declared before the first run

| # | Kind | Statement | Result |
|---|---|---|---|
| L1 | level | Steer, hide, MJ/kg: coarse is 6.25x fine. In collapsed debit-hours per kg the gap is 3.5x to 4.5x, not 6.25x | **Held.** 6.250x energy only; **4.096x** in hours |
| L2 | level | At least 40% of (product, step) cells are absent, in both cases | **Held.** Steer 12 of 28 (43%); refinery 34 of 56 (61%) |
| L3 | level | At q = 0.5 the TRUST reader's mean error is 15% to 60% of the true figure, on each chain | **Held.** Steer 50.1%; refinery 49.3% |
| L4 | level | Share of N cells hiding a real passage equals K/M within 0.02 | **Held.** Steer 0.569 to 0.573 vs 0.571; refinery 0.389 to 0.393 vs 0.393 |
| C1 | change | At q = 0.5 the SCOPED reader's mean error is below TRUST's, on each chain | **FAILED on both.** Steer 80.9% vs 50.1%; refinery 51.9% vs 49.3% |
| C2 | change | Under producer-chosen omission TRUST understates every product hit and SCOPED understates none | Held, but the SCOPED half is true by construction (see section 4) |

L4 is a counting identity and L2 is a count of the input table. Neither could have surprised the model. They are reported as checks on the code, not as findings about real sheets.

## 3. The numbers

Readers: **TRUST** reads absent as not passed. **CEILING** reads absent as maybe passed, so charges every step (the coarse reading). **SCOPED** has a scope line: E is not passed, N is charged. A reader with no scope line can only be TRUST or CEILING.

Cases: **steer** (illustrative digits, collapsed to hours with the illustrative weights 1 h, 0.05 h/kg pollutant, 0.002 h/MJ) and **refinery** (real DOE process energies; native units per kg, never converted to hours because DOE's TBtu per year and the per 100 bbl masses are on different scales, so only ratios between readers mean anything).

### 3a. The coarse reading against the truth (the "6.25x")

| Steer product | True h/kg | Coarse h/kg | Coarse / true |
|---|--:|--:|--:|
| hide | 0.1327 | 0.5437 | **4.10x** |
| organs | 0.1265 | 0.3625 | 2.87x |
| hooves and head | 0.2893 | 0.7250 | 2.51x |
| packaged beef | 0.0870 | 0.0870 | 1.00x |

Hide, energy only: 2.00 vs 12.50 MJ/kg = **6.25x**. Refinery coarse / true runs 1.25x (gasoline) to 2.56x (residual fuel, asphalt).

### 3b. How often each kind of absence occurs (iid sheets: each cell enumerated with probability q; 2,000 sheets per q; mean of pooled counts)

| q | Steer: N share of absent | Refinery: N share of absent |
|--:|--:|--:|
| 0.25 | 0.875 | 0.831 |
| 0.50 | 0.701 | 0.620 |
| 0.75 | 0.438 | 0.355 |
| 0.90 | 0.207 | 0.154 |

The N share is arithmetic in q: M(1-q) / (M(1-q) + q(M-K)). **The model does not say what q is for any real plant.** No real sheet's enumeration rate was measured (section 4).

Of the N cells, **57% (steer) and 39% (refinery) hide a real passage**, at every q. That is K/M, the share of cells that are passed, and nothing more.

### 3c. The error when a reader cannot tell E from N (q = 0.5, mean over products; ± is the spread over 2,000 sheets)

| Chain | Reader | Mean abs error per kg | Mean abs error, % of true | 5th to 95th pct | Direction |
|---|---|--:|--:|--:|---|
| Steer | TRUST | 0.0794 ± 0.0252 h/kg | 50.1 ± 14.7 | 25.8 to 74.5 | understates 89% of product-sheets |
| Steer | CEILING | 0.2707 h/kg | 161.7 | fixed | overstates |
| Steer | SCOPED | 0.1358 ± 0.0442 h/kg | 80.9 ± 26.1 | 38.6 to 124.0 | overstates 70% |
| Refinery | TRUST | 0.587 ± 0.186 units/kg | 49.3 ± 12.5 | 28.7 to 69.7 | understates 86% |
| Refinery | CEILING | 1.481 units/kg | 104.0 | fixed | overstates 100% |
| Refinery | SCOPED | 0.737 ± 0.169 units/kg | 51.9 ± 10.7 | 34.3 to 69.7 | overstates 96% |

The error is **not a fixed multiple**. It runs from 0% at q = 1 to 100% (TRUST reads zero) at q = 0. The q sweep is in `RUN.txt`.

### 3d. When the unlisted cells have a pattern

| Sheet | TRUST | CEILING | SCOPED |
|---|---|---|---|
| **Tail** (lists steps only up to each product's last passed step). Steer | 0.0% | 161.7% mean, 309.6% worst | 161.7% mean, 309.6% worst |
| Tail, refinery | 0.0% | 104.0% mean, 156.4% worst | 68.0% mean, 156.4% worst |
| **Adv, k=1** (producer omits the dearest passed step). Steer | understates 4 of 4, worst 59% | n/a | understates 0 of 4 |
| Adv, k=1, refinery | understates 7 of 7, worst 73% | n/a | understates 0 of 7 |
| Adv, k=2, both | understates all, worst 100% | n/a | understates none |

**No single reader wins.** On a tail-listed sheet TRUST is exactly right and a scope line makes things worse. On a producer-chosen omission TRUST is wrong by up to 100% and the scope line stops it.

## 4. What this does not show

1. **How often real plants leave steps never-looked-at.** q is an input here, swept from 0 to 1. No corpus of real flow sheets is in the project (`06-simulation/data/` holds BLS, EXIOBASE and IO tables, no plant sheets). The section 3b shares follow from q and the cell counts, and say nothing about industry.
2. **That the refinery or steer sheet is typical.** The refinery's passage table is a declared standard configuration, not a plant's own sheet. The steer's digits are illustrative. Two chains, 28 and 56 cells.
3. **A debit-hours figure for the refinery.** Its energy is in native units on a different scale from its masses. Only ratios between readers hold there.
4. **The weights.** The steer's hours use 0.002 h/MJ, which is unsourced, and 0.05 h/kg of pollutant. The 4.10x depends on them; the 6.25x does not.
5. **That SCOPED never understates, or that it stops an adversary.** SCOPED charges every unlisted step, so it cannot understate, and in the adversarial sheet every unlisted cell is a real passage, so it cannot overcharge either. Both follow from how the sheets are built. The result that carries weight is C1, which failed.
6. **Which cells a lying producer would choose.** Adv omits the dearest passed steps, one stylised rule. A producer who also has a different path's meter in mind (`../false-passage/`) is not modelled.
7. **Independence of cells.** The iid sheets treat each cell alone. Real unlisted steps cluster by unit or by plant section.
8. **That a scope line is cheap to publish or to check.** Nothing here prices the extra field, or who checks that an "enumerated-and-absent" record is honest. An E record is a claim by the producer like any other passage claim.

## 5. Command and seed

```
python 06-simulation/absent-step-scope/absent_step_scope.py
```

Seed **20261028**, 2,000 sheets per q, Python 3.14. Output in `RUN.txt`. Self-tests: 8 of 8 pass.
