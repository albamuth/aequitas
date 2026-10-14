---
title: The unassigned residual
summary: A network says how much of a region's output it did not see as one subtraction, R = N − Y, computed and published whole; the leftover is debit on no account, it is never divided by a count of producers, a figure built from two incomplete readings carries a floor, ceiling or not-identified label, and the outside total must be a physical measurement.
type: mechanism
ids: [§4.4]
status: settled
edges:
  - {rel: depends_on, to: statistical-coverage}
  - {rel: depends_on, to: no-externalities}
  - {rel: depends_on, to: physical-trace-test}
  - {rel: depends_on, to: estimation-engine}
  - {rel: implies, to: onboarding-incentive}
  - {rel: implies, to: lifetime-reconstruction}
  - {rel: constrained_by, to: "Conformance row 13"}
  - {rel: constrained_by, to: "Conformance row 14"}
  - {rel: constrained_by, to: "Conformance row 14a"}
  - {rel: constrained_by, to: "Conformance row 14b"}
  - {rel: constrained_by, to: "Conformance row 14d"}
  - {rel: constrained_by, to: "Conformance row 15"}
  - {rel: open_under, to: OP-28}
  - {rel: open_under, to: OP-24}
  - {rel: tested_by, to: 06-simulation/producer-side-splitting/RESULTS.md}
  - {rel: tested_by, to: 06-simulation/residual-attribution/RESULTS.md}
  - {rel: tested_by, to: 06-simulation/residual-unravelling/RESULTS.md}
  - {rel: source, to: "Foundations §4.4"}
  - {rel: source, to: "Overview §7"}
  - {rel: source, to: 00-strategy/open-problems/OP-28_dark_production_and_the_residual_denominator.md}
  - {rel: source, to: 00-strategy/open-problems/OP-26_coverage_and_closure.md}
---
# The unassigned residual

> **Version:** 0.1
> **Date:** 2026-10-14

> **`R = N − Y`.** `N` is the independently known total for a whole area; `Y` is what the measured producers recorded. **`R` is the leftover. It is computed, published whole, divided by nothing, and charged to nobody.**

## The words this page uses

| Term | What it means |
|---|---|
| **`N`** | A physical total for the whole extent, measured by something that reaches everybody in it: agricultural statistics, trade data, a satellite survey. |
| **`Y`** | What the network's own subscribers recorded. |
| **`R`** | The leftover, `N − Y`. Output the books did not see. |
| **Coverage** | `Y ÷ N`. The share of the extent's real flow the records captured. |
| **Attribution witness** | A record that binds a share of the leftover to a named person. A producer joining supplies one. Arithmetic never does. |

## The rule

**Two conditions, and the leftover does not work without both.** An independently known `N` must exist; where none does, this form is unavailable rather than weak. And `N` and `Y` must measure the same quantity, over the same piece of the world, over the same stretch of time, with error bounds smaller than the difference. **On the project's own worked case, skipping the second made the unmeasured pool look three times larger than it was** ([estimation-engine](estimation-engine.md) has that case).

**The leftover is never divided by a count of producers.** Two worlds whose truths differ by 1.21× hand one network identical books, so no per-head figure computed from those books describes either. And a head count left no physical trace; hectares did ([physical-trace-test](physical-trace-test.md)). Where a per-producer figure is needed it comes from a production model over measured extent, still computed over the leftover and never over the whole population, so that staying unmeasured stops paying.

**The leftover is charged to nobody.** A residual proves that activity is missing; it does not prove whose. Spreading it across the producers a network happens to know about would be a heuristic, and a heuristic is not a witness. **This is A4's third line, stated rather than excused**: where causation is unresolved the consequence is held explicitly unassigned until an attribution witness exists. Until a dark producer joins, they cannot transact inside the network at all, and that is the pressure to resolve.

**The outside total has to be a physical measurement.** A check that compares a thing to itself can find a mistake and cannot find a hole: delete two sacks from both halves of a record and every sum still balances. Only a record made on a second path, a counterparty's receipt, a reservoir's measured depletion, or `N` itself, can see a gap.

## An example, with the numbers

**A valley of 100 farms. Eighty subscribe and record 82,000 t. A satellite survey puts the valley at 88,000 t and measured the twenty unsubscribed farms' land at 5,000 hectares, unevenly held.**

| | |
|---|---|
| `N` | 88,000 t |
| `Y` | 82,000 t |
| **`R`, published whole** | **6,000 t**, on no account |
| Coverage | 82,000 ÷ 88,000 = **93%** |
| The leftover's rate over measured extent | 6,000 ÷ 5,000 = **1.2 t/ha** |

| An unsubscribed farm | Land | The withdrawn per-head slice | The production model |
|---|--:|--:|--:|
| The largest | 600 ha | 300 t | **720 t** |
| The smallest | 100 ha | 300 t | **120 t** |

**Both columns add to 6,000 t. Only one describes a farm.** And the right-hand column is not settled either: honest noise in the land readings barely moves it, but a farm declaring 300 hectares instead of 600 halves its own estimate and pushes the difference onto its neighbours. **A network publishes its extent register as unaudited** (conformance row 14d, OP-28).

## A figure built from two incomplete readings needs a label

**A count over incomplete coverage is a floor: it can only be too low. A subtraction is not**, because it reverses the direction of every error inside it.

| Which operand is blind | True `R` | So the published 6,000 t is |
|---|--:|---|
| `Y` under-records by 4,000 t | 2,000 t | a **ceiling**, three times the truth |
| `N` under-observes by 10,000 t | 16,000 t | a **floor** |

**So a derived figure is published as an interval with one of three labels: `floor`, `ceiling`, or `not identified`, and `not identified` is where every such figure starts.** A label is earned by an argument about each operand's blind spot. The default has to be the unflattering one, because whoever computes the figure benefits from one of its labels: four figures this project published were each found wrong in the direction that favoured it, every one from outside.

## Choosing not to record is legitimate

Subsistence, gifts, barter, output held back for the money economy, and the same produce listed with two networks are all ordinary and none is evasion. **Produce you do not enter cannot be sold on the network, and that is the whole of the discipline.** Gathering data on non-participants and helping a producer bring their chain into the record are both credited work.

## Depends on

- [statistical-coverage](statistical-coverage.md) · [no-externalities](no-externalities.md) · [physical-trace-test](physical-trace-test.md) · [estimation-engine](estimation-engine.md)

## Consequences

- [onboarding-incentive](onboarding-incentive.md) — the estimate for whoever stays out gets worse as others join
- [lifetime-reconstruction](lifetime-reconstruction.md) — the same rule applied to the undisclosed periods of one life

---
*Status: settled (the leftover rule) · OP-28 open (the extent register) · OP-24 (the constants)*
*Source: `00-strategy/Aequitas_Foundations.md` §4.4; `Aequitas_Conformance.md` rows 13, 14, 14a, 14b, 14d, 15*
