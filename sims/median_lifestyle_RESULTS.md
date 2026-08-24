# Median-Adult Lifestyle Cost — Running Results (bottom-up, v2)

> **Living log.** Updated as each track is computed. Method: [`median_lifestyle_METHOD.md`](median_lifestyle_METHOD.md). Data provenance + BLS-withdrawal note: memory `median-lifestyle-data-sources`, files in `data/`.
> **Question:** how many hours of human work per year does a median US adult's lifestyle command? (The disparity-ceiling proof's real-world anchor.)
> **Year:** 2023 (latest internally-consistent CE + BLS ERM/IO). **Scope so far:** DOMESTIC labour; imports (Track 3) and own-pollution (Track 4) still pending.

---

## Running total — per adult, hours/year

| Track | What | mean adult | median adult |
|---|---:|---:|---:|
| **1** | Consumption flows (all PCE, domestic, full supply chain) | **772** | **641** |
| **2** | Housing construction + improvement (annualised, §6.2b) | **45** | ~45 |
| **3** | Imports — foreign labour embodied **(EXIOBASE, measured)** | **785** | ~650 |
| **4** | Own pollution → remediation labour *(fork: 6–29)* | **~18** | ~18 |
| | **TOTAL — all tracks** | **~1,620** | **~1,350** |

**Bottom line: a median US adult's lifestyle commands ~1,600 hours of human labour per year — roughly 0.9 of one person's full-time work-year — and about half of it (785 h) is performed abroad.** Track 4 (pollution remediation) is a small tail whose range is the carbon-basis fork. *(Mean-adult basis; median scales the consumption-driven parts by ~0.83. Domestic figure cross-validated: EXIOBASE 872 vs BLS 772 per adult.)*

*Mean→median (×0.83) applies mainly to discretionary consumption (Track 1); housing and necessities are more uniform. hours/job = 1,750 throughout.*

---

## Track 1 — consumption flows ✅ [`track1_labour.py`](track1_labour.py)

**Method:** US PCE by commodity (BLS IO final-demand file, 2023, **producer values** — margins pre-allocated) × total (direct+indirect) jobs per $1M (BLS Employment Requirements Matrix, 2023, **domestic/import-adjusted**) × 1,750 h/job.

**Validation:** PCE total = **$18.82T** (exact match to US 2023); PCE-supported jobs = **114M** (≈ 0.68 × 160M US jobs). ✔

**Result:** 199 B hours/yr total US PCE labour →
- per capita 595 · **per adult 772** · per median adult **641** · per household 1,481 h/yr
- sensitivity (hours/job 1,650–1,850): per-adult **728–817**

**Where the hours are** (top drivers — all labour-intensive services):

| Commodity | PCE $B | jobs/$M | B hrs |
|---|---:|---:|---:|
| Hospitals (private) | 1,431 | 6.3 | 15.7 |
| All other retail trade | 1,202 | 7.3 | 15.5 |
| Food & drinking places | 700 | 11.1 | 13.6 |
| Full-service restaurants | 432 | 11.0 | 8.3 |
| Owner-occupied dwellings | 2,232 | 2.0 | 7.8 |
| Offices of physicians | 655 | 6.7 | 7.6 |

Healthcare ~34 B · retail+wholesale ~34 B · food service ~22 B hrs dominate.

**Scope note:** "owner-occupied dwellings" here is the imputed-rent *service* (a return on capital, 2.0 jobs/$M), **not** the construction of the house — that's Track 2.

---

## Track 2 — housing construction (annualised) ✅ [`track2_housing.py`](track2_housing.py)

**Method:** a home's construction labour was spent years ago, so it never shows in this year's PCE. Front-loaded + holding-time-split (§6.2b) → **annualise total build labour over the service life.** The ERM **Construction** total-multiplier (5.8 jobs/$M) already includes lumber/steel/concrete/windows/plumbing/electrical production labour as *indirect* requirements — so applied to **construction cost** (structure, excl land/finance) it *is* the bill-of-materials labour, via IO, no per-material rates invented.

**No double-count with Track 1:** residential construction is *investment*, not PCE.

**Result:** 2,000 sqft @ $160/sqft = $320k structure → **3,237 h total build (~1.8 person-years)** → 54 h/yr annualised over 60 yr + 35 h/yr improvement/repair = **89 h/yr per home**
- **per adult 45** · per person 36 h/yr
- sensitivity (1,600 sqft/80 yr … 2,400 sqft/50 yr): per-adult **32–61**

**Assumptions flagged:** home size 2,000 sqft, $160/sqft, 60-yr life, 2 adults/home, $3,500/yr improvement. An itemised NAHB bill-of-materials (lumber board-ft, concrete cu-yd, steel tons…) is available as a refinement/cross-check if wanted.

---

## Track 3 — imports (foreign labour) ✅ EXIOBASE MEASURED [`track3_exiobase.py`](track3_exiobase.py)

**Method:** consumption-based labour footprint from the **EXIOBASE 3 global MRIO (2022, pxp)**: `x_driven = L @ Y_us_households`; `hours = S_emp · x_driven`; split by origin region. Real foreign supply chains and country-of-origin wages baked in; currency cancels (hours/M.EUR × M.EUR).

**Result:** foreign labour in US household consumption = **202.7 B h/yr → 785 h/adult**. Foreign share **47.4%** of the consumption labour footprint.

