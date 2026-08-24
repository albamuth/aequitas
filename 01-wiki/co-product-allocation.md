# Co-Product Allocation

> One process, several outputs, one pool of debit. **The split is not a convention to be chosen — it is a measurement, because the process itself already performed it.**

## The problem

A steer yields beef, hide, tallow, bone, manure and enteric methane. A refinery yields a full fraction slate from one crude stream. A CHP plant yields heat and electricity at once. In each case there is **one pool of consumed energy, materials and labour** and several things coming out.

Split by mass, by energy content, by exergy, or by market price and you get four different answers, **none more physically true than the others.** [ISO 14044](https://iso-library.com/standard/14044/) ranks the physical options and then, when they are "inappropriate," falls through to **market price** — which [[price-equals-cost]] forbids, since price is supposed to be the *output* of the accounting, not an input.

The classical form is sharper. Once joint production is admitted, [Sraffa and Steedman showed labour values can go **negative**](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) — a commodity "containing" less than zero labour. Any single-substance cost accounting inherits this.

**This was registered as OP-17 and was the most dangerous open problem in the project.**

## The answer

> **A joint process's debit divides according to where the process itself physically sent its inputs.**

A steer is not a black box that mysteriously emits beef and leather. It is a **metabolism**, and metabolism is measured science: depositing a gram of protein, a gram of lipid, and a gram of mineralised bone have different, measured energetic costs. Where the animal spent its inputs is a **biological fact**, not a human choice.

| Process | What performs the split | What is measured |
|---|---|---|
| Steer | The animal's metabolism | Energy of tissue deposition per gram, by tissue type |
| Refinery | Distillation and cracking thermodynamics | Enthalpy and hydrogen consumed per fraction |
| CHP plant | The turbine's extraction curve | Measured heat/power trade-off at the operating point |
| Emission | Atmospheric chemistry + mitigation technology | Hours to remove a tonne, at today's best method |

**These are not rival conventions. They are different instruments reading the same underlying quantity.**

## Why the literature could not get here

Both the LCA and the Sraffian traditions searched for a **carrier quantity** — a property of the *outputs* by which cost could be apportioned. Every candidate works in some industries and is a category error in others.

**A carrier quantity is a property of the outputs. The allocation is a fact about the process.**

Aequitas can say this and they cannot, for one structural reason: **it has a universal denominator and they do not.** Under [[time-as-yardstick]], every physical quantity in the ledger — a kilogram, a joule, a tonne of CO₂ — is already a proxy for hours-to-produce or hours-to-mitigate. So the question *"mass or energy?"*, which is unanswerable as posed, **never has to be asked.**

> **The universal is the denominator, not the carrier.**

## Mass is an estimator, not a rule

Where a joint output is **compositionally uniform**, cost per gram is genuinely constant and mass allocation is *correct* — the right arithmetic under a true premise. Splitting a homogeneous grain harvest by weight needs no apology.

Where composition varies, mass is the **low-resolution reading**: recorded at low confidence and superseded when better science arrives. This is ordinary [[event-record]] resolution behaviour, which is what makes mass safe to use — it stops being an arbitrary choice and becomes a stated approximation with a known direction of error.

## Four consequences

**Human preference plays no part.** A hide's share does not change because leather is fashionable, exactly as manure's share does not change because nobody wants it. A demand-contingent split would give two identical steers in two towns different splits — a universality failure, and price allocation in costume.

**Waste outputs are co-products like any other.** Counting manure and methane in the split **removes the residual**, and with it the whole question of who absorbs an unwanted output.

**Fate sets ledger character; the process sets cost share.** Manure is pollution debit in a lagoon, a genuine co-product in a biodigester, and an *observed* fertiliser offset when spread on fields. [[event-record]]'s fate closure already records this — no new machinery.

**Negative values do not arise.** Nothing is inverted, so Steedman's result does not transfer: each share is a forward measurement of what physically went in, and a deposition cannot be negative. ⚠️ *Asserted, not yet proven for a recursive economy where every input is itself a joint split.*

## What it does not solve

**Labour.** The farmer's eight hours were spent on the animal, not on the hide. Nothing in physics apportions them, and splitting them in proportion to metabolic energy would be an assumption wearing a measurement's clothes. **This is OP-18, and it now blocks the estimation engine** — see [[physical-trace-test]].

**Shared overhead.** The barn shelters the whole animal. Interim rule: overhead inherits the proportions the traceable inputs established. **Thin, and thinnest where material inputs are small** — capital-intensive manufacturing. OP-23.

## Who games this

| Attack | Defence |
|---|---|
| **Ballast output** — make a worthless heavy output to soak up debit | Closed by construction: a co-product carries only the energy actually spent making it. *This attack works against mass allocation, which is why mass is only an estimator.* |
| **Boundary gerrymandering** — split one process in two to change the base | Stage-by-stage allocation must equal whole-process allocation. Detectable arithmetic, not an arguable judgement. |
| **Instrument shopping** | Only one instrument is *applicable* per process, and applicability is publicly arguable from that process's physics. |
| **Constant capture** — publish energetics favourable to your sector | [[rival-sector-audit]]. **Open — OP-24.** |

## Depends on

- [[material-flow-value]] · [[time-as-yardstick]] — the denominator that makes the rule possible
- [[event-record]] — the split is computed at projection time; **no schema change was required**
- [[retroactive-reweighting]] — better process science re-splits historical production

## Consequences

- [[physical-trace-test]] — the general rule this case produced
- [[estimation-engine]] — materials and energy unblocked; labour is not
- [[rival-sector-audit]] — what disciplines the constants the split depends on
- [[price-equals-cost]] — the reply to ISO 14044's price fallback

## Open questions

- **Does the recursion converge?** Every input's debit is itself a joint split. Untested, and **the sharpest technical risk in the project.**
- OP-23 — shared overhead · OP-18 — labour and team credit · OP-24 — understatement drift

---
*Status: settled (the rule) / unproven (recursion convergence)*
*Source: `00-strategy/OP-17_coproduct_allocation.md`; `00-strategy/Aequitas_Foundations_v0.4.md` §3.4a*
