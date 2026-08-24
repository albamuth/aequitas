# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.2
> **Date:** 2026-07-31
> **Status:** Working foundations, derived from `Aequitas_Overview_v0.1.md` + design interview.
> **Supersedes:** `99-archive/Aequitas_Foundations_v0.1.md`. **A7 amended** — see §12.
> **Also supersedes:** OFCS (Open Fair Credit Standard) — see §8 for what is deliberately *not* inherited.
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

**A7 — Universal accounting, voluntary realization.**
Every human is accounted for whether or not they participate, and **credit and debit are estimated symmetrically for everyone** (§5.1). A person who grows food grows it whether or not they hold an account; the accounting describes physical reality, not membership.

Estimation and entitlement are separate:

- **Accounted** — every human carries an estimated credit *and* debit position, derived from cohort models plus whatever is known. This is a factual claim about material flows, not a claim on or by the person.
- **Realizable** — an estimated position acts on a person's debit ceiling only once they hold a **verified account** and their estimates have been superseded by observed, attested records.

So non-participants are fully represented in the books and can draw nothing from them. **Participation is the act of converting an estimate into a record.**

**Corollary — credit is issuable retroactively.** When a person joins, their prior real contributions become knowable and enter the record at the dates they occurred. This is retroactive re-weighting (§3.3) applied to the credit side, and A6 already requires it.

> **Design constraint — estimation error is not symmetric.** Over-estimating someone's debit consumes nothing. Over-estimating credit inflates real consumption ceilings on the basis of guessed production. The two sides are symmetric in *form* and asymmetric in *consequence*, which is precisely why realization is gated on observation and estimation is not.

*Amended in v0.2. The original A7 held that only account-holders could be credited — see §12 for why that was inconsistent.*

**A8 — Governance is a protocol property, not an institution.**
No organization that grows up around Aequitas may acquire authority over its core rules. Rules evolve as *immutable core + local variance*, with variance competing in the open.

---

## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No ad-hoc rules, no exceptions, no special cases for professions, nations, or classes. The units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7, v0.2), so there is no population outside the model and no asymmetry between who is charged and who is credited. |
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
- **Participation is voluntary. Coverage is not.** Non-participants are accounted for by statistical proxy, on **both sides of the ledger**:

| | Estimated from |
|---|---|
| **Debit** | Demographic cohort average — e.g. "male American living in Houston" carries that cohort's average debit load, computed *excluding* registered participants. Public figures estimated from publicly known wealth and holdings. |
| **Credit** | Cohort production model — occupation, region, and known activity. A subsistence farmer's food production is real material flow and is estimated as such. |

- **Non-participants can neither draw on nor be charged for their estimated position.** It is a description of physical flows, not an account they hold.
- **Estimating only debit was a factual error, not merely an unfair one.** A non-participant's production is real; recording the consumption while omitting the production makes the global books describe a world where material appears from uncreditable sources. See §12.

### 5.1a Realization

An estimated position becomes a real one through two gates:

1. **Verified account** — one verified human, one account (C6).
2. **Observed supersession** — the estimate is replaced by attested records of what actually happened, under the monotonicity rule (records may only improve toward stronger basis and finer resolution; an observation may never be superseded by an estimate).

Only then does the position act on the holder's debit ceiling. **Assertion is not evidence.** A person joining and claiming large past production must supply attested records, not a claim.

### 5.2 Onboarding as resolution — and as the adoption incentive

Joining is the act of **replacing an assigned average with your real record.** A new account starts at a global average and progressively resolves toward granular truth as the person supplies facts about themselves: location, age, sex/gender, ethnicity, job category, property owned, past employment, economic history.

Two forces make it individually rational:

1. Most people's true footprint is *below* the average assigned to their cohort.
2. **Their estimated credit is unrealized until they join.** Retroactive credit (A7) means a lifetime of real contribution is already described in the books and waiting to be substantiated.

