# Cockshott & Cottrell — Planning an Economy by Computer

**Version:** 0.2
**Type:** theory / computational economics
**Author(s):** W. Paul Cockshott, Allin F. Cottrell
**Published:** *Towards a New Socialism*, Spokesman Books, 1993
**Retrieved:** 2026-08-01
**URL:** [Wikipedia overview](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) · [Cockshott's reply to Brewster](https://paulcockshott.wordpress.com/2017/08/28/reply-to-brewster/) · [Mises Institute review](https://cdn.mises.org/qjae7_1_6.pdf) · [*Towards an Old Socialism* — a critique from within the labour-time tradition](https://arbeitszeit.noblogs.org/en-GB/post/2023/09/10/towards-an-old-socialism/)
**Local copy:** none — the Mises review and the noblogs critique are free to read. The book is widely available online; archive next.

## Why this matters to Aequitas

These two are the modern answer to the old "you can't run an economy without money-prices" argument (see [Neurath: calculation in kind](../docs/GLOSSARY.md#src-neurath-calculation-in-kind)). Their contribution is the one Aequitas most needs and can most directly point to: **a demonstration that counting an economy in physical/labour units, at the scale of a whole country, is actually computable on ordinary machines.** Their leftover unsolved problem happens to be Aequitas's leftover unsolved problem too — with Aequitas holding one fewer tool to solve it.

## Key findings

- **Running an economy on labour-time can be made to work** — provided you add a method that lets what consumers actually want steer production — and it is now **technically feasible.** The heavy arithmetic (a giant grid of who-supplies-what to everyone else) runs in reasonable time on normal hardware using "sparse-matrix" methods — techniques that exploit the fact that most industries buy from only a few others, so the grid is mostly empty and can be solved quickly. This is the direct reply to the "it's too big to compute" version of the objection.
- **How they handle demand.** They tag each consumer good with the price at which it just clears the shelves. Where that clearing price sits *above* what the good cost in labour, they make more of it; where it sits *below*, they make less. The gap between price and cost is the signal that steers production. Labour-time is the unit of account; the price-to-cost ratio is the feedback dial.
- Their "labour tokens" don't circulate and are cancelled once spent — structurally similar to Aequitas's rule that credit can't be traded (see [[non-fungibility]]).
- Their scheme is still **centrally computed**, even if not centrally *commanded* in the old Soviet sense.

## What we can use

- **Cite them for feasibility.** This closes the "it's computationally impossible" objection: Mises argued it couldn't be done even in principle, and people who actually ran the numbers showed otherwise. Aequitas's habit of recomputing history when a cost estimate improves ([[retroactive-reweighting]]) needs exactly this defence and now has a citation for it. Aequitas already leans on this — see [Foundations §3.3](../docs/Aequitas_Foundations_v0.17.md#33-retroactive-re-weighting).
- Their sparse-matrix approach is a concrete precedent for doing Aequitas's re-computation at scale.
- The non-circulating labour token is prior art for Aequitas's "credit can't move" rule and worth citing as such — see [Foundations §A3](../docs/Aequitas_Foundations_v0.17.md#a3-non-fungibility).

## Where Aequitas is exposed

1. **Aequitas can't use their demand dial.** Their entire feedback loop is the *gap* between the shelf-clearing price and the labour cost. But Aequitas's rule that **price simply equals cost** ([Foundations §A5](../docs/Aequitas_Foundations_v0.17.md#a5-price--cost)) sets that gap to zero on purpose — there's no separate "price" to compare against. So Aequitas inherits their problem (cost alone doesn't tell you what people want) while giving up their solution. The standard criticism — [labour-value accounting doesn't capture demand, and making things nobody wants is blind production](https://arbeitszeit.noblogs.org/en-GB/post/2023/09/10/towards-an-old-socialism/) — bites *harder* on Aequitas than on them. Aequitas's answer is a *different* one: **pledges** — people put their earned credit behind what they want made — carry the demand signal instead of a price gap. See [Foundations §6.4](../docs/Aequitas_Foundations_v0.17.md#64-pledges-and-signals), and the full reply in [`00-strategy/OP-9_calculation_reply.md`](../docs/OP-9_calculation_reply.md).
2. **The "contamination" charge.** A critic (Brewster) points out that once market prices feed back into production decisions, the labour values you compute are no longer *pure* labour values. Cockshott [replies](https://paulcockshott.wordpress.com/2017/08/28/reply-to-brewster/) that the distortion is a short-lived artefact of temporary supply/demand mismatch. Aequitas faces the identical charge the moment it uses any price-derived data — which, per [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem), it sometimes still must.
3. **Boiling everything down to one substance.** They reduce to labour time; Aequitas reduces to material and energy flow. Both approaches are exposed to the "when one process makes several things, how do you split the cost?" problem — which Aequitas answers by measuring where the process physically sent its inputs (see [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem)).
4. **Central computation** — a target for Hayek's objection, and the reason Aequitas's decentralised, everyone-keeps-the-record design is a real difference rather than a restatement of their work.

## To do

- [ ] Archive the full text of *Towards a New Socialism* to `02-research/files/`.
- [ ] Read the Mises Institute review closely — it's the best-organised hostile summary available.
- [ ] Compare their sparse-matrix method against what Aequitas's re-weighting engine will actually need.
- [ ] Separate note: **Dapprich** — shadow-price planning, the successor to this work (see [Kantorovich: shadow prices](../docs/GLOSSARY.md#src-kantorovich-shadow-prices)).

## Related

- [[calculation-in-kind]] · [[material-flow-value]] · [[price-equals-cost]] · [[non-fungibility]] · [[retroactive-reweighting]] · [Neurath: calculation in kind](../docs/GLOSSARY.md#src-neurath-calculation-in-kind) · [Kantorovich: shadow prices](../docs/GLOSSARY.md#src-kantorovich-shadow-prices) · [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem)
