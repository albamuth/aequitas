# SB-06 — How much dearer does a small producer's product read because they cannot afford instruments?

> **Request:** `sr-20260905-sweep-producers-of-one-good-by-scale-and-by-` · filed 2026-09-05, from **@coywolf** at c40752 on post 3551.
> **Status:** open. **Nobody has run this. No figures exist.**

---

## 1. The question

> **Take one physical process, held fixed. Vary only how finely each producer can afford to read it. Measure the spread in published debit-hours per kilogram between the best-instrumented and the worst-instrumented producer, and report whether that spread widens as the chain gets longer.**

## 2. What depends on it

**Foundations §3.4a** establishes that **a coarse reading is a ceiling on a fine reading of the same chain**. A product carries the cost of the steps it passed through, divided by its own mass; **those steps are a subset of all the steps, so the coarse figure can never be lower.** Confirmed on **1,152 product-resolution pairs, no exception.**

**The document reports three consequences, and calls all three good:**

> *"A coarse reading errs against the producer, never for them… A producer wanting a lower figure has to buy more measurement, so the incentive points at better instruments. And resolution is not a lever to police."*

**@coywolf's objection, and it is not a contradiction — it is the same fact read from the other side:**

> **Erring against the producer is honest, and it is also a charge on whoever cannot buy instruments.**

**Foundations §4.8 already registers this as a watch item** and says the offset — *helping someone join is credited work borne by the network rather than the entrant* — **is empirical and "should be watched rather than assumed."**

> **Nobody has watched it. There are no figures. This brief makes some.**

**And there is a worked precedent for the worry:** organic-certification cost-share programmes exist because documentation burdens were found to disadvantage small producers in practice.

## 3. Terms

| Symbol | What it means |
|---|---|
| **`S`** | Steps in the process chain. Swept — this is the second axis |
| **`E_s`** | Energy and labour consumed at step `s`. **Physically fixed. Identical for every producer** |
| **`r`** | A producer's **resolution**: how many of the `S` steps they read separately. `1 ≤ r ≤ S`. At `r` = 1 the whole chain is one opaque block |
| **`k`** | A producer's **scale** — output mass per period |
| **`c(r)`** | What resolution `r` costs to buy: instruments, calibration, record-keeping |
| **The published figure** | Debit-hours per kilogram, computed under §3.4a: **cost of the steps the product passed through, divided by its own mass** |
| **The spread** | `figure(worst-instrumented) ÷ figure(best-instrumented)`, **for the same physical good** |

## 4. The model

**Step 1 — fix the physics.** One chain of `S` steps with fixed `E_s`. **Every producer runs the identical process.** Co-products leave at different steps.

**Step 2 — give each producer a resolution they can afford.** Instrumentation is largely a fixed cost, so **cost per kilogram falls with scale**:

> **A producer of scale `k` can afford resolution `r` if `c(r) ÷ k ≤ θ`**, where `θ` is the share of output value a producer will spend on measuring itself.

**This is the whole mechanism: `r` rises with `k`.**

**Step 3 — compute each producer's published figure** under §3.4a at their own `r`, for the same co-product.

**Step 4 — sweep `S`** and report whether the spread widens with chain length.

### A worked example, with the numbers

**Foundations §3.4a's own case: one 600 kg steer, 500 MJ across seven steps, of which dry-aging is 300 MJ. The hide, 40 kg, leaves at step 2.**

| Producer | Resolution | What the hide is charged for | MJ/kg for the hide |
|---|---|---|--:|
| **Large, fully instrumented** | `r` = 7 | steps 1–2 only, 80 MJ | 80 ÷ 40 = **2.00** |
| **Small, one opaque block** | `r` = 1 | the whole 500 MJ | 500 ÷ 40 = **12.50** |

> **The spread is 6.25×, for physically identical hides off physically identical animals.**

**In plain words: the small producer's hide reads six times dearer, and nothing about their process was worse.** The only difference is what they could afford to measure.

