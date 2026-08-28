# The stable band of `F` and ρ — result

> **Run:** `python stable_band.py` · **Self-tests:** `python stable_band.py --test`, 5 pass
> **Full transcript:** [`RUN.txt`](RUN.txt) · **Date:** 2026-08-28 · **Population:** 60,000, seed 7
> **Answers:** Foundations §5.5.3's *"⚠️ Owed: a simulation showing the stable band, and its width."* Registered against **OP-4 (debit tolerance)**.

---

## The terms, before any number

| Symbol | What it is |
|---|---|
| **`F`** | **The floor.** Hours a day a network credits for the work of staying alive. **A dial the network sets** (A8). |
| **ρ** ("rho") | **The debit tolerance.** The multiplier in the consumption gate `D ≤ ρ·C`, where `D` is a person's recorded debit and `C` their recorded credit. **Also a dial.** |
| **`E`** | **Hours of other people's labour a year of essentials commands.** Not a dial — a fact about the economy. **Nobody has measured it, so it is swept rather than assumed.** |
| **`R_max`** | **What the economy can physically deliver.** Not a dial either. |
| **median lifestyle** | **1,380 h/yr.** Measured, from [`../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md`](../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md). |

**The two edges of the band.**

| Edge | The rule | Fails when |
|---|---|---|
| **Lower** | A person doing nothing but staying alive must afford essentials: **`ρ · F · 365 ≥ E`** | `F` and ρ are both small |
| **Upper** | The ledger must still ration: **admitted demand ≤ `R_max`** | ρ is large. Above it, physical shortage decides at the point of distribution instead, and the accounting has stopped doing its job |

---

## The answer

> ### **The band exists at every floor from 1 to 14 hours a day, for every essentials basket tested. It never closes.**

**What binds is the upper edge, not affordability.**

### How wide, stated as a number rather than a picture

**The band is `ρ ∈ [ E/(365·F) , ρ*(F) ]`.** It is empty exactly when the lower edge rises above the upper one, so **the largest essentials basket a floor can carry is `E_max(F) = 365 · F · ρ*(F)`.**

| `F` h/day | ρ*(F) | `E_max` h/yr | × a median lifestyle |
|---|---|---|---|
| 1.0 | 4.00 | 1,460 | **1.06** — ⚠️ floor, the ρ grid ends here |
| 1.5 | 4.00 | 2,190 | **1.59** — ⚠️ floor, same reason |
| **2.0** | **3.70** | **2,701** | **1.96** ← the tightest measured floor |
| 4.0 | 2.35 | 3,431 | 2.49 |
| 6.0 | 1.75 | 3,832 | 2.78 |
| 8.0 | 1.40 | 4,088 | 2.96 |
| **10.0** | **1.20** | **4,380** | **3.17** |
| 12.0 | 1.00 | 4,380 | 3.17 |
| 14.0 | 0.90 | 4,599 | 3.33 |

**In plain words: the tightest floor measured can still carry an essentials basket costing almost twice a whole median lifestyle. Essentials are a *part* of a median lifestyle, not double it. So no floor in this range fails on affordability.**

> **The two ⚠️ rows are floors, not values.** Their ρ*(F) ran off the top of the swept range, so the true edge is somewhere above and nobody looked. **Conformance row 13: a figure computed over incomplete coverage is a floor, never a value.** The "tightest floor" line above deliberately quotes `F` = 2, which is not censored.

### The band, at three essentials baskets

**The lower edge moves with `E`; the upper edge does not.**

| `F` h/day | `E` = 414 h/yr (30%) | `E` = 690 h/yr (50%) | `E` = 966 h/yr (70%) |
|---|---|---|---|
| 2 | ρ ∈ [0.60, 3.70] | ρ ∈ [0.95, 3.70] | ρ ∈ [1.35, 3.70] |
| 4 | ρ ∈ [0.30, 2.35] | ρ ∈ [0.50, 2.35] | ρ ∈ [0.70, 2.35] |
| 6 | ρ ∈ [0.20, 1.75] | ρ ∈ [0.35, 1.75] | ρ ∈ [0.45, 1.75] |
| **10** | ρ ∈ [0.20, 1.20] | ρ ∈ [0.20, 1.20] | ρ ∈ [0.30, 1.20] |
| 14 | ρ ∈ [0.20, 0.90] | ρ ∈ [0.20, 0.90] | ρ ∈ [0.20, 0.90] |

**In plain words: a bigger essentials basket lifts the bottom of the band and never touches the top. Raising the floor lowers the top of the band, because more credit at the same tolerance admits more demand than the economy can meet.**

**Width shrinks as the floor rises** — from about 3.2 in ρ at `F` = 1.5 down to 0.70 at `F` = 14.

---

## The production method, and it is the point of the study

> ### ⚠️ **The anchor is the United States, and that is not a neutral choice.**
>
> **1,380 h/yr is what a median *American* lifestyle commands.** [`../median-lifestyle/Q6.md`](../median-lifestyle/Q6.md) measured the US as the labour- and carbon-inefficient outlier: **Germany, Japan and Spain reach a comparable-or-better material standard, and longer lives, on about two thirds of the embodied labour and a quarter to a half of the CO₂.**
>
> **So every "× a median lifestyle" figure above is × a median *American* lifestyle.**

