# Aequitas — Foundations & Long-Term Strategy

> **Version:** 0.7
> **Date:** 2026-08-06
> **Status:** Working foundations.
> **Supersedes:** `99-archive/Aequitas_Foundations_v0.6.md`. **Credit-realization & the supply-chain hand-off model (the C11-interview session).** Six folds: **(1) credit realizes on *verification of the output*, not on the work alone** — for a good, each hand-off *is* the verification (§6.4a); the event is still always logged (A7/IC-3), so this is a realization rule, not an approval gate. **(2) The supply-chain hand-off model** — every hand-off is simultaneously verification (realizes the *prior* holder's credit), debit transfer (property-debit follows possession), and a new credit event (the receiver's own labour), which defuses the monopsony-gatekeeper capture by *inverting* a hoarder's leverage (§6.4a). **(3) Pledge broadened** — a pledge is a 1:1-backed pre-authorization of *creditable work*; it need not involve an object or move any debit (the grass-mowing case), and is the job-creating demand lever (§6.4). **(4) The two-kinds-of-debit taxonomy refined** — embodied-*material* debit transfers with the atoms, but *creation-cost/labour* debit is holding-time-split and each holder's share is **permanent** (§3.2, §6.2b); plus the **deployment timestamp** and the rule that transfer to a non-participant does *not* discharge. **(5) Co-product split is data-first** — measured at the facility, per period, temporally matched; the physics model is fallback + auditor ballpark (§3.4a). **(6) Pre-Aequitas assets** enter by choice as an *estimated genesis entry*, not a reservoir extraction (§6.2a). Plus two new mechanics: **land-occupation remediation debt** (§3.7) and the **market-public / persons-private** transparency principle (§5.3). Stress-tested (all three credit-realization exploits defused; residuals route to OP-1/OP-22/OP-25) — Objections v0.8 B10.
> **Prior:** v0.6 superseded v0.5 — OP-18 (team-credit dissolves under A2; labour rides the material split; cost ≠ scarcity). v0.5 superseded v0.4 — OP-23 (capital front-loading + holding-time-split), §3.2b (pollution/transport never transfer), §3.3 stock-dependence, §3.6 recycling & end-of-life.
> **Also supersedes:** OFCS (Open Fair Credit Standard) — see §8 for what is deliberately *not* inherited.
> **Primary audience of the first paper:** technologists / implementers.
> **Companion:** `00-strategy/Aequitas_Objections_v0.8.md` — the objections register. Read alongside §10.

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
| **Split of a team's credit across its members** | ✅ **Not a convention — dissolved (A2)** | Credit is *time worked* (§6), so each member is credited **their own hours** — the "welder caused 40% of the bridge" number is never needed. Credit is not a share of output. **OP-18's team-credit half was a mis-statement; A2 already answers it.** *(A residual remains — apportioning a jointly-*caused debit* across a team — but that is a debit-attribution question, minor, sibling to OP-25.)* |
| **Split of *labour* across co-products** | ✅ **Convention with a measurable basis — rides the material split** | One labour process yields several products (farmer's hours → beef + hide); the hours leave no per-product trace, so a convention is required (physical-trace test). The declared convention: **labour rides the same physical split §3.4a already measures for the process's materials** (mass/deposition for cattle, cracking-energy for a refinery). Adds *no new lever* — it piggybacks on the rival-audited material θ. Changes no one's credit; it is a debit-side cost figure only. **OP-18(α) — closed 2026-08-05.** |
| **Split of an asset's residual creation-cost across its holders** | ✅ **Convention with a measurable basis — holding-time** | Apportioning a fixed creation-cost is a choice, but **holding-duration is a physical trace**, so the convention is measured, not invented: share = holder's holding-time ÷ total holding-time over the asset's life (§6.2b). Respects the dummy and symmetry axioms an even split fails. |

> **✅ Removed in v0.4 — the co-product split.** The row reading *"Split of a joint process's debit across its co-products — convention, not yet chosen"* is **deleted, not filled in.** It was never a convention. See §3.4a: the process itself performed the split, and it is measurable. `00-strategy/OP-17_coproduct_allocation.md`.
>
> **✅ Removed in v0.5 — shared-overhead attribution (OP-23).** The v0.4 row *"Attribution of shared overhead to co-products — convention, currently inherited proportions"* is **deleted, not filled in.** Under §6.2b all capital and overhead accrues to the **asset**, never to the co-products, so there is nothing to attribute. The barn stays on the operator; hide and beef carry only their own consumables. `00-strategy/OP-23_capital_and_pollution.md`.

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

### 3.2 The two kinds of debit — and the two components of property debit *(refined v0.7)*

**Property debit — a *current-holdings* term.** It has **two components that behave differently on transfer**, and conflating them was an internal contradiction before v0.7:

- **Embodied-*material* debit — dischargeable.** The atoms you hold. Transferring the object releases it entirely; the material rides the object to the new holder. This is the "dischargeable on transfer" behaviour v0.5 described.
- **Creation-cost / labour debit — holding-time-split, and each holder's share is *permanent*.** The hours that *made* the object do **not** vanish when you pass it on. Your share is set by how long you held it (share = your holding-duration ÷ total holding-duration over the asset's life, §6.2b), and it **stays on your ledger, diluting but never zeroing**, after transfer. *(Worked case: a 500,000-hour house held 10 years, then transferred, leaves ≈250,000 hours on the seller once the next holder has held it an equal span — the holding-time share, permanent.)*

> **Why the split.** §3.2 (v0.5) said property debit "releases entirely on transfer"; §6.2b said creation-cost is holding-time-permanent. Both cannot be true of one quantity. The resolution: **the material transfers with the atoms; the making is holding-time-split and permanent per holder** (§6.2b). This is A1-clean — both attach to the object — but only one leaves when the object does.

- Work done on property *increases* the property's creation-cost debit.
- **The self-work identity holds *for the holding period*:** while you hold a thing, a repair earns credit for the labour exactly equal to the property's debit increase — net zero, excluding materials/energy consumed. This is what makes property a burden rather than an engine. On transfer, the material leaves and your holding-time share of the creation-cost persists (§6.2b) — you were credited for real work and bear your time-proportional share of the resulting debit; no rent, no appreciation, nothing earned without working.
  - *Corollary — subsistence.* Growing food and eating it yourself is the same identity: the farming labour credits you, the food carries that debit, consuming it returns the debit to you. **Net zero on labour, net cost on materials and energy consumed.** No special rule is needed; the existing identity already answers it.

