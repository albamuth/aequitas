# Aequitas — Event Log Data Model (C1)

> **Version:** 0.1
> **Date:** 2026-07-31
> **Status:** Working draft. The structure is settled; the taxonomies and two marked mechanisms are open.
> **Depends on:** `Aequitas_Foundations_v0.2.md` A1–A7
> **Validates against:** the sandwich trace (§10)

---

## 1. What this document has to get right

Everything else in the spec is a function of this schema. If C1 is wrong, C2–C8 are built on sand.

Four requirements, each traceable to an axiom:

| Requirement | Axiom |
|---|---|
| A record describes **matter and energy moving**, nothing else | A1 |
| Every flow names **where it came from and where it went** | A1, A4 |
| A record contains **no valuation of any kind** | A6 |
| A record makes rate-scaled labor **unrepresentable** | A2 |
| Every quantity declares **how it is known, how sure, and how finely** | A7, §4 |

The last is what lets word-of-mouth, a written log, a video, an instrument reading, and a pure estimate coexist in one log without any of them masquerading as another — and it is what lets the same schema serve a village and a refinery.

---

## 2. Primitives

Four types. Nothing else exists in the log.

**`Event`** — a bounded transformation of the world. The only record that is ever written.

**`Parcel`** — a bounded quantity of stuff with an identity and a custody holder. Parcels are created, split, merged, and destroyed *by events*. Parcels carry [[property-debit]].

**`Reservoir`** — an unowned commons: an airshed, a watershed, an ore body, a soil column, a landfill, the biosphere. Reservoirs have no holder, so flows into them become permanent [[consumption-debit]] on the agent responsible.

**`Account`** — one verified human, or an institution composed of them. Accounts hold parcels and act as agents.

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

**Every flow names an endpoint on both sides.** There is no such thing as an input from nowhere or an output to nowhere: the endpoint is either a parcel (which has its own history) or a named reservoir (a specific airshed, watershed, soil column, or landfill). *Came from* and *went to* are structural, not optional. §7 turns this into enforceable closure in both directions.

**There is one record shape.** A transfer is an event whose inputs and outputs are physically identical and differ only in `custody`. An extraction is an event whose inputs are reservoir flows. A consumption is an event whose outputs are reservoir flows. No event subtypes, no special cases — this is the universality criterion enforced at the data layer.

*Known tension:* modelling a pure custody change as a "transformation with identical inputs and outputs" is slightly forced. It is worth the uniformity, but flag it if a cleaner formulation appears.

---

## 3. The rule that makes everything else work

> **No event contains a weight, a cost, a price, or a value. Only physical quantities.**

An event says *0.070 kg of wheat, 1.4 MJ, 340 seconds of human presence, 0.035 kg CO₂ to airshed-EU-W*. It never says what any of that is worth.

Cost is produced at **projection time** by applying the current weighting model to the log. This is A6 stated structurally, and it is what makes [[retroactive-reweighting]] mechanical rather than miraculous: improving the science changes the model, not the history. Nothing is rewritten; everything recomputes.

Corollary: **the log is valid independently of any weighting model.** Two communities running different models read the same log and disagree about balances while agreeing entirely about facts. That is the decentralization criterion holding at the data layer.

This is deliberate, not tolerated. There is no single authoritative Aequitas database and there will not be one — competing implementations, reconciliation between them, and possibly averaging services are the expected end state ([[ledger-ecosystem]]). **What must agree across implementations is the physical record; what may differ is the weighting.** Since standing is used for ratios and relative scale rather than to price transactions against a fixed unit, models that disagree on absolutes can still agree on positions.

---

## 4. Three independent axes of detail

Detail is **not one dimension.** Three things vary independently, and collapsing them is the fastest way to make the log dishonest:

| Axis | Question | Field |
|---|---|---|
| **Basis** | How do we know? | `basis` |
| **Confidence** | How sure are we? | `confidence` |
| **Resolution** | What is the claim *about*? | `resolution` |

They are genuinely orthogonal. A well-validated model can be more reliable than a badly calibrated meter. A video can be excellent evidence at coarse resolution and useless at fine. A precisely measured facility-month says very little about any one item that came out of it.

All three are **mandatory on every quantity.** None may be omitted or defaulted.

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

