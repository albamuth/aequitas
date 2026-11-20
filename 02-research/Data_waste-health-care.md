# Data: waste in United States health care

**Version:** 0.1
**Type:** dataset note
**Retrieved:** 2026-11-19
**Read:** abstracts of 13 papers, through the Europe PMC record of each (Europe PMC is a public index of medical papers) and the JAMA page for Shrank. The full author manuscript of Cutler and Ly on PubMed Central. 7 Bureau of Labor Statistics (BLS) tables. 3 Eurostat tables. One trade-press page and one policy brief. **Not opened:** the full text of any paper behind a paywall, the OECD pages (the server refused), the Congressional Budget Office paper (the server refused), the McKinsey report (the page timed out).
**Local copy:** none

## What the classes mean here

- **Class A:** care that was given and did no good, or care that was needed only because earlier care failed.
- **Class B:** work that exists only because of money. Billing, insurance work, marketing.
- **Price:** dollars paid above cost. A high price is not more hours. It is not waste in hours at all.
- **Check:** a row that is not a waste share. It is there to test the others.

## Rows

"bn $" is billions of US dollars. Each share of spending marked *(my arithmetic)* divides by 3,800 billion dollars, the 2019 total of US health spending. That total comes from a search summary of the McKinsey report and was not opened.

### 1. Shrank, Rogstad and Parekh: six kinds of waste

All rows: United States, 2019 dollars, from studies of 2012 to 2019. "Saving" is what tested measures could save, by the paper's own count.