**Transfer does not require a participant — and cannot be escaped by finding a non-participant** *(new in v0.7)*. Handing an object to someone **outside** Aequitas produces no event, so the record still shows *you* as holder: you keep its full debt-load. Handing it to someone **inside** Aequitas starts the new holder's holding-time accruing, so your share begins to dilute. **There is no exit through a non-participant** — the ledger only lightens when a real holder takes the thing on. (Effect: used goods enter cheap for the new holder — near-zero holding-time — and grow heavier the longer they are kept.)

**Consumption / pollution debit — a *permanent-history* term. Never discharged.**
- Locked into the record forever, **on whoever caused it.**
- But its **weight floats** with the current cost of mitigation (§3.3).

### 3.2b Only property transfers — pollution and transport never do *(new in v0.5)*

The two kinds of debit behave differently under transfer, and this is load-bearing:

> **Only property-debit — the embodied material you hold — transfers with an item. All pollution-debit and all transport/energy-consumption debit is permanent on whoever caused it and never transfers. Provenance records travel; the debit does not.**

- The **farmer** keeps the pollution-debt of the fertilizer runoff — not the person who buys the groceries.
- The **gold mine** is indebted by the mining process — not the owner of the jewelry.
- **Transport** fuel and its pollution stay on whoever caused the journey — the factory for inbound logistics, the consumer for final delivery — permanently, and cannot be shed by reselling the item.

**Why this is right under A1.** Ellerman's responsibility-imputation: only the miner *acted* to pollute; the buyer did not cause the mining. Charging the buyer would misattribute responsibility. This is simply the two-kinds distinction above taken to its conclusion — the *permanent* kind stays with its causer; the *transferable* kind rides the object.

> **This is the same principle as computational closure (§6.2a), seen from the other end.** Ellerman says pollution *must not* transfer to a non-causer; §6.2a says a cost *cannot* cascade indefinitely or the accounting never terminates. They are one rule: **cost never flows to whoever did not cause it** — downstream to a buyer (pollution) or upstream to the first human activity (historical cost). Both directions break the books, and the same non-cascade closes both. The gasoline case makes it concrete: the refinery's process emissions stay on the refinery, and the *combustion* emissions fall on whoever burns the fuel — never on the receiver of goods a truck delivered.

**The consumer signal is not lost.** §5.1b already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**. Buyers and pledgers can still see and prefer low-pollution goods; only the *debit* is pinned to the causer. See §7.2 for why this makes the anti-pollution incentive *stronger*, not weaker.

**Custody is accepted, not imposed** *(phrasing corrected in v0.5)*. "Custody follows possession, no right to refuse a transfer" means **no right to accept an object but refuse its debit** — you cannot take the object and disclaim what rides with it. It does **not** mean anyone can be forced to *receive* an object. Read the other way, the rule would license garbage-dumping, the exact abuse it exists to prevent (§3.6).

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

**Re-weighting is also *stock-dependent*, not only technology-dependent** *(new in v0.5)*. A pollutant's weight floats with the **ambient stock** of that pollutant, not merely with the state of mitigation technology. First, the baseline:

> **A flow is a *pollutant* only above the rate at which the natural world remediates it unaided.**

Steel produced only as fast as old steel rusts back to iron-oxide is in equilibrium and is not a pollutant. CO₂ emitted only as fast as the planet absorbs it — stable ppm, no warming — is at baseline and is not a pollutant. A compostable container carries no material pollution-debt, because it dissolves without human intervention in reasonable time.

Above baseline, the weight tracks **total remediation** — removal *plus* the escalating, nonlinear damage a unit does while resident — so:

- As excess CO₂ **rises**, there is more to remediate per unit, and **every historical record of CO₂ re-weights up.**
- As the stock is **drawn down**, those same records re-weight **down.**

Two consequences worth stating. **(1)** This is one mechanism, not two: atmospheric CO₂ and solid waste in a landfill are the same stock-dependent rule (§3.6). **(2)** It makes collective remediation individually rational — cleaning the commons *retroactively lightens every holder's own pollution-debt*, so environmental remediation pays the people who funded it, backwards through their history. A holder charged for others' current emissions is only ever charged for *their own* units, at a rate that reflects the collective damage — proportionality, not collective punishment.

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

**The v0.5 stock constants are governed here too** *(added v0.5)*. The **natural-remediation equilibrium baseline** and the **ambient-stock measurement** of §3.3 are powerful new constants — whoever sets them moves every pollution record in history — so they fall under exactly this regime: two unaffiliated replications before a re-weight, triage by magnitude × beneficiary concentration, and public membership as a capture screen. This is **OP-24** (understatement drift) acquiring a larger lever, not a new mechanism.

### 3.4 Resolution is opportunistic

**Resolution.** Record what is known; estimate the rest from averages; refine forever. If someone commutes daily, estimate from cohort averages; learn which car they drive and it sharpens. All of it revisable.

**⚠️ Amended in v0.4.** v0.3 stated flatly that *allocation is not a resolution problem because the indeterminacy is not epistemic.* **That is too strong and is now narrowed.** Allocation of physical inputs *is* a resolution problem — the process performed the split and better instruments converge on it (§3.4a). What is genuinely not epistemically resolvable is the division of quantities the process **never physically divided**: labour hours across co-products, shared overhead, and joint responsibility across a team.

> **The distinguishing test is whether the divided thing left a physical trace.** Where it did, measure. Where it did not, declare a convention (§1.1) and say so.

### 3.4a Joint production — the process allocates itself *(new in v0.4)*

One process, several outputs, one pool of debit. A steer yields beef, hide, tallow, bone, manure, and enteric methane; a refinery yields a full fraction slate; a CHP plant yields heat and power. **How the debit divides is a fact about the process, not a property of the outputs** — which is why a century of searching for the right *carrier quantity* (mass? energy? exergy? price?) found only rules that work in one industry and are category errors in the next.

