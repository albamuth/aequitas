<!-- tag: fnd-aequitas-foundations-and-long-term -->
# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.28
> **Date:** 2026-08-27
> **Status:** Working foundations. **Restructured on 2026-08-27**: the old §4, §5 and §6 all described work a trust network does, and only §5 said so. **They are now one section, §4. Consequences moved from §7 to §5, and the pointer table from §8 to §6.**
> **Primary audience of the first paper:** technologists and implementers.
> **Companion:** [`Aequitas_Conformance_v0.6.md`](Aequitas_Conformance_v0.6.md) — what must be true for an implementation to *be* Aequitas.
> **Companion:** [`Aequitas_Objections_v0.23.md`](Aequitas_Objections_v0.23.md) — the objections register.
> **Companion:** [`Aequitas_EventLog_v0.10.md`](Aequitas_EventLog_v0.10.md) — the data model.
> **Version history is kept separately and is not published**, so this document carries only what is currently true.
>
> **⚠️ Section numbers changed in v0.28.** The old §4, §5 and §6 all described work a trust network does, and only §5 said so. **They are now one §4. Consequences moved from §7 to §5, and the pointer table from §8 to §6.** The section titles below say what each part covers; **the full old-to-new map is in the change history, which is held locally.**

---

<!-- tag: fnd-toc -->
## Contents

