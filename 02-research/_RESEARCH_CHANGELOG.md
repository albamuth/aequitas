# Research Archive — Changelog

Single log for all changes to documents in `02-research/`. Newest entries at the top.
Backups of every pre-rewrite version live in `02-research/archive/`.

---

## 2026-08-23 — Two new data notes for the economy simulator, and four missing source-index rows

**Both new files serve the simulator's consumer cohorts** ([`06-simulation/KERNEL_PLAN_v0.2.md`](../06-simulation/KERNEL_PLAN_v0.2.md)).

| New file | What it settles |
|---|---|
| [`Data_consumer-segmentation-archetypes_v0.1.md`](Data_consumer-segmentation-archetypes_v0.1.md) | Where cohort profiles come from. Surveys that carry quantities (BLS CE, Eurostat HBS, World Bank Global Consumption Database, LIS) against marketing systems that do not. **Ruling: an archetype may name a cohort; it may never supply a number.** |
| [`Data_labour-and-pollution-intensity_v0.1.md`](Data_labour-and-pollution-intensity_v0.1.md) | Turning survey dollars into hours. **Spend × intensity, and the dollars cancel.** The BLS Employment Requirements Matrix and EXIOBASE are the tables; the CE-to-industry bridge is the hard part; the price-split bias and the coverage gap **both point the same way, so every figure is a floor.** |

**The archetype ruling is the substantive one.** The twelve Jungian marketing archetypes were raised as a possible basis for consumer types. **They carry no consumption quantities and there is no evidence they predict any** — they were built to help a brand choose a voice. Letting one set a number would put a marketing construct inside a materialist accounting, which is **A1** violated in our own instrument. **They keep a narrow and real job: making a cohort readable on a screen, and giving the culture dial a vocabulary.** The numbers underneath still come from household surveys.