> **A joint process's debit divides according to where the process itself physically sent its inputs.**
>
> The instrument is whatever that process makes traceable — tissue-deposition energetics for an animal, cracking enthalpy for a refinery, the extraction curve for a turbine, mitigation cost for an emission. These are not rival conventions; they are **different instruments reading the same underlying quantity, which is hours (A2).** Mass is an estimator, correct where composition is uniform and a low-resolution reading where it is not.

**Data first, model second — and match the period** *(sharpened v0.7)*. The split is driven **first by measured data at the actual facility over the actual period**, and only *then* by a physics model where data is missing. Three rules make this precise:

1. **Measure at the facility, per period.** The primary instrument is what the plant meters: masses in and out, energy and labour consumed, at *that* plant. Where a facility sub-meters per line (cutting vs tanning, grinding vs sieving), that **measured routing is the split**. Where it meters only aggregate energy plus output masses, the mass split is the low-resolution reading and a **physics model bridges the gap until finer metering exists.** Each dimension takes its own measured split (§3.2a).
2. **Temporal matching.** The split is computed from **data of the same period it describes** — never a stale back-average. Prefer the shortest practical window (a single day, a single batch run); a longer window forces you to cost output that has been sitting in inventory. *(Milling: weigh the oats in and flour+bran out per run — not from a standing table that cannot see changing conditions.)*
3. **The physics model is fallback and ballpark, not primary.** Tissue-deposition energetics, milling energetics, and the like fill gaps where no facility datum exists **and** give auditors the range a reported split must fall within. Finer data always supersedes the model (§3.3, §8-supersession).

> **This does not weaken "the process allocates itself" — it operationalises it.** "The process performed the split" *means* the split is a fact you measure at the process, per period; the model is what you use where the measurement is not (yet) taken. Data-first is the same discipline as the verification ladder (§4): a Level-1 producer reads mass, a Level-3 producer reads calorimetry, the model covers what neither instrument saw.

Four consequences worth stating:

