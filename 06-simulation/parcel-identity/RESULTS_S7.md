# SB-05 section 7: a refutation threshold both arms of which can fail

> Run 2026-10-23. Foundations v0.61. Extends `parcel_identity.py` (RESULTS of 2026-10-18 stay in `RESULTS.md`).

## 1. The question

> Rewrite SB-05 section 7 with a refutation threshold both arms of which can fail. Custos's candidate: P1 against P2, plus a penalty on P3's unreportable share, since the three policies partition the space. Then re-run the sweep, including the size-correlated variant our brief did not specify.

## 2. Outcomes declared before running

Full text: `DECLARED_S7.md`. Written before the first full run. One correction was made between the first self-test run and the full run: I had the direction of arm B backwards ("P3 wins above `lambda*`"). The self-tests caught it. The numeric cells were not changed.

| Cell | Declared | Result |
|---|---|---|
| S1 level | `lambda*_P1` at `u` = 0.1, full holding, flat = 0.34 (0.30 to 0.38) | **Held.** 0.337 |
| S2 level | same at `u` = 0.2 = 0.55 (0.50 to 0.60) | **Held.** 0.559 |
| S3 level | 21 two-co-product holdings, `u` = 0.1: `lambda*_P1` in 0.3 to 1.0 | **Held.** 0.369 |
| S4 level | crossover twin share `t*` = 0.58 ± 0.07 at `u` = 0.1 and 0.3 (full holding, flat) | **Held.** 0.549 and 0.550 |
| S5 level | small-parcels-undocumented P3 refusal at `u` = 0.2 lies 0.85 to 0.955, at or below flat | **Failed.** 0.974, above flat (0.957). I had Jensen's inequality backwards: uneven resolution raises the refusal share. The self-test I first wrote carried the same error and passed only by noise. Both are fixed |
| S6 level | `u` where P1's 95th-percentile error first exceeds 0.5 is 0.10 | **Held.** 0.10 (0.469 at 0.05, 0.675 at 0.10) |
| S7 change | `t*` within 0.3 to 0.9 in all modes, both holdings, `u` = 0.1 and 0.3 | **Held.** Range 0.50 to 0.88 |
| Arm B (P3 against P1) | `lambda*_P1` at `u` = 0.2 is at least 0.5 for the full holding, so P3 survives narrowly | **Held for the full holding (0.559). It fires in 4 of 6 cells**, see below |

**Excluded as unfailable:** P1 or P2 passing the naive sum (control only); `lambda*` against P2 with no twins (it is 0 because P2 is exact there).

## 3. The new threshold, and why each arm can fail

One unit for every policy: **relative error of the published figure**, `|books / T - 1|`, for one buyer's holding.

| Policy | Loss |
|---|---|
| P1 (assume distinct) | E1 = mean error over trials |
| P2 (assume same) | E2 = mean error over trials |
| P3 (refuse) | `lambda` × `s`. `s` = share of figures reported "not identified". `lambda` = the relative error a network treats as equal to having no figure |

- **Arm A, P1 against P2.** Decided by `t`, the share of ambiguous links that are twin parcels. P2 wins below `t*`, P1 above. It fails in both directions: at `t` = 0, E1 = 0.263 and E2 = 0.000 at `u` = 0.1; at `t` = 0.88, E1 = 0.010 and E2 = 0.048.
- **Arm B, P3 against the others.** P3 wins only if `lambda` < `lambda*`, where `lambda*` = (E1 or min(E1, E2)) ÷ `s`. It fails in both directions: P3 wins at `lambda` 0.1 and loses at `lambda` 5 (self-test).
- `lambda` is supplied by whoever runs the check, so the run does not fix it. It reports `lambda*` and the reader compares it to their own value.

**An entailed cell, stated openly.** With no twin parcels P2 is exact, so `lambda*` against the best of P1 and P2 is 0 at every `u`. That reading is decided by the twin share, which nobody has measured. Arm A's verdict is therefore decided by `t`, an input. The run reports `t*` and does not claim to say which side real flow sheets are on.

## 4. The numbers

Refinery (DOE 2015 process energies, 7 co-products, 14 links). 4,000 trials per full-holding row, 1,000 per pair-holding row. Truth `T` = 2,118 TBtu.

**Arm B, P3 against P1 (no twins).** E1 = mean P1 error, `s` = P3 refusal share.

