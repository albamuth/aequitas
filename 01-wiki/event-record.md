# Event Record

> The only thing ever written to the Aequitas log: a bounded transformation of the world, described purely as matter and energy moving, with no valuation of any kind.

## The four primitives

| Primitive | What it is |
|---|---|
| **Event** | A transformation. Inputs, outputs, agents, an interval, a place, a process classifier. |
| **Parcel** | A bounded quantity of stuff with an identity and a custody holder. Carries [property-debit](property-debit.md). |
| **Reservoir** | An unowned commons — airshed, watershed, ore body, landfill. Flows into it become permanent [consumption-debit](consumption-debit.md). |
| **Account** | One verified human, or an institution of them. |

## One record shape, no subtypes

Production, transport, transfer, consumption, extraction, and repair are all the *same* record. A transfer is an event whose inputs and outputs are physically identical and differ only in custody. An extraction draws from a reservoir; a consumption releases into one.

**This is the universality criterion enforced at the data layer** — no special cases, no per-activity schemas.

## The rule that makes it work

> No event contains a weight, cost, price, or value. Only physical quantities.

Cost is produced at *projection time* by applying the current weighting model to the log. This is [derived-ledger](derived-ledger.md) stated structurally, and it is why [retroactive-reweighting](retroactive-reweighting.md) is mechanical rather than miraculous: better science changes the model, never the history.

Consequence: **the log is valid independently of any weighting model.** Two communities running different models read identical facts and derive different balances — decentralization holding at the data layer.

## Enforcement by omission

There is no field for price, wage, rate, profit, margin, interest, currency, or balance. Rate-scaled labor is not forbidden — it is **unrepresentable** ([time-as-yardstick](time-as-yardstick.md)). Reintroducing profit requires forking the schema, and a fork is visible to anyone recomputing from the same log.

## Came from, went to

Every flow names an endpoint on **both** sides — a parcel with its own history, or a specific named reservoir. Two constraints make this enforceable in both directions:

- **Origin closure** — every parcel traces back to a reservoir extraction. Nothing materializes from nothing.
- **Fate closure** — every parcel is at all times *held*, *consumed*, or *released to a named sink*. Anything else is **unaccounted**, and the log reports it as a query result rather than dropping it silently.

Backward closure alone lets material vanish, which is precisely how real pollution disappears from real accounts.

## Conservation as an integrity check

Because the log is physical, it admits mass and energy balance constraints that no financial ledger can have.

**If a factory's declared outputs don't mass-balance its declared inputs, the missing mass went somewhere unrecorded — and the log itself says so.** Unrecorded emission becomes an arithmetic error detectable by anyone, with no authority and no inspection. This is the strongest technical argument the project has for [no-externalities](no-externalities.md).

Balance is checked *within* a resolution level — an item cannot be balanced against a facility-month.

## Three axes of detail, not one

Every quantity carries all three, mandatory. They are orthogonal, and collapsing them is the fastest way to make the log dishonest.

| Axis | Question | Values |
|---|---|---|
| **Basis** | How do we know? | `recalled` (word of mouth) · `testified` · `logged` · `instrumented` · `imaged` · `modelled` · `allocated` |
| **Confidence** | How sure? | a probability, **plus the named assessor** who asserts it |
| **Resolution** | About what? | `item` · `batch` · `site_period` · `class_period` · `cohort` |

Word of mouth is a **legitimate basis**, not a defect — it is the rung [verification-ladder](verification-ladder.md) Level 1 actually runs on. Imagery is the only basis that improves *retroactively* without a new observation: old footage can be re-analysed with better tools.

**The rule that matters:** precision at the aggregate does not transfer to the individual. A perfectly metered facility-month divided by 400,000 units is a strong aggregate claim and a weak per-unit one, and allocating downward must lower confidence.

Records improve by **supersession**, never edit — and only ever toward stronger basis and finer resolution, so nobody can bury a measurement under a flattering estimate.

## Joint outputs need no field

An event may have several outputs — milling yields flour *and* bran — and the schema **records them faithfully without saying how the debit divides.** That split is computed at projection time from the event's process classifier plus published process energetics ([co-product-allocation](co-product-allocation.md)).

**There is no field for an allocation fraction, and that is a guarantee rather than an omission.** Someone wanting to assert a self-serving split has nowhere to put it; they would have to publish a process model, in public, subject to [rival-sector-audit](rival-sector-audit.md). **The strongest kind of protection this schema offers is the one where the exploit has no field to live in.**

The schema absorbed the project's most dangerous open problem **without a single field being added**, which is the best evidence yet that C1 was right.

## Integrity constraints

**IC-1…IC-9 check the log** and are pure arithmetic — mass and energy balance, origin and fate closure, custody continuity, interval sanity, the 24-hours-per-24-hours cap, and pledge backing. No trust model, no authority, no inspection.

**IC-10…IC-12 check a *projection*** — the first constraints in the spec that do:

- **IC-10** — no allocated share is negative. *(Asserted, not proven for the recursive case; this is where Sraffa could re-enter.)*
- **IC-11** — per dimension, allocated shares sum to the recorded input total.
- **IC-12** — allocating a process stage-by-stage equals allocating it whole. **The defence against boundary gerrymandering.**

## Open

- **Confidence propagation** along the parcel DAG — asserted as "weakest link governs," arithmetic unspecified. Must now also cover allocated shares.
- **Conservative weighting of vague records** — now load-bearing four times over. Without it, staying coarse is free.
- Retracting a faulty measurement, given supersession may not move to a weaker basis
- **Labour allocation across co-products** — OP-18, and **it now blocks the [estimation-engine](estimation-engine.md)**
- **Process-energetics model registry** — the published data splits are computed from
- Substance, process, role, and reservoir taxonomies. *The **process** taxonomy is the underrated one: it keys retroactive hazard injection* and *the allocation model.*
- ~~Amortization denominator for training cost~~ — **resolved:** training does not flow downstream, so there is no denominator
- ~~Custody acceptance semantics~~ — **settled: possession decides.** No refusal right; the physical act of taking the thing is the consent step

---
*Status: provisional*
*Source: `00-strategy/Aequitas_EventLog_v0.3.md` (C1 v0.3)*