- **Human preference plays no part — and scarcity is not cost** *(sharpened v0.6)*. A hide's share does not change because leather is fashionable, exactly as manure's share does not change because nobody wants it. A split contingent on demand would give two identical steers in two towns different splits — a universality failure, and price allocation in costume. **The sharp case: a tenderloin (≈1% yield) and hamburger (≈5% yield) cost the *same* per pound**, because a pound of each embodies the same feed, water, and growing-labour — refined only by *measured* tissue composition (lean vs fat differ in deposition energy), **never by yield or desirability.** Weighting a rare, prized cut as *more costly* is scarcity smuggled into cost; worse, it would ration that cut by **who can absorb the larger debit** — price-rationing by standing, the exact mechanism A5/§7.1 removes. **The scarcity of the tenderloin is real, irreducible, and handled elsewhere:** on the demand side by pledges/signals (§6.4, how many cattle get raised) and by **decentralised local distribution** (a butcher's lottery, queue, or pledge-priority — §7.5), never by inflating cost. Cost states what a thing took; who gets a physically-scarce output is a distribution question, deliberately left to the local free market and out of any central authority's hands.
- **Waste outputs are co-products like any other.** Counting manure and methane in the split removes the residual, and with it the whole question of who absorbs an unwanted output.
- **An output's cost share is set by the process; its ledger character is set by its fate.** Manure is pollution debit in a lagoon, a co-product in a biodigester, and an observed fertiliser offset when spread. Fate closure (EventLog IC-4) already records this; no new machinery is required.
- **Negative values do not arise.** Nothing is inverted, so Steedman's result does not transfer: each share is a forward measurement of what physically went in, and a deposition cannot be negative. ⚠️ *This is asserted, not yet proven for a recursive economy where every input is itself a joint split — see the objections register.*

**Labour is now covered — by declared convention** *(v0.6, OP-18(α))*. Labour has no per-product trace, so it cannot be *measured* into co-products the way materials are. The convention: **labour rides the process's own material split** — the same θ measured above (mass/deposition for cattle, cracking-energy for a refinery, the turbine curve for CHP). This adds no new degree of freedom and no new capture surface: it inherits the rival-audited material split rather than introducing a labour-specific basis. It is honestly a convention, not a measurement (the physical-trace test demands one here), but the *least-arbitrary* one available, and it **changes no one's credit** — the worker is credited their own hours regardless (§6); this only sets how each co-product's *debit-cost* reads. *Shared overhead was OP-23; v0.5 closed it — capital and overhead accrue to the asset and never allocate to co-products (§6.2b).*

> **What genuinely remains indivisible** is now a single narrow item: apportioning a **jointly-*caused* debit** (pollution or later-discovered harm from a team process) across the team members who caused it. This is a debit-attribution convention, minor and non-blocking, sibling to OP-25. Everything else the co-product question raised is closed.

### 3.5 The books never balance — and must not

Every real process dissipates. Credit records useful work; debit records material and energy consumed plus pollution. **Aggregate debit therefore exceeds aggregate credit permanently and by construction.**

This is not an accounting defect. **It is the second law of thermodynamics appearing in the ledger**, and a material-flow accounting that *did* balance would be the one describing something physically false.

Two consequences:

1. **No mechanism may require global balance.** Anything that does is wrong on thermodynamic grounds, not merely impractical.
2. **Sums are not meaningful; two separate numbers are.** **Ratio** (debit:credit) measures *efficiency* — how much you consumed per unit contributed. **Absolute credit** measures *contribution*. Neither substitutes for the other: a pure-ratio metric is infinite for a newborn and is gamed by ascetics who minimize both sides; a pure-sum metric ignores waste entirely.

**Why this does not collapse the economy, where a currency would.** In a monetary system, aggregate debt exceeding aggregate money is a solvency crisis — debt-deflation, spiral, collapse. Here **there is no creditor to be made whole**, because credit is non-fungible and never moves (A3). Permanent aggregate net-debit is simply the correct description of an economy running on a thermal gradient.

### 3.6 End-of-life, recycling, and product-as-pollution *(new in v0.5)*

An object's life does not end when it stops being useful. Three rules govern what happens then.

**1. End-of-life is consumption if unwanted.** No one can be forced to receive an unwanted asset and its debit (§3.2b). But whoever *does* accept an object accepts the property-debit that rides with it. If nobody will accept a worn-out asset, its **last holder has consumed it** and holds its end-of-life debit forever, as if it were food. This produces three clean incentives, none of them altruistic:

- Prefer durable, repairable goods over cheap disposable ones — you will eat their end-of-life debit.
- Maintain what you hold — a cooperative is better off servicing its equipment than running it to failure.
- Pledge toward remediation and recycling — because doing so *lightens your own* accumulated pollution-debt (§3.3).

**2. A discarded product is itself a pollutant.** A non-functional object sitting in the environment is a pollution-debt for as long as it persists, borne by its final holder, weighted by the stock rule (§3.3). A plastic bottle in a landfill raises the remediation cost of plastic; recycling or atomizing it discharges that debt and lowers every future unit's burden. A compostable object generates none of this, because nature remediates it unaided (§3.3 baseline).

**3. Recycling traces material forward — but not prior pollution.** The **material** of a recycled object carries its accumulated *property*-debit onward (the atoms physically carried forward, §3.4a). It does **not** carry prior producers' *process-pollution*, because under §3.2b that pollution never transferred — it stayed permanently on each producer. So recycled steel is cleanly lower-burden than virgin: it never carried the miner's tailings, and using it commissions no new extraction. **Recyclers are credited** for the work of reducing pollutants; the recycled output re-enters as a low-cost co-input (§3.4a).

> **⚠️ Live enforcement gap — OP-25.** Rules 1–3 price *lawful* disposal correctly. They do not by themselves stop *illicit* dumping — abandoning an object in the environment to escape its end-of-life debit. Attribution of abandonment back to the abandoner is a Level-2 trust-and-provenance problem, registered as OP-25.

### 3.7 Land is not owned; a building carries a remediation debt *(new in v0.7)*

Land cannot be *owned*. A building does not sit on property it holds title to — it **occupies a bounded space relative to the Earth**, and that occupation is itself a debit.

> **Every structure carries a *remediation debt* — the cost to restore its bounded space to its natural state** (strip lead paint and contaminants, remove the foundation and buried piping, refill the excavation, restore native soil and wildlife). It is a property-debit on the structure's holders, weighted by the stock/remediation rule (§3.3), and it behaves like the end-of-life debit of §3.6: it is only discharged to **zero by actually remediating** the space.

Two things persist regardless of remediation: the structure's **construction and maintenance** debts (§3.2, §6.2b) stay in the entity record forever — remediating the land clears the *occupation* debt, not the record of what was built. And the holder bears only what *they* effected: original-construction pollution and human harm stay on the original causer (§3.2b), never transferring to a later occupant.

**Governance rides existing machinery.** The remediation cost is a mitigation-cost estimate under the §3.3 stock-dependence rule and is disciplined by §3.3a rival-sector audit / OP-24 — no new capture surface.

> **⚠️ Hard edge — the "natural state" baseline.** What is the natural state of an already-urban bounded space (a plot in Manhattan)? This is the same shape as the §3.3 pollution baseline (a convention with a measurable basis, contested at the margin) and inherits its governance. **Registered as the open sub-question of this section**; the mechanism is sound, the baseline convention needs specifying.

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

### 5.3 Privacy — market data public, personal ledgers private *(principle stated v0.7)*

> **The transparency of Aequitas is split by *level*: the market is radically transparent, persons are private.** Pledges, production quantities, hand-offs, and debit-costs — the *supply-and-demand record* — are public (a pledger may be anonymous, like a Kickstarter backer, but the pledge itself is visible). Individual persons' aggregate positions stay private.

This split is **load-bearing, not incidental.** Public market data is what makes §3.3a rival-sector audit and independent economic monitoring *possible at all* — a worker can read how in-demand their product is; an auditor can watch a supply chain; nobody can privately mislabel pledged-vs-speculative work against a public pledge ledger (§6.4a). Public flows are the same "make it public so it cannot be gamed in private" move used for co-product splits (§3.4a) and cost constants (§3.3a).

> **⚠️ But transparency *depends on* OP-22, it does not bypass it.** Public pseudonymous events can be chain-analysed to de-anonymise a person — the classic ledger-privacy problem. Reconciling **public flows + private persons + unlinkability** is exactly OP-22 (the minimum-disclosure question below). The Kickstarter-anonymous intuition is the right shape; the mechanism is unsolved.

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

**The decisive reason, though, is computational closure** *(added v0.5)*. If a hospital's construction were amortized into each patient's bill, the accounting would have to chase the construction company's costs, then the equipment manufacturer's, then the steelmaker's, then the doctors' education — **an infinite regress to the first human activity.** The accounting would never terminate. Front-loading is what makes it *terminate*: you never chase an asset's own history, because the asset carries whatever creation-cost is knowable within Aequitas and everything upstream is out of scope by construction.

> **This is the upstream face of the non-cascade rule in §3.2b.** Pollution not transferring downstream to a buyer and cost not regressing upstream to the first human are the *same* constraint: **cost attaches only to the causer, and never cascades to anyone who did not act.** Ellerman-imputation and computational closure are one principle read in two directions.

> **The boundary is capital vs. consumption, not temporal.** A cost flows to a unit only if it is *consumed* producing that unit. A durable asset's *acquisition* is capital (front-loaded); only what it *consumes now* — energy, materials used up, wear — is a flow. The two are told apart by **physical fate**: does the thing survive the process? A drill bit that survives is capital; the oil it burned is consumption. Auditable via IC-4, not by the producer's declaration — which closes the *consumption-launderer* (reclassifying a used-up input as capital to move its debit off the unit).

**Corollary — pre-Aequitas assets** *(added v0.5, expanded v0.7)*. A cooperative taking over a 50-year-old hospital cannot reconstruct the architects' fees or the original currency costs. The asset *enters* Aequitas and accrues history from genesis forward; the pre-genesis past is unrecoverable — the same cutoff, in a new domain. v0.7 makes the entry precise:

- **Recording a "before" object is a *choice*.** Leave it unrecorded → it is invisible to Aequitas, with no registered ownership (a thief inherits no debt; fine for clothing and heirlooms one intends to keep). But an object cannot receive *creditable work* without a record — repairing an old fridge requires the fridge to exist in the ledger so the repairer can be credited.
- **When recorded, the entry is an expert *estimate*, not zero and not a reservoir extraction.** A qualified estimator reconstructs the construction labour and materials **plus all subsequent rehab**, at `basis: modelled`, low confidence, superseded by real records later. **The estimator is credited** for the estimation work. The dollar purchase price is worthless as a basis — estimate the material/labour cost instead.
- **Genesis is a distinct origin-terminus, not a reservoir.** A pre-Aequitas object did not enter *from a commons inside the system*; it enters as an estimated **genesis entry**, which is a legitimate endpoint for backward origin-tracing (EventLog IC-3) alongside a reservoir extraction — but it is not dressed up as one.
- **Original-construction harm does not transfer to the current holder** (§3.2b). A 200-year-old building may have been raised with slave or unrecorded labour and its era's pollution; the *current* holder bears only what they effected during their tenure (the gas stove's methane), never the original construction's suffering or emissions.
- **The reconstructed creation-cost is holding-time-split, not dumped whole on whoever holds it now** (§6.2b). The estimator's figure — original construction labour and materials *plus* all subsequent repairs and modifications over the asset's life — is the asset's **creation-cost**, and it settles by the ordinary holding-time waterfall: each holder's permanent share = **their holding-duration ÷ the asset's total life**. A person who owned a property for 20 of the 200 years it has existed therefore carries **10%** of its construction-and-rehab debit, not all of it. This is *why* the pre-Aequitas entry cannot bankrupt a new owner: entering an old asset does not import its whole two-century debit onto the person at the door — it imports only their tenure's slice, and earlier holders' shares stay pinned to those holders (estimated on the same terms, §5.1) or ride the asset as an un-attributed remainder until its life completes (no A4 leak). Rehab is split the same way, over the years since *that* rehab, so a repair done a decade before you arrived is mostly not yours either.
- **An auditor may create the record without the owner's consent** (A7 — everyone is accounted). A reluctant owner's mansion can be entered from estimates of its size and construction; if the owner later joins, they may *refine* it (with contractor records, motivated to show the debt is lower than estimated) — but the only route to a favourable credit:debit ratio is to **transfer the debt** to others, not to hide the asset.

