# Data — US hours of childcare by age of youngest household child (ATUS)

> **Version:** 0.1
> **Date:** 2026-11-02

**Type:** data source · **Retrieved:** 2026-11-02 · **Unit:** hours per day, per person aged 18 and over

| | |
|---|---|
| **Citation** | U.S. Bureau of Labor Statistics. *American Time Use Survey*, Table 8A: *Time spent in primary activities for the civilian population 18 years and over by presence and age of youngest household child and sex, 2025 annual averages* |
| **URL** | <https://www.bls.gov/news.release/atus.t08A.htm> |
| **Survey home** | <https://www.bls.gov/tus/> |
| **Reference year** | 2025 annual averages (the other US note in this folder, [`Data_american-time-use-survey-2023.md`](Data_american-time-use-survey-2023.md), is the 2023 release) |
| **Read how** | Fetched through a summarising tool. The tool said the column labels did not extract cleanly and the *Educational activities* row may be misaligned. **Open the page and check the childcare rows before a sim cites them.** |

## Why this matters to Aequitas

The target is **hours**, not money. A parent's hours of childcare are credited work (Foundations §4.5). A sim of the 0.3 child weight (`sr-20261102-single-parent-and-two-adult-yearly-balance-f`) needs those hours by the age of the youngest child. This is the only US table found that gives them.

## What the table says

**Caring for and helping household children**, primary activity, hours per day:

| Group | Everyone | Men | Women |
|---|--:|--:|--:|
| Any household child under 18 | 1.20 | 0.84 | 1.52 |
| **Youngest child under 6** | **2.08** | **1.53** | **2.56** |
| **Youngest child 6 to 17** | **0.61** | **0.38** | **0.81** |

**Caring for and helping household members** (children and adults together):

| Group | Everyone | Men | Women |
|---|--:|--:|--:|
| Any household child under 18 | 1.46 | 1.06 | 1.81 |
| Youngest child under 6 | 2.37 | 1.75 | 2.90 |
| Youngest child 6 to 17 | 0.85 | 0.60 | 1.07 |
| No child under 18 | 0.08 | 0.09 | 0.07 |

## The same figures in hours a year

*Arithmetic: hours a day × 365. Not a BLS figure.*

| Youngest child under 6 | Hours a year |
|---|--:|
| Per adult | 2.08 × 365 = **759** |
| A man | 1.53 × 365 = **558** |
| A woman | 2.56 × 365 = **934** |
| A man and a woman together | **1,492** |

| Youngest child 6 to 17 | Hours a year |
|---|--:|
| Per adult | 0.61 × 365 = **223** |
| A man and a woman together | (0.38 + 0.81) × 365 = **434** |

**In plain words: with a child under 6, a couple spends about 1,490 hours a year on primary childcare. That is nearly three times the 552 h the 0.3 weight gives for the goods a child consumes.** The two numbers measure different things (labour given against goods used), and the labour is credit, not debit.

## What we can use

- A first estimate of the **credit** side for the child request, by two age bands.
- The **men and women split**, which matters for a single parent.

## Limits

- **Primary activity only.** A parent supervising a child while doing something else is not counted. These hours are a floor.
- **Two age bands only.** The request wants 0–4, 5–11 and 12–13. This table cannot split them. The ATUS microdata can, and so can IPUMS ATUS (free registration, <https://www.atusdata.org/>; not checked).
- **The population is adults in households with a child**, not parents. A grandparent or an adult sibling in the same home counts.
- **Single parents are not split out** in this table.
- The *Educational activities* row is mostly suppressed; do not use it.
- Hours are per person-day, averaged over weekdays and weekends.

## Related

[[property-debit]] · [`Data_cross-country-time-use-and-expenditure-sources.md`](Data_cross-country-time-use-and-expenditure-sources.md) · [`Method_oecd-modified-equivalence-scale.md`](Method_oecd-modified-equivalence-scale.md)
