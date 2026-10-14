---
title: Enrichment
summary: Enrichment is work in which knowledge, skill or culture reaches somebody; it is one of three names that decide whether an hour is creditable, it credits one hour for one hour, and it is verified by evidence the work happened, never by how many people liked it, because feedback is not credit.
type: mechanism
ids: [§2.3, OP-8]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: time-as-yardstick}
  - {rel: depends_on, to: non-fungibility}
  - {rel: implies, to: education-as-credited-work}
  - {rel: implies, to: meme-tracing}
  - {rel: implies, to: pledge-and-signal}
  - {rel: constrained_by, to: IC-7}
  - {rel: open_under, to: OP-6}
  - {rel: open_under, to: OP-10}
  - {rel: source, to: "Foundations §2.3"}
  - {rel: source, to: "Foundations §4.2"}
  - {rel: source, to: "Foundations §4.5"}
  - {rel: source, to: "Foundations §4.6"}
  - {rel: source, to: "Overview §2"}
  - {rel: source, to: "Overview §5"}
---
# Enrichment

> **Version:** 0.2
> **Date:** 2026-10-14

> **Enrichment is work in which knowledge, skill or culture reaches somebody.** Teaching, learning, research, writing, art, childcare. It is one of three names a trust network uses to decide whether an hour counts as work. It is not a kind of credit and it is not a social-value signal. **There is one credit, time spent, and an enrichment hour credits exactly as any other hour does.**

## The words this page uses

| Term | What it means |
|---|---|
| **Credit** | A record that a person spent an hour of their life on work. It belongs to one person and never moves ([non-fungibility](non-fungibility.md)). |
| **The three names** | [Production](production-credit.md), [service](service-credit.md) and enrichment. An activity is creditable if it is at least one of the three (Foundations §2.3). |
| **Feedback** | How a society signals what it wants more of: a stock-out, a referral, applause, a like. **It is not credit and never converts into credit** (Foundations §4.6). |
| **Pledge** | A permanent grant of debit-room, backed one hour for one hour by credit the pledger already earned ([pledge-and-signal](pledge-and-signal.md)). |

## What it is

**Enrichment is named separately for one reason: to give grounds for crediting work no economy has ever credited.** Going to school is work, and today the student or their parents pay for it. Teaching your own child is work. Caring for a relative is work. None of it is paid today, and all of it passes the threshold (Foundations §2.3). **Childcare alone brings the largest uncounted labour pool in history onto the books** (Foundations §4.5).

**The name decides whether an hour counts. It never decides how much.** An hour of teaching and an hour of bricklaying both credit one hour (A2). An apprentice plumber's hour is production, a service and enrichment at once, and it credits as **1 hour**, not 3.

**How it is checked.** A network publishes what evidence each kind of work needs (Foundations §4.2). For enrichment the evidence is **that the work happened**: the lesson was given, the paper exists, the mural is on the wall.

> **Verification asks whether the work happened. It never asks whether anyone valued it.** Letting credit depend on likes, citations or applause is forbidden, because it would make feedback a currency by the back door (Foundations §4.2, §4.6).

## Feedback is not credit, and there is nothing to firewall

**Feedback was never credit, so it cannot convert into credit.** A like, a review, a referral or a stock-out tells a society what it wants more of. The thing that carries real backing is a pledge, and a pledge is spent from a finite lifetime budget equal to the pledger's own earned hours.

### An example, with the numbers

**An artist spends 40 hours painting a street mural and posts a photograph. 5,000 people like it.**

| | Hours |
|---|--:|
| Credit for the 40 hours of painting, once the network's evidence rule is met | **40 h**, and no more however many likes arrive |
| Credit from the 5,000 likes | **0 h.** A like is feedback |
| Room raised, if each liker's app pledges 0.1 h from their own budget | 5,000 × 0.1 = **500 h** of debit-room for the artist |
| What the next mural needs in paint and travel | **300 h** |
| Left over | **200 h** of room the artist can use |

**In plain words: the likes turned into room only because 5,000 people each spent a tenth of an hour of their own finite pledge budget.** Nobody's credit moved, and the artist's 40 hours did not grow. That is the universal rule for how popularity reaches a creator, and it is the same whether the work is a mural, a film, or a theorem.

**The same rule pays for creative work up front.** A film's crew are credited during production, and the people who wanted the film pledge for it then. The audience pays for delivery only ([education-as-credited-work](education-as-credited-work.md) states the front-loading rule). **A popular film cannot gouge its audience, because there is no mechanism by which it could** (Overview §5).

## Who games this

- **Stretching the word.** A network cannot declare loyalty to itself enrichment, because loyalty passes none of the three names. **It can still stretch enrichment a long way**, and nothing here stops it. Three structural defences carry the rest: competing networks and ratio-based evaluation, a public membership list, and the published evidence rule. This is **OP-10 (weighting governance)** wearing different clothes (Foundations §2.3).
- **Claiming thinking hours nobody can see.** Recorded, as A7 requires, but weighed near zero until something corroborates it, and capped by IC-7 at 24 hours a day (Foundations §4.5).
- **Buying feedback.** If a signal could be bought it would be a currency by the back door. Whether feedback can be bought is **OP-6 (feedback mechanics)** and is open. What bounds it is that a pledge costs a real person a real hour from a budget that cannot be manufactured.
- **A popularity contest.** Whoever is already liked attracts the most pledges. That is OP-6 too, registered and not solved. A first-time creator attracts no pledges, and the documents say so rather than assuming it away (Foundations §4.5).

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md) · [non-fungibility](non-fungibility.md)

## Consequences

- [education-as-credited-work](education-as-credited-work.md) — schooling and childcare are enrichment, credited from the first day
- [meme-tracing](meme-tracing.md) — attribution of ideas is recognition, never credit
- [pledge-and-signal](pledge-and-signal.md) — where feedback goes instead of into credit

## Prior art

- [post-scarcity](post-scarcity.md) — Saadia's Star Trek reading, where reputation replaces money as motivation. Use it to make the goal vivid, never as evidence.

---
*Status: settled (the rule) · OP-6 open (feedback mechanics)*
*Source: `00-strategy/Aequitas_Foundations.md` §2.3 (what counts as work; why enrichment is named separately), §4.2 (verification never asks whether anyone valued it), §4.5 (what enrichment covers; work nobody can observe), §4.6 (feedback is not credit)*