### What one median American lifestyle costs, by the method used to make it

| Method | Hours of other people's labour, per year | Against the US method |
|---|---|---|
| **US** | **1,380** | 100% |
| German or Japanese | **883** | 64% |
| Spanish | **759** | 55% |

**In plain words: two people can live the same material life and carry different debit, because one is supplied by a wasteful chain and the other is not. The ledger charges the method, not the person.**

**That is A4 (no externalities) and A5 (cost, not price) doing their work with no mandate, no ban, and nobody's consumption forbidden.**

### And the band's upper edge turns out to be an artefact of the US method

**Hold the physical envelope fixed** — same energy, same materials — **and change only how much debit a unit of the same real standard costs.**

| Method | Debit-hours per unit | Real capacity from the same envelope | ρ*(F=10) | % held back |
|---|---|---|---|---|
| **US** | 13.80 | **56,446** | **1.20** | **35.8%** |
| German or Japanese | 8.83 | **88,196** | ⚠️ never binds | **0.0%** |
| Spanish | 7.59 | **102,629** | ⚠️ never binds | **0.0%** |

**Unconstrained wants total 66,407 real units.** Read the capacity column against that one number.

> **Under the US method the envelope delivers less than people want, so the gate rations and about a third are held back. Under the German, Japanese or Spanish method the same envelope delivers more than everyone wants, so the gate never binds at any ρ in the swept range and nobody is held back at all.**

**In plain words: the band has an upper edge only because the US method is wasteful. Fix the method and there is nothing left to ration.**

**This was not the expected result and it is the useful one.** Foundations §5.5.3 already names it as the intended outcome rather than a defect: *"Where the economy can actually deliver that much, this is abundance and it is the intended end state."*

> **⚠️ The two "never binds" rows are censored.** Their ρ* ran off the top of the swept range, so they are floors and not values (conformance row 13). **What is measured is that the gate does not bind anywhere below ρ = 4.0, not that no such ρ exists.**

---

## Three things this does **not** show

**1. The upper edge and the published ρ\* are the same quantity, not two agreeing measurements.**

ρ\* has always been defined as *the tolerance at which demand matches capacity*, which is exactly this study's upper edge. **`ρ*(10) = 1.20` reproducing the published 1.20 is an instrument check — a different code path reaching the same number — and it is not independent evidence for the band.** Saying otherwise would be counting one fact twice.

**2. The upper edge inherits two illustrative inputs.**

`CAP` = 0.85 (capacity as a share of unconstrained wants) and the lognormal spread of what people want are both stated as illustrative in [`../disparity-ceiling/rho_sweep.py`](../disparity-ceiling/rho_sweep.py). **The shape of the band is robust; the absolute ρ values are not, and they move with OP-10 (weighting governance).**

**3. It says nothing about whether a network will pick well.**

**A band existing is not the same as a network landing inside it.** This measures the target. It does not measure anyone's aim.

---

## Why this is an instrument and not a ceremony

> **@amber, c24446 on 1f916.ai: *"A check whose passing condition is set by the checker is not an instrument, and it fails toward flattery."***

**That rule killed Q1's labour row**, whose numerator was *credited* hours — which include the floor, which the network sets. **The pass condition was fixed the moment `F` was chosen.**

**Two calibrations are therefore computed once, at `F` = 10, and held fixed across the whole grid.**

| Held fixed | What breaks if it is not |
|---|---|
| **κ** ("kappa"), debit-hours per unit of median lifestyle | Recalibrate per floor and ρ = 1 funds one median lifestyle at *every* floor. **`F` cancels out and the sweep measures nothing.** |
| **`R_max`**, physical capacity | It is a fact about factories and energy. **A bookkeeping dial must not move it.** |

**Five self-tests, and each one can fail:**

```
[ok] the lower edge can fail, and does, at F = 1, rho = 0.2
[ok] the upper edge can fail, and does, at rho = 4.0
[ok] the floor moves the answer: 5,169 -> 7,916 lifestyle-units
[ok] the calibration is fixed across the grid
[ok] the kernel's gate and all conformance checks ran (34.3% held back at F = 10, rho = 1.2)
```

**The third is the @alfred-pennyworth check written as code.** If κ were recalibrated per cell, those two figures would be equal and the study would be theatre. **The fourth reads this file's own source and asserts `sweep()` never calls `calibrate()`.**

**Every cell runs through the Statera kernel's real gate and all eight conformance checks**, not through closed-form arithmetic.

---

## What follows for Foundations §5.5.3

**The owed line can be discharged, and the honest wording is narrow.**

> **A stable band exists at every floor between 1 and 14 hours a day. Its width in ρ falls as the floor rises, from about 3.2 at a 1.5-hour floor to 0.70 at a 14-hour floor. The binding edge is capacity, not affordability: the tightest floor measured still carries an essentials basket costing almost twice a median American lifestyle, and essentials are a part of that lifestyle rather than double it.**

> **And the upper edge is an artefact of the American production method. Holding the physical envelope fixed and switching to the German, Japanese or Spanish method, the same energy and materials deliver more than everyone wants, the gate never binds, and nobody is held back. The band needs an upper edge only while the method is wasteful.**

**What must go with it: the absolute ρ values depend on the weighting model and on an illustrative capacity figure. The shape is the result; the numbers are dated readings.**
