---
title: Integrity constraints IC-1 to IC-12
summary: The twelve arithmetic checks a ledger must never violate, each a conformance row; nine check the log itself (mass and energy balance, origin and fate closure, one holder at a time, interval sanity, the 24-hour cap, pledges drawn from credit and no refund) and three check what any output carries (nothing negative, the union equals what went in, a coarser reading never lowers a figure).
type: hub
ids: []
covers: [IC-1, IC-2, IC-3, IC-4, IC-5, IC-6, IC-7, IC-8, IC-9, IC-10, IC-11, IC-12]
status: settled
edges:
  - {rel: depends_on, to: event-record}
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: debit-vector}
  - {rel: implies, to: distributed-auditing}
  - {rel: implies, to: verification-ladder}
  - {rel: source, to: "Conformance row 7"}
  - {rel: source, to: "Conformance row 8"}
  - {rel: source, to: "Conformance row 9"}
  - {rel: source, to: "Conformance row 10b"}
  - {rel: source, to: "Conformance row 10c"}
  - {rel: source, to: "Conformance row 10d"}
  - {rel: source, to: 00-strategy/Aequitas_Conformance.md}
  - {rel: source, to: 00-strategy/GLOSSARY.md}
  - {rel: tested_by, to: 06-simulation/ic-recompute-cost/RESULTS.md}
  - {rel: tested_by, to: 06-simulation/audits/RESULTS.md}
---
# Integrity constraints IC-1 to IC-12

> **Version:** 0.1
> **Date:** 2026-10-14

> **Twelve rows of the conformance list are arithmetic the ledger must never violate.** They are pure computation on recorded quantities: no trust model, no authority, no inspection. They have been cited as `IC-1` to `IC-12` since 2026-07, and those labels stay valid. **The numbered conformance rows are the source; this page is the index.**

## The words this page uses

| Term | What it means |
|---|---|
| **Parcel** | One delivery or one holding of one substance, with one record ([event-record](event-record.md)). |
| **Reservoir** | An unowned commons: an airshed, a watershed, an ore body, a landfill. |
| **Pledge budget** | The credit a person earned in their life, which is the most they may ever pledge ([pledge-and-signal](pledge-and-signal.md)). |
| **Passage** | Whether a product went through a step of a process. A binary fact, never a share ([co-product-allocation](co-product-allocation.md)). |

## The twelve

| Label | What it says | Row | What it constrains |
|---|---|---|---|
| **IC-1** | Mass balances across every recorded process, within a stated tolerance, at one level of detail | 7 | [event-record](event-record.md) |
| **IC-2** | Energy balances the same way, with declared dissipation | 7 | [event-record](event-record.md) |
| **IC-3** | Everything has a beginning: an extraction from a reservoir, or an estimated entry for something that existed before the books started | 7 | [event-record](event-record.md) |
| **IC-4** | Everything has an end: at any moment it is held by somebody, used up, or released to a named place. Anything else is reported as *unaccounted*, never left out | 7 | [end-of-life-debit](end-of-life-debit.md), [front-loading-rule](front-loading-rule.md) |
| **IC-5** | One holder at any instant; every change of holder is a recorded event | 7a | [property-debit](property-debit.md) |
| **IC-6** | Nothing is used before it exists or after it is gone | 7 | [event-record](event-record.md) |
| **IC-7** | **No account claims more than 24 hours of activity in 24 hours** | 8 | [debit-tolerance](debit-tolerance.md), [disparity-ceiling](disparity-ceiling.md), [organisation-debit](organisation-debit.md) |
| **IC-8** | A person's pledges never exceed the credit they earned in their life, one hour for one hour. Backing received never enlarges the budget | 9 | [pledge-and-signal](pledge-and-signal.md) |
| **IC-9** | A pledge budget is spent when the pledge is made and is never returned; an unfulfilled pledge lapses | 9 | [pledge-and-signal](pledge-and-signal.md) |
| **IC-10** | No quantity a product carries is negative. A negative result is a measurement error or a badly drawn boundary | 10b | [co-product-allocation](co-product-allocation.md) |
| **IC-11** | The union of what every output carries is exactly what went into the process. Their naive total is never reported | 10c | [co-product-allocation](co-product-allocation.md) |
| **IC-12** | Reading a process more coarsely never lowers what any output carries, and the parts of a finer reading reconcile against the coarser figure | 10d | [co-product-allocation](co-product-allocation.md) |

**IC-1 to IC-9 check the log. IC-10 to IC-12 check what an output carries.** A ledger walk that unions parcels rather than summing them (row 10e) is what makes IC-11 hold.

**Two more were proposed, tested and rejected on 2026-08-22.** *IC-13 (genesis admissibility)* refused the ordinary case of somebody joining. *IC-14 (citation closure)* demanded a citation rather than a true one. Both checked a self-asserted field against a constant, where every surviving constraint checks one recorded quantity against another.

## Two examples, with the numbers

**IC-7 against the hardest identity case.** Two identical twins on the lowest rung of checking try to run one account between them.

| | Hours a day |
|---|--:|
| Two honest accounts, 18 h each | **36** |
| The most two twins faking one account between them can reach, with IC-7 capping that account at 24 | **34** |
| What the twins lose a year, 2 × 365 | **730 h**, and they gain nothing, because they share the goods either way |

**IC-11 against a joint process.** A process consumes 100 MJ and yields 100 kg of A and 300 kg of B.

| | What it carries |
|---|--:|
| Co-product A | 100 MJ |
| Co-product B | 100 MJ |
| Their naive total | 200 MJ, **never reported** |
| **Their union** | **100 MJ** = what went in. **IC-11 holds** |

**In plain words: every one of these is a subtraction or a comparison anyone can run on the log, and a lie has to survive all twelve at once.** What they cannot find is a hole: a producer nobody recorded is missing from both sides of every sum, and every sum still balances. Coverage is a different instrument, a physical measurement from outside ([statistical-coverage](statistical-coverage.md)).

## What a check costs

A billion-event log re-checks all nine log constraints in about **100 seconds** on one ordinary machine, in 11.4 MB of memory, flat in the length of the log. IC-5 is a sort and about a fifth of that pass (Foundations §3.4a).

## Depends on

- [event-record](event-record.md) · [material-flow-value](material-flow-value.md) · [debit-vector](debit-vector.md)

## Consequences

- [distributed-auditing](distributed-auditing.md) — the cheapest audits, and they need no trust model
- [verification-ladder](verification-ladder.md) — what arithmetic can and cannot catch

---
*Status: settled*
*Source: `00-strategy/Aequitas_Conformance.md` §2.4 (rows 7 to 10h) and "The `IC-n` labels"; `00-strategy/GLOSSARY.md` integrity-constraints table*
