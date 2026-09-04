# Method spread — how far a §3.4a split moves across honest methods

> **Date:** 2026-09-02 · **Code:** [`method_spread.py`](method_spread.py) · **Data:** [`method_spread.csv`](method_spread.csv)
> **Answers:** `sr-20260902-take-a-refinery-a-combined-heat-and-power-pl`, filed by the outreach agent for its public commitment at c37238.
> **Registers against:** Foundations §3.4a (joint production), closing paragraph — *"How far a split moves across honest methods. Nobody has measured this."*
> **⚠️ SUPERSEDED 2026-09-03.** The author withdrew the §3.4a split rule this file measures. **A joint process's cost is no longer divided at all**, so there is no declared basis, no conversion routing and no sub-process boundary to sweep. **This file is kept because it is the measurement that caused the withdrawal.** The rule that replaced it is measured in [`../chain-resolution/RESULTS.md`](../chain-resolution/RESULTS.md).
> **Status: ⚠️ LEG 1 OF 3 RUN.** The refinery leg is measured. The combined-heat-and-power leg and the livestock leg are not built. **The figures below are a floor on the method spread, not the whole of it.**

---

## 1. The question, and why it decides something

**Foundations §3.4a fixes four obligations on how a joint process's debit divides**, then leaves the method itself to the industry. Its own closing paragraph names the test that decides whether those obligations are enough:

> *"If the range is narrow, the obligations above are enough. If it is wide, method choice is a large lever and belongs with OP-10 (weighting governance)."*

**OP-10 (weighting governance) is the project's top blocking problem.** So this one measurement decides whether §3.4a is finished or feeds the largest open hole.

---

## 2. What was swept

**A joint process's split is not one choice. It is three, and [`../allocation-engine/refinery_slice.py`](../allocation-engine/refinery_slice.py) makes one reading of each.**

**Terms, so this reads without the other files open.**

| Term | What it means |
|---|---|
| **The declared basis** | Atmospheric and vacuum distillation heat the whole barrel to separate it. **No per-fraction trace exists**, so Foundations §2.5 requires a declared convention. `refinery_slice.py` declares **volume** |
| **The conversion routing** | Each conversion unit's metered energy goes to the products that unit makes. **Which products, in what shares, is modelled** — `REFINERY.md` §5 already calls it *"the remaining modelling layer"* |
| **The sub-process boundary** | Which units are read as traced, and which fall into the declared pool |

| Lever | Readings swept |
|---|---|
| **Declared basis** | volume · mass · equal split |
| **Conversion routing** | DOE Figure 2-2 · mass-weighted among named products · concentrated on each unit's primary product · equal among named products |
| **Sub-process boundary** | nine processes (published) · distillation read as traced · hydrotreating merged into the declared pool |

**3 × 4 × 3 = 36 methods.** Every one satisfies §3.4a's four published obligations. Energy figures are the real DOE 2015 Petroleum Refining Bandwidth Study per-process energies already loaded by `refinery_slice.py`.

---

## 3. The headline result

**Each fraction's share of the refinery's energy debit, across all 36 methods.**

| Fraction | Published | Min | Max | Spread, percentage points | Max ÷ min |
|---|--:|--:|--:|--:|--:|
| lpg | 5.0% | 1.3% | 15.1% | 13.9 | **12.02×** |
| gasoline | 55.1% | 35.4% | 60.8% | **25.4** | 1.72× |
| jet | 9.3% | 3.6% | 11.3% | 7.6 | 3.10× |
| diesel | 24.2% | 12.0% | 33.5% | 21.5 | 2.80× |
| residual_fuel | 1.1% | 1.1% | 8.0% | 6.9 | 7.36× |
| petcoke | 4.2% | 2.2% | 13.3% | 11.1 | 5.96× |
| asphalt | 1.1% | 1.1% | 8.0% | 6.9 | 7.36× |

**In plain words: two honest methods can disagree about what a barrel of LPG cost by a factor of twelve, and about gasoline by 25 percentage points of the whole refinery's energy.**

### The verdict, against a declared yardstick

**"Narrow" needs a yardstick or it is an opinion.** The yardstick used is the project's own already-measured number: `REFINERY.md` finds price allocation misprices petcoke by **5.7×**, and that divergence is the reason §3.4a rejects price allocation at all.

