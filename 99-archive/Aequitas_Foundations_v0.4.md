# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.4
> **Date:** 2026-08-01
> **Status:** Working foundations.
> **Supersedes:** `99-archive/Aequitas_Foundations_v0.3.md`. **OP-17 resolved; §1.1 loses a row; §3.4 narrowed; §3.3a added.** See §12.
> **Also supersedes:** OFCS (Open Fair Credit Standard) — see §8 for what is deliberately *not* inherited.
> **Primary audience of the first paper:** technologists / implementers.
> **Companion:** `00-strategy/Aequitas_Objections_v0.5.md` — the objections register. Read alongside §10.

---

## 0. The One-Sentence Theory

> **Aequitas is a universal accounting of material flows.** Every credit and every debit is a record of matter and energy moving through the world, attributable to the people who caused the movement. **Cost is nothing other than this.**

**Aequitas is a theory of cost. It is not a theory of value, and it does not need to be.**

This distinction is load-bearing. Every previous attempt at objective accounting — Odum's emergy, Technocracy's energy certificates, the labour theory of value — claimed to have found what things are *worth*, and every one was refuted on the same ground: **supply-side only, ignores demand.** The refutation is a stock move and takes one sentence.

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

> **A2 is also the reason the co-product allocation problem has an answer (§3.4a).** Because every physical quantity in the ledger — a kilogram, a joule, a tonne of CO₂ — is a proxy for hours to produce or to mitigate, **the system never has to choose between mass and energy as *the* unit of account.** The universal is the denominator, not the carrier. This is a stronger consequence of A2 than was recognised when it was written.

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

### 1.1 Named conventions *(one row removed in v0.4)*

Some quantities the system needs are **not** physical facts. Where that is true, it is stated here rather than hidden in an implementation detail. **A convention that is declared is not an ad-hoc rule; a convention that is disguised as a measurement is.**

| Quantity | Status | Why it is not a measurement |
|---|---|---|
| **Split of a team's credit across its members** | ⚠️ **Convention — currently hours-worked** | Responsibility for joint work is joint and non-decomposable (Ellerman). Hours-worked is defensible and simple, but it is a choice. **OP-18 — now the blocking division.** |
| **Attribution of shared overhead to co-products** | ⚠️ **Convention — currently inherited proportions** | The barn shelters the whole animal; no physical trace runs from it to the hide. Interim rule: overhead flows in the proportions the traceable inputs established. **OP-23 — new in v0.4.** |

> **✅ Removed in v0.4 — the co-product split.** The row reading *"Split of a joint process's debit across its co-products — convention, not yet chosen"* is **deleted, not filled in.** It was never a convention. See §3.4a: the process itself performed the split, and it is measurable. `00-strategy/OP-17_coproduct_allocation.md`.

**The test that separates the two columns, and it is the useful output of the OP-17 work:**

> **Did the thing being divided leave a physical trace?**
> **Where it did — measure.** Feed energy, cracking enthalpy, and a turbine's heat/power trade-off are facts about a process.
> **Where it did not — declare a convention and say so.** Labour hours and shared overhead leave no trace to an individual output, and no instrument will ever find one.

**The project's hard problem is division, not measurement** — but v0.4 narrows that: it is division **of the untraceable**. See the objections register §0.

---

## 2. Conformance to the Three Criteria

| Criterion | How Aequitas satisfies it |
|---|---|
| **Universality** | One mechanism only — material flow accounting. No exceptions for professions, nations, or classes. Units (mass, energy, seconds) are measurable identically anywhere in the universe. Coverage extends to non-participants by statistical estimation **on both sides of the ledger** (A7). Where a genuine convention is required, §1.1 names it rather than concealing it. |
| **Decentralization** | No issuer, no central bank, no authoritative institution. Anyone may verify any claim from the event log. The verification ladder (§4) begins with peer attestation, which requires no infrastructure and therefore no permission. Governance is core-immutable with competing local variance. **Cost constants are disciplined by rival-sector audit (§3.3a), which needs no reviewing body.** |
| **Fecundity** | The verification ladder *pulls* technological development (§4). Retroactive re-weighting (§3.3) creates permanent demand for better science. Regulators invert into services businesses want (§7.3). Onboarding is individually rational (§5.2). Pledges give surplus a purpose (§6.4). **Every co-product allocation is an open scientific question that better instruments improve (§3.4a).** |

