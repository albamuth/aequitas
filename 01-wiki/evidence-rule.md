---
title: The published evidence rule
summary: A trust network publishes, for every kind of work it credits, what evidence that work requires, before crediting any of it; it credits no kind of work it has no rule for; and it never converts another network's figures into its own, only re-computes the claim from the shared physical record.
type: mechanism
ids: [§4.2]
status: settled
edges:
  - {rel: depends_on, to: protocol-governance}
  - {rel: depends_on, to: trust-network}
  - {rel: depends_on, to: statistical-coverage}
  - {rel: implies, to: service-credit}
  - {rel: implies, to: enrichment}
  - {rel: implies, to: production-credit}
  - {rel: implies, to: debit-tolerance}
  - {rel: implies, to: verification-ladder}
  - {rel: constrained_by, to: "Conformance row 4a"}
  - {rel: constrained_by, to: "Conformance row 4b"}
  - {rel: constrained_by, to: "Conformance row 12c"}
  - {rel: constrained_by, to: "Conformance row 16d"}
  - {rel: open_under, to: OP-22}
  - {rel: related, to: op-22}
  - {rel: open_under, to: OP-10}
  - {rel: source, to: "Foundations §2.3"}
  - {rel: source, to: "Foundations §4.2"}
  - {rel: source, to: "Overview §6"}
---
# The published evidence rule

> **Version:** 0.1
> **Date:** 2026-10-14

> **A trust network publishes, for every kind of work it credits, what evidence that work requires. That published set is its contract with the subscriber. A network never credits a kind of work it cannot get evidence about.**

## The words this page uses

| Term | What it means |
|---|---|
| **Evidence rule** | A published statement of what a claim of one kind of work must show before it credits. |
| **The three names** | Production, service, enrichment. The outer wall on what a network may credit at all (Foundations §2.3). |
| **Weighting model** | The numbers a network uses to turn physical quantities into hours. Each network runs its own. |
| **Comparison, never conversion** | A second network re-computes a claim from the shared physical record through its own model. It never imports the first network's number. |

## The rule

**Two things follow.** A subscriber cannot claim work the network has no rule for, because there is no rule to satisfy. And a network that cannot say what would count as evidence does not credit that kind of work, and says so in public. **"Credited but measured badly" is not a state this design produces.**

**What the evidence usually is, by kind of output.**

| Output | How it is verified |
|---|---|
| **Goods** | The hand-off. The receiver accepts possession and the debit that rides with it ([production-credit](production-credit.md)) |
| **A service** | The client confirms it happened ([service-credit](service-credit.md)) |
| **Enrichment** | Evidence that the work happened, never that anyone valued it ([enrichment](enrichment.md)) |
| **Self-care** | Proof of life. A verified living human maintained itself ([debit-tolerance](debit-tolerance.md)) |

**Two rules stop this becoming a route for fraud.** Verification asks whether the work happened and never whether anyone valued it; letting credit depend on likes would make feedback a currency by the back door. And weak evidence weighs near zero until something corroborates it, inside a rule, never in place of one.

**A network never converts another network's figures into its own.** Converting a balance from one model into another would set an exchange rate between two credit-standards, which is a medium of exchange and forbidden by A3. **A network with lax checking therefore cannot export the credit it issues**: whoever trades with its members discounts it. That guard depends on OP-22, because re-computing what a claim is drawn from means seeing it.

## An example, with the numbers

**A network publishes its rule for translation work: the translated text exists, and the client confirms receiving it.**

| | Hours worked | Against the rule | Hours credited |
|---|---|---|---|
| **A** delivers a translation and the client confirms | 20 h | met | **20 h** |
| **B** says they translated for 20 hours, with no text and no client | 20 h | not met | **0 h** |

**B is not being judged.** B knew the rule before starting. **Now change the network instead of the person.** If translating for someone who cannot confirm is work this network wants to credit, it writes a rule for that case, perhaps a second witness, and then B's 20 hours credit at 20 hours, not at some fraction because a vague claim was weighted cautiously.

## What subscribing discloses, and what it does not

**Whatever a subscriber puts into the accounting is open to the network that keeps it. Whatever they keep out was never in the accounting at all.** A network cannot check arithmetic it may not read. This does not mean a subscriber discloses everything they do: the five legitimate cases of not recording stand ([unassigned-residual](unassigned-residual.md)), and produce not entered cannot be sold on the network, which is the whole of the cost. **And auditable does not mean checked independently**: reading a plant's own flow sheet is still reading the plant's own record. What defeats a self-serving claim is a record made on a different path.

## The honest limit

**Not every kind of real work is documentable.** A network that cannot write a rule for one leaves that work uncredited. What changes is where the gap sits: in a published list anybody can read before joining, not in a weighting nobody can see. **How a network decides which rules to write is its own business** (A8). The list is a capture surface, and it is worked under OP-10.

## Depends on

- [protocol-governance](protocol-governance.md) · [trust-network](trust-network.md) · [statistical-coverage](statistical-coverage.md)

## Consequences

- [production-credit](production-credit.md) · [service-credit](service-credit.md) · [enrichment](enrichment.md) — each kind's evidence
- [debit-tolerance](debit-tolerance.md) — the floor is a published rule, not a tally of a day
- [verification-ladder](verification-ladder.md) — how thoroughly the evidence is established

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §2.3 (the gate is the boundary), §4.2; `Aequitas_Conformance.md` rows 4a, 4b, 12c, 16d*
