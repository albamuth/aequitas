---
title: OP-4 — the debit-tolerance formula
summary: The floor F and the tolerance ρ are each network's settings with a bound at each end; the band inside which essentials stay affordable and the gate still rations was measured and never closes between 1 and 14 hours a day, but the formula was not derived, the band's upper edge halves under full pledging, and whether a network credits a child's learning time is a second dial on the same ceiling.
type: open-problem
ids: [OP-4]
status: contested
edges:
  - {rel: depends_on, to: debit-tolerance}
  - {rel: depends_on, to: disparity-ceiling}
  - {rel: depends_on, to: pledge-and-signal}
  - {rel: depends_on, to: protocol-governance}
  - {rel: related, to: open-problems}
  - {rel: tested_by, to: 06-simulation/stable-band/RESULTS.md}
  - {rel: tested_by, to: 06-simulation/stable-band/PLEDGE_BAND_RESULTS.md}
  - {rel: tested_by, to: 06-simulation/essentials-basket/RESULTS.md}
  - {rel: source, to: "Foundations §5.5.3"}
  - {rel: source, to: "Foundations §5.5.5"}
  - {rel: source, to: "Objections §C"}
---
# OP-4 — the debit-tolerance formula

> **Version:** 0.1
> **Date:** 2026-10-14

> **🟠 Open. The band was measured; the formula was not derived.** There is no single global debit-to-credit ratio, because total debit always exceeds total credit and A8 forbids an expert-set one. What a network sets is a per-person tolerance ρ and a floor `F`, **and the question is what values work.**

## The words this page uses

| Term | What it means |
|---|---|
| **The floor**, `F` | Hours a day the network counts as the work of staying alive. |
| **ρ** ("rho") | The multiplier in the gate `D ≤ ρ·(C + P)`. |
| **`E`** | What a year of essentials commands, in hours of other people's labour. |
| **ρ\*(`F`)** | The tolerance above which the gate stops rationing anything, at a given floor. |
| **`p`** | Pledge density: how much of the population's pledge budget is committed. Swept, not measured. |

## What is settled

**The lower bound is arithmetic:** `ρ · F · 365 ≥ E`. Measured for one US person, a broad essentials basket costs 826 to 965 h/yr, so the lowest floor at ρ = 1.2 is 1.9 to 2.2 h/day. **A network at `F` = 1 h/day has subscribers who cannot afford to eat.**

**The band exists and never closes.** Run on 2026-08-28 across 60,000 people and 6,237 grid cells: at every floor from 1 to 14 hours a day there is a range of ρ inside which essentials are affordable and the gate still rations. What binds it is what the economy can physically deliver, not affordability ([debit-tolerance](debit-tolerance.md)).

| `F` | ρ\*(`F`) | Largest essentials basket the floor can carry | Against a median American lifestyle |
|--:|--:|--:|--:|
| 2 h/day | 3.70 | 2,701 h/yr | 1.96× |
| 10 h/day | 1.20 | 4,380 h/yr | 3.17× |
| 14 h/day | 0.90 | 4,599 h/yr | 3.33× |

**ρ behaves like a prime rate.** A ρ can be chosen so demand matches capacity, and it moves sensibly: a 30% capacity disaster tightens it from about 1.2 to about 0.68, growth loosens it to about 2.2 ([disparity-ceiling](disparity-ceiling.md)).

## What is open

1. **The formula.** The band was found by sweeping, not derived from the axioms. Component C9 is not started.
2. **Pledging halves the upper edge.** Committed pledges can double a network's gate, so the publishable upper edge is `ρ*(F) ÷ (1 + p)`: at `F` = 10 it falls from 1.20 with no pledging to 0.60 at the one-for-one ceiling. **The ρ = 1.2 used throughout the documents sits exactly at the edge with no pledging and above it with any.** And the band closes at `F` = 1 with essentials at 70% of a median lifestyle, the first swept cell where it ever has.
3. **The childhood dial.** Whether a network credits a child's learning time moves the reachable ceiling from 2.400× to 2.085× at `F` = 10. It belongs here and with A8's list of always-creditable activities.
4. **ρ\*'s absolute values inherit the weighting model and an illustrative capacity figure.** The shape is the result; the numbers are dated readings.

## An example, with the numbers

**At `F` = 10 and ρ = 1.2, with no pledging**, the floor alone opens 1.2 × 10 × 365 = **4,380 h** of room a year against a median lifestyle of 1,380 h, so the gate does not bind. **Now let pledge density reach `p` = 1.** The same network's effective tolerance is 2 × 1.2 = 2.4, above ρ\*(10) = 1.20, so the gate rations nothing and physical shortage is decided at the point of distribution instead. **A network must choose ρ knowing pledges can double its gate.**

## Depends on

- [debit-tolerance](debit-tolerance.md) · [disparity-ceiling](disparity-ceiling.md) · [pledge-and-signal](pledge-and-signal.md) · [protocol-governance](protocol-governance.md)

---
*Status: contested — band measured, formula not derived, pledge term swept only*
*Source: `00-strategy/Aequitas_Foundations.md` §5.5.3, §5.5.5; `00-strategy/Aequitas_Objections.md` status board and §C test 8; `06-simulation/stable-band/`*