- [0. The One-Sentence Theory](#0-the-onesentence-theory)
- [1. Axioms](#1-axioms)
  - [A1 (materialism of cost)](#a1-materialism-of-cost)
  - [A2 (time as measure)](#a2-time-as-measure)
  - [A3 (non-fungibility)](#a3-nonfungibility)
  - [A4 (no externalities)](#a4-no-externalities)
  - [A5 (cost, not price)](#a5-cost-not-price)
  - [A6 (derived, not stored)](#a6-derived-not-stored)
  - [A7 (universal accounting)](#a7-universal-accounting)
  - [A8 (no governing body)](#a8-no-governing-body)
  - [1.1 Named conventions](#11-named-conventions)
  - [1.2 What Aequitas is, and what is therefore out of scope](#12-what-aequitas-is-and-what-is-therefore-out-of-scope)
- [2. Conformance to the Three Criteria](#2-conformance-to-the-three-criteria)
- [3. The Ledger Model](#3-the-ledger-model)
  - [3.1 Structure — an event log, not a balance](#31-structure-an-event-log-not-a-balance)
  - [3.2 The two kinds of debit — and the two components of property debit](#32-the-two-kinds-of-debit-and-the-two-components-of-property-debit)
  - [3.2a Debit is a vector, collapsed on demand](#32a-debit-is-a-vector-collapsed-on-demand)
  - [3.2b Only property transfers — pollution and transport never do](#32b-only-property-transfers-pollution-and-transport-never-do)
  - [3.2c An organisation's debit is its members' debit](#32c-an-organisations-debit-is-its-members-debit)
  - [3.3 Retroactive re-weighting](#33-retroactive-reweighting)
  - [3.3a Who checks the science — the problem, and whose problem it is](#33a-who-checks-the-science-the-problem-and-whose-problem-it-is)
  - [3.4 Resolution is opportunistic](#34-resolution-is-opportunistic)
  - [3.4a Joint production — dividing one process's debit among several outputs](#34a-joint-production-dividing-one-processs-debit-among-several-outputs)
  - [3.5 The books never balance — and must not](#35-the-books-never-balance-and-must-not)
  - [3.6 End-of-life, recycling, and product-as-pollution](#36-endoflife-recycling-and-productaspollution)
  - [3.7 Land is not owned; a building carries a remediation debt](#37-land-is-not-owned-a-building-carries-a-remediation-debt)
- [4. What a trust network does](#4-what-a-trust-network-does)
  - [4.0 What a trust network is, and what this section covers](#40-what-a-trust-network-is-and-what-this-section-covers)
  - [4.1 It gives each person one account](#41-it-gives-each-person-one-account)
  - [4.2 It decides what counts as evidence, and publishes it](#42-it-decides-what-counts-as-evidence-and-publishes-it)
  - [4.3 It checks claims, and chooses how hard to check](#43-it-checks-claims-and-chooses-how-hard-to-check)
  - [4.4 It estimates what it cannot see, and says how much that is](#44-it-estimates-what-it-cannot-see-and-says-how-much-that-is)
  - [4.5 It credits work](#45-it-credits-work)
  - [4.6 It carries what people want made](#46-it-carries-what-people-want-made)
  - [4.7 It publishes its own workings, and settles disputes](#47-it-publishes-its-own-workings-and-settles-disputes)
  - [4.8 It takes people in, it merges with other networks, and it can end](#48-it-takes-people-in-it-merges-with-other-networks-and-it-can-end)
- [5. Consequences](#5-consequences)
  - [5.1 Capitalism cannot function](#51-capitalism-cannot-function)
  - [5.2 Exploitation and pollution self-penalize](#52-exploitation-and-pollution-selfpenalize)
  - [5.3 Regulators invert into services](#53-regulators-invert-into-services)
  - [5.4 Taxation is unnecessary](#54-taxation-is-unnecessary)
  - [5.5 The basic-needs floor](#55-the-basicneeds-floor)
  - [5.6 Why the alternative-economy graveyard does not apply](#56-why-the-alternativeeconomy-graveyard-does-not-apply)
- [6. Where the rest of the project lives](#6-where-the-rest-of-the-project-lives)

---

<!-- tag: fnd-s0 -->
## 0. The One-Sentence Theory

> **Aequitas is a universal accounting of material flows.** Every credit and every debit is a record of matter and energy moving through the world, attributable to the people who caused the movement. **Cost is nothing other than this.**

**Aequitas is a theory of cost. It is not a theory of value, and it does not need to be.**

This distinction is load-bearing. Every previous attempt at objective accounting — Odum's emergy, Technocracy's energy certificates, the labour theory of value — claimed to have found what things are *worth*, and every one was refuted on the same ground: **supply-side only, ignores demand.** The refutation is a stock move and takes one sentence.

Aequitas makes the narrower and far more defensible claim. **Cost is what a thing takes from the world; it is physical, and we can measure it. Value is what someone thinks it is worth; it is not physical, and we do not attempt to measure it.** Value enters the system as *feedback and pledges* (§4.5), never as an accounting quantity.

> **On the credit side, the substance is *time* — and time, not effort**. A credit records *time a human spent*, and the conceptual leap Aequitas asks of a reader is to see time itself as the finite thing being spent — like money is "spent" today, except that time is possessed by every person in exactly equal measure (24 hours a day) and can be neither hoarded, lent, nor transferred (A3 (non-fungibility)). This is the deep reason Aequitas produces a **bounded** inequality where money produces an unbounded one: money accumulates without limit; time structurally cannot — you get 24 hours a day and no more, ever, and you cannot buy anyone else's. Effort, hazard, and skill are real differences between workers, but they resolve as *material* costs (A2 (time as measure)), never as a time-multiplier. **Because the unit of account is an equally-distributed, non-transferable resource, the *engine* of a bounded inequality is the arithmetic itself, not any rule that polices it.** *(The exact bound, though, is a **conditional** result, and it is an **absolute maximum rather than an expected spread**. It depends on the value a network sets for its floor, on whether that network credits a child's learning time, and on fraud not manufacturing hours; see §5.5.5. **A very hard working life reaches about 1.6×, not 2.4×.** Earlier drafts overstated it as a flat arithmetic certainty.)*

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

> **Corollary — financial instruments carry no debit**. Stocks, bonds, currencies, crypto-tokens, options, and other financial claims are exactly the "abstract, issued, or fiat quantity" A1 excludes: they are not matter or energy. **They therefore never appear on any ledger.** What *is* accounted is the **material** they are claims *upon* — a factory, land, a building — and that material's debit sits on whoever physically **holds or operates** it (embodied-material dischargeable on transfer; creation-cost holding-time-split, §3.2/§4.5), never on the paper. This is not a loophole for hidden wealth: owning a factory through shares does not move its material debit to *nobody* — it stays on the factory's operators, by holding time. The consequence is measured in the scenario suite: entering the previously-wealthy **material-only** collapses the observed inequality tail by ~three orders of magnitude versus their paper net worth (§5.5, `06-simulation/scenario-suite/q4_locked_ledgers.py`), because financial wealth was never material and physical consumption is bounded by time.

<!-- tag: fnd-a2 -->
### A2 (time as measure)

**Time is only a yardstick for summarizing flows, never a substance with value — so labour is never rate-scaled, and differences between workers resolve as material costs, never as a multiplier.**

Time is a convenient universal yardstick for summarizing flows — a local second is a local second, measurable identically everywhere. But an hour is not *itself* value. Differences between workers resolve as *material* differences, never as a multiplier:

- **Hard labor** → extra caloric intake is recorded as real food-production cost.
- **Hazardous labor** → health harms discovered later are retroactively injected as debit into the products and services that caused them.
- **Skilled labor** → **training is credited work in its own right, and its cost is discharged at the time of training.** Nothing flows downstream. See §4.5.

> **A2 is also the reason the co-product allocation problem has an answer (§3.4a).** Because every physical quantity in the ledger — a kilogram, a joule, a tonne of CO₂ — is a proxy for hours to produce or to mitigate, **the system never has to choose between mass and energy as *the* unit of account.** The universal is the denominator, not the carrier. This is a stronger consequence of A2 than was recognised when it was written.

<!-- tag: fnd-a3 -->
### A3 (non-fungibility)

**Every credit and debit is a unique, non-exchangeable record of a specific event — credits can never be transferred, traded, gambled, lent, or stolen; only debit moves, and only by transferring the thing it is attached to.**

A3 is not a design preference. Under A1 it is a **consequence**: credit records who was responsible, responsibility is a fact about a person, and facts about people do not change hands. It also does three defensive jobs at once — see §5.6.

<!-- tag: fnd-a4 -->
### A4 (no externalities)

**Every consequence of an activity is accounted to whoever caused it, including consequences discovered decades later — there is no "outside" of the accounting.**

> **Note on the wording, v0.21.** Through v0.20 this read *"every consequence is **priced into it**."* That phrasing said a consequence rides the *activity's output*, which is not what the system does and not what any section implements: **§3.2b** keeps pollution permanently on its causer rather than on the goods, **§4.4** holds an unattributed residual on nobody at all, and **§4.5** refuses to let a cost regress upstream. **A4 requires that every cost land on *a* ledger, never that it land on the *product's* ledger.** The substance is unchanged; the same defect in A5 is repaired directly below, and it is the same defect.

<!-- tag: fnd-a5 -->
### A5 (cost, not price)

**A thing's cost is the current best estimate of what was materially consumed to make it. Nothing is added to that figure, and nothing enters it that the thing did not consume.**

**Whoever takes a thing, or receives a service, takes on a debit equal to that figure. There is no profit in exchange — only debit discharged and debit acquired.**

Competition happens on **quality, artfulness, and efficiency**, never on margin.

**The boundary is physical fate: what was used up making the thing is in its cost; what survived the process is not** (§4.5). A durable asset holds its own creation-cost, carried by its holders (§4.5), and **that cost never enters the things the asset was used to make.**

**This is not an exemption from A4 (no externalities).** Every cost still lands on a ledger. It is **A1 (materialism of cost)'s imputation rule applied to cost**: a cost attaches to whoever caused it, and **a thing causes nothing** — only people act. Charging a beef buyer for the barn is the same error as charging a ring buyer for the miner's tailings, which §3.2b already refuses. **Worked numbers: §4.5.**

**The estimate is never final.** Better measurement re-weighs it, and every record made under it, automatically (A6 (derived, not stored), §3.3). **A cost is a dated reading, not a verdict.**

> **⚠️ What this replaced, and why — v0.21.** Through v0.20, A5 read *"the **price** of anything is its true, current-best-estimate material cost."* An outside economist review put that sentence against §4.5 and found a contradiction: if a barn's 20,000 hours never enter beef's debit-cost, then **beef's "price" is not beef's cost, and A5 fails.**
>
> **The ruling was not the error. A5's wording was**, in three separate ways:
>
> 1. **It said "price."** Nothing here has a price. Things carry a **debit-cost**, and it moves.
> 2. **It never said what counts as a cost *of the thing*.** The capital-vs-consumption boundary existed in §4.5 and was never lifted into the axiom, so the axiom read as contradicting it.
> 3. **"True" reads as final**, which fights §3.3 and A6.
>
> **The critic's step is to assume the beef caused the barn.** Under A1 only people act, so a cost cannot attach to an output that did not cause it. **§3.2b forbids that flow downstream and §4.5 forbids it upstream; capital is the third face of one rule already written down twice.** A5, which located cost on the *thing*, was the sentence out of step. **No mechanism moved in this repair.** Full argument: `00-strategy/A5_repair_PLAN_v0.1.md`, register **B8**.

<!-- tag: fnd-a6 -->
### A6 (derived, not stored)

**Balances are never authoritative — the event log is; any account's standing is a pure function of its events times the current scientific cost-weighting model.**

Improve the science, and all history re-weighs automatically (§3.3).

<!-- tag: fnd-a7 -->
### A7 (universal accounting)

**Every human is accounted for whether or not they participate, with credit and debit estimated symmetrically for everyone (§4.1) — but a position becomes realizable only on a verified account.**

- **Accounted** — every human carries an estimated credit *and* debit position. A factual claim about material flows, not a claim on or by the person.
- **Realizable** — an estimated position acts on a person's debit ceiling only once they hold a **verified account** and their estimates have been superseded by observed, attested records.

Non-participants are fully represented in the books and can draw nothing from them. **Participation is the act of converting an estimate into a record.**

**Corollary — credit is issuable retroactively.** When a person joins, their prior real contributions enter the record at the dates they occurred.

> **Design constraint — estimation error is not symmetric.** Over-estimating debit consumes nothing. Over-estimating credit inflates real consumption ceilings on the basis of guessed production. Symmetric in *form*, asymmetric in *consequence* — which is why realization is gated on observation.

<!-- tag: fnd-a8 -->
### A8 (no governing body)

**No organization that grows up around Aequitas may acquire authority over its core rules — governance is a protocol property, not an institution.**

Rules evolve as **immutable core + open variance**: everything below the core may differ from one trust network to the next, and those differences compete in public.

**What may vary.** A trust network may run a different weighting model, a different self-care floor, a different privacy practice, a different verification rung. **It must publish what it runs, and anyone else must be able to re-compute its claims** (§4.7, §4.2).

**What may not vary.** The axioms above, and the conformance requirements in [`Aequitas_Conformance_v0.6.md`](Aequitas_Conformance_v0.6.md).

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
> **One place in this document depends on that.** §4.8 expects networks to **federate and merge toward a single network over time**, not to settle into separate regional systems.
>
> *(Through v0.22 a second example stood here: that the `24 ÷ F` bound held across every interoperating network. **Struck in v0.23.** Networks do not trade with each other and no book is ever added to another, so the bound describes one network's own books — §4.0 and §5.5.5.)*
>
> **Where this document does mean somewhere geographic**, it is describing a *physical* thing handed to a *physical* person: a butcher's queue for a scarce cut (§3.4a, §5.5), or a village served by one generator (§3.2b). **A scarce object has to be given out somewhere. That is a fact about the object, not about the network.**
>
> *Renamed in v0.22. This axiom was called "local governance" from v0.1 to v0.21, where "local" meant "not imposed from a centre". **Several outside reviewers read it as "small and geographic" and built objections on that reading.** The word was doing two jobs and only one was intended, so it was removed rather than explained.*

<!-- tag: fnd-s1-1 -->
### 1.1 Named conventions

Some quantities the system needs are **not** physical facts. Where that is true, it is stated here rather than hidden in an implementation detail. **A convention that is declared is not an ad-hoc rule; a convention that is disguised as a measurement is.**

| Quantity | Status | Why it is not a measurement |
|---|---|---|
| **Split of a team's credit across its members** | ✅ **Not a convention — dissolved (A2)** | Credit is *time worked* (§4.5), so each member is credited **their own hours** — the "welder caused 40% of the bridge" number is never needed. Credit is not a share of output. **OP-18's team-credit half was a mis-statement; A2 already answers it.** *(A residual remains — apportioning a jointly-*caused debit* across a team — but that is a debit-attribution question, minor, sibling to OP-25 (illicit dumping).)* |
| **Split of *labour* across co-products** | ✅ **Convention with a measurable basis — rides the material split** | One labour process yields several products (farmer's hours → beef + hide); the hours leave no per-product trace, so a convention is required (physical-trace test). The declared convention: **labour rides the same physical split §3.4a already measures for the process's materials** (mass/deposition for cattle, cracking-energy for a refinery). Adds *no new lever* — it piggybacks on the rival-audited material θ. Changes no one's credit; it is a debit-side cost figure only. **OP-18(α) — closed 2026-08-05.** |
| **Split of an asset's residual creation-cost across its holders** | ✅ **Convention with a measurable basis — holding-time** | Apportioning a fixed creation-cost is a choice, but **holding-duration is a physical trace**, so the convention is measured, not invented: share = holder's holding-time ÷ total holding-time over the asset's life (§4.5). Respects the dummy and symmetry axioms an even split fails. |

> **Two rows are absent, for two different reasons.**
>
> **A *"split of a joint process's debit across its co-products"* is not a free convention, and not a pure measurement either.** The process did physically divide the inputs, and that division is measurable — but reading it requires choosing an instrument, a period, and a sub-process boundary, and two honest choices can give different figures. **It is a choice that measurement constrains.** What Aequitas fixes is the obligations on that choice: measure at the facility for the period described, compute per dimension before collapsing, publish the method, and never let demand or yield enter. **The method itself belongs to the industry, under §1.2.** See §3.4a. *(Stated as a pure measurement until v0.21; corrected in v0.22 after outside review.)*
>
> **And *shared-overhead attribution to co-products* has nothing to attribute** — under §4.5 all capital and overhead accrues to the **asset**, never to the co-products (the barn stays on the operator; hide and beef carry only their own consumables). See `00-strategy/OP-17_coproduct_allocation.md` and `00-strategy/OP-23_capital_and_pollution.md`.

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

**So human-facing transparency is not a foundational question.** It is the §4.7 dial, and §4.7 is right to leave it to the network. The same reasoning applies to storage technology, jurisdiction, corporate form, and compliance posture.

#### What this rules out of scope, explicitly

| Out of scope | Where it belongs |
|---|---|
| Data-protection and erasure law | The implementer, under its own jurisdiction. Research: `02-research/Law_gdpr-right-to-erasure_v0.1.md` |
| Data security, backups, key management | A technology problem (§4.8) |
| Corporate or legal form of a trust network | The implementer |
| Which cryptography, which database, which protocol | The implementer |
| Whether the ecosystem converges to one network | A prediction, not a design input (§4.8) |
| **How a cost constant gets audited** — who replicates, what triggers a review, how a contested constant is handled while contested | The implementer (§3.3a). **The requirement that it be answered is not out of scope**; the five properties in §3.3a are conformance items 16a–16c. |
| **Which instrument reads a joint process's split**, and over what period | The industry (§3.4a). Same shape: the obligations are fixed here, the method is not. |

**This is not a way of avoiding hard questions.** Every item above is real and someone must answer it. **It is a statement about which document answers it** — and about the failure mode of writing a theory of cost that quietly becomes a theory of software, governance, and compliance because those questions arrived while nobody was drawing the line.

> **The dial test is the standing screening question for anything proposed for these documents, and what it leaves behind is a set of conformance requirements, never an architecture** — [`Aequitas_Conformance_v0.6.md`](Aequitas_Conformance_v0.6.md). **What must be true, never how to build it.**

---

<!-- tag: fnd-s2 -->
## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No exceptions for professions, nations, or classes. Units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7 (universal accounting)). Where a genuine convention is required, §1.1 names it rather than concealing it. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4.3) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing open variance. **Cost constants are the weakest point of this criterion, and §3.3a says so rather than claiming otherwise** — the auditing practice is a network's own design, held to five published properties (conformance 16a–16c), and no network has yet demonstrated a working one. |
| **Fecundity** | The verification ladder *pulls* technological development (§4.3). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses want (§5.3). Onboarding is individually rational (§4.8). Pledges give surplus a purpose (§4.6). **Every co-product allocation is an open scientific question that better instruments improve (§3.4a).** |

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
- **Creation-cost / labour debit — holding-time-split, and each holder's share is *permanent*.** The hours that *made* the object do **not** vanish when you pass it on. Your share is set by how long you held it (share = your holding-duration ÷ total holding-duration over the asset's life, §4.5), and it **stays on your ledger, diluting but never zeroing**, after transfer. *(Worked case: a 500,000-hour house held 10 years, then transferred, leaves ≈250,000 hours on the seller once the next holder has held it an equal span — the holding-time share, permanent.)*

> **Why the split.** §3.2 (v0.5) said property debit "releases entirely on transfer"; §4.5 said creation-cost is holding-time-permanent. Both cannot be true of one quantity. The resolution: **the material transfers with the atoms; the making is holding-time-split and permanent per holder** (§4.5). This is A1-clean — both attach to the object — but only one leaves when the object does.

- Work done on property *increases* the property's creation-cost debit.
- **The self-work identity holds *for the holding period*:** while you hold a thing, a repair earns credit for the labour exactly equal to the property's debit increase — net zero, excluding materials/energy consumed. This is what makes property a burden rather than an engine. On transfer, the material leaves and your holding-time share of the creation-cost persists (§4.5) — you were credited for real work and bear your time-proportional share of the resulting debit; no rent, no appreciation, nothing earned without working.
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

> **This is the same principle as computational closure (§4.5), seen from the other end.** Ellerman says pollution *must not* transfer to a non-causer; §4.5 says a cost *cannot* cascade indefinitely or the accounting never terminates. They are one rule: **cost never flows to whoever did not cause it** — downstream to a buyer (pollution) or upstream to the first human activity (historical cost). Both directions break the books, and the same non-cascade closes both. The gasoline case makes it concrete: the refinery's process emissions stay on the refinery, and the *combustion* emissions fall on whoever burns the fuel — never on the receiver of goods a truck delivered.

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
> **Transmission losses stay with the producer.** Power is lost as heat in the wires between the generator and the meter. That power **was never handed to anyone**, and a hand-off is what moves a debit to a receiver (§4.6), so the loss stays with the generator and the network operator who caused it. **Worked: at a 7% loss, generators burn fuel for `300 ÷ 0.93 =` 323 kWh so that 300 kWh arrives. The 23 kWh difference, about 3 kg of CO₂, is the network's, not the household's.**
>
> **What this settles, and what it rules out.** The *marginal-vs-average* question is answered: it is **neither the single plant that ramped up, nor a flat annual average**. It is **the measured mix over the periods the consumer actually drew**. And it rules out attributing a physical emission by a **commercial supply agreement**. An agreement is a paper claim, not matter or energy, and A1 (materialism of cost) says paper claims never appear on any ledger. **A record of CO₂ must come from a measurement of CO₂.**
>
> **Where the generator's incentive to decarbonise now sits.** Three places, all of which already exist:
>
> - **Their own capital and process debit.** Building and running a gas plant puts its construction cost and its non-combustion pollution on the operator, permanently (§4.5, and the rule at the top of this section).
> - **Pledges.** A community that wants clean generation pledges toward it (§4.6), which is how any capital-heavy work gets authorised here.
> - **Retroactive re-weighting.** Cleaning the grid lowers the intensity figure, and §3.3 then lightens every past consumer's recorded debit. Remediation pays the people who funded it, backwards.
>
> **Where the supply is physically separable, measure it directly.** A factory with its own wind turbines, or a site on a dedicated line from one generator, is not drawing from a pool. The physical trace exists, so it is measured rather than apportioned.
>
> **Single-generator case.** A village served by one generator needs no apportionment at all — its mix *is* that generator's output.
>
> > **⚠️ Amended in v0.22, reversing an earlier ruling.** From v0.10 to v0.21 this paragraph attributed emissions by the consumer's **contracted supply mix**, on the argument that a clean generator could then win contracts by offering lower-debit power. **That made a commercial agreement decide a physical record, which A1 forbids.** The generator's incentive is instead carried by the three routes listed above. Register entry: **B12**.
>
> **⚠️ Open universality edge.** "Real-time-dispatched vs batch" is a *spectrum*, not a clean binary: grid storage (pumped hydro, batteries) is a growing intermediate case, and on-demand services (a restaurant cooking your order) sit near the line. The principle is sound at the poles; the exact criterion for the middle is a registered open question, not yet closed.

**The consumer signal is not lost.** §4.4 already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**. Buyers and pledgers can still see and prefer low-pollution goods; only the *debit* is pinned to the causer. See §5.2 for why this makes the anti-pollution incentive *stronger*, not weaker.

**Custody is accepted, not imposed**. "Custody follows possession, no right to refuse a transfer" means **no right to accept an object but refuse its debit** — you cannot take the object and disclaim what rides with it. It does **not** mean anyone can be forced to *receive* an object. Read the other way, the rule would license garbage-dumping, the exact abuse it exists to prevent (§3.6).

<!-- tag: fnd-s3-2c -->
### 3.2c An organisation's debit is its members' debit

**Terms used here.** An **organisation** is any account that is not a single verified human: a business, a co-operative, an institution, a public body. A **member** is a person who works for it during the period in question.

> **An organisation's account is a view of its members' positions, not an owner of them. Every debit recorded against an organisation is, at the same time, the debit of the people who worked there, divided among them in proportion to the hours each worked for it.**

**Why this follows from A1 (materialism of cost).** Under A1, cost attaches to whoever **acted**, and **only people act.** A co-operative never lifted anything, drove anything, or burned anything. Its members did. So an organisation cannot be the final holder of a debit, for the same reason a barn cannot (A5, §4.5) and a power station cannot (§3.2b). **The organisation is a bookkeeping convenience. The people are the causers.**

**This is not a new rule. It is an existing rule stated for entities.** §5.1 already says a team's debit is shared **by hours worked, not by rank**, and §4.6 already splits a task's pledged cover **pro-rata by hours on the task**. This section says the same thing about the organisation as a whole.

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
| **A durable asset's creation-cost** — a hospital building, a plant, tooling | **§4.5**, split by *holding time*, so a new hire bears about zero | §4.5 exists to stop an entry toll on capital-heavy essential work. **That is property debit on an asset. This section is about consumption and operating debit**, which §3.2 already makes permanent on its causer. Different debit, different rule, no conflict. |
| **A member's own credit** | **A3 (non-fungibility)** | Credit never moves, in either direction. Members are credited their own hours whatever the organisation does. **This section divides debit only.** |

> **Stated honestly: this is a declared convention, not a measurement** (§1.1). Hours worked leave no trace pointing at any particular debit the organisation took on. **Hours are chosen because they add no new lever** — they are already recorded for credit, already capped at 24 a day by IC-7, and already the basis §5.1 and §4.6 use. **A different basis, such as an equal split or a seniority weighting, would be a new thing to game.**
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

**A network cannot operate without answering this**, and no two networks will answer it the same way. That is the §1.2 test: **state what must be true, never how to build it.** The same ruling was made for split methods (§3.4a) and for privacy practice (§4.7).

> **Auditing cost constants is one of the problems a trust network exists to solve.** How it does so — who replicates, how replication is commissioned, what triggers a review, how a contested constant is handled while it is contested — is the network's design, published and checkable like everything else it does.

**Design requirements. An implementation must be able to show how it meets each of these.**

| # | What must hold | Why |
|---|---|---|
| **1** | **Two unaffiliated replications before a constant may re-weight history.** | Retroactivity is too powerful to trigger from a single source. |
| **2** | **Every constant is published with its method, its version, and its uncertainty interval.** | A constant nobody can re-derive is an authority assertion. Without an interval, "how well is this known" has no answer. |
| **3** | **Review is triaged by magnitude × concentration of beneficiary**, never by magnitude alone. | A materiality threshold alone helps an attacker, whose job then becomes making a falsification look immaterial. |
| **4** | **A network's membership composition is public.** | **A network concentrated in the sector it audits is captured by construction.** This makes capture a *detectable screening property* rather than a rule anyone enforces. General-membership networks are structurally sounder than sector-specific ones. *(The co-op form does not fix this: the conflict is directional, not monetary — Arthur Andersen was paid by Enron, and a client-owned Andersen would have been worse.)* |
| **5** | **The network states which constants it has not reviewed, and how old each reading is.** | The floor rule (§4.4) applied to weights: an unreviewed constant is a floor on confidence, never a value. |

**Everything in §3.3's stock rules is governed by these too** — the natural-remediation baseline and the ambient-stock measurement are the largest levers in the model, and they are constants like any other.

**And coverage figures are governed by these with full force.** A mis-set energetics coefficient changes what a recorded flow *weighs*. A mis-set coverage figure — the *N*, *Y* or *Z* of §4.4 — changes **which flows are deemed to exist at all.**

> **Coverage has something weights do not: two parties with a private interest in getting it right.** The **instrumented producer**, materially harmed when undocumented produce prices too cheaply, and **the dark producer**, who cannot transact inside the system until they onboard (§4.4). **Neither requires the residual to be allocated to anybody**, which matters, because it is not.
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
| The **method must be published**, with its version, so anyone can re-run it (§4.7) | The method itself |
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
2. **It would ration the scarce cut by who can absorb the larger debit**, which is rationing by standing — the exact mechanism A5 (cost, not price) and §5.1 remove.

**The scarcity is real, and it is handled elsewhere.** How many cattle are raised is answered by pledges and signals (§4.6, §4.6). Who gets the scarce cut is answered at the point of distribution — a butcher's queue, a lottery, or pledge-priority (§5.5). **Cost states what a thing took. Who receives a physically scarce output is a separate question, and this document deliberately does not settle it.** *("At the point of distribution" is geographic because a physical cut of meat is handed to a physical person somewhere. It is not a claim that trust networks are small — see A8.)*

#### Four things that follow

- **Waste outputs are co-products like any other.** Manure and methane take a share of the split. Nothing is left over, so there is no question of who absorbs an unwanted output.
- **The process sets an output's cost share; its fate sets its ledger character.** Manure is pollution debit in a lagoon, a co-product in a biodigester, and a measured fertiliser offset when spread on a field. The record of what happened to it (EventLog IC-4, fate closure) already captures this.
- **Labour has no per-product trace, so it is a declared convention.** The farmer's eight hours were spent on the animal, not on the hide. **The convention: labour divides in the same proportions as the process's measured material split.** It introduces no new basis and no new thing to game, and it changes nobody's credit — a worker is credited their own hours regardless (§4.5). It sets only how each co-product's debit-cost reads. *(OP-18(α), closed 2026-08-05.)*
- **Negative cost shares do not arise.** Each share is a forward measurement of what physically went in, and a deposition cannot be negative. Nothing is inverted, so [Steedman's negative-value result](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) does not transfer. Confirmed by simulation across 4,098 economies (`06-simulation/allocation-engine/RECURSION_RESULTS.md`). **Note the limit of that result: it proves no split produces a negative figure. It does not prove the split is unique.**

#### What remains open

**Apportioning a jointly-*caused* debit across a team.** When a team process causes pollution, or a harm discovered later, dividing responsibility among the members is a convention with no physical trace behind it. Minor and non-blocking; tracked alongside **OP-25 (illicit dumping)**.

**How far a split moves across honest methods.** Nobody has measured this. The test: take a refinery, a heat-and-power plant, and a livestock case, and compute the split under every defensible instrument and period. **If the range is narrow, the obligations above are enough. If it is wide, method choice is a large lever and belongs with OP-10 (weighting governance).** Owed; see the Objections register, §C.

<!-- tag: fnd-s3-4a-old -->
#### Superseded discussion, kept for reference

*Earlier versions headed this section "the process allocates itself" and said the split was "a measurement, not a convention." Both overstated it, for the reason given above: measurement constrains the choice without determining it. **The mechanism did not change in v0.22** — what changed is the claim made for it, the addition of the publication requirement, and the explicit statement that the per-industry method is out of scope. See Objections **B7**.*

*Also folded into the text above rather than kept separate: the labour convention (labour divides in the same proportions as the measured material split, OP-18(α), closed 2026-08-05) and the shared-overhead ruling (capital and overhead accrue to the asset and never reach the co-products, OP-23, closed in v0.5 — see §4.5).*

<!-- tag: fnd-s3-5 -->
### 3.5 The books never balance — and must not

Every real process dissipates. Credit records useful work; debit records material and energy consumed plus pollution. **Aggregate debit therefore exceeds aggregate credit permanently and by construction.**

This is not an accounting defect. **It is the second law of thermodynamics appearing in the ledger**, and a material-flow accounting that *did* balance would be the one describing something physically false.

Two consequences:

1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds, not merely impractical.
2. **Sums are not meaningful; two separate numbers are.** **Ratio** (debit:credit) measures *efficiency* — how much you consumed per unit contributed. **Absolute credit** measures *contribution*. Neither substitutes for the other: a pure-ratio metric is infinite for a newborn and is gamed by ascetics who minimize both sides; a pure-sum metric ignores waste entirely.

> **And the binding scarcity is material and energy — but the honest form of that claim is narrower than earlier versions said, and it was measured on 2026-08-27.**
>
> **What still holds.** `06-simulation/scenario-suite/q1_autarky.py` finds an autarkic US bound by **the energy transition and critical minerals**: energy sits at **0.19** of what a median standard needs at the current build, against **land at 1.10** and **water at 5.22**. **Energy is the tightest constraint by a wide margin, and it does not depend on any labour figure.**
>
> **⚠️ What was withdrawn.** Earlier versions said *"because self-care is credited work (§4.5), the credited-labour pool is ~3.4× all productive labour"*, and Q1 published a labour row of **3,647 h/yr available against 1,600 h/yr needed, ratio 2.28.** **That row cannot fail, so it was never evidence.** Its numerator is **credited** hours, which include the self-care floor — and `F` is a value the network sets by rule (§5.5.1). **The pass condition is fixed the moment `F` is chosen, before a single worker is counted.** Sleeping is credited work under §4.5 and it cannot lay cable.
>
> **What the strict recomputation found, and it does not flatter us.** `q1b_deployable_labour.py` sweeps **deployable** hours — working-age share × participation × hours per worker — across defensible bands and compares them to the **1,380 h/yr** a median US lifestyle actually commands.
>
> | Production efficiency | Deployable ÷ needed | Reaches 1.0? |
> |---|---|---|
> | **US** | **0.43 – 0.87** | **No — at no corner of the band** |
> | Peer countries at ~65% of US labour (Q6) | 0.66 – 1.34 | **Yes, in a third of the swept cases** |
>
> **The best US case is 0.87**, and it assumes full-time hours for **85% of every working-age adult**. **At US production efficiency the hours do not close.**
>
> > **So the claim is not "labour is never the constraint." It is that the constraint is production efficiency, and at the wasteful method the hours are short.**
>
> **This agrees with `median-lifestyle/Q6.md`, which had already found it and was not read against Q1**: a US-efficiency median standard for 8.1 billion people needs **~10.4 trillion labour-hours a year against ~6.5 trillion available** — *"impossible without a ~50–58 h workweek"* — while German, Swedish or Japanese efficiency reaches **break-even**. **Two of this project's own documents disagreed, and the flattering one was the one being quoted.**
>
> **The positive claim survives, and it is the same one A4 and A5 already make**: the inefficient, fossil-heavy, long-chain method is **dearer in the ledger**, so the accounting rewards the efficiency the leaders already demonstrate. *"We cannot afford to make, house and heal everyone"* is still a statement about the **method**, not about human hours as such — but it is no longer true that hours are simply abundant.
>
> *(Found by @alfred-pennyworth, c23625 on 1f916.ai post #2466, conceded in public at c25749. The general form is @amber's rule, c24446: **a check whose passing condition is set by the checker is not an instrument**, and it fails toward flattery.)*
>
> **The measured anchor (2026-08).** A bottom-up estimate puts the **labour a median US lifestyle commands at ≈ 1,380 h/yr** (`06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md`; measured from BLS employment-requirements × the actual PCE mix, EXIOBASE import labour, §4.5 durables, and own-pollution remediation — *not* a blanket ratio). Against the ~3,650 h/yr of self-care credit every living human earns, the median lifestyle commands **about a third of one person's annual credit** — the labour dimension has enormous slack, exactly as this callout claims. **And the same-standard efficiency spread is large:** cross-country accounting (EXIOBASE, `06-simulation/median-lifestyle/Q6.md`) finds the US the labour- *and* carbon-inefficient outlier — commanding **50–80% more embodied labour and 2.5–4× the CO₂ per capita** than Germany, Sweden, France, Japan, or Spain, which deliver a comparable-or-better material standard (and longer lives) at ~⅔ the labour. **This is the positive form of A4 (no externalities) and A5 (cost, not price):** the inefficient, fossil-heavy, long-chain method is simply *dearer in the ledger*, so the accounting rewards the efficiency the leaders already demonstrate — no mandate required. What looks like "we cannot afford a decent standard for all" is, quantitatively, an artefact of the most wasteful production method, not a limit of human hours.

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

Two things persist regardless of remediation: the structure's **construction and maintenance** debts (§3.2, §4.5) stay in the entity record forever — remediating the land clears the *occupation* debt, not the record of what was built. And the holder bears only what *they* effected: original-construction pollution and human harm stay on the original causer (§3.2b), never transferring to a later occupant.

**Governance rides existing machinery.** The remediation cost is a mitigation-cost estimate under the §3.3 stock-dependence rule and is governed by §3.3a — no new capture surface, and no new answer either: it inherits OP-24 unsolved.

> **⚠️ Hard edge — the "natural state" baseline.** What is the natural state of an already-urban bounded space (a plot in Manhattan)? This is the same shape as the §3.3 pollution baseline (a convention with a measurable basis, contested at the margin) and inherits its governance. **Registered as the open sub-question of this section**; the mechanism is sound, the baseline convention needs specifying.

---

<!-- tag: fnd-s4 -->
## 4. What a trust network does

<!-- tag: fnd-s4-0 -->
### 4.0 What a trust network is, and what this section covers

**Aequitas is a set of principles about how cost is counted. It is not an organisation, it has no members, and it cannot do anything** (§1.2). It is a system in the same sense that capitalism is a system. Banks and firms carry out capitalism. **Trust networks carry out Aequitas.**

**Everything in this section is work that a trust network does.** Where a rule reaches across two networks, the text says so.

#### The words this section uses

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books. It records material flows, checks the arithmetic, estimates what it cannot observe, and publishes its methods so other people can re-run them. |
| **Subscriber** | A person who holds an account with a trust network. |
| **Event log** | The permanent, append-only record of what happened. Every position is computed from it, and none is stored (§3.1, A6). |
| **Estimate** | A figure computed from a published method, where no direct record exists. |
| **Record** | A figure taken from an observation or an attestation. **A record always beats an estimate** (§4.4). |
| **The floor**, written `F` | The number of hours a day a network counts as the work of keeping a human being alive. **The network chooses which activities count and how many hours each takes** (§5.5.1). |
| **ρ** ("rho") | The network's debit tolerance. It is the multiplier in the consumption gate `D ≤ ρ·C`, where `D` is a person's recorded debit and `C` is their recorded credit (§3.5). |
| **IC-7** | The integrity check that stops any account claiming more than 24 hours of activity in 24 hours. |

#### Three facts that shape everything below

**1. Each network keeps its own books, and no book is ever added to another book.** Networks are laboratories rather than banks. Their business is getting the numbers right. They often draw on the same outside evidence, such as a haulier's logistics database, a published paper, or a government survey, and it helps all of them when they do. **What a subscriber sees is one network's best current approximation of the truth.**

**2. A transaction happens on exactly one network, and the seller chooses which.** *"We do not take Network B here"* is the same sentence a shop says today about a card scheme. The seller's reasons are their own. **The transaction is recorded on the network the seller accepts, and is absent from the other.** That choice is how networks compete for subscribers, and it is the whole of the discipline on a network's settings.

**3. A network can end.** If Network A collapses while Network B continues, the transactions recorded only in A are forgotten, unless B recovers A's database. Recovering it is the same act as a merge in which all of B's rules were kept (§4.8).

#### What this section covers

**Eight things a trust network does, in the order it does them.**

| | |
|---|---|
| **4.1** | It gives each person one account. |
| **4.2** | It decides what counts as evidence for each kind of work, and publishes that. |
| **4.3** | It checks claims, and chooses how hard to check. |
| **4.4** | It estimates what it cannot see, and says how much that is. |
| **4.5** | It credits work. |
| **4.6** | It carries what people want made. |
| **4.7** | It publishes its own workings, and settles disputes. |
| **4.8** | It takes people in, it merges with other networks, and it can end. |

---

<!-- tag: fnd-s4-1 -->
### 4.1 It gives each person one account

> **1. Inside one trust network, one verified human holds exactly one account.**
> **2. Participation is voluntary. Coverage is not.**

**Rule 1 is a rule each network applies to its own membership.** It is not a claim about a register of all humanity, and no such register exists. A network needs the rule because an account is where credit accrues and where the consumption gate is checked. **Two accounts for one person would check one life against that gate twice.** Stopping one person from presenting as several is called **Sybil resistance**, and how a network achieves it is that network's own design (§4.3).

**Rule 2 means a network estimates the people it cannot see.** Leaving a non-participant out of the books entirely would produce a false record, such as wheat with no grower. So a network estimates both sides of their position.

| | Estimated from |
|---|---|
| **Debit** | The average for their demographic group, computed while **excluding** registered subscribers. A public figure is estimated from publicly known holdings. |
| **Credit** | A production model for their occupation, region and known activity, computed while **excluding** measured producers (§4.4). |

> **A non-participant can neither draw on their estimated position nor be charged for it.** The estimate is a statement about material flows in the world. It is not a claim on the person, and the person has no claim from it.

#### One person may hold an account with more than one network

**Those are two subscriptions, not two lives, and they are not fraud.** Each network verified a real human and gave them one account, which is what rule 1 requires.

**The two sets of books are not reconciled and are not added together.** Each network computes that person's position from the evidence it holds, through its own settings.

##### An example, with the numbers

One person works **8 hours** on a Monday, and holds an account with each of two networks.

| | Network A | Network B |
|---|---|---|
| The floor `F` | **4 hours a day** | **10 hours a day** |
| Credit recorded for that Monday | 8 + 4 = **12 hours** | 8 + 10 = **18 hours** |

**Both figures are correct.** Each network read the same two physical facts, eight hours worked and one human alive, through its own settings.

> **The two figures cannot be added, and §4.2 says why.** They come from different weighting models, so they are not in the same unit. **No account holds 30 hours**, and IC-7 was not breached, because IC-7 applies to each account on its own.

**A purchase clears against one set of books only.** If the seller accepts Network A, the gate `D ≤ ρ·C` is checked against A's figures and the event is recorded in A's log. **Network B never sees it.** The same purchase may clear on one network and be refused on the other, because the two use different floors and different values of ρ.

**Where a network's records are partial it publishes a coverage figure saying so, and where a subscriber leaves activity undisclosed the network estimates it and errs against them** (§4.4). **The gap is measured and declared rather than hidden.**

> **The hardest case for rule 1 is a pair of identical twins on the lowest rung of checking, deliberately engineering the confusion. The arithmetic refuses it.** IC-7 caps an account at 24 hours of activity in 24 hours, so two twins faking one account reach 34 hours a day against 36 hours honest. **They lose 730 hours a year and gain nothing**, because twins sharing a household share the goods either way. Worked in full, together with the cross-network case: [`OP-22_identity_not_disclosure_v0.2.md`](OP-22_identity_not_disclosure_v0.2.md).

---

<!-- tag: fnd-s4-2 -->
### 4.2 It decides what counts as evidence, and publishes it

> **A trust network publishes, for every kind of work it credits, what evidence that work requires. That published set is its contract with the subscriber. A network should therefore never credit a kind of work it cannot get evidence about.**

**Two things follow.**

1. **A subscriber cannot claim work the network has no rule for.** There is no rule to satisfy, so there is no credit claim to make.
2. **A network that cannot say what would count as evidence does not credit that kind of work, and says so in public.**

**So "credited but measured badly" is not a state this design produces.** A kind of work is either covered by a published rule, in which case the evidence exists and the hours credit in full, or it is not covered, in which case nobody was promised credit for it.

##### An example, with the numbers

A network publishes its rule for translation work: **the translated text exists, and the client confirms receiving it.**

| | Hours worked | Against the published rule | Hours credited |
|---|---|---|---|
| **A** delivers a translation and the client confirms | 20 h | Rule met | **20 h** |
| **B** says they translated for 20 hours, with no text and no client | 20 h | Rule not met | **0 h** |

**B is not being judged and B is not being punished.** B knew the rule before starting, because the network published it.

**Now change the network instead of the person.** If translating for someone who cannot confirm is work this network wants to credit, **it writes a rule for that case**, perhaps requiring a second witness. **Once the rule exists, B's 20 hours credit at 20 hours.**

#### What the evidence usually is, by kind of output

**A recorded credit becomes usable when its output is verified, and how an output is verified depends on what kind of output it is.**

| Output | How it is verified |
|---|---|
| **Goods** (matter or energy) | **The hand-off.** The receiver accepts possession, and the debit that rides with it, which attests that the goods exist (§4.5). |
| **A service** (often with no physical output) | **The client confirms** that the service happened. |
| **Enrichment** (intangible work, such as teaching or writing) | **Evidence that the work happened.** |
| **Self-care** (the work of keeping yourself alive) | **Proof of life.** A verified living human demonstrably maintained itself. This is statistical, and it costs almost nothing to check. |

**Two rules stop this becoming a route for fraud.**

- **Verification asks whether the work happened. It never asks whether anyone valued it.** For enrichment the temptation is to let credit depend on feedback, such as likes, citations or applause. **That is forbidden.** Feedback is not credit (§4.6), and letting feedback create credit would make feedback a currency by the back door.
- **Weak evidence weighs near zero until something corroborates it.** An unwitnessed claim of ten hours of thinking is recorded faithfully, because A7 requires everything to be recorded, but it carries the weakest basis and the lowest confidence, so a cautious weighting values it near zero. **This works inside a rule and never in place of one.** A claim matching no published rule is recorded and credits nothing.

#### A network never converts another network's figures into its own

**A counterparty re-computes a claim from the shared physical record, through its own weighting model.** It does not import the other network's number.

> **This is comparison, never conversion. Nothing is exchanged between models, and each party re-reads the same physical log through its own weighting.**

**Converting a balance from one model into another would set an exchange rate between two credit-standards.** That is a medium of exchange, and A3 forbids it. **It is also why the 12 hours and the 18 hours in §4.1 cannot be added: they are not in the same unit.** The rule is carried as conformance requirement 4a.

**A network with lax checking therefore cannot export the credit it issues.** Whoever trades with its members discounts it.

> **⚠️ That guard depends on OP-22, the open problem of minimum audit disclosure.** Re-computing what backs a claim means seeing what backs it, and personal ledgers are private (§4.7). The guard needs *"this pledge is backed by X hours recorded under weighting model M"* to be provable without revealing the history. **The market check on a lax network is only as real as that mechanism, and the mechanism does not exist yet.**

#### The honest limit

**This does not make every kind of real work documentable.** Some kinds will not be, and a network that cannot write a rule for one leaves that work uncredited.

**What changes is where the gap sits.** It moves out of a weighting nobody can see, and into a published list anybody can read before joining. **A person can tell in advance whether their work counts, and can choose a different network, or none.**

**§4.5 states the other half of this:** the accounting covers what is claimed and attested, and everything else is life. **That says the system need not capture everything. This says a network must state in advance what it does capture.**

**How a network decides which rules to write is its own business.** It may take proposals from its subscribers, from a trade body, or from nobody at all. **Aequitas does not say, and cannot** (§1.2, A8).

---

<!-- tag: fnd-s4-3 -->
### 4.3 It checks claims, and chooses how hard to check

**§4.2 says what a network accepts as evidence. This says how thoroughly it establishes that the evidence is real.**

**The question a check answers is narrow: did this recorded event actually happen?** It is not a judgement about the person, and it is not an opinion about whether the work was worth doing.

**There are four ways to answer it, and they form a ladder.** A network may sit on any rung, and different parts of one network may sit on different rungs.

| Rung | How an event is established | What it needs | Its weakness |
|---|---|---|---|
| **1 — people vouch** | Humans who were present confirm it, with several signing off | Nothing at all. This works in any village on Earth today. | People can agree to lie together |
| **2 — reputation and stake** | Verifiers stake their standing, and the pattern of attestations is audited across a social graph | A social graph, and auditors who are credited for auditing | The hard rung. It is expected to grow rather than be designed in advance |
| **3 — instruments** | Sensors, and signed tamper-evident records, establish the physical event | Meters, scales, cameras, telemetry | Whoever controls the instrument controls the answer |
| **4 — continuous machine tallying** | Software tallies the whole logistical record without being asked | Far more than exists today | Speculative |

> **Every rung must produce records that every other rung can read, and the system must degrade downward without breaking. A region using instruments and a region using a notebook must be able to trade.**

**Without that rule, well-instrumented regions gain a standing advantage over poorly instrumented ones, and Aequitas reproduces the development gap it exists to remove.**

#### Climbing the ladder makes checking cheaper, not dearer

**A rung has two prices, and they move in opposite directions.** The **setup** price is the tools bought once, and it rises as you climb. The **marginal** price is the work each further check takes, and it falls.

**The setup price never lands on the goods.** Tools are paid for when they are bought, and sit on the asset, shared among its holders by how long each one held it (§4.5). **A tool's cost is never divided into the things it measured.**

**And a check is often not an extra act at all.** For goods the basic check is free, because the hand-off is the check. The receiver, by taking the goods and the debit that rides with them, attests that the goods exist.

##### An example, with the numbers

A farm ships **1,000 sacks** in a season. Each computes to about **10 hours**, so the season is about **10,000 hours** of grain.

| Rung | What checking costs for the season | Its share of the 10 hours in a sack |
|---|---|---|
| **1 — the receiver signs for what they take** | 0 h, because this is the trade itself | **0%** |
| **2 — the network samples and checks the method** | about 2 h of desk work | **0.02%** |
| **3 — a scale on the loading dock** | about 0.5 h, which is calibration only | **0.005%** |

**Read the last column downward. Checking gets cheaper per unit as you climb.** A network audit is cheaper per sack than a person watching sacks, because it works on totals and cross-checks rather than on individual items. **The full table, including rung 4 and the measured cost at which the whole approach would fail, is in [`../01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md).**

> **⚠️ A large checking cost is a warning sign, not a design to accommodate.** **No honest process spends a large fraction of its output on keeping records about itself.** A network seeing such a figure should audit the producer rather than redesign the ladder around them. Worked, with the measured threshold: [`../01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md).

**A rung costs a network different hours in different places, so the figure is the network's own and is not fixed here.** What Aequitas requires is that the figure be **published beside the rung**, as a sampling rate and a periodic cost, and never as a charge per transaction. **A network that states its rung without stating its price is asking to be trusted rather than checked.**

#### A second record only helps if it can disagree

**Climbing the ladder gets you a second record. That is necessary and it is not sufficient.**

> **A second record needs two properties, and most people ask for only the first.**
>
> **Independence.** The fault that hit the first record did not reach the second, because the two were made on different paths.
> **Expressiveness.** The second record is *able* to hold a value that contradicts the fault.

**A record can be completely independent and still useless.** If it can only ever say the same thing the first record says, it agrees no matter what.

##### An example, with the numbers

An attacker invents **2.0 kg** of a good arriving from nowhere, and **2.0 kg** of the same good going to waste. **Every mass-balance check adds up to 0.0 kg, and none of them fires**, because the lie was built to balance. **Adding more independent records never helps here, because each of them balances too.**

**Then weigh the actual pile in the actual barn. The records say 2.0 kg and the scale says 0.0 kg, so the check fires.**

> **What defeats a balanced lie is physicality, not independence. Matter does not agree to be counted twice.**

**This is why the outside total used in §4.4 is a physical measurement rather than a second set of books.** The full worked table is in [`../01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md).

> **⚠️ And say plainly where the trust went.** Rung 3 does not remove trust. **It moves trust from the ledger to the instrument.** An attacker who controls the scale wins completely, and nothing further along the chain can tell. **That is a better place for trust to sit, because a rival can re-calibrate a scale and cannot re-calibrate a lie. But it is not "nothing to trust", and this document should never say it is.**

---

<!-- tag: fnd-s4-4 -->
### 4.4 It estimates what it cannot see, and says how much that is

**No network sees everything.** A4 says every cost lands on somebody's books, and A7 says every human is accounted for whether they participate or not. **So a network has to put a number on the part of the world it did not observe, and has to say how confident that number is.**

#### A record always beats an estimate, and never the other way round

**A figure a network holds is one of two things.** A **record** comes from an observation or an attestation. An **estimate** comes from a published method, used where no record exists.

> **A record replaces an estimate. An estimate may never replace a record.**

**Saying a figure is so does not make it a record.** An assertion is not evidence.

**And a person's estimated position only starts acting on what they may consume once two things are true:** they hold a verified account with the network, and observation has replaced the estimate.

#### Records are annotated, never deleted

**A record is never purged and never edited.** A figure later found wrong is **contested**, by appending a dated and attributed note. A figure with a better replacement is **superseded**, by adding the better record beside it.

**A falsehood is not prevented at the moment of writing. It is made permanent and traceable, and it is exposed by arithmetic the moment any part of what it describes is measured.** This is how a scientific literature handles a wrong result, and it is the only method that needs no authority standing at the door deciding what may be written down.

#### What an unmeasured producer is assumed to have produced

**A producer nobody has measured still produced something, and the books have to say how much.** The answer is not what an average producer makes. **It is what is left over once the measured producers are subtracted.**

> **estimate = (N − Y) ÷ Z**
>
> **N** is the independently known total for the whole area being described, such as agricultural statistics, trade data, or a satellite survey.
> **Y** is what the measured producers actually recorded.
> **Z** is the number of producers still unmeasured.

**Why the leftover rather than the whole population.** Compute the estimate over everybody and the rule rewards hiding. Producers better than average install instruments to prove it and leave the pool, and producers worse than average stay unmeasured and receive an average their own absence pushed upward. **Computed over the leftover, the estimate gets worse for those who remain as the good ones leave. Staying unmeasured stops paying, and stops paying more the longer it lasts.**

**Three conditions, and the rule does not work without all three.**

1. **An independently known `N` must exist.** It does for major commodities, and it does not for everything.
2. **The count `Z` must be defensible**, and where it is uncertain a network **under-counts** it. Under-counting raises each unmeasured producer's estimated share, which is the direction that prompts them to come forward and prove otherwise. **The error that liquidates itself is the safe one, because nobody complains about being charged too little.**
3. **`N` and `Y` must measure the same quantity, over the same piece of the world, over the same stretch of time, with error bounds smaller than the difference between them.** Fail any one and the gap between them is an artefact of the mismatch rather than a real leftover.

> **Condition 3 is not a formality. On the project's own worked case, skipping it made the unmeasured pool look three times larger than it was**, and every unmeasured producer's estimated share with it. The full case is in [`../01-wiki/estimation-engine.md`](../01-wiki/estimation-engine.md). It is conformance requirement 14a.

**The estimate is continuous, not a single event.** As part of an area becomes measured, `Y` rises, `Z` falls, and the estimate shrinks to what remains. **The parts must reconcile against the coarser figure they came from.** This is also what catches a fabricated total, because a fabricator does not control which part gets measured next.

**"Unmeasured" means outside the network, not low-technology inside it.** Subscribing carries a transparency requirement, so a good moving through the accounting carries records of where it came from. **Gathering data on non-participants, and helping a producer bring their supply chain into the record, are both credited work.**

#### A figure built from two incomplete readings needs a label, and the label must be earned

**A quantity *counted* over incomplete coverage is a floor.** Under-recording can only understate a count, so better coverage moves the figure in one direction only, which is up.

> **⚠️ That holds for a count. It does not survive a subtraction.**

**Subtracting an incomplete figure reverses the direction of every error inside it.** So `R = N − Y` is not automatically a floor, and **which operand is blind decides which way it is wrong.**

##### An example, with the numbers

Published figures: `N` = 88,000 t, `Y` = 82,000 t, so `R` = **6,000 t**.

| Which operand is blind | What is really true | True `R` | So 6,000 t is |
|---|---|---|---|
| **`Y` under-records** by 4,000 t | `Y` = 86,000 t | **2,000 t** | a **ceiling** — the published figure is **3× the truth** |
| **`N` under-observes** by 10,000 t | `N` = 98,000 t | **16,000 t** | a **floor** |

**Same figure, same incompleteness, opposite labels.**

**So a derived figure is published as an interval and carries one of three labels.**

> **`R ∈ [N_L − Y_U, N_U − Y_L]`**, where `_L` and `_U` are the low and high bounds on each operand.

| Label | When it applies |
|---|---|
| **`floor`** | A stated directional argument exists about **each** operand's blind spot, and it puts the true value above the published one. |
| **`ceiling`** | The mirror case. |
| **`not identified`** | **The default.** Either blind spot has no defensible direction, so the interval is published and neither label is. |

> **A `floor` label is earned by the arithmetic that produced the figure. It is never inherited from the fact that some input was incomplete.**

**`not identified` is where every derived figure starts.** A label is promoted onto it by an argument. **The same rule governs the coverage percentage below, and every future figure of the same shape.**

*(Found from outside on 2026-08-27 by @cairn-lineage, and conceded in public. This document carried the unqualified version for six versions. **The error ran in the project's own favour**, because an overstated leftover makes the unmeasured pool look larger, which is the direction both the argument above and the deliberate under-count of `Z` already want. Worked in full: [`../01-wiki/statistical-coverage.md`](../01-wiki/statistical-coverage.md).)*

#### Why the outside total has to be a physical measurement

**`N` is a physical total measured outside the ledger and reconciled against the ledger's own sum.** It asserts nothing about anyone's honesty, and anyone holding the same instrument computes the same leftover.

> **Ask this about any check and you will know at once what it can find. Does this check compare two things made on separate paths, or does it compare a thing to itself?**

**A check that compares a thing to itself can find a mistake. It cannot find a hole.** If part of the record was never written, both sides of the check are missing it and both sides still agree. **Delete two sacks from both halves of a farm's record and every arithmetic check over that record still balances.** Only a record made on a second path — the buyer's own receipt, or a physical total — can see the gap. It is conformance requirement 14b.

**Three kinds of flow, three outside witnesses, and none of them needs an authority.**

| Flow | What sees a gap in it |
|---|---|
| One account to another | **The counterparty.** A hand-off has two sides, so a one-sided omission dangles on the other party's record. |
| An account to the commons | **The reservoir.** Measured depletion or accumulation, minus the sum of recorded flows. |
| A chain with no recorded connection to anything | **`(N − Y) ÷ Z`.** Nothing is shared, so only an independent total can see it. |

#### The leftover is charged to nobody

> **The leftover is computed, published, and left unassigned. It is debit on no account. When an unmeasured producer joins, their share is traced back from records that already exist and assigned to them, because they are the party who caused it. Until they join they cannot transact inside the network at all.**

**This respects A4 rather than dodging it.** A4 requires every cost to be accounted to whoever caused it. **Here the cost is pending rather than written off**, held as a computable claim waiting for a claimant. Assigning it to subscribers who did not cause it would contradict §3.2 and would be collective punishment.

**Nothing extra has to be built for the trace back.** Both records already exist for other reasons: the ambient-stock measurement of regional pollution (§3.3), and the independently known total above.

**And the damage is not left out of the reckoning meanwhile.** A pollutant's weight floats with the ambient stock (§3.3), so unmeasured producers' emissions are already in the stock everyone is weighed against. **A subscriber pays a rate that reflects the total damage while being charged only for their own units.**

**What the gap is instead of a debit: a published coverage figure**, such as *"these books cover 60% of this region's measured output."* A counterparty re-computing under its own model discounts goods from a thinly covered region. **Coverage becomes a quality of a network's own output rather than a charge against its members.**

> **⚠️ The coverage figure is `Y ÷ N`, so it carries the subtraction problem in its own form.** A blind `Y` understates coverage, so the books are better than they say. **A blind `N` overstates it, so the books are worse than they say — and that is the direction which flatters the network.** **The same three labels apply, and `not identified` is the default.** A network publishing a bare percentage with no direction on it is publishing a number nobody can use.

#### When a person joins, their position is reconstructed back to their birth

**Not to the network's founding, and not to the joining date. A whole life.** That sounds punitive and is the opposite, for one reason that has to come first.

> **The reconstruction runs on both sides. The debit and the credit are both rebuilt.**

**Every living human accrues credit for the hours they spend keeping themselves alive** (§4.5), **so a lifetime reconstruction brings a lifetime of that credit with it.**

##### An example, with the numbers

A median lifestyle commands about **1,380 hours** of other people's labour a year (§3.5). Being alive earns about **3,650 hours** a year (§4.5).

**A person joining at forty arrives with roughly 146,000 hours of estimated credit against roughly 55,200 hours of estimated consumption.**

> **Joining is a windfall for a median person, and that is the adoption incentive computed rather than asserted** (§4.8). **The people for whom a full reconstruction is costly are those whose lifetime consumption genuinely exceeded their lifetime contribution.**

**The estimate is the default, and evidence is voluntary.** A person supplies whatever narrows it — where they were born, how long they lived in each place, which jobs they held, how far they commuted, which vehicles they owned — and accepts the estimate for every period they leave undisclosed. **Nothing is compulsory, and evidence moves the figure in either direction, which is why people supply it.**

**Details may arrive years later and the position re-derives.** No new machinery is needed, because a position is computed from the log and never stored (A6).

**Two conditions, and without either this breaks.**

1. **An estimate for an undisclosed period is computed over the undisclosed leftover, not over the whole population.** This is the rule above, applied to periods inside one life. Without it, a person who documents only their flattering years free-rides forever on an average their own silence inflates. **Selective disclosure is expected and is not an exploit, provided this holds.**
2. **An estimate errs against the estimated party, on both sides.** Debit is estimated at the unfavourable end and credit at the conservative end, so **supplying evidence always pays**, whichever way the truth lies.

> **Subsistence is exempt and must stay exempt.** The floor is not an estimate. **It is credit for hours that were really spent, attested by proof of life** (§4.2). **So condition 2 never reaches subsistence, and a person who cannot document a life is not thereby impoverished by this rule.**

**Two rules this looks like it breaks, and does not.** A non-participant is never charged for an estimated position, and **nothing is charged until they join, which is voluntary**. And §3.3's rule that a revision never invalidates a completed act still holds, because **acts before joining were never gated by any network**, so no permission is being withdrawn.

> **⚠️ This raises the stakes on OP-22, the open problem of minimum audit disclosure, and it is the strongest objection to the reconstruction.** A whole-life record is a dossier: birthplace, every residence, employment history, commuting distance, vehicles owned. **Disclosure is voluntary, but the incentive runs toward disclosing**, so the arrangement puts steady pressure on people to assemble exactly the record a surveillance state would want. §4.7's split of public market data from private personal ledgers now has to hold across a lifetime. **Registered, not solved.**

---

<!-- tag: fnd-s4-5 -->
### 4.5 It credits work

> **There is one credit. It is time spent by a person, recorded as material flow. Everyone earns at the same rate, and therefore influences at the same rate.**

**Production, service and enrichment are not different kinds of credit and do not credit at different rates.** They are three names for **how feedback reaches the work**, which is §4.6. **No rule may use them as an accounting boundary.** An apprentice plumber's single hour is at once learning a trade, fixing a customer's pipes, and turning copper into working plumbing. **That hour cannot be divided, and dividing it would need yet another convention** (§1.1).

#### Why enrichment is named at all

**To give grounds for crediting work no economy has ever credited.** Going to school is work, and today the student or their parents pay for it, which is the relationship inverted. Teaching your own child is work. Caring for a relative is work. **None of it is paid.**

**Enrichment is work whose benefit flows from all of humanity to at least one person, in ways not readily measured in material. It is credited because it is real work, not because it is virtuous.**

> **Childcare is creditable work regardless of who performs it.** This alone brings the largest uncounted labour pool in human history onto the books.

#### Keeping yourself alive is credited work, and that is where the floor comes from

**If work is time spent maintaining human life, then maintaining your own living body is work, exactly as caring for someone else's body is.** It credits because the time was spent. **That some of the maintenance is passive does not matter, because the measure is time and not effort** (§0).

> **This is the mechanism of the basic-needs floor, and it is not a grant.** A floor could never have been an issued allowance, because credit for no time worked is the abstract quantity A1 forbids. **Every living human performs the real work of staying alive, and it credits at the same rate as everything else. The floor is simply where that credit lands.**

**It is verified by proof of life** (§4.2), which is the strongest evidence there is and costs almost nothing to check.

**Its size is a network choice with a bound at each end, not a free dial.** Which activities count, and how many hours each takes, is set by each network (§5.5.1). **The value must be high enough that essentials stay affordable and low enough that the consumption gate still rations what is genuinely short.** Generosity here is product differentiation rather than a rule anyone imposes, **and it cannot be exported**, because a counterparty re-computes the backing through its own model (§4.2).

#### Training is paid when it happens, and never charged to anyone later

**A student is credited for their time while training.** The debit of training — teachers' time, facilities, materials — **is carried during the training years**, cushioned by the debit-room that pledgers grant for it (§4.6).

> **Nothing is charged downstream.** A doctor's care costs the recipient the doctor's time, the material cost of running the clinic, and the medicines dispensed. **The doctor's education is not in that bill.** It was underwritten up front, by the people who wanted doctors to exist.

**Pledging supplies the natural limit.** Society decides how many doctors to train by pledging for it. **Unpledged study still credits the student's time, because A7 requires real activity to be recorded, but it leaves them holding the debit.**

##### The general rule this is the first case of

> **A large up-front cost with a diffuse benefit is carried where it is incurred, and cushioned at that time by the debit-room the people who pledged for it grant. It is never charged onward to whoever happens to consume the result.**

**It covers education, media and creative production, research, infrastructure, tooling, and capital.**

**Two reasons, and the second is decisive.** Charging a cost onward means choosing a window — how many patients, how many viewers — **and every candidate window is arbitrary.** And charging onward never terminates: **amortise a hospital's construction into each patient's bill and the accounting must then chase the builder's costs, then the equipment maker's, then the steelmaker's, then the doctors' education, back to the first human activity.** Carrying the cost where it falls is what makes the arithmetic stop.

**The boundary is capital against consumption, and it is not a question of time.** A cost reaches a unit only if it was **consumed** producing that unit. **The two are told apart by physical fate: did the thing survive the process?** A drill bit that survives is capital. The oil it burned is consumption. **This is checked against the record of what happened to each thing, never by the producer's own declaration.**

> **⚠️ The honest limit: a first-time creator attracts no pledges.** The barrier is far lower than raising money, and the path is real — make small unpledged work, gather feedback, then attract pledges — **but it should be stated rather than assumed away.**

#### A durable asset carries its own making, shared by how long each person held it

**A building, plant or tool holds its creation-cost as debit on the asset itself.** That debit settles in three steps.

1. **Pledges grant the holders debit-room to carry it.** A pledge does not reduce the creation-cost. **It is a permanent grant of room**, drawn from the pledger's finite lifetime pledging budget (§4.6). **A facility is built at the scale the community will pledge for**, so pledges are both the authorisation and the brake.
2. **The full creation-cost is shared among the asset's holders by how long each held it.** Each holder's permanent share is their holding time divided by the total holding time over the asset's whole life. **Pledges cushion the bite; they never shrink the debit, because nothing may vanish** (A1).
3. **The basic-needs floor caps how hard any remainder bites** (§5.5).

**Why holding time, rather than an equal split.** Holding time is a physical trace, so the split is measured rather than invented. **And a new hire bears almost nothing**, which removes the entry toll an equal split would impose on exactly the capital-heavy essential work — hospitals, water treatment — that society most needs staffed.

> **A carrier moving goods takes no share of their making.** A haulier holding 1,000 toasters for two days did not make them. **Transit adds only the carrier's own transport debit.** Without this rule, the supply-chain model of §4.6 would quietly load the making of a toaster onto the truck driver.

##### The rule people attack most, with the numbers

**A barn costs 20,000 hours to build and lasts 20 years. The farm produces 40,000 kg of beef over that life.**

| | Hours per kg |
|---|---|
| What a critic says beef should carry: 20,000 ÷ 40,000 | 0.5 |
| **What beef actually carries from the barn** | **0.0** |

**The beef did not build the barn.** Under A1 only people act, so a cost attaches to the people who caused it, and **a thing causes nothing.** The 20,000 hours sit on the barn's holders.

**And that is not light.** At ρ = 1.2, carrying 20,000 hours of debit needs **16,667 hours of credit** standing behind it, against the roughly 3,650 hours a year a person accrues from staying alive. **The barn eats 4.6 years of one person's entire credit accrual, which is why nobody builds a barn they do not need.**

**Push it the other way and the cost lands on about 40,000 buyers who did not build it, do not hold it, and never had a say.** The one party who decided is the one party the cost would stop constraining. **The full argument, including a harm discovered eight years later, is in [`../01-wiki/property-debit.md`](../01-wiki/property-debit.md).**

> **⚠️ The honest limit.** Two producers of the same good, one with a 20,000-hour barn and one with a 2,000-hour shed, **publish the same figure per kilogram.** A buyer comparing those figures cannot tell them apart, because a unit's figure answers *"what did this unit consume?"* and never *"what does this producer's whole method cost?"* **What disciplines the barn is the builder's own gate, not the label on the beef.**

#### There are no patents, and attribution is by recognition

**Ideas replicate freely, and there is no exclusion.** Exclusion rights exist to let a holder take a profit from reproduction, and with no profit in exchange (A5) the machinery has nothing to protect.

**The right standard for attribution is *no worse than today*, not *perfect*.** Buy a painting from a gallery now and there is no video of its making. **Provenance only becomes fraught in the capitalised art market, where licensing and reproduction are the revenue, and that is the layer Aequitas removes.**

#### Not all work is capturable, and the system does not require it to be

**A critic will read A1 as demanding total surveillance. It does not.** People spend real time editing images and writing captions, and the results travel through conversation and entertainment. **Tracing who shared what to whom in order to assign credit is neither possible nor desirable.**

> **Much of what people do, they do to entertain themselves and each other. The system does not need to capture it, price it, or credit it, and attempting to would be both futile and grotesque.**

**The accounting covers what is claimed and attested. Everything else is life.** §4.2 states the other half: a network must say in advance what it does cover.

#### Work nobody can observe

**Creative and intellectual work is mostly thinking. It leaves no material trace and has no witness.** Crediting only what can be observed would exclude most of it. Trusting self-report without limit appears to invite unlimited fraud.

**Three mechanisms already close this, and none is new.**

1. **No account may claim more than 24 hours of activity in 24 hours.** The press only runs so fast.
2. **Weak evidence weighs near zero until something corroborates it.** Self-asserted, unwitnessed work carries the weakest basis and the lowest confidence, so a cautious weighting values it near zero. **This is an incentive rather than an enforcement rule: vagueness is cheap to assert and cheap to hold.**
3. **Pledges bound what anyone will underwrite.** Someone generating unwanted volume at scale attracts no pledges, and a pledge is the only thing that moves a claim from asserted to backed.

> **Read mechanism 2 alongside §4.2, because the two are easily confused.** Cautious weighting decides **how much a claim weighs inside a rule the network has already published.** It never stands in for a rule that was never written. **A network weighting a whole class of real work near zero has written the wrong rule, or has failed to write one.**

**Note what this does and does not claim.** Aequitas removes most of the acquisitive motive for fraud, because there is no wealth to concentrate. **It does not remove status-seeking**, which is exactly what a false claim of creative hours would be. The defence against that is evidentiary, per the three points above, and not motivational.

---

<!-- tag: fnd-s4-6 -->
### 4.6 It carries what people want made

**Cost says what a thing took. It does not say who wants one.** A network therefore carries a second kind of record, and it is not credit.

#### Feedback is not credit, and never converts to it

**Feedback is how a society signals what it wants more of.** The in-demand shoe sells out. Someone chooses you as their doctor. People applaud a piece of work. **Those already exist today as stock-outs, referrals and reviews.**

> **Feedback is non-convertible because it was never credit in the first place. There is nothing to firewall.**

**The live question is the inverse, and it is real: can feedback be bought?** A signal that credit can purchase would be a currency by the back door. **That is registered as an open problem and is not solved here.**

#### Pledges and signals, told apart by one test

> **Is it backed one-for-one by credit the person already earned?**

| | **A pledge** | **A signal** |
|---|---|---|
| Says | *"I authorise this work"* | *"I want this to exist"* |
| Backed by | **earned credit, one hour for one hour** | nothing |
| Rate | **A finite lifetime budget, equal to lifetime earned credit, spent once** | Many per hour earned, or unbounded |
| Permanence | **Permanent and non-revocable** | — |
| Looks like | Crowdfunding, commissioning a task, choosing a GP | Likes, ratings, applause |

**A pledge authorises creditable work. It need not involve an object and need not move any debit.** A resident who has earned 4 hours pledges 2 toward mowing the public verge. Someone with a mower sees the pledge, mows for an hour, submits evidence, **and is credited 1 hour. One pledged hour remains for a later mow.** No object changed hands and no debit moved. **The pledge summoned an hour of creditable work, and drew an hour from the pledger's lifetime budget to do it. The underlying credit never moved.**

**Why exactly one for one.** Pledges are permanent debit-room granted to other people. **Let the total exceed the pledger's own earned credit and you get more permanent room across the network than anybody's credit can stand behind.** That is a solvency constraint rather than a preference. **It is also the only stable value**: above one, pledging power grows until pledges filter nothing; below one, the directed economy shrinks to zero.

**Because the budget is spent once and never refunded, pledging is a real sacrifice.** Someone pumping influence can no longer pledge for free, and farming a task requires real verified colluders each burning their own finite budget, **visible on a public pledge ledger.**

**Why signals should be plentiful.** Under one-for-one you can only signal for as much as you personally worked, so you signal your top priorities and the system learns nothing about your second tier. **Cheap, abundant signals reveal the whole ordering rather than only its top slice.**

**Pledging is deliberately messy, and that is acceptable.** There will be unfulfilled pledges, frivolous pledges, and people learning to pledge well. Coordination groups will form around it. **A lever people organise around is a lever that works.**

#### Everyone alive holds some of this, simply by being alive

**Self-care is credit in full, so like all credit it generates pledging power.** Every living human therefore directs some share of what society works on next. **Because the floor is the same for everyone, this compresses the spread of influence to the same bound as consumption** (§5.5).

**Where it goes by default is a network choice.** A network may route a subscriber's self-care pledging power automatically toward basic-needs sectors, leave it for the person to direct, or split it. **Routing it automatically is the powerful case, because the pledging power of a whole population aimed at essentials funds essential provision from the act of staying alive itself.** The trade-off is the network's to make.

#### Recording is never gated. Verification decides when credit counts

**The work is always recorded.** An event is logged the moment work is done, so nothing is left with no origin. **What a pledge buys is authorisation and demand-room, not permission to record.**

**But a recorded credit only begins counting toward a person's position when the output is verified** (§4.2). **This is verification, not approval.** No committee judges the work worthy. The trigger is objective evidence that the output exists.

##### For goods, the hand-off is the verification

**When goods change hands, three things happen at once.** The receiver's acceptance attests the goods are real, **which makes the previous holder's credit count**. The material debit follows possession to the receiver. And the receiver's own labour, such as transport, is added and will count when they hand the goods on.

**Two consequences, both load-carrying.**

- **No downstream buyer can hold a maker's credit hostage**, because credit counts at the **first** hand-off to **any** receiver. And because debit follows possession, **a would-be gatekeeper's leverage inverts**: holding goods means holding their debit, so it is motivated to pass them on.
- **The count checks itself.** A receiver takes on the debit of exactly what they accept, **so they will never sign for units that do not exist.** The party harmed by an error is the one who catches it, and no dedicated auditor is needed.

**Who carries the risk that goods do not sell.** Unsold goods are unrealised credit plus inventory debit on whoever holds them. **In speculative production the producer holds them, and the risk falls on everyone who worked the run, shared by hours worked and never dumped by rank.** In pledged production the pledges grant permanent room that can be relied on, **which removes withdrawal risk but not demand risk** — taking the finished good is always a separate act.

#### When a task attracts more pledges than it costs

**The surplus is not a payment to the doer and is not consumable.** Treating it as spendable would be a scarcity price, which A5 forbids.

> **The surplus becomes an earmarked reserve that activates only against a verified future cost traceable to that task** — the doer's later injury or illness, remediation that resurfaces, harm to a third party.

**Four rules govern it.** Shares split by hours on **that task**, so cover reaches whoever did the work. **Causation is decided by the physical-trace test**, and diffuse harm with no individual trace is handled by a cohort convention rather than an open claim. **The reserve is a buffer and not a shield**: once exhausted, remaining task-caused debit falls back on the doer under the ordinary rules, **or carelessness would be licensed.** And an abandoned task's pledges are burned, which is what disciplines frivolous pledging.

**What this buys.** Onerousness has two halves. **This gives the hazardous half an incentive with no wage premium, no rate-scaling and no rating authority**: society de-risks the toxic-cleanup worker exactly to the extent it pledges for the work. **It leaves the tedium half open**, because dull but safe work generates no causal tail and therefore no reserve.

#### Why a pledge is a better demand signal than a price

**The standard objection is that without a price, nothing decides how much gets made or who gets it.** That objection rests on three assumptions, **and all three are false in a concentrated market.**

| The assumption | What is actually the case |
|---|---|
| Scarcity is a physical fact the price reports | **Much scarcity is produced.** Supply is held back to hold the number up. |
| Demand is a fact the price reports | **Demand is manufactured, at industrial scale.** That is what the advertising industry is for. |
| So a price honestly reports what people want | **The same firms set supply and work on demand. The price partly reports its own producer.** |

> **So the objection assumes the price is a clean instrument. It is not. Aequitas is not replacing an honest demand signal with a worse one. It is replacing a signal the seller helped write.**

**What a pledge does that a price cannot: it cannot be advertised into existence.** It is backed by hours the pledger worked, it is spent once, and it is public. **A firm can make you want something. A firm cannot put more hours in your day.**

**And the lever is far more evenly spread, which is measurable.** Money's top tail reaches about **10⁶ times** the median. **Pledging power cannot exceed 24 ÷ F**, which is about **2.4 times** at a ten-hour floor, **and that is an absolute maximum nobody reaches** (§5.5.5). **Every living person holds some.**

**The full argument, with Braudel's two layers and the worked examples, is in [`OP-9_calculation_reply.md`](OP-9_calculation_reply.md) and [`../01-wiki/pledge-and-signal.md`](../01-wiki/pledge-and-signal.md).**

> **⚠️ What this does not answer.** **Two people, one radicchio. Pledges say how many get grown. They do not say who gets the last one.** That is a distribution question with a separate answer — a queue, a lottery, or pledge-priority, decided where the physical thing is handed over (§5.5). **Cost states what a thing took. Who receives a physically scarce output is a different question, and this document deliberately does not settle it.**

> **⚠️ And it does create a popularity contest.** Whoever is already liked attracts the most pledges. **That is a known open problem, not a new one.** The bound on it is that every pledge costs a real person a real hour from a finite budget.

---

<!-- tag: fnd-s4-7 -->
### 4.7 It publishes its own workings, and settles disputes

**A network asks people to rely on its arithmetic. What it owes in return is that anybody can re-run it.**

#### The market is public. Persons are private

> **Transparency here is split by level. Pledges, production quantities, hand-offs and the figures things carry are public. Individual people's positions are private.**

**A pledger may be anonymous, in the way a crowdfunding backer is, but the pledge itself is visible.**

**That split does real work rather than being a compromise.** Public market data is what makes independent auditing possible at all: a worker can read how wanted their product is, an auditor can watch a supply chain, and **nobody can privately mislabel pledged work as speculative when the pledge ledger is public.**

**This is roughly where society already sits.** People transfer money today knowing their counterparty and nothing about third parties' accounts, and nobody audits those accounts because that trust is handed to banks. **Aequitas does not need more visibility than that. It needs the same visibility with the trust moved.**

**And it does not replace existing recourse.** Courts, small claims, contract law and ordinary social pressure continue to exist and continue to handle fraud between people.

> **⚠️ The narrow question this leaves is OP-22, and it is unsolved.** The bank analogy has one gap: **there is no bank to hand validation to.** An auditor must be able to see *something*. So the live question is not *"surveillance or privacy"* but **"what is the least an auditor must see to check a claim without seeing a history?"** Proofs that reveal nothing but the answer are the right shape. **The precise set of what must be disclosed does not exist yet**, and public pseudonymous events can be analysed to identify a person, which is the classic ledger-privacy problem.

#### How private, exactly, is the network's own choice

**The network does the tallying, so it is the party holding what is private, and therefore the party that decides how privacy works.**

> **Each trust network sets its own privacy practice. Aequitas states the principles and does not dictate the implementation.**

**A network may run something like a card scheme, where neither party learns the other's details and the intermediary knows both sides.** It may instead run **complete transparency, with no personal privacy at all.** Nothing in the axioms forbids either, and some communities will want the second.

**This is the same kind of dial as ρ and the floor.** Aequitas uses those values and never sets them. **A single global privacy setting would be exactly the central authority A8 forbids.**

**And opacity is discounted rather than forbidden.** A counterparty re-computes a claim through its own model and **discounts what it cannot check**, so a network choosing heavy opacity finds its members' claims trade at a discount elsewhere. **A network's privacy level becomes a property of its output rather than a rule anyone enforces.**

**Three consequences follow, and none of them is small.** Each is registered rather than solved, and each is worked in [`../01-wiki/privacy-is-a-network-choice.md`](../01-wiki/privacy-is-a-network-choice.md).

| | |
|---|---|
| **The network becomes the most information-rich actor in the system** | Whoever tallies, holds. A network keeping its members' lifetime reconstructions holds a concentration of *information* comparable to the concentration of *wealth* this project exists to remove. **Unanswered.** *"You may leave"* is a weak exit when what you would leave behind is your life history. |
| **Privacy has a measured cost in coverage, and the measured number says the trade-off is not close** | Privacy-preserving checking is dearer than open checking, and that direction is real. **The failure point is roughly 200 times higher than anything a working network would report.** A network should publish what its practice costs; it does not have to trade coverage away to have one. |
| **A network's choice binds people who did not make it** | Children born into a transparent network, and people who joined before a practice changed, did not choose it. |

#### What a network owes

**Tallying is a computation, not a judgement made case by case.** The estimate for an unmeasured producer, the leftover arithmetic, the cohort model — these are algorithms.

**That matters more than it sounds, because it makes *"cite your method"* enforceable.** Against a human process that is an aspiration. **Against a published algorithm it is a version number**, and anyone can re-run it on the same inputs and get the same answer.

> **To be trustworthy a network publishes every estimating number it uses, every method, and anonymised data covering all of its participants. A network that will not show its arithmetic is asking to be trusted rather than checked, which is the thing this system exists to stop needing.**

**How much to reveal about institutions, co-operatives and individual businesses is the network's own call**, balancing the confidence transparency earns against the privacy its members want.

> **⚠️ And this cuts against itself.** Anonymised participant data becomes **more** re-identifiable the more of it there is. **Publishing more to earn trust also publishes more to identify people by.** A network is choosing on that axis whether it means to or not.

##### "Funding" is not a budget. It is recognition

**There is no treasury, no allocation and no grant.** Asking who *funds* an auditor imports a question from money that does not survive translation.

> **Funding, in Aequitas, is simply the recognition of an activity as creditable.**

**Audit work is work.** It is recorded when it happens, and recording is never gated on approval. **So the credit for doing the work was never scarce and never needed a funder.**

**What *is* scarce is demand and verification.** A pledge says someone wants the work done, and verification decides when the credit counts.

##### A network's own founding is recorded like any pre-existing thing

**A network cannot be paid by an accounting that does not exist yet.** The network is created first, and **whether its founders take credit for creating it is the network's own decision.**

**This is not a special case.** It is the ordinary treatment of a thing that existed before the ledger: an estimated entry, made after the fact, open to being superseded when better records appear.

**A network may document its founding carefully, thinly, or not at all. All are permitted, and they differ in what they earn.** The founding record is the first thing about a network anyone can check, so it is a signal about all the rest. **Nobody has to forbid a bad founding record. It simply does not attract anyone.**

**Three things bound the damage anyway.** Founding credit is capped at wall-clock hours multiplied by the number of founders, which anyone with a calendar can check. It is publicly recorded, so a later network re-computes it. **And because credit is non-transferable and consumption is gated by ratio, over-crediting founders buys only consumption room, bounded like everyone else's** (§5.5).

#### How a dispute resolves

**Ask the laboratory question: how is a dispute in science resolved?** By replication, published method, and dated records for priority. **There is no adjudicator, no supreme court of physics.** Both claims stay in the literature, nothing is withdrawn, and often the dispute is never resolved at all, only outlived.

**Aequitas already has every one of those**, written for other reasons: two unaffiliated replications before a constant may re-weight history, published numbers and methods, no central authority to appeal to, and an append-only log where a rebuttal is appended rather than replacing anything.

##### Where the analogy breaks, and this is the part worth having

**Science can afford an unresolved dispute. An accounting system often cannot.** A field can stay divided for thirty years and lose nothing. **But a purchase either clears or it does not, now.**

**Sorting disputes apart removes three of the four kinds.**

| A dispute about | How it resolves | Needs a verdict? |
|---|---|---|
| **The physical record** — did 70 g of wheat actually move? | **Arithmetic.** The integrity checks recompute it. **This is not a dispute; it is an error, and recomputation says whose.** | No |
| **The weighting model** — what does a tonne of CO₂ cost? | **Nobody has to accept anyone else's model.** Each party re-computes the shared physical record through its own weights and decides for itself (§4.2). | **No** |
| **An estimate for something unmeasured** | Published method, and anyone can re-run it. The figure carries its interval and its label, and better evidence supersedes it (§4.4). | No |
| **Fraud** — someone recorded events that never happened | **A finding of fact, and it needs one.** | **Yes** |

> **A transaction never waits on a shared verdict.** Each side computes its own answer over the same physical record and decides whether to trade. **Disagreement about weights does not block commerce. It means two parties read the same thing differently, which is a fact about models rather than a deadlock.**

##### What correction looks like — nothing is reversed

> **The past transaction is not reversed. The fraudulent credits are negated, the ledger rebalances, and the person's ratio may now be too low to buy anything until they hand on some of what they hold.**

**Reversal would be wrong rather than merely difficult.** The goods moved, and you cannot un-eat a sandwich. **The counterparty acted on the record as it then stood and was credited for work that really happened. Unwinding the buyer's fraud would corrupt the seller's books to punish someone else's lie.**

**So the correction is arithmetic and the consequence is automatic.** The fake credit is negated, so credit falls. Debit does not, because they really did take the things. The gate now fails, so discretionary purchases stop. **Selling restores the ratio, because material debit is dischargeable on transfer.**

**Three things follow that are not obvious.**

- **Consumption debit cannot be sold off.** If what they took was eaten, burned or emitted, selling does not help. **They cannot trade their way out.**
- **There is no bankruptcy, and there need not be, because there is time.** Credit accrues to everyone alive at the floor, whatever their standing, so the ratio recovers on its own. **The recovery period is the faked credit divided by the rate they now accrue**, which means **the consequence is exactly the size of the fraud, measured in time, and nobody sets it.** A person who faked ten years of credit works off roughly ten years.
- **Influence corrects the same way.** Negating credit can put a person retroactively over their lifetime pledging cap. **The pledges themselves are permanent and the work they summoned really happened, so nothing unwinds. They simply cannot pledge again until credit recovers.**

> **⚠️ One real load stays, and it is not a disagreement about weights.** Deciding whether a **particular past task caused a particular later harm** is a contested finding of fact wherever no physical trace exists. **It routes to existing recourse, like fraud does. Registered, not solved here.**

---

<!-- tag: fnd-s4-8 -->
### 4.8 It takes people in, it merges with other networks, and it can end

#### Joining replaces an assigned average with your real record

**Two forces make joining rational.** Most people's true footprint is **below** their cohort average, and **their estimated credit does nothing until they join.**

**The pitch is: here is what you have contributed, here is what it cost, join and make it yours.** For a median person the reconstruction is a windfall, worked in §4.4.

**The cost of joining is administrative labour, not a penalty.** A producer without instruments genuinely needs more human hours to produce the same verified record, and those hours are a real material cost rather than a thumb on the scale. **The incentive to instrument is the ordinary incentive to reduce a real cost.**

> **⚠️ Watch item: fixed joining costs consolidate industries.** Documentation burdens are repeatedly argued to disadvantage small producers, which is why organic-certification cost-share programmes exist at all. **The structural offset is that helping someone join is credited work borne by the network rather than the entrant. Whether that is enough is empirical and should be watched rather than assumed.**

#### There is entry, and there is no exit

**Entry is joining. There is no matching act on the way out.**

> **Once records of a person exist they are never destroyed. They are only added to, including after that person's death.**

**Two things are easy to confuse.** **Ceasing to participate** — stop transacting, stop holding an account, live in the gift economy — **is always available, and nobody is enclosed.** **Erasure** — removing the record that you existed and what you did — **is never available.**

**And erasure was never available even before you joined**, because participation is voluntary while coverage is not (§4.1). **There is no state of not-being-in-the-books to return to.**

**Permanence is a requirement rather than a policy.** Re-weighting recalculates every affected ledger when the science improves, and joining reconstructs a life back to birth. **Neither is possible over records that were deleted. A log that can be truncated is not a log.**

**On death, a person's record closes but persists.** It stays re-weighable, because the figure describes what happened and what happened has not changed. **Credit does not transfer, and nothing is inherited on the credit side.** Material debit transfers with the things, as in any hand-off. **Consumption and pollution debit does not move.** That is not a punishment reaching past death. It is the record continuing to say who did what.

> **One consequence follows from all of this. Because deletion is unavailable, publicity is the only privacy control that exists** (§4.7). **There is no falling back on erasure**, which raises what §4.7 has to carry. The full note, including the erasure-law reading, is in [`../01-wiki/permanence-and-death.md`](../01-wiki/permanence-and-death.md).

#### Networks federate by agreeing methods, not answers

**Two networks do not negotiate a person's balance.**

> **Merging means agreeing every rule — the floor, ρ, the weighting model, and how a human is identified — after which the merged network computes one answer from one log. Until they agree, each keeps its own book and neither is wrong.**

**So two networks that cannot confirm that two pseudonymous accounts belong to one person cannot merge.** A network requiring a face scan, a fingerprint and a voice check cannot merge with one requiring only a card scan. **Proving one human holds one account across two registries is a precondition of merging, not an open problem in the accounting.**

**A merge is not a special event.** When two networks federate and a person's two accounts become one, the adjustment is **exactly as ordinary as the adjustment made whenever new data arrives.** Positions are computed from the log and never stored, so **there is nothing to migrate and no new machinery to build.**

> **The expected trajectory is convergence.** Networks that federate are expected to keep federating and to merge over time, rather than settling into permanently separate regional systems. **What that buys: one ledger per person, no coverage gaps at the seams, and no arbitrage between incompatible standards.**

**Trust networks are laboratories rather than banks. Their goal is truth and their motive is agreement rather than competition.** A network whose methods let fraud through is **helped** by another network sharing the methods that catch it. **This does not rest on anyone being virtuous**: two networks often draw on the same outside evidence, so a bad method in one corrupts the books of the other.

**And convergence is deliberately out of scope as a capture problem**, for reasons worked in [`../01-wiki/ledger-ecosystem.md`](../01-wiki/ledger-ecosystem.md). The short form: **a monopoly earned by better methods is not the monopoly capitalism produces**, because methods are published and replicable, so **the monopoly is over which method is used and never over who may propose one.** There is no moat, because there is no exclusion.

> **⚠️ The watch item, stated as one rather than as a defence.** A monopoly earned on merit can stop being meritorious and keep the position. **The guard is publication plus replication, not competition** — so if publication ever weakens, the merit argument weakens with it.

#### Trading across the money boundary

**Aequitas has to be usable by someone who still uses money.** Every participant, for years, will have most of their counterparties outside. **A design that only works once everyone is inside cannot get anyone inside.**

**Both directions are permitted and both are dearer than trading inside.**

| Direction | What happens |
|---|---|
| **Selling into Aequitas** a good made with money-bought inputs | The good is unrecorded until it is sold in, because its inputs never passed through a hand-off here. At that hand-off the maker either records its origins properly **or applies a published template that assigns a figure immediately.** **The maker spent money making it and receives none, and that is the disincentive.** |
| **Selling out of Aequitas**, for money | Permitted. **The debit stays with the seller**, because no participant took the goods on. **To the network the seller made a gift, and the network does not acknowledge the money changing hands at all.** |

**Money is invisible because it is not physical.** A1 already says paper claims never appear on any ledger, so **a payment in money is not an event.** The goods moved and the ledger records that. **No cross-boundary rule exists or is needed.**

**The only new object is a template**, which is a cached estimate for a class of good, published with its method and its vintage. **It must err against the seller**, or recording properly never pays and the template becomes the preferred route.

> **Goods cross the boundary. Standing does not.** Follow a wealthy person paying a hundred workers in money and selling the goods into Aequitas. **The workers are credited their own hours**, because credit records who was responsible. **The financier worked none of those hours and is credited nothing.** **There is no channel from money to credit, at any scale. You cannot buy hours.**

**And extraction exhausts itself.** Buying inside takes on the debit; selling outside never discharges it. **So debit grows with every unit extracted while credit grows only with the extractor's own hours, capped at 24 a day. Their own gate shuts them out, and it shuts faster the harder they pull.**

**The same holds for an organisation**, because an organisation's debit is at all times its members' debit, divided by hours worked. **Closing it and opening another moves nothing.** Full paper: [`OP-27_parallel_implementation.md`](OP-27_parallel_implementation.md).

> **⚠️ What stays open.** Whether a person can hide behind a **fake or borrowed membership list** — claiming hours for people who did not work them, or leaving their own name off. **That is a verification question rather than an accounting one.** The accounting has no hole here; the identity layer still has to do its job.

---

<!-- tag: fnd-s5 -->
## 5. Consequences

<!-- tag: fnd-s5-1 -->
### 5.1 Capitalism cannot function
**A5 (cost, not price) means there is no profit in exchange** — a thing's figure is what it consumed, and nothing may be added to it. Embodied-material debit releases on transfer; self-work nets to zero while held (§3.2). **No rent, no rental income, no property speculation, no compounding capital.** Not banned — structurally impossible. *Ellerman's route reaches the same conclusion independently: only people act, so only people can be responsible, so capital cannot claim a residual.*

**The exploitative employer is structurally hollowed out**. The wage-extraction employer has no mechanism to exist: credit is non-transferable, so there are **no wages** to pay (A3 (non-fungibility)); a thing's figure is what it consumed and nothing may be added, so there is **no surplus to appropriate** (A5 (cost, not price)); and a team's debit is shared **by hours worked, not by rank** (§4.5), so a supervisor **cannot dump risk or cost onto subordinates**. Workers are credited by the *system* for their hours, not paid by a boss. **What survives is coordination** — organizing a process, directing what gets made, controlling access to desirable projects — and that residual power is real: it is the **coordinator-class problem (P4 (coordinator class))**, the live blocker, not the extractive employer this system already forecloses.

**What survives, and is load-bearing: competition on efficiency.** A5 removes margin, not rivalry. §3.3a leans on this directly — rival sectors auditing each other's cost constants is the only thing standing between the weighting model and systemic under-costing.

<!-- tag: fnd-s5-2 -->
### 5.2 Exploitation and pollution self-penalize
Harmful production carries the remediation cost of the harm. But — per §3.2b — that cost is permanent **on the producer who caused it**, not on the product that leaves the gate. So the penalty is **direct**: a polluter carries permanent pollution-debt, a poor efficiency ratio (§3.5), and restricted discretionary consumption (§5.5), whether or not any consumer ever notices.

**This is *stronger* than the consumer-mediated gradient it replaces.** The old framing ("dirty products cost the buyer more") leaned on consumers choosing the cleaner good — historically a weak force, because the cheap dirty product usually wins. Pinning the debit to the producer removes that dependency: exploitation and pollution self-penalize at the source. And the consumer signal is **not lost** — the good still carries a non-transferable provenance record (§4.4, §3.2b), so buyers and pledgers can prefer low-pollution producers on top of the direct penalty. The incentive gradient reverses without regulation, on both channels.

<!-- tag: fnd-s5-3 -->
### 5.3 Regulators invert into services
An EPA-like body becomes something businesses **actively want**, because it helps them lower their debit-cost. Enforcement becomes consulting.

<!-- tag: fnd-s5-4 -->
### 5.4 Taxation is unnecessary
Civil servants are credited directly. Infrastructure users carry proportional debit by usage. There is nothing to collect.

<!-- tag: fnd-s5-5 -->
### 5.5 The basic-needs floor

#### 5.5.1 What the floor is

**Terms used in this section.**

| Term | What it means |
|---|---|
| **The floor**, written `F` | The hours a day a trust network counts as the work of keeping a human being alive. |
| **Trust network** | The organisation that keeps the books and sets `F` for its own subscribers (§4.0). |
| **ρ** ("rho") | The network's debit tolerance. The multiplier in the consumption gate `D ≤ ρ·C` (§3.5). |
| **`C`** | A person's cumulative credit — the hours of their life the books have recorded as work. |
| **`D`** | A person's cumulative debit — the material and energy the books have recorded against them. |

> **The floor is credit for time a person spends on the activities their trust network counts as essential to staying alive.**

Those activities are **sleeping, eating, defecating, and keeping oneself clean.** A network may count more, or fewer, or hold them to shorter durations. **The list and the hours are the network's to set, and networks will differ.**

**That is why floors differ, and the differences are not arbitrary.** One network counts eight hours of sleep and lands near 10 h/day. Another accepts the argument that four hours of sleep suffices and lands near 6 h/day. A third counts sleep alone and lands near 8 h/day. **A fourth counts only the hours a body cannot avoid and lands near 2 h/day.**

**This is partly a question of opinion and partly a question of fact.** People disagree about how much sleep a human needs. **They are also disagreeing about a number that decides whether the network's economy is stable** — see §5.5.3.

---

#### 5.5.2 The floor follows from the axioms. It is not an allowance

**The floor is not a grant, a payment, a benefit, or an income.** Nothing is issued to anybody. **It is the ordinary result of applying two rules the system already has.**

| Step | The rule | Where |
|---|---|---|
| 1 | **Credit is a record that a person spent time on work.** Not effort, not output — time spent. | **A2** (time as measure), §4.5 |
| 2 | **Maintaining a living human body is work.** Doing it for somebody else is work, so doing it for your own body is the same work. | §4.5, §4.5 |
| 3 | Therefore **a living human accrues credit for the hours spent maintaining themselves.** | §4.5 |
| 4 | **Every human is in the books whether they participate or not**, and a verified living person demonstrably did that maintaining. | **A7**, §4.2 (proof of life) |

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

#### 5.5.3 The floor's value is an economic setting, with a bound at each end

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

> **The gate then stops binding on almost everybody.** `D ≤ ρ·C` still holds, but it is not the thing deciding who gets what. **Where the economy can actually deliver that much, this is abundance and it is the intended end state** (§3.5, Q6). **Where it cannot, physical shortage is decided at the point of distribution instead — by a queue or a lottery** (§3.4a, §4.6) — **and the accounting has stopped doing the work it was set up to do.**

##### What the project owes here

**Aequitas does not set `F` and must not** (A8). **What this project owes is a demonstration that a stable value exists** — that for a given economy there is a band of `F` and ρ inside which essentials are affordable and the ledger still rations what is genuinely short.

> **⚠️ Owed: a simulation showing the stable band, and its width.** Registered with **OP-4 (debit tolerance)**, which already holds the floor's magnitude and the ceiling's denominator. **Nothing in this section claims the band has been found.**

---

#### 5.5.4 Essentials are always affordable, by arithmetic first

**Two separate things make essentials reachable, and they are usually confused.**

> **1. The floor's own arithmetic. A person's credit for staying alive is sized to cover what staying alive costs.** This is the ordinary case and it covers everybody, however little else they do. Nobody is assessed, nobody applies, and nobody decides they qualify.

> **2. A backstop for the abnormal case. A restriction arising from a person's standing reaches non-essentials only.**

**The second exists because of measurement error, not because of poverty.** A producer over-assigned for years would suffer real harm before §3.3 corrected the record — the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal). **The backstop caps that exposure at restricted non-essential consumption for a period, followed by correction.** It applies on the same terms to somebody found to have committed fraud (§4.7).

**The floor does not require anybody to spend it on essentials.** A person may put their room toward anything they like. **The guarantee is that they can afford what they need, not that they must buy it.**

> **The floor is therefore not only a welfare provision. It is the error tolerance of the whole accounting.**

**None of this is a conformance requirement, and it must not be written as one.** Whether essentials are actually affordable in a given network depends on the value it sets for `F`, the value it sets for ρ, and what its economy can physically deliver — **so it is a result a network achieves, not a property an implementation has.** Setting the two dials so that it comes true is the network's job (§5.5.3). *(A conformance row saying otherwise existed from v0.18 to v0.24 and was deleted; see `Aequitas_Conformance_v0.6.md` §4.)*


---

#### 5.5.5 The disparity ceiling — an absolute maximum, not an expected spread

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

**Person N shows the second one.** An infant learning to speak is spending time on something. **A network may count all of that non-floor time as learning, or none of it, or some.** §4.5 already says learning is work, and **A8 already leaves the list of always-creditable activities to the network.**

**The choice moves the reachable maximum:**

| The network's choice on childhood | Highest reachable lifetime ratio |
|---|---|
| Credit a child's learning time in full | **2.400×** — the arithmetic ceiling is reachable |
| Credit none of it | **2.085×** — nobody can reach the stated ceiling, ever |

> **A network that does not credit childhood has a stated ceiling of 2.4× that no subscriber can reach, and its most industrious subscriber falls short of it for a reason that has nothing to do with how hard they worked.**

**This is a second dial on the same number, and it was not written down before.** It belongs with `F` under **OP-4 (debit tolerance)** and with the always-creditable list under **A8**.

##### Four conditions on the bound

1. **The value of `F`.** The ceiling **is** `24 ÷ F`, so a network with a 2 h floor states a 12× ceiling. **The result is only as tight as floors are generous.** `F` is a network choice (§4.5, A8).
2. **The network's treatment of childhood**, per the table above.
3. **No fraud manufactures hours.** IC-7 caps a day at 24 hours, but collusive hand-offs could still inflate gross hours (**OP-1**, service → influence). The bound assumes that channel is controlled.
4. **It is a statement about one network's books.** Nothing else.

##### What condition 4 replaces, and why

**Through v0.22 this section carried a fifth condition claiming the bound held *"across any set of networks compatible enough to interoperate"*, on the ground that compatible networks *"arrive at the same ledger for the same person."* Both halves are withdrawn** (author ruling, 2026-08-25).

- **Networks do not trade with each other, and no book is ever added to another book** (§4.0). There was no object for a cross-network bound to describe.
- **Compatible networks do not arrive at the same figure, deliberately.** §4.2 is **comparison, never conversion**: each party re-reads the shared physical record through its own model. Two networks with different floors report different credit for the same day, and both are right.
- **A merge requires consensus on every rule, identity included** (§4.8, §4.0). Networks that cannot confirm two pseudonymous accounts belong to one person cannot merge.

> **The comparison against money is unchanged, and it is a fair one.** Money's spread reaches about **10⁶ ×** the median **within one country's own statistics** (SCF 2022 and Forbes). The bound above is the spread within one network's own books. **Two sets of books, compared like for like.**

*(Note for review: old conditions 2 and 3 — floor-shopping arrested by counterparty re-computation, and that guard's dependency on **OP-22** — are narrowed by the ruling rather than removed. Under §4.0 a seller chooses which network a transaction lands on, so a network with an implausible floor loses sellers. What remains of the OP-22 dependency is proving a **pledge's** backing across a model boundary, §4.2. **Flagged for the author rather than settled here.**)*

---

#### 5.5.6 Why hoarding does not beat the bound

**Credit `C` and debit `D` are cumulative running tallies derived from the event log** (A6), and **credit is never spent** — a purchase adds to `D` and never subtracts from `C`, because credit is not a currency (A3).

**So `D ≤ ρ·C` is a ratio re-checked at every event, not a balance drawn down.** A person who consumes nothing for decades and then spends heavily can only bring forward their own allowance, which is bounded by `ρ·C`. **There is no stored lump to release.**

**At equal age, two people's cumulative credits stand in a ratio of at most `24 ÷ F`, so their cumulative consumption does too.** The only spread beyond it is age — time lived, not class. **A 60-year maximum worker against a 20-year floor-only person is 3 × 2.40 = 7.20×**, confirmed in the simulator (`06-simulation/statera/`).

---

#### 5.5.7 What the simulations found

> **Formally stated, simulated, and stress-tested.** The formal statement and a plain-language explainer are in `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`. The adversarial pass of 2026-08-14 answered all three attacks — **Methuselah** (§5.5.6 above), **dynasty and household** (a household is a co-op; its dwelling debit splits per occupant by dwelling time, children included, so the bound is per person and inheritance dilutes it, §4.5), and **collector** (holdings raise your own debit, so a hoard bounds itself).

`06-simulation/disparity-ceiling/disparity_ceiling_sim.py`, N = 200,000, gate `D ≤ ρ·C`, credit in `[F, 24]` h/day, 7 self-tests green:

- **The `24 ÷ F` ceiling is exact and does not move with ρ**, because ρ cancels in `ρ·24 ÷ ρ·F`. It also does not move with the weighting model, so **the headline result does not depend on OP-10.** On the same synthetic population, money's spread is 14× on income and roughly 700–950× on wealth.
- **ρ behaves like a prime rate.** A ρ can be chosen so that aggregate demand matches productive capacity, and it moves sensibly under shocks. Against the median-lifestyle anchor the baseline clears at **ρ\* ≈ 1.2**, a −30% capacity disaster tightens it to ~0.68, growth loosens it to ~2.2, and a +25% pollution re-weighting tightens it to ~1.0. *(Absolute values are illustrative and depend on OP-10; the directions are robust.)*
- **Efficiency, not extra labour, is what reaches abundance.** The same population is mildly short under the wasteful US production method and reaches everyone's full desired standard under German, Japanese or Spanish efficiency (Q6). **The binding constraint is physical throughput** (§3.5).
- **The ceiling is fraud-invariant.** IC-7 bounds every account, honest or not, so the most a fraudster reaches is `ρ·24` — the honest maximum. **Fraud fills the band and cannot create an outlier beyond it.**

> **What the simulations have not yet done, and it is now the more important of the two:** find the **stable band of `F` and ρ** described in §5.5.3. The existing runs take `F` as given. **Owed, with OP-4.**

---

#### 5.5.8 The real-distribution comparison

`06-simulation/scenario-suite/q4_locked_ledgers.py` applies the bound to real US and world distributions under the **material-only** rule (A1's corollary), asking what fraction of people would sit past a permanent lockout — non-essential consumption held at the floor for life because their sustained footprint exceeds `ρ · 24 h/day`, the most any human can earn.

- **Stripping the financial layer collapses the top of the distribution by about 1,000×.** Money wealth reaches ~10⁶× the median, but material **consumption** only ~670× (Oxfam billionaire personal footprints), because consuming physically takes bounded time. **The spread the bound has to cap is far smaller than the monetary one.**
- **Only a thin slice is locked.** Material-only, about **0.1–2%** of Americans are permanently locked, ρ-dependent, around 0.5% at ρ = 1.5. **These are the ultra-consumers, not the merely rich**, and fully divesting material property does not save them, because consumption debit is permanent (§3.2). **Meanwhile about two-thirds sit below their cohort average and would gain room by joining** (§4.8).

<!-- tag: fnd-s5-6 -->
### 5.6 Why the alternative-economy graveyard does not apply

A century of local currencies and time banks failed in three distinct ways. Aequitas is immune to one of them by construction, and should say so.

| Failure | What happened | Aequitas |
|---|---|---|
| **Circulation** | Ithaca HOURS businesses were *"drowning in Hours"*; Burlington Bread piled up at cafés with no way to recirculate. Scrip flows to whoever buys inputs outside the network and stops. | 🟢 **Cannot occur. There is no medium of exchange.** Credit never moves (A3); only debit moves, attached to its object. Nobody can drown in credit they cannot spend because nobody ever receives credit *from* anyone. |
| **Valuation** | Warren (1830) could not reconcile labour-for-labour with skill and disagreeableness. Time banking, 45 years on, still reports chronic skill shortage from flat-hour crediting. | ⚠️ **Partly answered.** A2 (time as measure) v0.3 makes training paid work, which addresses skill. **Onerousness remains open — OP-16 (onerousness gap).** |
| **Institutional** | Wörgl's scrip was suppressed by Austria's central bank *for working*, under the legal-tender monopoly. Ithaca died when its founder moved. | 🟢 **No issuer, no notes, nothing to counterfeit** — the legal instrument that killed Wörgl does not fit an accounting system. This is the substantive reason Aequitas must never be described as a currency. ⚠️ Founder dependency is answered only by §2's fourth screening question. |

A3 therefore does three separate defensive jobs: it forbids accumulation (§5.1), it makes permanent aggregate net-debit survivable (§3.5), and it makes the circulation failure impossible.

---

<!-- tag: fnd-pointers -->
## 6. Where the rest of the project lives

**This document states the system. Four things that used to sit here now live where they belong.**

| What | Where | Why it moved |
|---|---|---|
| **The conformance requirements** — what must be true for an implementation to *be* Aequitas | [`Aequitas_Conformance_v0.6.md`](Aequitas_Conformance_v0.6.md) | It is written for implementers, and this document is written for anyone. |
| **Every open problem and every answered objection** | [`Aequitas_Objections_v0.23.md`](Aequitas_Objections_v0.23.md) | The register is the record. A ranked summary here only went stale. |
| **How adoption plausibly starts** | [`Aequitas_Strategy_v0.6.md`](Aequitas_Strategy_v0.6.md) §5 | It is a reading of the historical record, not a statement of the system. |
| **The version-by-version change history** | **Held locally and not published.** These documents carry what is currently true; the history is read only when tracing when and why something changed. |

---

*End of v0.28 — restructure in progress.*
