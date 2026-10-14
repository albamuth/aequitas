---
title: Networks federate by agreeing methods, not answers
summary: Two networks never negotiate a person's balance; merging means agreeing every rule, after which one answer is computed from one log, and until then each keeps its own book; goods cross the money boundary in both directions at a deliberate cost, standing never does, and extraction exhausts itself through the extractor's own gate.
type: mechanism
ids: [§4.8, OP-27]
status: settled
edges:
  - {rel: depends_on, to: trust-network}
  - {rel: depends_on, to: ledger-ecosystem}
  - {rel: depends_on, to: one-account-per-person}
  - {rel: depends_on, to: non-fungibility}
  - {rel: depends_on, to: material-flow-value}
  - {rel: implies, to: evidence-rule}
  - {rel: implies, to: organisation-debit}
  - {rel: implies, to: onboarding-incentive}
  - {rel: constrained_by, to: "Conformance row 4a"}
  - {rel: open_under, to: OP-22}
  - {rel: open_under, to: OP-10}
  - {rel: source, to: "Foundations §4.0"}
  - {rel: source, to: "Foundations §4.8"}
  - {rel: source, to: "Overview §9"}
  - {rel: source, to: 00-strategy/open-problems/OP-27_parallel_implementation.md}
---
# Networks federate by agreeing methods, not answers

> **Version:** 0.1
> **Date:** 2026-10-14

> **Merging means agreeing every rule, the floor, ρ, the weighting model, and how a human is identified, after which the merged network computes one answer from one log. Until they agree, each keeps its own book and neither is wrong.**

## The words this page uses

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books ([trust-network](trust-network.md)). |
| **Template** | A cached estimate for a class of good, published with its method and vintage, used when a money-made good is sold in. It must err against the seller. |
| **Standing** | A person's credit and debit position. It never crosses any boundary. |

## Merging

**Two networks do not negotiate a person's balance.** They can only agree methods. Two networks that cannot confirm that two pseudonymous accounts belong to one person cannot merge: a network requiring a face scan, a fingerprint and a voice check cannot merge with one requiring only a card scan. **Proving one human holds one account across two registries is a precondition of merging, not an open problem in the accounting** ([one-account-per-person](one-account-per-person.md)).

**A merge is not a special event.** When a person's two accounts become one, the adjustment is exactly as ordinary as the adjustment made whenever new data arrives, because positions are computed from the log and never stored. **The expected trajectory is convergence**: networks that federate keep federating, which buys one ledger per person and no coverage gaps at the seams. Trust networks are laboratories rather than banks, and a network whose methods let fraud through is helped by another sharing the method that catches it, because two networks often draw on the same outside evidence.

**Convergence is deliberately not treated as a capture problem.** A monopoly earned by better methods is over which method is used, never over who may propose one, because methods are published and replicable. **The watch item: a monopoly earned on merit can stop being meritorious and keep the position. The guard is publication plus replication, so if publication weakens, so does this.**

## Trading across the money boundary

**Aequitas has to be usable by someone who still uses money**, because for years most of anyone's counterparties will be outside. Both directions are permitted and both are dearer than trading inside.

| Direction | What happens |
|---|---|
| **Selling into Aequitas** a good made with money-bought inputs | The good is unrecorded until it is sold in. At that hand-off the maker records its origins properly or applies a published template that assigns a figure at once. **The maker spent money and receives none, and that is the disincentive.** |
| **Selling out of Aequitas**, for money | Permitted. **The debit stays with the seller.** To the network the seller made a gift, and the network does not see the money at all. |

**Money is invisible because it is not physical.** A1 keeps paper claims off every ledger, so a payment in money is not an event. The goods moved and the ledger records that. **No cross-boundary rule exists or is needed.**

## An example, with the numbers

**A wealthy person pays 100 workers in money to make 1,000 chairs, then sells the chairs into Aequitas.** Each chair took 4 hours of work and 12 kg of timber bought with money.

| | What the books record |
|---|---|
| The 100 workers | **400 hours of credit each**, 4 h × 1,000 chairs ÷ 100, because credit records who did the work |
| The financier | **0 hours.** They worked none of them |
| The chairs at the hand-off in | 12,000 kg of timber by template, erring against the seller, as property debit on whoever takes them |
| The money that changed hands | **Nothing.** Not matter, not energy, not an event |

**In plain words: goods cross the boundary and standing does not. You cannot buy hours.**

**Now the other way.** Someone buys 500 kg of flour inside, bakes bread, and sells all of it outside for cash. Their debit gains 500 kg of flour and the baking energy; selling outside takes none of it off. The only thing that grows their credit is their own hours, capped at 24 a day. **Their own gate shuts them out, and it shuts faster the harder they pull.** The same holds for an organisation, because its debit is its members' debit by hours worked, and closing it and opening another moves nothing ([organisation-debit](organisation-debit.md)).

## What stays open

Whether a person can hide behind a fake or borrowed membership list is a verification question (OP-25, C6). A template can be captured like any constant (OP-24, OP-10). Proving a pledge's backing across a model boundary waits on OP-22.

## Depends on

- [trust-network](trust-network.md) · [ledger-ecosystem](ledger-ecosystem.md) · [one-account-per-person](one-account-per-person.md) · [non-fungibility](non-fungibility.md) · [material-flow-value](material-flow-value.md)

## Consequences

- [evidence-rule](evidence-rule.md) — comparison, never conversion
- [organisation-debit](organisation-debit.md) · [onboarding-incentive](onboarding-incentive.md)

---
*Status: settled (ruled and stress-tested 2026-08-23, OP-27)*
*Source: `00-strategy/Aequitas_Foundations.md` §4.0 (three facts), §4.8 (networks federate; trading across the money boundary); `00-strategy/open-problems/OP-27_parallel_implementation.md`*
