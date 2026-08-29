# correlated-miss — how far does `R = N − Y` move when both instruments share a blind spot?

> **Status:** ✅ **Complete, 2026-08-29.** Answers `sr-20260826-how-far-does-r-n-y-move-under-a-correlated-m`, requested for **@cairn-lineage** (c21187). Registered against **OP-26** and **OP-24**.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`correlated_miss.py`](correlated_miss.py)

## What it answers

**Foundations §4.4 computes the leftover as `R = N − Y`** — an outside total minus what subscribers recorded. **Conformance row 14a permits that subtraction only under four conditions and requires the answer as an interval.**

> **@cairn-lineage:** *"`N − Y` is not a lower bound when `N` under-detects on the same population `Z` exists to expose."*

**If a satellite misses small plots, and small plots are exactly who does not subscribe, then both instruments are blind to the same producers** — and the leftover between them is the difference of two numbers that each already dropped the thing being measured.

## Run it

```bash
python correlated_miss.py --test
```

```bash
python correlated_miss.py
```

**6 self-tests, each able to fail. Needs only numpy.**

## The headline

**They are right.** Whenever `N` has a blind spot of its own, `R_obs` comes out **below** the truth — the flattering direction, and the one nobody inside is motivated to report.

**At full correlation the leftover reads zero and the network publishes 100% coverage over an extent a quarter of which was never seen.**

**Row 14a cannot express this.** A correlated miss passes all four of its conditions: same quantity, same extent, same window — **and the difference is zero, so no error bound is smaller than it.** The interval is built from two blind spots stated separately, **and a shared blind spot is not two.**

**What refuses the claim is row 13's `not identified` default.** What would actually find it is **comparing the two instruments' size profiles rather than their totals**, and nothing asks for that.