**Cross-check (independent validation):** EXIOBASE's *domestic* US portion = 224.9 B h (872/adult) vs Track 1's BLS-based 199 B h (772/adult) — agree within ~13%, two unrelated data sources (EXIOBASE MRIO 2022 vs BLS ERM 2023). ✔

**Top foreign origins (B h/yr):** Rest-of-Asia-Pacific 52.8 · India 40.4 · China 33.9 · Mexico 18.4 · Rest-of-Americas 13.8 · Rest-of-Africa 9.5 · Indonesia 6.0 · Middle East 5.5. **Ultra-low-wage origins (India, rest-of-world) dominate embodied hours** — which is exactly why the earlier macro ballpark (350, band 137–782) undershot: it couldn't weight countries. The measured value (785) sits at the *top* of that band.

*Superseded ballpark: [`track3_imports.py`](track3_imports.py) (kept for the method + the lesson that country-weighting matters). Data year 2022 (1 yr behind the 2023 base — minor, flagged).*

---

## Track 4 — own pollution → remediation labour ✅ [wide fork] [`track4_pollution.py`](track4_pollution.py)

**Scope revision (2026-08-10):** emissions from **real-time, demand-dispatched** production follow the end-user. So the adult bears vehicle fuel, on-site home fuel, **and electricity generation** (non-storable; the draw commands the marginal turbine — the plant is a *tool*, the user *acts*). This aligns electricity with §3.2b's existing treatment of final-delivery transport and personal combustion; the earlier "generation stays with the plant" call was the inconsistent one. **⚠️ Revises the §3.2b electricity clarification — flagged for stress-test + fold into Foundations.** Fuel-supply *labour* is already in Track 1; Track 4 adds only *emissions remediation*.

**Emissions the adult causes:** vehicle 4.6 + home fuel 1.5 + **electricity 2.2** = **8.3 t CO₂/yr** (electricity ~doubles the non-vehicle carbon). Anchors: EPA typical vehicle 4.6 t; EIA residential fuel; eGRID ~0.37 t/MWh × residential electricity.

**Carbon → labour (REAL EEIO intensity, [`track4_carbon_intensity.py`](track4_carbon_intensity.py)):** each method is a basket of BLS sectors with measured ERM multipliers (not the economy-average shortcut). **Nature-based** (forestry-like) = 6.15 jobs/$M → 0.01077 h/$ × $50/t = **0.539 h/t**. **DAC** (energy/capital-heavy, labour-*light*) = 3.81 jobs/$M → 0.00666 h/$ × $500/t = **3.33 h/t** (the shortcut overstated DAC by ~37% — its dollars buy electricity (3.2) and chemicals (1.9), not hands). + wastewater ~1.6 h/yr.

**Result: 6–29 h/adult (mid ~18).** Small next to Tracks 1–3; spread is the nature-vs-DAC carbon basis. *Cost-share splits are the one remaining assumption (DAC cost literature); the multipliers are measured. Implementation note: used **average** grid emission factor; **marginal** (the "turbines spin up" intuition) is a refinement.*

---

## The AVERAGE person (mean, per person) — the "even-distribution" standard

*The mean, pulled up by the wealthy, = the living standard everyone would have under even distribution. Household figures ÷ 2.51 persons. [`average_household.py`](average_household.py) (labour) + [`average_footprint.py`](average_footprint.py) (environment, EXIOBASE 2022).*

**Purchasing power (labour-hours/yr per person):** Track 1 consumption 595 · Track 2 housing 36 · Track 3 imports 605 · Track 4 pollution ~14 → **~1,250 h/yr, 48% foreign.** Per household (×2.51) ~3,135. **Median person ~1,045 → mean/median = 1.20** (consumption is far more even than income, Gini ~0.3 vs ~0.5 — real consumption is naturally bounded, the disparity-ceiling intuition).

**Environmental footprint (what the lifestyle *drives*, per person/yr):** CO₂ 12.4 t (30% foreign) · materials 19 t (59%) · land 2.2 ha (49%) · water 1,600 m³ (57%). *Footprint driven ≠ debit borne:* under §3.2b most stays with producers; the consumer's own debit is ~6.4 t CO₂ direct (Track 4). Energy satellite omitted (empty aggregate row; ≈ reflected in CO₂).

**Two findings:** (1) environmental burden is offshored *more* than labour — 57–59% of materials/water are foreign, vs 48% of labour; CO₂ is the exception (30%, burned at home in cars/heat). (2) **Not globally universalizable:** ~1,250 h/person exceeds the ~800 h/person of labour available worldwide (~3.4 B workers × ~1,900 h ÷ 8.1 B people) by ~1.5× — the American average draws on the rest of the world's hours.

---

## Open items

- **§3.2b electricity revision** → stress-test + fold into Foundations (parked in NEXT.md).
- **Open sub-decisions:** per-adult normalisation (equivalence scale vs single-person CU); mean→median ratio (0.83 placeholder → refine from CE microdata); carbon basis (nature vs DAC).
- **Minor uncounted gap:** foreign content of *residential construction* (Track 2 domestic-only; Track 3 is consumption not investment). Small; noted.
- **Next deliverable:** rewrite the layperson explainer ([`MEDIAN_LIFESTYLE.md`](MEDIAN_LIFESTYLE.md)) from these rigorous numbers, with charts; then this anchors the ρ-sweep sim.
