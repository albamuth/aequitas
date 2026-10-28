---
title: OP-4 — the debit-tolerance formula
summary: The floor F and the tolerance ρ are each network's settings with a bound at each end; the band inside which essentials stay affordable and the gate still rations was measured and, at the US method, closes at a 2-hour floor on the broad essentials basket; but the formula was not derived, the band's upper edge halves under full pledging, and whether a network credits a child's learning time is a second dial on the same ceiling.
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

**At the US method the band is open at 10 and 14 hours a day, and closed at 2 hours on the broad essentials basket.** Re-measured on 2026-10-27 with each person's demand tied to the 1,380 h/yr anchor. The first run, on 2026-08-28, priced demand at 5,037 h/yr on the upper edge, so its edges were 3.65 times too high ([debit-tolerance](debit-tolerance.md)).

| `F` | ρ\*(`F`) | Largest essentials basket the floor can carry | Against a median American lifestyle |
|--:|--:|--:|--:|
| 2 h/day | 1.017 | 742 h/yr | 0.54× |
| 10 h/day | 0.330 | 1,205 h/yr | 0.87× |
| 14 h/day | 0.253 | 1,293 h/yr | 0.94× |

**Worked:** at 2 h/day the broad basket's 826 h needs ρ ≥ 826 ÷ 730 = 1.13, which is above 1.017, so no ρ works.

**ρ behaves like a prime rate.** A ρ can be chosen so demand matches capacity, and it moves sensibly: a 30% capacity disaster tightens it from about 1.2 to about 0.68, growth loosens it to about 2.2 ([disparity-ceiling](disparity-ceiling.md)).

## What is open

1. **The formula.** The band was found by sweeping, not derived from the axioms. Component C9 is not started.
2. **Pledging halves the upper edge.** Committed pledges can double a network's gate, so the publishable upper edge is `ρ*(F) ÷ (1 + p)`: at `F` = 10 it falls from 1.20 with no pledging to 0.60 at the one-for-one ceiling. And the band closes at `F` = 1 with essentials at 70% of a median lifestyle, the first swept cell where it ever has.
3. **The childhood dial.** Whether a network credits a child's learning time moves the reachable ceiling from 2.400× to 2.085× at `F` = 10. It belongs here and with A8's list of always-creditable activities.
4. **ρ\*'s absolute values inherit the weighting model and an illustrative capacity figure.** The shape is the result; the numbers are dated readings.
5. **The other production methods are not measured.** Under the German, Japanese or Spanish method the envelope covers all wants. Whether the band opens at 2 h/day there is inferred (a lower edge of 0.72–0.85, by scaling the basket by 0.64), and a run is requested. On a ledger rebuilt to birth the edges equal the one-day edges when past and future demand are both 1,380 h/yr, and that equality is built in. `06-simulation/stable-band/RESULTS_KAPPA.md`.

## An example, with the numbers

**At `F` = 10 and ρ = 1.2, with no pledging**, the floor alone balances 1.2 × 10 × 365 = **4,380 h** of debit a year against a median lifestyle of 1,380 h, so the gate does not bind: ρ = 1.2 is already above ρ\*(10) = 0.330. **Now let pledge density reach `p` = 1.** The same network's effective tolerance is 2 × 1.2 = 2.4, further above it, so the gate rations nothing and physical shortage is decided at the point of distribution instead. **A network must choose ρ knowing pledges can double its gate.**

## Depends on

- [debit-tolerance](debit-tolerance.md) · [disparity-ceiling](disparity-ceiling.md) · [pledge-and-signal](pledge-and-signal.md) · [protocol-governance](protocol-governance.md)

---
*Status: contested — band measured, formula not derived, pledge term swept only*
*Source: `00-strategy/Aequitas_Foundations.md` §5.5.3, §5.5.5; `00-strategy/Aequitas_Objections.md` status board and §C test 8; `06-simulation/stable-band/`*
