# OP-23 — Capital, Historical Costs, and the Non-Transfer of Pollution

> **Status:** Resolved 2026-08-04. Closes **OP-23** (shared-overhead attribution). **Re-attacked from outside 2026-08-24 and held — see §8.**
> **Feeds:** Foundations v0.4 → v0.5, Objections v0.5 → v0.6. **§8 feeds Foundations v0.21 (A4 + A5 repaired) and Objections v0.20 (B8).**
> **Method:** design interview → stress-test (capital front-loading) → stress-test (the full capital-debit waterfall) → adopted with changes.
> **One-line result:** *Historical costs do not cascade downstream; durable capital is front-loaded and holding-time-split; pollution is permanent on its causer and never transfers.*

> **⚠️ Note, 2026-09-04. §8 below quotes a wording of A4 that has since been withdrawn.**
> <!-- struck-ok: a dated note naming the withdrawn wording it is warning about -->
> **§8 says A4 requires every cost to land on *a* ledger.** That is true of the barn and false of the coverage residual, which lands on **no** ledger at all. **A4 now asks coverage and attribution separately**, and where causation is unresolved the consequence is held explicitly unassigned until an attribution witness exists — Foundations v0.39 A4, §2.2, §4.4.
> **This paper's ruling is unaffected**, because the attribution half is what carried it. Found by @cairn-lineage; see Objections **B15**. **The text below is left as the record of what was folded when.**

---

## 0. The problem

Capital and historical costs cannot flow downstream into a product or service. If the construction of a hospital had to be amortized into each patient's bill, the accounting would have to chase the construction company's costs, the equipment manufacturer's costs, the doctors' education, and so on — **an infinite regress back to the first human activity.** The accounting would never terminate.

Yet the hospital plainly *has* costs: daily energy, per-patient supplies, wear on the building. These are real and must land somewhere. The task was to draw the line between what flows downstream and what does not — **without inventing an ad-hoc rule, and without leaking any debit.**

---

## 1. The boundary rule — capital vs. consumption, not temporal

> **A cost flows to a unit only if it is *consumed* in producing that unit. A durable asset's *acquisition* is capital; only what it *consumes now* — energy, materials used up, wear — is a flow.**

The naïve boundary is temporal ("costs incurred during production"). That is wrong: a machine bought last year is used across ten thousand units. The correct axis is **capital (a surviving asset) vs. consumption (used up)**, and the two are told apart by **physical fate** — does the thing still exist after the process? A drill bit that survives is capital; the oil it burned is consumption. Auditable via conformance row 7 (fate closure), not by the producer's declaration — which closes the *consumption-launderer* exploit (reclassifying a used-up input as capital to move its debit off the unit).

**Why this makes the accounting terminate.** You never chase an asset's own history. The asset carries whatever creation-cost is *knowable within Aequitas*; everything upstream of that is out of scope by construction. This is the same computational-closure cutoff that A2 already applies to training (front-loaded, never amortized downstream) — now generalized to all durable capital.

**Corollary — pre-Aequitas assets.** A hospital cooperative taking over a 50-year-old building cannot reconstruct the architects' fees or the original currency costs. The asset therefore *enters* Aequitas at an estimated or zero creation-cost and accrues history from genesis forward. The pre-genesis past is unrecoverable, exactly as the deep historical regress is.

---

## 2. The capital-debit waterfall

A durable asset (building, plant, tooling) holds its own **creation-cost as property-debit on the asset itself** — property-debit legitimately attaches to objects (Foundations §3.2), so this is A1-clean.

