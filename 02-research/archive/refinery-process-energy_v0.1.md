# Refinery per-fraction process energy — data sources

**Type:** data source note — for the refinery slice (Objections §C Test 4)
**Author(s):** U.S. EIA; U.S. DOE (AMO Bandwidth Study); Argonne National Laboratory (Elgowainy, Han, Wang et al., GREET)
**Published:** DOE bandwidth study 2015; Argonne *Energy Efficiencies of Petroleum Refineries* 2011; Han et al. ES&T 2014/2015
**Retrieved:** 2026-08-06
**URL:**
- [EIA — U.S. Refinery Yield](https://www.eia.gov/dnav/pet/pet_pnp_pct_dc_nus_pct_m.htm) (volume % by product)
- [EIA Today in Energy — jet fuel record share of 2024 output](https://www.eia.gov/todayinenergy/detail.php?id=64786)
- [DOE AMO — Bandwidth Study on Energy Use… Petroleum Refining (2015)](https://www.energy.gov/sites/prod/files/2015/08/f26/petroleum_refining_bandwidth_report.pdf)
- [Argonne — Energy Efficiencies of Petroleum Refineries (2011)](https://publications.anl.gov/anlpubs/2011/01/69026.pdf)
- [Han et al., ES&T — Energy Efficiency and GHG Intensity of Petroleum Products at U.S. Refineries](https://pubs.acs.org/doi/10.1021/es5010347) *(paywalled)*
- [ENERGY STAR Guide for Petroleum Refineries (2015)](https://www.energystar.gov/sites/default/files/tools/ENERGY_STAR_Guide_Petroleum_Refineries_20150330.pdf)

**Local copy:** DOE bandwidth report and ENERGY STAR guide PDFs saved under `tool-results/`. **Text extracted with `pypdf` 2026-08-06 — the key DOE tables are captured below and now wired into `refinery_slice.py`.** Argonne 2011 and ES&T are 403/paywalled via WebFetch; retrieve manually to close the routing gap.

## DOE Bandwidth Study — extracted tables (U.S. 2010)

**Table 4-2 — onsite Current Typical energy by process** (metered actuals, incl. losses):

| Process | Energy intensity (Btu/bbl) | Throughput (M bbl/yr) | Onsite CT (TBtu/yr) |
|---|--:|--:|--:|
| Atmospheric crude distillation | 109,100 | 5,540 | 604 |
| Vacuum crude distillation | 89,100 | 2,504 | 222 |
| Catalytic reforming | 263,900 | 1,055 | 279 |
| Fluid catalytic cracking | 182,800 | 1,827 | 334 |
| Catalytic hydrocracking | 158,900 | 532 | 85 |
| Coking/visbreaking | 147,700 | 770 | 114 |
| Hydrotreating | 80,800 | 4,829 | 390 |
| Alkylation | 246,700 | 365 | 90 |
| Isomerization | 216,000 | 203 | 44 |
| **Total (9 processes)** | | | **2,163** (= 68% of 3,176 sector-wide) |

Distillation (atm+vac) = 826 TBtu (declared channel); the 7 conversion processes = 1,336 TBtu (measured channel) → **38% : 62%**.

**Table 2-1 — U.S. refinery product volumes 2010** (EIA 2013b, M bbl): distillate 1,538; motor gasoline 1,142; jet 521; petcoke 296; still gas 245; LRG 240; residual 210; asphalt 139; petrochem feedstock 119; lubes 60; misc 28. *(Note: this narrower production accounting inverts the usual gasoline>distillate ratio; the model uses the standard EIA **refinery-yield** proportions for volume shares instead.)* **Self-consumption:** ~90% of still gas, ~28% of petcoke, <1% of distillate/residual/LRG consumed onsite as fuel — the refinery-fuel loop.

> **Closes the open to-do in `joint-production-allocation-problem.md` line 74** ("Source refinery per-fraction process energy — no source identified yet").

## Why this matters

The refinery slice needs the §3.4a physical θ — **where the process physically sent its energy**, per fraction. This is exactly what the Argonne *process-level allocation method* produces (assign each refining unit's metered energy to the products that pass through it), and it is **not** in EXIOBASE/USEEIO, which fall back to market-value allocation. The slice contrasts the two.

## Key findings (anchors established; exact per-unit numbers pending OCR)

- **The load-bearing anchor:** gasoline is **≈49% of refinery output by volume but consumes ≈62% of refinery energy** (DOE bandwidth study / Argonne). Gasoline is **energy-intensive per unit** — the physical split pushes cost *toward* it, above its ~50% revenue share. **This corrects the plan's initial guess** ("price under-costs heavy fractions"): the real driver is *processing depth*, not weight.
- **Argonne process-level method** allocates each unit's energy to its outputs; **mass-based and energy-based allocation give similar results**, but **market-value allocation differs** — that difference is the Test-4 result.
- **Processing gain:** cracking dense heavies into lighter products makes Σ product volume > crude volume (~6% US). Volume is a *reporting unit, not conserved* — so it cannot be a split basis (we split by energy). Mass conserves.
- **Two energy channels (the physical-trace test inside the refinery):**
  - **Conversion (measured):** reforming, FCC, hydrocracking, coking, alkylation energy routes to the specific products those units make. Gasoline-pathway units dominate.
  - **Distillation (declared convention):** crude/vacuum distillation heats the whole barrel to separate it — shared, no per-fraction trace. Split by a declared basis (enthalpy-demand or volume), scaled to the *metered actual* (losses included).
- **Representative product prices** (for the revenue/price-allocation contrast): gasoline/diesel/jet are the high-value majority; **residual fuel oil is discounted; petcoke is very cheap** — yet petcoke and converted streams carry real coking/conversion energy, so price allocation under-costs them.

## To do

- [x] ~~Extract DOE bandwidth per-unit energy intensities~~ — **done 2026-08-06** (Table 4-2 above; wired into `refinery_slice.py`).
- [ ] Retrieve Argonne 2011 (69026) and Han et al. ES&T manually for a **published per-product process-energy allocation** — closes the last modelled layer (the conversion routing shares).
- [ ] Materials (crude mass), operating labour (BLS), and product prices (EIA spot) → replace the still-representative non-energy dimensions.
- [ ] Pull exact EIA volume yields per fraction from the yield console (currently standard proportions).

## Related

- `00-strategy/OP-17_coproduct_allocation.md` · `02-research/joint-production-allocation-problem.md` (line 74 closed)
- `06-simulation/allocation-engine/refinery_slice_PLAN.md` · `06-simulation/allocation-engine/refinery_slice.py`
- [[co-product-allocation]] · [[physical-trace-test]] · [[price-equals-cost]]
