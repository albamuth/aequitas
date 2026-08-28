# OP-17 — Co-Product Allocation: the process allocates itself

> **⚠️ The event-log paper was retired on 2026-08-28.** References to `EventLog §…` below are historical and no longer resolve. **The arithmetic constraints IC-1 to IC-12 are now conformance rows in [`Aequitas_Conformance_v0.8.md`](../Aequitas_Conformance_v0.8.md) §2**, which carries a label map; everything else it held is in Foundations. The archived paper is `99-archive/Aequitas_EventLog_v0.10.md`.


**Status:** ✅ **Resolved for the material/energy half. Two new problems spun out (OP-23, OP-24).**
**Version:** v3 — 2026-08-01 (v1 and v2 superseded same day, unreleased; see §10)
**Register:** `Aequitas_Objections_v0.5.md` — A1 / B7
**Research:** `GLOSSARY.md#src-joint-production-allocation-problem` · `GLOSSARY.md#src-auditor-independence`
**Amends:** Foundations §1.1 (row 1 **deleted**), §3.3, §3.4 (**narrowed**), §4, §10 · EventLog §7 (IC-10, IC-11, IC-12), §13
**Stress-tested:** 2026-08-01, verdict *passes with changes* — changes applied in this version.

---

## 0. The rule

> **A joint process's debit divides according to where the process itself physically sent its inputs. This is a measurement, not a convention.**
>
> The measuring instrument is whatever that process's own physics makes traceable — tissue-deposition energetics for an animal, process enthalpy for a refinery, the extraction curve for a CHP plant, mitigation cost for an emission. **These are not rival conventions to choose between. They are different instruments reading the same underlying quantity, which is hours of human time to produce or to mitigate (A2).**
>
> **The universal is the denominator, not the carrier.** Mass, joules, and tonnes of CO₂ are each correct in their own context and each reduce to hours downstream. Mass is used as an estimator only where composition is uniform enough that cost-per-gram is genuinely constant.
>
> **Human preference plays no part.** A hide's share does not change because leather is fashionable, exactly as manure's share does not change because nobody wants it.

**What the rule does not cover, and does not pretend to:** labour hours (§5) and shared overhead (§6). Both are stated as open problems rather than absorbed.

---

## 1. Why the literature could not reach this

The LCA and Sraffian literatures both searched for a **carrier quantity** — a property of the *outputs* by which cost could be apportioned. Mass, energy, exergy, area, price. Every candidate is right in some industries and a category error in others, which is why ISO 14044's hierarchy is [reported as frequently inapplicable](https://link.springer.com/article/10.1007/s11367-016-1161-2) and why practitioners fall through to market price.

**A carrier quantity is a property of the outputs. The allocation is a fact about the process.**

Aequitas can say this and they cannot, for one structural reason: **it has a universal denominator and they do not.** A1 and A2 fix the terminal unit as human time, and §3.3 already recomputes physical weights as science improves. So the question "mass or energy?" — which is unanswerable as posed — never has to be asked. Whichever is measurable in the case at hand is used, because both reduce to the same thing.

**This is the second time the project's own axioms already contained the answer to a problem imported from outside literature.** The first was A3 versus the circulation-failure class (Foundations §5.6). Worth recording as a working habit: **check the axioms before importing a solution.**

---

## 2. The rule derived

### 2.1 The process performs its own allocation

A steer is not a black box that mysteriously emits beef and leather. It is a metabolism, and metabolism is measured science: depositing a gram of protein, a gram of lipid, and a gram of mineralised bone have **different, measured energetic costs**, and the feed supplying that energy has a known debit-cost. Where the animal spent its inputs is a biological fact, not a human choice.

| Process | What performs the split | What is measured |
|---|---|---|
| **Steer** | The animal's metabolism | Energy of tissue deposition per gram, by tissue type ([NRC beef cattle energetics](https://nap.nationalacademies.org/catalog/19014/nutrient-requirements-of-beef-cattle-eighth-revised-edition)) |
| **Refinery** | Distillation and cracking thermodynamics | Enthalpy and hydrogen consumed per fraction, per cut point |
| **CHP plant** | The turbine's extraction curve | Measured heat/power trade-off at the operating point |
| **Emission** | Atmospheric chemistry + mitigation technology | Hours to remove a tonne at today's best method (§3.3) |

