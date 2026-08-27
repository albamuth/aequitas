# Consumer Segmentation and Archetypes — how to build a cohort

**Version:** 0.1
**Type:** source survey + method ruling
**Compiled:** 2026-08-23
**Bears on:** the simulator's consumer cohorts ([`06-simulation/statera/STATERA_PLAN_v0.2.md`](../06-simulation/statera/STATERA_PLAN_v0.2.md) §4), the culture and locale dials, and any scenario that asks *"which mix of people makes Aequitas stable?"*

> **Headline, and it is a warning as much as a finding.** There are two completely different kinds of "consumer type" in the world, and they are easy to confuse.
>
> **One kind carries numbers.** Government household surveys say how many dollars, kilograms, or kilowatt-hours a group actually consumed. **This is what the simulator must run on.**
>
> **The other kind carries stories.** Marketing archetypes say what a group *feels like*. They are genuinely useful for naming a cohort and for giving the culture dial a vocabulary. **They carry no quantities at all, and there is no evidence they predict any.**
>
> **The rule that follows: an archetype may NAME a cohort. It may never SUPPLY a number.**

---

## 1. Why this matters more here than in marketing

Aequitas is a materialist accounting. Under **A1 (materialism of cost)**, a cost is a real flow of matter or energy — *"there is no abstract, issued, or fiat quantity anywhere in the system."*

A brand archetype is a construct about how someone feels about a product. **It is not matter and it is not energy.** If an archetype ever sets a consumption quantity in the model, a marketing abstraction has been smuggled into the one place the project promises not to have one. **That would be an A1 failure in spirit, inside our own instrument.**

So this note keeps the two apart on purpose.

---

## 2. Sources that carry real quantities

### The United States

