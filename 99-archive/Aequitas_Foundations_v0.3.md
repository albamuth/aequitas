# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.3
> **Date:** 2026-08-01
> **Status:** Working foundations.
> **Supersedes:** `99-archive/Aequitas_Foundations_v0.2.md`. **A2 amended; §6 restructured; §0 reframed.** See §12.
> **Also supersedes:** OFCS (Open Fair Credit Standard) — see §8 for what is deliberately *not* inherited.
> **Primary audience of the first paper:** technologists / implementers.
> **Companion:** `00-strategy/Aequitas_Objections_v0.1.md` — the objections register. Read alongside §10.

---

## 0. The One-Sentence Theory

> **Aequitas is a universal accounting of material flows.** Every credit and every debit is a record of matter and energy moving through the world, attributable to the people who caused the movement. **Cost is nothing other than this.**

**Aequitas is a theory of cost. It is not a theory of value, and it does not need to be.**

This distinction is load-bearing and it is new in v0.3. Every previous attempt at objective accounting — Odum's emergy, Technocracy's energy certificates, the labour theory of value — claimed to have found what things are *worth*, and every one was refuted on the same ground: **supply-side only, ignores demand.** The refutation is a stock move and takes one sentence.

Aequitas makes the narrower and far more defensible claim. **Cost is what a thing takes from the world; it is physical, and we can measure it. Value is what someone thinks it is worth; it is not physical, and we do not attempt to measure it.** Value enters the system as *feedback and pledges* (§6), never as an accounting quantity.

Everything downstream — no capitalism, no rent, no taxation, no externalities, no inflation — is a *consequence* of taking the cost rule seriously and applying it without exception.

---

## 1. Axioms

These are the immutable core. Nothing in Aequitas may contradict them, and no local variance may amend them.

**A1 — Materialism of Cost.**
Credit and debit are records of material and energy flows. Down to the oxygen a human inhales and the CO₂ they exhale. There is no abstract, issued, or fiat quantity anywhere in the system.

