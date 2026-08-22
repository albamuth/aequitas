# Data — Cross-country labour efficiency of first-world lifestyles

> **Type:** data-source stub · **v0.1** · retrieved 2026-08-17
> **Why it matters:** anchors Q6 — the finding that the US-median material standard is unaffordable *only because of how the US produces it*. Other rich countries deliver comparable material welfare and better wellbeing at 55–65% of the US's embodied labour-hours. Feeds the disparity-ceiling calibration and the "labour is abundant" thesis (Foundations §3.5).

## Sources used

| Source | What it provides | Link | Retrieved |
|---|---|---|---|
| **EXIOBASE 3 (2022, pxp)** | Multi-regional IO table, 49 regions × 200 products, with **employment-hours satellite** (M.hr). The only dataset reporting embodied labour in *hours* across regions. On disk: `06-simulation/data/exiobase/IOT_2022_pxp.zip`. | [exiobase.eu](https://www.exiobase.eu/) | 2026-08-10 |
| **Eurostat — AIC per capita 2022** | Actual Individual Consumption per capita, PPP index (EU27=100). "Material welfare of households." | [ddn-20230620-2](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20230620-2) · dataset `prc_ppp_ind` | 2026-08-17 |
| **OECD — Purchasing Power Parities 2022** | US AIC on comparable basis (~150, EU=100). | [oecd.org PPPs](https://www.oecd.org/en/data/datasets/purchasing-power-parities.html) | 2026-08-17 |
| **World Bank / Our World in Data — life expectancy 2022** | Life expectancy at birth by country (physical wellbeing, money-free). | [ourworldindata.org/life-expectancy](https://ourworldindata.org/life-expectancy) | 2026-08-17 |
| **Our World in Data — energy per capita** | Primary energy/capita (US ~290 GJ vs Germany/France ~150, UK ~110, Switzerland ~100). | [ourworldindata.org/energy](https://ourworldindata.org/energy) | 2026-08-17 |
| **Millward-Hopkins, Steinberger, Rao & Oswald (2020)** | *Providing decent living with minimum energy: A global scenario.* Global Environmental Change 65. Decent living for ~10B at ~40% below current global final energy. | [doi:10.1016/j.gloenvcha.2020.102168](https://doi.org/10.1016/j.gloenvcha.2020.102168) | 2026-08-17 |
| **Oswald, Owen & Steinberger (2020)** | *Large inequality in international and intranational energy footprints.* Nature Energy. | doi:10.1038/s41560-020-0579-8 | 2026-08-17 |

## Headline numbers extracted (2022)

- **Embodied labour h/capita/yr** (EXIOBASE household consumption, domestic+imported): US 1,283 · UK 1,007 · Japan 862 · France 856 · Sweden 832 · Germany 820 · Italy 767 · Spain 709.
- **Life expectancy:** US 77.4 vs Spain 83.2, Japan 84.0, Italy 83.0, France 82.3, Sweden 83.0.
- **AIC (EU=100):** US ~150, Germany 119, France/UK 113, Sweden 111, Japan 108, Italy 99, Spain 91.

## Caveats (see Q6.md for full treatment)

- EXIOBASE gives **mean** per capita, not median (US more unequal → looks even worse on median).
- AIC is monetary/PPP (price-level distorted); life expectancy is the money-free axis.
- Small open economies (IE, NL, BE, CH, DK) inflated by transit/transfer-pricing — excluded from the affluent ranking.
- **EXIOBASE 2022 energy satellite is empty (all zeros)** in this vintage — energy figures are from OWID/literature, not EXIOBASE. CO₂ via the air-emissions satellite (populated) is an easy follow-up.

*Consuming docs: `06-simulation/Q6.md`, `track6_country_labour.py`, `track6_efficiency.py`.*
