# Data: capacity left idle

**Version:** 0.1
**Type:** dataset note
**Retrieved:** 2026-11-19
**Read:** BLS (US Bureau of Labor Statistics) Employment Situation tables A-1, A-8, A-12, A-15 and A-16 for October 2026. BLS annual tables 19, 20 and 35 for 2025. BLS series held by FRED (the data service of the Federal Reserve Bank of St. Louis), opened as data files. Federal Reserve release G.17 of 17 November 2026 and its capacity notes. Eurostat table `lfsi_sla_a` through the Eurostat data service, and the Eurostat article on labour market slack. Two BLS articles on reasons for not working. Two Bureau of Justice Statistics pages. One Dallas Fed press release, one San Francisco Fed letter, and the Federal Reserve projections of 16 September 2026.
**Local copy:** none

Class D is capacity left idle: hours and machines that could work and do not. The classes A, B and C are in [Data: waste by sector](Data_sector-waste.md).

**Three warnings before the rows.**

- **The rows overlap.** Unemployment, idle factories and the output gap are three views of the same slack. A run that adds them counts the same idle hour 3 times.
- **2025 annual figures are 11-month averages.** BLS collected no data for October 2025 because of the federal shutdown.
- **"Low" is the best year and "High" is the worst year** in the range rows. The latest value is in the Measure column.

## Rows

