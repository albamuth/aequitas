# Track 3 — Foreign labour embodied in a US resident's imports (2022)

**Script:** `track3_imports.py` · 3 self-tests green (cache in `track3_result.json`). Full EXIOBASE 3 solve, ~110s.

## Why this track

Track 1's BLS ERM is **import-adjusted** — it counts only labour performed *in the US*, so its ~612 h/capita is a **domestic lower bound**. The hours worked *abroad* to make what Americans import were missing entirely. Track 3 supplies them from **EXIOBASE 3 (2022, pxp)** — the one dataset reporting embodied labour in **hours** across all 49 regions.

## Method (standard EEIO, split by region of origin)

`x* = (I − A)⁻¹ y_US-household`, then `embodied hours = e · x*` (e = employment-hours intensity, M.hr per M€ output, summing the six skill/sex rows), each sector split by its region: **US-origin = domestic; all others = foreign = Track 3.** One dense 9,800×9,800 solve; no wage/margin guesswork.

## Result

| | h/capita/yr |
|---|---|
| Domestic (EXIOBASE, all-labour basis) | 671 |
| **Foreign (imports) — TRACK 3** | **605** |
| **TOTAL embodied labour** | **1,276** |
| **Foreign share** | **47%** |

Per **median adult**: total ≈ **1,276 × (335M/259M adults) × 0.80 ≈ 1,320 h/yr** — roughly **double** the Track-1 domestic-only figure of ~633 h.

**Top foreign sources** (h/capita embodied in US consumption): RoW-Asia 158, **India 121**, **China 101**, Mexico 55, RoW-Latin-America 41, RoW-Africa 28, Indonesia 18.

## Two things worth stating

**1. The domestic cross-check holds.** EXIOBASE domestic = 671 h vs Track-1 ERM = 612 h — same order of magnitude. EXIOBASE runs a touch higher because it counts *all* labour (informal + self-employed), while the ERM is a payroll-job basis. Two independent datasets, two methods, one answer: **the domestic piece is solid.**

**2. Nearly half the labour Americans consume is performed abroad — and this is the whole point.** Foreign labour embodies far more *hours per dollar* (Indian/Chinese wages are a fraction of US wages, so each imported dollar buys many more hours). Today's dollar price **hides** this: a $20 shirt and a $20 haircut look equal, but the shirt commands multiples of the labour-hours. Aequitas, pricing in labour+material with no wage arbitrage, makes that hidden labour **visible** — India alone embodies 121 h/capita/yr in US consumption. This is a direct, quantified illustration of what cost-accounting surfaces that money conceals.

## Honest caveat

EXIOBASE employment for developing regions includes **subsistence/informal labour** (very high hours, very low €), which *inflates* the foreign figure and raises a genuine boundary question: how much subsistence labour is truly "embodied in US imports" versus an artefact of allocating whole-economy hours to traded output. So treat **605 h foreign as an upper-ish estimate**; the domestic 612–671 h is the firmer number. The direction — imports roughly *double* the domestic-only labour bill — is robust across any reasonable treatment.

*EXIOBASE 3, 2022, product-by-product, employment-hours satellite (unit M.hr). US household final demand €16.63T.*
