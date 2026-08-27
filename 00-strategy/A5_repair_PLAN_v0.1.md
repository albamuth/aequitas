# A5 Repair — Plan

> **Status:** ✅ **Approved 2026-08-24.** All three decisions taken — see §6. Implementation in progress per §7.
> **Date:** 2026-08-24
> **Trigger:** outside-critique finding **#3** (economist, deepseek) — [`07-outreach/critique/REPORT_v0.1.md`](../07-outreach/critique/REPORT_v0.1.md).
> **One-line result:** *The §4.5/OP-23 ruling stands. **A5 was the malformed part**, and repairing its wording removes the contradiction without touching the ruling.*

---

## 1. The finding, and my own pass on it

### What the critic said

§4.5 rules that a durable asset's creation-cost sits on the asset and **never** allocates to the co-products. So beef carries none of the barn. But A5 reads *"the **price** of anything is its true, current-best-estimate material cost."* If the barn is not in beef's debit-cost, **beef's price is not beef's cost**, and A5 fails.

Their numbers: barn **20,000 h**, 20-year life, **2,000 kg** beef/yr → 40,000 kg over the life → the barn is **0.5 h/kg** of "true cost" that Aequitas shows as **0**.

### Why the ruling survives, in axiom terms

**The critic's step is to say the beef *caused* the barn. It did not.** Under **A1**, cost attaches to whoever **acted** — Ellerman's responsibility imputation. The barn was caused by the people who built it and is carried by the people who hold it. **A thing cannot act, so a thing cannot cause a cost.**

Charging the barn to the beef is the same move as charging the miner's tailings to the person who buys the ring — and **§3.2b already forbids that in one direction, §4.5 already forbids it in the other** (the non-cascade rule, stated in Foundations as *"cost never flows to whoever did not cause it"*). The capital case is the third face of one rule that is already written down twice.

> **So the contradiction is real, and it points the other way.** A5's wording says a cost lands on the *thing*. A1, §3.2b and §4.5 say a cost lands on the *causer*. **Two axioms cannot both be right, and the one that is out of step is A5.**

### What was actually wrong with the wording

Three defects, in order of size:

| # | Defect | Consequence |
|---|---|---|
| 1 | **It says "price."** Nothing in Aequitas has a price. Things have a **debit-cost**, and it is a dated reading. | Invites exactly this attack, and every reader who arrives from economics starts in the wrong frame. |
| 2 | **It never says what counts as a cost of the thing.** "Its true material cost" is silent on whether a barn used to make beef is a cost *of beef*. | The capital boundary lives in §4.5 and was never lifted into the axiom, so the axiom reads as contradicting it. |
| 3 | **"true" reads as final.** | Fights §3.3 and A6, which say every figure re-weighs when the science improves. |

### What I looked for and did not find

An adversarial pass on the repaired axiom. Four attacks, all closed by machinery that already exists:

| Attack | Closed by |
|---|---|
| **The capital launderer** — reclassify a used-up input as a durable asset to move its debit off the unit | **§4.5's physical-fate test** + **IC-4 (fate closure)**. Does the thing survive the process? Audited, never declared. Named and closed in v0.5. |
| **The borrowed barn** — A builds it, B uses it, so B's beef looks cheap | **§4.5 holding-time.** B holding it accrues B's share. And there is no rent to charge (§5.1). |
| **Scarcity re-entering cost** — price the rare cut higher | *Strengthened.* The repaired A5 says cost is a record of physical inputs and outputs, so desirability has no way in. The tenderloin ruling (§3.4a, B9) gets a cleaner ground than it had. |
| **A4 is being carved out** | No. **A4 says every cost lands on a ledger, not that it lands on the product's ledger.** GLOSSARY already words A4 that way; Foundations does not (see §5, flagged item). |

### The one real residue — and it must be written down

**Two producers of the same good, one with a 20,000 h barn and one with a 2,000 h shed, publish the same per-kg debit-cost.** A buyer comparing debit-costs cannot tell them apart.

