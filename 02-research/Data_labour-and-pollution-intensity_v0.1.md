# Labour and Pollution Intensity — turning dollars into hours

**Version:** 0.1
**Type:** method note + source survey
**Compiled:** 2026-08-23
**Bears on:** every cohort profile in the simulator, the median-lifestyle anchor, the locale dial, and any claim about what a way of living costs.

> **The question this answers.** Household surveys report **dollars**. Aequitas accounts in **hours, kilograms, and megajoules**. Something has to bridge them.
>
> **The bridge is an intensity table: how much labour, and how much pollution, sits behind one dollar of spending in a given sector.** Multiply spend by intensity and the dollars cancel out. Hours come out the other side.
>
> **This method is not a proposal. It is already built and already run** — it produced the 1,380 h/yr median-lifestyle figure the whole project leans on.

---

## 1. The arithmetic, with real numbers

**Spend × intensity = hours. The dollar sign cancels.**

```
   $9,985 of food   ×   0.0179 hours per dollar   =   178 hours
   ────────────────     ─────────────────────         ───────────
   BLS CE 2023          intensity table               what it cost
```

**Where the 0.0179 comes from, and why it is only a starting point.** The project's own measured result is that a median US lifestyle commands **1,380 hours a year** ([`MEDIAN_LIFESTYLE_RESULT.md`](../06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md)) against total spend of **$77,280** ([BLS CE 2023](https://www.bls.gov/news.release/cesan.nr0.htm)).

| | |
|---|---|
| Economy-wide average intensity | 1,380 ÷ 77,280 = **0.01786 hours per dollar** |
| The same figure read the other way | **$56.00 of spending per embodied hour** |

> **⚠️ But one average across the whole economy is exactly the mistake to avoid.** Food is more labour-intensive than the average; a pension contribution has no labour behind it at all and is struck by **A1** before it starts. **A single ratio would flatten every difference the cohorts exist to show.** The intensity must be **per sector**, which is what the tables below supply.

---

## 2. The tables, and where they are

### Labour — the US

**BLS Employment Requirements Matrix (ERM).** For each industry, the jobs and hours needed — **directly and through the whole supply chain** — to deliver one million dollars of final demand. This is precisely "hours per dollar, by sector."