**Fourth screening question — "does this need a Paul Glover?"**
Ithaca HOURS died when its founder relocated; he himself said every local currency needs a full-time networker to promote, facilitate, and troubleshoot. A mechanism that depends on an enthusiast is a mechanism with an expiry date. **Every proposed mechanism must pay its own maintainer from inside the system** — as auditing-as-credited-work does, and as rival-sector audit does (§3.3a). Apply alongside universality, decentralization, and *who games this?*

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

### 3.2a Debit is a vector, collapsed on demand *(new in v0.4)*

A debit is **not one number.** It is a bundle of physical quantities — kilograms of a substance, joules, labour-hours, cubic metres of water, land-area-years — stored separately in the log and combined into a single comparable figure only when someone needs to compare two things, via the current weighting model.

This is A3 and A6 working together: the physical record is what implementations must agree on; the collapse is what they may differ about (EventLog §3).

> **🔴 One rule follows immediately, and it is load-bearing. Any division of a debit — across co-products, across a team, across anything — is computed on the vector, per dimension, *before* collapsing.**
>
> Divide the collapsed number instead, and whoever maintains the weighting model silently controls every allocation in history. Divide per dimension, and the split is **weighting-independent**: two communities running different models compute the same split and disagree only about what it weighs. This closes a side entrance to OP-10 that would otherwise have been invisible.

### 3.3 Retroactive re-weighting

When science improves, **every affected ledger in history recalculates.** Cheaper CO₂ mitigation makes everyone's past fossil use weigh less; a newly discovered occupational harm retroactively adds debit to the products made by the process that caused it.

This is the engine of fecundity: **the system permanently rewards better measurement of reality.**

**Re-weighting applies to allocation splits, not only to mitigation weights** *(new in v0.4)*. New process science re-splits historical joint production the same way new mitigation science re-weighs historical emissions. A conservative early estimate is not a permanent verdict on anyone — **no inaccuracy in this system is irreversible**, which is the general answer to "what if the early numbers are wrong."

*Tractability is not speculative.* [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) demonstrated that in-kind calculation at national scale is computationally feasible with sparse-matrix methods. Mises's objection was in-principle; the empirical scale objection has been answered by people who ran the arithmetic.

### 3.3a Who checks the science — rival-sector audit *(new in v0.4)*

Retroactive re-weighting makes cost constants enormously powerful: whoever publishes the energetics of a process sets every split in that sector, backwards through all of history. That is a capture surface, and it needs an answer that is not a standards body.

**What Aequitas removes for free.** There is no market-dominating corporation to fund a favourable result, because A5 removes the profit that pays for captured science today. Labs are credited by trust networks for doing the work. **The classic funding-bias channel is structurally closed, and that should be claimed.**

**What it does not remove.** Trust networks are dominated by the *consuming* side of any given good — everyone eats beef, few raise cattle — so their members collectively benefit from that good's debit being **understated**. And the incentive to correct is one-sided:

| Error direction | Who wants it fixed | Result |
|---|---|---|
| Constant **overstates** debit | Every subscriber | Corrected |
| Constant **understates** debit | Nobody; correcting it worsens every subscriber's ledger | **Nobody funds the replication** |

Left alone this produces **systemic drift toward under-costing** — the failure mode of every carbon-accounting regime attempted so far. §3.5 tolerates it arithmetically, but it erodes **A4**, and A4 is not optional. Registered as **OP-24**.

> **The rule: the natural auditor of a cost constant is the rival sector, not the consumer.**
>
> If beef's energetics are understated, plant-protein producers are materially harmed and will fund the replication. Consumers police neither direction; rivals police both. This is an incentive, not an enforcement mechanism, and it is already implied by A5 — which removes profit *in exchange* while explicitly preserving **competition on efficiency** (§7.1). Rival-sector audit is that competition applied to the cost model itself.

