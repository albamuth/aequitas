# Does storing the log on disk move the re-weighting / record-check ratio?

> **Version:** 0.1
> **Date:** 2026-11-04
> **Code:** [`disk_ratio.py`](disk_ratio.py) · **Transcript:** [`RUN_DISK.txt`](RUN_DISK.txt) · **Declared first:** [`DISK_DECLARED.md`](DISK_DECLARED.md)
> **7 self-tests, each able to fail. All pass.**

## The question

From request `sr-20260914-run-the-record-check-pass-and-the-full-re-we`:

> *Run the record-check pass and the full re-weighting pass over a DISK-BACKED log on the author's machine, same generator, order alternated, at 10^8 and 10^9 events. Report ratio_disk and ratio_memory from that same machine, both absolute throughputs, the storage device class, the filesystem, and whether the page cache was forced cold. Pre-registered arms: (A) ratio_disk - ratio_memory inside run-to-run spread means shared I/O does not move it; (B) ratio_disk >= 0.9 means the memory ratio must not be quoted for a stored log; (C) anything between is NO VERDICT, report the interval.*

## What was and was not run

- **10⁸ and 10⁹ were not run.** At 34 bytes an event they need 3.4 GB and 34 GB of log. The budget is 1 GB of new files. **Run: 10⁷ (324 MB) and 2×10⁷ (649 MB)**, each deleted after its run.
- **The cache was forced cold** in the `disk-cold` arm, by opening the file with `FILE_FLAG_NO_BUFFERING` (Windows). The `disk-warm` arm reads through the page cache.
- **Device class: not determined.** The tools that name it (`Get-PhysicalDisk`) were refused in this unattended run. What can be said: NTFS; the cold read added about 0.42 s to a 649 MB pass, which is about 1.5 GB/s, a speed no spinning disk reaches. **Probably NVMe or fast SATA SSD; not confirmed.**

## Declared before running (full text in `DISK_DECLARED.md`)

| | Statement | Over | Result |
|---|---|---|---|
| L1 | Memory arm reproduces the single-generator level: all-nine ratio **0.27 ± 0.07**, eight-check **0.35 ± 0.07** | **a level** | **FAILED on all-nine**: 0.355. Eight-check 0.416–0.418 sits inside 0.28–0.42, at the top edge |
| L2 | Cold ratio_disk lies in [0.27, 1.0) | **a level** | Held: 0.451–0.457 |
| L3 | Cold read ≥ 0.5 GB/s | **a level** | Held, **inferred** (about 1.5 GB/s from the added seconds), not measured directly |
| A | \|disk − memory\| inside run-to-run spread | change | **Not met**: +0.10 against a spread of 0.009 |
| B | ratio_disk ≥ 0.9 | change | **Not met**: 0.457 |
| C | Between | change | **Applies. NO VERDICT under the request's wording; the interval is below** |

## The numbers

Machine: AMD64 Family 25 Model 33 (AuthenticAMD), Windows 10, 63.9 GB RAM (27.1 GB free), NTFS, Python 3.14.3, numpy 2.5.1, single core, k = 3, 1,000,000 accounts, seed 41. One generator (`make_chunk`), one packed 34-byte record, **the same bytes read by both passes in all three arms** (debit totals agree to 1e-9 in every arm). Order flipped on every repetition; 5 repetitions.

**Ratio, nine checks (IC-5 sort included).** Median, with min–max over 5 repeats:

| Events | Arm | Ratio (nine) | Min – max | Ratio (eight streaming) |
|--:|---|--:|---|--:|
| 10⁷ | memory | **0.355** | 0.349 – 0.359 | 0.416 |
| 10⁷ | disk, cache bypassed | **0.451** | 0.446 – 0.459 | 0.515 |
| 10⁷ | disk, page cache | 0.478 | 0.448 – 0.482 | 0.544 |
| 2×10⁷ | memory | **0.355** | 0.349 – 0.358 | 0.418 |
| 2×10⁷ | disk, cache bypassed | **0.457** | 0.454 – 0.459 | 0.522 |
| 2×10⁷ | disk, page cache | 0.473 | 0.470 – 0.475 | 0.538 |

