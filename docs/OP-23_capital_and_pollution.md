# OP-23 — Capital, Historical Costs, and the Non-Transfer of Pollution

> **Status:** Resolved 2026-08-04. Closes **OP-23** (shared-overhead attribution).
> **Feeds:** Foundations v0.4 → v0.5, Objections v0.5 → v0.6.
> **Method:** design interview → stress-test (capital front-loading) → stress-test (the full capital-debit waterfall) → adopted with changes.
> **One-line result:** *Historical costs do not cascade downstream; durable capital is front-loaded and holding-time-split; pollution is permanent on its causer and never transfers.*

---

## 0. The problem

Capital and historical costs cannot flow downstream into a product or service. If the construction of a hospital had to be amortized into each patient's bill, the accounting would have to chase the construction company's costs, the equipment manufacturer's costs, the doctors' education, and so on — **an infinite regress back to the first human activity.** The accounting would never terminate.

Yet the hospital plainly *has* costs: daily energy, per-patient supplies, wear on the building. These are real and must land somewhere. The task was to draw the line between what flows downstream and what does not — **without inventing an ad-hoc rule, and without leaking any debit.**

---

## 1. The boundary rule — capital vs. consumption, not temporal

> **A cost flows to a unit only if it is *consumed* in producing that unit. A durable asset's *acquisition* is capital; only what it *consumes now* — energy, materials used up, wear — is a flow.**

The naïve boundary is temporal ("costs incurred during production"). That is wrong: a machine bought last year is used across ten thousand units. The correct axis is **capital (a surviving asset) vs. consumption (used up)**, and the two are told apart by **physical fate** — does the thing still exist after the process? A drill bit that survives is capital; the oil it burned is consumption. Auditable via EventLog IC-4 (fate closure), not by the producer's declaration — which closes the *consumption-launderer* exploit (reclassifying a used-up input as capital to move its debit off the unit).

**Why this makes the accounting terminate.** You never chase an asset's own history. The asset carries whatever creation-cost is *knowable within Aequitas*; everything upstream of that is out of scope by construction. This is the same computational-closure cutoff that A2 already applies to training (front-loaded, never amortized downstream) — now generalized to all durable capital.

**Corollary — pre-Aequitas assets.** A hospital cooperative taking over a 50-year-old building cannot reconstruct the architects' fees or the original currency costs. The asset therefore *enters* Aequitas at an estimated or zero creation-cost and accrues history from genesis forward. The pre-genesis past is unrecoverable, exactly as the deep historical regress is.

---

## 2. The capital-debit waterfall

A durable asset (building, plant, tooling) holds its own **creation-cost as property-debit on the asset itself** — property-debit legitimately attaches to objects (Foundations §3.2), so this is A1-clean.

1. **Community pledges draw the creation-cost down first.** A pledge is *costly*: the pledger absorbs a share of the debit against their own debit-room. Pledges are simultaneously the **construction authorization** and the **demand brake** — a facility gets built at the scale the community will pledge for. (Hospital: 100k creation-cost − 50k pledged = 50k residual.)
2. **The un-pledged residual is holding-time-split among the asset's holders.** Each holder's permanent share = **their holding-duration ÷ total holding-duration over the asset's whole life.**
3. **The basic-needs floor caps how hard any residual bites** (Foundations §7.5).

**Why holding-time-split, and why it beats an even split.** It has a *measurable* basis — holding-duration is a physical trace — so it is far closer to a measured allocation than a bare convention, and it passes the cooperative-game checklist an even split fails:

- **Dummy:** zero holding-time → zero share. A brand-new hire bears ≈0, killing the *entry-toll* that an even split imposes on capital-intensive essential work.
- **Symmetry:** equal holding-time → equal share.
- **Progressive, re-weighting, final only at disposal.** While the asset lives, past holders' shares *dilute* as new holding-time accrues; shares freeze at disposal. This is A6 working exactly as designed — the not-yet-attributed remainder rides the asset until its life completes. **No leak.**

**Worked example.** A holds a thing 1 year, gives it to B, B uses it 1 year, then it is disposed. Total lifetime = 2 holder-years → **each holds 50% of the creation-cost, forever.** For a multi-staff facility the denominator is *holder-years across all concurrent staff*, so individual shares dilute hard: a 30-year veteran among ~200 staff over a 60-year facility holds ≈0.25%, not a crushing slab. A solo owner-operator of expensive private capital holds a large share — which is correct; they solely used it.

**Private durable goods** (no pledges) simply holding-time-split their full creation-cost across successive owners.

**This closes OP-23.** Shared overhead never allocates to co-products at all — the barn stays on the operator/asset as property-debit; hide and beef carry only their own consumables. There is no overhead-allocation convention anywhere. (Trade-off, stated honestly: a per-unit debit-cost is therefore *not* a full-lifecycle figure. The capital footprint is not lost — it sits on the asset and its holders — merely located there rather than smeared across units.)

---

## 3. Wear, transport, and the non-transfer of pollution

### 3.1 Wear → the asset
All wear, weathering and usage abrasion alike, accrues to the asset as property-debit and is settled at transfer or recycling. Products carry only true consumables (energy, materials used up). This is what lets OP-23 close.

### 3.2 The unified transfer rule *(the load-bearing result)*

> **Only property-debit — the embodied material you hold — transfers with an item. All pollution-debit and all transport/energy-consumption debit is permanent on whoever caused it and never transfers. Provenance records travel; the debit does not.**

- The farmer keeps the pollution-debt of the fertilizer runoff — **not** the person who buys the groceries.
- The gold mine is indebted by the mining process — **not** the owner of the jewelry.
- Transport fuel and its pollution stay on whoever caused the journey (the factory for inbound logistics, the consumer for final delivery), permanently, and cannot be shed by reselling the item.

