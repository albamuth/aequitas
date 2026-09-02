# Retroactive Re-weighting

> When science improves, every affected ledger in history recalculates. Events are permanent; their *weight* floats with the current cost of mitigation.

## What it is

The engine of fecundity. Because balances are derived and not stored ([derived-ledger](derived-ledger.md)), improving a measurement improves all history that depended on it — automatically, with no edit to any event.

Two directions:

- **Weight falls.** If atmospheric CO₂ capture gets cheaper per tonne, everyone's past fossil-fuel consumption weighs *less* — because undoing it now costs less time and energy than it used to.
- **Weight rises.** A newly discovered long-term health harm from a manufacturing process retroactively adds debit to the products made by it, trickling down to their current holders.

**A third direction, added with [co-product-allocation](co-product-allocation.md): splits re-split.** Better process science does not only change what a flow weighs — it changes *how a joint process's debit divides across its outputs*, backwards through all history. So the general guarantee is stronger than "weights float": **no inaccuracy in this system is irreversible.** A conservative early estimate is never a permanent verdict on anyone.

## Why it works this way

**It makes better measurement of reality permanently profitable.** No other component of Aequitas creates a standing, self-renewing demand for science.

It is also what makes [no-externalities](no-externalities.md) an honest claim rather than a boast. A4 doesn't assert we've measured everything; it asserts that anything later measured propagates backwards.

### Why mitigation cost, and not the harm's worth

**A pollutant's weight is the work of putting the world back — removing the substance, and repairing what it did while it sat there.** Not what the harm was worth to whoever suffered it, and not a market carbon price.

**Only one of the three is readable here.** A harm's worth is a value, and Aequitas measures cost and never value. A carbon price is a price, and [cost-not-price](cost-not-price.md) leaves none in the system. **What removing a tonne takes is a measurement, and anyone with the same equipment computes the same figure.** This is the [physical-trace-test](physical-trace-test.md) applied to a pollutant: a tonne in the air left a trace, and a sense of loss did not.

**The honest limit: the repair half is a far weaker reading than the removal half, and it is the larger of the two.** Both are cost constants, both are governed by [rival-sector-audit](rival-sector-audit.md) and the requirements above, and both inherit OP-24. Full statement: Foundations §2.2.

## Who games this

The obvious exploit: **capture the weighting model.** If one body decides what a tonne of CO₂ costs to remediate, that body silently controls every balance in the world. **This is the single largest centralization risk in Aequitas (OP-10) and it is not solved.** Candidate defences — competing weighting models under open variance (A8), forced publication of methodology, recomputation by any party from the same log — are asserted and still unspecified.

**Three partial answers now exist, all from the OP-17 work:**

1. **[rival-sector-audit](rival-sector-audit.md)** disciplines cost *constants*: if a constant understates a sector's debit, the rival sector is materially harmed and will fund the replication. Consumers police neither direction; rivals police both. Plus **two unaffiliated replications before a constant may re-weight history** — retroactivity is too powerful to trigger from one source.
2. **Splits happen per-dimension, before collapsing.** A debit is a vector of physical quantities collapsed to one comparable number only on demand. Any division is computed on the vector, so the split is **weighting-independent** — two communities with different models compute the *same* split. Had divisions been computed on the collapsed scalar, the model maintainer would have controlled every allocation in history invisibly.
3. **"Does this need an objective function?"** is a fast screen — see [physical-trace-test](physical-trace-test.md). Every mechanism requiring one hands someone this lever.

## Depends on

- [derived-ledger](derived-ledger.md)
- [no-externalities](no-externalities.md)
- [consumption-debit](consumption-debit.md) — the term whose weight floats

## Consequences

- [regulator-inversion](regulator-inversion.md) — helping firms lower debit-cost becomes a service they want
- [time-as-yardstick](time-as-yardstick.md) — the route by which hazardous labor gets priced
- [co-product-allocation](co-product-allocation.md) — splits re-split as process science improves
- [rival-sector-audit](rival-sector-audit.md) — what keeps the constants honest

## Open questions

- **C4 — re-weighting mechanism + feasibility at scale.** Recomputing all history on every model update is not obviously tractable — **and the co-product split makes it worse**, since the allocation is defined recursively.
- **OP-10 — governance of the weighting model.** Still the largest hole in [protocol-governance](protocol-governance.md).
- **OP-24 — understatement drift.** Errors favouring subscribers have no funder. Rival-sector audit is proposed, unproven.

## Prior art

- Social cost of carbon / mitigation cost curves — the closest existing analogue, and a live example of exactly the capture problem above
- Issuer-pays credit rating and audit independence — the historical record on why "competition produces accuracy" does not hold when the rated party pays. `../00-strategy/GLOSSARY.md#src-auditor-independence`

---
*Status: settled (principle) / contested (governance of the model)*
*Source: `00-strategy/Aequitas_Foundations_v0.4.md` §3.3, §3.3a*
