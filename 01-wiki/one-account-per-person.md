---
title: One person, one account
summary: Inside one trust network a verified human holds exactly one account; participation is voluntary but coverage is not, so a non-participant is estimated on both sides and can neither draw on that estimate nor be charged for it; one person may hold accounts with two networks, and the two are never added.
type: mechanism
ids: [§4.1, C6]
status: settled
edges:
  - {rel: depends_on, to: statistical-coverage}
  - {rel: depends_on, to: trust-network}
  - {rel: depends_on, to: verification-ladder}
  - {rel: implies, to: debit-tolerance}
  - {rel: implies, to: lifetime-reconstruction}
  - {rel: implies, to: network-federation}
  - {rel: constrained_by, to: IC-7}
  - {rel: constrained_by, to: "Conformance row 4a"}
  - {rel: constrained_by, to: "Conformance row 17a"}
  - {rel: open_under, to: OP-22}
  - {rel: open_under, to: OP-14}
  - {rel: source, to: "Foundations §4.1"}
  - {rel: source, to: "Overview §0"}
  - {rel: source, to: 00-strategy/open-problems/OP-22_identity_not_disclosure.md}
---
# One person, one account

> **Version:** 0.1
> **Date:** 2026-10-14

> **1. Inside one trust network, one verified human holds exactly one account.**
> **2. Participation is voluntary. Coverage is not.**

## The words this page uses

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books ([trust-network](trust-network.md)). |
| **Sybil resistance** | Stopping one person from presenting as several. How a network achieves it is its own design. |
| **Accounted** | Every human carries an estimated credit and debit position. A factual claim about material flows in the world. |
| **Realizable** | The position starts acting on what a person may consume. Only once they hold a verified account and observed records have replaced the estimates. |
| **IC-7** | No account claims more than 24 hours of activity in 24 hours. |

## The rule

**Rule 1 is a rule each network applies to its own membership.** It is not a claim about a register of all humanity, and no such register exists. A network needs it because the account is where the consumption gate `D ≤ ρ·(C + P)` is checked, and **two accounts for one person would check one life against that gate twice** ([debit-tolerance](debit-tolerance.md)).

**Rule 2 means a network estimates the people it cannot see.** Leaving a non-participant out would produce a false record, such as wheat with no grower. So the network estimates both sides: debit from the average for their demographic group, computed excluding subscribers; credit from a production model for their occupation and region, computed excluding measured producers ([unassigned-residual](unassigned-residual.md)).

> **Everyone is accounted. Only subscribers are realizable. Participation is the act of turning an estimate into a record.** A non-participant can neither draw on their estimated position nor be charged for it.

**One person may hold an account with more than one network.** Those are two subscriptions, not two lives, and they are not fraud. Each network verified a real human and gave them one account. **The two sets of books are never reconciled and never added** ([network-federation](network-federation.md)).

## Two examples, with the numbers

**One person works 8 hours on a Monday and holds an account with each of two networks.**

| | Network A | Network B |
|---|---|---|
| The floor `F` | 4 hours a day | 10 hours a day |
| Credit recorded for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |

**Both figures are correct**, and they cannot be added: they come from different weighting models, so they are not in the same unit. No account holds 30 hours and IC-7 was not breached, because it applies to each account on its own. A purchase clears against one set of books only, the one the seller accepts.

**The hardest case for rule 1: two identical twins on the lowest rung of checking, deliberately engineering the confusion.** The arithmetic refuses it. Two honest accounts record up to **36 hours** a day between them. One shared account is capped at 24 by IC-7, so the twins reach at most **34**. **They lose 730 hours a year and gain nothing**, because twins sharing a household share the goods either way (Foundations §4.1; the full case is in the OP-22 paper).

## Who games this

- **Many accounts, one person.** Each extra account would earn the floor again. Stopping it is Sybil resistance, a network's own design at whatever rung of the [verification-ladder](verification-ladder.md) it runs. The proof-of-personhood literature is the prior art.
- **Floor shopping.** Joining the network with the most generous floor. Arrested by the seller choosing which network a transaction lands on, so a network with an implausible floor loses sellers. Watch item, not measured: **OP-14**.
- **Proving a pledge's backing across two networks** still depends on what an auditor may see. **OP-22.**

## Depends on

- [statistical-coverage](statistical-coverage.md) · [trust-network](trust-network.md) · [verification-ladder](verification-ladder.md)

## Consequences

- [debit-tolerance](debit-tolerance.md) — the gate is checked against one account
- [lifetime-reconstruction](lifetime-reconstruction.md) — what joining does to the estimate
- [network-federation](network-federation.md) — proving one human holds one account across two registries is a precondition of a merge

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §4.1; `Aequitas_Conformance.md` rows 4a, 17a; `00-strategy/open-problems/OP-22_identity_not_disclosure.md`*
