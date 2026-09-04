# Chain resolution — what detail buys, and what a naive ledger walk costs

> **Date:** 2026-09-03 · **Code:** [`chain_resolution.py`](chain_resolution.py) · **Data:** [`chain_resolution.csv`](chain_resolution.csv)
> **Answers:** the author ruling of 2026-09-03 — *a joint process's cost is not divided.*
> **Replaces:** [`../method-spread/RESULTS.md`](../method-spread/RESULTS.md), whose question no longer exists.
> **Status: COMPLETE for the two cases it carries.** 8/8 self-tests pass.

---

## 1. What was asked

**The ruling withdrew the §3.4a split.** A joint process's cost is no longer divided among its outputs. **Every co-product carries the whole cost of the process it came through, read against its own output mass.** That raised two questions and this run answers both.

| | The question |
|---|---|
| **Q1** | **If nothing is divided, do the books inflate?** Two co-products each carrying "100 MJ" look like 200 MJ |
| **Q2** | **Does reading the chain more finely change the answer, and in which direction?** |

**Terms, so this reads without the code open.**

| Term | What it means |
|---|---|
| **A step** | One resolvable stage of a process — a kill, a hide removal, a distillation column |
| **A resolution** | A way of grouping the steps into **blocks**. A block is **opaque**: you see what went in and what came out, and nothing between |
| **Coarsest** | One block. *One cow in, co-products out* |
| **Finest** | One block per step |
| **Passage** | Whether a product went through a step. **Binary, off a flow sheet.** It is not a share |
| **Union** | Adding a buyer's parcels by **counting each identified record once** |
| **Naive sum** | Adding the figures as if they were amounts. **This is the defect, never the rule** |

**A product that passed through any step of an opaque block carries the whole block**, because from outside the block there is no way to say which part it used, and inventing one is the modelled layer this ruling withdrew.

---

## 2. Q2 first — a coarse reading is a ceiling, and the theorem holds

> **A product carries the cost of the steps it passed through, divided by its own mass. Those steps are a subset of all the steps, and its mass is the same either way, so the coarse figure can never be lower.** Equality holds only for a product that passes through the whole chain.

**Confirmed on 1,152 product-resolution pairs across both cases. No exception.**

### The steer — 7 steps, 4 co-products, all 64 resolutions swept

*(⚠️ The digits are illustrative and are declared as such. One 600 kg steer, 20 h of labour, 500 MJ, 15 kg of pollutants.)*

| Co-product | mass kg | dimension | coarsest | finest | coarse ÷ fine |
|---|--:|---|--:|--:|--:|
| **hide** — leaves at step 2 | 40 | labour h/kg | 0.5000 | **0.1250** | **4.00×** |
| | | energy MJ/kg | 12.500 | **2.000** | **6.25×** |
| | | pollutant kg/kg | 0.3750 | **0.0750** | **5.00×** |
| **organs** — step 3 | 60 | labour h/kg | 0.3333 | **0.1167** | 2.86× |
| | | energy MJ/kg | 8.333 | **2.000** | 4.17× |
| **hooves and head** — step 4 | 30 | labour h/kg | 0.6667 | **0.2667** | 2.50× |
| | | energy MJ/kg | 16.667 | **4.667** | 3.57× |
| **packaged beef** — step 7 | 250 | labour h/kg | 0.0800 | **0.0800** | **1.00×** |
| | | energy MJ/kg | 2.000 | **2.000** | **1.00×** |

**In plain words: reading the chain finely lowers the figure for anything that leaves early, and leaves the figure for the thing that goes all the way through exactly unchanged.** The hide never entered the dry-aging room, and dry-aging is 300 of the 500 MJ. **The fine reading stops charging it for one.**

### The refinery — 8 units, 7 fractions, all 128 resolutions swept

**Real DOE 2015 Petroleum Refining Bandwidth Study per-process energies**, taken from [`../allocation-engine/refinery_slice.py`](../allocation-engine/refinery_slice.py). Masses from EIA-representative yields × densities, per 100 barrels of crude.

| Fraction | mass kg | coarsest MJ/kg | finest MJ/kg | coarse ÷ fine |
|---|--:|--:|--:|--:|
| gasoline | 5,765 | 0.3674 | 0.2944 | **1.25×** |
| diesel | 4,006 | 0.5286 | 0.3247 | 1.63× |
| jet | 1,272 | 1.665 | 0.8483 | 1.96× |
| petcoke | 835 | 2.537 | 1.126 | 2.25× |
| residual fuel | 472 | 4.485 | 1.749 | **2.56×** |
| asphalt | 491 | 4.311 | 1.681 | **2.56×** |
| lpg | 437 | 4.844 | 2.351 | 2.06× |