This is not new — §4.5 already admits *"a per-unit debit-cost is not a full-lifecycle figure"* — but that one clause is too quiet to survive review, and **it is the half of the critic's point that is correct.**

**What disciplines the barn is the builder's own gate, not the price tag.** That reply has never been written down, which is why two models missed it. **This is the same shape as §5.2**, where pollution-debit was moved off the product onto the producer and the docs argue the producer-side penalty is *stronger* than a consumer-mediated one. The identical argument transfers, and §4.5 should carry it explicitly.

---

## 2. The two worked examples the documents need

CLAUDE.md requires a worked example with digits wherever a mechanism is explained. These are the two.

### 2a. Where the barn actually is — the critic's own numbers

- Barn creation-cost **20,000 h**, 20-year life. Beef **2,000 kg/yr → 40,000 kg** over the life.
- Beef's debit-cost carries feed, water, vet supplies, and the farmer's hours. Say the measured figure is **12.0 h/kg**. **The barn adds 0.0 h/kg.**
- **The 20,000 h did not vanish.** It is on the barn, holding-time-split. One operator holding it the whole 20 years carries **20,000 h**, permanently. Two operators at 10 years each carry **10,000 h** each.
- **What that does to them.** The gate is `D ≤ ρ·C`. At **ρ = 1.2**, carrying 20,000 h of extra debit needs `20,000 ÷ 1.2 = 16,667 h` of credit behind it. At the **3,650 h/yr** every living person accrues from self-care alone, that is **4.6 years of one person's entire credit accrual**, spent on the barn. **That is why nobody builds a barn they do not need.**
- **Now push it onto the beef instead.** Beef goes from 12.0 to **12.5 h/kg** — a **4.2%** rise — and **20,000 h moves off the one operator and onto roughly 40,000 separate buyers**, at about **0.5 h each**. The buyers did not build the barn, do not hold it, and cannot decide whether it gets built. **The party that decides is the only party the cost stops constraining.**

### 2b. The household cleaner — why capital-on-product would kill the incentive

A co-op makes a cleaner. It sells **5,000,000 bottles** over 8 years at **0.20 h/bottle**. Years later, its wastewater is found to be heating a local fishery. Abatement plant plus fishery remediation: **400,000 h**.

**If capital rode the product:**
- `400,000 ÷ 5,000,000 = 0.08 h` added to every bottle, **including the ones already sold**, because §3.3 re-weighs every affected record when the figure changes.
- Each past bottle's debit rises **40%** (0.20 → 0.28 h). A household that bought 200 bottles takes on **16 h of new debit** for a decision a factory made.
- **And the builder knows this in advance.** Any capital cost they incur lands on people who already bought and people who have not bought yet. **The cheapest siting decision is always someone else's problem.**

**Under the ruling as written:**
- The **400,000 h sits on the co-op's holders.** At ρ = 1.2 they need **333,333 h** of credit behind it. A 50-person co-op accruing 3,650 h/yr each earns **182,500 h/yr**, so the abatement absorbs **about 1.8 years of the entire co-op's credit accrual.**
- **Every buyer's ledger stays exactly where it was.**
- Separately, the thermal harm itself was **always** the factory's, and never rode the bottle either — that is **§3.2b**, unchanged since v0.5.

> **The incentive to scrutinise the factory design before building it exists only in the second version.**

---

## 3. Proposed replacement text for A5

Two changes to the author's draft, both argued:

**(i) Keep "no profit in exchange" inside the axiom.** The draft drops it. **It is the most-cited half of A5** — §5.1 (no surplus to appropriate), §3.3a (no profit to fund captured science), §4.8 (Aequitas costs, money prices), OA7/P4 (the employer is hollowed out), B8, OP-9. It is arguably derivable from A1 (a margin is not matter, so there is no field to write it in), but **making a dozen citations depend on a derivation the reader has to perform is how the first defect happened.** Say it.

