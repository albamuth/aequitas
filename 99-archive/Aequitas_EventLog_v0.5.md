<!-- tag: evt-aequitas-event-log-data-model -->
# Aequitas — Event Log Data Model (C1)

> **Version:** 0.5
> **Date:** 2026-08-07
> **Status:** Working draft. The structure is settled; the taxonomies and the marked mechanisms are open.
> **Depends on:** `Aequitas_Foundations_v0.12.md` A1–A8
> **Supersedes:** `99-archive/Aequitas_EventLog_v0.4.md`. See §14. **v0.5 folds in the work-definition session (Foundations v0.8):** **verification generalises by output type** — the hand-off (§7.3) is only the *goods* case; **service** verifies by client attestation, **enrichment** by occurrence-attestation (**never by feedback** — that re-opens OP-8 (feedback firewall)), **self-care** by proof-of-life (§7.3a). The **anti-arbitrage guard** is added: a counterparty re-computes a claim through its *own* weighting model — comparison, never conversion — so a lax or over-generous network cannot export the credit it issues (§7.3a, depends on OP-22 (audit disclosure)). **Still no new primitive and no new field on `Event`** — a verifying attestation of any kind is an ordinary Attestation (§5) pointing at the work event.
> **Validates against:** the sandwich trace (§10)

---

<!-- tag: evt-s1 -->
## 1. What this document has to get right

Everything else in the spec is a function of this schema. If C1 (event-log schema) is wrong, C2–C8 are built on sand.

Four requirements, each traceable to an axiom:

| Requirement | Axiom |
|---|---|
| A record describes **matter and energy moving**, nothing else | A1 (materialism of cost) |
| Every flow names **where it came from and where it went** | A1, A4 (no externalities) |
| A record contains **no valuation of any kind** | A6 (derived, not stored) |
| A record makes rate-scaled labor **unrepresentable** | A2 (time as measure) |
| Every quantity declares **how it is known, how sure, and how finely** | A7 (universal accounting), §4 |

The last is what lets word-of-mouth, a written log, a video, an instrument reading, and a pure estimate coexist in one log without any of them masquerading as another — and it is what lets the same schema serve a village and a refinery.

---

<!-- tag: evt-s2 -->
## 2. Primitives

Four types. Nothing else exists in the log.

**`Event`** — a bounded transformation of the world. The only record that is ever written.

**`Parcel`** — a bounded quantity of stuff with an identity and a custody holder. Parcels are created, split, merged, and destroyed *by events*. Parcels carry [[property-debit]].

**`Reservoir`** — an unowned commons: an airshed, a watershed, an ore body, a soil column, a landfill, the biosphere. Reservoirs have no holder, so flows into them become permanent [[consumption-debit]] on the agent responsible.

**`Account`** — one verified human, or an institution composed of them. Accounts hold parcels and act as agents.

<!-- tag: evt-s2-1 -->
### 2.1 The single event form

Every event — production, transport, transfer, consumption, emission, extraction, repair — has the same shape:

```
Event {
  id           : hash of canonical content
  scope        : Scope                   // §4.3 — what this record is ABOUT
  interval     : { start, end }          // instants, TAI
  locus        : { geo, reservoir_scope[] }
  process      : { taxonomy_ref, version }
  inputs       : Flow[]                  // where it came from
  outputs      : Flow[]                  // where it went
  agents       : AgentRole[]
  supersedes   : EventId?                // §8
}

Flow {
  endpoint : ParcelRef | ReservoirRef    // named on BOTH sides, always
  substance: SubstanceRef                // versioned material taxonomy
  quantity : Quantity
  custody  : AccountRef?                 // present only on parcel flows
}

Quantity {
  magnitude : number
  unit      : kg | J | s | m3 | count
  basis      : Basis                     // §4.1 — how we know   (mandatory)
  confidence : Confidence                // §4.2 — how sure      (mandatory)
  resolution : Resolution                // §4.3 — how finely    (mandatory)
}

AgentRole {
  account      : AccountRef
  role          : RoleRef                // taxonomy; NOT a rank
  interval      : { start, end }
  capacity_ref  : CapacityId?            // §6 — training provenance
}
```

**Every flow names an endpoint on both sides.** There is no such thing as an input from nowhere or an output to nowhere: the endpoint is either a parcel (which has its own history) or a named reservoir. *Came from* and *went to* are structural, not optional. §7 turns this into enforceable closure in both directions.

**There is one record shape.** A transfer is an event whose inputs and outputs are physically identical and differ only in `custody`. An extraction is an event whose inputs are reservoir flows. A consumption is an event whose outputs are reservoir flows. No event subtypes, no special cases — this is the universality criterion enforced at the data layer.

*Known tension:* modelling a pure custody change as a "transformation with identical inputs and outputs" is slightly forced. It is worth the uniformity, but flag it if a cleaner formulation appears.

<!-- tag: evt-s2-2 -->
### 2.2 Two special events — genesis and deployment *(new in v0.4)*

Neither needs a new primitive or a new field; both are ordinary `Event`s used in a particular way, called out because IC-3 (origin closure), IC-9 (pledge discharge), and the holding-time projection depend on recognising them.

**Genesis entry.** An event admitting a pre-Aequitas object into the ledger (Foundations §6.2a). It has **no reservoir input and no parcel ancestry** — its output parcel is rooted here — and carries an estimated creation-cost (`basis: modelled`, low confidence, superseded later). It is the second valid terminus for IC-3 origin-closure. The `AgentRole` on it credits the **estimator** for the estimation work. It is a *choice*: an object with no genesis entry is simply outside Aequitas (no registered ownership).

**Deployment marker.** An event recording the instant a durable good **enters service** (a toaster ≈ its purchase, even if unboxed later). It starts the good's **creation-cost holding-time** (Foundations §6.2b) for the deploying holder. It is distinct from the hand-offs that realize credit (§7.3): a good may pass through several transit custodians — each realizing the prior holder's credit and adding transport-debt — **before** any deployment marker, and those custodians accrue no creation-cost holding-time share.

---

<!-- tag: evt-s3 -->
## 3. The rule that makes everything else work

> **No event contains a weight, a cost, a price, or a value. Only physical quantities.**

An event says *0.070 kg of wheat, 1.4 MJ, 340 seconds of human presence, 0.035 kg CO₂ to airshed-EU-W*. It never says what any of that is worth.

Cost is produced at **projection time** by applying the current weighting model to the log. This is A6 (derived, not stored) stated structurally, and it is what makes [[retroactive-reweighting]] mechanical rather than miraculous: improving the science changes the model, not the history. Nothing is rewritten; everything recomputes.