**In plain words: gasoline moves least because it passes through the most units, and the heavy bottoms move most because they leave after distillation.** Nothing moves the wrong way.

> **What is DECLARED here, stated so it can be argued with:** the processing order, and which fractions pass through which unit. That is a standard refinery configuration. **It is binary — did this fraction go through this unit, yes or no — and it is read off a flow sheet.** The withdrawn rule needed the far stronger claim of **what share** of each unit's energy each fraction took, and that share is what moved LPG by **6.31×** on 2026-09-02.

---

## 3. Q1 — the books do not inflate, and here is the size of the mistake if you get it wrong

**A3 (non-fungibility):** *"Every credit and every debit is a unique record of one specific event."* **A debit is a pointer at an identified parcel, not an amount.** Two co-products naming the same 100 MJ name **one record**.

**So the ledger walk is a union over identified parcels, never a sum.** One buyer taking every co-product:

| Case | Resolution | **Union** | Naive sum | Sum inflation |
|---|---|--:|--:|--:|
| **Steer**, energy MJ | coarsest | **500** | 2,000 | **4.00×** |
| | finest | **500** | 840 | 1.68× |
| **Refinery**, energy MJ | coarsest | **2,118** | 14,826 | **7.00×** |
| | finest | **2,118** | 7,697 | 3.63× |

**And the union does not move.**

| Case · dimension | Distinct **union** values across all resolutions | Distinct **naive sum** values |
|---|--:|--:|
| Steer · labour | **1** | 13 |
| Steer · energy | **1** | 16 |
| Steer · pollutants | **1** | 11 |
| Refinery · energy | **1** | 111 |

**In plain words: the union figure is exactly the chain total, at every one of the 192 resolutions swept, in both cases. The naive sum overstates it by up to 7× and gives a different answer every time you re-read the same chain at a different level of detail.**

> **The 7.00× is the refinery's seven fractions.** That is the number the nightcheck plan of 2026-09-03 first reported as a property of the ruling. **It is not. It is the size of the error an implementation makes if it treats a debit as a quantity rather than as a unique record.**

---

## 4. Three things that follow

1. **Totals are invariant.** Labour, energy and pollutants are inputs, and reading them more finely does not change them. Confirmed at every resolution.
2. **A coarse reading errs against the producer, never for them.** That is the safe direction, and it is the one Foundations §4.4's label rule asks for: a figure carries the label its arithmetic earns.
3. **A producer wanting a lower figure has to buy more measurement.** **The incentive points at better instruments**, which is the fecundity direction. **Under the withdrawn rule, more information moved a figure in an unknown direction — that was the whole of the 6.31×.**

---

## 5. What this does not show

| | |
|---|---|
| **Two cases** | A steer and a refinery. A combined-heat-and-power plant, a chemical plant and a farm are not built |
| **The steer's digits are invented** | The **shape** is the result. The numbers are illustrative and are labelled as such in the code |
| **The refinery's passage table is declared** | The energies are real DOE actuals. **Which fraction passes which unit is a standard configuration, not a measurement taken here** |
| **Contiguous partitions only** | A block is a stretch of process you cannot see inside. A block made of step 1 and step 7 but not the ones between describes no real opacity, so it is not swept |
| **No fraud model** | Whether a producer can declare a **false** passage — claiming a product left before work it really consumed — is a verification question, and the integrity checks (conformance row 7, IC-1 to IC-6) are what answer it. **Not tested here** |

**The first four push the same way: the measured coarse-to-fine ratios are one chain's, not every chain's.**

---

## 6. Self-tests

**8 of 8 pass**, including a negative control that fails if resolution does not move the figures, and a universality guard that fails if any product's figure depends on another product's mass.

```bash
python 06-simulation/chain-resolution/chain_resolution.py --test
```

| Test | What it would catch |
|---|---|
| `totals_invariant` | Resolution changing an input |
| `coarse_is_a_ceiling` | The theorem failing on any of 1,152 pairs |
| `terminal_product_never_moves` | A whole-chain product moving with resolution |
| `union_equals_chain_total` | The union rule over- or under-stating |
| `naive_sum_inflates_and_moves` | The defect not being demonstrated |
| `the_sweep_actually_varies` | **Negative control** — an inert sweep proving nothing |
| `no_share_is_ever_computed` | **A split smuggled back in** — another product's mass changing this one's figure |
| `unpassed_step_charges_nobody` | A step no product passed reaching a product instead of staying with the producer (§3.2b) |