*Grounding for attribution.* Flows are attributed to whoever caused them, on the juridical principle of **responsibility imputation** — impute responsibility in accordance with who was in fact responsible. This is [David Ellerman's labour theory of property](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf), and it is deliberately preferred to any labour theory of *value*: it is a theory of imputation, it inherits none of the transformation or negative-value problems, and it appeals to a principle its opponents already accept everywhere else. Only humans act; tools and capital do not. Responsibility therefore imputes to people, never to machinery or its owners.

**A2 — Time is a measure, not a substance.** *(amended v0.3)*
Time is a convenient universal yardstick for summarizing flows — a local second is a local second, measurable identically everywhere. But an hour is not *itself* value. **Labor is never rate-scaled.** Differences between workers resolve as *material* differences, never as a multiplier:

- **Hard labor** → extra caloric intake is recorded as real food-production cost.
- **Hazardous labor** → health harms discovered later are retroactively injected as debit into the products and services that caused them.
- **Skilled labor** → **training is credited work in its own right, and its cost is discharged at the time of training.** Nothing flows downstream. See §6.2.

**A3 — Non-fungibility.**
Every credit and debit is a unique, non-exchangeable record of a specific event. Credits cannot be transferred, traded, gambled, lent, or stolen. Only *debit* moves, and only by transferring the thing it is attached to.

A3 is not a design preference. Under A1 it is a **consequence**: credit records who was responsible, responsibility is a fact about a person, and facts about people do not change hands. It also does three defensive jobs at once — see §7.6.

**A4 — No externalities.**
Every consequence of an activity is priced into it, including consequences discovered decades later. There is no "outside" of the accounting.

**A5 — Price ≡ Cost.**
The price of anything is its true, current-best-estimate material cost. There is no profit in exchange — only debit discharged and debit acquired. Competition happens on **quality, artfulness, and efficiency**, never on margin.

**A6 — Derived, not stored.**
Balances are not authoritative; the **event log** is. Any account's standing is a pure function of *(its events × the current scientific cost-weighting model)*. Improve the science, and all history re-weighs automatically (§3.3).

**A7 — Universal accounting, voluntary realization.**
Every human is accounted for whether or not they participate, and **credit and debit are estimated symmetrically for everyone** (§5.1).

- **Accounted** — every human carries an estimated credit *and* debit position. A factual claim about material flows, not a claim on or by the person.
- **Realizable** — an estimated position acts on a person's debit ceiling only once they hold a **verified account** and their estimates have been superseded by observed, attested records.

Non-participants are fully represented in the books and can draw nothing from them. **Participation is the act of converting an estimate into a record.**

**Corollary — credit is issuable retroactively.** When a person joins, their prior real contributions enter the record at the dates they occurred.

> **Design constraint — estimation error is not symmetric.** Over-estimating debit consumes nothing. Over-estimating credit inflates real consumption ceilings on the basis of guessed production. Symmetric in *form*, asymmetric in *consequence* — which is why realization is gated on observation.

**A8 — Governance is a protocol property, not an institution.**
No organization that grows up around Aequitas may acquire authority over its core rules. Rules evolve as *immutable core + local variance*, with variance competing in the open.

### 1.1 Named conventions — new in v0.3

Some quantities the system needs are **not** physical facts. Where that is true, it is stated here rather than hidden in an implementation detail. **A convention that is declared is not an ad-hoc rule; a convention that is disguised as a measurement is.**

| Quantity | Status | Why it is not a measurement |
|---|---|---|
| **Split of a joint process's debit across its co-products** | ⚠️ **Convention, not yet chosen** | Mass, energy, and exergy allocation give different answers and none is more physically true. **OP-17 — blocking C3.** |
| **Split of a team's credit across its members** | ⚠️ **Convention — currently hours-worked** | Responsibility for joint work is joint and non-decomposable (Ellerman). Hours-worked is defensible and simple, but it is a choice. **OP-18.** |
| **Division of a reproducible work's production debit across its audience** | ⚠️ **Convention, not yet chosen** | **OP-21.** |

These three are the same problem at three scales. **The project's hard problem is division, not measurement** — see the objections register §0.

---

## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No exceptions for professions, nations, or classes. Units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7). Where a genuine convention is required, §1.1 names it rather than concealing it. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing local variance. |
| **Fecundity** | The verification ladder *pulls* technological development (§4). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses want (§7.3). Onboarding is individually rational (§5.2). Pledges give surplus a purpose (§6.4). |

**Fourth screening question, added v0.3 — "does this need a Paul Glover?"**
Ithaca HOURS died when its founder relocated; he himself said every local currency needs a full-time networker to promote, facilitate, and troubleshoot. A mechanism that depends on an enthusiast is a mechanism with an expiry date. **Every proposed mechanism must pay its own maintainer from inside the system** — as auditing-as-credited-work does. Apply alongside universality, decentralization, and *who games this?*

---

## 3. The Ledger Model

### 3.1 Structure — an event log, not a balance

One permanent, append-only **record of activity**: who did what, when, involving which materials and energy. An account's displayed standing is a **continuously recomputed projection** of that log.

### 3.2 The two kinds of debit

**Property debit — a *current-holdings* term. Dischargeable.**
- You take on an item's accumulated life-cycle debit when you acquire it.
- Transferring ownership releases it entirely.
- Work done on property *increases* the property's debit-cost.
- **The self-work identity:** a homeowner repairing their own house earns credit for the labor exactly equal to the property's debit increase — net zero, excluding materials and energy consumed. This is what makes property a burden rather than an engine.
  - *Corollary — subsistence.* Growing food and eating it yourself is the same identity: the farming labour credits you, the food carries that debit, consuming it returns the debit to you. **Net zero on labour, net cost on materials and energy consumed.** No special rule is needed; the existing identity already answers it.

**Consumption / pollution debit — a *permanent-history* term. Never discharged.**
- Locked into the record forever.
- But its **weight floats** with the current cost of mitigation (§3.3).

### 3.3 Retroactive re-weighting

When science improves, **every affected ledger in history recalculates.** Cheaper CO₂ mitigation makes everyone's past fossil use weigh less; a newly discovered occupational harm retroactively adds debit to the products made by the process that caused it.

This is the engine of fecundity: **the system permanently rewards better measurement of reality.**

*Tractability is not speculative.* [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) demonstrated that in-kind calculation at national scale is computationally feasible with sparse-matrix methods. Mises's objection was in-principle; the empirical scale objection has been answered by people who ran the arithmetic.

### 3.4 Resolution is opportunistic — allocation is not

**Resolution.** Record what is known; estimate the rest from averages; refine forever. If someone commutes daily, estimate from cohort averages; learn which car they drive and it sharpens. All of it revisable.

**⚠️ Allocation is a different thing and does not behave this way.** When one process yields several outputs, no amount of better instrumentation resolves the split, because **the indeterminacy is not epistemic.** Refining forever converges on nothing. Allocation requires a declared convention (§1.1). Do not treat OP-17 as a data-quality problem.

### 3.5 The books never balance — and must not *(new in v0.3)*

Every real process dissipates. Credit records useful work; debit records material and energy consumed plus pollution. **Aggregate debit therefore exceeds aggregate credit permanently and by construction.**

This is not an accounting defect. **It is the second law of thermodynamics appearing in the ledger**, and a material-flow accounting that *did* balance would be the one describing something physically false.

Two consequences:

1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds, not merely impractical.
2. **Sums are not meaningful; two separate numbers are.** **Ratio** (debit:credit) measures *efficiency* — how much you consumed per unit contributed. **Absolute credit** measures *contribution*. Neither substitutes for the other: a pure-ratio metric is infinite for a newborn and is gamed by ascetics who minimize both sides; a pure-sum metric ignores waste entirely.

**Why this does not collapse the economy, where a currency would.** In a monetary system, aggregate debt exceeding aggregate money is a solvency crisis — debt-deflation, spiral, collapse. Here **there is no creditor to be made whole**, because credit is non-fungible and never moves (A3). Permanent aggregate net-debit is simply the correct description of an economy running on a thermal gradient.

---

## 4. Verification — the Four-Level Ladder

**Level 1 — Peer / witness attestation.** Events confirmed by humans present, multi-party sign-off. Zero infrastructure. Works in any village on Earth today. *Weakness: collusion.*

**Level 2 — Reputation + stake over a social graph.** Verifiers stake reputation; the graph audits attestation patterns. Treated as an **emergent market of trust networks** where auditing is credited work, not as a detector designed up front.

**Level 3 — Sensors + cryptographic proof.** Physical events proven by instruments with signed, tamper-evident records.

**Level 4 — Agentic auditing.** *(far-future)* Autonomous continuous tallying of the full logistical record.

**Design rule:** every level must produce records interoperable with every other level, and the system must degrade gracefully downward. A Level 3 region and a Level 1 region must be able to trade.

---

## 5. Identity, Privacy, and Onboarding

### 5.1 Coverage without coercion

- **One verified human = one account.** Hard Sybil resistance is required for integrity.
- **Participation is voluntary. Coverage is not.** Non-participants are estimated on **both sides**:

| | Estimated from |
|---|---|
| **Debit** | Demographic cohort average, computed *excluding* registered participants. Public figures estimated from publicly known wealth and holdings. |
| **Credit** | Cohort production model — occupation, region, known activity. |

- **Non-participants can neither draw on nor be charged for their estimated position.**

### 5.1a Realization

1. **Verified account** (C6).
2. **Observed supersession** — the estimate is replaced by attested records, under monotonicity (records may only improve toward stronger basis and finer resolution; an observation may never be superseded by an estimate).

**Assertion is not evidence.**

### 5.2 Onboarding as resolution — and as the adoption incentive

Joining replaces an assigned average with your real record. Two forces make it rational: most people's true footprint is *below* their cohort average, and **their estimated credit is unrealized until they join.**

The pitch is: *here is what you have contributed, and here is what it cost; join and make it yours.*

### 5.3 Privacy

Account holders keep a **private ledger with provable claims** — zero-knowledge proofs of balances and cost positions when transacting, not history.

**This is roughly where society already sits, and that is the point.** People transfer money to each other today knowing their counterparty and nothing about third parties' accounts. Nobody audits those accounts, because validation trust is externalized to banks. **Aequitas does not need more visibility than that; it needs the same visibility with the trust relocated.**

**Aequitas also does not replace existing recourse.** Courts, small claims, contract law, and ordinary social pressure continue to exist and continue to handle fraud between people. The system's contribution is upstream of enforcement: by removing wealth concentration and material insecurity, it **removes most of the motive** for the scams those mechanisms exist to punish.

> **⚠️ The narrow question that remains — OP-22.** The bank analogy has one gap: there is no bank to externalize validation to. Verification is the trust-network ecosystem (Level 2), and an auditor must be able to see *something*. So the live question is not "surveillance or privacy" but **"what is the minimum an auditor must see to verify a claim without seeing a history?"** Zero-knowledge proofs are the right shape of answer and are already specified above; what is missing is the precise disclosure set. **This is a C7 implementation problem, not a foundational contradiction.**

---

## 6. One Credit, Three Feedback Channels *(restructured in v0.3)*

**There is one credit: time worked, recorded as material flow.** Production, service, and enrichment are **not** different credit types and do not credit at different rates. Everyone earns at the same rate and therefore influences at the same rate.

**The categories have no accounting boundary and no rule may use them as one.** An apprentice plumber's single hour is simultaneously enrichment (learning the trade), service (fixing a customer's pipes), and production (copper and fittings → working plumbing). That hour is not partitionable, and any attempt to partition it would require yet another allocation convention (§1.1).

