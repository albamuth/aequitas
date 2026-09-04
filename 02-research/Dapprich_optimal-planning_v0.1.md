# Dapprich — Optimal Planning with Consumer Feedback

**Version:** 0.1
**Type:** theory / computational economics
**Author(s):** Jan Philipp Dapprich
**Published:** *Optimal Planning with Consumer Feedback: A Simulation of a Socialist Economy* (PhD thesis, University of Glasgow, 2021); related papers ongoing
**Retrieved:** 2026-08-13
**URL:** [thesis PDF](https://brightagebeyond.com/wp-content/uploads/2022/05/dapprich-philipp-2021-optimal-planning-with-consumer-feedback-a-simulation-of-a-socialist-economy.pdf) · [Glasgow thesis record](https://theses.gla.ac.uk/82360/)
**Local copy:** *thesis PDF is open — archive next.*

## Why this matters to Aequitas

Dapprich is the most recent serious attempt to plan an economy in physical/optimisation terms, and he tackles the two problems Aequitas most needs answered: **how to price scarcity without profit**, and **how to let what people actually want steer production** without a market. He is the direct successor to Kantorovich (shadow prices) and Cockshott & Cottrell (computational planning), and he couples their machinery to a *consumer-feedback loop* — which is close in spirit to what Aequitas does with pledges.

Bears on: pricing scarcity as a cost, not a profit (the "scarcity-as-debit" idea — see [Kantorovich](../00-strategy/GLOSSARY.md#src-kantorovich-shadow-prices)); the demand-side reply to the calculation critique ([`00-strategy/open-problems/OP-9_calculation_reply.md`](../00-strategy/open-problems/OP-9_calculation_reply.md)); and [Foundations §6.4 (pledges and signals)](../00-strategy/Aequitas_Foundations_v0.39.md).

## Key findings

- **Scarcity gets a shadow value, computed, not marked up.** Dapprich builds a full planning model in which each scarce resource carries an "opportunity-cost" value that falls out of the optimisation (following Kantorovich). These values ration genuinely scarce things *without* inventing profit — they're the cost of a bottleneck, not a seller's margin.
- **Consumers steer it through a feedback loop.** Rather than a central board guessing what to make, the plan adjusts to signals of what consumers actually take up — a demand loop bolted onto the physical plan, and simulated end-to-end.
- **Physical limits beat labour-time as the measure.** Dapprich argues (with Kantorovich, against a pure labour-time accounting) that some binding limits — finite resources, environmental ceilings — simply *can't* be expressed as hours of work, so an optimisation over physical constraints is the better tool.
- **He demonstrates it in simulation** — the point is not just that the maths exists, but that a planned economy with consumer feedback can be *run* on a computer.

## What we can use

- **Live prior art for Aequitas's two hardest open edges.** Dapprich is working the same two problems Aequitas flags — pricing scarcity honestly, and surfacing demand without a market — and has a *running* model. His scarcity-values are the strongest external template for Aequitas's "scarcity is a real cost, recorded as debit" idea. See [Kantorovich](../00-strategy/GLOSSARY.md#src-kantorovich-shadow-prices).
- **His consumer-feedback loop is a check on Aequitas's pledges.** Where Dapprich feeds back consumer *uptake* into the plan, Aequitas surfaces demand as *pledges* — people putting earned credit behind what they want made. Comparing the two is a way to stress-test whether pledges really do the job a feedback loop does. See [Foundations §6.4](../00-strategy/Aequitas_Foundations_v0.39.md).
- **Latest entry in the lineage Aequitas descends from.** Neurath → Kantorovich → Cockshott & Cottrell → Dapprich is the material/optimisation planning tradition; citing Dapprich shows the tradition is alive and computational, not a historical curiosity.

## What it gets wrong / limitations — from Aequitas's angle

- **It still needs a central optimiser with a stated objective.** Dapprich's scarcity-values only exist relative to an optimisation, and someone must set what is being maximised — which is exactly the "who controls the cost model" capture surface Aequitas worries about most. See [Foundations §10](../00-strategy/Aequitas_Foundations_v0.39.md). Aequitas would need a decentralised, per-bottleneck version.
- **It is a plan; Aequitas is not.** Dapprich optimises a whole economy toward chosen targets. Aequitas sets no targets and runs no grand optimisation — it keeps the books under an ordinary decentralised market where the person on the spot decides. This is the deep difference, and it's what lets Aequitas sidestep Hayek's objection to central planning.
- **Simulation, not deployment.** Like its predecessors, it's demonstrated in a model, not run in a real economy.

## To do

- [ ] Archive the thesis PDF to `02-research/files/`.
- [ ] Compare Dapprich's consumer-feedback loop head-to-head against Aequitas's pledge mechanism — does anything his loop captures fall through the pledge design?

## Related

- [Kantorovich: shadow prices](../00-strategy/GLOSSARY.md#src-kantorovich-shadow-prices) · [Cockshott & Cottrell: labour-time](../00-strategy/GLOSSARY.md#src-cockshott-cottrell-labour-time) · [Neurath: calculation in kind](../00-strategy/GLOSSARY.md#src-neurath-calculation-in-kind)
