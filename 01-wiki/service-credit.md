---
title: Service
summary: A service is work done for a person, an organisation or oneself, often with nothing to hand over; it credits one hour for one hour like any other work, the check is the client's confirmation, and keeping yourself alive is a service a network may recognise.
type: mechanism
ids: [§2.3]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: time-as-yardstick}
  - {rel: depends_on, to: non-fungibility}
  - {rel: implies, to: debit-tolerance}
  - {rel: implies, to: no-taxation}
  - {rel: implies, to: regulator-inversion}
  - {rel: constrained_by, to: IC-7}
  - {rel: open_under, to: OP-1}
  - {rel: source, to: "Foundations §2.3"}
  - {rel: source, to: "Foundations §4.2"}
  - {rel: source, to: "Foundations §4.5"}
  - {rel: source, to: "Foundations §5.5.2"}
  - {rel: source, to: "Overview §2"}
---
# Service

> **Version:** 0.2
> **Date:** 2026-10-14

> **A service is something done for a person, an organisation, or oneself, often with nothing to hand over.** It is one of three names a trust network uses to decide whether an hour counts as work. It is not a kind of credit. **There is one credit, time spent, and a service hour credits exactly as a production hour does.**

## The words this page uses

| Term | What it means |
|---|---|
| **Credit** | A record that a person spent an hour of their life on work. It belongs to one person and never moves ([non-fungibility](non-fungibility.md)). |
| **Trust network** | The organisation that keeps the books, publishes which activities it credits, and checks claims (Foundations §4.0). |
| **The three names** | [Production](production-credit.md), service and [enrichment](enrichment.md). An activity is creditable if it is at least one of the three (Foundations §2.3). |
| **The floor**, written `F` | The hours a day a network counts as the work of keeping a human being alive (Foundations §5.5.1). |
| **IC-7** | The integrity check that stops any account claiming more than 24 hours of activity in 24 hours. |

## What it is

**A service is the name for work whose output is not an object.** A nurse, a teacher, a bus driver and a city planner all spend hours and leave nothing to hand on. Under the three-name rule that does not matter: the hour is creditable because it is a service, and it credits at one hour for one hour (Foundations §2.3, A2).

**"For oneself" is in the definition on purpose.** Sleeping, eating, washing and other bodily upkeep are services a person does for themselves. A network may recognise them as work. Where it does, those hours credit like any other recognised hours, at the network's published duration for each activity. That is where the floor comes from ([debit-tolerance](debit-tolerance.md)), and it is the ordinary rule rather than a special one.

**A network credits no kind of work for which it has published no evidence rule** (Foundations §4.2). For a service the usual evidence is that the client confirms it happened. For self-care it is proof of life.

### An example, with the numbers

A network publishes its rule for translation work: **the translated text exists, and the client confirms receiving it.**

| | Hours worked | Against the published rule | Hours credited |
|---|---|---|---|
| **A** delivers a translation and the client confirms | 20 h | Rule met | **20 h** |
| **B** says they translated for 20 hours, with no text and no client | 20 h | Rule not met | **0 h** |

**B is not being punished.** B knew the rule before starting, because the network published it. If the network wants to credit translation for clients who cannot confirm, it writes a rule for that case, and then B's 20 hours credit at 20 hours.

**Now the self-care case, at `F` = 10.** A network counts 8 hours of sleep, 1 of eating, 0.5 of washing and 0.5 of other upkeep. A person who sleeps 8, eats 1, washes 1 and works 8 hours as a nurse records **10 + 8 = 18 hours** that day. A person who claims all 24 hours as self-care is capped at **24** by IC-7 and credited only for the activities the network published a rule for, so **10**.

## Two things a service hour does not do

- **It does not earn more than another hour.** A doctor's hour and an orderly's hour credit the same. The doctor's training was credited and carried when it happened ([education-as-credited-work](education-as-credited-work.md)), so nothing about it reaches the patient's bill.
- **It does not buy more say.** Every counted hour, whatever its name, adds equally to the person's lifetime pledge budget ([pledge-and-signal](pledge-and-signal.md)). A service hour buys no more influence than a production hour and no less.

**Essential provision is unconditional on the provider's side.** A counsellor is credited for the hours they worked, because credit is decided by the network's published evidence rule and never by the recipient's standing. Nobody is made to means-test before helping.

## Who games this

- **Claiming service hours nobody can check.** An unwitnessed claim is recorded, because A7 requires everything to be recorded, but it carries the weakest basis and a cautious weighting values it near zero (Foundations §4.5). A claim matching no published rule credits nothing.
- **A network declaring loyalty to itself a service.** It cannot. Loyalty is not production, not a service and not enrichment, so there is nothing to credit (Foundations §2.3). A network can still stretch the list a long way, which is why the list of always-credited activities is a published capture surface worked under OP-10.
- **Manufacturing hours by colluded confirmations.** Two people confirming each other's phantom services are capped by IC-7 at 24 hours a day each, and every hour claimed is visible in the log. The residue, how any credit becomes say without collusion inflating it, is **OP-1 (service → influence)** and is open.

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md) · [non-fungibility](non-fungibility.md)

## Consequences

- [debit-tolerance](debit-tolerance.md) — the floor is self-care credited as a service done for oneself
- [no-taxation](no-taxation.md) — civil servants are credited directly for service hours
- [regulator-inversion](regulator-inversion.md) — a regulator's advice is a service businesses want

---
*Status: settled (the rule) · OP-1 open (service → influence)*
*Source: `00-strategy/Aequitas_Foundations.md` §2.3 (what counts as work; keeping yourself alive), §4.2 (the evidence rule, the translation example), §4.5 (it credits work), §5.5.2 (the floor follows from the axioms)*