What the three names *do* describe is **how feedback reaches the work** — how a society tells someone that what they did mattered.

### 6.1 Why "enrichment" is named at all

**To give grounds for crediting work that no economy has ever credited.**

Going to school is work. Today we make students or their parents pay for it — the relationship is inverted. Teaching your own child is work. Caring for a relative is work. None of it is paid, and in a system that does not incentivize with material gain — *"go to school if you want to make money"* — something must make socially beneficial activity individually rational.

Enrichment is the name for work whose benefit flows **from all of humanity to at least one person, in ways not readily measured in material.** It is credited because it is real work, not because it is virtuous.

**Childcare is creditable work regardless of who performs it.** This alone brings the largest uncounted labour pool in human history onto the books.

### 6.2 Training, front-loaded *(A2 amendment — the substantive change in v0.3)*

**A student is credited for their time while training.** The debit of training — teachers' time, facilities, materials — is **discharged during the training years** by whoever pledged for it (§6.4).

**Nothing flows downstream.** A doctor's care costs the recipient exactly: the doctor's time, the material cost of running the clinic, and the medicines and correctives dispensed. **The doctor's education is not in that bill.** It was already paid for, by the people who wanted doctors to exist.

Why this is right and the v0.2 rule was wrong:

- **It makes training individually rational without any rate premium.** The old rule made the *service* expensive without ever rewarding the *trainee*; it answered a pricing question and left the incentive question open. Being trained is now paid work.
- **It matches who benefits.** Education's benefit is diffuse, so its cost should be borne diffusely. Charging it to one patient decades later is arbitrary — precisely the amortization problem that made OP-11 unanswerable.
- **It dissolves OP-11 rather than solving it.** There is no longer a cost to amortize over an uncertain career.
- **Pledging supplies the natural limit.** Society decides how many doctors to train by pledging for it. Unpledged study still credits the student's time — A7 requires that, it is real activity — but leaves them holding the debit. **No perpetual-studenthood exploit.**

