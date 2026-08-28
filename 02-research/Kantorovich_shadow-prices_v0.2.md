# Kantorovich — Pricing Scarcity Without Profit

**Version:** 0.2
**Type:** theory / mathematical economics
**Author(s):** Leonid V. Kantorovich; extended by Jan Philipp Dapprich
**Published:** Kantorovich, *The Best Use of Economic Resources*, 1959 (the underlying method, 1939); Nobel lecture 1975; Dapprich thesis 2021
**Retrieved:** 2026-08-01
**URL:** [Kantorovich's Nobel lecture](https://www.nobelprize.org/prizes/economic-sciences/1975/kantorovich/lecture/) · [Dapprich, *Optimal Planning with Consumer Feedback*](https://brightagebeyond.com/wp-content/uploads/2022/05/dapprich-philipp-2021-optimal-planning-with-consumer-feedback-a-simulation-of-a-socialist-economy.pdf) · [*Programming the USSR: Kantorovich in context*](https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/programming-the-ussr-leonid-v-kantorovich-in-context/4BF0F0D89079DD94AF595EA25A991299) · [*Von Mises, Kantorovich and in-natura calculation*](https://www.researchgate.net/publication/46547387_Von_Mises_Kantorovich_and_in-natura_calculation)
**Local copy:** none — the Dapprich thesis and the Nobel lecture are free to read. **Archive the Dapprich PDF next.**

## Why this matters to Aequitas

This is **the most promising available answer to Aequitas's weakest point:** the fact that cost alone doesn't tell you who should get a scarce thing when two people both want it. The Neurath note names this as the spot a sharp economist attacks first. Kantorovich offers a way to price scarcity itself — without inventing profit.

## Key findings

- Kantorovich found a way to attach a number to each scarce resource that falls straight out of the maths of using resources as well as possible. He pointedly *avoided* calling these numbers "prices" — for political safety in the Soviet Union — and called them "objectively determined valuations."
- His core result: **even a moneyless, planned economy has to use scarcity-values to allocate well.** Valuing scarce things isn't a capitalist quirk; it's a mathematical fact about sharing out limited resources.
- One of these valuations is simply **the cost of a bottleneck** — how much better off everyone would be if one more unit of the scarce thing existed. It is *not* a markup a seller pockets, and *not* someone's personal preference. Given what's scarce and what's needed, the number is fixed.
- **Dapprich** builds this into a full planning model and argues these scarcity-values are a *better* measure of true cost than labour-time, precisely because they capture limits — finite ores, environmental ceilings — that **can't be expressed as hours of work.** He bolts a consumer-feedback loop onto it and simulates the whole thing.

## What we can use

**The reframing that might rescue Aequitas's "price equals cost" rule: scarcity is itself a real cost.**

Aequitas's rule ([Foundations §A5](../00-strategy/Aequitas_Foundations_v0.29.md)) says there's no *profit* in a price. It does **not** say that using up something scarce is free. Taking the last unit of a limited resource genuinely burdens everyone else — they now have to make do with the next-best thing, or do the work of relieving the shortage. If that burden is written down **as a debit** (a real cost carried by the person who caused it) rather than skimmed **as a markup**, it fits Aequitas perfectly — and is arguably *required* by Aequitas's rule that no cost may be dumped on others ([Foundations §A4 (no externalities)](../00-strategy/Aequitas_Foundations_v0.29.md#a4-no-externalities)): a shortage you cause *is* a cost you impose.

This gives Aequitas a principled way to ration a one-of-a-kind lakeside house — without inventing profit, without an auction, and without breaking "price equals cost."

Dapprich's point that some limits can't be reduced to labour-time also directly supports Aequitas's choice to count in **materials and energy** rather than pure labour — that's the right substrate for modelling these bottlenecks. See [Foundations §A1](../00-strategy/Aequitas_Foundations_v0.29.md#a1-materialism-of-cost).

## Where Aequitas is exposed

1. **These scarcity-values need a goal to be computed against.** They only exist relative to *"using resources as well as possible"* — and someone has to say what "well" means (most food produced? least pollution? most health?). Whoever sets that goal quietly sets every scarcity-value in the economy. This runs straight into Aequitas's biggest existing hole: **who controls the cost model** ([Foundations §10](../00-strategy/Aequitas_Foundations_v0.29.md)). The "whose-want-wins" problem and the "who-controls-the-model" problem have to be worked as **one** problem, not two.
2. **It's centrally computed** — the usual Hayek exposure. Aequitas would need a decentralised version, plausibly done *per-bottleneck and locally*, since most shortages are local (this lake, this ore body) rather than global.
3. **The historical record is discouraging.** Kantorovich's methods were [only partly adopted in the USSR](https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/programming-the-ussr-leonid-v-kantorovich-in-context/4BF0F0D89079DD94AF595EA25A991299) and never displaced central command. Being mathematically right isn't the same as being adoptable — a caution that lands on Aequitas at least as hard.
4. The method assumes tidy, fully-known constraints. Real economies rarely oblige.

## To do

- [ ] **Archive the Dapprich thesis** to `02-research/files/`.
- [ ] Draft the "whose want wins" answer using the scarcity-as-debit framing; stress-test it against the price-equals-cost and non-transferability rules.
- [ ] Check whether scarcity-debit can be kept **local and federated** rather than needing one global optimisation.
- [ ] Read the *Von Mises, Kantorovich and in-natura calculation* paper — it's squarely on the project's central question.

## Related

- [price-equals-cost](../01-wiki/cost-not-price.md) · [no-externalities](../01-wiki/no-externalities.md) · [calculation-in-kind](../01-wiki/calculation-in-kind.md) · [material-flow-value](../01-wiki/material-flow-value.md) · [Neurath: calculation in kind](../00-strategy/GLOSSARY.md#src-neurath-calculation-in-kind) · [Cockshott & Cottrell: labour-time](../00-strategy/GLOSSARY.md#src-cockshott-cottrell-labour-time)