Three supporting rules:

1. **Two unaffiliated replications before a constant may re-weight history.** Retroactivity is too powerful to trigger from a single source.
2. **Audit triage weights magnitude × concentration of beneficiary.** Materiality thresholds alone help an attacker, whose job then becomes making the falsification look immaterial.
3. **A trust network concentrated in the sector it audits is captured by construction.** Membership composition is public, so this is a **detectable screening property** rather than a rule anyone enforces. General-membership networks are structurally sounder than sector-specific ones. *(The co-op form does not fix this on its own: the conflict is directional, not monetary — Arthur Andersen was paid by Enron, and a client-owned Andersen would have been worse.)*

### 3.4 Resolution is opportunistic

**Resolution.** Record what is known; estimate the rest from averages; refine forever. If someone commutes daily, estimate from cohort averages; learn which car they drive and it sharpens. All of it revisable.

**⚠️ Amended in v0.4.** v0.3 stated flatly that *allocation is not a resolution problem because the indeterminacy is not epistemic.* **That is too strong and is now narrowed.** Allocation of physical inputs *is* a resolution problem — the process performed the split and better instruments converge on it (§3.4a). What is genuinely not epistemically resolvable is the division of quantities the process **never physically divided**: labour hours across co-products, shared overhead, and joint responsibility across a team.

> **The distinguishing test is whether the divided thing left a physical trace.** Where it did, measure. Where it did not, declare a convention (§1.1) and say so.

### 3.4a Joint production — the process allocates itself *(new in v0.4)*

One process, several outputs, one pool of debit. A steer yields beef, hide, tallow, bone, manure, and enteric methane; a refinery yields a full fraction slate; a CHP plant yields heat and power. **How the debit divides is a fact about the process, not a property of the outputs** — which is why a century of searching for the right *carrier quantity* (mass? energy? exergy? price?) found only rules that work in one industry and are category errors in the next.

> **A joint process's debit divides according to where the process itself physically sent its inputs.**
>
> The instrument is whatever that process makes traceable — tissue-deposition energetics for an animal, cracking enthalpy for a refinery, the extraction curve for a turbine, mitigation cost for an emission. These are not rival conventions; they are **different instruments reading the same underlying quantity, which is hours (A2).** Mass is an estimator, correct where composition is uniform and a low-resolution reading where it is not.

Four consequences worth stating:

- **Human preference plays no part.** A hide's share does not change because leather is fashionable, exactly as manure's share does not change because nobody wants it. A split contingent on demand would give two identical steers in two towns different splits — a universality failure, and price allocation in costume.
- **Waste outputs are co-products like any other.** Counting manure and methane in the split removes the residual, and with it the whole question of who absorbs an unwanted output.
- **An output's cost share is set by the process; its ledger character is set by its fate.** Manure is pollution debit in a lagoon, a co-product in a biodigester, and an observed fertiliser offset when spread. Fate closure (EventLog IC-4) already records this; no new machinery is required.
- **Negative values do not arise.** Nothing is inverted, so Steedman's result does not transfer: each share is a forward measurement of what physically went in, and a deposition cannot be negative. ⚠️ *This is asserted, not yet proven for a recursive economy where every input is itself a joint split — see the objections register.*

