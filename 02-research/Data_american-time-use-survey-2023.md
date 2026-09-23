# Data — US hours worked per day, American Time Use Survey 2023

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** data source · **Retrieved:** 2026-09-23

| | |
|---|---|
| **Citation** | U.S. Bureau of Labor Statistics (2024). *American Time Use Survey — 2023 Results*. News release, 27 June 2024. [bls.gov (HTML)](https://www.bls.gov/news.release/archives/atus_06272024.htm) · [PDF](https://www.bls.gov/news.release/archives/atus_06272024.pdf) |
| **Survey home** | [BLS — American Time Use Survey](https://www.bls.gov/tus/) |

## What it says (figures read from the release on 2026-09-23)

| Figure | Value | Table |
|---|--:|---|
| Employed persons | 175,956 thousand | Table 4 |
| Share of employed persons who worked on an average day | **64.7%** | Table 4 |
| … on weekdays / on weekend days | 80.4% / 28.1% | Table 4 |
| Hours worked on days worked, all employed | **7.75 h** | Table 4 |
| Hours worked on days worked, full-time | 8.15 h | Table 4 |
| Working and work-related activities, all persons 15+, average day | **3.56 h** | Table 1 |

**Derived here, not stated in the release:** an employed person's work averaged over **every** day, weekends included, is `0.647 × 7.75 =` **about 5.0 h/day**.

## Why it matters to Aequitas

**`disparity_ceiling_sim.py` draws each worker's daily work from `normal(6.0, 3.0)`, clipped at `24 − F`, with 35% non-workers.** This survey is the nearest source for those settings.

| Setting in the code | What the survey gives | Match |
|---|---|---|
| Worker mean, 6.0 h/day | About 5.0 h/day for the employed, over all days | **About 20% high** |
| Worker spread, 3.0 h | **Not in the release.** It needs the microdata | Unsourced |
| 35% non-workers | Needs the 15+ population total, which the release does not print in the tables read | Unverified |
| **The top tail: people averaging 14 h/day of work every day for life** | **A diary survey records single days. It does not measure a lifetime average**, so it cannot source this at all | **Unsourceable from this survey** |

**The last row is the one that matters.** The rubric's tests 6 and 7 need people at the 24-hour wall. **Foundations §5.5.5 says of `24 ÷ F`: *"It is an extreme, and nobody reaches it"*.** See `06-simulation/ceiling-rubric/README.md`, *Test sources*.

**Used by:** `06-simulation/ceiling-rubric/README.md` and `06-simulation/disparity-ceiling/README.md`, *Test sources*.