**Source index repaired.** [`GLOSSARY.md`](../00-strategy/GLOSSARY.md) → **v0.3**. The index had drifted behind this folder — **cross-country labour efficiency** and the **GDPR erasure note** existed as files with no row. Added those two plus the two above, and a new [Simulation, cohort, and data terms](../00-strategy/GLOSSARY.md#simulation-terms) table (13 rows, each with a hidden anchor) covering cohort, exemplar consumer, headcount weight, archetype, brand personality, psychographic segmentation, intensity, ERM, CE, HBS, participation rate, coverage floor, and price-split bias.

**⚠️ One blocking gap recorded, not solved.** The 1% coverage cut needs a **participation rate** — what share of households bought a thing at all. **The BLS release gives mean spend and never says that.** Until the number is found, the cut is an intention rather than a working rule.

---

## 2026-08-13 — Versioned filenames + glossary single-indirection

**Renamed every research file to `Author_topic_vX.Y.md`** (author-first; `Category_topic_vX.Y.md` — `Data_`, `History_`, `Problem_`, `Review_` — for the no-author notes). Rewritten stubs are `_v0.2`; the six new figure pages and the new **Dapprich** page are `_v0.1`.

**New indirection architecture (mirrors the acronym registry):** the versioned filename now lives in exactly **one** place — the [Research source index](../00-strategy/GLOSSARY.md#research-sources) in `GLOSSARY.md`. Every other document (main strategy docs, wiki, sims, and the research files' own cross-links) points to a **stable `#src-…` anchor** in the glossary, never to a research file directly. A version bump now touches **one glossary cell** instead of dozens of links. 39 files were rewired; journal and `99-archive` left frozen as historical record.

**Also new:** [`Dapprich_optimal-planning_v0.1.md`](../02-research/Dapprich_optimal-planning_v0.1.md) — the timeline referenced Dapprich but had no page. GLOSSARY.md gained a table-of-contents and the source index.

---

## 2026-08-13 — Legibility rewrite pass (all stubs → v0.2)

**What and why.** Every research stub was rewritten for a layperson audience, in the style of the [Overview](../00-strategy/Aequitas_Overview_v0.10.md): no economics or academic jargon left undefined, no bare acronyms, every Aequitas concept stipulated in plain words on the page where it's used, and links to the [Foundations](../00-strategy/Aequitas_Foundations_v0.13.md) pointed at a *specific* section rather than the document as a whole. Where a stub leaned on the Objections register, the objection is now spelled out in full instead of referenced by code. Each document was given a **Version** field (first versioned edition = **0.2**); the prior version is preserved in `archive/`.

## 2026-08-13 — Six new research pages (timeline expansion)

Added stubs (v0.1) for figures added to the economic-theory timeline, each verified against a non-paywalled source via WebFetch and written in the same legible register:

| New file | Anchors it feeds |
|---|---|
| `keynes-general-theory` | Overview §2 (debt); §A3 (no creditor → no debt spiral). |
| `polanyi-great-transformation` | "fictitious commodities" land/labour/money → §3.7 / §A2 / §A1 (independent corroboration of three axioms at once). |
| `henry-george-land` | §3.7 (land not owned; remediation debt); §7.1 (no rent). |
| `veblen-conspicuous-consumption` | §3.2 (consumption debit); §7.1; bridge to [Technocracy: energy accounting](../00-strategy/GLOSSARY.md#src-technocracy-energy-accounting). |
| `bookchin-social-ecology` | §8 positioning (keep the municipality); §A4 (no externalities). |
| `graeber-debt` | Overview §2; §A3; the barter-myth prop under money. |

Timeline SVG [`01-wiki/assets/economic-theory-timeline.svg`](../01-wiki/assets/economic-theory-timeline.svg) rebuilt from 30 → 37 nodes (also added Ricardo as a value-lineage bridge node, no page). GLOSSARY.md gained rows for fictitious commodities, Georgism, conspicuous consumption, industry-vs-business, social ecology, libertarian municipalism, Keynesian aggregate demand, and the myth of barter.

---

## 2026-08-13 — Legibility rewrite pass (all stubs → v0.2)

Per-file notes below. **Every file went v0.1 → v0.2**; every v0.1 backup is in `archive/` as `<name>_v0.1.md`.

| File | Notes on the rewrite |
|---|---|
| `delanda-markets-antimarkets` | Stipulated "market vs. antimarket," "price-setter vs price-taker," "meshwork/hierarchy." Foundations links pointed at §A5 and §7.1. |
| `warren-cost-the-limit-of-price` | Explained labour notes, "toil and trouble," mutualism inline. Links → §A2, §A5. |
| `neurath-calculation-in-kind` | "Calculation in kind," commensurability, Mises/Hayek all spelled out. The weakest-link objection re-expressed as "whose want wins," with the pledges/floor mechanisms named in plain words; links → §A1, §A4, §A6, §6.4, §7.5. Noted OP-9 reply now exists. |
| `technocracy-energy-accounting` | Energy certificates, EROI, "rule by experts" glossed. Links → §A1, §A3, §A8, §10. |
| `saadia-trekonomics` | Recognition/feedback framing put in plain words; links → §6.3, §7.4, §10. |
| `proudhon-mutualism` | possession/property, "dead labour," People's Bank glossed; the "isn't this just mutualism?" answer stated via §A3. Links → §A5, §3.2, §7.1, §A2, §A3. |
| `participatory-economics` | Parecon's four institutions, "coordinator class," indicative prices, balanced job complexes all explained; objection codes replaced with prose + links → §10, §7.4, §6.4, §7.5. |
| `cockshott-cottrell-labour-time` | Sparse-matrix method, the price/value demand lever, "contamination" all in plain words; the demand-side gap answered via pledges (§6.4) + OP-9 reply. Links → §A3, §A5, §3.3. |
| `kantorovich-shadow-prices` | Shadow prices reframed as "pricing scarcity without profit"; scarcity-as-debit spelled out; objective-function trap tied to the "who controls the cost model" open problem (§10). Links → §A5, §A4, §A1. |
| `ellerman-labor-theory-of-property` | Responsibility-imputation, inalienable rights, de facto/de jure firm all glossed; the team-splitting limit tied to §10 and §1.1 (named conventions). Links → §A1, §A3. |
| `local-currency-experiments` | Retitled the three failure classes as plain "three ways these things die"; mutual credit, demurrage, double-coincidence explained. Links → §A3, §7.6, §6.2, §11, §4. |
| `joint-production-allocation-problem` | "Carrier vs denominator," negative labour values, ISO hierarchy, avoided-burden all put in plain words; links → §A2, §3.4a, §6.2b, §1.1, §10. Noted recursion sim since passed. |
| `estimation-engine-data-sources` | Added a plain-language jargon preface; EEIO, Leontief/input-output, satellite accounts, PIOT, LCA all stipulated at first use. The price-allocation clash tied to §A5/§A1/§A6. Kept all working tables and links. |
| `refinery-process-energy` | Btu/bbl/TBtu units glossed; measured-vs-declared channel tied to the physical-trace test; retained the DOE data tables as reference. Links → §3.4a. |
| `auditor-independence` | Retitled "who watches the watchers"; issuer-pays, the directional-conflict finding, rival-sector audit all in prose; objection codes replaced with §3.3a/§10 links. |
| `plastic-lca-and-cleanup-cost` | Units (MJ/kg, t, $/ton) and LCA/GPGP glossed; tied to §3.5 (stock rule) and §3.6 (recycling). |
| `external-critique-2026-08-09` | Faithfully re-presented with every internal code spelled out; added a closing "what the project did in response" section. |