- **Already on disk:** `06-simulation/data/erm_full/NOMINAL_DOMEMPREQ_2023.csv`
- **Program page:** [BLS Employment Projections — input-output data](https://www.bls.gov/emp/data/input-output-matrix.htm) *(link unverified — see the warning below)*

> **🔴 Fragility warning, from experience.** **BLS withdrew these matrices on 2026-02-06** and the project recovered them through the [Internet Archive Wayback Machine](https://web.archive.org/). **Treat every BLS download as perishable. Archive on the day you fetch it.**

### Labour — everywhere else

**EXIOBASE 3** is the only mainstream multi-region model that carries **hours worked** at supply-chain scale, split by skill and by gender, for 44 countries plus 5 rest-of-world regions.

- Stadler et al., [*EXIOBASE 3*](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715), *Journal of Industrial Ecology*, 2018
- **This is a critical dependency.** Ordinary footprint studies throw labour away as a cost to be minimised. **Aequitas counts it, and almost nobody else records it.**
- It is what the [cross-country efficiency result](../00-strategy/GLOSSARY.md#src-cross-country-labour-efficiency) was computed from, and therefore what the **locale dial** must reproduce.

### Pollution and materials

| Source | What it gives | Link |
|---|---|---|
| **USEEIO** — US EPA | 389 US sectors tagged with land, water, energy, minerals, air pollution, nutrient runoff, and toxic releases, per dollar. | [USEEIO](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models) |
| **EXIOBASE 3** | The same, multi-region, plus the labour layer. | [paper](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715) |
| **FIGARO-E3** | Newer, higher resolution, aligned to official statistics. Worth evaluating. | [Nature, 2025](https://www.nature.com/articles/s41597-025-04431-z) |
| **UN Global Material Flows** | National raw-material totals — the top-down sanity check. | [Resource Panel](https://www.resourcepanel.org/global-material-flows-database) |

---

## 2a. Below the sector — where subsector figures come from

**A sector average hides the differences that matter.** "Food" contains beef and lentils; "housing" contains a new build and a fifty-year-old roof repair. These are the sources that go finer.

### Food

| Source | What it gives | Link |
|---|---|---|
| **Poore & Nemecek (2018), *Science*** | **The standard dataset.** 38,700 farms, 40 products, 119 countries. Land, water, greenhouse gas, eutrophication per kilogram and per gram of protein. **This is where meat / vegetables / grains / seafood separate.** | [Our World in Data presentation](https://ourworldindata.org/environmental-impacts-of-food) · [paper](https://www.science.org/doi/10.1126/science.aaq0216) *(paywalled; the OWID version carries the data)* |
| **USDA Economic Research Service — organic production** | Acreage, yields, and input use for certified organic versus conventional. **The organic split lives here.** *Link unverified.* | [USDA ERS](https://www.ers.usda.gov/) |
| **USDA National Organic Program** | What "organic" legally excludes — which is what makes the label traceable to physical inputs rather than to marketing. *Link unverified.* | [AMS](https://www.ams.usda.gov/about-ams/programs-offices/national-organic-program) |
| **Argonne GREET** | Fuel and freight footprints — the transport half of the local/non-local split. *Link unverified.* | — |

> **⚠️ The finding that must not be suppressed.** Poore & Nemecek's headline result is that **transport is a small share of most foods' emissions**, and that *what* you eat dominates *how far it travelled*. **The local-versus-distant split is still worth modelling** — it moves the energy dimension measurably — **but the model must be free to report that it barely moves the collapsed figure.** Building it expecting local food to win would be building a mirror.

### Housing and productive space

| Source | What it gives | Link |
|---|---|---|
| **US Census Survey of Construction** | Floor area, cost, and characteristics of new US residential building. The denominator for "per square foot." *Link unverified.* | [Census SOC](https://www.census.gov/construction/chars/) |
| **NAHB construction cost surveys** | Cost breakdown by trade for a single-family home — the nearest public thing to labour hours per square foot. *Link unverified.* | — |
| **RSMeans** | The construction industry's standard labour-hour and cost database, by assembly. **Commercial licence** — the same reproducibility objection as PRIZM applies. | — |
| **EIA RECS / CBECS** | Residential and commercial energy use **per square foot**, by building type, vintage, and region. Physical units. | [RECS](https://www.eia.gov/consumption/residential/) · [CBECS](https://www.eia.gov/consumption/commercial/) |

> **✅ A cross-check that passed.** Foundations §3.2's worked example says **"a 500,000-hour house."** Read without context that looks impossible — 250 person-years. **The author's original case was a rich person's mansion**, and the word was lost in the writing.
>
> **At $56.00 per embodied hour, 500,000 hours implies a $28,000,000 build.** That is mansion scale. **A median US home at $400,000 comes to ~7,100 hours.** The 70× spread between the two is the right order of magnitude, so **the intensity figure and the Foundations example corroborate each other** rather than contradicting.
>
> **Action: Foundations §3.2 needs "mansion" restored to the sentence.** Queued for the next fold. The number is sound.

### Healthcare, entertainment, transport

| Source | What it gives | Link |
|---|---|---|
| **CMS National Health Expenditure Accounts** | 🔴 **Promoted to a critical dependency, 2026-08-23.** US health spend by type of service **and source of funds** — which is what lets us count care paid by employers and government, not only out-of-pocket. **The household survey sees about one-sixth of the healthcare actually consumed**, and under A1 the payer is invisible, so the care still counts. *Link unverified.* | [CMS NHE](https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data) |
| **OECD Health Statistics** | The same for other countries, harmonised. **Required for the locale dial**, or Europe looks artificially cheap because more of its care is publicly funded. *Link unverified.* | [OECD Health](https://www.oecd.org/health/health-data.htm) |
| **BLS Occupational Employment and Wage Statistics** | Employment by occupation and industry — the direct-labour side of a service, where the ERM gives only the supply chain. | [OEWS](https://www.bls.gov/oes/) |
| **US National Household Travel Survey** | Household travel in miles and modes. *Link unverified.* | — |

---

## 3. The bridge problem, and it is not small

**Household surveys and industry tables do not speak the same language.**

- The **Consumer Expenditure Survey** reports what a household bought: *"food at home," "rented dwellings," "gasoline."*
- The **ERM and the input-output tables** report industries: NAICS sectors like *"oilseed farming," "petroleum refineries."*

**A concordance has to map one onto the other**, and every mapping choice is a judgement someone can dispute. The project already built one — the "IO bridge" in [`median_lifestyle_METHOD.md`](../06-simulation/median-lifestyle/median_lifestyle_METHOD.md) — and **it must be published with the numbers, not buried in code.** That is **§5.3b** and **§9 requirement 16**: *every estimating number and every method is published, so anyone can re-run it.*

---

## 4. Three honest caveats, all pointing the same way

### 1. The tables split by price, and Aequitas says price is the thing to replace

Input-output models record what industries pay each other **in dollars**, and use those dollars to divide physical impacts. **We would be using price to compute the very thing we say should replace price.** An economist spots this immediately.

**It is acceptable as a measurement shortcut, on strict conditions** already set out in [Estimation-engine data sources](../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources) §7: every such figure is tagged **estimated, from a named model, at coarse resolution**, never dressed as a measurement, and replaceable by physical data later (**§5.1a**).

**And the bias runs in a known direction:** the money split **under-counts cheap, heavy, low-value flows** — waste, bulk materials, land — and over-counts expensive light ones.

### 2. Dollars are not comparable between countries

Comparing a US household to a Brazilian one at market exchange rates says something different from comparing at purchasing-power parity, and the gap is large. **Neither is wrong; they answer different questions.** The convention chosen must be stated on the face of any cross-country result. EXIOBASE works in basic prices in euros, which is a third convention again.

### 3. Years must match, and deflating compounds caveat 1

CE 2023 against ERM 2023 is clean. Mixing years needs a price deflator — **and using a price index to repair a price-based estimate stacks one money assumption on another.** Prefer matching vintages over deflating.

> ### The convergence worth noticing
> **Caveat 1 makes our figures too low.** The coverage gap — the ~11% of the basket with no chain, plus anything dropped by the 1% cut — **also makes our figures too low.**
>
> **Both errors point the same way, so every number this method produces is a floor and never a ceiling.** That is exactly what **§5.1a's floor rule** and **§9 requirement 13** already demand we say. **The two independent reasons agreeing is a small piece of luck: there is one honest statement to make, not two competing ones.**

---

## 5. The physical alternative, and why we are not using it yet

**Physical input-output tables** record what industries send each other in **tonnes rather than dollars**, which is what Aequitas actually wants.

- Weisz & Duchin, [*Physical and monetary input–output analysis*](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X), *Ecological Economics*, 2006
- [*A modular bottom-up approach for constructing physical input–output tables*](https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0123-1), 2018 — free to read

**Researchers argued a generation ago that physical tables are the right tool**, precisely because environmental pressure follows physical flow and not money. **That is the Aequitas position, stated in the mainstream literature decades before this project existed.**

**But they cover far less ground.** Use money-based tables now, labelled honestly, and migrate as physical coverage improves — which is what **§3.3 retroactive re-weighting** exists to absorb. **No figure computed this way is a permanent verdict on anyone.**

---

## 6. To do

- [ ] Archive the ERM CSV and its documentation into this folder with a dated citation stub. **It is currently only in `06-simulation/data/` and BLS has pulled it once already.**
- [ ] Verify the BLS input-output program-page link.
- [ ] Publish the CE-to-NAICS bridge as a readable table beside the numbers, not only as code.
- [ ] Compute per-sector intensities for the five exemplar chains — housing, transport, food, healthcare, entertainment — and check the five against the 1,380 h/yr total.
- [ ] Decide and record the cross-country convention: **market exchange rate or purchasing-power parity.** State it on the face of every locale result.
- [ ] Confirm EXIOBASE licence terms for redistribution of derived figures.

## Related

- [Consumer segmentation and archetypes](../00-strategy/GLOSSARY.md#src-consumer-segmentation-archetypes) — the surveys this note converts
- [Estimation-engine data sources](../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources) — the wider machinery and the price-split ruling
- [Cross-country labour efficiency](../00-strategy/GLOSSARY.md#src-cross-country-labour-efficiency) — what the locale dial must reproduce
- [Joint-production problem](../00-strategy/GLOSSARY.md#src-joint-production-allocation-problem) — why a sector figure still has to be split at the process
- [estimation-engine](../01-wiki/estimation-engine.md) · [[median-lifestyle]] · [retroactive-reweighting](../01-wiki/retroactive-reweighting.md) · [price-equals-cost](../01-wiki/cost-not-price.md)
