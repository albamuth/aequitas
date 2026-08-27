<!-- tag: cnf-aequitas-conformance -->
# Aequitas — Conformance Requirements

> **Version:** 0.2 · **Date:** 2026-08-25
> **Audience: implementers.** Anyone building a trust network.
> **Companion:** [`Aequitas_Foundations_v0.25.md`](Aequitas_Foundations_v0.25.md) — the system itself, and the argument for every row below. **Where the two differ, Foundations governs.**
> **Version history:** v0.1 (2026-08-25) extracted from Foundations §9. **v0.2 (2026-08-25) deleted requirement 17 by author ruling** — see §4.
> **Where this came from:** it was `Aequitas_Conformance_v0.2.md` from v0.18 to v0.23, and moved here on 2026-08-25 by author ruling. `Aequitas_Conformance_v0.2.md` also carried a restatement of §1.2, which was cut as redundant rather than moved.

---

<!-- tag: cnf-s1 -->
## 1. What this list is for

> **These documents state what must be true. They never state how to build it.**

Aequitas is an economic system, not a data-architecture project. A schema, a storage design, a transport protocol and a choice of cryptography are praxis, and they belong to whoever implements (Foundations §1.2).

**But an implementer is a real audience with a real need. Someone building a trust network has to know which system they are implementing.** That need is met by a list of things that must hold — never by an architecture.

> **The standing screening question is the dial test: if a principle survives at both ends of a dial, the dial is not part of the principle.** Conservation of mass and energy survives at both ends of every dial. A field name does not.

**An implementation is Aequitas if, and only if, every row in §2 holds.** Each is stated as a requirement rather than a design.

> **A requirement is a property an implementation *has*, never a result it must *achieve*.** §4 records the two things kept off this list on that ground, and why.

---

<!-- tag: cnf-s2 -->
## 2. What an implementation must satisfy

An implementation is Aequitas if, and only if, all of the following hold. Each is stated as a requirement rather than a design.

| # | Requirement | From |
|---|---|---|
| 1 | Every credit and debit records a real material or energy flow. **No issued, abstract, or fiat quantity exists anywhere.** | A1 |
| 2 | Flows are attributed to whoever **caused** them. Cost never passes to a party that did not act. | A1, §3.2b, §6.2a |
| 2a | A unit's debit-cost carries **only what that unit consumed.** A durable asset's creation-cost is held by the asset and its holders and is **never amortised into the things the asset was used to make.** The boundary is physical fate, audited by IC-4, never declared by the producer. | A5, §6.2a, §6.2b |
| 2b | **Nothing is added to a cost figure.** There is no margin, fee, or spread anywhere in the accounting. | A5 |
| 2c | **No account that is not a verified human is a final holder of debit.** An organisation's debit is at all times its members' debit, divided by hours worked for it. **Closing an organisation moves nothing and clears nothing.** | A1, §3.2c |
| 3 | Labour is **never rate-scaled.** Differences between workers resolve as material costs. | A2 |
| 4 | **Credit is never transferable** — not by gift, sale, loan, inheritance, or theft. Only debit moves, and only with the thing it attaches to. | A3 |
| 5 | Standing is **derived from an append-only record of events, never stored** as an authoritative balance. | A6 |
| 6 | **Records are never destroyed or edited.** A disputed record is annotated; a superseded one is added beside. | §5.1a, §5.4 |
| 7 | **Mass and energy conserve** across every recorded process, and every parcel has both an origin and a fate. | IC-1 … IC-4 |
| 8 | **No account claims more than 24 hours of activity per 24 hours.** | IC-7 |
| 9 | **Cumulative pledges never exceed lifetime earned credit**, 1:1. | IC-8, §6.4 |
| 10 | A debit is a **vector**. Any division is computed **per dimension, before collapsing** to a single figure. | §3.2a |
| 10a | A joint process's debit divides by **where the process physically sent its inputs**, measured at that facility for the period described, with a model used only where measurement is absent. The **method is published with its version**, so anyone can re-run it. **No split may depend on demand, desirability, or yield.** The method itself is the industry's to set, not this document's. | §3.4a, §1.2, §5.3b |
| 11 | The consumption gate is evaluated **at the moment of the transaction.** A later revision changes future room and never the validity of a completed act. | §3.3 |
| 12 | Every estimate carries its **basis, method, vintage and extent**, and may be superseded only by a **stronger** basis, never a weaker one. | §3.3, §5.1a |
| 13 | A quantity computed over **incomplete coverage is published as a floor**, with the gap named. | §5.1a, §7.4 of EventLog |
| 14 | Coverage is estimated over the **unmeasured residual**, never over the whole population. | §5.1b, §5.1d |
| 14a | Two figures are **subtracted only when they measure the same quantity, over the same boundary and window, within error bounds smaller than their difference.** Where they do not, the result is reported as a bound with the mismatch named. | §5.1b |
| 14b | A check that establishes coverage **compares two records made on separate paths.** Arithmetic over a single log establishes consistency and never completeness. | §5.1b, §4 |
| 14c | Every verification rung is **published with its running cost**, so a counterparty can see what a claim's assurance cost to produce. | §4, §5.3b |
| 15 | The coverage leftover is **computed, published, and charged to no account** until its causer onboards. | §5.1c |
| 16 | **Every estimating number and every method the implementer uses is published**, so anyone can re-run it. | §5.3b |
| 16a | **Every cost constant carries its method, its version, and its uncertainty interval**, and the implementer **states which constants it has not reviewed and how old each reading is.** | §3.3a, §5.1a |
| 16b | **A constant may re-weight history only after two unaffiliated replications.** Review is triaged by **magnitude × concentration of beneficiary**, never magnitude alone. **Membership composition is public**, so a network concentrated in the sector it audits is detectable. | §3.3a |
| 16c | **The implementer can show how it audits its cost constants.** *How* is its own design (§1.2); **having no answer is not conforming.** | §3.3a, §1.2 |