| Source | What it gives | Link |
|---|---|---|
| **Consumer Expenditure Survey (CE)** — US Bureau of Labor Statistics | Household spend by category, split by **age, income quintile, region, household composition, race, education, and housing tenure.** The backbone of any US cohort. | [CE tables](https://www.bls.gov/cex/tables.htm) · [2023 news release](https://www.bls.gov/news.release/cesan.nr0.htm) |
| **Residential Energy Consumption Survey (RECS)** — US Energy Information Administration | Household energy in **physical units**, by home type, region, and income. Not dollars. | [RECS](https://www.eia.gov/consumption/residential/) |
| **American Time Use Survey (ATUS)** — BLS | Hours of paid *and unpaid* work, by demographic. **The self-care floor and the credit side both need this.** | [ATUS](https://www.bls.gov/tus/) |
| **National Household Travel Survey (NHTS)** | Household travel in physical units — miles, modes, vehicles. *Link unverified — check before citing.* | — |

### Europe

| Source | What it gives | Link |
|---|---|---|
| **Household Budget Survey (HBS)** — Eurostat | The EU equivalent of CE, harmonised across member states, by income, household type, and degree of urbanisation. **The European cohort mix comes from here.** *Link unverified.* | [Eurostat HBS](https://ec.europa.eu/eurostat/web/household-budget-surveys) |
| **EU-SILC** — Eurostat | Income and living conditions, finer on deprivation than HBS. *Link unverified.* | [EU-SILC](https://ec.europa.eu/eurostat/web/income-and-living-conditions) |

### Latin America, and the rest of the world

| Source | What it gives | Link |
|---|---|---|
| **Global Consumption Database** — World Bank | Consumption by category and income quintile for **92 developing countries**, including Brazil, Colombia, Peru, Mexico. **This is the South American mix.** *Link unverified.* | [World Bank](https://datatopics.worldbank.org/consumption/) |
| **ECLAC / CEPAL household surveys** | Regional harmonisation of Latin American national household surveys. *Link unverified.* | [CEPAL](https://www.cepal.org/en) |
| **Luxembourg Income Study (LIS)** | Harmonised household microdata across ~50 countries. The best cross-country like-for-like. | [LIS](https://www.lisdatacenter.org/) |
| **OECD household consumption** | Consumption by purpose (COICOP) across OECD members. *Link unverified.* | [OECD Data](https://data.oecd.org/) |

> **All of these report money.** Turning money into hours, kilograms, and megajoules is a separate step with its own note: [Labour and pollution intensity](../00-strategy/GLOSSARY.md#src-labour-and-pollution-intensity).

---

## 3. Commercial segmentation systems — what they are worth

These are the real segmentation industry. They matter because they are built on **observed purchases**, not on self-reported personality.

| System | What it is | Honest assessment |
|---|---|---|
| **Claritas PRIZM** | 68 US neighbourhood segments, built from purchase data and census geography. | The most quantitatively grounded of the three. **Commercial licence.** *Link unverified: [Claritas](https://claritas.com/)* |
| **Experian Mosaic** | Similar, and international. | Same shape, same licence problem. *Link unverified.* |
| **VALS** — Strategic Business Insights | 8 US psychographic types, from a survey instrument. | **Halfway between the two kinds.** It is survey-validated but measures motivation, not throughput. [VALS](https://www.strategicbusinessinsights.com/vals/) |

**Recommendation: do not licence any of them.** The public surveys in §2 give us what we need, and a commercial segmentation would make our cohorts unreproducible by anyone who reads the code — which breaks **§5.3b (published methods)** and **§9 requirement 16**, *"every estimating number and every method the implementer uses is published, so anyone can re-run it."*

---

## 4. The 12 marketing archetypes — what they are, and what they are not

**The framework.** Twelve brand personalities — *Innocent, Everyman, Hero, Outlaw, Explorer, Creator, Ruler, Magician, Lover, Caregiver, Jester, Sage* — popularised by Margaret Mark and Carol S. Pearson in *The Hero and the Outlaw* (2001), loosely adapted from [Jung's archetypes](https://en.wikipedia.org/wiki/Jungian_archetypes).

- **Practitioner guide (the source that raised this):** [Octopus & Son — marketing archetypes guide](https://octopusandson.com/marketing-archetypes-guide/)
- **The nearest academically validated relative:** Jennifer Aaker's **Brand Personality** scale (1997), five dimensions — sincerity, excitement, competence, sophistication, ruggedness. [Overview](https://en.wikipedia.org/wiki/Brand_personality). *Note: it measures how a brand is perceived, not how much anyone consumes.*

### The honest verdict

**⚠️ There is no evidence, in the peer-reviewed literature or in the practitioner material, that the twelve archetypes predict consumption *quantity*.** They were built to help a brand choose a voice. They describe *why* someone might prefer one washing machine over another. **They say nothing about how many washing machines get made, how heavy they are, or how much energy they take.**

**That is exactly the number Aequitas needs, and archetypes do not have it.**

### What they are genuinely good for — three things

1. **Naming a cohort so a human can read it.** *"Cohort 7"* is unreadable on a screen. *"The Caregiver cohort — older, lower income, high healthcare and food share, low transport"* is readable in one glance. **This is real value and it costs nothing.**
2. **Giving the culture dial a vocabulary.** *"This locale weights Everyman and Caregiver heavily; that one weights Ruler and Explorer"* is a legible way to describe two mixes that differ. **The description is narrative; the numbers underneath still come from §2.**
3. **Generating theoretical mixes.** The author wants to test invented populations, not only real ones. Twelve named types give a principled way to vary a mix without pretending anyone measured it.

### 🔒 The rule

> **An archetype may name a cohort, colour it on the screen, and describe it in words.**
> **An archetype may never set a quantity.**
> **Every kilogram, megajoule, and hour in a cohort's profile traces to a survey in §2 or to an intensity table, and the cohort file records which.**

**A cohort built from an archetype alone must be labelled `basis: invented`** and reported as a theoretical population, never as a real one — the same discipline **§5.1a** applies to every other estimate.

---

## 5. What a cohort file must carry

Whatever the source, each cohort needs the same fields, so a real and an invented cohort are told apart by their labels and not by their shape.

| Field | Example | Why |
|---|---|---|
| `name` | "US — Caregiver, 65+" | Readable on screen |
| `basis` | `measured` · `modelled` · `invented` | **§5.1a monotonicity.** An observation may never be replaced by an estimate |
| `source` | "BLS CE 2023 Table 1300" | **§5.3b published methods** |
| `vintage` | 2023 | **§3.3.** Figures move; the date says which reading this is |
| `share` | 0.084 | Its slice of the population mix |
| `wants[category][age_band]` | hours | The consumption profile |
| `work_hours[age_band]` | hours/day | The credit side |
| `coverage` | 0.89 | **§9 requirement 13** — what share of the real basket this profile covers |

---

## 6. What no source provides

1. **🔴 Participation rates fine enough for the 1% cut.** The plan allows dropping anything used by under 1% of people. **The CE news release gives mean spend per household and never says how many households bought one.** The detailed CE tables carry a *percent-reporting* column for some items; whether it reaches yacht-level detail is untested. **Until this is found, the 1% cut is an intention and not a working rule.**
2. **Cohort *stability* has never been studied.** The author's question — *"which mixes of consumer types are stable, and where is the threshold?"* — has no literature behind it, because no existing economy is accounted this way. **This is original work, and it is the point of the simulator rather than a gap in the sources.**
3. **Archetype-to-consumption mapping.** Does not exist, and §4 argues it should not be invented.

---

## 7. To do

- [ ] Download the CE demographic tables (1101, 1300-series, 1500-series, 1800-series) and archive them here **on the day they are fetched.** The BLS employment-requirements matrices were withdrawn on 2026-02-06 and had to be recovered through the [Wayback Machine](https://web.archive.org/); expect a repeat.
- [ ] Verify the unverified links above: Eurostat HBS, EU-SILC, World Bank Global Consumption Database, CEPAL, OECD, Claritas, NHTS.
- [ ] Find whether CE detailed tables carry percent-reporting at item level. **This unblocks the 1% cut.**
- [ ] Build the first three preset mixes — US, European, South American — and record which survey each field came from.
- [ ] Decide how many cohorts. Too few and the disparity figure becomes a step function; too many and the event log grows back. **Empirical, not guessable.**

## Related

- [Labour and pollution intensity](../00-strategy/GLOSSARY.md#src-labour-and-pollution-intensity) — the money-to-hours conversion these surveys need
- [Estimation-engine data sources](../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources) — the supply-chain tracing machinery
- [Cross-country labour efficiency](../00-strategy/GLOSSARY.md#src-cross-country-labour-efficiency) — the Q6 result the locale dial must reproduce
- [Veblen — conspicuous consumption](../00-strategy/GLOSSARY.md#src-veblen-conspicuous-consumption) — the one classical treatment of *why* consumption differs by group
- [statistical-coverage](../01-wiki/statistical-coverage.md) · [estimation-engine](../01-wiki/estimation-engine.md) · [[median-lifestyle]]
