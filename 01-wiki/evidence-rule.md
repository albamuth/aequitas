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
| **A service** | A receiver who asked for it confirms that it happened. The confirmation is also the consent that puts the hours on that receiver. One confirming receiver is enough ([service-credit](service-credit.md)) |
| **Enrichment** | Where it is given to other people, a receiver who asked for it confirms, as for a service. For other enrichment, evidence that the work happened, under the network's published rule ([enrichment](enrichment.md)) |
| **Self-care** | Proof of life. A verified living human maintained itself ([debit-tolerance](debit-tolerance.md)) |
| **Essential care** (work that continues another person's life) | The network's published rule for that kind of care. The receiver does not have to confirm it. Where the receiver cannot confirm, a second witness does |

**Two rules stop this becoming a route for fraud.**

- **Verification asks whether the work happened, and whether a receiver accepted it. It never asks how much anyone valued it.** Letting credit depend on likes would make feedback a currency by the back door.
- **Weak evidence weighs near zero until something corroborates it**, inside a rule, never in place of one.

### Essential care is a published list

> **A network that counts some care as essential publishes the list, and an evidence rule for each entry on it.**

**Essential care is credited to the carer and adds no debit to the person cared for.** So an entry on the list is credit with no debit beside it, and its check must come from the evidence rule.

| The receiver | The evidence |
|---|---|
| Can confirm the care | The receiver's confirmation, as for any service |
| Cannot confirm it: an infant, an unconscious patient | A second witness, made on a different path. A hospital's admission record is one. Another carer's record is one |

**Worked, at a floor of `F` = 10 hours a day and a debit tolerance of ρ = 0.330.** Two adults each claim 14 hours a day of care for the other. That is 14 × 365 = 5,110 hours a year on top of 3,650 hours of floor credit.

| | Credit a year | New debit a year | Change in what each may carry |
|---|--:|--:|--:|
| Honest, floor only | 3,650 h | — | — |
| The pair, with the 14 hours on the essential list | 8,760 h | 0 h | 0.330 × 5,110 = **+1,686 h** |
| The pair, with the 14 hours counted as any other service | 8,760 h | 5,110 h | 1,686 − 5,110 = **−3,424 h** |

**In plain words: a false service that lands on the receiver costs each of the pair 3,424 hours a year. The same false service on the essential list gains each of them 1,686 hours.** A network that calls every service essential takes all service hours off its subscribers. The check on that is another network re-computing the claim through its own rules (below).

### Comparison, never conversion

**A network never converts another network's figures into its own.** Converting a balance from one model into another would set an exchange rate between two credit-standards, which is a medium of exchange and forbidden by A3. **A network with lax checking therefore cannot export the credit it issues**: whoever trades with its members discounts it. That guard depends on OP-22, because re-computing what a claim is drawn from means seeing it.

## An example, with the numbers

**A network publishes its rule for translation work: the translated text exists, and the client confirms receiving it.**

| | Hours worked | Against the rule | Hours credited |
|---|---|---|---|
| **A** delivers a translation and the client confirms | 20 h | met | **20 h** |
| **B** says they translated for 20 hours, with no text and no client | 20 h | not met | **0 h** |

**B is not being judged.** B knew the rule before starting. **Now change the network instead of the person.** A network may accept a different record of the client's agreement, such as an order signed before the work began. It writes a rule for that case. Once the rule exists, a translator who holds such an order and the finished text is credited 20 hours, not some fraction because a vague claim was weighted cautiously. **No rule can credit a service that nobody asked for.**

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
