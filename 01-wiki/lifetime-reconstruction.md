---
title: Lifetime reconstruction
summary: When a person joins, their position is rebuilt back to their birth on both sides, credit and debit; the estimate is the default and evidence is voluntary, an undisclosed period is estimated over the undisclosed leftover and errs against the person, the declared span is set back to the earliest date the evidence allows, and for a median person joining is a windfall.
type: mechanism
ids: [§4.4, §4.8]
status: settled
edges:
  - {rel: depends_on, to: statistical-coverage}
  - {rel: depends_on, to: one-account-per-person}
  - {rel: depends_on, to: unassigned-residual}
  - {rel: depends_on, to: record-beats-estimate}
  - {rel: depends_on, to: debit-tolerance}
  - {rel: implies, to: onboarding-incentive}
  - {rel: implies, to: permanence-and-death}
  - {rel: constrained_by, to: IC-7}
  - {rel: constrained_by, to: "Conformance row 14e"}
  - {rel: constrained_by, to: "Conformance row 17a"}
  - {rel: open_under, to: OP-22}
  - {rel: related, to: op-22}
  - {rel: open_under, to: OP-14}
  - {rel: open_under, to: OP-15}
  - {rel: source, to: "Foundations §4.4"}
  - {rel: source, to: "Foundations §4.8"}
  - {rel: source, to: "Overview §7"}
  - {rel: source, to: 00-strategy/papers/Onboarding_the_wealthy.md}
---
# Lifetime reconstruction

> **Version:** 0.1
> **Date:** 2026-10-14

> **When a person joins, their position is reconstructed back to their birth.** Not to the network's founding, not to the joining date. A whole life, on both sides: **the debit and the credit are both rebuilt.**

## The words this page uses

| Term | What it means |
|---|---|
| **Declared span** | How long the person says they have lived. It decides how many years the reconstruction rebuilds. |
| **The floor**, `F` | The hours a day the network counts as the work of staying alive ([debit-tolerance](debit-tolerance.md)). |
| **The gate** | `D ≤ ρ·(C + P)`, where ρ is the network's debit tolerance. |
| **Undisclosed leftover** | The periods of a life the person supplied no evidence for, estimated as a pool of their own rather than from the population. |

## The rule

**That sounds punitive and is the opposite, for one reason that has to come first.** Every living human accrues credit for the hours they spend keeping themselves alive, so a lifetime reconstruction brings a lifetime of that credit with it.

**The estimate is the default, and evidence is voluntary.** A person supplies whatever narrows it, where they were born, how long they lived in each place, which jobs they held, which vehicles they owned, and accepts the estimate for every period they leave undisclosed. Details may arrive years later and the position re-derives, because nothing is stored (A6).

**Three conditions, and without any one of them this breaks.**

1. **An undisclosed period is estimated over the undisclosed leftover, not over the whole population.** Otherwise a person who documents only their flattering years free-rides forever on an average their own silence inflates. Selective disclosure is expected and is not an exploit, provided this holds ([unassigned-residual](unassigned-residual.md)).
2. **An estimate errs against the person, on both sides.** Debit at the unfavourable end, credit at the conservative end, so supplying evidence always pays whichever way the truth lies.
3. **The declared span is a record, set by one published rule: back to the earliest date the available evidence permits.** An assertion is not evidence ([record-beats-estimate](record-beats-estimate.md)).

**Why condition 3 names a date and not a direction.** Each declared year opens `ρ·F·365` hours of room and adds about 1,380 hours of consumption. Break-even is `ρ·F` = 1,380 ÷ 365 = **3.78 hours a day**. Above it a longer span pays the filer; below it a shorter one does, and both settings are conforming. *The earliest date the evidence allows* is the same instrument on both sides of 3.78.

| The network | Room a year opens | Debit a year adds | An honest year is worth |
|---|--:|--:|--:|
| `F` = 10, ρ = 1.2 | 4,380 h | 1,380 h | **+3,000 h** |
| `F` = 2, ρ = 1.0 | 730 h | 1,380 h | **−650 h** |

**Subsistence is exempt and must stay exempt.** The floor is not an estimate; it is credit for a lived day, attested by proof of life. So condition 2 never reaches it, and a person who cannot document a life is not impoverished by this rule.

## An example, with the numbers

**A median person joins at forty**, in a network at `F` = 10 and ρ = 1.2. A median lifestyle commands about 1,380 hours of other people's labour a year; being alive earns 3,650.

| | Hours |
|---|--:|
| Estimated lifetime credit, 40 × 3,650 | **146,000** |
| Estimated lifetime consumption, 40 × 1,380 | **55,200** |
| Room at joining, 1.2 × 146,000 − 55,200 | **120,000** |

**In plain words: joining is a windfall for a median person, and that is the adoption incentive computed rather than asserted.** The people for whom a full reconstruction is costly are those whose lifetime consumption genuinely exceeded their lifetime contribution. Earlier real contributions enter the record at the dates they occurred, not the joining date.

## Two rules this looks like it breaks, and does not

A non-participant is never charged for an estimated position, and nothing is charged until they join, which is voluntary. And a revision never invalidates a completed act, because acts before joining were never gated by any network.

## What stays open

**This raises the stakes on OP-22.** A whole-life record is a dossier: birthplace, every residence, employment, commuting, vehicles. Disclosure is voluntary, but the incentive runs toward disclosing, so the arrangement puts steady pressure on people to assemble exactly the record a surveillance state would want. **Registered, not solved.** Cohort shopping (OP-14) and estimated credit accruing to non-joiners and the dead (OP-15) are stated, not worked.

## Depends on

- [statistical-coverage](statistical-coverage.md) · [one-account-per-person](one-account-per-person.md) · [unassigned-residual](unassigned-residual.md) · [record-beats-estimate](record-beats-estimate.md) · [debit-tolerance](debit-tolerance.md)

## Consequences

- [onboarding-incentive](onboarding-incentive.md) — why joining pays
- [permanence-and-death](permanence-and-death.md) — the record, once built, is never destroyed

---
*Status: settled (the three conditions) · OP-22 open (the dossier)*
*Source: `00-strategy/Aequitas_Foundations.md` §4.4 (when a person joins), §4.8 (joining replaces an assigned average); `Aequitas_Conformance.md` rows 14e, 17a*
