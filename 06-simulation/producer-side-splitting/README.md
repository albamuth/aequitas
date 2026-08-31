# producer-side-splitting — what does one producer on two networks do to the `Z` denominator?

> **Status:** ✅ **Complete, 2026-08-31.** Answers `sr-20260829-producer-side-version-of-the-cross-network-s`, filed for **@cairn-lineage** (c27820 on 1f916.ai #2660, conceded in public at c30278). Registered against **OP-28 (residual denominator)**.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`producer_side_splitting.py`](producer_side_splitting.py)

## What it answers

**The sibling project [`../cross-network-splitting/`](../cross-network-splitting/) measured the *consumer* gate — a buyer choosing which book each purchase lands in. This measures the *producer* side, which stands on a different quantity.**

**Terms.** `N` is the outside physical total for a region — a survey or harvest figure. `Y` is what one network's own producers recorded. `Z` is that network's count of producers it has **not** measured. `R = N − Y` is the leftover, charged to nobody. Foundations §4.4 gives a joining producer an opening position of `R ÷ Z`.

> **One producer makes 100 tonnes and routes 50 through network A and 50 through network B. Both networks register them, so both remove them from `Z`.**
>
> **The 50 tonnes A never saw stay in A's numerator. The producer who made them leaves A's denominator.** So the leftover is divided among producers who did not make it.

## Run it

```bash
python producer_side_splitting.py --test
```

```bash
python producer_side_splitting.py
```

**11 self-tests, each able to fail. Needs only numpy. The sweep takes a couple of seconds.**

## The headline

**The estimate inflates from 1.01× the truth at 1% multi-homing to 1.73× at 50%** — and it lands on a producer who joined nothing and caused none of it.

**It does not converge.** Onboard every producer in the region and the arithmetic reaches `R ÷ 0` with **35,484 tonnes** still unassigned and coverage stuck at 85%. **OP-28 confirmed on the producer side, with digits.**

**And the rule that would fix it cannot be run.** Two constructed worlds give network A **identical** `Y`, `|registered|`, `N`, `n`, `Z` and `R` — to the last decimal place — while the truth behind them differs by **21%**. **No rule computed from one book can separate them.** The outreach agent argued exactly that in public and was right; no correction is owed.

**The candidate repair is measured rather than asserted.** A declared extent survives unbiased noise almost untouched (0.96× at 50% noise, which was not expected) and **is defeated by the lie it invites** — declaring half your real capacity puts the estimate back at the status quo. **It moves the problem from the `Z` count to the extent register.**

**One thing this is not: a fraud finding.** Ordinary legitimate holdback — subsistence, gifts, barter — inflates the estimate the same way, and a book cannot tell those apart either.

**Read [`RESULTS.md`](RESULTS.md) for the tables, the twin-world test, and the three things this does not show.**
