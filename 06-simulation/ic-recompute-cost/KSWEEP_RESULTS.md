# How the re-weighting cost moves with k

> **Version:** 0.1
> **Date:** 2026-10-08

> **Run: 2026-10-08.** Answers `sr-20260916-measure-the-re-weighting-to-record-check-rat`, dated by the author for 2026-10-28.
> **Code:** [`reweight_ratio.py`](reweight_ratio.py) `--events 1e8 --reps 3 --k-sweep 1,3,5,10` · **Transcript:** [`RUN_KSWEEP.txt`](RUN_KSWEEP.txt)
> **9 self-tests, each able to fail. All pass.**

## Terms

| Term | What it means |
|---|---|
| **Record-check pass** | One walk over the log running the integrity checks IC-1 to IC-9. **Eight** of them stream. **IC-5** needs a sort, and is timed on its own |
| **Re-weighting pass** | One walk over the log that converts every stored physical quantity into hours under new weights (Foundations §3.3, §3.2a) |
| **k** | How many physical quantities each event carries and the re-weight collapses: mass, energy, a pollutant, water, land, and so on |
| **Ratio** | Re-weighting seconds ÷ record-check seconds, on the same events |

## The answer

> **The ratio grows by about 0.12 for every added dimension. It passes 1.0 near k = 8 against the eight streaming checks, and at k = 10 against all nine.**

| k | Record check (8) | IC-5 sort | Re-weight | Ratio, 8 checks | Ratio, all 9 |
|--:|--:|--:|--:|--:|--:|
| 1 | 9.2 s | 2.2 s | 1.2 s | **0.130** | 0.106 |
| 3 | 9.2 s | 2.1 s | 3.6 s | **0.393** | 0.320 |
| 5 | 9.2 s | 2.2 s | 5.6 s | **0.604** | 0.490 |
| 10 | 9.1 s | 2.1 s | 11.3 s | **1.232** | 1.000 |

10⁸ events, medians of 3 repeats, pass order flipped. Widest spread across repeats: **0.011**.

**The fitted lines.** Ratio (8 checks) = 0.012 + 0.122 × k. Ratio (all 9) = 0.010 + 0.099 × k. Re-weight time = 0.13 s + 1.11 s × k. The record check stays between 9.10 s and 9.22 s at every k, because it never reads the extra dimensions.

**In plain words: the re-weighting pass is linear in k and the record check is flat, so "about a third" holds only at k = 3.** At k = 10 the two passes cost the same.

## What this means for Foundations §3.4a

§3.4a says, in bold: *"A re-weighting pass costs about a third of a record-check pass."* It names `k` = 3 lower down, in a table.

**That bold sentence is a figure computed at a setting, printed without the setting.** Foundations v0.54 §2.5 forbids exactly that. And k = 3 is low for a real ledger: §2.2 lists kilograms of each substance, joules, labour-hours, water and land as separate dimensions.

**This is a wording fix, not a mechanism change.** Both passes stay linear in the log's length, and memory stays flat. **Folding it needs an author ruling.**

## Against the earlier run

At k = 3 this run gives **0.393**. The 2026-09-12 run gave **0.354** on the same machine and the same generator. Two things differ:

- The re-weight now loops over k columns instead of a fixed three-term sum. Self-test 9 shows the answer is identical. The loop is slightly slower.
- The record check ran at 10.9 M events/s here, against 13.2 M/s on 09-12. The machine was slower today, and both passes moved.

**So 0.354 and 0.393 are two readings on one stack, not one value.** The slope in k is the result. The level is not.

## What this does not show

1. **Disk.** Both passes read memory. The 2026-09 outside disk run (@hemei) raised the ratio by about 0.08 at k = 3. **No disk arm was run here.**
2. **Real data.** Dimensions 4 to 10 are random numbers on the same events. The arithmetic is what is timed, and it does not depend on the values.
3. **One machine.** The slope per k is a reading on one stack.
4. **10⁹ events.** Earlier runs showed both rates are flat from 10⁶ to 10⁹, so 10⁸ was used.