| Holding | Resolution | `u` | E1 | `s` | `lambda*_P1` |
|---|---|--:|--:|--:|--:|
| 7 co-products | flat | 0.05 | 0.134 | 0.516 | 0.260 |
| | flat | 0.10 | 0.263 | 0.781 | 0.337 |
| | flat | 0.20 | 0.535 | 0.957 | 0.559 |
| | flat | 0.50 | 1.313 | 1.000 | 1.314 |
| | big parcels dark | 0.20 | 0.658 | 0.962 | 0.684 |
| | small parcels dark | 0.20 | 0.344 | 0.974 | 0.353 |
| 2 co-products (mean of 21) | flat | 0.10 | 0.056 | 0.152 | 0.369 |
| | flat | 0.20 | 0.109 | 0.288 | 0.379 |
| | big parcels dark | 0.20 | 0.123 | 0.290 | 0.425 |
| | small parcels dark | 0.20 | 0.093 | 0.293 | 0.318 |

At `u` = 0.2 against a tolerance of `lambda` = 0.5, P3 is refuted in 4 of the 6 cells (all three pair cells, and small-dark on the full holding). It survives on the full holding with flat or big-dark resolution.

**P1's 95th-percentile error** (full holding, flat): 0.469 at `u` = 0.05, 0.675 at 0.10, 1.105 at 0.20, 1.941 at 0.50. The 95th percentile first passes 0.5 at `u` = 0.10 and 1.0 at `u` = 0.20.

**Arm A crossover `t*`** (twin share of ambiguous links at which P2's mean error passes P1's). It does not depend on `u` (0.547 to 0.581 on the full holding).

| Resolution | 7 co-products | 2 co-products |
|---|--:|--:|
| flat | 0.55 | 0.83 |
| big parcels dark | 0.58 | 0.87 |
| small parcels dark | 0.51 | 0.73 |

**With twins (full holding, flat, `u` = 0.1).** `lambda*` against the better of P1 and P2:

| Twin pairs | Twin share `t` | E1 | E2 | `s` | `lambda*` best |
|--:|--:|--:|--:|--:|--:|
| 0 | 0.00 | 0.263 | 0.000 | 0.781 | 0.000 |
| 5 | 0.26 | 0.168 | 0.019 | 0.861 | 0.022 |
| 10 | 0.42 | 0.067 | 0.037 | 0.922 | 0.041 |
| 21 | 0.60 | 0.032 | 0.044 | 0.971 | 0.033 |
| 100 | 0.88 | 0.010 | 0.048 | 1.000 | 0.010 |

## 5. What this shows

1. **A threshold with two failable arms exists, in one unit.** Arm A is read off `t*` (0.51 to 0.87), arm B off `lambda*` (0.17 to 1.31 across the swept cells).
2. **Arm B depends on the holding and the resolution pattern, not only on `u`.** At `u` = 0.2 against `lambda` = 0.5 it passes on 2 cells and fails on 4. Averaged pair holdings, which are the common case, fail it.
3. **Against the better of P1 and P2, P3 almost never pays.** `lambda*` is at most 0.04 once a few twins exist: refusing wins only if a missing figure is judged cheaper than a 4% error.
4. **Size-correlated resolution raises P3's refusal share slightly, and P1's error a lot in one direction.** At `u` = 0.2, full holding: refusal 0.957 flat, 0.962 big-dark, 0.974 small-dark. P1 error 0.535 flat, 0.658 big-dark (1.23×), 0.344 small-dark (0.64×). This agrees in direction with @custos (0.779 to 0.945) and is far smaller in size. Their model was seven parcels with resolution probability proportional to size; the models differ and I did not reproduce theirs.
5. **The old 7.00× arm is struck, not repaired.** P1 unions what it resolves, so it cannot pass the naive sum (3.634× at buyer level, 7.00× only for the single worst parcel). Control confirmed: P1's worst of 3,000 trials never passes 3.634×.

## 6. What this does not show

1. **Which side real flow sheets are on.** `t` (twin share) and `u` are swept. No plant data is in the project, so arm A's verdict is open until someone measures `t`.
2. **A correct `lambda`.** `lambda` is the cost of a missing figure, and I have no source for it. The 0.5 tolerance is mine. The `lambda*` table is the result; the verdict at 0.5 is an illustration.
3. **Custos's 0.945.** I did not reproduce their size-correlated model, so the size of the rise from 0.779 to 0.945 is unchecked here. Direction only.
4. **Independence.** Each link fails separately. A plant that lost a whole tank's records would fail many links together, which lowers `s` and leaves the mean P1 error alone.
5. **Row 7 closing the gap.** Row 10e reports unresolved parcels under row 7. This run treats that as P1/P2, not as a repair.
6. **One process.** The refinery is the only real chain. The steer is illustrative and was not rerun. The 2026-10-18 synthetic chains show the half-refusal `u` ranges 0.019 to 0.129, so `lambda*` would too.
7. **Twin parcels are resampled quantities**, not observed parcels.

## 7. Command and seed

```
python 06-simulation/parcel-identity/threshold_s7.py --test
python 06-simulation/parcel-identity/threshold_s7.py     # seed 20261023, writes threshold_s7.csv
```

Python 3 with numpy. About 2 minutes. Output: `threshold_s7.csv` (180 rows).
