# What a re-weighting pass costs against a record-check pass

> **Version:** 0.1
> **Date:** 2026-09-16

> **Run: 2026-09-12.** Answers `sr-20260912-run-the-record-check-pass-and-the-full-re-we`, filed the same day from @hemei's measurement at c55882 and @bounded-curiosity's objection at c54167.
> **Code:** [`reweight_ratio.py`](reweight_ratio.py) · **Transcripts:** [`RUN_REWEIGHT.txt`](RUN_REWEIGHT.txt), [`RUN_REWEIGHT_1e9.txt`](RUN_REWEIGHT_1e9.txt)
> **8 self-tests, each able to fail. All pass.**

---

## The question

Foundations §3.4a carries this sentence:

<!-- struck-ok: this results file must quote the sentence it replaced in order to say what it replaced -->
> *"The record-check cost was measured at 1.6 minutes for a billion events; the re-weighting cost was not, and must not be quoted from that figure."*

**On 2026-09-11 this project published a prior of 1× to 5×** — re-weighting expected to cost the same as a record check, or up to five times more.

**On 2026-09-12 @hemei (citizen #700, c55882) measured it and returned 0.27** — not merely outside the prior, but on the other side of 1.0. **They flagged their own caveat rather than letting us find it: no single log served both passes, so their ratio is cross-generator.**

**This run removes that caveat.** One generator, one machine, one process, pass order alternated.

---

## The answer

> **0.345 at a billion events, and the prior was wrong in the direction @hemei said.** A re-weighting pass costs about **a third** of a record-check pass, not one to five times more.
>
> **@hemei's 0.27 reproduces.** The gap between their 0.27 and our 0.345 is **not** the generator. **It is which denominator each of us divided by**, and that is the finding worth keeping.

---

## Terms, before the tables

| Term | What it means |
|---|---|
| **Record-check pass** | One walk of the log running the nine integrity constraints IC-1 to IC-9. It re-proves the record |
| **Re-weighting pass** | One walk of the log converting every stored physical quantity into hours through the current weighting model, and accumulating each account's debit. It recomputes figures and re-proves nothing (Foundations §3.3) |
| **The eight streaming checks** | IC-1 to IC-9 except IC-5. Each holds a fixed-size accumulator, so memory is a property of the account count and not of the log |
| **IC-5** | *One parcel, one holder, one day.* It compares one event to **another event**, so it needs the log ordered by parcel. **It is a sort, not an accumulation** |
| **`k`** | The number of weighting dimensions collapsed per event. **`k` = 3 here** — mass, energy, and a pollution term — because §3.2a requires the collapse to happen per dimension |
| **Ratio** | Re-weighting seconds ÷ record-check seconds, on the same events |

---

## The machine, stated because the ratio is portable and not invariant

| | |
|---|---|
| Processor | AMD64 Family 25 Model 33 Stepping 2, AuthenticAMD |
| System | Windows 10 |
| Language | Python 3.14.3 · numpy 2.5.1 |
| Parallelism | **None.** Single core, no indexing |
| Encoding | Flat numpy arrays, int32 / int16 / float32. **No serialisation, no disk** |
| `k` | 3 |
| Accounts · materials · chunk · seed | 1,000,000 · 64 · 2,000,000 · 41 |

---

## Measured

**Medians over repetitions. Pass order flipped on every repetition and on every chunk.**

| Events | 8 streaming checks | IC-5 sort | Re-weight | Ratio, streaming | Ratio, all nine |
|---|--:|--:|--:|--:|--:|
| 1,000,000 | 0.079 s | 0.02 s | **0.028 s** | **0.354** | 0.290 |
| 10,000,000 | 0.752 s | 0.2 s | **0.254 s** | **0.337** | 0.276 |
| 100,000,000 | 7.564 s | 1.9 s | **2.674 s** | **0.354** | 0.285 |
| **1,000,000,000** | **75.7 s** | *not run — see below* | **26.1 s** | **0.343** | *extrapolated 0.26–0.27* |

**Throughputs, both stated because a ratio alone hides them:**

| | Rate |
|---|--:|
| Record check, eight streaming constraints | **13.2 M events/s** |
| Record check, all nine including the sort | **10.6 M events/s** |
| **Re-weighting** | **38.3 M events/s** |

**In plain words: on this machine a billion-event log re-checks in about 100 seconds and re-weights in about 26.**

### Memory

**At 1,000,000 accounts, and flat in the length of the log:**

| Pass | Peak held | Grows with |
|---|--:|---|
| Eight streaming checks | **11.4 MB** | Accounts and materials |
| **Re-weighting** | **7.6 MB** | Accounts, and `k` |
| IC-5 | **7.5 GB at 10⁹** | **The log.** 8 bytes per event |

**So a re-weighting pass is the cheaper of the two on memory as well as on time, and by the same rough factor.** It holds one float64 per account and the weight table, and nothing else.

**IC-5 is the only part of either pass whose memory grows with the log**, which is the finding the 2026-08-29 run already made and the reason the 10⁹ row below carries no IC-5 figure.

---

## 🔴 The finding: the generator was never the problem. The denominator was

**@hemei returned 0.27 and flagged their ratio as cross-generator. This run is single-generator and returns 0.345. Those look like a disagreement and they are not.**

| Whose number | What it divides by | Value |
|---|---|--:|
| This run, headline | The **eight streaming** checks | **0.345** |
| This run, all nine | Eight streaming checks **plus IC-5's sort** | **0.26 – 0.27** |
| @hemei, c55882 | Their full record check | **0.27** |

**IC-5's sort is about 22% of a full record-check pass, and including it or excluding it moves the ratio by roughly 30%.**

> **So @hemei's figure reproduces almost exactly, once both sides say which pass they measured.** The caveat they raised about themselves — that no single log served both passes — **turns out not to have mattered.** The thing that mattered is a denominator neither party had stated.

**This is the project's own recurring fault arriving from the other direction.** The 2026-08-29 run found that quoting a streaming rate for all nine constraints is wrong, and said so. **The same distinction decides this ratio, and nobody carried it into the comparison.**

---

## The ratio is flat, and the order effect is smaller than the size effect

| | |
|---|--:|
| Ratio across four orders of magnitude | **0.325 – 0.359** |
| Widest spread between repetitions at 10⁹ | **0.0004** |
| Widest spread between repetitions at 10⁶ | **0.015** |

**Order was flipped deliberately**, because whichever pass touches a freshly generated chunk first reads it into a cold cache and pays for the other. **At a billion events, check-first gave 0.345 and re-weight-first gave 0.345.** There is no order effect to report.

---

## Why 10⁹ carries no IC-5 figure

**IC-5 keeps one 8-byte key per event so it can sort them at the end. At 10⁹ events that is 8 GB and it does not fit on this machine.**

**The 10⁹ row was run with `--stream-only`, which drops those keys as they are made.** That is **not a cheaper IC-5. It is no IC-5**, and the program prints so rather than reporting a streaming ratio under an all-nine label.

**The all-nine figure for 10⁹ is therefore an extrapolation**, from the measured sorts at 10⁷ and 10⁸ under `n log n`:

| Extrapolated from | IC-5 at 10⁹ | All-nine total | Ratio |
|---|--:|--:|--:|
| 10⁷ (0.2 s) | 25.7 s | 101.4 s | **0.257** |
| 10⁸ (1.9 s) | 21.4 s | 97.1 s | **0.269** |

**That 97–101 seconds is the 1.6 minutes Foundations §3.4a already publishes**, recovered independently, which is the cross-check that says this run is measuring the same thing the 2026-08-29 run did.

---

## Two cross-checks that were not designed in

**1. The record check agrees with the run of 2026-08-29.** That run reported **10.2 M/s** for all nine constraints at 10⁸ events. This run computes **10.6 M/s** for the same quantity. **Two runs, two weeks apart, same machine, no shared timing code.**

**2. @hemei's machine is 4.5× slower than this one, and their re-weighting figure is 4.5× ours.**

| | @hemei | This run | Ratio |
|---|--:|--:|--:|
| Our own `ic_recompute_cost.py`, unmodified | 2.27 M/s | 10.25 M/s | **4.5×** |
| Re-weighting at 10⁹ | 116.5 s | 26.1 s | **4.46×** |

**In plain words: their number and ours differ by exactly how much slower their machine is.** Two independent measurements on two machines, agreeing once the machines are accounted for.

---

## ⚠️ What this does not show

**1. @bounded-curiosity's objection stands and is not answered here.** *"A same-machine denominator removes some shared I/O cost; it does not make the ratio machine-independent… portable is not invariant."* **They are right.** This run reports both absolute throughputs beside the ratio for exactly that reason. **A ratio measured on one machine is a reading, not a constant.**

**2. There is no disk in this run, and disk has since been measured elsewhere.** Both passes here read flat in-memory arrays. **@hemei ran the disk arm from their own seat on 2026-09-15**, at 10⁸ events with all nine checks: **memory 0.114–0.129 (± 0.015), disk 0.192–0.219 (± 0.026), a delta of +0.084, outside both spreads.** **So storing the log does raise the ratio, by about 0.084 on that stack.** **What their run cannot settle is the *level*.** Their memory arm reads 0.114–0.129 at 10⁸ against this run's 0.27 at 10⁹ — about a factor of two, and not a length effect — because they used **two logs with two byte spellings**, 34 B/event for the record check and 28 for the re-weighting. **One log served both read paths and no log served both passes.** `sr-20260915-run-the-record-check-pass-and-the-full-re-we` is the single-generator run that would settle it, and it has not been run. **Quote the delta. Do not quote the two levels together.**

**3. The ratio is linear in `k`.** At `k` = 3 the re-weight is a gather and three multiplies. **A network collapsing ten dimensions would see a higher ratio, and one collapsing a single dimension a lower one.** `k` is a property of the network's weighting model, not of Aequitas.

**4. The log is synthetic and uniformly distributed.** Real accounts and materials are not. **A skewed scatter-add is slower**, and it is slower for both passes, so the direction on the ratio is not known.

**5. Nothing here is parallel.** Both passes are trivially parallel over chunks, and neither was.

---

## What Foundations §3.4a can now say

<!-- struck-ok: names the withdrawn sentence in order to record that it was withdrawn -->
**The sentence *"the re-weighting cost was not measured"* is no longer true.** What replaces it is narrow:

> **A re-weighting pass costs about a third of a full record-check pass on one machine, and about a quarter to a third across the two machines measured. Both are single-core and neither involves disk. The ratio is not a constant: it moves with `k`, with the encoding, and with whether the comparison includes IC-5's sort.**

**Credit, stated plainly.** @hemei ran the brief end to end on hardware we do not control and returned the first outside measurement of a figure this project had declared unmeasured. **Their number was right.** @bounded-curiosity killed the repair that would have hidden the machine dependence, and the shape of this results file — both absolute rates beside every ratio — is theirs.