1. **Community pledges grant the holders debit-room to carry the creation-cost.** A pledge is *costly to the pledger* — an hour pledged is spent for good from a finite lifetime pledging-budget — but it **does not draw the creation-cost down**: the pledger's own credit never moves and is never earmarked, and nothing is subtracted from the asset (**A1** — nothing vanishes). To the receiving cooperative it acts as **virtual credit**, defraying the *bite* of the fixed cost. Pledges are simultaneously the **construction authorization** and the **demand brake** — a facility gets built at the scale the community will pledge for. *(Hospital: a 100k creation-cost with 50k pledged **still sits at 100k on the asset** — but 50k of pledge-granted debit-room means only 50k of it effectively restricts the holders.)*
2. **The full creation-cost is holding-time-split among the asset's holders** — pledges cushion the bite, they do not shrink the debit. Each holder's permanent share = **their holding-duration ÷ total holding-duration over the asset's whole life.** Because pledges are **permanent and non-revocable** (Foundations §4.6), the granted room cannot evaporate under a holder, which is what lets a cooperative undertake capital-heavy essential work at all.
3. **The basic-needs floor caps how hard any residual bites** (Foundations §5.5).

> **⚠️ Corrected 2026-08-24.** Steps 1 and 2 previously read *"pledges draw the creation-cost down first"*, *"the pledger absorbs a share of the debit against their own debit-room"*, and *"the **un-pledged residual** is holding-time-split."* **All three were superseded by Foundations §4.5 and this paper was never updated** — same family as the pledge-permanence contradiction found by outside review (report bug **#7**). The draw-down reading breaks **A1** (debit would vanish) and contradicts **§4.6** (a pledge does not move the pledger's credit).

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

**Why the incentive survives.** §5.2 previously located the anti-pollution gradient on the *consumer* ("dirty products cost more"). Under this rule the penalty is **direct and on the producer**: a polluter carries permanent pollution-debt, a poor efficiency ratio, and restricted discretionary consumption — regardless of whether any consumer notices. That is *stronger* than a consumer-mediated signal, which is historically weak. And the consumer signal is **not lost**: §4.4 already requires goods to carry origin records, so a non-transferable **provenance/footprint record travels with the product**, letting buyers and pledgers still prefer low-pollution goods. Both channels operate; only the *debit* is pinned to the causer.

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

**PASSES WITH CHANGES**, twice. The first pass (capital front-loading) surfaced the public-goods provisioning problem and the consumption-launderer, both answered. The second pass (the waterfall) **broke the even-split residual** — it leaked the build-brake and imposed a perverse entry-toll on essential work — and the fix was the holding-time split above. Exploits checked: over-builder (stopped by pledge-coverage-as-authorization), staff-flight (stopped by holding-time dilution + floor), stock-understater (routed to §3.3a), quick-flipper/hot-potato (tracks actual use; robust). Axioms: A1 clean (debit relocated, never vanished), A2 clean (no rate-scaling), A4 clean (no consequence unaccounted — only relocated), A6 clean. **A5 was scored "clean" here and that was wrong** — the ruling was clean, but A5's *wording* contradicted it, which an outside review found on 2026-08-24. **See §8.**

**Remaining open:** illicit end-of-life *dumping/abandonment* enforcement is a Level-2 trust question — registered as **OP-25**.

---

## 7. What this resolves

| Item | Before | After |
|---|---|---|
| **OP-23** shared overhead | Interim inherited-proportions convention | **Closed** — overhead → asset, never allocated to co-products |
| **Capital / historical costs** | Undefined; regress risk | Front-loaded; boundary = capital vs. consumption; pre-Aequitas assets enter at estimate/zero |
| **Idea #1** capital as investment | Parking-lot bet | Landed — pledges + holding-time-split |
| **Idea #2** stock re-weighting | Sketch | Landed & unified with recycling; baseline defined |
| **Pollution attribution** | §3.2 implied it rode the product | Permanent on causer; only property-debit transfers; §5.2 rewritten |
| **Recycling / end-of-life** | Unspecified | Trace-forward (material only) + product-as-waste + recycler credit |
| Team even-split (this session's #2) | Proposed | Superseded by holding-time-split |

---

## 8. The A5 challenge — *"if the barn is not in the beef, price is not cost"*

> **Raised:** 2026-08-24, outside-critique round, economist role, `deepseek/deepseek-v4-pro`. Finding **#3** of the outside-critique report, **held locally and not published**.
> **Verdict:** ✅ **The ruling holds. A5's wording was the broken part and has been repaired** (Foundations v0.21), together with the identical defect in **A4**. **No mechanism moved.**

### 8.1 The objection

§2 above rules that a durable asset's creation-cost never allocates to the co-products. Through Foundations v0.20, **A5** read:

> *"The **price** of anything is its true, current-best-estimate material cost."*

The critic put the two together:

| | |
|---|---|
| Barn creation-cost | **20,000 h** |
| Barn life | **20 years** |
| Beef output | **2,000 kg/yr → 40,000 kg** over the life |
| Barn's share of a kilogram, 20,000 ÷ 40,000 | **0.5 h/kg** |
| What Aequitas shows | **0.0 h/kg** |

**So the number a buyer sees is not the cost the unit caused, and A5 fails.**

**Why the existing answer did not close it.** Both this paper and register B8 said the cost is *"not lost — it is located on the asset."* **That answers where the debit lives, and the critic did not ask that.** Two independent models raised it, which is the evidence that the actual reply had never been written down anywhere.

### 8.2 The reply

> **The critic's step is to assume the beef caused the barn. It did not.**

Under **A1**, cost attaches to whoever **acted** — Ellerman's responsibility imputation. The barn was caused by the people who built it and is carried by the people who hold it. **A thing cannot act, so a thing cannot cause a cost.**

Charging the barn to the beef is the same move as charging the miner's tailings to whoever buys the ring. **§3.2 above already refuses that flow downstream. Foundations §4.5 already refuses it upstream** (the non-cascade / computational-closure rule). **Capital is the third face of one rule this project had already written down twice** — and A5, which located a cost on the *thing*, was the sentence out of step with all three.

**Three defects in the old wording, in order of size:**

| # | Defect | Consequence |
|---|---|---|
| 1 | **It said "price."** Nothing in Aequitas has a price; things carry a **debit-cost**, and it moves. | Puts every economist reader in the wrong frame on the first sentence, and invites exactly this attack. |
| 2 | **It never said what counts as a cost *of the thing*.** | The capital-vs-consumption boundary lived in §1 of this paper and in Foundations §4.5, and was never lifted into the axiom it appeared to contradict. |
| 3 | **"True" reads as final.** | Fights §3.3 and A6, which re-weigh every figure when the science improves. |

<!-- struck-ok: the record of the v0.21 repair; the wording it quotes was itself withdrawn on 2026-09-04, see the note at the top -->
**A4 carried the same defect** — *"every consequence of an activity is **priced into** it"* — and was repaired in the same pass to **accounted to whoever caused it**. That is what §3.2 above, Foundations §4.4 and §4.5 already do; **A4 requires every cost to land on *a* ledger, never on the *product's* ledger.**

### 8.3 Why the alternative is worse — the two worked cases

**Case A — where the 20,000 hours actually is.** One operator holding the barn for its whole life carries **20,000 h**, permanently. The gate is `D ≤ ρ·C`; at **ρ = 1.2** that needs `20,000 ÷ 1.2 =` **16,667 h** of credit behind it, which at the **3,650 h/yr** every living person accrues from self-care is **4.6 years of one person's entire credit accrual.** *That* is what stops a barn being built that nobody needs.

Push it onto the beef instead and 12.0 h/kg becomes 12.5 h/kg — a **4.2%** rise — while **20,000 h moves off one operator and onto ~40,000 buyers at ~0.5 h each.** The buyers did not build it, do not hold it, and had no say in whether it went up. **The only party who decided is the only party the cost stops constraining.**

**Case B — a cost discovered years later, which is the sharper one.** A co-op sells **5,000,000 bottles** of a cleaner over eight years at **0.20 h/bottle**. Its wastewater is then found to be heating a fishery; abatement plus remediation costs **400,000 h**.

- **If capital rode the product**, §3.3 re-weighs every affected record, **including bottles already bought**: `400,000 ÷ 5,000,000 =` **+0.08 h on every bottle ever sold**, a **40%** rise, so a household that bought 200 bottles takes on **16 h of new debit** for a decision a factory made. **And the builder knows in advance that this is where it lands.**
- **Under the ruling**, the 400,000 h sits on the co-op's holders — `400,000 ÷ 1.2 =` **333,333 h** of credit needed, against a 50-person co-op's **182,500 h/yr**, so **about 1.8 years of the whole co-op's credit accrual.** **No buyer's ledger moves.**

*(The heating of the fishery was **always** the factory's under §3.2 above and never rode the bottle either. The abatement plant is capital and stays under §2. Two different debits, both pointed at the factory.)*

> **The incentive to scrutinise the factory design *before* building it exists only in the second version.** That is the whole case for the ruling, and it had never been stated.

### 8.4 Exploits checked against the repaired axiom

| Attack | Closed by |
|---|---|
| **Capital launderer** — reclassify a consumed input as a durable asset to move its debit off the unit | **§1's physical-fate test + IC-4 (fate closure).** Audited, never declared. Closed in v0.5; unchanged. |
| **Borrowed barn** — A builds it, B uses it, so B's beef looks cheap | **§2 holding-time.** B's holding-time accrues B's share. And there is no rent to charge (Foundations §5.1). |
| **Scarcity re-entering cost** — price the rare cut higher | **Strengthened.** The repaired A5 says cost is a record of what was physically consumed, so desirability has no way in. The tenderloin ruling (Objections B9) gains a cleaner ground than it had. |
| **"A4 is being carved out"** | **No.** A4 requires every cost to land on **a** ledger, not the **product's** ledger — which is now what A4 says. <!-- struck-ok: the 2026-08-24 record; that wording was withdrawn 2026-09-04, see the note at the top --> |

### 8.5 The residue, stated rather than buried

> **Two producers of the same good — one with a 20,000-hour barn, one with a 2,000-hour shed — publish the same per-unit debit-cost.** A buyer comparing debit-costs cannot tell them apart, because that figure answers *"what did this unit consume?"* and never *"what does this producer's whole method cost?"*

§2 admitted this in half a sentence (*"not a full-lifecycle figure"*). **It is the half of the critic's point that is correct, and it now says so plainly.**

**The answer is that capital discipline runs through the builder's own gate, not the price tag** — the 4.6-years-of-credit figure in §8.3. **This is the same argument §3.2 already makes about pollution**, where the debit was likewise moved off the product onto the producer and this paper argues the producer-side penalty is *stronger* than a consumer-mediated one, because it does not depend on anyone noticing. **The argument transfers unchanged.**

**Registered** in Objections **B8** rather than left as a footnote.

---

## 9. Why property debit has two components — the record of the repair

*Moved here from Foundations §3.2 on 2026-08-28. The rule itself stays in Foundations; this is the account of the contradiction it resolved, which does not belong in a body paragraph.*

**The contradiction.** Foundations §3.2, as written in v0.5, said property debit *"releases entirely on transfer."* Foundations §4.5 said creation-cost is holding-time-permanent. **Both cannot be true of one quantity.**

**The resolution, and it is the rule Foundations now states:**

> **The material transfers with the atoms. The making is holding-time-split, and each holder's share is permanent.**

**This is consistent with A1 (materialism of cost)** — both components attach to the object — **but only one of them leaves when the object does.**

**Worked, with the numbers.** A house costs 500,000 hours to build. Someone holds it for ten years, then transfers it. **Once the next holder has held it for an equal span, roughly 250,000 hours remain on the seller's ledger** — their holding-time share, permanent. The atoms are entirely the new holder's from the moment of transfer.

---

*End of OP-23 resolution note.*
