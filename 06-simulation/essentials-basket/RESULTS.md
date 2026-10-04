# `E` — the hours behind a year of essentials

> **Version:** 0.1
> **Date:** 2026-09-24

## The answer

**For one US person, a year of essentials takes 516 to 655 hours of other people's work for a narrow basket, and 826 to 965 hours for a broad one.**

**Terms used here.**

| Term | What it means |
|---|---|
| **`E`** | Hours of other people's work, anywhere on Earth, behind one person's year of essentials. Foundations §5.5.3 (the floor's two bounds) |
| **`F`**, the floor | Hours a day a network credits for the work of staying alive |
| **ρ** | The network's debit tolerance, the multiplier in the gate `D ≤ ρ·(C + P)` |
| **Narrow basket** | Food eaten at home, clothing and footwear, shelter, household utilities, health and social care, drugs |
| **Broad basket** | The narrow basket, plus household chemicals, paper and plastic goods, furniture and other goods, local transport, post and telecoms, schooling |
| **Peers** | Germany, Japan, Sweden, France and Spain. All cover everyone for care |

**Which goods count as essential is each network's choice.** So there are two baskets, and a network can sit anywhere between them.

| Basket | Care at the peer level | Care at the US level | Lowest floor at ρ = 1.2 |
|---|--:|--:|--:|
| **Narrow** | 516 – 546 h | 625 – 655 h | 1.2 – 1.5 h/day |
| **Broad** | 826 – 856 h | 935 – 965 h | 1.9 – 2.2 h/day |

**Each cell is a range because building a home is added as 31 to 61 hours a year** (Track 2 of `../median-lifestyle/`).

**Worked, broad basket at 965 h:** the lowest floor is 965 ÷ (1.2 × 365) = **2.2 h/day**. At `F` = 2 h/day the floor gives 1.2 × 2 × 365 = **876 h**, which is 89 h short. At `F` = 3 it gives 1,314 h and covers it.

**In plain words: a floor of about 2 hours a day covers the narrow basket, and a little over 2 covers the broad one.** The illustrative 700 h that Foundations used before sat between the two baskets.

## By category, per person per year

| Category | US | Peer median | Basket |
|---|--:|--:|---|
| Food eaten at home | 131 | 170 | narrow |
| Clothing and footwear | 121 | 89 | narrow |
| Shelter services | 38 | 4 | narrow |
| Household utilities | 21 | 17 | narrow |
| Health and social care | 253 | 144 | narrow |
| Drugs (US figure, from `health_share.py`) | 30 | — | narrow |
| Housing structure (Track 2) | 31 – 61 | — | narrow |
| Chemicals, paper, plastics (includes drugs) | 103 | 20 | broad only |
| Furniture and other goods | 78 | 13 | broad only |
| Land transport services | 59 | 38 | broad only |
| Post and telecoms | 13 | 3 | broad only |
| Schooling | 87 | 73 | broad only |

**Health and social care is the largest item in either basket.** That is why the care level moves `E` by 109 hours.

## Are the peers' supply chains shorter?

**Mostly no.** [`logistics_chain.py`](logistics_chain.py) counts the hours worked **in** shops, wholesale and transport behind each country's consumption, anywhere on Earth, however the accounts file them. Transcript: [`LOGISTICS_RUN.txt`](LOGISTICS_RUN.txt).

| Country | Shops and wholesale | Transport and storage | Both | Share of all hours behind consumption |
|---|--:|--:|--:|--:|
| **US** | **188** | **102** | **290** | **21%** |
| Japan | 209 | 78 | 286 | 24% |
| Sweden | 189 | 103 | 292 | 24% |
| France | 160 | 106 | 266 | 23% |
| Germany | 136 | 72 | 208 | 18% |
| Spain | 55 | 84 | 140 | 15% ⚠️ |

**In plain words: a US person's consumption takes about the same logistics work as a Japanese, Swedish or French person's.** The US is 5% above the median of those four and Germany. Its share of all hours, 21%, is lower than in Japan, Sweden or France. **Germany is the one peer with a clearly shorter chain**, 28% below the US, mostly in land transport (22 h against the US's 48).

**Japan settles the filing question.** Japanese households buy only 10 hours of shop work as a separate item, yet **209 hours** of shop work sit behind their consumption. The work is there, filed inside the goods.

**One caveat points toward shorter chains in the peers.** "Transport" includes passenger trains, buses and flights, not only freight. Europeans and Japanese ride more public transport, while Americans mostly drive their own cars, which is not counted here. So the peers' freight share is somewhat smaller than this table shows.

**⚠️ Spain's data is missing its shop work.** Spain records **3 hours** a year per resident of work in its own shops and wholesale. The other five record **84 to 169**. No country runs its shops on 3 hours a person, so this is a gap in the data set, not a finding. **It makes Spain look more efficient than it is.**

**A check of all 23 countries in Q6 finds one more: Poland**, at 18 hours. Every other country records 48 to 169 hours a resident, which is 6% to 18% of all its work. Spain's share is 0.3% and Poland's 1.8%. Transcript: [`LOGISTICS_CENSUS.txt`](LOGISTICS_CENSUS.txt).

| Country | Hours in its own shops and wholesale, per resident | Share of all its work |
|---|--:|--:|
| Spain | **3** | **0.3%** ⚠️ |
| Poland | **18** | **1.8%** ⚠️ |
| Belgium, the lowest of the rest | 48 | 6.1% |
| US | 117 | 11.8% |
| Italy | 106 | 14.1% |
| Japan, the highest | 169 | 15.4% |

**Italy's data is complete**, so Q6's finding for Italy stands. **Spain's does not.** See the parking lot, 2026-09-24.

## Why the US level is the figure to use

**A network in the US runs on the US production method.** The peer figures mix two things: a different quantity of goods, and a more efficient way of making them (`../median-lifestyle/Q6.md`). **Using peer hours for a US network would make essentials look cheaper than they are**, which is the direction Foundations §4.4 warns about. **The one exception is care, by author ruling on 2026-09-24:** the US average includes over-treatment and insurance paperwork, so adequate care is read at the peer level.

## Limits

- **Category totals across countries are unreliable. The basket totals are safer.** US households buy **224 hours** of retail and wholesale work as a separate item. The peers buy only 10 to 73 hours that way. **Tested, and it is mostly a filing difference:** the peers' shop work sits inside the goods (see *Are the peers' supply chains shorter?* above). Post and telecoms reads 0 for Sweden and 69 for Germany, which is the same kind of problem.
- **Retail hours are shared out by spending.** The 224 US hours go to goods categories by each category's share of goods spending, as Track 1 does with margins. This is why household chemicals, which include drugs, reads 103 h.
- **"Health and social work" includes childcare and elder care**, in every country.
- **Drugs are counted twice in the broad basket if you add the drug line to it.** The script does not. Drugs sit inside "chemicals" there.
- **`E` is per person, all ages.** The 1,380 h anchor is per median adult. The two are not on the same basis. All US consumption per person, on this method, is **1,398 h**, so the narrow basket is about 40% of it and the broad basket about 65%.
- **The broad basket at the US level is about 70% of a median lifestyle.** That is the one cell in which the stable band closed, at `F` = 1 h/day under full pledging (`../stable-band/PLEDGE_BAND_RESULTS.md`). A floor of 1 h/day is below the lowest floor in the table above anyway.
