---
title: Debit is a vector
summary: A debit is stored as a bundle of physical quantities, never as one number; it is collapsed into hours only when somebody asks, and any division of a debit happens on each quantity separately, before collapsing, so the split never depends on the weighting model.
type: mechanism
ids: [§3.2a]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: non-fungibility}
  - {rel: depends_on, to: derived-ledger}
  - {rel: implies, to: retroactive-reweighting}
  - {rel: implies, to: co-product-allocation}
  - {rel: implies, to: pollution-making-vs-using}
  - {rel: implies, to: organisation-debit}
  - {rel: constrained_by, to: "Conformance row 5"}
  - {rel: constrained_by, to: "Conformance row 10"}
  - {rel: constrained_by, to: "Conformance row 10f"}
  - {rel: open_under, to: OP-10}
  - {rel: tested_by, to: 06-simulation/ic-recompute-cost/KSWEEP_RESULTS.md}
  - {rel: source, to: "Foundations §2.2"}
  - {rel: source, to: "Foundations §3.2a"}
  - {rel: source, to: "Foundations §3.4a"}
---
# Debit is a vector

> **Version:** 0.1
> **Date:** 2026-10-14

> **A debit is not one number.** It is a bundle of physical quantities, stored separately in the log, and turned into a single comparable figure only when somebody needs to compare two things. **Any division of a debit happens on each quantity separately, before that figure is produced.**

## The words this page uses

| Term | What it means |
|---|---|
| **Debit** | A record that matter or energy was taken from the world, and who holds the consequence ([debit-taxonomy](debit-taxonomy.md)). |
| **Weighting model** | The set of numbers that says what a kilogram of a substance, a joule, or a tonne of CO₂ costs in hours. Each trust network runs its own. |
| **Collapse** | Applying a weighting model to a debit's quantities to get one figure in hours. It happens when somebody asks, never in storage. |
| **Parcel** | One delivery or one holding of one substance, with one record ([co-product-allocation](co-product-allocation.md)). |

## The rule

**The log stores kilograms of each substance, joules, labour-hours, cubic metres of water and land-area-years, each as its own line.** Nobody stores "4.62 hours". A reader who wants hours applies the weighting model in force on the day they ask (A6, [derived-ledger](derived-ledger.md)).

> **Any division of a debit, across co-products, across a team, across holders, is computed on the vector, per dimension, before collapsing.**

**Why that order matters.** Divide the collapsed number instead and whoever maintains the weighting model controls every allocation in history without anyone seeing it happen. Divide per dimension and the split does not depend on the weighting at all. **Two networks running different weighting models compute the same split and disagree only about what it weighs.** That closes one route into OP-10 (weighting governance).

**The physical record is what implementations must agree on. The collapse is what they may differ about.** This is A3 and A6 working together.

## An example, with the numbers

**A tank holds a 100 kg parcel of gas carrying 212 MJ.** Somebody draws off 10 kg with a pump that consumes 3 MJ. *(Digits from Foundations §3.4a; the hour rates are illustrative.)*

| | Mass | Energy |
|---|--:|--:|
| The parent parcel | 100 kg | 212 MJ |
| The 10 kg child, divided by mass on each line | 10 kg | 21.2 MJ |
| Plus the pump | — | + 3 MJ |
| **The child parcel carries** | **10 kg** | **24.2 MJ** |

**Now two networks read that same child parcel.**

| | Network A, 1 MJ = 0.01 h | Network B, 1 MJ = 0.02 h |
|---|--:|--:|
| The child's energy line | 24.2 MJ | 24.2 MJ |
| What it reads as | **0.242 h** | **0.484 h** |

**In plain words: both networks agree the child carries 24.2 MJ, because the split was done on the joules.** They disagree about the hours, and that is the only thing they are allowed to disagree about. Had the parent been stored as "2.12 hours" under A's model and split there, B could never have re-read it.

**The same rule is why a better capture method re-reads history.** 40 litres of petrol is stored as 40 litres. At 0.05 h per kg of CO₂ it reads 4.62 hours; halve what capture costs and the same 40 litres reads 2.31 hours, backwards through every record that ever held a litre ([retroactive-reweighting](retroactive-reweighting.md)).

## What this costs

**A re-weighting pass has to touch every dimension of every event.** Measured: at `k` = 3 dimensions a billion-event log re-weights in about 26 seconds on one ordinary machine, about a third of a record-check pass, and each further dimension adds about 0.12 to that ratio (Foundations §3.4a). A real ledger carries more than three dimensions, so the figure is quoted with its `k`.

## Depends on

- [material-flow-value](material-flow-value.md) · [non-fungibility](non-fungibility.md) · [derived-ledger](derived-ledger.md)

## Consequences

- [retroactive-reweighting](retroactive-reweighting.md) — only a stored quantity can be re-read
- [co-product-allocation](co-product-allocation.md) — a split divides by mass per dimension; a joint process divides nothing
- [organisation-debit](organisation-debit.md) — a team's debit divides by hours worked, per dimension

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §2.2 (a debit is stored as a bundle), §3.2a (the rule), §3.4a (a split is not joint production); `Aequitas_Conformance.md` rows 5, 10, 10f*