In none of these does a human choose a split. The accountant's job is **instrument selection and measurement**, which is what the verification ladder (Foundations §4) already governs.

### 2.2 🔴 Split per-dimension, before collapsing

Debit is stored as a **vector** of physical quantities and collapsed to a comparable scalar only on demand, via the weighting model.

> **The split must be computed on each dimension separately, on the vector, before any collapse.**

If the split were computed on the collapsed number, **whoever controls the weighting model would silently control every allocation in history** — OP-10, arriving through a side door. Splitting per-dimension makes the allocation **weighting-independent**: two communities running different weighting models compute the same split and disagree only about what it weighs, exactly as the record model requires of everything else.

This is a hard requirement, not an optimisation.

### 2.3 Mass is an estimator, not a rule

Where a joint output is **compositionally uniform**, cost per gram is genuinely constant and mass allocation is *correct* — not a compromise but the right arithmetic under a true premise. Splitting a homogeneous grain harvest by weight needs no apology.

Where composition varies, mass is the **low-resolution reading**: recorded at low confidence, superseded when better science arrives. **This is ordinary resolution behaviour** (Foundations §3.4 ¶1), not a special allocation regime — which is what makes mass safe to use. It stops being an arbitrary choice and becomes a stated approximation with a known direction of error.

### 2.4 Why negative values do not arise

Steedman's negative labour values come from inverting an unconstrained linear system. Nothing is inverted here. Each output's share is a **forward measurement** of energy and materials that physically went into it, and a physical deposition cannot be negative.

- **IC-10 — no allocated share is negative.** A computed negative is a measurement error or a misdrawn process boundary, never a commodity containing less than nothing.
- **IC-11 — allocated shares sum to exactly the process's recorded debit, per dimension.**

⚠️ **Honest limit, from the stress test:** IC-10 *asserts* non-negativity rather than deriving it. The claim that forward measurement cannot produce a negative is sound for a single process in isolation; it is **not yet proven for a recursive economy** where every input's own debit is itself a joint split. See §7.

### 2.5 Fate decides what an output *is*

Manure is the clean demonstration that a co-product's ledger character is not fixed at production:

| Fate | Ledger effect |
|---|---|
| **Lagoon / open storage** | Methane release → **pollution debit**, permanent, re-weighted with mitigation cost (§3.3) |
| **Biodigester** | A genuine co-product carrying its share of production cost; recovered energy is a real output |
| **Field rotation / spreading** | Displaces synthetic fertiliser — the avoided production is **observed, not counterfactual**, so the offset is a measurement |
| **Unmanaged runoff** | Pollution debit, on the holder, per A4 |

**Same substance, four ledger positions, decided by observed fate — not by a rule about manure.** Conformance row 7 (everything has a fate) already records this; no new machinery.

Generalised: **an output's cost share is set by the process; its ledger character is set by its fate.** The allocation literature conflates these two questions, which is part of why it goes in circles.

---

## 3. The three tests

### 3.1 Slaughterhouse ✅
Tissue-deposition energetics split the animal's accumulated feed, water, and care debit across muscle, fat, hide, and bone. Manure and enteric methane are outputs too, per §2.5. **Cuts are not differentiated by desirability** — tenderloin and shank differ only by measured deposition cost, if at all. Interim: mass, at low confidence, superseded when livestock energetics are loaded.

### 3.2 Oil refinery ✅
Cracking and hydrotreating energy attaches to the fractions that required it, from metered process data. Mass allocation would have loaded resid; the physics does not. Same justification, different instrument.

### 3.3 CHP plant ✅
The extraction-condensing curve is directly metered. Mass is inapplicable, and that is not a failure of the rule **because mass was never the rule** — it is one instrument among several. The turbine's own measured trade-off gives the split.

**One justification — the process's own physics. Three cases, three instruments. Not disqualified.**

---

## 4. The three criteria

