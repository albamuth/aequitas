<!-- tag: fnd-aequitas-foundations-and-long-term -->
# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.17
> **Date:** 2026-08-22
> **Status:** Working foundations.
> **Supersedes:** `99-archive/Aequitas_Foundations_v0.16.md`. **Coverage folded in (OP-26) — consistency is not completeness, and the closure witness turns out to have been in §5.1b all along.** An external objection established that arithmetic over a log testifies to nothing outside that log; the answer is that a **closure witness is neither an assertion nor a proof but a citation** — method, provenance, vintage, extent, and an obligation to recompute when it improves. Four things follow. **§3.3** now states that coverage estimates ride the retroactive-recomputation engine like any other science, and adds the previously-unstated **transaction-time rule**: the ratio gate is evaluated when the transaction happens, so a later re-weight changes *future* room and never the validity of a completed act. **§3.3a** extends rival-sector audit to coverage estimates — the natural auditor of a dark-residual figure is the *instrumented producer in the same market* — and notes the lever is larger than a cost constant, because a coverage figure changes which flows are deemed to exist at all. **§5.1a** gains the **floor rule** beside monotonicity: a quantity computed over incomplete coverage is a lower bound, not a value. **§5.3b** is new: **what a network owes, and what funding one means.** Tallying is **algorithmic**, which is what makes §3.3's *citation* requirement enforceable — a published algorithm gives `method_ref` a version number to point at. A trustworthy network **publishes its estimating numbers, its methods, and anonymised data covering all participants**; how much it reveals about institutions and businesses is its own call. **"Funding" is not a budget** — it is the recognition of an activity as creditable, and recording is never gated (A7), so the credit for audit work was never scarce; what is scarce is **demand (pledges) and verification**. This narrows OP-24's *funding* half out of existence while leaving its *incentive* half intact. **The bootstrap is a genesis entry pointed at the network itself.** ⚠️ Founding credit is flagged as the one record with no possible contemporaneous check — bounded by IC-7, public re-computation, and the `24/F` ceiling, but not closed. **§5.3a** is new: **privacy is a network choice.** The trust network does the tallying, so it holds what is private and it decides the practice — pseudo-privacy on the payment-intermediary model, or radical transparency, or anything between. Aequitas states principles and does not dictate implementation; inter-network compatibility is negotiated between networks. This is the third dial of the same kind as ρ and the floor `F`. **Opacity is priced rather than forbidden** — a counterparty discounts what it cannot verify (OP-14), so a privacy practice becomes a property of a network's output. Three residues are flagged: **information capture by the network itself**, a **measured coverage cost** to privacy, and a network's choice **binding members who did not make it**. **§5.1d** is new: **the back-trace horizon is birth, and it runs on both sides** — a lifetime of estimated consumption arrives together with a lifetime of self-care credit, which at roughly 3,650 h/yr against roughly 1,380 h/yr makes onboarding a windfall for a median person rather than a penalty. Evidence is voluntary, moves the figure either way, may arrive at any later date, and re-derives the ledger under A6. Two conditions carry it: estimates for undisclosed periods are computed over the **undisclosed residual**, and estimates **err against the estimated party** on both sides so evidence always pays — with the self-care floor exempt, because it is credited by proof-of-life and not estimated at all. **⚠️ It escalates OP-22 sharply: a back-trace is a life dossier.** **§5.1c** is new: **the residual is held, not allocated** — a coverage gap is computed and published but charged to nobody, and a dark producer's share is back-traced to them when they onboard, which is also the only way they can transact at all. A4 is not abandoned but **pending**, and the damage is already priced through §3.3's ambient stock without anyone being charged for another's units. **§5.1b** gains the **conservative-count rule** (under-count the dark; the self-liquidating error is the safe one) and generalises the witness from production to any conserved dimension. Schema consequences are in EventLog v0.8 §4.1a/§7.4. No axiom changed. Full paper: `00-strategy/OP-26_coverage_and_closure.md`.
> **Prior (v0.16):** **Empirical calibration folded into §3.5 and §7.5 — the "labour is abundant, physical throughput binds" thesis is now anchored to measured numbers, and the ρ prime-rate is calibrated.** Three results, all from `06-simulation/`: (1) the **labour cost of a median US lifestyle is ≈ 1,380 h/yr**, built bottom-up from measured supply chains (BLS ERM × PCE + EXIOBASE imports + §6.2b durables + own-pollution remediation), *far* below the ~3,650 h/yr self-care credit every human earns — so the median commands about a third of one person's annual credit. (2) **Cross-country efficiency (Q6):** the US is the labour- *and* carbon-inefficient outlier — it commands 50–80% more embodied labour and 2.5–4× the CO₂ per capita than Germany/Sweden/France/Japan/Spain for a comparable-or-worse material standard; efficient peers deliver the same life at ~⅔ the labour. (3) **The ρ-sweep** (`rho_sweep.py`) shows a pickable ρ clears the market, moves predictably under shocks, and — the load-bearing new finding — **efficient production, not extra labour, is what crosses society toward post-scarcity**, while the `24/F` ceiling stays invariant throughout. No mechanism or axiom changed; this is anchoring, and the absolute ρ\* is illustrative (OP-10-dependent) while the directions are robust.
> **Prior (v0.15):** **Disparity-ceiling proof completed and stress-tested → PASSES (§7.5).** The `24/F` bound has a formal statement (`06-simulation/DISPARITY_CEILING.md`, with a plain-language explainer) and an adversarial pass that dissolved three attacks (Methuselah hoarder, dynasty/household, collector). The load-bearing precision it forced: **credit and debit are cumulative running tallies (A6), the gate `D ≤ ρ·C` is a ratio re-checked at each event, and credit is *never spent* — a purchase adds to debit, never decrements credit (A3: not a currency).** So there is no "banking" of credit to splurge; hoarding only front-loads one's own `ρ·C`, and at equal age disparity is exactly `24/F` (the only spread beyond it is age). The result is coupled to v0.14's pledge fold: making pledged surplus non-consumable (§6.4c) closed the one transfer channel that could have breached A3.
> **Prior (v0.14):** **Pledges made PERMANENT (§6.2b, §6.4, §6.4a), reversing v0.13's revocable model.** A pledge is a *permanent, non-revocable* grant of debit-room; a person's lifetime pledging-budget equals their lifetime earned credit, spent down once (pledging never diminishes credit itself). A task's pledges first cushion its cost, split pro-rata by hours **on the task**; any **surplus becomes a non-consumable contingent reserve** earmarked to any *verified task-caused future cost* (causation by physical-trace; diffuse/latent harm by cohort convention). The reserve is a **buffer, not a shield** — once exhausted, residual task-caused debit reverts to the causer (§3.2/§3.7). A pledge to an abandoned task is **burned**, not reverted. This gives onerous *hazardous* work a demand-gated incentive without profit or rate-scaling (the hazard half of OP-16); sim `06-simulation/pledge_reserve.py`. Full change log in the companion `Aequitas_Foundations_CHANGELOG.md`.
> **Also supersedes:** OFCS (Open Fair Credit Standard) — see §8 for what is deliberately *not* inherited.
> **Primary audience of the first paper:** technologists / implementers.
> **Companion:** `00-strategy/Aequitas_Objections_v0.17.md` — the objections register. Read alongside §10.

---

<!-- tag: fnd-toc -->
## Contents

