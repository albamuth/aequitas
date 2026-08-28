# Kernel v0.2 — the time axis. Design on paper.

> **Version:** 0.2 (plan) · **Date:** 2026-08-23 · **Status:** Design only. No code written against this yet.
> **Author sign-off required before step 1.**
> **Parent:** [`../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md`](../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md) — this is **step 2**, and **Phase 1** of [`LAB_DESIGN_v0.1.md`](LAB_DESIGN_v0.1.md).
> **Built on:** [`statera.py`](statera.py) v0.1, [`STATERA.md`](README.md), `STATERA_CHANGELOG.md`.
> **Tracks:** `../../00-strategy/Aequitas_Foundations_v0.19.md` (superseded; held locally).

---

## 0. What v0.2 is, in one line

**Time passes. People are born, work, consume, age, and die. The books hold every period.**

v0.1 was one accrual and one purchase. v0.2 is a run.

### 🎯 What the whole simulation programme is for — author, 2026-08-23

> **We are looking for the thresholds, conditions, and variables that lead to Aequitas being adopted — how fast, how slow, or where it fails critically.**

**This re-aims everything.** The conformance checks, the disparity ceiling, the clearing rate: **those are instrument checks.** They prove the machine is measuring the thing it claims to measure. **They are not the object of study.**

**The object of study is adoption dynamics.** Which starting populations catch. Which stall. What the critical population is, which industries have to be inside first, how the money boundary behaves, and where the whole thing dies.

**Three consequences for this plan:**

1. **A scenario earns its place by bearing on adoption.** A run that shows the ceiling holding for the twelfth time teaches nothing new. **A run that finds a population Aequitas cannot carry teaches a great deal.**
2. **Failure is the product.** §4b's mix sweep must find failing mixes. §8's honest limits must be reported next to results. **A simulator that only produces good news is advocacy with a Python interpreter attached.**
3. **Timescales get long.** Adoption is generational — see [`../../00-strategy/papers/Onboarding_the_wealthy_v0.1.md`](../../00-strategy/papers/Onboarding_the_wealthy_v0.1.md), where the arithmetic runs to 70–170 years. **The period length must be a dial.**

> **Parked, deliberately: marketing, education, and advocacy.** Aequitas will eventually need a phase that persuades people. **This is not it, and nothing in this programme should be built as if it were.**

---

## 1. The five decisions, settled by the author 2026-08-23

| # | Question | Ruling |
|---|---|---|
| 1 | Do people age and die? | **Yes.** Born, aged one period at a time, dead on a mortality schedule. **Records stay after death**, as §4.8 (there is entry, and there is no exit) requires. |
| 2 | What does a person want each period? | **Consumer types from real demographic segments**, with dials for culture and locale. Not one average shopper. **Cohorts are fully customizable** — ship real preset mixes (US, European, South American) *and* let anyone invent theoretical ones, so a stranger can hunt for the unstable threshold. |
| 3 | Who moves the gate dial `rho`? | **All three modes must be available**, chosen per scenario: fixed, a written rule, or solved each period. |
| 4 | How is the log kept small enough? | **One exemplar consumer per cohort, plus a headcount.** If 30% of people are type A, the type-A exemplar is the basis for 30% of the population. |
| 5 | Where do costs per unit come from? | **Exemplar chains, modelled in full** — **not only goods.** Services and everyday consumption too: medical treatment, entertainment, housing, transport, food. Each supplies the cost per unit that everyone else pays. |
| 6 | How much of the shopping basket must be covered? | **Anything used by under 1% of people may be left out** — yachts, private jets. **Two conditions ride with it:** cut on physical size as well as headcount, and **publish the gap** so every figure reads as a floor (§4.4). |

**Nothing here contradicts an axiom.** Checked against A1–A8 and the 17 conformance requirements of §9. Where the design gives up accuracy, it is named in §8 below rather than hidden.

---

## 2. The structural change — cohorts carry a headcount

**One new column on the event log: `weight`.** It says how many real people this row stands for.

- An **actor** is now a **cohort**, and each cohort has **one exemplar person**.
- Everything stored in the log stays **per person** — the exemplar's hours, the exemplar's kilograms.
- **Aggregate figures multiply by `weight`. Per-person figures do not.**

**Worked numbers.** A cohort of **60,000** type-A adults. The exemplar works 6 hours, self-cares 10 hours, and eats 4.2 kg of food this month.

