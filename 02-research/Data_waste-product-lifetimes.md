# Data: product lifetimes and early replacement

**Version:** 0.1
**Type:** dataset note
**Retrieved:** 2026-11-19
**Read:** Opened in full text: the English summary (pages 40 to 52) of the German Environment Agency study by Prakash and others (2016); the agency's position paper of 2017; the European Environmental Bureau report "Coolproducts don't cost the Earth" (2019); the European Commission impact assessment for the repair directive, SWD(2023) 59, problem section; the PROMPT consumer survey report (2021), replacement tables; WRAP "Valuing Our Clothes" (2017), page 9. Opened as web pages: the European Environment Agency briefing on electronics (2020); the BLS Consumer Expenditures report for 2023; abstracts of Bulow (1986) and Waldman (2003); Laitala and Klepp on clothing disposal; S&P Global Mobility on vehicle age; Krajewski on the lamp cartel; Que Choisir on the Apple fine in France. Everything else is marked "search summary" in the last column.
**Local copy:** none

## Rows

The rule for a row is in [Data_sector-waste.md](Data_sector-waste.md). Class A is a product that was made and thrown away. Class C is spending that is a choice about the standard of living. A machine that broke early is class A. A working television replaced by a bigger one is class C. The sources mix the two, so each row says which it is.

"UBA" is the German Environment Agency (Umweltbundesamt). "IA" is the European Commission impact assessment for the repair directive. "First-use life" is the time a product spends with its first owner.

### How long goods last, and how long they could

