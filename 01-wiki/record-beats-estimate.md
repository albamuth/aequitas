---
title: A record beats an estimate
summary: A record comes from an observation or attestation and an estimate from a published method; a record replaces an estimate and never the reverse; no record is ever deleted or edited, only annotated or superseded beside the original; and a network publishes, before anyone joins, how a correction is asked for.
type: mechanism
ids: [§4.4]
status: settled
edges:
  - {rel: depends_on, to: derived-ledger}
  - {rel: depends_on, to: statistical-coverage}
  - {rel: depends_on, to: trust-network}
  - {rel: implies, to: retroactive-reweighting}
  - {rel: implies, to: lifetime-reconstruction}
  - {rel: implies, to: dispute-resolution}
  - {rel: implies, to: permanence-and-death}
  - {rel: constrained_by, to: "Conformance row 6"}
  - {rel: constrained_by, to: "Conformance row 6a"}
  - {rel: constrained_by, to: "Conformance row 12"}
  - {rel: source, to: "Foundations §4.4"}
  - {rel: source, to: "Overview §7"}
  - {rel: source, to: "Objections B18"}
---
# A record beats an estimate, and nothing is ever deleted

> **Version:** 0.1
> **Date:** 2026-10-14

> **A record replaces an estimate. An estimate may never replace a record.** A record is never purged and never edited: a figure found wrong is contested by appending a dated, attributed note, and a figure with a better replacement is superseded by adding the better one beside it.

## The words this page uses

| Term | What it means |
|---|---|
| **Record** | A figure that came from an observation or an attestation. |
| **Estimate** | A figure that came from a published method, used where no record exists. |
| **Contested** | A dated, attributed note is appended saying the record is wrong. The record stays. |
| **Superseded** | A better record is added beside the old one. Both stay. |
| **Basis** | What a figure rests on: recalled, testified, logged, instrumented, modelled. A figure may be replaced only by one with a stronger basis. |

## The rule

**Saying a figure is so does not make it a record.** An assertion is not evidence. A person's estimated position only starts acting on what they may consume once they hold a verified account and observation has replaced the estimate ([one-account-per-person](one-account-per-person.md)).

**A falsehood is not prevented at the moment of writing.** It is made permanent and traceable, and it is exposed by arithmetic the moment any part of what it describes is measured. This is how a scientific literature handles a wrong result, and it is the only method that needs no authority standing at the door deciding what may be written down.

**A network publishes how a correction is asked for.** A rule saying what happens to a wrong record is no use to somebody who cannot get one looked at. The procedure covers three different problems wearing one word: a **mistake** (the quantity is wrong), **bad data** (the instrument or source was faulty), and **fraud** (the event did not happen). Four properties any procedure must have:

1. It is published and readable before a person joins.
2. It says who may raise a correction, and on what evidence.
3. It says what happens to the record while the correction is open.
4. Every correction is dated, attributed and appended. Nothing is deleted.

**What the procedure is, is the network's design. That one exists and is published is not optional** (conformance row 6a).

## An example, with the numbers

**A person joins at forty, and the network estimates their declared span back to the earliest date its evidence permits.** At `F` = 10 h/day and ρ = 1.2, each declared year's credit balances 1.2 × 10 × 365 = **4,380 hours** of debit and adds about **1,380 hours** of consumption, so an honest year is worth **+3,000 hours** a person may carry.

**Eight years later a baptismal register turns up showing they were born three years later than the estimate.**

| | |
|---|---|
| The original estimated span | **not edited, not deleted** |
| The register | **appended beside it**, dated and attributed |
| The person's position | **re-derived from the log**, so 3 × 3,000 = **9,000 hours** a person may carry come off |
| What the procedure decided | who could file the register, and what the books did for the eight years in between |

**In plain words: the append-only rule settles where the record ends up, and the procedure settles how it got looked at.** Without the second, the first describes an outcome nobody can reach.

**And the gate is checked at the moment of the transaction.** A correction changes what a person may carry in future; it never makes a completed purchase invalid ([retroactive-reweighting](retroactive-reweighting.md), conformance row 11).

## Depends on

- [derived-ledger](derived-ledger.md) · [statistical-coverage](statistical-coverage.md) · [trust-network](trust-network.md)

## Consequences

- [retroactive-reweighting](retroactive-reweighting.md) — recomputation is the normal state, not a repair
- [lifetime-reconstruction](lifetime-reconstruction.md) — evidence supplied later re-derives the position
- [dispute-resolution](dispute-resolution.md) — fraud is corrected by negation, never by reversal
- [permanence-and-death](permanence-and-death.md) — the same rule applied to a whole person

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §4.4 (a record always beats an estimate; records are annotated, never deleted; a network publishes how a correction is asked for); `Aequitas_Conformance.md` rows 6, 6a, 12; `Aequitas_Objections.md` B18*