Corollary: **the log is valid independently of any weighting model.** Two communities running different models read the same log and disagree about balances while agreeing entirely about facts. That is the decentralization criterion holding at the data layer.

This is deliberate, not tolerated. There is no single authoritative Aequitas database and there will not be one — competing implementations, reconciliation between them, and possibly averaging services are the expected end state ([[ledger-ecosystem]]). **What must agree across implementations is the physical record; what may differ is the weighting.**

<!-- tag: evt-s3-1 -->
### 3.1 Debit is a vector, and splits happen on the vector *(new in v0.3)*

A projected debit is not one number. It is a bundle of physical quantities — kilograms per substance, joules, labour-hours, water volume, land-area-years — collapsed into a single comparable figure only on demand (Foundations §3.2a).

> **🔴 Any division of a debit is computed per dimension, on the vector, before collapsing.**
>
> Divide the collapsed scalar instead, and whoever maintains the weighting model silently controls every allocation in history. Per-dimension division is **weighting-independent**: two communities running different models compute *the same split* and disagree only about what it weighs — which is precisely the property §3 promises for everything else in the log.

This is a hard requirement on any implementation of the projection layer, and it closes a side entrance to OP-10 (weighting governance) that was invisible before the allocation rule was written.

---

<!-- tag: evt-s4 -->
## 4. Three independent axes of detail

Detail is **not one dimension.** Three things vary independently, and collapsing them is the fastest way to make the log dishonest:

| Axis | Question | Field |
|---|---|---|
| **Basis** | How do we know? | `basis` |
| **Confidence** | How sure are we? | `confidence` |
| **Resolution** | What is the claim *about*? | `resolution` |

They are genuinely orthogonal. A well-validated model can be more reliable than a badly calibrated meter. A video can be excellent evidence at coarse resolution and useless at fine. A precisely measured facility-month says very little about any one item that came out of it.

All three are **mandatory on every quantity.** None may be omitted or defaulted.

<!-- tag: evt-s4-1 -->
### 4.1 Basis — how we know

```
Basis = recalled | testified | logged | instrumented | imaged | modelled | allocated
```

| Basis | Meaning | Ladder rung |
|---|---|---|
| `recalled` | Human memory after the fact. Word of mouth. | L1 |
| `testified` | Contemporaneous human assertion, ideally multi-party | L1–2 |
| `logged` | A written or kept record — books, delivery note, work order | L1–2 |
| `instrumented` | Meter, scale, flow sensor, telemetry | L3 |
| `imaged` | Photo, video, satellite capture | L3 |
| `modelled` | Derived from a model with no direct observation | any |
| `allocated` | An apportioned share of a coarser parent claim | any |

Two things this ladder is designed to capture:

**Word of mouth is a legitimate basis.** `recalled` is not a defect to be tolerated — it is the rung on which [[verification-ladder]] Level 1 actually runs. What distinguishes it is low confidence and easy supersession, not exclusion.

**`imaged` behaves unlike every other basis.** A meter reading is a number someone recorded; the underlying reality is gone. An image is *re-interpretable later by better analysis*. Imagery is the only basis that gets **better retroactively without a new observation**, which makes it uniquely valuable to [[retroactive-reweighting]].

> **`allocated` means something more specific as of v0.3.** It marks a quantity apportioned from a coarser parent — and where that parent is a **joint process**, the apportionment is now governed by [[co-product-allocation]]: the share is measured from where the process physically sent its inputs, not chosen from a menu. `allocated` therefore names *how the number was reached*, and the confidence attached to it should reflect the quality of the process-physics data used, not the quality of the parent measurement alone.

<!-- tag: evt-s4-2 -->
### 4.2 Confidence — how sure

```
Confidence { p: number | interval, assessor: AccountRef, method_ref: ModelRef }
```

Confidence must be **asserted by someone**, not floated. An unattributed confidence number is an authority with no name, which is precisely what A8 (local governance) forbids. Different assessors may disagree about the same quantity; that disagreement is data.

Confidence is **not** derivable from basis. Do not build a table that maps `instrumented → 0.95`.

<!-- tag: evt-s4-3 -->
### 4.3 Resolution — what the claim is about

```
Resolution = item | batch | site_period | class_period | cohort
Scope { resolution, extent }        // on the Event itself
```

| Resolution | Example |
|---|---|
| `item` | This sandwich |
| `batch` | This morning's 400-loaf bake |
| `site_period` | This bakery, March 2026 |
| `class_period` | Commercial bakeries, this region, 2026 |
| `cohort` | Adults 30–45 in this metro area |

**Events carry a scope too**, not just quantities. An event may legitimately describe one baking, one bakery-month, or one industry-year. This is what makes coarse recording *honest* rather than merely permitted — the record states its own grain.

> **The rule that matters: precision at the aggregate does not transfer to the individual.**
> A perfectly instrumented facility-month divided by 400,000 units is a strong aggregate claim and a weak per-unit claim. Allocation down a resolution level must *lower* the resulting confidence.

<!-- tag: evt-s4-4 -->
### 4.4 Why all three are mandatory

Without them, an estimate and a measurement are indistinguishable downstream and the estimation engine (C3 (estimation engine)) silently launders guesses into facts.

With them, any aggregation can report its own composition — *"this balance is 60% instrumented at item resolution, 25% testified at batch, 15% modelled at cohort"* — and a reader may **recompute while rejecting whichever portion they don't accept.**

<!-- tag: evt-s4-5 -->
### 4.5 Interoperability across technology levels

- **The record shape never changes.** A village elder's `recalled` / `cohort` record and a refinery's `instrumented` / `item` record are the same structure with different field values.
- **A low-basis record is never refused.** Refusal would make participation conditional on infrastructure, which kills universality.
- **Confidence and resolution propagate downstream** through the parcel DAG. A product built from testified inputs cannot claim instrumented certainty about its footprint.
- **Upgrading is ordinary.** A record improves by supersession (§8) as better evidence arrives.

**Allocation instruments sit on the same ladder** *(added v0.3)*. Splitting a carcass by mass is the Level 1 reading of the same rule whose Level 3 reading is calorimetry. The instrument differs by rung; the justification does not. This is why [[co-product-allocation]] required no new schema and no new ladder.

---

<!-- tag: evt-s5 -->
## 5. Attestation is not a field

Attestations are **separate append-only records pointing at events**:

```
Attestation {
  id, event_id, attestor: AccountRef, stance: affirm | dispute,
  basis: Basis,                     // §4.1 — same enum as quantities
  scope: FieldRef[]?,               // may affirm part of an event, not all
  timestamp, signature
}
```