**What this does not cover, and does not pretend to:** **labour** (no trace from the farmer's hours to the hide — that is **OP-18**) and **shared overhead** (**OP-23**). Both are in §1.1 as declared conventions.

### 3.5 The books never balance — and must not

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

**Instrument selection is a ladder question, not a separate discipline** *(added v0.4)*. Under §3.4a, allocating a joint process means choosing and reading the instrument its physics makes available. A Level 1 producer splits a carcass by mass and records low confidence; a Level 3 producer reads calorimetry. **Same rule, same record shape, different rung** — which is exactly what the ladder exists to accommodate.

---

## 5. Identity, Privacy, and Onboarding

### 5.1 Coverage without coercion

- **One verified human = one account.** Hard Sybil resistance is required for integrity.
- **Participation is voluntary. Coverage is not.** Non-participants are estimated on **both sides**:

| | Estimated from |
|---|---|
| **Debit** | Demographic cohort average, computed *excluding* registered participants. Public figures estimated from publicly known wealth and holdings. |
| **Credit** | Cohort production model — occupation, region, known activity, computed *excluding* measured producers (§5.1b). |

- **Non-participants can neither draw on nor be charged for their estimated position.**

### 5.1a Realization

1. **Verified account** (C6).
2. **Observed supersession** — the estimate is replaced by attested records, under monotonicity (records may only improve toward stronger basis and finer resolution; an observation may never be superseded by an estimate).

**Assertion is not evidence.**

### 5.1b The residual rule — averages cover only the unmeasured *(new in v0.4)*

An unmeasured producer's estimated output is the **independently-known total minus what measured producers actually produced, divided among the producers who remain dark**:

> **estimate = (N − Y) / Z** — *N* the independently-known total (FAO figures, trade data, satellite survey), *Y* the measured producers' recorded output, *Z* the count of unmeasured producers.

**Computed over the whole population instead, this creates adverse selection.** Better-than-average producers instrument to prove it; worse-than-average stay dark and free-ride on an average their own absence inflates. Over the residual, the estimate *worsens* as good producers exit — **so darkness stops paying.** This is the same discipline already applied to the cohort debit average above, extended to production.

**Two conditions.** It requires an independently known *N*, which exists for major commodities and not for everything; and a defensible count *Z*, since under-counting dark producers over-states each one's share.

**"Dark" means outside Aequitas, not low-tech within it.** Participation carries a transparency requirement — a good moving through the Aequitas economy carries records of its origin. Seeking data on non-participants, and assisting producers to bring their supply chain into the record, are both **credited trust-network work**.

### 5.2 Onboarding as resolution — and as the adoption incentive

Joining replaces an assigned average with your real record. Two forces make it rational: most people's true footprint is *below* their cohort average, and **their estimated credit is unrealized until they join.**

The pitch is: *here is what you have contributed, and here is what it cost; join and make it yours.*

**The cost of joining is administrative labour, not a penalty** *(clarified v0.4)*. A producer without instruments genuinely needs more human hours to produce the same verified record, and those hours are a real material cost under A1 — not a thumb on the scale. The incentive to instrument is the ordinary incentive to reduce a real cost.

> **⚠️ Watch item: fixed onboarding costs consolidate industries.** Documentation burdens are repeatedly argued to disadvantage small producers — which is why [organic certification cost-share programmes](https://www.ams.usda.gov/services/grants/occsp) exist at all, and the same argument is made of [REACH](https://echa.europa.eu/regulations/reach/understanding-reach) and [FSMA](https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma). The structural offset is that **onboarding assistance is credited work borne by the trust network rather than the entrant.** Whether that is sufficient is empirical and should be watched, not assumed.

### 5.3 Privacy

Account holders keep a **private ledger with provable claims** — zero-knowledge proofs of balances and cost positions when transacting, not history.

**This is roughly where society already sits, and that is the point.** People transfer money to each other today knowing their counterparty and nothing about third parties' accounts. Nobody audits those accounts, because validation trust is externalized to banks. **Aequitas does not need more visibility than that; it needs the same visibility with the trust relocated.**

**Aequitas also does not replace existing recourse.** Courts, small claims, contract law, and ordinary social pressure continue to exist and continue to handle fraud between people. The system's contribution is upstream of enforcement: by removing wealth concentration and material insecurity, it **removes most of the motive** for the scams those mechanisms exist to punish.

> **⚠️ The narrow question that remains — OP-22.** The bank analogy has one gap: there is no bank to externalize validation to. Verification is the trust-network ecosystem (Level 2), and an auditor must be able to see *something*. So the live question is not "surveillance or privacy" but **"what is the minimum an auditor must see to verify a claim without seeing a history?"** Zero-knowledge proofs are the right shape of answer and are already specified above; what is missing is the precise disclosure set. **This is a C7 implementation problem, not a foundational contradiction.**

---

## 6. One Credit, Three Feedback Channels

**There is one credit: time worked, recorded as material flow.** Production, service, and enrichment are **not** different credit types and do not credit at different rates. Everyone earns at the same rate and therefore influences at the same rate.

**The categories have no accounting boundary and no rule may use them as one.** An apprentice plumber's single hour is simultaneously enrichment (learning the trade), service (fixing a customer's pipes), and production (copper and fittings → working plumbing). That hour is not partitionable, and any attempt to partition it would require yet another allocation convention (§1.1).

What the three names *do* describe is **how feedback reaches the work** — how a society tells someone that what they did mattered.

### 6.1 Why "enrichment" is named at all

**To give grounds for crediting work that no economy has ever credited.**

Going to school is work. Today we make students or their parents pay for it — the relationship is inverted. Teaching your own child is work. Caring for a relative is work. None of it is paid, and in a system that does not incentivize with material gain — *"go to school if you want to make money"* — something must make socially beneficial activity individually rational.

Enrichment is the name for work whose benefit flows **from all of humanity to at least one person, in ways not readily measured in material.** It is credited because it is real work, not because it is virtuous.

**Childcare is creditable work regardless of who performs it.** This alone brings the largest uncounted labour pool in human history onto the books.

### 6.2 Training, front-loaded

**A student is credited for their time while training.** The debit of training — teachers' time, facilities, materials — is **discharged during the training years** by whoever pledged for it (§6.4).

**Nothing flows downstream.** A doctor's care costs the recipient exactly: the doctor's time, the material cost of running the clinic, and the medicines and correctives dispensed. **The doctor's education is not in that bill.** It was already paid for, by the people who wanted doctors to exist.

Why this is right and the v0.2 rule was wrong:

- **It makes training individually rational without any rate premium.** The old rule made the *service* expensive without ever rewarding the *trainee*; it answered a pricing question and left the incentive question open. Being trained is now paid work.
- **It matches who benefits.** Education's benefit is diffuse, so its cost should be borne diffusely. Charging it to one patient decades later is arbitrary — precisely the amortization problem that made OP-11 unanswerable.
- **It dissolves OP-11 rather than solving it.** There is no longer a cost to amortize over an uncertain career.
- **Pledging supplies the natural limit.** Society decides how many doctors to train by pledging for it. Unpledged study still credits the student's time — A7 requires that, it is real activity — but leaves them holding the debit. **No perpetual-studenthood exploit.**

### 6.2a The front-loading principle

Training is the first instance of a general rule, and the rule is worth stating once rather than rediscovering per case:

> **A large up-front cost with diffuse benefit is discharged at the time it is incurred, by those who pledged for it. It is never amortized downstream onto whoever happens to consume the result.**

Three instances so far:

| Case | Front-loaded cost | What the eventual recipient pays |
|---|---|---|
| **Education** | Teachers' time, facilities, materials | The professional's time, clinic materials, medicines — **not the education** |
| **Media production** | Years of crew time, sets, equipment, post | **Delivery only** — theatre maintenance, projectionist hours, print or bandwidth, power |
| **Research, infrastructure, tooling** | The build | Use, wear, and energy |

**Why downstream amortization is always the wrong answer.** It requires choosing a window (how many patients? how many viewers?) and every candidate window is arbitrary. That arbitrariness *was* OP-11, and it is also what made OP-21 look hard. **The question was malformed in both cases.** Front-loading removes the division rather than solving it.

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

### 6.4 Pledges and signals

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

**What survives, and is load-bearing: competition on efficiency.** A5 removes margin, not rivalry. §3.3a leans on this directly — rival sectors auditing each other's cost constants is the only thing standing between the weighting model and systemic under-costing.

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

> **This section also bounds the cost of being wrong** *(noted in v0.4)*. Debit binds hard, and §3.3 corrects errors only eventually — so a producer over-assigned for years would suffer real harm before the correction arrived, the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal). The floor caps that exposure: the worst case is *restricted discretionary consumption for a period, then corrected*, not destitution. **The floor is not only a welfare provision; it is the error-tolerance of the whole accounting.**