| Class | What is idle | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|---|---|---|---|---|
| D | People with no job who looked for one in the last 4 weeks | United States | Jan 2000 to Oct 2026, monthly | U-3, the official unemployment rate. Latest (Oct 2026): 4.1 | 3.4 (Apr 2023) | 14.8 (Apr 2020) | % of labour force | [FRED, UNRATE and U6RATE monthly](https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE,U6RATE&cosd=2000-01-01) · [BLS table A-15](https://www.bls.gov/news.release/empsit.t15.htm) | Opened both |
| D | The same | United States | 2000 to 2025, annual | U-3, annual average. 2025: 4.3. Mean of the 26 years: 5.65 | 3.6 (2023) | 9.6 (2010) | % of labour force | [FRED, UNRATE annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE&cosd=2000-01-01&fq=Annual&fam=avg) | Opened |
| D | Unemployed, plus people who want a job, are available and looked in the last 12 months, plus people who work part time and want full time | United States | Jan 2000 to Oct 2026, monthly | U-6, the broad measure. Latest (Oct 2026): 7.9 | 6.6 (Dec 2022, Apr 2023) | 22.9 (Apr 2020) | % of labour force plus marginally attached | [FRED, UNRATE and U6RATE monthly](https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE,U6RATE&cosd=2000-01-01) · [BLS table A-15](https://www.bls.gov/news.release/empsit.t15.htm) | Opened both |
| D | The same | United States | 2000 to 2025, annual | U-6, annual average. 2025: 8.0. Mean of the 26 years: 10.2 | 6.9 (2022, 2023) | 16.7 (2010) | % | [FRED, U6RATE annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=U6RATE&cosd=2000-01-01&fq=Annual&fam=avg) | Opened |
| D | Unemployed people, count | United States | 2000 to 2025, annual | Latest (Oct 2026): 7,068. 2025: 7,282 | 5,685 (2000) | 14,808 (2010) | thousand people | [FRED, UNEMPLOY annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNEMPLOY&cosd=2000-01-01&fq=Annual&fam=avg) · [BLS table A-1](https://www.bls.gov/news.release/empsit.t01.htm) | Opened both |
| D | Employed people, count. This is the base for every share below | United States | 2000 to 2025, annual | Latest (Oct 2026): 163,615. 2025: 163,551 | 136,481 (2002) | 163,551 (2025) | thousand people | [FRED, CE16OV annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CE16OV&cosd=2000-01-01&fq=Annual&fam=avg) · [BLS table A-1](https://www.bls.gov/news.release/empsit.t01.htm) | Opened both |
| D | People who work under 35 hours for economic reasons: slack work, or they found only part-time work | United States | 2000 to 2025, annual | Latest (Oct 2026): 4,840, of which slack work 3,252 and found only part-time work 1,265. 2025: 4,802 | 3,229 (2000) | 8,916 (2009) | thousand people | [FRED, LNS12032194 annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=LNS12032194&cosd=2000-01-01&fq=Annual&fam=avg) · [BLS table A-8](https://www.bls.gov/news.release/empsit.t08.htm) | Opened both |
| D | Hours that a person on part time for economic reasons lacks | United States | 2025 | They average 22.6 hours a week. Low: up to the 35-hour line. High: up to the full-time average of 41.9 hours. The average week of all people at work is 38.3 hours | 12.4 | 19.3 | hours a week | [BLS annual table 20](https://www.bls.gov/cps/cpsaat20.htm) · [BLS annual table 19](https://www.bls.gov/cps/cpsaat19.htm) | Opened both. The subtraction is done here |
| D | People outside the labour force who say they want a job | United States | 2000 to 2025, annual | Latest (Oct 2026): 6,024. 2025: 5,988 | 4,413 (2000) | 7,122 (2020) | thousand people | [FRED, NILFWJN annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NILFWJN&cosd=2000-01-01&fq=Annual&fam=avg) · [BLS table A-1](https://www.bls.gov/news.release/empsit.t01.htm) | Opened both |
| D | Of those: "marginally attached", who are available now and looked in the last 12 months | United States | 2000 to 2025, annual | Latest (Oct 2026): 1,610. 2025: 1,716 | 1,157 (2000) | 2,573 (2011) | thousand people | [FRED, LNU05026642 annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=LNU05026642&cosd=2000-01-01&fq=Annual&fam=avg) · [BLS table A-16](https://www.bls.gov/news.release/empsit.t16.htm) | Opened both |
| D | Of those: "discouraged", who stopped looking because they expect to find nothing | United States | 2000 to 2025, annual | Latest (Oct 2026): 451. 2025: 510 | 262 (2000) | 1,173 (2010) | thousand people | [FRED, LNU05026645 annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=LNU05026645&cosd=2000-01-01&fq=Annual&fam=avg) · [BLS table A-16](https://www.bls.gov/news.release/empsit.t16.htm) | Opened both |
| D | Why the marginally attached did not look in the last 4 weeks | United States | 2025 | Of 1,716: discouraged 509, family duties 181, school or training 195, ill health or disability 151, other 680. Of the 6,018 who want a job, 3,591 did not look at all in the last year and 711 are not available now | 1,189 (discouraged plus other) | 1,716 (all) | thousand people | [BLS annual table 35](https://www.bls.gov/cps/cpsaat35.htm) | Opened |
| not D | People who did not work or look for work in the year, by main reason | United States | 2022 | Total 94,522. Retired 48,832. Going to school 15,048. Ill or disabled 14,534. Home or family duties 13,097. Other, which includes "could not find work", 3,011 | 0 | 3,011 (the "other" group only) | thousand people | [BLS Monthly Labor Review, September 2024](https://www.bls.gov/opub/mlr/2024/article/why-did-labor-force-nonparticipation-increase-from-1999-to-2022.htm) · 2014 figures in [BLS Beyond the Numbers, December 2015](https://www.bls.gov/opub/btn/volume-4/people-who-are-not-in-the-labor-force-why-arent-they-working.htm) | Opened both |
| not D | People in state and federal prisons, and in local jails | United States | 2023 | Prisons 1,254,200 at the end of 2023. Jails 664,200 at mid 2023. No BLS measure counts them | not used | not used | people | [BJS, Prisoners in 2023](https://bjs.ojp.gov/library/publications/prisoners-2023-statistical-tables) · [BJS, Jail Inmates in 2023](https://bjs.ojp.gov/library/publications/jail-inmates-2023-statistical-tables) | Opened both |
| D | Labour market slack: unemployed, part-timers who want more hours, people who look and are not available, people who are available and do not look | Germany | 2009 to 2025, annual | 2025: 7.9 (unemployed 3.7, part-timers who want more hours 1.2, look and not available 0.8, available and do not look 2.2) | 6.4 (2019) | 13.2 (2009) | % of extended labour force, ages 15 to 74 | [Eurostat, table lfsi_sla_a](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsi_sla_a?format=JSON&lang=EN&sex=T&age=Y15-74&unit=PC_ELF&geo=DE&geo=EU27_2020&sinceTimePeriod=2009) | Opened. The series starts in 2009. Germany has series breaks in 2010, 2011 and 2020 |
| D | The same | European Union, 27 countries | 2009 to 2025, annual | 2025: 11.8 (unemployed 5.8, part-timers who want more hours 2.4, look and not available 0.9, available and do not look 2.7). Highest country in 2025: Finland 19.5. Lowest: Malta 4.9 | 11.8 (2024, 2025) | 19.6 (2013) | % of extended labour force, ages 15 to 74 | [Eurostat, table lfsi_sla_a](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsi_sla_a?format=JSON&lang=EN&sex=T&age=Y15-74&unit=PC_ELF&geo=DE&geo=EU27_2020&sinceTimePeriod=2009) · [Eurostat article](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Labour_market_slack_-_employment_supply_and_demand_mismatch) | Opened both |
| D | Unemployed only, inside the slack measure | Germany | 2009 to 2025 | 2025: 3.7 | 2.9 (2019) | 7.1 (2009) | % of extended labour force | Eurostat table above | Opened |
| D | Unemployed only, inside the slack measure | European Union | 2009 to 2025 | 2025: 5.8 | 5.7 (2024) | 11.0 (2013) | % of extended labour force | Eurostat table above | Opened |
| D | Factories, mines and utilities that run below capacity | United States | Jan 2000 to Oct 2026, monthly | Capacity utilization, total industry. Latest (Oct 2026): 76.4. Average of 1972 to 2025: 79.4. High of 1988-89: 85.2 | 64.1 (Apr 2020) | 82.4 (Apr 2000) | % of capacity in use | [Federal Reserve, G.17](https://www.federalreserve.gov/releases/g17/current/) · [FRED, TCU monthly](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TCU&cosd=2000-01-01) | Opened both |
| D | Factories only | United States | Jan 2000 to Oct 2026, monthly | Capacity utilization, manufacturing. Latest (Oct 2026): 76.0. Average of 1972 to 2025: 78.2. High of 1988-89: 85.5 | 62.5 (Apr 2020) | 80.7 (Apr 2000) | % of capacity in use | [Federal Reserve, G.17](https://www.federalreserve.gov/releases/g17/current/) · [FRED, MCUMFN monthly](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MCUMFN&cosd=2000-01-01) | Opened both |
| D | The same two rates as annual averages | United States | 2000 to 2025 | Total industry 2025: 75.9. Manufacturing 2025: 75.3 | Total 68.4, manufacturing 65.4 (both 2009) | Total 81.6, manufacturing 79.6 (both 2000) | % of capacity in use | [FRED, TCU annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TCU&cosd=2000-01-01&fq=Annual&fam=avg) · [FRED, MCUMFN annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MCUMFN&cosd=2000-01-01&fq=Annual&fam=avg) | Opened both |
| D | Extra industrial output that the idle capacity allows, October 2026 | United States | Oct 2026 | Low: back to the 1972 to 2025 average (79.4 ÷ 76.4). High: up to the 1988-89 high (85.2 ÷ 76.4). Manufacturing alone: 2.9 to 12.5 | 3.9 | 11.5 | % more industrial output | Derived here from the G.17 row | Arithmetic done here |
| D | Factories | European Union | Jul 2026 | Capacity utilisation in manufacturing, from the European Commission's business survey: 78.2. Germany, second quarter of 2026: 78.4 | not found | not found | % of capacity in use | [European Commission survey, July 2026, copy at wifo.ac.at](https://www.wifo.ac.at/wp-content/uploads/upload-2181/bcs_2026_07_en.pdf) (link not verified) | Search summary only |
| D | Output lost in the slump of 2008 to 2009 | United States | 2009 | Output gap: real output against the Congressional Budget Office's (CBO) potential output. Low: the year 2009 at today's figures. Worst quarter at today's figures: 5.0 (second quarter). High: CBO's estimate at the time for the first quarter of 2009 | 4.7 | 6.2 | % of potential output | Low: [FRED, GDPC1](https://fred.stlouisfed.org/graph/fredgraph.csv?id=GDPC1&cosd=2005-01-01&coed=2026-12-31) ÷ [FRED, GDPPOT](https://fred.stlouisfed.org/graph/fredgraph.csv?id=GDPPOT&cosd=2005-01-01&coed=2026-12-31). High: [San Francisco Fed letter 2009-19](https://www.frbsf.org/research-and-insights/publications/economic-letter/2009/06/output-gap/) | Opened all 3. The division is done here. A St. Louis Fed page gives 6.7 for the second quarter of 2009: [link](https://files.stlouisfed.org/files/htdocs/datatrends/pdfs/mt/20091201/cover.pdf) (link not verified) |
| D | Output lost over the whole slump and slow recovery | United States | 2008 to 2017 | Low: the sum of the 10 yearly output gaps at today's figures. High: the Dallas Fed's range of 40 to 90, measured against the trend before the crisis | 21 | 90 | % of one year's output | Low: the two FRED series above. High: [Dallas Fed press release, 29 July 2013](https://www.dallasfed.org/news/releases/2013/nr130729a) | Opened. The sum is done here |
| D | Output lost in 2020 | United States | 2020 | Low: the year 2020. High: the second quarter of 2020. A summary of CBO's figures at the time gives 10.8 for that quarter | 3.3 | 8.8 | % of potential output | The two FRED series above. The 10.8: [Mercatus Center](https://www.mercatus.org/media/71906/download) (link not verified) | Opened the FRED series. The division is done here |
| D | Output gap now | United States | 2025, and third quarter of 2026 | Output is above CBO's potential: +1.4 in 2025 and +1.7 in the third quarter of 2026. By this measure no output is lost to a slump now | 0 | 0 | % of potential output | The two FRED series above | Opened. The division is done here |
| limit | Unemployment that is people between jobs: unemployed for less than 5 weeks | United States | Oct 2026 | 2,170 thousand of a labour force of 170,683 thousand. This is a stand-in for the frictional rate. BLS publishes no frictional rate | 1.3 | 1.3 | % of labour force | [BLS table A-12](https://www.bls.gov/news.release/empsit.t12.htm) | Opened. The division is done here |
| limit | Unemployment that stays when no slump is on: between jobs, plus a skill or place that does not fit the open jobs | United States | 2000 to 2026 | CBO's noncyclical rate of unemployment. 2026: 4.4. The Federal Reserve's longer-run rate, September 2026: median 4.2, range 3.8 to 4.4 | 4.4 (2026) | 5.1 (2000) | % of labour force | [FRED, NROU annual](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NROU&cosd=2000-01-01&fq=Annual&fam=avg) · [Federal Reserve projections, 16 September 2026](https://federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm) | Opened both |
| D | **Result: extra hours the United States could work, latest full year** | United States | 2025 | Method below. October 2026 gives 1.2 and 9.5 | **1.3** | **9.6** | % of hours actually worked | Derived here from the BLS rows above | Arithmetic done here |
| D | **Result: the same in the worst year of the 26** | United States | 2010 | Method below | **8.0** | **18.2** | % of hours actually worked | Derived here | Arithmetic done here |
| D | **Result: the same in the best year of the 26** | United States | 2023 | Method below | **1.0** | **8.4** | % of hours actually worked | Derived here | Arithmetic done here |
| D | **Result: mean of the 26 years 2000 to 2025** | United States | 2000 to 2025 | Method below. This is the row that shows the cost of booms and slumps in hours | **2.8** | **11.7** | % of hours actually worked | Derived here | Arithmetic done here |

## How to turn these into hours

All counts are in thousands of people. A new worker is assumed to work the average week of 38.3 hours. So one unemployed person who gets a job adds the hours of 1 average worker.

**The two weights for part time.** A person on part time for economic reasons works 22.6 hours a week.

- Low weight: they rise to 35 hours. 35 − 22.6 = 12.4 hours. 12.4 ÷ 38.3 = **0.324** of an average worker.
- High weight: they rise to the full-time average. 41.9 − 22.6 = 19.3 hours. 19.3 ÷ 38.3 = **0.504** of an average worker.

**HIGH.** Everybody who says they want work gets it, with no allowance for people between jobs.

`HIGH = (unemployed + want a job + part time for economic reasons × 0.504) ÷ employed`

**LOW.** Only the unemployment above CBO's noncyclical rate counts. Of the people outside the labour force, only the discouraged count. Part-timers rise only to 35 hours.

`LOW = (unemployed − noncyclical rate × labour force, never below 0, + discouraged + part time for economic reasons × 0.324) ÷ employed`

**Worked example, 2025.**

- Employed 163,551. Unemployed 7,282. Labour force 163,551 + 7,282 = 170,833.
- HIGH: 7,282 + 5,988 + 4,802 × 0.504 = 7,282 + 5,988 + 2,420 = 15,690. 15,690 ÷ 163,551 = **9.6%**.
- LOW: the noncyclical rate is 4.405%. 4.405% × 170,833 = 7,525. That is more than the 7,282 unemployed, so the first term is 0. Then 510 + 4,802 × 0.324 = 510 + 1,555 = 2,065. 2,065 ÷ 163,551 = **1.3%**.

**Worked example, 2010 (the worst year).**

- Employed 139,077. Unemployed 14,808. Labour force 153,885.
- HIGH: 14,808 + 6,065 + 8,874 × 0.504 = 14,808 + 6,065 + 4,472 = 25,345. 25,345 ÷ 139,077 = **18.2%**.
- LOW: 5.028% × 153,885 = 7,737. 14,808 − 7,737 = 7,071. Then 7,071 + 1,173 + 8,874 × 0.324 = 7,071 + 1,173 + 2,873 = 11,117. 11,117 ÷ 139,077 = **8.0%**.

**In hours per head of population, 2025.** The population was 341.9 million at mid 2025 ([FRED, POPTHM](https://fred.stlouisfed.org/graph/fredgraph.csv?id=POPTHM&cosd=2024-01-01), opened).

- At the 1,750 hours per worker that the project's own band cites: 163,551 × 1,750 ÷ 341,900 = **837 hours per head**.
- At the BLS household survey: 157,736 thousand at work × 38.3 hours × 52 weeks = 314 billion hours. 314 billion ÷ 341.9 million = **919 hours per head**. People report long weeks in this survey, so 919 is the upper figure.
- LOW adds 1.3%: 11 to 12 hours per head. HIGH adds 9.6%: 80 to 88 hours per head.

**Idle factories do not add hours. They need hours.** Manufacturing employed 12,632 thousand people in 2025 ([FRED, MANEMP](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MANEMP&cosd=2024-01-01&fq=Annual&fam=avg), opened). That is 7.7% of the employed. To raise manufacturing output by 2.9% to 12.5% takes about 0.2% to 1.0% of all hours, if hours rise in step with output. Those hours come out of the idle hours above. They are not a second source.

## What the project's own band already counts

**The band already holds all of the idle hours in this note. None of them may be added on top of it.**

The band is in [Q1B_DEPLOYABLE_LABOUR.md](../06-simulation/scenario-suite/Q1B_DEPLOYABLE_LABOUR.md). It multiplies 3 dials: working-age share 0.60 to 0.68, participation 0.62 to 0.85, hours per worker 1,600 to 2,080. It treats every person who participates as a person at work. So it has no unemployment in it at all.

| | Workers per head of population | Hours per head | Share of the 1,380 hours needed |
|---|---|---|---|
| Band, lowest corner | 0.60 × 0.62 = 0.372 | 595 | 0.43 |
| United States as it is, 2025 | 163,551 ÷ 341,900 = 0.478 | 837 to 919 | 0.61 to 0.67 |
| United States plus LOW idle hours (1.3%) | | 848 to 931 | 0.61 to 0.67 |
| United States plus HIGH idle hours (9.6%) | (163,551 + 7,282 + 5,988) ÷ 341,900 = 0.517 | 917 to 1,007 | 0.66 to 0.73 |
| Band, highest corner | 0.68 × 0.85 = 0.578 | 1,202 | 0.87 |

- **Unemployed people (U-3):** inside the band. The participation dial counts them as working.
- **People who want a job and do not look:** inside the band. The dial goes to 0.85 of every working-age adult. The United States with all of them at work reaches 0.517 workers per head, below the band's 0.578.
- **Part-timers who want full time:** inside the band. The hours dial goes to 2,080. Giving every one of them full time lifts the US average from 1,750 to about 1,776 hours.
- **The band's top corner is 31% to 44% above the hours the United States works now** (1,202 ÷ 919 and 1,202 ÷ 837). The HIGH idle share is 9.6%. So the band's top assumes far more than the end of unemployment: it also puts carers, students and early retirees to work.
- **Idle factories and the output gap:** not in the band, and they should stay out. The band counts hours of people. A machine that runs again uses hours and does not supply them.

**What this note changes for the band.** Nothing at the corners. It fixes one point inside the band: the United States works about 0.61 to 0.67 of the hours needed, and full use of everyone who wants work lifts that to about 0.66 to 0.73.

## What is not idle

- **People between jobs.** About 1.3% of the labour force has been unemployed for less than 5 weeks. CBO puts all unemployment that is not from a slump at 4.4%. The LOW value leaves the whole 4.4% out. The HIGH value keeps it in, so the HIGH value overstates.
- **Carers.** 13,097 thousand people gave home or family duties as the main reason for no paid work in 2022. The project counts care as work. They are not idle. The same holds for 181 thousand of the marginally attached, and for the 1,309 thousand who worked short weeks in 2025 because of child-care problems.
- **Students.** 15,048 thousand in 2022, and 195 thousand of the marginally attached. The project counts study as work.
- **Ill or disabled people.** 14,534 thousand in 2022. No source in this note says how many could work with support. They are counted as 0.
- **Retired people.** 48,832 thousand in 2022. The band's working-age dial already leaves most of them out.
- **People in prison or jail.** About 1.9 million. Jails hold about 90 thousand of them for state and federal authorities, so the two counts may overlap by that much (the 90 thousand is from a search summary of the jail report, not from an opened page). BLS surveys leave all of them out. Their number follows from law and sentencing. It is a choice about how to live, like class C. It is not slack.
- **Part-timers by choice.** 22,664 thousand people worked part time for other than economic reasons in October 2026: school, family, health, partial retirement. They are not idle.

**Truly idle, by the survey's own words:** the unemployed above the noncyclical rate, the discouraged, the "other" marginally attached, and part-timers for economic reasons.

## Limits

- **Stated wishes are not hours.** Of the 6,018 thousand who wanted a job in 2025, 3,591 thousand had not looked for a year and 711 thousand were not available. The HIGH value counts them all at a full average week.
- **New workers are not average workers.** The idle are younger and less trained than the employed. The note gives each of them 38.3 hours and says nothing about output per hour. Output would rise by less than hours.
- **Hours are not all alike.** An idle retail worker does not staff a hospital. The band has the same limit.
- **The 2025 weights are used for every year.** The 12.4 and 19.3 hours come from 2025. The 2010 and 2023 results use them too.
- **Potential output moves.** CBO lowers its potential after a long slump. That is why the 2009 gap is 4.7% at today's figures and was 6.2% or more at the time. The Dallas Fed measured against the old trend and found 40% to 90% of a year's output. The low and high values in that row measure different things.
- **Capacity is not 24 hours a day.** The Federal Reserve defines capacity as "sustainable maximum output": what a plant can keep up on a realistic schedule, with normal downtime and enough inputs. The rate has not been above 85.2% since 1988-89. So 100 − 76.4 = 23.6% is not idle capacity. The usable figure is 3.0 to 8.8 points.
- **G.17 covers industry only.** It has no rate for services, where most hours are worked.
- **Eurostat slack is not U-6.** Eurostat covers ages 15 to 74 and counts people who are available and did not look at all. U-6 asks that they looked in the last 12 months. Eurostat counts people, and its table gives no hours. The Eurostat series starts in 2009, so its range covers 17 years and not 25.
- **Not found.** CBO's own output-gap table: the CBO page refused the request. A frictional unemployment rate from an agency: none is published, so the under-5-weeks share stands in for it. A long-run average for European capacity utilisation. A count of ill or disabled people who could work. Hours lacked by underemployed part-timers in Germany and the European Union.
- **No page asked the reader to do anything.**

## Related

- [Data: waste by sector](Data_sector-waste.md) · [Problem_artificial-scarcity.md](Problem_artificial-scarcity.md)
- [Q1B_DEPLOYABLE_LABOUR.md](../06-simulation/scenario-suite/Q1B_DEPLOYABLE_LABOUR.md), the deployable-hours band
- [debit-tolerance](../01-wiki/debit-tolerance.md)
