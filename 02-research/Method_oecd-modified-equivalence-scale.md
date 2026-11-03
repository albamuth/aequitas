# Method — the OECD-modified equivalence scale (1 / 0.5 / 0.3)

> **Version:** 0.1
> **Date:** 2026-11-02

**Type:** method / convention · **Retrieved:** 2026-11-02 (search summaries; primary documents not opened, see the list at the end)

## Why this matters to Aequitas

`00-strategy/papers/Pledges.md` §13.1 prices a child at **0.3 of an adult** (552 h/yr in a two-adult home, 414 h/yr in a one-adult home, at 1,380 h per adult). The 0.3 is not a measurement. It is a convention from the poverty-statistics literature. This note says where it comes from and what an empirical weight would need.

## What the scale is

| Scale | First adult | Each further adult | Each child | Child age rule |
|---|--:|--:|--:|---|
| **Oxford, recommended by the OECD in 1982** | 1.0 | 0.7 | 0.5 | under 14 |
| **OECD-modified, Hagenaars, de Vos and Zaidi (1994)** | 1.0 | 0.5 | **0.3** | under 14 in most sources; **under 16 in one** |
| Square root of household size | — | — | — | not age-based |

Eurostat replaced the Oxford scale with the modified scale during the 1990s, and it is now the standard for equivalised income in EU statistics.

## What the sources say about its basis

- **It is conventional.** One search result quotes Hagenaars et al. (1994, p. 194) calling the choice *"a pragmatic choice"* that *"should be considered as arbitrary"* as the alternatives. **That quotation reached me through a search summary and I have not seen the page. Unverified.**
- **It reconciled diverging estimates.** One source says the scale was meant to reconcile the empirical findings available at the time, and has no direct empirical basis of its own.
- **The INSEE note** says scales rest on convention and names the 0.3 of the OECD-modified scale as an example.
- **The age rule is not fixed.** Most sources say 0–13. An Italian appendix says under 16. A project that quotes "a child under 14" must say which source it follows.

## What an empirical weight needs

A child's share of household spending cannot be read off a budget directly, because most goods are shared. Two standard methods:

| Method | Idea | Needs |
|---|---|---|
| **Engel** | A household with a child that spends the same food share as a childless household is *worse off*; the extra income that restores the share measures the child's cost | Household spending by composition |
| **Rothbarth** | Spending on **goods only adults consume** falls when a child arrives; the fall measures what the child takes | At least one adult-only good (the Bargain and Donni paper states this requirement) |

Results depend on the method. Oyama's study of Japanese panel data found that the traditional Rothbarth estimate implied modest child costs and a subjective-satisfaction scale implied much higher ones. Deaton and Muellbauer (1986) is the standard reference for the two methods; Oyama reports their Sri Lanka figure as 1.12 (unverified, from the Oyama paper's summary).

## What we can use

- **State the 0.3 as a declared convention** (Foundations §2.5), not as a result. It matches §2.5's rule: a division that cannot be measured is declared and labelled.
- **Test the weight on other countries' budget data.** Run a Rothbarth estimate on household budget surveys, and report the range by country and method. Sources for that are in [`Data_cross-country-time-use-and-expenditure-sources.md`](Data_cross-country-time-use-and-expenditure-sources.md).
- **Separate the three effects** the weight lumps together: goods consumed, care and schooling bought, and care labour given. Pledges.md §13.1's 0.3 covers the first two; the third is credit (Foundations §4.5).

## What it gets wrong / limitations

- A weight for **consumption** says nothing about **time**. Parents' care hours are credit, not debit, and need a time-use source.
- Weights from rich-country budget surveys may not hold where children work, where schooling is mostly private, or where extended households share goods.
- Child age matters. A flat 0.3 for 0–13 hides the gap between an infant (care-heavy) and a 12-year-old (food- and clothes-heavy).

## Sources

| Source | Link | Status |
|---|---|---|
| Hagenaars, de Vos, Zaidi (1994), *Poverty Statistics in the Late 1980s: Research Based on Micro-Data*, Eurostat | Not found online in this search | **Cited by others; not opened** |
| OECD Project on Income Distribution and Poverty, *What Are Equivalence Scales?* | The OECD URL I tried returned 404 | **Not opened. Find the current URL.** |
| Understanding Society, "Modified OECD equivalence scale" | <https://www.understandingsociety.ac.uk/?p=233576> | Seen in results only |
| INSEE, Martin, on equivalence scales | <https://www.insee.fr/en/statistiques/fichier/2647434/491-492_Martin_EN.pdf> | Seen in results only |
| BLS research paper on equivalence scales | <https://www.bls.gov/osmr/research-papers/2019/pdf/ec190090.pdf> | Seen in results only |
| *Journal of Social Policy*, "Minimum income standard and equivalisation" | <https://core-prod.cambridgecore.org/core/journals/journal-of-social-policy/article/minimum-income-standard-and-equivalisation-reassessing-relative-costs-of-singles-and-couples-and-of-adults-and-children/3B42D333207D0C9F0F0391143AC45E56> | Seen in results only |
| Bargain and Donni, IZA DP 4654 (later *European Economic Review* 2012), child costs with economies of scale | <https://econpapers.repec.org/RePEc:iza:izadps:dp4654> | Seen in results only |
| Oyama, Hitotsubashi DP 220, Japanese panel data | <https://www.ier.hit-u.ac.jp/pie/stage1/Japanese/discussionpaper/dp2004/dp220/text.pdf> | Seen in results only |
| Deaton and Muellbauer (1986), cost-of-children estimates | Not found | **Cited by Oyama; not opened** |

**Next step:** open the three primary documents marked *not opened* and replace this note's summaries with page-level quotations.

## Related

[[property-debit]] · `00-strategy/papers/Pledges.md` §13.1 · [`Data_american-time-use-survey-2023.md`](Data_american-time-use-survey-2023.md)
