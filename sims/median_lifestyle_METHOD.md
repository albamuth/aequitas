# Method Plan — Work-Hours to Support a Median US Adult (v2, bottom-up)

**Status:** PROPOSED — awaiting approval before any data-gathering or coding.
**Supersedes the method in** [`median_lifestyle.py`](median_lifestyle.py) / [`MEDIAN_LIFESTYLE.md`](MEDIAN_LIFESTYLE.md) (top-down v1), which was rejected as unsound: it *assumes* the labour allocation, misses carried-forward labour in durables, and mixed data years. v1 is kept only as a rough sanity bracket.

**Goal (one line):** estimate the total human work-hours per year embodied in the consumption of a **median US *adult*** (not per-capita), for one **internally-consistent year**, built up **category by category**, plus the labour to remediate that adult's **own** pollution.

---

## Design rules (from the critique)

1. **Bottom-up, per category** — never a single blanket labour/dollar ratio.
2. **Each category converts by its *best* route** — money→hours for flows, physical embodied-labour for durables, wage/margin for imports.
3. **Measured supply chains, not assumed** — indirect labour comes from an input-output employment matrix, not a guess about where spending goes.
4. **Carried-forward labour is counted** — durables annualised over service life (= Aequitas §6.2b holding-time share).
5. **One year, stated** — pin the latest year where all sources coexist; disclose any extrapolation. No mixing 2025 hours with 2026 GDP.
6. **Per median adult** — normalise CE Survey consumer-unit figures to one adult.

---

## The four tracks

### Track 1 — Everyday flows (food, household energy, communications, entertainment, personal services, most healthcare)
- **Dollars by category:** BLS **Consumer Expenditure Survey** (CE), median, pinned year.
- **Dollars → hours:** BLS **Employment Requirements Matrix** (ERM, Employment Projections program) — total (direct **+ indirect**) jobs per \$1M of final demand by industry; convert jobs→hours with BLS average weekly hours by industry. Anchored in BEA input-output tables, so it captures the *whole* domestic supply chain.
- **Output:** hours embodied per category, summed.

### Track 2 — Durables (housing structure, vehicles, appliances, furniture) — **physical, annualised**
- **Do NOT** convert housing/vehicle dollars (mostly land, finance, interest — near-zero labour).
- **Per item:** embodied construction/manufacturing **labour-hours ÷ service life**, + annual maintenance hours.
  - Housing: build-hours per dwelling ÷ ~60 yr, scaled to median dwelling size / occupancy → per adult.
  - Vehicles: assembly + parts labour-hours per vehicle ÷ ~15 yr, × vehicles per adult.
  - Appliances/furniture: manufacturing hours ÷ service life.
- **Basis for build-hours:** construction-sector labour-hours per dwelling (NAHB / Census construction stats) and auto-manufacturing labour-hours per vehicle (industry/BLS). Cross-check against the ERM construction & motor-vehicle rows.

### Track 3 — Imports (clothing, consumer electronics, etc.)
- **Wage/margin decomposition:** retail price → strip brand/retail markup → factory-gate cost → labour share → **÷ local wage = manufacturing hours per item**.
- **Inputs:** overseas garment/electronics wages (ILO / national statistics), typical labour cost share, and apparel retail markup studies.
- **Cross-checks:** garment-industry "Standard Allowed Minutes" per item; EXIOBASE foreign employment-hours per sector if/when the full dataset is loaded.

### Track 4 — The adult's own pollution → remediation labour (bucket-2 debit)
- **Gasoline:** miles/yr → gallons → tons CO₂ (EPA factors) → **labour-hours to sequester**, = tons × (labour-hours per ton sequestered).
- **Wastewater:** gallons/yr → **labour-hours to treat**, from municipal utility staffing-per-volume benchmarks.
- **Note:** upstream production pollution is excluded (Foundations §3.2b — permanent on the producer). Electricity's generation pollution stays with the power plant; the adult carries only electricity's labour+material (already in Track 1).

---

## Two categories that need special care (flagged, not assumed away)

| Category | Why the naive route fails | Treatment |
|---|---|---|
| **Housing** | Dollars are land + mortgage interest + finance — almost no labour. | Track 2 physical embodied labour only. |
| **Healthcare** | US dollars are inflated by admin/margin, so hours/\$ *understates* real care labour. | Prefer physical (staff-hours per visit/procedure, NAMCS/AHA data); use ERM health row only as a floor. |

---

## Open decisions (need your call before/at execution)

1. **Carbon-remediation basis (Track 4) — big swing.** Labour-hours per ton CO₂ depends entirely on *which* remediation counts as restoring baseline (Foundations §3.3):
   - **Nature-based** (afforestation/soil): cheap, **low labour/ton**.
   - **Engineered Direct Air Capture**: expensive, **high labour/ton** (but the defensible "true cost to undo").
   - This is genuinely an Aequitas §3.3 baseline question, not just a data pick. Recommend we compute **both** and report a range, rather than choose one.
2. **Pinned data year.** Latest fully-consistent set is likely **2023** (CE Survey + ERM + EPA all exist; ERM lags). Confirm 2023, or accept partial extrapolation to force 2024/2025?
3. **Scope of "support a median adult":** consumption only, or also the adult's *share* of collective goods (roads, defence, public services)? v1 was consumption-only. Recommend **start consumption-only**, add collective share as a labelled second layer.

---

## Execution sequence (once approved)

1. **Pin sources + year**, verify every URL and table live (the v1 BEA mis-link must not recur) → a small `sources.md` with exact citations.
2. **Track 1** — CE median category dollars × ERM hours/dollar. Build `median_adult_bottomup.py` with a category table.
3. **Track 2** — durables embodied-labour annualisation.
4. **Track 3** — import wage/margin module.
5. **Track 4** — pollution → remediation labour (both carbon bases).
6. **Assemble + sensitivity** — total hours/yr per median adult, with a per-category chart and a tornado chart of the biggest assumptions.
7. **Sanity-bracket** against the v1 top-down range (~470–750 h labour) and explain any divergence — the durables + import additions should push it **up**.
8. **Rewrite** MEDIAN_LIFESTYLE.md for a layperson from the sound numbers.

---

## What we expect to change vs v1

- **Number goes up.** v1's ~470–750 h counted only *current-year* production labour and a blanket consumption share. Adding durables' carried-forward labour and full import labour should raise it — possibly substantially for housing.
- **The disparity-ceiling logic is unaffected.** The 24/F ceiling argument (Foundations §7.5) does not depend on this number; this only calibrates *where the median sits* inside the band. So getting it right sharpens the comparison without risking the headline result.

---

*Tracks Foundations v0.9 (§6.2b holding-time durables, §3.2b pollution stays with producer, §3.3 remediation baseline, §7.5 the 24/F ceiling). Companion scripts to be built on approval.*
