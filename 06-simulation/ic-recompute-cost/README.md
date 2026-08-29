# ic-recompute-cost — what does re-running IC-1 to IC-9 cost at scale?

> **Status:** ✅ **Complete, 2026-08-29.** Answers `sr-20260827-wall-clock-recomputation-cost-of-ic-1-ic-9-o`, asked by the drafting council's **Futurist lens**, 2026-08-22.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`ic_recompute_cost.py`](ic_recompute_cost.py)

## What it answers

**Foundations §4.7 and conformance row 16 both rest on a stranger being able to re-compute a network's claims.** The Futurist lens asked the follow-up nobody had measured:

> ***"Any stranger can recompute the verdict" is only decentralizing if any stranger can afford to.***

## Run it

```bash
python ic_recompute_cost.py --test
```

```bash
python ic_recompute_cost.py --full
```

**9 self-tests, each able to fail. Needs only numpy.** `--full` measures a real 10⁸-event pass and takes about 15 seconds.

## The headline

**A 10⁹-event log re-checks in about 1.6 minutes on one core**, at a rate flat across two orders of magnitude. **A stranger can afford it.**

**And the self-tests forced a finding nobody was looking for: IC-5 does not stream.** It is the only constraint that compares one event to **another event** rather than to a running total, so it needs the log **ordered by parcel**. The other eight hold 11.4 MB whatever the log's size.

> **The first version of this program claimed all nine streamed. It was wrong twice before a test capable of falsifying it was written.**

**Read [`RESULTS.md`](RESULTS.md) for the tables, the four things this does not show, and the defects the tests caught.**
