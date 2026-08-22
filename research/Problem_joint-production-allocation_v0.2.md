# The Joint-Production Problem — When One Process Makes Several Things

**Version:** 0.2
**Type:** technical problem — spans economics and life-cycle assessment
**Author(s):** Piero Sraffa; Ian Steedman; Michio Morishima; and, separately, the life-cycle-assessment methodology literature (the ISO 14044 standard, Ardente & Cellura, Mackenzie et al.)
**Published:** Sraffa, *Production of Commodities by Means of Commodities*, 1960; Steedman, *Marx after Sraffa*, 1977; ISO 14044:2006
**Retrieved:** 2026-08-01
**URL:** [Sraffa, joint production and the labour theory of value](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) · [Kurz, *Sraffa and the Labour Theory of Value*](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/kurz_heinz/Dokumente/2010_Sraffa_and_the_labour_theory_of_value__in_Economic_Theory_and_Economic_Thought_.pdf) · [Is "biophysical" allocation progress?](https://link.springer.com/article/10.1007/s11367-016-1161-2) · [Allocation in field crop and livestock LCA](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) · [ISO 14044](https://iso-library.com/standard/14044/)
**Local copy:** none — the Springer and ScienceOpen items are partly paywalled; the Kurz PDF and the PMC article are open.

> **✅ STATUS — 2026-08-01. This problem is solved for the material/energy side.** See [`00-strategy/OP-17_coproduct_allocation.md`](../docs/OP-17_coproduct_allocation.md) and [Foundations §3.4a](../docs/Aequitas_Foundations_v0.17.md#34a-joint-production--the-process-allocates-itself). The solution did *not* come from this literature — it came from noticing what this literature was fruitlessly searching for, and why Aequitas doesn't have to. This note is kept in full because it records exactly the objections a hostile economist will raise.

## Why this mattered to Aequitas

**This was the most dangerous unsolved problem in the project.** You can't publish an honest cost figure for anything without a rule for splitting a shared process's cost among its several products — and for a century, no such rule worked in every industry.

Two separate bodies of work, half a century and a whole discipline apart, ran into the *same* wall. Aequitas sits right at their intersection.

## Key findings

**The problem in one line.** One physical process, several outputs. A steer yields beef, leather, tallow, and bone meal. An oil refinery yields the whole slate of fuels from one stream of crude. A combined heat-and-power plant yields both electricity and heat. There's **one pool of consumed energy, materials, and labour**, and no obvious physical fact saying which output owns which slice.

**From economics.** Sraffa showed that once you allow a process to make several things at once, the "labour content" of a good becomes undefined — or even **negative** (a good "containing" less than zero hours of work, which is nonsense). Morishima concluded this made the labour theory of value incompatible with joint production. Whether Sraffa's own workaround survives is [still debated](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/kurz_heinz/Dokumente/2010_Sraffa_and_the_labour_theory_of_value__in_Economic_Theory_and_Economic_Thought_.pdf), but the negative-value result itself is not disputed.

**From life-cycle assessment** (the discipline that measures a product's total environmental footprint). The ISO 14044 standard offers a ranked recipe for splitting a shared process:
1. **Avoid splitting** — break the process into finer steps, or widen the boundary so the split disappears.
2. **Split by a physical relationship** — weight, energy content, chemical energy, area.
3. **Split by something else** — usually market price.

Practitioners hit step 3 constantly. Splitting by weight, by energy, and by chemical energy give **materially different answers for the same process**, and the literature notes the ranking is [often simply inapplicable](https://link.springer.com/article/10.1007/s11367-016-1161-2). The deepest criticism is the sharp one: these splits fail because **"benefit" isn't a property built into a material** — it's a preference inside an economy.

## ✅ How it was solved — and why the literature couldn't

**Both traditions were hunting for a *carrier* — some property of the *outputs* (their weight, their energy, their price) by which to divide the cost.** Every candidate is right in some industries and a category error in others.

The fix is to stop looking at the outputs. **A carrier is a property of the outputs. The split is a fact about the *process*.** A steer is a metabolism, and *where its body actually sent the feed energy* is a biological fact you can measure. A refinery's cracking energy went into specific fuel fractions and is metered. A turbine's electricity-versus-heat split is measured.

**Aequitas can say this and the life-cycle literature can't, for one structural reason: Aequitas has a single common unit underneath everything, and they don't.** Because Aequitas ultimately measures everything in *hours* (hours to produce, or hours to clean up — see [Foundations §A2](../docs/Aequitas_Foundations_v0.17.md#a2-time-as-measure)), the unanswerable question *"should we split by weight or by energy?"* never has to be asked. Whichever quantity you can actually *measure* in the case in front of you is the one you use, because both are just proxies for the same underlying thing.

> **The universal thing is the yardstick underneath, not any single property of the products.**

**On the negative-value result specifically:** under Aequitas's rule nothing is ever run backwards, so Steedman's algebra (which produces the negative values) doesn't apply. Each share is a *forward* measurement of what physically went in, and something physically deposited can't be negative. ⚠️ **This is asserted, not yet fully proven for a whole interlocking economy** where every input's cost is *itself* a joint split feeding another — which is exactly where Sraffa's problem could sneak back in. That proof is now the sharpest open technical risk in the project. (A convergence simulation has since been run and passed — see the recursion result in [`06-simulation/RESULTS.md`](../sims/RESULTS.md).)

## What was used, for and against

**Used in support:**
- **ISO's own ranking, read as a confession.** The fact that its step 1 is "avoid the split" and its fallback is *price* is an admission that the physical options don't actually work as posed. The recipe's failure *is* the argument that the question was wrong.
- **The "benefit isn't inherent to a material" criticism — turned around.** It's exactly why Aequitas *rejects* splitting by demand: benefit is a preference, cost is not, and only cost is being divided.
- **Mackenzie et al. on livestock** as the hardest published case.

**Used against candidate rules — all four rejected:**

| Candidate rule | Why it fails |
|---|---|
| **By weight** | Meaningless for heat-and-power (heat has no weight). Survives only as a rough estimator where a product is uniform throughout. |
| **By energy** | Picked for heat-and-power precisely because it flatters the answer people already expected; a category error when applied to beef versus leather. |
| **By market price** | Breaks the price-equals-cost rule, and is circular. (Standard footprint databases split by price only because nothing else is on hand — swapping data source doesn't escape it.) |
| **By "avoided burden"** (crediting a product for the alternative it displaced) | Needs a guess about an unobserved alternative economy. Demoted to an *evidence source*: where the displaced alternative is genuinely *observed* in the records, the offset becomes a real measurement. |

A fifth option from the maths literature (the Aumann–Shapley method) is rigorous but needs a stated *objective* to compute against — which would re-open Aequitas's "who controls the cost model" problem. Rejected for that reason.

## Where Aequitas is still exposed

1. ~~**Is the rule just another convention?**~~ **Resolved** — it's a measurement. A row was *deleted* from the Foundations' list of conventions rather than filled in.
2. **The price-equals-cost collision, narrowed.** Standard footprint databases split by price, which Aequitas can't treat as *truth* — but it can still use their numbers as *data*, flagged as "declared/estimated," not "measured."
3. **It comes back one level up, among people — and that half didn't move.** A team's *labour* leaves no physical trace pointing to who caused which part of the output, so splitting a team's *credit* is still undetermined. See [Ellerman: labour theory of property](../docs/GLOSSARY.md#src-ellerman-labor-theory-of-property). This is now the live version of the problem — the "splitting blame within a team" open problem ([Foundations §10](../docs/Aequitas_Foundations_v0.17.md#10-open-problems)).
4. **Shared overhead** (the buildings and machinery a business runs on) leaves no trace either — and Aequitas handles it the same way it handles a hospital: carried by the people who run the place, never sliced into each product. See [Foundations §6.2b (the capital-debit waterfall)](../docs/Aequitas_Foundations_v0.17.md#62b-the-capital-debit-waterfall).

## To do

- [x] **Test candidate rules against three cases** (slaughterhouse, oil refinery, heat-and-power plant). *Done — one justification, three measuring instruments.*
- [x] Assess carrying joint cost as one unsplit bundle. *Rejected — it only defers the split, and the deferred question is worse.*
- [ ] **🔴 Prove or disprove that the whole interlocking economy settles to sensible numbers.** A simulation over a synthetic joint-production economy. *A negative result would invalidate the solution above.* (Since run and passed — [`06-simulation/RESULTS.md`](../sims/RESULTS.md).)
- [ ] Read [Mackenzie et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) properly on the livestock case.
- [ ] Source the tissue-deposition energetics for cattle. Starting point: [NRC, *Nutrient Requirements of Beef Cattle*](https://nap.nationalacademies.org/catalog/19014/nutrient-requirements-of-beef-cattle-eighth-revised-edition). *Not yet retrieved.*
- [ ] Source refinery per-fuel process energy. *No source identified yet.*

## Related

- [[co-product-allocation]] · [[physical-trace-test]] · [[material-flow-value]] · [[price-equals-cost]] · [[estimation-engine]] · [[event-record]] · [Ellerman: labour theory of property](../docs/GLOSSARY.md#src-ellerman-labor-theory-of-property) · [Estimation-engine data sources](../docs/GLOSSARY.md#src-estimation-engine-data-sources)
