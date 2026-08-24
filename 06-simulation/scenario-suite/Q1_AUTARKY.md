# Highest Egalitarian Autarkic Standard of Living — Q1 (plain-language companion)

> Companion to [`q1_autarky.py`](q1_autarky.py). Third sim of the [scenario suite](scenario_suite_METHOD.md).
> **Question:** what is the highest *egalitarian, physical* standard of living the continental US can sustain on local labour and resources alone — no imports, no exports?

## The one-line answer

**Autarkic America is not short of labour, land, water, or food. Its ceiling is set by two things only: finishing the renewable-energy build-out, and a short list of critical minerals it can't dig up at home. Complete the transition and everyone can live at roughly today's *average* — sustainably and forever. Leave energy where it is, and per-capita energy falls to about a fifth of today's.**

## How the model works

For each physical input, compute the US per-capita availability ÷ the average-person footprint. Ratio below 1 → it binds; above 1 → room. The smallest ratio is what limits the universal standard.

| Resource | Available/person | Footprint/person | Ratio | |
|---|---|---|---|---|
| Labour | 3,647 h/yr | 1,600 h/yr | **2.28** | room |
| Energy — *today's clean build* | 52 GJ | 279 GJ | **0.19** | **binds hard** |
| Energy — *full renewable potential* | 2,948 GJ | 279 GJ | **10.6** | room |
| Land (food) | 1.43 ha | 1.3 ha | **1.10** | adequate (tightest) |
| Water | 8,358 m³/yr | 1,600 m³/yr | **5.22** | room |

## What each result means

**Labour is not the limit — this is the surprise.** Even re-shoring *all* imports (roughly half of what Americans consume is foreign labour, per this project), the credited-labour pool is ~2.3× what's needed. The reason is structural to Aequitas: **self-care is credited work**, and the self-care pool (~940 B h/yr) is ~3.4× all productive labour. Hours are abundant; the old fear that a nation "can't afford" to make everything itself is a money illusion, not a physical one.

**Water and food are adequate.** The US has ~5× its water footprint in renewable supply, and is a large **net food exporter** — domestic land feeds the domestic diet with margin. Land is the *tightest* of the "adequate" resources (~1.1×), and a higher-meat diet makes it bind — so **diet is a real lever**, but there's no hard food wall.

**Energy is the swing, and it's a build-out question, not a resource one.** At today's sustainable build (renewables + nuclear ≈ 16 quads), the autarkic ceiling is only **~1/5 of current per-capita energy** — a big cut. But the US renewable *technical potential* (NREL) is **many times** current consumption; solar + wind could power the country several times over. So the constraint isn't the resource — it's how much we've *built*. And the build-out itself consumes land and minerals, which is what couples energy back to the other two.

**Critical minerals are the genuine autarky loss.** The US is >50% net-import-reliant for ~50 mineral commodities (USGS). These are the real casualties of closing the borders — they must be substituted, recycled hard (recall Q3: recycling avoids the mine entirely), or forgone.

## The egalitarian bundle (the metric you chose)

Because physical consumption is **naturally bounded** (footprint mean/median ≈ 1.20 — you can only consume so much in a 24-hour day), levelling everyone to a universal standard costs very little versus the average. Distributed under the 24/F ceiling:

> **The US can sustain a *universal* physical standard of living at roughly today's mean — autarkically and sustainably — provided it completes the renewable transition and manages a short critical-minerals list. Labour was never the constraint. The energy transition is the whole game.**

## Honesty ledger

- **This is an aggregate envelope, not a spatial or dynamic model.** It compares national per-capita totals; it does not model regional water stress, transmission, or the *time/capital* of the build-out (which is the actual hard part).
- **Land footprint is put on a domestic-diet basis** (~1.3 ha), not the gross 2.2 ha (which includes foreign land being removed under autarky). The US net-exporter status backs "adequate."
- **Renewable potential is cited conservatively** (10× consumption); NREL supply curves suggest more, but real deployment is limited by land, minerals, storage, and grid — not the raw resource.
- **Critical minerals are flagged, not quantified** here — a per-mineral substitution/recycling analysis is a follow-up (ties to the Q5 engine).
- **"Sustainable" = renewable/nuclear only.** The fossil 5/6ths of today's energy is excluded by construction — that's the point of the current-build vs potential split.

## Sources

- US energy 2023 — [EIA: production exceeded consumption by record amount](https://www.eia.gov/todayinenergy/detail.php?id=62407).
- Renewable technical potential — [NREL: Solar PV & Land-Based Wind Technical Potential, 2023 ed.](https://research-hub.nrel.gov/en/publications/solar-photovoltaics-and-land-based-wind-technical-potential-and-s).
- Land — [USDA ERS: Land and Natural Resources](https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/land-and-natural-resources).
- Critical minerals — [USGS Mineral Commodity Summaries 2024](https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries).
- Labour & footprint anchors — this project ([`median_lifestyle_RESULTS.md`](../median-lifestyle/median_lifestyle_RESULTS.md), BLS ERM).

*Tracks Foundations v0.11 §2 (universality) / §7.5 (the 24/F egalitarian bound). Physical-envelope method; the Q1/Q2/Q5 shared engine (EXIOBASE) refines the import-substitution detail.*
