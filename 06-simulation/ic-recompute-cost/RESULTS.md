# IC recomputation cost — results

> **Run: 2026-08-29.** Answers `sr-20260827-wall-clock-recomputation-cost-of-ic-1-ic-9-o`, asked by the drafting council's **Futurist lens** on 2026-08-22.
> **Code:** [`ic_recompute_cost.py`](ic_recompute_cost.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **9 self-tests, each able to fail. All pass.**

---

## The question

> *"The demonstration is 13 events, 6 parcels, 6 accounts. **'Any stranger can recompute the verdict' is only decentralizing if any stranger can afford to.** Cockshott and Cottrell are cited for feasibility but no timing has been measured in this project."*

## The answer

> **A stranger can afford it. A 10⁹-event log re-checks in about 1.6 minutes on one core of an ordinary machine.**

---

## Measured

**1,000,000 accounts · 64 materials · single core · no parallelism · no indexing.**

| Events | 8 streaming checks | IC-5 sort | All nine | Rate |
|---|---|---|---|---|
| 1,000,000 | 0.1 s | 0.0 s | **0.1 s** | 9.9 M/s |
| 10,000,000 | 0.8 s | 0.2 s | **1.0 s** | 10.4 M/s |
| **100,000,000** | **7.9 s** | **1.9 s** | **9.8 s** | **10.2 M/s** |

**The rate is flat across two orders of magnitude.** Extrapolated at the fastest measured rate:

| Events | Time to re-check the whole log |
|---|---|
| 10⁸ | 9.7 s |
| **10⁹** | **1.6 min** |
| 10¹⁰ | 16.1 min |

---

## 🔴 The finding the self-tests forced: IC-5 does not stream

**Eight of the nine constraints are running accumulators.** Their memory is a property of the **account count**, never of the log.

| Accounts | State held by the eight |
|---|---|
| 10,000 | 117.7 KB |
| **1,000,000** | **11.4 MB** |
| 100,000,000 | 1.1 GB |

**IC-5 is the exception, and it is the interesting half of the answer.**

> **IC-5 is the only constraint that compares one event to *another event* rather than to a running total.** One parcel, one holder, one day. **So it needs the log ordered by parcel** — an external sort, or an index kept as the log is written.

| Events | IC-5 memory, keeping the pairs |
|---|---|
| 1,000,000 | 7.6 MB |
| 100,000,000 | 762.9 MB |
| 10⁹ | **7.5 GB** |

**A real network does not do it this way.** It keeps the log indexed by parcel as it is written, which turns IC-5 back into a scan. **That is an implementation choice and conformance §3 leaves it there.** What is **not** optional is that **IC-5 needs an ordering the other eight do not.**

---

## What this does not show

**1. The expensive half is not here.** IC-1 to IC-9 check the **record**. They apply no weighting model. **Foundations §3.3 says a better constant re-weighs every affected record in history**, and that pass reads the same log and multiplies through a model. **Its cost is not measured here, and nobody should quote this figure for it.**

**2. It does not show the cost of *getting* the log.** A stranger must obtain it first. At 10⁹ events that is a transfer problem, and conformance §3 puts it with the implementer. **Cheap to check is not the same as cheap to obtain.**

**3. IC-10 to IC-12 are excluded deliberately.** They check a figure computed **through** a weighting model, so their cost belongs to the model rather than to the log.

**4. Synthetic data, one machine, one core.** These are an **upper bound** on cost, not an estimate of what an implementation would achieve.

---

## Three defects the self-tests caught

**Test 4 failed three times before it passed, and each failure was real.**

| What failed | What it was |
|---|---|
| **The test could never have passed** | It drew each chunk from a shared generator, so two chunkings consumed the stream differently and produced **different data**. It was comparing two logs and calling the difference a chunking bug |
| **IC-5 missed clashes at chunk boundaries** | A within-chunk sort forgets everything at the edge. Carrying the last day each parcel was seen fixed the adjacent case |
| **And the carry was still wrong** | A parcel on days 3 and 7 in one chunk, then day 3 again in the next: only day 7 was kept. **That is when IC-5's real property became clear — it does not stream at all** |

**A fourth, in the timing rather than the model:** the headline rate excluded IC-5 entirely, because `verdict()` was never called inside the timing loop. **The figure was for eight checks and was labelled nine.**

> **The first version reported "all nine constraints stream, memory is flat" and it was wrong.** The claim survived two fixes before a test capable of falsifying it was written.
