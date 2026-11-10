# The middle fifth — hours behind a near-median life, by country

> **Version:** 0.1
> **Date:** 2026-11-09

**Script:** [`middle_fifth.py`](middle_fifth.py) · 6 self-tests green · run transcript [`MIDDLE_FIFTH_RUN.txt`](MIDDLE_FIFTH_RUN.txt)

## The answer

**In the US the middle fifth of households consumes 0.86 of the average's hours. In the nine European countries measured it consumes 0.89 to 0.99.** European spending is spread far more evenly, so there the average and the median are close.

**Terms used here.**

| Term | What it means |
|---|---|
| **Hours** | Hours of work, anywhere on Earth, behind one person's consumption in a year. Every payer is counted: households, non-profits, and government care and schooling. This is the `AIC_HOURS` column of [`q6_payers.py`](q6_payers.py) |
| **Average** | All of a country's hours divided by its population. A few large consumers pull it up |
| **Middle fifth** | The households from the 40th to the 60th percentile of income. Its spending sits close to the median household's |
| **COICOP division** | One of the 12 standard spending categories used by every national survey: food, housing, transport, health, and so on |
| **Ratio method** | For each division, the middle fifth's spending divided by the average household's, both from the same survey. Currency and units cancel |

## The figures

| Country | Average | **Middle fifth** | Middle ÷ average | Survey year | Share of hours worked abroad |
|---|--:|--:|--:|--:|--:|
| Netherlands | 1,497 | **1,454** | 0.97 | 2020 | 78% |
| Belgium | 1,475 | **1,437** | 0.97 | 2020 | 81% |
| Denmark | 1,437 | **1,284** | 0.89 | 2020 | 72% |
| Great Britain | 1,319 | **1,270** | 0.96 | 2015 | 60% |
| **United States** | **1,283** | **1,104** | **0.86** | 2023 | 47% |
| Norway | 1,239 | **1,227** | 0.99 | 2020 | 62% |
| Finland | 1,138 | **1,118** | 0.98 | 2020 | 60% |
| Sweden | 1,120 | **1,070** | 0.96 | 2015 | 62% |
| France | 1,101 | **1,036** | 0.94 | 2020 | 59% |
| Austria | 1,077 | **1,061** | 0.99 | 2020 | 64% |
| Germany | 1,072 | **1,048** | 0.98 | 2020 | 61% |

*Hours per person per year. EXIOBASE 3, 2022. Sweden and Great Britain have no 2020 survey.*

**In plain words: using the middle fifth lowers the US figure by 14% and most European figures by 1% to 6%.** By the average the US takes 20% more hours than Germany. By the middle fifth it takes 5% more: 1,104 against 1,048.

## How it is computed

**Worked, for the US and Germany.**

| | US (BLS, per household) | Germany (Eurostat, per adult equivalent) |
|---|--:|--:|
| Average household spends | $77,280 | 22,074 PPS |
| Middle fifth spends | $65,487 | 22,162 PPS |
| Middle ÷ average | **0.847** | **1.004** |

**PPS** is the purchasing power standard, Eurostat's common unit for spending across countries. An **adult equivalent** counts a household's second adult as 0.5 and each child as 0.3, so households of different sizes compare. The US middle fifth and the US average both have 2.5 people per household, so the US ratio per household is also the ratio per person.

**The overall ratio is not applied to the total.** It is applied division by division, because the middle fifth spends its money differently from the average, and each division takes a different number of hours per euro. For each country `c` and division `d`:

> **middle-fifth household hours = Σ over d of ( r_cd × H_cd )**

where `r_cd` is the middle fifth's spending on `d` divided by the average household's, and `H_cd` is the household hours per person behind division `d` in EXIOBASE. **Government care and schooling, and non-profits, are held at each country's average**, because they are used about equally across income fifths.

**Worked, for the US.** The US average is 1,283 h, all of it household spending in EXIOBASE. Division by division the middle fifth's ratios run from 0.65 (education) and 0.75 (recreation) to 0.95 (food at home) and 1.02 (communication), and the sum is **1,104 h**, which is 0.86 of the average.

## Why some countries stay high at the median

**The Netherlands and Belgium stay near 1,450 h even for the middle fifth, so a few large consumers do not explain their figure.** What explains it is where the work is done: **78% and 81% of their hours are worked abroad**, against 47% for the US.

| | Spending per person | Hours per €1,000 spent |
|---|--:|--:|
| United States | €49,900 | 25.7 |
| Germany | €30,800 | 34.8 |
| Netherlands | €32,300 | **46.3** |

**In plain words: a euro buys far more hours of work in a low-wage country than in Europe, and the Netherlands and Belgium import much of what they consume.** Hours count every worker's hour as one hour wherever it was worked (A2, time as measure), so money that buys cheap foreign labour shows up as many hours.

## Limits

1. **The middle fifth is near the median, not the median.** It is the 40th to 60th percentile of income, not the 50th percentile of consumption.
2. **Household surveys miss most of the spending of the very rich.** The survey average is therefore too low, and the middle fifth reads closer to it than it is. **The true middle-to-average ratios are lower than printed**, most of all in the US. By how much is not measured.
3. **The survey years do not match.** EXIOBASE is 2022; the US survey is 2023; the European waves are 2015 and 2020. **2020 was a COVID year.** Seven of the eight countries with both waves agree within 4.1%; **Denmark does not** (1,413 h in 2015, 1,284 h in 2020, 10% apart).
4. **The match between EXIOBASE products and COICOP divisions is this script's own**, written out in full in `middle_fifth.py`. Beverages are put with alcohol and tobacco, and "chemicals n.e.c." with household goods; both include some items of other divisions.
5. **These are hours per person of all ages.** The 1,380 h/yr anchor ([`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md)) is per median adult and adds durables and own-pollution remediation, so the two are not on one basis.
6. **One cross-check on the anchor.** Track 1 assumed a median adult consumes **0.80** of the average ([`TRACK1.md`](TRACK1.md)). The measured US middle-fifth ratio is **0.86** in hours and 0.85 in spending. **The anchor has not been recomputed with it.**

## Sources

- **Eurostat, Household Budget Survey:** tables `hbs_exp_t133` (mean consumption expenditure by income quintile) and `hbs_str_t223` (structure of consumption expenditure by income quintile and COICOP), waves 2015 and 2020, downloaded 2026-11-09 through the [Eurostat dissemination API](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/hbs_exp_t133?format=TSV&compressed=false). Overview: [Household budget survey — statistics on consumption expenditure](https://ec.europa.eu/eurostat/statistics-explained/index.php/Household_budget_survey_-_statistics_on_consumption_expenditure).
- **US Bureau of Labor Statistics, Consumer Expenditure Survey, Table 1101:** quintiles of income before taxes, 2023. bls.gov refuses scripted downloads, so the copy is the [Internet Archive's](https://web.archive.org/web/2025/https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-quintiles-before-taxes-2023.xlsx), retrieved 2026-11-09.
- **EXIOBASE 3, 2022, product by product**, as in [`q6_payers.py`](q6_payers.py).

All three survey files are in `06-simulation/data/`, which is not committed.

## Run it

```bash
python middle_fifth.py           # about 3 minutes; writes middle_fifth_result.json
python middle_fifth.py --show    # the table, from the cache
python middle_fifth.py --test    # 6 self-tests
```
