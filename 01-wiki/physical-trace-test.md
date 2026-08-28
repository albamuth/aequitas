# The Physical-Trace Test

> **Did the thing being divided leave a physical trace?**
> **Trace → measure it. No trace → declare a convention and say so.**

## What it is

A screening question applied to every division problem in Aequitas. It came out of resolving [co-product-allocation](co-product-allocation.md) and it is the most transferable result that work produced.

The project's recurring difficulty has never been measuring totals. A refinery consumed *X* joules; a team of nine built the bridge. **Totals are physically well-defined. Splits are where every predecessor system died** — Warren's storefront, Sraffa's negative values, ISO 14044's fallback to price.

The register's earlier headline was *"the hard problem is division, not measurement."* **That was too broad**, and the trace test is what narrows it:

| Being divided | Trace? | Treatment |
|---|---|---|
| A refinery's cracking energy across fractions | ✅ The energy physically went somewhere; a meter finds it | **Measure** |
| A steer's feed energy across tissues | ✅ Metabolism deposited it; calorimetry finds it | **Measure** |
| A turbine's fuel across heat and power | ✅ The extraction curve is metered | **Measure** |
| A farmer's hours across hide and beef | ❌ The hours were spent on the animal | **Declare a convention** |
| A barn across the animals it shelters | ❌ Shelter does not decompose | **Declare a convention** |
| Responsibility for a bridge across nine builders | ❌ [Ellerman](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf): joint responsibility is non-decomposable | **Declare a convention** |

## Why it matters

**It tells you which of two completely different kinds of work you are facing**, and the two are easy to confuse.

- **Where there is a trace**, refining converges. Better instruments get closer to a real number, [retroactive-reweighting](retroactive-reweighting.md) propagates the improvement backwards, and the answer improves forever. Treating this as a convention would be *dishonest in the other direction* — it would hide a measurable fact behind a chosen rule.
- **Where there is no trace**, refining converges on nothing. No instrument will ever help, because there is nothing to instrument. The only honest move is to name the convention in the axioms and defend the choice openly.

> **A convention that is declared is not an ad-hoc rule. A convention that is disguised as a measurement is.**

Half the project's history of thrashing on division problems was **applying the wrong one of these two treatments.** Foundations v0.3 declared co-product allocation a convention; v0.4 deleted that row because the trace was there all along and nobody had looked for it.

## The residue is small and sharply defined

Applying the test leaves exactly three genuinely indivisible things, and they are the same thing at three scales:

1. **Labour across co-products** (OP-18)
2. **Shared overhead across co-products** (OP-23)
3. **Responsibility across a team** (OP-18 again)

**All three are human-attribution problems.** None is a physics problem. That is a much narrower and more defensible place for a theory of material cost to have its irreducible conventions than "division in general."

## A companion question

Applied alongside the other screening questions, and earned the same way:

> **Does this need an objective function?**

Both allocation rules rejected for [co-product-allocation](co-product-allocation.md) — Aumann–Shapley marginal allocation and Kantorovich shadow prices — required one, and **whoever sets an objective function sets every number that derives from it.** It is a fast proxy for *"does this create a capture surface?"*, and it is why the adopted rule leaves [protocol-governance](protocol-governance.md)'s largest hole no wider than it found it.

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md)

## Consequences

- [co-product-allocation](co-product-allocation.md) — the case that produced the test
- [protocol-governance](protocol-governance.md) — declared conventions are auditable; disguised ones are capture surfaces

## Open questions

- Does the test itself have edge cases — a trace that exists in principle but is unmeasurable in practice? *Probably resolved by resolution and confidence rather than by the test, but unverified.*

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations_v0.4.md` §2.5, §3.4; `Aequitas_Objections_v0.5.md` §0*
