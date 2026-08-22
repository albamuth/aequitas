# Refinery Energy, Split Fuel by Fuel — Data Sources

**Version:** 0.2
**Type:** data-source note — for the oil-refinery worked example
**Author(s):** US Energy Information Administration; US Department of Energy (its manufacturing-efficiency study); Argonne National Laboratory
**Published:** DOE efficiency study 2015; Argonne *Energy Efficiencies of Petroleum Refineries* 2011; Han et al. 2014/2015
**Retrieved:** 2026-08-06
**URL:**
- [US Energy Information Administration — Refinery Yield](https://www.eia.gov/dnav/pet/pet_pnp_pct_dc_nus_pct_m.htm) (how a barrel of crude splits into products, by volume)
- [EIA — jet fuel's record share of 2024 output](https://www.eia.gov/todayinenergy/detail.php?id=64786)
- [DOE — Bandwidth Study on Energy Use in Petroleum Refining (2015)](https://www.energy.gov/sites/prod/files/2015/08/f26/petroleum_refining_bandwidth_report.pdf)
- [Argonne — Energy Efficiencies of Petroleum Refineries (2011)](https://publications.anl.gov/anlpubs/2011/01/69026.pdf)
- [Han et al. — Energy Efficiency and Greenhouse-Gas Intensity of Petroleum Products](https://pubs.acs.org/doi/10.1021/es5010347) *(paywalled)*
- [ENERGY STAR Guide for Petroleum Refineries (2015)](https://www.energystar.gov/sites/default/files/tools/ENERGY_STAR_Guide_Petroleum_Refineries_20150330.pdf)

**Local copy:** the DOE and ENERGY STAR PDFs are saved locally. **The key DOE tables were extracted 2026-08-06 and are reproduced below**, and are now wired into the refinery simulation. The Argonne and Han papers are paywalled or blocked online; retrieve them by hand to close the last gap.

## Why this matters to Aequitas

A refinery is the textbook case of the joint-production problem (see [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem)): one stream of crude oil goes in, and a whole slate of fuels comes out — gasoline, diesel, jet fuel, tar, coke. The question is *how to divide the refinery's cost among those fuels.*

Aequitas's rule is: **measure where the process physically sent its energy**, fuel by fuel, and split the cost accordingly. See [Foundations §3.4a](../docs/Aequitas_Foundations_v0.17.md#34a-joint-production--the-process-allocates-itself). That's exactly what Argonne's process-level method produces — it assigns each refining unit's *metered* energy to the fuels that actually pass through it. Standard footprint databases don't do this; they fall back to splitting by *market value* instead. The worked example contrasts the two — and the difference is the point.

## The DOE study — extracted energy tables (US, 2010)

*Units, plainly: "Btu" (British thermal units) is just a measure of heat energy; "bbl" is a barrel of oil; "TBtu/yr" is trillions of Btu per year — the total heat a process burns nationally in a year. The exact numbers matter less than the split they produce.*

**Energy used by each refining step** (metered actuals, losses included):

| Process | Energy per barrel (Btu/bbl) | Throughput (M bbl/yr) | National total (TBtu/yr) |
|---|--:|--:|--:|
| Atmospheric crude distillation | 109,100 | 5,540 | 604 |
| Vacuum crude distillation | 89,100 | 2,504 | 222 |
| Catalytic reforming | 263,900 | 1,055 | 279 |
| Fluid catalytic cracking | 182,800 | 1,827 | 334 |
| Catalytic hydrocracking | 158,900 | 532 | 85 |
| Coking / visbreaking | 147,700 | 770 | 114 |
| Hydrotreating | 80,800 | 4,829 | 390 |
| Alkylation | 246,700 | 365 | 90 |
| Isomerization | 216,000 | 203 | 44 |
| **Total (9 processes)** | | | **2,163** (= 68% of all refinery energy) |

The two *distillation* steps (826 TBtu) simply heat the whole barrel to separate it — a shared cost with no per-fuel trace. The seven *conversion* steps (1,336 TBtu) each work on specific product streams, so their energy *can* be traced to particular fuels. That gives a roughly **38% shared : 62% traceable** split of refinery energy.

**How a barrel splits into products, 2010** (millions of barrels): diesel/heating oil 1,538; gasoline 1,142; jet 521; petroleum coke 296; refinery gas 245; liquefied gases 240; heavy fuel oil 210; asphalt 139; petrochemical feedstock 119; lubricants 60; misc 28. **Self-consumption:** the refinery burns ~90% of its own gas and ~28% of its coke as fuel to run itself — an internal loop worth noting.

> **This closes the open task in [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem)** ("source refinery per-fuel process energy — none found yet").

## Key findings

- **The load-bearing result:** gasoline is **~49% of refinery output by volume but eats ~62% of refinery energy.** Gasoline is *energy-intensive to make* — so splitting by physical energy pushes cost *toward* gasoline, above its ~50% share of revenue. This **corrects the plan's first guess** (that price under-costs the *heavy* fractions): the real driver is *how much processing a fuel needs*, not how heavy it is.
- **Argonne's process-level method** assigns each unit's energy to its outputs. Splitting by weight and splitting by energy give *similar* answers here; splitting by *market value* gives a *different* one — and that difference is the whole result of the example.
- **"Processing gain":** cracking heavy molecules into lighter ones means the products add up to *more* volume than the crude that went in (~6% more in the US). So volume is a *reporting* figure, not a conserved physical quantity — which is exactly why it *can't* be the basis for splitting cost. (Weight *is* conserved; the example splits by energy.)
- **Two kinds of energy inside the refinery — the physical-trace test applied within one plant:**
  - **Traceable (measured):** the conversion units (reforming, cracking, coking, alkylation) whose energy flows to the specific fuels they make. Gasoline-pathway units dominate.
  - **Shared (declared convention):** the distillation that heats the whole barrel at once, with no per-fuel trace. This is split by a *declared* rule and then scaled to match the metered actual, losses included. (The distinction between a *measured* split and a *declared* one is Aequitas's physical-trace test — trace it, measure it; no trace, declare a convention and say so.)
- **Prices for the contrast:** gasoline, diesel, and jet are the high-value majority; heavy fuel oil is discounted; petroleum coke is very cheap — yet coke and the converted streams carry real conversion energy. So splitting by *price* under-costs them, which is the discrepancy the example exposes.

## To do

- [x] ~~Extract the DOE per-unit energy figures~~ — **done 2026-08-06** (table above; wired into the simulation).
- [ ] Retrieve the Argonne 2011 and Han papers by hand for a *published* per-fuel energy split — closes the last modelled layer.
- [ ] Add the remaining dimensions from real data: crude mass (materials), operating labour, and product prices — replacing the current stand-in figures.
- [ ] Pull exact per-fuel volume yields from the EIA yield data (currently using standard proportions).

## Related

- [[co-product-allocation]] · [[physical-trace-test]] · [[price-equals-cost]] · [Joint-production problem](../docs/GLOSSARY.md#src-joint-production-allocation-problem)
- [`00-strategy/OP-17_coproduct_allocation.md`](../docs/OP-17_coproduct_allocation.md)