**The threshold is declared, not measured: a relative spread reaching half the price divergence — 2.85× — is treated as wide.** It is stated here so it can be argued with rather than buried (Foundations §2.5).

> **⚠️ WIDE. Five of the seven fractions exceed the threshold. Method choice moves the split by a factor comparable to the price allocation §3.4a exists to rule out.**

---

## 4. Which lever does the work — and this is the useful half

**Each row holds the other two levers at the published reading and moves one.** The basis row uses only volume and mass, the two physical bases of ISO 14044, so it is the fairest test of the declared convention on its own.

| Lever | Widest fraction | Max ÷ min |
|---|---|--:|
| **Declared basis** (volume vs mass) | asphalt | **1.29×** |
| **Conversion routing** | lpg | **6.31×** |
| **Sub-process boundary** | residual_fuel | **1.47×** |

**In plain words: the declared convention is nearly inert, and the modelled routing carries almost the whole spread.**

**That is not the result the project would have predicted.** Foundations §2.5 and §3.4a both treat the *declared convention* as the dangerous part — the place where a choice with no physical trace enters. **It turns out to be the safe part.** The danger sits in the layer §3.4a calls a measurement: *"each conversion unit's metered energy routes to the products it makes."* **The energy is metered. The routing to products is not, and nothing in §3.4a's four obligations requires it to be.**

### A worked example, with digits

Take LPG under three routings, holding the basis at volume and the boundary at the published nine processes.

| Routing | What it assumes | LPG's energy share |
|---|---|--:|
| **Concentrated** | Each unit's energy goes to its single primary product. LPG is nobody's primary product | **1.8%** |
| **DOE Figure 2-2** (published) | Standard refinery flow shares | **5.0%** |
| **Equal among named** | Each unit's energy splits equally among the products it names | **11.5%** |

**All three are honest. All three publish their method. All three satisfy §3.4a. They differ by 6.31×.**

---

## 5. A first run that had to be thrown out, and why it is recorded

**The first sweep included a fourth declared basis this project constructed: mass × the temperature rise to each cut's mid boiling point.** It returned a headline relative spread of **2,307×**.

**That number is an artefact of one arbitrary constant.** LPG's mid-cut boiling point is −20 °C, which is below ambient, so its temperature rise is negative and has to be clamped to a floor. The floor was set at 1 °C. **That single number handed LPG a 0.017% share against diesel's 40.1%, and produced the entire headline.**

**The basis is kept in the code as a labelled sensitivity rather than deleted**, and the run still prints it. Foundations §4.4: *a derived figure carries the label its arithmetic earns, never the one its author prefers.* **Deleting it would have been the flattering move — it makes the spread look worse than the defensible methods support.**

---

## 6. What this does not show

| | |
|---|---|
| **Two of the three legs are missing** | The combined-heat-and-power plant and the livestock case are not built. CHP is the leg with the most published rival methods, so it is likely to widen the result |
| **The period lever was not swept at all** | The DOE source is one annual figure. **No period can be swept from it**, and §3.4a names period as one of the choices |
| **One refinery** | A hydroskimming plant and a deep-conversion plant have different slates. Per-refinery is the high-resolution version |
| **Energy only** | Materials and labour ride the material split and were not swept |
| **The threshold is declared** | 2.85× is half the measured price divergence. A different yardstick gives a different verdict, and the raw spreads in §3 are what a reader should argue with |

**All five push the same way: the measured spread is a floor.**

---

## 7. What follows

**This is a finding against the project, and it is narrow and fixable.**

1. **§3.4a's four obligations do not cover the routing layer.** They require the method to be published. They do not require a routing to be metered rather than modelled, and they do not require a producer to say which it is. **A fifth obligation of that shape is the candidate repair** — and it needs stress-testing before anything is folded, because "state whether each routing share is metered or modelled" is cheap to satisfy and may buy nothing.
2. **The declared-convention worry can be relaxed, with evidence.** Volume against mass moves nothing much. That is worth saying in public, because it is the half of §3.4a a critic attacks first.
3. **Do not fold either point until legs 2 and 3 run.** One industry is one industry.

**Self-tests: 6/6 pass**, including a negative control that fails if the levers do not move the split, and a check that the sweep reproduces `refinery_slice.py`'s published figure exactly.

```bash
python 06-simulation/method-spread/method_spread.py --test
```
