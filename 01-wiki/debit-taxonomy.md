# Debit Taxonomy

> The master map of §3.2: **what kind of debit a thing carries, and how each kind behaves when the thing changes hands.** This is the engine room of the theory — most of what makes Aequitas different from money is a consequence of these distinctions. The reviewer (2026-08-09) flagged §3.2 as load-bearing but text-only; this is the visual.

![[debit-taxonomy.svg]]

*(If the diagram doesn't render, the same structure is in the tables below.)*

---

## The one thing to hold first: a debit is a vector

A debit is **not one number.** It is a bundle of physical quantities — kilograms of a substance, joules, labour-hours, cubic metres of water, land-area-years — stored separately and collapsed into a single comparable figure only when someone needs to compare two things, using the current [weighting model](retroactive-reweighting.md).

> **The load-bearing rule (§3.2a): any division of a debit — across co-products, across a team, across holders — happens per-dimension, *before* collapsing.** Divide the collapsed number instead and whoever maintains the weighting model silently controls every allocation in history. Divide per dimension and the split is weighting-independent. This closed a side entrance to [OP-10](protocol-governance.md).

---

## The two kinds, and the behaviour that separates them

| | **[Property debit](property-debit.md)** | **[Consumption / pollution debit](consumption-debit.md)** |
|---|---|---|
| **What it is** | The debit of a thing you currently hold | What you used up, emitted, or burned |
| **Term type** | *Current-holdings* — a snapshot of what you hold now | *Permanent-history* — locked into the record forever |
| **Attaches to** | The **object** | The **causer** (a person, permanently) |
| **On transfer** | See the split below | Never moves. Provenance travels; the debit doesn't |
| **Weight** | Fixed by what was made | **Floats** with ambient stock (§3.3) — more pollution out there ⇒ every past unit re-weights up |

### The third case the table above does not show: a thing that has not been used yet

**A can of petrol has polluted nothing.** Nobody has caused an emission, so there is no consumption debit to attach to anybody. **But burning it will emit, and the accounting has to hold that somewhere.**

> **A thing that will pollute when it is used carries that future pollution as part of its debit, in physical units, and it moves with the thing** (§3.2b).

**It is recorded at the hand-off rather than at the moment of use, because a purchase is an event the books see and a combustion mostly is not.** Sell the fuel on and it goes with the fuel. Burn it and it becomes ordinary consumption debit on the burner, permanently.

**Worked, with the numbers.** 40 litres of petrol, at about 2.31 kg of CO₂ a litre.

| | Stored in the log | Read off the ledger |
|---|---|---|
| At the hand-off | **40 litres** | 92.4 kg, at 0.05 h/kg → **4.62 h** |
| After a better capture method halves remediation | **still 40 litres** | **2.31 h** |
| Sold on to somebody else | the litres move | **0 h on the seller** |
| The refinery's own process emissions | on the refinery's log | **0 h on the buyer, ever** |

**This is the clearest case in the theory for why a debit is stored as a vector.** A system that had stored *4.62 hours* instead of *40 litres* could not have re-read itself when the science improved.

### Property debit has three components that behave differently

They are not the same quantity and they do not move together:

| Component | What it is | On transfer |
|---|---|---|
| **Embodied material** | The atoms you hold | 🟢 **Dischargeable.** Rides the object to the new holder; you are clear of it entirely. *(Effect: used goods enter cheap — the new holder has put in no time yet.)* |
| **Creation-cost / labour** | The hours that *made* the thing | 🔴 **Permanent per holder.** Holding-time split: your share = your holding-duration ÷ the asset's whole life. Dilutes as later holders accrue time, but **never zeroes**. Clock starts at **deployment**, not purchase; transit carriers accrue **none**. (§4.5) |
| **Latent pollution** | What the thing **will** emit when it is used | 🟡 **Rides the object, then locks.** Nobody has caused an emission yet, so it moves with the thing at every hand-off. **On use it converts into ordinary consumption debit, permanently, on whoever used it.** Recorded in litres or kilograms, never in hours. (§3.2b) |

**Worked case.** Hold a 500,000-hour house for 10 years, then pass it on. Once the next holder has held it an equal span, ≈250,000 hours of *making* is still on your books — the holding-time share, permanent. The *material* left with the house; the *making* did not. You cannot escape it through a non-participant either: with no record of a hand-off, the ledger still shows you holding it, so you keep the whole weight.

---

## Two rules that cut across both branches

**Self-work identity** → [self-work-identity](self-work-identity.md). While you hold a thing, working on it earns credit exactly equal to the property-debit it adds → **net zero** (bar materials used up). This is *why* property is a burden, not an engine: no rent, no appreciation, nothing earned by mere holding. Repair your own roof and you are credited the hours *and* the house's debit rises by the same hours — net effect on you, zero.

**Non-cascade** (§3.2b = §4.5, one rule read in two directions). **Cost attaches only to the causer and never cascades:**
- **not downstream** to a buyer — the miner keeps the tailings, not the person wearing the ring ([Ellerman responsibility-imputation](no-externalities.md));
- **not upstream** to the first human who ever built anything — an asset carries only the creation-cost knowable *within* Aequitas, and everything before genesis is out of scope (computational closure).

Either cascade breaks the books. This is the same constraint as the [[#The Front-Loading Rule|Front-Loading Rule]] below, seen from the ledger side.

**End of life** → [consumption-debit](consumption-debit.md). Refuse to pass a worn-out thing on and you have *consumed* it: its property-debit becomes your permanent consumption debit, as if you had eaten it. A discarded object is itself a pollutant for as long as it sits (§3.6).

---

## The Front-Loading Rule

*A named consolidation of §4.5 / §4.5 / §4.5 and objections B3 / B8 — the second thing §3.2 needs to be legible. Where the taxonomy above says how a cost **behaves**, this says **when it is paid and by whom**, for the one class of cost that would otherwise never terminate.*

> ### 🔒 THE FRONT-LOADING RULE
> **A large up-front cost with a diffuse benefit is carried when it is incurred, cushioned by the debit-room the people who pledged for it grant. It is never amortized downstream onto whoever happens to consume the result.**

**What it covers.** Four cases, one rule:

| Case | Front-loaded cost | What the eventual recipient pays |
|---|---|---|
| **Education** ([education-as-credited-work](education-as-credited-work.md)) | Teachers' time, facilities, materials | The professional's time, clinic materials, medicines — **not the education** |
| **Media / creative** | Years of crew time, sets, post-production | **Delivery only** — venue, projectionist, bandwidth, power |
| **Research · infrastructure · tooling** | The build | Use, wear, and energy |
| **Capital & overhead** ([property-debit](property-debit.md)) | The plant, the barn, the machinery | Only what a unit *consumes* now — never a slice of the building |

**Why downstream amortization is always wrong — two reasons:**

1. **The window is arbitrary.** Amortizing a hospital into patient-bills means choosing *how many patients* — and every candidate window is a guess. That arbitrariness *was* OP-11 (training) and OP-21 (media). Front-loading **removes the division** rather than solving it.
2. **Computational closure.** Chase a hospital's construction into each bill and you must chase the builder's costs, the steelmaker's, the engineers' schooling — **an infinite regress to the first human activity.** The sum never finishes. Front-loading is what makes the accounting *terminate*. *(This is the upstream face of non-cascade above.)*

**The boundary is capital vs. consumption — not time.** A cost flows to a unit only if it is *consumed* producing that unit. Told apart by **physical fate**: does the thing survive the process? A drill bit that survives is capital (front-loaded); the oil it burned is consumption (flows to the unit). Auditable via [IC-4 fate closure](event-record.md), not the producer's say-so — which closes the *consumption-launderer* who reclassifies a used-up input as capital.

**Who actually carries front-loaded capital — the waterfall (§4.5):**

1. **Community pledges grant the holders debit-room to carry it.** A [pledge](pledge-and-signal.md) does **not** draw the cost down: it is a *permanent grant of debit-room* — virtual credit conferred on the co-op, drawn from the pledger's finite lifetime pledging-budget; their credit itself never moves. It cushions the bite (and, being permanent, can be relied on rather than re-exposed by withdrawal), and doubles as the construction authorization *and* the demand brake — a facility is built at the scale the community will pledge for.
2. **The full cost is holding-time split** among the asset's holders (share = holding-duration ÷ total holder-years over its life) — pledges cushion the bite, they don't shrink the debit (nothing vanishes, [A1](material-flow-value.md)). Holding-duration is a [physical trace](physical-trace-test.md), so this is measured, not invented — and it passes the cooperative-game checklist an even split fails (**dummy:** a new hire bears ≈0, killing the entry-toll that would scare people off staffing hospitals; **symmetry;** progressive; final only at disposal).
3. **The [basic-needs floor](debit-tolerance.md) caps how hard any residual bites** (§5.5).

*A 30-year veteran among ~200 staff over a 60-year hospital holds ≈0.25% of it — not a crushing slab. A solo owner of expensive private capital holds a large share, correctly: they alone used it.*

**What it dissolved.** OP-11 (training amortization), OP-5 (education), OP-21 (media reproduction) — all one malformed question (B3). And OP-23 (shared overhead) — capital accrues to the asset and its holders and **never allocates to co-products**; the barn stays on the operator, hide and beef carry only their own consumables (B8).

**⚠️ Honest residues.**
- **Cold start.** Pledges follow reputation, so a first-time creator attracts none — the same wall unknown creators hit with capital today, lower (attention, not money) but real.
- **A per-unit debit-cost is therefore not a full-lifecycle figure.** The capital footprint sits on the asset, not smeared across units. It is never *lost* (no [A4](no-externalities.md) breach) — just located honestly.

---

## Depends on

- [material-flow-value](material-flow-value.md) · [non-fungibility](non-fungibility.md) · [cost-not-price](cost-not-price.md)

## Consequences

- [self-work-identity](self-work-identity.md) · [capitalism-cannot-function](capitalism-cannot-function.md) · [no-externalities](no-externalities.md) · [no-taxation](no-taxation.md)

## Open questions

- [OP-10](protocol-governance.md) — who controls the collapse (weighting) model
- C5 — consent/refusal on acquisition. *(Pledge reversion is **resolved**: pledges are permanent and non-revocable, and an unfulfilled pledge burns — nothing reverts. Foundations §4.6, [pledge-and-signal](pledge-and-signal.md).)*
- OP-25 — illicit dumping (escaping end-of-life debit by abandonment)

---
*Status: settled (tracks Foundations v0.20 §3.2, §3.2a, §3.2b, §4.5, §4.5, §4.5)*
*Source: highest-versioned `00-strategy/Aequitas_Foundations_v*.md`; objections B3, B8 in the current `Aequitas_Objections_v*.md`*
