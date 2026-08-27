<!-- tag: fnd-aequitas-foundations-and-long-term -->
# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.25
> **Date:** 2026-08-25
> **Status:** Working foundations. **Truncated at §8 by author ruling** — the OFCS comparison is gone, and the conformance list, the open problems and the adoption reading now live in their own documents (§8 below). **§5 and §7.5 were rewritten in substance earlier the same day**; §5.2–§5.5 are the owed remainder, and the companions (Overview, GLOSSARY) are bumped once it lands.
> **Primary audience of the first paper:** technologists / implementers.
> **Companion:** `00-strategy/Aequitas_Objections_v0.23.md` — the objections register. Read alongside §10.
> **Companion:** `00-strategy/Aequitas_EventLog_v0.9.md` — the C1 data model, which carries the §5.1b scope-alignment check as §7.2a.
> **Version history & what each version superseded:** `00-strategy/Aequitas_Foundations_CHANGELOG.md`.

---

<!-- tag: fnd-toc -->
## Contents

- [0. The One-Sentence Theory](#0-the-one-sentence-theory)
- [1. Axioms](#1-axioms)
  - [A1 (materialism of cost)](#a1-materialism-of-cost)
  - [A2 (time as measure)](#a2-time-as-measure)
  - [A3 (non-fungibility)](#a3-non-fungibility)
  - [A4 (no externalities)](#a4-no-externalities)
  - [A5 (cost, not price)](#a5-cost-not-price)
  - [A6 (derived, not stored)](#a6-derived-not-stored)
  - [A7 (universal accounting)](#a7-universal-accounting)
  - [A8 (no governing body)](#a8-no-governing-body)
  - [1.1 Named conventions](#11-named-conventions)
  - [1.2 What Aequitas is, and what is therefore out of scope](#12-what-aequitas-is-and-what-is-therefore-out-of-scope)
- [2. Conformance to the Three Criteria](#2-conformance-to-the-three-criteria)
- [3. The Ledger Model](#3-the-ledger-model)
  - [3.1 Structure — an event log, not a balance](#31-structure--an-event-log-not-a-balance)
  - [3.2 The two kinds of debit — and the two components of property debit](#32-the-two-kinds-of-debit--and-the-two-components-of-property-debit)
  - [3.2a Debit is a vector, collapsed on demand](#32a-debit-is-a-vector-collapsed-on-demand)
  - [3.2b Only property transfers — pollution and transport never do](#32b-only-property-transfers--pollution-and-transport-never-do)
  - [3.2c An organisation's debit is its members' debit](#32c-an-organisations-debit-is-its-members-debit)
  - [3.3 Retroactive re-weighting](#33-retroactive-re-weighting)
  - [3.3a Who checks the science — the problem, and whose problem it is](#33a-who-checks-the-science--the-problem-and-whose-problem-it-is)
  - [3.4 Resolution is opportunistic](#34-resolution-is-opportunistic)
  - [3.4a Joint production — dividing one process's debit among several outputs](#34a-joint-production--dividing-one-processs-debit-among-several-outputs)
  - [3.5 The books never balance — and must not](#35-the-books-never-balance--and-must-not)
  - [3.6 End-of-life, recycling, and product-as-pollution](#36-end-of-life-recycling-and-product-as-pollution)
  - [3.7 Land is not owned; a building carries a remediation debt](#37-land-is-not-owned-a-building-carries-a-remediation-debt)
- [4. Verification — the Four-Level Ladder](#4-verification--the-four-level-ladder)
  - [Each rung has a price, and the ladder must show it](#each-rung-has-a-price-and-the-ladder-must-show-it)
  - [A second record only helps if it can disagree](#a-second-record-only-helps-if-it-can-disagree)
- [5. Identity, Privacy, and Onboarding](#5-identity-privacy-and-onboarding)
  - [5.0 What this section is about, and who does the things in it](#50-what-this-section-is-about-and-who-does-the-things-in-it)
  - [5.1 One account per person, and coverage that does not require consent](#51-one-account-per-person-and-coverage-that-does-not-require-consent)
  - [5.1a How an estimate becomes a record](#51a-how-an-estimate-becomes-a-record)
  - [5.1b The residual rule — an average covers only what was not measured](#51b-the-residual-rule--an-average-covers-only-what-was-not-measured)
  - [5.1c The residual is held, and charged to nobody](#51c-the-residual-is-held-and-charged-to-nobody)
  - [5.1d The back-trace reaches birth, and it runs on both sides](#51d-the-back-trace-reaches-birth-and-it-runs-on-both-sides)
  - [5.2 Onboarding as resolution — and as the adoption incentive](#52-onboarding-as-resolution--and-as-the-adoption-incentive)
  - [5.3 Privacy — market data public, personal ledgers private](#53-privacy--market-data-public-personal-ledgers-private)
  - [5.3a Privacy is a network choice — Aequitas sets principles, not practice](#53a-privacy-is-a-network-choice--aequitas-sets-principles-not-practice)
  - [5.3b What a trust network owes, and what "funding" one means](#53b-what-a-trust-network-owes-and-what-funding-one-means)
  - [5.3c Federation, and where it is going](#53c-federation-and-where-it-is-going)
  - [5.3d How a dispute resolves](#53d-how-a-dispute-resolves)
  - [5.4 There is entry, and there is no exit](#54-there-is-entry-and-there-is-no-exit)
  - [5.5 Parallel implementation — trading across the money boundary](#55-parallel-implementation--trading-across-the-money-boundary)
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
  - [6.4d Who holds the demand lever](#64d-who-holds-the-demand-lever)
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
- [8. Where the rest of the project lives](#8-where-the-rest-of-the-project-lives)

---

<!-- tag: fnd-s0 -->
## 0. The One-Sentence Theory

> **Aequitas is a universal accounting of material flows.** Every credit and every debit is a record of matter and energy moving through the world, attributable to the people who caused the movement. **Cost is nothing other than this.**

**Aequitas is a theory of cost. It is not a theory of value, and it does not need to be.**

This distinction is load-bearing. Every previous attempt at objective accounting — Odum's emergy, Technocracy's energy certificates, the labour theory of value — claimed to have found what things are *worth*, and every one was refuted on the same ground: **supply-side only, ignores demand.** The refutation is a stock move and takes one sentence.

Aequitas makes the narrower and far more defensible claim. **Cost is what a thing takes from the world; it is physical, and we can measure it. Value is what someone thinks it is worth; it is not physical, and we do not attempt to measure it.** Value enters the system as *feedback and pledges* (§6), never as an accounting quantity.

> **On the credit side, the substance is *time* — and time, not effort**. A credit records *time a human spent*, and the conceptual leap Aequitas asks of a reader is to see time itself as the finite thing being spent — like money is "spent" today, except that time is possessed by every person in exactly equal measure (24 hours a day) and can be neither hoarded, lent, nor transferred (A3 (non-fungibility)). This is the deep reason Aequitas produces a **bounded** inequality where money produces an unbounded one: money accumulates without limit; time structurally cannot — you get 24 hours a day and no more, ever, and you cannot buy anyone else's. Effort, hazard, and skill are real differences between workers, but they resolve as *material* costs (A2 (time as measure)), never as a time-multiplier. **Because the unit of account is an equally-distributed, non-transferable resource, the *engine* of a bounded inequality is the arithmetic itself, not any rule that polices it.** *(The exact bound, though, is a **conditional** result, and it is an **absolute maximum rather than an expected spread**. It depends on the value a network sets for its floor, on whether that network credits a child's learning time, and on fraud not manufacturing hours; see §7.5.5. **A very hard working life reaches about 1.6×, not 2.4×.** Earlier drafts overstated it as a flat arithmetic certainty.)*

Everything downstream — no capitalism, no rent, no taxation, no externalities, no inflation — is a *consequence* of taking the cost rule seriously and applying it without exception.

---

<!-- tag: fnd-s1 -->
## 1. Axioms

These are the immutable core. Nothing in Aequitas may contradict them, and nothing that varies below them may amend them (A8).

<!-- tag: fnd-a1 -->
### A1 (materialism of cost)

**Every credit and debit is a record of a real material or energy flow — there is no abstract, issued, or fiat quantity anywhere in the system.**

Down to the oxygen a human inhales and the CO₂ they exhale.

*Grounding for attribution.* Flows are attributed to whoever caused them, on the juridical principle of **responsibility imputation** — impute responsibility in accordance with who was in fact responsible. This is [David Ellerman's labour theory of property](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf), and it is deliberately preferred to any labour theory of *value*: it is a theory of imputation, it inherits none of the transformation or negative-value problems, and it appeals to a principle its opponents already accept everywhere else. Only humans act; tools and capital do not. Responsibility therefore imputes to people, never to machinery or its owners.

> **Corollary — financial instruments carry no debit**. Stocks, bonds, currencies, crypto-tokens, options, and other financial claims are exactly the "abstract, issued, or fiat quantity" A1 excludes: they are not matter or energy. **They therefore never appear on any ledger.** What *is* accounted is the **material** they are claims *upon* — a factory, land, a building — and that material's debit sits on whoever physically **holds or operates** it (embodied-material dischargeable on transfer; creation-cost holding-time-split, §3.2/§6.2b), never on the paper. This is not a loophole for hidden wealth: owning a factory through shares does not move its material debit to *nobody* — it stays on the factory's operators, by holding time. The consequence is measured in the scenario suite: entering the previously-wealthy **material-only** collapses the observed inequality tail by ~three orders of magnitude versus their paper net worth (§7.5, `06-simulation/scenario-suite/q4_locked_ledgers.py`), because financial wealth was never material and physical consumption is bounded by time.

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

**Every consequence of an activity is accounted to whoever caused it, including consequences discovered decades later — there is no "outside" of the accounting.**

> **Note on the wording, v0.21.** Through v0.20 this read *"every consequence is **priced into it**."* That phrasing said a consequence rides the *activity's output*, which is not what the system does and not what any section implements: **§3.2b** keeps pollution permanently on its causer rather than on the goods, **§5.1c** holds an unattributed residual on nobody at all, and **§6.2a** refuses to let a cost regress upstream. **A4 requires that every cost land on *a* ledger, never that it land on the *product's* ledger.** The substance is unchanged; the same defect in A5 is repaired directly below, and it is the same defect.

<!-- tag: fnd-a5 -->
### A5 (cost, not price)

**A thing's cost is the current best estimate of what was materially consumed to make it. Nothing is added to that figure, and nothing enters it that the thing did not consume.**

**Whoever takes a thing, or receives a service, takes on a debit equal to that figure. There is no profit in exchange — only debit discharged and debit acquired.**

Competition happens on **quality, artfulness, and efficiency**, never on margin.

**The boundary is physical fate: what was used up making the thing is in its cost; what survived the process is not** (§6.2a). A durable asset holds its own creation-cost, carried by its holders (§6.2b), and **that cost never enters the things the asset was used to make.**

**This is not an exemption from A4 (no externalities).** Every cost still lands on a ledger. It is **A1 (materialism of cost)'s imputation rule applied to cost**: a cost attaches to whoever caused it, and **a thing causes nothing** — only people act. Charging a beef buyer for the barn is the same error as charging a ring buyer for the miner's tailings, which §3.2b already refuses. **Worked numbers: §6.2b.**

**The estimate is never final.** Better measurement re-weighs it, and every record made under it, automatically (A6 (derived, not stored), §3.3). **A cost is a dated reading, not a verdict.**

> **⚠️ What this replaced, and why — v0.21.** Through v0.20, A5 read *"the **price** of anything is its true, current-best-estimate material cost."* An outside economist review put that sentence against §6.2b and found a contradiction: if a barn's 20,000 hours never enter beef's debit-cost, then **beef's "price" is not beef's cost, and A5 fails.**
>
> **The ruling was not the error. A5's wording was**, in three separate ways:
>
> 1. **It said "price."** Nothing here has a price. Things carry a **debit-cost**, and it moves.
> 2. **It never said what counts as a cost *of the thing*.** The capital-vs-consumption boundary existed in §6.2a and was never lifted into the axiom, so the axiom read as contradicting it.
> 3. **"True" reads as final**, which fights §3.3 and A6.
>
> **The critic's step is to assume the beef caused the barn.** Under A1 only people act, so a cost cannot attach to an output that did not cause it. **§3.2b forbids that flow downstream and §6.2a forbids it upstream; capital is the third face of one rule already written down twice.** A5, which located cost on the *thing*, was the sentence out of step. **No mechanism moved in this repair.** Full argument: `00-strategy/A5_repair_PLAN_v0.1.md`, register **B8**.

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
### A8 (no governing body)

**No organization that grows up around Aequitas may acquire authority over its core rules — governance is a protocol property, not an institution.**

Rules evolve as **immutable core + open variance**: everything below the core may differ from one trust network to the next, and those differences compete in public.

**What may vary.** A trust network may run a different weighting model, a different self-care floor, a different privacy practice, a different verification rung. **It must publish what it runs, and anyone else must be able to re-compute its claims** (§5.3b, §6.4b).

**What may not vary.** The axioms above, and the conformance requirements in [`Aequitas_Conformance_v0.3.md`](Aequitas_Conformance_v0.3.md).

#### Which activities are always creditable is left to the network

Which activities are **always** creditable — childcare, schooling and whose schooling, subsistence farming, untrained medical assistance — is **not settled by this document, and should not be.** It is exactly the kind of question open variance leaves to networks competing in public.

**But name the risk: the set of always-credited activities is a capture surface.** A network that can declare an activity creditable can issue credit. **The defence is structural rather than procedural.** Competing networks, plus ratio-based evaluation (§3.5): a network that credits worthless activity produces members with poor efficiency ratios, and other networks stop trading with it. **This is OP-10 (weighting governance) wearing different clothes and should be worked with it.**

**A second structural defence, from §3.3a.** A trust network's membership composition is public, and **a network concentrated in the sector it audits is captured by construction.** That makes capture *detectable from the log* rather than something anyone must police. It is a screening property, and it applies to always-creditable activity lists as much as to cost constants.

*(This was §10.1 through v0.23. It moved here in v0.24 because it states what may vary, which is what this axiom is about.)*

> ### 📦 A TRUST NETWORK HAS NO SET SIZE
>
> **A8 is about who may change the rules. It is not about how big anyone is.**
>
> A trust network may cover one valley, one trade, one country, several continents, or the world. **Nothing in these documents fixes the size of a network, and nothing should.** Size is one more dial under §1.2 — the accounting is identical at both ends of it.
>
> **One place in this document depends on that.** §5.3c expects networks to **federate and merge toward a single network over time**, not to settle into separate regional systems.
>
> *(Through v0.22 a second example stood here: that the `24 ÷ F` bound held across every interoperating network. **Struck in v0.23.** Networks do not trade with each other and no book is ever added to another, so the bound describes one network's own books — §5.0 and §7.5.5.)*
>
> **Where this document does mean somewhere geographic**, it is describing a *physical* thing handed to a *physical* person: a butcher's queue for a scarce cut (§3.4a, §7.5), or a village served by one generator (§3.2b). **A scarce object has to be given out somewhere. That is a fact about the object, not about the network.**
>
> *Renamed in v0.22. This axiom was called "local governance" from v0.1 to v0.21, where "local" meant "not imposed from a centre". **Several outside reviewers read it as "small and geographic" and built objections on that reading.** The word was doing two jobs and only one was intended, so it was removed rather than explained.*

<!-- tag: fnd-s1-1 -->
### 1.1 Named conventions

Some quantities the system needs are **not** physical facts. Where that is true, it is stated here rather than hidden in an implementation detail. **A convention that is declared is not an ad-hoc rule; a convention that is disguised as a measurement is.**

| Quantity | Status | Why it is not a measurement |
|---|---|---|
| **Split of a team's credit across its members** | ✅ **Not a convention — dissolved (A2)** | Credit is *time worked* (§6), so each member is credited **their own hours** — the "welder caused 40% of the bridge" number is never needed. Credit is not a share of output. **OP-18's team-credit half was a mis-statement; A2 already answers it.** *(A residual remains — apportioning a jointly-*caused debit* across a team — but that is a debit-attribution question, minor, sibling to OP-25 (illicit dumping).)* |
| **Split of *labour* across co-products** | ✅ **Convention with a measurable basis — rides the material split** | One labour process yields several products (farmer's hours → beef + hide); the hours leave no per-product trace, so a convention is required (physical-trace test). The declared convention: **labour rides the same physical split §3.4a already measures for the process's materials** (mass/deposition for cattle, cracking-energy for a refinery). Adds *no new lever* — it piggybacks on the rival-audited material θ. Changes no one's credit; it is a debit-side cost figure only. **OP-18(α) — closed 2026-08-05.** |
| **Split of an asset's residual creation-cost across its holders** | ✅ **Convention with a measurable basis — holding-time** | Apportioning a fixed creation-cost is a choice, but **holding-duration is a physical trace**, so the convention is measured, not invented: share = holder's holding-time ÷ total holding-time over the asset's life (§6.2b). Respects the dummy and symmetry axioms an even split fails. |

> **Two rows are absent, for two different reasons.**
>
> **A *"split of a joint process's debit across its co-products"* is not a free convention, and not a pure measurement either.** The process did physically divide the inputs, and that division is measurable — but reading it requires choosing an instrument, a period, and a sub-process boundary, and two honest choices can give different figures. **It is a choice that measurement constrains.** What Aequitas fixes is the obligations on that choice: measure at the facility for the period described, compute per dimension before collapsing, publish the method, and never let demand or yield enter. **The method itself belongs to the industry, under §1.2.** See §3.4a. *(Stated as a pure measurement until v0.21; corrected in v0.22 after outside review.)*
>
> **And *shared-overhead attribution to co-products* has nothing to attribute** — under §6.2b all capital and overhead accrues to the **asset**, never to the co-products (the barn stays on the operator; hide and beef carry only their own consumables). See `00-strategy/OP-17_coproduct_allocation.md` and `00-strategy/OP-23_capital_and_pollution.md`.

**The test that separates the two columns, and it is the useful output of the OP-17 (joint production) work:**

> **Did the thing being divided leave a physical trace?**
> **Where it did — measure.** Feed energy, cracking enthalpy, and a turbine's heat/power trade-off are facts about a process.
> **Where it did not — declare a convention and say so.** Labour hours and shared overhead leave no trace to an individual output, and no instrument will ever find one.

**The project's hard problem is division, not measurement** — but v0.4 narrows that: it is division **of the untraceable**. See the objections register §0.

---

<!-- tag: fnd-s1-2 -->
### 1.2 What Aequitas is, and what is therefore out of scope

**Aequitas is a system in the sense that capitalism is a system.** It is not an organisation, a protocol, a piece of software, or a body that anyone joins. **It is a set of principles about how cost is accounted for.**

> **Cost accounting is the principle. Records and data collection are praxis, executed by implementers.**

**And it is deliberately narrow in what it asks society to change.** Municipal government, planning bodies, courts and the civil service are kept. **Only their economic nature changes** — they stop being funded by extraction and are credited for the work they do. **The target is oligarchic capture, not administration that works.**

Trust networks operate in the real world and must deal with governments, courts, statutes and regulators. **That is their problem, not this document's.** How an implementer stays lawful where it operates is up to that implementer. Capitalism does not carry a data-protection chapter; banks do.

#### The test for what belongs here

> **If a principle survives at both ends of a dial, the dial is not part of the principle.**

Two thought experiments, both fully compatible with everything in this document:

- **A machine-governed society with zero transparency**, where only the machines know the ledgers and no human ever reads one.
- **A techno-anarchist society with total transparency and no privacy at all**, every record public to everyone.

**The accounting is identical in both.** Conservation still holds, the integrity constraints still recompute, the residual rule still runs, the disparity ceiling still binds. **Nothing in this document changes.**

**So human-facing transparency is not a foundational question.** It is the §5.3a dial, and §5.3a is right to leave it to the network. The same reasoning applies to storage technology, jurisdiction, corporate form, and compliance posture.

#### What this rules out of scope, explicitly

| Out of scope | Where it belongs |
|---|---|
| Data-protection and erasure law | The implementer, under its own jurisdiction. Research: `02-research/Law_gdpr-right-to-erasure_v0.1.md` |
| Data security, backups, key management | A technology problem (§5.3c) |
| Corporate or legal form of a trust network | The implementer |
| Which cryptography, which database, which protocol | The implementer |
| Whether the ecosystem converges to one network | A prediction, not a design input (§5.3c) |
| **How a cost constant gets audited** — who replicates, what triggers a review, how a contested constant is handled while contested | The implementer (§3.3a). **The requirement that it be answered is not out of scope**; the five properties in §3.3a are conformance items 16a–16c. |
| **Which instrument reads a joint process's split**, and over what period | The industry (§3.4a). Same shape: the obligations are fixed here, the method is not. |

**This is not a way of avoiding hard questions.** Every item above is real and someone must answer it. **It is a statement about which document answers it** — and about the failure mode of writing a theory of cost that quietly becomes a theory of software, governance, and compliance because those questions arrived while nobody was drawing the line.

> **The dial test is the standing screening question for anything proposed for these documents, and what it leaves behind is a set of conformance requirements, never an architecture** — [`Aequitas_Conformance_v0.3.md`](Aequitas_Conformance_v0.3.md). **What must be true, never how to build it.**

---

<!-- tag: fnd-s2 -->
## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No exceptions for professions, nations, or classes. Units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7 (universal accounting)). Where a genuine convention is required, §1.1 names it rather than concealing it. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing open variance. **Cost constants are the weakest point of this criterion, and §3.3a says so rather than claiming otherwise** — the auditing practice is a network's own design, held to five published properties (conformance 16a–16c), and no network has yet demonstrated a working one. |
| **Fecundity** | The verification ladder *pulls* technological development (§4). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses want (§7.3). Onboarding is individually rational (§5.2). Pledges give surplus a purpose (§6.4). **Every co-product allocation is an open scientific question that better instruments improve (§3.4a).** |

**Fourth screening question — "does this need a Paul Glover?"**
Ithaca HOURS died when its founder relocated; he himself said every local currency needs a full-time networker to promote, facilitate, and troubleshoot. A mechanism that depends on an enthusiast is a mechanism with an expiry date. **Every proposed mechanism must pay its own maintainer from inside the system** — as auditing-as-credited-work does. **Cost-constant auditing is the case that does *not* clearly pass this test**, which is why §3.3a states it as an unsolved network-design problem rather than a mechanism. Apply alongside universality, decentralization, and *who games this?*

---

<!-- tag: fnd-s3 -->
## 3. The Ledger Model

<!-- tag: fnd-s3-1 -->
### 3.1 Structure — an event log, not a balance

One permanent, append-only **record of activity**: who did what, when, involving which materials and energy. An account's displayed standing is a **continuously recomputed projection** of that log.

<!-- tag: fnd-s3-2 -->
### 3.2 The two kinds of debit — and the two components of property debit

![The debit taxonomy: DEBIT as a vector splits into property debit (embodied-material, dischargeable; and creation-cost/labour, holding-time-permanent) and consumption/pollution debit (never discharged, stays on the causer); two cross-cutting rules — self-work identity and non-cascade.](../01-wiki/assets/debit-taxonomy.svg)

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

<!-- tag: fnd-s3-2a -->
### 3.2a Debit is a vector, collapsed on demand

A debit is **not one number.** It is a bundle of physical quantities — kilograms of a substance, joules, labour-hours, cubic metres of water, land-area-years — stored separately in the log and combined into a single comparable figure only when someone needs to compare two things, via the current weighting model.

This is A3 (non-fungibility) and A6 (derived, not stored) working together: the physical record is what implementations must agree on; the collapse is what they may differ about (EventLog §3).

> **One rule follows immediately: any division of a debit — across co-products, across a team, across anything — is computed on the vector, per dimension, *before* collapsing.**
>
> Divide the collapsed number instead, and whoever maintains the weighting model controls every allocation in history without anyone seeing it happen. Divide per dimension, and the split does not depend on the weighting at all: two communities running different weighting models compute the same split, and disagree only about what it weighs. This closes one route into OP-10 (weighting governance).

<!-- tag: fnd-s3-2b -->
### 3.2b Only property transfers — pollution and transport never do

The two kinds of debit behave differently under transfer:

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
> **Attribution is by the grid's actual fuel mix at the times the consumer drew power.**
>
> **Terms used here.** A **grid** is the wired network that joins several generators to many consumers. Its **fuel mix** is the proportion of its output coming from each fuel at a given moment — for example 55% gas, 30% nuclear, 15% wind. Its **emission intensity** is the CO₂ released per kilowatt-hour delivered, computed from that mix. A **half-hourly period** is the settlement interval most grids already meter and publish.
>
> **How the figure is produced.** Three records already exist and are combined:
>
> 1. The consumer's meter records **how much** they drew, and **when**.
> 2. The grid operator records its **output and fuel mix** for the same period.
> 3. Multiplying the two gives the consumer's emission for that period. The month is the sum of its periods.
>
> Nothing new has to be built or agreed. The grid is one entity with several inputs running together: nuclear plants hold a steady base, wind varies with weather, gas plants start and stop to follow demand. **A consumer drawing power during a period when more gas was running drew dirtier power, and the ledger says so for that period.**
>
> #### An example, with the numbers
>
> A household draws **300 kWh** in a month. *(Emission intensities below are illustrative, not sourced.)*
>
> | When they drew | kWh | Grid gas share | Intensity | CO₂ |
> |---|---|---|---|---|
> | Peak, 6–9pm | 180 | 55% | 0.20 kg/kWh | **36.0 kg** |
> | Overnight, 1–5am | 120 | 15% | 0.06 kg/kWh | **7.2 kg** |
> | **Total** | **300** | | | **43.2 kg** |
>
> Over the same month the grid as a whole averaged **0.13 kg/kWh**. A flat monthly average would have charged this household `300 × 0.13 =` **39.0 kg**. **The timed figure is 43.2 kg, about 11% higher, because this household draws mostly at peak.**
>
> **Now move 100 kWh — a car, a dishwasher, a water heater — from peak to overnight.** Peak becomes 80 kWh (16.0 kg), overnight becomes 220 kWh (13.2 kg). **The total falls to 29.2 kg, a cut of 14 kg or 32%, with no reduction in how much power was used.** Under any flat-average rule that change is worth nothing.
>
> **Transmission losses stay with the producer.** Power is lost as heat in the wires between the generator and the meter. That power **was never handed to anyone**, and a hand-off is what moves a debit to a receiver (§6.4a), so the loss stays with the generator and the network operator who caused it. **Worked: at a 7% loss, generators burn fuel for `300 ÷ 0.93 =` 323 kWh so that 300 kWh arrives. The 23 kWh difference, about 3 kg of CO₂, is the network's, not the household's.**
>
> **What this settles, and what it rules out.** The *marginal-vs-average* question is answered: it is **neither the single plant that ramped up, nor a flat annual average**. It is **the measured mix over the periods the consumer actually drew**. And it rules out attributing a physical emission by a **commercial supply agreement**. An agreement is a paper claim, not matter or energy, and A1 (materialism of cost) says paper claims never appear on any ledger. **A record of CO₂ must come from a measurement of CO₂.**
>
> **Where the generator's incentive to decarbonise now sits.** Three places, all of which already exist:
>
> - **Their own capital and process debit.** Building and running a gas plant puts its construction cost and its non-combustion pollution on the operator, permanently (§6.2b, and the rule at the top of this section).
> - **Pledges.** A community that wants clean generation pledges toward it (§6.4), which is how any capital-heavy work gets authorised here.
> - **Retroactive re-weighting.** Cleaning the grid lowers the intensity figure, and §3.3 then lightens every past consumer's recorded debit. Remediation pays the people who funded it, backwards.
>
> **Where the supply is physically separable, measure it directly.** A factory with its own wind turbines, or a site on a dedicated line from one generator, is not drawing from a pool. The physical trace exists, so it is measured rather than apportioned.
>
> **Single-generator case.** A village served by one generator needs no apportionment at all — its mix *is* that generator's output.
>
> > **⚠️ Amended in v0.22, reversing an earlier ruling.** From v0.10 to v0.21 this paragraph attributed emissions by the consumer's **contracted supply mix**, on the argument that a clean generator could then win contracts by offering lower-debit power. **That made a commercial agreement decide a physical record, which A1 forbids.** The generator's incentive is instead carried by the three routes listed above. Register entry: **B12**.
>
> **⚠️ Open universality edge.** "Real-time-dispatched vs batch" is a *spectrum*, not a clean binary: grid storage (pumped hydro, batteries) is a growing intermediate case, and on-demand services (a restaurant cooking your order) sit near the line. The principle is sound at the poles; the exact criterion for the middle is a registered open question, not yet closed.

**The consumer signal is not lost.** §5.1b already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**. Buyers and pledgers can still see and prefer low-pollution goods; only the *debit* is pinned to the causer. See §7.2 for why this makes the anti-pollution incentive *stronger*, not weaker.

**Custody is accepted, not imposed**. "Custody follows possession, no right to refuse a transfer" means **no right to accept an object but refuse its debit** — you cannot take the object and disclaim what rides with it. It does **not** mean anyone can be forced to *receive* an object. Read the other way, the rule would license garbage-dumping, the exact abuse it exists to prevent (§3.6).

<!-- tag: fnd-s3-2c -->
### 3.2c An organisation's debit is its members' debit

**Terms used here.** An **organisation** is any account that is not a single verified human: a business, a co-operative, an institution, a public body. A **member** is a person who works for it during the period in question.

> **An organisation's account is a view of its members' positions, not an owner of them. Every debit recorded against an organisation is, at the same time, the debit of the people who worked there, divided among them in proportion to the hours each worked for it.**

**Why this follows from A1 (materialism of cost).** Under A1, cost attaches to whoever **acted**, and **only people act.** A co-operative never lifted anything, drove anything, or burned anything. Its members did. So an organisation cannot be the final holder of a debit, for the same reason a barn cannot (A5, §6.2b) and a power station cannot (§3.2b). **The organisation is a bookkeeping convenience. The people are the causers.**

**This is not a new rule. It is an existing rule stated for entities.** §7.1 already says a team's debit is shared **by hours worked, not by rank**, and §6.4c already splits a task's pledged cover **pro-rata by hours on the task**. This section says the same thing about the organisation as a whole.

**Closing an organisation is therefore not an event that moves anything.** There is nothing to distribute at the end, because nothing was ever held anywhere else. **Dissolution has no effect on any ledger.**

#### An example, with the numbers

Ten people each work **2,000 hours** in a year for one co-operative. The co-operative takes on **24,000 hours** of debit that year.

| | |
|---|---|
| Total member hours | 10 × 2,000 = **20,000 h** |
| Each member's share of the hours | 2,000 ÷ 20,000 = **10%** |
| Each member's share of the debit | 10% × 24,000 = **2,400 h** |

**Now close the co-operative and open a new one with the same ten people.** Each member still carries 2,400 h. Repeat the year, and each carries 4,800 h. **After ten rounds each member carries 24,000 h, and their own gate `D ≤ ρ·C` begins to bind.** The count never resets.

#### Two boundaries this rule does **not** cross

| Not covered | Which rule covers it | Why they do not collide |
|---|---|---|
| **A durable asset's creation-cost** — a hospital building, a plant, tooling | **§6.2b**, split by *holding time*, so a new hire bears about zero | §6.2b exists to stop an entry toll on capital-heavy essential work. **That is property debit on an asset. This section is about consumption and operating debit**, which §3.2 already makes permanent on its causer. Different debit, different rule, no conflict. |
| **A member's own credit** | **A3 (non-fungibility)** | Credit never moves, in either direction. Members are credited their own hours whatever the organisation does. **This section divides debit only.** |

> **Stated honestly: this is a declared convention, not a measurement** (§1.1). Hours worked leave no trace pointing at any particular debit the organisation took on. **Hours are chosen because they add no new lever** — they are already recorded for credit, already capped at 24 a day by IC-7, and already the basis §7.1 and §6.4c use. **A different basis, such as an equal split or a seniority weighting, would be a new thing to game.**
>
> **This convention may also close the residue §3.4a leaves open** — apportioning a jointly-*caused* debit across a team. The two questions have the same shape and now have the same answer. **Not claimed as closed until it is checked against §3.4a's case directly.**

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
### 3.3a Who checks the science — the problem, and whose problem it is

> **Ruling, v0.22: how a cost constant gets audited is a trust-network design problem, not a foundational one.** This section states the problem and the properties any answer must have. **It does not supply the answer, and earlier versions overstated the one they offered.** See "What this section used to claim" below.

#### The problem

**Terms.** A **cost constant** is a published number saying what a process takes — the energy to smelt a tonne of aluminium, the hours to remediate a tonne of CO₂. **Re-weighting** is §3.3: when a constant improves, every record computed from it recalculates, backwards through history.

**So whoever publishes a constant sets every figure in that sector, for all time.** That is the largest capture surface in the system.

**And the pressure on it runs one way.**

| Error direction | Who wants it fixed | What happens |
|---|---|---|
| The constant **overstates** a debit | Everyone paying it | Corrected quickly |
| The constant **understates** a debit | Nobody — correcting it worsens every subscriber's ledger | **Nothing happens** |

**The result is systematic drift toward under-costing.** This is not a prediction. **It is the observed failure mode of every carbon-accounting regime attempted so far**, and §3.5 tolerates it arithmetically, which is what makes it insidious: **no equation breaks.** Registered as **OP-24 (understatement drift)**.

**One channel is closed for free, and should be claimed.** There is no market-dominating firm to fund a favourable result, because **A5 (cost, not price) removes the profit that pays for captured science today.** The Enron-shaped failure cannot operate the same way here. **That is real and it is not sufficient.**

#### What this section used to claim, and why it was withdrawn

From v0.4 to v0.21 this section offered a fix:

> *"The natural auditor of a cost constant is the rival sector, not the consumer. If beef's energetics are understated, plant-protein producers are materially harmed and will fund the replication."*

**Two objections, and the second is the one that sinks it.**

1. **Rivals are often absent.** The register already said this. A good with no substitute has no rival, and **a constant that cuts across every sector equally has no rival by construction.**
2. **A rival's best move is not to fund your correction.** Funding a replication costs real hours and the benefit is **shared with every other producer in the rival sector** — a public good among rivals. **Getting their own constant set generously is cheaper and the benefit is private.** So the equilibrium is **mutual understatement, not mutual policing.** The mechanism assumed rivals are adversaries; on this axis their interests are aligned.

> **And it failed hardest where the stakes are highest.** This section itself called the **ambient-stock and baseline constants** the largest levers in the weighting model. **Those have no rival at all** — everyone benefits from a high pollution baseline and a low stock reading. **A mechanism that works for beef versus plant protein and fails for CO₂ is pointed the wrong way round.**

**Rival-sector audit survives as one pressure among several. It is not the answer and this document no longer presents it as one.**

#### Whose problem it is

**A network cannot operate without answering this**, and no two networks will answer it the same way. That is the §1.2 test: **state what must be true, never how to build it.** The same ruling was made for split methods (§3.4a) and for privacy practice (§5.3a).

> **Auditing cost constants is one of the problems a trust network exists to solve.** How it does so — who replicates, how replication is commissioned, what triggers a review, how a contested constant is handled while it is contested — is the network's design, published and checkable like everything else it does.

**Design requirements. An implementation must be able to show how it meets each of these.**

| # | What must hold | Why |
|---|---|---|
| **1** | **Two unaffiliated replications before a constant may re-weight history.** | Retroactivity is too powerful to trigger from a single source. |
| **2** | **Every constant is published with its method, its version, and its uncertainty interval.** | A constant nobody can re-derive is an authority assertion. Without an interval, "how well is this known" has no answer. |
| **3** | **Review is triaged by magnitude × concentration of beneficiary**, never by magnitude alone. | A materiality threshold alone helps an attacker, whose job then becomes making a falsification look immaterial. |
| **4** | **A network's membership composition is public.** | **A network concentrated in the sector it audits is captured by construction.** This makes capture a *detectable screening property* rather than a rule anyone enforces. General-membership networks are structurally sounder than sector-specific ones. *(The co-op form does not fix this: the conflict is directional, not monetary — Arthur Andersen was paid by Enron, and a client-owned Andersen would have been worse.)* |
| **5** | **The network states which constants it has not reviewed, and how old each reading is.** | The floor rule (§5.1a) applied to weights: an unreviewed constant is a floor on confidence, never a value. |

**Everything in §3.3's stock rules is governed by these too** — the natural-remediation baseline and the ambient-stock measurement are the largest levers in the model, and they are constants like any other.

**And coverage figures are governed by these with full force.** A mis-set energetics coefficient changes what a recorded flow *weighs*. A mis-set coverage figure — the *N*, *Y* or *Z* of §5.1b — changes **which flows are deemed to exist at all.**

> **Coverage has something weights do not: two parties with a private interest in getting it right.** The **instrumented producer**, materially harmed when undocumented produce prices too cheaply, and **the dark producer**, who cannot transact inside the system until they onboard (§5.1c). **Neither requires the residual to be allocated to anybody**, which matters, because it is not.
>
> **This is why OP-24 is narrower than it looks: the audit of *extent* has interested parties; the audit of *weight* does not.** That asymmetry is the useful thing this section knows.

#### What is not scoped out

**The requirement stays here even though the mechanism does not.** A4 (no externalities) requires every cost to be accounted to whoever caused it. **It does not require the first estimate to be right** — §3.3 already makes every figure a dated reading that improves. **But systematic, uncorrected drift is costs escaping, and that is an A4 failure.**

> **So a network that cannot show how it audits its constants is not conforming. It is not free to have no answer.**

**⚠️ And say the honest part plainly: no network has yet demonstrated a working answer, because no network yet exists.** The five requirements above are what a design will be judged against. **They are not evidence that the problem is solved.** Test still owed: simulate a population of networks under these incentives and find the conditions under which drift stops being arrested (Objections §C, item 2).

<!-- tag: fnd-s3-4 -->
### 3.4 Resolution is opportunistic

**Resolution.** Record what is known; estimate the rest from averages; refine forever. If someone commutes daily, estimate from cohort averages; learn which car they drive and it sharpens. All of it revisable.

**⚠️ Allocation is only partly a resolution problem.** Dividing **physical inputs** is largely a resolution problem: the process did divide them, and better instruments read that division more finely (§3.4a). *Largely, not entirely* — better instruments narrow the range but do not pick the instrument, the period, or the sub-process boundary, and those choices are the industry's to make (§3.4a). What is **not** resolvable at all is dividing quantities the process **never physically divided**: labour hours across co-products, shared overhead, and joint responsibility across a team.

> **The distinguishing test is whether the divided thing left a physical trace.** Where it did, measure. Where it did not, declare a convention (§1.1) and say so.

<!-- tag: fnd-s3-4a -->
### 3.4a Joint production — dividing one process's debit among several outputs

> **This section is written to the document standard set in v0.22: state the rule, define the terms, show it working with numbers, stop. It is the reference for the plain-language pass across the rest of Foundations.**

#### What the problem is

Some processes produce several things at once from one pool of inputs. A steer eats feed and yields beef, hide, tallow, bone, manure, and methane. A refinery heats one stream of crude oil and yields petrol, diesel, jet fuel, heavy fuel oil, and coke. A combined-heat-and-power plant burns gas and yields both heat and electricity.

**These are called *joint products* or *co-products*.** One process, one bill of inputs, several outputs. The question is how much of that bill each output carries.

#### The rule

> **A joint process's debit divides according to where the process physically sent its inputs, measured at that facility, over the period being described.**

**What "where the inputs went" means.** Feed eaten by a steer is deposited as muscle, fat, hide, and bone, in proportions that can be measured. Heat applied in a refinery breaks specific bonds to make specific fractions, and the energy required for each is measurable. Fuel in a heat-and-power plant splits between heat and electricity along a relationship the turbine's own performance curve describes.

**This is not a rule about the outputs.** It does not ask what an output weighs, what it is worth, or whether anyone wants it. It asks what the process did.

#### How the split is actually produced, in order

1. **Read what the facility meters, for the period in question.** Masses in and out, energy used, labour hours. Where a plant meters separate production lines — cutting separately from tanning, grinding separately from sieving — **that metered routing is the split.** Nothing needs to be inferred.
2. **Where metering is coarse, use a physical model to bridge the gap.** If a plant records only total energy plus output masses, the mass split is a low-resolution reading, and a model of the process physics estimates the rest. The model is a fallback, not the primary source.
3. **Replace the model whenever finer measurement becomes available.** Better data always supersedes a model (§3.3 — every affected record recalculates when the science improves).

**Match the period to the output.** Compute the split from data covering the same stretch of time as the output it describes. Do not use a standing table from last year. A longer window forces you to assign costs to goods that were sitting in storage while conditions changed.

#### What Aequitas fixes here, and what it does not

This is the part earlier versions stated too strongly, and an outside review was right to say so *(economist review, 2026-08-24, finding #24)*.

> **Aequitas fixes the obligations. It does not fix the method, and it cannot.**

| Aequitas fixes | Left to the industry |
|---|---|
| The split must describe **where the process physically sent its inputs** | Which instrument reads that, in this industry |
| It must come from **measurement at that facility, for that period**, before any model | What counts as a workable period for this process |
| It must be **computed per dimension before collapsing** to one figure (§3.2a) | Where the sensible sub-process boundaries are |
| The **method must be published**, with its version, so anyone can re-run it (§5.3b) | The method itself |
| It may **never depend on demand, desirability, or yield** (see below) | — |

**Why the method cannot be fixed here.** Determining how a process divides its inputs requires knowing that process. Oat milling has many stages — curing, cleaning, dehusking, aspiration, kilning, cutting — and a batch cleaned on Monday may be split across several dehusking runs on different days. **No single model fits every industrial process, and a document that tried to write one would be wrong in most industries and unfalsifiable in the rest.** This is the same scope rule §1.2 applies everywhere else: **state what must be true, never how to build it.** The people competent to set a milling method are millers; the people competent to check it are other millers.

**So the split is a choice that measurement constrains, not a number read straight off nature.** Two honest methods can give different figures. What stops that becoming a free hand is the four obligations above, plus the audit below.

#### What stops a producer choosing a flattering method

**There is no profit motive, because there is no margin to protect (A5).** There *is* a weaker motive, and it must be named: **understating your own debit improves your debit-to-credit ratio and makes your goods lighter for whoever takes them.** That is the standing open problem **OP-24 (understatement drift)**.

**Consumers of a good benefit from that good being under-costed, so they will not fund a correction.** A competing producer is at least *harmed* by it, which is better than nobody — but **§3.3a explains why that is a weak pressure rather than a mechanism**, and treats constant-auditing as an open network-design problem. **What this section fixes is the precondition: the method must be published, because nobody can challenge arithmetic they cannot see.**

**And the claim is auditable against records that already exist.** A mill claiming a figure for its flour can be asked for its power bills, its intake weights, its output weights, and its account of which power went to milling rather than to lighting and offices. The claim must reconcile with those records, within a stated margin of error.

#### One thing the split may never do

> **Cost may not follow demand, desirability, or yield.**

**A worked case.** A steer yields roughly 1% of its carcass as tenderloin and roughly 5% as material for hamburger. Tenderloin is scarce and sought-after; hamburger is neither.

**A pound of each costs the same**, because a pound of each embodies the same feed, water, and growing labour — adjusted only by *measured* tissue composition, since lean and fat differ in the energy required to deposit them. **It is not adjusted by yield or by desirability.**

Two reasons:

1. **Two identical steers in two towns would otherwise carry different splits**, because the towns want different cuts. The same physical process would produce two different cost figures. That fails universality (§2).
2. **It would ration the scarce cut by who can absorb the larger debit**, which is rationing by standing — the exact mechanism A5 (cost, not price) and §7.1 remove.

**The scarcity is real, and it is handled elsewhere.** How many cattle are raised is answered by pledges and signals (§6.4, §6.4d). Who gets the scarce cut is answered at the point of distribution — a butcher's queue, a lottery, or pledge-priority (§7.5). **Cost states what a thing took. Who receives a physically scarce output is a separate question, and this document deliberately does not settle it.** *("At the point of distribution" is geographic because a physical cut of meat is handed to a physical person somewhere. It is not a claim that trust networks are small — see A8.)*

#### Four things that follow

- **Waste outputs are co-products like any other.** Manure and methane take a share of the split. Nothing is left over, so there is no question of who absorbs an unwanted output.
- **The process sets an output's cost share; its fate sets its ledger character.** Manure is pollution debit in a lagoon, a co-product in a biodigester, and a measured fertiliser offset when spread on a field. The record of what happened to it (EventLog IC-4, fate closure) already captures this.
- **Labour has no per-product trace, so it is a declared convention.** The farmer's eight hours were spent on the animal, not on the hide. **The convention: labour divides in the same proportions as the process's measured material split.** It introduces no new basis and no new thing to game, and it changes nobody's credit — a worker is credited their own hours regardless (§6). It sets only how each co-product's debit-cost reads. *(OP-18(α), closed 2026-08-05.)*
- **Negative cost shares do not arise.** Each share is a forward measurement of what physically went in, and a deposition cannot be negative. Nothing is inverted, so [Steedman's negative-value result](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) does not transfer. Confirmed by simulation across 4,098 economies (`06-simulation/allocation-engine/RECURSION_RESULTS.md`). **Note the limit of that result: it proves no split produces a negative figure. It does not prove the split is unique.**

#### What remains open

**Apportioning a jointly-*caused* debit across a team.** When a team process causes pollution, or a harm discovered later, dividing responsibility among the members is a convention with no physical trace behind it. Minor and non-blocking; tracked alongside **OP-25 (illicit dumping)**.

**How far a split moves across honest methods.** Nobody has measured this. The test: take a refinery, a heat-and-power plant, and a livestock case, and compute the split under every defensible instrument and period. **If the range is narrow, the obligations above are enough. If it is wide, method choice is a large lever and belongs with OP-10 (weighting governance).** Owed; see the Objections register, §C.

<!-- tag: fnd-s3-4a-old -->
#### Superseded discussion, kept for reference

*Earlier versions headed this section "the process allocates itself" and said the split was "a measurement, not a convention." Both overstated it, for the reason given above: measurement constrains the choice without determining it. **The mechanism did not change in v0.22** — what changed is the claim made for it, the addition of the publication requirement, and the explicit statement that the per-industry method is out of scope. See Objections **B7**.*

*Also folded into the text above rather than kept separate: the labour convention (labour divides in the same proportions as the measured material split, OP-18(α), closed 2026-08-05) and the shared-overhead ruling (capital and overhead accrue to the asset and never reach the co-products, OP-23, closed in v0.5 — see §6.2b).*

<!-- tag: fnd-s3-5 -->
### 3.5 The books never balance — and must not

Every real process dissipates. Credit records useful work; debit records material and energy consumed plus pollution. **Aggregate debit therefore exceeds aggregate credit permanently and by construction.**

This is not an accounting defect. **It is the second law of thermodynamics appearing in the ledger**, and a material-flow accounting that *did* balance would be the one describing something physically false.

Two consequences:

1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds, not merely impractical.
2. **Sums are not meaningful; two separate numbers are.** **Ratio** (debit:credit) measures *efficiency* — how much you consumed per unit contributed. **Absolute credit** measures *contribution*. Neither substitutes for the other: a pure-ratio metric is infinite for a newborn and is gamed by ascetics who minimize both sides; a pure-sum metric ignores waste entirely.

> **And the scarce factor is not labour**. A recurring result across the societal-scale simulations is that **human hours are abundant, and the binding scarcity is material and energy.** Because self-care is credited work (§6.1b), the credited-labour pool is ~3.4× all *productive* labour — so re-shoring an entire economy's imports, or reallocating the world's captured/wasted hours to essentials, is nowhere near hours-limited (`06-simulation/scenario-suite/q1_autarky.py`: an autarkic US is bound by the energy transition and critical minerals, not labour; `q5_reallocation.py`: the freed pool covers the global health-worker shortage ~50–100× over). This sharpens what §3.5 already implies: since debit (materials + energy + waste) structurally outruns credit (hours), the **constraint the system actually binds against is physical throughput, not the supply of human time.** "We cannot afford to make/house/heal everyone" is a statement about money, not about hours.
>
> **The measured anchor (2026-08).** A bottom-up estimate puts the **labour a median US lifestyle commands at ≈ 1,380 h/yr** (`06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md`; measured from BLS employment-requirements × the actual PCE mix, EXIOBASE import labour, §6.2b durables, and own-pollution remediation — *not* a blanket ratio). Against the ~3,650 h/yr of self-care credit every living human earns, the median lifestyle commands **about a third of one person's annual credit** — the labour dimension has enormous slack, exactly as this callout claims. **And the same-standard efficiency spread is large:** cross-country accounting (EXIOBASE, `06-simulation/median-lifestyle/Q6.md`) finds the US the labour- *and* carbon-inefficient outlier — commanding **50–80% more embodied labour and 2.5–4× the CO₂ per capita** than Germany, Sweden, France, Japan, or Spain, which deliver a comparable-or-better material standard (and longer lives) at ~⅔ the labour. **This is the positive form of A4 (no externalities) and A5 (cost, not price):** the inefficient, fossil-heavy, long-chain method is simply *dearer in the ledger*, so the accounting rewards the efficiency the leaders already demonstrate — no mandate required. What looks like "we cannot afford a decent standard for all" is, quantitatively, an artefact of the most wasteful production method, not a limit of human hours.

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

**Governance rides existing machinery.** The remediation cost is a mitigation-cost estimate under the §3.3 stock-dependence rule and is governed by §3.3a — no new capture surface, and no new answer either: it inherits OP-24 unsolved.

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

<!-- tag: fnd-s4-cost -->
#### Each rung has a price, and the ladder must show it

The four levels say **how well** a claim is checked. They do not say **what the check costs to run**. A network choosing a rung is choosing a cost, and it must be able to see that cost before it chooses.

> ### 📦 WHAT A CHECK COSTS — IN PLAIN WORDS
>
> **A rung has two prices, and they move in opposite directions.**
>
> | Price | What it is | As you climb |
> |---|---|---|
> | **Setup** | The tools you must buy once | **Rises** |
> | **Marginal** | The work each further check takes | **Falls** |
> |
>
> **Climbing the ladder buys you cheaper checking, and you pay for it in tools.** A person must look at every item. A tool looks at every item by itself.
>
> **The setup price never lands on the goods.** Tools are front-loaded (§6.2a) and sit on the asset, split among its holders by holding time (§6.2b). **A tool's cost is never divided into the things it measured.** §6.2b closed OP-23 on exactly that point.
>
> **A check is not always an extra act.** For goods the base check is free, because the hand-off **is** the check: the receiver, by taking the goods and their debit, attests the goods exist (§6.4a). Nobody does a second thing.
>
> #### An example, with the numbers
>
> A farm ships **1,000 sacks** in a season. Each sack computes to about **10 hours** when it is handed over. The season is about **10,000 hours** of grain.
>
> | Rung | What actually happens | Per season | Per sack | Share of 10 h |
> |---|---|---|---|---|
> | **1 — the receiver signs for what they take** | This *is* the trade (§6.4a). No second act. | 0 h | 0 h | **0%** |
> | **2 — the network checks the method, by sampling** | Desk work. Field area × known yield per acre, against the loads the carrier recorded. **It never touches a sack.** | 2 h | 0.002 h | **0.02%** |
> | **3 — a scale on the loading dock** | Bought once, sits on the asset. Reads every load by itself. Only calibration is labour. | 0.5 h | 0.0005 h | **0.005%** |
> | **4 — a machine tallying continuously** | Machine time only. | 0.1 h | 0.0001 h | **0.001%** |
>
> **Read the last column downward. It falls.** Checking gets *cheaper* per unit as you climb, not dearer.
>
> **And note row 2.** A network audit is **cheaper per sack than a person watching sacks**, because it works on totals and cross-checks, not on items. It reads the size of the fields, what an acre of that crop is known to yield, and what the carrier recorded leaving the gate. **Three numbers that must agree.** Counting sacks would be the expensive way to learn less.
>
> #### ⚠️ A large verification cost is a red flag, not a design regime
>
> Suppose a producer reports that self-tracking costs **40%** of what they produce. On this farm that is **4,000 hours** to keep records on 10,000 hours of grain.
>
> **The network does the same job in 2 hours.** That is a **2,000-fold** gap.
>
> **No honest process costs that.** Overheads of that size belong to bureaucracy, not to measurement. **A network seeing such a figure should audit the producer, not redesign the ladder around them.**
>
> **And the system already reaches it.** Verification work is credited work (§5.3b), so inflating it is a way to claim hours — the unobservable-work problem of §6.6, already answered there by weighting a weak claim near zero and by IC-7's cap of 24 hours a day. **The party harmed is the rival producer whose own overhead is 0.02%**, and §3.3a already makes that rival the auditor.

**The cost of a rung is a network's own figure, not a constant here.** A scale costs different hours in different places. What Aequitas requires is that the figure be **published beside the rung** — the sampling rate and the periodic cost, never a per-transaction charge — exactly as §5.3b requires every estimating number to be published. A network that states its rung without stating its price is asking to be trusted rather than checked.

> **What the measured threshold actually says.** `06-simulation/residual-unravelling/residual_unravelling.py` sweeps a producer's disclosure cost against a population whose median unit carries about **1.0** in debit. The dark pool still unravels to **0.1%** at a cost of **0.40**; it collapses between **0.40** and **0.80**. **Plausible costs sit near 0.002** — the row-2 figure above. **The measured bound is therefore roughly 200 times higher than anything a working network would report.**
>
> **Read that as reassurance about the mechanism, not as a live constraint on it.** The residual rule keeps working across the whole range of realistic costs, and it fails only in a regime that would itself be evidence of something wrong. Earlier drafts, and §5.3a, read this backwards.

<!-- tag: fnd-s4-witness -->
#### A second record only helps if it can disagree

Climbing the ladder gets you a second record. That is necessary and it is not sufficient, and the difference is easy to miss.

> ### 📦 TWO PROPERTIES, NOT ONE — IN PLAIN WORDS
>
> **A second record must have two properties. Most people ask for only the first.**
>
> **1. Independence.** The fault that hit the first record did not reach the second record. The two were made on different paths.
>
> **2. Expressiveness.** The second record is *able* to hold a value that contradicts the fault.
>
> **A record can be fully independent and still useless.** If it can only say the same thing the first record says, it agrees no matter what.
>
> #### An example, with the numbers
>
> An attacker adds two false records at once. They invent 2.0 kg of a good arriving from nowhere, and 2.0 kg of the same good going to waste. This is a **balanced pair**.
>
> | What the check adds up | Answer | Does it fire? |
> |---|---|---|
> | Mass in − mass out, first record | 2.0 − 2.0 = **0.0 kg** | ❌ No |
> | Mass in − mass out, second record, made by a different party | 2.0 − 2.0 = **0.0 kg** | ❌ No |
> | Mass in − mass out, a third record, also independent | 2.0 − 2.0 = **0.0 kg** | ❌ No |
>
> **Adding more independent records never helps here.** Every one of them adds up to zero, because the lie was built to add up to zero. The check looks for a gap and there is no gap.
>
> Now weigh the actual pile of grain in the actual barn:
>
> | What the instrument reads | Answer | Does it fire? |
> |---|---|---|
> | Recorded stock | 2.0 kg | — |
> | Weighed stock | **0.0 kg** | ✅ **Yes — short by 2.0 kg** |
>
> **The scale fired because it can say a number the records cannot argue with.** It is expressive. The other records were only independent.

> **What defeats a balanced lie is physicality, not independence.** This is why the closure witness of §5.1b is a *physical* total and not a second set of books. Matter does not agree to be counted twice.

> **⚠️ And it says plainly where the trust went.** Rung 3 does not remove trust; it **moves** trust from the ledger to the **instrument**. An attacker who controls the scale wins completely, and nothing further down the chain can tell. **That is a better place for trust to sit than a ledger — a scale can be re-calibrated by a rival, and a lie cannot — but it is not "nothing to trust", and this document should never say it is.** Registered with **OP-22 (minimum audit disclosure)** and **OP-10 (weighting governance)**; a mis-calibrated constant is the same attack arriving at specification time rather than at reading time (§3.3a).

---

<!-- tag: fnd-s5 -->
## 5. Identity, Privacy, and Onboarding

<!-- tag: fnd-s5-0 -->
### 5.0 What this section is about, and who does the things in it

**This section describes work that a trust network does.** Nothing in it is done by Aequitas, because **Aequitas is not a body and cannot do anything** (§1.2). It is a set of principles about how cost is counted, in the same way that capitalism is a set of principles about how value moves. Banks and firms carry out capitalism. **Trust networks carry out Aequitas.**

**Terms used in this section.**

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books. It records material flows, checks the arithmetic, estimates what it cannot observe, and publishes its methods so that others can re-run them. |
| **Subscriber** | A person who holds an account with a trust network. |
| **Event log** | The permanent, append-only record of what happened, from which every position is computed (§3.1, A6). |
| **Estimate** | A figure computed from a published method where no direct record exists. |
| **Record** | A figure taken from an observation or an attestation. A record always beats an estimate (§5.1a). |
| **Onboarding** | The act of a person joining a trust network, which replaces estimates about them with records. |
| **The floor**, written `F` | The hours a day a network counts as the work of keeping a human being alive — sleeping, eating, defecating, keeping clean. The network sets the list and the hours (§7.5.1). |

**Read every rule below as a rule a trust network applies to its own subscribers and its own books.** Where a rule reaches across two networks, this section says so explicitly.

#### Networks keep separate books, and no book is ever added to another

> **Each trust network keeps its own event log. A network's books are never summed with another network's books, because there is nothing that would be summing them.**

Networks are **laboratories, not banks** (§5.3c). Their business is getting the numbers right. They frequently draw on the **same underlying evidence** — a haulier's logistics database, a published scientific paper, a government agency's survey — and it is in every network's interest when they do, because a method that catches a fault in one network's books catches it in the other's.

**What a subscriber sees is one network's best current approximation of the truth**, presented by something shaped like a payment-card application.

#### A transaction happens on exactly one network, and the seller chooses which

A seller decides which networks they will accept, the same way a shop today decides which card schemes it takes. *"We do not take Network B here"* is an ordinary sentence. **The seller's reasons are their own** — they may think B's floor is set too high or too low (§7.5.3), or that B's identity check is too weak.

**That preference is how networks compete for subscribers**, and it is the whole of the discipline on a network's settings. **The transaction is recorded on the accepted network and is absent from the other.**

**A network can also simply end.** If Network A collapses while Network B continues, the transactions recorded only in A are **forgotten**, unless B recovers A's database. Recovering it is the same act as a merge in which all of B's rules were kept (§5.3c).

---

<!-- tag: fnd-s5-1 -->
### 5.1 One account per person, and coverage that does not require consent

#### The two rules

> **1. Within a trust network, one verified human holds exactly one account.**
> **2. Participation is voluntary. Coverage is not.**

**Rule 1 is a rule each network applies to its own membership.** It is not a claim about a register of all humanity, and no such register exists. A network needs it because an account is where credit accrues and where the consumption gate `D ≤ ρ·C` is checked; two accounts for one person would check the gate twice against one life. **Resisting this is called Sybil resistance**, after the practice of one person presenting as many, and how a network achieves it is that network's design (§4, the verification ladder).

**Rule 2 means a network estimates the people it cannot see.** Leaving a non-participant out of the books entirely would produce a false record — wheat with no grower — so a network estimates both sides of their position:

| | Estimated from |
|---|---|
| **Debit** | The average for their demographic cohort, computed **excluding** registered subscribers. A public figure is estimated from publicly known holdings. |
| **Credit** | A cohort production model — occupation, region, known activity — computed **excluding** measured producers (§5.1b). |

> **A non-participant can neither draw on their estimated position nor be charged for it.** The estimate is a statement about material flows in the world. It is not a claim on the person, and the person has no claim from it.

#### Why one account per person survives the weakest possible technology

**The rule has to hold on the bottom rung of the verification ladder** (§4, level 1) — people writing in a notebook or a spreadsheet, all of whom know each other. That is where it looks most fragile, so that is where to test it.

**The only way it fails there is a pair of identical twins who deliberately engineer the confusion.** And the arithmetic already refuses it.

##### An example, with the numbers

Twins T1 and T2 each work **8 hours** a day. Their network counts **10 hours** a day as the work of staying alive (§6.1b).

| | T1 claims | T2 claims | Family total |
|---|---|---|---|
| **Honest** | 8 + 10 = **18 h/day** | 8 + 10 = **18 h/day** | **36 h/day** |
| **Faked** — T1 takes both twins' work | 16 + 10 = 26 h → **refused** | 0 + 10 = **10 h/day** | — |
| **Faked, at the most that is allowed** | 14 + 10 = **24 h/day** | 0 + 10 = **10 h/day** | **34 h/day** |

**IC-7 caps any account at 24 hours of activity per 24 hours** (conformance requirement 8). T1 cannot hold 16 worked hours plus a 10-hour floor, because that is 26 hours in a 24-hour day. The most T1 can claim is 14 worked hours.

> **The twins lose 2 hours a day by pretending to be one person — 730 hours a year.**

**T2 keeps accruing the floor either way**, because T2 is alive and is therefore doing the work of staying alive, whatever else they do or fail to do (§6.1b, §7.5.2).

**And there was nothing to win.** Twins sharing a household share the goods, so one twin holding the credit while the other holds the debit reaches the same family position as reporting honestly. **The fraud costs 730 hours a year and buys nothing.**

#### One person, two networks

**A person may hold an account with more than one trust network.** They are two subscriptions, not two lives, and they are not fraud: each network verified a real human and gave them one account, which is exactly what rule 1 requires.

**The two books are not reconciled, and they are not summed.** Each network computes that person's position from the evidence it holds, through its own settings. **Two networks with different settings will report different figures for the same day, and both figures are correct.**

##### An example, with the numbers

One person works **8 hours** on a Monday. They hold an account with each of two networks.

| | Network A | Network B |
|---|---|---|
| The floor `F` | **4 h/day** | **10 h/day** |
| Credit recorded for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |
| That network's own absolute maximum spread, 24 ÷ `F` | 24 ÷ 4 = **6.0×** | 24 ÷ 10 = **2.4×** |

**Read the last row as a wall, not as an expected outcome.** Reaching it takes 24 credited hours every day of a whole life. **A very hard working life reaches about 1.6× a life spent only staying alive** (§7.5.5).

**Neither network converted the other's figure.** Each read the same physical facts — eight hours worked, one human alive — through its own model. This is §6.4b, **comparison, never conversion**: a counterparty re-computes a claim through its own weighting model rather than importing a number.

**A purchase clears against one book only.** If the seller takes Network A, the gate `D ≤ ρ·C` is checked against A's figures and the event is recorded in A's log. B never sees it. **The same purchase might clear on one network and be refused on the other**, because the two use different floors and different values of ρ.

**Nothing about that is unresolved.** Where a network's records are partial, it publishes a coverage figure saying so (§5.1c), and where a subscriber leaves activity undisclosed, the network estimates it over the undisclosed residual and errs against them (§5.1d). **The gap is measured and declared. It is not hidden.**

---

<!-- tag: fnd-s5-1a -->
### 5.1a How an estimate becomes a record

**A position is realizable — able to act on what a person may consume — after two things are true.**

1. **The person holds a verified account** with the network (C6, identity).
2. **The estimate has been superseded by observation.** A record replaces an estimate; **an estimate may never replace a record.** This one-way rule is called **monotonicity**.

> **Assertion is not evidence.** Saying a figure is so does not make it a record.

#### The floor rule — the second one-way axis

**Monotonicity governs *basis*: how well a thing is known. The floor rule governs *extent*: how much of the world was looked at.**

> **A quantity computed over incomplete coverage is a floor, never a value.**

Under-recording can only understate a total, so a figure computed from a partial record is a **lower bound** on the true one, and better coverage moves it in one direction only: up. **A partial input downgrades a claim rather than invalidating it.** Where the evidence that would establish closure is missing, the figure is reported as a floor with the gap named (EventLog §7.4).

#### Records are annotated, never deleted

**A record is never purged and never edited.**

- A figure later found wrong is **contested** — a dated, attributed, appended note carrying its own provenance.
- A figure with a better replacement is **superseded** — the better record is added beside it.

**Falsehood is not prevented at the moment of writing. It is made permanent, traceable, and arithmetically exposed the moment any part of its extent is measured** (EventLog §7.2a, §8.2a). This is how a scientific literature handles a wrong result, and it is the only method that does not need an authority standing at the door deciding what may be written down.

---

<!-- tag: fnd-s5-1b -->
### 5.1b The residual rule — an average covers only what was not measured

#### The rule

**A producer nobody has measured still produced something, and the books have to say how much.** The answer is not the average producer's output. It is what is left over once the measured producers are subtracted.

> **estimate = (N − Y) ÷ Z**
>
> **N** — the independently known total for the whole extent. Agricultural statistics, trade data, a satellite survey.
> **Y** — what the measured producers actually recorded.
> **Z** — the count of producers still unmeasured.

#### Why it is the residual and not the whole population

**Compute the estimate over the whole population instead, and the rule creates adverse selection.** Producers who are better than average install instruments to prove it. Producers who are worse than average stay dark and are handed an average that their own absence pushed upward.

**Computed over the residual, the estimate gets *worse* for those who remain as good producers leave the pool.** Darkness stops paying, and stops paying more the longer it lasts.

#### Three conditions

1. **An independently known *N* must exist.** It does for major commodities and does not for everything.
2. **The count *Z* must be defensible.** Under-counting dark producers overstates each one's share.
3. ***N* and *Y* must measure the same quantity, over the same boundary, over the same window, with error bounds small enough that the difference between them is real.**

> ### 📦 WHY THE TWO NUMBERS MUST MATCH BEFORE YOU SUBTRACT
>
> **You may only subtract two numbers that measure the same thing.**
>
> `R = N − Y` looks like arithmetic. It is not arithmetic until four things are true.
>
> | Must match | The question it answers |
> |---|---|
> | **The quantity** | Do both numbers count the same stuff, in the same unit? |
> | **The boundary** | Do both numbers cover the same piece of the world? |
> | **The window** | Do both numbers cover the same stretch of time? |
> | **The error bounds** | Is the difference bigger than the doubt in the two numbers? |
>
> **If any one of these fails, `R` is not a residual.** It is two different measurements pushed together, and the gap is an artefact of the mismatch.
>
> #### An example, with the numbers
>
> A region reports its wheat.
>
> - **N** = 100,000 tonnes — a satellite survey of the whole region, for the 2026 year.
> - **Y** = 82,000 tonnes — recorded by the farms inside the network.
> - **R = 100,000 − 82,000 = 18,000 tonnes**, said to be grown by dark farms.
>
> Now check the four rows.
>
> | Check | What is actually true | Effect on R |
> |---|---|---|
> | Quantity | *N* is **harvested** grain. *Y* is grain **sold**. The farms kept 6,000 t for seed and feed. | R is **6,000 t too big** |
> | Boundary | The satellite covers the whole valley. The network's farms are in the **upper valley only**. | Not comparable at all |
> | Window | *N* is the **crop year**. *Y* is the **calendar year**. | Two months counted wrong |
> | Error bounds | The satellite figure is ±12%, which is **±12,000 t**. | R = 18,000 ± 12,000 |
>
> **Read the last row on its own.** The residual is 18,000 tonnes and the doubt is 12,000 tonnes, so the true residual is somewhere between **6,000 and 30,000 tonnes**. A five-fold range is not a finding.
>
> **Now fix the four rows.** Use sold grain for both. Use the upper valley for both. Use the crop year for both. Use a survey with ±3% error.
>
> - **N** = 88,000 t ± 3,000
> - **Y** = 82,000 t
> - **R = 6,000 t ± 3,000** — between 3,000 and 9,000 tonnes.
>
> **That is a residual.** It is smaller, it is honest, and it can be acted on.
>
> **Note what happened to the number.** The unchecked residual was 18,000 t and the checked one is 6,000 t. **Skipping this check made the dark pool look three times larger than it is**, and every dark producer's estimated share with it.

**Where the check happens.** Both *N* and *Y* already carry the fields this needs — extent, vintage and error bounds sit in the provenance block that every estimated record must have (EventLog §4.1a). EventLog §7.2a carries the check.

**What to publish when the check fails.** A mismatch downgrades the claim rather than invalidating it, exactly as the floor rule downgrades a partial count. **Report the residual as a lower bound, and state the boundary and window actually observed.** A residual is attributed to a named person only on attribution evidence, never on membership of a cohort (§5.1c).

#### The closure witness

***N* is a closure witness: a physical total measured outside the ledger and reconciled against the ledger's own sum.** It asserts nothing about anyone's honesty. Anyone holding the same instrument computes the same residual.

**The same reconciliation runs on any conserved quantity against any physical reservoir**, and §3.3's ambient-stock measurement is already such a reading — it has simply been used as an input to a weight rather than as a statement about coverage.

| Flow type | Closure witness | Authority required |
|---|---|---|
| account → account | **The counterparty.** A hand-off has two sides, so a one-sided omission dangles on the other party's record. The witness is a party with the opposite interest. | None |
| account → commons | **The reservoir stock.** Measured depletion or accumulation, minus the sum of recorded flows. | None — an instrument |
| a fully disjoint chain | **(N − Y) ÷ Z.** No shared edge and no shared parcel, so only an independent total can see it. | None — an instrument and a tally |

> ### 📦 THE ONE QUESTION THAT SORTS EVERY CHECK
>
> **Ask this about any check and you will know at once what it can find:**
>
> > **Does this check compare two things made on separate paths? Or does it compare a thing to itself?**
>
> A check that compares a thing to itself can find a **mistake**. It cannot find a **hole**. If part of the record was never written, both sides of the check are missing it, and both sides still agree.
>
> A check that compares two things made on separate paths can find a hole — **if** the second thing is able to say so (§4, expressiveness).
>
> #### An example, with the numbers
>
> A farm records 8 sacks in and 8 sacks out. Someone then deletes the last 2 sacks from **both** halves of the record.
>
> | Check | What it compares | Sum | Does it fire? |
> |---|---|---|---|
> | Mass balance on the log | The log against itself | 6 in − 6 out = **0** | ❌ No |
> | Origin closure on the log | The log against itself | every sack has a source | ❌ No |
> | Fate closure on the log | The log against itself | every sack has an end | ❌ No |
> | **The buyer's own receipt** | **A record made on a second path** | **buyer holds 8, farm says 6** | ✅ **Yes — short by 2** |
>
> **The first three checks are arithmetic over one log, and cutting a log never breaks arithmetic over that log**, because what is left is still balanced. Only the fourth check reaches outside.

#### Three further rules on the estimate

- **When *Z* is uncertain, under-count it.** Under-counting raises each dark producer's estimated share, which is the direction that prompts them to surface and prove otherwise. Over-counting dilutes the estimate and feeds **OP-24 (understatement drift)**. **The self-liquidating error is the safe one**, because nobody complains about being charged too little.
- **The estimate is continuous, not a single event.** As part of an extent becomes measured, *Y* rises, *Z* falls, the estimate shrinks to what remains, and the parts must reconcile against the coarser figure they came from (EventLog §7.2a). Grapes tallied as one region become one measured region and one still estimated. **This is also what catches a fabricated total, because a fabricator does not control which sub-extent is measured next.**
- **One method for *Z* that needs no headcount:** `Z ≥ (N − Y) ÷ capacity`, where *capacity* is the most one producer could physically make, bounded by hours in a day, by land, or by throughput. Using that minimum assigns each dark producer the most they plausibly could have made, which is the conservative direction. **This is a candidate method, not the method** — the capacity ceiling is itself a constant under §3.3a, though one bounded by physics.

**"Dark" means outside the network, not low-technology inside it.** Subscribing carries a transparency requirement: a good moving through the accounting carries records of where it came from. **Gathering data on non-participants, and helping a producer bring their supply chain into the record, are both credited work.**

---

<!-- tag: fnd-s5-1c -->
### 5.1c The residual is held, and charged to nobody

**A coverage gap is real material that really moved. The question is whose books it sits on.**

> **The residual is computed, published, and left unassigned. It is debit on no account. When a dark producer joins, their share is back-traced from records that already exist and assigned to them — the party who actually caused it. Until they join, they cannot transact inside the network at all.**

**Why this respects A4 (no externalities) rather than dodging it.** A4 requires every cost to be accounted to whoever caused it. Here the cost is **pending**, not written off: it is held as a computable claim waiting for a claimant. **Assigning it to subscribers who did not cause it would contradict §3.2**, which keeps consumption and pollution debit on its causer, and would be collective punishment of the kind §3.3 already rejects.

**Nothing extra has to be built for the back-trace.** Both records already exist and are kept for other reasons — the ambient-stock measurement of regional pollution (§3.3), and the independently known production total of §5.1b. **A producer's share is derivable from those the moment there is a producer to derive it for.**

**And the damage is not unpriced meanwhile.** Because a pollutant's weight floats with the **ambient stock** (§3.3), dark producers' emissions are already in the stock that everyone is weighed against. **A subscriber pays a rate that reflects the total damage, while being charged only for their own units.** That is proportionality, not collective punishment. **The residual is felt correctly without being allocated.**

**What the gap is instead of a debit: a published coverage figure.** *"These books cover 60% of this region's measured output."* That is the extent rule (EventLog §7.4) at regional scale, and it does real work: a counterparty re-computing under its own model discounts goods from a thinly covered region. **Coverage becomes a quality of a network's own output rather than a charge against its members.**

---

<!-- tag: fnd-s5-1d -->
### 5.1d The back-trace reaches birth, and it runs on both sides

**When a person joins, their position is reconstructed back to their birth** — not to the network's founding, and not to the joining date. A whole life.

That sounds punitive and is the opposite, for one reason that has to come first.

> **The back-trace is symmetric. Both sides are reconstructed — the debit and the credit.**

§5.1 already estimates non-participants on both sides, and §7.5 credits every living human for the hours they spend keeping themselves alive. **Everyone alive is doing that work, whatever else they do** (§7.5.2). **So a lifetime back-trace brings a lifetime of floor credit with it.**

#### An example, with the numbers

| | |
|---|---|
| Labour a median lifestyle commands, per year (§3.5) | **1,380 h** |
| Credit earned per year simply by being alive (§6.1b) | **3,650 h** |
| Ratio, credit to consumption | **2.6×** |

**A person joining at forty arrives with roughly 3,650 × 40 = 146,000 hours of estimated credit against roughly 1,380 × 40 = 55,200 hours of estimated consumption.**

> **Joining is a windfall for a median person.** That is not a coincidence — it is §5.2's adoption incentive, computed. **The people for whom a full back-trace is costly are those whose lifetime consumption genuinely exceeded their lifetime contribution.** That is correct targeting.

#### What the joining person supplies, and why they bother

**The estimate is the default. Evidence is voluntary and moves you off it.** A person supplies whatever narrows the estimate — where they were born, how long they lived in each place, which jobs they held, how far they commuted, which vehicles they owned and the mileage on them — and **accepts the cohort estimate for every period and activity they leave dark.** Nothing is compulsory.

**Evidence moves the figure in either direction, which is why people supply it.** Mileage records plus a vehicle model may show a hybrid driven below the commuter average, and the debit falls. The same records could raise it. **The estimate is not a verdict.**

**Details may arrive years later and the position re-derives.** No new machinery is needed: the position is derived from the log and never stored (A6), and §3.3 already recalculates every affected record when the science improves. **A life is refined the same way a cost constant is.** Supersession stays one-way (§5.1a) — an observation is never replaced by an estimate.

#### Two conditions, and without either this breaks

1. **An estimate for an undisclosed period is computed over the undisclosed residual, not over the whole population.** This is §5.1b's rule applied to periods and dimensions inside one life. Without it, a person who documents only their flattering years free-rides forever on an average their own silence inflates. With it, the pool of the undisclosed worsens as the well-documented leave it. **Selective disclosure is expected and is not an exploit, provided the residual rule holds.**
2. **An estimate errs against the estimated party, on both sides.** Debit is estimated at the unfavourable end and credit at the conservative end, so **supplying evidence always pays**, whichever direction the truth lies.

> **The floor is exempt and must stay exempt.** The floor is not an estimate. **It is credit for hours that were really spent**, attested by proof of life (§6.1b, §6.4b, §7.5.2). **So condition 2 never reaches subsistence, and a person who cannot document a life is not thereby impoverished by this rule.**

#### Why this does not contradict two rules it looks like it contradicts

| Looks like it breaks | Why it does not |
|---|---|
| **§5.1** — a non-participant is never charged for an estimated position | **Nothing is charged until they join, and joining is voluntary.** |
| **§3.3's transaction-time rule** — a revision never invalidates a completed act | **That rule protects acts the system gated at the time.** Acts before joining were never gated by any network, so no permission is being withdrawn. **A position is reconstructed; no verdict on past conduct is passed.** |

> ⚠️ **This raises the stakes on OP-22 (minimum audit disclosure), and that is the strongest objection to it.** A full back-trace is a life dossier — birthplace, every residence, employment history, commuting distance, vehicles owned, mileage. **Disclosure is voluntary, but the incentive runs toward disclosing**, so the arrangement puts steady pressure on people to assemble exactly the record a surveillance state would want. §5.3's split of public market data from private personal ledgers now has to hold across a lifetime. **Registered, not solved.**

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

> **🟢 (b) Privacy has a measured coverage cost, and the measured number says the trade-off is not close.** Privacy-preserving verification is dearer than open verification, and that direction is real. **What was wrong was the magnitude, and it was stated backwards.** `06-simulation/residual-unravelling/residual_unravelling.py` sweeps a producer's disclosure cost against a population whose median unit carries about **1.0** in debit. The dark pool still unravels to **0.1% at a cost of 0.40**; it collapses between **0.40 and 0.80**. Realistic disclosure costs sit near **0.002** (§4). **So the failure point is roughly 200 times higher than anything a working network would report**, and a privacy practice would have to be some two hundred times dearer than open recording before coverage suffered at all. **A network should still publish what its practice costs (§4, §5.3b); it does not have to trade coverage away to have one.** *Earlier drafts of this residue said the residual rule "stops unravelling" above 40%. It does not — at 40% it still reaches 0.1%, in 18 rounds rather than 13. Corrected 2026-08-24.*

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

**This narrows OP-24 rather than answering it.** OP-24's complaint was that a correction which worsens every subscriber's ledger has "no funder." The **funding** half dissolves — there was never a budget to find. The **incentive** half stands untouched, and v0.22 sharpened it: someone must still *want* the correction, and **§3.3a now shows the rival sector does not reliably want it either** — funding a correction is a public good among rivals, while getting one's own constant set generously is cheaper and private.

**Participants may pledge toward the network's own infrastructure** like any other work. Nothing special is needed for it.

#### The bootstrap: a network's founding is its own genesis entry

A trust network is the basis on which all accounting rests, so it cannot be paid by an accounting that does not exist yet. **The network is created first. Assigning its founders credit for creating it, once it is live, is the network's own decision, however it chooses to be governed.**

**This is not a special case, and it should not be written as one.** It is exactly the situation §6.2a already handles: a **genesis entry** admits a thing that existed before the ledger, at an estimated cost, crediting the estimator, superseded when better records appear. And §5.1d has just established that reconstructing a position from before the ledger existed is ordinary rather than exceptional.

> **A network's founding work is admitted the way any pre-ledger asset is admitted: as an estimated record, entered after the fact, open to supersession.** The bootstrap is a genesis entry pointed at the network itself.

**And Aequitas does not prescribe what that record must contain.** §1.2 applies: the principle is that **all costs must be accounted for**; how a particular network documents its own founding is praxis.

A network may write the founding up carefully. It may document it thinly. It may say *trust me* and offer nothing. **Or it may take no credit for setting itself up at all.** All four are permitted, and they are not equivalent — they differ in what they earn.

> **A network's traction rests on how it chooses to disclose this. It thrives or dies on its ability to deliver the truth, or the nearest to truth it can manage.**

**The founding record is the first thing about a network that anyone can check, and it is therefore a signal about all the rest.** A network vague about its own origin is asking to be trusted rather than checked — precisely what §5.3b says a laboratory does not do. **Nobody has to forbid a bad founding record. It simply does not attract anyone.**

**Three things bound the damage anyway, without anyone enforcing them.** **IC-7** caps founding credit at wall-clock hours × founders, so it cannot be arbitrarily large and the ceiling is checkable by anyone with a calendar. It is **publicly recorded**, so a later network re-computes it (OP-14). And because credit is **non-transferable** (A3) and consumption is ratio-gated, over-crediting founders buys only consumption room, **bounded by `24/F` like everyone else's** — *the disparity ceiling doing the backstop job it was argued to do, in a case nobody designed it for.*

**Taking no credit at all is a gift, not a gap.** Founders who decline to record their hours are donating them, and the gift economy is always available (§5.3c). *Minor imprecision worth recording rather than fixing: unclaimed founding hours understate the network's own cost, and the founders absorb that personally.*

<!-- tag: fnd-s5-3c -->
### 5.3c Federation, and where it is going

**Interoperating means agreeing on the algorithms, not on the answers.**

Two networks do not negotiate a person's balance. **Merging means agreeing every rule** — the floor `F`, ρ, the weighting model, and how a human is identified — after which the merged network computes one answer from one log. **Until they agree, each keeps its own book and neither is wrong** (§5.0, §6.4b). Consensus is at the **method** level, and reaching it is what makes a merge possible at all.

**So two networks that cannot confirm that two pseudonymous accounts belong to one person cannot merge.** A network requiring a face scan, a fingerprint and a voice check at every interaction cannot merge with one requiring only an RFID card scan. **Cross-registry uniqueness is a precondition of merging, not an open problem in the accounting.**

**A merge is not a special event.** When two networks federate and a person's two accounts become one, the adjustment to that person's ledger is **exactly as ordinary as the adjustment made whenever new data arrives.** §3.3 already recalculates every affected ledger when the science improves, and A6 derives the ledger rather than storing it, so **there is nothing to migrate and no new machinery to build.** Ledgers shift constantly. A merge is one more reason for one more shift.

> **The expected trajectory is convergence.** Networks that federate are expected to keep federating, and to **merge into a single network over time** — not to settle into permanently isolated regional systems.

**What convergence buys.** One ledger per person, so no double counting. No coverage gaps at the seams. No arbitrage between incompatible standards. **And the disparity ceiling holds globally rather than per compatible set.**

#### The escape is non-participation, and it never closes

An earlier draft of this section worried that convergence removes exit, because §5.3a and §5.3b discipline a network by letting members choose a different one.

**That mistook which exit matters.** The escape from Aequitas is not another network. **It is not participating at all.** The gift economy exists now, has always existed, and does not stop existing because an accounting system does. Nobody is enclosed by this.

**But exit is not the discipline, and it never was.** Leaving does not correct a bad method — it only removes the person who left. What corrects a method is **replication**, which is why §3.3a already requires *two unaffiliated replications* before a constant may re-weight history. That rule was written as an audit safeguard; it is better read as the norm it actually is.

#### Trust networks are laboratories, not banks

> **Their goal is truth, and their motive is consensus rather than competition.** A network whose methods let fraud through is **helped** by another network sharing the methods that catch it.

This is the correct frame and it changes what "monopoly" means here.

**And it does not rest on anyone being virtuous.** The reason a neighbour helps is structural: **if two networks interoperate, a bad method in one contaminates the books of the other.** Beta has a direct, selfish interest in Alpha's arithmetic being sound. That is the same logic as counterparty re-computation (OP-14), pointed at methods instead of claims.

*Honest note: laboratories also have replication crises and priority races. The claim here is not that researchers are nicer than bankers. It is that the payoff structure rewards shared correction, because contamination travels.*

#### Why a converged network is not the capture problem it looks like

**Concentration of information under convergence is deliberately out of scope, for four reasons.**

1. **It is hypothetical.** Convergence is a prediction, not an observation. Designing against a predicted end state is designing against a guess.
2. **The timeline and the technology are unknown.** If it happens, we do not know when, nor what will have been invented by then. A safeguard designed now for conditions we cannot describe is decoration.
3. **A monopoly earned by better methods is not the monopoly capitalism produces.** Capitalist monopolies come from anti-market practices — exclusion, capture, barriers — **not** from serving people better. A single Aequitas network would arrive because its methods are the best ones, and the best methods prevail by being *better*. **That is good service, not capture.**
4. **Data security and backups are a technology problem, not an economics one.** They are real, they matter, and they are **outside this project's scope.**

> **The strongest form of point 3, and the reason it holds: methods are published (§5.3b) and replicable. The monopoly is over *which method is used*, never over *who may propose one*.** There is no moat, because there is no exclusion — which is exactly what a capitalist monopoly has and this does not.
>
> **⚠️ The one thing worth watching, stated as a watch item rather than a defence:** a monopoly earned on merit can stop being meritorious and keep the position. **The guard is publication plus replication, not competition** — so if publication ever weakens (§5.3b) the merit argument weakens with it. **Those two sections are load-bearing for each other.**

<!-- tag: fnd-s5-3d -->
### 5.3d How a dispute resolves

§5.3c says trust networks are laboratories. **Ask the laboratory question: how does a dispute in science get resolved?**

**Replication. Published method. Dated records for priority. No adjudicator — there is no supreme court of physics. Both claims stay in the literature; nothing is withdrawn from the record. And often it is never resolved at all, only outlived.**

**Aequitas already has every one of those**, written for other reasons:

| Scientific practice | Already in Aequitas |
|---|---|
| Replication before a result is accepted | §3.3a — **two unaffiliated replications** before a constant may re-weight history |
| You can only dispute what you can inspect | §5.3b — networks publish numbers, methods and anonymised participant data |
| No adjudicating body | **A8.** No central authority exists to appeal to |
| Nothing is withdrawn; the rebuttal is appended | EventLog §8.2a **contest without replacement**, and §5.4 no erasure |
| Dated records settle priority | An append-only log with intervals |

#### Where the analogy breaks — and this is the part worth having

**Science can afford an unresolved dispute. An accounting system often cannot.**

A field can stay divided for thirty years and lose nothing. But a purchase either clears or it does not, **now**. You cannot tell a buyer that opinion is divided on whether their debit exceeds their room and to come back when the literature settles.

**The lab framing supplies the epistemics. It does not supply a decision procedure.** So the question is what decides *at transaction time*.

#### The answer is that most disputes never need deciding

Sorting them apart dissolves three of the four classes.

| Dispute about | How it resolves | Needs a verdict? |
|---|---|---|
| **The physical record** — did 70 g of wheat actually move? | **Arithmetic.** IC-1…IC-9 recompute it. **This is not a dispute; it is an error, and recomputation says whose.** | No |
| **The weighting model** — what does a tonne of CO₂ cost? | **Nobody has to accept anyone else's model.** A counterparty re-computes the shared physical record through **its own** weights and decides for itself — OP-14, *comparison never conversion*. Meanwhile §3.3a's replication and rival-sector audit move the field, slowly, the way science does. | **No — and this is the load the framing carries** |
| **An estimate for a dark actor** — what is *Z*? | Published method, replicable (§5.3b). The figure is a **floor** that improves (§5.1a), not a finding. Better evidence supersedes it. | No |
| **Fraud** — someone recorded events that never happened | **A finding of fact, and it needs one.** | **Yes** |

> **The insight is that a transaction never waits on a shared verdict.** Each side computes its own answer over the same physical record and decides whether to trade. **Disagreement about weights does not block commerce; it just means two parties price the same thing differently** — which is a fact about models, not a deadlock. **Comparison, never conversion, was always the dispute-resolution mechanism. It had simply never been named as one.**

#### The one residue, and where it goes

**Fraud is the class that needs an actual finding of fact**, and the analogy holds here too: **science is not purely self-correcting about fraud either.** Replication catches error; it does not catch a fabricated dataset that replicates because it was designed to. Science answers with **investigation and retraction, by an institution** — a university integrity office, a funder, a journal.

**Aequitas answers the same way, and §5.3 already said so:** *courts, small claims, contract law, and ordinary social pressure continue to exist and continue to handle fraud between people.* Per **§1.2**, how an implementer engages them is praxis, not foundations.

**What the accounting contributes is upstream of that.** IC-1…IC-9 make a fabricated record *arithmetically expensive* — a lie must balance mass, balance energy, close origin, close fate, and survive a counterparty's recomputation. **The remaining fraud is the fraud that is internally consistent, which is exactly OP-26's coverage question, answered by measurement against the world rather than by adjudication.**

#### What correction looks like — nothing is reversed

**Catching fraud is the trust network's task** (§5.3b), and what it does on finding some is the same thing it does on any other day.

> **The past transaction is not reversed. The fraudulent credits are negated, the ledger rebalances, and the person's ratio may now be too low to buy anything until they sell some of what they hold.**

**This is the transaction-time rule (§3.3), not a special fraud procedure.** The gate is evaluated when the transaction happens; a later correction changes *future* room and never the validity of a completed act. **Fraud correction is an ordinary re-weighting that happens to be large.**

**And reversal would be wrong, not merely difficult.** The goods moved. You cannot un-eat a sandwich. The counterparty acted on the record as it then stood, shed their property-debit legitimately under custody (§3.2), and was credited for work that really happened. **Unwinding the buyer's fraud would corrupt the seller's books to punish someone else's lie.**

**So the correction is arithmetic, and the consequence is automatic:**

1. The fake credit is negated. **C falls.**
2. **D does not.** They really did take the things.
3. `D ≤ ρ·C` now fails. **They cannot make discretionary purchases.**
4. **Selling restores the ratio** — property debit is dischargeable on transfer (§3.2), so handing goods on lowers *D*.

**Nobody imposes a penalty. The books are simply correct, and being correct is the penalty.** Essentials are untouched throughout — §7.5.4's backstop reaches non-essentials only, and it does so for the fraudster on exactly the terms it does for anyone mis-measured.

**Three consequences worth stating, because they are not obvious.**

- **Consumption debit cannot be sold off.** If what they took was eaten, burned or emitted, selling does not help — consumption debit is permanent (§3.2). **They are over their ratio and cannot trade their way out.**
- **But there is no bankruptcy, and there does not need to be, because there is time.** Credit accrues to everyone alive at the self-care floor, whatever their standing (§7.5). So *C* grows again on its own, and the ratio recovers. **The recovery period is the faked credit divided by the rate they now accrue** — which means **the sentence is exactly the size of the fraud, measured in time, and nobody sets it.** A person who faked ten years of credit works off roughly ten years. *That is a proportionate, self-expiring, un-appealable consequence produced by arithmetic rather than by judgement.*
- **The influence axis corrects the same way.** IC-8 caps cumulative pledges at lifetime earned credit. Negating credit can put a person retroactively over that cap; the pledges themselves are permanent and the work they summoned was really done, so nothing unwinds. **They simply cannot pledge again until credit recovers.** Same mechanism, no second procedure.

> **⚠️ One real load stays, and it is not a weighting dispute.** The pledge-reserve claims process (§6.4c) asks whether a *particular past task caused a particular later harm*. Where a physical trace exists, the trace decides and it is arithmetic. **Where it does not, this is a contested finding of fact with no analogue in the list above**, and it is the genuine adjudication load flagged when the reserve was folded. **It routes to existing recourse like fraud does. Registered; not solved here.**

<!-- tag: fnd-s5-4 -->
### 5.4 There is entry, and there is no exit

**Entry is onboarding** (§5.2) — the act of turning an estimate into a record. It is voluntary, and it is usually to the joiner's advantage (§5.1d).

**There is no matching act on the way out.**

> **Once records of a person exist, they are never destroyed. They are only appended to — including after that person's death.**

#### Two things that are easy to confuse

| | Available? |
|---|---|
| **Ceasing to participate** — stop transacting, stop holding an account, live in the gift economy (§5.3c) | **Always.** Nobody is enclosed. |
| **Erasure** — removing the record that you existed and what you did | **Never.** |

**And erasure was never available even before you joined.** §5.1 says participation is voluntary but **coverage is not**: a non-participant already carries an estimated position on both sides. There is no state of not-being-in-the-books to return to.

> **You can stop transacting. You cannot stop having existed.**

#### Why permanence is a requirement, not a policy

This is not a rule imposed for tidiness. **It is what makes the rest of the system work.**

§3.3 recalculates every affected ledger when the science improves. §5.1d reconstructs a life back to birth when someone onboards. **Neither is possible over records that were deleted.** A6 derives the ledger from an append-only log; **a log that can be truncated is not a log.** Permanence is the precondition of recomputation, and recomputation is the engine of fecundity.

The same logic already governs corrections: a challenged record is **annotated, never removed** (EventLog §8.2a). **§5.4 is that rule applied to a whole person rather than a single entry.**

#### Death

A person's record **closes but persists**, and three things follow.

- **It stays re-weighable.** §3.3 does not stop at the grave. A dead person's recorded debit still moves when the science behind it improves — which is correct, because the figure describes what happened, and what happened has not changed.
- **Credit does not transfer.** A3: credit is non-transferable, and death is not an exception. **Nothing is inherited on the credit side.**
- **Property debit transfers with the things.** Custody follows possession (§3.2), so whoever takes the goods takes their material debit, exactly as in any other hand-off. **Consumption and pollution debit does not move** — it stays permanently with the person who caused it, undischarged, for good. That is not a punishment reaching past death; it is the record continuing to say who did what.

> **On the right to be forgotten — out of scope, and here is why that is not a dodge.** Erasure law binds an implementer in a jurisdiction, not a theory of cost (§1.2). It was checked anyway, because a flag had been raised: the right is **not absolute**, and three of [GDPR Article 17](https://gdpr-info.eu/art-17-gdpr/)'s five exemptions apply — legal obligation (accounting retention already outlives erasure requests), **archiving and scientific or statistical research, which carries no time limit**, and legal claims. The live difficulty is that exemptions are applied case-by-case rather than as a standing position. **All of it is a matter for whoever operates a network, under whichever law they operate.** Full note: [`02-research/Law_gdpr-right-to-erasure_v0.1.md`](../02-research/Law_gdpr-right-to-erasure_v0.1.md).
>
> **One consequence follows regardless.** Because deletion is unavailable, **publicity is the only privacy control that exists** — §5.3a for persons, §5.3b for institutions. There is no falling back on erasure, which raises what those two sections have to carry.
>
> **One consequence follows immediately.** Because a record can never be removed, **publicity is the only privacy control that exists** — §5.3a for persons, §5.3b for institutions. There is no deletion to fall back on, which raises what those two sections have to carry.

<!-- tag: fnd-s5-5 -->
### 5.5 Parallel implementation — trading across the money boundary

**Aequitas has to be usable by someone who still uses money, as an alternative that does not exclude them.** §5.2 assumes this and does not work it out, and so does the adoption reading in [`Aequitas_Strategy_v0.6.md`](Aequitas_Strategy_v0.6.md) §5. This section works it out.

**Every participant, for years, will have most of their counterparties outside.** A design that only works once everyone is inside cannot get anyone inside.

#### The two directions, and both are deliberately costly

> **Selling *into* Aequitas — a good made with money-bought inputs.**
> The good is **dark until it is sold into Aequitas**, because its inputs never passed through a hand-off here. At that hand-off the maker either **onboards it properly**, with the origin-chain records §5.1b requires, **or applies a pre-approved template** that assigns a debit-cost immediately so the transaction clears without waiting for a reconstruction.
> **The maker spent money making it and receives none. They lose money, and that is the disincentive.**

> **Selling *out* of Aequitas — for money.**
> Permitted. **The debit stays with the seller.** No participant took the goods on, so the ledger does not lighten (§3.2), and the seller's own ratio absorbs it.
> **To the network the seller made a gift** (§5.3c), and **the network does not acknowledge the money changing hands at all.**
> **That is also the disincentive.**

**Neither direction is forbidden, and both are dearer than trading inside.** This is the same shape as every other answer here: *price the costly path rather than forbidding it at a door somebody has to guard.*

#### Why money is invisible, and why that is not a special rule

**A1's corollary already says it.** Stocks, bonds, currencies and tokens are not matter or energy, so they *"never appear on any ledger."* **A payment in money is therefore not an event.** The goods moved and the ledger records that; the money moved and the ledger cannot see it.

> **So no cross-boundary rule exists or is needed.** Money is invisible because it is not physical; the good left the records, so §3.2 applies; the fate closes as §3.6 already closes it, with the last recorded holder having consumed what no one else would take. **The ordinary rules cover the boundary without being told about it.**

#### The template

The only new object, and it is a **cache rather than a mechanism**: §5.1b's dark-production estimate, computed once per class of good, published, and applied at the point of sale.

**Two rules it carries, both inherited:**

1. **It errs against the seller.** §5.1b's conservative-count rule. **A template must be dearer than a real record**, or onboarding properly never pays and the template becomes the preferred route.
2. **It is published, with its method and its vintage** (§5.3b). A template nobody can re-derive is an authority assertion, which is the thing this system exists to stop needing.

> **⚠️ The template list is a capture surface.** Whoever sets it sets the entry price for every dark good in that class, and setting it low lets money-economy goods undercut the instrumented producer who paid to measure their own supply chain. **This is OP-24 at the boundary and it inherits OP-24's answer** (§3.3a): the natural auditor is the **rival producer**, materially harmed by cheap undocumented goods, who will fund the replication. **Work it with OP-10 and OP-24, not separately.**

#### What the boundary lets through, and what it does not

**Goods cross. Standing does not.**

Follow a wealthy person paying a hundred workers **in money** to make goods and selling them into Aequitas. **The workers are credited their own hours** — credit records who was responsible, and responsibility is a fact about a person (A2, A3, and Ellerman-imputation under A1). **The financier worked none of those hours and is credited nothing.** They are out the money and hold no credit.

> **There is no channel from money to credit, at any scale.** You cannot buy hours: a credit is a record that a specific person spent a specific hour, and IC-7 caps every account at 24 hours a day regardless of who paid. **The boundary is permeable to goods and impermeable to standing.**

#### Extraction, and why it exhausts itself

**The attack worth taking seriously.** Aequitas states a thing's cost (A5 (cost, not price)) and the money economy states a price, so anything whose market price exceeds its Aequitas debit-cost is an arbitrage: buy inputs inside cheaply, sell outputs outside at a profit, and disregard a ledger you do not care about.

**It self-limits, in proportion to the extraction.** Buying inside **takes on** the property debit. Selling outside **never discharges it**. So `D` grows with every unit extracted while `C` grows only with the extractor's own hours, capped at 24 a day.

> **`D ≤ ρ·C` fails, and the extractor can no longer acquire the inputs they were draining. Their own gate shuts them out, and it shuts faster the harder they pull.** Nobody enforces it and nobody has to notice.

#### What is not settled

#### Repeat-shell organisations — closed in v0.22

**The attack.** Buy goods inside. Sell them out for money. The debit stays, so the gate `D ≤ ρ·C` shuts. **For a person that is the end of it**, because one verified human has one account (§5.1) and a person cannot be closed and re-opened. **A co-operative is not a person, so the obvious next move is to close it and start another with a clean gate.**

**Two outside economists raised this on 2026-08-24** and both said the register under-rated it. Their reason is worth keeping: **the trades most exposed to the money boundary are the ones normally organised as businesses** — haulage, warehousing, shops, building work, farm co-operatives. **The gap was not at the edge of adoption. It was on the main road.**

**It is closed by §3.2c, and no new rule was needed.** An organisation's debit is at all times its members' debit, divided by hours worked. **Closing the organisation moves nothing, because nothing was held anywhere else.**

| Round | Debit the shell takes | Where it sits | Does a new shell reset it? |
|---|---|---|---|
| 1 | 24,000 h | 2,400 h on each of 10 members | **No** |
| 2 | 24,000 h | 4,800 h on each | **No** |
| 10 | 24,000 h | **24,000 h on each — their own gates now bind** | **No** |

**So the self-limit §5.5 claims for a person holds for an organisation too, at the same rate and for the same reason.** The extractor's own gate shuts, and it shuts faster the harder they pull.

> **What stays open.** Whether a person can hide behind a **fake or borrowed membership list** — claiming hours for people who did not work them, or leaving their own name off. That is a verification question, not an accounting one, and it routes to **C6 (identity)** and the verification ladder (§4), where it belongs. **The accounting no longer has a hole; the identity layer still has to do its job.**

**Nothing above is new theory.** Money's invisibility is A1, the dark estimate is §5.1b and EventLog §12.3a, the retained debit is §3.2, the gift is §5.3c, and the fate closure is §3.6. **The contribution of this section is that the pieces are now assembled in one place and the boundary is shown to need no rule of its own.** Full paper and stress test: `00-strategy/OP-27_parallel_implementation.md`.

---

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
- **Its magnitude is a network choice with a bound at each end, not a free dial.** **Which activities count — sleeping, eating, defecating, keeping clean — and how many hours each takes is set by each trust network** (§7.5.1). **The value must be high enough that essentials stay affordable and low enough that the gate still rations what is genuinely short** (§7.5.3, worked with numbers there). ≈10 h is a defensible physiological figure and ~8 h of sleep is not arbitrary, but **the number is an economic setting as much as a physiological one**, and it is disciplined like any weighting (§3.3a). Generosity here is product differentiation, not a rule anyone imposes (A8) — and it **cannot be exported**: a counterparty re-computes a pledge's backing through its own model (§6.4a), so an over-generous floor is discounted by whoever trades with it, never forced on them.
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

<!-- tag: fnd-s6-2b-barn -->
> ### 📦 WHY THE BARN IS NOT IN THE BEEF — IN PLAIN WORDS
>
> **This is the most-attacked rule in the document, so here is the reply with the numbers in it.**
>
> **The objection.** A barn shelters the cattle. If the barn's cost is not in the beef, the beef looks cheaper than it really was. **That sounds like the accounting is hiding something.**
>
> **The reply is one sentence: the beef did not build the barn.** Under A1 (materialism of cost) only people act, so a cost attaches to the people who caused it. **A thing causes nothing.** The barn's cost sits on the people who built and hold it, and it stays there.
>
> #### An example, with the numbers
>
> A barn costs **20,000 hours** to build and lasts **20 years**. The farm produces **2,000 kg** of beef a year — **40,000 kg** over the barn's life.
>
> | | Hours |
> |---|---|
> | What the critic says beef should carry: 20,000 h ÷ 40,000 kg | **0.5 h/kg** |
> | What beef actually carries from the barn | **0.0 h/kg** |
>
> **So where did the 20,000 hours go?** Onto the barn, split by holding time (above). One operator who holds it the whole 20 years carries **20,000 hours**, permanently.
>
> **And that is not a light thing to carry.** The gate is `D ≤ ρ·C`. At **ρ = 1.2**, carrying 20,000 hours of debit needs `20,000 ÷ 1.2 =` **16,667 hours** of credit standing behind it. Every living person accrues about **3,650 hours a year** from self-care alone (§6.1b), so the barn eats **4.6 years of one person's entire credit accrual.**
>
> > **That is why nobody builds a barn they do not need.**
>
> #### Now try it the other way, and watch what breaks
>
> Push the barn onto the beef and two things happen:
>
> | | |
> |---|---|
> | Beef goes from **12.0** to **12.5 h/kg** | a **4.2%** rise |
> | 20,000 hours move off **one operator** and onto about **40,000 buyers** | about **0.5 h each** |
>
> **The buyers did not build the barn, do not hold it, and never got a say in whether it went up.** The one party who decided is the one party the cost stops constraining. **The rule that looked like it was hiding a cost is the rule that keeps the cost pointed at the person who chose it.**
>
> #### The sharper case — a cost discovered years later
>
> A co-op makes a household cleaner. It sells **5,000,000 bottles** over eight years at **0.20 h/bottle**. Then its wastewater is found to be heating a nearby fishery. Stopping the harm and repairing the fishery costs **400,000 hours**.
>
> **If capital rode the product**, §3.3 would re-weigh every affected record, **including bottles already bought**:
>
> | | |
> |---|---|
> | 400,000 h ÷ 5,000,000 bottles | **+0.08 h** on every bottle ever sold |
> | Each past bottle | 0.20 → **0.28 h**, a **40%** rise |
> | A household that bought 200 bottles | **+16 hours of debit**, for a decision a factory made |
>
> **And the builder would know that in advance.** Every hour of capital they ever incur lands on people who already bought and people who have not bought yet. **The cheapest possible siting decision is always someone else's problem.**
>
> **Under the rule as written**, the 400,000 hours sit on the co-op's holders. At ρ = 1.2 they need **333,333 hours** of credit behind it; a 50-person co-op accruing 3,650 h/yr each earns **182,500 h/yr**, so the repair absorbs **about 1.8 years of the whole co-op's credit accrual.** **Not one buyer's ledger moves.**
>
> *(The heating of the fishery was **always** the factory's under §3.2b, and never rode the bottle either. The abatement plant is capital and stays under this section. **Two different debits, both pointed at the factory, neither pointed at a buyer.**)*
>
> > **The incentive to examine the factory design *before* building it exists only in the second version.**

**The honest residue, stated plainly rather than in a clause.** Two producers of the same good — one with a 20,000-hour barn, one with a 2,000-hour shed — publish **the same per-kg debit-cost**. A buyer comparing debit-costs cannot tell them apart, because a unit's debit-cost answers *"what did this unit consume?"* and never *"what does this producer's whole method cost?"*

> **What disciplines the barn is the builder's own gate, not the price tag.** The capital-heavy producer carries the creation-cost on their own ledger, so their `D` is higher and their debit-room tighter for as long as they hold the asset — the 4.6-years-of-credit figure above.
>
> **This is the same argument §7.2 already makes about pollution**, where the debit was likewise moved off the product and onto the producer, and where the document argues the producer-side penalty is **stronger** than a consumer-mediated one because it does not depend on anyone noticing. **The argument transfers unchanged, and it is registered rather than assumed** (Objections **B8**).

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

Because pledges are **public** (§5.3), pledged-vs-speculative is not a label a producer can privately misapply to recruit or to shed risk — a worker reads it off the pledge ledger, including how much has been pledged toward the run and how much of it has actually been drawn against by work done so far. *(Pledges do not get withdrawn — they are permanent and non-revocable, §6.4; what a worker watches is the pledged total accumulating or stalling, never a pledge being taken back.)*

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

**Trust networks design, administer, and audit the specific verification method for each activity** — A8 open variance, the same capture surface as the always-creditable-activity list (A8), and disciplined the same way: **a counterparty re-computes a claim's realization and backing through its *own* weighting model** (A6, EventLog §3), so a network with lax verification cannot *export* the credit it issues — whoever trades with its members discounts it. This is **comparison, never conversion**: nothing is exchanged between models; each party re-reads the shared physical log through its own weighting. Converting a balance from one model into another would be an exchange rate between credit-standards — a medium of exchange, which A3 and the circulation-failure analysis (§7.6) forbid.

> **⚠️ This anti-arbitrage guard depends on OP-22 (audit disclosure).** Re-computing a pledge's backing requires seeing *what backs it*, but personal ledgers are private (§5.3). The guard therefore needs "this pledge is backed by *X* hours realized under weighting model *M*" to be provable in zero-knowledge. The market check on lax or over-generous networks is only as real as that disclosure mechanism — **which is OP-22.**

<!-- tag: fnd-s6-4c -->
### 6.4c The contingent reserve — how over-pledging incentivises hazardous work

Because pledges are permanent, a task can attract **more pledged hours than it costs**. The surplus is **not** a payment to the doer and is **not** consumable — treating it as spendable would be a scarcity price (profit), which A5 forbids, and would re-open a channel for concentrating consumption advantage. Instead the surplus becomes a **contingent reserve**: earmarked, non-spendable debit-room that activates **only against a verified future cost causally traceable to the task** — the doer's later injury or illness, site remediation that resurfaces, third-party harm. This is *any* task-caused cost, not only the doer's.

- **Pledge shares split pro-rata by hours *on the task*** (a doer's share of a pledge = their task-hours ÷ total task-hours), so the cover reaches whoever actually did *this* work — not, via a whole-co-op-history denominator, whoever has been a member longest (which would be the P4 seniority-skim).
- **Causation is decided by the physical-trace test** (§3.4a / OP-17): a claim draws the reserve only if the harm left a trace linking it to the task; diffuse or latent harm with no individual trace is handled by a **cohort/actuarial convention** (the §5.1b residual rule), never an open claim.
- **The reserve is a buffer, not a shield: overflow reverts to the causer.** Once a reserve is exhausted, residual task-caused debit falls back on the doer/cooperative under the ordinary rules (§3.2 possession, §3.7 remediation). Without this, third-party/environmental cover would licence carelessness; with it, the care incentive survives.
- **An abandoned task's pledges are burned** — the pledger's finite budget is spent for nothing, which is what disciplines frivolous pledging. Unused reserve on a completed task likewise never becomes consumable and never reverts; it lapses. **This resolves C5's reversion question in the negative: nothing reverts.**

**What it buys.** Onerousness has two halves. This mechanism gives the *hazardous* half a demand-gated incentive **without** wage premium, rate-scaling, or a rating authority: society de-risks the toxic-cleanup worker exactly to the extent it pledges for the work, and the danger internalises as the size of the reserve the task must attract. It leaves the *tedium/indignity* half open (dull but safe work generates no causal tail, so no reserve, no incentive) — that remainder stays with OP-16. Because the reserve only ever *cancels* a task-caused cost and never *adds* spendable room, it creates no consumption advantage. Sim: `06-simulation/pledge-reserve/pledge_reserve.py` (clears the job at coverage ≈ cover-the-tail; overflow-reverts preserves care; integrity rests on physical-trace causation).

<!-- tag: fnd-s6-4d -->
### 6.4d Who holds the demand lever

**Terms used here.** The **demand lever** is whatever decides how much of a thing gets made. A **pledge** is a request for work, backed 1:1 by hours the pledger has already earned, spent once from a lifetime budget (§6.4).

#### The objection this answers

> *Cost says what a thing took. It does not rank two people who both want the last one. Without a price, what decides how much gets made and who gets it?*

This is the standard reply from economics, and it rests on three assumptions. **All three are false in a concentrated market.**

| The assumption | What is actually the case |
|---|---|
| **Scarcity is a physical fact the price reports.** | Much scarcity is produced. Supply is held back to hold the number up. |
| **Demand is a fact the price reports.** | Demand is manufactured, at scale. That is what the whole advertising industry is for. |
| **A price is therefore an honest reading of what people want.** | In a concentrated market the same firms set supply *and* work on demand. **The price partly reports its own producer.** |

**This is not a new claim, and it is not a left-wing one.** Fernand Braudel's economic history separates two layers: **market towns**, where many small sellers meet and price settles from below, and above them a small number of large operators who set prices instead of taking them. [Manuel DeLanda's summary](https://nettime.org/Lists-Archives/nettime-l-9610/msg00025.html) of that layer is direct: capitalism *"has always engaged in anti-competitive practices, manipulating demand and supply in a variety of ways."* **He calls the upper layer an *anti*-market, and so does this project.** See `02-research/DeLanda_markets-antimarkets_v0.2.md`.

> **So the objection assumes the price is a clean instrument. It is not. Aequitas is not replacing an honest demand signal with a worse one. It is replacing a signal that is partly written by the seller.**

#### What pledges change

**A pledge cannot be manufactured by a seller.** It is backed by hours the pledger worked, it is spent once, and it is public (§5.3). A firm cannot advertise a pledge into existence, because a pledge costs the pledger something real that only they can spend.

**And the lever is distributed far more evenly, which is measurable.**

| System | How concentrated the demand lever is |
|---|---|
| Money | Top-tail wealth reaches about **10⁶ ×** the median (SCF 2022 + Forbes, §7.5) |
| Aequitas | Pledging power cannot exceed **24 ÷ F ≈ 2.4 ×** at a 10-hour floor — and that is an **absolute maximum nobody reaches.** A very hard working life reaches about **1.6 ×** (§7.5.5) |

**That is the argument in one line: the demand lever moves from a distribution with no upper bound to one bounded at about 2.4 ×.** Every living person holds some, because self-care credits everyone (§6.1b).

#### Two examples, with the numbers

**Example 1 — a person wants their grocer to stock radicchio.**

They tell their device. Under presets they set earlier, it pledges **0.5 h** toward getting radicchio to that grocer.

| | |
|---|---|
| Work to put one extra box on the shelf — pick, load, the truck's extra time, unload, stack | **≈ 2 h** |
| Pledges needed | 2 ÷ 0.5 = **4 people** |
| Cost to one person, against a budget growing ~5,450 h a year | **≈ 0.009% of one year** |

**Four wishes fill one box.** A haulier reads the pledge, adds a box, and the grocer accepts it. **Nobody planned this and no price moved.**

**Example 2 — an artist posts a street-art photograph.**

**5,000 people like it.** Their apps convert likes to pledges under presets they chose.

| | |
|---|---|
| Pledged debit-room raised | 5,000 × 0.1 h = **500 h** |
| The artist's next work — materials and travel | **300 h** |
| Surplus | **200 h** |

**The surplus does not become spendable.** Under §6.4c it becomes an earmarked contingent reserve, and unused reserve lapses. **Nobody is paid a bonus for being liked.**

> **⚠️ A design point that matters, found while working these numbers.** A **flat rate per like** does not discipline anything. At 0.1 h a like, a person earning 5,450 h a year could give **54,500 likes a year** before their budget bound. **The sound preset is a share of a budget:** *this like costs (my art budget) ÷ (likes I give this period)*. Allocate 50 h a year and give 500 likes, and each is 0.1 h; give 5,000 likes and each is 0.01 h. **It normalises itself.** A network offering the flat preset is offering a broken one.

#### Two checks against existing rules

- **Does example 2 let feedback buy credit?** **No.** §6.4b forbids *credit* from realising on feedback, which would make likes a currency (OP-8). **A pledge is not credit.** It grants debit-room and is backed 1:1 by hours the pledger already earned. Auto-routing your own pledging budget is the same permitted move §6.4 already describes for self-care.
- **Does it create a popularity contest?** **Yes, and that is the known open problem OP-6 (feedback mechanics), not a new one.** Whoever is already liked attracts the most pledges. The bound is that every pledge costs a real person a real hour from a finite budget, and the ceiling above holds. **Registered, not solved.**

#### What this does **not** answer

> **Two people, one radicchio. Pledges say how many get grown. They do not say who gets the last one.**

That is a distribution question and it has a separate answer: a queue, a lottery, or pledge-priority, decided at the point of distribution (§7.5, §3.4a). **Cost states what a thing took. Who receives a physically scarce output is a different question, and this document deliberately does not settle it.**

**Full statement of the reply, including the Mises and Hayek arguments:** `00-strategy/OP-9_calculation_reply.md`.

<!-- tag: fnd-s6-5 -->
### 6.5 Attribution without intellectual property

There are no patents and no exclusion. Ideas replicate freely; **meme tracing** gives feedback-weighted recognition to originators as ideas spread.

**Art is not a commodity, and intellectual property is the antithesis of treating it as anything else.** Exclusion rights exist to let a holder extract profit from reproduction. With no profit in exchange (A5 (cost, not price)), the machinery has nothing to protect and no reason to exist.

**The right standard for attribution is *no worse than today*, not *perfect*.** Buy a painting from a gallery now and there is no video of its making; you trust the seller, and at person-to-person scale the stakes are low enough that this is fine. Provenance only becomes fraught in the capitalized art market, where licensing and reproduction are the revenue — which is precisely the layer Aequitas removes. **Aequitas does not need to solve a problem that the current world also has not solved and does not much suffer from.**

*A useful illustration, though not a general mechanism:* someone can copy an MP3 and claim it, but is unlikely to perform it live. When the incentive is to share the work rather than to sell copies, a recording functions as an advertisement for the performance. This holds well for music and poorly for writing, visual art, software, and research — so treat it as a good example rather than a rule.

<!-- tag: fnd-s6-5a -->
### 6.5a Not all work is capturable — and the system does not require it to be

A2 and A4 describe how flows are accounted **when they are recorded**. Neither claims that all human activity must be recorded, and the difference matters, because a critic will read A1 (materialism of cost) as demanding total surveillance.

Memes are the clean case. People spend real time editing images and writing captions; the results propagate through conversation, entertainment, and provocation. **Tracing who shared what to whom in order to assign work-credit is neither possible nor desirable**, and a trust network that proposed it would be laughed out of the room — which is A8's open variance working exactly as intended.

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
**A5 (cost, not price) means there is no profit in exchange** — a thing's figure is what it consumed, and nothing may be added to it. Embodied-material debit releases on transfer; self-work nets to zero while held (§3.2). **No rent, no rental income, no property speculation, no compounding capital.** Not banned — structurally impossible. *Ellerman's route reaches the same conclusion independently: only people act, so only people can be responsible, so capital cannot claim a residual.*

**The exploitative employer is structurally hollowed out**. The wage-extraction employer has no mechanism to exist: credit is non-transferable, so there are **no wages** to pay (A3 (non-fungibility)); a thing's figure is what it consumed and nothing may be added, so there is **no surplus to appropriate** (A5 (cost, not price)); and a team's debit is shared **by hours worked, not by rank** (§6.2b), so a supervisor **cannot dump risk or cost onto subordinates**. Workers are credited by the *system* for their hours, not paid by a boss. **What survives is coordination** — organizing a process, directing what gets made, controlling access to desirable projects — and that residual power is real: it is the **coordinator-class problem (P4 (coordinator class))**, the live blocker, not the extractive employer this system already forecloses.

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

#### 7.5.1 What the floor is

**Terms used in this section.**

| Term | What it means |
|---|---|
| **The floor**, written `F` | The hours a day a trust network counts as the work of keeping a human being alive. |
| **Trust network** | The organisation that keeps the books and sets `F` for its own subscribers (§5.0). |
| **ρ** ("rho") | The network's debit tolerance. The multiplier in the consumption gate `D ≤ ρ·C` (§3.5). |
| **`C`** | A person's cumulative credit — the hours of their life the books have recorded as work. |
| **`D`** | A person's cumulative debit — the material and energy the books have recorded against them. |

> **The floor is credit for time a person spends on the activities their trust network counts as essential to staying alive.**

Those activities are **sleeping, eating, defecating, and keeping oneself clean.** A network may count more, or fewer, or hold them to shorter durations. **The list and the hours are the network's to set, and networks will differ.**

**That is why floors differ, and the differences are not arbitrary.** One network counts eight hours of sleep and lands near 10 h/day. Another accepts the argument that four hours of sleep suffices and lands near 6 h/day. A third counts sleep alone and lands near 8 h/day. **A fourth counts only the hours a body cannot avoid and lands near 2 h/day.**

**This is partly a question of opinion and partly a question of fact.** People disagree about how much sleep a human needs. **They are also disagreeing about a number that decides whether the network's economy is stable** — see §7.5.3.

---

#### 7.5.2 The floor follows from the axioms. It is not an allowance

**The floor is not a grant, a payment, a benefit, or an income.** Nothing is issued to anybody. **It is the ordinary result of applying two rules the system already has.**

| Step | The rule | Where |
|---|---|---|
| 1 | **Credit is a record that a person spent time on work.** Not effort, not output — time spent. | **A2** (time as measure), §6 |
| 2 | **Maintaining a living human body is work.** Doing it for somebody else is work, so doing it for your own body is the same work. | §6.1, §6.1b |
| 3 | Therefore **a living human accrues credit for the hours spent maintaining themselves.** | §6.1b |
| 4 | **Every human is in the books whether they participate or not**, and a verified living person demonstrably did that maintaining. | **A7**, §6.4b (proof of life) |

> **A person who does nothing else is still doing that work, and the books record it because it happened.**

**The alternative would break A2.** Handing a person credit they did not earn would be credit for no time worked. **That is exactly the "abstract, issued quantity" A1 forbids**, and it is why the floor could never have been written as an allowance.

##### What this rules out saying

| Do not say | Why it is wrong |
|---|---|
| *"a basic income"* | An income is paid by somebody to somebody. **Nothing is paid, and there is no payer.** |
| *"a safety net"*, *"the dole"*, *"an entitlement"* | All three describe a claim on other people. **Credit is a record of the holder's own time and is a claim on nobody** (A3). |
| *"the system supports people who cannot work"* | **Everyone alive is working, by this definition.** The floor does not distinguish between the busy and the idle, because keeping yourself alive takes the same hours either way. |

**The praxis varies. The derivation does not.** A network chooses which activities count and how many hours each takes. **No network chooses whether staying alive is work, because A2 already decided that.**

---

#### 7.5.3 The floor's value is an economic setting, with a bound at each end

**Setting `F` is not an act of generosity.** It is the network deciding how much consumption room the act of being alive creates, and the number has to work.

> **Set it too low and people cannot afford what they need. Set it too high and the books stop rationing anything. Finding the value that balances the economy is the network's job.**

##### The lower bound, with the numbers

**A year of essentials commands some quantity of other people's labour.** Call it `E`. The floor must be large enough that a person doing nothing else can still take that much.

`ρ · F · 365 ≥ E`

**Worked, with `E` = 700 h/year** *(illustrative — the real figure is the network's to measure against its own basket)* **and ρ = 1.2:**

| | |
|---|---|
| Minimum floor | 700 ÷ (1.2 × 365) = **1.6 h/day** |
| At `F` = 2 h/day, room per year | 1.2 × 2 × 365 = **876 h** — covers 700 h of essentials |
| At `F` = 1 h/day, room per year | 1.2 × 1 × 365 = **438 h** — **short by 262 h** |

**A network at `F` = 1 h/day has subscribers who cannot afford to eat. That network fails.**

##### The upper bound, with the numbers

**Compare the floor's room against what a year of ordinary life actually commands.** A median lifestyle commands about **1,380 hours** of other people's labour a year (§3.5).

| Floor | Room from the floor alone, `ρ·F·365` at ρ = 1.2 | As a multiple of a median lifestyle |
|---|---|---|
| 2 h/day | 876 h | **0.63×** |
| 4 h/day | 1,752 h | **1.27×** |
| 8 h/day | 3,504 h | **2.54×** |
| 10 h/day | 4,380 h | **3.17×** |

**At `F` = 10 and ρ = 1.2, being alive entitles a person to over three times a median material standard before they do a single hour of anything else.**

> **The gate then stops binding on almost everybody.** `D ≤ ρ·C` still holds, but it is not the thing deciding who gets what. **Where the economy can actually deliver that much, this is abundance and it is the intended end state** (§3.5, Q6). **Where it cannot, physical shortage is decided at the point of distribution instead — by a queue or a lottery** (§3.4a, §6.4d) — **and the accounting has stopped doing the work it was set up to do.**

##### What the project owes here

**Aequitas does not set `F` and must not** (A8). **What this project owes is a demonstration that a stable value exists** — that for a given economy there is a band of `F` and ρ inside which essentials are affordable and the ledger still rations what is genuinely short.

> **⚠️ Owed: a simulation showing the stable band, and its width.** Registered with **OP-4 (debit tolerance)**, which already holds the floor's magnitude and the ceiling's denominator. **Nothing in this section claims the band has been found.**

---

#### 7.5.4 Essentials are always affordable, by arithmetic first

**Two separate things make essentials reachable, and they are usually confused.**

> **1. The floor's own arithmetic. A person's credit for staying alive is sized to cover what staying alive costs.** This is the ordinary case and it covers everybody, however little else they do. Nobody is assessed, nobody applies, and nobody decides they qualify.

> **2. A backstop for the abnormal case. A restriction arising from a person's standing reaches non-essentials only.**

**The second exists because of measurement error, not because of poverty.** A producer over-assigned for years would suffer real harm before §3.3 corrected the record — the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal). **The backstop caps that exposure at restricted non-essential consumption for a period, followed by correction.** It applies on the same terms to somebody found to have committed fraud (§5.3d).

**The floor does not require anybody to spend it on essentials.** A person may put their room toward anything they like. **The guarantee is that they can afford what they need, not that they must buy it.**

> **The floor is therefore not only a welfare provision. It is the error tolerance of the whole accounting.**

**None of this is a conformance requirement, and it must not be written as one.** Whether essentials are actually affordable in a given network depends on the value it sets for `F`, the value it sets for ρ, and what its economy can physically deliver — **so it is a result a network achieves, not a property an implementation has.** Setting the two dials so that it comes true is the network's job (§7.5.3). *(A conformance row saying otherwise existed from v0.18 to v0.24 and was deleted; see `Aequitas_Conformance_v0.3.md` §4.)*


---

#### 7.5.5 The disparity ceiling — an absolute maximum, not an expected spread

> **Inside any one trust network's books, the ratio between the largest and the smallest lifetime credit cannot exceed `24 ÷ F`.**

**Why the arithmetic gives that.** IC-7 caps any account at **24 hours of activity per 24 hours** (conformance requirement 8). Every living subscriber accrues at least `F`. **Highest ÷ lowest = 24 ÷ F.** At `F` = 10 h/day that is **2.4**.

##### It is an extreme, and nobody reaches it

**`24 ÷ F` requires one person to hold 24 credited hours every single day of their life, from birth to death, without exception.** That means `24 − F` hours of work a day, 7 days a week, 365 days a year, for eighty years.

**No ordinary life comes near it.** An astronaut on an unceasing duty schedule is the shape of thing that approaches it, and only while the schedule lasts.

###### An example, with the numbers

**A network with `F` = 10 h/day. Four whole lives, 80 years each.**

| | How the credit accrues | Lifetime credit | Against a floor-only life |
|---|---|---|---|
| **L — lives only** | 10 h/day, birth to death | 10 × 365 × 80 = **292,000 h** | **1.00×** |
| **M — the arithmetic maximum** | 24 h/day, birth to death | 24 × 365 × 80 = **700,800 h** | **2.400×** |
| **N — maximum, but childhood not credited** | 10 h/day to age 18, then 24 h/day | 65,700 + 543,120 = **608,820 h** | **2.085×** |
| **P — a very hard working life** | 12 h work/day, 300 days a year, ages 20 to 70 | 362,500 + 109,500 = **472,000 h** | **1.616×** |

**Person P's working years, shown in full:** 300 working days × (12 + 10) = 6,600 h, plus 65 rest days × 10 = 650 h, giving **7,250 h a year** for 50 years. The 30 years outside that run at the floor: 30 × 3,650 = **109,500 h**.

> **The figure to quote is not 2.4×. It is that a very hard working life reaches about 1.6× a life spent only staying alive, and that 2.4× is the wall nobody gets to.**

##### The ceiling depends on two network choices, not one

**Person N shows the second one.** An infant learning to speak is spending time on something. **A network may count all of that non-floor time as learning, or none of it, or some.** §6.1 already says learning is work, and **A8 already leaves the list of always-creditable activities to the network.**

**The choice moves the reachable maximum:**

| The network's choice on childhood | Highest reachable lifetime ratio |
|---|---|
| Credit a child's learning time in full | **2.400×** — the arithmetic ceiling is reachable |
| Credit none of it | **2.085×** — nobody can reach the stated ceiling, ever |

> **A network that does not credit childhood has a stated ceiling of 2.4× that no subscriber can reach, and its most industrious subscriber falls short of it for a reason that has nothing to do with how hard they worked.**

**This is a second dial on the same number, and it was not written down before.** It belongs with `F` under **OP-4 (debit tolerance)** and with the always-creditable list under **A8**.

##### Four conditions on the bound

1. **The value of `F`.** The ceiling **is** `24 ÷ F`, so a network with a 2 h floor states a 12× ceiling. **The result is only as tight as floors are generous.** `F` is a network choice (§6.1b, A8).
2. **The network's treatment of childhood**, per the table above.
3. **No fraud manufactures hours.** IC-7 caps a day at 24 hours, but collusive hand-offs could still inflate gross hours (**OP-1**, service → influence). The bound assumes that channel is controlled.
4. **It is a statement about one network's books.** Nothing else.

##### What condition 4 replaces, and why

**Through v0.22 this section carried a fifth condition claiming the bound held *"across any set of networks compatible enough to interoperate"*, on the ground that compatible networks *"arrive at the same ledger for the same person."* Both halves are withdrawn** (author ruling, 2026-08-25).

- **Networks do not trade with each other, and no book is ever added to another book** (§5.0). There was no object for a cross-network bound to describe.
- **Compatible networks do not arrive at the same figure, deliberately.** §6.4b is **comparison, never conversion**: each party re-reads the shared physical record through its own model. Two networks with different floors report different credit for the same day, and both are right.
- **A merge requires consensus on every rule, identity included** (§5.3c, §5.0). Networks that cannot confirm two pseudonymous accounts belong to one person cannot merge.

> **The comparison against money is unchanged, and it is a fair one.** Money's spread reaches about **10⁶ ×** the median **within one country's own statistics** (SCF 2022 and Forbes). The bound above is the spread within one network's own books. **Two sets of books, compared like for like.**

*(Note for review: old conditions 2 and 3 — floor-shopping arrested by counterparty re-computation, and that guard's dependency on **OP-22** — are narrowed by the ruling rather than removed. Under §5.0 a seller chooses which network a transaction lands on, so a network with an implausible floor loses sellers. What remains of the OP-22 dependency is proving a **pledge's** backing across a model boundary, §6.4b. **Flagged for the author rather than settled here.**)*

---

#### 7.5.6 Why hoarding does not beat the bound

**Credit `C` and debit `D` are cumulative running tallies derived from the event log** (A6), and **credit is never spent** — a purchase adds to `D` and never subtracts from `C`, because credit is not a currency (A3).

**So `D ≤ ρ·C` is a ratio re-checked at every event, not a balance drawn down.** A person who consumes nothing for decades and then spends heavily can only bring forward their own allowance, which is bounded by `ρ·C`. **There is no stored lump to release.**

**At equal age, two people's cumulative credits stand in a ratio of at most `24 ÷ F`, so their cumulative consumption does too.** The only spread beyond it is age — time lived, not class. **A 60-year maximum worker against a 20-year floor-only person is 3 × 2.40 = 7.20×**, confirmed in the simulator (`06-simulation/statera/`).

---

#### 7.5.7 What the simulations found

> **Formally stated, simulated, and stress-tested.** The formal statement and a plain-language explainer are in `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`. The adversarial pass of 2026-08-14 answered all three attacks — **Methuselah** (§7.5.6 above), **dynasty and household** (a household is a co-op; its dwelling debit splits per occupant by dwelling time, children included, so the bound is per person and inheritance dilutes it, §6.2b), and **collector** (holdings raise your own debit, so a hoard bounds itself).

`06-simulation/disparity-ceiling/disparity_ceiling_sim.py`, N = 200,000, gate `D ≤ ρ·C`, credit in `[F, 24]` h/day, 7 self-tests green:

- **The `24 ÷ F` ceiling is exact and does not move with ρ**, because ρ cancels in `ρ·24 ÷ ρ·F`. It also does not move with the weighting model, so **the headline result does not depend on OP-10.** On the same synthetic population, money's spread is 14× on income and roughly 700–950× on wealth.
- **ρ behaves like a prime rate.** A ρ can be chosen so that aggregate demand matches productive capacity, and it moves sensibly under shocks. Against the median-lifestyle anchor the baseline clears at **ρ\* ≈ 1.2**, a −30% capacity disaster tightens it to ~0.68, growth loosens it to ~2.2, and a +25% pollution re-weighting tightens it to ~1.0. *(Absolute values are illustrative and depend on OP-10; the directions are robust.)*
- **Efficiency, not extra labour, is what reaches abundance.** The same population is mildly short under the wasteful US production method and reaches everyone's full desired standard under German, Japanese or Spanish efficiency (Q6). **The binding constraint is physical throughput** (§3.5).
- **The ceiling is fraud-invariant.** IC-7 bounds every account, honest or not, so the most a fraudster reaches is `ρ·24` — the honest maximum. **Fraud fills the band and cannot create an outlier beyond it.**

> **What the simulations have not yet done, and it is now the more important of the two:** find the **stable band of `F` and ρ** described in §7.5.3. The existing runs take `F` as given. **Owed, with OP-4.**

---

#### 7.5.8 The real-distribution comparison

`06-simulation/scenario-suite/q4_locked_ledgers.py` applies the bound to real US and world distributions under the **material-only** rule (A1's corollary), asking what fraction of people would sit past a permanent lockout — non-essential consumption held at the floor for life because their sustained footprint exceeds `ρ · 24 h/day`, the most any human can earn.

- **Stripping the financial layer collapses the top of the distribution by about 1,000×.** Money wealth reaches ~10⁶× the median, but material **consumption** only ~670× (Oxfam billionaire personal footprints), because consuming physically takes bounded time. **The spread the bound has to cap is far smaller than the monetary one.**
- **Only a thin slice is locked.** Material-only, about **0.1–2%** of Americans are permanently locked, ρ-dependent, around 0.5% at ρ = 1.5. **These are the ultra-consumers, not the merely rich**, and fully divesting material property does not save them, because consumption debit is permanent (§3.2). **Meanwhile about two-thirds sit below their cohort average and would gain room by joining** (§5.2).

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

<!-- tag: fnd-pointers -->
## 8. Where the rest of the project lives

**This document states the system. Four things that used to sit here now live where they belong.**

| What | Where | Why it moved |
|---|---|---|
| **The conformance requirements** — what must be true for an implementation to *be* Aequitas | [`Aequitas_Conformance_v0.3.md`](Aequitas_Conformance_v0.3.md) | It is written for implementers, and this document is written for anyone. |
| **Every open problem and every answered objection** | [`Aequitas_Objections_v0.23.md`](Aequitas_Objections_v0.23.md) | The register is the record. A ranked summary here only went stale. |
| **How adoption plausibly starts** | [`Aequitas_Strategy_v0.6.md`](Aequitas_Strategy_v0.6.md) §5 | It is a reading of the historical record, not a statement of the system. |
| **The version-by-version change history** | [`Aequitas_Foundations_CHANGELOG.md`](Aequitas_Foundations_CHANGELOG.md) | Already pointed at from the header. |

---

*End of v0.25.*