**The v0.2 amendment inverts the pitch.** Under the original A7, Aequitas approached a non-participant with an estimated debt and nothing else — which is both a weak offer and, as §12 notes, a false picture. Symmetric estimation lets it say instead: *here is what you have contributed, and here is what it cost; join and make it yours.*

This also resolves the framing problem previously logged as unaddressed — *"you assigned me a debt I didn't consent to."* The answer is that the system assigned an estimate of **both** sides, and the estimate is a description of physical activity, carrying no enforcement against non-participants whatsoever.

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
- **OP-3 — The estimation engine.** Cohort model, granularity hierarchy, and the convergence path from global average → individual truth. **v0.2 widens this: it now requires a cohort *production* model, not only a consumption model.**
- **OP-14 — Cohort shopping.** Under symmetric estimation, a joiner has an incentive to self-identify into a high-production cohort. Nothing currently prevents it. *Introduced by the v0.2 amendment.*
- **OP-15 — Ghost harvesting.** Estimated credit accrues to people who never join, and to the dead. Who, if anyone, may substantiate a position on behalf of a person who cannot? Interacts with proof-of-personhood (C6) and with the unresolved question of what happens to a closed account's permanent consumption history. *Introduced by the v0.2 amendment.*
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

---

## 12. Amendment record

### v0.2 — A7 amended (2026-07-31)

**Original A7 (v0.1):**
> Every human is accounted for whether or not they participate. Non-participants are estimated statistically (§5.1). But **only account-holders can be credited.**

**Changed to:** symmetric estimation of credit and debit for every human, with realization gated on a verified account and observed supersession. Credit is issuable retroactively.

Amending a fixed axiom requires a reason strong enough to survive re-litigation. There are three, in descending order of force.

**1. The original A7 was internally inconsistent with the event log (C1).**

This is the decisive argument and it is not a matter of fairness.

A non-participant subsistence farmer grows wheat. That wheat is a real parcel with real ancestry, and under C1's origin closure (IC-3) every parcel must trace to a reservoir extraction through events that have agents. The event is recorded; the agent exists; but under v0.1 that agent could not be credited. The global books therefore describe a world in which **material is produced and no one produced it.**

The old rule did not merely under-credit non-participants — it made the accounting describe something physically false. Since the entire theory rests on the accounting being a description of material reality (A1), that is a contradiction at the root, not a policy preference.

**2. It was an ad-hoc asymmetry, and universality forbids those.**

v0.1 estimated one side of the ledger for everyone and the other side only for members. That is a special case keyed on participation status — precisely the kind of exception the universality criterion exists to exclude. Symmetric estimation removes it. **The amendment makes A7 more universal, not less.**

**3. It made the system's public posture false and hostile.**

Under v0.1, Aequitas approached every non-participant on Earth with an estimated debt and no acknowledgement of anything they had ever produced. That is both a weak offer and an inaccurate one, and it was already logged as an unresolved framing problem. §5.2 now inverts it.

### What the amendment does *not* change

- **Only realized positions act on a debit ceiling.** The substance of v0.1's "only account-holders can be credited" survives as the realization gate — it is relocated, not deleted.
- **Estimates carry no enforcement.** Nothing may be collected from a non-participant, before or after this change.
- **Assertion is not evidence.** Retroactive credit requires attested records under the supersession monotonicity rule.

### Known costs of the amendment

- **Estimation error becomes asymmetric in consequence.** Over-estimated debit consumes nothing; over-estimated credit inflates real consumption ceilings. This is why realization is gated, and it is a permanent design constraint rather than a solved problem.
- **OP-3 widens** — a cohort *production* model is now required, not only consumption.
- **Two new open problems:** OP-14 (cohort shopping) and OP-15 (ghost harvesting).
- **Decentralization pressure increases.** Whoever maintains the cohort production model influences ceilings. This compounds the unresolved weighting-model governance problem.

---

*End of v0.2.*
