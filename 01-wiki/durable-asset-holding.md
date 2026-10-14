---
title: A durable asset is shared by holding time
summary: A building, plant or tool holds its creation cost as debit on the asset itself; each holder's permanent share is their holding time divided by the total holding time over the asset's life, so a new hire bears almost nothing, a carrier in transit takes no share, and the share dilutes but never reaches zero after a hand-off.
type: mechanism
ids: [§4.5]
status: settled
edges:
  - {rel: depends_on, to: property-debit}
  - {rel: depends_on, to: front-loading-rule}
  - {rel: depends_on, to: physical-trace-test}
  - {rel: depends_on, to: pledge-and-signal}
  - {rel: implies, to: self-work-identity}
  - {rel: implies, to: organisation-debit}
  - {rel: implies, to: land-and-remediation}
  - {rel: constrained_by, to: IC-5}
  - {rel: constrained_by, to: "Conformance row 2a"}
  - {rel: constrained_by, to: "Conformance row 7a"}
  - {rel: source, to: "Foundations §2.5"}
  - {rel: source, to: "Foundations §3.2"}
  - {rel: source, to: "Foundations §4.5"}
  - {rel: source, to: "Overview §2"}
---
# A durable asset carries its own making, shared by how long each person held it

> **Version:** 0.1
> **Date:** 2026-10-14

> **A building, plant or tool holds its creation cost as debit on the asset itself.** Each holder's permanent share is their holding time divided by the total holding time over the asset's whole life. **Pledges cushion the bite; they never shrink the debit, because nothing may vanish.**

## The words this page uses

| Term | What it means |
|---|---|
| **Creation cost** | The hours and materials that made the thing. One of the components of [property-debit](property-debit.md). |
| **Holding time** | How long a person held the asset, counted from when it entered service. A physical trace, so the split is measured rather than invented ([physical-trace-test](physical-trace-test.md)). |
| **Holder-years** | The total holding time across every holder over the asset's life, the denominator of every share. |
| **Transit custodian** | A carrier holding goods on the way somewhere. Takes no share of their making. |

## The rule

**Why holding time rather than an equal split.** Holding time is a trace, so the figure is read, not chosen. And a new hire bears almost nothing, which removes the entry toll an equal split would put on exactly the capital-heavy essential work society most needs staffed: hospitals, water treatment. In the language of cooperative games, the split passes the dummy test (zero time, zero share) and the symmetry test (equal time, equal share), and it is final only at disposal: while the asset lives, earlier holders' shares dilute as new holding time accrues, and the not-yet-attributed remainder rides the asset until its life completes. **No leak.**

**The share stays with you after a hand-off.** The material leaves with the thing; your holding-time share of its making does not. Hand a 500,000-hour house on after ten years and, once the next holder has held it an equal span, about 250,000 hours of making are still on your books. You cannot escape it through a non-participant: with no record of a hand-off, the books still show you holding it.

**A carrier moving goods takes no share of their making.** A haulier holding 1,000 toasters for two days did not make them. Transit adds only the carrier's own transport debit. Without this rule the supply-chain hand-off model would quietly load the making of a toaster onto the truck driver.

**Work done on the asset raises its creation cost.** While you hold it, a repair credits you the hours and raises the asset's debit by the same hours, net zero ([self-work-identity](self-work-identity.md)).

## An example, with the numbers

**A hospital costs 100,000 hours to build and lasts 60 years. About 200 people staff it at any time, so its life holds 200 × 60 = 12,000 holder-years.**

| Holder | Holding time | Share | Hours |
|---|--:|--:|--:|
| A nurse hired on Monday | 0 years | **≈ 0%** | **≈ 0 h** |
| A nurse after one year | 1 year | 1 ÷ 12,000 = 0.008% | **8 h** |
| A 30-year veteran | 30 years | 30 ÷ 12,000 = **0.25%** | **250 h** |

**Now a privately held tool, with no pledges.** A holds a 2,000-hour lathe for 1 year, hands it to B, who uses it for 1 year, after which it is scrapped. Total 2 holder-years.

| | Share | Hours, permanent |
|---|--:|--:|
| A | 1 ÷ 2 = **50%** | **1,000 h** |
| B | 1 ÷ 2 = **50%** | **1,000 h** |

**In plain words: a solo owner of expensive private capital holds a large share, correctly, because they alone used it. Two hundred hospital staff hold slivers, correctly, because two hundred of them used it.** The hospital's whole 100,000 hours are still on somebody; they are just not on the patient's bill.

## Depends on

- [property-debit](property-debit.md) · [front-loading-rule](front-loading-rule.md) · [physical-trace-test](physical-trace-test.md) · [pledge-and-signal](pledge-and-signal.md)

## Consequences

- [self-work-identity](self-work-identity.md) · [organisation-debit](organisation-debit.md) — the two rules that do not collide: holding time for an asset, hours worked for operating debit
- [land-and-remediation](land-and-remediation.md) — a building's remediation debt is shared the same way

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §2.5 (what this system divides), §3.2 (the two components of property debit), §4.5 (a durable asset carries its own making); `Aequitas_Conformance.md` rows 2a, 7a*