**The consequence for media is worth spelling out.** Pledgers replace studios and investors, and **they receive no profit and cannot receive one** — so there is no mechanism by which a popular film gouges its audience at the box office. A production company's only return is recognition, which converts into demand and pledges for the next work. That is the entire incentive, and it points at making something good rather than something extractive.

**⚠️ Cold start.** Pledges follow reputation, so a first-time filmmaker attracts none — structurally similar to the problem unknown creators already face with capital. The barrier is far lower (attention, not money) and the ladder is real: make small unpledged work, accrue feedback (§6.3), then attract pledges. But it should be stated honestly rather than assumed away.

### 6.2b The capital-debit waterfall *(new in v0.5)*

Front-loading says *when* a durable asset's cost is discharged. This says *by whom*. A building, plant, or tool holds its own **creation-cost as property-debit on the asset itself** — property-debit attaches to objects (§3.2), so this is A1-clean. That debit is settled in three steps:

1. **Community pledges draw the creation-cost down first.** A pledge is *costly*: the pledger absorbs a share of the debit against their own debit-room (§6.4). Pledges are simultaneously the **construction authorization** and the **demand brake** — a facility is built at the scale the community will pledge for, the same "pledging supplies the natural limit" logic as §6.2. *(Hospital: 100k creation-cost − 50k pledged = 50k residual.)*
2. **The un-pledged residual is holding-time-split among the asset's holders.** Each holder's permanent share = **their holding-duration ÷ total holding-duration over the asset's whole life** (§1.1).
3. **The basic-needs floor caps how hard any residual bites** (§7.5).

**Why holding-time, and why it beats an even split.** Holding-duration is a *physical trace*, so the split is measured, not invented, and it passes the cooperative-game checklist an even split fails:

- **Dummy** — zero holding-time → zero share. A new hire bears ≈0, which kills the **entry-toll** an even split would impose on exactly the capital-intensive essential work (hospitals, water treatment) society most needs staffed.
- **Symmetry** — equal holding-time → equal share.
- **Progressive, and final only at disposal.** While the asset lives, earlier holders' shares *dilute* as new holding-time accrues; they freeze at disposal. This is A6 (progressive resolution), and the not-yet-attributed remainder rides the asset until its life completes — **no leak.**

**Worked example.** A holds a thing 1 year, passes it to B, B uses it 1 year, then it is disposed. Total = 2 holder-years → **each holds 50% of the creation-cost, forever.** For a multi-staff facility the denominator is holder-years across *all concurrent staff*, so shares dilute hard: a 30-year veteran among ~200 staff over a 60-year hospital holds ≈0.25%, not a crushing slab. A solo owner-operator of expensive private capital holds a large share — correctly; they solely used it. **Private durable goods** (no pledges) simply holding-time-split their full creation-cost across successive owners.

**The holding-time clock starts at *deployment*** *(new in v0.7)*. A durable good's ledger records the moment it **enters service** — a toaster's clock starts roughly at purchase, even if it sits boxed for a year. Holding-time (above) is counted from deployment, because deployment is when a holder begins actually *using* the asset and accepting its load.

> **Transit custodians do not accrue a creation-cost share** *(new in v0.7)*. A carrier holding 1,000 toasters for two days did not *make* them, so they take **no** holding-time share of the toasters' *creation-cost*. Transit adds only the carrier's own **transport-debt** (their labour + fuel, attributed to them, §3.2b), which becomes embodied cost in the goods. Creation-cost holding-time-split begins at **deployment/operation by an end-holder**, not during transit. This keeps the supply-chain hand-off model (§6.4a) — where every carrier briefly holds the goods — from silently loading the making of the toaster onto the truck driver.

**This closes OP-23.** All capital and overhead accrues to the asset and its holders; **it never allocates to co-products.** The barn stays on the operator; hide and beef carry only their own consumables. The honest trade-off: a per-unit debit-cost is therefore *not* a full-lifecycle figure — the capital footprint is located on the asset, not smeared across units, and is never lost (no A4 breach). See `00-strategy/OP-23_capital_and_pollution.md`.

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

