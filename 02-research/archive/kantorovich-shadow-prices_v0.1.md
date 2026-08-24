# Kantorovich — Objectively Determined Valuations

**Type:** theory / mathematical economics
**Author(s):** Leonid V. Kantorovich; extended by Jan Philipp Dapprich
**Published:** Kantorovich, *The Best Use of Economic Resources*, 1959 (LP method 1939); Nobel lecture 1975; Dapprich thesis 2021
**Retrieved:** 2026-08-01
**URL:** [Kantorovich Nobel Prize lecture](https://www.nobelprize.org/prizes/economic-sciences/1975/kantorovich/lecture/) · [Dapprich, *Optimal Planning with Consumer Feedback: A Simulation of a Socialist Economy*](https://brightagebeyond.com/wp-content/uploads/2022/05/dapprich-philipp-2021-optimal-planning-with-consumer-feedback-a-simulation-of-a-socialist-economy.pdf) · [*Programming the USSR: Kantorovich in context* (BJHS)](https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/programming-the-ussr-leonid-v-kantorovich-in-context/4BF0F0D89079DD94AF595EA25A991299) · [*Von Mises, Kantorovich and in-natura calculation*](https://www.researchgate.net/publication/46547387_Von_Mises_Kantorovich_and_in-natura_calculation)
**Local copy:** none — the Dapprich thesis PDF and the Nobel lecture are open access. **Archive the Dapprich PDF next.**

## Why this matters to Aequitas

This is **the most promising available answer to OP-9 (preference revelation)** — the objection the Neurath note names as the weakest link in the whole project, and the place a competent economist attacks first.

## Key findings

- Kantorovich derived **objectively determined valuations** (Russian *o.o.o.*) as the dual solutions of a linear program. He avoided the word "price" deliberately, for political reasons in the USSR.
- The substantive result: **even a socialist economy must use valuations reflecting resource scarcity** in order to allocate efficiently. Scarcity valuations are not a capitalist artefact; they are a mathematical property of allocation under constraint.
- An ODV is the **cost of a binding constraint** — how much the objective improves if one more unit of a scarce resource becomes available. It is not a margin extracted by a seller and it is not a subjective preference. It is *objectively determined* given the constraint set.
- **Dapprich** extends this into a full planning model: shadow prices are a better measure of opportunity cost than labour time precisely because they capture constraints — limited natural resources, environmental limits — that **cannot be reduced to labour time**. He couples it to a consumer-feedback loop and simulates the result.

## What we can use

**The reframing that may rescue A5: scarcity is itself a material cost.**

A5 says there is no profit in exchange. It does **not** say opportunity cost is not a cost. Taking the last unit of a constrained resource imposes a genuine burden on everyone else — the cost of the next-best substitute, or the cost of relieving the constraint. If that burden is recorded **as a debit** rather than skimmed **as a margin**, it is compatible with A5 and arguably required by A4 (no externalities): a scarcity externality is an externality.

This gives Aequitas a principled way to ration a unique lakeside house without inventing profit, without an auction, and without abandoning price ≡ cost.

Dapprich's point about constraints irreducible to labour time is also directly supportive of A1 over any labour-time accounting: **Aequitas already counts in material and energy, which is the right substrate for constraint modelling.**

## What it gets wrong / limitations — and where Aequitas is exposed

1. **A dual requires a primal.** Shadow prices only exist relative to an optimisation, which requires an **objective function** — a social judgement about what is being maximised. Whoever sets it sets every scarcity valuation in the economy. This collides head-on with **OP-10 (weighting-model governance)**, the largest existing hole in A8. **OP-9 and OP-10 must be worked as one problem, not two.**
2. **Centralised computation**, with the usual Hayek exposure. Aequitas would need a decentralised or federated formulation — plausibly per-constraint and local, since most scarcity constraints are local (this lake, this ore body) rather than global.
3. **Historical record is poor.** Kantorovich's methods were [only partially adopted in the USSR](https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/programming-the-ussr-leonid-v-kantorovich-in-context/4BF0F0D89079DD94AF595EA25A991299) and never displaced the command structure. Being mathematically right is not the same as being institutionally adoptable — a caution that applies to Aequitas at least as much.
4. LP assumes convexity and known constraints. Real economies supply neither reliably.

## To do

- [ ] **Archive the Dapprich thesis** to `02-research/files/`
- [ ] Draft the OP-9 answer using the scarcity-as-debit framing; stress-test it against A5 and A3
- [ ] Check whether scarcity debit can be made **local and federated** rather than requiring a global optimisation
- [ ] Read the *Von Mises, Kantorovich and in-natura calculation* paper — it is squarely on the project's central question

## Related

- [[price-equals-cost]] · [[no-externalities]] · [[calculation-in-kind]] · [[material-flow-value]]
- `02-research/neurath-calculation-in-kind.md` · `02-research/cockshott-cottrell-labour-time.md`
- Register: `00-strategy/Aequitas_Objections_v0.1.md` — **OP-9**, OP-10