### 6.2a The front-loading principle *(generalized in v0.3)*

Training is the first instance of a general rule, and the rule is worth stating once rather than rediscovering per case:

> **A large up-front cost with diffuse benefit is discharged at the time it is incurred, by those who pledged for it. It is never amortized downstream onto whoever happens to consume the result.**

Three instances so far:

| Case | Front-loaded cost | What the eventual recipient pays |
|---|---|---|
| **Education** | Teachers' time, facilities, materials | The professional's time, clinic materials, medicines — **not the education** |
| **Media production** | Years of crew time, sets, equipment, post | **Delivery only** — theatre maintenance, projectionist hours, print or bandwidth, power |
| **Research, infrastructure, tooling** | The build | Use, wear, and energy |

**Why downstream amortization is always the wrong answer.** It requires choosing a window (how many patients? how many viewers?) and every candidate window is arbitrary. That arbitrariness *was* OP-11, and it is also what made OP-21 look hard. **The question was malformed in both cases.** Front-loading removes the division rather than solving it — which is worth noticing, because §1.1's unsolved conventions are all divisions that could not be removed.

**The consequence for media is worth spelling out.** Pledgers replace studios and investors, and **they receive no profit and cannot receive one** — so there is no mechanism by which a popular film gouges its audience at the box office. A production company's only return is recognition, which converts into demand and pledges for the next work. That is the entire incentive, and it points at making something good rather than something extractive.

**⚠️ Cold start.** Pledges follow reputation, so a first-time filmmaker attracts none — structurally similar to the problem unknown creators already face with capital. The barrier is far lower (attention, not money) and the ladder is real: make small unpledged work, accrue feedback (§6.3), then attract pledges. But it should be stated honestly rather than assumed away.

### 6.3 Feedback: what each channel looks like

Feedback is **not credit** and never converts to it. It is how a society signals what it wants more of.

| Channel | What feedback looks like | Already exists today as |
|---|---|---|
| **Production** | The in-demand shoe sells out | Stock-outs, waiting lists, pre-orders |
| **Service** | Someone chooses you as their doctor, plumber, therapist | Ratings, referrals, repeat custom |
| **Enrichment** | People signal appreciation for the work | Likes, reviews, citations, applause |

**Non-convertibility, restated correctly.** v0.2 asserted that "Enrichment is not convertible to time or material" and then needed a firewall to enforce it (old OP-8). Under the corrected structure **no firewall is required**: enrichment *work* credits as time like everything else, and enrichment *feedback* is non-convertible because **it was never credit in the first place.** There is nothing to firewall.

**The live question is the inverse, and it is real: can feedback be *bought*?** A signal that credit can purchase is a currency by the back door. This is what OP-8 becomes.

### 6.4 Pledges and signals *(new in v0.3)*

Credit-earners direct what gets worked on next. Two distinct instruments, distinguished by one test:

> **Does it commit debit?**

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I will absorb this debit" | "I want this to exist" |
| Backed by | earned credit | nothing |
| Rate | **exactly 1 hour pledged per hour earned** | *n* per hour earned, or unbounded |
| Analogue | pre-order; choosing a GP; crowdfunding | likes, ratings, applause |

**Why pledges must be exactly 1:1.** A pledge that commits debit-absorption cannot exceed the credit backing it, or you get **fractional-reserve pre-ordering** — more debit committed than can be honoured, so when the goods arrive some pledger cannot take them and the producer is stranded holding it. This is a solvency constraint, not a preference. It also happens to be the only stationary value: pledging power created per period is *kL* and consumed at most *L*, so any *k* > 1 diverges until pledges filter nothing, and any *k* < 1 shrinks the directed economy to zero.

**Why signals should be plentiful.** Under 1:1 you can only signal for as much as you personally worked, so you signal your top priorities and the system learns nothing about your second tier. Cheap, abundant signals **reveal the full preference ordering rather than just the top slice.**

**What pledging is for:**

