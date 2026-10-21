# Declared before the first run (2026-10-18)

Written before `parcel_identity.py` was executed. The refinery inputs (DOE energies, passage table) were read; no output was computed.

Request: `sr-20260905-how-often-does-a-joint-process-flow-sheet-fa` (SB-05 in `sim-briefs/`).

## Definitions fixed in advance

- **`u`** = probability that one *link* is unresolved. A parcel read by `m` paths has `m - 1` links (each later reading to the first). An unresolved link means the flow sheet cannot say whether that reading is the same parcel or a new one that reads equal.
- **Truth `T`** = each true parcel counted once. **Overstatement** = books ÷ `T`.
- **Policies:** naive sum (counts every reading); P1 assume distinct; P2 assume same; P3 refuse (`not identified` if any link in the walk is unresolved); P4 = the rule now in conformance row 10e, which publishes the resolved union and reports unresolved parcels under row 7, read here as the interval [P2, P1].

## Outcomes

**Level cells (a statement about the size of a number):**

| # | Cell | Fails if |
|---|---|---|
| L1 | Refinery, one buyer holding all 7 co-products: mean P1 overstatement is linear in `u` with slope **2.63** (analytic: (7,697 - 2,118) / 2,118 from the passage table). At `u` = 0.5 it reads **2.32 ± 0.05**. | The simulated slope is outside 2.53 to 2.73. This checks the code against arithmetic done by hand. |
| L2 | Same holding: P3 is unreportable in **more than half** of draws from `u` = **0.05** (analytic 1 - (1-u)^14 = 0.51). | Simulated share at `u` = 0.05 is outside 0.46 to 0.56. |
| L3 | A single co-product's figure needs no identity: P3 unreportable share is **0.000** at every `u`. | Any nonzero value. |
| L4 | Two-co-product holdings (all 21 pairs, refinery) at `u` = 0.1: mean P3 unreportable share lies between **0.05 and 0.40**. | Outside that range. |
| L5 | P4's interval width (P1 ÷ P2) for the full holding at `u` = 0.5 equals the P1 overstatement, i.e. **2.32 ± 0.05**, because P2 is exact when there are no twins. | Outside that range. |

**Change cells (about movement):**

| # | Cell | Fails if |
|---|---|---|
| C1 | **Both directions of the size effect.** At a fixed count-rate `u` = 0.2 on the refinery full holding, "big parcels are undocumented" (unresolved weight ∝ quantity) raises the P1 excess (overstatement - 1) to **more than 1.2×** the uncorrelated excess. "Small parcels undocumented" (weight ∝ 1/quantity) lowers it to **less than 0.8×**. | Either direction fails. |
| C2 | **Twin crossover.** With twin parcels added (distinct, equal quantity, each read by one path) at `u` = 0.3, P2's mean absolute error exceeds P1's once the twin share of equal-reading pairs passes some `t*`. I declare `t*` lies in **0.15 to 0.45**. | No crossover in [0,1], or `t*` outside the range. |
| C3 | In the refinery, P1 stays below the naive sum at every `u` up to 0.5. **This cannot fail by construction (P1 unions what it resolves). It is reported as a control and is not counted as an outcome.** | — |

## Excluded as unfailable (per brief 4b)

- "P4's interval contains the truth." The interval is [P2, P1] and the truth lies between them by construction, so no input can fail it. The interval's **width** (L5) is reported instead.
- P1 ≤ naive sum (C3), for the reason @custos gave at c47620.

## Not declared (exploratory, reported as such)

- Random synthetic chains (6 to 12 steps, 3 to 8 co-products): spread of the slope and of the half-unreportable `u`.