Three reasons this cannot live inside the event:

1. Attestations arrive **later**, sometimes years later. An event with mutable attestation fields is not immutable.
2. An event can accrue **unboundedly many**, including disputes.
3. Different [[verification-ladder]] levels attach differently to the *same* event.

**Events are immutable. Attestations accrete.**

<!-- tag: evt-s5-1 -->
## 5.1 Pledges and signals

Foundations §6.4 introduces the demand side. Both instruments are **records about the future**, so like attestations they point at things rather than living inside events.

```
Pledge {
  id, pledger: AccountRef,
  target      : EventRef | ProcessRef | AccountRef | Description,
  hours       : Duration,           // backed 1:1 by the pledger's earned credit
  expires_at  : Instant,            // §5.1a — unspent pledges must revert
  discharged_by : EventId?,         // set when the pledged work occurs
  timestamp, signature
}

Signal {
  id, signaller: AccountRef,
  target      : EventRef | AccountRef | ParcelRef,
  weight      : Scalar,             // unbacked; no credit is consumed
  timestamp, signature
}
```

**The distinguishing property is structural, not a flag: a `Pledge` carries `hours` backed 1:1 by earned credit (IC-8 (pledge backing)); a `Signal` does not.** *(Reframed in v0.4.)* v0.3 said the distinction was "a Pledge transfers debit and a Signal does not" — but a pledge need not transfer any debit. A pledge is a **1:1-backed pre-authorization of creditable work** (Foundations §6.4): pledging toward mowing a public verge summons an hour of creditable work and moves *no* property-debit at all. Debit transfer happens only when the pledged work yields a *held object* the pledger receives, and then it is the ordinary custody rule (IC-5 (custody continuity)), not what defines a pledge. **The invariant is the `hours` backing, checked by IC-8.** A signal has no `hours` field and never touches a ledger.

<!-- tag: evt-ic-8 -->
**IC-8 — Pledge backing.** For any account, the sum of its outstanding (undischarged, unexpired) pledged hours may not exceed its earned credit hours. This forbids fractional-reserve pre-ordering.

<!-- tag: evt-ic-9 -->
**IC-9 (pledge discharge) — Pledge discharge.** When pledged work occurs, `discharged_by` is set to the event. **If the work yields a held object**, its property debit moves to the pledger under the ordinary custody rules (IC-5); **if it is a pure service or public good** (mowing a public verge), no property-debit moves — the pledge simply consumed pledging-power to summon creditable work *(clarified v0.4, Foundations §6.4)*. Either way the discharge is capped by IC-8.

> **⚠️ Corrected in v0.3.** v0.2 described a pledge as *"the affirmative case of custody acceptance — the same rule that lets a transfer be refused."* **There is no such rule.** Custody is decided by physical possession (§5.2). A pledge is therefore a **pre-commitment to take possession**, not the positive half of a refusal right. The pledge mechanism is unchanged; the justification was wrong.

**Signals need no integrity constraint**, because nothing is conserved. Their failure mode is *flooding*, not imbalance, and flooding is a projection-side problem (OP-6 (feedback mechanics)).

<!-- tag: evt-s5-1a -->
### 5.1a Expiry

Unspent pledging power must revert, or the pool drifts down as pledges are made and forgotten. `expires_at` is mandatory. **Where reverted capacity goes — back to the pledger, or to a commons pool — is open and belongs to C5 (debit taxonomy).**

<!-- tag: evt-s5-1b -->
### 5.1b Credit recording is ungated; realization gates on verification *(revised v0.4)*

**A pledge never gates the *recording* of credit.** An agent's work is logged as an event whether or not anyone pledged for it — gating *recording* on approval would contradict A7 (universal accounting) and reproduce the origin-closure failure the A7 v0.2 amendment repealed (unpledged wheat must still have a grower for IC-3 (origin closure) to hold).

**But a recorded credit *realizes* — begins counting toward the worker's position — only on verification of the output** *(new in v0.4, Foundations §6.4a)*. This is not an approval gate: no one judges the work worthy. The trigger is **objective evidence the output exists**, exactly as A7 already gates an *estimated* position on observed supersession. **For a physical good, that verification is the hand-off** (§7.3): the receiver, by accepting possession, attests the goods are real and thereby realizes the maker's credit. The event is recorded at work-time; realization is a projection-time property that flips when a verifying attestation (typically a custody-accepting hand-off) arrives. See §7.3.

<!-- tag: evt-s5-2 -->
### 5.2 Custody is decided by possession *(settled in v0.3)*

**There is no right to refuse a transfer at the ledger level.** Whoever holds the thing holds its property debit. Author's decision, 2026-08-01.

Two consequences, and the second is the important one:

1. **A rule that was being relied on does not exist.** The rejected v1 of the OP-17 (joint production) work assumed a butcher and a tanner would negotiate a carcass split because either could refuse custody. They cannot. That branch of the argument was discarded, and any future mechanism resting on refusal must be checked against this section.
2. **Debit dumping has a physical defence rather than a ledger one.** You cannot move a parcel's debit without moving the parcel, and you cannot move the parcel without someone physically taking it. **The physical act is the consent step.** Combined with one-verified-human-one-account (C6 (identity)), which removes throwaway accounts, this closes the crude form of the attack.

**What remains open:** coerced or deceptive transfers — someone induced to accept a high-debit object. That is a fraud problem handled by courts and social pressure (Foundations §5.3), not a schema problem. **C5 should state this rather than leave "custody acceptance" listed as unspecified work.**

---

<!-- tag: evt-s6 -->
## 6. Labor, and why A2 is enforced by omission

An `AgentRole` records **who, in what role, for what interval**. That is all.

There is no rate. There is no wage. There is no skill multiplier. **The schema has no field in which one could be written**, which is a far stronger guarantee than a rule forbidding it. The three real differences between workers resolve elsewhere, as material:

- **Hard labor** → the worker's extra caloric intake is a separate consumption event in their own record.
- **Hazardous labor** → the `process` classifier is what makes retroactive injection possible: when process P is later found harmful, every event tagged P is found by query and re-weighed.
- **Skilled labor** → training is **credited work in its own right**, recorded as ordinary events at the time it occurs. `capacity_ref` is **attribution and audit metadata only** — it feeds no downstream calculation.

<!-- tag: evt-s6-1 -->
### 6.1 ⚠️ Labour hours do not allocate across co-products

The allocation rule adopted in v0.3 (§7.1a) splits a joint process's **materials and energy** by measuring where the process physically sent them. **It does not split labour, and no instrument will.**

