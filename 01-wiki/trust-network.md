---
title: Trust network
summary: A trust network is the organisation that keeps the books, records material flows, checks the arithmetic, estimates what it cannot see, and publishes its methods; it has no set size, keeps its own books that are never added to another network's, and does eight jobs in order.
type: mechanism
ids: [§4.0, C2]
status: settled
edges:
  - {rel: depends_on, to: protocol-governance}
  - {rel: depends_on, to: derived-ledger}
  - {rel: depends_on, to: statistical-coverage}
  - {rel: implies, to: ledger-ecosystem}
  - {rel: implies, to: verification-ladder}
  - {rel: implies, to: estimation-engine}
  - {rel: implies, to: pledge-and-signal}
  - {rel: implies, to: privacy-is-a-network-choice}
  - {rel: implies, to: dispute-resolution}
  - {rel: implies, to: onboarding-incentive}
  - {rel: implies, to: debit-tolerance}
  - {rel: implies, to: one-account-per-person}
  - {rel: implies, to: evidence-rule}
  - {rel: implies, to: unassigned-residual}
  - {rel: implies, to: record-beats-estimate}
  - {rel: implies, to: lifetime-reconstruction}
  - {rel: implies, to: publish-own-workings}
  - {rel: implies, to: network-federation}
  - {rel: related, to: components}
  - {rel: constrained_by, to: "Conformance row 4a"}
  - {rel: constrained_by, to: "Conformance row 16"}
  - {rel: constrained_by, to: "Conformance row 16d"}
  - {rel: open_under, to: OP-22}
  - {rel: open_under, to: OP-24}
  - {rel: source, to: "Foundations §2.6"}
  - {rel: source, to: "Foundations §4.0"}
  - {rel: source, to: "Overview §0"}
  - {rel: source, to: 00-strategy/papers/C2_TrustNetworks.md}
---
# Trust network

> **Version:** 0.1
> **Date:** 2026-10-14

> **A trust network keeps the books.** It records material flows, hand-offs, services, pledges, and measurements of the world itself. It checks the arithmetic, estimates what it cannot observe, and publishes its methods so anyone can re-run them. **Aequitas says what should be counted. Trust networks are where the counting happens, or fails to.**

## The words this page uses

| Term | What it means |
|---|---|
| **Subscriber** | A person who holds an account with a trust network. |
| **Event log** | The permanent, append-only record of what happened. Every position is computed from it and none is stored ([derived-ledger](derived-ledger.md)). |
| **Record** | A figure taken from an observation or an attestation. **A record always beats an estimate.** |
| **Estimate** | A figure computed from a published method, where no direct record exists ([estimation-engine](estimation-engine.md)). |
| **The floor**, `F` | The hours a day the network counts as the work of keeping a human alive. Each network sets its own ([debit-tolerance](debit-tolerance.md)). |
| **ρ** ("rho") | The network's debit tolerance, the multiplier in the gate `D ≤ ρ·(C + P)`. |

## What it is

**Aequitas is a system in the sense that capitalism is a system.** Nobody joins capitalism; banks and firms carry it out. Trust networks carry out Aequitas. **Think of them as laboratories rather than banks**: their business is getting the numbers right, and they publish how they got them so that other networks can find their mistakes.

**A trust network has no set size.** It may cover a valley, a trade, a country, several continents, or the world. A8 is about who may change the rules, not about how big anyone is. Networks that work together are expected to keep merging ([ledger-ecosystem](ledger-ecosystem.md)).

**Three facts shape everything a network does** (Foundations §4.0).

1. **Each network keeps its own books, and no book is ever added to another book.** What a subscriber sees is one network's best current approximation of the truth.
2. **A transaction happens on exactly one network, and the seller chooses which.** *"We do not take Network B here"* is the same sentence a shop says today about a card scheme. That choice is the whole of the discipline on a network's settings.
3. **A network can end.** Transactions recorded only in a collapsed network are forgotten unless another network recovers its database, which is a merge.

## The eight jobs, in the order a network does them

| | Job | Page |
|---|---|---|
| **4.1** | It gives each person one account, and estimates everyone it cannot see | [statistical-coverage](statistical-coverage.md) |
| **4.2** | It decides what counts as evidence for each kind of work, and publishes that | [service-credit](service-credit.md), [enrichment](enrichment.md) |
| **4.3** | It checks claims, and chooses how hard to check | [verification-ladder](verification-ladder.md) |
| **4.4** | It estimates what it cannot see, and says how much that is | [estimation-engine](estimation-engine.md) |
| **4.5** | It credits work | [production-credit](production-credit.md), [front-loading-rule](front-loading-rule.md) |
| **4.6** | It carries what people want made | [pledge-and-signal](pledge-and-signal.md) |
| **4.7** | It publishes its own workings, and settles disputes | [privacy-is-a-network-choice](privacy-is-a-network-choice.md), [dispute-resolution](dispute-resolution.md) |
| **4.8** | It takes people in, it merges with other networks, and it can end | [onboarding-incentive](onboarding-incentive.md), [permanence-and-death](permanence-and-death.md) |

**What is not prescribed.** How a network handles privacy, what technology it runs on, which laws it must satisfy, how it documents its own founding, and how it audits its cost constants are all the network's own design (Foundations §2.6). **What it must do is publish what it runs, so anybody can re-compute its claims** (A8).

## An example, with the numbers

**One person works 8 hours on a Monday and holds an account with each of two networks.**

| | Network A | Network B |
|---|---|---|
| The floor `F` | 4 hours a day | 10 hours a day |
| Credit recorded for that Monday | 8 + 4 = **12 hours** | 8 + 10 = **18 hours** |

**Both figures are correct.** Each network read the same two physical facts, eight hours worked and one human alive, through its own settings. **They cannot be added.** An hour in A's books and an hour in B's are not the same unit, and adding them would set an exchange rate between two networks, which is a currency (A3). No account holds 30 hours and IC-7 was not breached, because it applies to each account on its own. A purchase clears against one set of books only, the one the seller accepts.

## Depends on

- [protocol-governance](protocol-governance.md) · [derived-ledger](derived-ledger.md) · [statistical-coverage](statistical-coverage.md)

## Consequences

- Every page in the table above. **A trust network is the thing doing it.**

---
*Status: settled (what a network is; its eight jobs) · OP-22 and OP-24 open (what an auditor must see; how constants are audited)*
*Source: `00-strategy/Aequitas_Foundations.md` §2.6 (what this document answers, and what it does not), §4.0; `Aequitas_Overview.md` §0; `00-strategy/papers/C2_TrustNetworks.md`*