- **A decentralized demand signal.** Cost says what a thing takes; pledges say who wants it. Aequitas obtains this with no prices, no central optimizer, and **no Iteration Facilitation Board** — the standing body Parecon requires and [is attacked as implausible for](https://ejpe.org/journal/article/view/867).
- **A purpose for surplus.** A high producer whose ceiling far exceeds their appetite can *direct what gets made* instead of accumulating, which A3 forbids by design.
- **Funding education and speculative work** (§6.2, §6.6).
- **Collective prizes.** An X-Prize needs no oligarch or patron — a large enough pool of pledges is a crowdfunded bounty. Enterprise remains genuinely risky, as it always has been, and innovation has always flourished under that risk.

**Pledges are the affirmative case of custody acceptance**, the same rule that lets a transfer be refused. One mechanism, two directions — not a new primitive.

**Approval never gates credit.** You are always credited for what you materially did. What a pledge buys is a **guaranteed counterparty** for the resulting property debit. Gating credit on approval would resurrect the repealed A7 v0.1 and describe a world where unpledged wheat has no grower.

### 6.5 Attribution without intellectual property

There are no patents and no exclusion. Ideas replicate freely; **meme tracing** gives feedback-weighted recognition to originators as ideas spread.

**Art is not a commodity, and intellectual property is the antithesis of treating it as anything else.** Exclusion rights exist to let a holder extract profit from reproduction. With no profit in exchange (A5), the machinery has nothing to protect and no reason to exist.

**The right standard for attribution is *no worse than today*, not *perfect*.** Buy a painting from a gallery now and there is no video of its making; you trust the seller, and at person-to-person scale the stakes are low enough that this is fine. Provenance only becomes fraught in the capitalized art market, where licensing and reproduction are the revenue — which is precisely the layer Aequitas removes. **Aequitas does not need to solve a problem that the current world also has not solved and does not much suffer from.**

*A useful illustration, though not a general mechanism:* someone can copy an MP3 and claim it, but is unlikely to perform it live. When the incentive is to share the work rather than to sell copies, a recording functions as an advertisement for the performance. This holds well for music and poorly for writing, visual art, software, and research — so treat it as a good example rather than a rule.

### 6.5a Not all work is capturable — and the system does not require it to be

A2 and A4 describe how flows are accounted **when they are recorded**. Neither claims that all human activity must be recorded, and the difference matters, because a critic will read A1 as demanding total surveillance.

Memes are the clean case. People spend real time editing images and writing captions; the results propagate through conversation, entertainment, and provocation. **Tracing who shared what to whom in order to assign work-credit is neither possible nor desirable**, and a trust network that proposed it would be laughed out of the room — which is A8's local variance working exactly as intended.

> **Much of what people do, they do to entertain themselves and each other. The system does not need to capture it, price it, or credit it, and attempting to would be both futile and grotesque.**

The accounting covers what is claimed and attested. Everything else is life.

### 6.6 Unobservable work — and the lone fraudster

Creative and intellectual work is mostly thinking, which leaves no material trace and has no witness. Crediting only observable performance excludes most of it; trusting self-report without limit appears to invite unlimited fraud.

**The apparent hole is closed by three mechanisms that already exist, and none of them is new:**

1. **IC-7 caps the volume.** No account may claim more than 24 hours of activity per 24 hours. The press only runs so fast.
2. **Conservative weighting of low-confidence flows** (C1 §12) does the real work. Self-asserted, unwitnessed, near-zero-material work carries the weakest `basis` and lowest `confidence` in the log. Weighed at the **pessimistic end of its interval — which for a credit claim is close to zero** — the fabricated hours are recorded faithfully and are worth almost nothing until something corroborates them. **This is the general answer to unobservable work, and it is an incentive rather than an enforcement rule: vagueness is cheap to assert and cheap to hold.**
3. **Pledges bound what anyone will underwrite.** Someone pretending to be an artist, or generating unwanted volume at scale, attracts no pledges — and a pledge is the only thing that moves a claim from *asserted and near-worthless* to *backed*.

**On mass-produced slop specifically:** generation cost trending to zero means volume trending to infinity, so the defence cannot be per-item cost. It is that **nothing accrues without someone choosing to back it**, and a curation venue with no ad inventory to sell has no reason to reward volume. Note where the residual risk actually sits: not in credit issuance, but in **flooding the free signal channel** (§6.4). That belongs to **OP-6**, not here.

**Note what this does and does not claim.** Aequitas removes most of the *acquisitive* motive for fraud — there is no wealth to concentrate. It does not remove status-seeking, which is exactly what a false claim of creative hours would be. The defence against that is evidentiary, per points 1–3, not motivational.

---

## 7. Consequences

### 7.1 Capitalism cannot function
Price ≡ cost means no profit in exchange. Property debit releases only on transfer; self-work nets to zero. **No rent, no rental income, no property speculation, no compounding capital.** Not banned — structurally impossible. *Ellerman's route reaches the same conclusion independently: only people act, so only people can be responsible, so capital cannot claim a residual.*

### 7.2 Exploitation and pollution self-penalize
Harmful production carries the remediation cost of the harm. Exploitative labour and pollution make a product *dearer*, not cheaper. The incentive gradient reverses without regulation.

### 7.3 Regulators invert into services
An EPA-like body becomes something businesses **actively want**, because it helps them lower their debit-cost. Enforcement becomes consulting.

### 7.4 Taxation is unnecessary
Civil servants are credited directly. Infrastructure users carry proportional debit by usage. There is nothing to collect.

### 7.5 The basic-needs floor
- **Age-based debit tolerance** — every account may carry a baseline of debit with no credit backing it (OP-4).
- **Essential provision is unconditional** — a counselor is credited for providing service regardless of the recipient's standing.
- **Enforcement is graduated, not punitive:** exceeding tolerance restricts **non-essentials only**.
- **The efficiency ratio governs the discretionary layer only** (§3.5). It may never reach essentials, or it would fall hardest on the newborn, the old, the sick, and the disabled — exactly the people this section exists to protect.

### 7.6 Why the alternative-economy graveyard does not apply *(new in v0.3)*

A century of local currencies and time banks failed in three distinct ways. Aequitas is immune to one of them by construction, and should say so.

| Failure | What happened | Aequitas |
|---|---|---|
| **Circulation** | Ithaca HOURS businesses were *"drowning in Hours"*; Burlington Bread piled up at cafés with no way to recirculate. Scrip flows to whoever buys inputs outside the network and stops. | 🟢 **Cannot occur. There is no medium of exchange.** Credit never moves (A3); only debit moves, attached to its object. Nobody can drown in credit they cannot spend because nobody ever receives credit *from* anyone. |
| **Valuation** | Warren (1830) could not reconcile labour-for-labour with skill and disagreeableness. Time banking, 45 years on, still reports chronic skill shortage from flat-hour crediting. | ⚠️ **Partly answered.** A2 v0.3 makes training paid work, which addresses skill. **Onerousness remains open — OP-16.** |
| **Institutional** | Wörgl's scrip was suppressed by Austria's central bank *for working*, under the legal-tender monopoly. Ithaca died when its founder moved. | 🟢 **No issuer, no notes, nothing to counterfeit** — the legal instrument that killed Wörgl does not fit an accounting system. This is the substantive reason Aequitas must never be described as a currency. ⚠️ Founder dependency is answered only by §2's fourth screening question. |

A3 therefore does three separate defensive jobs: it forbids accumulation (§7.1), it makes permanent aggregate net-debit survivable (§3.5), and it makes the circulation failure impossible.

---

## 8. Deliberate Divergences from OFCS

| OFCS | Aequitas |
|---|---|
| "Credit syndicates" | **Businesses / institutions.** "Syndicate" is alienating jargon. |
| Restructures society broadly | **Surgical.** Keep the functional parts — municipal government, planning bodies, civil service — and change only their *economic nature*. Target oligarchic capture, not institutions that work. |
| Loose "set of requirements" | Rigorous axioms with a single mechanism (§1). |
| Self-regulation by participants | Governance as **protocol property** (A8). |
| — | **Pledges and signals** as the demand side (§6.4). |
| — | **Meme tracing** for idea attribution. |
| — | **Retroactive re-weighting** of all history as science improves. |
| — | **Statistical coverage of non-participants**, symmetric. |

---

## 9. Document Roadmap

1. **Foundations & Protocol** *(this document → next: full spec)* — audience **implementers**. **Build first.**
2. **Academic paper** — engages Marx / Hayek / Ostrom; must answer the socialist-calculation critique head-on. Lead with: theory of *cost* not value; Ellerman on attribution; Cockshott & Cottrell on tractability; pledges as a decentralized answer to preference revelation.
3. **Civic reformer brief** — municipalities, co-ops, transition communities.
4. **Public-facing text.**

---

## 10. Open Problems

Ranked by how load-bearing they are. Full detail in `00-strategy/Aequitas_Objections_v0.1.md`.

**Blocking**
- **OP-17 — Joint production allocation.** No physical rule splits one process's debit across its co-products; every candidate is a convention, and price-based allocation (what EEIO uses) collides with A5. **Blocks C3 — no debit-cost figure can be published without it.**
- **OP-10 — Weighting-model governance.** Whoever sets the cost model controls every balance in history without touching a core rule. Largest hole in A8. Now entangled with OP-9.

**High**
- **OP-18 — Responsibility is not divisible.** Hours-worked is a convention (§1.1), not a measurement.
- **OP-16 — The onerousness gap.** A2 resolves exertion, hazard, and (in v0.3) skill. **Tedium and indignity have no material signature and nothing allocates labour to them.** Leading candidate: *hour-ceiling differentiation* — pay the premium in hours, not rate, justified by measured physiological sustainability limits. First check how much of OP-16 is simply unmeasured hazard.
- **OP-1 — Service → influence.** Fourth and strongest candidate, new in v0.3: **pledging power accrues per hour worked, equally for all.** Not a voting scheme.
- **OP-6 — Feedback mechanics.** How signals aggregate without becoming a popularity plutocracy. **Promoted** — with accumulation forbidden, feedback and pledging are the entire motivation system for anyone past their own consumption ceiling.

**Medium**
- **OP-3 — The estimation engine.** Requires a cohort *production* model as well as consumption.
- **OP-8 — Can feedback be bought?** *(reframed)* The old firewall question dissolved with §6.3; what remains is whether credit can purchase signals.
- **OP-9 — Preference revelation.** Largely answered by §6.4 pledges, plus scarcity-as-debit on the Kantorovich framing — *taking the last unit of a constrained resource is a real cost to everyone else, recordable as debit rather than skimmed as margin.*
- **OP-22 — Minimum audit disclosure.** *(narrowed)* What must an auditor see to verify a claim without seeing a history? A C7 disclosure-set question, not a foundational conflict — see §5.3.
- **OP-4 — Debit tolerance formula.**
- **OP-14 — Cohort shopping.** · **OP-15 — Ghost harvesting.**
- **OP-7 — Cross-level trade.**
- **OP-19 — Saturated producer.** Largely resolved by §6.4.

**Closed in v0.3**
- ~~**OP-20 — Unobservable work.**~~ Closed by three existing mechanisms (§6.6): IC-7 caps volume, conservative weighting makes unattested credit worth ~nothing, and pledges bound what anyone will underwrite. **No new mechanism was required.** Residual risk is signal flooding, which belongs to OP-6.
- ~~**OP-21 — Media reproduction.**~~ Closed by §6.2a: production cost is **front-loaded and pledged, never divided across an audience.** The audience pays delivery only. The division question was malformed.

**Deprioritized**
- **OP-2 — Anti-collusion at Level 2.** Level 2 is treated as an emergent market of trust networks; revisit once the system is defined.

**Dissolved in v0.3**
- ~~**OP-11 — Training-cost amortization.**~~ There is no longer a downstream cost to amortize (§6.2).
- ~~**OP-5 — Education.**~~ Largely answered by §6.2 and §6.4.

### 10.1 Deliberately left to trust networks

Which activities are *always* creditable — childcare, schooling (and whose schooling), subsistence farming, untrained medical assistance — is **not** settled by this document, and should not be. It is exactly the kind of question A8 assigns to local variance competing in the open.

**But name the risk:** the set of always-credited activities is a capture surface. A network that can declare an activity creditable can issue credit. The defence is structural rather than procedural — competing networks, plus ratio-based evaluation (§3.5): a network that credits worthless activity produces members with poor efficiency ratios, and other networks stop trading with it. **This is OP-10 wearing different clothes and should be worked with it.**

---

## 11. First Foothold — the MVP

**Full-cost accounting as a parallel overlay on existing commerce.** No adoption, no permission, no legal change — it computes and publishes truth alongside money.

> **⚠️ Read that sentence cold and it describes every complementary currency that ever died.** Ithaca HOURS was *defined* as $10; Burlington Bread mirrored dollars in slices. None was an independent unit of account — they were national currency with a local-loyalty restriction, they added nothing money did not already do, and they died quietly.
>
> **The distinction is the whole point of the MVP: Aequitas's overlay computes a number money cannot produce.** A true debit-cost is not a price with a different label; it is information that does not exist anywhere in the current system. If the MVP ever stops being able to say that, it has become a loyalty scheme.

**(a) Product & service debit-costing.** Compute and publish the true debit-cost of real products. *Gated on OP-17.*

**(b) Account intake with progressive resolution.** A person opens an account and answers questions; their estimated position resolves from **global average → granular cohort → individual record**.

> A **"try it" account** — answer questions about yourself and watch your assigned position sharpen from the global average toward something specific to your location, age, work, and holdings. It demonstrates the estimation engine, the onboarding incentive, and the honesty of the accounting at once.

**If a first *real* deployment is ever wanted rather than an overlay**, the field record is unambiguous about the shape: WIR (1934–present, ~60,000 businesses) and Sardex (4,000+ businesses) survived by starting **B2B inside dense input loops**, where no participant is a one-way sink. Both are countercyclical — adoption rises when conventional money is scarce. **A downturn is the moment.**

---

## 12. Amendment record

### v0.3 (2026-08-01)

**1. A2 amended — training is front-loaded, not charged downstream.** *(substantive)*

> **Old (v0.1–v0.2):** *"Skilled labor → the training (time + materials of schooling) is a real cost that flows downstream into the debit of the service recipient."*
> **New:** training is credited work in its own right, and its cost is discharged during the training years by those who pledged for it. Nothing flows downstream.

Reasons, in descending force:

- **The old rule answered a pricing question and left the incentive question open.** It made the doctor's service expensive; it never made becoming a doctor rational. In a system that deliberately removes material gain as a motive, that gap is fatal — and it is precisely the gap that 45 years of time banking evidence says causes chronic skill shortage.
- **The benefit of education is diffuse, so its cost should be.** Assigning it to one patient decades later is arbitrary. That arbitrariness *was* OP-11: every candidate amortization window (expected career, actual career, statutory) had a defect, because the question was malformed.
- **Pledging supplies the limiting mechanism the old rule lacked.** Society decides how many doctors to train by backing it. Unpledged study still credits the student's time (A7 requires it) but leaves them the debit — so there is no perpetual-studenthood exploit.

*Not changed:* labour is still never rate-scaled; hard and hazardous labour still resolve materially.
*Dissolves:* **OP-11**, and most of OP-5. *Improves:* the skill half of **OP-16**.

**2. §6 restructured — one credit, three feedback channels.**
Production / service / enrichment are not credit types. An apprentice plumber's hour is all three at once and cannot be partitioned, so no accounting rule may use the categories as a boundary. Non-convertibility now holds *because feedback was never credit*, requiring no firewall. **OP-8 reframed** to the live question: can feedback be bought?

**3. §0 and A1 reframed — a theory of cost, not of value.**
"Nothing else is value" invited the one-sentence refutation that ended emergy, Technocracy, and the labour theory of value: supply-side only, ignores demand. The actual theory is narrower and stronger. Sensorica, the most developed real-world contribution-accounting project, renamed its "value accounting system" to a *contribution* accounting system on the same reasoning.

**4. A1 grounded in Ellerman's responsibility imputation** rather than left as a bare assertion. Makes A3 a consequence rather than a design choice, and supplies a second independent route to §7.1.

**5. §6.4 added — pledges and signals.** Pledges commit debit at 1:1; signals commit nothing and should be plentiful. Supplies the decentralized demand signal the system lacked, a purpose for surplus, and the funding mechanism for education and speculative work.

**6. §3.5 added — the books never balance.** Aggregate debit exceeds credit permanently; that is the second law, not a defect. A3 is why it does not collapse the economy. Sums are replaced by two numbers: ratio for efficiency, absolute credit for contribution.

**7. §1.1 added — named conventions.** Three quantities the system needs are not physical facts. Declaring them preserves universality; disguising them as measurements would not.

**8. §3.4 split** — resolution improves with instrumentation; allocation does not. **9. §7.6 added** — the alternative-economy graveyard, and which failures do not apply. **10. §11 hardened** against being read as one more complementary currency. **11. §2** gains the fourth screening question.

### v0.3 — same-day refinements

*Amended in place rather than bumped to v0.4: v0.3 was hours old and unreleased, so a version split would archive a document nobody had read. Noted here so the change is a decision and not a slip.*

**12. §6.2a added — the front-loading principle, generalized.** Training was the first instance of a rule that also covers media production and research: a large up-front cost with diffuse benefit is discharged when incurred, by pledgers, and never amortized downstream. **This closes OP-21 and confirms the shape of the OP-11 dissolution.** The general insight is that downstream amortization always requires an arbitrary window — so front-loading **removes the division** rather than solving it, which is what distinguishes it from the three unsolved conventions in §1.1.

**13. OP-20 closed (§6.6).** The lone fraudster was already handled by machinery in place: **IC-7** caps claimed hours at wall-clock time; **conservative weighting** (C1 §12) prices unattested, near-zero-material claims at the pessimistic end of their interval, which for credit is ~zero; and **pledges** are the only route from *asserted* to *backed*. Nobody pledges to a fake artist. The residual risk is flooding the free signal channel, which is **OP-6's** problem, not a credit-issuance problem.

**14. OP-22 narrowed sharply (§5.3, §6.5).** The provenance-vs-privacy conflict was overstated. The correct bar for attribution is **no worse than today** — a gallery buyer already has no proof the artist painted the work, and provenance only becomes fraught in the capitalized art market that A5 removes. On privacy, the current world already runs on counterparty-visible, third-party-opaque transfers, and Aequitas does not replace courts, small claims, or social pressure. What survives is narrow and technical: **the minimum disclosure set an auditor needs**, since unlike banking there is no institution to externalize validation to. A C7 question.

**15. §6.5a added — not all work is capturable, and the system does not require it to be.** Memes are the clean case: real time is spent, propagation is untraceable, and attempting to credit it would be futile and grotesque. A1 describes how flows are accounted *when recorded*; it does not demand that all activity be recorded. Worth stating explicitly, because critics will read A1 as totalizing surveillance.

### v0.2 (2026-07-31) — A7 amended

Symmetric estimation of credit and debit for every human, with realization gated on a verified account and observed supersession; credit issuable retroactively. Decisive reason: the original A7 was inconsistent with C1's origin closure — a non-participant's wheat had no creditable grower, so the books described material appearing from nowhere, contradicting A1. Full argument retained in `99-archive/Aequitas_Foundations_v0.2.md` §12.

---

*End of v0.3.*
