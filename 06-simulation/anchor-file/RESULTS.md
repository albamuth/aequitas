# anchor-file — results

> **Date:** 2026-11-18 · **Request:** `sr-20261106-in-rho-sweep-anchor-py-and-stable-band-kappa`

## 1. The question

> In rho_sweep_anchor.py and stable_band_kappa.py, replace the typed 1380 with a read from one published machine-readable anchor file holding value, interval (1,350-1,400 per MEDIAN_LIFESTYLE_RESULT.md), method and version; pin its sha256 and fail the run on a digest change. Move self-test 5 of rho_sweep_anchor.py into a predictions file that is logged and never edited. Print rho* at 1,350, 1,380 and 1,400 at F = 2, 10, 14. Report which inputs to the anchor a stranger cannot recompute from public files.

## 2. Outcomes declared before running

Filed in `predictions.json` (sha256 `c626204e…cb28`, registered in `predictions_log.jsonl` line 1) before the sweep ran.

| # | Statement | Kind |
|---|---|---|
| P1 | rho* at anchor 1,380, F = 10, no shock lies in **0.31–0.35** | **Level** |
| P2 | rho* at 1,350, F = 10 lies in **0.31–0.335** (scale relation: 0.323) | **Level** |
| P3 | rho* at 1,400, F = 10 lies in **0.32–0.35** (scale relation: 0.335) | **Level** |
| P5, P6 | rho* at 1,380 lies in 0.85–1.00 at F = 2 and 0.23–0.27 at F = 14 | **Level** |
| P4 | rho* is non-decreasing in the anchor at F = 10 | Change |
| P7 | The whole 1,350→1,400 interval moves rho* at F = 10 by between 0.005 and 0.020 | Change (size) |
| P0 | Old self-test 5: F = 10 at −30% shock gives rho* below 0.2263 | Level |

Plumbing outcomes: a one-byte change to the anchor file must raise `AnchorDigestError`; an edited predictions file must raise `PredictionsEditedError`. Both could fail and both were tested (T1, T3).

## 3. The numbers

Anchor file: v1.0, value 1,380 h/yr, interval 1,350–1,400, sha256 `1d53b2f36d3df2671e97cf0f710f96c799377a5545218df9140aeaf294a4e970`.

**A. `rho_sweep_anchor.py`, baseline (no shock), N = 200,000, seed 7, grid step 0.01.** Right two columns are the exact rescale `rho*(1380) × anchor/1380`, unrounded.

| F | 1,350 | 1,380 | 1,400 | Span 1,400−1,350 | Rescale to 1,350 | Rescale to 1,400 |
|--:|--:|--:|--:|--:|--:|--:|
| 2 | 0.90 | 0.92 | 0.93 | 0.03 | 0.900 | 0.933 |
| 10 | 0.32 | 0.33 | 0.33 | 0.01 | 0.323 | 0.335 |
| 14 | 0.25 | 0.25 | 0.26 | 0.01 | 0.245 | 0.254 |

**B. `stable_band_kappa.py`, 60,000 people, seed 7.** One-day edge; the cumulative edge (mean over the three declared age seeds, sd 0.0000 in every cell) is identical because the joiner's past debit is set equal to the anchor.

| F | 1,350 | 1,380 | 1,400 | Step 1,350→1,380 | Step 1,380→1,400 |
|--:|--:|--:|--:|--:|--:|
| 2 | 0.995 | 1.017 | 1.032 | +2.23% | +1.44% |
| 10 | 0.323 | 0.330 | 0.335 | +2.26% | +1.48% |
| 14 | 0.247 | 0.253 | 0.256 | +2.27% | +1.45% |

The anchor steps are +2.22% (1,350→1,380) and +1.45% (1,380→1,400). The stable-band edges follow them within 0.05 percentage points.

**Predictions: 8 of 8 held** (log lines 2–9). The two forward-looking ones, P2 and P3, read 0.32 and 0.33 on the 0.01 grid, inside the request's 0.323–0.335 band. Stable-band B reads 0.323 and 0.335 exactly.

**Self-tests:** `rho_sweep_anchor.py` 6/6; `stable_band_kappa.py --test` 9/9; `anchor_sweep.py --test` 5/5.

