<!-- generated-from: Aequitas_Foundations_v0.33.md -->
# Aequitas — Foundations, distilled

> ## ⚠️ THIS FILE IS GENERATED. DO NOT EDIT IT.
>
> **Every edit belongs in [`Aequitas_Foundations_v0.33.md`](Aequitas_Foundations_v0.33.md), which is the document this was made from.**
> An edit made here is lost the next time anyone runs the generator, and while it survives it is a
> second version of a rule — which is the failure this file exists to avoid.
>
> **Regenerate with:** `python bin/distill.py`

> **Source:** [`Aequitas_Foundations_v0.33.md`](Aequitas_Foundations_v0.33.md) · **version 0.33**
> **Generated:** 2026-08-28
> **Size:** 96,189 bytes, from 201,017 — **48% of the source**

**What was kept:** every heading, every rule, every table, and the stated result of every worked
example. **What was dropped:** the explanation prose between them.

> **So this file is complete on rules and incomplete on reasoning.** If a rule here looks wrong or
> arbitrary, **the argument for it is in the source at the same section number.** Read that before
> concluding the rule is unsupported.

**Section numbers match the source exactly**, so a citation taken from here is valid there.

---

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
- [2. What the axioms imply](#2-what-the-axioms-imply)
  - [2.1 The three criteria, and why they are the test](#21-the-three-criteria-and-why-they-are-the-test)
  - [2.2 Debit](#22-debit)
  - [2.3 Credit](#23-credit)
  - [2.4 Transactions and sales](#24-transactions-and-sales)
  - [2.5 Measurement and convention](#25-measurement-and-convention)
  - [2.6 What this document answers, and what it does not](#26-what-this-document-answers-and-what-it-does-not)
- [3. The Ledger Model](#3-the-ledger-model)
  - [3.0 What a ledger is](#30-what-a-ledger-is)
  - [3.1 Structure — an event log, not a balance](#31-structure-an-event-log-not-a-balance)
  - [3.2 The two kinds of debit — and the two components of property debit](#32-the-two-kinds-of-debit-and-the-two-components-of-property-debit)
  - [3.2a Debit is a vector, collapsed on demand](#32a-debit-is-a-vector-collapsed-on-demand)
  - [3.2b Pollution from making stays with the maker; pollution from using belongs to the user](#32b-pollution-from-making-stays-with-the-maker-pollution-from-using-belongs-to-the-user)
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
> **On the credit side, the substance is *time* — and time, not effort**. A credit records *time a human spent*, and the conceptual leap Aequitas asks of a reader is to see time itself as the finite thing being spent — like money is "spent" today, except that time is possessed by every person in exactly equal measure (24 hours a day) and can be neither hoarded, lent, nor transferred (A3 (non-fungibility)). This is the deep reason Aequitas produces a **bounded** inequality where money produces an unbounded one: money accumulates without limit; time structurally cannot — you get 24 hours a day and no more, ever, and you cannot buy anyone else's. Effort, hazard, and skill are real differences between workers, but they resolve as *material* costs (A2 (time as measure)), never as a time-multiplier. **Because the unit of account is an equally-distributed, non-transferable resource, the *engine* of a bounded inequality is the arithmetic itself, not any rule that polices it.** *(The exact bound, though, is a **conditional** result, and it is an **absolute maximum rather than an expected spread**. It depends on the value a network sets for its floor, on whether that network credits a child's learning time, and on fraud not manufacturing hours; see §5.5.5. **A very hard working life reaches about 1.6×, not 2.4×.** Earlier drafts overstated it as a flat arithmetic certainty.)*
## 1. Axioms
> **Each axiom below is a definition and nothing else.** What follows from it, why it holds, and what it rules out are in §2 onward, and each axiom says where to look. **An axiom that argues for itself is doing another section's job.**
### A1 (materialism of cost)
### A2 (time as measure)
### A3 (non-fungibility)
### A4 (no externalities)
### A5 (cost, not price)
### A6 (derived, not stored)
### A7 (universal accounting)
### A8 (no governing body)
## 2. What the axioms imply
| | |
|---|---|
| **2.1** | The three criteria every rule here is tested against, and why a system built on axioms needs them |
| **2.2** | **Debit** |
| **2.3** | **Credit** |
| **2.4** | **Transactions and sales** |
| **2.5** | How to tell a measurement from a convention, and the three conventions this system declares |
| **2.6** | What this document answers, and what it deliberately leaves to somebody else |
### 2.1 The three criteria, and why they are the test
| The criterion | The question it asks | What failing it means |
|---|---|---|
| **Universality** | Does one mechanism cover every case, with no exception, profession, nation or class carved out? | A system with exceptions cannot be shown to be wrong. Any awkward case gets a new exception |
| **Decentralization** | Can a stranger check a claim without asking anybody's permission? | Somebody has to be trusted, and whoever that is becomes the thing to capture |
| **Fecundity** | Does the system pay for its own upkeep and reward its own improvement? | It works while an enthusiast runs it, and stops when they leave |
| Schick and Vaughn | Here | What the rename does |
|---|---|---|
| **Scope** — how much diverse phenomena it covers | **Universality** | Sharpened from *"covers a lot"* to *"covers everything, with no exception"* |
| **Testability** | **Decentralization** | Narrowed to *who* may test it. A claim anyone can re-run without permission |
| **Fruitfulness** — it predicts new phenomena | **Fecundity** | Widened from prediction to upkeep. **A mechanism must pay its own maintainer from inside the system** |
> **⚠️ This attribution is the nearest match, not a confirmed source.** The three criteria entered this project through the Open Fair Credit Standard, and which book they came from was not recorded at the time. Research stub: [`../02-research/Schick_Vaughn_criteria-of-adequacy_v0.1.md`](../02-research/Schick_Vaughn_criteria-of-adequacy_v0.1.md).
#### Conformance to the three criteria
| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No exceptions for professions, nations, or classes. Units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7 (universal accounting)). Where a genuine convention is required, §2.5 names it rather than concealing it. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4.3) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing open variance. **Cost constants are the weakest point of this criterion, and §3.3a says so rather than claiming otherwise** — the auditing practice is a network's own design, held to five published properties (conformance 16a–16c), and no network has yet demonstrated a working one. |
| **Fecundity** | The verification ladder *pulls* technological development (§4.3). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses want (§5.3). Onboarding is individually rational (§4.8). Pledges give surplus a purpose (§4.6). **Every co-product allocation is an open scientific question that better instruments improve (§3.4a).** |
### 2.2 Debit
> **A debit is a record that matter or energy was taken from the world, together with a statement of who is holding the consequence.**
#### Who a flow is attributed to, and why
> **Only people act. A tool does not, a machine does not, and neither does whoever owns one.** So responsibility attaches to people, and never to machinery or to its owner.
| Kind | What it records | When the thing is handed on |
|---|---|---|
| **Property debit** | The matter you are holding, and the hours that made it | **The matter goes with the thing.** Your share of the making-hours is set by how long you held it, and it stays with you |
| **Consumption and pollution debit** | What you used up, burned, or released | **It never moves.** It stays on whoever caused it, permanently |
#### A1 and A5 answer two different questions, and that is what the two rows are
| The question | The axiom that answers it | The example |
|---|---|---|
| **Who is responsible for a flow they caused?** | **A1.** Responsibility is a fact about a person | The miner keeps the tailings. The driver keeps the tailpipe |
| **Who carries the debit that rides an object?** | **A5.** Possession decides it | Whoever is holding the ring carries its gold |
> **A pollution debit follows the causer and never the object** (§3.2b). **A property debit follows the object, and therefore follows possession** (§3.2). **The two never compete for the same debit.**
##### An example, with the numbers
| What happened | What the log stores | Which kind | Where it sits after the sale |
|---|---|---|---|
| Flour, water and salt went in | **0.8 kg** | Property | **The buyer.** It moved with the loaf |
| The baker worked on it | **0.2 h** | Property | Split by holding time. The buyer's share starts near zero |
| The oven burned gas | **0.3 kg of CO₂** | Pollution | **The baker, permanently.** The buyer did not light the oven |
**Nothing was added to any of those three figures, and no total was struck.** The buyer took a loaf carrying 0.8 kg and a small share of 0.2 hours. The 0.3 kg of CO₂ stayed where it was.
#### Two things a debit is not
> **A debit is never final.** Better measurement re-weighs it, and re-weighs every record made under the old figure, automatically (A6, §3.3). **A cost is a dated reading, not a verdict.**
> **And A4 does not require a cost to land on the made thing.** **A4 requires every cost to land on *a* ledger. It says nothing about whose.** §3.2b keeps pollution permanently on its causer rather than on the goods. §4.4 holds an unattributed leftover on nobody at all. §4.5 refuses to let a cost run backwards into the history of its inputs. **All three satisfy A4.**
### 2.3 Credit
> **A credit is a record that a person spent an hour of their life on work. It is a true statement about the past, so it belongs to one person and never moves.**
#### Everyone earns at the same rate
| The difference | Where it lands |
|---|---|
| **Hard work** | The extra food a labourer eats is recorded as **real food-production cost** |
| **Dangerous work** | A harm discovered later is injected back as debit into the products and services made by the process that caused it (§3.3) |
| **Skilled work** | **Training is credited work in its own right, and its cost is settled at the time of training.** Nothing is charged to whoever uses the skill later (§4.5) |
#### What counts as work
> **A trust network may credit an activity only if that activity is at least one of these three things.**
| | What it means | An example |
|---|---|---|
| **Production** | Matter or energy is turned into something | Milling wheat into flour |
| **A service** | Something is done for a person or a body, often with nothing to hand over | Setting a broken arm |
| **Enrichment** | Knowledge, skill or culture reaches somebody | Teaching a child to read |
> **The three categories decide whether an hour is creditable. They never decide how much it credits.** No rule in this system may credit production at one rate and enrichment at another, or divide a single hour between them (§4.5).
#### The gate is the boundary. What sits inside it is the network's choice
> **The three categories are the outer wall, and they do not vary. The list of always-credited activities sits inside that wall, and it does.**
| | |
|---|---|
| **Competing networks and ratio-based evaluation** (§3.5) | A network that credits worthless activity produces members with poor efficiency ratios, and other networks stop trading with it |
| **Public membership composition** (§3.3a) | A network concentrated in the sector it audits is captured by construction, and **that is visible from the log** rather than something anyone must police |
| **The published evidence rule** (§4.2) | A network credits no kind of work for which it has published no rule, and the rule is readable before anyone joins |
#### Why enrichment is named separately
#### Keeping yourself alive passes the threshold
### 2.4 Transactions and sales
> **A transaction is a hand-off. One person gives another a physical thing, and the debit riding with that thing goes too. That is the whole of a sale, and it is the only kind of sale there is.**
##### An example, with the numbers
| | The shop, before | The buyer, after |
|---|---|---|
| The metal | 18 kg | **18 kg.** It moved with the bicycle |
| The making-hours | 40 h, the shop's holding-time share so far | starts at **0 h**, and grows the longer they keep it |
| The shop's collection fuel | 3 h | **0 h.** The shop burned it, so the shop keeps it |
**So a second-hand bicycle starts cheap for a new owner and grows heavier the longer they hold it.** No margin was taken, no money is visible to the books at all (§4.8), and the only thing that moved was an object and what it carries.
### 2.5 Measurement and convention
> **Did the thing being divided leave a physical trace?**
>
> **Where it did — measure it.** Feed energy, the heat needed to crack crude oil, and a turbine's trade-off between heat and power are facts about a process.
>
> **Where it did not — declare a convention and say so.** Labour hours and shared overhead leave no trace pointing at any one output, and no instrument will ever find one.
#### The three conventions this system declares
| The quantity | What it is | The rule |
|---|---|---|
| **A team's credit, split across its members** | **Not a convention at all.** It dissolves | Credit is time worked (§2.3), so **each member is credited their own hours.** Nobody ever needs a figure saying the welder caused 40% of the bridge, because credit was never a share of the output |
| **One process's labour, split across its several outputs** | **A convention, on a measurable basis** | **The labour divides in the same proportions as the process's measured material split** (§3.4a). It introduces no new basis and nothing new to game |
| **A durable asset's creation-cost, split across its holders** | **A convention, on a measurable basis** | **Holding time is a physical trace, so the split is measured rather than invented:** your share is your holding time divided by the total holding time over the asset's whole life (§4.5) |
##### An example, with the numbers
**So the hours ride the material split, which was measured.**
| Output | Measured share of the feed | Hours it carries |
|---|---|---|
| Beef | 78% | 6.24 h |
| Tallow | 9% | 0.72 h |
| Hide | 7% | 0.56 h |
| Bone | 6% | 0.48 h |
| **Total** | **100%** | **8.00 h** |
> **The farmer is credited 8 hours whatever the split says.** The convention decides only **what each output's debit-cost reads**, never anybody's credit.
#### Two quantities that look like they belong here and do not
> **It is a choice that measurement constrains.** What this document fixes is the obligations on the choice: measure at the facility, for the period described, per dimension before collapsing, publish the method, and never let demand or yield enter. **The method itself belongs to the industry** (§2.6). Worked in full in §3.4a.
> **The project's hard problem is division, and specifically division of what left no trace.** See the objections register, §0.
### 2.6 What this document answers, and what it does not
> **Cost accounting is the principle. Records and data collection are praxis, carried out by implementers.**
#### The test for what belongs here
> **If a principle survives at both ends of a dial, the dial is not part of the principle.**
#### Which settings vary from one network to the next
| The setting | Where it is described |
|---|---|
| **The weighting model** — what a kilogram, a joule or a tonne of CO₂ costs in hours | §3.3, §3.3a |
| **The floor, `F`** — how many hours a day count as the work of staying alive | §5.5.1 |
| **The debit tolerance, ρ** — the multiplier in the consumption gate | §3.0, §5.5.3 |
| **The privacy practice** — how much anyone can see | §4.7 |
| **The verification rung** — how hard the network checks a claim | §4.3 |
| **The list of always-creditable activities** — inside the boundary §2.3 fixes | §2.3 |
| **The size of the network** | §4.0 |
#### What is out of scope, explicitly
| Out of scope | Whose question it is |
|---|---|
| Data-protection and erasure law | The implementer, under its own jurisdiction. Research: [`Law_gdpr-right-to-erasure_v0.1.md`](../02-research/Law_gdpr-right-to-erasure_v0.1.md) |
| Data security, backups, key management | A technology problem (§4.8) |
| The corporate or legal form of a trust network | The implementer |
| Which cryptography, which database, which protocol | The implementer |
| Whether the ecosystem converges to one network | A prediction, not a design input (§4.8) |
| **How a cost constant gets audited** — who replicates, what triggers a review, how a contested constant is handled while it is contested | The implementer (§3.3a). **That it must be answered is not out of scope**; the five properties in §3.3a are conformance items 16a–16c |
| **Which instrument reads a joint process's split**, and over what period | The industry (§3.4a). Same shape: the obligations are fixed here, the method is not |
> **The dial test is the standing screening question for anything proposed for these documents. What it leaves behind is a set of conformance requirements, never an architecture** — [`Aequitas_Conformance_v0.8.md`](Aequitas_Conformance_v0.8.md). **What must be true, never how to build it.**
## 3. The Ledger Model
### 3.0 What a ledger is
> **A person's ledger is two numbers, side by side.**
> **`C`, their credit — every hour of their life the books have recorded as work.**
> **`D`, their debit — every hour their consumption is currently reckoned to cost, once the bundle of physical quantities is converted at today's weightings.**
##### An example, with the numbers
| | Credit `C` | Debit `D` | `D ÷ C` | Room left, `ρ·C − D` |
|---|---|---|---|---|
| **A — stays alive, and works 1,000 h a year** | 40 × (3,650 + 1,000) = **186,000 h** | 40 × 1,380 = **55,200 h** | **0.30** | **168,000 h** |
| **B — stays alive, works nothing, consumes the same** | 40 × 3,650 = **146,000 h** | **55,200 h** | **0.38** | **120,000 h** |
**Neither person's numbers ever went down.** A's extra work did not cancel A's consumption. **It widened the gap between two figures that both only grow**, and both people sit far inside the gate.
**§3.5 says why the two figures can never be added into one and why the books must never balance.** The rest of §3 is the machinery that produces them.
### 3.1 Structure — an event log, not a balance
#### What never goes in the log: financial instruments
> **Stocks, bonds, currencies, crypto-tokens, options and other financial claims never appear on any ledger.** They are exactly the abstract, issued quantity A1 excludes, because they are not matter and not energy.
##### An example, with the numbers
**The effect was measured.** Entering the previously wealthy into the books **material-only** collapses the observed inequality tail by **about three orders of magnitude** against their paper net worth — money wealth reaches roughly **10⁶ ×** the median, while material consumption reaches roughly **670 ×** (§5.5, `06-simulation/scenario-suite/q4_locked_ledgers.py`).
**The reason is not a rule. It is that consuming physically takes time, and nobody has more than 24 hours in a day.**
### 3.2 The two kinds of debit — and the two components of property debit
### 3.2a Debit is a vector, collapsed on demand
> **One rule follows immediately: any division of a debit — across co-products, across a team, across anything — is computed on the vector, per dimension, *before* collapsing.**
>
> Divide the collapsed number instead, and whoever maintains the weighting model controls every allocation in history without anyone seeing it happen. Divide per dimension, and the split does not depend on the weighting at all: two communities running different weighting models compute the same split, and disagree only about what it weighs. This closes one route into OP-10 (weighting governance).
### 3.2b Pollution from making stays with the maker; pollution from using belongs to the user
> **1. Pollution caused by *making* a thing stays with the maker, permanently. It never attaches to the thing and it never reaches a buyer.**
> **2. Pollution caused by *using* a thing belongs to whoever uses it.**
> **3. A thing that will pollute when it is used carries that future pollution as part of its debit, in physical units, and it moves with the thing.**
##### An example, with the numbers
| | What the log stores | What the ledger reads |
|---|---|---|
| At the hand-off | **40 litres** | 40 × 2.31 = 92.4 kg, at 0.05 h per kg → **4.62 hours** |
| The refinery's own process emissions | on the refinery's own log | **0 hours on the buyer.** They never transfer |
| **After a better capture method halves what remediation costs** | **still 40 litres** | **2.31 hours** |
| **If the buyer sells the 40 litres on** | the litres move to the new holder | **0 hours on the seller** |
**The stored quantity never changed. Only the weighting did.** This is §3.2a working: a debit is a bundle of physical quantities, converted into a single figure only when somebody asks. **A system that stored 4.62 hours instead of 40 litres could not re-read itself when the science improved.**
> **Two things line 3 is not, and a careful reader will ask about both.**
>
> **It is not part of the thing's cost, so A5 (cost, not price) is unaffected.** A5 governs what a thing **cost to make**. Line 3 governs what a **holder carries while holding it**. A litre of petrol's creation cost and the CO₂ its burning will release are **two separate lines on the debit vector** (§3.2a), and neither is inside the other. **Nothing was added to the petrol's cost figure.**
>
> **It is not a second charge on top of §3.6.** For an object whose pollution *is* its disposal — a plastic bottle rather than a litre of fuel — line 3 and §3.6 describe **one quantity, recorded once.** Line 3 is the **carry** rule, saying how it travels while the object is held. §3.6 is the **terminus** rule, saying where it lands when nobody will take the object on. **An implementation that charges both has counted one physical fact twice.**
**Why this is right under A1 (materialism of cost).** Ellerman's responsibility-imputation: only the miner *acted* to pollute; the buyer did not cause the mining. Charging the buyer would misattribute responsibility. This is simply the two-kinds distinction above taken to its conclusion — the *permanent* kind stays with its causer; the *transferable* kind rides the object.
> **This is the same principle as computational closure (§4.5), seen from the other end.** Ellerman says pollution *must not* transfer to a non-causer; §4.5 says a cost *cannot* cascade indefinitely or the accounting never terminates. They are one rule: **cost never flows to whoever did not cause it** — downstream to a buyer (pollution) or upstream to the first human activity (historical cost). Both directions break the books, and the same non-cascade closes both. The gasoline case makes it concrete: the refinery's process emissions stay on the refinery, and the *combustion* emissions fall on whoever burns the fuel — never on the receiver of goods a truck delivered.
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
> **⚠️ Open universality edge.** "Real-time-dispatched vs batch" is a *spectrum*, not a clean binary: grid storage (pumped hydro, batteries) is a growing intermediate case, and on-demand services (a restaurant cooking your order) sit near the line. The principle is sound at the poles; the exact criterion for the middle is a registered open question, not yet closed.
**The consumer signal is not lost.** §4.4 already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**. Buyers and pledgers can still see and prefer low-pollution goods; only the *debit* is pinned to the causer. See §5.2 for why this makes the anti-pollution incentive *stronger*, not weaker.
### 3.2c An organisation's debit is its members' debit
> **An organisation's account is a view of its members' positions, not an owner of them. Every debit recorded against an organisation is, at the same time, the debit of the people who worked there, divided among them in proportion to the hours each worked for it.**
#### An example, with the numbers
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
> **Stated honestly: this is a declared convention, not a measurement** (§2.5). Hours worked leave no trace pointing at any particular debit the organisation took on. **Hours are chosen because they add no new lever** — they are already recorded for credit, already capped at 24 a day by IC-7, and already the basis §5.1 and §4.6 use. **A different basis, such as an equal split or a seniority weighting, would be a new thing to game.**
>
> **This convention may also close the residue §3.4a leaves open** — apportioning a jointly-*caused* debit across a team. The two questions have the same shape and now have the same answer. **Not claimed as closed until it is checked against §3.4a's case directly.**
### 3.3 Retroactive re-weighting
> **A flow is a *pollutant* only above the rate at which the natural world remediates it unaided.**
> **The transaction-time rule.** Because figures move, the gate must not. **`D ≤ ρ·C` is evaluated at the moment of the transaction.** A later re-weight, re-split, or coverage revision changes **future** debit-room; it never retroactively invalidates a completed act.
>
> Without this, a dynamic ledger implies retroactive liability — a revision could make a past purchase an offence — and no one should adopt a system that does that. Re-weighting corrects *the record of what things cost*; it does not reopen *what people were permitted to do* under the record as it then stood.
### 3.3a Who checks the science — the problem, and whose problem it is
> **How a cost constant gets audited is a trust-network design problem, not a foundational one.** This section states the problem and the properties any answer must have. **It does not supply the answer.**
#### The problem
| Error direction | Who wants it fixed | What happens |
|---|---|---|
| The constant **overstates** a debit | Everyone paying it | Corrected quickly |
| The constant **understates** a debit | Nobody — correcting it worsens every subscriber's ledger | **Nothing happens** |
#### Why the obvious answer does not work
> **And it failed hardest where the stakes are highest.** This section itself called the **ambient-stock and baseline constants** the largest levers in the weighting model. **Those have no rival at all** — everyone benefits from a high pollution baseline and a low stock reading. **A mechanism that works for beef versus plant protein and fails for CO₂ is pointed the wrong way round.**
#### Whose problem it is
> **Auditing cost constants is one of the problems a trust network exists to solve.** How it does so — who replicates, how replication is commissioned, what triggers a review, how a contested constant is handled while it is contested — is the network's design, published and checkable like everything else it does.
| # | What must hold | Why |
|---|---|---|
| **1** | **Two unaffiliated replications before a constant may re-weight history.** | Retroactivity is too powerful to trigger from a single source. |
| **2** | **Every constant is published with its method, its version, and its uncertainty interval.** | A constant nobody can re-derive is an authority assertion. Without an interval, "how well is this known" has no answer. |
| **3** | **Review is triaged by magnitude × concentration of beneficiary**, never by magnitude alone. | A materiality threshold alone helps an attacker, whose job then becomes making a falsification look immaterial. |
| **4** | **A network's membership composition is public.** | **A network concentrated in the sector it audits is captured by construction.** This makes capture a *detectable screening property* rather than a rule anyone enforces. General-membership networks are structurally sounder than sector-specific ones. *(The co-op form does not fix this: the conflict is directional, not monetary — Arthur Andersen was paid by Enron, and a client-owned Andersen would have been worse.)* |
| **5** | **The network states which constants it has not reviewed, and how old each reading is.** | The floor rule (§4.4) applied to weights: an unreviewed constant is a floor on confidence, never a value. |
> **Coverage has something weights do not: two parties with a private interest in getting it right.** The **instrumented producer**, materially harmed when undocumented produce prices too cheaply, and **the dark producer**, who cannot transact inside the system until they onboard (§4.4). **Neither requires the residual to be allocated to anybody**, which matters, because it is not.
>
> **This is why OP-24 is narrower than it looks: the audit of *extent* has interested parties; the audit of *weight* does not.** That asymmetry is the useful thing this section knows.
#### What is not scoped out
> **So a network that cannot show how it audits its constants is not conforming. It is not free to have no answer.**
### 3.4 Resolution is opportunistic
> **The distinguishing test is whether the divided thing left a physical trace.** Where it did, measure. Where it did not, declare a convention (§2.5) and say so.
### 3.4a Joint production — dividing one process's debit among several outputs
#### What the problem is
#### The rule
> **A joint process's debit divides according to where the process physically sent its inputs, measured at that facility, over the period being described.**
> **A2 is why this problem has an answer at all, and it is worth seeing why.** Every other attempt at this had to pick **one** unit of account and then defend it: split by mass, and energy-heavy outputs read as free; split by energy, and heavy outputs read as free. **A2 removes the choice.** Because every physical quantity in the ledger — a kilogram, a joule, a tonne of CO₂ — is a stand-in for the hours it takes to produce or to clean up, **the system never has to name one of them as *the* unit.** The universal is the denominator, not the carrier.
#### How the split is actually produced, in order
#### What Aequitas fixes here, and what it does not
> **Aequitas fixes the obligations. It does not fix the method, and it cannot.**
| Aequitas fixes | Left to the industry |
|---|---|
| The split must describe **where the process physically sent its inputs** | Which instrument reads that, in this industry |
| It must come from **measurement at that facility, for that period**, before any model | What counts as a workable period for this process |
| It must be **computed per dimension before collapsing** to one figure (§3.2a) | Where the sensible sub-process boundaries are |
| The **method must be published**, with its version, so anyone can re-run it (§4.7) | The method itself |
| It may **never depend on demand, desirability, or yield** (see below) | — |
#### What stops a producer choosing a flattering method
#### One thing the split may never do
> **Cost may not follow demand, desirability, or yield.**
#### Four things that follow
#### What remains open
### 3.5 The books never balance — and must not
> **And the binding scarcity is material and energy. The honest form of that claim is narrow, and it was measured on 2026-08-27.**
>
> **What still holds.** `06-simulation/scenario-suite/q1_autarky.py` finds an autarkic US bound by **the energy transition and critical minerals**: energy sits at **0.19** of what a median standard needs at the current build, against **land at 1.10** and **water at 5.22**. **Energy is the tightest constraint by a wide margin, and it does not depend on any labour figure.**
>
> **⚠️ One comparison looks like evidence and is not. Do not use it.** Setting the **credited**-labour pool against the labour an economy needs — Q1's row of *3,647 h/yr available against 1,600 h/yr needed, ratio 2.28* — **cannot fail, so it was never evidence.** Its top number includes the self-care floor, and `F` is a value the network sets by rule (§5.5.1). **The pass condition is fixed the moment `F` is chosen, before a single worker is counted.** Sleeping is credited work under §2.3, and it cannot lay cable.
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
> **The measured anchor (2026-08).** A bottom-up estimate puts the **labour a median US lifestyle commands at ≈ 1,380 h/yr** (`06-simulation/median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md`; measured from BLS employment-requirements × the actual PCE mix, EXIOBASE import labour, §4.5 durables, and own-pollution remediation — *not* a blanket ratio). **Do not set that figure against the 3,650 h/yr of self-care credit and call the difference slack.** That is the circular comparison struck above. **The figure earns its place as the denominator for the deployable-hours test, and for the efficiency spread below. And the same-standard efficiency spread is large:** cross-country accounting (EXIOBASE, `06-simulation/median-lifestyle/Q6.md`) finds the US the labour- *and* carbon-inefficient outlier — commanding **50–80% more embodied labour and 2.5–4× the CO₂ per capita** than Germany, Sweden, France, Japan, or Spain, which deliver a comparable-or-better material standard (and longer lives) at ~⅔ the labour. **This is the positive form of A4 (no externalities) and A5 (cost, not price):** the inefficient, fossil-heavy, long-chain method is simply *dearer in the ledger*, so the accounting rewards the efficiency the leaders already demonstrate — no mandate required. What looks like "we cannot afford a decent standard for all" is, quantitatively, an artefact of the most wasteful production method, not a limit of human hours.
### 3.6 End-of-life, recycling, and product-as-pollution
> **⚠️ Live enforcement gap — OP-25.** Rules 1–3 price *lawful* disposal correctly. They do not by themselves stop *illicit* dumping — abandoning an object in the environment to escape its end-of-life debit. Attribution of abandonment back to the abandoner is a Level-2 trust-and-provenance problem, registered as OP-25.
### 3.7 Land is not owned; a building carries a remediation debt
> **Every structure carries a *remediation debt* — the cost to restore its bounded space to its natural state** (strip lead paint and contaminants, remove the foundation and buried piping, refill the excavation, restore native soil and wildlife). It is a property-debit on the structure's holders, weighted by the stock/remediation rule (§3.3), and it behaves like the end-of-life debit of §3.6: it is only discharged to **zero by actually remediating** the space.
> **⚠️ Hard edge — the "natural state" baseline.** What is the natural state of an already-urban bounded space (a plot in Manhattan)? This is the same shape as the §3.3 pollution baseline (a convention with a measurable basis, contested at the margin) and inherits its governance. **Registered as the open sub-question of this section**; the mechanism is sound, the baseline convention needs specifying.
## 4. What a trust network does
### 4.0 What a trust network is, and what this section covers
> ### 📦 A TRUST NETWORK HAS NO SET SIZE
>
> **A8 is about who may change the rules. It is not about how big anyone is.**
>
> A trust network may cover one valley, one trade, one country, several continents, or the world. **Nothing in these documents fixes the size of a network, and nothing should.** Size is one more dial under §2.6, and the accounting is identical at both ends of it.
>
> **One place in this document depends on that.** §4.8 expects networks to **federate and merge toward a single network over time**, rather than settling into separate regional systems.
>
> **The `24 ÷ F` bound is not a second example of it.** That bound describes **one network's own books** and says nothing about any wider set of networks, because networks do not trade with each other and no book is ever added to another (§4.0, §5.5.5).
>
> **Where this document does mean somewhere geographic**, it is describing a *physical* thing handed to a *physical* person: a butcher's queue for a scarce cut (§3.4a, §5.5), or a village served by one generator (§3.2b). **A scarce object has to be given out somewhere. That is a fact about the object, not about the network.**
#### The words this section uses
| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books. It records material flows, checks the arithmetic, estimates what it cannot observe, and publishes its methods so other people can re-run them. |
| **Subscriber** | A person who holds an account with a trust network. |
| **Event log** | The permanent, append-only record of what happened. Every position is computed from it, and none is stored (§3.1, A6). |
| **Estimate** | A figure computed from a published method, where no direct record exists. |
| **Record** | A figure taken from an observation or an attestation. **A record always beats an estimate** (§4.4). |
| **The floor**, written `F` | The number of hours a day a network counts as the work of keeping a human being alive. **The network chooses which activities count and how many hours each takes** (§5.5.1). |
| **ρ** ("rho") | The network's debit tolerance — the multiplier in the consumption gate `D ≤ ρ·C`, defined in §3.0. |
| **IC-7** | The integrity check that stops any account claiming more than 24 hours of activity in 24 hours. |
#### Three facts that shape everything below
#### What this section covers
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
### 4.1 It gives each person one account
> **1. Inside one trust network, one verified human holds exactly one account.**
> **2. Participation is voluntary. Coverage is not.**
| | Estimated from |
|---|---|
| **Debit** | The average for their demographic group, computed while **excluding** registered subscribers. A public figure is estimated from publicly known holdings. |
| **Credit** | A production model for their occupation, region and known activity, computed while **excluding** measured producers (§4.4). |
> **A non-participant can neither draw on their estimated position nor be charged for it.** The estimate is a statement about material flows in the world. It is not a claim on the person, and the person has no claim from it.
#### Two words A7 uses, and the difference between them decides everything
| | What it means |
|---|---|
| **Accounted** | Every human carries an estimated credit **and** debit position. **This is a factual claim about material flows in the world.** It is not a claim on the person, and not a claim the person holds |
| **Realizable** | An estimated position starts acting on what a person may consume **only once two things are true**: they hold a verified account, and observed, attested records have replaced the estimates |
> **Everyone is accounted. Only subscribers are realizable. Participation is the act of turning an estimate into a record.**
#### One person may hold an account with more than one network
##### An example, with the numbers
| | Network A | Network B |
|---|---|---|
| The floor `F` | **4 hours a day** | **10 hours a day** |
| Credit recorded for that Monday | 8 + 4 = **12 hours** | 8 + 10 = **18 hours** |
**Both figures are correct.** Each network read the same two physical facts, eight hours worked and one human alive, through its own settings.
> **The two figures cannot be added, and §4.2 says why.** They come from different weighting models, so they are not in the same unit. **No account holds 30 hours**, and IC-7 was not breached, because IC-7 applies to each account on its own.
**A purchase clears against one set of books only.** If the seller accepts Network A, the gate `D ≤ ρ·C` is checked against A's figures and the event is recorded in A's log. **Network B never sees it.** The same purchase may clear on one network and be refused on the other, because the two use different floors and different values of ρ.
**Where a network's records are partial it publishes a coverage figure saying so, and where a subscriber leaves activity undisclosed the network estimates it and errs against them** (§4.4). **The gap is measured and declared rather than hidden.**
> **The hardest case for rule 1 is a pair of identical twins on the lowest rung of checking, deliberately engineering the confusion. The arithmetic refuses it.** IC-7 caps an account at 24 hours of activity in 24 hours, so two twins faking one account reach 34 hours a day against 36 hours honest. **They lose 730 hours a year and gain nothing**, because twins sharing a household share the goods either way. Worked in full, together with the cross-network case: [`OP-22_identity_not_disclosure_v0.2.md`](open-problems/OP-22_identity_not_disclosure_v0.2.md).
### 4.2 It decides what counts as evidence, and publishes it
> **A trust network publishes, for every kind of work it credits, what evidence that work requires. That published set is its contract with the subscriber. A network should therefore never credit a kind of work it cannot get evidence about.**
##### An example, with the numbers
| | Hours worked | Against the published rule | Hours credited |
|---|---|---|---|
| **A** delivers a translation and the client confirms | 20 h | Rule met | **20 h** |
| **B** says they translated for 20 hours, with no text and no client | 20 h | Rule not met | **0 h** |
**B is not being judged and B is not being punished.** B knew the rule before starting, because the network published it.
**Now change the network instead of the person.** If translating for someone who cannot confirm is work this network wants to credit, **it writes a rule for that case**, perhaps requiring a second witness. **Once the rule exists, B's 20 hours credit at 20 hours.**
#### What the evidence usually is, by kind of output
| Output | How it is verified |
|---|---|
| **Goods** (matter or energy) | **The hand-off.** The receiver accepts possession, and the debit that rides with it, which attests that the goods exist (§4.5). |
| **A service** (often with no physical output) | **The client confirms** that the service happened. |
| **Enrichment** (intangible work, such as teaching or writing) | **Evidence that the work happened.** |
| **Self-care** (the work of keeping yourself alive) | **Proof of life.** A verified living human demonstrably maintained itself. This is statistical, and it costs almost nothing to check. |
#### A network never converts another network's figures into its own
> **This is comparison, never conversion. Nothing is exchanged between models, and each party re-reads the same physical log through its own weighting.**
> **⚠️ That guard depends on OP-22, the open problem of minimum audit disclosure.** Re-computing what backs a claim means seeing what backs it, and personal ledgers are private (§4.7). The guard needs *"this pledge is backed by X hours recorded under weighting model M"* to be provable without revealing the history. **The market check on a lax network is only as real as that mechanism, and the mechanism does not exist yet.**
#### The honest limit
### 4.3 It checks claims, and chooses how hard to check
| Rung | How an event is established | What it needs | Its weakness |
|---|---|---|---|
| **1 — people vouch** | Humans who were present confirm it, with several signing off | Nothing at all. This works in any village on Earth today. | People can agree to lie together |
| **2 — reputation and stake** | Verifiers stake their standing, and the pattern of attestations is audited across a social graph | A social graph, and auditors who are credited for auditing | The hard rung. It is expected to grow rather than be designed in advance |
| **3 — instruments** | Sensors, and signed tamper-evident records, establish the physical event | Meters, scales, cameras, telemetry | Whoever controls the instrument controls the answer |
| **4 — continuous machine tallying** | Software tallies the whole logistical record without being asked | Far more than exists today | Speculative |
> **Every rung must produce records that every other rung can read, and the system must degrade downward without breaking. A region using instruments and a region using a notebook must be able to trade.**
#### Climbing the ladder makes checking cheaper, not dearer
##### An example, with the numbers
| Rung | What checking costs for the season | Its share of the 10 hours in a sack |
|---|---|---|
| **1 — the receiver signs for what they take** | 0 h, because this is the trade itself | **0%** |
| **2 — the network samples and checks the method** | about 2 h of desk work | **0.02%** |
| **3 — a scale on the loading dock** | about 0.5 h, which is calibration only | **0.005%** |
**Read the last column downward. Checking gets cheaper per unit as you climb.** A network audit is cheaper per sack than a person watching sacks, because it works on totals and cross-checks rather than on individual items. **The full table, including rung 4 and the measured cost at which the whole approach would fail, is in [`../01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md).**
> **⚠️ A large checking cost is a warning sign, not a design to accommodate.** **No honest process spends a large fraction of its output on keeping records about itself.** A network seeing such a figure should audit the producer rather than redesign the ladder around them. Worked, with the measured threshold: [`../01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md).
**A rung costs a network different hours in different places, so the figure is the network's own and is not fixed here.** What Aequitas requires is that the figure be **published beside the rung**, as a sampling rate and a periodic cost, and never as a charge per transaction. **A network that states its rung without stating its price is asking to be trusted rather than checked.**
#### A second record only helps if it can disagree
> **A second record needs two properties, and most people ask for only the first.**
>
> **Independence.** The fault that hit the first record did not reach the second, because the two were made on different paths.
> **Expressiveness.** The second record is *able* to hold a value that contradicts the fault.
##### An example, with the numbers
**Then weigh the actual pile in the actual barn. The records say 2.0 kg and the scale says 0.0 kg, so the check fires.**
> **What defeats a balanced lie is physicality, not independence. Matter does not agree to be counted twice.**
**This is why the outside total used in §4.4 is a physical measurement rather than a second set of books.** The full worked table is in [`../01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md).
> **⚠️ And say plainly where the trust went.** Rung 3 does not remove trust. **It moves trust from the ledger to the instrument.** An attacker who controls the scale wins completely, and nothing further along the chain can tell. **That is a better place for trust to sit, because a rival can re-calibrate a scale and cannot re-calibrate a lie. But it is not "nothing to trust", and this document should never say it is.**
### 4.4 It estimates what it cannot see, and says how much that is
#### A record always beats an estimate, and never the other way round
> **A record replaces an estimate. An estimate may never replace a record.**
#### Records are annotated, never deleted
#### What an unmeasured producer is assumed to have produced
> **estimate = (N − Y) ÷ Z**
>
> **N** is the independently known total for the whole area being described, such as agricultural statistics, trade data, or a satellite survey.
> **Y** is what the measured producers actually recorded.
> **Z** is the number of producers still unmeasured.
> **Condition 3 is not a formality. On the project's own worked case, skipping it made the unmeasured pool look three times larger than it was**, and every unmeasured producer's estimated share with it. The full case is in [`../01-wiki/estimation-engine.md`](../01-wiki/estimation-engine.md). It is conformance requirement 14a.
#### A figure built from two incomplete readings needs a label, and the label must be earned
> **⚠️ That holds for a count. It does not survive a subtraction.**
##### An example, with the numbers
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
#### Why the outside total has to be a physical measurement
> **Ask this about any check and you will know at once what it can find. Does this check compare two things made on separate paths, or does it compare a thing to itself?**
| Flow | What sees a gap in it |
|---|---|
| One account to another | **The counterparty.** A hand-off has two sides, so a one-sided omission dangles on the other party's record. |
| An account to the commons | **The reservoir.** Measured depletion or accumulation, minus the sum of recorded flows. |
| A chain with no recorded connection to anything | **`(N − Y) ÷ Z`.** Nothing is shared, so only an independent total can see it. |
#### The leftover is charged to nobody
> **The leftover is computed, published, and left unassigned. It is debit on no account. When an unmeasured producer joins, their share is traced back from records that already exist and assigned to them, because they are the party who caused it. Until they join they cannot transact inside the network at all.**
> **⚠️ The coverage figure is `Y ÷ N`, so it carries the subtraction problem in its own form.** A blind `Y` understates coverage, so the books are better than they say. **A blind `N` overstates it, so the books are worse than they say — and that is the direction which flatters the network.** **The same three labels apply, and `not identified` is the default.** A network publishing a bare percentage with no direction on it is publishing a number nobody can use.
#### When a person joins, their position is reconstructed back to their birth
> **The reconstruction runs on both sides. The debit and the credit are both rebuilt.**
##### An example, with the numbers
**A person joining at forty arrives with roughly 146,000 hours of estimated credit against roughly 55,200 hours of estimated consumption.**
> **Joining is a windfall for a median person, and that is the adoption incentive computed rather than asserted** (§4.8). **The people for whom a full reconstruction is costly are those whose lifetime consumption genuinely exceeded their lifetime contribution.**
**The estimate is the default, and evidence is voluntary.** A person supplies whatever narrows it — where they were born, how long they lived in each place, which jobs they held, how far they commuted, which vehicles they owned — and accepts the estimate for every period they leave undisclosed. **Nothing is compulsory, and evidence moves the figure in either direction, which is why people supply it.**
**Details may arrive years later and the position re-derives.** No new machinery is needed, because a position is computed from the log and never stored (A6).
**Two conditions, and without either this breaks.**
> **Why the two sides are not treated alike, and it is not a preference.** **Over-estimating somebody's debit consumes nothing** — it costs them room they were not using. **Over-estimating their credit hands out real consumption room on the strength of a guess about production.** The two errors are the same shape and have opposite consequences, **which is why a position only starts acting on what a person may consume once observation has replaced the estimate** (A7).
> **Credit is issuable backwards, and this is where that happens.** When a person joins, their earlier real contributions enter the record **at the dates they occurred**, not at the date they joined.
> **Subsistence is exempt and must stay exempt.** The floor is not an estimate. **It is credit for hours that were really spent, attested by proof of life** (§4.2). **So condition 2 never reaches subsistence, and a person who cannot document a life is not thereby impoverished by this rule.**
**Two rules this looks like it breaks, and does not.** A non-participant is never charged for an estimated position, and **nothing is charged until they join, which is voluntary**. And §3.3's rule that a revision never invalidates a completed act still holds, because **acts before joining were never gated by any network**, so no permission is being withdrawn.
> **⚠️ This raises the stakes on OP-22, the open problem of minimum audit disclosure, and it is the strongest objection to the reconstruction.** A whole-life record is a dossier: birthplace, every residence, employment history, commuting distance, vehicles owned. **Disclosure is voluntary, but the incentive runs toward disclosing**, so the arrangement puts steady pressure on people to assemble exactly the record a surveillance state would want. §4.7's split of public market data from private personal ledgers now has to hold across a lifetime. **Registered, not solved.**
### 4.5 It credits work
> **There is one credit. It is time spent by a person, recorded as material flow. Everyone earns at the same rate, and therefore influences at the same rate.**
#### What enrichment covers
> **Childcare is creditable work regardless of who performs it.** This alone brings the largest uncounted labour pool in human history onto the books.
#### The floor is where self-care credit lands
#### Training is paid when it happens, and never charged to anyone later
> **Nothing is charged downstream.** A doctor's care costs the recipient the doctor's time, the material cost of running the clinic, and the medicines dispensed. **The doctor's education is not in that bill.** It was underwritten up front, by the people who wanted doctors to exist.
##### The general rule this is the first case of
> **A large up-front cost with a diffuse benefit is carried where it is incurred, and cushioned at that time by the debit-room the people who pledged for it grant. It is never charged onward to whoever happens to consume the result.**
> **⚠️ The honest limit: a first-time creator attracts no pledges.** The barrier is far lower than raising money, and the path is real — make small unpledged work, gather feedback, then attract pledges — **but it should be stated rather than assumed away.**
#### A durable asset carries its own making, shared by how long each person held it
> **A carrier moving goods takes no share of their making.** A haulier holding 1,000 toasters for two days did not make them. **Transit adds only the carrier's own transport debit.** Without this rule, the supply-chain model of §4.6 would quietly load the making of a toaster onto the truck driver.
##### The rule people attack most, with the numbers
| | Hours per kg |
|---|---|
| What a critic says beef should carry: 20,000 ÷ 40,000 | 0.5 |
| **What beef actually carries from the barn** | **0.0** |
> **This is not an exemption from A4 (no externalities), and the objection is worth answering here rather than leaving it.** Every hour still lands on a ledger. **A4 requires that; it never required the ledger to be the product's** (§2.2). **Charging a beef buyer for the barn is the same error as charging a ring buyer for the miner's tailings**, which §3.2b already refuses. One rule, two directions.
> **⚠️ The honest limit.** Two producers of the same good, one with a 20,000-hour barn and one with a 2,000-hour shed, **publish the same figure per kilogram.** A buyer comparing those figures cannot tell them apart, because a unit's figure answers *"what did this unit consume?"* and never *"what does this producer's whole method cost?"* **What disciplines the barn is the builder's own gate, not the label on the beef.**
#### There are no patents, and attribution is by recognition
#### Not all work is capturable, and the system does not require it to be
> **Much of what people do, they do to entertain themselves and each other. The system does not need to capture it, price it, or credit it, and attempting to would be both futile and grotesque.**
#### Work nobody can observe
> **Read mechanism 2 alongside §4.2, because the two are easily confused.** Cautious weighting decides **how much a claim weighs inside a rule the network has already published.** It never stands in for a rule that was never written. **A network weighting a whole class of real work near zero has written the wrong rule, or has failed to write one.**
### 4.6 It carries what people want made
#### Feedback is not credit, and never converts to it
> **Feedback is non-convertible because it was never credit in the first place. There is nothing to firewall.**
#### Pledges and signals, told apart by one test
> **Is it backed one-for-one by credit the person already earned?**
| | **A pledge** | **A signal** |
|---|---|---|
| Says | *"I authorise this work"* | *"I want this to exist"* |
| Backed by | **earned credit, one hour for one hour** | nothing |
| Rate | **A finite lifetime budget, equal to lifetime earned credit, spent once** | Many per hour earned, or unbounded |
| Permanence | **Permanent and non-revocable** | — |
| Looks like | Crowdfunding, commissioning a task, choosing a GP | Likes, ratings, applause |
#### Everyone alive holds some of this, simply by being alive
#### Recording is never gated. Verification decides when credit counts
##### For goods, the hand-off is the verification
#### When a task attracts more pledges than it costs
> **The surplus becomes an earmarked reserve that activates only against a verified future cost traceable to that task** — the doer's later injury or illness, remediation that resurfaces, harm to a third party.
#### Why a pledge is a better demand signal than a price
| The assumption | What is actually the case |
|---|---|
| Scarcity is a physical fact the price reports | **Much scarcity is produced.** Supply is held back to hold the number up. |
| Demand is a fact the price reports | **Demand is manufactured, at industrial scale.** That is what the advertising industry is for. |
| So a price honestly reports what people want | **The same firms set supply and work on demand. The price partly reports its own producer.** |
> **So the objection assumes the price is a clean instrument. It is not. Aequitas is not replacing an honest demand signal with a worse one. It is replacing a signal the seller helped write.**
> **⚠️ What this does not answer.** **Two people, one radicchio. Pledges say how many get grown. They do not say who gets the last one.** That is a distribution question with a separate answer — a queue, a lottery, or pledge-priority, decided where the physical thing is handed over (§5.5). **Cost states what a thing took. Who receives a physically scarce output is a different question, and this document deliberately does not settle it.**
> **⚠️ And it does create a popularity contest.** Whoever is already liked attracts the most pledges. **That is a known open problem, not a new one.** The bound on it is that every pledge costs a real person a real hour from a finite budget.
### 4.7 It publishes its own workings, and settles disputes
#### The market is public. Persons are private
> **Transparency here is split by level. Pledges, production quantities, hand-offs and the figures things carry are public. Individual people's positions are private.**
> **⚠️ The narrow question this leaves is OP-22, and it is unsolved.** The bank analogy has one gap: **there is no bank to hand validation to.** An auditor must be able to see *something*. So the live question is not *"surveillance or privacy"* but **"what is the least an auditor must see to check a claim without seeing a history?"** Proofs that reveal nothing but the answer are the right shape. **The precise set of what must be disclosed does not exist yet**, and public pseudonymous events can be analysed to identify a person, which is the classic ledger-privacy problem.
#### How private, exactly, is the network's own choice
> **Each trust network sets its own privacy practice. Aequitas states the principles and does not dictate the implementation.**
| | |
|---|---|
| **The network becomes the most information-rich actor in the system** | Whoever tallies, holds. A network keeping its members' lifetime reconstructions holds a concentration of *information* comparable to the concentration of *wealth* this project exists to remove. **Unanswered.** *"You may leave"* is a weak exit when what you would leave behind is your life history. |
| **Privacy has a measured cost in coverage, and the measured number says the trade-off is not close** | Privacy-preserving checking is dearer than open checking, and that direction is real. **The failure point is roughly 200 times higher than anything a working network would report.** A network should publish what its practice costs; it does not have to trade coverage away to have one. |
| **A network's choice binds people who did not make it** | Children born into a transparent network, and people who joined before a practice changed, did not choose it. |
#### What a network owes
> **To be trustworthy a network publishes every estimating number it uses, every method, and anonymised data covering all of its participants. A network that will not show its arithmetic is asking to be trusted rather than checked, which is the thing this system exists to stop needing.**
> **⚠️ And this cuts against itself.** Anonymised participant data becomes **more** re-identifiable the more of it there is. **Publishing more to earn trust also publishes more to identify people by.** A network is choosing on that axis whether it means to or not.
##### "Funding" is not a budget. It is recognition
> **Funding, in Aequitas, is simply the recognition of an activity as creditable.**
##### A network's own founding is recorded like any pre-existing thing
#### How a dispute resolves
##### Where the analogy breaks, and this is the part worth having
| A dispute about | How it resolves | Needs a verdict? |
|---|---|---|
| **The physical record** — did 70 g of wheat actually move? | **Arithmetic.** The integrity checks recompute it. **This is not a dispute; it is an error, and recomputation says whose.** | No |
| **The weighting model** — what does a tonne of CO₂ cost? | **Nobody has to accept anyone else's model.** Each party re-computes the shared physical record through its own weights and decides for itself (§4.2). | **No** |
| **An estimate for something unmeasured** | Published method, and anyone can re-run it. The figure carries its interval and its label, and better evidence supersedes it (§4.4). | No |
| **Fraud** — someone recorded events that never happened | **A finding of fact, and it needs one.** | **Yes** |
> **A transaction never waits on a shared verdict.** Each side computes its own answer over the same physical record and decides whether to trade. **Disagreement about weights does not block commerce. It means two parties read the same thing differently, which is a fact about models rather than a deadlock.**
##### What correction looks like — nothing is reversed
> **The past transaction is not reversed. The fraudulent credits are negated, the ledger rebalances, and the person's ratio may now be too low to buy anything until they hand on some of what they hold.**
> **⚠️ One real load stays, and it is not a disagreement about weights.** Deciding whether a **particular past task caused a particular later harm** is a contested finding of fact wherever no physical trace exists. **It routes to existing recourse, like fraud does. Registered, not solved here.**
### 4.8 It takes people in, it merges with other networks, and it can end
#### Joining replaces an assigned average with your real record
> **⚠️ Watch item: fixed joining costs consolidate industries.** Documentation burdens are repeatedly argued to disadvantage small producers, which is why organic-certification cost-share programmes exist at all. **The structural offset is that helping someone join is credited work borne by the network rather than the entrant. Whether that is enough is empirical and should be watched rather than assumed.**
#### There is entry, and there is no exit
> **Once records of a person exist they are never destroyed. They are only added to, including after that person's death.**
> **One consequence follows from all of this. Because deletion is unavailable, publicity is the only privacy control that exists** (§4.7). **There is no falling back on erasure**, which raises what §4.7 has to carry. The full note, including the erasure-law reading, is in [`../01-wiki/permanence-and-death.md`](../01-wiki/permanence-and-death.md).
#### Networks federate by agreeing methods, not answers
> **Merging means agreeing every rule — the floor, ρ, the weighting model, and how a human is identified — after which the merged network computes one answer from one log. Until they agree, each keeps its own book and neither is wrong.**
> **The expected trajectory is convergence.** Networks that federate are expected to keep federating and to merge over time, rather than settling into permanently separate regional systems. **What that buys: one ledger per person, no coverage gaps at the seams, and no arbitrage between incompatible standards.**
> **⚠️ The watch item, stated as one rather than as a defence.** A monopoly earned on merit can stop being meritorious and keep the position. **The guard is publication plus replication, not competition** — so if publication ever weakens, the merit argument weakens with it.
#### Trading across the money boundary
| Direction | What happens |
|---|---|
| **Selling into Aequitas** a good made with money-bought inputs | The good is unrecorded until it is sold in, because its inputs never passed through a hand-off here. At that hand-off the maker either records its origins properly **or applies a published template that assigns a figure immediately.** **The maker spent money making it and receives none, and that is the disincentive.** |
| **Selling out of Aequitas**, for money | Permitted. **The debit stays with the seller**, because no participant took the goods on. **To the network the seller made a gift, and the network does not acknowledge the money changing hands at all.** |
> **Goods cross the boundary. Standing does not.** Follow a wealthy person paying a hundred workers in money and selling the goods into Aequitas. **The workers are credited their own hours**, because credit records who was responsible. **The financier worked none of those hours and is credited nothing.** **There is no channel from money to credit, at any scale. You cannot buy hours.**
> **⚠️ What stays open.** Whether a person can hide behind a **fake or borrowed membership list** — claiming hours for people who did not work them, or leaving their own name off. **That is a verification question rather than an accounting one.** The accounting has no hole here; the identity layer still has to do its job.
## 5. Consequences
### 5.1 Capitalism cannot function
> **Producers compete on quality, artfulness, and efficiency. They never compete on margin, because there is no margin to compete on.**
### 5.2 Exploitation and pollution self-penalize
### 5.3 Regulators invert into services
### 5.4 Taxation is unnecessary
### 5.5 The basic-needs floor
#### 5.5.1 What the floor is
| Term | What it means |
|---|---|
| **The floor**, written `F` | The hours a day a trust network counts as the work of keeping a human being alive. |
| **Trust network** | The organisation that keeps the books and sets `F` for its own subscribers (§4.0). |
| **ρ** ("rho") | The network's debit tolerance. The multiplier in the consumption gate `D ≤ ρ·C` (§3.5). |
| **`C`** | A person's cumulative credit — the hours of their life the books have recorded as work. |
| **`D`** | A person's cumulative debit — the material and energy the books have recorded against them. |
> **The floor is credit for time a person spends on the activities their trust network counts as essential to staying alive.**
##### The evidence on sleep, and how a floor is built from it
##### A worked floor, with the numbers
| Activity | Hours a day | Why it qualifies (§2.3) |
|---|---|---|
| Sleep | **8.0** | A service performed on your own body, or enrichment of your own brain. Either reading credits the same hour |
| Eating and preparing food | **1.0** | A service on your own body |
| Washing and grooming | **0.5** | A service on your own body |
| Using a toilet, dressing, other bodily upkeep | **0.5** | A service on your own body |
| **`F`** | **10.0 h/day** | = **3,650 hours a year** |
#### 5.5.2 The floor follows from the axioms. It is not an allowance
| Step | The rule | Where |
|---|---|---|
| 1 | **Credit is a record that a person spent time on work.** Not effort, not output — time spent. | **A2** (time as measure), §2.3 |
| 2 | **Maintaining a living human body is work.** Doing it for somebody else is work, so doing it for your own body is the same work. | §2.3 |
| 3 | Therefore **a living human accrues credit for the hours spent maintaining themselves.** | §2.3 |
| 4 | **Every human is in the books whether they participate or not**, and a verified living person demonstrably did that maintaining. | **A7**, §4.2 (proof of life) |
> **A person who does nothing else is still doing that work, and the books record it because it happened.**
##### What this rules out saying
| Do not say | Why it is wrong |
|---|---|
| *"a basic income"* | An income is paid by somebody to somebody. **Nothing is paid, and there is no payer.** |
| *"a safety net"*, *"the dole"*, *"an entitlement"* | All three describe a claim on other people. **Credit is a record of the holder's own time and is a claim on nobody** (A3). |
| *"the system supports people who cannot work"* | **Everyone alive is working, by this definition.** The floor does not distinguish between the busy and the idle, because keeping yourself alive takes the same hours either way. |
#### 5.5.3 The floor's value is an economic setting, with a bound at each end
> **Set it too low and people cannot afford what they need. Set it too high and the books stop rationing anything. Finding the value that balances the economy is the network's job.**
##### The lower bound, with the numbers
| | |
|---|---|
| Minimum floor | 700 ÷ (1.2 × 365) = **1.6 h/day** |
| At `F` = 2 h/day, room per year | 1.2 × 2 × 365 = **876 h** — covers 700 h of essentials |
| At `F` = 1 h/day, room per year | 1.2 × 1 × 365 = **438 h** — **short by 262 h** |
##### The upper bound, with the numbers
| Floor | Room from the floor alone, `ρ·F·365` at ρ = 1.2 | As a multiple of a median lifestyle |
|---|---|---|
| 2 h/day | 876 h | **0.63×** |
| 4 h/day | 1,752 h | **1.27×** |
| 8 h/day | 3,504 h | **2.54×** |
| 10 h/day | 4,380 h | **3.17×** |
> **The gate then stops binding on almost everybody.** `D ≤ ρ·C` still holds, but it is not the thing deciding who gets what. **Where the economy can actually deliver that much, this is abundance and it is the intended end state** (§3.5, Q6). **Where it cannot, physical shortage is decided at the point of distribution instead — by a queue or a lottery** (§3.4a, §4.6) — **and the accounting has stopped doing the work it was set up to do.**
##### The band, measured
> **The band exists at every floor from 1 to 14 hours a day, and it never closes. What binds it is capacity, not affordability.**
| `F` | ρ*(`F`) | `E_max` | As a multiple of a median **American** lifestyle |
|---|---|---|---|
| **2 h/day** | 3.70 | 2,701 h/yr | **1.96×** — the tightest floor measured |
| 10 h/day | 1.20 | 4,380 h/yr | 3.17× |
| 14 h/day | 0.90 | 4,599 h/yr | 3.33× |
##### And the upper edge is an artefact of the American production method
> **⚠️ The 1,380 h/yr anchor is a median *American* lifestyle, and that is not a neutral choice.** `06-simulation/median-lifestyle/Q6.md` measures the US as the labour- and carbon-inefficient outlier: **Germany, Japan and Spain reach a comparable-or-better material standard, and longer lives, on about two thirds of the embodied labour.**
| Production method | Debit-hours per unit | Real living the same envelope delivers | Share held back by the gate |
|---|---|---|---|
| **US** | 13.80 | **56,446** | **35.8%** |
| German or Japanese | 8.83 | **88,196** | **0.0%** |
| Spanish | 7.59 | **102,629** | **0.0%** |
> **Under the American method the envelope delivers less than people want, so the gate rations and about a third are held back. Under the German, Japanese or Spanish method the same envelope delivers more than everyone wants, the gate never binds, and nobody is held back at all.**
> **⚠️ What is measured and what is not.** The two zero rows are **floors, not values** (conformance row 13): the gate does not bind anywhere below ρ = 4.0, which is where the swept range ended. Nobody looked above it. **And ρ\*'s absolute values inherit the weighting model and an illustrative capacity figure — the shape is the result, the numbers are dated readings.** Full method, the three things it does not show, and five self-tests that can each fail: `06-simulation/stable-band/RESULTS.md`. Registered with **OP-4 (debit tolerance)**.
#### 5.5.4 Essentials are always affordable, by arithmetic first
> **1. The floor's own arithmetic. A person's credit for staying alive is sized to cover what staying alive costs.** This is the ordinary case and it covers everybody, however little else they do. Nobody is assessed, nobody applies, and nobody decides they qualify.
> **2. A backstop for the abnormal case. A restriction arising from a person's standing reaches non-essentials only.**
> **The floor is therefore not only a welfare provision. It is the error tolerance of the whole accounting.**
#### 5.5.5 The disparity ceiling — an absolute maximum, not an expected spread
> **Inside any one trust network's books, the ratio between the largest and the smallest lifetime credit cannot exceed `24 ÷ F`.**
##### It is an extreme, and nobody reaches it
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
| The network's choice on childhood | Highest reachable lifetime ratio |
|---|---|
| Credit a child's learning time in full | **2.400×** — the arithmetic ceiling is reachable |
| Credit none of it | **2.085×** — nobody can reach the stated ceiling, ever |
> **A network that does not credit childhood has a stated ceiling of 2.4× that no subscriber can reach, and its most industrious subscriber falls short of it for a reason that has nothing to do with how hard they worked.**
##### Four conditions on the bound
##### Why condition 4 is stated as narrowly as it is
> **The comparison against money is unchanged, and it is a fair one.** Money's spread reaches about **10⁶ ×** the median **within one country's own statistics** (SCF 2022 and Forbes). The bound above is the spread within one network's own books. **Two sets of books, compared like for like.**
> **⚠️ What is left open, and it is narrow.** **Floor-shopping** — joining the network with the most generous floor — is arrested by the seller choosing which network a transaction lands on (§4.0), so a network with an implausible floor loses sellers. **What still depends on OP-22 (minimum audit disclosure) is proving a *pledge's* backing across a model boundary** (§4.2). Registered, not settled.
#### 5.5.6 Why hoarding does not beat the bound
#### 5.5.7 What the simulations found
> **Formally stated, simulated, and stress-tested.** The formal statement and a plain-language explainer are in `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`. The adversarial pass of 2026-08-14 answered all three attacks — **Methuselah** (§5.5.6 above), **dynasty and household** (a household is a co-op; its dwelling debit splits per occupant by dwelling time, children included, so the bound is per person and inheritance dilutes it, §4.5), and **collector** (holdings raise your own debit, so a hoard bounds itself).
> **The stable band described in §5.5.3 was found on 2026-08-28** and is reported there. `06-simulation/stable-band/`, 60,000 people, every cell driven through the kernel's own gate and all eight conformance checks. **The band never closes, capacity binds rather than affordability, and the upper edge turns out to be an artefact of the American production method.**
#### 5.5.8 The real-distribution comparison
### 5.6 Why the alternative-economy graveyard does not apply
| Failure | What happened | Aequitas |
|---|---|---|
| **Circulation** | Ithaca HOURS businesses were *"drowning in Hours"*; Burlington Bread piled up at cafés with no way to recirculate. Scrip flows to whoever buys inputs outside the network and stops. | 🟢 **Cannot occur. There is no medium of exchange.** Credit never moves (A3); only debit moves, attached to its object. Nobody can drown in credit they cannot spend because nobody ever receives credit *from* anyone. |
| **Valuation** | Warren (1830) could not reconcile labour-for-labour with skill and disagreeableness. Time banking, 45 years on, still reports chronic skill shortage from flat-hour crediting. | ⚠️ **Partly answered.** A2 (time as measure) v0.3 makes training paid work, which addresses skill. **Onerousness remains open — OP-16 (onerousness gap).** |
| **Institutional** | Wörgl's scrip was suppressed by Austria's central bank *for working*, under the legal-tender monopoly. Ithaca died when its founder moved. | 🟢 **No issuer, no notes, nothing to counterfeit** — the legal instrument that killed Wörgl does not fit an accounting system. This is the substantive reason Aequitas must never be described as a currency. ⚠️ Founder dependency is answered only by §2's fourth screening question. |
## 6. Where the rest of the project lives
### Start here for any abbreviation or section reference
> **[`GLOSSARY.md`](GLOSSARY.md) is the index.** Every abbreviation this project uses — `OP-#` for an open problem, `A#` for an axiom, `IC-#` for an integrity check, `P#` for a named problem, `C#` for a critical-path item — resolves there, with a link to where it is defined. **If a label in these documents means nothing to you, the glossary is the first place to look, not this document's search box.**
### The companion documents
| What it is | Where |
|---|---|
| **The conformance requirements** — what must be true for an implementation to *be* Aequitas, written for implementers | [`Aequitas_Conformance_v0.8.md`](Aequitas_Conformance_v0.8.md) |
| **The objections register** — every open problem and every answered objection, with its status | [`Aequitas_Objections_v0.24.md`](Aequitas_Objections_v0.24.md) |
| **The plain-language companion**, assuming no economics background | [`Aequitas_Overview_v0.20.md`](Aequitas_Overview_v0.20.md) |
| **How adoption plausibly starts** — a reading of the historical record, not a statement of the system | [`Aequitas_Strategy_v0.6.md`](Aequitas_Strategy_v0.6.md) §5 |
| **The simulation programme** — what is being tested and in what order | [`Aequitas_Simulation_Roadmap_v0.2.md`](Aequitas_Simulation_Roadmap_v0.2.md) |
| **One paper per open problem** | [`open-problems/`](open-problems/) |
| **Settled working papers these documents still cite by name** | [`papers/`](papers/) |
### The rest of the project
| Folder | What is in it |
|---|---|
| [`../01-wiki/`](../01-wiki/) | One concept per page, linked to each other. **The worked detail behind most sections of this document lives here** — [`property-debit.md`](../01-wiki/property-debit.md), [`verification-ladder.md`](../01-wiki/verification-ladder.md), [`estimation-engine.md`](../01-wiki/estimation-engine.md), [`statistical-coverage.md`](../01-wiki/statistical-coverage.md), [`debit-taxonomy.md`](../01-wiki/debit-taxonomy.md) |
| [`../02-research/`](../02-research/) | Downloaded sources and original research notes, each with its citation and the date it was retrieved |
| [`../03-journal/`](../03-journal/) | A dated development log |
| [`../04-use-cases/`](../04-use-cases/) | End-user scenarios |
| [`../05-marketing/`](../05-marketing/) | Public-facing material |
| [`../06-simulation/`](../06-simulation/) | Every simulation, one folder each, with its own README and results. **Where the numbers quoted in §3.5 and §5.5 were produced** |
| [`../07-outreach/`](../07-outreach/) | The outreach agent that puts these arguments in front of outside critics |
| [`../99-archive/`](../99-archive/) | Superseded versions and finished plans. **Nothing in it is current** |
