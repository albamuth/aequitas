# Median lifestyle — results

> **Read this instead of re-running.** From the track `--test` runs, last verified 2026-08-24.
> This is the summary layer. The originals are kept in full beside it: [`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md) (the assembly), [`TRACK1.md`](TRACK1.md), [`TRACK3.md`](TRACK3.md), [`TRACK4.md`](TRACK4.md), [`Q6.md`](Q6.md), and the running log [`median_lifestyle_RESULTS.md`](median_lifestyle_RESULTS.md).

---

## The headline

> **A median US adult's yearly consumption embodies about 1,350–1,400 hours of human labour.**

Set that against the **≈ 3,650 hours a year** every person earns simply by being alive, at a 10-hour self-care floor:

> **The median lifestyle commands about one third of one person's annual credit.**

**That is the anchor under the whole disparity argument.** The median sits far below the ceiling, and labour turns out to be abundant rather than scarce.

## Where the hours are

| Track | What | Hours per adult per year |
|---|---|---|
| 1 | Domestic embodied labour | **612** per capita (**772** per adult on the payroll basis) |
| 2 | Housing structure, annualised | **45** (range 31–61) |
| 3 | Foreign labour in imports | **≈ 47%** of the total; domestic cross-check 671 h against track 1's 612 h |
| 4 | Remediating own pollution | **6–29** (mid ≈ 18) |
| | **Total** | **≈ 1,350–1,400** |

**Track 4 is small and that is the finding, not a gap.** Only pollution a person causes by their own action counts — the fuel they burn, the gas in their furnace, their rubbish. Everything upstream stays permanently on the producer.

**Track 2 is almost entirely housing.** Vehicles, furniture and appliances are already inside tracks 1 and 3, because in a rough steady state the annual purchase of a durable equals the annualised labour of holding it. Counting them again would double-count. **The one durable genuinely missing is the housing structure**, because residential construction is booked as investment rather than consumption — which is exactly why track 1 reported construction at zero hours.

## Where the hours sit, by category

Top three buckets: **healthcare, food and alcohol, housing.** Healthcare alone is **131 hours** against **7 hours** for energy and fuels.

> **Labour is in services, not in stuff.** That single comparison reshapes what "an expensive lifestyle" means.

## Q6 — the American way of producing it is the expensive part

Embodied labour hours per person per year in household consumption, from EXIOBASE 3 (2022), domestic plus imported:

| Country | Hours per person | Life expectancy 2022 | Hours per life-year |
|---|---|---|---|
| **US** | **1,283** | 77.4 | **16.6** |
| UK | 1,007 | 80.4 | 12.5 |
| **Spain** | **709** | **83.2** | — |

> **Spain delivers a comparable material life on 709 hours against the US's 1,283 — and Spaniards live nearly six years longer.**

The US also sits **below the median** on material consumption per hour worked (117 against a median of 132). The hypothesis that the US-median standard looks unaffordable mainly because of *how* America produces it **holds, hard.**

## What would falsify this

- Track 1 and track 3 disagreeing by more than an order of magnitude on the domestic figure. They do not: 612 against 671, on two different bases.
- The category breakdown failing to sum to the total. It does sum — the partition covers all 176 sectors.
- Track 2 turning out large. If housing were a big number, the double-counting argument would need rechecking.
- Any rich country delivering a comparable life on hours close to the US figure. Spain and the UK both undercut it substantially.

## The method's own limits

- **All figures are US-2023, one internally consistent year.** Tracks 3 and 6 use 2022 EXIOBASE, the latest available.
- **Track 1's source is import-adjusted**, so its 612 hours is a domestic **lower bound** by construction. Track 3 supplies the rest.
- **The bases differ between tracks.** Track 1 counts payroll hours; EXIOBASE counts all labour including the self-employed. The two are the same order, which is the check, not the same number.
- **The v1 top-down estimate in [`archive/`](archive/) is not a result.** It assumed the labour allocation instead of measuring it. It is kept only as a sanity bracket, and the two methods do agree in magnitude.

## Figures

| File | Shows |
|---|---|
| `figA_breakdown.png` | The four-track total, domestic against foreign |
| `figB_domestic.png` | Where the domestic hours are, by sector group |
| `figC_foreign.png` | Which countries the offshore hours are in |
| `figD_average.png` | Mean against median |

Three older figures from the superseded v1 estimate are in [`archive/`](archive/).
