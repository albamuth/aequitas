# SB-03 — What does a full re-weighting of a billion-event log actually cost?

> **Version:** 0.1
> **Date:** 2026-09-16

> **Request:** `sr-20260901-wall-clock-and-memory-cost-of-a-full-re-weig` · filed 2026-09-01.
> **Status:** open. **Nobody has run this.** **This is the most reproducible brief here** — it needs no theory, only a machine.
> **Read the format first:** [`README.md`](README.md), especially section 7.

---

## 1. The question

> **Measure the wall-clock time and peak memory of a full re-weighting pass over synthetic event logs of 10⁶, 10⁸ and 10⁹ events — reading every event, collapsing its physical vector through a weighting model, and aggregating per account.**

**This is a different pass from the one already measured.** The published **1.6 minutes at 10⁹ events** covers the **nine record checks** — arithmetic over the log itself. **It does not cover re-weighting**, and we have said so in public.

## 2. What depends on it

**Foundations §2.1** claims decentralization: *"Can a stranger check a claim without asking anybody's permission?"* **A cost nobody can afford is a permission in disguise.**

**Foundations A6** says a position is **never stored** and is **computed from the log whenever anyone asks**. **§3.3** says that when the science improves, **every affected ledger in history recalculates** — and calls recomputation *"not a repair, it is how the system normally runs."*

> **That sentence is a performance claim and it has never been measured.**

**And the honest position we already hold in public:** post 3397 publishes the 1.6-minute figure **and says the re-weighting pass is unmeasured and must not be quoted from it.** Somebody will ask. **We would rather hand them a number than a caveat.**

## 3. Terms

| Term | What it means |
|---|---|
| **Event** | One append-only record: who, when, and **a vector of physical quantities** — kilograms of a substance, joules, labour-hours, cubic metres, land-area-years |
| **Weighting model** | The table saying what one unit of each physical dimension costs in hours. **Each network runs its own** |
| **Collapse** | Turning one event's physical vector into a single comparable figure, by applying the weighting model. **It happens when somebody asks, never in storage** (§3.2a) |
| **Re-weighting pass** | **Collapse every event in the log, then aggregate by account.** This is the thing being measured |
| **The record checks** | The nine arithmetic integrity checks over the log. **Already measured: 1.6 min at 10⁹.** Not this |

## 4. The model

**The pass is three steps, and step 2 is the whole cost.**

1. **Read** the log, event by event.
2. **Collapse:** for each event, compute `h(e) = Σ_d q(e, d) · w(d)` — the dot product of the event's physical vector `q` with the weighting model `w`, over dimensions `d`.
3. **Aggregate:** add `h(e)` to the debit or credit total of the account the event names.

**So the arithmetic per event is one dot product over `k` dimensions, and one addition.**

### A worked example, with the numbers

**Take `k` = 6 dimensions and 10⁹ events.**

| | |
|---|--:|
| Multiply-adds per event | 6 |
| Total multiply-adds | **6 × 10⁹** |
| Aggregation additions | **10⁹** |
| **Total floating-point operations** | **≈ 7 × 10⁹** |

**In plain words: about seven billion arithmetic operations.** A single modern core does on the order of 10⁹ of those a second in a scripting language and far more in a compiled one, **so the arithmetic is not the cost. Reading 10⁹ events off a disk is.**

> **That is the actual question. Report which one binds on your machine, and say which it was.**

**Two variants worth separating, and the difference is the whole engineering story:**

| Variant | What it does |
|---|---|
| **Cold** | Read the log from disk, collapse, aggregate. Nothing cached |
| **Streaming** | Never hold more than one chunk in memory. **Peak memory should be roughly the account table, not the log** |

## 5. Inputs

**A generator, not real data.** State:

- **`k`**, the number of physical dimensions per event (we suggest 6; report what you used).
- **The account count** — the aggregation table's size. We suggest 10⁶.
- **The event encoding** and its bytes-per-event on disk. **Report this; it dominates the cold number.**
- **Your seed.**
- **Your machine:** cores used, RAM, and whether storage is a spinning disk, a SATA SSD, or NVMe. **A result without the storage type is not comparable.**

**The existing run to compare against:** `06-simulation/ic-recompute-cost/`. **It measured a different pass.** Use it for the log format and the machine baseline, not for the answer.

## 6. What an answer looks like

| Events | Variant | Wall-clock | Peak memory | Bytes read | What bound it |
|--:|---|--:|--:|--:|---|
| 10⁶ | cold | | | | I/O / CPU |
| 10⁸ | cold | | | | |
| 10⁹ | cold | | | | |
| 10⁹ | streaming | | | | |

**Plus one line: does wall-clock scale linearly from 10⁶ to 10⁹?** If it does not, say where it breaks.

## 7. Declared in advance

| | |
|---|---|
| **Our prior** | **A full re-weighting is between 1× and 5× the record-check pass**, so **roughly 1.6 to 8 minutes at 10⁹ events on one ordinary core**, and **I/O-bound rather than CPU-bound**. Peak memory under the streaming variant should be **the account table, not the log** |
| **Refutation threshold** | **If a 10⁹-event re-weighting takes more than one hour on one ordinary core, or if peak memory exceeds available RAM under the streaming variant, then "recomputation is how the system normally runs" is false as written** |
| **What we do if it is crossed** | **§3.3's claim is qualified with a measured cost, and §2.1's decentralization claim is qualified with it too.** A stranger who cannot afford the check has not been given one. **We would also have to say what an implementation may cache**, which A6 currently forbids outright |

**We are not confident in this prior.** The 1.6-minute figure is ours and it is the only anchor we have, and **§4.4's rule about a check that compares a thing to itself applies to a benchmark as much as to a ledger.**

## 8. Self-tests, each able to fail

1. **A weighting model of all ones makes the collapsed total equal the raw physical sum.** If it does not, the dot product is wrong.
2. **Doubling every weight doubles every account's figure.** Linearity.
3. **Wall-clock at 10⁸ is within ±30% of ten times wall-clock at 10⁷.** If not, something is caching that should not be.
4. **Peak memory under the streaming variant does not grow between 10⁸ and 10⁹.** If it does, it is not streaming.
5. **Running the same log twice gives the same account totals.** Determinism.

## 9. Out of scope

- **The cost of *obtaining* the log.** At 10⁹ events that is a transfer problem, and Foundations §2.6 puts it with the implementer. **`ic-recompute-cost` already says this: cheap to check is not the same as cheap to obtain.**
- **Whether the weighting model is right.** That is OP-24 and §3.3a.
- **Distributed or GPU execution.** **The claim is that one stranger on one ordinary machine can do it.** A cluster result does not answer it.

## 10. Known ways to get this wrong

- **Measuring warm cache and reporting it as cold.** Drop caches between runs, or say you did not.
- **Reporting only the arithmetic.** Section 4 shows the arithmetic is roughly seven billion operations, which is minutes at worst. **The interesting number is I/O.**
- **Using a compiled implementation and comparing it to our scripted one.** Report the language. **Both numbers are useful; conflating them is not.**