**Now the second axis.** Because dry-aging is 300 of the 500 MJ, **most of that spread comes from one expensive step the hide never entered.** So the prediction is that **the spread grows with how unevenly cost is distributed along the chain**, not simply with `S`. **Test both.**

## 5. Inputs

**A generator, plus one real chain as an anchor.**

- **The real anchor:** the seven-step steer of §3.4a, digits above. **Reproduce the 2.00 and 12.50 first.** If you cannot, stop and tell us.
- **The generator:** sweep `S` ∈ [2, 20], the distribution of `E_s` (uniform, and heavily skewed), the scale distribution of producers, `θ`, and the shape of `c(r)`. **State your seed.**
- **`06-simulation/chain-resolution/`** holds our resolution machinery and the 1,152 pairs. **Section 4 is complete without it.**

## 6. What an answer looks like

| `S` | `E_s` shape | Spread, worst ÷ best | Median producer's figure ÷ best | Share of producers above 2× the best |
|--:|---|--:|--:|--:|
| 7 | skewed (steer) | 6.25 | | |
| … | | | | |

**Plus one line: does the spread widen with `S`, with the skew of `E_s`, or with neither?**

**And one number we specifically want:** **the share of producers whose figure is more than 2× the best-instrumented producer's.** That is the closest thing to "how many people does this actually hit."

## 7. Declared in advance

| | |
|---|---|
| **Our prior** | **The spread is driven by the skew of `E_s`, not by `S` itself.** A long chain of equal steps should produce a modest spread; a short chain with one dominant step should produce a large one. **We expect the median producer to sit much closer to the best than the worst does**, so the burden falls on a tail rather than on half the field |
| **Refutation threshold** | **If more than a third of producers publish figures above 2× the best-instrumented producer's, the §4.8 offset is not enough** and *"a producer wanting a lower figure has to buy more measurement"* is a charge on scale rather than an incentive |
| **What we do if it is crossed** | **§3.4a's three "things that follow" get a fourth, stating the cost.** §4.8's watch item is promoted to a named open problem with a measured size. **And the honest framing changes**: erring against the producer is no longer simply *"the direction §4.4's label rule asks for"* — it is that, **and** a scale-dependent charge |

**We do not have a defence ready if this comes back badly, and that is the reason to run it.** §4.8's offset — helping someone join is credited work — **reduces the cost of joining. It does nothing about the cost of instruments after you have joined.**

## 8. Self-tests, each able to fail

1. **Reproduce §3.4a's published digits:** hide at `r` = 7 reads **2.00 MJ/kg**, at `r` = 1 reads **12.50 MJ/kg**, and **packaged beef reads 2.00 either way**. If beef moves, the model is wrong.
2. **A coarse reading is never lower than a fine one, for any product, at any `S`.** This is §3.4a's ceiling result and **it must hold in your implementation too**. A violation means the walk is wrong, not that we are.
3. **At `r` = `S` every producer publishes the same figure.** With instruments free, scale does not matter.
4. **A product that passes through every step reads the same at every `r`.** The ceiling is tight only for that product.
5. **Total energy is conserved across resolutions.** `Σ E_s` does not change when you read the chain differently.

## 9. Out of scope

- **Whether §3.4a is right.** The ceiling result is measured and this brief assumes it. **This is about who pays for it.**
- **The cost of joining a network.** §4.8's offset covers that. **This is the recurring cost of instruments afterwards.**
- **Cross-network comparison.** One network's books, per §4.0.

## 10. Known ways to get this wrong

- **Sweeping `S` with uniform `E_s` only.** The steer case is heavily skewed and that is where the effect lives. **A uniform-only sweep will report no problem and will be wrong.**
- **Letting the physical process vary with scale.** Then you are measuring real efficiency differences, not the resolution tax. **`E_s` must be identical for every producer.**
- **Reporting the worst-case spread alone.** The worst case is one producer. **The share above 2× is the number that says how many people it hits.**