## 3. What this list does not carry

| Not here | Where it belongs |
|---|---|
| Field names, record shapes, schema versions | The implementer |
| Storage, indexing, backups, key management | The implementer (§1.2) |
| Transport protocol and choice of cryptography | The implementer (§1.2) |
| Privacy practice | A network choice (§5.3a) |
| The values of ρ and the self-care floor `F` | Network dials (§3.5, §6.1b, A8) |
| Corporate form, jurisdiction, compliance posture | The implementer (§1.2) |

---

<!-- tag: cnf-not-requirements -->
## 4. Two things that are deliberately not on this list

**A requirement here is a property an implementation *has*. It is never a result an implementation must *achieve*.** The difference decides what belongs.

#### Essential provision is not a conformance requirement

**Foundations §7.5.4 rules that essentials are affordable to everyone alive**, because the floor credits the hours of staying alive and is set large enough to cover what staying alive costs. **That is true of the system. It is not a test an implementation passes.**

There was a row 17 saying so, from Foundations v0.18 to v0.23 and briefly here. **It was deleted on 2026-08-25 by author ruling**, on this ground:

> **Requiring it would be like saying that to conform to Aequitas, a network must succeed at a stated political goal.**

**Whether essentials are actually affordable in a given network depends on three things this list cannot check:** the value that network sets for its floor `F`, the value it sets for ρ, and what its real economy can physically deliver. **All three are dials or physical facts, not properties of an implementation** (Foundations §7.5.3, A8). A network can be built exactly to this list and still set `F` too low, and no reading of its code would say so.

**Nothing is lost from the theory.** The rule stands where it belongs, in Foundations §7.5.4, as a statement of how the system works. **Setting `F` and ρ so that it comes true is the network's job**, and the open problem of finding a stable band for them is **OP-4** in the objections register.

*(Every other row was checked against the same test in the same pass. **16c** is the closest call — *the implementer can show how it audits its cost constants* — and it survives, because showing a design is something an implementation either does or does not do. It does not require the audit to work.)*

#### "One verified human = one account" is not here either

Foundations §5.1 states it, and the **OP-22 ruling of 2026-08-25** makes it a rule each network applies to its own members rather than a requirement holding across networks — so it stays in §5.1 and is deliberately absent here. Record: [`OP-22_identity_not_disclosure_v0.2.md`](OP-22_identity_not_disclosure_v0.2.md) §11, row 3a.

---

*End of v0.2.*
