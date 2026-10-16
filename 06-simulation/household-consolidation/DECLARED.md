# Household consolidation — outcomes declared before running

> **Date:** 2026-10-16
> **Request:** `sr-20261014-over-a-realistic-household-basket-two-adults`

**Written before any code ran.** One honest note: while designing the model I made a rough mental estimate of the central case. No code ran before these were written, and none ran after (Python was refused tonight; see the report).

## The quantity

Two adults, A and B, one network. For each joint process (one steer; one refinery run), each person holds some co-products. **The saving** is

`S = (debit of A under max) + (debit of B under max) − (debit of one account holding everything A and B hold)`

computed per parcel (per step), per dimension, with the max rule of Foundations §3.4a (conformance row 10i). It is reported in hours a year and as a share of the household's debit, `2 × 1,380 = 2,760 h/yr` (§3.5 anchor, one reading).

## Outcomes

| # | Kind | Statement | What a failure means |
|---|---|---|---|
| **O1** | **Level, reproduction** | On an 8 h one-block steer, A holding 10% of the beef and B 10% of the hide carry **1.60 h** together; one account holding both carries **0.80 h**; S = **0.80 h** exactly | The code misreads the max rule, and nothing else it says can be trusted |
| **O2** | Control | Under the sum rule (`f_A + f_B` inside one account), S = **0.000 h** in every household | The code is wrong: the sum rule is additive across accounts by construction |
| **O3** | **Level** | For a typical household (petrol plus a grill's propane, beef and leather bought in shops), central S is **under 1 h/yr and under 0.1%** of household debit | If S ≥ 1 h or ≥ 0.1%, the lever is material for an ordinary household |
| **O4** | **Level, ceiling** | In every swept corner, including a deliberate farm share that takes one steer's beef and its hide, S stays **under 1% of household debit (27.6 h/yr)** | If any corner exceeds 1%, report it as material and name the corner |
| **O5** | Direction | When both adults hold **both** co-products in similar proportions, S is near **0** | If S is large in that case, the lever is not about routing at all |

**Excluded as evidence, kept only as code self-tests.** *"S never exceeds the smaller holding's carry on the shared steps"* and *"S is never negative"* follow from the algebra of `max` (`max(a,b) ≤ a + b`; `a + b − max(a,b) = min(a,b)`). No input could fail them, so under brief §4b they test the code and not the world.
