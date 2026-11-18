# Scale-the-anchor self-test and anchor census — RESULTS

> **Request:** `sr-20261105-add-a-scale-the-anchor-self-test-to-rho-swee`
> **Date run:** 2026-11-17 · **Seed:** 7 (both scripts' own seed) · **Foundations read:** v0.69

## 1. The question (quoted)

> Add a scale-the-anchor self-test to rho_sweep_anchor.py and stable_band_kappa.py: run at kappa x 0.5 and kappa x 2, require rho* to scale by the same factor within one grid step, with no literal in the assertion. Predicted from the published cells at F = 10: baseline 0.33 becomes 0.165 and 0.66; -30% 0.19 becomes about 0.095 and 0.38. Then census every script under 06-simulation that assigns a named anchor: how many have an assertion that fails when that anchor is scaled, and how many pin a literal output. Print the count and the denominator.

## 2. Outcomes declared before running

| # | Outcome | Kind |
|---|---|---|
| D1 | All 66 scaled cells of `rho_sweep_anchor.py` (3 floors × 11 shocks × 2 scales) land within one grid step (0.01) of `factor × unscaled`. One miss means the script reads the anchor somewhere other than through ρ ÷ κ | change |
| D2 | **Level:** baseline at F = 10 reads 0.33 ± 0.02 unscaled, 0.165 ± 0.015 at ×0.5, 0.66 ± 0.02 at ×2. −30%: 0.19 ± 0.02, 0.095 ± 0.015, 0.38 ± 0.02 | **level** |
| D3 | `stable_band_kappa.py` one-day edge scales exactly (within bisection tolerance 3e-4 relative to size) at F = 2, 10, 14 | change |
| D4 | **Predicted to fail:** the cumulative edge does NOT scale if only κ is scaled, because `stable_band_cumulative.PAST_RATE = 1380.0` is a second, independent copy of the anchor. It scales when `past_rate` is scaled with κ | change, can fail |
| D5 | Census: most scripts that assign an anchor have no assertion that fails when it is scaled (< 50%) | level |

## 3. The numbers

### 3a. `rho_sweep_anchor.py` (N = 200,000, seed 7, grid step 0.01)

| F = 10 | Unscaled | ×0.5 predicted | ×0.5 measured | ×2 predicted | ×2 measured |
|---|--:|--:|--:|--:|--:|
| baseline | 0.33 | 0.165 | **0.16** | 0.660 | **0.66** |
| −30% shock | 0.19 | 0.095 | **0.09** | 0.380 | **0.37** |

Baseline by floor, ρ\*: F = 2: 0.46 / 0.92 / 1.84 · F = 10: 0.16 / 0.33 / 0.66 · F = 14: 0.13 / 0.25 / 0.51 (×0.5 / ×1 / ×2).

- **66 of 66 scaled cells within one grid step (0.01); worst deviation 0.010.** No censored or never-binding cell in 99 runs.
- The two predictions are off by one grid step in the direction of the grid: 0.165 and 0.095 are half-step values the 0.01 grid cannot print. The −30% ×2 cell reads 0.37, not 0.38.
- **Exact identity:** admitted demand at (s·ρ, s·κ) equals demand at (ρ, κ) to relative 1e-12 (asserted in `scale_the_anchor.py`). The sweep cannot fail this test unless the script reads κ somewhere other than through ρ ÷ κ.
- **F = 2 baseline reads 0.92 here against 1.017 in the Foundations §5.5.3 table.** That 1.017 is the stable-band instrument's number; at F = 10 the two agree (0.330), at F = 2 they do not. Not tested further tonight.

### 3b. `stable_band_kappa.py` (N = 60,000, seed 7, age seed 11, M = 100)

| F | ×0.5 one-day | ×1 | ×2 | ×0.5 cum. (past scaled) | ×1 | ×2 | ×0.5 cum. (κ only) | ×2 cum. (κ only) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 | 0.509 | 1.017 | 2.034 | 0.509 | 1.017 | 2.034 | 0.618 | 1.896 |
| 10 | 0.165 | 0.330 | 0.661 | 0.165 | 0.330 | 0.661 | 0.167 | **0.389** |
| 14 | 0.126 | 0.253 | 0.505 | 0.126 | 0.253 | 0.505 | 0.126 | 0.279 |

- Max relative deviation from exact scaling: one-day **0.14%**; cumulative with past debit scaled too **0.14%**; cumulative with κ only **44.8%**.
- **D4 held.** At F = 10, ×2, scaling κ alone gives a cumulative edge of 0.389 instead of 0.661. The anchor 1,380 h/yr appears twice (κ and `PAST_RATE`), and a test that scales one copy tests half of it.
- The `--test` run of `stable_band_kappa.py` now carries `test_scale_the_anchor` (small population, n = 6,000, F = 10, M = 20). It scales both copies. Its assertions hold no numeric literal.

### 3c. Census (`census.py`; 96 scripts under 06-simulation, excluding `data/`, `99-superseded/`, `log/`)

**Denominator: 21 scripts assign a named anchor** (of 96).

| Measure | Count |
|---|--:|
| Have at least one assert | 19 / 21 |
| An assert touches the anchor by data flow (static, upper bound) | 15 / 21 |
| **Fail when the anchor is scaled ×2 or ×0.5 (dynamic, strict)** | **9 / 21** |
| Survive scaling (tests still pass) | 6 / 21 |
| Not run (no `__main__` guard, writes files, import error, timeout) | 6 / 21 |
| **Pin a literal in at least one assert (heuristic)** | **18 / 21** |
| Pin a literal and no assert touches the anchor | 3 / 21 |

162 assert statements in those scripts: 66 pinned (heuristic), 122 touch an anchor name by data flow.

The 9 that fail when scaled: `rho_sweep_anchor`, `german_prime_sweep`, `res_vs_eff`, `pledge_band_kappa`, `stable_band_births`, `stable_band_children`, `stable_band_kappa`, `stable_band_methods`, `stock_gate_clearing`. In every case the failing test names include a published-level test (`test_kappa_is_the_anchor…`, `test_us_control_reproduces_published_edges`, `test_flow_published_level`, `test_arm0_equals_the_published_script`) or `self_tests` with the 0.33 pin. **None of the 9 was shown to fail on a scale-covariant assertion.** They fail because a pin moved. `rho_sweep_anchor.py` is the case I can state exactly: its `self_tests` fail at ×2 through tests 3 and 5 (pins), and my new test 6 passes at ×2.

**D5 held:** 9 of 21 is 43%, under half. That figure counts pins as "fails", so the count of scripts with a scale-covariant assertion is lower than 9 and was not separated tonight.

## 4. Outcome check

| # | Result |
|---|---|
| D1 | **Held.** 66 / 66, worst 0.010 |
| D2 | **Held.** 0.33 / 0.16 / 0.66; 0.19 / 0.09 / 0.37, all inside the declared bands. The request's 0.095 and 0.38 sit on the edge of one step |
| D3 | **Held.** 0.14% worst |
| D4 | **Held (predicted failure occurred).** 44.8% with κ only |
| D5 | **Held.** 9 / 21 |

## 5. What this does not show

1. **The scale test is a homogeneity check, not a model check.** Admitted demand is a function of ρ ÷ κ and `R_max` never reads κ, so the 66 / 66 result follows from the algebra. It catches a stray literal or a second copy of the anchor. It cannot say 1,380 h/yr is the right anchor, or that ρ\* is right at any scale. By the project's own §3.5 split this is entailed by the model for any correct implementation. Its only job is to catch an implementation slip, and it passed.
2. **Scaling κ alone is not scaling the anchor in `stable_band_*`.** The cumulative edge reads `PAST_RATE` = 1,380 as well. Whether other scripts hold further private copies of 1,380 was not searched beyond the census name rule.
3. **The census "fails when scaled" count cannot tell a scale-covariant assertion from a pin that moved.** All 9 failures are consistent with pins. Pins fail on any change, including a correct rescale, so 9 / 21 is an upper bound on scripts whose assertions respond to the anchor in a meaningful way.
4. **The 6 "survive" cases may be false negatives.** `stable_band_cumulative.py` binds `PAST_RATE` as a default argument at definition time, so setting the module attribute at run time does not reach it. Static data flow says 7 of its 7 asserts touch it. Mutation by attribute assignment misses default-bound and copied constants.
5. **6 of 21 scripts were not run.** Reasons: no `__main__` guard, a file-writing call, an import error, a 60 s timeout (`rho_sweep.py`). Their dynamic status is unknown, not "survives".
6. **The anchor-name rule is a regex** (`ANCHOR|KAPPA|MEDIAN_LIFESTYLE|PAST_RATE`, plus bare 1380 literals). Scripts holding the anchor under another name (`fp_q1_anchor`, `US_H` were caught; `HOUSEHOLD_DEBIT_H` was caught) are only as complete as that rule. A first version missed `stable_band_kappa.py` itself, because `KAPPA_ANCHOR` is derived (`sb.X / 365.0`); that is fixed, but the same gap could exist for names the rule does not match.
7. **"Pins a literal" is a heuristic.** A tolerance such as `<= 0.02` beside a number can read as a pin. Values 0, 1, 2, 3, 4, 5, 10, 100 and below 1e-3 are skipped. 18 / 21 was not hand-audited.
8. **Census counts are after tonight's edits** to `rho_sweep_anchor.py` and `stable_band_kappa.py`. `rho_sweep_anchor.py` had no scale-covariant assertion before (tests 3 and 5 pin 0.33 and 0.226). `stable_band_kappa.py` already had one for the one-day edge (`test_one_day_edge_scales_with_kappa`, against the old κ ratio), and had none for the cumulative edge until tonight.

## 6. Command and seed

```
python 06-simulation/disparity-ceiling/rho_sweep_anchor.py          # self-tests 1-6, seed 7
python 06-simulation/stable-band/stable_band_kappa.py --test        # includes test_scale_the_anchor
python 06-simulation/anchor-scaling/scale_the_anchor.py             # §3a, §3b (seed 7, age seed 11)
python 06-simulation/anchor-scaling/census.py                       # §3c (no randomness; ~2 min)
```
