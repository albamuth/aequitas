# Track 4 — Labour to remediate the adult's OWN pollution (bucket-2 debit)

**Script:** [`track4_pollution.py`](track4_pollution.py) · 5 self-tests green.

## Scope (Foundations v0.15 §3.2b)

Only pollution the consumer causes by their **own action** — everything upstream stays permanently on the producer (§3.2b), and Track 1 already carries the goods' labour+material:

| Source | CO₂ (per capita/yr) | Why it's the consumer's |
|---|---|---|
| Vehicle fuel | 3.0 t | they burn it (driver acts) |
| On-site home gas | 1.0 t | they burn it (occupant acts) |
| **Residential electricity** | **1.7 t** | **real-time dispatch — §3.2b** |
| **Own CO₂ total** | **5.7 t** | |

Plus wastewater (~30 kgal) and MSW (811 kg) → **treatment** labour.

### ⚠️ Axiom-vs-method-doc discrepancy — FLAGGED

`median_lifestyle_METHOD.md` (written against Foundations **v0.9**) says *exclude electricity* — "generation stays with the plant." Foundations **v0.15 §3.2b real-time-dispatch** **reversed** this: non-storable, demand-dispatched electricity is generated the instant it's drawn, so the emission is the **end-user's** (same logic as a car tailpipe). This script follows the current axiom and **includes** residential electricity (+1.7 t, +42% on the own-CO₂). The method doc should be updated on this point. `INCLUDE_ELECTRICITY=False` reproduces the stale figure (4.0 t).

## Result

| Remediation basis (§3.3 open choice) | labour h/capita/yr |
|---|---|
| Nature-based (afforestation, $15–50/t) | **0.8 – 2.6** |
| Engineered DAC ($250–600/t) | **12.8 – 30.8** |
| Wastewater + MSW treatment | 0.003 (negligible) |
| **Track-4 range (per capita)** | **~0.8 – 31 h/yr** |
| **Track-4 range (median adult)** | **~0.8 – 32 h/yr** |

Cost→labour via an economy-average bridge (0.009 h/$; = ~5 jobs/$1M × 1,800 h, the ERM Level-1 ballpark, matching Q3 plastic's 0.010 h/$).

## What it means

- **Own-pollution remediation is a SMALL labour add** — even at the DAC high end, ~31 h/yr against the ~1,276 h/capita of Tracks 1+3 (≤2.5%). Under nature-based restoration it's ~1 h/yr, a rounding error.
- **The carbon-basis choice swings it ~14×** — the single biggest lever here, and it's the genuine §3.3 baseline question, not a data gap. Reported as a range by design.
- **The real environmental debit isn't this flow-remediation — it's the near-PERMANENT stock kind** (Q3: microplastics, landfill) that *no* scalable remediation retires and that sits near-permanently on the last holder (§3.3, §3.6). Track 4 is the cheap, reversible half; Q3 is the expensive, irreversible half.

*Constants are per-capita US 2022–23 aggregates, documented in-script and overridable. The absolute hours are basis-dependent; the finding — own-pollution remediation is minor vs embodied-goods labour — is robust.*