**(ii) Anchor the boundary on *consumed vs survived*, not on "directly."** "Directly" is undefined and a reviewer will ask what it excludes. **"What was used up in making the thing"** is the test §4.5 already states, and it is auditable through IC-4. Lifting the existing test into the axiom is what actually removes the contradiction.

Also: **debit, not "debt"** — the project's term.

### Draft

> ### A5 (cost, not price)
>
> **A thing's cost is the current best estimate of what was materially consumed to make it. Nothing is added to that figure, and nothing enters it that the thing did not consume.**
>
> **Whoever takes a thing, or receives a service, takes on a debit equal to that figure. There is no profit in exchange — only debit discharged and debit acquired.**
>
> **The boundary is physical fate: what was used up making the thing is in its cost; what survived the process is not** (§4.5). A durable asset holds its own creation-cost, carried by its holders (§4.5), and that cost never enters the things the asset was used to make.
>
> **This is not an exemption from A4 (no externalities).** Every cost still lands on a ledger. It is **A1's imputation rule applied to cost**: a cost attaches to whoever caused it, and **a thing causes nothing** — only people act. Charging a buyer for the barn is the same error as charging them for the miner's tailings, which §3.2b already refuses.
>
> **The estimate is never final.** Better measurement re-weighs it, and every record made under it, automatically (A6, §3.3). **A cost is a dated reading, not a verdict.**
>
> Competition happens on **quality, artfulness, and efficiency**, never on margin.

### On the name