**Residual typed copies of 1,380.** `stable_band.py` line 96 (`MEDIAN_LIFESTYLE_H_YR`) and `stable_band_cumulative.py` line 54 (`PAST_RATE`) still hold typed 1380.0. `stable_band_kappa.py` no longer reads the first. It asserts both equal the file, so a changed anchor fails the run instead of half-propagating. Other files in `stable-band/` and `median-lifestyle/` still type it (`stable_band_methods.py:34`, `stable_band_children.py`, `gated_vs_locked.py:36`). They were out of scope.

## 3b. Inputs to the anchor that a stranger cannot recompute from public files

Listed with their status in `median_lifestyle_anchor.json`. No `06-simulation/data/` folder is public.

| Input | Can a stranger recompute? |
|---|---|
| BLS Employment Requirements Matrix 2023 (176×176) | **Not from the public files.** BLS withdrew it on 2026-02-06. The project's copy came from the Wayback Machine and sits in the private `data/` folder |
| Final-demand aggregates 2023 (PCE column) | Not from the public files. Same withdrawal and the same private copy |
| EXIOBASE 3, 2022 | Yes in principle (public, several GB). Not in the repository, and the foreign-hours step (~690 of the ~1,380 h) needs it |
| BLS Consumer Expenditure 2023 | Yes (public release). Only a local HTML copy here |
| 1,800 h per job-year | **No file.** A typed constant in `track1_embodied_hours.py` line 64 |
| Median/mean consumption 0.80 | **No file.** A typed constant in `track1_embodied_hours.py` line 68, "CE spread" |
| Housing build-hours (~3,500 on-site, ×2) and Track 4 carbon basis | **No file.** Level-1 constants and a basis choice (Track 4 alone swings about 14×, 1–32 h) |
| BEA secondary-product reassignment | **No.** An upstream convention in the tables; effect on 1,380 not measured (Foundations §3.4a) |

Net: about 2 of the 3 large inputs (the two BLS tables) cannot be fetched from where they were first published, and 4 of the 8 listed items are typed constants no file backs. The anchor file now carries the digest of its own number; it does **not** carry digests of these inputs.

## 4. What this does not show

1. **It does not show 1,380 is right.** The digest pin proves the sims read the same number. It says nothing about whether the number is correct. Reading the file rather than typing the number is the point coywolf made, and it is all this change does.
2. **The interval 1,350–1,400 is a stated range, not a measured one.** The result file gives no sampling distribution. The sweep shows rho* is smooth in the anchor, not that the anchor lies in that range. The unmeasured BEA convention could move it by an unknown amount.
3. **Most predictions were filed with the earlier answers already known.** P0, P1, P5 and P6 restate 2026-11-04 readings, and P2 and P3 come from the rescale law that self-test 6 already enforces. P2 and P3 could not have failed unless the code broke. Only P7 (the span) was a real test of size, and it is also a corollary of the same law.
4. **The predictions log is append-only by convention and by a sha check, not by storage.** Someone who edits both `predictions.json` and the first log line defeats it. Git history is the outside witness, and the launcher commits after the run.
5. **The 0.01 grid hides the answer in instrument A.** At F = 10 the 1,350 and 1,400 cells read 0.32 and 0.33, a span of one grid step. Instrument B reads the same cells at 0.323 and 0.335 by bisection. Quote B for the sub-0.01 differences.
6. **The cumulative edge in B equals the one-day edge by construction** (joiner's past rate = the anchor), so its zero spread is not a finding. Foundations §5.5.3 already says so.
7. **Two typed copies remain upstream**, and only an assertion guards them (see section 3).
8. Capacity (CAP = 0.85), wants sigma and the synthetic population are unchanged and unaudited here.

## 5. Command and seed

```
python 06-simulation/anchor-file/anchor_sweep.py --test
python 06-simulation/anchor-file/anchor_sweep.py
python 06-simulation/disparity-ceiling/rho_sweep_anchor.py
python 06-simulation/stable-band/stable_band_kappa.py --test
```

Seeds: population seed 7 (both instruments); age seeds `stable_band_cumulative.AGE_SEEDS`. Python 3.14, numpy. Wall clock for the sweep: a few minutes. New files: under 100 KB.