### 7.6 Why the alternative-economy graveyard does not apply

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
2. **Academic paper** — engages Marx / Hayek / Ostrom; must answer the socialist-calculation critique head-on. Lead with: theory of *cost* not value; Ellerman on attribution; Cockshott & Cottrell on tractability; pledges as a decentralized answer to preference revelation. **Add: joint production solved by process physics rather than by convention (§3.4a) — this is the reply to Sraffa/Steedman and to ISO 14044 simultaneously.**
3. **Civic reformer brief** — municipalities, co-ops, transition communities.
4. **Public-facing text.**

---

## 10. Open Problems

Ranked by how load-bearing they are. Full detail in `00-strategy/Aequitas_Objections_v0.5.md`.

**Blocking**
- **OP-18 — Responsibility is not divisible.** ⬆ **Promoted to the critical path in v0.4.** Hours-worked is a convention (§1.1), not a measurement — and since §3.4a cannot split *labour* across co-products, **C3 is blocked here rather than on OP-17.** C3 needs per-product labour hours.
- **OP-10 — Weighting-model governance.** Whoever sets the cost model controls every balance in history without touching a core rule. Largest hole in A8. §3.2a closes one side entrance (split before collapse) and §3.3a supplies a mechanism for cost constants; the general problem stands.

**High**
- **OP-24 — Understatement drift.** *(new in v0.4)* Errors that overstate debit get corrected; errors that understate it have no funder. Proposed fix — rival-sector audit (§3.3a) — is unproven and wants a simulation. **Attacks A4.**
- **OP-23 — Shared-overhead attribution.** *(new in v0.4)* The barn does not trace to the hide. Interim rule inherits the traceable proportions, which is thin, and **thinnest exactly where material inputs are small — capital-intensive manufacturing.**
- **OP-16 — The onerousness gap.** A2 resolves exertion, hazard, and skill. **Tedium and indignity have no material signature and nothing allocates labour to them.** Leading candidate: *hour-ceiling differentiation* — pay the premium in hours, not rate, justified by measured physiological sustainability limits. First check how much of OP-16 is simply unmeasured hazard.
- **OP-1 — Service → influence.** Strongest candidate: **pledging power accrues per hour worked, equally for all.** Not a voting scheme.
- **OP-6 — Feedback mechanics.** How signals aggregate without becoming a popularity plutocracy. With accumulation forbidden, feedback and pledging are the entire motivation system for anyone past their own consumption ceiling.