> **Is it backed 1:1 by earned credit?** *(revised v0.7 — the old test was "does it commit debit?", which the grass-mowing case below breaks.)*

| | **Pledge** | **Signal** |
|---|---|---|
| Says | "I authorize this creditable work" | "I want this to exist" |
| Backed by | earned credit, 1:1 | nothing |
| Rate | **exactly 1 hour pledged per hour earned** | *n* per hour earned, or unbounded |
| Analogue | pre-order; choosing a GP; crowdfunding; commissioning a task | likes, ratings, applause |

**A pledge is a 1:1-backed pre-authorization of creditable work — it need not involve an object or move any debit** *(broadened v0.7)*. The old framing ("I will absorb this debit") was too narrow. Concrete case: a resident earns 4 credit-hours and **pledges 2 toward mowing the public verge on their block**. Someone with a mower sees the pledge, mows for an hour, submits evidence, and **is credited 1 hour** — 1 pledged hour remains for a later mow. *That is the entire transaction: no object changes hands, no property-debit moves, credits and pledges do not cancel.* The pledge simply **summoned an hour of creditable work** and spent an hour of the pledger's pledging-power to do it. Where the pledged work *does* yield a held object (a pre-order), the pledger takes on that object's property-debit on receipt — but that is the ordinary possession rule (§3.2), not what *defines* a pledge. What defines a pledge is the 1:1 credit backing (IC-8).

**Pledging is deliberately messy, and that is fine.** There will be unfulfilled pledges, frivolous pledges toward trivial or unverifiable tasks, and people learning to pledge well. Coordination groups and pledge-influencing politics will emerge around it. None of this is a defect: **pledges are the job-creating demand lever**, and a lever people organize around is a lever that works.

**Why pledges must be exactly 1:1.** A pledge that commits debit-absorption cannot exceed the credit backing it, or you get **fractional-reserve pre-ordering** — more debit committed than can be honoured, so when the goods arrive some pledger cannot take them and the producer is stranded holding it. This is a solvency constraint, not a preference. It also happens to be the only stationary value: pledging power created per period is *kL* and consumed at most *L*, so any *k* > 1 diverges until pledges filter nothing, and any *k* < 1 shrinks the directed economy to zero.

**Why signals should be plentiful.** Under 1:1 you can only signal for as much as you personally worked, so you signal your top priorities and the system learns nothing about your second tier. Cheap, abundant signals **reveal the full preference ordering rather than just the top slice.**

**What pledging is for:**