| Criterion | Verdict |
|---|---|
| **Universality** | ✅ One rule, no domain condition, no per-industry exception. Instrument varies; justification does not. ⚠️ *Outcomes* still vary with instrumentation access — see §8. |
| **Decentralization** | ✅ **The rule's strongest property.** Metabolic and thermodynamic constants are published science, independently verifiable. **No objective function is required**, so this does not re-open OP-10 — which both the marginal-allocation and Kantorovich routes would have. ⚠️ A residual capture surface exists in *who publishes the constants* — see §7. |
| **Fecundity** | ✅ Every allocation is an open scientific question that better measurement improves, and §3.3 propagates improvements backwards through all history. Permanent demand for process science. |
| **Needs a Paul Glover?** | ✅ No. No board, no facilitator, no standards committee. |

---

## 5. 🔴 What this does not solve: labour

**The rule traces matter and energy. Labour leaves no physical trace to any individual co-product.**

The farmer's eight hours were spent on *the animal*, not on the hide. Splitting those hours by tissue-deposition energetics assumes labour was expended in proportion to metabolic energy, which is an assumption, not a measurement — the same unjustified proportional inheritance §6 flags for overhead, applied to the input the whole system is denominated in.

**So OP-17 resolves the material and energy half only. The labour half is genuinely joint, and it belongs to OP-18** — where Ellerman's argument already says joint responsibility is non-decomposable, and where hours-worked remains a *declared convention* in Foundations §1.1.

> **🔴 Consequence, and it changes the roadmap: C3 is no longer blocked on OP-17. It is blocked on OP-18.**
> C3 needs per-product **labour hours** — that is precisely the layer EXIOBASE carries and almost nobody else collects, and it is the layer this rule cannot split. The critical path moves.

This is stated rather than papered over because papering over it is exactly what §1.1 exists to prevent.

---

## 6. 🔴 What this does not solve: shared overhead → **OP-23**

First-order inputs decompose metabolically or thermodynamically. **Overhead does not.** The barn shelters the whole animal; the vet treats the whole animal; supervision covers the herd. There is no physical trace from the barn to the hide.

**Interim treatment** — derived rather than freshly invented:

> Overhead attaches to the **bundle** and flows to outputs in the proportions the traceable inputs already established.

No new convention is introduced; the split is inherited from a measurement. But this is weak, and two problems are known:

1. It presumes overhead is *caused* in the same proportion as feed. A hide requires no more barn than a kilogram of muscle does.
2. **In overhead-heavy processes the residue is not small.** A semiconductor fab's cleanroom and tooling dwarf its material inputs, so inheriting proportions from a tiny traceable base does nearly all the work. **The rule is strong for agriculture and process industry and thin for capital-intensive manufacturing**, and that gap must close before C3 covers those sectors.

**Registered as OP-23 — shared-overhead attribution.**

---

## 7. 🔴 Understatement drift → **OP-24**, and the fix

The stress test found a capture surface the rule does not close by itself, and the session then found that the obvious fix moves the bias rather than removing it.

**The surface.** Whoever publishes a process-energetics constant sets every split in that sector — and because §3.3 re-weights retroactively, capturing a constant re-splits all of history. Competing trust networks discipline *estimates* cheaply (re-interviewing a farmer is cheap) but not *constants* (re-running calorimetry is not). **Replication cost is asymmetric.**

**Why the classic funding-bias channel is nonetheless closed.** There is no market-dominating corporation to pay a lab for a favourable result. Labs are credited by trust networks, and A5 removes the profit that funds captured science today. **That is a genuine structural advantage over the status quo and should be claimed.**

**But the mirror problem is real.** A general-membership trust network is dominated by the *consuming* side — everyone consumes beef, few produce it. Its members therefore collectively benefit from beef's debit being **understated**. And the correction incentive is asymmetric in a way that makes this self-reinforcing:

| Error direction | Who wants it fixed | Outcome |
|---|---|---|
| Constant **overstates** debit | Every subscriber | Gets corrected |
| Constant **understates** debit | Nobody — correcting it makes every subscriber's ledger worse | **Nobody funds the calorimetry** |

**Result: systemic drift toward under-costing** — which is precisely how every carbon-accounting regime to date has failed. Foundations §3.5 tolerates it arithmetically (no global balance is required), but it **erodes A4 progressively**, and A4 is not optional.

