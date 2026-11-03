# Data — India Time Use Survey 2019 (unpaid caregiving hours)

> **Version:** 0.1
> **Date:** 2026-11-02

**Type:** data source (press note read; full report and microdata not reached) · **Retrieved:** 2026-11-02 · **Unit:** minutes per day, persons aged 6 and over

| | |
|---|---|
| **Citation** | National Statistical Office, Ministry of Statistics and Programme Implementation, Government of India. *Press Note on NSS Report: Time Use in India-2019*, 29 September 2020 |
| **URL** | <https://www.mospi.gov.in/sites/default/files/press_release/PRESS%20NOTE%20on%20TUS-%202019.pdf> |
| **Survey home** | <https://microdata.gov.in/NADA/index.php/catalog/223> (reference DDI-IND-CSO-TUS-2019-19). **Refused the connection from this machine on 2026-11-02, twice, on two paths** |
| **Method deck** | NSO presentation, UN workshop, Xi'an, June 2024: <https://unstats.un.org/unsd/demographic-social/meetings/2024/tus-wk-china-2024/10b.%20Time%20Use%20Survey%20in%20India_India_Mr.%20Sandip%20Kumar%20Sadhu.pdf> |
| **Read how** | Downloaded the press note and converted it with `pdftotext`. The tables are in columns, and the layout is clear for the three all-India rows used below |

## What the survey covered

- First all-India time-use survey, January to December 2019.
- 138,799 households (82,897 rural, 55,902 urban). 447,250 persons aged 6 and over.
- Personal interview. A 24-hour recall from 4 AM the day before.
- **The press note counts every activity in a time slot, not only the main one.** So secondary care is inside these numbers.
- Activity coding: ICATUS 2016.

## The figures that bear on childcare

The press note publishes one caregiving row. **It is not childcare alone.** The row is *unpaid caregiving services for household members*, which is ICATUS major division 4. That includes care of children and also care of sick, elderly and disabled adults.

| All-India, rural + urban | Men | Women | Everyone |
|---|--:|--:|--:|
| Share who gave unpaid care in a day (participation) | 14.0% | 27.6% | 20.7% |
| Minutes a day, **per participant** | 76 | 134 | 114 |
| Share of the 1,440-minute day, **per person** | 0.8% | 2.6% | 1.7% |

**Hours a year per person aged 6 and over** (arithmetic: participation × minutes ÷ 60 × 365; not a NSO figure):

| | Men | Women | Everyone |
|---|--:|--:|--:|
| Participation × minutes | 10.6 min/day | 37.0 min/day | 23.6 min/day |
| Hours a year | **65** | **225** | **144** |

The share-of-day row gives the same answer (0.8%, 2.6% and 1.7% of 1,440 minutes are 11.5, 37.4 and 24.5 minutes). The two rows agree to rounding.

**In plain words: the average Indian woman aged 6 or over gives about 225 hours a year to unpaid care, and the average man about 65. Both groups include people with no children at home, so the figure is not the load of a parent.**

## Why this does not yet answer the child question

- **No split by age of youngest child.** The press note groups everyone. A parent with a child under 6 gives far more than the national average, and the note cannot show how much.
- **Childcare is mixed with adult care.** The ICATUS division 41 lines (childcare and instruction) are in the full report and the microdata, which were not reached.
- **The age floor is 6.** A child's own time use is not recorded under that age. That does not matter for parents' hours.
- **No household type.** There is no "couple with child under 6" cell in the press note.

## A wrong turn, recorded so it is not repeated

A PDF named `Report of the Time Use Survey-Final.pdf` on the mospi.gov.in site (<https://www.mospi.gov.in/sites/default/files/publication_reports/Report%20of%20the%20Time%20Use%20Survey-Final.pdf>) is **not the 2019 report**. It is the Ministry's **1998–99 pilot survey**, six states, 18,620 households. It does hold childcare lines, in hours per week, by state and sex. For example *care for children*: women 3.16 and men 0.32 hours a week across the pilot. **That is a different year and a partial country. Do not combine it with the 2019 figures.** It may serve as a rough 1998 comparison, with that label.

## What we can use

- **A check on the scale of unpaid care** in a low-income country: about 144 hours a year per person aged 6 and over, against the US adult figure for any child under 18 of 1.20 hours a day (438 hours a year). The two groups differ and the figures are not paired. The comparison shows only that the Indian figure is the average over all people aged 6 and over.
- **The gender gap:** women's unpaid care time is about 3.5 times men's (225 against 65).

## Next steps

1. Find the **full 2019 report** (the NSO calls it NSS Report on Time Use in India-2019; one source says it runs to about 2,140 pages). It should hold the childcare line, by state and by activity. The mospi.gov.in publication listing did not appear in search. Try the MoSPI site's publication-reports page by hand.
2. **Microdata** (ID DDI-IND-CSO-TUS-2019-19). The portal refuses connections from this machine. Try a different network. Check the access terms before downloading anything.
3. If microdata are reached, build childcare hours from ICATUS division 41, with household members' ages to find the youngest child.

## Related

[[property-debit]] · [`Data_cross-country-time-use-and-expenditure-sources.md`](Data_cross-country-time-use-and-expenditure-sources.md) · [`Data_eurostat-childcare-by-household-type.md`](Data_eurostat-childcare-by-household-type.md) · [`Data_atus-childcare-by-age-of-youngest-child.md`](Data_atus-childcare-by-age-of-youngest-child.md)
