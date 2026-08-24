# Data Sources for the Estimation Engine

**Version:** 0.2
**Type:** source survey
**Compiled:** 2026-07-31
**Bears on:** the "estimation engine" (the software that works out a thing's true cost by tracing its whole supply chain), the demonstration that Aequitas leaves people better off, the mechanism that recomputes costs as the science improves, and the first pilot deployment.

> **Headline: don't build the cost-tracing engine from scratch.** The hard part already exists as a mature scientific field — it's the study of how every industry feeds into every other, extended to track environmental impacts. It comes with open models, open code, and government-maintained data. What Aequitas has to *add* is a labour dimension nobody else bothers to track, plus a correction to how shared costs get split. Section 7 covers the one place this borrowed machinery clashes with an Aequitas principle.

*A note on jargon: this field is full of acronyms. Each is spelled out and explained in plain words the first time it appears, and the underlying idea is always simple — "follow a product back through everyone who helped make it, and add up what they each used."*

---

## 1. What the engine actually has to compute

Start from the question *"what does a typical American household truly cost?"* The steps are:

1. Take everything the household buys.
2. Trace each item back through its **entire supply chain** — the shop, the factory, the factory's suppliers, their suppliers, and so on.
3. At every step, tally up the labour hours, energy, materials, and pollution.
4. Re-weight all of it by what it would cost *today* to clean up or replace.
5. That total is the "true cost."

Step 2 is the hard one — and it's a *solved* problem in a field the project hadn't been drawing on: **input-output analysis.** This is a decades-old technique (going back to the economist Wassily Leontief) that takes a basket of final purchases and automatically pushes it back through *all* the upstream layers of the economy at once — direct suppliers, their suppliers, and so on until it converges. That's exactly the supply-chain tracing Aequitas needs, and it has been standard practice since the 1970s.

---

## 2. The core tool — environmentally-extended input-output models

"Environmentally-extended input-output" (**EEIO**) just means the input-output tracing above, with pollution and resource-use figures bolted on so that tracing a purchase also tells you the emissions, water, land, and materials behind it.

### The US model (start here)

- **Program page:** [US Environmentally-Extended Input-Output (USEEIO) Models, US EPA](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models)
- **Model paper:** Ingwersen et al., [*USEEIO v2.0*](https://www.nature.com/articles/s41597-022-01293-7), *Scientific Data*, 2022 — free to read
- **Code:** [`useeior`, an open-source R package](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175389/) — open source, and the models can be rebuilt from a configuration file

**What it gives us:** 389 US industry sectors, each tagged with its **land, water, energy and mineral use, air pollution, nutrient runoff, and toxic releases.** Version 2 adds a proper accounting for the waste sector, ready-made "what a US household consumes" baskets, a domestic-only variant (to separate impacts made at home from impacts imported), and adjustments for price changes between years. Those ready-made consumption baskets are close to purpose-built for the "does Aequitas leave people better off?" demonstration.

### The international — and *labour* — layer

- **Paper:** Stadler et al., [*EXIOBASE 3*](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715), *Journal of Industrial Ecology*, 2018

EXIOBASE is the same kind of model, but spanning many countries *and* — crucially — carrying **hours worked**, broken down by skill level and gender, drawn from official labour statistics ([ILOSTAT](https://ilostat.ilo.org/) and others). It even tracks precarious work (unpaid family workers, the self-employed).

**Why this matters more to Aequitas than to anyone else:** the labour hours embodied in a supply chain are exactly what Aequitas counts and ordinary footprint studies throw away — those studies treat labour as a dollar cost to be minimised, not as human activity to be tallied. EXIOBASE is the only mainstream dataset that carries hours at supply-chain scale. Treat it as a critical dependency. It covers 44 countries plus 5 "rest of world" regions, from 1995 on.

### A newer alternative

- Nature, 2025: [*FIGARO-E3*](https://www.nature.com/articles/s41597-025-04431-z) — a higher-resolution model built to line up with official statistics, which may make any public claim easier to defend. Worth evaluating against EXIOBASE.

---

## 3. What a household actually consumes

| Source | What it gives us | Link |
|---|---|---|
| **Consumer Expenditure Survey** (US Bureau of Labor Statistics) | what a typical household buys, by category and by income band | [overview](https://www.bls.gov/opub/ted/consumer-expenditure-survey.htm) |
| **Residential Energy Consumption Survey** (US Energy Information Administration) | household energy use in **physical units** — not dollars — covering appliances, home size, and energy hardship | [survey](https://www.eia.gov/consumption/residential/) |
| **American Time Use Survey** (US Bureau of Labor Statistics) | hours spent on paid *and unpaid* work — housework, childcare, eldercare, volunteering — yearly since 2003 | [summary](https://www.bls.gov/news.release/atus.nr0.htm) |

**The time-use survey is the backbone of the "less work" claim.** To say "Aequitas supports people with *less* work" you need a baseline of how much work people do now — and unpaid housework and care have to be in that baseline, or the comparison quietly flatters today's economy. This survey was built to measure exactly that non-market work.

*Also needed, not yet verified:* a national travel survey for household transport in physical units. **Check the link before citing.**

---

## 4. Finer physical detail where the broad model is too coarse

The 389 industry sectors above are broad. For a *specific* product, "process-level" life-cycle data is finer-grained:

| Source | Status | Link |
|---|---|---|
| **Federal LCA Commons** | free, searchable US government repository. **First stop for US process data.** *Link unverified — check.* | — |
| **ecoinvent** | the dominant such database. **Commercial licence** — a budget item, not free | [support](https://support.ecoinvent.org/ecoinvent-lca-software-tools) |
| **Brightway** | free, open-source, Python. The open alternative to the expensive proprietary tools | `brightway.dev` |
| **openLCA** | free software, large mix of free and paid datasets | `openlca.org` |

("LCA" = life-cycle assessment: the discipline that measures a product's total footprint from raw material to disposal.) Argonne National Laboratory's **GREET** model is the standard for fuel and transport footprints — relevant to the truck in the sandwich example. *Link unverified.*

---

## 5. An economy-wide sanity check

| Source | What it gives us | Link |
|---|---|---|
| **UN Global Material Flows Database** | how much raw material each of 200+ countries digs up, imports, exports, and consumes, 1970–2024 | [Resource Panel](https://www.resourcepanel.org/global-material-flows-database) · [materialflows.net](https://www.materialflows.net/) |

Useful as a top-down reality check: the bottom-up household figures, scaled up to the whole country, shouldn't contradict these national totals.

---

## 6. Recommended build path

1. **Adopt the open `useeior` engine as the prototype.** Building our own supply-chain tracer would be reinventing a fifty-year-old wheel.
2. **Take the household basket, energy, and hours from the three US surveys in §3.**
3. **Take embodied labour hours from EXIOBASE** — the one dimension the US model lacks and Aequitas requires.
4. **Cross-check totals against the UN material-flows database.**
5. **Drop to finer process data only where a broad sector isn't credible** — food and transport first.

This also delivers the first-pilot deployment almost for free: both "cost out a product" and "sign up an account at rough resolution and sharpen it over time" are queries against the same engine.

---

## 7. ⚠ The one clash with an Aequitas principle — splitting by price

> **✅ RESOLVED 2026-08-01 for materials and energy** — see [`00-strategy/OP-17_coproduct_allocation.md`](../docs/OP-17_coproduct_allocation.md) and [[co-product-allocation]]. Where a shared process's own physics can be measured, the split is a *measurement*, and splitting by price isn't just undesirable, it's *wrong*. So the US model **can't be used as a source of truth** — only as data, with its price-based splits flagged as "declared," not "measured." The conditions below still govern that use. **Not resolved for labour** — see §8 item 1.

**This must be settled before any figure is published, and it's the most important thing in this note.**

These input-output models are built on **money.** They record what each industry pays every other industry in *dollars*, and they use those dollar amounts to divide up the physical impacts. In the field's own words, this is "using monetary units as a proxy for physical units."

For Aequitas that collides head-on with two core rules: that a price is just a cost with no markup ([Foundations §A5](../docs/Aequitas_Foundations_v0.19.md#a5-price--cost)), and that cost is measured as physical flow, not money ([Foundations §A1](../docs/Aequitas_Foundations_v0.19.md#a1-materialism-of-cost)). **We'd be using price to compute the very thing we say price should be replaced by.** An economist will spot this instantly, and if we haven't addressed it up front, it discredits the number.

### Why it's acceptable anyway — with strict conditions

- Here, price is a **measurement shortcut**, not a claim about worth. We're estimating physical flows from the best proxy on hand — exactly what a first pilot does, computing true cost alongside existing money commerce.
- **The event-record schema already handles this honestly:** such figures are tagged as *estimated* (from a named model, at coarse resolution, with a stated confidence), never dressed up as measurements, and openly replaceable by real physical data later. See [Foundations §A6](../docs/Aequitas_Foundations_v0.19.md#a6-derived-not-stored).
- The money-based split distorts in a *known* direction: it under-counts cheap, heavy, low-value flows (waste, bulk materials, land) and over-counts expensive light ones. That bias can be stated openly.

**Condition: every figure computed this way must be labelled as money-split, with the direction of its known bias stated. No exceptions.**

### The physical alternative

"Physical input-output tables" record what industries send each other in **tonnes rather than dollars** — which is what Aequitas actually wants.

- Weisz & Duchin, [*Physical and monetary input–output analysis*](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X), *Ecological Economics*, 2006
- [*A modular bottom-up approach for constructing physical input–output tables*](https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0123-1), 2018 — free to read
- [*A physically extended framework for material efficiency*](https://arxiv.org/pdf/2510.15121), arXiv 2025 — the hybrid direction

Researchers argued a generation ago that physical tables are the *right* tool for tracking land, materials, energy, and water, precisely because environmental pressure follows physical flow, not money. **That's the Aequitas position, stated in the mainstream literature decades ago** — strong support for the materials-not-money principle.

**But physical tables cover far less ground than money-based ones.** Realistic plan: use money-based models now, labelled honestly, and migrate toward physical as coverage improves — which is exactly what the "recompute as the data improves" mechanism ([[retroactive-reweighting]]) is built to absorb.

---

## 8. What no existing source provides — genuine Aequitas research

1. **🔴 Labour hours down to a single product.** EXIOBASE gives hours per *sector*. Pinning hours to a *specific product* needs a split — and unlike materials and energy, **labour leaves no physical trace pointing to one output**, so no instrument will ever supply it (see [[physical-trace-test]]). Price is the usual fallback, which reopens §7. This is the live "splitting a team's contribution" problem and it's what blocks the demonstration. It will end in a *declared convention*, not a measurement. See [Ellerman: labour theory of property](../docs/GLOSSARY.md#src-ellerman-labor-theory-of-property).
2. ~~**Training cost buried in skilled work.**~~ **Dissolved.** Training is paid up front and settled when it happens, so nothing flows downstream and no dataset is needed. See [Foundations §6.2](../docs/Aequitas_Foundations_v0.19.md#62-training-front-loaded).
3. **Occupational-harm accounting.** Aequitas requires health harms to flow *backwards* into the products a dangerous job made. *Lead to check: the Social Hotspots Database and the "social life-cycle assessment" literature — verify they exist and assess coverage before relying on them.*
4. **Household unpaid labour tied to consumption.** The time-use survey has the hours; nothing connects them to the goods they support.
5. **🆕 Per-process energy detail.** The physics the split rule computes from — how a steer's body distributes feed energy, how a refinery's energy splits across fuels, a turbine's electricity-versus-heat curve. A new dependency created by the joint-production solution, and where the "understatement drift" risk lives. See [Refinery process energy](../docs/GLOSSARY.md#src-refinery-process-energy) and [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem).

---

## 9. To do

- [ ] **🔴 Prove the whole interlocking calculation settles** — every input's cost is itself a split, feeding another, so the whole thing is defined in a loop with no guarantee it converges. *A negative result would invalidate the joint-production solution.* (Since run and passed — [`06-simulation/RESULTS.md`](../sims/RESULTS.md).)
- [ ] Verify the unverified links: Federal LCA Commons, the travel survey, GREET, Brightway, openLCA, the expenditure-survey program page.
- [ ] Install `useeior`, run one household basket end to end — this *is* the prototype.
- [ ] **Re-compute a refinery's fuel slate by process-physics versus by price.** A materially different answer is the most publishable early result available (see [Refinery process energy](../docs/GLOSSARY.md#src-refinery-process-energy)).
- [ ] Confirm EXIOBASE licence terms, and check whether its labour layer uses a different splitting rule than the US model.
- [ ] Check whether the Social Hotspots Database / social life-cycle assessment exist as claimed and what they cover.
- [ ] Decide and document the disclosure format for imported price-split figures (§7).

## Related

- [[estimation-engine]] · [[event-record]] · [[material-flow-value]] · [[price-equals-cost]] · [[statistical-coverage]] · [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem) · [Refinery process energy](../docs/GLOSSARY.md#src-refinery-process-energy)