### 7.1 The fix — rival-sector audit

> **The natural auditor of a cost constant is the rival sector, not the consumer.**

If beef's energetics are understated, plant-protein producers are **materially harmed** and will fund the replication. Consumers police neither direction; rivals police both.

Why this is the right shape for Aequitas:

- **Decentralized.** No authority, no standards body, no appointed reviewer. It is an incentive, not an enforcement rule.
- **Self-funding.** The replication is credited work paid for by a party with a real stake — it passes the fourth screening question ("does this need a Paul Glover?") without help.
- **Two-sided.** It converts a one-way asymmetry into a market. Every constant has a party who benefits from it being lower and a party who benefits from it being higher.
- **Already implied.** A5 removes profit *in exchange*; it does not remove **rivalry in efficiency**, which Foundations §5.1 explicitly preserves ("producers compete on quality, artfulness, and efficiency"). Rival-sector audit is that competition applied to the cost model itself.

**Supporting rules:**
1. **A constant must be replicated by two unaffiliated sources before it may re-weight history.** Retroactive re-weighting is powerful enough that a single-source constant should not trigger it.
2. **Audit triage is weighted by magnitude × concentration of beneficiary**, not magnitude alone. Materiality thresholds alone *help* an attacker, whose job becomes making a falsification look immaterial. Equal-magnitude constants are audited in order of who profits from the current value.
3. **A trust network whose membership is concentrated in the sector it audits is captured by construction.** Membership composition is public in the log, so this is a **detectable screening property**, not a rule anyone must enforce. General-membership networks are structurally sounder than sector-specific ones.

**Registered as OP-24 — understatement drift.** The fix above is proposed, not proven; it wants a simulation (§9).