| Class | Part of health care | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | Failure of care delivery: errors, infections caught in hospital, prevention not done | US | 2019 | Cost of waste | 102.4 | 165.7 | bn $ | [Shrank and others, JAMA 2019](https://jamanetwork.com/journals/jama/fullarticle/2752664) | Abstract opened |
| A | Same | US | 2019 | Saving by tested measures | 44.4 | 97.3 | bn $ | Same | Abstract opened |
| A | Failure of care coordination | US | 2019 | Cost of waste | 27.2 | 78.2 | bn $ | Same | Abstract opened |
| A | Same | US | 2019 | Saving by tested measures | 29.6 | 38.2 | bn $ | Same | Abstract opened |
| A | Overtreatment or low-value care | US | 2019 | Cost of waste | 75.7 | 101.2 | bn $ | Same | Abstract opened |
| A | Same | US | 2019 | Saving by tested measures | 12.8 | 28.6 | bn $ | Same | Abstract opened |
| **A** | **The three class A kinds together** | US | 2019 | Cost of waste *(my sum)* | **205.3** | **345.1** | bn $ | Same | My sum |
| **A** | **Same, as a share** | US | 2019 | Cost as a share of spending *(my arithmetic)* | **5.4** | **9.1** | % of dollars | Same | My arithmetic |
| **A** | **Same** | US | 2019 | Saving by tested measures, as a share *(my arithmetic)*: 86.8 to 164.1 bn $ | **2.3** | **4.3** | % of dollars | Same | My arithmetic |
| B | Administrative complexity: billing and coding | US | 2019 | Cost of waste. One value, no range | 265.6 | 265.6 | bn $ | Same | Abstract opened |
| B | Same | US | 2019 | Share of spending *(my arithmetic)* | 7.0 | 7.0 | % of dollars | Same | My arithmetic |
| B | Same | US | 2019 | Saving by tested measures | none found | none found | bn $ | Same | Abstract opened |
| Price | Pricing failure | US | 2019 | Cost of waste | 230.7 | 240.5 | bn $ | Same | Abstract opened |
| Price | Same | US | 2019 | Saving by tested measures | 81.4 | 91.2 | bn $ | Same | Abstract opened |
| Mixed | Fraud and abuse | US | 2019 | Cost of waste | 58.5 | 83.9 | bn $ | Same | Abstract opened |
| Mixed | Same | US | 2019 | Saving by tested measures | 22.8 | 30.8 | bn $ | Same | Abstract opened |
| All | All six kinds | US | 2019 | Cost of waste. The paper calls it about 25% of spending | 760 | 935 | bn $ | Same | Abstract opened |
| All | All six kinds | US | 2019 | Saving by tested measures. Administrative complexity adds 0 to this | 191 | 286 | bn $ | Same | Abstract opened |

**Checks.** The six low costs add to 760.1 and the six high costs to 935.1. The five savings add to 191.0 and 286.1. Against 3,800 billion the total is 20.0% to 24.6%, and the saving is 5.0% to 7.5%.

**What these rows do not show.** They are dollars. The paper adds up 71 estimates from 54 sources, and each source drew its own line. "Failure of care delivery" is mostly the cost of treating harm that could have been prevented. That care was needed once the harm happened. The low saving for care coordination (29.6) is above the low cost (27.2), because the two come from different studies.

### 2. Other measures of class A

| Class | Part of health care | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | 26 named low-value services, Medicare (the public insurance for people over 65) | US | 2009 | Share of Medicare spending. Low = strict test, high = loose test | 0.6 | 2.7 | % of dollars | [Schwartz and others, JAMA Internal Medicine 2014](https://doi.org/10.1001/jamainternmed.2014.1541) (DOI link not opened) | Abstract opened, Europe PMC record 24819824 |
| A | All medical care, by doctors' opinion | US | 2017 | Share of care that 2,106 doctors called unnecessary. Tests 24.9%, drugs 22.0%, procedures 11.1% | 20.6 | 20.6 | % of care, opinion | [Lyu and others, PLoS One 2017](https://doi.org/10.1371/journal.pone.0181970) (DOI link not opened) | Abstract opened, Europe PMC record 28877170 |

**What these rows do not show.** Schwartz counts 26 services only, so it is a floor and not a total. Lyu is a survey of opinion. Nobody measured the care.

### 3. Administration, in dollars

| Class | Part of health care | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| Check | All administration: insurers and the paperwork inside hospitals, practices, nursing homes | US | 2017 | Share of spending, in the parts with data. 812.0 bn $, 2,497 $ a person | 34.2 | 34.2 | % of dollars | [Himmelstein, Campbell and Woolhandler, Annals of Internal Medicine 2020](https://doi.org/10.7326/M19-2818) (DOI link not opened) | Abstract opened, Europe PMC record 31905376 |
| Check | Same | Canada | 2017 | Share of spending. 551 $ a person | 17.0 | 17.0 | % of dollars | Same | Abstract opened |
| B | All administration, US above Canada | US | 2017 | Cut that brings the US share to 17.0% *(my arithmetic)*: (34.2 − 17.0) ÷ (100 − 17.0) | 20.7 | 20.7 | % of dollars | Same | My arithmetic |
| B | Insurer overhead | US, Canada | 2017 | US 844 $ a person, Canada 146 $. The gap is 83% of the US figure | 83 | 83 | % of insurer dollars | Same | Abstract opened |
| Check | Administration, earlier count by the same group | US, Canada | 1999 | Share of spending: US 31.0%, Canada 16.7% | 16.7 | 31.0 | % of dollars | [Woolhandler, Campbell and Himmelstein, NEJM 2003](https://doi.org/10.1056/NEJMsa022033) (DOI link not opened) | Abstract opened, Europe PMC record 12930930 |
| Check | Administration, narrow count: insurers and government only | US and 10 rich countries | 2013–2016 | Share of spending. US 8%, others 1% to 3% | 1 | 8 | % of dollars | [Papanicolas, Woskie and Jha, JAMA 2018](https://doi.org/10.1001/jama.2018.1150) (DOI link not opened) | Abstract opened, Europe PMC record 29536101 |
| B | Billing and insurance work, all settings | US | 2012 | Cost: 471 bn $ (330 to 597). Excess over a simple system: 375 bn $ (254 to 507), which is 80% of it | 254 | 507 | bn $ | [Jiwani and others, BMC Health Services Research 2014](https://doi.org/10.1186/s12913-014-0556-7) (DOI link not opened) | Abstract opened, Europe PMC record 25540104 |
| **B** | **Same, as a share** | US | 2012 | Saving in a simple system, as the paper states it | **about 15** | **about 15** | % of dollars | Same | Abstract opened |
| B | Administration, savable with no change of system | US | 2019 | 950 bn $ of administration, about 25% of spending. 265 bn $ savable, which is 28% of administration and 7.0% of spending | 7.0 | 7.0 | % of dollars | [Sahni, Mishra, Carrus and Cutler, McKinsey 2021](https://www.mckinsey.com/industries/healthcare/our-insights/administrative-simplification-how-to-save-a-quarter-trillion-dollars-in-us-healthcare) (link not verified: the page timed out) | **Search summary only.** The 265 bn $ and its parts (210 + 105 − 50) were opened on [a trade-press page](https://www.hfma.org/finance-and-business-strategy/administrative-simplification/research-highlights-ways-to-save-more-than-250-billion-per-year/) |
| B | Payer administration under a single public payer | US | 2020 | Share of spending, Congressional Budget Office (CBO) estimate, as a critic reports it | 1.5 | 1.6 | % of dollars | [Blahous, Mercatus Center 2021](https://www.mercatus.org/research/policy-briefs/understanding-cbos-medicare-all-cost-estimates), on [the CBO paper](https://www.cbo.gov/publication/56811) (link not verified: the server refused) | Brief opened. CBO paper not opened |
| B | Billing cost of one primary-care visit, one university hospital system | US | 2016–2017 | 13 minutes of work and 20.49 $, which is 14.5% of the doctor's fee. One emergency visit: 32 minutes, 25.2% | 14.5 | 25.2 | % of professional revenue | [Tseng and others, JAMA 2018](https://doi.org/10.1001/jama.2017.19148) (DOI link not opened) | Abstract opened, Europe PMC record 29466590 |
| B | Marketing of drugs, tests and health services | US | 2016 | 29.9 bn $, up from 17.7 bn $ in 1997. 13.5 bn $ of it is free samples, which are goods and not work | 29.9 | 29.9 | bn $ | [Schwartz and Woloshin, JAMA 2019](https://doi.org/10.1001/jama.2018.19320) (DOI link not opened) | Abstract opened, Europe PMC record 30620375 |

**What these rows do not show.** Every row is dollars. Himmelstein counts all administration, and much of it is work any health system needs. The paper leaves out dentists and pharmacies. Papanicolas counts only insurers and government, so 8% and 34.2% are not two answers to one question. The Canada rows compare with one country that has one public payer. They say nothing about Germany, which has many insurers.

### 4. Administration, in workers and hours

| Class | Part of health care | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| Check | Doctors' offices and clinics, including home health (BLS industry 621) | US | May 2023 | Jobs in management, business and finance, and office work: 2,200,030 of 8,337,190 | 26.4 | 26.4 | % of jobs | [BLS, occupational employment, industry 621](https://www.bls.gov/oes/2023/may/naics3_621000.htm) | Opened. Shares are my arithmetic |
| Check | Hospitals (BLS industry 622) | US | May 2023 | Same three groups: 1,065,300 of 6,234,730 | 17.1 | 17.1 | % of jobs | [BLS, industry 622](https://www.bls.gov/oes/2023/may/naics3_622000.htm) | Opened |
| Check | Nursing and residential care (BLS industry 623) | US | May 2023 | Same three groups: 340,900 of 3,079,930 | 11.1 | 11.1 | % of jobs | [BLS, industry 623](https://www.bls.gov/oes/2023/may/naics3_623000.htm) | Opened |
| **Check** | **All three industries** | US | May 2023 | Same three groups: 3,606,230 of 17,651,850 | **20.4** | **20.4** | % of jobs | The three tables above | My sum |
| **B** | **All three industries: jobs whose title is billing or coding** | US | May 2023 | Billing and posting clerks 173,100, medical records specialists 117,370. Together 290,470 of 17,651,850 | **1.6** | **1.6** | % of jobs | The three tables above | My sum |
| B | Health insurance companies (BLS industry 524114) | US | May 2023 | 430,460 jobs. That is 2.4% of the 17,651,850 jobs in care | 430,460 | 430,460 | jobs | [BLS, industry 524114](https://www.bls.gov/oes/2023/may/naics5_524114.htm) | Opened |
| Check | Administrative workers in the health labour force, insurers left out | US | 1969, 1999 | 18.2% in 1969, 27.3% in 1999 | 18.2 | 27.3 | % of workers | [Woolhandler and others, NEJM 2003](https://doi.org/10.1056/NEJMsa022033) (DOI link not opened) | Abstract opened |
| Check | Same | Canada | 1971, 1996 | 16.0% in 1971, 19.1% in 1996 | 16.0 | 19.1 | % of workers | Same | Abstract opened |
| **B** | **Administrative workers, US above Canada** | US | 1999 | Cut that brings the US share to 19.1% *(my arithmetic)*: (27.3 − 19.1) ÷ (100 − 19.1) | **10.1** | **10.1** | % of workers | Same | My arithmetic |
| B | Administrative staff per person, US above Canada | US, Canada | year of the data not checked; paper of 2011 | The US has 44% more. So 1 − 1 ÷ 1.44 = 31% of US administrative staff are above the Canadian level | 31 | 31 | % of administrative staff | [Cutler and Ly, Journal of Economic Perspectives 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC4511963) | Full author manuscript opened |
| **B** | **Same, as a share of all care jobs** | US | 2023 base | 31% of the 20.4% above *(my arithmetic)* | **6.2** | **6.2** | % of jobs | Cutler and Ly, with the BLS tables | My arithmetic |
| Check | Administrative workers per office doctor | US | year of the data not checked; paper of 2011 | 2.2 in the US. Canada has about half. Hospitals: 1.5 administrative staff a bed in the US, 1.1 in Canada | 1.1 | 2.2 | workers per doctor | Cutler and Ly | Opened |
| B | Nurses and medical assistants, time spent dealing with insurers | US | paper of 2011 | 20.6 hours per doctor per week. Nearly 10 times the figure in Ontario | 20.6 | 20.6 | hours per doctor per week | [Morra and others, Health Affairs 2011](https://doi.org/10.1377/hlthaff.2010.0893) (DOI link not opened) | Abstract opened, Europe PMC record 21813866 |
| B | Clerical staff, same | US, Ontario | paper of 2011 | US 53.1, Ontario 15.9 | 15.9 | 53.1 | hours per doctor per week | Same paper | **Search summary only** |
| B | Doctors' own time dealing with insurers | US | paper of 2009 | 3 hours a week | 3 | 3 | hours per week | [Casalino and others, Health Affairs 2009](https://doi.org/10.1377/hlthaff.28.4.w533) (DOI link not opened) | Abstract opened, Europe PMC record 19443477 |

**What these rows do not show.** A job title is not a task. A receptionist books patients and also checks insurance. A nurse fills in an insurer's form. So 1.6% is too low and 20.4% is far too high as a count of billing work. The BLS tables count jobs and not hours, and they leave out the self-employed. The 27.3% is from 1999 and from a different job classification than the BLS tables.

### 5. Prices against quantities

| Class | Part of health care | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| Price | All health care | US and 29 OECD countries | 2000 | US use of services is below the OECD median on most measures. Prices explain most of the higher spending. No percentage is given | — | — | — | [Anderson, Reinhardt, Hussey and Petrosyan, Health Affairs 2003](https://doi.org/10.1377/hlthaff.22.3.89) (DOI link not opened) | Abstract opened, Europe PMC record 12757275 |
| Price | All health care | US and OECD | 2015–2016 | The US has fewer hospital beds, doctors and nurses per person than the OECD median. No percentage is given | — | — | — | [Anderson, Hussey and Petrosyan, Health Affairs 2019](https://doi.org/10.1377/hlthaff.2018.05144) (DOI link not opened) | Abstract opened, Europe PMC record 30615520 |
| Price | All health care | US and 10 rich countries | 2013–2016 | US spending is 17.8% of GDP. The others spend 9.6% to 12.4%. Use of care is similar | 9.6 | 17.8 | % of GDP | [Papanicolas, Woskie and Jha, JAMA 2018](https://doi.org/10.1001/jama.2018.1150) (DOI link not opened) | Abstract opened |
| Price | Pay of a general doctor | US and 10 rich countries | 2013–2016 | US 218,173 $ a year. Others 86,607 $ to 154,126 $ | 86,607 | 218,173 | $ a year | Same | Abstract opened |
| Price | Drugs | US and 10 rich countries | 2013–2016 | US 1,443 $ a person. Others 466 $ to 939 $ | 466 | 1,443 | $ a person | Same | Abstract opened |
| Check | Doctors and nurses | US | 2013–2016 | 2.6 doctors and 11.1 nurses per 1,000 people | 2.6 | 11.1 | per 1,000 people | Same | Abstract opened |
| **Split** | **Hospitals and doctors: the gap between the US and Canada, 1,589 $ a person** | US, Canada | 2002 | Administration 616 $ (39%). Provider incomes 490 $ (31%). Extra procedures 224 $ (14%). Not explained 259 $ (16%) | 31 | 31 | % of the gap that is pay | [Cutler and Ly 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC4511963), from Pozen and Cutler 2010 | Opened |
| **Split** | **Same** | US, Canada | 2002 | Administration and extra procedures together: 39 + 14 | 53 | 53 | % of the gap that is extra work | Same | My sum |

**What these rows do not show.** Only the Cutler and Ly row gives a split in numbers. It covers hospitals and doctors, not drugs, and it compares with Canada in 2002. The 616 $ of administration is also dollars: part of it is higher pay for each administrator. The 259 $ "not explained" is my subtraction; the paper explains 1,330 $ of the 1,589 $.

### 6. Health-care work per person: the direct check on hours

The OECD pages could not be opened. These rows use Eurostat national accounts for Germany, France and Sweden, and BLS tables for the United States. US population is 335 million, the figure in [HEALTH_SHARE.md](../06-simulation/median-lifestyle/HEALTH_SHARE.md).

| Class | Part of health care | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| Check | Human health activities: hospitals, practices, other health work | Germany | 2023 | 3,443,000 workers ÷ 83.12 million people | 41.4 | 41.4 | workers per 1,000 people | [Eurostat, employment by industry](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_a64_e?format=JSON&geo=DE&geo=FR&geo=SE&nace_r2=Q86&nace_r2=Q87_Q88&nace_r2=Q&na_item=EMP_DC&unit=THS_PER&time=2019&time=2022&time=2023) and [population](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?format=JSON&geo=DE&geo=FR&geo=SE&sex=T&age=TOTAL&time=2019&time=2022&time=2023) | Opened. Germany 2023 is provisional |
| Check | Same | France | 2023 | 2,143,600 ÷ 68.44 million | 31.3 | 31.3 | workers per 1,000 people | Same | Opened |
| Check | Same | Sweden | 2023 | 380,000 ÷ 10.52 million | 36.1 | 36.1 | workers per 1,000 people | Same | Opened |
| Check | Same: BLS industries 621 and 622 | US | May 2023 | 14,571,920 ÷ 335 million. Without home health (1,601,940 jobs) it is 38.7 | 38.7 | 43.5 | jobs per 1,000 people | BLS tables above and [industry 6216](https://www.bls.gov/oes/2023/may/naics4_621600.htm) | Opened |
| **Check** | **Human health activities, hours** | Germany | 2023 | 4,488,918 thousand hours ÷ 83.12 million | **54.0** | **54.0** | hours worked per person per year | [Eurostat, hours worked by industry](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_a64_e?format=JSON&geo=DE&geo=FR&geo=SE&nace_r2=Q86&nace_r2=Q87_Q88&nace_r2=Q&na_item=EMP_DC&unit=THS_HW&time=2019&time=2022&time=2023) | Opened |
| **Check** | **Same** | France | 2023 | 3,100,481 thousand hours ÷ 68.44 million | **45.3** | **45.3** | hours per person per year | Same | Opened |
| **Check** | **Same** | Sweden | 2023 | 538,360 thousand hours ÷ 10.52 million | **51.2** | **51.2** | hours per person per year | Same | Opened |
| **Check** | **Same** | US | 2023 jobs, 2025 hours | Clinics 8,337,190 jobs × 31.6 hours × 52 weeks, plus hospitals 6,234,730 × 36.3 × 52. Together 25,468 million hours ÷ 335 million | **76.0** | **76.0** | paid hours per person per year | BLS tables above and [BLS weekly hours](https://www.bls.gov/web/empsit/ceseeb2a.htm) | Opened. My arithmetic |
| Check | Health and social work together, hours | Germany, France, Sweden | 2023 | Germany 98.6, France 80.6, Sweden 129.5 | 80.6 | 129.5 | hours per person per year | Eurostat hours table above | Opened |
| Check | Same: BLS industries 621 to 624 | US | 2023 jobs, 2025 hours | 22,068,570 jobs. 37,754 million hours ÷ 335 million | 112.7 | 112.7 | paid hours per person per year | BLS tables above and [industry 624](https://www.bls.gov/oes/2023/may/naics3_624000.htm) | Opened. My arithmetic |

**Ratios to the United States, in hours.** Health activities alone: Germany 0.71, France 0.60, Sweden 0.67. Health and social work together: Germany 0.87, France 0.72, Sweden 1.15.

**What these rows do not show.** A head count hides the hours. Germany has 41.4 health workers per 1,000 people and the US has 43.5, which is nearly the same. But a German health worker works 1,304 hours a year (4,488,918 ÷ 3,443), and a US health job is paid for 33.4 hours a week, about 1,737 a year. The US figure is hours paid, with holidays in it. The European figure is hours worked. That alone could close several points of the gap. The two industry lists also draw the line between health and social care in different places.

## Dollars are not hours

**A high price is a transfer of dollars. It is not more work.** The project counts hours, so a price has to be taken out before a dollar share is used.

**Worked example 1: the same hour at two prices.** A general doctor in the US is paid 218,173 dollars a year. In the best-paying of 10 other rich countries the figure is 154,126 dollars (Papanicolas). 218,173 ÷ 154,126 = 1.42. One hour of that doctor's work costs 1.42 times the dollars. In hours it is still 1 hour.

**Worked example 2: splitting the US excess.** Hospitals and doctors cost 1,589 dollars a person more in the US than in Canada in 2002 (Cutler and Ly).

| Part of the 1,589 $ gap | $ a person | Share | Is it hours? |
|---|--:|--:|---|
| Administration | 616 | 39% | Yes, mostly. Class B |
| Higher incomes of doctors and other providers | 490 | 31% | No. Price |
| Extra procedures on hospital patients | 224 | 14% | Yes. Some of it is class A |
| Not explained | 259 | 16% | Unknown |

**So about 31% of the excess is price, about 53% is real extra work, and 16% is unknown.** Most of the real extra work is administration (39 of the 53 points). Extra treatment is the small part.

**A second check gives a similar answer.** The US spends about 2 times what peer countries spend (Papanicolas). In hours of health work per person the US is at 1.4 to 1.7 times Germany, France and Sweden (1 ÷ 0.71 and 1 ÷ 0.60, section 6). Take 2.0 for dollars and 1.5 for hours. The excess in dollars is 1.0 and the excess in hours is 0.5. So about half the excess is price and half is work.

**The two "prices" papers and the hours check do not contradict each other.** Anderson counts doctors, nurses and beds, and the US has fewer of each. The extra US hours are in other jobs: 20.4% of US care jobs are management, finance and office work.

**Pricing failure and fraud are not rows for the run.** Shrank's pricing failure is 230.7 to 240.5 billion dollars, about 6% of spending. It is 0 hours. Fraud is mostly a payment for care that was not given, which is also 0 hours.

## How to turn these into a share of the 218 hours

The 218 hours are: care services 180, drugs and devices 33, insurance administration 6 ([HEALTH_SHARE.md](../06-simulation/median-lifestyle/HEALTH_SHARE.md); the parts add to 219 by rounding).

### Class B: billing, insurance work

| | Low | High |
|---|--:|--:|
| Insurance administration, of 6 hours | 83% = **5 h** (the US overhead above Canada's, Himmelstein) | 100% = **6 h** (the project has no money to pool) |
| Billing work inside care services, of 180 hours | 1.6% = **3 h** (jobs titled billing or coding, BLS) | 10.1% = **18 h** (administrative workers above the Canadian share, Woolhandler) |
| **Class B by worker counts** | **8 h = 4% of 218** | **24 h = 11% of 218** |
| Class B by the highest dollar study used here | | about 15% = **33 h** (Jiwani) |

- **Low: 4%.** It counts only people whose job title is billing or coding, and insurer staff above the Canadian level.
- **High: 15%.** Worker counts reach 11%. They leave out the hours that nurses and doctors spend on insurers' forms (20.6 hours per doctor per week for nursing staff, Morra). Jiwani's 15% of dollars is the published figure that includes them.
- **A middle value: 7%.** Cutler and Ly's 44% gives 6.2% of care jobs, which is 11 hours of 180. Add 5 hours of insurance. 16 ÷ 218 = 7%. Shrank and McKinsey each reach 7.0% of dollars by other routes.
- **Not used as the high value: 20.7%.** That is the Himmelstein dollar figure. It is contested, and no worker count supports it.

### Class A: care that did no good

Apply to the 212 hours of care services and drugs.

| | Share | Hours of 212 |
|---|--:|--:|
| **Low:** overtreatment alone, low value (Shrank) | 2.0% | **4 h** |
| Saving by tested measures, three class A kinds (Shrank) | 2.3% to 4.3% | 5 to 9 h |
| **High:** three class A kinds, high cost (Shrank) | 9.1% | **19 h** |
| Not used as the high value: doctors' opinion (Lyu) | 20.6% | 44 h |

- **Low: 2%. High: 9%.**
- A share of dollars equals a share of hours only if wasted care costs the same dollars an hour as other care. Low-value care leans toward scans and tests, which use costly machines and fewer hours. So the share of hours is probably below the share of dollars. No source measures this.

### Both classes

| | Low | High |
|---|--:|--:|
| Class A | 4 h | 19 h |
| Class B | 8 h | 33 h |
| **A and B** | **12 h = 6% of 218** | **52 h = 24% of 218** |

**Do not count the peer-country gap as well.** [HEALTH_SHARE.md](../06-simulation/median-lifestyle/HEALTH_SHARE.md) cuts care services from 180 to 103 hours by a ratio of 0.57 to peer countries, and removes the 6 insurance hours. That is 83 hours, or 38% of 218. The class A and class B hours are inside that gap. A run that applies both counts the same hours twice.

## What cannot be cut

- **Administration that any system needs.** Booking, patient records, payroll, ordering supplies. Canada still spends 17.0% of its health dollars on administration, and 19.1% of its health workers were administrative in 1996.
- **Most of the waste has no tested cure.** Shrank found tested measures for 191 to 286 of the 760 to 935 billion dollars. For administrative complexity the paper found none.
- **Care that turns out not to help.** A test that finds nothing still ruled something out. Schwartz's strict test finds 0.6% and the loose test 2.7%: the answer depends on how sure one must be before calling care useless.
- **Care that repairs harm.** "Failure of care delivery" is 102.4 to 165.7 billion dollars. Once a patient has a hospital infection, the treatment is needed. Only prevention removes those hours, and prevention takes hours too.
- **Hours that would move, not vanish.** 10% of Americans had no insurance in the Papanicolas data. The CBO expects providers to use time freed from paperwork to give more care (from a search summary of a Health Affairs article, not opened).
- **A trust network's own records.** Foundations section 4.7 gives a network auditors and estimators. Their hours go back in.
- **Prices and fraud.** They are dollars, not hours. Cutting them saves 0 hours.

## Where the sources disagree

| The question | One answer | Another answer | Why they differ |
|---|---|---|---|
| Shrank's saving | 191 to 282 bn $ (news of October 2019) | 191 to 286 bn $ (the JAMA page today) | JAMA printed a correction. The care-delivery saving went from 93.3 to 97.3. Use 286 |
| Administration as a share of spending | 34.2% (Himmelstein) | 25% (McKinsey) · 8% (Papanicolas) | Three definitions. Himmelstein counts paperwork inside hospitals and practices. Papanicolas counts insurers and government only |
| How much administration is waste | 20.7% of spending (Himmelstein, against Canada) | 7.0% (Shrank; McKinsey) · about 15% (Jiwani) | Himmelstein assumes a change to one payer. McKinsey assumes no change of system |
| Is Himmelstein's comparison sound | Yes (the authors; they say it is an undercount) | No: a critic at Brookings in 2003 said the two countries' accounts cannot be compared that way | Search summary only; the critique was not opened |
| Overtreatment | 2.0% to 2.7% of spending (Shrank) | 20.6% of care (Lyu) | Measured services against doctors' opinion |
| Does the US use more real resources | No: fewer doctors, nurses and beds (Anderson 2019) | Yes: 1.4 to 1.7 times the hours of health work per person (section 6) | Anderson counts 3 clinical resources. The hours count includes office staff |
| Peer countries' hours against the US | 0.57 (the project's own figure, all hours behind health and social work, imports included) | 0.60 to 0.71 for health work alone; 0.72 to 1.15 with social work (section 6, direct hours only) | Different boundaries. Sweden files much elder care under social work |

## Limits

- **Every page was read through a tool that summarises.** Check each digit against its source before the run. The BLS and Eurostat digits were read twice or cross-checked by sums.
- **Abstracts only** for 13 of the 14 papers. The tables inside them were not seen. Cutler and Ly is the exception.
- **The CBO paper, the McKinsey report and the OECD tables were not opened.** Their rows are marked.
- **OECD Health Statistics was asked for and not used.** Section 6 uses Eurostat and BLS, which do not define "health care" the same way.
- **The years run from 1999 to 2025.** The Canada comparisons are from 1999, 2002 and 2017. The US hours a week are from October 2025 and the US jobs from May 2023.
- **US hours are paid hours, and the BLS job tables leave out the self-employed.** The first makes the US look higher. The second makes it look lower.
- **The 3,800 billion dollar total and the 335 million population were not opened at a source.**
- **Canada is the only country any administration study compares with.** No row here measures German, French or Swedish administration.
- **Drugs and devices (33 hours) have one row, marketing, and it is in dollars.** No source here turns it into hours.
- **No row gives class A or class B waste directly in hours.** Every share of the 218 hours rests on the assumption named beside it.
- **No page asked the reader to do anything.**

## Related

- [Data: waste by sector](Data_sector-waste.md) · [Problem: artificial scarcity](Problem_artificial-scarcity.md) · [Data: cross-country labour efficiency](Data_cross-country-labour-efficiency.md)
- [Healthcare's share of the 1,380-hour anchor](../06-simulation/median-lifestyle/HEALTH_SHARE.md)
