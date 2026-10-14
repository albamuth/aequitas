---
title: Physical-trace test
summary: Before dividing a cost, ask whether the thing divided left a physical trace; measure it if so, declare a convention and say so if not, and refuse to divide where nothing was divided in the world.
type: mechanism
ids: [§2.5, §3.4]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: time-as-yardstick}
  - {rel: implies, to: co-product-allocation}
  - {rel: implies, to: property-debit}
  - {rel: implies, to: debit-tolerance}
  - {rel: implies, to: protocol-governance}
  - {rel: source, to: "Foundations §2.5"}
  - {rel: source, to: "Foundations §3.4"}
  - {rel: source, to: "Objections §0"}
---
# The Physical-Trace Test

> **Version:** 0.1
> **Date:** 2026-09-16

> **Did the thing being divided leave a physical trace?**
> **Trace → measure it. No trace → declare a convention and say so. Or refuse to divide, where nothing was divided in the world.**

## What it is

A screening question applied to every division problem in Aequitas. It came out of resolving [co-product-allocation](co-product-allocation.md) and it is the most transferable result that work produced.

The project's recurring difficulty has never been measuring totals. A refinery consumed *X* joules; a team of nine built the bridge. **Totals are physically well-defined. Splits are where every predecessor system died** — Warren's storefront, Sraffa's negative values, ISO 14044's fallback to price.

**The test has three answers, and the third should be tried first** (Foundations §2.5).

| Answer | When | What you do |
|---|---|---|
| **Measure** | The thing divided left a physical trace: a meter, a scale, a clock | Read the instrument. Better instruments improve the figure forever |
| **Declare a convention** | A division is genuinely required and nothing in the world performed it | Name the rule in the documents and say it is a convention |
| **Refuse to divide** | Nothing was divided in the world | Divide nothing in the books either. **Not a third kind of convention, because nothing is chosen** |

**What this system divides, and how**, from Foundations §2.5:

| Being divided | Answer | The rule |
|---|---|---|
| A team's credit across its members | **Dissolves** | Each member is credited their own hours. Credit was never a share of the output |
| One process's cost across its several outputs | **Refused** | The energy was spent entirely on both outputs. Every co-product carries the whole process cost against its own mass ([co-product-allocation](co-product-allocation.md)) |
| One parcel of one substance, split into parts | **Measure** | Mass is a physical trace, so the split is by mass, per dimension ([debit-vector](debit-vector.md)) |
| An organisation's debit across its members | **Convention, on a measurable basis** | Hours worked, already recorded and already capped by IC-7 ([organisation-debit](organisation-debit.md)) |
| The hours a floor activity counts for | **Convention, on a measurable basis** | Proof of life is the trace; the duration per activity is published ([debit-tolerance](debit-tolerance.md)) |
| A durable asset's creation cost across its holders | **Convention, on a measurable basis** | Holding time is a trace, so the share is holding time ÷ total holding time ([front-loading-rule](front-loading-rule.md)) |
| Shared overhead across outputs | **Nothing to split** | All capital accrues to the asset, never to the outputs ([property-debit](property-debit.md)) |

## Why it matters

**It tells you which of three different kinds of work you are facing**, and they are easy to confuse.

- **Where there is a trace**, refining converges. Better instruments get closer to a real number, [retroactive-reweighting](retroactive-reweighting.md) propagates the improvement backwards, and the answer improves forever. Treating this as a convention would be *dishonest in the other direction* — it would hide a measurable fact behind a chosen rule.
- **Where there is no trace and a division is required**, refining converges on nothing. No instrument will ever help. The only honest move is to name the convention and defend the choice openly.
- **Where nothing was divided**, a convention is what you declare to avoid noticing that none is needed. The joint-production case is this: Foundations once declared a convention for it, then measured 36 honest methods 6.31× apart, then withdrew the division altogether.

> **A convention that is declared is not an ad-hoc rule. A convention that is disguised as a measurement is.**

### An example, with the numbers

**A farmer spends 8 hours on one steer, which yields 250 kg of beef and 40 kg of hide.** The 8 hours left no trace saying which output they went to, and they did not need to: they were spent on the whole animal.

| Output | Mass | Hours it carries per kg |
|---|--:|--:|
| Beef | 250 kg | 8 ÷ 250 = **0.032 h/kg** |
| Hide | 40 kg | 8 ÷ 40 = **0.200 h/kg** |

**The farmer is credited 8 hours either way.** The test decided only what each output's figure reads, never anybody's credit.

## The residue is small and sharply defined

Applying the test leaves the declared conventions in the table above, and they share one shape: **each is a human-attribution problem with a measurable basis** (hours, holding time, proof of life). None is a physics problem. That is a narrower and more defensible place for a theory of material cost to keep its conventions than "division in general."

## A companion question

Applied alongside the other screening questions, and earned the same way:

> **Does this need an objective function?**

Both allocation rules rejected for [co-product-allocation](co-product-allocation.md) — Aumann–Shapley marginal allocation and Kantorovich shadow prices — required one, and **whoever sets an objective function sets every number that derives from it.** It is a fast proxy for *"does this create a capture surface?"*, and it is why the adopted rule leaves [protocol-governance](protocol-governance.md)'s largest hole no wider than it found it.

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md)

## Consequences

- [co-product-allocation](co-product-allocation.md) — the case that produced the test, and the first case of *refuse to divide*
- [organisation-debit](organisation-debit.md) · [front-loading-rule](front-loading-rule.md) · [debit-tolerance](debit-tolerance.md) — the three declared conventions
- [protocol-governance](protocol-governance.md) — declared conventions are auditable; disguised ones are capture surfaces

## Open questions

- Does the test itself have edge cases — a trace that exists in principle but is unmeasurable in practice? *Probably resolved by resolution and confidence rather than by the test, but unverified.*

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §2.5 (measurement and convention; what this system divides), §3.4 (resolution is opportunistic); `Aequitas_Objections.md` §0*
