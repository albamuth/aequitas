---
title: The books never balance
summary: Total debit exceeds total credit permanently, because every real process wastes something; no mechanism may require global balance, sums are meaningless, and two separate numbers matter instead, a person's ratio of debit to credit and their absolute credit.
type: mechanism
ids: [§3.5]
status: settled
edges:
  - {rel: depends_on, to: material-flow-value}
  - {rel: depends_on, to: non-fungibility}
  - {rel: depends_on, to: derived-ledger}
  - {rel: implies, to: debit-tolerance}
  - {rel: implies, to: co-product-allocation}
  - {rel: implies, to: capitalism-cannot-function}
  - {rel: constrained_by, to: "Conformance row 10c"}
  - {rel: tested_by, to: 06-simulation/scenario-suite/RESULTS.md}
  - {rel: tested_by, to: 06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md}
  - {rel: tested_by, to: 06-simulation/median-lifestyle/Q6.md}
  - {rel: source, to: "Foundations §3.0"}
  - {rel: source, to: "Foundations §3.5"}
  - {rel: source, to: "Overview §2"}
---
# The books never balance, and must not

> **Version:** 0.1
> **Date:** 2026-10-14

> **Total debit exceeds total credit, everywhere, permanently, by construction.** Credit records useful work; debit records material and energy consumed plus pollution; every real process dissipates. **A set of books that balanced would be describing something physically impossible.**

## The words this page uses

| Term | What it means |
|---|---|
| **`C`** | A person's credit: every hour of their life the books have recorded as work. |
| **`D`** | A person's debit: every hour their consumption is currently reckoned to cost, once the physical quantities are converted at today's weightings. |
| **Ratio** | `D ÷ C`. How much a person consumed per hour contributed. A measure of efficiency. |
| **The gate** | `D ≤ ρ·(C + P)`, where ρ is the network's debit tolerance ([debit-tolerance](debit-tolerance.md)). |

## The rule

**This is the second law of thermodynamics appearing in the ledger.** Two consequences follow.

1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds, not merely impractical.
2. **Sums are not meaningful; two separate numbers are.** The ratio measures efficiency. Absolute credit measures contribution. Neither substitutes for the other: a pure-ratio metric is infinite for a newborn and is gamed by an ascetic who minimises both sides, and a pure-sum metric ignores waste entirely.

**Why this does not collapse the economy, where a currency would.** In a monetary system, aggregate debt exceeding aggregate money is a solvency crisis. Here there is no creditor to be made whole, because credit is non-fungible and never moves (A3, [non-fungibility](non-fungibility.md)). Permanent aggregate net-debit is the correct description of an economy running on a thermal gradient.

**The same rule is why two co-products' figures are never added.** Both point at the same parcel, and a ledger walk is a union, never a sum ([co-product-allocation](co-product-allocation.md)).

## An example, with the numbers

**Three people at age 40, in a network with `F` = 10 h/day and ρ = 1.2.** A median lifestyle commands about 1,380 hours of other people's labour a year.

| | Credit `C` | Debit `D` | Ratio `D ÷ C` |
|---|--:|--:|--:|
| **A** stays alive and works 1,000 h a year | 40 × 4,650 = **186,000 h** | 40 × 1,380 = **55,200 h** | **0.30** |
| **B** stays alive, works nothing, consumes the same | 40 × 3,650 = **146,000 h** | **55,200 h** | **0.38** |

**In plain words: nothing was subtracted and nothing was spent.** A's extra 40,000 hours did not cancel A's consumption; it widened the gap between two figures that only ever grow. The two are compared as a ratio, never netted to a balance that could reach zero.

## The binding scarcity is material, and the honest form of that claim is narrow

**One comparison looks like evidence and is not.** Setting credited labour (which includes the self-care floor) against the labour an economy needs cannot fail, because `F` is a value the network sets before a single worker is counted. Sleeping is credited work and it cannot lay cable. **That check was excluded, not restated** (Foundations §3.5).

**The check that can fail asks about deployable hours**: working-age share × participation × hours per worker, against the 1,380 h/yr a median US lifestyle commands.

| Production method | Deployable ÷ needed | Closes? |
|---|---|---|
| **United States** | **0.43 – 0.87** | **No, at no corner of the band** |
| Peer countries at about ⅔ of US labour | 0.66 – 1.34 | **Yes, in about a third of cases** |

**So the claim is not that labour is never the constraint. It is that the constraint is production efficiency**, and at the wasteful method the hours are short. The same lifestyle costs **1,380** hours by the American method, **883** by the German or Japanese, and **759** by the Spanish. Energy, not labour, is the tightest physical constraint on an autarkic US: **0.19** of what a median standard needs at the current build.

## Depends on

- [material-flow-value](material-flow-value.md) · [non-fungibility](non-fungibility.md) · [derived-ledger](derived-ledger.md)

## Consequences

- [debit-tolerance](debit-tolerance.md) — the gate is a ratio because there is no balance to draw down
- [co-product-allocation](co-product-allocation.md) — a union, never a sum
- [capitalism-cannot-function](capitalism-cannot-function.md) — no creditor, so no debt spiral

---
*Status: settled*
*Source: `00-strategy/Aequitas_Foundations.md` §3.0 (a ledger is three numbers that never cancel), §3.5 (the rule, the deployable-hours test, the 1,380 h/yr anchor)*