**Word of mouth is a legitimate basis.** `recalled` is not a defect to be tolerated — it is the rung on which [[verification-ladder]] Level 1 actually runs, and it must be first-class or the system is not adoptable without infrastructure. What distinguishes it is low confidence and easy supersession, not exclusion.

**`imaged` behaves unlike every other basis.** A meter reading is a number someone recorded; the underlying reality is gone. An image is *re-interpretable later by better analysis* — footage of a delivery truck can be re-examined years on to identify the model, and therefore its real fuel consumption. Imagery is the only basis that gets **better retroactively without a new observation**, which makes it uniquely valuable to [[retroactive-reweighting]]. Worth a design note of its own later.

### 4.2 Confidence — how sure

```
Confidence { p: number | interval, assessor: AccountRef, method_ref: ModelRef }
```

Confidence must be **asserted by someone**, not floated. An unattributed confidence number is an authority with no name, which is precisely what A8 forbids. Different assessors may disagree about the same quantity; that disagreement is data.

Confidence is **not** derivable from basis. Do not build a table that maps `instrumented → 0.95`. Miscalibrated instruments, badly sited sensors, and well-validated models all break it.

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
> A perfectly instrumented facility-month divided by 400,000 units is a strong aggregate claim and a weak per-unit claim. Allocation down a resolution level must *lower* the resulting confidence, and the schema keeps the two claims separable so it can.

### 4.4 Why all three are mandatory

Without them, an estimate and a measurement are indistinguishable downstream and the estimation engine (C3) silently launders guesses into facts.

With them, any aggregation can report its own composition — *"this balance is 60% instrumented at item resolution, 25% testified at batch, 15% modelled at cohort"* — and a reader may **recompute while rejecting whichever portion they don't accept.** That capability is what makes the log verifiable by anyone rather than trusted from someone.

### 4.5 Interoperability across technology levels

The design rule from [[verification-ladder]] §4, made concrete:

- **The record shape never changes.** A village elder's `recalled` / `cohort` record and a refinery's `instrumented` / `item` record are the same structure with different field values.
- **A low-basis record is never refused.** It is accepted and its derived confidence degrades. Refusal would make participation conditional on infrastructure, which kills universality.
- **Confidence and resolution propagate downstream** through the parcel DAG. A product built from testified inputs cannot claim instrumented certainty about its footprint, no matter how well instrumented the final assembly was.
- **Upgrading is ordinary.** A record improves by supersession (§8) as better evidence arrives — the original stays permanently auditable.

The third point is the honest answer to OP-7 (cross-level trade): a Level 1 region and a Level 3 region trade freely, and the *confidence* of the resulting figures reflects the weaker link rather than the stronger. Whether that is **fair** — whether low-confidence regions end up systematically penalised — is still open and remains OP-7's real question.

---

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

**Events are immutable. Attestations accrete.** Confidence in an event is a projection over its attestation set — which is exactly the surface OP-2's collusion detection operates on.

---

## 6. Labor, and why A2 is enforced by omission

An `AgentRole` records **who, in what role, for what interval**. That is all.

There is no rate. There is no wage. There is no skill multiplier. **The schema has no field in which one could be written**, which is a far stronger guarantee than a rule forbidding it. The three real differences between workers resolve elsewhere, as material:

- **Hard labor** → the worker's extra caloric intake is a separate consumption event in their own record.
- **Hazardous labor** → the `process` classifier is what makes retroactive injection possible: when process P is later found harmful, every event tagged P is found by query and re-weighed. *This is the field that makes A2's hazard clause implementable at all.*
- **Skilled labor** → `capacity_ref` points at the training provenance: the events that constituted the person's schooling, with their real time and material costs.

### ⚠ Open: the amortization denominator

`capacity_ref` says *what the training cost*. It does not say **over how many future service-hours that cost spreads**. Candidates: expected career hours, actual career hours (only knowable posthumously), a fixed statutory window.

Every candidate has a problem, and the choice materially changes the debit borne by the recipient of a skilled service. **A2 is not fully implementable until this is settled.** Recommend it becomes an explicit open problem rather than sitting inside C1.

---

## 7. Integrity constraints — the part money can't do

Because the log is physical, it admits **conservation checks**. This is the schema's strongest property and has no analogue in any financial ledger.

**IC-1 — Mass balance.** For every event, Σ input mass = Σ output mass, within a declared tolerance. **Balance is checked within a single resolution level** — an `item` input cannot be balanced against a `site_period` output. Mixing grains to evade the check is itself a violation.