- [0. The One-Sentence Theory](#0-the-one-sentence-theory)
- [1. Axioms](#1-axioms)
  - [A1 (materialism of cost)](#a1-materialism-of-cost)
  - [A2 (time as measure)](#a2-time-as-measure)
  - [A3 (non-fungibility)](#a3-non-fungibility)
  - [A4 (no externalities)](#a4-no-externalities)
  - [A5 (price ≡ cost)](#a5-price--cost)
  - [A6 (derived, not stored)](#a6-derived-not-stored)
  - [A7 (universal accounting)](#a7-universal-accounting)
  - [A8 (local governance)](#a8-local-governance)
  - [1.1 Named conventions](#11-named-conventions)
- [2. Conformance to the Three Criteria](#2-conformance-to-the-three-criteria)
- [3. The Ledger Model](#3-the-ledger-model)
  - [3.1 Structure — an event log, not a balance](#31-structure--an-event-log-not-a-balance)
  - [3.2 The two kinds of debit — and the two components of property debit](#32-the-two-kinds-of-debit--and-the-two-components-of-property-debit)
  - [3.2b Only property transfers — pollution and transport never do](#32b-only-property-transfers--pollution-and-transport-never-do)
  - [3.2a Debit is a vector, collapsed on demand](#32a-debit-is-a-vector-collapsed-on-demand)
  - [3.3 Retroactive re-weighting](#33-retroactive-re-weighting)
  - [3.3a Who checks the science — rival-sector audit](#33a-who-checks-the-science--rival-sector-audit)
  - [3.4 Resolution is opportunistic](#34-resolution-is-opportunistic)
  - [3.4a Joint production — the process allocates itself](#34a-joint-production--the-process-allocates-itself)
  - [3.5 The books never balance — and must not](#35-the-books-never-balance--and-must-not)
  - [3.6 End-of-life, recycling, and product-as-pollution](#36-end-of-life-recycling-and-product-as-pollution)
  - [3.7 Land is not owned; a building carries a remediation debt](#37-land-is-not-owned-a-building-carries-a-remediation-debt)
- [4. Verification — the Four-Level Ladder](#4-verification--the-four-level-ladder)
- [5. Identity, Privacy, and Onboarding](#5-identity-privacy-and-onboarding)
  - [5.1 Coverage without coercion](#51-coverage-without-coercion)
  - [5.1a Realization](#51a-realization)
  - [5.1b The residual rule — averages cover only the unmeasured](#51b-the-residual-rule--averages-cover-only-the-unmeasured)
  - [5.1c The residual is held, not allocated](#51c-the-residual-is-held-not-allocated)
  - [5.1d The back-trace horizon is birth — and it runs on both sides](#51d-the-back-trace-horizon-is-birth--and-it-runs-on-both-sides)
  - [5.2 Onboarding as resolution — and as the adoption incentive](#52-onboarding-as-resolution--and-as-the-adoption-incentive)
  - [5.3 Privacy — market data public, personal ledgers private](#53-privacy--market-data-public-personal-ledgers-private)
  - [5.3a Privacy is a network choice — Aequitas sets principles, not practice](#53a-privacy-is-a-network-choice--aequitas-sets-principles-not-practice)
  - [5.3b What a trust network owes, and what "funding" one means](#53b-what-a-trust-network-owes-and-what-funding-one-means)
- [6. One Credit, Three Feedback Channels](#6-one-credit-three-feedback-channels)
  - [6.1 Why "enrichment" is named at all](#61-why-enrichment-is-named-at-all)
  - [6.1b Self-care is credited work — and it is the floor's mechanism](#61b-self-care-is-credited-work--and-it-is-the-floors-mechanism)
  - [6.2 Training, front-loaded](#62-training-front-loaded)
  - [6.2a The Front-Loading Rule](#62a-the-front-loading-rule)
  - [6.2b The capital-debit waterfall](#62b-the-capital-debit-waterfall)
  - [6.3 Feedback: what each channel looks like](#63-feedback-what-each-channel-looks-like)
  - [6.4 Pledges and signals](#64-pledges-and-signals)
  - [6.4a Hand-off gates credit realization — the supply-chain model](#64a-hand-off-gates-credit-realization--the-supply-chain-model)
  - [6.4b Verification generalises by output type](#64b-verification-generalises-by-output-type)
  - [6.4c The contingent reserve — how over-pledging incentivises hazardous work](#64c-the-contingent-reserve--how-over-pledging-incentivises-hazardous-work)
  - [6.5 Attribution without intellectual property](#65-attribution-without-intellectual-property)
  - [6.5a Not all work is capturable — and the system does not require it to be](#65a-not-all-work-is-capturable--and-the-system-does-not-require-it-to-be)
  - [6.6 Unobservable work — and the lone fraudster](#66-unobservable-work--and-the-lone-fraudster)
- [7. Consequences](#7-consequences)
  - [7.1 Capitalism cannot function](#71-capitalism-cannot-function)
  - [7.2 Exploitation and pollution self-penalize](#72-exploitation-and-pollution-self-penalize)
  - [7.3 Regulators invert into services](#73-regulators-invert-into-services)
  - [7.4 Taxation is unnecessary](#74-taxation-is-unnecessary)
  - [7.5 The basic-needs floor](#75-the-basic-needs-floor)
  - [7.6 Why the alternative-economy graveyard does not apply](#76-why-the-alternative-economy-graveyard-does-not-apply)
- [8. Deliberate Divergences from OFCS](#8-deliberate-divergences-from-ofcs)
- [9. Document Roadmap](#9-document-roadmap)
- [10. Open Problems](#10-open-problems)
  - [10.1 Deliberately left to trust networks](#101-deliberately-left-to-trust-networks)
- [11. First Foothold — the MVP](#11-first-foothold--the-mvp)
- [12. Amendment record](#12-amendment-record)

---

<!-- tag: fnd-s0 -->
## 0. The One-Sentence Theory

> **Aequitas is a universal accounting of material flows.** Every credit and every debit is a record of matter and energy moving through the world, attributable to the people who caused the movement. **Cost is nothing other than this.**

**Aequitas is a theory of cost. It is not a theory of value, and it does not need to be.**

This distinction is load-bearing. Every previous attempt at objective accounting — Odum's emergy, Technocracy's energy certificates, the labour theory of value — claimed to have found what things are *worth*, and every one was refuted on the same ground: **supply-side only, ignores demand.** The refutation is a stock move and takes one sentence.

Aequitas makes the narrower and far more defensible claim. **Cost is what a thing takes from the world; it is physical, and we can measure it. Value is what someone thinks it is worth; it is not physical, and we do not attempt to measure it.** Value enters the system as *feedback and pledges* (§6), never as an accounting quantity.

> **On the credit side, the substance is *time* — and time, not effort**. A credit records *time a human spent*, and the conceptual leap Aequitas asks of a reader is to see time itself as the finite thing being spent — like money is "spent" today, except that time is possessed by every person in exactly equal measure (24 hours a day) and can be neither hoarded, lent, nor transferred (A3 (non-fungibility)). This is the deep reason Aequitas produces a **bounded** inequality where money produces an unbounded one: money accumulates without limit; time structurally cannot — you get 24 hours a day and no more, ever, and you cannot buy anyone else's. Effort, hazard, and skill are real differences between workers, but they resolve as *material* costs (A2 (time as measure)), never as a time-multiplier. **Because the unit of account is an equally-distributed, non-transferable resource, the *engine* of a bounded inequality is the arithmetic itself, not any rule that polices it.** *(The exact bound, though, is a **conditional** result — it depends on the network's self-care floor staying in a narrow band and on OP-22 (audit disclosure) being solved; see §7.5. Earlier drafts overstated it as a flat arithmetic certainty.)*

Everything downstream — no capitalism, no rent, no taxation, no externalities, no inflation — is a *consequence* of taking the cost rule seriously and applying it without exception.

---

<!-- tag: fnd-s1 -->
## 1. Axioms

These are the immutable core. Nothing in Aequitas may contradict them, and no local variance may amend them.

<!-- tag: fnd-a1 -->
### A1 (materialism of cost)

**Every credit and debit is a record of a real material or energy flow — there is no abstract, issued, or fiat quantity anywhere in the system.**

Down to the oxygen a human inhales and the CO₂ they exhale.

*Grounding for attribution.* Flows are attributed to whoever caused them, on the juridical principle of **responsibility imputation** — impute responsibility in accordance with who was in fact responsible. This is [David Ellerman's labour theory of property](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf), and it is deliberately preferred to any labour theory of *value*: it is a theory of imputation, it inherits none of the transformation or negative-value problems, and it appeals to a principle its opponents already accept everywhere else. Only humans act; tools and capital do not. Responsibility therefore imputes to people, never to machinery or its owners.

> **Corollary — financial instruments carry no debit**. Stocks, bonds, currencies, crypto-tokens, options, and other financial claims are exactly the "abstract, issued, or fiat quantity" A1 excludes: they are not matter or energy. **They therefore never appear on any ledger.** What *is* accounted is the **material** they are claims *upon* — a factory, land, a building — and that material's debit sits on whoever physically **holds or operates** it (embodied-material dischargeable on transfer; creation-cost holding-time-split, §3.2/§6.2b), never on the paper. This is not a loophole for hidden wealth: owning a factory through shares does not move its material debit to *nobody* — it stays on the factory's operators, by holding time. The consequence is measured in the scenario suite: entering the previously-wealthy **material-only** collapses the observed inequality tail by ~three orders of magnitude versus their paper net worth (§7.5, `06-simulation/q4_locked_ledgers.py`), because financial wealth was never material and physical consumption is bounded by time.

<!-- tag: fnd-a2 -->
### A2 (time as measure)

**Time is only a yardstick for summarizing flows, never a substance with value — so labour is never rate-scaled, and differences between workers resolve as material costs, never as a multiplier.**

Time is a convenient universal yardstick for summarizing flows — a local second is a local second, measurable identically everywhere. But an hour is not *itself* value. Differences between workers resolve as *material* differences, never as a multiplier:

- **Hard labor** → extra caloric intake is recorded as real food-production cost.
- **Hazardous labor** → health harms discovered later are retroactively injected as debit into the products and services that caused them.
- **Skilled labor** → **training is credited work in its own right, and its cost is discharged at the time of training.** Nothing flows downstream. See §6.2.

> **A2 is also the reason the co-product allocation problem has an answer (§3.4a).** Because every physical quantity in the ledger — a kilogram, a joule, a tonne of CO₂ — is a proxy for hours to produce or to mitigate, **the system never has to choose between mass and energy as *the* unit of account.** The universal is the denominator, not the carrier. This is a stronger consequence of A2 than was recognised when it was written.

<!-- tag: fnd-a3 -->
### A3 (non-fungibility)

**Every credit and debit is a unique, non-exchangeable record of a specific event — credits can never be transferred, traded, gambled, lent, or stolen; only debit moves, and only by transferring the thing it is attached to.**

A3 is not a design preference. Under A1 it is a **consequence**: credit records who was responsible, responsibility is a fact about a person, and facts about people do not change hands. It also does three defensive jobs at once — see §7.6.

<!-- tag: fnd-a4 -->
### A4 (no externalities)

**Every consequence of an activity is priced into it, including consequences discovered decades later — there is no "outside" of the accounting.**

<!-- tag: fnd-a5 -->
### A5 (price ≡ cost)

**The price of anything is its true, current-best-estimate material cost — there is no profit in exchange, only debit discharged and debit acquired.**

Competition happens on **quality, artfulness, and efficiency**, never on margin.

<!-- tag: fnd-a6 -->
### A6 (derived, not stored)

**Balances are never authoritative — the event log is; any account's standing is a pure function of its events times the current scientific cost-weighting model.**

Improve the science, and all history re-weighs automatically (§3.3).

<!-- tag: fnd-a7 -->
### A7 (universal accounting)

**Every human is accounted for whether or not they participate, with credit and debit estimated symmetrically for everyone (§5.1) — but a position becomes realizable only on a verified account.**

- **Accounted** — every human carries an estimated credit *and* debit position. A factual claim about material flows, not a claim on or by the person.
- **Realizable** — an estimated position acts on a person's debit ceiling only once they hold a **verified account** and their estimates have been superseded by observed, attested records.

Non-participants are fully represented in the books and can draw nothing from them. **Participation is the act of converting an estimate into a record.**

**Corollary — credit is issuable retroactively.** When a person joins, their prior real contributions enter the record at the dates they occurred.

> **Design constraint — estimation error is not symmetric.** Over-estimating debit consumes nothing. Over-estimating credit inflates real consumption ceilings on the basis of guessed production. Symmetric in *form*, asymmetric in *consequence* — which is why realization is gated on observation.

<!-- tag: fnd-a8 -->
### A8 (local governance)

**No organization that grows up around Aequitas may acquire authority over its core rules — governance is a protocol property, not an institution.**

Rules evolve as *immutable core + local variance*, with variance competing in the open.

<!-- tag: fnd-s1-1 -->
### 1.1 Named conventions

Some quantities the system needs are **not** physical facts. Where that is true, it is stated here rather than hidden in an implementation detail. **A convention that is declared is not an ad-hoc rule; a convention that is disguised as a measurement is.**

| Quantity | Status | Why it is not a measurement |
|---|---|---|
| **Split of a team's credit across its members** | ✅ **Not a convention — dissolved (A2)** | Credit is *time worked* (§6), so each member is credited **their own hours** — the "welder caused 40% of the bridge" number is never needed. Credit is not a share of output. **OP-18's team-credit half was a mis-statement; A2 already answers it.** *(A residual remains — apportioning a jointly-*caused debit* across a team — but that is a debit-attribution question, minor, sibling to OP-25 (illicit dumping).)* |
| **Split of *labour* across co-products** | ✅ **Convention with a measurable basis — rides the material split** | One labour process yields several products (farmer's hours → beef + hide); the hours leave no per-product trace, so a convention is required (physical-trace test). The declared convention: **labour rides the same physical split §3.4a already measures for the process's materials** (mass/deposition for cattle, cracking-energy for a refinery). Adds *no new lever* — it piggybacks on the rival-audited material θ. Changes no one's credit; it is a debit-side cost figure only. **OP-18(α) — closed 2026-08-05.** |
| **Split of an asset's residual creation-cost across its holders** | ✅ **Convention with a measurable basis — holding-time** | Apportioning a fixed creation-cost is a choice, but **holding-duration is a physical trace**, so the convention is measured, not invented: share = holder's holding-time ÷ total holding-time over the asset's life (§6.2b). Respects the dummy and symmetry axioms an even split fails. |

> **Two rows are absent by design, not omission.** A *"split of a joint process's debit across its co-products"* is **not** a convention — the process itself performed the split and it is measurable (§3.4a). And *shared-overhead attribution to co-products* has nothing to attribute — under §6.2b all capital and overhead accrues to the **asset**, never to the co-products (the barn stays on the operator; hide and beef carry only their own consumables). See `00-strategy/OP-17_coproduct_allocation.md` and `00-strategy/OP-23_capital_and_pollution.md`.

**The test that separates the two columns, and it is the useful output of the OP-17 (joint production) work:**

> **Did the thing being divided leave a physical trace?**
> **Where it did — measure.** Feed energy, cracking enthalpy, and a turbine's heat/power trade-off are facts about a process.
> **Where it did not — declare a convention and say so.** Labour hours and shared overhead leave no trace to an individual output, and no instrument will ever find one.

**The project's hard problem is division, not measurement** — but v0.4 narrows that: it is division **of the untraceable**. See the objections register §0.

---

<!-- tag: fnd-s2 -->
## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No exceptions for professions, nations, or classes. Units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7 (universal accounting)). Where a genuine convention is required, §1.1 names it rather than concealing it. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing local variance. **Cost constants are disciplined by rival-sector audit (§3.3a), which needs no reviewing body.** |
| **Fecundity** | The verification ladder *pulls* technological development (§4). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses want (§7.3). Onboarding is individually rational (§5.2). Pledges give surplus a purpose (§6.4). **Every co-product allocation is an open scientific question that better instruments improve (§3.4a).** |

**Fourth screening question — "does this need a Paul Glover?"**
Ithaca HOURS died when its founder relocated; he himself said every local currency needs a full-time networker to promote, facilitate, and troubleshoot. A mechanism that depends on an enthusiast is a mechanism with an expiry date. **Every proposed mechanism must pay its own maintainer from inside the system** — as auditing-as-credited-work does, and as rival-sector audit does (§3.3a). Apply alongside universality, decentralization, and *who games this?*

---

<!-- tag: fnd-s3 -->
## 3. The Ledger Model

<!-- tag: fnd-s3-1 -->
### 3.1 Structure — an event log, not a balance

One permanent, append-only **record of activity**: who did what, when, involving which materials and energy. An account's displayed standing is a **continuously recomputed projection** of that log.

<!-- tag: fnd-s3-2 -->
### 3.2 The two kinds of debit — and the two components of property debit

![The debit taxonomy: DEBIT as a vector splits into property debit (embodied-material, dischargeable; and creation-cost/labour, holding-time-permanent) and consumption/pollution debit (never discharged, stays on the causer); two cross-cutting rules — self-work identity and non-cascade.](../wiki/assets/debit-taxonomy.svg)

*Schematic of this section (§3.2 + §3.2a/b), embedded from the wiki master page `01-wiki/debit-taxonomy.md`. The prose below is authoritative; the diagram is the map.*

**Property debit — a *current-holdings* term.** It has **two components that behave differently on transfer**, and conflating them was an internal contradiction before v0.7:

- **Embodied-*material* debit — dischargeable.** The atoms you hold. Transferring the object releases it entirely; the material rides the object to the new holder. This is the "dischargeable on transfer" behaviour v0.5 described.
- **Creation-cost / labour debit — holding-time-split, and each holder's share is *permanent*.** The hours that *made* the object do **not** vanish when you pass it on. Your share is set by how long you held it (share = your holding-duration ÷ total holding-duration over the asset's life, §6.2b), and it **stays on your ledger, diluting but never zeroing**, after transfer. *(Worked case: a 500,000-hour house held 10 years, then transferred, leaves ≈250,000 hours on the seller once the next holder has held it an equal span — the holding-time share, permanent.)*

> **Why the split.** §3.2 (v0.5) said property debit "releases entirely on transfer"; §6.2b said creation-cost is holding-time-permanent. Both cannot be true of one quantity. The resolution: **the material transfers with the atoms; the making is holding-time-split and permanent per holder** (§6.2b). This is A1-clean — both attach to the object — but only one leaves when the object does.

- Work done on property *increases* the property's creation-cost debit.
- **The self-work identity holds *for the holding period*:** while you hold a thing, a repair earns credit for the labour exactly equal to the property's debit increase — net zero, excluding materials/energy consumed. This is what makes property a burden rather than an engine. On transfer, the material leaves and your holding-time share of the creation-cost persists (§6.2b) — you were credited for real work and bear your time-proportional share of the resulting debit; no rent, no appreciation, nothing earned without working.
  - *Corollary — subsistence.* Growing food and eating it yourself is the same identity: the farming labour credits you, the food carries that debit, consuming it returns the debit to you. **Net zero on labour, net cost on materials and energy consumed.** No special rule is needed; the existing identity already answers it.

**Transfer does not require a participant — and cannot be escaped by finding a non-participant**. Handing an object to someone **outside** Aequitas produces no event, so the record still shows *you* as holder: you keep its full debt-load. Handing it to someone **inside** Aequitas starts the new holder's holding-time accruing, so your share begins to dilute. **There is no exit through a non-participant** — the ledger only lightens when a real holder takes the thing on. (Effect: used goods enter cheap for the new holder — near-zero holding-time — and grow heavier the longer they are kept.)

**Consumption / pollution debit — a *permanent-history* term. Never discharged.**
- Locked into the record forever, **on whoever caused it.**
- But its **weight floats** with the current cost of mitigation (§3.3).

<!-- tag: fnd-s3-2b -->
### 3.2b Only property transfers — pollution and transport never do

The two kinds of debit behave differently under transfer, and this is load-bearing:

> **Only property-debit — the embodied material you hold — transfers with an item. All pollution-debit and all transport/energy-consumption debit is permanent on whoever caused it and never transfers. Provenance records travel; the debit does not.**

- The **farmer** keeps the pollution-debt of the fertilizer runoff — not the person who buys the groceries.
- The **gold mine** is indebted by the mining process — not the owner of the jewelry.
- **Transport** fuel and its pollution stay on whoever caused the journey — the factory for inbound logistics, the consumer for final delivery — permanently, and cannot be shed by reselling the item.

**Why this is right under A1 (materialism of cost).** Ellerman's responsibility-imputation: only the miner *acted* to pollute; the buyer did not cause the mining. Charging the buyer would misattribute responsibility. This is simply the two-kinds distinction above taken to its conclusion — the *permanent* kind stays with its causer; the *transferable* kind rides the object.

> **This is the same principle as computational closure (§6.2a), seen from the other end.** Ellerman says pollution *must not* transfer to a non-causer; §6.2a says a cost *cannot* cascade indefinitely or the accounting never terminates. They are one rule: **cost never flows to whoever did not cause it** — downstream to a buyer (pollution) or upstream to the first human activity (historical cost). Both directions break the books, and the same non-cascade closes both. The gasoline case makes it concrete: the refinery's process emissions stay on the refinery, and the *combustion* emissions fall on whoever burns the fuel — never on the receiver of goods a truck delivered.

<!-- tag: fnd-s3-2b-realtime -->
> **The real-time-dispatch principle — and why electricity generation is the consumer's**. The two cases just given — final-delivery transport and fuel combustion — share a feature worth naming, because it settles a case that looks harder: **electricity.**
>
> **The rule:** *emissions from real-time, demand-dispatched, non-storable production follow the **end-user**; emissions embodied in stockpiled or batch-produced goods stay with the **producer**.* A steel bar was made in advance, on a forecast, independent of any particular buyer — its emission is the mill's (batch → producer). But grid electricity **cannot be stored** and is generated the instant it is drawn: flipping the switch physically commands a generator to burn fuel *now*. Under A1, the plant is a **tool** and only the human drawing power **acts** — exactly as the driver, not the car, causes the tailpipe emission. **So electricity's generation pollution is the consumer's, not the generator's.** This *aligns* electricity with the transport and combustion rules above; treating generation pollution as "the plant's" (as an early informal reading did) was the inconsistency.
>
> **Attribution is by the consumer's *contracted supply mix* (provenance, §5.1b), not the physical marginal unit.** On a pooled grid the electrons are physically indistinguishable, so "which turbine served *your* kilowatt" has no physical answer — but *which generator you contracted with* does (this is how a renewable tariff already works). The consumer therefore bears the emission profile of **the supply they bought**. This is load-bearing for incentives: it keeps the consumer's **conservation** incentive (use less → owe less) *and* the generator's **decarbonisation** incentive (a cleaner generator can offer lower-debit power and win contracts) — where dumping the raw grid-average on a captive consumer would have removed the debit from the only party that chooses the fuel. It also settles the *marginal-vs-average* question: it is **neither** — it is your contracted mix.
>
> **No-choice fallback.** Where the consumer genuinely cannot choose (a regulated monopoly grid, a single-generator village), the **local supply average** applies, and decarbonisation is driven collectively — pledges toward clean generation (§6.4) and the §3.3 stock rule, under which cleaning the grid retroactively lightens every past consumer's debit.
>
> **⚠️ Open universality edge.** "Real-time-dispatched vs batch" is a *spectrum*, not a clean binary: grid storage (pumped hydro, batteries) is a growing intermediate case, and on-demand services (a restaurant cooking your order) sit near the line. The principle is sound at the poles; the exact criterion for the middle is a registered open question, not yet closed.

**The consumer signal is not lost.** §5.1b already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**. Buyers and pledgers can still see and prefer low-pollution goods; only the *debit* is pinned to the causer. See §7.2 for why this makes the anti-pollution incentive *stronger*, not weaker.

**Custody is accepted, not imposed**. "Custody follows possession, no right to refuse a transfer" means **no right to accept an object but refuse its debit** — you cannot take the object and disclaim what rides with it. It does **not** mean anyone can be forced to *receive* an object. Read the other way, the rule would license garbage-dumping, the exact abuse it exists to prevent (§3.6).

<!-- tag: fnd-s3-2a -->
### 3.2a Debit is a vector, collapsed on demand

A debit is **not one number.** It is a bundle of physical quantities — kilograms of a substance, joules, labour-hours, cubic metres of water, land-area-years — stored separately in the log and combined into a single comparable figure only when someone needs to compare two things, via the current weighting model.

This is A3 (non-fungibility) and A6 (derived, not stored) working together: the physical record is what implementations must agree on; the collapse is what they may differ about (EventLog §3).

> **🔴 One rule follows immediately: Any division of a debit — across co-products, across a team, across anything — is computed on the vector, per dimension, *before* collapsing.**
>
> Divide the collapsed number instead, and whoever maintains the weighting model silently controls every allocation in history. Divide per dimension, and the split is **weighting-independent**: two communities running different models compute the same split and disagree only about what it weighs. This closes a side entrance to OP-10 (weighting governance) that would otherwise have been invisible.

<!-- tag: fnd-s3-3 -->
### 3.3 Retroactive re-weighting

When science improves, **every affected ledger in history recalculates.** Cheaper CO₂ mitigation makes everyone's past fossil use weigh less; a newly discovered occupational harm retroactively adds debit to the products made by the process that caused it.

This is the engine of fecundity: **the system permanently rewards better measurement of reality.**

**Re-weighting applies to allocation splits, not only to mitigation weights**. New process science re-splits historical joint production the same way new mitigation science re-weighs historical emissions. A conservative early estimate is not a permanent verdict on anyone — **no inaccuracy in this system is irreversible**, which is the general answer to "what if the early numbers are wrong."

**Re-weighting is also *stock-dependent*, not only technology-dependent**. A pollutant's weight floats with the **ambient stock** of that pollutant, not merely with the state of mitigation technology. First, the baseline:

> **A flow is a *pollutant* only above the rate at which the natural world remediates it unaided.**

Steel produced only as fast as old steel rusts back to iron-oxide is in equilibrium and is not a pollutant. CO₂ emitted only as fast as the planet absorbs it — stable ppm, no warming — is at baseline and is not a pollutant. A compostable container carries no material pollution-debt, because it dissolves without human intervention in reasonable time.

Above baseline, the weight tracks **total remediation** — removal *plus* the escalating, nonlinear damage a unit does while resident — so:

- As excess CO₂ **rises**, there is more to remediate per unit, and **every historical record of CO₂ re-weights up.**
- As the stock is **drawn down**, those same records re-weight **down.**

Two consequences worth stating. **(1)** This is one mechanism, not two: atmospheric CO₂ and solid waste in a landfill are the same stock-dependent rule (§3.6). **(2)** It makes collective remediation individually rational — cleaning the commons *retroactively lightens every holder's own pollution-debt*, so environmental remediation pays the people who funded it, backwards through their history. A holder charged for others' current emissions is only ever charged for *their own* units, at a rate that reflects the collective damage — proportionality, not collective punishment.

*Tractability is not speculative.* [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) demonstrated that in-kind calculation at national scale is computationally feasible with sparse-matrix methods. Mises's objection was in-principle; the empirical scale objection has been answered by people who ran the arithmetic.

**Coverage estimates ride this engine too, and that is the whole answer to "how do you count what you cannot see."** How many producers, emitters, or people sit outside the records is not a number conjured from nothing — censuses, supply records, trade data and satellite survey already produce it, by methods that are published and improvable. **Aequitas does not prescribe how an authoritative total is made, and should not.** What it requires is what a citation requires: *where the data came from, and how it was tallied.* A tally with a stated method is not an authority assertion; it is a claim anyone can re-run, dispute, or better.

So a coverage figure is a dated reading with a stated basis, exactly like every other estimate here — and when the science improves, **every affected ledger recalculates.** This costs nothing structurally, because the ledger is derived from the log and never stored (A6): recomputation is not a repair, it is how the system normally runs. And it means the fecundity loop closes for coverage as well: **improving the estimate of the dark is credited work, recorded as a tally event** (EventLog §2.2), *in the same ledger the estimate corrects*.

> **The transaction-time rule.** Because figures move, the gate must not. **`D ≤ ρ·C` is evaluated at the moment of the transaction.** A later re-weight, re-split, or coverage revision changes **future** debit-room; it never retroactively invalidates a completed act.
>
> Without this, a dynamic ledger implies retroactive liability — a revision could make a past purchase an offence — and no one should adopt a system that does that. Re-weighting corrects *the record of what things cost*; it does not reopen *what people were permitted to do* under the record as it then stood.

<!-- tag: fnd-s3-3a -->
### 3.3a Who checks the science — rival-sector audit

Retroactive re-weighting makes cost constants enormously powerful: whoever publishes the energetics of a process sets every split in that sector, backwards through all of history. That is a capture surface, and it needs an answer that is not a standards body.

**What Aequitas removes for free.** There is no market-dominating corporation to fund a favourable result, because A5 (price ≡ cost) removes the profit that pays for captured science today. Labs are credited by trust networks for doing the work. **The classic funding-bias channel is structurally closed, and that should be claimed.**

**What it does not remove.** Trust networks are dominated by the *consuming* side of any given good — everyone eats beef, few raise cattle — so their members collectively benefit from that good's debit being **understated**. And the incentive to correct is one-sided:

| Error direction | Who wants it fixed | Result |
|---|---|---|
| Constant **overstates** debit | Every subscriber | Corrected |
| Constant **understates** debit | Nobody; correcting it worsens every subscriber's ledger | **Nobody funds the replication** |

Left alone this produces **systemic drift toward under-costing** — the failure mode of every carbon-accounting regime attempted so far. §3.5 tolerates it arithmetically, but it erodes **A4 (no externalities)**, and A4 is not optional. Registered as **OP-24 (understatement drift)**.

> **The rule: the natural auditor of a cost constant is the rival sector, not the consumer.**
>
> If beef's energetics are understated, plant-protein producers are materially harmed and will fund the replication. Consumers police neither direction; rivals police both. This is an incentive, not an enforcement mechanism, and it is already implied by A5 — which removes profit *in exchange* while explicitly preserving **competition on efficiency** (§7.1). Rival-sector audit is that competition applied to the cost model itself.

Three supporting rules:

1. **Two unaffiliated replications before a constant may re-weight history.** Retroactivity is too powerful to trigger from a single source.
2. **Audit triage weights magnitude × concentration of beneficiary.** Materiality thresholds alone help an attacker, whose job then becomes making the falsification look immaterial.
3. **A trust network concentrated in the sector it audits is captured by construction.** Membership composition is public, so this is a **detectable screening property** rather than a rule anyone enforces. General-membership networks are structurally sounder than sector-specific ones. *(The co-op form does not fix this on its own: the conflict is directional, not monetary — Arthur Andersen was paid by Enron, and a client-owned Andersen would have been worse.)*

**The v0.5 stock constants are governed here too**. The **natural-remediation equilibrium baseline** and the **ambient-stock measurement** of §3.3 are powerful new constants — whoever sets them moves every pollution record in history — so they fall under exactly this regime: two unaffiliated replications before a re-weight, triage by magnitude × beneficiary concentration, and public membership as a capture screen. This is **OP-24** (understatement drift) acquiring a larger lever, not a new mechanism.

**Coverage estimates are governed here too, and they are the largest lever of all.** A mis-set energetics coefficient changes what a recorded flow *weighs*. A mis-set coverage figure — the *N*, *Y*, or *Z* of §5.1b — changes **which flows are deemed to exist at all**. The three supporting rules above therefore apply to it with full force.

> **And the rival-sector argument extends to coverage with no new mechanism.** Ask who is materially harmed when a dark residual is *understated*, and the answer is immediate: **the instrumented producer competing in the same market.** A grower who paid to measure their own supply chain is directly damaged when undocumented produce prices too cheaply. They will fund the replication. Consumers police neither direction here either; rivals police both.

**This gives OP-24 partial relief it did not have.** OP-24's core complaint is that a constant which *understates* has no natural corrector, because correcting it worsens every subscriber's ledger. That still holds for weighting constants. It does **not** hold for coverage, which has **two** funders that a weighting constant lacks:

1. **The rival producer.** An instrumented grower is materially harmed when undocumented produce prices too cheaply, and will fund the work of exposing it — the same argument as the rival-sector rule above, needing nothing new.
2. **The dark producer themselves.** They cannot transact inside the system at all until they onboard (§5.1c), so the pull toward the records is theirs, not something anyone has to impose.

**Neither funder requires the residual to be allocated to anybody**, which matters, because it is not — see §5.1c. The audit of *extent* therefore has a funder even where the audit of *weight* does not.

<!-- tag: fnd-s3-4 -->
### 3.4 Resolution is opportunistic

**Resolution.** Record what is known; estimate the rest from averages; refine forever. If someone commutes daily, estimate from cohort averages; learn which car they drive and it sharpens. All of it revisable.

**⚠️ Allocation is only partly a resolution problem.** Allocation of physical inputs *is* a resolution problem — the process performed the split and better instruments converge on it (§3.4a). What is genuinely not epistemically resolvable is the division of quantities the process **never physically divided**: labour hours across co-products, shared overhead, and joint responsibility across a team.

> **The distinguishing test is whether the divided thing left a physical trace.** Where it did, measure. Where it did not, declare a convention (§1.1) and say so.

<!-- tag: fnd-s3-4a -->
### 3.4a Joint production — the process allocates itself

One process, several outputs, one pool of debit. A steer yields beef, hide, tallow, bone, manure, and enteric methane; a refinery yields a full fraction slate; a CHP plant yields heat and power. **How the debit divides is a fact about the process, not a property of the outputs** — which is why a century of searching for the right *carrier quantity* (mass? energy? exergy? price?) found only rules that work in one industry and are category errors in the next.

> **A joint process's debit divides according to where the process itself physically sent its inputs.**
>
> The instrument is whatever that process makes traceable — tissue-deposition energetics for an animal, cracking enthalpy for a refinery, the extraction curve for a turbine, mitigation cost for an emission. These are not rival conventions; they are **different instruments reading the same underlying quantity, which is hours (A2 (time as measure)).** Mass is an estimator, correct where composition is uniform and a low-resolution reading where it is not.

**Data first, model second — and match the period**. The split is driven **first by measured data at the actual facility over the actual period**, and only *then* by a physics model where data is missing. Three rules make this precise:

1. **Measure at the facility, per period.** The primary instrument is what the plant meters: masses in and out, energy and labour consumed, at *that* plant. Where a facility sub-meters per line (cutting vs tanning, grinding vs sieving), that **measured routing is the split**. Where it meters only aggregate energy plus output masses, the mass split is the low-resolution reading and a **physics model bridges the gap until finer metering exists.** Each dimension takes its own measured split (§3.2a).
2. **Temporal matching.** The split is computed from **data of the same period it describes** — never a stale back-average. Prefer the shortest practical window (a single day, a single batch run); a longer window forces you to cost output that has been sitting in inventory. *(Milling: weigh the oats in and flour+bran out per run — not from a standing table that cannot see changing conditions.)*
3. **The physics model is fallback and ballpark, not primary.** Tissue-deposition energetics, milling energetics, and the like fill gaps where no facility datum exists **and** give auditors the range a reported split must fall within. Finer data always supersedes the model (§3.3, §8-supersession).

> **This does not weaken "the process allocates itself" — it operationalises it.** "The process performed the split" *means* the split is a fact you measure at the process, per period; the model is what you use where the measurement is not (yet) taken. Data-first is the same discipline as the verification ladder (§4): a Level-1 producer reads mass, a Level-3 producer reads calorimetry, the model covers what neither instrument saw.

Four consequences worth stating:

- **Human preference plays no part — and scarcity is not cost**. A hide's share does not change because leather is fashionable, exactly as manure's share does not change because nobody wants it. A split contingent on demand would give two identical steers in two towns different splits — a universality failure, and price allocation in costume. **The sharp case: a tenderloin (≈1% yield) and hamburger (≈5% yield) cost the *same* per pound**, because a pound of each embodies the same feed, water, and growing-labour — refined only by *measured* tissue composition (lean vs fat differ in deposition energy), **never by yield or desirability.** Weighting a rare, prized cut as *more costly* is scarcity smuggled into cost; worse, it would ration that cut by **who can absorb the larger debit** — price-rationing by standing, the exact mechanism A5/§7.1 removes. **The scarcity of the tenderloin is real, irreducible, and handled elsewhere:** on the demand side by pledges/signals (§6.4, how many cattle get raised) and by **decentralised local distribution** (a butcher's lottery, queue, or pledge-priority — §7.5), never by inflating cost. Cost states what a thing took; who gets a physically-scarce output is a distribution question, deliberately left to the local free market and out of any central authority's hands.
- **Waste outputs are co-products like any other.** Counting manure and methane in the split removes the residual, and with it the whole question of who absorbs an unwanted output.
- **An output's cost share is set by the process; its ledger character is set by its fate.** Manure is pollution debit in a lagoon, a co-product in a biodigester, and an observed fertiliser offset when spread. Fate closure (EventLog IC-4 (fate closure)) already records this; no new machinery is required.
- **Negative values do not arise.** Nothing is inverted, so Steedman's result does not transfer: each share is a forward measurement of what physically went in, and a deposition cannot be negative. ⚠️ *This is asserted, not yet proven for a recursive economy where every input is itself a joint split — see the objections register.*

**Labour is now covered — by declared convention** *(v0.6, OP-18(α))*. Labour has no per-product trace, so it cannot be *measured* into co-products the way materials are. The convention: **labour rides the process's own material split** — the same θ measured above (mass/deposition for cattle, cracking-energy for a refinery, the turbine curve for CHP). This adds no new degree of freedom and no new capture surface: it inherits the rival-audited material split rather than introducing a labour-specific basis. It is honestly a convention, not a measurement (the physical-trace test demands one here), but the *least-arbitrary* one available, and it **changes no one's credit** — the worker is credited their own hours regardless (§6); this only sets how each co-product's *debit-cost* reads. *Shared overhead was OP-23 (shared overhead); v0.5 closed it — capital and overhead accrue to the asset and never allocate to co-products (§6.2b).*

> **What genuinely remains indivisible** is now a single narrow item: apportioning a **jointly-*caused* debit** (pollution or later-discovered harm from a team process) across the team members who caused it. This is a debit-attribution convention, minor and non-blocking, sibling to OP-25 (illicit dumping). Everything else the co-product question raised is closed.

<!-- tag: fnd-s3-5 -->
### 3.5 The books never balance — and must not

Every real process dissipates. Credit records useful work; debit records material and energy consumed plus pollution. **Aggregate debit therefore exceeds aggregate credit permanently and by construction.**

This is not an accounting defect. **It is the second law of thermodynamics appearing in the ledger**, and a material-flow accounting that *did* balance would be the one describing something physically false.

Two consequences:

1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds, not merely impractical.
2. **Sums are not meaningful; two separate numbers are.** **Ratio** (debit:credit) measures *efficiency* — how much you consumed per unit contributed. **Absolute credit** measures *contribution*. Neither substitutes for the other: a pure-ratio metric is infinite for a newborn and is gamed by ascetics who minimize both sides; a pure-sum metric ignores waste entirely.

> **And the scarce factor is not labour**. A recurring result across the societal-scale simulations is that **human hours are abundant, and the binding scarcity is material and energy.** Because self-care is credited work (§6.1b), the credited-labour pool is ~3.4× all *productive* labour — so re-shoring an entire economy's imports, or reallocating the world's captured/wasted hours to essentials, is nowhere near hours-limited (`06-simulation/q1_autarky.py`: an autarkic US is bound by the energy transition and critical minerals, not labour; `q5_reallocation.py`: the freed pool covers the global health-worker shortage ~50–100× over). This sharpens what §3.5 already implies: since debit (materials + energy + waste) structurally outruns credit (hours), the **constraint the system actually binds against is physical throughput, not the supply of human time.** "We cannot afford to make/house/heal everyone" is a statement about money, not about hours.
>
> **The measured anchor (2026-08).** A bottom-up estimate puts the **labour a median US lifestyle commands at ≈ 1,380 h/yr** (`06-simulation/MEDIAN_LIFESTYLE_RESULT.md`; measured from BLS employment-requirements × the actual PCE mix, EXIOBASE import labour, §6.2b durables, and own-pollution remediation — *not* a blanket ratio). Against the ~3,650 h/yr of self-care credit every living human earns, the median lifestyle commands **about a third of one person's annual credit** — the labour dimension has enormous slack, exactly as this callout claims. **And the same-standard efficiency spread is large:** cross-country accounting (EXIOBASE, `06-simulation/Q6.md`) finds the US the labour- *and* carbon-inefficient outlier — commanding **50–80% more embodied labour and 2.5–4× the CO₂ per capita** than Germany, Sweden, France, Japan, or Spain, which deliver a comparable-or-better material standard (and longer lives) at ~⅔ the labour. **This is the positive form of A4 (no externalities) and A5 (price ≡ cost):** the inefficient, fossil-heavy, long-chain method is simply *dearer in the ledger*, so the accounting rewards the efficiency the leaders already demonstrate — no mandate required. What looks like "we cannot afford a decent standard for all" is, quantitatively, an artefact of the most wasteful production method, not a limit of human hours.

**Why this does not collapse the economy, where a currency would.** In a monetary system, aggregate debt exceeding aggregate money is a solvency crisis — debt-deflation, spiral, collapse. Here **there is no creditor to be made whole**, because credit is non-fungible and never moves (A3). Permanent aggregate net-debit is simply the correct description of an economy running on a thermal gradient.

<!-- tag: fnd-s3-6 -->
### 3.6 End-of-life, recycling, and product-as-pollution

An object's life does not end when it stops being useful. Three rules govern what happens then.

**1. End-of-life is consumption if unwanted.** No one can be forced to receive an unwanted asset and its debit (§3.2b). But whoever *does* accept an object accepts the property-debit that rides with it. If nobody will accept a worn-out asset, its **last holder has consumed it** and holds its end-of-life debit forever, as if it were food. This produces three clean incentives, none of them altruistic:

- Prefer durable, repairable goods over cheap disposable ones — you will eat their end-of-life debit.
- Maintain what you hold — a cooperative is better off servicing its equipment than running it to failure.
- Pledge toward remediation and recycling — because doing so *lightens your own* accumulated pollution-debt (§3.3).

**2. A discarded product is itself a pollutant.** A non-functional object sitting in the environment is a pollution-debt for as long as it persists, borne by its final holder, weighted by the stock rule (§3.3). A plastic bottle in a landfill raises the remediation cost of plastic; recycling or atomizing it discharges that debt and lowers every future unit's burden. A compostable object generates none of this, because nature remediates it unaided (§3.3 baseline).

**3. Recycling traces material forward — but not prior pollution.** The **material** of a recycled object carries its accumulated *property*-debit onward (the atoms physically carried forward, §3.4a). It does **not** carry prior producers' *process-pollution*, because under §3.2b that pollution never transferred — it stayed permanently on each producer. So recycled steel is cleanly lower-burden than virgin: it never carried the miner's tailings, and using it commissions no new extraction. **Recyclers are credited** for the work of reducing pollutants; the recycled output re-enters as a low-cost co-input (§3.4a).

> **⚠️ Live enforcement gap — OP-25.** Rules 1–3 price *lawful* disposal correctly. They do not by themselves stop *illicit* dumping — abandoning an object in the environment to escape its end-of-life debit. Attribution of abandonment back to the abandoner is a Level-2 trust-and-provenance problem, registered as OP-25.

<!-- tag: fnd-s3-7 -->
### 3.7 Land is not owned; a building carries a remediation debt

Land cannot be *owned*. A building does not sit on property it holds title to — it **occupies a bounded space relative to the Earth**, and that occupation is itself a debit.

> **Every structure carries a *remediation debt* — the cost to restore its bounded space to its natural state** (strip lead paint and contaminants, remove the foundation and buried piping, refill the excavation, restore native soil and wildlife). It is a property-debit on the structure's holders, weighted by the stock/remediation rule (§3.3), and it behaves like the end-of-life debit of §3.6: it is only discharged to **zero by actually remediating** the space.

Two things persist regardless of remediation: the structure's **construction and maintenance** debts (§3.2, §6.2b) stay in the entity record forever — remediating the land clears the *occupation* debt, not the record of what was built. And the holder bears only what *they* effected: original-construction pollution and human harm stay on the original causer (§3.2b), never transferring to a later occupant.

**Governance rides existing machinery.** The remediation cost is a mitigation-cost estimate under the §3.3 stock-dependence rule and is disciplined by §3.3a rival-sector audit / OP-24 — no new capture surface.

> **⚠️ Hard edge — the "natural state" baseline.** What is the natural state of an already-urban bounded space (a plot in Manhattan)? This is the same shape as the §3.3 pollution baseline (a convention with a measurable basis, contested at the margin) and inherits its governance. **Registered as the open sub-question of this section**; the mechanism is sound, the baseline convention needs specifying.

---

<!-- tag: fnd-s4 -->
## 4. Verification — the Four-Level Ladder

**Level 1 — Peer / witness attestation.** Events confirmed by humans present, multi-party sign-off. Zero infrastructure. Works in any village on Earth today. *Weakness: collusion.*

**Level 2 — Reputation + stake over a social graph.** Verifiers stake reputation; the graph audits attestation patterns. Treated as an **emergent market of trust networks** where auditing is credited work, not as a detector designed up front.

**Level 3 — Sensors + cryptographic proof.** Physical events proven by instruments with signed, tamper-evident records.

**Level 4 — Agentic auditing.** *(far-future)* Autonomous continuous tallying of the full logistical record.

**Design rule:** every level must produce records interoperable with every other level, and the system must degrade gracefully downward. A Level 3 region and a Level 1 region must be able to trade.

**Instrument selection is a ladder question, not a separate discipline**. Under §3.4a, allocating a joint process means choosing and reading the instrument its physics makes available. A Level 1 producer splits a carcass by mass and records low confidence; a Level 3 producer reads calorimetry. **Same rule, same record shape, different rung** — which is exactly what the ladder exists to accommodate.

---

<!-- tag: fnd-s5 -->
## 5. Identity, Privacy, and Onboarding

<!-- tag: fnd-s5-1 -->
### 5.1 Coverage without coercion

- **One verified human = one account.** Hard Sybil resistance is required for integrity.
- **Participation is voluntary. Coverage is not.** Non-participants are estimated on **both sides**:

| | Estimated from |
|---|---|
| **Debit** | Demographic cohort average, computed *excluding* registered participants. Public figures estimated from publicly known wealth and holdings. |
| **Credit** | Cohort production model — occupation, region, known activity, computed *excluding* measured producers (§5.1b). |

- **Non-participants can neither draw on nor be charged for their estimated position.**

<!-- tag: fnd-s5-1a -->
### 5.1a Realization

1. **Verified account** (C6 (identity)).
2. **Observed supersession** — the estimate is replaced by attested records, under monotonicity (records may only improve toward stronger basis and finer resolution; an observation may never be superseded by an estimate).

**Assertion is not evidence.**

> **The floor rule — monotonicity's second axis.** A quantity computed over **incomplete coverage** is a **floor, not a value**. Under-recording can only understate, so a recorded figure is a lower bound on the true one and improved coverage moves it in one direction only: up.
>
> Monotonicity governs *basis* — how well a thing is known. The floor rule governs *extent* — how much of the world was looked at. Together they say a record may only ever get better, and that a partial input **downgrades a claim rather than invalidating it.** A verdict whose closure basis is absent is reported as a floor, with the gap named (EventLog §7.4).

**A record is never purged or edited, only annotated.** A figure later found wrong is *contested* — an appended, dated, attributed note carrying its own provenance — and separately superseded if a better record exists. Falsehood is not prevented at write time; it is made permanent, traceable, and arithmetically exposed the moment any part of its extent is measured (EventLog §7.2a, §8.2a). **This is how science works, and it is the only defence that does not require an authority at the gate.**

<!-- tag: fnd-s5-1b -->
### 5.1b The residual rule — averages cover only the unmeasured

An unmeasured producer's estimated output is the **independently-known total minus what measured producers actually produced, divided among the producers who remain dark**:

> **estimate = (N − Y) / Z** — *N* the independently-known total (FAO figures, trade data, satellite survey), *Y* the measured producers' recorded output, *Z* the count of unmeasured producers.

**Computed over the whole population instead, this creates adverse selection.** Better-than-average producers instrument to prove it; worse-than-average stay dark and free-ride on an average their own absence inflates. Over the residual, the estimate *worsens* as good producers exit — **so darkness stops paying.** This is the same discipline already applied to the cohort debit average above, extended to production.

**Two conditions.** It requires an independently known *N*, which exists for major commodities and not for everything; and a defensible count *Z*, since under-counting dark producers over-states each one's share.

**The witness generalises beyond production.** *N* is the **closure witness** — a physical total measured *outside* the ledger and reconciled against the ledger's own sum. It asserts nothing about anyone's honesty; anyone with the same instrument computes the same residual. The same reconciliation runs on any conserved dimension against any physical reservoir, and §3.3's **ambient-stock measurement** is already exactly such a reading — it has simply been used as a weight input rather than as a coverage statement.

| Flow type | Closure witness | Authority required |
|---|---|---|
| account → account | **The counterparty.** A hand-off has two sides; a unilateral omission dangles on the other party's record. The witness is an adversary with the opposite interest. | None |
| account → commons | **The reservoir stock.** Measured depletion or accumulation minus the sum of recorded flows. | None — an instrument |
| fully disjoint chain | **(N − Y) / Z.** No shared edge, no shared parcel; only an independent total can see it. | None — an instrument and a tally |

> **The conservative-count rule.** When *Z* is uncertain, **under-count it.** Under-counting raises each dark actor's estimated share, which is the direction that provokes them to surface and prove otherwise (§5.1a). Over-counting dilutes the estimate and feeds **OP-24**. **The self-liquidating error is the safe one** — nobody complains about being charged too little.

**The estimate is continuous, not a one-off.** As part of an extent becomes measured, *Y* rises, *Z* falls, the estimate shrinks to the remainder, and the parts must reconcile against the coarser figure they came from (EventLog §7.2a). Grapes tallied as one region become one measured region and one still estimated. **This is also what catches a fabricated total: a fabricator does not control which sub-extent is measured next.**

*One method for *Z* worth recording, because it needs no headcount:* **Z ≥ (N − Y) ÷ capacity**, where *capacity* is the most one actor could physically produce — bounded by hours in a day, land, or throughput. Using that minimum assigns each dark actor the most they plausibly could have, which is the conservative direction. **A candidate method, not the method** — the capacity ceiling is itself a constant under §3.3a, though one bounded by physics rather than free.

**"Dark" means outside Aequitas, not low-tech within it.** Participation carries a transparency requirement — a good moving through the Aequitas economy carries records of its origin. Seeking data on non-participants, and assisting producers to bring their supply chain into the record, are both **credited trust-network work**.

<!-- tag: fnd-s5-1c -->
### 5.1c The residual is held, not allocated

A coverage gap is real material that really moved. The question is whose books it sits on, and the answer is **nobody's — yet**.

> **The residual is computed, published, and left unassigned. It is not debit on any account. When a dark producer onboards, their share is back-traced from the records that already exist and assigned to them — the actual causer. Until they onboard, they cannot transact inside the system at all.**

**Why this is the axiom-respecting answer and not a dodge.** A4 (no externalities) is not abandoned here; it is **pending**. The cost does not vanish and is not written off — it is held as a computable claim waiting for a claimant. Assigning it to innocent participants in the meantime would contradict the rule that consumption and pollution debit **stays with whoever caused it** (§3.2), and would be collective punishment in the exact sense §3.3 already rejects.

**Nothing extra has to be built to make the back-trace possible.** Both records already exist and are already kept for other reasons: the **ambient-stock measurement** of regional pollution (§3.3) and the **independently-known production total** of §5.1b. A producer's share is derivable from those the moment there is a producer to derive it for.

**And the damage is not unpriced in the meantime.** Because pollution weight floats with the **ambient stock** (§3.3), the dark producers' emissions are already in the stock everyone is weighed against. Participants therefore pay a rate that reflects the *total* damage while being charged only for their **own** units — proportionality, not collective punishment, exactly as §3.3 states. **The residual is felt correctly without being allocated.**

**What the gap is instead of a debit: a published coverage figure.** *"These books cover 60% of this region's measured output."* That is the extent rule (EventLog §7.4) at regional scale, and it does real work — a counterparty re-computing under its own model (OP-14) can discount goods from a thinly-covered region. Coverage becomes a quality property of a network's own output rather than a charge against its members.

<!-- tag: fnd-s5-1d -->
### 5.1d The back-trace horizon is birth — and it runs on both sides

**The back-trace reaches back to the person's birth.** Not to the ledger's epoch, not to the onboarding date. A whole life.

That sounds punitive and is the opposite, for one reason that has to be stated first and never dropped:

> **The back-trace is symmetric. Both sides are reconstructed — the debit *and* the credit.**

§5.1 already estimates non-participants on both sides, and §7.5 credits every living human for the work of staying alive, qualified by *being alive* rather than by being able to work. So a lifetime back-trace brings a lifetime of self-care credit with it.

**The arithmetic, which is the whole argument.** A median lifestyle embodies roughly **1,380 hours** of others' labour per year (§3.5). Simply being alive credits roughly **3,650 hours** per year. Per year of life, credit runs about **2.6×** consumption. A person onboarding at forty therefore arrives with roughly 146,000 hours of estimated credit against roughly 55,000 hours of estimated consumption.

**Onboarding is a windfall for a median person, and that is not a coincidence — it is §5.2's adoption incentive, computed.** The people for whom a full back-trace is *costly* are those whose lifetime consumption genuinely exceeded their lifetime contribution. That is correct targeting, not a defect.

**Estimate is the default; evidence is voluntary and moves you off it.** An onboarding person supplies whatever narrows the estimate — where they were born, how long they lived in each place, which jobs they held, how far they commuted, which cars they owned and the mileage on them — and **accepts the cohort estimate for every period and activity they leave dark.** Nothing is compulsory.

**Evidence moves the figure in either direction, and that is why people supply it.** Mileage records plus a car model may show a hybrid driven below the commuter average — and the debit falls. The same records could raise it. The point is that the estimate is not a verdict.

**Details may arrive at any later date, and the ledger re-derives.** This needs no new machinery: the ledger is derived from the log and never stored (A6), and §3.3 already recalculates every affected record when the science improves. **A life is refined the same way a cost constant is.** Supersession stays monotone (§5.1a) — an observation may never be replaced by an estimate.

**Two conditions make this work, and without either it breaks.**

1. **Estimates for undisclosed periods are computed over the *undisclosed residual*, not over the whole population.** This is §5.1b's rule generalised from producers to periods and dimensions *within a life*. Without it, a person who documents only their flattering years free-rides forever on an average their own silence inflates. With it, the pool of the undisclosed worsens as the well-documented leave it — the same adverse-selection reversal, one level down. **Selective disclosure is expected and is not an exploit, provided the residual rule holds.**
2. **An estimate errs against the estimated party, on both sides.** Debit is estimated at the unfavourable end, credit at the conservative end, so **supplying evidence always pays** whichever direction the truth lies. This is the conservative-count rule (§5.1b) applied per person.

> **The floor is exempt, and must stay exempt.** The self-care floor is **not** an estimate — it is credited by proof-of-life (§6.1b, §7.5), and being alive is the whole qualification. So condition 2 never bites on subsistence. **Someone who cannot document a life is not thereby impoverished by this rule**, which is the difference between a conservative estimate and a punishment for poor record-keeping.

**Why this does not contradict §5.1 or the transaction-time rule.** §5.1 forbids charging a **non-participant** for an estimated position, and that is untouched — nothing is charged until they onboard, and onboarding is voluntary. The transaction-time rule (§3.3) protects **completed acts that the system gated at the time**; pre-onboarding acts were never gated by Aequitas, so there is no permission being revoked retroactively. **What is reconstructed is a position, not a verdict on past conduct.**

> ⚠️ **This escalates OP-22 (minimum audit disclosure) sharply, and that is the strongest objection to it.** A full back-trace is a life dossier — birthplace, every residence, employment history, commuting distance, vehicles owned, mileage. Disclosure is voluntary, but the *incentive* runs toward disclosing, so the system exerts steady pressure on people to assemble exactly the record a surveillance state would want. **§5.3's "market data public, personal ledgers private" now has to hold across a lifetime**, and OP-22's question — proving a claim is backed without exposing the history behind it — becomes the load-bearing privacy problem of the whole system rather than a C7 implementation detail. **Registered, not solved.**


<!-- tag: fnd-s5-2 -->
### 5.2 Onboarding as resolution — and as the adoption incentive

Joining replaces an assigned average with your real record. Two forces make it rational: most people's true footprint is *below* their cohort average, and **their estimated credit is unrealized until they join.**

The pitch is: *here is what you have contributed, and here is what it cost; join and make it yours.*

**The cost of joining is administrative labour, not a penalty**. A producer without instruments genuinely needs more human hours to produce the same verified record, and those hours are a real material cost under A1 (materialism of cost) — not a thumb on the scale. The incentive to instrument is the ordinary incentive to reduce a real cost.

> **⚠️ Watch item: fixed onboarding costs consolidate industries.** Documentation burdens are repeatedly argued to disadvantage small producers — which is why [organic certification cost-share programmes](https://www.ams.usda.gov/services/grants/occsp) exist at all, and the same argument is made of [REACH](https://echa.europa.eu/regulations/reach/understanding-reach) and [FSMA](https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma). The structural offset is that **onboarding assistance is credited work borne by the trust network rather than the entrant.** Whether that is sufficient is empirical and should be watched, not assumed.

<!-- tag: fnd-s5-3 -->
### 5.3 Privacy — market data public, personal ledgers private

> **The transparency of Aequitas is split by *level*: the market is radically transparent, persons are private.** Pledges, production quantities, hand-offs, and debit-costs — the *supply-and-demand record* — are public (a pledger may be anonymous, like a Kickstarter backer, but the pledge itself is visible). Individual persons' aggregate positions stay private.

This split is **load-bearing, not incidental.** Public market data is what makes §3.3a rival-sector audit and independent economic monitoring *possible at all* — a worker can read how in-demand their product is; an auditor can watch a supply chain; nobody can privately mislabel pledged-vs-speculative work against a public pledge ledger (§6.4a). Public flows are the same "make it public so it cannot be gamed in private" move used for co-product splits (§3.4a) and cost constants (§3.3a).

> **⚠️ But transparency *depends on* OP-22 (audit disclosure), it does not bypass it.** Public pseudonymous events can be chain-analysed to de-anonymise a person — the classic ledger-privacy problem. Reconciling **public flows + private persons + unlinkability** is exactly OP-22 (the minimum-disclosure question below). The Kickstarter-anonymous intuition is the right shape; the mechanism is unsolved.

Account holders keep a **private ledger with provable claims** — zero-knowledge proofs of balances and cost positions when transacting, not history.

**This is roughly where society already sits, and that is the point.** People transfer money to each other today knowing their counterparty and nothing about third parties' accounts. Nobody audits those accounts, because validation trust is externalized to banks. **Aequitas does not need more visibility than that; it needs the same visibility with the trust relocated.**

**Aequitas also does not replace existing recourse.** Courts, small claims, contract law, and ordinary social pressure continue to exist and continue to handle fraud between people. The system's contribution is upstream of enforcement: by removing wealth concentration and material insecurity, it **removes most of the motive** for the scams those mechanisms exist to punish.

> **⚠️ The narrow question that remains — OP-22.** The bank analogy has one gap: there is no bank to externalize validation to. Verification is the trust-network ecosystem (Level 2), and an auditor must be able to see *something*. So the live question is not "surveillance or privacy" but **"what is the minimum an auditor must see to verify a claim without seeing a history?"** Zero-knowledge proofs are the right shape of answer and are already specified above; what is missing is the precise disclosure set.

<!-- tag: fnd-s5-3a -->
### 5.3a Privacy is a network choice — Aequitas sets principles, not practice

**The gap in the bank analogy closes by naming what plays the bank's part. It is the trust network.** The network does the tallying and the tracking, so it is the party that holds what is private — and it is therefore the party that decides how privacy works.

> **Each trust network sets its own privacy practice. Aequitas states the principles and does not dictate the implementation. Compatibility between networks is a matter for those networks to negotiate.**

**The working shape is the payment intermediary.** A card network today facilitates a transaction in which **neither party learns the other's private details**. The intermediary knows both sides; the counterparties know a token and an outcome. That is *pseudo-privacy*, it is deployed at planetary scale, and it is the nearest existing analogue of what a Level-2 network does here.

**A network may also choose the opposite.** Radical transparency — no personal privacy at all — is an available and legitimate setting. Nothing in the axioms forbids it. Some communities will want it.

**This is the same move as ρ and the self-care floor `F`.** Aequitas *uses* those dials and never sets their value (§3.5, A8). Privacy is a third dial of the same kind: a network-level choice that the accounting reads and never legislates. **A global privacy constant would be exactly the central authority A8 forbids.**

**Opacity is priced, not forbidden — and that is what stops network-shopping.** A counterparty re-computes a claim through its own model (OP-14) and **discounts what it cannot verify**. So a network that chooses heavy opacity finds its members' claims trade at a discount elsewhere, exactly as a network with thin coverage does (§5.1c). **A network's privacy level becomes a priceable property of its output** rather than a rule anyone enforces — the same shape as every other answer in this document: *price the costly path rather than forbidding it at a door somebody has to guard.*

**Three residues, and none of them is small.**

> **⚠️ (a) The network becomes the most information-rich actor in the system.** Whoever tallies, holds. A Level-2 network that keeps its members' lifetime back-traces (§5.1d) holds a concentration of *information* comparable to the concentration of *wealth* this project exists to dissolve. §3.3a's public-membership capture screen was written for **sector** capture and does not address **information** capture. **This is P4/OP-10 shaped and it is currently unanswered.** "You may leave" is a weak exit when the thing you would be leaving behind is your life history.

> **⚠️ (b) Privacy has a measured coverage cost.** Privacy-preserving verification is more expensive than open verification. `06-simulation/residual_unravelling.py` measures where that matters: **once verification costs more than roughly 40% of a median unit's debit, the residual rule stops unravelling the dark pool and darkness becomes stable again.** A network is therefore choosing, whether it knows it or not, on a curve with coverage at the other end. **The trade-off is real, it now has a number, and no network should pick a privacy practice without pricing it.**

> **⚠️ (c) A network's choice binds members who did not make it.** Children born into a radically transparent network, and people who joined before a practice changed, did not choose it. Entry, exit, and the portability of a personal record across a privacy boundary are **C2 questions**, and this ruling adds them to C2's list.

**What is settled and what is not.** *Who decides* is settled: the network. *What Aequitas mandates* is settled: principles, not practice. **What remains open is the minimum disclosure set itself** — what an auditor must see to verify a claim without seeing a history — which stays a C7 implementation problem, now with a named holder and a priced trade-off attached.

---

<!-- tag: fnd-s5-3b -->
### 5.3b What a trust network owes, and what "funding" one means

§5.3a settles that a network chooses its privacy practice. This settles what it owes in return, and dissolves the question of how it is paid for.

#### The tally is an algorithm, and the algorithm is published

**Tallying is algorithmic.** The estimate for a dark producer, the residual arithmetic of §5.1b, the cohort model of §5.1 — these are computations, not judgements exercised case by case.

That matters more than it sounds, because it is what makes §3.3's *citation* requirement enforceable. **"Cite your method" against a human process is an aspiration. Against a published algorithm it is a version number**, and `method_ref` (EventLog §4.1a) has something concrete to point at. Anyone can re-run it on the same inputs and get the same answer, which is the whole content of "not an authority assertion."

> **To be trustworthy, a network publishes: every estimating number it uses, every method, and anonymised data covering all of its participants.** Its books are in the light. A network that will not show its arithmetic is asking to be trusted rather than checked, which is the thing this system exists to stop needing.

**How much to reveal about institutions, co-ops and individual businesses is the network's own call**, balancing the confidence transparency earns against the privacy its members want. That is the §5.3a dial again, applied to entities rather than persons.

> **⚠️ And it cuts against itself.** Anonymised participant data is *more* re-identifiable the more of it there is — the chain-analysis problem §5.3 already names. **Publishing more to earn trust also publishes more to de-anonymise.** A network is choosing on this axis whether it means to or not, and it is a different axis from §5.3a's verification-cost curve, not the same one twice.

**What the publication rule does buy is a sharper bound on information capture.** §5.3a's residue (a) was "the network becomes the most information-rich actor." With full anonymised publication, its remaining advantage narrows to exactly one thing: **it holds the linkage between the anonymised rows and the people.** That is a much smaller and much more attackable statement of the problem than the one it replaces — still unsolved, but now specific.

#### "Funding" is not a budget — it is recognition

**There is no treasury, no allocation, and no grant.** Asking who *funds* an auditor imports a question from money that does not survive translation.

> **Funding, in Aequitas, is simply the recognition of an activity as creditable.**

Audit work is work. It is recorded when it happens, and recording is never gated on approval (§6.4a, EventLog §5.1b) — gating recording on permission would contradict **A7** and re-open the origin-closure failure A7 repealed. So the credit for doing the work is not scarce and never needed a funder.

**What *is* scarce is demand and verification.** A **pledge** says someone wants the work done (§6.4); **verification** decides when the credit realizes (§6.4a). Those are the real levers, and they are the ones §3.3a's rival-sector argument already pulls: the instrumented producer harmed by a cheap dark competitor is the party who *pledges* for the audit.

**This narrows OP-24 rather than answering it.** OP-24's complaint was that a correction which worsens every subscriber's ledger has "no funder." The **funding** half dissolves — there was never a budget to find. The **incentive** half stands untouched: someone must still *want* the correction, and for an understating weight constant, the rival sector is still the only party who does.

**Participants may pledge toward the network's own infrastructure** like any other work. Nothing special is needed for it.

#### The bootstrap: a network's founding is its own genesis entry

A trust network is the basis on which all accounting rests, so it cannot be paid by an accounting that does not exist yet. **The network is created first. Assigning its founders credit for creating it, once it is live, is the network's own decision, however it chooses to be governed.**

**This is not a special case, and it should not be written as one.** It is exactly the situation §6.2a already handles: a **genesis entry** admits a thing that existed before the ledger, at an estimated cost, crediting the estimator, superseded when better records appear. And §5.1d has just established that reconstructing a position from before the ledger existed is ordinary rather than exceptional.

> **A network's founding work is admitted the way any pre-ledger asset is admitted: as an estimated record, entered after the fact, open to supersession.** The bootstrap is a genesis entry pointed at the network itself.

> **⚠️ The one genuinely unguarded record in the system.** Founding credit is written when there is no counterparty, no rival network, and no prior ledger to check it against — the single case where nothing contemporaneous can verify a claim. Three things bound the damage rather than prevent it: **IC-7** caps it at wall-clock hours × founders, so it cannot be arbitrarily large; it is **publicly recorded** and a later network can re-compute it (OP-14); and because credit is **non-transferable** (A3) and consumption is ratio-gated, over-crediting founders buys only consumption room, **bounded by the `24/F` ceiling** like everyone else's. *The disparity ceiling doing exactly the backstop job it was argued to do is worth noting.* **Bounded, not closed. C2 should say what a network's founding record must disclose.**

<!-- tag: fnd-s6 -->
## 6. One Credit, Three Feedback Channels

**There is one credit: time spent by a person, recorded as material flow.** Production, service, and enrichment are **not** different credit types and do not credit at different rates. Everyone earns at the same rate and therefore influences at the same rate.


**The categories have no accounting boundary and no rule may use them as one.** An apprentice plumber's single hour is simultaneously enrichment (learning the trade), service (fixing a customer's pipes), and production (copper and fittings → working plumbing). That hour is not partitionable, and any attempt to partition it would require yet another allocation convention (§1.1).

What the three names *do* describe is **how feedback reaches the work** — how a society tells someone that what they did mattered.

<!-- tag: fnd-s6-1 -->
### 6.1 Why "enrichment" is named at all

**To give grounds for crediting work that no economy has ever credited.**

Going to school is work. Today we make students or their parents pay for it — the relationship is inverted. Teaching your own child is work. Caring for a relative is work. None of it is paid, and in a system that does not incentivize with material gain — *"go to school if you want to make money"* — something must make socially beneficial activity individually rational.

Enrichment is the name for work whose benefit flows **from all of humanity to at least one person, in ways not readily measured in material.** It is credited because it is real work, not because it is virtuous.

**Childcare is creditable work regardless of who performs it.** This alone brings the largest uncounted labour pool in human history onto the books.

<!-- tag: fnd-s6-1b -->
### 6.1b Self-care is credited work — and it is the floor's mechanism

If work is time spent maintaining human life (§6), then maintaining *your own* living body — sleep, sustenance, basic hygiene, recovery — is work, exactly as caring for another's body (§6.1) is. It credits because the time was spent; that the maintenance is partly *passive* is irrelevant, because the measure is time, not effort (§0). This is the extension of the social-reproduction insight from caring for another to maintaining oneself.

- **It is the mechanism of the §7.5 basic-needs floor, not a grant.** The floor could not be an *issued* allowance — credit-for-nothing would break "credit = time worked" (A2 (time as measure)). As *credited maintenance time* it is no grant at all: every living human performs the real work of staying alive, and it credits at the universal rate. The floor is simply where that credit lands. This resolves what had looked like an axiom conflict: the floor is derived, not bolted on.
- **Same shape as the subsistence identity (§3.2).** Crediting the labour of maintaining the human, against the material cost of maintaining it (food, shelter energy), makes being-alive close to *net-neutral* rather than net-negative — which is exactly what a basic-needs floor is for, and answers the standing worry that permanent consumption debit (§3.5) drives every ordinary person into ever-deeper deficit merely for existing. Self-care is a credit stream sized to the cost-of-living debit stream.
- **Its magnitude is a weighting choice, set per network.** How many hours a day count as necessary self-maintenance (≈10 h is a defensible physiological figure — ~8 h sleep is not arbitrary) is set by each trust network for its subscribers, and disciplined like any weighting (§3.3a). Generosity here is product differentiation, not a rule anyone imposes (§10.1) — and it **cannot be exported**: a counterparty re-computes a pledge's backing through its own model (§6.4a), so an over-generous floor is discounted by whoever trades with it, never forced on them.
- **Verification is proof-of-life** (§6.4a). A verified living human (C6 (identity)) demonstrably maintained itself over the period — the strongest evidence there is, at near-zero verification burden. Self-care credit therefore realizes continuously and is pledgeable (IC-8 (pledge backing)); what its pledging-power *does* is §6.4 and §7.5.

<!-- tag: fnd-s6-2 -->
### 6.2 Training, front-loaded

**A student is credited for their time while training.** The debit of training — teachers' time, facilities, materials — is **carried up front, during the training years, cushioned by the debit-room that pledgers grant for it** (§6.4). A pledge underwrites the training without moving the pledger's credit and without amortizing onto whoever the trainee later serves.

**Nothing flows downstream.** A doctor's care costs the recipient exactly: the doctor's time, the material cost of running the clinic, and the medicines and correctives dispensed. **The doctor's education is not in that bill.** It was already underwritten up front, by the people who wanted doctors to exist.

Why this is right and the v0.2 rule was wrong:

- **It makes training individually rational without any rate premium.** The old rule made the *service* expensive without ever rewarding the *trainee*; it answered a pricing question and left the incentive question open. Being trained is now paid work.
- **It matches who benefits.** Education's benefit is diffuse, so its cost should be borne diffusely. Charging it to one patient decades later is arbitrary — precisely the amortization problem that made OP-11 (training amortization) unanswerable.
- **It dissolves OP-11 rather than solving it.** There is no longer a cost to amortize over an uncertain career.
- **Pledging supplies the natural limit.** Society decides how many doctors to train by pledging for it. Unpledged study still credits the student's time — A7 (universal accounting) requires that, it is real activity — but leaves them holding the debit. **No perpetual-studenthood exploit.**

<!-- tag: fnd-s6-2a -->
### 6.2a The Front-Loading Rule

Training is the first instance of a general rule, and the rule is worth stating once — and naming — rather than rediscovering per case. It is referenced across the theory as **the Front-Loading Rule**:

> ### 🔒 THE FRONT-LOADING RULE
> **A large up-front cost with a diffuse benefit is carried where it is incurred and cushioned at that time by the debit-room the people who pledged for it grant. It is never amortized downstream onto whoever happens to consume the result.**
>
> **Covers:** education (§6.2), media/creative production, research · infrastructure · tooling, and **capital & overhead** (§6.2b — which is *why* it also closed OP-23).
> **Why it's right:** the downstream window is always arbitrary (that arbitrariness *was* OP-11/OP-21), and downstream amortization triggers an infinite regress to the first human activity — **computational closure** (the upstream face of the §3.2b non-cascade rule).
> **Boundary:** capital vs. consumption, told apart by **physical fate** (does the thing survive the process?), auditable via IC-4 (fate closure) — not by the producer's declaration.
> **Who carries the capital:** the §6.2b waterfall — the full creation-cost is holding-time-split among the asset's holders; community pledges grant debit-room that cushions the bite; basic-needs-floor cap.
> **Dissolved:** OP-11 (training amortization), OP-5 (education), OP-21 (media) as one malformed question (B3); OP-23 (shared overhead), by accruing capital to the asset, never to co-products (B8).
> **Honest residue:** cold start (a first-time creator attracts no pledges); a per-unit debit-cost is therefore *not* a full-lifecycle figure — the capital footprint sits on the asset, never lost (no A4 breach), just located honestly.

Three instances so far:

| Case | Front-loaded cost | What the eventual recipient pays |
|---|---|---|
| **Education** | Teachers' time, facilities, materials | The professional's time, clinic materials, medicines — **not the education** |
| **Media production** | Years of crew time, sets, equipment, post | **Delivery only** — theatre maintenance, projectionist hours, print or bandwidth, power |
| **Research, infrastructure, tooling** | The build | Use, wear, and energy |

**Why downstream amortization is always the wrong answer.** It requires choosing a window (how many patients? how many viewers?) and every candidate window is arbitrary. That arbitrariness *was* OP-11, and it is also what made OP-21 (media reproduction) look hard. **The question was malformed in both cases.** Front-loading removes the division rather than solving it.

**The decisive reason, though, is computational closure**. If a hospital's construction were amortized into each patient's bill, the accounting would have to chase the construction company's costs, then the equipment manufacturer's, then the steelmaker's, then the doctors' education — **an infinite regress to the first human activity.** The accounting would never terminate. Front-loading is what makes it *terminate*: you never chase an asset's own history, because the asset carries whatever creation-cost is knowable within Aequitas and everything upstream is out of scope by construction.

> **This is the upstream face of the non-cascade rule in §3.2b.** Pollution not transferring downstream to a buyer and cost not regressing upstream to the first human are the *same* constraint: **cost attaches only to the causer, and never cascades to anyone who did not act.** Ellerman-imputation and computational closure are one principle read in two directions.

> **The boundary is capital vs. consumption, not temporal.** A cost flows to a unit only if it is *consumed* producing that unit. A durable asset's *acquisition* is capital (front-loaded); only what it *consumes now* — energy, materials used up, wear — is a flow. The two are told apart by **physical fate**: does the thing survive the process? A drill bit that survives is capital; the oil it burned is consumption. Auditable via IC-4 (fate closure), not by the producer's declaration — which closes the *consumption-launderer* (reclassifying a used-up input as capital to move its debit off the unit).

**Corollary — pre-Aequitas assets**. A cooperative taking over a 50-year-old hospital cannot reconstruct the architects' fees or the original currency costs. The asset *enters* Aequitas and accrues history from genesis forward; the pre-genesis past is unrecoverable — the same cutoff, in a new domain. v0.7 makes the entry precise:

- **Recording a "before" object is a *choice*.** Leave it unrecorded → it is invisible to Aequitas, with no registered ownership (a thief inherits no debt; fine for clothing and heirlooms one intends to keep). But an object cannot receive *creditable work* without a record — repairing an old fridge requires the fridge to exist in the ledger so the repairer can be credited.
- **When recorded, the entry is an expert *estimate*, not zero and not a reservoir extraction.** A qualified estimator reconstructs the construction labour and materials **plus all subsequent rehab**, at `basis: modelled`, low confidence, superseded by real records later. **The estimator is credited** for the estimation work. The dollar purchase price is worthless as a basis — estimate the material/labour cost instead.
- **Genesis is a distinct origin-terminus, not a reservoir.** A pre-Aequitas object did not enter *from a commons inside the system*; it enters as an estimated **genesis entry**, which is a legitimate endpoint for backward origin-tracing (EventLog IC-3 (origin closure)) alongside a reservoir extraction — but it is not dressed up as one.
- **Original-construction harm does not transfer to the current holder** (§3.2b). A 200-year-old building may have been raised with slave or unrecorded labour and its era's pollution; the *current* holder bears only what they effected during their tenure (the gas stove's methane), never the original construction's suffering or emissions.
- **The reconstructed creation-cost is holding-time-split, not dumped whole on whoever holds it now** (§6.2b). The estimator's figure — original construction labour and materials *plus* all subsequent repairs and modifications over the asset's life — is the asset's **creation-cost**, and it settles by the ordinary holding-time waterfall: each holder's permanent share = **their holding-duration ÷ the asset's total life**. A person who owned a property for 20 of the 200 years it has existed therefore carries **10%** of its construction-and-rehab debit, not all of it. This is *why* the pre-Aequitas entry cannot bankrupt a new owner: entering an old asset does not import its whole two-century debit onto the person at the door — it imports only their tenure's slice, and earlier holders' shares stay pinned to those holders (estimated on the same terms, §5.1) or ride the asset as an un-attributed remainder until its life completes (no A4 (no externalities) leak). Rehab is split the same way, over the years since *that* rehab, so a repair done a decade before you arrived is mostly not yours either.
- **An auditor may create the record without the owner's consent** (A7 — everyone is accounted). A reluctant owner's mansion can be entered from estimates of its size and construction; if the owner later joins, they may *refine* it (with contractor records, motivated to show the debt is lower than estimated) — but the only route to a favourable credit:debit ratio is to **transfer the debt** to others, not to hide the asset.

**The consequence for media is worth spelling out.** Pledgers replace studios and investors, and **they receive no profit and cannot receive one** — so there is no mechanism by which a popular film gouges its audience at the box office. A production company's only return is recognition, which converts into demand and pledges for the next work. That is the entire incentive, and it points at making something good rather than something extractive.

**⚠️ Cold start.** Pledges follow reputation, so a first-time filmmaker attracts none — structurally similar to the problem unknown creators already face with capital. The barrier is far lower (attention, not money) and the ladder is real: make small unpledged work, accrue feedback (§6.3), then attract pledges. But it should be stated honestly rather than assumed away.

<!-- tag: fnd-s6-2b -->
### 6.2b The capital-debit waterfall

Front-loading says *when* a durable asset's cost falls due. This says *who carries it, and what a pledge actually does to it*. A building, plant, or tool holds its own **creation-cost as property-debit on the asset itself** — property-debit attaches to objects (§3.2), so this is A1-clean. That debit is settled in three steps:

1. **Community pledges grant the holders debit-room to carry the creation-cost.** A pledge does **not** draw the creation-cost down: it is a *permanent grant of debit-room* — virtual credit conferred on the receiving cooperative, drawn from the pledger's finite lifetime pledging-budget (§6.4). The pledger's credit itself never moves and is never earmarked; the cost is that a pledged hour is spent from that budget for good. To the receiver it acts as virtual credit, defraying the bite of the fixed cost. Pledges are simultaneously the **construction authorization** and the **demand brake** — a facility is built at the scale the community will pledge for, the same "pledging supplies the natural limit" logic as §6.2. *(Hospital: a 100k creation-cost with 50k pledged still sits at 100k on the asset — but 50k of pledge-granted debit-room means only 50k of it effectively restricts the holders.)*
2. **The full creation-cost is holding-time-split among the asset's holders** — pledges cushion the bite, they do not shrink the debit (nothing may vanish, A1). Each holder's permanent share = **their holding-duration ÷ total holding-duration over the asset's whole life** (§1.1). Because pledges are **permanent and non-revocable**, the granted debit-room does not evaporate under a holder — the cooperative can rely on it, which is precisely what lets it undertake capital-heavy or hazardous essential work without a withdrawal hanging over it. The discipline on the pledger is therefore *at pledge time* (an hour pledged is spent from a finite budget), not an ongoing threat of retraction.
3. **The basic-needs floor caps how hard any residual bites** (§7.5).

**Why holding-time, and why it beats an even split.** Holding-duration is a *physical trace*, so the split is measured, not invented, and it passes the cooperative-game checklist an even split fails:

- **Dummy** — zero holding-time → zero share. A new hire bears ≈0, which kills the **entry-toll** an even split would impose on exactly the capital-intensive essential work (hospitals, water treatment) society most needs staffed.
- **Symmetry** — equal holding-time → equal share.
- **Progressive, and final only at disposal.** While the asset lives, earlier holders' shares *dilute* as new holding-time accrues; they freeze at disposal. This is A6 (derived, not stored) (progressive resolution), and the not-yet-attributed remainder rides the asset until its life completes — **no leak.**

**Worked example.** A holds a thing 1 year, passes it to B, B uses it 1 year, then it is disposed. Total = 2 holder-years → **each holds 50% of the creation-cost, forever.** For a multi-staff facility the denominator is holder-years across *all concurrent staff*, so shares dilute hard: a 30-year veteran among ~200 staff over a 60-year hospital holds ≈0.25%, not a crushing slab. A solo owner-operator of expensive private capital holds a large share — correctly; they solely used it. **Private durable goods** (no pledges) simply holding-time-split their full creation-cost across successive owners.

**The holding-time clock starts at *deployment***. A durable good's ledger records the moment it **enters service** — a toaster's clock starts roughly at purchase, even if it sits boxed for a year. Holding-time (above) is counted from deployment, because deployment is when a holder begins actually *using* the asset and accepting its load.

> **Transit custodians do not accrue a creation-cost share**. A carrier holding 1,000 toasters for two days did not *make* them, so they take **no** holding-time share of the toasters' *creation-cost*. Transit adds only the carrier's own **transport-debt** (their labour + fuel, attributed to them, §3.2b), which becomes embodied cost in the goods. Creation-cost holding-time-split begins at **deployment/operation by an end-holder**, not during transit. This keeps the supply-chain hand-off model (§6.4a) — where every carrier briefly holds the goods — from silently loading the making of the toaster onto the truck driver.

**This closes OP-23 (shared overhead).** All capital and overhead accrues to the asset and its holders; **it never allocates to co-products.** The barn stays on the operator; hide and beef carry only their own consumables. The honest trade-off: a per-unit debit-cost is therefore *not* a full-lifecycle figure — the capital footprint is located on the asset, not smeared across units, and is never lost (no A4 breach). See `00-strategy/OP-23_capital_and_pollution.md`.

<!-- tag: fnd-s6-3 -->
### 6.3 Feedback: what each channel looks like

Feedback is **not credit** and never converts to it. It is how a society signals what it wants more of.

| Channel | What feedback looks like | Already exists today as |
|---|---|---|
| **Production** | The in-demand shoe sells out | Stock-outs, waiting lists, pre-orders |
| **Service** | Someone chooses you as their doctor, plumber, therapist | Ratings, referrals, repeat custom |
| **Enrichment** | People signal appreciation for the work | Likes, reviews, citations, applause |

**Non-convertibility, restated correctly.** v0.2 asserted that "Enrichment is not convertible to time or material" and then needed a firewall to enforce it (old OP-8 (feedback firewall)). Under the corrected structure **no firewall is required**: enrichment *work* credits as time like everything else, and enrichment *feedback* is non-convertible because **it was never credit in the first place.** There is nothing to firewall.

**The live question is the inverse, and it is real: can feedback be *bought*?** A signal that credit can purchase is a currency by the back door. This is what OP-8 becomes.

<!-- tag: fnd-s6-4 -->
### 6.4 Pledges and signals

Credit-earners direct what gets worked on next. Two distinct instruments, distinguished by one test:

> **Is it backed 1:1 by earned credit?**

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I authorize this creditable work" | "I want this to exist" |
| Backed by | earned credit, 1:1 | nothing |
| Rate | **1 hour pledged per hour earned — a finite lifetime budget, spent once** | *n* per hour earned, or unbounded |
| Permanence | **permanent, non-revocable** | — |
| Analogue | a wishlist that funds a run; choosing a GP; crowdfunding; commissioning a task | likes, ratings, applause |

**A pledge is a 1:1-backed pre-authorization of creditable work — it need not involve an object or move any debit**. The old framing ("I will absorb this debit") was too narrow. Concrete case: a resident earns 4 credit-hours and **pledges 2 toward mowing the public verge on their block**. Someone with a mower sees the pledge, mows for an hour, submits evidence, and **is credited 1 hour** — 1 pledged hour remains for a later mow. *That is the entire transaction: no object changes hands, no property-debit moves, credits and pledges do not cancel.* The pledge simply **summoned an hour of creditable work** and drew an hour from the pledger's lifetime pledging-budget to do it — without spending or transferring the underlying credit, which stays on the pledger's ledger. **A pledge is permanent and non-revocable, and is not a promise to buy.** Where the pledged work *does* yield a held object, taking that object is a *separate* act: whoever accepts possession takes on its property-debit against their own debit-room (§3.2), whether or not they pledged. That is the ordinary possession rule, not what *defines* a pledge. What defines a pledge is the 1:1 credit backing (IC-8).

**Pledging is deliberately messy, and that is fine.** There will be unfulfilled pledges, frivolous pledges toward trivial or unverifiable tasks, and people learning to pledge well. Coordination groups and pledge-influencing politics will emerge around it. None of this is a defect: **pledges are the job-creating demand lever**, and a lever people organize around is a lever that works.

**Why pledges must be exactly 1:1.** A person's pledges are permanent debit-room they confer on receivers, and every hour of it is drawn from a **finite lifetime pledging-budget equal to their lifetime earned credit**; the 1:1 cap (IC-8) holds cumulative pledging to that backing. Let it exceed and you get **fractional-reserve pledging** — more permanent debit-room granted across the network than the grantors' credit can stand behind. This is a solvency constraint, not a preference. It also happens to be the only stationary value: pledging power created per period is *kL* and consumed at most *L*, so any *k* > 1 diverges until pledges filter nothing, and any *k* < 1 shrinks the directed economy to zero. **Because the budget is spent once and never refunded, pledging is itself a real sacrifice — which is what re-arms the influence guard: an influence-pumper can no longer pledge for free (tightening OP-1), and pledge-farming a task now requires real verified colluders each burning their own finite budget, visible on the public pledge ledger (§5.3).**

**Why signals should be plentiful.** Under 1:1 you can only signal for as much as you personally worked, so you signal your top priorities and the system learns nothing about your second tier. Cheap, abundant signals **reveal the full preference ordering rather than just the top slice.**

**What pledging is for:**

- **A decentralized demand signal.** Cost says what a thing takes; pledges say who wants it. Aequitas obtains this with no prices, no central optimizer, and **no Iteration Facilitation Board** — the standing body Parecon requires and [is attacked as implausible for](https://ejpe.org/journal/article/view/867).
- **A purpose for surplus.** A high producer whose ceiling far exceeds their appetite can *direct what gets made* instead of accumulating, which A3 (non-fungibility) forbids by design.
- **Funding education and speculative work** (§6.2, §6.6).
- **Collective prizes.** An X-Prize needs no oligarch or patron — a large enough pool of pledges is a crowdfunded bounty. Enterprise remains genuinely risky, as it always has been, and innovation has always flourished under that risk.

**Self-care pledging-power — a universal basic voice**. Self-care (§6.1b) is credit in full, so like all credit it generates **pledging-power** as well as consumption headroom (§7.5). Every living human therefore directs some share of what society works on next simply by being alive — a **universal basic voice** — and because the self-care floor is equal for all (§0), it compresses the influence distribution to the same bounded ratio as consumption (§7.5). **Its default routing is a trust-network policy choice** (A8): a network may **auto-pledge** a subscriber's self-care pledging-power toward the **basic-needs sectors** (food, water, shelter, care), leave it **unpledged** for the person to direct, or split it. Auto-pledging is the powerful case — the aggregate self-care pledging-power of a whole population, routed to essentials, **mechanically funds essential provision**, turning §7.5's "essential provision is unconditional" from an assertion into a funded demand signal sourced from the very act of staying alive. The trade-off is the network's to make: auto-pledge guarantees essentials but leaves the subscriber less discretionary voice; leaving it unpledged does the reverse. Self-care adds to a person's lifetime pledging-budget like any other credit; unpledged budget simply stays theirs to direct, and once a self-care pledge is made it is permanent like any other (§6.4).

**Approval never gates credit — but *verification* gates its realization**. The work is **always recorded**: an event is logged the moment work is done, so origin closure holds and unpledged wheat still has a grower (A7, IC-3). What a pledge buys is **authorization and demand-room** for the work — a permanent grant, but still not a guaranteed sale; whoever ultimately takes the resulting good uses their own debit-room to hold it (§3.2, §6.4a). But a recorded credit **realizes** — begins counting toward the worker's position — only when the output is **verified**, exactly as A7 already gates an estimated position on observation. This is *verification, not approval*: no committee judges the work worthy; the trigger is objective evidence the output exists. See §6.4a for how, for a physical good, that verification *is* the hand-off.

<!-- tag: fnd-s6-4a -->
### 6.4a Hand-off gates credit realization — the supply-chain model

For a physical good, the output is verified when it **changes hands**: the receiver, by accepting possession, attests the goods exist. So credit realization and the supply chain are the same events. Every hand-off along a chain is **three things at once**:

1. **Verification** — the receiver's acceptance attests the goods are real, which **realizes the *prior* holder's credit** for making (or moving) them.
2. **Debit transfer** — the property-debit (embodied material) follows possession to the receiver (§3.2).
3. **A new credit event** — the receiver's own labour (e.g. transport) is added to the item's debit-load and is itself realized when *they* hand it on.

*Worked case.* A co-op makes 1,000 toasters and hands them to an independent carrier. The carrier's acceptance verifies that 1,000 finished toasters left the co-op → **the co-op's making-credit realizes** and the toasters' property-debit moves to the carrier. The carrier delivers to a distributor; the transport hours are credited to the carrier and added to each toaster's debit-load; the distributor accepts the (now slightly heavier) debit. The co-op was credited the moment *any* carrier took the goods — it never waited on the distributor.

**Three properties, all load-bearing:**

- **It defuses the gatekeeper-capture problem.** Because a maker's credit realizes at the *first* hand-off to *any* receiver, no downstream buyer can hold it hostage. And because **debit follows possession**, a would-be monopsony gatekeeper's leverage *inverts*: holding goods means holding their debit (a worse ratio, §3.5), so it is motivated to pass them on, not to withhold. Power to gatekeep evaporates.
- **The count self-audits.** A receiver eats the debit of *exactly what they accept*, so they will never sign for phantom units — the maker cannot unilaterally inflate the hand-off count. This is the **same incentive logic as rival-sector audit (§3.3a)**: the party harmed by an error is the one who polices it, so verification needs no dedicated auditor.
- **Credit realization ≠ deployment.** Realization is at first hand-off; the **deployment timestamp** (§6.2b) is a *separate* clock that starts the end-holder's creation-cost holding-time. Do not conflate them.

**Who bears demand risk, and the two credit-without-a-pledge paths.** Since realization waits on hand-off, *unsold* goods are unrealized credit plus inventory debt on whoever holds them. Two cases:

- **Speculative production** (no pledge): the entrepreneur/producer **owns the goods and their debit-ledgers until sold**, and the risk that they never sell is borne by everyone who worked the run — but **symmetrically, by hours worked** (§6.2b holding-time / the same share as any supervisor), never dumped onto labour by rank, and floored by §7.5. The worker who joins an unpledged run takes the same bet the entrepreneur does, knowingly.
- **Pledged production** (a run backed by pledges): the pledges **soften the run's demand risk** — they signal committed demand and grant the producer permanent debit-room to carry the work. A pledge is **permanent and non-revocable** (§6.4), so the granted room can be relied on and does not evaporate mid-run; but it is still **not a promise to buy** — taking the finished good is always a separate possession act on the buyer's own debit-room, so a run can still go unsold. What the permanence removes is *withdrawal* risk, not *demand* risk. Most work is of this kind.

Because pledges are **public** (§5.3), pledged-vs-speculative is not a label a producer can privately misapply to recruit or to shed risk — a worker reads it off the pledge ledger, including whether pledges are holding or being withdrawn.

> **⚠️ Residual — the influence back-door.** Realized credit generates pledging-power (influence), which is measured in *gross hours worked*. A consumption-indifferent actor could in principle collude on hand-offs to fake gross hours and pump influence — bounded by IC-7 (24-hour cap) (24 h/day) and paid for in a wrecked ratio. Whether this bites is an **OP-1 (service → influence) (influence) question, not a credit-realization flaw** — see Objections §B10 / the OP-1 entry.

<!-- tag: fnd-s6-4b -->
### 6.4b Verification generalises by output type

The hand-off (§6.4a) is only the **goods** case of a more general rule: **a recorded credit realizes when its output is verified, and *how* an output is verified depends on what kind of output it is.** A good is verified by a hand-off; service and enrichment are not, and forcing them into the hand-off mould would leave most service and nearly all enrichment unrealizable.

| Output | How realization is verified |
|---|---|
| **Goods** (matter / energy) | **Hand-off** — the receiver accepts possession and its debit (§6.4a). |
| **Service** (often no physical output) | **Client attestation** — the recipient confirms the service occurred (the same fact §6.3 reads as "someone chose you as their doctor"). |
| **Enrichment** (intangible, abstract) | **Occurrence-attestation** — evidence the work *happened*. |
| **Self-care** (universal maintenance) | **Proof-of-life** — a verified living human (C6) demonstrably maintained itself; statistical (A7), near-zero burden. |

Two rules keep this from becoming a fraud channel:

- **Verification asks "did the work occur?" — never "did anyone value it?"** For enrichment especially, the temptation is to realize credit on *feedback* (likes, citations, applause). **That is forbidden:** feedback is non-credit by construction (§6.3), and letting it realize credit makes feedback a currency by the back door — exactly **OP-8**. Verification and feedback stay separate.
- **The weak cases are priced near zero until corroborated** (§6.6). Unwitnessed "I thought for ten hours" is *recorded* faithfully (A7) but carries the weakest basis and lowest confidence, so conservative weighting values it at ≈0 until something corroborates it. Fabrication is cheap to assert and cheap to hold — an incentive, not an enforcement rule.

**Trust networks design, administer, and audit the specific verification method for each activity** — A8 local variance, the same capture surface as the always-creditable-activity list (§10.1), and disciplined the same way: **a counterparty re-computes a claim's realization and backing through its *own* weighting model** (A6, EventLog §3), so a network with lax verification cannot *export* the credit it issues — whoever trades with its members discounts it. This is **comparison, never conversion**: nothing is exchanged between models; each party re-reads the shared physical log through its own weighting. Converting a balance from one model into another would be an exchange rate between credit-standards — a medium of exchange, which A3 and the circulation-failure analysis (§7.6) forbid.

> **⚠️ This anti-arbitrage guard depends on OP-22 (audit disclosure).** Re-computing a pledge's backing requires seeing *what backs it*, but personal ledgers are private (§5.3). The guard therefore needs "this pledge is backed by *X* hours realized under weighting model *M*" to be provable in zero-knowledge. The market check on lax or over-generous networks is only as real as that disclosure mechanism — **which is OP-22.**

<!-- tag: fnd-s6-4c -->
### 6.4c The contingent reserve — how over-pledging incentivises hazardous work

Because pledges are permanent, a task can attract **more pledged hours than it costs**. The surplus is **not** a payment to the doer and is **not** consumable — treating it as spendable would be a scarcity price (profit), which A5 forbids, and would re-open a channel for concentrating consumption advantage. Instead the surplus becomes a **contingent reserve**: earmarked, non-spendable debit-room that activates **only against a verified future cost causally traceable to the task** — the doer's later injury or illness, site remediation that resurfaces, third-party harm. This is *any* task-caused cost, not only the doer's.

- **Pledge shares split pro-rata by hours *on the task*** (a doer's share of a pledge = their task-hours ÷ total task-hours), so the cover reaches whoever actually did *this* work — not, via a whole-co-op-history denominator, whoever has been a member longest (which would be the P4 seniority-skim).
- **Causation is decided by the physical-trace test** (§3.4a / OP-17): a claim draws the reserve only if the harm left a trace linking it to the task; diffuse or latent harm with no individual trace is handled by a **cohort/actuarial convention** (the §5.1b residual rule), never an open claim.
- **The reserve is a buffer, not a shield: overflow reverts to the causer.** Once a reserve is exhausted, residual task-caused debit falls back on the doer/cooperative under the ordinary rules (§3.2 possession, §3.7 remediation). Without this, third-party/environmental cover would licence carelessness; with it, the care incentive survives.
- **An abandoned task's pledges are burned** — the pledger's finite budget is spent for nothing, which is what disciplines frivolous pledging. Unused reserve on a completed task likewise never becomes consumable and never reverts; it lapses. **This resolves C5's reversion question in the negative: nothing reverts.**

**What it buys.** Onerousness has two halves. This mechanism gives the *hazardous* half a demand-gated incentive **without** wage premium, rate-scaling, or a rating authority: society de-risks the toxic-cleanup worker exactly to the extent it pledges for the work, and the danger internalises as the size of the reserve the task must attract. It leaves the *tedium/indignity* half open (dull but safe work generates no causal tail, so no reserve, no incentive) — that remainder stays with OP-16. Because the reserve only ever *cancels* a task-caused cost and never *adds* spendable room, it creates no consumption advantage. Sim: `06-simulation/pledge_reserve.py` (clears the job at coverage ≈ cover-the-tail; overflow-reverts preserves care; integrity rests on physical-trace causation).

<!-- tag: fnd-s6-5 -->
### 6.5 Attribution without intellectual property

There are no patents and no exclusion. Ideas replicate freely; **meme tracing** gives feedback-weighted recognition to originators as ideas spread.

**Art is not a commodity, and intellectual property is the antithesis of treating it as anything else.** Exclusion rights exist to let a holder extract profit from reproduction. With no profit in exchange (A5 (price ≡ cost)), the machinery has nothing to protect and no reason to exist.

**The right standard for attribution is *no worse than today*, not *perfect*.** Buy a painting from a gallery now and there is no video of its making; you trust the seller, and at person-to-person scale the stakes are low enough that this is fine. Provenance only becomes fraught in the capitalized art market, where licensing and reproduction are the revenue — which is precisely the layer Aequitas removes. **Aequitas does not need to solve a problem that the current world also has not solved and does not much suffer from.**

*A useful illustration, though not a general mechanism:* someone can copy an MP3 and claim it, but is unlikely to perform it live. When the incentive is to share the work rather than to sell copies, a recording functions as an advertisement for the performance. This holds well for music and poorly for writing, visual art, software, and research — so treat it as a good example rather than a rule.

<!-- tag: fnd-s6-5a -->
### 6.5a Not all work is capturable — and the system does not require it to be

A2 and A4 describe how flows are accounted **when they are recorded**. Neither claims that all human activity must be recorded, and the difference matters, because a critic will read A1 (materialism of cost) as demanding total surveillance.

Memes are the clean case. People spend real time editing images and writing captions; the results propagate through conversation, entertainment, and provocation. **Tracing who shared what to whom in order to assign work-credit is neither possible nor desirable**, and a trust network that proposed it would be laughed out of the room — which is A8's local variance working exactly as intended.

> **Much of what people do, they do to entertain themselves and each other. The system does not need to capture it, price it, or credit it, and attempting to would be both futile and grotesque.**

The accounting covers what is claimed and attested. Everything else is life.

<!-- tag: fnd-s6-6 -->
### 6.6 Unobservable work — and the lone fraudster

Creative and intellectual work is mostly thinking, which leaves no material trace and has no witness. Crediting only observable performance excludes most of it; trusting self-report without limit appears to invite unlimited fraud.

**The apparent hole is closed by three mechanisms that already exist, and none of them is new:**

1. **IC-7 caps the volume.** No account may claim more than 24 hours of activity per 24 hours. The press only runs so fast.
2. **Conservative weighting of low-confidence flows** (C1 (event-log schema) §12) does the real work. Self-asserted, unwitnessed, near-zero-material work carries the weakest `basis` and lowest `confidence` in the log. Weighed at the **pessimistic end of its interval — which for a credit claim is close to zero** — the fabricated hours are recorded faithfully and are worth almost nothing until something corroborates them. **This is the general answer to unobservable work, and it is an incentive rather than an enforcement rule: vagueness is cheap to assert and cheap to hold.**
3. **Pledges bound what anyone will underwrite.** Someone pretending to be an artist, or generating unwanted volume at scale, attracts no pledges — and a pledge is the only thing that moves a claim from *asserted and near-worthless* to *backed*.

**On mass-produced slop specifically:** generation cost trending to zero means volume trending to infinity, so the defence cannot be per-item cost. It is that **nothing accrues without someone choosing to back it**, and a curation venue with no ad inventory to sell has no reason to reward volume. Note where the residual risk actually sits: not in credit issuance, but in **flooding the free signal channel** (§6.4). That belongs to **OP-6 (feedback mechanics)**, not here.

**Note what this does and does not claim.** Aequitas removes most of the *acquisitive* motive for fraud — there is no wealth to concentrate. It does not remove status-seeking, which is exactly what a false claim of creative hours would be. The defence against that is evidentiary, per points 1–3, not motivational.

---

<!-- tag: fnd-s7 -->
## 7. Consequences

<!-- tag: fnd-s7-1 -->
### 7.1 Capitalism cannot function
Price ≡ cost means no profit in exchange. Embodied-material debit releases on transfer; self-work nets to zero while held (§3.2). **No rent, no rental income, no property speculation, no compounding capital.** Not banned — structurally impossible. *Ellerman's route reaches the same conclusion independently: only people act, so only people can be responsible, so capital cannot claim a residual.*

**The exploitative employer is structurally hollowed out**. The wage-extraction employer has no mechanism to exist: credit is non-transferable, so there are **no wages** to pay (A3 (non-fungibility)); price ≡ cost, so there is **no surplus to appropriate** (A5 (price ≡ cost)); and a team's debit is shared **by hours worked, not by rank** (§6.2b), so a supervisor **cannot dump risk or cost onto subordinates**. Workers are credited by the *system* for their hours, not paid by a boss. **What survives is coordination** — organizing a process, directing what gets made, controlling access to desirable projects — and that residual power is real: it is the **coordinator-class problem (P4 (coordinator class))**, the live blocker, not the extractive employer this system already forecloses.

**What survives, and is load-bearing: competition on efficiency.** A5 removes margin, not rivalry. §3.3a leans on this directly — rival sectors auditing each other's cost constants is the only thing standing between the weighting model and systemic under-costing.

<!-- tag: fnd-s7-2 -->
### 7.2 Exploitation and pollution self-penalize
Harmful production carries the remediation cost of the harm. But — per §3.2b — that cost is permanent **on the producer who caused it**, not on the product that leaves the gate. So the penalty is **direct**: a polluter carries permanent pollution-debt, a poor efficiency ratio (§3.5), and restricted discretionary consumption (§7.5), whether or not any consumer ever notices.

**This is *stronger* than the consumer-mediated gradient it replaces.** The old framing ("dirty products cost the buyer more") leaned on consumers choosing the cleaner good — historically a weak force, because the cheap dirty product usually wins. Pinning the debit to the producer removes that dependency: exploitation and pollution self-penalize at the source. And the consumer signal is **not lost** — the good still carries a non-transferable provenance record (§5.1b, §3.2b), so buyers and pledgers can prefer low-pollution producers on top of the direct penalty. The incentive gradient reverses without regulation, on both channels.

<!-- tag: fnd-s7-3 -->
### 7.3 Regulators invert into services
An EPA-like body becomes something businesses **actively want**, because it helps them lower their debit-cost. Enforcement becomes consulting.

<!-- tag: fnd-s7-4 -->
### 7.4 Taxation is unnecessary
Civil servants are credited directly. Infrastructure users carry proportional debit by usage. There is nothing to collect.

<!-- tag: fnd-s7-5 -->
### 7.5 The basic-needs floor
- **The floor is credited maintenance time** — every living human performs the work of staying alive (§6.1b), which credits by proof-of-life (§6.4a) and provides real credit backing for basic consumption. **It is not a grant.** And it covers exactly the people the floor exists to protect — the newborn, the old, the sick, the disabled — because *being alive*, not *being able to work*, is the qualification. Its magnitude, and any residual **age-based debit tolerance** for maintenance a body cannot itself perform, is the **OP-4 (debit tolerance)** question, set per network (§6.1b).
- **Essential provision is unconditional** — a counselor is credited for providing service regardless of the recipient's standing; and the aggregate self-care pledging-power of the population *funds* that provision where a network auto-routes it (§6.4).
- **Enforcement is graduated, not punitive:** exceeding tolerance restricts **non-essentials only**.
- **The efficiency ratio governs the discretionary layer only** (§3.5). It may never reach essentials, or it would fall hardest on the newborn, the old, the sick, and the disabled — exactly the people this section exists to protect.

> **The floor is the denominator of the inequality ceiling — a *conditional* result, not an arithmetic certainty**. Because credit accrues in equally-distributed, non-transferable time (§0), the ratio between the highest and lowest credit-accrual rate is bounded by **`24 h ÷ the network's self-care floor`** — ≈2.4× for a 10 h floor, 3× for 8 h, and so on — against the *unbounded* (Pareto) top tail money produces. **The bound is *per network*, and it holds only when five conditions hold. Presenting it as pure arithmetic — or as a global figure — overstates it:**
>
> 1. **The floor stays in a narrow band.** The ceiling *is* `24 ÷ floor`, so a network with a 2 h floor admits a 12× ceiling. The result is only as tight as floors are uniform and generous — a small constant, not a fixed one (the floor is a network weighting choice, §6.1b).
> 2. **Floor-shopping is arrested by counterparty re-computation** (§6.4b, OP-14 (cohort shopping)). If an agent could migrate to a low-floor network to inflate their relative accrual, the bound would leak; it holds because each counterparty re-weights a claim through its *own* model — **comparison, never conversion.**
> 3. **That re-computation depends on OP-22 (audit disclosure).** Proving "backed by X hours under model M" without exposing the private ledger is unsolved. Until it is, the anti-arbitrage guard is not implementable — so the ceiling is **conditional on OP-22**, which is the sharpest way to state the dependency.
> 4. **No fraud manufactures gross hours** (OP-1 (service → influence)). *Within a single network*, IC-7 (24-hour cap) caps a day at 24 h, but collusive fake hand-offs could still inflate gross accrual; the bound assumes that channel is controlled.
> 5. **Cross-network uniqueness is attested.** A person may legitimately hold an account on more than one network (§5.3a). **IC-7 does not cover this, because it caps per account per network.** Goods are anchored physically — a parcel has one custody chain (IC-5), so output-backed credit cannot be duplicated across networks without surfacing. **Self-care credit has no such anchor**: it is credited by proof-of-life and needs no output, so a person on *k* networks can accrue the floor *k* times and reach `k × 24/F`. The defence is **federation** — on merge, two networks holding the same records for the same person collapse them into one account, and a network that accepts inflated credit damages its own books, so cross-checking uniqueness with peers is in its own interest (OP-14 applied to persons rather than goods).
>
> So the honest statement is: **if OP-22 is solved, floors stay in-band, and cross-network uniqueness is attested, then the accrual ceiling is `24 h ÷ floor` — per network, within-model.** It remains the **disparity ceiling** — the strongest defensive result the theory reaches — a *conditional* result whose debit-tolerance dynamics are OP-4 (debit tolerance).

> **Why hoarding cannot beat it — the ratio-gate precision.** Credit `C` and debit are **cumulative running tallies** derived from the event log (A6), and **credit is never *spent*** — a purchase adds to debit, it never decrements credit (A3: credit is not a currency). The gate `D ≤ ρ·C` is therefore a **ratio re-checked at each event**, not a balance drawn down. A lifelong "hoarder" who consumes nothing and then splurges can only **front-load their own allowance** (bounded by `ρ·C`) — there is no banked lump to blow. At **equal age** two people's cumulative credits stand in ratio ≤ `24/F`, so cumulative-consumption disparity is bounded by `24/F` too; the **only** spread beyond it is age (time lived, not class). This resolves the Methuselah objection *without* any separate "rate gate" — it is just A3 + A6.

> **Formally stated, simulated, and stress-tested → PASSES.** The formal statement + a plain-language explainer are in `06-simulation/DISPARITY_CEILING.md`; the adversarial pass (2026-08-14) dissolved all three attacks — **Methuselah** (above), **dynasty/household** (a household is a co-op; its dwelling-debit holding-time-splits per occupant by dwelling-time, children included — the bound is **per-person**, and inheritance *dilutes* it, §6.2b), and **collector** (holdings are a burden that raise your own debit, so a hoard self-bounds). The agent-based model — `06-simulation/disparity_ceiling_sim.py` (N = 200,000, gate `D_i ≤ ρ·C_i`, credit ∈ `[F,24]` h/day), **7 self-tests green** — shows, all within-model:
>
> - **The `24/F` ceiling is exact and ρ-independent** — flat at 2.4× (for F = 10 h) across every ρ ∈ [1, 3], because ρ cancels in `ρ·24 / ρ·F`. It is also **weighting-independent** (total consumption ≤ ρ·C whatever the collapse weights), so **the headline result does not depend on OP-10**. On the same synthetic population, money's disparity is 14× (income) to ~700–950× (wealth), against a real top tail of 10⁴–10⁶×.
> - **ρ behaves like a prime rate.** A ρ can be chosen so aggregate demand matches productive capacity, and it moves sensibly under shocks. Calibrated to the median-lifestyle anchor (`06-simulation/rho_sweep.py`, `RHO_SWEEP.md`), the baseline clears at **ρ\* ≈ 1.2** (the median person gets ~92% of their desired lifestyle); a −30% capacity disaster *tightens* it to ~0.68, growth *loosens* it to ~2.2, a +25% pollution re-weighting tightens it to ~1.0, and population decline barely moves it. This is the operational meaning of "Aequitas *uses* ρ but does not *set* it" (§3.5/A8). *(Absolute ρ\* is OP-10-dependent and illustrative; the **directions** are robust.)*
> - **Efficiency, not extra labour, crosses society toward post-scarcity.** In the same calibrated model, the *same* population is mildly scarcity-constrained under the wasteful US production method (ρ\* ≈ 1.2, ~35% of people held below their wants) but tips into **post-scarcity — the debit gate stops binding at all, everyone reaches their full desired lifestyle — under German/Japanese or Spanish efficiency** (Q6). Because the binding constraint is physical throughput (§3.5), lowering the debit-intensity of production (less energy, shorter chains, less adversarial overhead) does far more than adding labour ever could. This closes the loop between §3.5 (labour abundant), Q6 (the efficiency spread), and the ρ dial: **abundance is reached by producing efficiently, not by working more** — and the `24/F` ceiling holds throughout the transition.
> - **The ceiling is fraud-invariant.** Because IC-7 (24-hour cap) bounds *every* account, honest or fraudulent, the most a fraudster reaches is `ρ·24` — the honest maximum. Fraud fills the band; it cannot create an outlier beyond it. Security becomes "how much does undetected cheating get you?" — answer: never past the ceiling.
> - **The ceiling survives hoarding (Claim 4 / Methuselah).** On the cumulative ledger with the ratio gate, a hoarder who attempts a splurge of 10× their allowance is **clipped to `ρ·C`** and lands at exactly the steady consumer's total; equal-age disparity stays `2.4×`. The only spread beyond it is age (a 60-year max-worker vs a 20-year subsistence person = `7.2× = 3×·24/F`).
>
> **Still conditional on OP-22** — the sim *assumes* the anti-arbitrage guard is implementable (it does not model the disclosure mechanism), and the structural results (2.4×, ρ-independence, fraud-invariance) hold for any distribution while the *clearing-ρ\** values are illustrative. What remains for full closure is the like-for-like against real wealth micro-data (Objections §C test 8). This anchors on the median-lifestyle work (`06-simulation/MEDIAN_LIFESTYLE_RESULT.md`).

> **The real-distribution comparison, now run**. `06-simulation/q4_locked_ledgers.py` applies the ceiling to real US/world distributions under the **material-only** rule (A1 corollary above), asking what fraction would sit past a *permanent* efficiency-ratio lockout — discretionary consumption pinned to the floor for life because their sustained footprint exceeds `ρ · 24 h/day`, the most any human can ever earn. Two results sharpen §7.5:
> - **The A1 tail-compression.** Stripping the financial layer collapses the top of the distribution by **~1,000×**: money wealth reaches ~10⁶× the median (SCF/Forbes), but material *consumption* only ~670× (Oxfam billionaire personal footprints), because you cannot physically consume without spending bounded time. The disparity the ceiling has to cap is far smaller than the monetary one — the material world was never as unequal as the paper one.
> - **Only a thin slice is locked.** Material-only, ~**0.1–2%** of Americans are permanently locked (ρ-dependent; ~0.5% at ρ = 1.5) — the ultra-consumers, *not* the merely rich — and even fully divesting material property does not save them (permanent consumption debit, §3.2). Meanwhile ~two-thirds sit *below* cohort average and would gain discretionary room by joining (§5.2). This is the honest, quantified form of "the gap money produces is uncapped; the one Aequitas produces is not."

> **This section also bounds the cost of being wrong**. Debit binds hard, and §3.3 corrects errors only eventually — so a producer over-assigned for years would suffer real harm before the correction arrived, the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal). The floor caps that exposure: the worst case is *restricted discretionary consumption for a period, then corrected*, not destitution. **The floor is not only a welfare provision; it is the error-tolerance of the whole accounting.**

<!-- tag: fnd-s7-6 -->
### 7.6 Why the alternative-economy graveyard does not apply

A century of local currencies and time banks failed in three distinct ways. Aequitas is immune to one of them by construction, and should say so.

| Failure | What happened | Aequitas |
|---|---|---|
| **Circulation** | Ithaca HOURS businesses were *"drowning in Hours"*; Burlington Bread piled up at cafés with no way to recirculate. Scrip flows to whoever buys inputs outside the network and stops. | 🟢 **Cannot occur. There is no medium of exchange.** Credit never moves (A3); only debit moves, attached to its object. Nobody can drown in credit they cannot spend because nobody ever receives credit *from* anyone. |
| **Valuation** | Warren (1830) could not reconcile labour-for-labour with skill and disagreeableness. Time banking, 45 years on, still reports chronic skill shortage from flat-hour crediting. | ⚠️ **Partly answered.** A2 (time as measure) v0.3 makes training paid work, which addresses skill. **Onerousness remains open — OP-16 (onerousness gap).** |
| **Institutional** | Wörgl's scrip was suppressed by Austria's central bank *for working*, under the legal-tender monopoly. Ithaca died when its founder moved. | 🟢 **No issuer, no notes, nothing to counterfeit** — the legal instrument that killed Wörgl does not fit an accounting system. This is the substantive reason Aequitas must never be described as a currency. ⚠️ Founder dependency is answered only by §2's fourth screening question. |

A3 therefore does three separate defensive jobs: it forbids accumulation (§7.1), it makes permanent aggregate net-debit survivable (§3.5), and it makes the circulation failure impossible.

---

<!-- tag: fnd-s8 -->
## 8. Deliberate Divergences from OFCS

| OFCS | Aequitas |
|---|---|
| "Credit syndicates" | **Businesses / institutions.** "Syndicate" is alienating jargon. |
| Restructures society broadly | **Surgical.** Keep the functional parts — municipal government, planning bodies, civil service — and change only their *economic nature*. Target oligarchic capture, not institutions that work. |
| Loose "set of requirements" | Rigorous axioms with a single mechanism (§1). |
| Self-regulation by participants | Governance as **protocol property** (A8 (local governance)). |
| — | **Pledges and signals** as the demand side (§6.4). |
| — | **Meme tracing** for idea attribution. |
| — | **Retroactive re-weighting** of all history as science improves. |
| — | **Statistical coverage of non-participants**, symmetric. |

---

<!-- tag: fnd-s9 -->
## 9. Document Roadmap

1. **Foundations & Protocol** *(this document → next: full spec)* — audience **implementers**. **Build first.**
2. **Academic paper** — engages Marx / Hayek / Ostrom; must answer the socialist-calculation critique head-on. Lead with: theory of *cost* not value; Ellerman on attribution; Cockshott & Cottrell on tractability; pledges as a decentralized answer to preference revelation. **Add: joint production solved by process physics rather than by convention (§3.4a) — this is the reply to Sraffa/Steedman and to ISO 14044 simultaneously.**
3. **Civic reformer brief** — municipalities, co-ops, transition communities.
4. **Public-facing text.**

---

<!-- tag: fnd-s10 -->
## 10. Open Problems

Ranked by how load-bearing they are. Full detail in `00-strategy/Aequitas_Objections_v0.17.md`.

**Blocking**
- ~~**OP-18 (labour & team credit) — Responsibility is not divisible.**~~ **✅ Closed 2026-08-05 as the C3 (estimation engine) blocker.** Team-credit dissolves under A2 (time as measure) (own hours); labour-across-co-products rides the material split by declared convention (§1.1, §3.4a); co-product cost is embodied input, not scarcity. **C3 is unblocked.** Narrow residue (jointly-caused debit across a team) is minor and parked. Note: `00-strategy/OP-18_labour_and_team_credit.md`.
- **OP-10 (weighting governance) — Weighting-model governance.** Whoever sets the cost model controls every balance in history without touching a core rule. Largest hole in A8 (local governance). §3.2a closes one side entrance (split before collapse) and §3.3a supplies a mechanism for cost constants; the general problem stands. **Now the top blocking problem.** *v0.8 identifies its highest-leverage single instance:* the **self-care floor** (§6.1b) is a weighting constant that is both **universal** (every human) and **influence-bearing** (§6.4), so it moves every account's consumption *and* voice at once — the fattest OP-10 target in the system. The v0.8 anti-arbitrage guard (counterparty re-computation, §6.4b) is the general shape of the answer, and it depends on OP-22 (audit disclosure).

**High**
- **OP-24 (understatement drift) — Understatement drift.** Errors that overstate debit get corrected; errors that understate it have no funder. Proposed fix — rival-sector audit (§3.3a) — is unproven and wants a simulation. **Attacks A4 (no externalities).**
- **OP-16 (onerousness gap) — The onerousness gap.** A2 resolves exertion, hazard, and skill. **Tedium and indignity have no material signature and nothing allocates labour to them.** Leading candidate: *hour-ceiling differentiation* — pay the premium in hours, not rate, justified by measured physiological sustainability limits. First check how much of OP-16 is simply unmeasured hazard.
- **OP-1 (service → influence) — Service → influence.** Strongest candidate: **pledging power accrues per hour worked, equally for all.** Not a voting scheme. *v0.7 adds a sub-question:* since realized credit → pledging-power is measured in *gross hours*, collusive hand-offs (§6.4a) could in principle fake gross hours to pump influence — bounded by IC-7 (24-hour cap) and paid in ratio, possibly self-starving via the debit-room cost of pledging. **The influence residual of the credit-realization model lands here.** *v0.8 adds the other half:* self-care credit generates a **universal basic voice** (§6.4), which bounds the *influence* disparity to the same **`24 h ÷ floor`** ceiling as consumption — a strong result, and **per network for the same reason §7.5 condition 5 gives**: self-care credit has no physical anchor, so a person on *k* networks accrues the floor *k* times on the influence axis too — but its routing is a network lever (§6.4) and its backing is only checkable via OP-22. Universal basic influence is largely a *feature* (equal baseline voice, anti-oligarchy); the open part is the collusion residual above.
- **OP-6 (feedback mechanics) — Feedback mechanics.** How signals aggregate without becoming a popularity plutocracy. With accumulation forbidden, feedback and pledging are the entire motivation system for anyone past their own consumption ceiling.

**Medium**
- **OP-3 (estimation convergence) — The estimation engine.** Requires a cohort *production* model as well as consumption, on the residual rule (§5.1b).
- **OP-8 (feedback firewall) — Can feedback be bought?** *(reframed)* *v0.8 sharpens the guard: §6.4b forbids realizing credit on feedback — enrichment verifies by occurrence-attestation ("did the work happen?"), never by likes/citations, or realization becomes purchasable and feedback becomes a currency.*
- **OP-9 (calculation reply) — Preference revelation.** Largely answered by §6.4 pledges, plus scarcity-as-debit on the Kantorovich framing.
- **OP-22 — Minimum audit disclosure.** A C7 (privacy layer) disclosure-set question — see §5.3. **The "market-public / persons-private" transparency principle (§5.3) *depends* on this being solved:** public flows must not chain-analyse into de-anonymised persons. Right shape (zero-knowledge); disclosure set unspecified. *v0.8: it now also gates the **anti-arbitrage guard** of §6.4b* — a network's lax or over-generous weighting can only be discounted by a counterparty if "backed by *X* hours under model *M*" is provable without revealing the private ledger. The market check on weighting pluralism is only as real as OP-22.
- **OP-4 (debit tolerance) — Debit tolerance formula.** ⬆⬆ *More load-bearing after v0.8: it is now the **denominator of the disparity ceiling** (§7.5) and sets the **self-care floor magnitude** (§6.1b). Finding: there is **no single global debit:credit ratio** — §3.5 forbids one (aggregate is always >1 and rising; a pure-ratio metric is infinite for a newborn) and A8 forbids an expert-set one (capture surface). Axiom-clean shape: a **per-person, network-set tolerance floor + personal efficiency ratio on the discretionary layer only.** Prerequisite of the disparity-ceiling proof.*
- **OP-14 (cohort shopping) — Cohort shopping.** *v0.8: now also **self-care-floor and routing shopping** — subscribers gravitate to networks with a generous self-care floor or favourable pledging-routing (§6.1b); arrested (if at all) by counterparty re-computation (§6.4b), the OP-24 test.* · **OP-15 (ghost harvesting) — Ghost harvesting.**
- **OP-7 (cross-level trade) — Cross-level trade.**
- **OP-25 (illicit dumping) — Illicit end-of-life dumping.** §3.6 prices *lawful* disposal correctly; abandoning an object in the environment to escape its end-of-life debit is a Level-2 trust-and-provenance attribution problem.

**Closed**
- ✅ ~~**OP-23 (shared overhead) — Shared-overhead attribution.**~~ **Closed in v0.5** (§6.2b): capital and overhead accrue to the asset and its holders and **never allocate to co-products**, so there is nothing to attribute. The interim inherited-proportions convention was deleted, not refined. `00-strategy/OP-23_capital_and_pollution.md`.
- ✅ ~~**OP-17 (joint production) — Joint production allocation.**~~ **Closed in v0.4 for the material/energy half** (§3.4a): the process performed the split and it is measurable. The labour half moved to OP-18; the overhead half moved to OP-23, **now also closed.** **A row was deleted from §1.1 rather than filled in.**
- ~~**OP-20 (unobservable work) — Unobservable work.**~~ Closed by three existing mechanisms (§6.6).
- ~~**OP-21 (media reproduction) — Media reproduction.**~~ Closed by front-loading (§6.2a).
- ~~**OP-19 (saturated producer) — Saturated producer.**~~ Resolved by pledges.

**Deprioritized**
- **OP-2 — Anti-collusion at Level 2.** Level 2 is an emergent market of trust networks; revisit once the system is defined.

**Dissolved**
- ~~**OP-11 (training amortization) — Training-cost amortization.**~~ · ~~**OP-5 (education cost) — Education.**~~ · ~~**OP-8 — Enrichment firewall**~~ *(reframed, see above)*.

<!-- tag: fnd-s10-1 -->
### 10.1 Deliberately left to trust networks

Which activities are *always* creditable — childcare, schooling (and whose schooling), subsistence farming, untrained medical assistance — is **not** settled by this document, and should not be. It is exactly the kind of question A8 assigns to local variance competing in the open.

**But name the risk:** the set of always-credited activities is a capture surface. A network that can declare an activity creditable can issue credit. The defence is structural rather than procedural — competing networks, plus ratio-based evaluation (§3.5): a network that credits worthless activity produces members with poor efficiency ratios, and other networks stop trading with it. **This is OP-10 wearing different clothes and should be worked with it.**

**Added in v0.4 — a second structural defence, from §3.3a.** A trust network's membership composition is public, and **a network concentrated in the sector it audits is captured by construction.** That makes capture *detectable from the log* rather than something anyone must police. It is a screening property, and it applies to always-creditable activity lists as much as to cost constants.

---

<!-- tag: fnd-s11 -->
## 11. First Foothold — the MVP

**Full-cost accounting as a parallel overlay on existing commerce.** No adoption, no permission, no legal change — it computes and publishes truth alongside money.

> **⚠️ Read that sentence cold and it describes every complementary currency that ever died.** Ithaca HOURS was *defined* as $10; Burlington Bread mirrored dollars in slices. None was an independent unit of account — they were national currency with a local-loyalty restriction, they added nothing money did not already do, and they died quietly.
>
> **The distinction is the whole point of the MVP: Aequitas's overlay computes a number money cannot produce.** A true debit-cost is not a price with a different label; it is information that does not exist anywhere in the current system. If the MVP ever stops being able to say that, it has become a loyalty scheme.

**(a) Product & service debit-costing.** Compute and publish the true debit-cost of real products. *Materials and energy are unblocked (§3.4a); the labour layer is gated on OP-18 (labour & team credit).* **A first publishable target: re-derive a refinery's fraction slate under process-physics allocation and compare it against USEEIO's price allocation.** A materially different answer is the strongest technical result available early.

**(b) Account intake with progressive resolution.** A person opens an account and answers questions; their estimated position resolves from **global average → granular cohort → individual record**.

> A **"try it" account** — answer questions about yourself and watch your assigned position sharpen from the global average toward something specific to your location, age, work, and holdings. It demonstrates the estimation engine, the onboarding incentive, and the honesty of the accounting at once.

**If a first *real* deployment is ever wanted rather than an overlay**, the field record is unambiguous about the shape: WIR (1934–present, ~60,000 businesses) and Sardex (4,000+ businesses) survived by starting **B2B inside dense input loops**, where no participant is a one-way sink. Both are countercyclical — adoption rises when conventional money is scarce. **A downturn is the moment.**

---

<!-- tag: fnd-s12 -->
## 12. Amendment record

The full version-by-version change history now lives in a separate file, read only when needed: **[`Aequitas_Foundations_CHANGELOG.md`](Aequitas_Foundations_CHANGELOG.md)**.

---

*End of v0.13.*
