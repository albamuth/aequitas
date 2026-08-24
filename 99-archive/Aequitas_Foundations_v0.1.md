# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.1
> **Date:** 2026-07-31
> **Status:** Working foundations, derived from `Aequitas_Overview_v0.1.md` + design interview.
> **Supersedes:** OFCS (Open Fair Credit Standard) — see §8 for what is deliberately *not* inherited.
> **Primary audience of the first paper:** technologists / implementers. Academic, civic-reformer, and public-facing papers follow later (§9).

---

## 0. The One-Sentence Theory

> **Aequitas is a universal accounting of material flows.** Every credit and every debit is a record of matter and energy moving through the world, attributable to the people who caused the movement. Nothing else is value.

Everything downstream — no capitalism, no rent, no taxation, no externalities, no inflation — is a *consequence* of taking that single rule seriously and applying it without exception.

---

## 1. Axioms

These are the immutable core. Nothing in Aequitas may contradict them, and no local variance may amend them.

**A1 — Materialism of Value.**
Credit and debit are records of material and energy flows. Down to the oxygen a human inhales and the CO₂ they exhale. There is no abstract, issued, or fiat value anywhere in the system.

**A2 — Time is a measure, not a substance.**
Time is a convenient universal yardstick for summarizing flows (it is measurable identically everywhere — a local second is a local second, even at relativistic speed). But an hour is not *itself* value. **Labor is never rate-scaled.** Differences between workers resolve as *material* differences, never as a multiplier:
- *Hard labor* → extra caloric intake is recorded as real food-production cost.
- *Skilled labor* → the training (time + materials of schooling) is a real cost that flows downstream into the debit of the service recipient.
- *Hazardous labor* → health harms discovered later are retroactively injected as debit into the products/services that caused them.

**A3 — Non-fungibility.**
Every credit and debit is a unique, non-exchangeable record of a specific event. Credits cannot be transferred, traded, gambled, lent, or stolen. Only *debit* moves, and only by transferring the thing it is attached to.

**A4 — No externalities.**
Every consequence of an activity is priced into it, including consequences discovered decades later. There is no "outside" of the accounting.

**A5 — Price ≡ Cost.**
The price of anything is its true, current-best-estimate material cost. There is no profit in exchange — only debit discharged and debit acquired. Competition happens on **quality, artfulness, and efficiency**, never on margin.

**A6 — Derived, not stored.**
Balances are not authoritative; the **event log** is. Any account's standing is a pure function of *(its events × the current scientific cost-weighting model)*. Improve the science, and all history re-weighs automatically (§3.3).

**A7 — Universal coverage, voluntary participation.**
Every human is accounted for whether or not they participate. Non-participants are estimated statistically (§5.1). But **only account-holders can be credited.**

**A8 — Governance is a protocol property, not an institution.**
No organization that grows up around Aequitas may acquire authority over its core rules. Rules evolve as *immutable core + local variance*, with variance competing in the open.

---

## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No ad-hoc rules, no exceptions, no special cases for professions, nations, or classes. The units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation, so there is no population outside the model. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing local variance — capture of one body cannot alter the system. |
| **Fecundity** | The verification ladder *pulls* technological development (§4). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses actively want (§7.3). Onboarding converts an assigned average debit into a real, offsettable balance — so joining is individually rational (§5.2). Enrichment funds its own future production (§6.3). |

---

## 3. The Ledger Model

### 3.1 Structure — an event log, not a balance

There is one permanent, append-only **record of activity**: who did what, when, involving which materials and energy. A record of work done on a certain day making a certain batch of goods stays part of that person's account data forever, and simultaneously forms part of the global logistical record of human activity.

An account's displayed standing is a **continuously recomputed projection** of that log.

### 3.2 The two kinds of debit

This distinction does an enormous amount of the theory's work.

**Property debit — a *current-holdings* term. Dischargeable.**
- You take on an item's accumulated life-cycle debit when you acquire it.
- Transferring ownership releases it entirely.
- Work done on property *increases* the property's debit-cost (and thus the holder's).
- **The self-work identity:** a homeowner repairing their own house earns credit for the labor exactly equal to the property's debit increase — net zero, excluding materials and energy consumed. This is the mechanism that makes property a burden rather than an engine.

**Consumption / pollution debit — a *permanent-history* term. Never discharged.**
- Locked into the record forever.
- But its **weight floats** with the current cost of mitigation (§3.3).

### 3.3 Retroactive re-weighting

When science improves — better emissions measurement, cheaper carbon capture, a newly discovered occupational harm — **every affected ledger in history recalculates.**