| Reading | Arithmetic | Result |
|---|---|---|
| The exemplar's credit | 10 + 6 | **16 h** — this is what IC-7 (the 24-hour cap) checks |
| The cohort's food draw | 4.2 × 60,000 | **252,000 kg** — this is what IC-1 (mass conservation) checks |
| The cohort's credit share of the economy | 16 × 60,000 | **960,000 h** |

**Why this is not a fudge.** The log is still append-only, still the only authority, and a standing is still derived by adding rows up (A6). **Nothing is stored as a balance.** The only change is that one row now speaks for many identical people.

> **🔒 `weight` defaults to 1.0, and at `weight = 1.0` the v0.2 kernel *is* the v0.1 kernel.** Full individual agents are the special case, not a separate mode. **One code path, two settings.** This is what keeps the existing 12 self-tests meaningful.

**Size, with digits.** 20 years at monthly steps, 8 consumer types, 3 locales:

| Design | Rows |
|---|---|
| v0.1 shape: 200,000 people × 240 months × 3 events | **144,000,000** — about 9 GB. Will not run. |
| v0.2 shape: ~1,900 cohorts × 240 months × 3 events | **1,368,000** — about 90 MB. Runs in a browser. |

---

## 3. Ages, births, and deaths

**A cohort is a birth group.** It is created in one period, ages together, and shrinks as its members die.

**A cohort's identity is `(consumer type, birth period, locale)`.**

- **Ageing.** The exemplar's age is `current period − birth period`. Nothing moves between cohorts.
- **Work hours come from age**, not from a random draw. A child works ~0 h. A working-age adult works the type's hours. A retired person works ~0 h. **This replaces v0.1's "35% do little paid work" guess with something derived.**
- **Wants come from age too**, read from the demographic table at `(type, age band)`.
- **Death is weight decay.** Each period the cohort's headcount falls by its mortality rate. **The rows stay in the log forever** (§4.8). When the weight reaches zero the cohort stops accruing and is never removed.
- **Birth is a new cohort** each period, sized by the birth rate, split across types by the type mix.

### What this makes testable for the first time

Foundations §5.5 says **age is the only spread beyond `24/F`**. v0.1 could not check that, because everyone was the same age. Now credit accrues from birth, so the claim has an arithmetic form:

> A 60-year maximum worker against a 20-year floor person should be **3 × 24/F**. At `F` = 10 h that is **7.2×**.

**If the run does not produce 7.2×, either the model or §5.5 is wrong. Both are results.**

---

## 4. Consumer types — and the data we do not have yet

**⚠️ This is the one part of v0.2 that is blocked on an outside download.**

