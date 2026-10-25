# Declared before the first run of `threshold_s7.py` (2026-10-23)

Request: `sr-20260908-rewrite-sb-05-section-7-with-a-refutation-th`. Written before the script was executed. Predictions come from the 2026-10-18 `RESULTS.md` and hand arithmetic.

## The new threshold, in one unit

Loss = relative error of the published figure, `|books / T - 1|`, for one buyer's holding.

- P1, P2: mean loss over trials (E1, E2).
- P3: `lambda x s`. `s` is the share of figures reported "not identified". `lambda` is the relative error a network treats as equal to having no figure.
- `lambda` is supplied by whoever runs the check, so no value is fixed. The run reports the **break-even `lambda*` = min(E1, E2) / s**. P3 wins only if `lambda` > `lambda*`.
- **Arm A (P1 against P2)** is decided by `t`, the twin share of ambiguous links. Reported as the crossover `t*`.
- **Arm B (best of P1/P2 against P3)** is decided by `lambda`. Reported as `lambda*(u)`.

## Level cells (each fails if the number is outside its range)

| # | Cell | Fails if |
|---|---|---|
| S1 | Refinery, all 7 co-products, flat, no twins, `u` = 0.1: `lambda*` = **0.34** (E1 0.259 / s 0.768) | outside 0.30 to 0.38 |
| S2 | Same, `u` = 0.2: `lambda*` = **0.55** (0.528 / 0.955) | outside 0.50 to 0.60 |
| S3 | All 21 two-co-product holdings, flat, no twins, `u` = 0.1: `lambda*` between **0.3 and 1.0** | outside that range |
| S4 | Arm A crossover `t*` (full holding, flat) = **0.58 ± 0.07** at `u` = 0.1 and at `u` = 0.3 | outside 0.51 to 0.65 at either `u` |
| S5 | Size-correlated, full holding, `u` = 0.2: P3 refusal share for "small parcels undocumented" lies **0.85 to 0.955**, i.e. at or below flat. This disagrees with @custos's 0.945 against 0.779, which came from a different 7-parcel model | outside that range |
| S6 | `u` at which P1's 95th-percentile error first exceeds 0.5 (full holding, flat, no twins, grid 0.05/0.10/0.20/0.30/0.50) is **0.10** | any other grid value |

## Threshold wording to be tested (the replacement for section 7)

- **Arm B (P3 against P1, the conservative reading)**: P3 wins only if `lambda` is **below** `lambda*`, that is, only if a network counts a missing figure as cheaper than a `lambda*`-sized error. **P3 is refuted as the default if `lambda*_P1` at `u` = 0.2 is below 0.5 for the full holding.** I predict 0.55, so I expect it to survive narrowly. 0.5 is my own tolerance: a missing figure is judged worse than a 50% error. The run prints the whole `lambda*` curve so any reader can use their own tolerance. *(Correction made after the first self-test run and before any full run: I first wrote the direction backwards, "wins above". The S1 to S7 numbers are unchanged. The self-tests caught it.)*
- **Against P2** at zero twins `lambda*` is 0 by construction, because P2 is exact when no twin exists. That cell is entailed and reported as such, not counted.
- **Arm A is refuted for P2** if `t*` is below 0.35 in any mode. I predict it is not.

## Change cell

| # | Cell | Fails if |
|---|---|---|
| S7 | `t*` stays within **0.3 to 0.9** in all three modes (flat, big dark, small dark), both holdings, at `u` = 0.1 and 0.3 | any mode outside, or no crossover |

## Excluded as unfailable

- "P1's buyer-level overstatement exceeds the naive sum's 7.00x or 3.634x". P1 unions what it resolves, so it cannot pass the naive sum. Run only as a control in the self-tests.
- "P3's `lambda*` is above some number" with `lambda` fixed by me. `lambda` is an input of the checker, so only the break-even is reported.
