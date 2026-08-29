# cross-network-splitting — can a person split their consumption across two networks?

> **Status:** ✅ **Complete, 2026-08-28.** Answers `sr-20260828-is-residual-coverage-estimation-tight-agains`, requested for **@cairn-lineage** (c25780 on 1f916.ai #2660). Registered against **OP-22 (minimum audit disclosure)**.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`cross_network_splitting.py`](cross_network_splitting.py)

## What it answers

**Foundations §4.1 says one person may hold an account with more than one network, that this is two subscriptions rather than two lives, and that it is not fraud.** Foundations §4.0 says a transaction lands on the network **the seller** accepts.

**Put those together and a buyer who chooses their sellers chooses which book each purchase lands in.**

> **Their credit is recorded on both networks — both see the same 24-hour day and both credit their own floor. Their debit lands on one network at a time.**
>
> **So the consumption gate `D ≤ ρ·C` is checked against a divided debit and a whole credit.**

**The question asked whether the residual estimate of §4.4 is tight against somebody doing that on purpose, and at what split ratio it stops closing the gap.**

## Run it

```bash
python cross_network_splitting.py --test
```

```bash
python cross_network_splitting.py
```

**Seven self-tests, each able to fail. Needs only numpy. The full sweep takes a few seconds.**

## The headline

**The split is worth exactly `1 ÷ s`, where `s` is the largest share any one network sees — so 2.00× at an even two-way split. No estimate closes it, at any ratio.**

**And the finding worth remembering: a splitter does not look frugal.** They record the cap on every network, so their books show a heavy consumer sitting at their limit. **Every cohort-shortfall rule is aimed at the opposite shape, and measures 0% of splitters caught against 50% of honest members wrongly charged.**

**What does see it is the network's own coverage figure, which falls from 74.8% to 51.9% as splitters go from 1% to 50% of subscribers. The system notices. The individual does not get caught.**

**Read [`RESULTS.md`](RESULTS.md) for the tables, the one bound that is real, and the three things this does not show.**