**Why this is right under A1.** Ellerman's responsibility-imputation: only the miner *acted* to pollute; the buyer did not cause the mining. Charging the buyer would misattribute responsibility. This is also just Foundations §3.2's existing two-kinds-of-debit distinction taken to its conclusion — pollution/consumption debit is the *permanent* kind, so it stays on its causer; property debit is the *transferable* kind, so it rides the object.

**Why the incentive survives.** §7.2 previously located the anti-pollution gradient on the *consumer* ("dirty products cost more"). Under this rule the penalty is **direct and on the producer**: a polluter carries permanent pollution-debt, a poor efficiency ratio, and restricted discretionary consumption — regardless of whether any consumer notices. That is *stronger* than a consumer-mediated signal, which is historically weak. And the consumer signal is **not lost**: §5.1b already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**, letting buyers and pledgers still prefer low-pollution goods. Both channels operate; only the *debit* is pinned to the causer.

---

## 4. End-of-life, recycling, and the pollution baseline

### 4.1 End-of-life is consumption if unwanted
There is no right to force an unwanted asset (and its debit) onto anyone — custody is *accepted*, not imposed. But whoever **does** accept an object accepts its full transferable debit; you cannot take the object and refuse the debit. If nobody will accept a worn-out asset, its last holder has **consumed** it and holds its end-of-life debit forever, as if it were food. Recyclers are **credited** for reducing pollutants.

> **Axiom phrasing fix (carried into §3.2 / OP-17):** "custody follows possession, no right to refuse a transfer" must read as *no right to accept an object but refuse its debit* — **not** "no right to decline receiving an object." The latter reading would enable garbage-dumping, the exact abuse the rule exists to prevent.

### 4.2 Trace-forward, corrected
The **material** of a recycled object carries its accumulated *property*-debit forward (the atoms physically carried forward — Foundations §3.4a). It does **not** carry prior producers' *process-pollution*, because — per §3.2 above — that pollution never transferred; it stayed permanently on each producer. What a discarded product *does* generate is a **new** pollution-debt: a non-functional product sitting in the environment **is** a pollutant for as long as it persists, borne by its final holder. Recycling or remediating it discharges that end-of-life debt and lowers every future unit's burden. This resolves the perverse-incentive worry: recycled material is cleanly lower-burden than virgin because it never carried mining pollution and it avoids commissioning new extraction.

### 4.3 The pollution baseline — natural-remediation equilibrium
> **A flow is a *pollutant* only above the rate at which the natural world remediates it unaided.**

Steel produced only as fast as old steel rusts back to iron-oxide dust is in equilibrium and is not a pollutant. CO₂ emitted only as fast as the planet absorbs it (stable ppm, no warming) is at baseline and is not a pollutant. A compostable container carries no material pollution-debt, because it dissolves without human intervention in reasonable time.

**Pollution-debt weight is stock-dependent.** It floats with the ambient stock of the pollutant *above baseline*: more excess raises the estimated human-time to remediate, so every historical record of that pollutant re-weights **up**; drawdown re-weights them **down**. This unifies solid waste and atmospheric CO₂ under **one** mechanism, and it makes collective remediation individually rational — cleaning the commons retroactively lightens every holder's own pollution-debt.

The interpretation adopted for the per-unit weight is **total remediation** (removal *plus* the escalating nonlinear damage a unit does while resident), not removal cost alone — which is why the weight rises, not falls, with concentration.

---

## 5. Governance of the new constants

The **equilibrium baseline** and the **ambient-stock measurement** are powerful new cost-constants: whoever sets them moves every pollution record in history. They go under **§3.3a rival-sector audit** — two unaffiliated replications before re-weighting history, triage by magnitude × beneficiary concentration, and a network concentrated in the sector it audits is captured by construction. This is **OP-24** (understatement drift) with a larger lever, not a new mechanism.

---

## 6. Stress-test verdict

**PASSES WITH CHANGES**, twice. The first pass (capital front-loading) surfaced the public-goods provisioning problem and the consumption-launderer, both answered. The second pass (the waterfall) **broke the even-split residual** — it leaked the build-brake and imposed a perverse entry-toll on essential work — and the fix was the holding-time split above. Exploits checked: over-builder (stopped by pledge-coverage-as-authorization), staff-flight (stopped by holding-time dilution + floor), stock-understater (routed to §3.3a), quick-flipper/hot-potato (tracks actual use; robust). Axioms: A1 clean (debit relocated, never vanished), A2 clean (no rate-scaling), A4 clean (no consequence unaccounted — only relocated), A5/A6 clean.

**Remaining open:** illicit end-of-life *dumping/abandonment* enforcement is a Level-2 trust question — registered as **OP-25**.

---

## 7. What this resolves

| Item | Before | After |
|---|---|---|
| **OP-23** shared overhead | Interim inherited-proportions convention | **Closed** — overhead → asset, never allocated to co-products |
| **Capital / historical costs** | Undefined; regress risk | Front-loaded; boundary = capital vs. consumption; pre-Aequitas assets enter at estimate/zero |
| **Idea #1** capital as investment | Parking-lot bet | Landed — pledges + holding-time-split |
| **Idea #2** stock re-weighting | Sketch | Landed & unified with recycling; baseline defined |
| **Pollution attribution** | §3.2 implied it rode the product | Permanent on causer; only property-debit transfers; §7.2 rewritten |
| **Recycling / end-of-life** | Unspecified | Trace-forward (material only) + product-as-waste + recycler credit |
| Team even-split (this session's #2) | Proposed | Superseded by holding-time-split |

---

*End of OP-23 resolution note.*