| Class | Sector | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | Large household appliances | Germany | 2012/13 and 2004 | Average first-use life. Low is 2012/13, high is 2004 | 13.0 | 14.1 | years | [UBA, Prakash and others 2016, Texte 11/2016](https://www.umweltbundesamt.de/system/files/medien/378/publikationen/texte_11_2016_einfluss_der_nutzungsdauer_von_produkten_obsoleszenz.pdf), p. 43 | Opened |
| A | Large household appliances replaced after a defect | Germany | 2012/13 and 2004 | Average age at replacement. Low is 2012/13, high is 2004 | 12.5 | 13.5 | years | Same, p. 43 | Opened |
| A | Washing machines | Germany | 2013 and 2004 | Average age at municipal collection points. Low is 2013, high is 2004. The reason for disposal is not known | 13.7 | 16.0 | years | Same, p. 43 | Opened |
| A | Washing machines | Europe | 2013 to 2019 | Life in use, across 4 sources: 8 (Austria, cited by EEA), 11.4 (EU, cited by EEB), 11.6 (Germany, Bonn survey), 13.7 (Germany, collection points) | 8 | 13.7 | years | [EEA briefing 2020](https://www.eea.europa.eu/en/analysis/publications/europes-consumption-in-a-circular-economy-the-benefits-of-longer-lasting-electronics); [EEB 2019](https://eeb.org/wp-content/uploads/2019/09/Coolproducts-report.pdf), p. 6; UBA p. 43 | Opened |
| A | Washing machines | Europe | 2016 to 2020 | Life that could be reached: 12.5 is what buyers want (EEA), 20 is the long-life machine in the UBA comparison | 12.5 | 20 | years | EEA briefing; UBA p. 51 | Opened |
| A | Refrigerators | EU | 2022 | Life in practice (low) and life as designed (high) | 10 | 20 | years | [IA, SWD(2023) 59](https://data.consilium.europa.eu/doc/document/ST-7767-2023-ADD-2/en/pdf), footnote 19 | Opened |
| A and C | Flat-screen televisions | Germany | 2010 and 2012 | Average first-use life. It was 5.7 in 2007 | 4.4 | 5.6 | years | UBA p. 44 | Opened |
| A and C | Televisions | EU | 2022 | Life in practice (low) and life as designed (high). The UBA long-life set lasts 10 | 7 | 22 | years | IA footnote 19; UBA p. 51 | Opened |
| A and C | Smartphones | EU and world | 2019 to 2023 | Life in use, across 4 sources: 1.7 (IA), under 2 (EEA), 3 (EEB), 3.6 (Counterpoint, world, 43.4 months) | 1.7 | 3.6 | years | IA footnote 19; EEA briefing; EEB p. 4; [Counterpoint](https://counterpointresearch.com/research_portal/smartphone-replacement-cycle-forecast-2023-2027) (link not verified) | IA, EEA, EEB opened. Counterpoint from a search summary |
| A and C | Smartphones | EU | 2022 | Life as designed | 7 | 7 | years | IA footnote 19 | Opened |
| A and C | Laptops | Germany and EU | 2012 to 2022 | Life in use: 4 (IA), 4.5 (EEB), 5.1 (UBA, 2012). It was 6.0 in 2005/06 | 4 | 5.1 | years | IA footnote 19; EEB p. 9; UBA p. 44 | Opened |
| A and C | Laptops | EU | 2016 to 2022 | Life that could be reached: 6 is the UBA long-life laptop, 7 is the IA design life | 6 | 7 | years | UBA p. 52; IA footnote 19 | Opened |
| A and C | Clothing | United Kingdom | 2012 and 2015 | Average life of a garment. 2.2 is an assumption of 2012. 3.3 is a survey of 2015. WRAP says the two cannot be compared | 2.2 | 3.3 | years | [WRAP, Valuing Our Clothes 2017](https://www.almendron.com/tribuna/wp-content/uploads/2018/10/valuing-our-clothes-the-cost-of-uk-fashion-wrap.pdf), p. 9 (a copy on a third-party site) | Opened |
| A and C | Clothing by type | United Kingdom | 2015 | Projected life: tops 2.74, coats 4.58 | 2.74 | 4.58 | years | Same, Table 1 | Opened |
| A and C | Jackets | EU | 2022 | Life in practice (low) and as designed (high). The 1 year disagrees with WRAP's 4.58 years for coats | 1 | 4 | years | IA footnote 19 | Opened |
| A and C | Shoes | EU | 2022 | Life in practice (low) and as designed (high) | 3 | 5 | years | IA footnote 19 | Opened |
| A and C | Wooden furniture | EU | 2022 | Life in practice (low) and as designed (high) | 10 | 22 | years | IA footnote 19 | Opened |
| A | Cars | EU | 2022 | Life in practice (low) and as designed (high) | 11.5 | 18 | years | IA footnote 19 | Opened |
| A | Passenger cars | United States | 1970s and 2000s | Average life before scrapping. Low is the 1970s, high is the 2000s. Life rose | 12.2 | 15.6 | years | [Bento, Roth and Zuo 2018, Energy Journal](https://www.iaee.org/ej/ejexec/EJ391_ExecSum_Bento.pdf) (link not verified) | Search summary |
| A | Cars and light trucks on the road | United States | 2024 | Average age of the fleet. This is age, not life | 12.8 | 12.8 | years | [S&P Global Mobility, May 2025](https://press.spglobal.com/2025-05-21-U-S-Vehicle-Age-Rises-Again-to-12-8-Years-in-2025,-According-to-S-P-Global-Mobility) | Opened |
| A | Clothes washers | United States | 2012 | Typical life 7 to 14, average 11 | 7 | 14 | years | [DOE Buildings Energy Data Book, table 5.7.15](https://webarchive.library.unt.edu/web/20130214084702/http:/buildingsdatabook.eren.doe.gov/docs/xls_pdf/5.7.15.pdf) (link not verified) | Search summary |
| A | Household lamps under the lamp cartel | World | 1933/34 and 1926 | Average life of the reference lamp. The cartel's standard was 1,000 hours | 1,205 | 1,800 | hours | [Krajewski, IEEE Spectrum 2014](https://spectrum.ieee.org/the-great-lightbulb-conspiracy) | Opened |

### Why goods are replaced

| Class | Sector | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | Large household appliances | Germany | 2012 and 2004 | Share of replacements made after a defect. Low is 2012, high is 2004 | 55.6 | 57.6 | % | UBA p. 43 | Opened |
| C | Large household appliances | Germany | 2012/13 | Share of replacements where the old machine worked and the owner wanted a better one | 30.5 | 30.5 | % | UBA p. 43 | Opened |
| A | Large household appliances | Germany | 2004 and 2012 | Share of all replacements made within 5 years because of a defect. Low is 2004, high is 2012 | 3.5 | 8.3 | % | UBA p. 43 | Opened |
| A | Washing machines | Germany | 2004 and 2013 | Share of machines at collection points aged 5 years or less | 6 | 10 | % | UBA p. 43 | Opened |
| C | Flat-screen televisions | Germany | 2012 | Share replaced while they worked, for a better set | 60 | 60 | % (the source says over 60) | UBA p. 44 | Opened |
| A | Flat-screen televisions | Germany | 2012 and 2008 | Share of replacements made after a defect | 25 | 28 | % | UBA p. 44 | Opened |
| A | Laptops | Germany | 2012 to 2014 | Share replaced after a defect: over 25 in sales data, 46 in the Bonn survey | 25 | 46 | % | UBA pp. 44 to 45 | Opened |
| C | Mobile phones replaced within 3 years | Germany | about 2013 | Share replaced for a better phone (40) or because the contract gave a new one (28) | 68 | 68 | % | UBA pp. 46 to 47, citing Stiftung Warentest | Opened |
| A | Mobile phones replaced within 3 years | Germany | about 2013 | Share replaced because of the battery | 9 | 9 | % | UBA p. 46 | Opened |
| A | Washing machines | Belgium, France, Italy, Portugal, Spain | 2019 | Share replaced for a fault or a failed repair. Low and high are countries. All 5: 74.7 | 73 | 76 | % | [PROMPT survey report 2021](https://prompt-project.eu/wp-content/uploads/2021/07/2021_PROMPT-lifecycle-and-replacement-reasons-report.pdf), pp. 66 to 67. 31,914 answers | Opened |
| C | Washing machines | Same 5 countries | 2019 | Share replaced while they worked well. Another 14.8 gave other reasons, such as moving | 10.5 | 10.5 | % | Same, p. 66 | Opened |
| A | Smartphones | Same 5 countries | 2019 | Share replaced for a fault or a failed repair. All 5: 36.6 | 30 | 37 | % | Same, p. 73 | Opened |
| C | Smartphones | Same 5 countries | 2019 | Share replaced while they worked well. Another 19.2 gave other reasons | 39.1 | 39.1 | % | Same, p. 73 | Opened |
| A | Televisions | Same 5 countries | 2019 | Share replaced for a fault or a failed repair. The chart adds to 35.9, the text says 34 | 27 | 41 | % | Same, p. 80 | Opened |
| C | Televisions | Same 5 countries | 2019 | Share replaced while they worked well | 42.2 | 42.2 | % | Same, p. 80 | Opened |
| A | Vacuum cleaners | Same 5 countries | 2019 to 2020 | Share replaced for a fault or a failed repair. All 5: 63.8 | 57 | 69 | % | Same, p. 87 | Opened |
| A and C | Clothing | 17 studies, several countries | 1987 to 2020 | Share of disposals by reason: wear 37, poor fit 28, no longer wanted 35 | 37 | 37 | % for wear | [Laitala and Klepp, review of clothing disposal reasons](https://clothingresearch.oslomet.no/?p=3676) | Opened |

### Repair

| Class | Sector | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | 8 consumer goods | EU | 2022 | Share of buyers who choose a new item over repair when a fault shows within the legal guarantee. Low is cars, high is shoes and clothes. Average 64 | 45 | 78 | % | IA p. 8 and footnote 14 | Opened |
| A | Washing machines | 5 countries | 2019 | Share of replaced machines that the owner says should have been repaired: cost too high 31.0, no spare parts 3.6 | 34.6 | 34.6 | % | PROMPT p. 66 | Opened |
| A | Washing machines | 5 countries | 2019 | Share replaced because the machine worked badly and the owner did not want a repair | 26.0 | 26.0 | % | PROMPT p. 66 | Opened |
| A | Smartphones, televisions, vacuum cleaners | 5 countries | 2019 to 2020 | Share that should have been repaired, cost or parts: phones 9.4, televisions 10.8, vacuum cleaners 13.9 | 9.4 | 13.9 | % | PROMPT pp. 73, 80, 87 | Opened |
| A | Televisions and refrigerators | EU | 2022 | Share of owners who replaced because the item could not be repaired: televisions 25, refrigerators 37 | 25 | 37 | % | IA footnote 84 | Opened |
| A | Vacuum cleaners | EU | 2018 | Share of owners who did not repair the last broken one | 40 | 40 | % (the source says over 40) | EEA briefing, citing a Commission study of 2018 | Opened |
| A | 8 consumer goods | EU | 2022 | Highest repair cost buyers accept, as a share of the purchase cost. Low is cars, high is smartphones | 17 | 27 | % | IA footnotes 76 and 79 | Opened |
| A | Repair shops | EU | 2021 | Share of items brought in that were fixed | 58 | 58 | % | IA footnote 119 | Opened |
| A | Mobile phones | Germany | 2013 | Share of tested models with a battery the owner cannot change | 36 | 36 | % | UBA p. 46, citing Stiftung Warentest | Opened |
| A | Washing machines | Germany | 2000 to 2014 | Share of 196 tested models that failed a test of 10 years of use: 41 ÷ 196 | 20.9 | 20.9 | % | UBA p. 48, citing Stiftung Warentest | Opened |
| A | Repairable consumer goods, without cars | EU | 2022 | Yearly loss to buyers who tried to repair and failed, 5.1 to 25 billion euro, as a share of 792 billion euro of repairable goods | 0.6 | 3.2 | % | IA p. 12 and footnotes 31 and 33 | Opened. The shares are computed here |

### What a longer life costs

| Class | Sector | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | Washing machines | Germany | 2016 | Extra yearly total cost of a 5-year machine over a 20-year machine. The saving is 283 euro over 20 years | 13 | 13 | % | UBA p. 52 | Opened |
| A | Washing machines | Germany | 2017 | Material a 5-year machine needs, below a 20-year machine. This is an assumption of the UBA comparison | 35 | 35 | % less | [UBA position paper 2017](https://www.umweltbundesamt.de/system/files/medien/1410/publikationen/uba_position_obsoleszenz_engl_bf.pdf), footnote 1 | Opened |
| A | Laptops | Germany | 2016 | Money a 6-year laptop saves over 12 years against a 3-year laptop: plus 196 with no repair, minus 261 with repairs | −261 | 196 | euro | UBA p. 52 | Opened |
| A | Televisions | Germany | 2016 | A 10-year set against a 5.6-year set: the yearly cost is almost the same. With one repair the long-life set costs more | 0 | 0 | % (about) | UBA p. 52 | Opened |

### Weights

| Class | Sector | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| — | Vehicle purchases, net outlay | United States | 2023 | Yearly spending of an average household. Total spending is 77,280 | 5,539 | 5,539 | dollars | [BLS, Consumer Expenditures in 2023](https://www.bls.gov/opub/reports/consumer-expenditures/2023), Table A | Opened |
| — | Household furnishings and equipment | United States | 2023 | Same | 2,508 | 2,508 | dollars | Same | Opened |
| — | Apparel and services | United States | 2023 | Same | 2,041 | 2,041 | dollars | Same, and the [BLS release of 25 September 2024](https://www.bls.gov/news.release/archives/cesan_09252024.htm) | Opened |

### The estimate, by group

| Class | Sector | Place | Year | Measure | Low | High | Unit | Source (markdown link) | Opened? |
|---|---|---|---|---|--:|--:|---|---|---|
| A | Cars | United States | — | Share of purchases a longer life would save. Low: life has risen, no shortening is measured. High: 15.6 years to the 18-year design life | 0 | 13 | % | Computed here from Bento and the IA | See the rows above |
| A | Household furnishings and equipment | Germany, applied to the United States | — | Low: appliances back to their 2004 life, 13.0 to 14.1 years. High: a 13-year machine replaced by a 20-year machine | 8 | 35 | % | Computed here from UBA | See the rows above |
| A and C | Clothing | United Kingdom, applied to the United States | — | Low: no shortening is measured. High: 9 more months on a 2.2-year life | 0 | 25 | % | Computed here from WRAP | See the rows above |
| A and C | Phones, laptops, televisions | Germany and EU | — | Low: laptops back to their 2005/06 life, 5.1 to 6.0 years. High: laptops 4 to 7 years | 15 | 43 | % | Computed here from UBA and the IA | See the rows above |
| A | **Cars, furnishings and clothing together, by US spending** | United States | 2023 | Share of spending on these three groups that a longer life would save | **2** | **21** | % | Computed below | — |

## How to turn these into a share of hours

**The rule.** Hold the number of goods in use fixed. Then the number bought each year is the stock divided by the life. If the life grows from L1 to L2, purchases fall by 1 − (L1 ÷ L2).

**Worked example, low.** German large appliances lasted 14.1 years with their first owner in 2004 and 13.0 years in 2012/13. If they lasted 14.1 years again: 13.0 ÷ 14.1 = 0.922. So 7.8% fewer machines are needed. Rounded: 8%.

**Worked example, high.** A machine lasts 13 years. A long-life machine lasts 20 years. 13 ÷ 20 = 0.65. So 35% fewer machines are needed.

**The three groups together.** The weights are US household spending in 2023: vehicles 5,539 dollars, furnishings and equipment 2,508, apparel 2,041. The sum is 10,088 dollars, which is 13.1% of all spending (10,088 ÷ 77,280).

| | Cars | Furnishings and equipment | Clothing | Sum | Share of 10,088 |
|---|--:|--:|--:|--:|--:|
| Low | 0% × 5,539 = 0 | 7.8% × 2,508 = 196 | 0% × 2,041 = 0 | 196 | **1.9%** |
| High | 13.3% × 5,539 = 739 | 35% × 2,508 = 878 | 25% × 2,041 = 510 | 2,127 | **21.1%** |

**In hours, for one person.** A typical US life takes 1,380 hours a year. If hours follow dollars, these three groups take 1,380 × 13.1% = 180 hours. Low: 180 × 1.9% = 3.5 hours a year. High: 180 × 21.1% = 38 hours a year. That is 0.3% to 2.8% of the 1,380 hours.

**Every assumption.**

1. **The stock is fixed.** People keep the same number of machines, cars and garments. WRAP warns that longer life saves production only if people buy fewer new items.
2. **The low value counts only a measured fall in life.** Appliances: 14.1 to 13.0 years. Cars: life rose, so 0. Clothing: no fall is measured, so 0.
3. **The low value applies the German appliance figure to all US furnishings and equipment.** That group also holds furniture and household textiles. No measured fall was found for those.
4. **The high value for cars mixes two sources.** The 15.6 years is US scrappage data. The 18 years is the design life in the EU impact assessment.
5. **The high value for clothing uses the WRAP scenario of 2012.** 2.2 ÷ 2.95 = 0.746, a 25% cut. WRAP's own claim was 20% to 30% (from a search summary). On the 3.3-year survey life, 9 more months gives 3.3 ÷ 4.05 = 0.815, an 18.5% cut.
6. **The high value ignores the extra work in a long-life product.** The one sourced figure: a 5-year washing machine needs 35% less material than a 20-year machine. So the 35% saving in machines is larger than the saving in hours. No source gives the size of this for other goods.
7. **Neither value adds back repair hours.** A longer life needs more repairs. Repair is local labour. No source gives repair hours per year of added life.
8. **Hours follow dollars.** This is false in detail. A dollar of clothing and a dollar of car take different hours. The simulation should use its own hours by sector in place of the 180.
9. **Phones, laptops and televisions are not in the sum.** Their US spending weight was not found in the tables opened. Their own row is 15% to 43%.
10. **The base figures are German and British.** US appliance and clothing lifetimes may differ. The German method already makes the same standard on fewer hours, so part of this saving may already be counted in the comparison with Germany.

**A ceiling, not for use.** If every item reached the design life in the EU impact assessment, the saving would be: cars 1 − 11.5 ÷ 18 = 36%, refrigerators 50%, furniture 55%, shoes 40%. Weighted as above with 36%, 50% and 40%, that is about 40%. The impact assessment itself says goods could be used about twice as long as they are (p. 9). This ceiling assumes no accidents, free repair, and no wish for a newer model.

**A second check on the low value.** The Commission puts the yearly loss from failed repair attempts at 5.1 to 25 billion euro, on 792 billion euro of repairable goods. That is 0.6% to 3.2%. The low value of 1.9% sits inside that range.

## What cannot be cut

- **Wear.** A washing machine shakes and heats on every cycle. The German study found that almost any part can be the one that fails. In tests of 196 models, 155 passed 10 years of use and 41 did not.
- **Accidents.** One study cited by UBA found that 10.6% of laptops failed within 3 years from drops and misuse, and 20.4% from hardware faults.
- **Technical progress.** In tests of 2004, a new washing machine used half the electricity of a 15-year-old machine and a quarter of a 30-year-old one, for the same wash. Flat screens replaced tube televisions. Broadcast standards changed. Microsoft supported Windows XP for almost 13 years before older computers lost security updates.
- **Energy.** A newer machine can use less energy. This rarely justifies early replacement today. The European Environmental Bureau found that a washing machine should be kept 17 to 23 years even if new machines improved by 5% a year. The impact assessment names refrigerators as a case where replacement at a certain age can pay.
- **Fit and taste in clothing.** 28% of garments are discarded for poor fit and 35% because they are no longer wanted. A stronger fabric does not change those. Only the 37% discarded for wear respond to durability.
- **Choice.** 30.5% of German appliance replacements, over 60% of flat-screen replacements and 39.1% of smartphone replacements were of goods that still worked. Cutting these changes the standard of living. That is class C in this project, and it is not a saving.
- **The cost of repair.** Buyers accept a repair that costs up to 17% to 27% of the purchase cost. Repair of a washing machine at home can cost several hundred euro, because a technician travels to it.
- **The cost of durability.** A machine built for 20 years takes more material than one built for 5.

## Evidence against deliberate shortening

- **The German study tested the 3 best-known accusations and none stood up.** The 3 were: capacitors placed near heat, plastic tubs in washing machines, and ink pads that stop printers. Capacitors sit near the processor for electrical reasons. Plastic tubs caused few failures in 600 tested machines. The ink-pad stop protects against leaks, though the study says other designs could do that without stopping the printer.
- **The study says a product's life is planned, as a target.** Designers aim for parts that last about as long as each other and about as long as the buyer will use the product. The study's phrase is that products are built to last "as long as necessary and not as long as possible". A cheaper product gets a shorter target.
- **The study adds a limit on itself.** It says that proving or disproving built-in defects was not its main aim (p. 51).
- **Most early replacement is the buyer's choice.** See the class C rows above.
- **Car life rose.** US passenger cars lasted 12.2 years in the 1970s and 15.6 years in the 2000s (search summary).
- **Defect-prone laptops became less common.** Laptops replaced as faulty were 4.8 years old in 2004 and 6.2 years old in 2012.
- **Short life can be the cheaper trade.** In the UBA cost comparison, a long-life television that needs one repair costs more per year than a short-life set. A long-life laptop that needs repairs costs 261 euro more over 12 years.
- **Economic theory ties shortening to sellers with market power, and not to sellers that compete.** [Bulow (1986)](https://econpapers.repec.org/RePEc:oup:qjecon:v:101:y:1986:i:4:p:729-749.) finds that a single seller gains from a life shorter than the efficient one, and that a group of sellers can gain by agreeing to cut durability. His starting point is the standard view that competing firms supply a given service as cheaply as they can. [Swan (1972)](https://www.journals.uchicago.edu/doi/10.1086/259906) (link not verified) argued that even a single seller chooses the efficient life. [Waldman (2003)](https://econpapers.repec.org/RePEc:aea:jecper:v:17:y:2003:i:1:p:131-154) surveys when that result fails. [Fishman, Gandal and Shy (1993)](https://econpapers.repec.org/RePEc:bla:jindec:v:41:y:1993:i:4:p:361-70) (link not verified) argue that a competitive market can make goods that last too long, and that short lives can pay for faster progress.

### Evidence for, to set beside it

- **The lamp cartel is proven.** Makers agreed on a 1,000-hour lamp in 1925 and fined members whose lamps ran longer. The reference lamp fell from 1,800 hours in 1926 to 1,205 hours in 1933/34. The cartel is the case Bulow's theory predicts: a group of sellers that agrees. The history is in [the thread note](History_artificial-scarcity-thread.md).
- **Early failures rose in Germany.** Appliances replaced within 5 years for a defect went from 3.5% to 8.3% of all replacements between 2004 and 2012. The study calls this critical and gives no cause.
- **Software slowed phones, and two regulators fined the makers.** France: Apple paid 25 million euro in February 2020 for not telling owners that updates could slow the iPhone 6, SE and 7 ([Que Choisir](https://www.quechoisir.org/actualite-iphone-ralentis-25-millions-d-euros-d-amende-pour-apple-n75643/), opened). The charge was a misleading practice by omission. It was not planned obsolescence. Italy: Apple 10 million euro and Samsung 5 million euro in 2018 ([AppleInsider](https://appleinsider.com/articles/18/10/24/italy-fines-apple-114m-over-iphone-battery-slowdown-controversy), link not verified, search summary).
- **Design blocks repair.** 36% of phone models tested in 2013 had a fixed battery. 25% of television owners and 37% of refrigerator owners in the EU study replaced because the item could not be repaired.
- **Makers shorten their own life tests.** The German study reports that some television makers cut software testing from about 15 weeks to about 3, because a new model comes every year. That is neglect to save cost. The study does not call it intent.
- **The Commission describes a business model.** The impact assessment says some makers rely on frequent replacement and produce less durable, cheaper goods.

## Limits

- **No source measures the share of spending that longer life would save.** The low and high values here are computed from lifetimes. They are this note's arithmetic and no agency published them.
- **"Life" means 4 different things in these sources.** Time with the first owner. Age at disposal. Age of goods still in use. Life as designed. The washing-machine figures run from 8 to 13.7 years for that reason.
- **The design lives in the impact assessment come from a consultant's study that was not opened.** The 1-year life for jackets disagrees with WRAP's 4.58 years for coats. Treat that table with care.
- **The impact assessment misquotes the German study.** It gives the rise from 3.5% to 8.3% as a figure for refrigerators. The German study gives it for all large household appliances.
- **Surveys ask owners why they replaced.** Owners may call a wish for a new model a defect, or the reverse. The German study found this: owners said 76.2% of discarded hand mixers were defective, and an inspection at a collection point found a technical defect in 35%.
- **The PROMPT survey is of members of consumer organisations in 5 countries.** They are not a random sample of households.
- **Almost all figures are European.** For the United States this note has cars, one figure for clothes washers from a search summary, and the spending weights.
- **The spending weights are broad.** "Apparel and services" includes shoes and cleaning. "Household furnishings and equipment" includes textiles and small goods. Phones, computers and televisions sit in other lines that were not found.
- **Money is not hours, and units are not hours.**
- **Not found:** Kotler's statement on planned obsolescence in a source that could be opened. The WRAP report of 2012 in its own text. The EEA figure with the 4 design lives. US lifetimes for refrigerators, televisions, furniture and clothing. Hours of repair work per year of added life. The full text of Bulow, Swan, and Fishman, Gandal and Shy; only abstracts were read.
- **No web page asked the reader to do anything.**

## Related

- [Data: waste by sector](Data_sector-waste.md) · [Problem: artificial scarcity](Problem_artificial-scarcity.md) · [History: the artificial scarcity thread](History_artificial-scarcity-thread.md)
- [Data: cross-country labour efficiency](Data_cross-country-labour-efficiency.md) · [Data: labour and pollution intensity](Data_labour-and-pollution-intensity.md)
- [debit-tolerance](../01-wiki/debit-tolerance.md)