**Medium**
- **OP-3 — The estimation engine.** Requires a cohort *production* model as well as consumption, on the residual rule (§5.1b).
- **OP-8 — Can feedback be bought?** *(reframed)*
- **OP-9 — Preference revelation.** Largely answered by §6.4 pledges, plus scarcity-as-debit on the Kantorovich framing.
- **OP-22 — Minimum audit disclosure.** *(narrowed)* A C7 disclosure-set question — see §5.3.
- **OP-4 — Debit tolerance formula.** ⬆ *Slightly more load-bearing after v0.4: §7.5 is now the error-tolerance of the accounting, not only a welfare floor.*
- **OP-14 — Cohort shopping.** · **OP-15 — Ghost harvesting.**
- **OP-7 — Cross-level trade.**

**Closed**
- ✅ ~~**OP-17 — Joint production allocation.**~~ **Closed in v0.4 for the material/energy half** (§3.4a): the process performed the split and it is measurable. The labour half moved to OP-18 and the overhead half to OP-23. **A row was deleted from §1.1 rather than filled in.**
- ~~**OP-20 — Unobservable work.**~~ Closed by three existing mechanisms (§6.6).
- ~~**OP-21 — Media reproduction.**~~ Closed by front-loading (§6.2a).
- ~~**OP-19 — Saturated producer.**~~ Resolved by pledges.

**Deprioritized**
- **OP-2 — Anti-collusion at Level 2.** Level 2 is an emergent market of trust networks; revisit once the system is defined.

**Dissolved**
- ~~**OP-11 — Training-cost amortization.**~~ · ~~**OP-5 — Education.**~~ · ~~**OP-8 — Enrichment firewall**~~ *(reframed, see above)*.

### 10.1 Deliberately left to trust networks

