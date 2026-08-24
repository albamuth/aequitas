# Residual unravelling — does staying dark stop paying?

> **Status:** ✅ Built and green, 8 self-tests. **Passes**, with one measured limit and three stated assumptions.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Full write-up:** [`UNRAVELLING.md`](UNRAVELLING.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

## The question

Someone who does not measure their own production gets a cohort estimate instead. Foundations §5.1b says that estimate must be computed over **the unmeasured residual** — the people still undisclosed — and never over the whole population.

That rule was folded in on the strength of an argument, with no arithmetic behind it. This project supplies the arithmetic.

**The claim being tested:** as good producers instrument themselves and leave the dark pool, the estimate applied to whoever is left gets *worse*. So the pull to leave strengthens over time and darkness stops paying.

**The same rule one level down** applies to periods within a single life (Foundations §5.1d, condition 1). Someone who documents only their flattering years should not free-ride forever on an average their own silence inflates. **It is one mechanism at two scales, so one model serves both** — read "agent" as a producer at the first scale and as a life-period at the second.

## Run it

```bash
python residual_unravelling.py            # the full run and its report
python residual_unravelling.py --test     # self-tests only
```

Pure Python — no `numpy`, no data files, nothing to download.

## What is in here

| Path | What it is |
|---|---|
| [`residual_unravelling.py`](residual_unravelling.py) | The model. Two claims, eight self-tests, and a control run using the rule §5.1b rejects. |
| [`UNRAVELLING.md`](UNRAVELLING.md) | The write-up. **New readers should start at §0**, a five-farm example small enough to check by hand. |

## Checkable without running it

**The entire 2,000-agent fixture is published as data** — every true debit, every disclosure cost — in [`../audits/audits_inert/residual_unravelling.json`](../audits/audits_inert/residual_unravelling.json), with the arithmetic in [`../audits/audits_inert/bonus_sims.md`](../audits/audits_inert/bonus_sims.md).

**The five-farm example in §0 has no random numbers in it at all.** A reader can redo every round on paper.

## What this bears on

The verification-cost limit found here (see [`RESULTS.md`](RESULTS.md)) is the measured precondition behind the coverage argument in Foundations §5.1b and §5.1c, and it feeds directly into OP-22 (minimum audit disclosure) and the trust-network work in `00-strategy/C2_TrustNetworks_v0.1.md`.
