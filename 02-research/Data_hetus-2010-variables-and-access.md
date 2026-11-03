# Data — HETUS 2010 microdata: which variables exist, and how to get the files

> **Version:** 0.1
> **Date:** 2026-11-02

**Type:** data source (codebook read) · **Retrieved:** 2026-11-02 · **Unit:** 10-minute diary slots, one record per person-day

| | |
|---|---|
| **Citation** | Eurostat. *HETUS 2010 Scientific Use File (SUF): variables description*, document F4, dated 23 January 2020. 51 pages |
| **URL** | <https://ec.europa.eu/eurostat/documents/203647/10397147/HETUS_variables+description.pdf/54efe947-767f-2e46-09ee-fc13688f04ac> |
| **Companion** | *HETUS anonymisation rules*: <https://ec.europa.eu/eurostat/documents/203647/10397147/HETUS_anonymisation+rules.pdf/d0ad6d6a-482a-a085-ca53-104a176eacae> (linked from the page; **not opened**) |
| **Access guide** | Eurostat, *Access to European microdata: procedures, guidance and forms*, 13 pages: <https://ec.europa.eu/eurostat/documents/203647/771732/How_to_apply_for_microdata_access.pdf> |
| **Landing page** | <https://ec.europa.eu/eurostat/web/microdata/harmonised-european-time-use-surveys> |
| **Read how** | Downloaded the PDF and converted it with `pdftotext`. The text was read in full around the household, lifecycle and "with whom" variables. **The tables are laid out in columns, so a few cells run together. Open the PDF before a sim cites a code.** |

## Why this matters to Aequitas

The target is **hours**. The sim `sr-20261102-single-parent-and-two-adult-yearly-balance-f` needs hours of childcare at home, by age of child, for parents in Europe. This note says exactly what the 2010 European files can give, and what they cannot.

## The answer, in plain words

**There is no "age of the youngest child" variable in the files researchers receive.** Eurostat deleted it on purpose, to protect privacy. Three coarser things remain.

| What exists | Variable | Codes | Use for the child sim |
|---|---|---|---|
| **Life-cycle group** | `INC3` (also called `HHG`) | 5 = single parent, youngest child under 18; 6 = person in a couple, youngest child 0–6; 7 = person in a couple, youngest child 7–17; others are no child under 18 | **The main handle.** Two age bands for couples (0–6, 7–17), one for single parents (under 18). It matches the two ATUS bands (under 6, 6–17) closely enough to compare |
| **Count of children, household** | `HHC3`: persons under 7; `HHC4`: persons 7–17; `HHC5`: persons 18 and over | `HHC3` top-coded at 2; `HHC4` and `HHC5` recoded to 0–2 | Tells a one-child home from a two-child home, up to 2 |
| **"With a household member up to 9 years", per 10-minute slot** | `Wchild001` to `Wchild144` | 1 = yes, blank = not ticked, −1 = sleeping, −6 = not asked, −9 = no answer | Marks the time a person spent in the company of a child under 10. This is **supervision time**, so it catches what ATUS primary activity misses |

**Deleted before release:** `HHC2` (age of the youngest person in the household), `HHQ1` (children in formal long-term care) and `HHQ2` (public or private child care). The last two are the nearest thing to a "purchased care" variable, and they are gone.

**Kept:** `HHQ10a`, *received help with childcare* (yes or no, not in hours), and `HHQ9_1`, household net monthly income in five bands.

## What the diary records

- `Mact001` to `Mact144`: main activity in each 10-minute slot, 144 slots from 04:00. HETUS Activity Coding List 2008, 108 three-digit codes.
- `Sact001` to `Sact144` and `Sactn001` to `Sactn144`: secondary activity, same list.
- Location, and "alone / with partner / with parent / with household member up to 9 years / with other household member", per slot.
- The childcare code is 38 in the HETUS list (mapped earlier to ICATUS division 41). **The code list itself is a separate document and was not opened.**

**Meaning for the hours target:** the files give both a floor (main activity) and a wider count (secondary activity, and slots "with a child up to 9"). Childcare hours can therefore be reported two ways. The gap between them is the supervision hours that ATUS Table 8A leaves out.

## Which countries and what is missing

17 countries hold microdata: AT, BE, DE, EE, EL, ES, FI, FR, HU, IT, LU, NL, PL, RO, UK, NO, RS.

| Footnote in the codebook | Effect |
|---|---|
| `INC3` (life cycle): "LU: not asked, NL: not possible to construct, BE, DE: in relation to the household reference person" | **Luxembourg has no life-cycle group, and the Netherlands cannot be built.** Belgium and Germany measure it against the reference person, not the respondent |
| `HHQ1` footnotes: AT, LU, NL, UK not asked; FI under 8 only | Moot, because `HHQ1` is deleted |
| Age of respondent (`INC2`): 5-year bands; DE cut at 75 and in age groups; LU 10–74; NO 10–80; FR from 11; RS 15+ | Coarse age; fine for a parent, rough for a grandparent |

## How to get the files

From the Eurostat access guide (last updated 18 September 2026 on its cover):

1. **Your organisation must first be recognised as a research entity.** Examples named: a university, research institution, a research department in a public administration, bank or statistical institute. It must have research as a main activity, show published research, be independent in its conclusions, and have data security. **This takes about 4 weeks and is done once.**
2. **Then submit a research proposal.** About 8 weeks.
3. **Eurostat sends the files** to the principal researcher. Access is for the period in the proposal. At the end, **the files and any confidential derived data must be destroyed**, and the results sent to Eurostat.

**What this means for Aequitas:** an independent author with no university or institute behind the project probably does not qualify. That is unconfirmed. Whether the project could partner with a recognised entity is a decision for the author. The files also cannot be kept on disk after the project, so the sim output would need to stay aggregate and the raw rows could not live in `06-simulation/data/`.

## What is public without any application

Eurostat publishes aggregate tables built from these files (`tus_00hhstatus`, `tus_00npaycare`, others; see the sources note). They give mean hours by household type, including couples with the youngest child under 7 and 7 to 17, and single parents. **The tables were listed in search results and were not opened in this pass.** They are the realistic European source for the child sim until access is settled.

## Limits

- **No exact child age.** Two bands for couples, one for single parents. The request wanted 0–4, 5–11 and 12–13. The 2010 European files cannot split them. Nor can the public tables.
- **Purchased childcare cannot be measured here.** The two childcare variables were deleted, so the "daycare is no longer a parent debit" effect cannot be sized from HETUS. A separate source is needed (OECD Family Database, or Eurostat childcare-use tables).
- **Parents are not marked.** The life-cycle group tells you a person lives with a child in the stated age range, in a couple or alone. It does not say the child is the person's own.
- **Old data.** Collected 2008–2015, released 2020. The 2020 round arrives in 2027 at the earliest.
- **Access takes about 12 weeks and may be refused.**

## Related

[[property-debit]] · [`Data_cross-country-time-use-and-expenditure-sources.md`](Data_cross-country-time-use-and-expenditure-sources.md) · [`Data_atus-childcare-by-age-of-youngest-child.md`](Data_atus-childcare-by-age-of-youngest-child.md) · [`Method_oecd-modified-equivalence-scale.md`](Method_oecd-modified-equivalence-scale.md)
