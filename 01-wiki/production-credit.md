---
title: Production
summary: Production is one of the three names (production, service, enrichment) that decide whether an hour is creditable, never how much it credits; there is one credit, time spent, and a made thing's hours start counting when the thing changes hands.
type: mechanism
ids: [§2.3]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: time-as-yardstick}
  - {rel: depends_on, to: non-fungibility}
  - {rel: implies, to: property-debit}
  - {rel: implies, to: debit-tolerance}
  - {rel: constrained_by, to: IC-5}
  - {rel: constrained_by, to: IC-7}
  - {rel: source, to: "Foundations §2.3"}
  - {rel: source, to: "Foundations §4.2"}
  - {rel: source, to: "Foundations §4.5"}
  - {rel: source, to: "Foundations §4.6"}
  - {rel: source, to: "Overview §2"}
---
# Production

> **Version:** 0.2
> **Date:** 2026-10-14

> **Production is work that turns matter or energy into something.** It is one of three names a trust network uses to decide whether an hour counts as work at all. It is not a kind of credit. **There is one credit, time spent, and it credits one hour for one hour whichever name applies.**

## The words this page uses

| Term | What it means |
|---|---|
| **Credit** | A record that a person spent an hour of their life on work. It belongs to one person and never moves ([non-fungibility](non-fungibility.md)). |
| **Trust network** | The organisation that keeps the books, publishes which activities it credits, and checks claims (Foundations §4.0). |
| **The three names** | Production, [service](service-credit.md) and [enrichment](enrichment.md). An activity is creditable if it is at least one of the three (Foundations §2.3). |
| **Hand-off** | One person giving another a physical thing. The debit riding with the thing goes too (Foundations §2.4). |

## What it is

**The three names are a threshold, not a filing system.** A trust network may credit an activity only if it is at least one of production, a service, or enrichment. Which one it is, is never recorded, and it never changes the figure.

| | What it means | An example |
|---|---|---|
| **Production** | Matter or energy is turned into something | Milling wheat into flour |
| **A service** | Something is done for a person, an organisation, or oneself | Setting a broken arm |
| **Enrichment** | Knowledge, skill or culture reaches somebody | Teaching a child to read |

**An hour that is all three is still one hour.** An apprentice plumber's hour turns copper into working plumbing (production), fixes a customer's pipes (a service), and teaches the apprentice a trade (enrichment). **It credits as 1 hour, not 3.** Splitting it would need a convention nobody can measure ([physical-trace-test](physical-trace-test.md)), and there is no reason to want one.

> **No rule may credit production at one rate and enrichment at another, or divide a single hour between them** (Foundations §2.3, §4.5).

## What is particular to a made thing

**The check is the hand-off.** A network publishes what evidence each kind of work needs (Foundations §4.2). For goods the evidence is the hand-off itself: the receiver accepts the thing and the debit that rides with it, which attests that the thing exists. **No second act is needed, so for goods the basic check costs nothing** ([verification-ladder](verification-ladder.md)).

**Three things follow** (Foundations §4.6):

- **Credit counts at the first hand-off to any receiver.** No downstream buyer can hold a maker's credit hostage. And because debit follows possession, a middleman sitting on goods is sitting on their debit, so they are pushed to pass them on.
- **The count checks itself.** A receiver takes on the debit of exactly what they accept, so they never sign for units that do not exist. The party harmed by an error is the party who catches it.
- **Unsold goods are a risk the makers share by hours worked.** Unsold goods are unrealised credit plus inventory debit on whoever holds them. In speculative production that falls on everyone who worked the run, by hours and never by rank. Pledged production removes the risk that backing is withdrawn, not the risk that nobody takes the finished thing.

### An example, with the numbers

A workshop of **10 people** spends **40 hours each** making **200 toasters**, using **2 kg** of steel and plastic per toaster. A driver collects the batch.

| | Before the hand-off | At the hand-off |
|---|---|---|
| The makers' hours | 10 × 40 = **400 h**, recorded but not yet counting | **400 h counts**, 40 h on each maker's ledger |
| The toasters' material | 200 × 2 = **400 kg**, property debit on the workshop | **400 kg moves to the driver** with the toasters |
| The toasters' making-hours | 400 h of creation cost on the asset | The driver, as a carrier, takes **no share** of the making. Only their own driving hours and fuel are added (Foundations §4.5) |

**In plain words: the driver's acceptance is what turns 400 recorded hours into 400 counted hours, and nothing else was needed.** If the workshop had made 220 toasters and recorded 200, the driver would have refused to sign for 20 that were not there, because signing takes on their debit.

## Who games this

- **Claiming hours for things that were never made.** Nothing counts until a receiver accepts the output, and the receiver pays for every unit they accept. A colluding receiver can sign for phantom toasters, but then carries 2 kg of phantom debit each, and IC-7 caps what any account can claim at 24 hours a day. The residue is collusive hand-offs manufacturing gross hours, which is OP-1.
- **Calling a dull or dangerous job "production" to earn more.** There is no more to earn. The name decides whether the hour counts, never how much. Backing for unwanted work comes from people pledging more for it ([pledge-and-signal](pledge-and-signal.md)).

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md) · [non-fungibility](non-fungibility.md)

## Consequences

- [property-debit](property-debit.md) — what the receiver takes on at the hand-off
- [debit-tolerance](debit-tolerance.md) — every counted hour raises what the gate lets a person carry

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §2.3 (what counts as work), §4.2 (the evidence rule), §4.5 (it credits work), §4.6 (for goods, the hand-off is the verification)*