### 7.2 Why the co-op framing does not by itself fix it
Considered and rejected during the session: *trust networks are co-ops funded by member pledges, so they have no profit motive to be lenient.* **The conflict is directional, not monetary.** [Arthur Andersen was paid by Enron](https://en.wikipedia.org/wiki/Arthur_Andersen); making Andersen a co-op *owned by its clients* would have been worse, not better. Removing the profit motive leaves the leniency motive intact. See `GLOSSARY.md#src-auditor-independence`.

---

## 8. Instrumentation, estimation, and who pays for vagueness

The stress test charged the rule with being **regressive**: a producer without meters falls back to mass, gets weighed conservatively, and pays more debit for the same physical activity. **The charge does not stand, for three reasons, and the residue is a watch item rather than a defect.**

**1. Admin labour is a real material cost, not a penalty.** A farmer without instruments genuinely needs more human hours to produce the same verified record. Charging those hours is A1 behaving correctly. The incentive to instrument is real and is the ordinary incentive to reduce a real cost — not a thumb on the scale.

**2. Nothing is irreversible.** Years later the number of cattle that left that farm will be known exactly, and every debit-cost that rested on a conservative weight recomputes — including on the ledgers of everyone who consumed the products. **This holds for all inaccuracy, not just allocation.** (Foundations §3.3.)

**3. Transient harm is bounded by the basic-needs floor.** Debit binds hard, so a multi-year over-assignment corrected later would otherwise be a real injustice — the shape of the [Post Office Horizon scandal](https://en.wikipedia.org/wiki/British_Post_Office_scandal), where accounting output was treated as fact and corrected two decades on. **Foundations §5.5 caps the exposure:** enforcement restricts non-essentials only, and the efficiency ratio may never reach essentials. The harm is *"cannot buy discretionary goods for a period, then corrected"* — not destitution.

**Estimating the un-instrumented.** For producers outside Aequitas, use the finest-resolution data that exists (the smallest region with published figures), per A7. **Seeking that data — interviewing the farmer, counting the herd — is credited trust-network work**, and the resulting estimate tables are independently re-testable by any other network.

> **🔴 Required correction to the cohort rule.** The average assigned to unmeasured producers must be computed over the **unmeasured residual only**:
>
> **average = (N − Y) / Z**, where *N* is the independently-known global total, *Y* the output of measured producers, *Z* the count of dark producers.
>
> Computed over the whole population instead, this creates **adverse selection**: better-than-average producers instrument to prove it, worse-than-average stay dark and free-ride on an average their own absence inflates. Over the residual, the estimate worsens as good producers exit, and **darkness stops paying.** *(This generalises Foundations §4.1, which already excludes registered participants from the cohort debit average — the same discipline now applies to production.)*
>
> **Two conditions:** it needs an independently known *N* (fine for cattle via FAO and trade data; not universal), and a defensible count *Z*. Under-counting *Z* over-states every dark producer's share.

**"Dark" means outside Aequitas, not low-tech inside it.** Participation carries a transparency requirement: a good moving through the Aequitas economy must carry records of its origin. Onboarding assistance — bringing a producer's logistics into the light — is trust-network work.

> **⚠️ Watch item, not a blocker: onboarding is a fixed-ish cost, and fixed costs consolidate.** Compliance regimes with per-entrant documentation burdens — [organic certification](https://www.ams.usda.gov/services/grants/occsp), [REACH](https://echa.europa.eu/regulations/reach/understanding-reach), [FSMA](https://www.fda.gov/food/guidance-regulation-food-and-dietary-supplements/food-safety-modernization-act-fsma) — are repeatedly argued to disadvantage small producers, which is why cost-share programmes exist. The offset here is that onboarding labour is **credited work borne by the network rather than the entrant**, which is the right shape. Whether it is sufficient is empirical. Watch it.

---

## 9. Tests this rule still owes

1. **Recursion convergence.** Every input's debit is itself a joint split, so the allocation is defined recursively with no proof it terminates or converges. **Test:** a sparse-matrix simulation over a synthetic joint-production economy, following [Cockshott & Cottrell's method](https://en.wikipedia.org/wiki/Towards_a_New_Socialism). **This is the sharpest surviving technical risk** — it is where Sraffa could re-enter, and it would falsify IC-10 as a derived property (§2.4).
2. **Understatement drift.** Simulate a population of trust networks with the incentive structure of §7 and measure whether rival-sector audit actually arrests the drift, and at what rival density it stops working.
3. **The fuzzy middle.** A hide-to-carcass ratio varies slightly by breed and feed. Does the rule behave sensibly at small derivatives, or degenerate? Needs real livestock data — [Mackenzie et al. on biophysical allocation in livestock](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) is the hardest published case.
4. **Refinery re-derivation.** Compute a refinery's slate under process-physics allocation and under USEEIO's price allocation, and compare. **A materially different answer is the most publishable technical result the project could produce.**

---

## 10. Consequence for C3

**USEEIO allocates by price. It is definitively unusable as a source of truth**, though still usable as data.

- Price-derived sector splits must be flagged **`declared` basis, never `measured`.** Best available, honestly labelled — §1.1's discipline applied to imported data.
- **EXIOBASE's physical layers remain sound.** Its embodied-labour-hours layer is now doubly important, because §5 hands the labour split to OP-18 and EXIOBASE is where that data lives.
- **Highest-value first targets: livestock and refining** — published process energetics, large sectors, and the sharpest contrast with price allocation.

---

## 11. Version history

**v1** proposed **Aumann–Shapley** marginal allocation for variable-proportion processes and a declared bilateral split for fixed-proportion ones. Discarded: it needed a domain condition ("is the plant dial-able?"), its fallback assumed a **right to refuse custody** that does not exist (possession decides), and without refusal that branch degenerated into demand-set allocation — **price in costume, violating A5**. It also searched for a carrier quantity and so inherited the literature's dead end.

**v2** replaced the carrier search with process-physics allocation but still treated debit as a scalar (fixed in §2.2), claimed OP-10 was fully closed (corrected in §7), and claimed to unblock C3 (corrected in §5).

**A demand-contingent split was considered and rejected.** Splitting by what people want makes two identical steers, processed identically in two towns, carry different splits — a universality failure, and OP-9 wearing OP-17's clothes.

**Load-bearing corrections came from the author, not the analysis:** that the universal is the denominator rather than the carrier; that unwanted outputs are co-products like any other; that "dark" means outside the system rather than low-tech within it; and the residual-only cohort average.
