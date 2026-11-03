# Data — European childcare hours by household type (Eurostat, HETUS aggregates)

> **Version:** 0.1
> **Date:** 2026-11-02

**Type:** data source · **Retrieved:** 2026-11-02 · **Unit:** hours per day, average over **everyone** in the group (not only those who did childcare), main activity only

| | |
|---|---|
| **Citation** | Eurostat. Dataset `tus_00hhstatus`: *Time spent, participation time and participation rate in the main activity by sex and household composition (2000 and 2010)*. Last updated 2024-03-22 |
| **URL (data browser)** | <https://ec.europa.eu/eurostat/databrowser/view/tus_00hhstatus/default/table?lang=en> |
| **URL (the pull used)** | <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tus_00hhstatus?lang=en&format=JSON> |
| **Local copy** | [`files/hetus_childcare_by_household_type_2000_2010.csv`](files/hetus_childcare_by_household_type_2000_2010.csv): the childcare rows only, 19 countries, 2000 and 2010, men and women |
| **Read how** | Downloaded the full JSON through Eurostat's public API and parsed it with Python. Values are shown by Eurostat in hh:mm and converted here to hours. **No application or account was needed.** |

## Why this matters to Aequitas

The target is **hours**. A parent's childcare hours are credit (Foundations §4.5). The child sim (`sr-20261102-single-parent-and-two-adult-yearly-balance-f`) needs those hours by age band. This is the European source that needs no application. The restricted HETUS files add nothing on child age ([`Data_hetus-2010-variables-and-access.md`](Data_hetus-2010-variables-and-access.md)).

## What the table holds

- **Household types used:** `CPL_CH6` (person in a couple, youngest child under 6), `CPL_CH7-17` (person in a couple, youngest child 7 to 17), `P1_CH18` (single parent, youngest child under 18). Nine more types hold no child under 18.
- **Activities used:** `AC38A` childcare except teaching, reading and talking; `AC38B` teaching, reading and talking with the child; `AC938` transporting a child (travel, listed apart).
- **Years:** 2000 and 2010. **Countries:** 19, but Bulgaria, Latvia, Lithuania and Slovenia have no childcare figures in the household-type cells.
- **Childcare hours below = `AC38A` + `AC38B`.** Transporting a child is not included.

## Childcare hours per day, 2010

Per person aged 10 and over in the group. M is men, F is women.

| Country | Couple, youngest under 6 — M | F | Couple, youngest 7–17 — M | F | Single parent, youngest under 18 — M | F |
|---|--:|--:|--:|--:|--:|--:|
| Belgium | 1.12 | 2.20 | 0.23 | 0.55 | 0.43 | 1.02 |
| Germany | 1.18 | 2.40 | 0.30 | 0.63 | 0.67 | 1.15 |
| Estonia | 1.10 | 2.85 | 0.18 | 0.42 | 0.22 | 1.40 |
| Greece | 1.40 | 3.05 | 0.50 | 0.67 | 1.70 | 0.97 |
| Spain | 1.48 | 2.75 | 0.38 | 0.70 | 0.23 | 1.22 |
| France | 0.93 | 2.07 | 0.23 | 0.60 | 0.42 | 1.00 |
| Italy | 1.00 | 2.42 | 0.28 | 0.65 | 0.72 | 1.18 |
| Hungary | 1.50 | 3.65 | 0.43 | 0.82 | 0.15 | 1.33 |
| Austria | 1.55 | 3.12 | 0.33 | 0.73 | 0.65 | 1.73 |
| Poland | 1.55 | 3.33 | 0.30 | 0.63 | 0.70 | 1.78 |
| Romania | 0.92 | 2.55 | 0.15 | 0.35 | 0.62 | 1.18 |
| Finland | 1.38 | 2.82 | 0.18 | 0.30 | 0.18 | 1.42 |
| Norway | 1.52 | 2.50 | 0.23 | 0.45 | 0.60 | 1.17 |
| United Kingdom | 1.18 | 2.60 | 0.18 | 0.40 | 1.02 | 1.33 |
| Serbia | 1.18 | 2.83 | 0.18 | 0.52 | 1.17 | 1.45 |

