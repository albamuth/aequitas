# The Simulations, in Plain Language — a skeptical tour

> **Who this is for:** anyone who wants to know what the code in this folder actually did, whether the results mean anything, and where to look to check the math — *without* needing a background in economics or linear algebra.
> **The spirit of it:** you asked the right question — *did we just generate the answer we wanted to see?* This document takes that suspicion seriously and walks through each simulation asking exactly that. Some come out looking solid. One is honestly just a worked example. Let's find out which is which.

---

## Start here: the worry worth having

There is a failure mode that haunts any project like this. You believe something ("physical cost accounting is better than price accounting"), you write a program, and — surprise — the program agrees with you. But of course it does: *you wrote it.* A simulation that can only ever confirm the thing you built it to confirm has told you nothing. It's a mirror, not a microscope.

So the honest question isn't "did the simulations pass?" It's: **for each one, could it have failed? And if it couldn't have, then passing means nothing.**

Let's go through them with that knife out. There are four.

Two of them, I think, survive the knife. One is real but limited. And one is — I'll say it plainly — a worked example with made-up numbers that proves our arithmetic is self-consistent and *nothing whatsoever about the real world.* Knowing which is which is the whole point.

---

## The problem sitting underneath everything

Before the simulations make sense, here's the problem they're all circling.

Imagine a cow. You spend money, feed, water, and labour raising it. Out the other end come several different things at once: steak, hamburger, leather (from the hide), tallow (fat), bone, manure. **One process, many products.** Now: how much of the cost of raising the cow does the *leather* owe? How much does the *steak* owe?

There's no obvious answer, and that's not a failure of imagination — it's a genuinely hard, roughly century-old problem. Economists call it [**joint production**](https://en.wikipedia.org/wiki/Joint_product). Accountants call it the [**cost allocation**](https://en.wikipedia.org/wiki/Cost_allocation) problem. Environmental scientists hit the exact same wall and call it the [**allocation problem in life-cycle assessment**](https://en.wikipedia.org/wiki/Life-cycle_assessment).

You could split the cost by **weight** (the heavy bits owe more). Or by **energy content**. Or by **price** (the valuable bits owe more). Each rule gives a *completely different* answer, and — this is the punchline the literature keeps arriving at — none of them is obviously "the truth." The valuable-bits-owe-more rule (splitting by price) is what standard economic accounting actually does, mostly because nothing else is available.

Aequitas's bet is that there *is* a physical truth here: **split the cost by where the process physically sent its inputs** — measure where the feed-energy actually went in the cow, where the crude actually went in the refinery. The simulations are attempts to check whether that bet holds together.

Now, the four simulations.

---

## Simulation 1 — the self-eating economy

**Files:** [`recursion_convergence.py`](recursion_convergence.py), write-up [`RESULTS.md`](RESULTS.md), **raw data `results.csv` (5,224 rows).**

### The question it's actually asking

Here's a wrinkle that makes cost accounting genuinely tricky. **The economy feeds itself.** You need steel to build the machines that make steel. You need electricity to run the pumps that pump the oil that fuels the power plant that makes the electricity. So the cost of steel depends on the cost of steel. It's a circular definition.

Circular definitions can do one of two things. They can **settle** — like echoes in a canyon, each bounce fainter than the last, until they die away to a definite total. Or they can **blow up** — like a microphone held too close to its own speaker, the squeal feeding itself louder and louder to infinity. Which one does Aequitas's cost calculation do?

