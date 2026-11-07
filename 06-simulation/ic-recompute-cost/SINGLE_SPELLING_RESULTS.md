# One generator, one byte spelling: record check and re-weight, memory and disk, 10⁸ and 10⁹

> **Date:** 2026-11-07
> **Code:** [`single_spelling.py`](single_spelling.py) · **Transcripts:** [`RUN_SINGLE_1e8.txt`](RUN_SINGLE_1e8.txt), [`RUN_SINGLE_1e9.txt`](RUN_SINGLE_1e9.txt) · **Declared first:** [`SINGLE_SPELLING_DECLARED.md`](SINGLE_SPELLING_DECLARED.md)
> **10 self-tests, each able to fail. All pass.**

## The question

From request `sr-20260915-run-the-record-check-pass-and-the-full-re-we`:

> *Run the record-check pass and the full re-weighting pass off ONE generator with ONE bytes-per-event spelling, on one machine, from DISK and from MEMORY, at 10^8 and 10^9 events, nine checks and eight. Report the four absolute rates and the two ratios, and state whether the memory ratio reproduces the published 0.27.*

## Answer

**The memory ratio does not reproduce 0.27. Under one generator and one packed 34-byte spelling it reads 0.338 (nine checks) and 0.403 (eight) at 10⁸, and 0.334 and 0.405 at 10⁹.** Disk, with the page cache bypassed, reads 0.433 (nine) and 0.500 – 0.508 (eight) at both sizes. Length does not move any of them.

## What was and was not run

- **No 3.4 GB or 34 GB log was stored.** The budget is 1 GB of new files. **Memory** at 10⁸ and 10⁹: each 2,048,000-event chunk is generated and packed untimed, then both passes parse it from RAM (`mem-fresh`: distinct events at any length). **Disk**: one 797 MiB file (12 chunks, 24,576,000 events) is **replayed** with the cache bypassed, 4.08 times for 10⁸ and 40.7 times for 10⁹. **The disk figures at 10⁸ and 10⁹ are therefore a replay proxy.** The control is `mem-replay`, the same file held in RAM.
- Actual sizes: 100,352,000 and 999,424,000 events. k = 3, 1,000,000 accounts, seed 41, single core.
- 10⁸: 3 repetitions per arm. **10⁹: 1 repetition per arm** (about 5 minutes each), so it has no spread.

## Declared before running, and what happened

| | Statement | Over | Result |
|---|---|---|---|
| L1 | mem-fresh 10⁸, nine checks, in 0.22 – 0.32 (0.27 ± 0.05) | **a level** | **Failed.** 0.338 (predicted: outside) |
| L2 | mem-fresh 10⁸, eight checks, in 0.30 – 0.40 | **a level** | **Failed by 0.003.** 0.403 |
| L3 | \|ratio(10⁹) − ratio(10⁸)\| < 0.03, mem-fresh | **a level** | Held. 0.004 (nine), 0.002 (eight) |
| L4 | disk-cold nine checks in 0.40 – 0.52 at both sizes | **a level** | Held. 0.433 and 0.433 |
| L5 | replay control < 0.03 at 10⁸ | **a level** | Held. −0.012 (nine), −0.016 (eight); at 10⁹ −0.007, −0.008 |
| A | disk − memory ≥ +0.05 and above the widest range | change | **Met.** +0.107 against a range of 0.007 |
| B | disk ≥ 0.9 | change | Not met |
| C | in between | change | Does not apply |

## The numbers

Machine: AMD64 Family 25 Model 33, Windows 10, 63.9 GB RAM, NTFS, Python 3.14.3, numpy 2.5.1. Medians; 10⁸ spread is min – max over 3 repetitions. Million events a second is written Mev/s.

**10⁸ events (100,352,000)**

| Arm | Record check, nine (Mev/s) | Record check, eight (Mev/s) | Re-weight (Mev/s) | Ratio, nine | Ratio, eight |
|---|--:|--:|--:|---|---|
| Memory, fresh events | 8.63 | 10.28 | 25.51 | **0.338** (0.338 – 0.340) | **0.403** |
| Memory, replay | 8.45 | 10.03 | 25.92 | 0.326 (0.324 – 0.330) | 0.387 |
| Disk, cache bypassed | 7.19 | 8.31 | 16.63 | **0.433** (0.429 – 0.435) | **0.500** |