**Single-parent men are few.** The cell holds a small sample in each country, and Greece (1.70 for men) is an outlier. Use the women's column for a single parent.

## The same figures in hours a year

*Arithmetic: hours a day × 365, then the middle value across the 15 countries. Not a Eurostat figure.*

| Group | Middle value, h/day | Range, h/day | Hours a year |
|---|--:|---|--:|
| **Couple, youngest under 6** (man + woman) | **4.02** | 3.00 (France) to 5.15 (Hungary) | **1,466** |
| **Couple, youngest 7–17** (man + woman) | **0.83** | 0.48 (Finland) to 1.25 (Hungary) | **304** |
| **Single parent, youngest under 18** (women) | **1.22** | — | **446** |
| Single parent (men) | 0.62 | — | 226 |

**Next to the US (ATUS Table 8A, [`Data_atus-childcare-by-age-of-youngest-child.md`](Data_atus-childcare-by-age-of-youngest-child.md)):** a US couple with the youngest under 6 gives 1,492 h a year, and the European middle is 1,466. The two agree. For the older band the US figure is 434 h (youngest 6 to 17, any adult in the home) and the European middle is 304 h (couples only, youngest 7 to 17).

**In plain words: a couple with a child under 6 spends about 1,470 hours a year on primary childcare in both Europe and the US. That is about 2.7 times the 552 h the 0.3 weight gives for the goods a child consumes. The labour is credit, and the 552 h is debit, so the two do not net directly.**

## What the numbers say about the 0.3 weight

This is arithmetic on what is on the table, and not yet a result:

- A child under 6 draws 1,470 h of parental credit a year in a couple home. The 0.3 weight sets the child's goods at 552 h of debit. The ratio of credit to debit is about 2.7 to 1 at that age.
- For a child 7 to 17 the parents give about 300 h (Europe) or 430 h (US), against the same 552 h of goods debit. The ratio is about 0.5 to 0.8.
- **These ages are not the same weight.** A flat 0.3 for ages 0–13 hides the fact that care hours fall by about four-fifths between the two bands while the goods side moves less. See [`Method_oecd-modified-equivalence-scale.md`](Method_oecd-modified-equivalence-scale.md).

## Limits

- **Main activity only.** A parent watching a child while cooking is not counted. These hours are a floor. The restricted files hold secondary activity and "with a child up to 9" ticks, and this public table does not.
- **Mean over all members of the group**, not only those who gave care. A couple's two columns can be added for hours per household, but only if both partners are in the same cell. Not checked.
- **Two age bands.** Under 6, and 7 to 17. A child aged exactly 6 falls in neither label (the table's band names skip age 6). The codebook labels the same groups "0–6" and "7–17", so the break is probably at 7 and the label "under 6" is loose. **Not confirmed.**
- **Household types, not parents.** The group contains the child's parents, and step-parents or other adults living with the child.
- **Single-parent men are a small sample.**
- **Old data.** The survey waves ran 2000 and 2010. The table was updated in 2024 and holds no 2020 round.
- **Hungary and Poland are high; France and Romania are low.** The spread comes from method differences as well as from real differences, and the codebook does not separate the two.
- **No purchased care.** Hours of formal childcare and school are not in this table.

## Related

[[property-debit]] · [`Data_hetus-2010-variables-and-access.md`](Data_hetus-2010-variables-and-access.md) · [`Data_cross-country-time-use-and-expenditure-sources.md`](Data_cross-country-time-use-and-expenditure-sources.md) · [`Data_atus-childcare-by-age-of-youngest-child.md`](Data_atus-childcare-by-age-of-youngest-child.md)