**Delta (disk − memory), nine checks:** cache bypassed **+0.096** (10⁷) and **+0.102** (2×10⁷); page cache +0.123 and +0.119. The widest run-to-run range in any pair is 0.034 (10⁷, page cache) and 0.009–0.013 for the others. **For the cache-bypassed arm the delta is 7 to 11 times the spread.**

**Absolute throughputs, millions of events a second (2×10⁷ events):**

| Arm | Record check, nine | Record check, eight | Re-weight |
|---|--:|--:|--:|
| memory | 8.51 | 10.01 | 23.98 |
| disk, cache bypassed | 7.22 | 8.25 | 15.80 |
| disk, page cache | 6.89 | 7.83 | 14.66 |

**In plain words:** putting the log on disk slows the re-weight by about a third (24.0 to 15.8 M/s) and the record check by about a seventh (8.5 to 7.2 M/s). The re-weight loses more because it is the faster pass, so the same extra seconds of reading are a bigger share of it. The ratio rises from 0.355 to 0.457.

## Reading it against the request's three arms

- **A (no movement): not met.** The delta is +0.10 and the spread is 0.009.
- **B (≥ 0.9): not met.** The ratio is 0.457, about half of B's line.
- **C (between): applies, and the request calls that NO VERDICT with the interval reported.** The interval, for this stack: **ratio_disk 0.446 – 0.459 (cache bypassed), 0.448 – 0.482 (page cache); ratio_memory 0.349 – 0.359; delta +0.096 to +0.123.**
- What can be said without a verdict: **shared I/O moves the ratio up by about 0.1 on this stack and does not push it near 1.0.** That agrees in direction and roughly in size with the outside run (+0.084).

## What this does not show

1. **The memory level did not reproduce.** Declared outcome L1 failed. This stack reads 0.355 in memory against 0.27 published. **The cause is the read path this run added, not drift:** both passes here parse a packed 34-byte record, and the re-weight (5 columns, little arithmetic) pays proportionally more for parsing than the record check (11 columns, more arithmetic). **So the 0.355 is a ratio for packed-record logs, not a correction of 0.27 for flat arrays.** Do not quote 0.355 and 0.27 as measures of one thing.
2. **The re-weight read the whole 34 bytes an event, though it uses 18.** A column-oriented store would let it skip 16 of 34 bytes. **The disk delta here is therefore an upper estimate for the re-weight, and a row-store reading, not the only layout.**
3. **Device class is not known, and one device was tested.** The conclusion "about +0.10" belongs to this NTFS volume on this machine. A slower device would push the ratio higher; a spinning disk could reach 0.9. **No slope across devices was measured; this is one more point, not the project's point.**
4. **10⁸ and 10⁹ were not run.** The 10⁷ and 2×10⁷ rows agree to 0.006 on the delta, so there is no sign of a length effect, but **nothing here was measured at the sizes the request names.**
5. **The cold arm is cold to the page cache only.** Windows can still hold data in the drive's own cache, and I could not drop the standby list (needs administrator rights). The cold read ran at about 1.5 GB/s, consistent with a fast SSD, not with a hard disk.
6. **The warm arm reads slower than the cold arm (0.47 against 0.455).** I did not find out why. A likely cause is the extra copy through the page cache; it is a guess.
7. **Single core, synthetic uniform events, k = 3** — as in the earlier runs. At higher k the memory arm rises (KSWEEP) and the disk delta, which is a read cost shared by both passes, would shrink in relative terms; **this was not run.**

## Exact command and seed

```
cd 06-simulation/ic-recompute-cost
python disk_ratio.py --test
python disk_ratio.py --events 1e7,2e7 --reps 5 > RUN_DISK.txt
```

Seed 41 (the project's `SEED`), k = 3, 1,000,000 accounts, 64 materials, chunk 2,048,000 events. Log files are written to `06-simulation/log/tmp/` and deleted after each size.