Which activities are *always* creditable — childcare, schooling (and whose schooling), subsistence farming, untrained medical assistance — is **not** settled by this document, and should not be. It is exactly the kind of question A8 assigns to local variance competing in the open.

**But name the risk:** the set of always-credited activities is a capture surface. A network that can declare an activity creditable can issue credit. The defence is structural rather than procedural — competing networks, plus ratio-based evaluation (§3.5): a network that credits worthless activity produces members with poor efficiency ratios, and other networks stop trading with it. **This is OP-10 wearing different clothes and should be worked with it.**

**Added in v0.4 — a second structural defence, from §3.3a.** A trust network's membership composition is public, and **a network concentrated in the sector it audits is captured by construction.** That makes capture *detectable from the log* rather than something anyone must police. It is a screening property, and it applies to always-creditable activity lists as much as to cost constants.

---

## 11. First Foothold — the MVP

**Full-cost accounting as a parallel overlay on existing commerce.** No adoption, no permission, no legal change — it computes and publishes truth alongside money.

> **⚠️ Read that sentence cold and it describes every complementary currency that ever died.** Ithaca HOURS was *defined* as $10; Burlington Bread mirrored dollars in slices. None was an independent unit of account — they were national currency with a local-loyalty restriction, they added nothing money did not already do, and they died quietly.
>
> **The distinction is the whole point of the MVP: Aequitas's overlay computes a number money cannot produce.** A true debit-cost is not a price with a different label; it is information that does not exist anywhere in the current system. If the MVP ever stops being able to say that, it has become a loyalty scheme.

**(a) Product & service debit-costing.** Compute and publish the true debit-cost of real products. *Materials and energy are unblocked as of v0.4 (§3.4a); the labour layer is gated on OP-18.* **A first publishable target: re-derive a refinery's fraction slate under process-physics allocation and compare it against USEEIO's price allocation.** A materially different answer is the strongest technical result available early.

**(b) Account intake with progressive resolution.** A person opens an account and answers questions; their estimated position resolves from **global average → granular cohort → individual record**.

> A **"try it" account** — answer questions about yourself and watch your assigned position sharpen from the global average toward something specific to your location, age, work, and holdings. It demonstrates the estimation engine, the onboarding incentive, and the honesty of the accounting at once.

**If a first *real* deployment is ever wanted rather than an overlay**, the field record is unambiguous about the shape: WIR (1934–present, ~60,000 businesses) and Sardex (4,000+ businesses) survived by starting **B2B inside dense input loops**, where no participant is a one-way sink. Both are countercyclical — adoption rises when conventional money is scarce. **A downturn is the moment.**

---

## 12. Amendment record

### v0.4 (2026-08-01) — OP-17 resolved

**1. §3.4a added — joint production allocates itself.** *(substantive)*

> **A joint process's debit divides according to where the process itself physically sent its inputs.** The instrument varies with the process; the justification does not.

The literature searched for a **carrier quantity** — a property of the outputs by which cost could be split — and found only rules that work in one industry and fail in the next. **The allocation is a fact about the process, not a property of the outputs.** Aequitas can say this because A2 gives it a universal *denominator* (hours), so it never has to choose between mass and energy as *the* unit; both reduce to the same thing. Tested against a slaughterhouse, an oil refinery, and a CHP plant with one justification and three instruments.

*Removes:* the co-product row from §1.1 — **deleted, not filled in.** *Spawns:* OP-23, OP-24. *Moves:* the labour half to OP-18.

**2. §1.1 gains a test, and it is the transferable result.** *Did the thing being divided leave a physical trace?* Trace → measure. No trace → declare a convention. This is what separates OP-17 (solved) from OP-18 and OP-23 (genuine conventions), and it should be applied to every future division question.

**3. §3.4 narrowed.** v0.3 claimed allocation is never a resolution problem because the indeterminacy is not epistemic. **Too strong.** Allocation of *physical inputs* is epistemic and does converge. Only division of what was never physically divided is not.

