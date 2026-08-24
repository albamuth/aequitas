# Refinery slice — physical split vs price allocation

> **Date:** 2026-08-06 · **Code:** [`refinery_slice.py`](refinery_slice.py) · **Plan:** [`refinery_slice_PLAN.md`](refinery_slice_PLAN.md) · **Data:** [`../docs/GLOSSARY.md#src-refinery-process-energy`](../docs/GLOSSARY.md#src-refinery-process-energy)
> **Answers:** Objections §C **Test 4** / Foundations **§11(a)** — re-derive a refinery's fraction slate under §3.4a process-physics allocation and show it differs *materially* from the market-value (price) allocation USEEIO/EXIOBASE fall back to.
> **Status: ✅ BUILT & RUN — energy dimension on REAL DOE data.** The energy split now uses the DOE 2015 Petroleum Refining Bandwidth Study per-process energies (Table 4-2, U.S. 2010); six faithfulness gates pass; physical and price allocations diverge up to **~6×** on the same slate.

---

## 1. What this establishes

The EXIOBASE loader reproduced standard EEIO footprints — but a monetary IOT has *already* price-allocated joint production, so it can only agree with price. This slice is the first exercise of the engine's genuine joint-production path (`Θ ≠ I`) on real-grounded data, and it produces the project's first **materially-different, defensible** per-fraction result — the most publishable early technical claim.

**One refinery process → seven fractions, measured in barrels.** Three debit dimensions, each split per §3.2a; the headline is **energy**, split by *where the process physically sent it*.

## 2. The result (energy debit per barrel, MMBtu/bbl — real DOE energies)

| fraction | yield % | physical | price | physical ÷ price | |
|---|--:|--:|--:|--:|---|
| lpg | 4.8 | 0.393 | 0.154 | **2.6×** | under-costed by price |
| gasoline | 46.7 | 0.439 | 0.404 | 1.1× | ~similar |
| jet | 9.5 | 0.364 | 0.384 | 0.9× | |
| diesel | 28.6 | 0.315 | 0.434 | **0.7×** | over-costed by price |
| residual_fuel | 2.9 | 0.142 | 0.250 | **0.6×** | over-costed by price |
| **petcoke** | 4.8 | **0.327** | **0.058** | **5.7×** | **badly under-costed by price** |
| asphalt | 2.9 | 0.142 | 0.192 | 0.7× | over-costed by price |

**The headline:** **petcoke costs ~5.7× more under physical allocation than under price.** It is a cheap byproduct (~$15/bbl) that nonetheless consumed real coking energy — price allocation, keying off revenue, assigns it almost nothing. **LPG** is similarly under-costed (2.6×). Conversely, **diesel, residual fuel and asphalt are *over*-costed by price** — valuable (diesel) or mid-priced but much of their volume is lightly-processed straight-run, so their true energy cost is lower than their revenue share implies.

**The direction is processing depth, not weight** — which corrected the plan's initial guess. Gasoline is **47% of volume but 55% of the energy** (DOE sector-wide anchor: ~49% / ~62%; this model covers the nine bandwidth processes = 68% of sector energy), because the gasoline pathway (reforming, FCC, alkylation, isomerization) is energy-intensive. Cost follows the energy the process actually spent, wherever price and weight happen to fall. Physical energy debit is in real units: **gasoline ~0.44 MMBtu/bbl of process energy** (~8% of gasoline's ~5.2 MMBtu heating value), residual ~0.14.

## 3. Why it's faithful — the six gates

1. **Conservation** — both allocations sum to the pool in every dimension (efficiency axiom); neither invents or loses debit.
2. **Non-negativity** — inherited from the Neumann-series result.
3. **Universality** (the important one) — the physical split is **exactly price-independent**: shock every price ×3.7 and the physical per-barrel debit does not move at all. This is the §3.4a / B9 property that killed demand-contingent splitting — *demand cannot enter cost*.
4. **Material divergence** — L1 distance 47.4; petcoke under-costed by price; gasoline energy share > volume share.
5. **Gasoline energy anchor** — 56%, inside the DOE ~62% ballpark, validating the two-channel construction against a real published number.
6. **OP-18** — labour rides the material split exactly (constant hr/kg across fractions).

