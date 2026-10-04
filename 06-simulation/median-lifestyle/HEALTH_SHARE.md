# Healthcare's share of the 1,380-hour anchor

> **Version:** 0.1
> **Date:** 2026-09-24

**Scripts:** [`health_share.py`](health_share.py) · 4 self-tests green · transcript [`HEALTH_SHARE_RUN.txt`](HEALTH_SHARE_RUN.txt)
[`health_peer.py`](health_peer.py) · transcript [`HEALTH_PEER_RUN.txt`](HEALTH_PEER_RUN.txt)

## The answer

**Healthcare is about 218 of the 1,380 hours a median US adult's consumption takes in a year. That is 15.8%.**

**Terms used here.**

| Term | What it means |
|---|---|
| **The anchor** | 1,380 h/yr: the hours of other people's work a median US adult's yearly consumption takes. Built in [`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md) |
| **Domestic hours** | Hours worked inside the US. From the BLS employment requirements matrix, as Track 1 |
| **Foreign hours** | Hours worked abroad, in imports. From EXIOBASE, as Track 3 |
| **Care services** | Physicians, dentists, paramedical services, hospitals, nursing homes |
| **Covered** | The network does not put the hours on the patient's ledger. Pledges or a network rule carry them instead |

| Part | h / median adult / yr |
|---|--:|
| Care services | **180** |
| Drugs and medical devices | **33** |
| Health insurance administration | **6** |
| **All healthcare** | **218** |

## The range, by how a network attributes care

**Which treatments land on the patient is each trust network's own choice.** One network might cover only life-saving care. Another might also cover reconstructive surgery after an injury. Elective cosmetic work, such as botox, would most likely land on the person who receives it. **So the anchor is not one number. It is a range.**

| What the network does | Anchor, h/yr | Change |
|---|--:|--:|
| **A** — every treatment lands on the patient | **1,380** | — |
| **B** — care services covered; drugs and devices on the patient | **1,194** | −13.5% |
| **C** — all healthcare covered | **1,162** | −15.8% |

**In plain words: how a network rules on healthcare moves the median debit by up to 218 hours, or 16%.** A real network sits somewhere between A and C. Where it sits depends on how much care it counts as necessary.

## The US average is not the right target

**The 218 hours are an average over all 335 million Americans.** That average mixes people who get too little care, people who get too much, and insurance paperwork. **The figure the anchor needs is the care a person uses when they are adequately provided for.**

**The stand-in used here: countries where everyone is covered.** [`health_peer.py`](health_peer.py) reads EXIOBASE for 23 countries. It counts every hour, worked anywhere, behind the health services each country's residents use, **whoever pays**: households, non-profits or the state. The state has to be included, because in most universal systems the state pays.

| Country | Health and social work, h/person/yr |
|---|--:|
| **US** | **252.8** |
| Japan | 170.9 |
| Germany | 144.7 |
| Sweden | 143.8 |
| France | 129.3 |
| Spain | 82.7 |
| **Median of the five** | **143.8 = 0.57 × US** |
| Median of all 22 peers | 136.2 = 0.54 × US |

**In plain words: a country that covers everyone uses a little over half the US hours of care per person.** Q6 (the country efficiency comparison, [`Q6.md`](Q6.md)) already found these countries give their people longer lives.

**Worked into the anchor.** Take the 180 hours of care services and multiply by 0.57, which gives **103 hours**. Remove the 6 hours of insurance paperwork, which Aequitas has no use for. Keep drugs at the US figure, because EXIOBASE cannot separate them.

| | h/yr |
|---|--:|
| The anchor at US care levels | 1,380 |
| Care services, 180 → 103 | −77 |
| Insurance paperwork | −6 |
| **The anchor at adequate provision** | **1,296** |
| Range across the five countries (Spain to Japan) | 1,253 – 1,316 |

**So the anchor at adequate provision is about 1,300 hours, and a network's care rule moves it down to 1,162.**

**Limits of this comparison.**
- **The product is "health and social work".** It also holds childcare, elder care and social services. That is why Norway, Denmark and Finland read high. The definition is the same in every country.
- **The spread is wide**: Ireland reads 39 h and Greece 45 h. Countries file state spending differently, and some of it may sit under public administration. **The median of several countries is safer than any one of them.**
- **Hours are not outcomes.** Fewer hours with longer lives shows these countries are adequate. It does not show they are the minimum.

## Drug research and drug marketing

**These two carry almost no hours in the anchor.**

| Inside the 12.6 domestic h/capita of drugs | h / capita |
|---|--:|
| Wholesale and retail trade | 6.18 |
| Drug manufacturing | 3.39 |
| Everything else | 2.77 |
| Medical equipment manufacturing | 0.11 |
| Insurance | 0.08 |
| Marketing research and other professional services | 0.05 |
| Advertising and PR | 0.04 |
| **Scientific R&D** | **0.00** |

**Why research reads zero.** US national accounts have counted R&D as **investment** since 2013, not as a purchase that goes into a product. So research labour is outside consumption, and outside the anchor. **That already matches Foundations §4.5 (training is paid when it happens): a large up-front cost is carried where it happens and cushioned by pledges, and never charged to whoever uses the result.** Drug research is pledged enrichment work, like a grant today.

**Why advertising reads so low.** The matrix counts advertising agencies' jobs only. **Broadcast airtime sits under broadcasting**, inside "everything else". So the 0.04 h is a lower bound on marketing. It is not the whole of it.

**Neither splits brand-name drugs from generics.** The data has one drug category.

## Limits

- **Drugs' foreign hours are a stand-in.** EXIOBASE has no separate drug product; drugs sit inside "Chemicals nec". The script applies the whole-economy foreign ratio (0.90 foreign hours per domestic hour). A real drug-import figure could be higher or lower.
- **Care services' foreign hours** use EXIOBASE's health-services ratio (0.35). EXIOBASE puts domestic health services at 186 h/capita against BLS's 123 h. **The script uses the BLS figure and only borrows EXIOBASE's ratio.**
- **Insurance administration would not exist in Aequitas**, because there is no money to pool. Its 6 hours are counted here only because they are inside today's anchor.
- The two big assumptions of Track 1 carry over: **1,800 hours per job-year**, and **median = 0.80 × mean**.
- **The anchor was built under the withdrawn co-product division** (Foundations §3.4a, what remains open). This result does not recompute that.
