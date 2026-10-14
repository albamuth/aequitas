---
title: A network publishes its own workings
summary: A network asks people to rely on its arithmetic, so it publishes every estimating number, every method, and anonymised data covering all its participants; funding is only the recognition of an activity as creditable; a network's own founding is recorded like any pre-existing thing; and publishing more to earn trust also publishes more to identify people by.
type: mechanism
ids: [§4.7]
status: settled
edges:
  - {rel: depends_on, to: protocol-governance}
  - {rel: depends_on, to: trust-network}
  - {rel: depends_on, to: derived-ledger}
  - {rel: implies, to: privacy-is-a-network-choice}
  - {rel: implies, to: dispute-resolution}
  - {rel: implies, to: distributed-auditing}
  - {rel: implies, to: record-beats-estimate}
  - {rel: constrained_by, to: "Conformance row 16"}
  - {rel: constrained_by, to: "Conformance row 16a"}
  - {rel: constrained_by, to: "Conformance row 16c"}
  - {rel: constrained_by, to: "Conformance row 16d"}
  - {rel: open_under, to: OP-22}
  - {rel: open_under, to: OP-24}
  - {rel: source, to: "Foundations §4.7"}
  - {rel: source, to: "Foundations §3.3a"}
  - {rel: source, to: "Overview §7"}
---
# A network publishes its own workings

> **Version:** 0.1
> **Date:** 2026-10-14

> **To be trustworthy a network publishes every estimating number it uses, every method, and anonymised data covering all of its participants. A network that will not show its arithmetic is asking to be trusted rather than checked, which is the thing this system exists to stop needing.**

## The words this page uses

| Term | What it means |
|---|---|
| **Tallying** | Computing positions, estimates and the leftover from the log. A computation, not a judgement made case by case. |
| **Funding** | In Aequitas, only the recognition of an activity as creditable. There is no treasury, no allocation and no grant. |
| **Genesis entry** | The estimated record made for a thing that existed before the ledger started. |

## What a network owes

**Tallying is a computation, which is what makes "cite your method" enforceable.** Against a human process that is an aspiration. **Against a published algorithm it is a version number**, and anyone can re-run it on the same inputs and get the same answer. How much to reveal about institutions and individual businesses is the network's own call ([privacy-is-a-network-choice](privacy-is-a-network-choice.md)).

**The market is public; persons are private.** Pledges, production quantities, hand-offs and the figures things carry are visible. Individual positions are not. The split does real work: a worker can read how wanted their product is, an auditor can watch a supply chain, and nobody can privately mislabel pledged work as speculative when the pledge ledger is public.

> **And this cuts against itself.** Anonymised participant data becomes more re-identifiable the more of it there is. **Publishing more to earn trust also publishes more to identify people by.** A network is choosing on that axis whether it means to or not. The minimum an auditor must see is OP-22, unsolved.

**"Funding" is not a budget.** Asking who funds an auditor imports a question from money that does not survive translation. Audit work is work, recorded when it happens, and recording is never gated on approval. **The credit for doing the work was never scarce.** What is scarce is demand (a pledge says someone wants the work done) and verification (which decides when the credit counts).

**A network's own founding is recorded like any pre-existing thing.** A network cannot be paid by an accounting that does not exist yet, so whether its founders take credit for creating it is the network's own decision, entered as an estimate after the fact and open to supersession. A network may document its founding carefully, thinly, or not at all; **the founding record is the first thing anyone can check, so it is a signal about all the rest.**

## An example, with the numbers

**Three founders spend 14 months building a network before it opens, and claim founding credit.** Three things bound the damage whatever they claim.

| Bound | Figure |
|---|---|
| Wall-clock cap: 3 founders × 14 months × 24 h a day, checkable with a calendar | **≈ 30,660 h** at most, and IC-7 holds each to 24 a day |
| What over-crediting buys | **Consumption room only**, gated by `D ≤ ρ·(C + P)` like everyone else's. Credit is non-transferable, so it buys nothing else |
| Who re-computes it | **Any later network**, from the public founding record |

**In plain words: a generous founding record is visible, bounded by the calendar, and worth only what any other credit is worth.** Nobody has to forbid a bad founding record. It simply does not attract anyone.

## How a dispute resolves

Replication, published method, dated records, no adjudicator. Aequitas already has every one of those, written for other reasons. The transaction-time consequence, that a purchase either clears or does not, now, and that most disputes therefore never need deciding, is worked in [dispute-resolution](dispute-resolution.md).

## Depends on

- [protocol-governance](protocol-governance.md) · [trust-network](trust-network.md) · [derived-ledger](derived-ledger.md)

## Consequences

- [privacy-is-a-network-choice](privacy-is-a-network-choice.md) — how private, exactly, is the network's own dial
- [dispute-resolution](dispute-resolution.md) · [distributed-auditing](distributed-auditing.md) · [record-beats-estimate](record-beats-estimate.md)

---
*Status: settled · OP-22 open (what an auditor must see)*
*Source: `00-strategy/Aequitas_Foundations.md` §4.7 (what a network owes; funding is recognition; a network's own founding), §3.3a (what a published constant carries); `Aequitas_Conformance.md` rows 16, 16a, 16c, 16d*
