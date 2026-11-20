# Data: waste by sector

**Version:** 0.2
**Type:** dataset note (the input table that a simulation reads)
**Author(s):** project note
**Retrieved:** 2026-11-19
**Read:** the eight detail notes named in the table. Each says which sources its writer opened.
**Local copy:** none

## Why this matters to Aequitas

*(Author, 2026-11-19: "The wastefulness of each sector must be the basis of a new sim for calculating what values of rho are plausible.")* Rho is the tolerance: the share of a person's counted hours that their consumption may reach. Every tolerance in Foundations section 5.5.3 is measured at a method that includes today's waste. This note holds the inputs for a run that takes the waste out. The design of the run is in [Problem_artificial-scarcity.md](Problem_artificial-scarcity.md).

## The rule for a row

- **A row is a share of one sector's hours that are waste, with a low and a high value.**
- **Every row has a published source.** A sector with no source runs at 0, and the run lists it.
- **Each row has a class.** A: a product or a service that was made and did no good. B: work that exists only because of money. C: spending that is a choice about the standard of living. D: people who want work and have none.
- **The rows are written before the run.** Nobody changes a row after seeing a result.
- **A low value is what the sources measure. A high value is the most that a source supports.** Where a share is the judgement of the note's writer, the row says so.

## The input table

| Class | Sector | Low | High | A share of what | Detail note | How firm |
|---|---|--:|--:|---|---|---|
| A | Food | 14% | 29% | The hours behind US food | [Data_waste-food.md](Data_waste-food.md) | Two agencies, opened. The saving shown in practice is far smaller: about 4% |
| A | Goods that fail or date early: cars, furnishings, appliances, clothing | 2% | 21% | US spending on those goods. In hours: about 3.5 to 38 of 1,380 | [Data_waste-product-lifetimes.md](Data_waste-product-lifetimes.md) | The low is measured. The high assumes every good reaches its design life |
| A | Clothing destroyed before use | 4% | 9% | Clothing made, European Union, 2020 | [Data_waste-unsold-goods-and-empty-buildings.md](Data_waste-unsold-goods-and-empty-buildings.md) | One agency, opened. No US figure |
| A | Housing that is empty and usable, beyond normal turnover | 0.8% | 1.5% | US housing stock, 2024 | The same note | The writer's own sorting of census tables. A case for 0 exists |
| A | Health care that did no good | 2% | 9% | The 218 health-care hours: 4 to 19 hours | [Data_waste-health-care.md](Data_waste-health-care.md) | One paper, abstract only. Dollars, taken as hours |
| B | Lending, insurance, property dealing, billing, selling and other money-only work | 5.3% | 12.4% | All US jobs. In hours: 73 to 171 of 1,380 | [Data_waste-money-only-work.md](Data_waste-money-only-work.md) | The job counts are opened tables. **The split into money-only and needed is the writer's judgement** |
| B | The same, after a network's own record-keepers are added back | 4.5% | 12.4% | All US jobs | The same note | Every add-back is a stand-in |
| B | Billing and insurance work in health care | 4% | 15% | The 218 health-care hours: 8 to 33 hours | [Data_waste-health-care.md](Data_waste-health-care.md) | **Inside the row above. Do not add** |
| C | Armed forces and the work that supplies them | 1.5% | 2.9% | The US labour force, 2025 | [Data_waste-armed-forces-and-top-consumption.md](Data_waste-armed-forces-and-top-consumption.md) | Head counts from a reprint. No official count of supplier jobs |
| C | Consumption of the top two fifths above the middle fifth | 16.8% | 27.7% | US consumer spending, 2025 | The same note | Opened survey tables. Money, not hours. The survey misses much spending by the very rich |
| D | People who want work and have none, and part-timers who want full time | 1.3% | 9.6% | Hours worked in the US, 2025. In 2010: 8.0% to 18.2% | [Data_waste-idle-capacity.md](Data_waste-idle-capacity.md) | Opened tables |
| D | Jobs that employers' power over wages keeps from existing | 0.8% | 22.5% | US employment | [Data_waste-labour-idle-by-market-power.md](Data_waste-labour-idle-by-market-power.md) | One model. **Inside the row above. Do not add** |
| D | Unemployment held above its lowest level | 1.0% | 3.2% | Hours worked in the US | The same note | Derived from a published rate. **Inside the first D row. Do not add** |