**IC-2 — Energy balance.** Σ input energy = Σ output energy + declared dissipation. Same resolution rule.

**IC-3 — Origin closure (backward).** Every parcel traces backward to a reservoir extraction. **No parcel may appear without ancestry.** This forbids materialization from nothing.

**IC-4 — Fate closure (forward).** Every parcel is, at any instant, in exactly one of three states: **held** by an account, **consumed** as input to a later event, or **released** to a named reservoir. A parcel with no current holder, no successor event, and no release is **unaccounted**, and the log reports it as such.

> IC-3 and IC-4 are the two halves of *"where it came from and where it went."* Backward closure alone lets material vanish; a mass that enters the system and never resolves to a holder, a transformation, or a named sink is exactly how real-world pollution disappears from real-world accounts. **Unaccounted mass is a first-class query result, not an absence.**

**IC-5 — Custody continuity.** A parcel has exactly one holder at any instant, and every change of holder is an event.

**IC-6 — Interval sanity.** An event cannot consume a parcel before it exists or after it is destroyed.

**IC-7 — Agent-time plausibility.** For any account and any window, the sum of its `AgentRole` intervals across all events cannot exceed wall-clock time in that window. **Nobody is credited with more than 24 hours of work per 24 hours.** Overlapping intervals within one event are permitted (a person may participate in concurrent activities); the total is what is bounded.

### 7.1 These checks need no trust model

IC-1 through IC-7 are **pure arithmetic on the log.** They require no social graph, no reputation system, no authority, and no inspection — only the ability to recompute, which [[derived-ledger]] gives to everyone.

That makes them the cheapest and most valuable audits available, and they should be built first. They catch the crude fraud for free and leave only the sophisticated cases to the trust ecosystem ([[distributed-auditing]]), which is the correct division of labour: **arithmetic where arithmetic suffices, judgement only where it doesn't.**

The consequence is worth stating plainly: **if a factory's declared outputs do not mass-balance its declared inputs, the missing mass went somewhere unrecorded — and the log itself says so.** Unrecorded emission stops being an enforcement problem and becomes an arithmetic error, detectable by anyone recomputing from the log with no authority and no inspection. That is [[no-externalities]] with teeth, and it is the single most compelling technical argument the project has.

---

## 8. Refinement and supersession

The log is append-only, so nothing is ever deleted or edited. **Records improve by supersession**: a new event carries `supersedes: <old_event_id>`. Projections follow the chain to its head; every superseded record stays permanently auditable.

This is the mechanism for all three kinds of improvement, and it is how the log grows more detailed over time without ever rewriting itself:

| Refinement | Example |
|---|---|
| **Basis** improves | A `recalled` delivery is superseded by the `logged` delivery note, later by `imaged` yard footage |
| **Resolution** sharpens | A `cohort` estimate of household energy use is superseded by `site_period` meter data, then by `item` |
| **Confidence** rises | Same basis and resolution, better calibration or a second independent assessor |

### 8.1 Estimated events

A7 requires records for flows nobody logged — a non-participant's commute, a cohort's average consumption. These are **generated events**: `basis: modelled`, `resolution: cohort`, attributed to a cohort-proxy account. They are ordinary events in every other respect.

They must be **distinguishable** (never silently aggregable with observed events — §4.4 makes this automatic) and **replaceable**.

### 8.2 The monotonicity rule

> Supersession may only move **toward** better evidence. A record may be superseded by one of equal or stronger basis and equal or finer resolution — never weaker or coarser.

An estimate may be superseded by an observation. **An observation may never be superseded by an estimate**, and an `item`-resolution record may never be superseded by a `cohort` one.

Without this, supersession is a laundering channel: anyone finding their measured record inconvenient could bury it under a flattering model. The rule is what makes [[onboarding-incentive]]'s progressive resolution honest rather than an invitation to selectively re-describe your history.

*Note the unresolved case:* a measurement later discovered to be **wrong** — a faulty meter. It cannot be superseded by anything weaker, but it should not stand. Likely answer is a `disputed` marker via attestation (§5) plus a same-or-better-basis correction, but this needs specifying.

---

## 9. What is deliberately absent

The schema has no field for: **price · wage · rate · profit · margin · interest · currency · value · balance · account total.**

Each omission is an axiom made structural:

| Absent | Axiom |
|---|---|
| price, margin, profit | A5 — [[price-equals-cost]] |
| wage, rate, multiplier | A2 — [[time-as-yardstick]] |
| currency, transferable credit | A3 — [[non-fungibility]] |
| balance, account total | A6 — [[derived-ledger]] |

A future implementer wanting to reintroduce profit cannot do it by populating a field. They must fork the schema, and the fork is visible to everyone recomputing from the same log ([[protocol-governance]]).

---

## 10. Validation — the sandwich, end to end

The completion test for C1. Numbers are **illustrative placeholders**, not sourced LCA figures — the point is that every flow has somewhere to go.

### 10.1 The chain

| # | Event | Inputs | Outputs | Note |
|---|---|---|---|---|
| E1 | Wheat cultivation | soil-N (res), water (res), CO₂ (res), fertilizer parcel, diesel parcel, agent 6 h | wheat parcel 70 g (share), CO₂ 0.031 kg → airshed, N-runoff 0.004 kg → watershed | Root event: draws from reservoirs |
| E2 | Harvest + haul to mill | wheat parcel, diesel 0.9 MJ | wheat parcel (custody → miller), CO₂ 0.002 kg | Transfer + transform in one |
| E3 | Milling | wheat 70 g, grid energy 0.4 MJ | flour 55 g, bran 15 g (parcel, not waste) | Mass balances: 70 = 55 + 15 |
| E4 | Baking | flour 55 g, water 35 g, gas 1.1 MJ | bread 80 g, water vapour 10 g → airshed, CO₂ 0.06 kg | Balances with vapour declared |
| E5 | Assembly + wrap | bread 80 g, filling 115 g, LDPE film 5 g | sandwich parcel 200 g | Film parcel traces to petro chain (stub) |
| E6 | Truck to retail | sandwich parcel, diesel 0.15 MJ (allocated share) | sandwich parcel (custody → retailer), CO₂ 0.011 kg | See E6b |
| **E6b** | **Mechanic repairs oil filter** | agent 45 min, filter parcel, **waste oil 0.3 kg → watershed** | truck parcel (debit increased) | **Attaches to the truck, propagates to every parcel it later carries** |
| E7 | Sale | sandwich parcel | sandwich parcel (custody → consumer) | Pure custody change; property debit moves |
| E8 | Consumption | sandwich 200 g, O₂ (res) | CO₂ + H₂O → airshed, excrement 40 g → sewer res, wrapper 5 g (custody retained) | Permanent consumption debit |
| E9 | Wrapper to landfill | wrapper 5 g | LDPE 5 g → landfill res | Custody released to reservoir |
| E10 | Microplastic release | *(generated, estimated)* | microplastics → water table, over 1000 y | Long-tail; re-weighed as remediation improves |

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

Note what is present and what is not: quantities, substances, reservoirs, an interval, a person and how long they were there. **No cost anywhere in the record.**

Note also the *mixture*. Within one event the fertilizer is `logged`, the yield is `instrumented`, the soil nitrogen is `modelled`, and the emissions figure is `modelled` at a coarser resolution than the event itself. That is the normal case, not a degenerate one — and the 70 g of wheat that reaches the sandwich inherits `basis: allocated`, `resolution: item`, at a confidence strictly lower than the 41,800 kg batch it was cut from (§4.3).

### 10.3 What the trace demonstrates

- **Externalities have nowhere to hide.** Fertilizer runoff, waste oil, and microplastics are ordinary output flows, structurally identical to the wheat. There is no "environmental" special case (A4).
- **The mechanic's leaky oil filter propagates.** E6b raises the truck parcel's debit; the truck's later transport events inherit a share into every parcel carried. This is the interconnectedness claim of the Overview, made mechanical.
- **Retroactive re-weighting has a handle.** E10's microplastic release is one `process` classifier away from being re-weighed the day remediation gets cheaper — with no edit to any record.
- **Mixed evidence coexists honestly.** One event carries `logged`, `instrumented`, and `modelled` quantities at three different resolutions, and the sandwich's inherited share is weaker than any of them. Nothing is rounded up to the best number in the record.
- **The chain runs at whatever level each link can manage.** E6b's mechanic may be `recalled` — one person's memory of a repair, months later — while E3's milling is `instrumented`. Neither blocks the other; the sandwich's final figure carries the confidence of its weakest link, which is the correct answer.
- **Custody and consumption separate cleanly.** E7 moves property debit entirely; E8 creates permanent consumption debit that never moves.
- **Nothing escapes.** The wrapper is tracked from parcel (E5) through retained custody (E8) to reservoir release (E9) to long-tail emission (E10). Had E9 never been written, IC-4 would have reported 5 g unaccounted rather than silently dropping it.