An `AgentRole` interval attaches to the **event**, not to any one of its outputs. The farmer's six hours were spent on the herd; nothing in physics apportions them between the hide and the beef. Splitting them in proportion to metabolic energy would be an assumption wearing a measurement's clothes — exactly what §4.4 exists to prevent.

> **Schema consequence: none, and that is the correct outcome.** `AgentRole` already attaches at event level. **Projection consequence: severe.** A per-product labour-hour figure — which C3 (estimation engine) requires, and which [EXIOBASE](https://www.exiobase.eu/) uniquely carries — cannot be derived from this schema without a declared convention. **That convention is OP-18 (labour & team credit), and it is now what blocks C3.**

<!-- tag: evt-s6-2 -->
### 6.2 Resolved in v0.2: the amortization denominator

v0.1 flagged that `capacity_ref` said *what the training cost* but not **over how many future service-hours that cost spreads**. Every candidate denominator had a defect.

**The A2 (time as measure) v0.3 amendment dissolves the question.** Training cost does not flow downstream at all, so there is no denominator to choose. **No field may make a past training event contribute debit to a later service event** — the guarantee is structural, like the absent `rate` field.

---

<!-- tag: evt-s7 -->
## 7. Integrity constraints — the part money can't do

Because the log is physical, it admits **conservation checks**. This is the schema's strongest property and has no analogue in any financial ledger.

<!-- tag: evt-ic-1 -->
**IC-1 (mass balance) — Mass balance.** For every event, Σ input mass = Σ output mass, within a declared tolerance. **Balance is checked within a single resolution level.**

<!-- tag: evt-ic-2 -->
**IC-2 (energy balance) — Energy balance.** Σ input energy = Σ output energy + declared dissipation. Same resolution rule.

<!-- tag: evt-ic-3 -->
**IC-3 (origin closure) — Origin closure (backward).** Every parcel traces backward to one of **two valid termini**: a **reservoir extraction**, or a **genesis entry** for a pre-Aequitas asset *(second terminus added in v0.4)*. **No parcel may appear without ancestry.** A genesis entry is an estimated record of an object that existed before the ledger began (§2.2); it is a legitimate root **but not a reservoir** — it does not draw from a commons and creates no consumption-debit, it merely admits an already-existing object at an estimated creation-cost (Foundations §6.2a).

<!-- tag: evt-ic-4 -->
**IC-4 (fate closure) — Fate closure (forward).** Every parcel is, at any instant, **held**, **consumed**, or **released** to a named reservoir. A parcel with none of these is **unaccounted**, and the log reports it as such.

> IC-3 and IC-4 are the two halves of *"where it came from and where it went."* **Unaccounted mass is a first-class query result, not an absence.**

<!-- tag: evt-ic-5 -->
**IC-5 (custody continuity) — Custody continuity.** A parcel has exactly one holder at any instant, and every change of holder is an event.

<!-- tag: evt-ic-6 -->
**IC-6 (interval sanity) — Interval sanity.** An event cannot consume a parcel before it exists or after it is destroyed.

<!-- tag: evt-ic-7 -->
**IC-7 (24-hour cap) — Agent-time plausibility.** For any account and any window, the sum of its `AgentRole` intervals cannot exceed wall-clock time. **Nobody is credited with more than 24 hours of work per 24 hours.**

<!-- tag: evt-s7-1 -->
### 7.1 These checks need no trust model

IC-1 through IC-7 are **pure arithmetic on the log.** They require no social graph, no reputation system, no authority, and no inspection — only the ability to recompute.

**If a factory's declared outputs do not mass-balance its declared inputs, the missing mass went somewhere unrecorded — and the log itself says so.** Unrecorded emission stops being an enforcement problem and becomes an arithmetic error. That is [[no-externalities]] with teeth, and it is the single most compelling technical argument the project has.

<!-- tag: evt-s7-1a -->
### 7.1a Co-product allocation is a projection rule, not a schema rule *(new in v0.3)*

Foundations §3.4a settles how a joint process's debit divides across its outputs: **by where the process itself physically sent its inputs**, read with whatever instrument that process makes available.

**Nothing is added to the schema, and that is the finding.** An event already records several `outputs`, and §3 already forbids the event from carrying any weight or cost. The split is therefore computed **at projection time**.

**Data first, model second** *(sharpened v0.4, Foundations §3.4a)*. The split is computed **first from the event's own measured quantities** — the `inputs` and `outputs` metered at that facility for that `interval` (per line where the event records per-line flows, else the mass split) — and only **falls back to the published process-energetics model** (keyed by `process.taxonomy_ref`) for dimensions the event did not measure. Two consequences for the schema's honesty axes (§4):

- **Temporal matching is automatic** because the split is derived from *that event's* flows over *its* `interval` — not from a standing table. Prefer events at `batch`/`item` resolution over the shortest practical window; a wide `site_period` event costs inventory that sat.
- **The `allocated` basis's confidence tracks which path was used.** A split read from the event's own per-line meters is high-confidence; one filled from the process-energetics model inherits that model's confidence (§4.1). Finer data supersedes the model (§8).

Where the split *is* model-derived, it is computed from the published process-energetics model for that classifier — exactly where the mitigation-cost weights already live.

Three things follow:

1. **The process taxonomy is doing more work than ever** (§14 item 2). It is now the key not only for retroactive hazard injection but for the allocation model itself. **It was already underrated; it is now load-bearing twice.**
2. **Two communities with different energetics models will split the same event differently**, and both are valid readings of the same log — the same tolerance §3 already grants to weighting. What they may *not* differ on is the physical record.
3. **The schema needed no change to accommodate the single most dangerous open problem in the project.** That is a reasonable signal C1 (event-log schema) was right.

<!-- tag: evt-s7-2 -->
### 7.2 Projection-side integrity constraints *(new class in v0.3)*

IC-1…IC-9 check the log. **IC-10…IC-12 check a projection** — the first constraints in the spec that do. They are still pure arithmetic and still need no trust model, but they are computed against a weighting model rather than against records alone.

<!-- tag: evt-ic-10 -->
**IC-10 (non-negative allocation) — Non-negative allocation.** No output's allocated share of any dimension is negative. A computed negative is a measurement error or a misdrawn process boundary, never a commodity containing less than nothing.

> ⚠️ **This is asserted, not derived.** The argument — that a forward measurement of physical deposition cannot be negative — holds for one process in isolation. It is **not yet proven for a recursive economy** in which every input's own debit is itself a joint split. If the recursion does not converge, Sraffa re-enters here. **Objections register §C test 1.**

<!-- tag: evt-ic-11 -->
**IC-11 (exhaustive allocation) — Exhaustive allocation.** Per dimension, the outputs' allocated shares sum to exactly the event's recorded input total for that dimension. Nothing is created or lost in the split.

<!-- tag: evt-ic-12 -->
**IC-12 (boundary additivity) — Boundary additivity.** Allocating a process stage-by-stage must yield the same result as allocating it whole. **This is the defence against boundary gerrymandering**: a producer who redraws the process boundary to manufacture a favourable split produces a detectable arithmetic discrepancy rather than an arguable judgement call.

<!-- tag: evt-s7-3 -->
### 7.3 Credit realization is a projection property, set by verification *(new in v0.4)*

Foundations §6.4a rules that production credit **realizes on verification of the output**, and for a physical good the verifying event is the **hand-off** — a custody change (IC-5) in which the receiver, by accepting the parcel and its property-debit, attests the goods exist. This needs **no schema change**: a hand-off is already an ordinary custody-change event, and "realized?" is computed at projection time from whether such a verifying attestation exists — the same shape as A7 (universal accounting) realization (§8.2).

**One custody-change event does three things, all already representable:**

1. **Verification** → realizes the *prior* holder's production credit for the parcel.
2. **Debit transfer** → the parcel's embodied-material debit moves to the receiver (IC-5, §5.2).
3. **A new credit event** → the receiver's own labour (e.g. transport) is a normal `AgentRole` on the same or a linked event, realized when *they* hand on.

**Why this is safe against the obvious attacks:**

- **Gatekeeper capture** — a maker's credit realizes at the *first* hand-off to *any* receiver, so no downstream buyer can withhold it; and because debit follows possession (§5.2), a hoarder's leverage inverts. *(Foundations §6.4a.)*
- **Count inflation** — a receiver eats the debit of exactly what they accept (§5.2), so IC-1 mass-balance plus self-interest pin the hand-off quantity; the maker cannot unilaterally over-claim. Same incentive as rival-sector audit (Foundations §3.3a).
- **Wash-pledging / wash-trade** — see §12.1: real deployable work dominates it, so it is defused rather than merely mitigated.

> **Note — realization ≠ deployment.** Realization is at first hand-off. The **deployment marker** (§2.2) is a *separate* event that starts an end-holder's creation-cost holding-time (Foundations §6.2b). Transit custodians realize the *prior* holder's credit and add transport-debt, but accrue **no** creation-cost holding-time share.

---

<!-- tag: evt-s7-3a -->
### 7.3a Verification generalises by output type *(new in v0.5)*

Foundations §6.4b: the hand-off is only the **goods** case of realization. The schema already carries the general form, because a verifying event is just an **Attestation** (§5) pointing at the work event — no new primitive:

| Output | Verifying record |
|---|---|
| **Goods** | a custody-change **Event** (the hand-off, §7.3) |
| **Service** | a client **Attestation** (`stance: affirm`) on the service event |
| **Enrichment** | an occurrence **Attestation** on the work event — attesting it *happened*, never that it was liked |
| **Self-care** | statistical / proof-of-life: a verified live account (C6 (identity)) over the period; no per-event record needed |

Two schema-level consequences:

- **Feedback is not an attestation.** An affirming Attestation says *"this work occurred"*; a Signal (§5.1) says *"I want this."* Realization reads the former and **must never read the latter**, or Signals become convertible to credit — OP-8 (feedback firewall). They are different record types precisely so an implementation cannot conflate them.
- **The anti-arbitrage guard is a projection property, not a schema rule.** Because the log is valid independently of any weighting model (§3), a counterparty verifying a claim **re-computes it through its own model** over the shared physical log — *comparison*. There is no record that *converts* a balance from one model's units into another's; such a record would be an exchange rate, and the schema deliberately has no field for one (§9). This is what stops a lax or over-generous network exporting the credit it issues — and it **presumes the verifier can see enough to re-compute without seeing a full private history (OP-22 (audit disclosure), §5.3).**

<!-- tag: evt-s8 -->
## 8. Refinement and supersession

The log is append-only, so nothing is ever deleted or edited. **Records improve by supersession**: a new event carries `supersedes: <old_event_id>`.

| Refinement | Example |
|---|---|
| **Basis** improves | A `recalled` delivery is superseded by the `logged` delivery note, later by `imaged` yard footage |
| **Resolution** sharpens | A `cohort` estimate is superseded by `site_period` meter data, then by `item` |
| **Confidence** rises | Same basis and resolution, better calibration or a second independent assessor |

<!-- tag: evt-s8-1 -->
### 8.1 Estimated events

A7 (universal accounting) requires records for flows nobody logged. These are **generated events**: `basis: modelled`, `resolution: cohort`, attributed to a cohort-proxy account.

**Cohort figures are computed over the unmeasured residual only** *(added v0.3, Foundations §5.1b)*: **(N − Y) / Z**. Computed over the whole population instead, an estimated event free-rides on measured producers and the estimate improves as the *worst* producers stay dark. The residual rule makes darkness stop paying.

<!-- tag: evt-s8-2 -->
### 8.2 The monotonicity rule

> Supersession may only move **toward** better evidence. Equal or stronger basis, equal or finer resolution — never weaker or coarser.

An estimate may be superseded by an observation. **An observation may never be superseded by an estimate.**

Without this, supersession is a laundering channel.

*Note the unresolved case:* a measurement later discovered to be **wrong** — a faulty meter. Likely answer is a `disputed` marker via attestation plus a same-or-better-basis correction, but this needs specifying.

---

<!-- tag: evt-s9 -->
## 9. What is deliberately absent

The schema has no field for: **price · wage · rate · profit · margin · interest · currency · value · balance · account total.**

| Absent | Axiom |
|---|---|
| price, margin, profit | A5 (price ≡ cost) — [[price-equals-cost]] |
| wage, rate, multiplier | A2 (time as measure) — [[time-as-yardstick]] |
| currency, transferable credit | A3 (non-fungibility) — [[non-fungibility]] |
| balance, account total | A6 (derived, not stored) — [[derived-ledger]] |

A future implementer wanting to reintroduce profit cannot do it by populating a field. They must fork the schema, and the fork is visible to everyone recomputing from the same log.

**Add to the list as of v0.3: there is no field for an allocation fraction.** A co-product split is never *written*; it is *computed* (§7.1a). Someone wanting to assert a self-serving split has nowhere to put it — they would have to publish a process-energetics model, in public, subject to rival-sector audit (Foundations §3.3a). **The strongest kind of guarantee this document offers is the one where the exploit has no field to live in.**

---

<!-- tag: evt-s10 -->
## 10. Validation — the sandwich, end to end

The completion test for C1 (event-log schema). Numbers are **illustrative placeholders**.

<!-- tag: evt-s10-1 -->
### 10.1 The chain

| # | Event | Inputs | Outputs | Note |
|---|---|---|---|---|
| E1 | Wheat cultivation | soil-N (res), water (res), CO₂ (res), fertilizer parcel, diesel parcel, agent 6 h | wheat parcel 70 g (share), CO₂ 0.031 kg → airshed, N-runoff 0.004 kg → watershed | Root event: draws from reservoirs |
| E2 | Harvest + haul to mill | wheat parcel, diesel 0.9 MJ | wheat parcel (custody → miller), CO₂ 0.002 kg | Transfer + transform in one |
| E3 | Milling | wheat 70 g, grid energy 0.4 MJ | flour 55 g, bran 15 g (parcel, not waste) | **Joint production — see §10.4** |
| E4 | Baking | flour 55 g, water 35 g, gas 1.1 MJ | bread 80 g, water vapour 10 g → airshed, CO₂ 0.06 kg | Balances with vapour declared |
| E5 | Assembly + wrap | bread 80 g, filling 115 g, LDPE film 5 g | sandwich parcel 200 g | Film parcel traces to petro chain (stub) |
| E6 | Truck to retail | sandwich parcel, diesel 0.15 MJ (allocated share) | sandwich parcel (custody → retailer), CO₂ 0.011 kg | See E6b |
| **E6b** | **Mechanic repairs oil filter** | agent 45 min, filter parcel, **waste oil 0.3 kg → watershed** | truck parcel (debit increased) | **Attaches to the truck, propagates to every parcel it later carries** |
| E7 | Sale | sandwich parcel | sandwich parcel (custody → consumer) | Pure custody change; property debit moves |
| E8 | Consumption | sandwich 200 g, O₂ (res) | CO₂ + H₂O → airshed, excrement 40 g → sewer res, wrapper 5 g (custody retained) | Permanent consumption debit |
| E9 | Wrapper to landfill | wrapper 5 g | LDPE 5 g → landfill res | Custody released to reservoir |
| E10 | Microplastic release | *(generated, estimated)* | microplastics → water table, over 1000 y | Long-tail; re-weighed as remediation improves |

<!-- tag: evt-s10-2 -->
### 10.2 One record in full

```json
{
  "id": "evt:3f9c…",
  "scope": { "resolution": "site_period", "extent": "farm:1129 / 2026-season" },
  "interval": { "start": "2026-03-14T06:00:00Z", "end": "2026-09-02T00:00:00Z" },
  "locus": { "geo": "…", "reservoir_scope": ["airshed:EU-W", "watershed:Seine-01"] },
  "process": { "taxonomy_ref": "proc:agri.cereal.cultivation", "version": "2026.1" },
  "inputs": [
    { "endpoint": "res:soil-col:FR-2841", "substance": "sub:N-available",
      "quantity": { "magnitude": 1240, "unit": "kg",
                    "basis": "modelled",
                    "confidence": { "p": 0.6, "assessor": "acct:org:inra", "method_ref": "mdl:soil-n:4.2" },
                    "resolution": "site_period" } },
    { "endpoint": "parcel:fert:88a1", "substance": "sub:urea",
      "quantity": { "magnitude": 2400, "unit": "kg",
                    "basis": "logged",
                    "confidence": { "p": 0.97, "assessor": "acct:farm:1129", "method_ref": "mdl:invoice-recon:1.0" },
                    "resolution": "site_period" },
      "custody": "acct:farm:1129" }
  ],
  "outputs": [
    { "endpoint": "parcel:wheat-lot:c410", "substance": "sub:wheat.grain",
      "quantity": { "magnitude": 41800, "unit": "kg",
                    "basis": "instrumented",
                    "confidence": { "p": 0.99, "assessor": "acct:coop:220", "method_ref": "mdl:weighbridge:2.1" },
                    "resolution": "batch" },
      "custody": "acct:farm:1129" },
    { "endpoint": "res:airshed:EU-W", "substance": "sub:CO2",
      "quantity": { "magnitude": 18600, "unit": "kg",
                    "basis": "modelled",
                    "confidence": { "p": 0.75, "assessor": "acct:org:inra", "method_ref": "mdl:agri-ghg:7.1" },
                    "resolution": "class_period" } }
  ],
  "agents": [
    { "account": "acct:h:7731", "role": "role:cultivation.field",
      "interval": { "start": "2026-03-14T06:00:00Z", "end": "2026-03-14T12:00:00Z" },
      "capacity_ref": null }
  ]
}
```

**No cost anywhere in the record**, and — worth noting after v0.3 — **no allocation fraction either**, despite this event having two outputs. The split of its debit between the wheat and the CO₂ is computed later, from `proc:agri.cereal.cultivation`.

<!-- tag: evt-s10-3 -->
### 10.3 What the trace demonstrates

- **Externalities have nowhere to hide.** Fertilizer runoff, waste oil, and microplastics are ordinary output flows, structurally identical to the wheat (A4 (no externalities)).
- **The mechanic's leaky oil filter propagates.** E6b raises the truck parcel's debit; the truck's later transport events inherit a share into every parcel carried.
- **Retroactive re-weighting has a handle.** E10 is one `process` classifier away from being re-weighed.
- **Mixed evidence coexists honestly.** The sandwich's inherited share is weaker than any single record it came from.
- **Custody and consumption separate cleanly.** E7 moves property debit entirely; E8 creates permanent consumption debit that never moves.
- **Nothing escapes.** Had E9 never been written, IC-4 (fate closure) would have reported 5 g unaccounted.

<!-- tag: evt-s10-4 -->
### 10.4 The sandwich already contained a joint process *(new in v0.3)*

**E3 — milling — is joint production, and v0.1 and v0.2 both walked past it.** 70 g of wheat plus 0.4 MJ yields 55 g of flour *and* 15 g of bran. Mass balances, so IC-1 (mass balance) passes — but **how much of the 0.4 MJ belongs to the flour?**

Under mass allocation the bran takes 21%. Under the rule adopted in v0.3, the answer is measured: milling energy goes into **size reduction of the endosperm**, and separating bran is largely a sieving step. The split is *not* 79/21, and the correct figure comes from milling energetics rather than from a ratio anyone picked.

**Three things worth recording:**

1. **The problem was in the project's own validation trace from the start and nobody saw it.** Joint production is not an exotic edge case reachable only via refineries and slaughterhouses — **it is in a cheese sandwich.**
2. **The trace still validates**, because the schema records the outputs faithfully and defers the split to projection (§7.1a). No record had to change.
3. **`bran 15 g (parcel, not waste)` was already the right call** — v0.1 made it for tidiness, and v0.3's rule says every output of a joint process is a co-product, including the ones nobody particularly wants. **The instinct was correct before the reasoning existed.**

**C1's completion condition is met.** The sandwich encodes end to end, including the awkward parts and the one that was hiding.

---

<!-- tag: evt-s11 -->
## 11. What the projections do with this

| Projection | Derivation |
|---|---|
| **Co-product split** | Per dimension, from `process.taxonomy_ref` × the process-energetics model (§7.1a). **Computed before any collapse to a scalar (§3.1).** |
| Parcel debit-cost | Sum over the parcel's provenance DAG × current weighting model |
| Property debit | Σ debit-cost of parcels currently held |
| Consumption debit | Σ weighted reservoir-releases attributed to the account, all history |
| Production credit | Agent participation in events yielding parcels |
| Confidence | Distribution of basis/confidence/resolution across the aggregation |

The DAG sum is the expensive operation and it is the whole of C4's feasibility question. **The co-product split makes it worse**: the allocation is defined recursively, since every input's debit is itself a joint split. **Whether that recursion converges is untested and is the sharpest technical risk in the project** (Objections §C test 1).

---

<!-- tag: evt-s12 -->
## 12. Who games this

| Exploit | Defence | Status |
|---|---|---|
| **Phantom parcels** — stuff from nowhere | IC-3 (origin closure) origin closure | Closed |
| **Vanishing material** | IC-4 (fate closure) fate closure; unaccounted mass is a reported query result | Closed structurally |
| **Unrecorded emission** | IC-1/IC-2 conservation | Closed structurally |
| **Estimation shopping** | `method_ref` and `assessor` are recorded, so the choice is named and comparable | Mitigated |
| **Confidence inflation** | `confidence.assessor` is named and disputable; basis is separate and cannot be dressed up | Mitigated |
| **Granularity gaming** | `scope` forces a record to declare its own grain; conservative weighting makes vagueness expensive | Partly closed — C4 (re-weighting) |
| **Precision laundering** | §4.3: allocation must lower confidence | Closed |
| **Supersession laundering** | §8.2 monotonicity | Closed |
| **Faulty measurement that can't be retracted** | §8.2 forbids weaker supersession; correction path unspecified | **Open** |
| **Debit dumping** | §5.2 — possession is the consent step; C6 (identity) removes throwaway accounts | **Closed for the crude form**; coerced transfer is a fraud problem, not a schema one |
| **Attestation rings** | — | OP-2, deprioritized |

<!-- tag: evt-s12-1 -->
### 12.1 Attacks on the new records

| Attack | Structural answer | Status |
|---|---|---|
| **Over-pledging** | IC-8 (pledge backing) caps outstanding pledges at earned credit | Closed structurally |
| **Fabricated labour claims** | IC-7 (24-hour cap) caps at wall-clock; conservative weighting prices unattested claims at ~zero; pledges are the only route from asserted to backed | Closed |
| **Pledge parking** | `expires_at` is mandatory | Closed structurally |
| **Signal flooding** | Nothing in the schema; signals are unbacked by design | **Open — OP-6 (feedback mechanics)** |
| **Wash-pledging / wash-trade rings** | **Real deployable work dominates it** *(v0.4)*: real work *sheds* the debit (a buyer takes it) while a wash-trade *retains* it (the make-and-keep self-work identity nets ~zero, Foundations §3.2), plus real overhead is pure loss. Colluders end with ~zero net contribution, a wrecked ratio, and debt they can only shed by dumping (OP-25 (illicit dumping)). The residual — colluders manufacturing *pledging-power/influence* from gross fake hours — is bounded by IC-7 and routes to OP-1 (service → influence), not here. | ✅ **Defused** (residual → OP-1) |

<!-- tag: evt-s12-2 -->
### 12.2 Attacks on the allocation rule *(new in v0.3)*

| Attack | Structural answer | Status |
|---|---|---|
| **Ballast output** — produce a worthless high-mass output to soak up debit | **Closed by construction.** Under §7.1a a co-product carries only the energy and materials actually spent making it; genuine waste absorbs near zero. This attack works against *mass* allocation, which is why mass is only an estimator. | ✅ Closed |
| **Boundary gerrymandering** — split one process into two to change the base | **IC-12 (boundary additivity)** — stage-by-stage allocation must equal whole-process allocation. Detectable arithmetic, not an arguable judgement. | ✅ Closed |
| **Negative shares** | **IC-10 (non-negative allocation)** — asserted, not proven for the recursive case | ⚠️ Mitigated |
| **Instrument shopping** — pick whichever physical instrument flatters your product | Only one instrument is *applicable* per process, and applicability is publicly arguable from the process's own physics. A disputed instrument choice is priced pessimistically for the chooser (conservative weighting). | 🟠 Adequate, untested |
| **Overhead stuffing** — reclassify traceable inputs as overhead to escape into the soft inheritance rule | **Nothing yet.** §1.1 makes the choice visible; nothing makes it expensive. | 🔴 **Open — OP-23 (shared overhead)** |
| **Constant capture** — publish energetics favourable to your sector | Rival-sector audit + two unaffiliated replications before re-weighting history (Foundations §3.3a). Unproven. | 🔴 **Open — OP-24 (understatement drift)** |
| **Split before collapse violation** — an implementation that divides the scalar | §3.1 is a hard requirement; a conforming implementation is checkable by recomputing with a second weighting model and confirming the split is identical | ✅ Testable |

> **⚠ Conservative weighting remains load-bearing and unspecified.** It now backs *four* things: granularity (§12), OP-20's closure (Foundations §6.6), instrument-shopping above, and the interim mass estimator for un-instrumented producers. **C4, early.**

---

<!-- tag: evt-s13 -->
## 13. Open dependencies

C1 (event-log schema) cannot be finalized without external artifacts it does not itself define:

1. **Substance taxonomy** — versioned material identity. Build on an existing standard.
2. **Process taxonomy** — ⬆ **now load-bearing twice.** It keys retroactive hazard injection *and* the co-product allocation model (§7.1a). **The most underrated item on this list.**
3. **Role taxonomy** — must describe *what was done*, never rank.
4. **Reservoir registry** — fate closure (IC-4 (fate closure)) is only as good as this registry.
5. ~~**Amortization denominator**~~ — ✅ resolved in v0.2.
6. **Confidence propagation rule** — how basis, confidence, and resolution combine along a parcel DAG. **Prerequisite for C3 (estimation engine) and C4 (re-weighting).** *Now also needs to cover allocated shares, whose confidence derives from process-energetics data quality rather than from the parent measurement alone (§4.1).*
7. **Conservative weighting of low-confidence flows** — **escalated again** (§12.2). C4, early.
8. ~~**Co-product allocation convention**~~ — ✅ **resolved in v0.3.** Not a convention: the process performed the split and it is measurable (§7.1a, Foundations §3.4a). **Required no schema change.**
9. **Pledge reversion target** (§5.1a) — C5 (debit taxonomy).
10. **Process-energetics model registry** *(new)* — the published per-process data that §7.1a's splits are computed from, plus the replication and rival-audit rules of Foundations §3.3a. **This is a new external dependency created by resolving item 8, and it is where OP-24 (understatement drift) lives.**
11. **Labour allocation convention across co-products** *(new)* — §6.1. **This is OP-18 (labour & team credit), and it is what now blocks C3.**

Items 1–4 are ordinary standards work. **Items 6, 7, 9, 10 and 11 are theory work. Item 11 is the blocking one.**

---

<!-- tag: evt-s14 -->
## 14. Changes in v0.5

Folds in the work-definition session (Foundations v0.8). **Still no new primitive and no new field on `Event`.**

1. **§7.3a added — verification generalises by output type.** The hand-off is only the *goods* case; **service** verifies by a client Attestation, **enrichment** by an occurrence Attestation (attesting the work *happened*, never that it was liked), **self-care** by proof-of-life. A verifying attestation of any kind is an ordinary `Attestation` (§5) pointing at the work event — the schema already carried the general form.
2. **Feedback ≠ attestation, at the record level.** An affirming Attestation ("this occurred") realizes credit; a Signal ("I want this", §5.1) never does. They are distinct record types so an implementation cannot let feedback realize credit (OP-8 (feedback firewall)).
3. **The anti-arbitrage guard stated as a projection property.** A counterparty re-computes a claim through its *own* weighting model over the shared log (comparison); no record converts a balance between models (that would be an exchange rate — no field for one, §9). Presumes the OP-22 (audit disclosure) disclosure set (§5.3).

*Unchanged: every primitive and field; the three detail axes; IC-1 (mass balance) through IC-12 (boundary additivity); supersession monotonicity; the sandwich trace.*

<!-- tag: evt-s14-2 -->
## 14-prev. Changes in v0.4

Folds in the credit-realization session (Foundations v0.7). **No new primitive, and no new field on `Event`** — the strongest evidence yet that C1's schema is right.

1. **§7.3 added — credit realization is a projection property, set by verification.** For a physical good the verifying event is the hand-off; one custody-change event realizes the prior holder's credit, transfers the material debit, and hosts the receiver's own new labour. Defuses gatekeeper capture and makes the hand-off count self-auditing.
2. **§5.1b reworded — recording is ungated; *realization* gates on verification** (not approval). Preserves A7/IC-3 (unpledged wheat still has a grower) while making credit count only when the output is verified.
3. **§5.1 reframed — the Pledge/Signal distinction is the 1:1 `hours` backing (IC-8 (pledge backing)), not "transfers debit."** A pledge is a pre-authorization of creditable work and may move no debit (the public-verge case).
4. **IC-9 (pledge discharge) clarified** — discharge moves property-debit only when the work yields a held object; a pure service moves none.
5. **§2.2 added — genesis entries and deployment markers**, both ordinary events. **IC-3 (origin closure) now accepts a genesis terminus** (pre-Aequitas asset) alongside a reservoir extraction — a legitimate root that is *not* a reservoir.
6. **§7.1a — the co-product split is data-first**: computed first from the event's own measured flows over its interval, model as fallback; temporal matching is automatic and the `allocated` confidence tracks which path was used.
7. **§12.1 — wash-pledging/wash-trade upgraded from *Mitigated* to *Defused*** (real work dominates it; residual routes to OP-1 (service → influence)).

*Unchanged: every primitive, every field of `Event`, `Flow`, `Parcel`, `Reservoir`, `Account`, the three detail axes, IC-1 (mass balance) through IC-8, IC-10 (non-negative allocation) through IC-12 (boundary additivity), supersession monotonicity, and the sandwich trace.*

<!-- tag: evt-s14-3 -->
## 14-prev2. Changes in v0.3

1. **§7.1a added — co-product allocation is a projection rule.** Foundations §3.4a settles the split; **the schema needed no change to accommodate it**, because §3 already forbids events from carrying weights. Dependency item 8 closes.
2. **§3.1 added — debit is a vector and splits happen per dimension before collapsing.** Hard requirement on the projection layer; closes a side entrance to OP-10 (weighting governance).
3. **§7.2 added — IC-10 (non-negative allocation), IC-11 (exhaustive allocation), IC-12 (boundary additivity)**, the first **projection-side** integrity constraints in the spec. Non-negativity (asserted, not proven), exhaustiveness, and boundary additivity.
4. **§6.1 added — labour does not allocate across co-products**, and this is now what blocks C3 (estimation engine). Schema consequence: none. Projection consequence: severe.
5. **§5.2 added — custody is decided by possession; there is no refusal right.** Author's decision. **Corrects IC-9's justification in v0.2**, which described a pledge as the affirmative case of a rule that does not exist. Debit dumping moves from *open* to *closed for the crude form*, with a physical rather than a ledger defence.
6. **§10.4 added — the sandwich already contained a joint process.** E3 (milling → flour + bran) is joint production and was walked past in v0.1 and v0.2. The trace still validates. **Joint production is not exotic; it is in a cheese sandwich.**
7. **§8.1 — cohort estimates use the residual rule** (N − Y) / Z.
8. **§4.1, §4.5 — `allocated` basis clarified** and allocation instruments placed on the existing verification ladder.
9. **§9 — no field for an allocation fraction**, added to the deliberate-absence list. A self-serving split has nowhere to live; asserting one requires publishing a public model.
10. **§12.2 added** — attack table for the allocation rule. Two exploits closed by construction, two open (OP-23 (shared overhead), OP-24 (understatement drift)).
11. **§13 — item 8 closed; items 10 and 11 created.** Resolving the allocation problem produced one new external dependency (the process-energetics registry) and promoted one theory gap to blocking (labour allocation).

*Unchanged: every primitive, every field of `Event`, `Flow`, `Parcel`, `Reservoir`, `Account`, the three detail axes, IC-1 (mass balance) through IC-9 (pledge discharge), supersession monotonicity, and the sandwich trace. **The schema survived the resolution of the project's most dangerous open problem without a single field being added**, which is the strongest evidence yet that C1 (event-log schema) was right.*

---

*End of v0.5.*
