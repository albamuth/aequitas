# Parcel identity: results

> Run 2026-10-18. Foundations v0.60, conformance rows 10c, 10e, 10g.

## 1. The question

> How often does a joint-process flow sheet fail to resolve parcel identity - that is, cannot distinguish one input parcel read by two output paths from two separate parcels that read equal? Measure the books' overstatement under an unresolved-identity rate swept from 0 to 50 percent, against the union figure.

**A simulation cannot say how often real flow sheets fail.** That needs plant records, and none is in this project. What it can say is what each failure rate costs. `u` below is a free parameter, swept from 0 to 0.5.

## 2. Outcomes declared before running

Full text in `DECLARED.md`. Result of each cell:

| Cell | Declared | Result |
|---|---|---|
| L1 level | Refinery, all 7 co-products held: slope of mean P1 overstatement in `u` is 2.63 (hand calculation); 2.32 ± 0.05 at `u` = 0.5 | **Held.** 2.325 at `u` = 0.5; slope 2.65 |
| L2 level | P3 unreportable passes one half at `u` = 0.05 (0.51 ± 0.05) | **Held.** 0.513 |
| L3 level | A single co-product never needs identity: 0.000 | **Held.** 0.000 at every `u` |
| L4 level | Two-co-product holdings, `u` = 0.1: mean P3 unreportable between 0.05 and 0.40 | **Held.** 0.153 (range across the 21 pairs 0.086 to 0.267) |
| L5 level | P4 interval width = P1 overstatement, 2.32 ± 0.05 at `u` = 0.5 | **Held, and nearly an identity.** With no twins P2 is exact, so the width is P1 by construction. It checks the code, not the world |
| C1 change | Big parcels undocumented raises the P1 excess above 1.2× flat; small ones undocumented lowers it below 0.8× | **Held both.** 1.24× and 0.65× at `u` = 0.2 |
| C2 change | Twin crossover `t*` between 0.15 and 0.45 | **Failed.** `t*` = 0.58 at `u` = 0.1 and 0.58 at `u` = 0.3 |

**On C2:** before running I had worked out that the mean errors give a crossover near 0.6, which is outside the range I had written down. I kept the declaration as written, and the cell fails.

**Excluded as unfailable:** "P1 is below the naive sum" (structural, @custos c47620), and "P4's interval contains the truth" (the interval is [P2, P1]).

## 3. The numbers

Refinery (real DOE 2015 process energies, 8 steps, 7 co-products, 14 links), one buyer holding every co-product. 4,000 trials per row. Truth `T` = 2,118 TBtu. The naive sum reads 7,697 TBtu, 3.634× `T`.

| `u` | P1 mean | sd | 95th pct | worst of 4,000 | P2 | P3 unreportable | Closed form P1 |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 0.00 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 |
| 0.05 | 1.134 | 0.173 | 1.469 | 2.183 | 1.000 | 0.513 | 1.132 |
| 0.10 | 1.259 | 0.233 | 1.715 | 2.329 | 1.000 | 0.768 | 1.263 |
| 0.20 | 1.528 | 0.315 | 2.086 | 2.921 | 1.000 | 0.955 | 1.527 |
| 0.30 | 1.801 | 0.357 | 2.407 | 3.309 | 1.000 | 0.996 | 1.790 |
| 0.50 | 2.325 | 0.389 | 2.959 | 3.529 | 1.000 | 1.000 | 2.317 |

Steer (illustrative digits, 7 steps, 4 co-products): P1 mean 1.067 at `u` = 0.1 and 1.338 at `u` = 0.5. P3 unreportable 0.612 and 0.998.

**P3 by number of co-products held** (refinery, every combination, mean over holdings, 1,500 trials each):

| Held | Links in the walk (mean) | `u` = 0.05 | `u` = 0.10 | `u` = 0.20 |
|--:|--:|--:|--:|--:|
| 1 | 0 | 0.000 | 0.000 | 0.000 |
| 2 | 1.6 | 0.076 | 0.153 | 0.287 |
| 3 | 3.6 | 0.165 | 0.310 | 0.539 |
| 4 | 5.9 | 0.260 | 0.460 | 0.723 |
| 5 | 8.4 | 0.351 | 0.590 | 0.844 |
| 6 | 11.1 | 0.435 | 0.687 | 0.916 |
| 7 | 14 | 0.515 | 0.759 | 0.969 |

**Size-correlated resolution** (same mean `u` across links; refinery, full holding), P1 excess over truth:

| `u` | Flat | Big parcels undocumented | Small parcels undocumented |
|--:|--:|--:|--:|
| 0.05 | 0.133 | 0.161 (1.20×) | 0.086 (0.65×) |
| 0.10 | 0.263 | 0.329 (1.25×) | 0.172 (0.65×) |
| 0.20 | 0.528 | 0.656 (1.24×) | 0.342 (0.65×) |
| 0.30 | 0.788 | 0.985 (1.25×) | 0.507 (0.64×) |

