# The Joint Production / Allocation Problem

**Type:** technical problem — spans political economy and life-cycle assessment
**Author(s):** Piero Sraffa; Ian Steedman; Michio Morishima; and separately the LCA methodology literature (ISO 14044, Ardente & Cellura, Mackenzie et al.)
**Published:** Sraffa, *Production of Commodities by Means of Commodities*, 1960; Steedman, *Marx after Sraffa*, 1977; ISO 14044:2006
**Retrieved:** 2026-08-01
**URL:** [Sraffa, joint production and the LTV](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) · [Kurz, *Sraffa and the Labour Theory of Value*](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/kurz_heinz/Dokumente/2010_Sraffa_and_the_labour_theory_of_value__in_Economic_Theory_and_Economic_Thought_.pdf) · [Is "biophysical" allocation progress?](https://link.springer.com/article/10.1007/s11367-016-1161-2) · [Allocation in field crop and livestock LCA](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) · [ISO 14044](https://iso-library.com/standard/14044/)
**Local copy:** none — Springer and ScienceOpen items partly paywalled; the Kurz PDF and the PMC article are open.

> **✅ STATUS UPDATE — 2026-08-01. OP-17 is resolved for the material/energy half.** See `00-strategy/OP-17_coproduct_allocation.md` and Foundations v0.4 §3.4a. **The resolution did not come from this literature; it came from noticing what this literature was searching for and why Aequitas does not have to.** Kept in full because the objections it records are exactly what a hostile economist will raise.

## Why this mattered to Aequitas

**This was the most dangerous unresolved problem in the project.** It blocked C3: no honest debit-cost figure could be published without an allocation rule, and no allocation rule satisfied universality.

Two literatures, a half-century and a discipline apart, discovered the same thing. Aequitas sits precisely at their intersection.

## Key findings

**The problem.** One physical process, several outputs. A steer yields beef, leather, tallow, and bone meal. A refinery yields the full fraction slate from one crude stream. A CHP plant yields electricity and heat. There is **one pool of consumed energy, materials, and labour** and no physical fact about which output owns which share.

**From political economy.** Sraffa showed that once joint production is admitted, labour values become indeterminate or **negative** — a commodity "containing" less than zero labour. Morishima concluded on this basis that the labour theory of value is incompatible with joint production. The debate over whether Sraffa's physical-numeraire approach survives is [still live](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/kurz_heinz/Dokumente/2010_Sraffa_and_the_labour_theory_of_value__in_Economic_Theory_and_Economic_Thought_.pdf), but the negative-value result is not disputed.

**From life-cycle assessment.** ISO 14044 §4.3.4 gives a hierarchy:
1. **Avoid allocation** — subdivide the process, or expand the system boundary.
2. **Allocate by underlying physical relationships** — mass, energy content, chemical exergy, area.
3. **Allocate by other relationships** — economic value, market price.

Practitioners hit step 3 constantly. Mass, energy, and exergy allocation give **materially different answers for the same process**, and the literature notes the prioritisation is [often simply inapplicable](https://link.springer.com/article/10.1007/s11367-016-1161-2). The deeper criticism is the sharp one: allocation choices fail because **benefit is not an inherent property of a material** — it is a preference within an economic system.

## ✅ How it was resolved — and why the literature could not

**Both traditions were searching for a *carrier quantity*: a property of the *outputs* by which cost could be apportioned.** Mass, energy, exergy, area, price. Every candidate is right in some industries and a category error in others.

**A carrier quantity is a property of the outputs. The allocation is a fact about the process.** A steer is a metabolism, and where it spent its feed energy is a biological fact. A refinery's cracking enthalpy went into specific fractions and is metered. A turbine's extraction curve is measured.

**Aequitas can say this and the LCA literature cannot, for one structural reason: it has a universal denominator and they do not.** Under A2, every physical quantity in the ledger is already a proxy for hours-to-produce or hours-to-mitigate, so the unanswerable question *"mass or energy?"* never has to be asked — whichever is measurable in the case at hand is used, because both reduce to the same thing.

> **The universal is the denominator, not the carrier.**

**On the negative-value result specifically:** nothing is inverted under the adopted rule, so Steedman's algebra does not transfer. Each share is a forward measurement of what physically went in, and a deposition cannot be negative. ⚠️ **This is asserted, not yet proven for a recursive economy** where every input's debit is itself a joint split — which is where Sraffa could re-enter. **That is now the sharpest open technical risk in the project.**

## What was used, for and against

**Used in support:**
- **ISO's own hierarchy, read as evidence.** That step 1 is "avoid allocation" and step 3 is price is an admission that the physical options are inadequate as posed. The hierarchy's failure is the argument that the question was wrong.
- **The "benefit is not inherent to a material" critique** — turned around. It is exactly why *demand-contingent* allocation was rejected: benefit is a preference, cost is not, and only cost is being divided.
- **Mackenzie et al. on livestock** as the hardest published case, and the source for the fuzzy-middle test still owed.

**Used against candidate rules — and all four were rejected:**

| Candidate | Killed by |
|---|---|
| **Mass** | Undefined for CHP (heat has no mass). Survives only as an *estimator* where composition is uniform. |
| **Energy / exergy** | Chosen for CHP precisely because it flatters the known answer; a category error applied to beef and leather. |
| **Market price** | A5, and circularity. **EEIO allocates by price because nothing else is available** — changing data source does not escape it. |
| **System expansion / avoided burden** | Needs a counterfactual about an unobserved alternative economy. **Demoted to an evidence source**: where the displaced alternative is genuinely *observed* in the log, the offset is a measurement and constrains the split. |
| **Aumann–Shapley** *(considered outside this note's literature)* | Rigorous, but needs a domain condition and — decisively — **a cost function, i.e. an objective, which re-opens OP-10.** |

## Where Aequitas is still exposed

1. ~~**Universality** — every candidate rule is a convention~~ — **resolved.** The rule is a measurement; a row was *deleted* from Foundations §1.1 rather than filled in.
2. **A5 collision, narrowed.** USEEIO's price allocation is now definitively unusable as truth. It remains usable as data, flagged `declared` basis rather than `measured`.
3. **It recurs one level up, among people — and that half did not move.** Labour leaves no physical trace to an individual co-product, so splitting a team's credit is still indeterminate. See `02-research/ellerman-labor-theory-of-property.md`. **OP-18 now blocks C3 in OP-17's place.**
4. **Shared overhead** has no trace either. **OP-23.**

## To do

- [x] **Test candidate rules against three cases**: slaughterhouse, oil refinery, CHP plant. *Done — one justification, three instruments.*
- [x] Assess option 1 from the register — carry joint debit as an unsplit set. *Rejected: it defers the division rather than removing it, and the deferred question is worse.*
- [ ] **🔴 Prove or disprove recursion convergence.** Sparse-matrix sim over a synthetic joint-production economy, [Cockshott & Cottrell's method](https://en.wikipedia.org/wiki/Towards_a_New_Socialism). **A negative result invalidates the resolution above.**
- [ ] Read [Mackenzie et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) properly on biophysical allocation in livestock — the fuzzy-middle test
- [ ] Source tissue-deposition energetics for cattle. Starting point: [NRC, *Nutrient Requirements of Beef Cattle*](https://nap.nationalacademies.org/catalog/19014/nutrient-requirements-of-beef-cattle-eighth-revised-edition). *Not yet retrieved or verified.*
- [ ] Source refinery per-fraction process energy. *No source identified yet.*
- [ ] Check whether EXIOBASE's embodied-labour layer uses a different allocation basis than USEEIO — **now more urgent, since labour is the blocking layer**

## Related

- [[co-product-allocation]] · [[physical-trace-test]] · [[material-flow-value]] · [[price-equals-cost]] · [[estimation-engine]] · [[event-record]]
- `00-strategy/OP-17_coproduct_allocation.md` — the resolution
- `02-research/estimation-engine-data-sources.md` — where the price-allocation collision was first flagged
- Register: `00-strategy/Aequitas_Objections_v0.5.md` — **B7** (answered), **A1/A4** (what did not move)