## Five rules against counting twice

1. **Health-care billing is inside money-only work.** Use one of the two rows.
2. **The health-care rows are inside the peer-country cut.** The project's own note on health hours cuts care from 180 to 103 hours by comparing with peer countries. A run that applies that cut and these rows counts the same hours twice.
3. **The gap between the US and Germany holds some of class B.** Lending and insurance are 4.17% of US jobs and 2.36% of German employment.
4. **On food there is no gap between the US and Germany to count twice.** By one source the US wastes about 123 kg a person a year, and Germany 129 to 131.
5. **Class D is inside the project's own band of hours.** That band treats every person who takes part as a person at work. Class D fixes one point inside the band. It is never added to the band.

## A first look, before any run

**This is arithmetic on the rows above. It is not a result.** It leaves out food and clothing, because the hours behind them in the 1,380 are not in these notes.

| | Low | High |
|---|--:|--:|
| Class B, money-only work | 73 h | 171 h |
| Class A, health care | 4 h | 19 h |
| Class A, goods that fail early | 3.5 h | 38 h |
| **A and B, without food and clothing** | **about 80 h, which is 6% of 1,380** | **about 228 h, which is 17%** |

**Against the three thresholds** (15%, 25% to 29%, 37.5%): the low case passes none. The high case passes the first one only. Food would have to add about 117 hours of waste for the high case to reach 25%, and at 29% waste that needs 400 hours of food in the 1,380.

**Class C does not help the world test.** That test asks whether the world can live a *typical* US life. A typical life already has no luxury in it.

**Class D, in the United States.** People in the US work 837 to 919 hours a head each year. A typical US life takes 1,380 hours. So the US works 0.61 to 0.67 of the hours behind its own typical life, and people in other countries work the rest. With every person who wants work at work, the share is 0.66 to 0.73.

## What the claims look like against the rows

| The author's claim, 2026-11-19 | What the rows say |
|---|---|
| Americans waste food | True in tons: 23.4 million tons from homes in 2024. By one source they waste no more a person than Germans |
| Goods are made to fail | A study for the German government tested the three best-known accusations, and none stood up. Life did fall for large appliances: 14.1 years to 13.0 |
| Cheap goods are made and dumped | 4% to 9% of clothing in the European Union is destroyed before use. The well-known "30% never sold" has no method behind it |
| Much work serves only money | 5% to 12% of US jobs. This is the largest single row |
| Buyouts cut staff | Mixed. A listed firm taken private: 11.9% fewer jobs after 2 years. A private firm bought out: 14.9% more. All buyouts: 1.8% fewer, which may be 0 |
| Employers hold wages down | Supported: wages are 15% to 25% lower than with full competition. The effect on the number of jobs rests on one model |
| Unemployment is kept on purpose | The Congressional Budget Office publishes the rate, 4.4%. Above the lowest rates seen, that is 1.0% to 3.2% of hours |
| The labour force is idle | 1.3% to 9.6% of hours in 2025. In 2010 it was 8% to 18% |

## Limits

- **Tons and dollars are not hours.** Each detail note says how it turned one into the other.
- **Not all waste can be cut.** The United Kingdom cut edible food waste at home by 24% in 15 years. That is the one measured cut in these notes.
- **Several shares are a writer's judgement.** The split of each industry in class B is the main one.
- **Most sources were read through a tool that sums up a page.** Digits need a second check before any of them is printed in a public document.
- **The rows are for the United States.** Germany is given for comparison where a source exists.

## Related

- [Problem_artificial-scarcity.md](Problem_artificial-scarcity.md) · [Data: cross-country labour efficiency](Data_cross-country-labour-efficiency.md) · [Data: labour and pollution intensity](Data_labour-and-pollution-intensity.md)
- [debit-tolerance](../01-wiki/debit-tolerance.md)