**Twin parcels** (distinct parcels of equal quantity, each read once, added to the refinery; quantities resampled from the refinery's own steps; twin pairs 0 to 100). P1 is exact on twins and over-counts shared parcels. P2 is exact on shared parcels and under-counts twins. In the mean, P1's error is `u` × (quantity of the shared parcels × their links) and P2's is `u` × (quantity of the twin parcels). `u` cancels, so the crossover does not depend on it. Measured crossover: twin share of ambiguous links **0.58** (`u` = 0.1) and **0.58** (`u` = 0.3). That share is 21 twin pairs against 14 shared links. The measured mean P2 reads 0.958 at 20 twin pairs and 0.952 at 100 (`u` = 0.1), so P2 never understates by more than the twins' quantity times `u`.

**Synthetic chains** (exploratory, 2,000 random chains, 6 to 12 steps, 3 to 8 co-products, closed form): the P1 slope in `u` has mean 2.15 (5th to 95th percentile 0.56 to 4.07). The `u` at which P3 refuses half of full-holding figures has median 0.038 (5th to 95th 0.019 to 0.129), at a median of 18 links.

## 4. What this shows

1. **The books overstate in proportion to `u` and stay under the naive sum.** Refinery, all co-products: 1.13× at `u` = 0.05, 1.26× at 0.10, 1.53× at 0.20, 2.33× at 0.50, against 3.63× for the naive sum. At `u` = 0.1 the error is about a quarter, not a factor. The worst single trial in 4,000 at `u` = 0.5 was 3.53×.
2. **P3 (refuse) is the expensive policy, and it is expensive because of the number of co-products held.** A single co-product's per-kg figure involves no identity and never refuses. A holding of two refuses 15% of the time at `u` = 0.1. A holding of all seven refuses 77% of the time. **@custos's 0.505 at `u` = 0.1 (their 7-parcel model) falls between a holding of 4 co-products (0.46) and one of 5 (0.59) here.** Their figure is the right order of size, and it is for a holding that needs seven identity checks.
3. **The policy choice between P1 and P2 does not depend on `u`.** It depends on the quantity in twin parcels against the quantity in shared parcels. In this model P2 is worse once twin parcels are about 58% of the ambiguous links (about 85% of the quantity).
4. **Where the failures concentrate matters by about a quarter either way.** If large parcels are the undocumented ones, P1's overstatement is 1.2 to 1.25 times larger than the flat case; if small ones are, it is 0.65 times.
5. **Row 10e's remedy (report under row 7) costs, as an interval, [P2, P1].** For the refinery, all co-products, that interval is 1.26× wide at `u` = 0.1 and 2.33× wide at `u` = 0.5.

## 5. What this does not show

1. **How often real flow sheets fail.** `u` is swept, not measured. No plant data is in the project.
2. **Whether failures are independent.** Each link fails on its own. A plant that lost its mix records would lose a whole tank's links together, and the P3 shares here are therefore upper estimates of how often a single document fails, though the P1 means are unaffected (the mean of a sum does not need independence).
3. **The twin crossover is only as real as the twins.** No twin parcels exist in the DOE data. The twin quantities were resampled from the refinery's own steps, and the number of twins is a free parameter. The 0.58 depends on that quantity distribution.
4. **Row 7 closing the gap.** Row 10e says an unresolved parcel is reported under row 7 and never left out. This run treats that as the interval [P2, P1]. Whether row 7 in fact catches a missing mix event is not simulated, so the P3 shares are the share of figures with an open link, not the share a network would end up unable to publish.
5. **Quantity weighting.** Quantities are energy (MJ-equivalent TBtu) only. The labour and pollutant dimensions of the steer are not run, and a parcel that is large in one dimension may be small in another.
6. **The steer is illustrative.** Its digits are declared illustrative in `chain-resolution`.
7. **Interval honesty is not tested.** P4's interval contains the truth by construction, so the run says how wide it is and not whether it is reliable.

## 6. Does the 7.00× matter?

Not as a threshold. 7.00× is the worst parcel (the crude column, read by 7 paths). The buyer-level naive sum is 3.634× and the buyer-level P1 never exceeds 3.53× in any of the 4,000 trials at `u` = 0.5. The two are in different units, as the change log noted.

## 7. Command and seed

```
python 06-simulation/parcel-identity/parcel_identity.py --test
python 06-simulation/parcel-identity/parcel_identity.py        # seed 20261018, 4,000 trials per row
```

Python 3.14, numpy. All inputs are in the repository (`../allocation-engine/refinery_slice.py`, `../chain-resolution/chain_resolution.py`).
