# Data Sources for the Estimation Engine (C3)

**Type:** source survey
**Compiled:** 2026-07-31
**Bears on:** C3 (estimation engine), C2 (material-superiority demonstration), C4 (re-weighting), §11 MVP

> **Headline finding: we should not build the estimation engine from scratch.** The architecture already exists as a mature scientific discipline — environmentally-extended input-output (EEIO) analysis — with open models, open code, and government-maintained data. What Aequitas adds is a labor dimension nobody else needs and a physical-allocation correction. See §7 for the axiom problem this creates.

---

## 1. What C3 actually has to compute

The pipeline implied by the question *"what does a median American household truly cost?"*:

```
household consumption basket
   → propagate through the entire supply chain
      → labor hours + energy + materials + emissions at every tier
         → weight by current mitigation cost
            → "true cost"
```

Step 2 is the hard one, and it is a solved problem in a discipline we have not been using: **Leontief input-output analysis**. The Leontief inverse propagates a final-demand vector through *all* upstream tiers automatically — direct, indirect, and indirect-of-indirect, to convergence. That is precisely the supply-chain traversal Aequitas needs, and it has been standard practice since the 1970s.

---

## 2. The core tool — EEIO

### USEEIO (US EPA) — start here

- **Program page:** [US Environmentally-Extended Input-Output (USEEIO) Models, EPA](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models)
- **Model paper:** Ingwersen et al., [*USEEIO v2.0, The US Environmentally-Extended Input-Output Model v2.0*](https://www.nature.com/articles/s41597-022-01293-7), *Scientific Data*, 2022 — open access
- **Code:** [`useeior`: An Open-Source R Package for Building and Using US EEIO Models](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175389/) — open source, and the models are rebuildable from configuration

**What it gives us:** 389 US industry sectors, with satellite accounts covering **land, water, energy and mineral use, air pollution, nutrients, and toxics**. v2.0 adds waste-sector disaggregation, explicit **final demand vectors for US consumption**, a domestic-only variant separating domestic from foreign impact, and price-adjustment matrices across dollar years.

The final-demand consumption vectors are the direct input for a household basket. This is close to purpose-built for C2.

### EXIOBASE — the international and *labor* layer

- **Paper:** Stadler et al., [*EXIOBASE 3: Developing a Time Series of Detailed Environmentally Extended Multi-Regional Input-Output Tables*](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715), *Journal of Industrial Ecology*, 2018

**Why it matters more to us than to anyone else:** EXIOBASE carries **employment satellite accounts — hours worked, disaggregated by skill level and gender**, sourced from EUROSTAT, [ILOSTAT](https://ilostat.ilo.org/), and OECD statistics. It also tracks *vulnerable employment* (unpaid family workers and the self-employed).

**Labor hours embodied in a supply chain is exactly what Aequitas needs and standard LCA does not provide**, because conventional LCA prices labor out as a cost rather than counting it as material activity. EXIOBASE is the only mainstream dataset carrying it at supply-chain scale. Treat this as a critical dependency.

Coverage: 44 countries plus 5 rest-of-world regions, time series from 1995.

### FIGARO-E3 — the newer alternative

- Nature, 2025: [*FIGARO-E3: a high-resolution extended multi-regional input-output database consistent with official statistics*](https://www.nature.com/articles/s41597-025-04431-z)

Worth evaluating against EXIOBASE; being consistent with official statistics may make it more defensible for a public-facing claim.

---

## 3. Layer 1 — what a household actually consumes

| Source | Gives us | Link |
|---|---|---|
| **BLS Consumer Expenditure Survey** | The demand vector: what a median household buys, by category, by income decile | [BLS CE overview](https://www.bls.gov/opub/ted/consumer-expenditure-survey.htm) · program site `bls.gov/cex` |
| **EIA Residential Energy Consumption Survey (RECS)** | Household energy in **physical units** — not dollars. 2024 collection complete; first release covers structure, appliances, square footage, and energy insecurity | [EIA RECS](https://www.eia.gov/consumption/residential/) · [reports](https://www.eia.gov/consumption/residential/reports.php) |
| **BLS American Time Use Survey (ATUS)** | Hours spent on paid *and unpaid* work — housework, childcare, eldercare, volunteering. Annual since 2003 | [ATUS summary](https://www.bls.gov/news.release/atus.nr0.htm) · [charts](https://www.bls.gov/tus/charts.htm) · [Census program page](https://www.census.gov/programs-surveys/atus.html) |

**ATUS is the backbone of C2's central claim.** "Aequitas supports people with *less work*" requires a baseline of how much work people currently do — and unpaid domestic labor has to be in that baseline, or the comparison flatters the status quo. ATUS was built precisely to measure non-market work.

*Also needed, not yet verified:* National Household Travel Survey (`nhts.ornl.gov`) for household transport in physical units. **Check this link before citing.**

---

## 4. Layer 3 — physical detail where IO is too coarse

IO sectors are broad (389 for the whole US economy). For specific products, process-level LCA is finer:

| Source | Status | Link |
|---|---|---|
| **Federal LCA Commons** | US government repository, searchable, free. **First stop for US process data.** *Link unverified — check `lcacommons.gov`* | — |
| **ecoinvent** | The dominant LCI database. **Commercial licence** — budget item, not free | [ecoinvent software support](https://support.ecoinvent.org/ecoinvent-lca-software-tools) |
| **Brightway** | Free and open-source LCA framework, Python. The open alternative to SimaPro/GaBi/Umberto, which are proprietary and expensive | `brightway.dev` |
| **openLCA** | Free software with a large repository of free and premium datasets | `openlca.org` |
| **Overview of LCI databases** | Useful orientation on what exists | [Ecochain: LCI databases in LCA](https://ecochain.com/blog/lci-databases-in-lca/) |

Argonne's **GREET** model (`greet.anl.gov`) is the standard for fuel and transportation life-cycles — relevant to the sandwich trace's truck. *Link unverified.*

---

## 5. Layer 4 — economy-wide material flows

| Source | Gives us | Link |
|---|---|---|
| **UNEP IRP Global Material Flows Database** | Domestic extraction, imports/exports, domestic material consumption, and **material footprint** for 200+ countries, 1970–2024. Basis for SDG indicators 8.4.1/12.2.1 | [Resource Panel](https://www.resourcepanel.org/global-material-flows-database) · [materialflows.net](https://www.materialflows.net/) |
| **2024 methodology update** | Schandl et al., *Global material flows and resource productivity: The 2024 update* | [J. Industrial Ecology](https://onlinelibrary.wiley.com/doi/10.1111/jiec.13593) |
| **UN SEEA / EW-MFA manual** | The accounting standard itself | [SEEA announcement](https://seea.un.org/news/unep-updates-global-manual-economy-wide-material-flow-accounting-and-global-material-flows) |

The IRP database is being extended to include waste and emissions data. Useful as a top-down sanity check: our bottom-up household figures, multiplied out, should not contradict national material footprint totals.

---

## 6. What we can use — recommended build path

1. **Adopt `useeior` as the C3 prototype engine.** Open code, open model, government-maintained, purpose-shaped. Building our own Leontief propagation would be reinventing a fifty-year-old wheel.
2. **Take the household basket from CE, energy from RECS, hours from ATUS.**
3. **Take embodied labor hours from EXIOBASE**, which is the one dimension USEEIO lacks and Aequitas requires.
4. **Cross-check totals against UNEP IRP** material footprint.
5. **Drop to process LCA (Federal LCA Commons / Brightway) only where a sector is too coarse** to be credible — likely food and transport first.

This also delivers §11's MVP almost as a by-product: (a) product debit-costing and (b) account intake with progressive resolution are both queries against the same engine.

---

## 7. ⚠ The axiom problem — monetary allocation

> **✅ RESOLVED 2026-08-01 for materials and energy — see `00-strategy/OP-17_coproduct_allocation.md` and [co-product-allocation](../../01-wiki/co-product-allocation.md).**
> Where a joint process's own physics is measurable, the split is a **measurement**, and price allocation is not merely undesirable but *wrong*. **USEEIO is therefore unusable as a source of truth**, though still usable as data with its splits flagged `declared` basis rather than `measured`. The conditions below still govern that use, so they are retained.
> **Not resolved for labour** — see §8 item 1, which is now OP-18 and blocks C3.

**This must be resolved before any published figure, and it is the most important thing in this note.**

EEIO models are **monetary**. They record inter-sector transactions in dollars and use price as the allocation key for distributing physical impacts. As the IO literature states plainly, this is *"the current practice of using monetary units as a proxy for physical units to represent flows of physical materials."*

For Aequitas that is a direct collision with [price-equals-cost](../../01-wiki/cost-not-price.md) (A5) and [material-flow-value](../../01-wiki/material-flow-value.md) (A1). **We would be using price to compute the very quantity we claim price should be replaced by.** An economist will spot this immediately, and if we haven't addressed it first, it discredits the number.

### Why it is nonetheless acceptable — with conditions

The collision is smaller than it looks, provided we are strict:

- Price here is a **measurement expedient**, not a value claim. We are estimating physical flows from the best available proxy, exactly as §11's MVP describes — computing true cost as a parallel overlay on existing commerce.
- **The C1 schema already handles this honestly.** Such figures are `basis: modelled`, `resolution: class_period`, with `method_ref` naming the IO model and an explicit confidence. They are *not* dressed as measurements, and they are visibly supersedable by physical data ([event-record](../../01-wiki/event-record.md) §8).
- Monetary allocation is known to distort in a *specific* direction: it under-weights cheap, heavy, low-value flows (waste, bulk materials, land) and over-weights expensive light ones. That bias is documented and can be stated.

**Condition: every published figure derived this way must be labelled as monetary-allocated, and the direction of its known bias stated.** No exceptions.

### The physical alternative — PIOTs

Physical Input-Output Tables record inter-sector flows in **metric tons rather than dollars**, which is what Aequitas actually wants.

- Weisz & Duchin, [*Physical and monetary input–output analysis: What makes the difference?*](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X), *Ecological Economics*, 2006
- [*A modular bottom-up approach for constructing physical input–output tables based on process engineering models*](https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0123-1), *Journal of Economic Structures*, 2018 — open access
- [*A physically extended EEIO framework for material efficiency assessment in United States manufacturing supply chains*](https://arxiv.org/pdf/2510.15121), arXiv 2025 — the hybrid direction

Hubacek & Giljum argued PIOTs are more appropriate for direct and indirect resource requirements — land, raw materials, energy, water — precisely because environmental pressure tracks physical flow, not monetary flow. **That is the Aequitas position, stated in the mainstream literature a generation ago.** It is strong citable support for A1.

Hybrid approaches exist (PIMO; the Waste Input-Output filter-matrix method for deriving physical flows from MRIO), which is likely the pragmatic middle path.

**PIOT coverage is far patchier than monetary IO.** Realistic sequence: monetary EEIO now, labelled honestly; migrate toward physical as coverage improves. Which is exactly what [retroactive-reweighting](../../01-wiki/retroactive-reweighting.md) is designed to absorb.

---

## 8. What is missing entirely

Gaps no existing source fills, i.e. genuine Aequitas research:

1. **🔴 Labor hours at product resolution.** EXIOBASE gives sector-level hours. Attributing hours to a specific product requires allocation — **and unlike materials and energy, labour leaves no physical trace to any one output**, so no instrument will ever supply it ([physical-trace-test](../../01-wiki/physical-trace-test.md)). Price is the usual key, which reopens §7. **This is now OP-18 and it is what blocks C3.** It will end in a *declared convention*, not a measurement.
2. ~~**Training cost embodied in skilled service.**~~ **Dissolved.** Training is front-loaded and discharged when incurred, so nothing flows downstream and no dataset is needed. *(Foundations §6.2.)*
3. **Hazard and occupational-harm accounting.** A2 requires health harms to flow retroactively into products. *Lead to check: the Social Hotspots Database (SHDB) and the Social LCA (S-LCA) literature — verify these exist and assess coverage before relying on them.*
4. **Household unpaid labor attributed to consumption.** ATUS has the hours; nothing connects them to the goods they service.
5. **🆕 Per-process energetics.** The data the allocation rule computes from — tissue-deposition energetics for livestock, per-fraction process energy for refining, turbine extraction curves. **A new dependency created by resolving OP-17**, and where OP-24 (understatement drift) lives. No source verified yet; starting points in `02-research/joint-production-allocation-problem.md`.

---

## 9. To do

- [ ] **🔴 Recursion convergence sim** — every input's debit is itself a joint split, so the allocation is defined recursively with no proof it converges. **A negative result invalidates the OP-17 resolution.** Do before building on it.
- [ ] Verify links flagged unverified: Federal LCA Commons, NHTS, GREET, Brightway, openLCA, BLS CE program page
- [ ] Install `useeior`, run a single household basket end to end — this *is* the C3 prototype
- [ ] **Re-derive a refinery slate under process-physics allocation vs USEEIO's price allocation.** A materially different answer is the most publishable early result available.
- [ ] Confirm EXIOBASE licence terms and current release — **and check whether its embodied-labour layer uses a different allocation basis than USEEIO.** More urgent now that labour is the blocking layer.
- [ ] Check whether SHDB / Social LCA exist as claimed and what they cover
- [ ] Separate note: Leontief and the mathematics of IO propagation
- [ ] Decide and document the `declared`-basis disclosure format for imported price-allocated figures (§7)

## Related

- [estimation-engine](../../01-wiki/estimation-engine.md) · [event-record](../../01-wiki/event-record.md) · [material-flow-value](../../01-wiki/material-flow-value.md) · [price-equals-cost](../../01-wiki/cost-not-price.md) · [statistical-coverage](../../01-wiki/statistical-coverage.md) · [honest-advantage](../../01-wiki/honest-advantage.md)
