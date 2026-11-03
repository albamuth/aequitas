# Data — which countries have time-use and household-spending data we can run sims on

> **Version:** 0.1
> **Date:** 2026-11-02

**Type:** data-source survey · **Retrieved:** 2026-11-02 (web search summaries and two page fetches; most catalogue pages not opened)

## Why this matters to Aequitas

The child-consumption request (`sr-20261102-single-parent-and-two-adult-yearly-balance-f`) needs, for each age band: **(a)** hours of childcare given at home, **(b)** spending on purchased care and schooling, **(c)** goods spending by household type. The US note for ATUS 2023 ([`Data_american-time-use-survey-2023.md`](Data_american-time-use-survey-2023.md)) holds no childcare table; [`Data_atus-childcare-by-age-of-youngest-child.md`](Data_atus-childcare-by-age-of-youngest-child.md) now holds two age bands. A claim about the 0.3 weight needs other countries, because a US-only result is a US-method result (Foundations §3.5, §5.5.3). Weight convention: [`Method_oecd-modified-equivalence-scale.md`](Method_oecd-modified-equivalence-scale.md).

## What we are after: hours, not money

**The target on both sides is hours.** Credit is the parent's hours of care, which time-use diaries record. Debit is the hours of other people's work behind what the child consumes. **Money spending data is useful only as a mix of goods and services**, converted to hours with labour coefficients (BLS employment requirements for the US, EXIOBASE for other countries, as in `06-simulation/median-lifestyle/`). A price column is never a result here.

## Checked on 2026-11-02 (second pass)