- **A decentralized demand signal.** Cost says what a thing takes; pledges say who wants it. Aequitas obtains this with no prices, no central optimizer, and **no Iteration Facilitation Board** — the standing body Parecon requires and [is attacked as implausible for](https://ejpe.org/journal/article/view/867).
- **A purpose for surplus.** A high producer whose ceiling far exceeds their appetite can *direct what gets made* instead of accumulating, which A3 forbids by design.
- **Funding education and speculative work** (§6.2, §6.6).
- **Collective prizes.** An X-Prize needs no oligarch or patron — a large enough pool of pledges is a crowdfunded bounty. Enterprise remains genuinely risky, as it always has been, and innovation has always flourished under that risk.

**Approval never gates credit — but *verification* gates its realization** *(revised v0.7)*. The work is **always recorded**: an event is logged the moment work is done, so origin closure holds and unpledged wheat still has a grower (A7, IC-3). What a pledge buys is a **guaranteed counterparty** for the resulting property debit. But a recorded credit **realizes** — begins counting toward the worker's position — only when the output is **verified**, exactly as A7 already gates an estimated position on observation. This is *verification, not approval*: no committee judges the work worthy; the trigger is objective evidence the output exists. See §6.4a for how, for a physical good, that verification *is* the hand-off.

### 6.4a Hand-off gates credit realization — the supply-chain model *(new in v0.7)*

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
- **Pledged production** (a pre-order = a promise to buy): the pledge **assures the run** — it guarantees a receiver, so the credit is effectively assured. Most work is of this kind.

Because pledges are **public** (§5.3), pledged-vs-speculative is not a label a producer can privately misapply to recruit or to shed risk — a worker reads it off the pledge ledger.

> **⚠️ Residual — the influence back-door.** Realized credit generates pledging-power (influence), which is measured in *gross hours worked*. A consumption-indifferent actor could in principle collude on hand-offs to fake gross hours and pump influence — bounded by IC-7 (24 h/day) and paid for in a wrecked ratio, and possibly self-starving since pledging *costs* debit-room (§6.2b). Whether this bites is an **OP-1 (influence) question, not a credit-realization flaw** — see Objections §B10 / the OP-1 entry.

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
Price ≡ cost means no profit in exchange. Embodied-material debit releases on transfer; self-work nets to zero while held (§3.2). **No rent, no rental income, no property speculation, no compounding capital.** Not banned — structurally impossible. *Ellerman's route reaches the same conclusion independently: only people act, so only people can be responsible, so capital cannot claim a residual.*

**The exploitative employer is structurally hollowed out** *(sharpened v0.7)*. The wage-extraction employer has no mechanism to exist: credit is non-transferable, so there are **no wages** to pay (A3); price ≡ cost, so there is **no surplus to appropriate** (A5); and a team's debit is shared **by hours worked, not by rank** (§6.2b), so a supervisor **cannot dump risk or cost onto subordinates**. Workers are credited by the *system* for their hours, not paid by a boss. **What survives is coordination** — organizing a process, directing what gets made, controlling access to desirable projects — and that residual power is real: it is the **coordinator-class problem (P4)**, the live blocker, not the extractive employer this system already forecloses.

**What survives, and is load-bearing: competition on efficiency.** A5 removes margin, not rivalry. §3.3a leans on this directly — rival sectors auditing each other's cost constants is the only thing standing between the weighting model and systemic under-costing.

### 7.2 Exploitation and pollution self-penalize *(rewritten v0.5)*
Harmful production carries the remediation cost of the harm. But — per §3.2b — that cost is permanent **on the producer who caused it**, not on the product that leaves the gate. So the penalty is **direct**: a polluter carries permanent pollution-debt, a poor efficiency ratio (§3.5), and restricted discretionary consumption (§7.5), whether or not any consumer ever notices.

**This is *stronger* than the consumer-mediated gradient it replaces.** The old framing ("dirty products cost the buyer more") leaned on consumers choosing the cleaner good — historically a weak force, because the cheap dirty product usually wins. Pinning the debit to the producer removes that dependency: exploitation and pollution self-penalize at the source. And the consumer signal is **not lost** — the good still carries a non-transferable provenance record (§5.1b, §3.2b), so buyers and pledgers can prefer low-pollution producers on top of the direct penalty. The incentive gradient reverses without regulation, on both channels.

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
- ~~**OP-18 — Responsibility is not divisible.**~~ **✅ Closed 2026-08-05 as the C3 blocker.** Team-credit dissolves under A2 (own hours); labour-across-co-products rides the material split by declared convention (§1.1, §3.4a); co-product cost is embodied input, not scarcity. **C3 is unblocked.** Narrow residue (jointly-caused debit across a team) is minor and parked. Note: `00-strategy/OP-18_labour_and_team_credit.md`.
- **OP-10 — Weighting-model governance.** Whoever sets the cost model controls every balance in history without touching a core rule. Largest hole in A8. §3.2a closes one side entrance (split before collapse) and §3.3a supplies a mechanism for cost constants; the general problem stands. **Now the top blocking problem.**

**High**
- **OP-24 — Understatement drift.** *(new in v0.4)* Errors that overstate debit get corrected; errors that understate it have no funder. Proposed fix — rival-sector audit (§3.3a) — is unproven and wants a simulation. **Attacks A4.** *(v0.5 enlarges its lever: the new stock/baseline constants of §3.3 are governed here.)*
- **OP-16 — The onerousness gap.** A2 resolves exertion, hazard, and skill. **Tedium and indignity have no material signature and nothing allocates labour to them.** Leading candidate: *hour-ceiling differentiation* — pay the premium in hours, not rate, justified by measured physiological sustainability limits. First check how much of OP-16 is simply unmeasured hazard.
- **OP-1 — Service → influence.** Strongest candidate: **pledging power accrues per hour worked, equally for all.** Not a voting scheme. *v0.7 adds a sub-question:* since realized credit → pledging-power is measured in *gross hours*, collusive hand-offs (§6.4a) could in principle fake gross hours to pump influence — bounded by IC-7 and paid in ratio, possibly self-starving via the debit-room cost of pledging. **The influence residual of the credit-realization model lands here.**
- **OP-6 — Feedback mechanics.** How signals aggregate without becoming a popularity plutocracy. With accumulation forbidden, feedback and pledging are the entire motivation system for anyone past their own consumption ceiling.

**Medium**
- **OP-3 — The estimation engine.** Requires a cohort *production* model as well as consumption, on the residual rule (§5.1b).
- **OP-8 — Can feedback be bought?** *(reframed)*
- **OP-9 — Preference revelation.** Largely answered by §6.4 pledges, plus scarcity-as-debit on the Kantorovich framing.
- **OP-22 — Minimum audit disclosure.** *(narrowed; more load-bearing after v0.7)* A C7 disclosure-set question — see §5.3. **The "market-public / persons-private" transparency principle (§5.3) *depends* on this being solved:** public flows must not chain-analyse into de-anonymised persons. Right shape (zero-knowledge); disclosure set unspecified.
- **OP-4 — Debit tolerance formula.** ⬆ *Slightly more load-bearing after v0.4: §7.5 is now the error-tolerance of the accounting, not only a welfare floor.*
- **OP-14 — Cohort shopping.** · **OP-15 — Ghost harvesting.**
- **OP-7 — Cross-level trade.**
- **OP-25 — Illicit end-of-life dumping.** *(new in v0.5)* §3.6 prices *lawful* disposal correctly; abandoning an object in the environment to escape its end-of-life debit is a Level-2 trust-and-provenance attribution problem.

**Closed**
- ✅ ~~**OP-23 — Shared-overhead attribution.**~~ **Closed in v0.5** (§6.2b): capital and overhead accrue to the asset and its holders and **never allocate to co-products**, so there is nothing to attribute. The interim inherited-proportions convention was deleted, not refined. `00-strategy/OP-23_capital_and_pollution.md`.
- ✅ ~~**OP-17 — Joint production allocation.**~~ **Closed in v0.4 for the material/energy half** (§3.4a): the process performed the split and it is measurable. The labour half moved to OP-18; the overhead half moved to OP-23, **now also closed.** **A row was deleted from §1.1 rather than filled in.**
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

### v0.7 (2026-08-06) — credit realization & the supply-chain hand-off model

Product of an adversarial design interview (the C11 session) with the author. Every substantive ruling was stress-tested; all three credit-realization exploits were defused and the residuals route to already-open problems (Objections v0.8 B10).

**1. §6.4 / §6.4a — credit realizes on verification; hand-off is that verification for a good.** *(substantive; near-axiomatic)* The work is always *recorded* (event logged, A7/IC-3 intact), but a credit **realizes** only when the output is verified — *verification, not approval*. For a physical good, each hand-off is verification + debit transfer + a new credit event. This **defuses the monopsony-gatekeeper capture** (a maker is credited at the first hand-off to any receiver; debit-follows-possession inverts a hoarder's leverage) and makes the count **self-auditing** (a receiver eats the debit of exactly what they accept). *Revises the v0.6 "approval never gates credit; always credited for what you materially did" to "recording is ungated; realization gates on verification."*

**2. §6.4 — pledge broadened.** A pledge is a **1:1-backed pre-authorization of creditable work**; it need not involve an object or move any debit (the grass-mowing case). The distinguishing test changes from "does it commit debit?" to "is it 1:1-backed by earned credit?" (IC-8). Pledges are deliberately messy and are the job-creating demand lever.

**3. §3.2 — the two-kinds-of-debit taxonomy refined (contradiction fixed).** Property debit has two components: embodied-**material** (transfers with the atoms) and **creation-cost/labour** (holding-time-split, each holder's share permanent, §6.2b). Resolves the v0.5 §3.2-vs-§6.2b contradiction (Bezos keeps his holding-time share after transfer). Adds: transfer to a **non-participant does not discharge**; used goods enter cheap and grow heavier with holding.

**4. §6.2b — deployment timestamp + transit-custodian rule.** Holding-time counts from **deployment** (entry into service). A **transit custodian accrues no creation-cost share** — transit adds only transport-debt; creation-cost holding-time-split starts at deployment, keeping the supply-chain model (§6.4a) from loading the making onto the carrier.

**5. §3.4a — co-product split is data-first.** Measured at the facility, per period, temporally matched (prefer day/batch); each dimension its own measured split; the physics model is fallback + auditor ballpark; finer data supersedes. Operationalises "the process allocates itself" without weakening it.

**6. §6.2a — pre-Aequitas assets expanded.** Recording is a *choice*; when recorded it is an expert *estimate* (estimator credited), at `basis: modelled`; **genesis is a distinct origin-terminus, not a reservoir**; original-construction harm does not transfer to the current holder; an auditor may create the record without consent (A7).

**7. §3.7 added — land is not owned; a building carries a remediation debt** (cost to restore its bounded space to natural state), governed by §3.3/§3.3a. Open sub-question: the "natural state" baseline of already-urban space.

**8. §5.3 — the "market-public / persons-private" transparency principle**, stated and made load-bearing (it powers §3.3a audit and §6.4a's public pledge ledger), and shown to *depend on* OP-22.

**9. §7.1 — the exploitative employer is structurally hollowed out** (no wages A3, no surplus A5, no rank-based dumping §6.2b); the residual power is coordination = P4.

**10. §10 updated** — OP-1 gains the influence-back-door sub-question; OP-22 becomes more load-bearing.

*Not changed:* every axiom A1–A8; the co-product physical-trace rule (only its *data-first ordering* is made explicit); the vector/split-before-collapse rule; the front-loading principle. *Stress-test:* Objections v0.8 B10 + §C tests owed (2b floor sim; OP-1 influence sim).

### v0.6 (2026-08-05) — OP-18 closed as the C3 blocker; labour & the cost-not-scarcity rule

**1. §1.1 — the two OP-18 rows.** *(substantive)* The "team credit" row is marked **dissolved (A2)**: credit is own hours worked, so no output-decomposition is ever needed to credit a team — the objection conflated credit-for-hours with share-of-output. A new row declares the genuine residue: **labour across co-products rides the process's material split** (the θ of §3.4a), a convention with a measurable basis that adds no new capture surface and changes no one's credit.

**2. §3.4a — labour covered by convention + cost ≠ scarcity.** *(substantive)* Labour has no per-product trace, so by declared convention it rides the material split. And a new consequence: **co-product cost is embodied input, never yield/scarcity** — a pound of tenderloin and a pound of hamburger cost the same, because each embodied the same feed and labour. Scarcity-weighting would ration the prized cut by who can absorb the larger debit (price-rationing, A5), so scarcity is routed to the demand side (pledges/signals) and to decentralised distribution (§7.5), never into cost. *(Method 2, yield-weighting, raised and rejected.)*

**3. §10 — OP-18 moved out of Blocking.** C3 is unblocked; OP-10 becomes the top blocking problem. Residue (jointly-caused debit across a team) is minor and parked.

*Not changed:* labour is still never rate-scaled; the material split itself is still a measurement (§3.4a), only its *extension to labour* is a convention. *Confirmed by:* `06-simulation/RESULTS.md` (recursion sim), which cleared the materials/energy split this extends. *Resolution note:* `00-strategy/OP-18_labour_and_team_credit.md`.

### v0.5 (2026-08-04) — OP-23 resolved; capital and pollution

**1. §6.2a + §6.2b — capital front-loading and the capital-debit waterfall.** *(substantive)* A durable asset holds its own creation-cost as property-debit; community pledges draw it down first (authorization + demand brake); the residual is **holding-time-split** among holders (share = holding-duration ÷ total holding-duration, final at disposal). The decisive justification is **computational closure** — downstream amortization would regress to the first human activity — and the boundary is **capital vs. consumption**, told apart by physical fate. *Closes OP-23; deletes its §1.1 row rather than filling it. Supersedes this session's interim even-split proposal.*

**2. §3.2b — only property transfers; pollution and transport never do.** *(substantive)* Only embodied-material property-debit rides an item. All pollution-debit and all transport/energy-consumption debit is **permanent on its causer** (the farmer's runoff, the miner's tailings), never transferring downstream. A1/Ellerman-grounded. Provenance records travel (§5.1b) so the consumer signal survives; only the debit is pinned to the causer.

**3. §7.2 rewritten.** The anti-pollution penalty is now **direct on the producer**, not consumer-mediated via a "dearer product" — stronger, because it does not depend on consumers noticing.

**4. §3.3 — stock-dependent re-weighting + the pollution baseline.** A flow is a pollutant only *above the natural-remediation equilibrium*; above it, weight floats with the ambient **stock** (total-remediation interpretation → rises with concentration). Unifies atmospheric CO₂ and solid waste under one rule; makes remediation retroactively lighten every holder's own debit.

**5. §3.6 — end-of-life, recycling, product-as-pollution.** Unwanted assets are consumed by their last holder; a discarded product is itself a stock-weighted pollutant; recycling traces *material* forward but not prior *process-pollution* (which never transferred), so recycled material is cleanly lower-burden. Custody phrasing corrected: no right to accept an object but refuse its debit — **not** a right to force acceptance.

**6. §3.3a, §1.1, §10 updated.** The new stock/baseline constants fall under rival-sector audit (enlarging OP-24's lever). §1.1 gains the holding-time-split convention (measurable basis) and loses the shared-overhead row. **OP-23 closed; OP-25 (illicit dumping) opened.**

*Stress-tested twice before adoption (capital front-loading; then the full waterfall) — verdict PASSES WITH CHANGES both times, all changes applied. The even-split residual was broken by the second pass and replaced by the holding-time split.* `00-strategy/OP-23_capital_and_pollution.md`.

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

*End of v0.7.*