`06-simulation/data/` currently holds only the **single US average** from the [BLS Consumer Expenditure Survey 2023 news release](https://www.bls.gov/news.release/cesan.nr0.htm) plus the employment-requirements matrices. **The demographic splits are not there.**

**What is needed**, from the [BLS Consumer Expenditure Survey tables](https://www.bls.gov/cex/tables.htm):

| Split | BLS table | Gives us |
|---|---|---|
| Age of reference person | 1300-series | The age curve of wants |
| Income quintile | 1101 | The spread of wants at the same age |
| Region | 1800-series | The locale dial, inside the US |
| Household composition | 1500-series | Children, couples, single adults |

*Exact table numbers to be confirmed at download time.* **Precedent warning:** the BLS employment-requirements matrices were withdrawn on 2026-02-06 and had to be recovered through the [Internet Archive Wayback Machine](https://web.archive.org/). Expect the same and plan for it.

**For locales outside the US:** the [Eurostat Household Budget Survey](https://ec.europa.eu/eurostat/web/household-budget-surveys) for Europe, and the [World Bank Global Consumption Database](https://datatopics.worldbank.org/consumption/) — 92 developing countries including Brazil, Colombia, Peru — for South America *(both URLs unverified)*. Full survey of what exists: [Consumer segmentation and archetypes](../../02-research/Data_consumer-segmentation-archetypes_v0.1.md).

**How a type reaches the kernel.** A type is a row of wants per age band, in **lifestyle units**, converted to debit-hours by the intensity table in [Labour and pollution intensity](../../02-research/Data_labour-and-pollution-intensity_v0.1.md). **The kernel never reads a spreadsheet.** A build script turns the tables into a small file, and the scenario names the file.

### 4a. Cohorts are data, and anyone may write them

**This is the point of the whole design.** A cohort mix is a file, not code. **Nothing in the kernel knows what a "consumer type" is** — it reads a list of profiles and headcounts and runs them.

**Three kinds of mix, told apart by one field and never by their shape:**

| `basis` | What it is | Example |
|---|---|---|
| `measured` | Built from a household survey, with the table and vintage recorded | "US 2023, BLS CE" |
| `modelled` | Derived from a survey through a stated method — a locale blend, a projected age structure | "EU average, HBS 2020, re-aged to 2040" |
| `invented` | **A theoretical population nobody measured** | "Half Caregiver, half Explorer, no retirees" |

> **🔒 An invented mix is reported as invented, every time it appears.** §4.4 monotonicity: **an observation may never be superseded by an estimate**, and a made-up population may never be quietly presented as a real one. **The screen carries the `basis` beside the result, not in a footnote.**

**Ship three presets:** United States, Europe, South America. **Each records which survey each field came from**, because §4.7 and conformance requirement 16 require the estimating numbers and methods to be published so anyone can re-run them.

### 4b. The mix sweep — the capability the author actually asked for

> *"Anyone could find 'this is the unstable threshold' or 'this is the range of stable cohort types'."*

**That is a sweep over mixes, not over dials, and it is a new capability.** v0.1 could sweep `rho` and `F`. This sweeps the **population itself**.

**How it works.** A mix is a vector of shares that sums to 1. The sweep walks that space, runs the same scenario at each point, and records whether the run held. **What comes back is a map, not a number.**

**Worked example with digits.** Two types, and one dial to walk: the share of the population that is high-consuming.

| Share high-consuming | Aggregate want | Capacity | Clearing `rho` | Held? |
|---|---|---|---|---|
| 10% | 1,610 h | 2,000 h | 1.9 | ✅ |
| 25% | 2,030 h | 2,000 h | 1.4 | ✅ |
| 40% | 2,450 h | 2,000 h | 1.1 | ✅ |
| 55% | 2,870 h | 2,000 h | **no clearing `rho` exists** | ❌ |

*Illustrative numbers, not a result — this is the shape of the output, and finding the real edge is the job.*

> **The interesting answer is the boundary, and it is a surface rather than a line** once you move three or more shares at once. **"Which populations can this system carry?" has never been asked of any economic design, because no other design lets you ask it.**

**Two rules keep this honest:**

1. **A mix that fails is a result, not a bug.** If a population cannot be carried, **say which one and why.** A simulator that only reports the mixes that worked is a brochure.
2. **The sweep reports the boundary with its assumptions attached** — the floor, the capacity, the intensity table, the coverage. **A threshold found at one `F` is not a threshold.** This is the same over-claim shape the project has now hit three times: *a bound proved inside a boundary, stated without the boundary.*

### 4c. What archetypes may and may not do

The author raised the [twelve marketing archetypes](https://octopusandson.com/marketing-archetypes-guide/). **They earn a place, and a narrow one.**

> **An archetype may NAME a cohort, colour it on screen, and describe it in words.**
> **An archetype may never SUPPLY a quantity.**

**Why the line is drawn there.** Archetypes were built to help a brand choose a voice. **There is no evidence they predict how much anyone consumes**, and consumption quantity is the only thing the kernel needs. Let one set a number and a marketing construct has entered a materialist accounting — which is **A1** violated inside our own instrument.

**What they are worth is real, though:** *"Cohort 7"* is unreadable; *"the Caregiver cohort — older, lower income, high healthcare and food, low transport"* lands in one glance. **That is a genuine gain for a screen a stranger has to understand without being told how.** Full assessment and the alternatives that *do* carry numbers: [Consumer segmentation and archetypes](../../02-research/Data_consumer-segmentation-archetypes_v0.1.md) §4.

---

## 5. The exemplar chains — where cost per unit comes from

**Goods are not enough.** Services and everyday consumption need exemplars too — a course of medical treatment, a night out. Each chain is modelled event by event. Its measured cost per unit becomes the price every cohort pays for that kind of thing.

**Why a chain and not just a coefficient.** A coefficient asserts a number. A chain **produces** one, and while producing it, it exercises rules a one-period toy could not touch.

### What a median US household actually spends on

From the [BLS Consumer Expenditure Survey 2023](https://www.bls.gov/news.release/cesan.nr0.htm), Table B, already on disk at `06-simulation/data/`. Average annual expenditure per consumer unit: **$77,280**.

**Two corrections applied first, both settled by the author on 2026-08-23** — see [`SUBSECTOR_CANDIDATES_v0.1.md`](SUBSECTOR_CANDIDATES_v0.1.md) §0.

| Category | Household spend | **Everything that flowed** | Chain? |
|---|---|---|---|
| Healthcare | 8.0% · $6,159 | **32.9% · ~$34,800** | ✅ **substituted** |
| Housing | 32.9% · $25,436 | **24.0%** | ✅ |
| Transportation | 17.0% · $13,174 | **12.4%** | ✅ |
| Food | 12.9% · $9,985 | **9.4%** | ✅ |
| Entertainment | 4.7% · $3,635 | **3.4%** | ✅ |
| *Personal insurance and pensions* | *12.4% · $9,556* | *9.0%* | ❌ **struck by A1 — not matter** |
| *Cash contributions* | *3.1% · $2,396* | *2.3%* | ❌ **struck by A1 — money leaves no trace** |
| Everything else | 9.0% | 6.5% | ⬜ not in v0.2 |
| **Total** | **$77,280** | **~$106,021** | |

> **🔴 The survey sees about one-sixth of the healthcare people actually consume.** The rest was paid by employers and government. **Under A1 money is invisible and under A7 everyone is accounted, so who wrote the cheque does not matter — the care happened and the debit lands on whoever received it.**
>
> **This is not a detail. It restructures the basket:** healthcare becomes the largest category and housing drops to second. **And it is the difference between a working locale dial and a broken one** — measure only household out-of-pocket spend and Europe looks artificially cheap, because more of its healthcare is publicly paid. **The locale comparison is the main thing we are trying to measure.**

> **A1 still strikes 11.3% before we model anything.** Pensions, Social Security, life insurance and cash given away are financial claims, not matter or energy, so they *"never appear on any ledger."* **Not a coverage gap — a category error the axiom removes.**
>
> **Five chains cover 82.1% of the total, and 92.6% of what a person materially consumes.**

### The five chains, and what each one proves

| Chain | Share | Mechanisms it tests that the kernel cannot express today |
|---|---|---|
| **Housing** | 32.9% | **§3.7** — a building carries a remediation debt for its bounded space. **§4.5** — creation-cost splits by holding time. *Worked case already in Foundations: a 500,000-hour house held 10 years leaves ≈250,000 hours on the seller.* **§3.2** — property debit discharges on transfer. |
| **Transportation** | 17.0% | **§3.2b** — fuel and its pollution stay permanently on whoever made the journey and **cannot be shed by reselling the car.** The **real-time-dispatch rule** — an electric car's emissions follow the **contracted supply mix**, not the grid average. *The [refinery slice](../allocation-engine/REFINERY.md) becomes the upstream half of this chain, so that work is not wasted.* |
| **Food** | 12.9% | **§3.4a joint production** — the canonical steer: beef, hide, tallow, bone, manure, methane, split by **where the feed energy physically went**. **§3.2b** — the farmer keeps the fertiliser runoff, not the shopper. |
| **Healthcare** | 8.0% | **§4.5 front-loading** — **the doctor's education is not in the bill.** **§4.5** — the hospital's cost sits on its staff by holding time, never on the patient. **§4.2** — a service verifies by **client attestation**, not by a hand-off. **§5.5** — essential, so never gated. |
| **Entertainment** | 4.7% | **§4.5 media** — the viewer pays **delivery only**: the projectionist's hours, the power, the bandwidth. **Not the film's production**, which pledgers front-loaded. **§4.6** — feedback is not credit and never converts to it. Closes the loop on **OP-21** (media reproduction). |

> **Every one of the five tests something the kernel currently cannot say anything about.** Three of them — healthcare, entertainment, and housing — test the **Front-Loading Rule**, which is the mechanism that dissolved OP-11, OP-5, OP-21 and OP-23 and has **never once been simulated.**

### 5a. Sectors break into subsectors — and the two tests for when

**A sector is too coarse the moment two things inside it have genuinely different debit vectors.** But splitting has no natural end, so it needs a rule.

> **Test 1 — does the split move the numbers ENOUGH to be worth carrying?** Not the name. **The debit vector.** *Author's rule, 2026-08-23: "if it makes no significant difference, it is not worth making a subsector for."* **A split can be true and still not earn its place.**
>
> **Test 2 — is the split measurable?** The physical-trace test. **Kilograms of nitrogen are measured.** A label on a package is not a measurement — but the inputs behind the label are.
>
> **Stopping rule: split until the next split is smaller than the model's own uncertainty.** That is checkable, so the splitting ends somewhere defensible instead of wherever anyone got bored.
>
> **And record the rejects.** A split that was considered and dropped for being too small is **written down with its magnitude**, not silently omitted. Otherwise the next person re-proposes it, and nobody can tell an untested idea from a tested one.

#### Food — the author's splits, and which dimension each one moves

| Split | What actually moves | Verdict |
|---|---|---|
| **Meat vs dairy vs vegetables vs grains vs seafood** | **All three dimensions, by one to two orders of magnitude per kilogram** | ✅ **Take.** [Poore & Nemecek 2018](https://ourworldindata.org/environmental-impacts-of-food) — 38,700 farms, 40 products |
| **Organic vs conventional** | `mass_kg` of synthetic nitrogen and pesticide → runoff pollution. **And `labour_h` goes UP.** And land goes up. | ✅ **Take** — see the crossover below |
| ~~**Local (< 100 mi) vs non-local**~~ | `energy_mj` for freight — but freight is typically **under ~10% of a food's footprint**, and food is 12.9% of the basket, so the split moves **roughly 1% of the total.** | ❌ **DROPPED 2026-08-23.** Below the model's own uncertainty. **True, and not worth carrying.** |
| **Air-freighted vs not** | Air freight runs on the order of **50× sea freight per tonne-kilometre**, and it is concentrated in a small set of goods — out-of-season berries, fresh fish, cut flowers. | ✅ **Take instead.** This is where the transport effect actually lives |

> **Why the replacement is the right move rather than a save.** The intuition behind "local food" is real, but **it is not distance that matters, it is mode.** Averaging distance across all food buries a 50× effect inside a 10% category. **Splitting on air freight puts the large difference where it can be seen and leaves the small one out.**

#### The organic case is the best demonstration in the whole plan

**Organic wheat probably costs MORE labour and LESS pollution than conventional.** So which is cheaper under Aequitas **depends entirely on the weighting model — which is OP-10.**

**Worked example. Illustrative numbers; the structure is the point.**

| Per tonne of wheat | Labour | Pollution, in hours to remediate |
|---|---|---|
| Conventional | 2.0 h | **P** |
| Organic | 3.2 h | 0.2 P |

They cost the same when `2.0 + P = 3.2 + 0.2P`, so `0.8P = 1.2`, so **`P` = 1.5 hours.**

> **Above 1.5 hours of remediation per tonne, organic is cheaper under Aequitas. Below it, conventional is.** Nobody votes on this. **The crossover is a number, and the sim can print it.**
>
> **This is exactly why §3.2a keeps the debit as a vector and collapses only on demand.** Collapse early and this question becomes invisible — you get one figure and no way to see what it depended on.

#### Housing — and the author has re-derived Foundations' own split

The proposed units are **labour per square foot to build** and **labour per square foot per year to maintain**. **Those are the two terms §3.2 and §4.5 already use, in measurable form:**

| The author's unit | What it already is |
|---|---|
| Labour per sq ft **to build** | The asset's **creation-cost** — holding-time-split, each holder's share **permanent** (§4.5) |
| Labour per sq ft **per year to maintain** | The **self-work identity** (§3.2) — while you hold it, repair earns credit equal to the debit it adds. **Net zero on labour, net cost on materials** |

> ### ✅ And this cross-checks Foundations' own worked example — once its context is restored
> **§3.2 says "a 500,000-hour house."** Read cold that looks absurd — 250 person-years for a house. **It is not. The author's original case was a very rich person's mansion, and the context was lost in the writing.**
>
> **Check it against our intensity figure.** At $56.00 of spend per embodied hour (§1 of [Labour and pollution intensity](../../02-research/Data_labour-and-pollution-intensity_v0.1.md)):
>
> | | Hours | Implied build cost |
> |---|---|---|
> | Foundations' example | 500,000 h | **$28,000,000** — mansion scale ✅ |
> | A median US home | ~7,100 h | $400,000 |
>
> **The two methods agree, and that is a small piece of independent validation of the $56/hour figure.** A 70× spread between a median home and a mega-mansion is the right order of magnitude.
>
> **📌 Action, not a correction: Foundations §3.2 needs the word "mansion" put back.** Queued for the next fold — the number stands, only its context is missing.

#### Settled: 27 categories and 5 modifiers

**Full list and reasoning: [`SUBSECTOR_CANDIDATES_v0.1.md`](SUBSECTOR_CANDIDATES_v0.1.md) §0.**

| Chain | Categories |
|---|---|
| Healthcare | **8** — preventive · acute · chronic · end-of-life, each split by drugs / procedures / practitioner time |
| Housing | **6** — {new build, existing stock} × {cold, temperate, hot} |
| Transport | **5** — car-combustion · car-electric · transit · air · walk-cycle |
| Food | **5** — beef · other meat · dairy · plant staples · seafood |
| Entertainment | **3** — pets and hobbies · fees and admissions · devices and supplies |

> ### 🔑 The move that made this fit: a split that MULTIPLIES is a modifier, not a category
> **Floor area does not create a new kind of housing. It makes the same housing bigger.** Carried as a multiplier it costs **one number per cohort** instead of tripling the matrix.
>
> **Five splits are carried this way:** floor area per person, organic share, food-away share, air-freight share, powertrain blend. **Every split the author asked for is present. None of them cost a row.**

**The real size of the model: 27 × 8 consumer types × 8 age bands = 1,728 numbers to source.** Within budget, and all from public tables.

### 🔒 The 1% coverage cut, and the rule that must ride with it

**Author's ruling: a good or service used by fewer than 1% of people may be left out.** Yachts, private jets, bespoke tailoring.

**Two conditions, and neither is optional.**

**1. Cut on headcount *and* on physical size.** A private jet is used by roughly 0.01% of people and is a large share of aviation energy. **Cutting on headcount alone would drop something physically enormous, and A1 says cost is material, not popular.**

> **Drop a category only if it is under 1% of the population AND under 1% of every physical dimension** — hours, kilograms, and megajoules, each checked on its own. If it is 0.1% of people but 4% of energy, **keep it.**

**2. Publish the gap and report a floor.** Foundations **§4.4** and **conformance requirement 13**: *a quantity computed over incomplete coverage is published as a floor, with the gap named.*

> **So every cost figure this simulator produces is a lower bound, not a value**, and the screen must say so. This is not a caveat we are adding out of modesty. **It is a conformance requirement, and a simulator that breaks it is not simulating Aequitas.**

> ### ⚠️ And the cut must be switched OFF for any result about the top tail
> [`q4_locked_ledgers.py`](../scenario-suite/q4_locked_ledgers.py) found that **0.1–2% of Americans sit past a permanent lockout** — the ultra-consumers. **Those are precisely the people whose consumption is niche.**
>
> **Drop the niche basket and you may drop the very thing that locks them**, which would flatter the system in exactly the place the project is most often accused of flattering itself. **The cut is safe for median results and dishonest for tail results.** A scenario measuring the tail must carry the full basket.

---

## 6. The rho policy — three modes, and one hard rule

`rho` is the gate dial: how much a person may hold and consume per hour worked. `D ≤ rho × C`.

```json
"rho": { "mode": "fixed", "value": 1.20 }
"rho": { "mode": "rule",  "rule": "clear_capacity", "step": 0.05, "bounds": [0.2, 4.0] }
"rho": { "mode": "solve", "target": "capacity",     "bounds": [0.2, 4.0] }
```

| Mode | What it does | What it is for |
|---|---|---|
| **fixed** | Never moves unless a shock moves it. | The purest reading of A8 — Aequitas uses `rho` and never sets it. |
| **rule** | A named function from a small published list, applied each period. `clear_capacity` nudges `rho` down when demand exceeds what we can make, up when it does not. **A slow adjuster, not an optimiser.** | Watching `rho` behave like a central bank rate (§5.5). **The rule is readable in the scenario file.** |
| **solve** | Searches for the `rho` at which demand equals capacity, every period. | Finding the clearing rate, as [`rho_sweep.py`](../disparity-ceiling/rho_sweep.py) does today, but over time. |

> ### 🔒 The no-look-ahead rule
> **`rho` is set for a period BEFORE any transaction in that period, and never changed after seeing what people did.**
>
> The network announces the rate, then trade happens. Setting `rho` after the fact would let the model quietly clear a market that did not clear, and would break §3.3 (the transaction-time rule), which requires the gate to be evaluated **at the moment of the transaction** with the value that then held.
>
> **Every consumption event already records the `rho` and the room that applied to it.** That is the witness that makes this checkable rather than merely promised.

---

## 7. What becomes checkable that was not

`Aequitas_Conformance_v0.8.md` lists **17 conformance requirements**. v0.1 could express 10 of them. v0.2 adds three.

| # | Requirement | v0.1 | v0.2 |
|---|---|---|---|
| **11** | The gate is evaluated at transaction time; a later revision changes future room only | Checked, but nothing ever revised | ✅ **A real test.** A mid-run re-weight shock fires at period *n* and every earlier event must stay valid |
| **6** | Records are never destroyed or edited; a disputed record is annotated | Only proved by the absence of a `delete()` method | ✅ A `CONTEST` event kind: a challenge appends beside the original, and the original stays readable |
| **2** | Flows attribute to whoever **caused** them | Not expressible | ⚠️ **Partly.** The example chain gives multi-party processes, so pollution can be shown staying on the causer under §3.2b |

**Still not expressible, and honestly so:** requirements 12, 13, 14, 15 and 16 — basis and vintage, the floor rule, residual estimation over the unmeasured, the leftover charged to nobody, and published methods. **All five need dark producers, which means the outside-world plug.** That is v2 of the Lab, not this version.

### The nearly-free win: a pollutant discovered late

Weights are applied only inside `collapse()`. So a shock of the form

```json
{ "at": 60, "target": "dials.weights.mass_kg", "multiply": 1.25 }
```

**re-weights all of history at once, at no cost**, because the ledger was never stored. This is the author's *"a discovered pollutant that was previously unaccounted for"* scenario, and it arrives almost for free from the v0.1 design.

> **⚠️ The shock must start from a NON-ZERO weight, or it does nothing** *(outside-critique finding #12, 2026-08-24)*. `mass_kg` defaults to `0.0` (breathing sits at its natural-remediation baseline, Sec.3.3), and `1.25 × 0.0 = 0.0` — a `multiply` shock on a zero weight is arithmetically inert, and a scenario built that way would prove nothing while looking like it tested re-weighting. So this scenario must **set `dials.weights.mass_kg` to a small non-zero mitigation cost from period 0** (the pollutant was always there, just uncosted), and the shock then *raises* it — which is what `test_a_reweight_moves_a_number` in `statera.py` asserts actually shrinks the gate. A `multiply` on a baseline-zero flow is the wrong model for "discovered pollutant"; an `add`/`set` to a non-zero cost, or a `multiply` on an already-priced flow, is the right one. (Note also: `labour_h` is pinned to `1.0` and cannot be a shock target — the gate guard refuses any other value.)

---

## 8. Honest limits of the cohort model

**Name these now, so no result is later stated without them.**

1. **Everyone inside a cohort is identical.** The model **cannot show inequality within a type**. All spread it reports is spread *between* types and ages.
2. **The disparity figure gets coarser.** `24/F` is measured between the top exemplar and the bottom exemplar. With few cohorts, the observed spread is a step function. **The v0.1 finding that a low floor goes unfilled came from a smooth 200,000-person distribution and may not survive coarse cohorts.** If it does not, that is a limit of the cohorts, not a change in the result — and it must be said that way.
3. **Headcounts become fractional** as mortality decays a cohort. Acceptable in a model. Stated, not hidden.
4. **A cohort exemplar cannot cheat on its own.** Fraud and collusion scenarios need `weight = 1.0` individual agents. The code supports it; the long runs will not use it.
5. **Each exemplar chain's cost per unit is one chain's answer.** It is a measurement of a modelled process, not of the world.
6. **Every cost figure is a floor, never a value.** The five chains cover ~89% of material consumption. The missing ~11%, plus everything dropped by the 1% cut, means the true cost is **at least** what the simulator says and never less. **This must appear on screen, not only in a footnote** — conformance requirement 13.
7. **The 1% cut lies about the top tail.** Switch it off for any tail result. See §5.

---

## 9. Build order

**Reproduce before extending.** The roadmap's guard rule stands: the kernel must re-derive the published results through the *new* machinery before a single new scenario runs.

| Step | What | Done when |
|---|---|---|
| **1** | The `weight` column. Cohort projections. Conservation scales by weight. | **All 12 existing self-tests pass unchanged at `weight = 1.0`**, and the disparity bound is still 2.4000× at `F` = 10 h. |
| **2** | The period loop. | **A ten-period run holds every §9 check, and the bound stays at `24/F` for whatever floor the scenario set.** |
| **3** | Ages, births, deaths. | Credit accruing from birth reproduces the age term: a 60-year worker against a 20-year floor person is **7.2×** at `F` = 10 h. |
| **4** | **The five exemplar chains** — housing, transport, food, healthcare, entertainment. Build them in that order, largest share first. | IC-1 to IC-4 close on every chain; **the doctor's education is provably absent from the medical bill** and **the film's production is provably absent from the ticket**; and the five together price a basket within range of the [measured 1,380 h/yr median](../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md). |
| **4b** | The coverage declaration. | The simulator states, on screen, what share of the basket it covers and what it dropped — and **labels every cost figure a floor.** A run that cannot state its own coverage fails conformance requirement 13 and must refuse to report. |
| **5** | Consumer types from the BLS tables. | The population's mean want reproduces **1,380 h/yr**. Moving the locale dial reproduces the Q6 spread — Germany and Japan at roughly two-thirds the US labour. |
| **6** | The `rho` policy plug, all three modes. | `fixed` reproduces `rho*` = 1.20. `rule` and `solve` both settle on it from either side. |
| **7** | Mid-run re-weight shock. | A +25% pollution re-weight at period 60 tightens future room and **invalidates no past event.** |
| **8** | **The mix sweep** (§4b). Walk the space of population mixes, run the scenario at each point, return a map. | The three presets all hold, **and at least one invented mix provably fails**, with the reason named. **A sweep that finds no failing mix has not been run hard enough.** |

> **Step 5 is the one that can stall**, because it waits on a download that may need the Wayback Machine. **Steps 1–4 and 6–7 do not depend on it** and should be built first. If the tables cannot be got, step 5 falls back to the single US average already in hand, and the culture dial waits.

---

## 10. Risks

| Risk | What we do |
|---|---|
| **The cohort refactor changes the published numbers** | Step 1 is nothing but the refactor, and it must reproduce 2.4000× before anything else is written. A change there is a bug, not a finding. |
| **BLS tables are withdrawn again** | Expect it. Archive every file to `02-research/` on download, with a citation stub, on the day it is fetched. |
| **The cohorts are too coarse to see the low-floor result** | Named in §8. Test it directly: run the same scenario at `weight = 1.0` with 200,000 agents over ten periods and compare. |
| **`rho` mode `solve` becomes the default by habit** | The scenario file must state the mode explicitly. **No default.** An absent `rho.mode` is an error. |
| **The time axis pulls the project back into data architecture** | §2.6 again. This is an instrument for testing the theory. The moment a scenario needs a schema decision rather than an economics decision, stop and re-read the scope ruling. |

---

## 11. Open, and not settled here

1. **How many consumer types.** Too few and the disparity figure is a step function; too many and the log grows back. **A number to find empirically at step 5, not to guess now.**
2. **What a period is.** Monthly is assumed throughout (240 periods = 20 years), matching [`LAB_DESIGN_v0.1.md`](LAB_DESIGN_v0.1.md) §3. **Not yet tested against IC-7**, which is a per-24-hours rule and needs the period to carry its day count. **⚠️ And 20 years is not enough for one scenario we now have:** [`../../00-strategy/papers/Onboarding_the_wealthy_v0.1.md`](../../00-strategy/papers/Onboarding_the_wealthy_v0.1.md) works on a **70-to-170-year** timescale, because that is how long one year of billionaire-scale consumption takes to clear. **Generational runs need annual periods, or 2,000 monthly ones.** The period length must therefore be a scenario dial, not a constant.
2b. **The adoption scenario is now specified and not yet scheduled.** The onboarding note §8 lists six things a run needs — a non-participant pool whose estimated share rises as others join, a published residual charged to nobody, a per-cohort join decision, a verification-cost dial to cross the ~40% stall threshold, a real wealth tail, and generational time. **Most of it is the outside-world plug, which LAB_DESIGN put in v2.** Decide whether that ruling still holds now that the scenario exists.
3. **Whether pledges do anything over time.** IC-8 is checked, but nothing in v0.2 pledges. Pledges as a demand lever (§4.6) are a behaviour-layer question, which is roadmap step 3.
4. **⚠️ We cannot yet apply the 1% cut, because we have no participation rates.** The Consumer Expenditure news release reports **mean spend per household**, never *"what share of households bought one at all."* The detailed CE tables carry a **percent-reporting** column for some items; whether it reaches yacht-level detail is unknown until we look. **Until that number exists, the 1% cut is a stated intention and not a working rule**, and the first version simply keeps everything in the five chains.
5. **Whether entertainment needs a second chain.** A cinema ticket is delivery-only under §4.5. **A pet is not** — and "pets, toys, hobbies" is $1,057 of the $3,635 entertainment line, the largest piece of it. A pet is ongoing material consumption, closer to food than to media. **Possibly two chains, not one.**

---

## 12. Sign-off

| | |
|---|---|
| **Plan written** | 2026-08-23 |
| **Five design decisions** | ✅ Settled by the author, 2026-08-23 |
| **Data for step 5** | ⚠️ Not in hand. Download required. |
| **Step 1** | **Blocked on the author's word to begin.** |
