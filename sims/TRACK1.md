# Track 1 — Domestic embodied labour in a median US adult's consumption (2023)

**Script:** `track1_embodied_hours.py` · 5 self-tests green.
**Supersedes** the top-down `median_lifestyle.py` (which *assumed* the labour allocation). Here the allocation is **measured** from published supply chains.

## Headline

| Figure | Value |
|---|---|
| PCE total (check) | **$18.82T** = actual 2023 US PCE ✓ |
| PCE-embodied jobs (direct+indirect) | **113.9 M** (US total ~161M; PCE ~68% of GDP ✓) |
| Mean embodied labour | **612 h / capita / yr** |
| Mean per adult | **791 h / adult / yr** |
| **Median adult (×0.80)** | **≈ 633 h / yr** ← Track-1 anchor |

**This is a DOMESTIC lower bound.** The BLS ERM is import-adjusted (US labour only), so the foreign hours embodied in imports (apparel, electronics) are **Track 3** and add on top. **Track 3 is now done ([TRACK3.md](TRACK3.md)): foreign labour ≈ 605 h/capita, so the combined total ≈ 1,276 h/capita ≈ 1,320 h/median adult/yr — imports roughly double the domestic figure.**

## Method (rigorous, no blanket ratio)

`hours_i = PCE_i[$M] × ERM_colsum_i[thousand-jobs/$M] × 1000 × 1800 h/job`, summed over 176 commodities, ÷ population.

- **ERM 2023** (`data/erm_full/NOMINAL_DOMEMPREQ_2023.csv`, 176×176): column-sum = total direct+indirect domestic jobs per $1M of that commodity's final demand.
- **PCE producer-value vector** (`data/io/NOMINAL_FDAGG.xlsx` sheet 2023, col 1): the actual 2023 composition of personal consumption in producer values — trade/transport **margins already reallocated to the retail/wholesale/transport rows**, so retail labour is counted where it happens (no margin lost, the v1 worry).
- jobs→hours via **1,800 h/job-year** (OECD US ~1,811); per-sector avg-hours refinement flagged.

## Where the hours sit (per-capita h/yr)

Labour concentrates in **labour-intensive services**, exactly as the cost-not-value model predicts — *not* in fuels or materials:

| Group | h/cap |
|---|---|
| Wholesale & retail trade | 132 |
| Healthcare | 131 |
| Other services & government | 118 |
| Arts, recreation, food service, hotels | 49 |
| Information & communications | 42 |
| Professional & business services | 34 |
| Education | 31 |
| Food & agriculture | 20 |
| Other manufacturing | 18 |
| Transport & warehousing | 14 |
| Apparel & leather (mfg, domestic) | 8 |
| Energy & fuels | 7 |
| Finance, insurance, real estate | 5 |
| Vehicles & transport equip (mfg) | 2 |
| Construction | 0 |

Top single commodities: private hospitals (48h), retail (47h), food & drinking places (42h + 26h full-service), owner-occupied dwellings' real-estate labour (24h), physicians' offices (24h).

**Construction ≈ 0 and Energy ≈ 7** confirm the method's housing/fuel warning: residential structure labour is investment, not PCE (→ **Track 2** durables via the §6.2b holding-time split), and fuel is near-zero-labour by the barrel. Apparel is low **because it's imported** (→ Track 3).

## By CE-comparable category (the 132-detail bridge)

**Script:** `track1_by_category.py` · 3 self-tests green · reproduces the 612h aggregate exactly. Uses `NOMINAL_FD.xlsx` (176 commodities × 132 detail final-demand categories, PCE = cols 1–79), extracted on disk from `data/io_full.zip → IONom/` — **no Wayback re-pull needed.** Trade/transport margins (51h) reallocated to goods buckets by goods-dollar share.

| CE category | embodied h/cap | CE 2023 $ (mean/CU) |
|---|---|---|
| Healthcare | **145** | $6,159 |
| Food & alcohol | 113 | $9,985 |
| Housing (shelter+utils+ops) | 76 | $25,436 |
| Entertainment & recreation | 65 | $3,635 |
| Personal care & services | 54 | $950+ |
| Transportation | 45 | $13,174 |
| Tobacco, reading, misc | 40 | ~$1,900 |
| Apparel & footwear | 28 | $2,041 |
| Financial & insurance | 20 | (in pensions/ins) |
| Education | 20 | $1,656 |
| Communications | 6 | (in housing/ent) |

**The dollar↔labour mismatch is the headline lesson, and it vindicates cost≠value.** Housing has the **largest CE dollar bill ($25k) but only 76 embodied hours** — most housing "cost" is rent / imputed rent / finance, a *transfer*, not labour (Foundations A1: financial claims carry no debit). Transportation is the same: big dollars, modest labour (fuel + vehicles are low-labour-per-dollar). **Healthcare inverts it** — moderate dollars, the *most* embodied labour, because care is people. Under Aequitas, the price *is* the labour+material — so the categories that look expensive today (housing, finance) get radically cheaper, and labour-borne services (care, food prep) are costed honestly.

## How this sits against the disparity ceiling (Foundations §7.5)

The median adult commands **~633 h/yr of others' domestic labour** — well under the **self-care credit every human earns (~10 h/day → 3,650 h/yr)**. So the **labour dimension never binds** a consumption ceiling: labour is abundant (the Q1/Q5 result). Where the rich diverge is the **material/energy** dimensions of the debit vector, not labour-time. This calibrates *where the median sits inside the 24/F band* without touching the headline ceiling result.

## Honest limits / next

- **Domestic only** — Track 3 (imports) adds foreign hours; expect the total to rise, most in apparel/electronics.
- **Track 2 durables** are inside PCE at producer value here, but *not* re-annualised over service life (§6.2b holding-time). A refinement, not a gap.
- **Track 4** (own-pollution → remediation labour) still to build.
- **Per-category CE breakdown** (the 132-PCE bridge) needs re-pulling `NOMINAL_FD.xlsx` from Wayback; the commodity-group breakdown above is the on-disk substitute and is arguably cleaner (producer-side, margin-correct).
- `1800 h/job` and `median/mean 0.80` are the two biggest single-number assumptions; both refinable and flagged.

*Tracks Foundations v0.15 (§6.2b, §3.2b, §7.5). Data year 2023 throughout.*