**4. §3.2a added — debit is a vector, and divisions happen per dimension before collapsing.** Divide the collapsed number and the weighting-model maintainer silently controls every allocation in history. Per-dimension division is **weighting-independent**. This closes a side entrance to OP-10 that was invisible until the split rule was written.

**5. §3.3a added — rival-sector audit.** Retroactive re-weighting makes cost constants powerful enough to be worth capturing. A5 closes the classic funding-bias channel (no corporation to pay for a favourable result), but trust networks are consumer-dominated and therefore biased toward **understating** the debit of what their members consume — and nobody funds the correction of an error in their own favour. **The natural auditor of a cost constant is the rival sector.** Plus: two unaffiliated replications before re-weighting history; triage by magnitude × beneficiary concentration; and networks concentrated in the sector they audit are captured by construction.

**6. §5.1b added — the residual rule.** Estimates for unmeasured producers are computed as **(N − Y) / Z** over the *unmeasured residual only*. Over the whole population it creates adverse selection: good producers instrument, bad ones stay dark and free-ride on an average their absence inflates. Extends the discipline §5.1 already applied to cohort debit.

**7. §5.2 clarified, §7.5 strengthened.** The cost of joining without instruments is **administrative labour** — a real material cost under A1, not a penalty. And §7.5 is now recognised as **the error-tolerance of the whole accounting**: since debit binds hard and corrections arrive late, the floor is what keeps a mis-estimate from becoming destitution. Watch item added: fixed onboarding costs consolidate industries.

**8. §4, §7.1, §9, §10, §11 updated for consistency** — instrument selection is a ladder question; competition-on-efficiency is load-bearing for §3.3a; the academic paper gains a Sraffa/ISO reply; the MVP's product-costing is unblocked for materials and energy and gated on OP-18 for labour.

### v0.3 (2026-08-01)

**1. A2 amended — training is front-loaded, not charged downstream.** *(substantive)*

> **Old (v0.1–v0.2):** *"Skilled labor → the training (time + materials of schooling) is a real cost that flows downstream into the debit of the service recipient."*
> **New:** training is credited work in its own right, and its cost is discharged during the training years by those who pledged for it. Nothing flows downstream.

Reasons, in descending force:

- **The old rule answered a pricing question and left the incentive question open.** It made the doctor's service expensive; it never made becoming a doctor rational. In a system that deliberately removes material gain as a motive, that gap is fatal — and it is precisely the gap that 45 years of time banking evidence says causes chronic skill shortage.
- **The benefit of education is diffuse, so its cost should be.** Assigning it to one patient decades later is arbitrary. That arbitrariness *was* OP-11: every candidate amortization window had a defect, because the question was malformed.
- **Pledging supplies the limiting mechanism the old rule lacked.**

*Not changed:* labour is still never rate-scaled; hard and hazardous labour still resolve materially.
*Dissolves:* **OP-11**, and most of OP-5. *Improves:* the skill half of **OP-16**.

**2. §6 restructured — one credit, three feedback channels.** Production / service / enrichment are not credit types. Non-convertibility holds *because feedback was never credit*, requiring no firewall. **OP-8 reframed.**

**3. §0 and A1 reframed — a theory of cost, not of value.** **4. A1 grounded in Ellerman's responsibility imputation.** **5. §6.4 added — pledges and signals.** **6. §3.5 added — the books never balance.** **7. §1.1 added — named conventions.** **8. §3.4 split.** **9. §7.6 added.** **10. §11 hardened.** **11. §2** gains the fourth screening question.

**12. §6.2a added — the front-loading principle, generalized.** Closes OP-21 and confirms the shape of the OP-11 dissolution. **13. OP-20 closed (§6.6).** **14. OP-22 narrowed sharply.** **15. §6.5a added — not all work is capturable.**

### v0.2 (2026-07-31) — A7 amended

Symmetric estimation of credit and debit for every human, with realization gated on a verified account and observed supersession; credit issuable retroactively. Decisive reason: the original A7 was inconsistent with C1's origin closure — a non-participant's wheat had no creditable grower, so the books described material appearing from nowhere, contradicting A1. Full argument retained in `99-archive/Aequitas_Foundations_v0.2.md` §12.

---

*End of v0.4.*
