---
title: An organisation's debit is its members' debit
summary: An organisation's account is a view of its members' positions, not an owner of them; every debit its members caused while acting for it is their own debit, divided by the hours each worked, so closing the organisation moves nothing and a chain of shells escapes nothing.
type: mechanism
ids: [§3.2c]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: time-as-yardstick}
  - {rel: depends_on, to: debit-vector}
  - {rel: depends_on, to: physical-trace-test}
  - {rel: implies, to: pollution-making-vs-using}
  - {rel: implies, to: capitalism-cannot-function}
  - {rel: implies, to: ledger-ecosystem}
  - {rel: constrained_by, to: IC-7}
  - {rel: constrained_by, to: "Conformance row 2c"}
  - {rel: supersedes, to: OP-18}
  - {rel: source, to: "Foundations §2.5"}
  - {rel: source, to: "Foundations §3.2c"}
  - {rel: source, to: "Foundations §4.8"}
  - {rel: source, to: "Objections B19"}
---
# An organisation's debit is its members' debit

> **Version:** 0.1
> **Date:** 2026-10-14

> **An organisation's account is a view of its members' positions, not an owner of them.** Every debit an organisation's members caused while acting for it is, at the same time, their own debit, divided among them in proportion to the hours each worked for it.

## The words this page uses

| Term | What it means |
|---|---|
| **Organisation** | Any account that is not a single verified human: a business, a co-operative, an institution, a public body. |
| **Member** | A person who works for it during the period in question. |
| **Acting for it** | Causing a debit on the organisation's own work. A member burning the organisation's fuel on its route caused that jointly. A member burning their own fuel on their own errand caused it alone, and carries it alone. |
| **The gate** | `D ≤ ρ·(C + P)`, checked at each transaction ([debit-tolerance](debit-tolerance.md)). |

## The rule

**Why it follows from A1.** Cost attaches to whoever acted, and only people act. A co-operative never lifted, drove or burned anything; its members did. So an organisation cannot be the final holder of a debit, for the same reason a barn cannot ([property-debit](property-debit.md)) and a power station cannot ([pollution-making-vs-using](pollution-making-vs-using.md)). **The organisation is a bookkeeping convenience. The people are the causers.**

**Why it divides at all.** A reader can object that only the driver's foot was on the pedal. That reads "the causer" as one pair of hands. The route existed because ten people organised it, and every one of them acted. Naming the driver alone would be picking the last person in the chain.

**Why hours, and why that is a declared convention.** Hours worked leave no trace pointing at any particular debit the organisation took on, so this is a convention and the documents say so ([physical-trace-test](physical-trace-test.md)). Hours are chosen because they add no new lever: they are already recorded for credit, already capped at 24 a day by IC-7, and already the basis pledges distribute by. An equal split or a seniority weighting would be a new thing to game.

**Closing an organisation moves nothing.** Nothing was ever held anywhere else, so there is nothing to distribute at the end.

## An example, with the numbers

**Ten people each work 2,000 hours in a year for one co-operative. The co-operative takes on 24,000 hours of debit that year.**

| | |
|---|---|
| Total member hours | 10 × 2,000 = **20,000 h** |
| Each member's share of the hours | 2,000 ÷ 20,000 = **10%** |
| Each member's share of the debit | 10% × 24,000 = **2,400 h** |

**Now close the co-operative and open a new one with the same ten people.** Each still carries 2,400 h. Repeat the year and each carries 4,800 h. After ten rounds each carries 24,000 h. **The count never resets, so a shell chain escapes nothing.**

**It also does not make the gate bind**, because each round adds credit as well as debit. At `F` = 10 and ρ = 1.2:

| Per member | `D` | `C` (2,000 worked + 3,650 floor a year) | `D ÷ ρ·C` |
|---|--:|--:|--:|
| After round 1 | 2,400 h | 5,650 h | **0.354** |
| After round 10 | 24,000 h | 56,500 h | **0.354** |

**In plain words: the round count cancels.** At these settings a member's gate binds only when the organisation takes on more than 1.2 × 5,650 ÷ 2,000 = **3.39 hours of debit per member-hour worked**, in the first round or the thousandth.

## Two boundaries this rule does not cross

| Not covered | Which rule covers it |
|---|---|
| **A durable asset's creation cost** (a hospital building, a plant, tooling) | [front-loading-rule](front-loading-rule.md): split by *holding time*, so a new hire bears about zero. That is property debit on an asset; this page is consumption and operating debit. |
| **A member's own credit** | A3. Credit never moves in either direction. Members are credited their own hours whatever the organisation does. **This page divides debit only.** |

**What stays open.** Whether a person can hide behind a fake or borrowed membership list, claiming hours for people who did not work them. That is a verification question, not an accounting one (Foundations §4.8).

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md) · [debit-vector](debit-vector.md) · [physical-trace-test](physical-trace-test.md)

## Consequences

- [pollution-making-vs-using](pollution-making-vs-using.md) — a company's emissions land on its staff by hours
- [capitalism-cannot-function](capitalism-cannot-function.md) — a supervisor cannot dump cost onto subordinates by rank
- [ledger-ecosystem](ledger-ecosystem.md) — extraction across the money boundary exhausts itself the same way for an organisation as for a person

---
*Status: settled (a declared convention, checked 2026-09-09 against a metered delivery tailpipe)*
*Source: `00-strategy/Aequitas_Foundations.md` §2.5 (the convention table), §3.2c, §4.8 (the organisation case at the money boundary); `Aequitas_Conformance.md` row 2c; `Aequitas_Objections.md` B19*