If atmospheric CO₂ mitigation gets cheaper per tonne, then everyone's past fossil-fuel consumption *weighs less*, because undoing it now costs less time and energy. Conversely, a newly discovered long-term health harm from a manufacturing process retroactively adds debit to the products made by it, trickling down to their final owners.

This is the engine of fecundity: **the system permanently rewards better measurement of reality.**

### 3.4 Granularity is opportunistic

Record what is known; estimate the rest from averages; refine forever.

> If someone commutes daily, their road usage can be computed and shown in their ledger. Absent specifics, estimate from averages (average commuter fuel use, Schaumburg → downtown Chicago, 5×/week). Learn which car they drive, and the carbon cost and road-wear share sharpen. All of it is revisable retroactively.

---

## 4. Verification — the Four-Level Ladder

Aequitas does not require advanced technology to begin. It specifies a **maturity ladder**, and each rung is independently viable. This is what lets it be universal *now* and rigorous *later*.

**Level 1 — Peer / witness attestation.**
Events confirmed by humans present, multi-party sign-off. Zero infrastructure. Works in any village on Earth today. *Weakness: collusion.*

**Level 2 — Reputation + stake over a social graph.**
Attestation augmented by relationship and proximity data — the way social media models connections. Verifiers stake reputation; the graph itself is used to audit attestation patterns and detect collusion rings. *This is the rung that makes Level 1 trustworthy at scale.*

**Level 3 — Sensors + cryptographic proof.**
Physical events proven by instruments (meters, cameras, GPS, industrial telemetry) with signed, tamper-evident records. Objective, infrastructure-heavy.

**Level 4 — Agentic auditing.** *(far-future)*
Autonomous systems perform continuous tallying and auditing of the full logistical record.

**Design rule:** every level must produce records interoperable with every other level, and the system must degrade gracefully downward. A Level 3 region and a Level 1 region must be able to trade.

---

## 5. Identity, Privacy, and Onboarding

### 5.1 Coverage without coercion

- **One verified human = one account.** Hard Sybil resistance is required for integrity.
- **Participation is voluntary.** Non-participants are still accounted for by statistical proxy:
  - Ordinary person → demographic average (e.g. "male American living in Houston" carries the average debit load for that cohort, computed *excluding* registered participants).
  - Public figure → estimated from publicly known wealth and holdings.
- **Non-participants cannot be credited.** They can only accrue estimated debit.

### 5.2 Onboarding as debt-resolution — and as the adoption incentive

Joining is the act of **replacing an assigned average with your real record.** A new account starts at a global average and progressively resolves toward granular truth as the person supplies facts about themselves: location, age, sex/gender, ethnicity, job category, property owned, past employment, economic history.

Because most people's true footprint is *below* the average assigned to their cohort, and because only account-holders can earn credit, **onboarding is individually rational.** This is the growth mechanism.

### 5.3 Privacy

Account holders keep a **private ledger with provable claims** — you disclose zero-knowledge proofs of your balances and cost positions when transacting, not your history.

---

## 6. The Three Credit Types

The Production / Service / Enrichment triad is not decorative — each behaves differently and answers a different question.

### 6.1 Production credit → raises the debit ceiling
Making material things. Governs how much you may hold and consume.

### 6.2 Service credit → converts to responsibility and influence
Labor that produces no object: care, teaching, medicine, civil service. **This is a genuine gap requiring design work** (§10, OP-1). Three candidate mechanisms to develop and reconcile:
- **Domain-scoped voting weight** — service credit in transit weighs on transit decisions only. Expertise-weighted democracy, non-transferable across domains.
- **Stewardship eligibility** — accumulated service unlocks the right to hold coordinating/planning roles. Influence via office.
- **Proposal power with universal suffrage** — high service credit grants the right to *propose*; everyone affected votes equally. Separates agenda-setting from deciding.

### 6.3 Enrichment → non-convertible social metric
Art, science, teaching, discovery. **Enrichment is not convertible to time or material.** It is a social value signal that "comes in many flavors that defy strict categorization."

Its function: **it is the channel by which people voluntarily direct their credit surplus.** A production company that makes a film many people appreciate is granted more **debit-room** for its next film by the very people who appreciated it.

**Hard constraint: allocation must be entirely voluntary, never compulsory.**

Enrichment is also the mechanism for **meme tracing** — feedback-weighted recognition of idea originators as ideas replicate and spread, crediting creators without ever suppressing usage. No patents, no exclusion.

---

## 7. Consequences (why the claims in the Overview hold)

### 7.1 Capitalism cannot function
Price ≡ cost means no profit in exchange. Property debit releases only on transfer, and self-work nets to zero. Therefore: **no rent, no rental income, no property speculation, no compounding capital.** Not banned by rule — structurally impossible.