**10⁹ events (999,424,000), one repetition**

| Arm | Record check, nine (Mev/s) | Record check, eight (Mev/s) | Re-weight (Mev/s) | Ratio, nine | Ratio, eight |
|---|--:|--:|--:|--:|--:|
| Memory, fresh events | 8.51 | 10.31 | 25.49 | **0.334** | **0.405** |
| Memory, replay | 8.60 | 10.43 | 26.32 | 0.327 | 0.397 |
| Disk, cache bypassed | 7.27 | 8.53 | 16.80 | **0.433** | **0.508** |

**The four absolute rates the request asked for, at 10⁹, nine checks:** record check 8.51 Mev/s from memory and 7.27 from disk; re-weight 25.49 from memory and 16.80 from disk. Times: record check 117.4 s, re-weight 39.2 s (memory); 137.5 s and 59.5 s (disk). **Two ratios: 0.334 memory, 0.433 disk.** The IC-5 sort took 20.4 s at 10⁹ and 1.9 s at 10⁸ in every arm.

**Delta (disk − memory-replay, same bytes), nine checks:** +0.107 at 10⁸, +0.106 at 10⁹. The 2×10⁷ run of 2026-11-04 gave +0.102. The three agree.

## Why 0.27 does not reproduce

Not a length effect (10⁸ and 10⁹ agree to 0.004). Not a generator or spelling split (one generator, one spelling here). **The 2026-11-04 run already showed the cause: both passes here parse a packed record, and the re-weight (5 columns, little arithmetic) pays proportionally more for parsing than the record check (11 columns).** The 0.27 comes from flat arrays with no parse. So **0.27 and 0.34 are ratios for two different log layouts**, and neither is wrong. I did not run the flat-array layout again tonight, so this explanation is carried from the earlier run and is not retested here.

## What this does not show

1. **No stored 10⁸ or 10⁹ log was read.** The disk figures replay an 797 MiB file. The replay control (mem-replay vs mem-fresh, −0.012 and −0.007) says replay does not distort the memory ratio. It cannot say the same about disk: a real 34 GB file spans far more of the device than 797 MiB does, and the device could behave differently over that span.
2. **The 10⁹ rows are one repetition each.** The 10⁸ spread (0.002 – 0.007) suggests they are tight, but a single run has no spread of its own.
3. **It does not explain hemei's 0.114 – 0.129.** Their memory arm is about a third of this stack's, and their logs were 34 B and 28 B an event. A single-spelling run on this machine cannot say whether their gap is the spelling, their hardware, or their code. **A run on their hardware with `single_spelling.py` would.**
4. **The disk delta is one device, one filesystem.** NTFS, probably a fast SSD; the device class was not determined. A slower device would raise the ratio.
5. **The re-weight reads all 34 bytes of each event though it uses 18.** A column store would shrink the disk cost for the re-weight. This is a row-store reading.
6. **k = 3 only.** The re-weight cost rises with k, so every ratio here moves up at higher k (KSWEEP), and the disk delta, a read cost shared by both passes, would shrink in relative terms. Not run.
7. **Single core, synthetic uniform events.** IC-5's sort on real logs may cost more or less than on uniform random keys, and the replay arms hold repeated keys.

## Exact command and seed

```
python 06-simulation/ic-recompute-cost/single_spelling.py --test
python 06-simulation/ic-recompute-cost/single_spelling.py --arms mem-fresh,mem-replay,disk-cold --chunks 49 --reps 3
python 06-simulation/ic-recompute-cost/single_spelling.py --arms mem-fresh,mem-replay,disk-cold --chunks 488 --reps 1
```

Seed 41 (the project's `SEED`), k = 3, 1,000,000 accounts, 64 materials, chunk 2,048,000 events. The 10⁹ run needs about 15 GB of free RAM for IC-5's sort. The replay file is written to `06-simulation/log/tmp/` and deleted at the end. Needs Windows for the cache-bypassed arm.