**C1's completion condition is met.** The sandwich encodes end to end, including the awkward parts.

---

## 11. What the projections do with this

Not C1's job to specify, but the schema must support each:

| Projection | Derivation |
|---|---|
| Parcel debit-cost | Sum over the parcel's provenance DAG × current weighting model |
| Property debit | Σ debit-cost of parcels currently held |
| Consumption debit | Σ weighted reservoir-releases attributed to the account, all history |
| Production credit | Agent participation in events yielding parcels |
| Confidence | Distribution of `knowledge` tags across the aggregation |

The DAG sum is the expensive operation and it is the whole of C4's feasibility question.

---

## 12. Who games this

| Exploit | Defence | Status |
|---|---|---|
| **Phantom parcels** — stuff from nowhere | IC-3 origin closure | Closed |
| **Vanishing material** — mass that quietly stops being tracked | IC-4 fate closure; unaccounted mass is a reported query result | Closed structurally |
| **Unrecorded emission** | IC-1/IC-2 conservation | Closed structurally; still depends on inputs being declared honestly, which is OP-2 |
| **Estimation shopping** — pick the model giving the lowest number | `method_ref` and `assessor` are recorded, so the choice is named, visible, and comparable across peers | Mitigated, not closed |
| **Confidence inflation** — assert high confidence on a weak basis | `confidence.assessor` is named and disputable via attestation; basis is separate and cannot be dressed up | Mitigated |
| **Granularity gaming** — record coarsely to hide detail | `scope` forces a record to declare its own grain, and IC-1 forbids cross-resolution balancing. **But nothing yet compels anyone to record finely when they could record coarsely.** | **Partly closed — see below** |
| **Precision laundering** — allocate a precise aggregate down to items and claim item-level precision | §4.3: allocation must lower confidence | Closed |
| **Supersession laundering** | §8.2 monotonicity — never toward weaker basis or coarser resolution | Closed |
| **Faulty measurement that can't be retracted** | §8.2 forbids weaker supersession; correction path unspecified | **Open** |
| **Debit dumping** — transfer high-debit parcels to a throwaway account | Requires acceptance semantics on custody change; not yet specified | **Open — C5** |
| **Attestation rings** | — | **OP-2, the critical path** |

### Granularity gaming — what's left

Declaring scope makes coarse recording *honest*, which is most of the problem. The residue is that a producer with something to hide can stay legitimately coarse forever, and the log will faithfully report "coarse, low confidence" without ever forcing improvement.

The likely answer is a **projection-side** one rather than a schema one: if low-confidence flows are weighed conservatively — costed at the pessimistic end of their interval — then vagueness becomes expensive and precision pays for itself. That converts an enforcement problem into an incentive, which is the correct shape for Aequitas.

**It is not specified, and it interacts with the weighting model, so it belongs to C4 rather than C1.** Flagging it as the most important open item this section produced.

---

## 13. Open dependencies

C1 cannot be finalized without external artifacts it does not itself define:

1. **Substance taxonomy** — versioned material identity. Probably built on an existing standard rather than invented.
2. **Process taxonomy** — the classifier that makes retroactive re-weighting queryable. Underrated; it is doing as much work as the schema.
3. **Role taxonomy** — must describe *what was done*, never rank. Watch that this does not become a wage ladder by the back door.
4. **Reservoir registry** — how airsheds, watersheds, soil columns, and landfills are identified and scoped. Fate closure (IC-4) is only as good as this registry: a release to an unnamed sink is exactly the hole IC-4 exists to close.
5. **Amortization denominator** for `capacity_ref` (§6) — blocks full A2 implementation.
6. **Confidence propagation rule** — how basis, confidence, and resolution combine along a parcel DAG. §4.5 asserts that the weakest link governs; the actual arithmetic is unspecified and is a prerequisite for C3 and C4.
7. **Conservative weighting of low-confidence flows** (§12) — the incentive that makes precision worth paying for. Belongs to C4.

Items 1–4 are ordinary standards work. **Items 5, 6 and 7 are theory work and each should be raised as an open problem.**

---

*End of v0.1.*
