# Estimation Engine

> The machinery that turns "what a household consumes" into "what it truly cost" — propagating a consumption basket through the entire supply chain into labor, energy, materials, and pollution at every tier.

## What it does

```
consumption basket → propagate through all supply-chain tiers
   → labor hours + energy + materials + emissions
      → weight by current mitigation cost → true cost
```

It is also what fills the gaps in [[statistical-coverage]]: where no [[event-record]] exists, the engine supplies an estimate, at a stated confidence and resolution, replaceable the moment real data arrives.

## We are not building this from scratch

The supply-chain propagation step is a solved problem in a discipline the project had not been drawing on: **Leontief input-output analysis**. The Leontief inverse propagates a final-demand vector through *all* upstream tiers automatically, to convergence.

The mature open implementation is **environmentally-extended input-output (EEIO)**:

- [**USEEIO**](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models) (US EPA) — 389 US sectors with satellite accounts for land, water, energy, minerals, air pollution, nutrients and toxics. Model paper: [Ingwersen et al., *Scientific Data* 2022](https://www.nature.com/articles/s41597-022-01293-7). Open-source code: [`useeior`](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175389/).
- [**EXIOBASE**](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715) (Stadler et al., 2018) — multi-regional, and the one mainstream dataset carrying **employment satellite accounts: hours worked by skill level**, sourced from [ILOSTAT](https://ilostat.ilo.org/), EUROSTAT and OECD.

**EXIOBASE's labor hours matter disproportionately to us.** Conventional LCA prices labor out as a cost; Aequitas counts it as activity ([[time-as-yardstick]]). Almost nobody else needs embodied labor hours, so almost nobody else collects them.

Household-side inputs: [BLS Consumer Expenditure Survey](https://www.bls.gov/opub/ted/consumer-expenditure-survey.htm) for the basket, [EIA RECS](https://www.eia.gov/consumption/residential/) for household energy in physical units, and [BLS American Time Use Survey](https://www.bls.gov/news.release/atus.nr0.htm) for paid *and unpaid* hours.

Full source map with links: `../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources`.

## ⚠ The monetary-allocation problem — now answered, but only for materials and energy

**EEIO models are monetary.** They record inter-sector transactions in dollars and use **price as the allocation key** for distributing physical impacts.

That collides directly with [[price-equals-cost]] and [[material-flow-value]]: we would be using price to compute the very quantity we claim should replace price.

**[[co-product-allocation]] supplies the replacement.** Where a joint process's own physics is measurable — tissue energetics, cracking enthalpy, a turbine curve — the split is a **measurement**, and price allocation is not merely undesirable but *wrong*. So:

- **USEEIO is unusable as a source of truth**, though still usable as data.
- **Any price-derived sector split must be flagged `declared` basis, never `measured`.** Best available, honestly labelled — the same discipline the axioms apply to conventions, applied to imported data.
- The bias has a **known direction**: monetary allocation under-weights cheap, heavy, low-value flows (waste, bulk materials, land) and over-weights expensive light ones.
- Improvements propagate: as process energetics are loaded, [[retroactive-reweighting]] re-splits everything computed the old way.

> **First high-value target: re-derive a refinery's fraction slate under process-physics allocation and compare it against USEEIO's price allocation.** A materially different answer is the most publishable technical result available early.

**Physical Input-Output Tables (PIOTs)** are the correct long-run answer — inter-sector flows in tonnes rather than dollars. See [Weisz & Duchin, *Ecological Economics* 2006](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X) and [this open-access PIOT construction method](https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0123-1). Hubacek & Giljum's argument that physical flows — not monetary ones — are what environmental pressure actually tracks is **the Aequitas position stated in mainstream literature a generation early.** Coverage is patchy, so: monetary now, labelled; physical as it matures, absorbed by [[retroactive-reweighting]].

## 🔴 What blocks this engine

**Labour hours at product resolution.** EXIOBASE is sector-level, and going finer requires splitting labour across a process's outputs — **which no instrument can do**, because the farmer's hours were spent on the animal, not on the hide ([[physical-trace-test]]). Materials and energy are unblocked; labour is not.

> **This is OP-18, and it is now what blocks the estimation engine.** The blocking position moved here from co-product allocation without anything being solved twice — the material half was a measurement all along, and the labour half is a genuine convention that must be *declared*, not found.

## Estimating what nobody recorded

For producers outside the system, use the finest-resolution data that exists — the smallest region with published figures ([[statistical-coverage]]). Seeking that data, and helping producers bring their supply chain into the record, is **credited trust-network work** ([[distributed-auditing]]).

> **The residual rule: cohort averages cover only the unmeasured.**
> **estimate = (N − Y) / Z** — the independently-known total, minus what measured producers actually produced, divided among those still dark.
>
> Averaged over the *whole* population instead, this creates adverse selection: good producers instrument to prove they are good, bad ones stay dark and free-ride on an average their own absence inflates. Over the residual, the estimate worsens as good producers exit — **so darkness stops paying.**
>
> Needs an independently known *N* (fine for major commodities, not universal) and a defensible count *Z*.

## Other gaps, unblocking

- ~~**Training cost embodied in skilled service**~~ — **dissolved.** Training is front-loaded, so nothing flows downstream and no dataset is needed
- **Occupational harm flowing retroactively into products** — A2 requires it; needs Social LCA sources verified
- **Household unpaid labor attributed to the goods it services**
- **Process energetics per sector** — a *new* dependency created by the allocation rule, and where OP-24 lives

## Depends on

- [[event-record]] · [[statistical-coverage]] · [[material-flow-value]]
- [[co-product-allocation]] — how a joint process's figures divide

## Consequences

- [[onboarding-incentive]] — the "try it" account is a query against this engine
- [[honest-advantage]] — the material-superiority comparison cannot be computed without it

---
*Status: provisional — OP-3. **Blocked on OP-18.***
*Source: `../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources`; `00-strategy/OP-17_coproduct_allocation.md` §10*
