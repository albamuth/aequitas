# Estimation Engine

> The machinery that turns "what a household consumes" into "what it truly cost" — propagating a consumption basket through the entire supply chain into labor, energy, materials, and pollution at every tier.

## What it does

```
consumption basket → propagate through all supply-chain tiers
   → labor hours + energy + materials + emissions
      → weight by current mitigation cost → true cost
```

It is also what fills the gaps in [statistical-coverage](statistical-coverage.md): where no [event-record](event-record.md) exists, the engine supplies an estimate, at a stated confidence and resolution, replaceable the moment real data arrives.

## We are not building this from scratch

The supply-chain propagation step is a solved problem in a discipline the project had not been drawing on: **Leontief input-output analysis**. The Leontief inverse propagates a final-demand vector through *all* upstream tiers automatically, to convergence.

The mature open implementation is **environmentally-extended input-output (EEIO)**:

- [**USEEIO**](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models) (US EPA) — 389 US sectors with satellite accounts for land, water, energy, minerals, air pollution, nutrients and toxics. Model paper: [Ingwersen et al., *Scientific Data* 2022](https://www.nature.com/articles/s41597-022-01293-7). Open-source code: [`useeior`](https://pmc.ncbi.nlm.nih.gov/articles/PMC9175389/).
- [**EXIOBASE**](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715) (Stadler et al., 2018) — multi-regional, and the one mainstream dataset carrying **employment satellite accounts: hours worked by skill level**, sourced from [ILOSTAT](https://ilostat.ilo.org/), EUROSTAT and OECD.

**EXIOBASE's labor hours matter disproportionately to us.** Conventional LCA prices labor out as a cost; Aequitas counts it as activity ([time-as-yardstick](time-as-yardstick.md)). Almost nobody else needs embodied labor hours, so almost nobody else collects them.

Household-side inputs: [BLS Consumer Expenditure Survey](https://www.bls.gov/opub/ted/consumer-expenditure-survey.htm) for the basket, [EIA RECS](https://www.eia.gov/consumption/residential/) for household energy in physical units, and [BLS American Time Use Survey](https://www.bls.gov/news.release/atus.nr0.htm) for paid *and unpaid* hours.

Full source map with links: `../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources`.

## ⚠ The monetary-allocation problem — now answered, but only for materials and energy

**EEIO models are monetary.** They record inter-sector transactions in dollars and use **price as the allocation key** for distributing physical impacts.

That collides directly with [cost-not-price](cost-not-price.md) and [material-flow-value](material-flow-value.md): we would be using price to compute the very quantity we claim should replace price.

**[co-product-allocation](co-product-allocation.md) supplies the replacement.** Where a joint process's own physics is measurable — tissue energetics, cracking enthalpy, a turbine curve — the split is a **measurement**, and price allocation is not merely undesirable but *wrong*. So:

- **USEEIO is unusable as a source of truth**, though still usable as data.
- **Any price-derived sector split must be flagged `declared` basis, never `measured`.** Best available, honestly labelled — the same discipline the axioms apply to conventions, applied to imported data.
- The bias has a **known direction**: monetary allocation under-weights cheap, heavy, low-value flows (waste, bulk materials, land) and over-weights expensive light ones.
- Improvements propagate: as process energetics are loaded, [retroactive-reweighting](retroactive-reweighting.md) re-splits everything computed the old way.

> **First high-value target: re-derive a refinery's fraction slate under process-physics allocation and compare it against USEEIO's price allocation.** A materially different answer is the most publishable technical result available early.

**Physical Input-Output Tables (PIOTs)** are the correct long-run answer — inter-sector flows in tonnes rather than dollars. See [Weisz & Duchin, *Ecological Economics* 2006](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X) and [this open-access PIOT construction method](https://journalofeconomicstructures.springeropen.com/articles/10.1186/s40008-018-0123-1). Hubacek & Giljum's argument that physical flows — not monetary ones — are what environmental pressure actually tracks is **the Aequitas position stated in mainstream literature a generation early.** Coverage is patchy, so: monetary now, labelled; physical as it matures, absorbed by [retroactive-reweighting](retroactive-reweighting.md).

## 🔴 What blocks this engine

**Labour hours at product resolution.** EXIOBASE is sector-level, and going finer requires splitting labour across a process's outputs — **which no instrument can do**, because the farmer's hours were spent on the animal, not on the hide ([physical-trace-test](physical-trace-test.md)). Materials and energy are unblocked; labour is not.

> **This is OP-18, and it is now what blocks the estimation engine.** The blocking position moved here from co-product allocation without anything being solved twice — the material half was a measurement all along, and the labour half is a genuine convention that must be *declared*, not found.

## Estimating what nobody recorded

For producers outside the system, use the finest-resolution data that exists — the smallest region with published figures ([statistical-coverage](statistical-coverage.md)). Seeking that data, and helping producers bring their supply chain into the record, is **credited trust-network work** ([distributed-auditing](distributed-auditing.md)).

> **The residual rule: cohort averages cover only the unmeasured.**
> **estimate = (N − Y) / Z** — the independently-known total, minus what measured producers actually produced, divided among those still dark.
>
> Averaged over the *whole* population instead, this creates adverse selection: good producers instrument to prove they are good, bad ones stay dark and free-ride on an average their own absence inflates. Over the residual, the estimate worsens as good producers exit — **so darkness stops paying.**
>
> Needs an independently known *N* (fine for major commodities, not universal) and a defensible count *Z*.

### Two states, not one — corrected 2026-08-29, Foundations v0.34

**A producer can be missing from the books in two unrelated ways, and calling both of them "unmeasured" hides one of them.**

| Term | What it means |
|---|---|
| **Unsubscribed** | The **person** holds no account with this network |
| **Unrecorded** | The **output** is not in this network's books |

**They are independent, and most subscribers will have unrecorded output** — a household vegetable garden the drone survey saw and the ledger did not, food given away, produce held back for the ordinary money economy, the same crop listed with two networks so it finds a buyer. **None of that is evasion**, and the discipline needs nothing added: produce you do not enter into the network cannot be sold on the network.

> **And nobody outside is charged anything.** The leftover is debit on no account. An unflattering estimate sits there until the producer joins and replaces it with a record.

## Other gaps, unblocking

- ~~**Training cost embodied in skilled service**~~ — **dissolved.** Training is front-loaded, so nothing flows downstream and no dataset is needed
- **Occupational harm flowing retroactively into products** — A2 requires it; needs Social LCA sources verified
- **Household unpaid labor attributed to the goods it services**
- **Process energetics per sector** — a *new* dependency created by the allocation rule, and where OP-24 lives

## Depends on

- [event-record](event-record.md) · [statistical-coverage](statistical-coverage.md) · [material-flow-value](material-flow-value.md)
- [co-product-allocation](co-product-allocation.md) — how a joint process's figures divide

## Why the two numbers must match before you subtract

> **Moved here from Foundations §4.4 on 2026-08-27, when §4, §5 and §6 were consolidated. The rule and its three conditions stay in Foundations §4.4. This page carries the worked case.** It is conformance requirement **14a**.

**You may only subtract two numbers that measure the same thing.**

`R = N − Y` looks like arithmetic. **It is not arithmetic until four things are true.**

| Must match | The question it answers |
|---|---|
| **The quantity** | Do both numbers count the same stuff, in the same unit? |
| **The boundary** | Do both numbers cover the same piece of the world? |
| **The window** | Do both numbers cover the same stretch of time? |
| **The error bounds** | Is the difference bigger than the doubt in the two numbers? |

**If any one of these fails, `R` is not a leftover.** It is two different measurements pushed together, and the gap between them is an artefact of the mismatch.

### The worked case

A region reports its wheat.

- **N** = 100,000 tonnes, from a satellite survey of the whole region, for the 2026 year.
- **Y** = 82,000 tonnes, recorded by the farms inside the network.
- **R = 100,000 − 82,000 = 18,000 tonnes**, said to be grown by farms nobody measured.

**Now check the four rows.**

| Check | What is actually true | Effect on R |
|---|---|---|
| Quantity | *N* is **harvested** grain. *Y* is grain **sold**. The farms kept 6,000 t for seed and feed. | R is **6,000 t too big** |
| Boundary | The satellite covers the whole valley. The network's farms are in the **upper valley only**. | Not comparable at all |
| Window | *N* is the **crop year**. *Y* is the **calendar year**. | Two months counted wrong |
| Error bounds | The satellite figure is ±12%, which is **±12,000 t**. | R = 18,000 ± 12,000 |

**Read the last row on its own.** The leftover is 18,000 tonnes and the doubt is 12,000 tonnes, so the true figure is somewhere between **6,000 and 30,000 tonnes**. **A five-fold range is not a finding.**

**Now fix the four rows.** Use sold grain for both. Use the upper valley for both. Use the crop year for both. Use a survey with ±3% error.

- **N** = 88,000 t ± 3,000
- **Y** = 82,000 t
- **R = 6,000 t ± 3,000**, so between 3,000 and 9,000 tonnes.

**That is a leftover. It is smaller, it is honest, and it can be acted on.**

> **Note what happened to the number.** The unchecked figure was 18,000 t and the checked one is 6,000 t. **Skipping this check made the unmeasured pool look three times larger than it is**, and every unmeasured producer's estimated share with it.

**Where the check happens.** Both *N* and *Y* already carry the fields it needs. Extent, vintage and error bounds sit in the provenance block that every estimated record must have. **No new field was required.**

## One method for `Z` that needs no headcount

`Z ≥ (N − Y) ÷ capacity`, where **capacity** is the most one producer could physically make, bounded by hours in a day, by land, or by throughput.

**Using that minimum assigns each unmeasured producer the most they plausibly could have made**, which is the conservative direction and the one that prompts them to come forward.

> **This is a candidate method, not the method.** The capacity ceiling is itself a constant under Foundations §3.3a, though one bounded by physics rather than by opinion.

---

## Consequences

- [onboarding-incentive](onboarding-incentive.md) — the "try it" account is a query against this engine
- [honest-advantage](honest-advantage.md) — the material-superiority comparison cannot be computed without it

---
*Status: provisional — OP-3. **Blocked on OP-18.***
*Source: `../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources`; `00-strategy/open-problems/OP-17_coproduct_allocation.md` §10*