### 7.2 Exploitation and pollution self-penalize
Harmful production carries the remediation cost of the harm. Exploitative labor and pollution make a product *dearer*, not cheaper. The incentive gradient reverses without any regulation.

### 7.3 Regulators invert into services
An EPA-like body stops being an adversary and becomes something businesses **actively want**, because it helps them lower the debit-cost of their products. Enforcement becomes consulting.

### 7.4 Taxation is unnecessary
Civil servants are credited directly for service. Infrastructure providers are credited; users carry proportional debit by usage. There is nothing to collect.

### 7.5 The basic-needs floor
- **Age-based debit tolerance** — every account may carry a baseline of debit with no credit backing it. The formula should be derived by evaluating total production of essential goods and asking what an even distribution looks like.
- **Essential provision is unconditional** — a mental health counselor is credited for providing service *regardless of the recipient's debit standing*.
- **Enforcement is graduated, not punitive:** exceeding tolerance restricts **non-essentials only**. Essentials always flow.

---

## 8. Deliberate Divergences from OFCS

| OFCS | Aequitas |
|---|---|
| "Credit syndicates" | **Businesses / institutions.** "Syndicate" is alienating jargon; drop it. |
| Restructures society broadly | **Surgical.** Keep the functional parts of society — municipal government, planning bodies, civil service — and change only their *economic nature*. Target the corrupt influence of capitalists and oligarchy, not the institutions that work. |
| Loose "set of requirements" | Rigorous axioms with a single mechanism (§1). |
| Self-regulation by participants | Governance as **protocol property**, independent of any organization that arises (A8). |
| — | **Enrichment** as a distinct, non-convertible credit type. |
| — | **Meme tracing** for idea attribution. |
| — | **Retroactive re-weighting** of all history as science improves. |
| — | **Statistical coverage of non-participants.** |

**Guiding principle of the divergence:** OFCS went too far in re-structuring the organization of society. Aequitas creates an economic system in which the functional aspects of society continue to serve and improve, while tearing out oligarchic capture.

---

## 9. Document Roadmap

1. **Foundations & Protocol** *(this document → next: full spec)* — audience: **implementers**. Data model, verification ladder, estimation engine, interop. **Build first.**
2. **Academic paper** — engages Marx / Hayek / Ostrom; must answer the socialist-calculation critique head-on.
3. **Civic reformer brief** — municipalities, co-ops, transition communities. Pilot-oriented.
4. **Public-facing text** — the readable, persuasive foundational book.

Each needs its own strategy; 2–4 follow after the practical implementation exists.

---

## 10. Open Problems

Ranked by how load-bearing they are.

- **OP-1 — Service → influence.** Formalize how service credit becomes responsibility and direction over public services. Explore all three candidates in §6.2. *The most important unsolved piece.*
- **OP-2 — Anti-collusion at Level 2.** Precisely how the social graph audits attestation. The whole decentralization claim rests here.
- **OP-3 — The estimation engine.** Cohort model, granularity hierarchy, and the convergence path from global average → individual truth.
- **OP-4 — Debit tolerance formula.** Derive the age-based baseline from total essential-goods production under even distribution.
- **OP-5 — Education.** Schooling is credited work (it enriches the individual *and* society indirectly), while its cost flows downstream into the services the graduate later provides. Needs a full treatment.
- **OP-6 — Enrichment mechanics.** How voluntary surplus-direction actually works without becoming a popularity plutocracy.
- **OP-7 — Cross-level trade.** Ensuring a Level 1 community and a Level 3 community can transact fairly.
- **OP-8 — Non-convertibility boundaries.** Exactly where Enrichment must be firewalled from Production/Service to prevent it becoming currency by the back door.

---

## 11. First Foothold — the MVP

**Full-cost accounting as a parallel overlay on existing commerce.** It requires no adoption, no permission, and no legal change — it just computes and publishes truth alongside money.

Two components:

**(a) Product & service debit-costing.** Compute and publish the true debit-cost of real products. Proves the math publicly and immediately.

**(b) Account intake with progressive debt resolution.** A person opens an account and answers questions about themselves; their estimated debit resolves from **global average → granular cohort → individual record** as facts accumulate.

> A compelling early tool: a **"try it" account** — answer questions about yourself and watch your assigned debit sharpen from the global average down to something specific to your location, age, work, and holdings. It demonstrates the estimation engine, the onboarding incentive, and the honesty of the accounting all at once — and it is genuinely fun.

This single build exercises the estimation engine (OP-3), produces the public artifact that makes the theory legible, and creates the on-ramp for every later stage.

---

*End of v0.1.*