And there's a second, sharper worry. When mathematicians tried to do this kind of self-referential cost calculation the *old* way (using money-values and a bit of algebra that involves "dividing" by the production process), they discovered something absurd: sometimes the math says a product contains a **negative amount of cost.** A barrel of oil that took *less than zero* effort to make. That's not a rounding error; it's a famous, real result from the 1970s ([Ian Steedman](https://en.wikipedia.org/wiki/Ian_Steedman), building on [Piero Sraffa](https://en.wikipedia.org/wiki/Piero_Sraffa)'s [*Production of Commodities by Means of Commodities*](https://en.wikipedia.org/wiki/Production_of_Commodities_by_Means_of_Commodities)), and it was a genuine embarrassment for that whole school of economics. **Does Aequitas's way of splitting costs fall into the same trap?**

### What the simulation did

It built 5,224 pretend economies — different sizes, different amounts of "self-feeding," different degrees of joint production — and for each one it ran the cost calculation and asked: (1) did it settle or blow up? (2) did any product come out with negative cost?

It also ran the *old* money-value method on the same economies, as a control, to see whether that one produced the negative-cost absurdity.

### What it found — and why it isn't wish-fulfillment

- Every economy that was "productive" (produced more than it consumed) **settled to a definite answer. 100% of them** — 4,098 out of 4,098.
- **Not one** produced a negative cost. (The most negative number anywhere was 0.0000000000000029 — that's a floating-point rounding speck, i.e. zero.)
- The old money-value method, on the *same* economies, produced negative or nonsensical costs **94.6% of the time.**

Now — why is this *not* just the mirror-trap? Because the result isn't something the simulation "discovered." It's a **mathematical theorem you can look up.** Aequitas's cost split, written out, is what's called a [**Neumann series**](https://en.wikipedia.org/wiki/Neumann_series) of a [non-negative matrix](https://en.wikipedia.org/wiki/Nonnegative_matrix) — and there's a classical theorem ([Perron–Frobenius](https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem), and the same math [Wassily Leontief](https://en.wikipedia.org/wiki/Wassily_Leontief) built [input–output economics](https://en.wikipedia.org/wiki/Input%E2%80%93output_model) on) guaranteeing that such a series settles to a unique, non-negative answer whenever the economy is productive. The condition for "productive" even has a name: the [**spectral radius**](https://en.wikipedia.org/wiki/Spectral_radius) being less than 1.

The reason Aequitas dodges the negative-cost trap is almost embarrassingly simple: the old method **divides by** the production process (matrix inversion), and dividing can flip signs. Aequitas only ever **multiplies and adds** non-negative quantities, and you cannot add positive things and get a negative. That's it. The simulation isn't *proving* this — it's *confirming* that a known theorem behaves as advertised across thousands of cases. A simulation confirming a theorem is about as trustworthy as simulations get.

**Could it have failed?** Yes — if the theorem didn't apply (e.g. if the "split fractions" could be negative, or if productive economies could still blow up). It didn't. And I re-checked the raw `results.csv` by hand while writing this: the 4,098 / 0-negatives / 94.6% numbers are all really in the data, not just in the write-up.

### The one honest caveat

The theorem assumes the split fractions (where the process sent its inputs) are **real, measurable, non-negative numbers.** The simulation *assumes* those exist and are given; it does **not** prove you can actually measure them for a real cow or a real refinery. So this result proves: *if* you can physically measure the split, *then* the accounting is mathematically well-behaved and never absurd. Whether you *can* measure the split is a different question — that's what Simulation 4 starts to probe with real data.

---

## Simulation 2 — checking our homework against the standard tool

**File:** `exiobase_loader.py` (described in [`ESTIMATION.md`](ESTIMATION.md) §5).

### The question

Fine, the method is internally sound. But does our *code* actually compute standard economics correctly, or did we make a mistake somewhere? The cleanest way to check: take a real, widely-used academic dataset and tool, feed the same data through our code, and see if we get the same answer.

The tool is [**pymrio**](https://github.com/IndEcol/pymrio), an open-source library economists use to analyse [**EXIOBASE**](https://www.exiobase.eu/), a large real-world database of how every industry's output flows into every other industry (the "environmentally-extended input–output" tables — the same [input–output](https://en.wikipedia.org/wiki/Input%E2%80%93output_model) idea from Simulation 1, but with real data and pollution/energy figures attached).

### What it found

Our code reproduced pymrio's own footprint numbers **to fourteen decimal places** (the difference was 0.000000000000057 — machine rounding). 

**Why this matters, and why it's genuinely reassuring:** pymrio is external. We didn't write it, we can't fudge it, and thousands of researchers rely on it. Matching it exactly means our engine is not doing anything weird or broken — it's doing textbook economics correctly. This is the "check your new calculator against a trusted one" test, and we passed it.

**The catch, which we flag loudly:** matching the standard tool means that *on this particular data, we did nothing new.* EXIOBASE has already split its joint production the old way (essentially by price), so feeding it through our engine can only ever reproduce the old answer. To show Aequitas does something *different*, we need data where the physical split hasn't already been thrown away. That's Simulation 4.

---

## Simulation 3 — the pretend cow (this is the honest one)

**File:** [`estimation_engine.py`](estimation_engine.py), write-up [`ESTIMATION.md`](ESTIMATION.md), table `estimation_debit_vectors.csv`.

I want to be very direct about this one, because it's the one most vulnerable to your suspicion.

### What it is

It's a made-up economy — twelve products, a cattle process, a tannery — with **invented numbers.** Not estimated, not sourced: invented, to be plausible and illustrative. It then checks a handful of things: that the cost splits add up correctly, that labour is handled by the "rides the material split" rule, and — the headline — that a pound of tenderloin and a pound of hamburger come out costing **the same**, even though tenderloin is rare and expensive.

### What it does and does not prove

Here's the thing you should hold onto: **the tenderloin-equals-hamburger result is not a discovery. It's arithmetic falling out of a choice we made.** We *decided* to split the cost by weight (a pound is a pound), so of course a pound of one costs the same as a pound of the other. If we'd split by price, the tenderloin would come out more expensive. The simulation didn't find that physical cost ignores scarcity; it *implements a rule that ignores scarcity* and then confirms the rule does what the rule says.

Is that worthless? No — but it's important to be exact about what it's worth. It's a **worked example**, like a physics problem that says "assume a frictionless cow." It proves that our *code correctly implements our own rules* — that the spec and the software agree, that nothing contradicts itself, that the accounting conserves (nothing created or destroyed). That's a real and necessary check on the *software*. But it is **not evidence about real cattle**, and it would be dishonest to present it as such. The numbers are ours; the world didn't supply them.

Think of it as the difference between "our recipe is internally consistent" and "our cake tastes good." Simulation 3 checks the recipe. Only real data checks the cake.

### Where it's genuinely interesting anyway

One part *does* rise above pure tautology: it shows the rule is **self-consistent across a whole connected economy** (the cattle feed comes from grain, which needs electricity, which needs fuel, in a loop), and that every product's cost stays positive and finite — which is Simulation 1's theorem showing up again in a concrete case. And it lets you *see* the mechanism working, which is worth something for understanding. But as evidence that Aequitas is *right about the world*, this simulation contributes essentially nothing, and you were correct to smell that.

---

## Simulation 4 — the real refinery

**File:** [`refinery_slice.py`](refinery_slice.py), write-up [`REFINERY.md`](REFINERY.md), table `refinery_allocation.csv`, data sources [`../00-strategy/GLOSSARY.md#src-refinery-process-energy`](../docs/GLOSSARY.md#src-refinery-process-energy).

This is the one that uses **real government data** and produces a finding that isn't baked in from the start.

### The setup

An [oil refinery](https://en.wikipedia.org/wiki/Oil_refinery) is the joint-production problem in its purest form: one stream of crude oil goes in, and out come gasoline, diesel, jet fuel, [petroleum coke](https://en.wikipedia.org/wiki/Petroleum_coke) ("petcoke"), fuel oil, asphalt, and more — all at once. How much of the refinery's energy does each product "owe"?

The standard answer (what economic databases use) is: **split by revenue** — the valuable products owe more. Aequitas's answer is: **split by the energy each product's processing actually consumed.** Do these disagree? And if so, who's right?

To answer, we needed real numbers for how much energy each refining step uses. Those come from the **U.S. Department of Energy's 2015 Petroleum Refining Bandwidth Study** — actual measured energy consumption, process by process, for the whole U.S. refining sector in 2010. (An amusing side-note: the tool we first used to read the DOE report claimed the PDF was "corrupted." It wasn't — the automated reader just choked on it. The real text was fine, and the numbers are in [`../00-strategy/GLOSSARY.md#src-refinery-process-energy`](../docs/GLOSSARY.md#src-refinery-process-energy) for anyone to check.)

### The finding

Split by revenue vs. split by real energy give **materially different answers**, and the most striking case is **petcoke**:

| product | costs this much under **energy** | costs this much under **price** | ratio |
|---|--:|--:|--:|
| **petcoke** | 0.33 (MMBtu/barrel) | 0.06 | **5.7× more** |
| LPG | 0.39 | 0.15 | 2.6× more |
| gasoline | 0.44 | 0.40 | about the same |
| diesel | 0.31 | 0.43 | 0.7× (less) |
| fuel oil | 0.14 | 0.25 | 0.6× (less) |

**Read petcoke's row slowly, because it's the whole point.** Petcoke is a cheap leftover — it sells for almost nothing. So price-based accounting treats it as if it cost almost nothing to make. But petcoke comes out of the [coker](https://en.wikipedia.org/wiki/Delayed_coker), one of the most energy-hungry units in the refinery. It really did soak up a lot of energy. Aequitas's physical accounting says petcoke costs about **5.7 times more** than its price implies. Price accounting was, in effect, *hiding* petcoke's real footprint by pointing at its cheap sticker.

### Is *this* one wish-fulfillment?

Partly real, partly modelled — and it's important to separate the two:

- **The direction of the finding is grounded in facts we didn't choose.** Petcoke is cheap: real market fact. Coking is energy-intensive: real DOE measurement. Put those two undeniable facts together and petcoke *must* come out under-costed by price accounting. That conclusion isn't something we dialled in; it falls out of external data.
- **The exact number (5.7×) depends on modelling choices we did make** — chiefly, our assumption about *which* products each refinery unit's energy should be credited to (the "routing"). We used standard refinery-flow knowledge for that, and flagged it as the one piece still to be pinned down against a published source. So trust the **direction and rough size** of the gap; don't treat "5.7×" as a precise measurement yet.

Notice this simulation *could* have failed: if physical and price accounting had agreed, there'd be no story and Aequitas would offer nothing new here. They didn't agree — and the disagreement points exactly where the theory predicted (cheap-but-costly byproducts are where price accounting lies most).

There's also a nice built-in honesty check in the code: we shocked all the prices by a random factor and confirmed the physical answer **didn't budge at all.** That matters, because it proves the physical split genuinely doesn't sneak a look at prices — it's measuring something else.

---

## The blunt scorecard

| Simulation | What it really is | Does it survive "could it have failed?" | Trust it as… |
|---|---|---|---|
| **1. Self-eating economy** | Numerical confirmation of a classical math theorem | **Yes** — and re-checked against the raw 5,224-row data | A solid result: the accounting never blows up and never goes negative, *if* the physical split is measurable |
| **2. EXIOBASE match** | External sanity-check vs. a standard academic tool | **Yes** — matched to 14 decimals | Proof our code does textbook economics correctly (but does nothing *new* on that data) |
| **3. Pretend cow** | Worked example with invented numbers | **No** — it can only confirm our own rules | Evidence the *software matches the spec*. **Not** evidence about the real world |
| **4. Real refinery** | Real DOE energy data + some modelling | **Yes** for the direction; the exact size is model-dependent | A real, grounded finding: price accounting hides the cost of cheap-but-energy-hungry byproducts |

The short version: **two solid, one external check, one honest illustration.** The thing you were worried about — a result generated purely as wish-fulfillment — describes Simulation 3 fairly, and we've labelled it as such. It does *not* describe 1, 2, or 4, each of which had a real chance to fail and either didn't (1, 2) or produced a finding driven by outside data (4).

---

## How to check any of this yourself

Everything is inspectable. From this folder:

- **The self-eating economy's full data** — 5,224 rows, one per test economy:
  ```bash
  # open results.csv in any spreadsheet; columns rho, min_p, converged, value_min_v
  ```
  The claim "no productive economy ever went negative" is the `min_p` column: filter `rho < 1` and check none is below zero.

- **Re-run everything from scratch** (each prints its own checks first, then results):
  ```bash
  python recursion_convergence.py --test
  python estimation_engine.py
  python exiobase_loader.py
  python refinery_slice.py
  ```

- **The cattle and refinery result tables** are saved as `estimation_debit_vectors.csv` and `refinery_allocation.csv` — open them in a spreadsheet and the arithmetic is checkable by hand (e.g. petcoke's energy share = coking energy 51.3 + distillation share 39.3 = 90.6, out of 2,162 total = 4.2%).

- **The real refinery energy numbers** (U.S. DOE, 2010) are transcribed in [`../00-strategy/GLOSSARY.md#src-refinery-process-energy`](../docs/GLOSSARY.md#src-refinery-process-energy), with links to the original reports.

---

## A short reading list (for grounding)

If you want to understand the ideas underneath, roughly in order of usefulness:

- [**Joint product**](https://en.wikipedia.org/wiki/Joint_product) — the core problem: one process, many outputs, how to split the cost.
- [**Cost allocation**](https://en.wikipedia.org/wiki/Cost_allocation) — the accountant's version of the same problem.
- [**Input–output model**](https://en.wikipedia.org/wiki/Input%E2%80%93output_model) and [**Wassily Leontief**](https://en.wikipedia.org/wiki/Wassily_Leontief) — how economists handle an economy that feeds itself. This is the mathematical backbone of Simulations 1 and 2.
- [**Production of Commodities by Means of Commodities**](https://en.wikipedia.org/wiki/Production_of_Commodities_by_Means_of_Commodities) ([Piero Sraffa](https://en.wikipedia.org/wiki/Piero_Sraffa)) and [**Ian Steedman**](https://en.wikipedia.org/wiki/Ian_Steedman) — where the "negative cost" embarrassment comes from, and why avoiding it matters.
- [**Neumann series**](https://en.wikipedia.org/wiki/Neumann_series), [**Perron–Frobenius theorem**](https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem), [**spectral radius**](https://en.wikipedia.org/wiki/Spectral_radius) — the actual theorems behind "it settles and stays positive." Heavier going, but this is *why* Simulation 1 isn't wishful thinking.
- [**Life-cycle assessment**](https://en.wikipedia.org/wiki/Life-cycle_assessment) — where the same allocation problem shows up in environmental science, and where "split by price" is openly acknowledged as a last resort.
- [**Oil refinery**](https://en.wikipedia.org/wiki/Oil_refinery) and [**petroleum coke**](https://en.wikipedia.org/wiki/Petroleum_coke) — for Simulation 4.
- [**Externality**](https://en.wikipedia.org/wiki/Externality) — the broader reason any of this matters: costs that fall on people who didn't cause them.

---

*If any single claim in the technical write-ups (`RESULTS.md`, `ESTIMATION.md`, `REFINERY.md`) doesn't match what you find in the CSVs, that's a bug worth surfacing — the data files are the authority, not the prose.*