| Option | For | Against |
|---|---|---|
| **A5 (cost, not price)** ← *recommended* | Names the correction; kills the word that caused the attack; pairs against §0's *"a theory of cost, not of value."* | — |
| **A5 (cost is what was consumed)** | Most descriptive of the actual rule and of the capital fix. | Longer as an inline gloss, and it appears ~41 times. |
| **A5 (true cost is a work in progress)** *(author's draft)* | True, and readable. | **It names the least load-bearing clause.** Revisability is already **A6**'s job and §3.3's mechanism; naming A5 after it duplicates A6 and hides both halves A5 is actually cited for. |

---

## 4. File-by-file change list

### Tier 1 — substantive

| File | `[MODIFY]` | What |
|---|---|---|
| `00-strategy/Aequitas_Foundations_v0.22.md` | new version | **§1 A5 replaced** (§3 above). **§4.5 gains a boxed explainer** — *"Why the barn is not in the beef"* — carrying **both worked examples** (§2) and the producer-gate reply. **§5.1** reworded off "price ≡ cost." **§9** conformance gains one row: *a unit's debit-cost carries only what that unit consumed; a durable asset is never amortised into it* (A5, §4.5, §4.5). |
| `00-strategy/Aequitas_Objections_v0.21.md` | new version | **B8 gains the A5 challenge and the reply** — B8 is the entry that declares OP-23 closed, so it is the entry that must now hold the defence. Status-board line updated. **Register the residue** (per-unit figure carries no capital signal) as a named, answered item rather than a silent trade-off. |
| `00-strategy/Aequitas_Overview_v0.18.md` | new version | Line 234 — *"prices are simply costs… you cannot mark up a measurement"* keeps its punch, gains one plain-language sentence on what is **not** in the number, with the barn in words and one number. |
| `00-strategy/OP-23_capital_and_pollution.md` | in place | New **§8 — the A5 challenge**, with the reply and both examples. **Plus a stale-text fix I found while reading it:** §2 step 1 still says pledges *"draw the creation-cost down first"* and that *"the pledger absorbs a share of the debit against their own debit-room."* **Foundations §4.5 says the opposite** — a pledge is a permanent **grant** of debit-room, the pledger's credit never moves, and the debit does not shrink (A1). Same family as report bug **#7**. |
| `00-strategy/GLOSSARY.md` | in place | A5 row: name and gloss. |
| `01-wiki/cost-not-price.md` | `[NEW]` | Replaces `price-equals-cost.md`, which teaches the malformed maxim as *"Status: settled."* Old page → `99-archive/`. |

### Tier 2 — mechanical gloss sweep

`A5 (price ≡ cost)` → the new name. **~41 occurrences**, all inline glosses, no argument changes:

| File | Count |
|---|---|
| `Aequitas_Objections` | 12 |
| `Aequitas_Foundations` | 11 |
| `OP-9_calculation_reply.md` | 7 |
| `OP-17_coproduct_allocation.md` | 3 |
| `GLOSSARY.md` · `OP-27_parallel_implementation.md` | 2 each |
| `OP-18` · `OP-23` · `OP-26` · `Aequitas_EventLog_v0.10.md` | 1 each |

### Tier 3 — wiki

**23 pages carry `[[price-equals-cost]]`** → `[[cost-not-price]]` (Q3: full sweep).

### Tier 4 — bookkeeping

Three `_CHANGELOG.md` files (Foundations, Objections, Overview) · `NEXT.md` · a `03-journal/2026-08-24.md` entry · archive the superseded versions to `99-archive/`.

---

## 5. What does **not** change — and one thing I am flagging

**Unchanged.** The §4.5 holding-time waterfall. B8's closure of OP-23. §4.5 front-loading. §3.2b non-transfer. The conformance list's substance. **No mechanism moves. This is a wording repair to an axiom, and it makes the existing mechanisms consistent rather than altering any of them.**

> ### ✅ Also being repaired — **A4 has the same defect** *(approved, Q2)*
>
> A4 currently reads: *"Every consequence of an activity is **priced into it**…"*
>
> **"Priced into it" is the same word and the same implication that broke A5** — that a cost rides the thing. GLOSSARY already states A4 correctly (*"Every cost lands on a ledger; nothing escapes"*); **Foundations does not.**
>
> A reviewer who accepts the new A5 will read A4 next and ask the identical question. **Recommend the same one-clause repair in the same pass:** *every consequence of an activity is accounted to whoever caused it — there is no "outside" of the accounting.* **Substance identical, and it is what §3.2b and §4.4 already do.**
>
> **✅ Approved 2026-08-24.** Folded in the same pass. **No mechanism moves** — §3.2b (pollution stays on its causer), §4.4 (the residual is held, not allocated) and §4.5 (no upstream regress) are all already doing exactly what the repaired wording says.

---

## 6. Decisions needed before I start

**✅ All three decided by the author, 2026-08-24.**

| Q | Question | **Ruling** |
|---|---|---|
| **Q1** | A5's name | ✅ **A5 (cost, not price)** |
| **Q2** | Repair A4's *"priced into it"* in the same pass? | ✅ **Yes.** A4 becomes *accounted to whoever caused it*. Substance identical — it is what §3.2b and §4.4 already do, and it is how GLOSSARY already words A4. |
| **Q3** | The wiki page `price-equals-cost.md` | ✅ **Full rename and sweep.** New page `01-wiki/cost-not-price.md`; all **23** linking pages updated; the old page moves to `99-archive/`. Cleanest end state, and it matches *one concept per file*. |

**Not asked, because they are mine to make:** the boxed explainer goes in Foundations §4.5 (house style, and CLAUDE.md requires the worked example beside the mechanism); both examples use the critic's own numbers so the reply is checkable against the attack.

---

## 7. Order of work, once approved

1. Foundations v0.21 — A5, the §4.5 box, §5.1, §9. *(the argument)*
2. Objections v0.20 — B8 reply + status board + the registered residue. *(the record)*
3. OP-23 §8 + the stale-pledge fix. *(the full paper)*
4. Overview v0.16 + GLOSSARY. *(the plain-language layer)*
5. Tier-2 gloss sweep. *(mechanical)*
6. Wiki. *(per Q3)*
7. CHANGELOGs, `NEXT.md`, journal, archive.

**Steps 1–3 are one sitting. 4–7 are a second.**

---

*End of plan v0.1.*
