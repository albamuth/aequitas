<!-- tag: evt-aequitas-event-log-data-model -->
# Aequitas — Event Log Data Model (C1)

> **Version:** 0.8
> **Date:** 2026-08-22
> **Status:** Working draft. The structure is settled; the taxonomies and the marked mechanisms are open.
> **Depends on:** `Aequitas_Foundations_v0.19.md` A1–A8
> **Supersedes:** `99-archive/Aequitas_EventLog_v0.7.md`. **Coverage folded in (OP-26): consistency is not completeness, and provenance becomes a field rather than a word.** One over-claim in §7.1 is narrowed — IC-1/IC-2 convert an *under-declared* emission on a *recorded* event into an arithmetic error, and say nothing about a process recorded nowhere, which is a **coverage** question answered by Foundations §5.1b. Four additions follow: a **provenance block** beside the three axes (§4.1a) carrying `source_ref`, `method_ref`, `as_of`, `extent`, `uncertainty` and `supersedes`; **a tally is an event** that credits whoever performed it (§2.2), so provenance points into the log and is audited by the existing machinery; **the extent rule** (§7.4) — a passing check must publish what it was capable of detecting; and **IC-12 boundary additivity generalised from processes to tallies** (§7.2a), so a split tally's parts must sum to the coarser figure they came from. §8.1 gains the **conservative-count** and **floor** rules; §8.2's flagged open case — a measurement later found wrong — is resolved as **contest-without-replacement**. Two candidate constraints, **IC-13 (genesis admissibility)** and **IC-14 (citation closure)**, were stress-tested the same day and **rejected** (§12.3a): IC-13 refuses the ordinary late-joiner case and is defeated by epoch-shopping, and neither is arithmetic on the log. They are replaced by a **weighting rule** (a genesis creation-cost is estimated at the end unfavourable to the admitter, so laundering costs more than honest recording) and a **mandatory field** (the §4.1a provenance block, making "unsourced" a malformed record rather than a checker's finding). Full paper: `00-strategy/OP-26_coverage_and_closure.md`.
> **Prior (v0.7):** **Conforms the pledge records to Foundations v0.14 (pledges made permanent + the contingent reserve).** A pledge is now a **permanent, non-revocable grant of debit-room**, drawn from a finite lifetime pledging-budget (= lifetime earned credit). Record-level consequences: the **`retracted_by`** field is removed (there is no withdrawal); **`expires_at`** now marks a *burn* deadline, not a reversion (an undischarged pledge lapses and its budget is lost, never returned — resolving C5 in the negative); **IC-8** is read cumulatively; and surplus pledges beyond a task's cost form a **contingent reserve** (§5.1c) that activates only against a verified task-caused cost, with overflow reverting to the causer.
> **Change history:** `00-strategy/Aequitas_EventLog_CHANGELOG.md`.
> **Validates against:** the sandwich trace (§10)

---

<!-- tag: evt-toc -->
## Contents

- [1. What this document has to get right](#1-what-this-document-has-to-get-right)
- [2. Primitives](#2-primitives)
- [3. The rule that makes everything else work](#3-the-rule-that-makes-everything-else-work)
- [4. Three independent axes of detail](#4-three-independent-axes-of-detail)
- [5. Attestation is not a field](#5-attestation-is-not-a-field)
  - [5.1 Pledges and signals](#51-pledges-and-signals)
- [6. Labor, and why A2 is enforced by omission](#6-labor-and-why-a2-is-enforced-by-omission)
- [7. Integrity constraints — the part money can't do](#7-integrity-constraints--the-part-money-cant-do)
- [8. Refinement and supersession](#8-refinement-and-supersession)
- [9. What is deliberately absent](#9-what-is-deliberately-absent)
- [10. Validation — the sandwich, end to end](#10-validation--the-sandwich-end-to-end)
- [11. What the projections do with this](#11-what-the-projections-do-with-this)
- [12. Who games this](#12-who-games-this)
- [13. Open dependencies](#13-open-dependencies)
- [Change history](#change-history)

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
### 2.2 Three special events — genesis, deployment, and the tally

None needs a new primitive or a new field; all three are ordinary `Event`s used in a particular way, called out because IC-3 (origin closure), IC-9 (pledge discharge), the holding-time projection, and §4.1a provenance depend on recognising them.

**Genesis entry.** An event admitting a pre-Aequitas object into the ledger (Foundations §6.2a). It has **no reservoir input and no parcel ancestry** — its output parcel is rooted here — and carries an estimated creation-cost (`basis: modelled`, low confidence, superseded later). It is the second valid terminus for IC-3 origin-closure. The `AgentRole` on it credits the **estimator** for the estimation work. It is a *choice*: an object with no genesis entry is simply outside Aequitas (no registered ownership).

**Deployment marker.** An event recording the instant a durable good **enters service** (a toaster ≈ its purchase, even if unboxed later). It starts the good's **creation-cost holding-time** (Foundations §6.2b) for the deploying holder. It is distinct from the hand-offs that realize credit (§7.3): a good may pass through several transit custodians — each realizing the prior holder's credit and adding transport-debt — **before** any deployment marker, and those custodians accrue no creation-cost holding-time share.

**Tally.** An event recording a **measurement of a domain rather than a transformation of it** — a census, a survey, a satellite pass, a port manifest, a reservoir stock reading. It moves no parcel and touches no custody. Its `outputs` are the measured figure and the `extent` it covers; its `AgentRole` **credits whoever performed the measurement**, exactly as a genesis entry credits its estimator.

Three reasons it earns a name:

- **It makes provenance internal.** An estimated record's `source_ref` (§4.1a) points at a tally event, so the citation chain lives inside the append-only log and is audited by the machinery already there, rather than living in prose beside it.
- **It makes measuring the unmeasured *paid work*.** Foundations §5.1b already calls seeking data on non-participants *credited trust-network work*; the tally event is where that credit is actually recorded. This is what closes the fecundity loop for coverage concretely rather than rhetorically — **whoever improves the estimate of the dark is credited in the same ledger the estimate corrects.**
- **It is what splits.** When part of a tally's extent later becomes directly measured, the remainder re-estimates over the smaller extent (§8.1), and the parts must reconcile against the parent (§7.2a).

A tally whose source lies outside the system — an FAO figure, a national census — is recorded as a **declared external citation** instead of an in-log event. That is a trust boundary of exactly the same kind as a genesis entry, with exactly the same weakness; see §12.3.

---

<!-- tag: evt-s3 -->
## 3. The rule that makes everything else work

> **No event contains a weight, a cost, a price, or a value. Only physical quantities.**

An event says *0.070 kg of wheat, 1.4 MJ, 340 seconds of human presence, 0.035 kg CO₂ to airshed-EU-W*. It never says what any of that is worth.

Cost is produced at **projection time** by applying the current weighting model to the log. This is A6 (derived, not stored) stated structurally, and it is what makes [[retroactive-reweighting]] mechanical rather than miraculous: improving the science changes the model, not the history. Nothing is rewritten; everything recomputes.

Corollary: **the log is valid independently of any weighting model.** Two communities running different models read the same log and disagree about balances while agreeing entirely about facts. That is the decentralization criterion holding at the data layer.

This is deliberate, not tolerated. There is no single authoritative Aequitas database and there will not be one — competing implementations, reconciliation between them, and possibly averaging services are the expected end state ([[ledger-ecosystem]]). **What must agree across implementations is the physical record; what may differ is the weighting.**

<!-- tag: evt-s3-1 -->
### 3.1 Debit is a vector, and splits happen on the vector

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

> **`allocated` carries a specific meaning.** It marks a quantity apportioned from a coarser parent — and where that parent is a **joint process**, the apportionment is now governed by [[co-product-allocation]]: the share is measured from where the process physically sent its inputs, not chosen from a menu. `allocated` therefore names *how the number was reached*, and the confidence attached to it should reflect the quality of the process-physics data used, not the quality of the parent measurement alone.

<!-- tag: evt-s4-1a -->
### 4.1a Provenance — the citation beside the axes

**This is not a fourth axis.** The three axes describe *the claim*; provenance describes *where the claim came from*. A `basis` of `modelled` says what kind of number it is and never says who produced it, by what method, over what territory, or as of when. **"Cite your method" is not enforceable against a category tag**, so the citation gets fields of its own.

Every estimated record — and any record whose basis is not first-hand — carries:

| Field | Holds |
|---|---|
| `source_ref` | The tally this rests on: **an event id** where the tally is in the log (§2.2), else a declared external citation |
| `method_ref` | Resolvable pointer to the published method, with its vintage |
| `as_of` | The **data's** vintage — when the world was like this, distinct from when the record was written |
| `extent` | The domain the tally claims to cover |
| `uncertainty` | Stated error bounds, not merely a confidence number |
| `supersedes` | The earlier estimate this replaces, if any |
| `contested_by` | Appended dispute notes — see §8.2. **A record is never purged or edited; it is annotated.** |

**`basis` is unchanged.** Provenance is additive.

> **Provenance and extent are the same object.** §7.4's extent rule asks a verdict to publish its domain, extent and closure basis; the block above answers exactly those questions about a record's inputs. A verdict's extent is the union of its records' extents. That two separate requirements want the same fields is the signal the shape is right.

Note that `method_ref` also appears inside `Confidence` (§4.2), where it names the *assessor's* method for judging certainty. The two are different objects and both are wanted: one cites how the quantity was tallied, the other how the doubt about it was assessed.

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

**Allocation instruments sit on the same ladder**. Splitting a carcass by mass is the Level 1 reading of the same rule whose Level 3 reading is calorimetry. The instrument differs by rung; the justification does not. This is why [[co-product-allocation]] required no new schema and no new ladder.

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
  hours       : Duration,           // pledging-power spent (permanent), drawn 1:1 from lifetime earned credit
  expires_at  : Instant,            // §5.1a — undischarged pledges BURN at expiry (budget lost, not reverted)
  discharged_by : EventId?,         // set when the summoned work occurs (permanently records the grant as used)
  timestamp, signature
}

Signal {
  id, signaller: AccountRef,
  target      : EventRef | AccountRef | ParcelRef,
  weight      : Scalar,             // unbacked; no credit is consumed
  timestamp, signature
}
```

**The distinguishing property is structural, not a flag: a `Pledge` carries `hours` backed 1:1 by earned credit (IC-8 (pledge backing)); a `Signal` does not.** A pledge is a **permanent, non-revocable grant of debit-room** — a 1:1-backed pre-authorization of creditable work that confers *virtual credit* on its `target` at projection time, giving that target more room to carry a cost (Foundations §6.4, §6.2b). Three properties matter at the record level:

- **It consumes no credit, but spends a finite budget.** The pledger's earned *credit* never moves and is never earmarked; what a pledge spends is *pledging-power* — a **lifetime budget equal 1:1 to earned credit, drawn down permanently** (IC-8). A pledged hour is gone from that budget for good.
- **It is permanent.** There is no withdrawal; a receiver can rely on the granted room. The only way pledging-power leaves without funding work is the **burn** at `expires_at` (§5.1a) — and that too is a permanent loss to the pledger, never a return. A cooperative still cannot treat a pledge as a guaranteed sale (it is authorization + room, not a purchase), but it *can* count on the room not vanishing.
- **It moves no property-debit by itself.** Pledging toward mowing a public verge summons an hour of creditable work and moves *no* property-debit at all. Where the pledged work yields a *held object*, its debit moves under the ordinary custody rule (IC-5 (custody continuity)) to **whoever accepts possession** — which need not be the pledger — not because the pledge compelled it.

**The invariant is the `hours` backing, checked by IC-8.** A signal has no `hours` field and never touches a ledger.

<!-- tag: evt-ic-8 -->
**IC-8 — Pledge backing.** For any account, the sum of **all pledged hours it has ever made** (discharged, outstanding, and burned alike) may not exceed its **lifetime earned credit hours**. Pledging is a permanent draw on a finite budget, so the cap is cumulative, not a running "outstanding" total — the record-level form of "no fractional-reserve pledging" (Foundations §6.4).

<!-- tag: evt-ic-9 -->
**IC-9 (pledge discharge) — Pledge discharge.** When the summoned work occurs, `discharged_by` is set to the event; the pledging-power was already spent at pledge time, so discharge merely records the grant as *used* (not *returned*). **If the work yields a held object**, that object's property-debit moves under the ordinary custody rule (IC-5) to **whoever accepts possession** — the pledge does not compel the pledger to receive it, and taking it is a separate custody act on the accepter's own debit-room (§5.2). **If it is a pure service or public good** (mowing a public verge), no property-debit moves. There is no retraction path.

> **⚠️ A pledge is not a pre-commitment to take possession.** Custody is decided by physical possession (§5.2); there is no ledger-level obligation created by a pledge. A pledge confers *debit-room* on its target permanently (Foundations §6.4/§6.2b); it never binds the pledger to accept an object. Any earlier reading of a pledge as "the affirmative case of a custody-refusal right" is void — there is no such right.

**Signals need no integrity constraint**, because nothing is conserved. Their failure mode is *flooding*, not imbalance, and flooding is a projection-side problem (OP-6 (feedback mechanics)).

<!-- tag: evt-s5-1a -->
### 5.1a Expiry — burn, not reversion

An undischarged pledge cannot linger forever, or the projection carries dead grants. `expires_at` is mandatory, but at expiry an unspent pledge **burns**: the pledging-power is permanently lost to the pledger, **not** returned and **not** moved to a commons pool. Because pledges are non-revocable and unspent ones burn, **there is no reversion target to decide — this closes C5 (debit taxonomy) in the negative.** The burn is the discipline: pledging costs a finite budget whether or not the work ever happens, so frivolous or fantasy pledges are self-penalising.

<!-- tag: evt-s5-1c -->
### 5.1c The contingent reserve

When a task attracts **more pledged hours than it costs**, the surplus does not vanish and does not become consumable. It forms a **contingent reserve** attached to the task: earmarked, non-spendable debit-room that a projection activates **only against a verified future cost causally traceable to the task** (Foundations §6.4c). Record-level shape:

- **Activation is a claim event** carrying trace evidence; the projection honours it under the **physical-trace** test, or — for diffuse/latent harm with no individual trace — under the §5.1b cohort convention. An unfounded claim draws nothing.
- **Overflow reverts to the causer.** A claim exceeding the remaining reserve is only covered up to the reserve; the residual task-caused debit lands on the doer/cooperative under IC-5 / §3.7, not on the pledgers.
- **Pledge shares (and thus the reserve's cover) split pro-rata by hours *on the task*** — a doer's share = their task-hours ÷ total task-hours.
- **Unused reserve lapses** with the task; like a burned pledge, it never becomes consumable and never reverts.

<!-- tag: evt-s5-1b -->
### 5.1b Credit recording is ungated; realization gates on verification

**A pledge never gates the *recording* of credit.** An agent's work is logged as an event whether or not anyone pledged for it — gating *recording* on approval would contradict A7 (universal accounting) and reproduce the origin-closure failure A7 repealed (unpledged wheat must still have a grower for IC-3 (origin closure) to hold).

**But a recorded credit *realizes* — begins counting toward the worker's position — only on verification of the output**. This is not an approval gate: no one judges the work worthy. The trigger is **objective evidence the output exists**, exactly as A7 already gates an *estimated* position on observed supersession. **For a physical good, that verification is the hand-off** (§7.3): the receiver, by accepting possession, attests the goods are real and thereby realizes the maker's credit. The event is recorded at work-time; realization is a projection-time property that flips when a verifying attestation (typically a custody-accepting hand-off) arrives. See §7.3.

<!-- tag: evt-s5-2 -->
### 5.2 Custody is decided by possession

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

The allocation rule (§7.1a) splits a joint process's **materials and energy** by measuring where the process physically sent them. **It does not split labour, and no instrument will.**

An `AgentRole` interval attaches to the **event**, not to any one of its outputs. The farmer's six hours were spent on the herd; nothing in physics apportions them between the hide and the beef. Splitting them in proportion to metabolic energy would be an assumption wearing a measurement's clothes — exactly what §4.4 exists to prevent.

> **Schema consequence: none, and that is the correct outcome.** `AgentRole` already attaches at event level. **Projection consequence: severe.** A per-product labour-hour figure — which C3 (estimation engine) requires, and which [EXIOBASE](https://www.exiobase.eu/) uniquely carries — cannot be derived from this schema without a declared convention. **That convention is OP-18 (labour & team credit), and it is now what blocks C3.**

<!-- tag: evt-s6-2 -->
### 6.2 The amortization denominator — dissolved

An earlier draft flagged that `capacity_ref` said *what the training cost* but not **over how many future service-hours that cost spreads**. Every candidate denominator had a defect.

**The A2 (time as measure) amendment dissolves the question.** Training cost does not flow downstream at all, so there is no denominator to choose. **No field may make a past training event contribute debit to a later service event** — the guarantee is structural, like the absent `rate` field.

---

<!-- tag: evt-s7 -->
## 7. Integrity constraints — the part money can't do

Because the log is physical, it admits **conservation checks**. This is the schema's strongest property and has no analogue in any financial ledger.

<!-- tag: evt-ic-1 -->
**IC-1 (mass balance) — Mass balance.** For every event, Σ input mass = Σ output mass, within a declared tolerance. **Balance is checked within a single resolution level.**

<!-- tag: evt-ic-2 -->
**IC-2 (energy balance) — Energy balance.** Σ input energy = Σ output energy + declared dissipation. Same resolution rule.

<!-- tag: evt-ic-3 -->
**IC-3 (origin closure) — Origin closure (backward).** Every parcel traces backward to one of **two valid termini**: a **reservoir extraction**, or a **genesis entry** for a pre-Aequitas asset. **No parcel may appear without ancestry.** A genesis entry is an estimated record of an object that existed before the ledger began (§2.2); it is a legitimate root **but not a reservoir** — it does not draw from a commons and creates no consumption-debit, it merely admits an already-existing object at an estimated creation-cost (Foundations §6.2a).

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

**If a factory's declared outputs do not mass-balance its declared inputs, the missing mass went somewhere unrecorded — and the log itself says so.** An **under-declared** emission stops being an enforcement problem and becomes an arithmetic error: the inputs are on the books, the outputs are on the books, and the difference has nowhere to go. That is [[no-externalities]] with teeth, and it is the single most compelling technical argument the project has.

> **The limit of that claim, stated precisely.** It is a statement about **recorded** processes. Arithmetic over a set testifies to nothing outside the set, so a process recorded *nowhere* — one whose inputs came from an unrecorded source and whose outputs went to an unrecorded sink — is not an arithmetic error. **It is a coverage question, and coverage is answered by Foundations §5.1b, not by IC-1…IC-9.**
>
> The residual is narrower than it first appears. **IC-3, IC-4, IC-5 and IC-6 already force closure over everything the log touches**: delete a recorded event and its inputs lose their fate, its outputs lose their ancestry, its custody changes leave a gap. What survives is only a fully disjoint chain — *unrecorded extraction → off-ledger transformation → off-ledger sink* — which is a **participation boundary**, not a hole in the checks (Foundations §5.1: *participation is voluntary, coverage is not*).

<!-- tag: evt-s7-1a -->
### 7.1a Co-product allocation is a projection rule, not a schema rule

Foundations §3.4a settles how a joint process's debit divides across its outputs: **by where the process itself physically sent its inputs**, read with whatever instrument that process makes available.

**Nothing is added to the schema, and that is the finding.** An event already records several `outputs`, and §3 already forbids the event from carrying any weight or cost. The split is therefore computed **at projection time**.

**Data first, model second**. The split is computed **first from the event's own measured quantities** — the `inputs` and `outputs` metered at that facility for that `interval` (per line where the event records per-line flows, else the mass split) — and only **falls back to the published process-energetics model** (keyed by `process.taxonomy_ref`) for dimensions the event did not measure. Two consequences for the schema's honesty axes (§4):

- **Temporal matching is automatic** because the split is derived from *that event's* flows over *its* `interval` — not from a standing table. Prefer events at `batch`/`item` resolution over the shortest practical window; a wide `site_period` event costs inventory that sat.
- **The `allocated` basis's confidence tracks which path was used.** A split read from the event's own per-line meters is high-confidence; one filled from the process-energetics model inherits that model's confidence (§4.1). Finer data supersedes the model (§8).

Where the split *is* model-derived, it is computed from the published process-energetics model for that classifier — exactly where the mitigation-cost weights already live.

Three things follow:

1. **The process taxonomy is doing more work than ever** (§14 item 2). It is now the key not only for retroactive hazard injection but for the allocation model itself. **It was already underrated; it is now load-bearing twice.**
2. **Two communities with different energetics models will split the same event differently**, and both are valid readings of the same log — the same tolerance §3 already grants to weighting. What they may *not* differ on is the physical record.
3. **The schema needed no change to accommodate the single most dangerous open problem in the project.** That is a reasonable signal C1 (event-log schema) was right.

<!-- tag: evt-s7-2 -->
### 7.2 Projection-side integrity constraints

IC-1…IC-9 check the log. **IC-10…IC-12 check a projection** — the first constraints in the spec that do. They are still pure arithmetic and still need no trust model, but they are computed against a weighting model rather than against records alone.

<!-- tag: evt-ic-10 -->
**IC-10 (non-negative allocation) — Non-negative allocation.** No output's allocated share of any dimension is negative. A computed negative is a measurement error or a misdrawn process boundary, never a commodity containing less than nothing.

> ⚠️ **This is asserted, not derived.** The argument — that a forward measurement of physical deposition cannot be negative — holds for one process in isolation. It is **not yet proven for a recursive economy** in which every input's own debit is itself a joint split. If the recursion does not converge, Sraffa re-enters here. **Objections register §C test 1.**

<!-- tag: evt-ic-11 -->
**IC-11 (exhaustive allocation) — Exhaustive allocation.** Per dimension, the outputs' allocated shares sum to exactly the event's recorded input total for that dimension. Nothing is created or lost in the split.

<!-- tag: evt-ic-12 -->
**IC-12 (boundary additivity) — Boundary additivity.** Allocating a process stage-by-stage must yield the same result as allocating it whole. **This is the defence against boundary gerrymandering**: a producer who redraws the process boundary to manufacture a favourable split produces a detectable arithmetic discrepancy rather than an arguable judgement call.

<!-- tag: evt-s7-2a -->
### 7.2a Boundary additivity applies to tallies, not only to processes

A tally (§2.2) covers an extent. When part of that extent later becomes directly measured, the estimate for the remainder is recomputed over what is left — **which is the residual rule `(N − Y) / Z` applied recursively at finer extent** (§8.1). Splitting a tally and running the residual rule are the same operation; §8.1 simply performs it once.

> **IC-12 extends unchanged: a split tally's parts must sum to the coarser figure they came from.** Measured part + still-estimated part = parent. When the sum fails, the discrepancy is not an argument — it is *located*, and whichever component disagrees is the one to re-examine.

**This is how a fabricated tally is caught without testing the citation directly.** A fabricator does not control which sub-extent someone measures next, so a false regional total is exposed the first time any part of its extent is measured and the reconciliation fails. Independent testability, made arithmetic.

**The attack it invites, named:** choosing *which* part of an extent to measure so the residual lands favourably — boundary gerrymandering moved from processes to tallies. The additivity check above is the same defence IC-12 was written for, which is why generalising it beats inventing a new mechanism.

*Reservoirs are physically additive, so the same check applies to a reservoir's catchment partitioned into sub-catchments. This also answers cohort-boundary gerrymandering: a residual computed over a partition must equal the residual computed whole.*

<!-- tag: evt-s7-3 -->
### 7.3 Credit realization is a projection property, set by verification

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
### 7.3a Verification generalises by output type

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

<!-- tag: evt-s7-4 -->
### 7.4 The extent rule — a check must publish what it could see

Every constraint in §7 returns a verdict over a domain. **A bare verdict is not a result.**

> **A passing check must publish what it was capable of detecting.** A verdict is `(result, domain, extent, closure-basis)` — never a bare result.

| Part | Answers |
|---|---|
| `result` | Did the constraints hold? |
| `domain` | What was this check *about* — which accounts, which reservoirs, which window? |
| `extent` | What did it actually cover, which is not always the domain it intended |
| `closure-basis` | What warrants the claim that the extent is complete — a reconciled reservoir reading, a counterparty attestation, a cited tally, or *nothing*, said plainly |

**Why this is a schema-level rule and not a reporting nicety.** A check that reports `12/12 clean` with no statement of its blind spots invites exactly the reading §7.1 had to be narrowed against: internal consistency mistaken for completeness. **A zero means only that no violation was observed by those particular checks, over that stated extent.**

The four parts are the same four questions §4.1a's provenance block answers about a record's inputs, which is why **a verdict's extent is the union of its records' extents** and needs no separate machinery to compute.

*Where closure-basis is absent, the verdict is downgraded rather than invalidated — see the floor rule, §8.1.*

---

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

**Cohort figures are computed over the unmeasured residual only**: **(N − Y) / Z**. Computed over the whole population instead, an estimated event free-rides on measured producers and the estimate improves as the *worst* producers stay dark. The residual rule makes darkness stop paying.

**The rule runs continuously, not once.** As part of an extent becomes directly measured, *Y* rises, the extent of the estimate shrinks, and the remainder re-estimates over what is left. Grapes tallied as one region become a measured region and an estimated one. The parts must reconcile against the parent (§7.2a).

**Two disciplines govern the estimate itself.**

> **The conservative-count rule.** When *Z* — the count of actors that remain dark — is uncertain, **under-count it.** Under-counting raises each dark actor's estimated share, which is the direction that provokes them to surface and prove otherwise (Foundations §5.1a realization). Over-counting dilutes the estimate and feeds OP-24 (understatement drift). **The self-liquidating error is the safe one.**

> **The floor rule.** A quantity computed over incomplete coverage is a **floor, not a value**. Under-recording can only understate, so the recorded figure is a lower bound and improved coverage moves it in one direction only — up.

The floor rule sits beside §8.2's monotonicity and is the same discipline on a second axis: **monotonicity governs *basis*, the floor rule governs *extent*.** Together they say a record may only ever get better, whether the improvement is in how it is known or in how much of the world it saw.

<!-- tag: evt-s8-2 -->
### 8.2 The monotonicity rule

> Supersession may only move **toward** better evidence. Equal or stronger basis, equal or finer resolution — never weaker or coarser.

An estimate may be superseded by an observation. **An observation may never be superseded by an estimate.**

Without this, supersession is a laundering channel.

<!-- tag: evt-s8-2a -->
### 8.2a Contest without replacement

The case §8.2 leaves open — a measurement later discovered to be **wrong**, a faulty meter, a fabricated tally — is answered without weakening monotonicity, because **the answer is not supersession at all.**

> **No record is ever purged or edited. A record that is challenged is *annotated*.**

Two distinct operations, and conflating them is the error:

| Operation | Field | Meaning |
|---|---|---|
| **Supersede** | `supersedes` | A better record *replaces* this one. Monotonicity applies: equal-or-stronger basis, equal-or-finer resolution. |
| **Contest** | `contested_by` (§4.1a) | An appended note saying *this figure is disputed, here is the study*. **Replaces nothing.** Carries its own provenance block. |

A reader therefore sees the claim and its challenges together — a citation with a reply, which is what the literature does and what a ledger of estimates needs.

**The defence against a false record is independent testability, not a gate at write time.** A wrong figure persists until someone disproves it, exactly as in science. What the log guarantees is not that falsehood cannot enter, but that **entering leaves a permanent, dated, attributed trace, and that any part of its extent later being measured will expose it arithmetically** (§7.2a).

*Consequence for a faulty meter specifically:* the correction is an ordinary same-or-better-basis record that `supersedes` the reading, plus a `contested_by` note explaining the fault — so the instrument's failure is itself on the record and can be used to triage everything else it measured.

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

**Also on the list: there is no field for an allocation fraction.** A co-product split is never *written*; it is *computed* (§7.1a). Someone wanting to assert a self-serving split has nowhere to put it — they would have to publish a process-energetics model, in public, subject to rival-sector audit (Foundations §3.3a). **The strongest kind of guarantee this document offers is the one where the exploit has no field to live in.**

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

**No cost anywhere in the record**, and — worth noting — **no allocation fraction either**, despite this event having two outputs. The split of its debit between the wheat and the CO₂ is computed later, from `proc:agri.cereal.cultivation`.

<!-- tag: evt-s10-3 -->
### 10.3 What the trace demonstrates

- **Externalities have nowhere to hide.** Fertilizer runoff, waste oil, and microplastics are ordinary output flows, structurally identical to the wheat (A4 (no externalities)).
- **The mechanic's leaky oil filter propagates.** E6b raises the truck parcel's debit; the truck's later transport events inherit a share into every parcel carried.
- **Retroactive re-weighting has a handle.** E10 is one `process` classifier away from being re-weighed.
- **Mixed evidence coexists honestly.** The sandwich's inherited share is weaker than any single record it came from.
- **Custody and consumption separate cleanly.** E7 moves property debit entirely; E8 creates permanent consumption debit that never moves.
- **Nothing escapes.** Had E9 never been written, IC-4 (fate closure) would have reported 5 g unaccounted.

<!-- tag: evt-s10-4 -->
### 10.4 The sandwich already contained a joint process

**E3 — milling — is joint production, and the first drafts both walked past it.** 70 g of wheat plus 0.4 MJ yields 55 g of flour *and* 15 g of bran. Mass balances, so IC-1 (mass balance) passes — but **how much of the 0.4 MJ belongs to the flour?**

Under mass allocation the bran takes 21%. Under the adopted rule, the answer is measured: milling energy goes into **size reduction of the endosperm**, and separating bran is largely a sieving step. The split is *not* 79/21, and the correct figure comes from milling energetics rather than from a ratio anyone picked.

**Three things worth recording:**

1. **The problem was in the project's own validation trace from the start and nobody saw it.** Joint production is not an exotic edge case reachable only via refineries and slaughterhouses — **it is in a cheese sandwich.**
2. **The trace still validates**, because the schema records the outputs faithfully and defers the split to projection (§7.1a). No record had to change.
3. **`bran 15 g (parcel, not waste)` was already the right call** — an early draft made it for tidiness, and the rule says every output of a joint process is a co-product, including the ones nobody particularly wants. **The instinct was correct before the reasoning existed.**

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
| **Over-pledging** | IC-8 (pledge backing) caps *cumulative* pledges at *lifetime* earned credit | Closed structurally |
| **Fabricated labour claims** | IC-7 (24-hour cap) caps at wall-clock; conservative weighting prices unattested claims at ~zero; pledges are the only route from asserted to backed | Closed |
| **Pledge parking** | `expires_at` is mandatory | Closed structurally |
| **Signal flooding** | Nothing in the schema; signals are unbacked by design | **Open — OP-6 (feedback mechanics)** |
| **Wash-pledging / wash-trade rings** | **Real deployable work dominates it**: real work *sheds* the debit (a buyer takes it) while a wash-trade *retains* it (the make-and-keep self-work identity nets ~zero, Foundations §3.2), plus real overhead is pure loss. Colluders end with ~zero net contribution, a wrecked ratio, and debt they can only shed by dumping (OP-25 (illicit dumping)). The residual — colluders manufacturing *pledging-power/influence* from gross fake hours — is bounded by IC-7 and routes to OP-1 (service → influence), not here. | ✅ **Defused** (residual → OP-1) |

<!-- tag: evt-s12-2 -->
### 12.2 Attacks on the allocation rule

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

<!-- tag: evt-s12-3 -->
### 12.3 Two trust boundaries with the same weakness — ❌ candidates REJECTED 2026-08-22

**Stress-tested jointly and both rejected as integrity constraints.** The attack they were written against is real; the instrument was wrong in both cases. The replacements are in §12.3a. Recorded here in full because the reasoning matters more than the verdict.

**The shape.** IC-3 admits parcels by two termini: a reservoir extraction, or a **genesis entry**. §4.1a admits estimates by two termini: an in-log tally, or a **declared external citation**. In each pair, the second terminus is a claim the log cannot re-derive from its own bytes. **A terminus that cannot be re-derived is a laundering surface.**

**Attack A — genesis-entry laundering.** Extract off-ledger → transform off-ledger → **admit the product via a genesis entry** → origin closure satisfied, extraction and process debit erased and replaced by a low-confidence estimate. Genesis is *described* as admitting an object that existed **before the ledger began**, but no constraint enforces that.

> **Candidate IC-13 — genesis admissibility.** A genesis entry's asserted creation must precede the **ledger epoch** of the network admitting it. A post-epoch genesis is origin-laundering, and the log reports it the way IC-4 reports unaccounted mass.
>
> *Known residue:* a young network has a late epoch, so cross-network trade can launder through it. Same shape as floor-shopping, and it terminates in the same place — the receiving network re-derives origin under **its own** epoch and discounts what it cannot root (OP-14 counterparty re-computation).

**Attack B — citation laundering.** Fabricate an external citation and let an estimate enter on it.

> **Candidate IC-14 — citation closure.** Every estimate traces back to one of two valid termini: a **tally event inside the log**, or a **declared external citation**. An estimate with neither is **unsourced**, and the log reports it. Two termini for parcels, two termini for claims.
>
> *Mitigation, stated rather than assumed:* the citation must be **resolvable and independently re-runnable**, and Foundations §3.3a's **two unaffiliated replications** stand before any re-weight. Beyond that, §7.2a does the work — a fabricator cannot choose which sub-extent gets measured next.

<!-- tag: evt-s12-3a -->
### 12.3a Why both were rejected, and what replaces them

**Stress-test, 2026-08-22. Verdict: FAILS as integrity constraints.**

**IC-13 refuses the ordinary case.** A non-participant makes something in 2041 and sells it into a network founded in 2040. Its true creation is **after** that epoch, so an honest genesis entry would be *blocked* — and that is the normal onboarding path (Foundations §5.2), not an attack. A constraint that refuses the common case to catch the rare one fails universality.

**Epoch-shopping makes it toothless anyway.** Found a network today and *everything on Earth* predates its epoch. IC-13 is therefore satisfied trivially by the newest network, which is a fresh laundering licence per network — and networks are cheap to found. Worse, it **rewards founding networks and penalises joining one**, inverting the adoption incentive, and it stratifies goods by the age of the network that admitted them.

**Neither is arithmetic on the log, and that is the deeper objection.** IC-1…IC-9 check recorded quantities against *other recorded quantities*. IC-13 checks a **self-asserted date** against a constant; nothing in the log contradicts a launderer who writes "made in 2019". IC-14 demands *a* citation, not a true one. Both are plausibility filters wearing an integrity constraint's name — and shipping them as ICs would re-widen the §7.1 claim that this very fold had to narrow.

**Replacement for IC-13 — the author's ruling, 2026-08-22. A weighting rule, not a constraint, and the date disappears entirely.**

> **A good created at any time, in order to be transacted in the system, must show its logistical origin-chain record, and the seller must be onboarded.** Where no record or evidence of origin exists, **the cost is estimated exactly as all dark production is estimated** (Foundations §5.1b).

Two consequences do the work that a date test could not:

1. **The producer forfeits their efficiency.** A cohort estimate is by construction the *average* of the dark pool. Any producer who is genuinely better than that average — leaner process, shorter chain, cleaner energy — **cannot show a single unit of that advantage without records.** Efficiency becomes unbankable in the dark.
2. **The producer inherits the pool's pollution and waste.** The estimate carries the **averaged** pollution and waste of dark production, not their own. A clean producer with no records is charged as a dirty one.

**No date is checked, and nothing legitimate is refused.** Both requirements are already implied by existing machinery: origin-or-estimate is IC-3's two termini, and "the seller must be onboarded" is IC-5 — a parcel has exactly one holder, holders are `Account`s, and every change of holder is an event. **The ruling is a clarification of what the schema already required, not a new rule.** That is why it passes universality where IC-13 failed.

> **What genesis actually is, restated.** A genesis entry is not a special category of object defined by its age. It is **the dark-production estimate applied to origin** — the record you get when no chain is available. Predating the ledger is one *reason* a chain is unavailable, not a *rule* about what qualifies. IC-13's error was trying to promote the explanation into a gate.

**Two qualifications that must travel with this rule.**

- **Evidence is not instrumentation.** §4.1 admits `recalled` and `testified` as legitimate bases at Level 1. A low-tech producer supplies an origin chain at L1 basis and is fully served. Read as "instrument or be punished," the rule would fail universality; read as "show your chain at whatever basis you have," it does not. **Say so wherever this is stated.**
- **The transitional subsidy is real.** A producer *worse* than the dark average is better off staying dark, and is subsidised by the pool's better members. §5.1b's residual rule closes this over time — the average worsens as good producers leave — but it converges rather than biting immediately. **Name it as a transitional cost, not a hole.**

⚠️ **Owed: a sim** comparing stay-dark against onboard, for producers above and below the pool average, under §5.1b residual dynamics. The rule only holds if the estimate genuinely dominates for enough of the distribution, and the convergence speed is unmeasured.

**Where it belongs on fold:** Foundations §6.2a (with the front-loading rule) and §5.1b (as the origin case of the residual rule); EventLog §2.2's genesis paragraph.

**Replacement for IC-14 — a mandatory field, not a constraint.**

> **The §4.1a provenance block is mandatory on any estimated record.**

"Unsourced" then becomes a **malformed record refused at write time**, not a condition discovered by a checker afterwards, and §7.4's extent rule already reports what a verdict could see. IC-14 was redundant with machinery folded in the same version.

**What survives from the original worry.** A terminus the log cannot re-derive from its own bytes is still a soft spot. The answer is not to gate it but to **price it** — genesis and external citations are admissible, and both carry conservative estimates plus §3.3a's two unaffiliated replications before they can move history. That is the same answer the project gives everywhere else: *make the dishonest path cost more, rather than forbidding it at a door somebody has to guard.*

---

<!-- tag: evt-s13 -->
## 13. Open dependencies

C1 (event-log schema) cannot be finalized without external artifacts it does not itself define:

1. **Substance taxonomy** — versioned material identity. Build on an existing standard.
2. **Process taxonomy** — ⬆ **now load-bearing twice.** It keys retroactive hazard injection *and* the co-product allocation model (§7.1a). **The most underrated item on this list.**
3. **Role taxonomy** — must describe *what was done*, never rank.
4. **Reservoir registry** — fate closure (IC-4 (fate closure)) is only as good as this registry.
5. ~~**Amortization denominator**~~ — ✅ resolved (training front-loaded; no downstream flow).
6. **Confidence propagation rule** — how basis, confidence, and resolution combine along a parcel DAG. **Prerequisite for C3 (estimation engine) and C4 (re-weighting).** *Now also needs to cover allocated shares, whose confidence derives from process-energetics data quality rather than from the parent measurement alone (§4.1).*
7. **Conservative weighting of low-confidence flows** — **escalated again** (§12.2). C4, early.
8. ~~**Co-product allocation convention**~~ — ✅ **resolved.** Not a convention: the process performed the split and it is measurable (§7.1a, Foundations §3.4a). **Required no schema change.**
9. ~~**Pledge reversion target**~~ — ✅ **resolved (v0.7).** Pledges are permanent and unspent ones **burn** (§5.1a); nothing reverts, so there is no target to decide. Closes C5 (debit taxonomy) in the negative.
10. **Process-energetics model registry** *(new)* — the published per-process data that §7.1a's splits are computed from, plus the replication and rival-audit rules of Foundations §3.3a. **This is a new external dependency created by resolving item 8, and it is where OP-24 (understatement drift) lives.**
11. **Labour allocation convention across co-products** *(new)* — §6.1. **This is OP-18 (labour & team credit), and it is what now blocks C3.**

Items 1–4 are ordinary standards work. **Items 6, 7, 9, 10 and 11 are theory work. Item 11 is the blocking one.**

---

---

<!-- tag: evt-changelog-pointer -->
## Change history

The version-by-version change log (former §14) now lives in a separate file, read only when needed: **[`Aequitas_EventLog_CHANGELOG.md`](Aequitas_EventLog_CHANGELOG.md)**.

---

*End of v0.6.*
