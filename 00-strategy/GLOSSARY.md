# Aequitas — Acronym Registry & Glossary

> **Version:** 0.3 · **Date:** 2026-08-23 · **Status:** canonical index
> **Why this exists:** the [external critique](#src-external-critique-2026-08-09) flagged abbreviation density (OP-#, C#, IC-#, A#, P#, §x.x) with no master index as the #1 accessibility barrier. This is that index, and the resolution target for the acronym-titling pass in `NEXT.md`.
> **v0.3 (2026-08-23):** added the [Simulation, cohort, and data terms](#simulation-terms) table — the vocabulary the economy simulator introduced — and **four missing rows to the source index**, which had drifted behind `02-research/`: cross-country labour efficiency, the GDPR erasure note, and two new files on consumer segmentation and on labour/pollution intensity.
> **v0.2 (2026-08-13):** added the [Research & academic terms](#research-terms) table — the outside vocabulary (economic theory, alternative-currency history, accounting method) used across `02-research/`, each with a plain definition, the research doc that best explains it, and an external authoritative (non-paywalled) source. Every definition below was checked against its linked source on 2026-08-13.

## Contents

- [How to use this file](#how-the-acronym-titling-pass-uses-this-file)
- [The `A#` collision (resolved)](#the-a-collision--resolved-2026-08-09)
- [Axioms (A1–A8)](#axioms)
- [Components (C1–C12)](#components)
- [Integrity constraints (IC-1–IC-12)](#integrity-constraints)
- [Open problems (OP-#)](#open-problems)
- [Objection analysis-sections (OA0–OA11)](#objection-analysis-sections)
- [Legacy problem-codes (P#)](#legacy-problems)
- [Research & academic terms](#research-terms)
  - [**Research source index** — every research file, latest version](#research-sources)
  - [Simulation, cohort, and data terms](#simulation-terms)
  - [Value, property, and markets](#research-terms)
  - [Calculation and planning](#research-terms)
  - [Energy and material accounting](#research-terms)
  - [Alternative-currency history and institutions](#research-terms)
- [Maintenance](#maintenance)

---

## How the acronym-titling pass uses this file
Each acronym in the body docs gets a **1–3 word title appended in-line, hyperlinked to its row *here***, e.g.:

> …resolved by **OP-9 ([the calculation reply](GLOSSARY.md#op-9))**…

**Link to this glossary, not directly to the source doc.** The source docs are version-stamped (`Foundations_v0.16`), so direct links rot on every fold. This file is the *single indirection*: the in-text link points here, and the row below points onward to the current versioned doc. On a fold, update the target in **one** place — here — instead of hundreds of in-text links.

## The `A#` collision — RESOLVED 2026-08-09
Formerly `A#` meant two things: a Foundations **axiom** *and* an Objections **analysis section**. The Objections analysis sections were renamed **`A#` → `OA#`** (Objection Analysis) to end the collision. The rule is now clean:
- **`A1`–`A8` = an axiom, always.** (Foundations §1.) → [`#axioms`](GLOSSARY.md#axioms)
- **`OA0`–`OA11` = an Objections analysis section** (Part A), each tied to an Open Problem. → [`#objection-analysis-sections`](GLOSSARY.md#objection-analysis-sections)
- **`B#` = an answered objection** (Objections Part B).

*Legacy note for the append pass:* any surviving `A9/A10/A11` in an un-migrated doc is an **old analysis-section ref** (there is no axiom above A8) → rewrite to `OA9/OA10/OA11`. An `A1`–`A8` in a doc **other than Objections** is almost always an axiom — read the context before touching it.

---

## <a id="axioms"></a>Axioms (A1–A8) — Foundations §1
The fixed core. Do not re-litigate (see `CLAUDE.md`).

| Acronym | Title (1–3 words) | Statement | Source |
|---|---|---|---|
| <a id="a1"></a>**A1** | materialism of cost | Cost **is** material/energy flow. | Foundations §1 |
| <a id="a2"></a>**A2** | time as measure | Time is a yardstick, not the substance; labour never rate-scaled *(amended v0.3)*. | Foundations §1 |
| <a id="a3"></a>**A3** | non-fungibility | Credit is non-transferable; no medium of exchange. | Foundations §1 |
| <a id="a4"></a>**A4** | no externalities | Every cost is accounted to whoever caused it; nothing escapes. **On *a* ledger — never necessarily the product's.** *(Eroded by OP-24 — see note.)* | Foundations §1 |
| <a id="a5"></a>**A5** | **cost, not price** | A thing's cost is what was **consumed** to make it. Nothing is added (no margin, no profit in exchange) and nothing enters that the thing did not consume — so a durable asset is **never amortised into what it made** (§4.5). The figure is a dated estimate, not a verdict. *(Renamed in Foundations v0.21; it read "price ≡ cost", which contradicted §4.5. See Objections B8.)* | Foundations §1 |
| <a id="a6"></a>**A6** | derived, not stored | The ledger is computed from the event log on demand. | Foundations §1 |
| <a id="a7"></a>**A7** | universal accounting | Work is recorded universally; credit *realized* voluntarily *(amended v0.2)*. | Foundations §1 |
| <a id="a8"></a>**A8** | no governing body | Governance is a protocol property with open variance, not a central institution. | Foundations §1 |

---

## <a id="components"></a>Components (C1–C12) — the spec build list, Strategy §3

| Acronym | Title (1–3 words) | Meaning | Status |
|---|---|---|---|
| <a id="c1"></a>**C1** | event-log schema | The data model. | ✅ v0.3 |
| <a id="c2"></a>**C2** | verification / trust networks | 4-level verification; Level-2 trust-network shape. | Partial (straw-man pulled forward) |
| <a id="c3"></a>**C3** | estimation engine | Global-avg → cohort → individual (OP-3). | In progress |
| <a id="c4"></a>**C4** | re-weighting | Re-weighting + conservative weighting. | Not started |
| <a id="c5"></a>**C5** | debit taxonomy | Property vs consumption; transfer rules; pledge discharge. | Partial |
| <a id="c6"></a>**C6** | identity | Proof-of-personhood; one human, one account. | Not started |
| <a id="c7"></a>**C7** | privacy layer | Privacy + minimum audit disclosure (OP-22). | Not started |
| <a id="c8"></a>**C8** | influence mechanics | OP-1 + feedback aggregation (OP-6). | Partial |
| <a id="c9"></a>**C9** | debit-tolerance formula | The OP-4 tolerance formula. | Not started |
| <a id="c10"></a>**C10** | cross-level trade | OP-7; deferred to v2. | Not started |
| <a id="c11"></a>**C11** | arithmetic audits | IC-1…IC-12 as runnable checks. | ✅ Closed |
| <a id="c12"></a>**C12** | energetics registry | Per-process data + rival-audit rules; home of OP-24. | New |

---

## <a id="integrity-constraints"></a>Integrity Constraints (IC-1–IC-12) — Conformance
**Arithmetic the ledger must never violate.** IC-1…IC-9 check the record itself and are pure arithmetic. IC-10…IC-12 check a figure computed from it against a weighting model. **The `Source` column gives the conformance row each one is now stated in** (`Aequitas_Conformance_v0.11.md` §2).

| Acronym | Title (1–3 words) | Constraint | Source |
|---|---|---|---|
| <a id="ic-1"></a>**IC-1** | mass balance | Σ input mass = Σ output mass. | Conformance row 7 |
| <a id="ic-2"></a>**IC-2** | energy balance | Σ input energy = Σ output + declared dissipation. | Conformance row 7 |
| <a id="ic-3"></a>**IC-3** | origin closure | Every parcel traces to a reservoir extraction or a genesis terminus. | Conformance row 7 |
| <a id="ic-4"></a>**IC-4** | fate closure | Every parcel is held, consumed, or released; else *unaccounted*. | Conformance row 7 |
| <a id="ic-5"></a>**IC-5** | custody continuity | One holder at any instant; every hand-off is an event. | Conformance row 7a |
| <a id="ic-6"></a>**IC-6** | interval sanity | No consuming a parcel before it exists or after it's destroyed. | Conformance row 7 |
| <a id="ic-7"></a>**IC-7** | 24-hour cap | Agent-time can't exceed wall-clock; ≤24h credited per 24h. | Conformance row 8 |
| <a id="ic-8"></a>**IC-8** | pledge backing | **Cumulative** pledged hours ≤ **lifetime** earned credit (no fractional reserve). The budget is spent at pledge time and never returned. | Conformance row 9 |
| <a id="ic-9"></a>**IC-9** | pledge discharge | On occurrence, a held object's debit follows possession to whoever accepts it (not necessarily the pledger); a pure service moves none. Pledges are **permanent and non-revocable** (§4.6); an unfulfilled pledge burns, it is not returned. | Conformance row 9 |
| <a id="ic-10"></a>**IC-10** | non-negative allocation | No output's share of any dimension is negative. | Conformance row 10b |
| <a id="ic-11"></a>**IC-11** | exhaustive allocation | Per dimension, shares sum to the recorded input total. | Conformance row 10c |
| <a id="ic-12"></a>**IC-12** | boundary additivity | Stage-by-stage split = whole-process split (anti-gerrymandering). | Conformance row 10d |

---

## <a id="open-problems"></a>Open Problems (OP-#) — Objections register
Series is non-contiguous (early merges left gaps at OP-2/12/13). Status taxonomy being standardized to **CLOSED / DISSOLVED / MITIGATED / OPEN** (Accessibility track).

| Acronym | Title (1–3 words) | Problem | Status |
|---|---|---|---|
| <a id="op-1"></a>**OP-1** | service → influence | How service work converts to influence without becoming a currency. | 🟠 Open |
| <a id="op-3"></a>**OP-3** | estimation convergence | Does estimation converge from cohort average to individual truth? (C3) | In progress |
| <a id="op-4"></a>**OP-4** | debit tolerance | The per-person tolerance floor + efficiency ratio (no global ratio). (C9) | Open |
| <a id="op-5"></a>**OP-5** | education cost | Perpetual-studenthood exploit. | ✅ Dissolved (B3, front-loading) |
| <a id="op-6"></a>**OP-6** | feedback mechanics | Feedback aggregation + signal flooding. | 🟠 Open |
| <a id="op-7"></a>**OP-7** | cross-level trade | Fairness of trade across verification levels. | Open (v2) |
| <a id="op-8"></a>**OP-8** | feedback firewall | Can feedback be bought? (a purchasable signal = back-door currency). | ✅ Dissolved (B4) |
| <a id="op-9"></a>**OP-9** | calculation reply | Preference revelation / the Mises–Hayek critique (= P5). | 🟠 Substantially answered, needs writing up |
| <a id="op-10"></a>**OP-10** | weighting governance | Who governs the weighting model (= P8). | 🔴 Top blocker |
| <a id="op-11"></a>**OP-11** | training amortization | Choosing a training-cost denominator. | ✅ Dissolved (B3, front-loading) |
| <a id="op-14"></a>**OP-14** | cohort shopping | Joiners self-identify into a favourable cohort / floor. | Open |
| <a id="op-15"></a>**OP-15** | ghost harvesting | Estimated credit accrues to non-joiners and the dead. | Open |
| <a id="op-16"></a>**OP-16** | onerousness gap | Tedium/indignity have no material signature. | 🔴 Underweight, unsolved *(re-rated 2026-08-09)* |
| <a id="op-17"></a>**OP-17** | joint production | Allocating a joint process's debit across co-products. | ✅ Closed — the split follows **where the process physically sent its inputs**; measurement constrains the choice without determining it (B7) |
| <a id="op-18"></a>**OP-18** | labour & team credit | Responsibility/labour split across co-products and teams. | ✅ Closed (B9) |
| <a id="op-19"></a>**OP-19** | saturated producer | What surplus production is for. | ✅ Resolved by pledges (B5) |
| <a id="op-20"></a>**OP-20** | unobservable work | Crediting work that leaves no trace. | ✅ Closed (IC-7 + conservative weighting) |
| <a id="op-21"></a>**OP-21** | media reproduction | Charging for infinitely-copyable media. | ✅ Dissolved (B3, front-loading) |
| <a id="op-22"></a>**OP-22** | audit disclosure | The minimum zero-knowledge disclosure set. (C7) | 🔽 Load-bearing — gates the disparity ceiling & anti-arbitrage |
| <a id="op-23"></a>**OP-23** | shared overhead | Attributing capital/overhead across co-products. | ✅ Closed — accrues to the asset (B8) |
| <a id="op-24"></a>**OP-24** | understatement drift | Cost errors that favour subscribers have no funder. | 🔴 Fix proposed (rival-audit), unproven |
| <a id="op-25"></a>**OP-25** | illicit dumping | Abandonment/end-of-life attribution. | 🔽 New, minor (Level-2) |
| <a id="op-28"></a>**OP-28** | residual denominator | What `(N − Y)` is divided by. A headcount where §2.5 requires a measurement. | 🟠 Open — candidate repair unmeasured |

---

## <a id="objection-analysis-sections"></a>Objection analysis-sections (OA0–OA11) — Objections Part A
**Not axioms** (renamed from `A#` on 2026-08-09). Internal IDs for the write-up of each live objection.

| ID | Addresses | ID | Addresses |
|---|---|---|---|
| <a id="oa0"></a>OA0 | field record (no OP) | <a id="oa6"></a>OA6 | OP-6 |
| <a id="oa1"></a>OA1 | OP-18 *(→ B9)* | <a id="oa7"></a>OA7 | P4 (coordinator class) |
| <a id="oa2"></a>OA2 | OP-10 / P8 | <a id="oa8"></a>OA8 | OP-9 / P5 |
| <a id="oa3"></a>OA3 | OP-24 | <a id="oa9"></a>OA9 | OP-22 |
| <a id="oa4"></a>OA4 | OP-23 *(→ B8)* | <a id="oa10"></a>OA10 | auditor independence |
| <a id="oa5"></a>OA5 | OP-16 | <a id="oa11"></a>OA11 | OP-25 |

*(B-series: B3 front-loading, B4 one-credit/three-channels, B5 misc, B7 OP-17, B8 OP-23, B9 OP-18, B10 credit-realization, B11 self-care — resolution write-ups in Objections Part B.)*

---

## <a id="legacy-problems"></a>Legacy problem-codes (P#) — original critique
Early problem list; several merged into the OP series.

| Acronym | Title | Now |
|---|---|---|
| <a id="p4"></a>**P4** | coordinator class | 🟠 Open (coordination residual only) |
| <a id="p5"></a>**P5** | preference revelation | = OP-9 |
| <a id="p7"></a>**P7** | theory of value | ✅ Adopted (Ellerman imputation) |
| <a id="p8"></a>**P8** | weighting governance | = OP-10 |
| <a id="p9"></a>**P9** | local-currency read | ✅ Fixed (the overlay computes what money can't) |

---

## <a id="research-terms"></a>Research & academic terms — the outside vocabulary

The economic-theory, historical, and accounting language that appears across `02-research/`. Each row gives a plain 1–3 sentence definition, the **research doc** that explains it in Aequitas's own terms, and an **external authoritative source** (all non-paywalled). Definitions were verified against the external source on 2026-08-13.

The "in our research" links point to the **source index** just below — the single place that carries each research file's *versioned* filename. Every other document in the project links to these `#src-…` anchors, never to a research file directly, so a research-file version bump only ever needs updating **here**.

### <a id="research-sources"></a>Research source index — the one place with the versioned filenames

> **Maintenance rule:** when a research file is version-bumped and renamed, update its **Full file** link in this table only. All in-text references across the project point to the stable `#src-…` anchors in the first column, so nothing else needs touching.

| Source | One-line answer | Full file (current version) |
|---|---|---|
| <a id="src-warren-cost-the-limit-of-price"></a>**Warren — Cost the Limit of Price** | The only real shop run at cost with no profit (1827–30); it broke on the skill/effort problem Aequitas's time-measure is built to solve. | [Warren_cost-the-limit-of-price_v0.2](../02-research/Warren_cost-the-limit-of-price_v0.2.md) |
| <a id="src-proudhon-mutualism"></a>**Proudhon — mutualism** | Rent, interest, and profit as extraction; possession vs. property. His remedy was a currency — the failure Aequitas's non-transferable credit avoids. | [Proudhon_mutualism_v0.2](../02-research/Proudhon_mutualism_v0.2.md) |
| <a id="src-delanda-markets-antimarkets"></a>**DeLanda — markets & antimarkets** | Braudel's two layers: a market is not capitalism. Aequitas dissolves the price-*setters* and keeps ordinary commerce. | [DeLanda_markets-antimarkets_v0.2](../02-research/DeLanda_markets-antimarkets_v0.2.md) |
| <a id="src-henry-george-land"></a>**Henry George — land & rent** | Rent captures the gains of progress, causing poverty amid growth; the pedigree for Aequitas's "you don't own the land." | [George_land-and-rent_v0.1](../02-research/George_land-and-rent_v0.1.md) |
| <a id="src-neurath-calculation-in-kind"></a>**Neurath — calculation in kind** | Plan in physical units, not money; provoked the Mises/Hayek "you can't calculate without prices" critique Aequitas must answer. | [Neurath_calculation-in-kind_v0.2](../02-research/Neurath_calculation-in-kind_v0.2.md) |
| <a id="src-veblen-conspicuous-consumption"></a>**Veblen — conspicuous consumption** | Display-waste, and industry-vs-business; named what consumption-debit exposes and seeded the Technocracy movement. | [Veblen_conspicuous-consumption_v0.1](../02-research/Veblen_conspicuous-consumption_v0.1.md) |
| <a id="src-technocracy-energy-accounting"></a>**Technocracy — energy accounting** | Nearest relative that died: money replaced by energy certificates; the cautionary tale for "no organisation owns the core." | [Technocracy_energy-accounting_v0.2](../02-research/Technocracy_energy-accounting_v0.2.md) |
| <a id="src-keynes-general-theory"></a>**Keynes — the General Theory** | Demand drives output; the debt economy Aequitas's §2 answers. With no transferable credit there is no creditor, so no debt spiral. | [Keynes_general-theory_v0.1](../02-research/Keynes_general-theory_v0.1.md) |
| <a id="src-kantorovich-shadow-prices"></a>**Kantorovich — shadow prices** | Pricing scarcity as a computed cost, not a profit — the template for Aequitas's scarcity-as-debit. | [Kantorovich_shadow-prices_v0.2](../02-research/Kantorovich_shadow-prices_v0.2.md) |
| <a id="src-polanyi-great-transformation"></a>**Polanyi — The Great Transformation** | Land, labour, and money are "fictitious commodities" — independent backing for three Aequitas axioms at once. | [Polanyi_great-transformation_v0.1](../02-research/Polanyi_great-transformation_v0.1.md) |
| <a id="src-cockshott-cottrell-labour-time"></a>**Cockshott & Cottrell — labour-time** | Showed physical-unit planning is computable at national scale; answers the "too big to compute" objection. | [Cockshott_Cottrell_labour-time_v0.2](../02-research/Cockshott_Cottrell_labour-time_v0.2.md) |
| <a id="src-participatory-economics"></a>**Albert & Hahnel — Participatory Economics** | Closest living non-market model; source of the coordinator-class and unpleasant-work challenges. | [Albert_Hahnel_participatory-economics_v0.2](../02-research/Albert_Hahnel_participatory-economics_v0.2.md) |
| <a id="src-ellerman-labor-theory-of-property"></a>**Ellerman — labour theory of property** | Grounds Aequitas's attribution in responsibility (not Marx's value theory); exposes the team-splitting limit. | [Ellerman_labor-theory-of-property_v0.2](../02-research/Ellerman_labor-theory-of-property_v0.2.md) |
| <a id="src-bookchin-social-ecology"></a>**Bookchin — social ecology** | Ecological harm is a social problem; libertarian municipalism is the home for "keep the municipality, change its economics." | [Bookchin_social-ecology_v0.1](../02-research/Bookchin_social-ecology_v0.1.md) |
| <a id="src-saadia-trekonomics"></a>**Saadia — Trekonomics** | Post-scarcity as an "organisational option" — an on-ramp for public writing, not a mechanism. | [Saadia_trekonomics_v0.2](../02-research/Saadia_trekonomics_v0.2.md) |
| <a id="src-graeber-debt"></a>**Graeber — Debt** | Credit predates barter and coinage; removes the standard argument that a transferable money is necessary. | [Graeber_debt_v0.1](../02-research/Graeber_debt_v0.1.md) |
| <a id="src-dapprich-optimal-planning"></a>**Dapprich — optimal planning** | Latest computational planner: scarcity shadow-values + a consumer-feedback loop — the live cousin of Aequitas's pledges. | [Dapprich_optimal-planning_v0.1](../02-research/Dapprich_optimal-planning_v0.1.md) |
| <a id="src-local-currency-experiments"></a>**Local-currency field record** | A century of Ithaca / Wörgl / WIR: three ways alt-money dies. Aequitas is structurally immune to the circulation death. | [History_local-currency-experiments_v0.2](../02-research/History_local-currency-experiments_v0.2.md) |
| <a id="src-auditor-independence"></a>**Auditor independence** | Issuer-pays conflict (Enron, credit ratings) killed the "networks compete on accuracy" claim; rival-sector audit adopted instead. | [History_auditor-independence_v0.2](../02-research/History_auditor-independence_v0.2.md) |
| <a id="src-joint-production-allocation-problem"></a>**Joint-production problem** | When one process makes several things: Sraffa's negative values, solved by measuring where the process physically sent its inputs. | [Problem_joint-production-allocation_v0.2](../02-research/Problem_joint-production-allocation_v0.2.md) |
| <a id="src-estimation-engine-data-sources"></a>**Estimation-engine data sources** | The datasets and models (input–output, EEIO, EXIOBASE, US surveys) for computing a thing's true cost — and the price-allocation clash and its fix. | [Data_estimation-engine-sources_v0.2](../02-research/Data_estimation-engine-sources_v0.2.md) |
| <a id="src-refinery-process-energy"></a>**Refinery process energy** | Real US energy tables splitting a refinery fuel-by-fuel — the worked joint-production example. | [Data_refinery-process-energy_v0.2](../02-research/Data_refinery-process-energy_v0.2.md) |
| <a id="src-plastic-lca-and-cleanup-cost"></a>**Plastic LCA & cleanup** | Energy to make vs. recycle plastic, plus ocean-cleanup cost; anchors the permanent-pollution-debt result. | [Data_plastic-lca-cleanup_v0.2](../02-research/Data_plastic-lca-cleanup_v0.2.md) |
| <a id="src-external-critique-2026-08-09"></a>**External critique (2026-08-09)** | First outside review; it validated the risk register and set the Mises/Hayek-reply priority. | [Review_external-critique-2026-08-09_v0.2](../02-research/Review_external-critique-2026-08-09_v0.2.md) |
| <a id="src-cross-country-labour-efficiency"></a>**Cross-country labour efficiency** | The US commands 50–80% more embodied labour and 2.5–4× the CO₂ per head than Germany, Sweden, France, Japan or Spain for a comparable standard. What the simulator's locale dial must reproduce. | [Data_cross-country-labour-efficiency_v0.1](../02-research/Data_cross-country-labour-efficiency_v0.1.md) |
| <a id="src-consumer-segmentation-archetypes"></a>**Consumer segmentation & archetypes** | Where cohort profiles come from — household surveys carry quantities, marketing archetypes carry only names. **An archetype may name a cohort; it may never supply a number.** | [Data_consumer-segmentation-archetypes_v0.1](../02-research/Data_consumer-segmentation-archetypes_v0.1.md) |
| <a id="src-labour-and-pollution-intensity"></a>**Labour & pollution intensity** | Turning survey dollars into hours, kilograms and megajoules: spend × intensity, the dollars cancel. Carries the price-split bias and why every figure it produces is a floor. | [Data_labour-and-pollution-intensity_v0.1](../02-research/Data_labour-and-pollution-intensity_v0.1.md) |
| <a id="src-gdpr-right-to-erasure"></a>**GDPR right to erasure** | Erasure is not absolute; three of Article 17's five exemptions apply, and the research exemption carries no time limit. Out of scope per §2.6 — checked anyway. | [Law_gdpr-right-to-erasure_v0.1](../02-research/Law_gdpr-right-to-erasure_v0.1.md) |

### <a id="simulation-terms"></a>Simulation, cohort, and data terms

The vocabulary the economy simulator introduced. **Every row carries a hidden anchor**, so any document can link straight to a definition — e.g. `[cohort](GLOSSARY.md#term-cohort)`.

| Term | Short definition | In our research | Authoritative source |
|---|---|---|---|
| <a id="term-cohort"></a>**Cohort** | A group of people the simulator treats as identical, sharing one consumer type, one birth period, and one locale. Carries a headcount rather than existing as separate individuals. | [segmentation](#src-consumer-segmentation-archetypes) | [Cohort (statistics)](https://en.wikipedia.org/wiki/Cohort_(statistics)) |
| <a id="term-exemplar-consumer"></a>**Exemplar consumer** | The single modelled person who stands for a whole cohort. If 30% of the population is type A, the type-A exemplar's rows are the basis for 30% of everyone. | — | — |
| <a id="term-headcount-weight"></a>**Headcount weight** | The column on an event-log row saying how many real people that row speaks for. At a weight of 1 the simulator models individuals. | — | — |
| <a id="term-consumer-archetype"></a>**Consumer archetype** | One of twelve brand personalities (Innocent, Hero, Outlaw, Caregiver…) adapted from Jung by Mark & Pearson. **A naming device. It carries no consumption quantity and there is no evidence it predicts one.** | [segmentation §4](#src-consumer-segmentation-archetypes) | [Jungian archetypes](https://en.wikipedia.org/wiki/Jungian_archetypes) · [practitioner guide](https://octopusandson.com/marketing-archetypes-guide/) |
| <a id="term-brand-personality"></a>**Brand personality** | Aaker's five-dimension scale — sincerity, excitement, competence, sophistication, ruggedness. The nearest academically validated relative of the archetypes. Measures perception, not throughput. | [segmentation §4](#src-consumer-segmentation-archetypes) | [Wikipedia](https://en.wikipedia.org/wiki/Brand_personality) |
| <a id="term-psychographic-segmentation"></a>**Psychographic segmentation** | Grouping people by values and motivation rather than by age or income. VALS and PRIZM are the working systems. | [segmentation §3](#src-consumer-segmentation-archetypes) | [VALS](https://www.strategicbusinessinsights.com/vals/) |
| <a id="term-intensity"></a>**Intensity** | How much labour, pollution, or material sits behind one dollar of spending in a sector. **Spend × intensity = hours; the dollars cancel.** | [intensity](#src-labour-and-pollution-intensity) | [Input–output model](https://en.wikipedia.org/wiki/Input%E2%80%93output_model) |
| <a id="term-erm"></a>**ERM** — Employment Requirements Matrix | The BLS table giving jobs and hours needed, directly and through the whole supply chain, per million dollars of final demand by industry. **The US labour intensity source.** | [intensity §2](#src-labour-and-pollution-intensity) | [BLS](https://www.bls.gov/emp/data/input-output-matrix.htm) *(unverified — withdrawn once, 2026-02-06)* |
| <a id="term-ce"></a>**CE** — Consumer Expenditure Survey | The BLS survey of what US households buy, split by age, income, region and household composition. **The US cohort source.** | [segmentation §2](#src-consumer-segmentation-archetypes) | [BLS CE](https://www.bls.gov/cex/tables.htm) |
| <a id="term-hbs"></a>**HBS** — Household Budget Survey | Eurostat's harmonised European equivalent of the CE. **The European cohort source.** | [segmentation §2](#src-consumer-segmentation-archetypes) | [Eurostat](https://ec.europa.eu/eurostat/web/household-budget-surveys) *(unverified)* |
| <a id="term-participation-rate"></a>**Participation rate** | The share of households that bought a thing at all, as opposed to the average spent per household. **Needed for the 1% coverage cut, and we do not have it yet.** | [segmentation §6](#src-consumer-segmentation-archetypes) | — |
| <a id="term-coverage-floor"></a>**Coverage floor** | A cost computed over an incomplete basket is a **lower bound, never a value.** Foundations §4.4 and conformance requirement 13. Every figure the simulator prints must say so. | [intensity §4](#src-labour-and-pollution-intensity) | Foundations §4.4 |
| <a id="term-price-split-bias"></a>**Price-split bias** | Input–output tables divide physical impacts by dollars, which **under-counts cheap heavy flows** (waste, bulk materials, land) and over-counts expensive light ones. Direction known; must be declared. | [intensity §4](#src-labour-and-pollution-intensity) · [estimation §7](#src-estimation-engine-data-sources) | [Physical vs monetary IO](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X) |

### Value, property, and markets

| Term | Short definition | In our research | Authoritative source |
|---|---|---|---|
| **Cost the limit of price** | Josiah Warren's rule that a good's price should be capped at the labour it cost to make — so profit, rent, and interest (income for no work) are excluded. | [warren](#src-warren-cost-the-limit-of-price) | [Wikipedia](https://en.wikipedia.org/wiki/Cost_the_limit_of_price) |
| **Mutualism** | An anarchist economic theory: a free market of artisans and co-ops trading at cost, with interest-free "mutual credit" and property held by occupation-and-use rather than title. | [proudhon](#src-proudhon-mutualism) | [Wikipedia](https://en.wikipedia.org/wiki/Mutualism_%28economic_theory%29) |
| **Property vs. possession** | Proudhon's distinction: *possession* is what you use and occupy; *property* is holdings that earn income from others' labour (rent, interest). Only the latter is what he called "theft." | [proudhon](#src-proudhon-mutualism) | [*What Is Property?*](https://www.gutenberg.org/ebooks/360) |
| **Labour theory of property** (Ellerman) | Responsibility for what's produced belongs to the people who actually work — since only humans act, not tools or their owners — the same responsibility principle courts use for crimes, applied to production. | [ellerman](#src-ellerman-labor-theory-of-property) | [Wikipedia](https://en.wikipedia.org/wiki/David_Ellerman) |
| **Inalienable rights** (de facto) | Ellerman's argument that some rights can't validly be transferred because the underlying capacity — human agency — cannot in fact be handed to another, only pretended to be; this is what invalidates both the slavery and the employment contract. | [ellerman](#src-ellerman-labor-theory-of-property) | [Wikipedia](https://en.wikipedia.org/wiki/David_Ellerman) |
| **Market vs. antimarket** | Braudel's two layers of commerce: a bottom layer of small competitive producers (the true "market"), and an upper layer of monopolists and financiers big enough to *set* prices ("capitalism," effectively an anti-market). | [delanda](#src-delanda-markets-antimarkets) | [Braudel (Wikipedia)](https://en.wikipedia.org/wiki/Civilization_and_Capitalism,_15th%E2%80%9318th_Century) |
| **Post-scarcity** | A theoretical situation where most goods are produced in great abundance with minimal human labour, so they become available to all cheaply or freely. | [saadia](#src-saadia-trekonomics) · [bookchin](#src-bookchin-social-ecology) | [Wikipedia](https://en.wikipedia.org/wiki/Post-scarcity) |
| **Fictitious commodities** | Polanyi's term for land, labour, and money — treated as ordinary goods for sale though none is actually produced for sale; forcing them through the market "subordinates society to the market." Aequitas independently reaches the same three conclusions. | [polanyi](#src-polanyi-great-transformation) | [Wikipedia](https://en.wikipedia.org/wiki/The_Great_Transformation_(book)) |
| **Georgism / land-value** | Henry George's argument that the gains of progress are captured as land rent (causing poverty amid growth), remedied by a single tax on land value — land treated as a common resource. | [henry-george](#src-henry-george-land) | [Wikipedia](https://en.wikipedia.org/wiki/Progress_and_Poverty) |
| **Conspicuous consumption** | Veblen's term for spending to display wealth and status through visible waste rather than to meet a need — the display-wealth Aequitas's permanent consumption-debit makes visible. | [veblen](#src-veblen-conspicuous-consumption) | [Wikipedia](https://en.wikipedia.org/wiki/Conspicuous_consumption) |
| **Industry vs. business** | Veblen's split between *industry* (engineers/workers making useful things) and *business* (owners/financiers restricting output to make money); it seeded the Technocracy movement and prefigures Aequitas's "remove the profit layer, keep the making layer." | [veblen](#src-veblen-conspicuous-consumption) | [Wikipedia](https://en.wikipedia.org/wiki/Thorstein_Veblen) |
| **Social ecology** | Bookchin's thesis that ecological destruction stems chiefly from *social* hierarchy and domination — you can't fix the human–nature relation without fixing human–human ones. | [bookchin](#src-bookchin-social-ecology) | [Wikipedia](https://en.wikipedia.org/wiki/Social_ecology_(Bookchin)) |
| **Libertarian municipalism** | Bookchin's proposal to replace the nation-state with directly-democratic local assemblies that confederate — the friendliest home for Aequitas's stance of keeping municipal government and changing only its economic nature. | [bookchin](#src-bookchin-social-ecology) | [Wikipedia](https://en.wikipedia.org/wiki/Libertarian_municipalism) |

### Calculation and planning

| Term | Short definition | In our research | Authoritative source |
|---|---|---|---|
| **Economic calculation problem** | Mises's argument that without money prices for capital goods a planned economy can't rationally allocate resources; Hayek's sharper version holds the needed knowledge is *dispersed and tacit*, so no central body can ever gather it. | [neurath](#src-neurath-calculation-in-kind) | [Wikipedia](https://en.wikipedia.org/wiki/Economic_calculation_problem) |
| **Calculation in kind** | Neurath's counter-proposal: plan in physical units (tonnes, hours, joules) and compare whole ways of life directly, rather than squashing everything onto a single money price — which he argued destroys information. | [neurath](#src-neurath-calculation-in-kind) | [Wikipedia](https://en.wikipedia.org/wiki/Economic_calculation_problem) |
| **Shadow price** | The marginal value of relaxing a binding constraint by one unit in an optimisation — i.e. what one more unit of a scarce resource is worth. Kantorovich derived these as "objectively determined valuations" to price scarcity without profit. | [kantorovich](#src-kantorovich-shadow-prices) | [Wikipedia](https://en.wikipedia.org/wiki/Shadow_price) |
| **Labour-time planning** (Cockshott & Cottrell) | A demonstration that planning an economy in labour/physical units is computationally feasible at national scale, steering output by the gap between a good's shelf-clearing price and its labour cost. | [cockshott-cottrell](#src-cockshott-cottrell-labour-time) | [Wikipedia](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) |
| **Participatory economics** (Parecon) | A decentralised planned economy using self-managing worker/consumer councils, balanced job complexes, pay for effort and sacrifice, and iterative "participatory planning" in place of markets. | [participatory-economics](#src-participatory-economics) | [Wikipedia](https://en.wikipedia.org/wiki/Participatory_economics) |
| **Balanced job complexes** | Bundles of tasks arranged so that empowering and rote work are spread evenly across everyone, preventing any group from monopolising the interesting, decision-making work. | [participatory-economics](#src-participatory-economics) | [Wikipedia](https://en.wikipedia.org/wiki/Participatory_economics) |
| **Coordinator class** | Parecon's third class, between capitalists and workers: professionals who monopolise empowering, conceptual work and can congeal into a new ruling class even after capitalists are abolished. | [participatory-economics](#src-participatory-economics) | [Wikipedia](https://en.wikipedia.org/wiki/Participatory_economics) |

### Energy and material accounting

| Term | Short definition | In our research | Authoritative source |
|---|---|---|---|
| **Energy accounting** (Technocracy) | The 1930s Technocracy movement's proposal to price everything in energy units and distribute goods via non-tradeable, expiring "energy certificates," abolishing money and the price system. | [technocracy](#src-technocracy-energy-accounting) | [Wikipedia](https://en.wikipedia.org/wiki/Technocracy_movement) |
| **EROI** (energy return on energy invested) | The ratio of usable energy an energy source delivers to the energy spent obtaining it — the salvageable, respectable descendant of Technocracy's energy accounting. | [technocracy](#src-technocracy-energy-accounting) | [Wikipedia](https://en.wikipedia.org/wiki/Energy_returned_on_energy_invested) |
| **Input–output analysis** (Leontief) | A model of how each industry's output feeds every other industry and final demand; its "Leontief inverse" traces how a change in what people buy ripples back through *all* upstream suppliers at once. | [estimation-engine](#src-estimation-engine-data-sources) | [Wikipedia](https://en.wikipedia.org/wiki/Input%E2%80%93output_model) |
| **Environmentally-extended input–output** (EEIO) | Input–output analysis with pollution and resource-use data attached, so tracing a purchase also yields its embodied emissions, energy, water, land, and materials. | [estimation-engine](#src-estimation-engine-data-sources) | [US EPA](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models) |
| **Physical input–output tables** | Input–output tables that record what industries send each other in *tonnes* rather than *dollars* — the physical basis Aequitas prefers over money-based models. | [estimation-engine](#src-estimation-engine-data-sources) | [Weisz & Duchin (2006)](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X) |
| **Life-cycle assessment** (LCA) | A method for tallying a product's environmental impacts across its whole life, from raw-material extraction ("cradle") through manufacture and use to disposal ("grave"). | [joint-production](#src-joint-production-allocation-problem) | [Wikipedia](https://en.wikipedia.org/wiki/Life-cycle_assessment) |
| **Joint production** | One process yielding several outputs from one pool of inputs (a steer → beef, hide, tallow…). Admitting it can make computed "labour values" indeterminate or *negative* (Steedman's result) — the classic attack on labour-based accounting. | [joint-production](#src-joint-production-allocation-problem) | [*Marx After Sraffa* (Wikipedia)](https://en.wikipedia.org/wiki/Marx_After_Sraffa) |
| **Great Pacific Garbage Patch** | A large accumulation of floating plastic debris — mostly microscopic particles — in the central North Pacific gyre; the anchor for the "cost to clean up plastic" figure. | [plastic-lca](#src-plastic-lca-and-cleanup-cost) | [Wikipedia](https://en.wikipedia.org/wiki/Great_Pacific_garbage_patch) |
| **Entropy economics** (Georgescu-Roegen) | The view that the economy is bound by the second law of thermodynamics — usable energy and materials irreversibly degrade — so perfect recycling is impossible and the books never balance. | [external-critique](#src-external-critique-2026-08-09) | [Wikipedia](https://en.wikipedia.org/wiki/Nicholas_Georgescu-Roegen) |

### Alternative-currency history and institutions

| Term | Short definition | In our research | Authoritative source |
|---|---|---|---|
| **Time banking** | A system where every hour of service is credited equally, regardless of the task, and members exchange hours with one another — the modern flat-hour experiment whose chronic skill shortage is real-world evidence on crediting all hours equally. | [local-currency](#src-local-currency-experiments) | [Wikipedia](https://en.wikipedia.org/wiki/Time-based_currency) |
| **Mutual credit** (WIR) | A currency created in the act of a trade — balances start at zero and net back to zero — used business-to-business. The Swiss WIR (1934–) is the long-running example and is claimed to be countercyclical (expanding when regular money is scarce). | [local-currency](#src-local-currency-experiments) | [Wikipedia](https://en.wikipedia.org/wiki/WIR_Bank) |
| **Demurrage** | A carrying cost (negative interest) on holding money, designed to make it lose value over time so people spend rather than hoard it — as in Gesell's stamp scrip and the Wörgl experiment. | [local-currency](#src-local-currency-experiments) | [Wikipedia](https://en.wikipedia.org/wiki/Demurrage_%28currency%29) |
| **LETS** (local exchange trading system) | A community mutual-credit network where members trade goods and services and settle in a locally-recorded unit rather than national money. | [local-currency](#src-local-currency-experiments) | [Wikipedia](https://en.wikipedia.org/wiki/Local_exchange_trading_system) |
| **Double coincidence of wants** | The barter matching problem: a direct swap needs each party to have exactly what the other wants at the same time and place — its rarity is the classic argument for money. | [local-currency](#src-local-currency-experiments) | [Wikipedia](https://en.wikipedia.org/wiki/Double_coincidence_of_wants) |
| **Issuer-pays conflict** | When the party being rated or audited pays for the assessment, verdicts drift favourable; the US Financial Crisis Inquiry Commission found this a central cause of the 2008 ratings failures. | [auditor-independence](#src-auditor-independence) | [Wikipedia](https://en.wikipedia.org/wiki/Credit_rating_agencies_and_the_subprime_crisis) |
| **Sarbanes–Oxley Act** | US law (2002) that restricted the non-audit services an auditor may sell its own audit clients — itself an admission that competition alone doesn't keep auditors independent. | [auditor-independence](#src-auditor-independence) | [Wikipedia](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act) |
| **Aggregate demand / Keynesianism** | Keynes's argument that total spending, not the price of labour, sets employment; markets can stall below full employment, justifying active intervention — the reason the modern economy runs on ever-rising debt. | [keynes](#src-keynes-general-theory) | [Wikipedia](https://en.wikipedia.org/wiki/The_General_Theory_of_Employment,_Interest_and_Money) |
| **Myth of barter / debt-first** | Graeber's finding that credit and debt (running tallies of who owes whom) predate coinage and barter, refuting the economists' story that money arose to fix barter — which removes a standard argument for why a transferable money is necessary. | [graeber](#src-graeber-debt) | [Wikipedia](https://en.wikipedia.org/wiki/Debt:_The_First_5000_Years) |

---

## Maintenance
- **On any fold:** if an OP/C/IC status or a doc version changes, update the row here — the in-text links don't need touching.
- **Research terms:** when a new `02-research/` stub introduces a term of art, add a row to [Research & academic terms](#research-terms) with a verified external source (non-paywalled).
- **When a new acronym is coined:** add its row here *before* using it in a body doc, and give it an `<a id>` anchor.
- **Source-of-truth docs:** Foundations (axioms, §), Conformance (numbered rows, IC-#), Objections (OP-#, P#, analysis A#/B#), Strategy §3 (C#). Titles here are convenience labels — the source doc's own statement governs.