## 4. The two-channel energy split (physical-trace test *inside* the refinery)

Energy `θ` is built from the real DOE per-process energies in two channels, honestly labelled:

- **Conversion (`measured`)** — reforming/FCC/hydrocracking/coking/hydrotreating/alkylation/isomerization energy (1,336 TBtu) routes to the specific products those units make. A genuine physical trace (the routing shares are the remaining modelled layer, §5).
- **Distillation (`declared` convention)** — atmospheric + vacuum distillation (826 TBtu) heat the whole barrel to separate it; there is no per-fraction trace, so the shared column energy is split by a declared basis (volume as an enthalpy-demand stand-in). The DOE figures are Current-Typical *metered* consumption, so inefficiency is already counted (§3.5/A1 — the 100 MJ applied, not the 80 MJ "usefully" used).

The real distillation-to-conversion split is **826 : 1,336 ≈ 38% : 62%** — i.e. most refinery process energy is *conversion*, which is exactly why physical allocation departs so far from volume.

This is the refinery being *harder* than the cattle case: part measurement, part convention — and saying so, per the physical-trace test.

## 5. What is real, and what still isn't

**Real (numbers pass, 2026-08-06):**
- **Per-process energies** — DOE 2015 Bandwidth Study, Table 4-2, U.S. 2010 onsite Current Typical energy by process (TBtu/yr): atmospheric distillation 604, vacuum 222, reforming 279, FCC 334, hydrocracking 85, coking 114, hydrotreating 390, alkylation 90, isomerization 44. Sum 2,163 TBtu = 68% of sector-wide onsite energy. Per-bbl-crude intensity from Table 3-1 throughput (5,540 M bbl).
- **Metered actuals, losses included** — these are Current Typical consumption, not thermodynamic minima, so the §3.5/A1 principle (count the 100 MJ, not the 80) is satisfied by the source.
- **Volume yields** — standard EIA refinery-yield proportions.

**Still representative (flagged, next refinement):**
- **The conversion routing** — *which* fractions each conversion unit's energy goes to (FCC→70% gasoline, coking→45% petcoke, …) is a modelled convention from standard refinery flow (DOE Fig 2-2), not a metered per-fraction number. This is the remaining modelling layer; Argonne 2011 (69026) / Han et al. ES&T give a published process-level allocation to swap in.
- **Materials, labour, prices** — the DOE bandwidth study is *process energy only*, so crude mass, operating labour, and product prices remain representative. Materials/labour don't affect the energy headline; prices only scale the (already price-independent) physical result's contrast.

**By design / structural:**
- **Pollution excluded** — a fraction's transferable cost carries no pollution (§3.2b non-cascade = §6.2a closure). See the plan's §6a.
- **Crude exogenous** — folded into direct inputs; upstream recursion already proven.
- **Single representative refinery** — hydroskimming vs deep-conversion differ (the "fuzzy middle", §C Test 3). Per-refinery is the high-resolution version.
- **Petcoke in volume** — conventionally mass/short-tons; kept in bbl-equivalent for a uniform basis.

## 6. What's next

- **Close the routing gap:** retrieve Argonne 2011 (69026) / Han et al. ES&T for a *published* per-product process-energy allocation, replacing the modelled conversion routing. Then every energy number is sourced.
- **Materials/labour/prices** from EIA/BLS for a full real vector.
- **This is the academic paper's Sraffa/ISO reply in concrete form** (Foundations §9): process-physics allocation gives a different, universality-satisfying answer where price allocation is arbitrary — now on real DOE energy data.