| Item | Result |
|---|---|
| **ATUS, US** | Table 8A fetched. Childcare 2.08 h a day with the youngest child under 6, 0.61 with the youngest 6 to 17. See [`Data_atus-childcare-by-age-of-youngest-child.md`](Data_atus-childcare-by-age-of-youngest-child.md) |
| **HETUS metadata** (<https://ec.europa.eu/eurostat/cache/metadata/en/tus_00_esms.htm>) | Fetched. Activities use the HETUS Activity Coding List in 10-minute slots; childcare is one of six activity tables; "household composition" is a breakdown, but **no page defines an age-of-youngest-child variable**. Wave 2 lists 18 countries (collected 2008–2015, including Turkey) and the microdata page lists 17. **The researcher-file codebook was found in a third pass and is summarised in [`Data_hetus-2010-variables-and-access.md`](Data_hetus-2010-variables-and-access.md).** HETUS code 38, *Childcare*, maps to ICATUS 2016 division 41 (an Italian statistics presentation, not opened) |
| **ICATUS 2016** | Childcare and instruction is **division 41** under **major division 4, unpaid caregiving services for household and family members**. My earlier guess of "group 3" was wrong: division 3 is unpaid domestic services |
| **India 2019** | Verified from the NSSO presentation at the UN workshop in Xi'an, June 2024 (<https://unstats.un.org/unsd/demographic-social/meetings/2024/tus-wk-china-2024/10b.%20Time%20Use%20Survey%20in%20India_India_Mr.%20Sandip%20Kumar%20Sadhu.pdf>): first all-India survey, January–December 2019, CAPI, **ages 6 and over**, 24-hour diary from 4 AM, 30-minute slots with activities of 10 minutes or more, **ICATUS 2016**, 138,799 households. **A simultaneous-activity flag exists**, so secondary care can be separated. Male and female respondents 226,644 and 218,526. The second survey is in the field in 2024. **The microdata catalogue (microdata.gov.in) refused the connection from this machine**, so the catalogue entry and the code list are still unread |

## The short answer

| Group | Time use (childcare hours) | Household spending |
|---|---|---|
| **Europe, rich** | **HETUS 2010**: 17 countries, researcher files by application. Aggregate tables by youngest child's age are public | **Eurostat HBS**: files for 2010, 2015, 2020 by application. Tables by household type are public |
| **Europe, post-socialist** ("second world") | Same HETUS 2010 round holds **Estonia, Hungary, Poland, Romania, Serbia**. Moldova ran a survey (case study found, data not checked) | Same HBS, which covers the EU's post-socialist members |
| **Upper-middle income** | **South Africa 2010** (free registration, a childcare variable exists). **Mexico ENUT** (open or on request, page not confirmed) | Mexico **ENIGH** (INEGI publishes file descriptors) |
| **Low and lower-middle income** ("third world") | **India 2019** (open catalogue, 138,799 households). **Kenya** (survey run, access not confirmed) | **LSMS** panels: Uganda and Nigeria confirmed, free registration |

## Detail

### Europe

| Source | What it holds | Access | Link | Verified |
|---|---|---|---|---|
| **HETUS 2010 microdata** | Scientific-use files for **AT, BE, DE, EE, EL, ES, FI, FR, HU, IT, LU, NL, PL, RO, UK, NO, RS**. Diary activity in 10-minute slots. **Age comes in 5-year bands**. Country of birth and citizenship are suppressed | Application under Eurostat's microdata procedure; the page does not give the steps | <https://ec.europa.eu/eurostat/web/microdata/harmonised-european-time-use-surveys> | **Fetched.** The page does not say whether *age of youngest child* is a variable; check the variable description PDF |
| **HETUS 2020 microdata** | Round 3 | **Not before 2027** | same page | Fetched |
| **HETUS aggregate tables** (`tus_00hhstatus`, `tus_00npaycare` and others) | Time by household type, including *couple with youngest child under 6*, *youngest child 7–17*, *single parent*. Childcare split into *childcare except teaching, reading and talking* and *teaching, reading and talking*. 2000 and 2010 rounds seen | Public tables, mirrored by EIGE | e.g. <https://dgs-p.eige.europa.eu/data/information/ta_timeuse_careact_chldrn__tus_00npaycare> | Seen in search results; not opened |
| **Eurostat HBS** | Consumption by COICOP purpose and household type; files for **2010, 2015, 2020**. In the 2020 main tables Sweden, Finland, Ireland and Portugal are missing; Cyprus, France and Malta are converted from 2015 | Tables public; files under Commission Regulation (EC) No 831/2002 | <https://ec.europa.eu/eurostat/web/microdata/household-budget-survey> and the metadata <https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm> | Seen in search results. **Education and childcare cells not confirmed** |
| **MTUS / MTUS-X** (Centre for Time Use Research, UCL) | Harmonised diaries, 25–30 countries (sources disagree), 1961–2018, mostly affluent countries | **Free, on registration** | <https://timeuse.org/mtus> | Seen in search results. Country list and childcare codes not checked |

### Upper-middle and lower-middle income

| Country | Source | What it holds | Access | Link | Verified |
|---|---|---|---|---|---|
| **India** | National Statistics Office Time Use Survey 2019 | 138,799 households, 447,250 persons aged 6+. Activity-level file with 9,436,777 cases and a paid/unpaid flag | Open catalogue, reference DDI-IND-CSO-TUS-2019-19 | <https://microdata.gov.in/NADA/index.php/catalog/223> | Seen in search results. **The childcare activity codes are in the documentation, not checked.** The 2020 press note was read: unpaid care of all kinds averages about 144 h a year per person aged 6 and over (women 225, men 65). Childcare alone and age of child are not in it. See [`Data_india-time-use-survey-2019.md`](Data_india-time-use-survey-2019.md) |
| **South Africa** | Stats SA *Time Use Survey 2010* via DataFirst | Four files (person, household, activities, all persons). **Person file has `Q57ChildCare`** | **Free registration** | <https://www.datafirst.uct.ac.za/dataportal/index.php/catalog/497> | Seen in search results |
| **Mexico** | INEGI ENUT (time use) and ENIGH (spending) | ENIGH publishes file descriptors | INEGI says microdata go to anyone who asks, with a microdata laboratory and remote processing; the ENUT page itself was **not found** | <https://www.inegi.org.mx> | **Unconfirmed for ENUT** |
| **Kenya** | KNBS time-use module in the Continuous Household Survey, ages 15+, 47 counties | UN Women used it to size demand for care | **Not confirmed** | <https://data.unwomen.org/sites/default/files/documents/Publications/2024/Kenya_time-use_care-assessment_summarybrief.pdf> | Brief seen |
| **Uganda, Nigeria** | World Bank LSMS-ISA panels | Household consumption; the Nigeria 2018–19 wave asks about scholarships | **Free account** on the Microdata Library | <https://microdata.worldbank.org/index.php/catalog/3795/get-microdata> | Seen; **education and childcare modules not checked** |
| **Ethiopia, Malawi, Mali, Niger, Nigeria, Tanzania, Uganda** | Harmonised LSMS-ISA panel 2008–2021 | Agriculture-focused, plot-level | Per World Bank working paper | <https://econpapers.repec.org/RePEc:wbk:wbrwps:10976> | Seen; probably too farm-centred |
| **Moldova** | Time-use survey case study (Data2X, UNDP) | Not checked | — | <https://www.undp.org/sites/g/files/zskgke326/files/migration/md/Data2x-TUS-Case-Studies-Moldova.pdf> | Title only |

### Compilations, which give summary tables and not microdata

| Source | What it holds | Link |
|---|---|---|
| UN Statistics Division time-use portal | Average paid and unpaid work by sex, plus metadata. Aggregates only | <https://data2x.org/resource-center/united-nations-statistics-division-unsd-gender-statistics-time-use-portal/> |
| UNDP, *Time use across the world* | 102 surveys, 65 countries; mostly from national statistics office sites | <https://hdr.undp.org/en/content/time-use-across-world-findings-world-compilation-time-use-surveys> |
| UN Women | 84 countries have run a time-use survey; **24% of them have data from 2010 or later** | <https://data.unwomen.org/sites/default/files/documents/Publications/THE%20TELLING%20NATURE%20OF%20TIME.pdf> |

## What we can run, in plain words

- **Ready now, and open:** India 2019 (once the childcare codes are read). **Free account:** South Africa 2010, MTUS, Uganda and Nigeria LSMS. **Application:** HETUS 2010 and Eurostat HBS files. **Public aggregate tables only:** Europe by youngest child's age, for 2000 and 2010.
- **Not confirmed at all:** Mexico's ENUT, Kenya's microdata, and any childcare spending line in the LSMS modules.
- **Nothing found** in this pass for Ghana, Tanzania (outside the farm panel), Pakistan, Bangladesh, Vietnam or Brazil. That is a gap in my search and not evidence that the data does not exist.

## What it gets wrong / limitations

- **Time-use methods differ.** Data2X's review says methods that suit low-income countries differ from those in rich ones, so childcare hours are not directly comparable across the groups above.
- **Most of these entries come from search summaries.** Rows marked *seen in search results* are leads, not verified facts. Each needs its catalogue page opened before a sim cites it.
- **The distinction between primary and secondary care** (a parent watching a child while cooking) changes the hours a great deal, and each survey codes it differently.
- **European aggregates stop at 2010.** HETUS 2020 microdata arrive in 2027 at the earliest.

## Next steps

1. **HETUS: codebook read** ([`Data_hetus-2010-variables-and-access.md`](Data_hetus-2010-variables-and-access.md)). No exact child age; two bands for couples (0–6, 7–17) and one for single parents. Access needs a recognised research entity, about 12 weeks. **Public aggregate table opened and filed:** [`Data_eurostat-childcare-by-household-type.md`](Data_eurostat-childcare-by-household-type.md) (`tus_00hhstatus`, 15 countries, 2010). `tus_00npaycare` has no household-type split, so it is not useful for age bands.
2. **India:** the catalogue refused the connection again on 2026-11-02. The press note is filed; the full 2019 report (with the childcare line) and the microdata are still not reached. Try a different network, or find the report on the MoSPI publications page by hand. The PDF named `Report of the Time Use Survey-Final.pdf` is the 1998–99 pilot, not 2019.
3. Register for DataFirst, MTUS and IPUMS ATUS, and record the exact childcare variables and the age bands they allow.
4. Find the OECD paper and the 1994 Eurostat monograph (see the method note).
5. **ATUS: done at table level** (two age bands). The finer bands 0–4, 5–11 and 12–13 need the microdata.
6. Embodied-hours coefficients for the countries chosen (EXIOBASE, already on disk for `06-simulation/median-lifestyle/`), so a household's goods convert to hours.

## Related

[[property-debit]] · [`Method_oecd-modified-equivalence-scale.md`](Method_oecd-modified-equivalence-scale.md) · [`Data_cross-country-labour-efficiency.md`](Data_cross-country-labour-efficiency.md)
