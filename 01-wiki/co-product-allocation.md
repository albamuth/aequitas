# Co-Product Allocation

> One process, several outputs, one pool of debit. **There is no split. Every co-product carries the whole process cost, read against its own output mass.**
>
> **⚠️ This page was rewritten on 2026-09-03.** It previously said the split was a measurement, because the process itself performed it. **That rule was withdrawn** after 36 methods that all satisfied its four obligations came out **6.31× apart**. What follows is the rule that replaced it.

## The problem

A steer yields beef, hide, tallow, bone, manure and enteric methane. A refinery yields a full fraction slate from one crude stream. A CHP plant yields heat and electricity at once. In each case there is **one pool of consumed energy, materials and labour** and several things coming out.

Split by mass, by energy content, by exergy, or by market price and you get four different answers, **none more physically true than the others.** [ISO 14044](https://iso-library.com/standard/14044/) ranks the physical options and then, when they are "inappropriate," falls through to **market price** — which [cost-not-price](cost-not-price.md) forbids, since price is supposed to be the *output* of the accounting, not an input.

The classical form is sharper. Once joint production is admitted, [Sraffa and Steedman showed labour values can go **negative**](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) — a commodity "containing" less than zero labour. Any single-substance cost accounting inherits this.

**This was registered as OP-17 and was the most dangerous open problem in the project.**

## The answer

> **A joint process's cost is not divided. Every co-product carries the whole cost of the process it came through, read against its own output mass.**

**Why there is nothing to divide.** The feed a steer eats is not spent partly on the beef and partly on the hide. **It is spent entirely on both.** Take the hide away and raising the animal costs the same. **So no fraction of the feed belongs to the beef, and any number claiming to be that fraction was invented.**

### A worked example, with digits

A process consumes **100 MJ** and **10 hours**, and yields **100 kg of A** and **300 kg of B**.

| | Energy | Labour |
|---|--:|--:|
| **A**, 100 kg | 100 ÷ 100 = **1.000 MJ/kg** | **0.100 h/kg** |
| **B**, 300 kg | 100 ÷ 300 = **0.333 MJ/kg** | **0.033 h/kg** |

**The books do not hold 200 MJ.** Both records point at **the same** 100 MJ — one supplier, one delivery, one record. [non-fungibility](non-fungibility.md) says a debit is a unique record of one specific event, **so a ledger walk is a union over identified parcels, never a sum.** One buyer taking both carries 100 MJ.

### What each process now has to supply

**Only whether a product passed through a step — a binary fact off a flow sheet.** The withdrawn rule needed the far stronger claim of **what share** of each step's energy each product took.

| Process | What is recorded | What is no longer needed |
|---|---|---|
| Steer | Which steps each cut passed through — the hide leaves before dry-aging | Energy of tissue deposition per gram, by tissue type |
| Refinery | Which units each fraction passed through | Enthalpy and hydrogen consumed per fraction |
| CHP plant | The plant's cost, and the mass or energy of heat and power delivered | The turbine's extraction curve as an allocator |

### Resolution moves a figure one way only

> **A coarse reading is a ceiling on a fine reading of the same chain**, because the steps a product passed through are a subset of all the steps and its mass is unchanged. **Equality holds only for a product that passes through the whole chain.**

**A 600 kg steer, 20 h and 500 MJ over seven steps.** Read as one block, the hide carries **12.5 MJ/kg**. Read as seven steps, it carries **2.0** — it never entered the dry-aging room, and dry-aging is 300 of the 500 MJ. **The packaged beef reads 2.0 either way.**

**So a producer wanting a lower figure has to buy more measurement.** Confirmed on 1,152 product-resolution pairs: `../06-simulation/chain-resolution/RESULTS.md`.
| Emission | Atmospheric chemistry + mitigation technology | Hours to remove a tonne, at today's best method |

**These are not rival conventions. They are different instruments reading the same underlying quantity.**

## Why the literature could not get here

Both the LCA and the Sraffian traditions searched for a **carrier quantity** — a property of the *outputs* by which cost could be apportioned. Every candidate works in some industries and is a category error in others.

**A carrier quantity is a property of the outputs. The allocation is a fact about the process.**

Aequitas can say this and they cannot, for one structural reason: **it has a universal denominator and they do not.** Under [time-as-yardstick](time-as-yardstick.md), every physical quantity in the ledger — a kilogram, a joule, a tonne of CO₂ — is already a proxy for hours-to-produce or hours-to-mitigate. So the question *"mass or energy?"*, which is unanswerable as posed, **never has to be asked.**

> **The universal is the denominator, not the carrier.**

## Mass is an estimator, not a rule

Where a joint output is **compositionally uniform**, cost per gram is genuinely constant and mass allocation is *correct* — the right arithmetic under a true premise. Splitting a homogeneous grain harvest by weight needs no apology.

Where composition varies, mass is the **low-resolution reading**: recorded at low confidence and superseded when better science arrives. This is ordinary [event-record](event-record.md) resolution behaviour, which is what makes mass safe to use — it stops being an arbitrary choice and becomes a stated approximation with a known direction of error.

## Four consequences

**Human preference plays no part.** A hide's figure does not change because leather is fashionable, exactly as manure's does not change because nobody wants it. **Nothing in the arithmetic reads what anyone wants** — only the process's cost and the output's own mass.

**Yield does, and that is deliberate.** A smaller output reads dearer per kilogram, because the same whole process stands behind less of it. **Output mass is physical and a scale reads it; demand and desirability are not, and nobody can weigh them.** Who receives a physically scarce output stays a [distribution](pledge-and-signal.md) question.

**Waste outputs are co-products like any other**, and a step no product passed through **reaches no product** and stays with the producer.

**Fate sets ledger character.** Manure is pollution debit in a lagoon, a genuine co-product in a biodigester, and an *observed* fertiliser offset when spread on fields. [event-record](event-record.md)'s fate closure already records this — no new machinery.

**Negative values do not arise.** Nothing is inverted and nothing is subtracted, so Steedman's result does not transfer. **The earlier simulation across 4,098 economies confirmed it for the withdrawn division; the result survives a fortiori here, because no division is performed at all.**

## What it does not solve

**Labour is no longer one of these.** The farmer's hours are the process's hours, and every co-product carries all of them against its own mass, exactly as the energy does. **The OP-18(α) convention — labour rides the material split — is withdrawn with the split it rode.** The *team* half of OP-18 stands: dividing a jointly-caused harm among the people who caused it is still a convention, and [§3.2c's hours basis](physical-trace-test.md) is the candidate answer.

**Shared overhead.** The barn shelters the whole animal. **All capital and overhead accrues to the asset**, never to the outputs, so there is nothing to inherit. OP-23.

**A false passage.** Claiming a co-product left the chain before work it really consumed would lower its figure. **That is a verification question rather than an accounting one**, and the event-record closure checks answer it. Not measured.

## Who games this

| Attack | Defence |
|---|---|
| **Ballast output** — make a worthless heavy output to soak up debit | **Nothing is soaked up.** Adding an output does not change any other output's figure, because no figure was ever a share of a pool |
| **Call a co-product waste, so the rest looks cheap** | **The label buys nothing.** The remaining product already carries the whole process cost |
| **Boundary gerrymandering** — read one process as two to lower the base | **Not an attack, it is resolution.** A coarse reading is a **ceiling** on a fine one, so a finer reading only ever lowers a figure — and it does so by being truer. **A producer wanting a lower figure has to buy more measurement** |
| **Instrument shopping** | **No instrument is chosen.** The cost of the process, the output masses and the passage list are all read at the fence |
| **Constant capture** — publish energetics favourable to your sector | [rival-sector-audit](rival-sector-audit.md). **Open — OP-24, unchanged** |

## Depends on

- [material-flow-value](material-flow-value.md) · [time-as-yardstick](time-as-yardstick.md) — the denominator that makes the rule possible
- [event-record](event-record.md) — a product's figure is computed at projection time; **no schema change was required**
- [retroactive-reweighting](retroactive-reweighting.md) — better process science re-weighs historical production

## Consequences

- [physical-trace-test](physical-trace-test.md) — the general rule this case produced
- [estimation-engine](estimation-engine.md) — materials and energy unblocked; labour is not
- [rival-sector-audit](rival-sector-audit.md) — what disciplines the cost constants
- [cost-not-price](cost-not-price.md) — the reply to ISO 14044's price fallback

## Open questions

- **Does the recursion converge?** Every input's debit is itself a joint process's cost. Confirmed for the withdrawn division across 4,098 economies; **not re-run under this rule.**
- OP-23 — shared overhead · OP-18 — labour and team credit · OP-24 — understatement drift

---
*Status: settled (the rule) / unproven (recursion convergence)*
*Source: `00-strategy/open-problems/OP-17_coproduct_allocation.md`; `00-strategy/Aequitas_Foundations_v0.4.md` §3.4a*
