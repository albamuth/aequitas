<!-- tag: obj-aequitas-objections-register -->
# Aequitas — Objections Register

> **Version:** 0.23 · **Date:** 2026-08-27
> **Tracks:** `Aequitas_Foundations_v0.28.md` · `Aequitas_Conformance_v0.7.md` · `OP-22_identity_not_disclosure_v0.2.md` · `OP-27_parallel_implementation.md` · `OP-26_coverage_and_closure.md` · `OP-18_labour_and_team_credit.md` · `OP-23_capital_and_pollution.md` · `OP-17_coproduct_allocation.md` · `06-simulation/allocation-engine/RECURSION_RESULTS.md` · `06-simulation/disparity-ceiling/DISPARITY_CEILING.md` · `06-simulation/pledge-reserve/pledge_reserve.py` · `06-simulation/scenario-suite/scenario_suite_METHOD.md`
> **Version history & what each version superseded:** `00-strategy/Aequitas_Objections_CHANGELOG.md`.
> **Purpose:** one place holding every serious objection to the theory, its source, the axiom it attacks, and its status.

**This register is now the only ranked list of open problems.** Foundations carried a summary of it as §10 from v0.1 to v0.23. **It was truncated on 2026-08-25 by author ruling** — a summary of the objections belongs here, not in the document that states the system. **Seven entries that existed only in Foundations §10 were folded into the status board below**, so nothing was lost: OP-2, OP-3, OP-4, OP-7, OP-8 (reframed), OP-14 and OP-15.

**Part B is not an archive.** It holds the objections that have been answered, and it is the most immediately useful section in the project — those are the arguments the academic paper is built from, and every one of them will be raised again by someone who has not read this. `99-archive/` holds superseded *document versions*; an answered objection is not superseded, it is ammunition. Nothing here gets filed away.

**Sources:** a comparative pass over Participatory Economics, Cockshott & Cottrell, Sraffa/Steedman, LCA allocation theory, Kantorovich, Ellerman, Odum and Sensorica, plus the **field record** of local currencies and time banking (§OA0), and the **auditor-independence literature** (§OA10).

---

<!-- tag: obj-toc -->
## Contents

- [Status board](#status-board)
- [0. The headline finding](#0-the-headline-finding)

**[PART A — LIVE OBJECTIONS](#part-a--live-objections)**

  - [OA0. The field record — what actually kills these systems](#oa0-the-field-record--what-actually-kills-these-systems)
  - [OA1 — OP-18. Responsibility for joint work is not divisible](#oa1--op-18-responsibility-for-joint-work-is-not-divisible)
  - [OA2 — OP-10 / P8. Weighting-model governance, and the Hayek residue](#oa2--op-10--p8-weighting-model-governance-and-the-hayek-residue)
  - [OA3 — OP-24. Understatement drift](#oa3--op-24-understatement-drift)
  - [OA4 — OP-23. Shared-overhead attribution](#oa4--op-23-shared-overhead-attribution--closed-in-v06--moved-to-b8)
  - [OA5 — OP-16. The onerousness gap](#oa5--op-16-the-onerousness-gap)
  - [OA6 — OP-6. Feedback mechanics](#oa6--op-6-feedback-mechanics)
  - [OA7 — P4. Abolishing property income does not abolish class](#oa7--p4-abolishing-property-income-does-not-abolish-class)
  - [OA8 — OP-9 / P5. Preference revelation](#oa8--op-9--p5-preference-revelation)
  - [OA9 — OP-22. Minimum audit disclosure](#oa9--op-22-minimum-audit-disclosure)
  - [OA10 — The auditor-independence problem](#oa10--the-auditor-independence-problem)
  - [OA11 — OP-25. Illicit end-of-life dumping](#oa11--op-25-illicit-end-of-life-dumping)
  - [OA12 — OP-26. The coverage gap](#oa12--op-26-the-coverage-gap)

**[PART B — ANSWERED](#part-b--answered)**

  - [B7 — OP-17. Joint production](#b7--op-17-joint-production--closed-for-materials-and-energy)
  - [B8 — OP-23. Shared overhead](#b8--op-23-shared-overhead--closed--capital-accrues-to-the-asset-not-the-co-products)
  - [B13 — OP-27. Parallel implementation](#b13--op-27-parallel-implementation--ruled-and-stress-tested)
  - [B9 — OP-18. Labour & team credit](#b9--op-18-labour--team-credit--closed-as-the-c3-blocker--team-credit-dissolves-labour-rides-the-material-split)
  - [B10 — Credit realization & the supply-chain hand-off model](#b10--credit-realization--the-supply-chain-hand-off-model--passes-with-changes)
  - [B12 — §3.2b electricity attribution (the real-time-dispatch principle)](#b12--32b-electricity-attribution-the-real-time-dispatch-principle--passes-with-changes)
  - [B11 — Self-care as credited work & the definition of work](#b11--self-care-as-credited-work--the-definition-of-work--passes-instance-of-op-10op-22)
  - [B1 — P7. "Nothing else is value"](#b1--p7-nothing-else-is-value--fixed)
  - [B2 — W1. A3 defeats the sink problem](#b2--w1-a3-defeats-the-sink-problem--claimed)
  - [B3 — Front-loading](#b3--front-loading--dissolved-op-11-op-5-op-21)
  - [B4 — One credit, three feedback channels](#b4--one-credit-three-feedback-channels--dissolved-op-8)
  - [B5 — OP-19, OP-20, S1, W2, P9](#b5--op-19-op-20-s1-w2-p9-)
  - [B6 — Ellerman replaces Marx](#b6--ellerman-replaces-marx--adopted)
- [C. Tests owed](#c-tests-owed)
- [D. Not yet examined](#d-not-yet-examined)
- [Change history](#change-history)

---

<!-- tag: obj-status-board -->
## Status board

| | Item | Status |
|---|---|---|
| ✅ | **OP-27 (parallel implementation) — Using Aequitas while the world still uses money** | **Registered, ruled and stress-tested on 2026-08-23 — it enters the register already answered (B13).** Both directions across the money boundary are deliberately costly and neither is forbidden: a money-made good is **dark until sold in** and clears via a **published template**; selling out **keeps the debit and reads as a gift**, because money is not matter (A1). **No axiom moved and no cross-boundary rule was needed.** The §3.2/§3.2b contradiction claim **fails** — they govern different debits. **Money cannot buy standing at any scale**, and extraction **self-limits** through the extractor's own ratio gate. **Two residuals enter open: repeat-shell *entities* (→ OP-25 / C6) and template capture (→ OP-24 / OP-10).** Folded to Foundations §4.8. |
| 🔴 | **OP-10 (weighting governance) / P8 (weighting governance) — Weighting-model governance** | Open. One side entrance closed (§3.2a); cost constants have a mechanism (§3.3a); the general problem stands. **Now the top blocking problem.** §4.8 settles the convergence worry rather than deepening it: **the escape from Aequitas is non-participation — the gift economy — not another network**, so nothing closes; and **exit was never the discipline. Replication is**, which is what §3.3a's two-unaffiliated-replications rule already was. **Trust networks are laboratories, not banks**, and a neighbour helps fix a bad method out of self-interest, because in an interoperating pair a bad method contaminates both books. **A monopoly earned by better methods is not the monopoly capitalism produces** — methods are published and replicable, so it is a monopoly over *which* method is used, never over who may propose one. No exclusion, no moat. **What survives for OP-10 is the original question, unchanged in size: who governs the method set.** |
| 🔴 | **OP-24 (understatement drift) — Understatement drift** | Errors favouring subscribers have no funder. Attacks A4 (no externalities). **v0.21: the proposed fix — rival-sector audit — was WITHDRAWN as a weak mechanism.** A rival's best move is not to fund your correction but to get their own constant set generously: **the equilibrium is mutual understatement, not mutual policing.** And it fails hardest on the largest levers (the stock and baseline constants), which have no rival at all. **Ruled out of scope as a *mechanism*, and kept as a *requirement*:** auditing cost constants is a trust-network design problem (§1.2), held to five published properties in Foundations §3.3a and conformance 16a–16c. **A network with no answer is not conforming.** Unproven and labelled as such. **Lever enlarged in v0.6** by the stock/baseline constants. **Partially relieved in v0.17 (OP-26): the audit of *extent* has a funder even though the audit of *weight* does not.** And §4.7 **dissolves the *funding* half entirely** — "funding" in Aequitas is only the recognition of an activity as creditable, recording is never gated (A7), so the credit for audit work was never scarce. **What OP-24 is actually about is the surviving half: demand.** Someone must still *want* the correction, and for an understating weight constant the rival sector remains the only party who does. The objection is narrower and sharper than it was, not closed. |
| 🟠 | **OP-26 (coverage gap) — Consistency is not completeness** | **v0.19: a second outside pass folded four more findings and revealed that six others were already answered.** The residual rule gains its **third condition** — *N* and *Y* must be scope-aligned before subtraction (Foundations §4.4, conformance 14a); the **sorting question** replaces the old log-side/projection-side cut (14b); the **verification ladder gains a cost column** with the ~40% ceiling stated where the rung is chosen (Foundations §4.3 — it was conformance 14c until the row was deleted on 2026-08-28, because audit hours are already credited work and a query returns them); and **independence is separated from expressiveness**, which relocates trust from the ledger to the instrument and says so. **The organisational finding is the larger one:** the outreach agent conceded six points in public that these documents settle, because its brief never told it to read Foundations. Fixed procedurally. **The first objection sourced from outside the project** (@cairn-lineage, 1f916.ai). Answered and folded: the closure witness was already Foundations §4.4; the residual is **held, not allocated** (§4.4); IC-13/IC-14 were stress-tested and **rejected**, replaced by the origin-evidence ruling and a mandatory provenance block. **Mechanism complete 2026-08-22** — the back-trace horizon is settled at birth (§4.4) and **both owed sims are green**. `residual_unravelling.py`: the residual basis leaves **0.1%** dark against **52.5%** for the population basis, so §4.4 is load-bearing — and it measures the limit, **unravelling collapses once verification costs more than ~40% of a median unit's debit**, which makes cheap verification a precondition and routes into **OP-22** and **C2**. `arithmetic_audits.py` now declares its own extent and blind spots per §5.4. See **OA12**. |
| 🟠 | **OP-16 (onerousness gap) — Onerousness gap** | **Hazard half addressed** by the contingent reserve (§4.6, v0.15); skill half fixed by A2 v0.3. **Tedium/indignity half open.** |
| 🟠 | **OP-6 (feedback mechanics) — Feedback mechanics** | Promoted; also carries signal flooding. |
| 🟠 | **P4 (coordinator class) — Coordinator class** | **Weakened again in v0.8.** Credit-accumulation form dead; **wage-extraction employer now structurally hollowed out** (no wages A3 (non-fungibility), no surplus A5 (cost, not price), no rank-based dumping); mislabeling defused (public pledge ledger). Only the *coordination* residual (who holds empowering work; hours-inequality in pledging) survives. |
| 🟠 | **OP-1 (service → influence) — Service → influence** | **Carries the credit-realization residual** (gross fake hours from collusive hand-offs — bounded by IC-7 (24-hour cap) and paid in a wrecked ratio; B10). The old "self-starving" brake is gone — pledging no longer costs the pledger debit-room (Foundations v0.13), so it no longer starves an influence-pumper. The flip side: self-care credit → a **universal basic voice** bounding influence disparity to `24h ÷ floor` (a feature); routing is a network lever, backing checkable only via OP-22 (audit disclosure). See B10/B11. |
| 🟢 | **OP-9 (calculation reply) / P5 (preference revelation) — Socialist-calculation reply** | **Written up (v0.10)** → `OP-9_calculation_reply.md`. Cost≠value defeats Mises; pledges reveal demand; tractability cited; scarcity-as-debit rations without a margin. **Re-opened by two outside economists 2026-08-24 and answered with a fifth move (§5a):** *the price being defended is not an honest signal.* Every form of the objection assumes a price honestly reports scarcity and demand; **in a concentrated market the same firms restrict supply and manufacture demand** — Braudel's anti-market layer, via DeLanda. **A pledge cannot be advertised into existence**, and the demand lever's concentration falls from money's ≈10⁶× to the `24/F ≈ 2.4×` ceiling. Worked cases in Foundations **§4.6**. **Answered for cost; the objective-function edge and the Hayek tacit-knowledge residue still terminate in OP-10, and the last-unit question stays with distribution (§5.5).** See OA8. |
| 🟠 | **OP-22 — Minimum audit disclosure** | **THE SPLIT WAS PROPOSED AND REFUSED — author ruling 2026-08-25, recorded here in v0.23.** @cairn-lineage argued a hiding proof does not establish non-reuse and asked for OP-22a / OP-22b. **OP-22 is not split and OP-22b is not opened.** Their falsifier builds — Network A at a 4 h floor records 12 credited hours for the same Monday that Network B at a 10 h floor records as 18, and **12 + 18 = 30 hours in a 24-hour day** — **and no party computes that sum**, because no book is ever added to another and a transaction lands on one network the seller picks (§4.0). **The non-reuse witness is C6 and a merge precondition** (§4.8). **They were right about the ceiling**: §5.5's cross-network clause was ours and is **struck, not narrowed**. **And the two networks' figures cannot be added.** A's hours and B's hours are collapsed through different weighting models, so summing them sets an exchange rate between credit-standards — forbidden by **A3** and **§4.2**, and now **conformance 4a**. **IC-7 was never breached either: 12 and 18 are each under 24, and it binds each account separately.** What is left is a **coverage** question — activity one network cannot see — already handled by §4.4 and §4.4. Paper: [`OP-22_identity_not_disclosure_v0.2.md`](open-problems/OP-22_identity_not_disclosure_v0.2.md). See **OA9**. *Prior:* **Promoted to red, then partly answered, in v0.17.** §4.7 settles *who decides*: **the trust network**, because it does the tallying and therefore holds what is private. Aequitas states principles and does not dictate practice — the third dial of the same kind as ρ and the floor. Pseudo-privacy on the payment-intermediary model, radical transparency, or anything between; inter-network compatibility is negotiated. **Opacity is priced rather than forbidden** (OP-14 discounts what it cannot verify). **Residues, updated by §4.7 and then by §4.8.** (a) ~~Information capture~~ **— CLOSED, scoped out with reasons** (`C2_information_capture.md` §13). The escape is non-participation and never closes; **trust networks are laboratories, not banks**, corrected by replication rather than by competition; and a monopoly earned by better methods is not the monopoly capitalism produces, because methods are published and there is no exclusion. Concentration under convergence is hypothetical, its timing and technology unknown, and data security is a technology problem outside this project. **Watch item, not a defence: a merit monopoly can stop being meritorious — the guard is publication plus replication, so §4.7 and this argument are load-bearing for each other.** (b) **A measured coverage cost to privacy** — the ~40% verification-cost threshold (`residual_unravelling.py`). (c) **A network's choice binds members who did not make it** (C2). (d) **New, from §4.7:** publishing more to earn trust also publishes more to de-anonymise — a *second* axis, not a restatement of (b). The minimum disclosure set itself is still unspecified. *Prior in v0.17:* Was a C7 implementation question. §4.4's lifetime back-trace makes a person's record a **life dossier** — birthplace, every residence, employment, commuting distance, vehicles, mileage. Disclosure is voluntary but the *incentive* runs toward disclosing, so the system pressures people to assemble exactly the record a surveillance state would want. **§4.7's market-public/persons-private principle now has to hold across a lifetime**, and OP-22 becomes the load-bearing privacy problem of the whole system. It also still powers the anti-arbitrage guard. See B11 and **OA12**. |
| ✅ | **Credit-realization / hand-off model** | **PASSES WITH CHANGES (v0.8).** All three exploits (wash-trade, gatekeeper, risk-dumper) defused; residuals route to OP-1/OP-22/OP-25. See **B10**. |
| ✅ | **Work-definition / self-care cluster** | **PASSES (v0.9).** Self-care is credited *time* (the §5.5 floor's mechanism, not a grant); verification generalises by output type; self-care → universal basic voice. Not a new hole — an instance of OP-10/OP-22. See **B11**. |
| 🔽 | **OP-25 (illicit dumping) — Illicit end-of-life dumping** | **New.** §3.6 prices lawful disposal; abandonment attribution is a Level-2 problem. |
| 🟠 | **OP-4 (debit tolerance) — Debit tolerance formula** | *Folded from Foundations §10 on 2026-08-25.* It is the **denominator of the disparity ceiling** (Foundations §5.5.5) and it sets the **floor magnitude** (§4.5, §5.5.1). **There is no single global debit:credit ratio** — §3.5 forbids one (aggregate is always >1 and rising, and a pure-ratio metric is infinite for a newborn) and A8 forbids an expert-set one. Axiom-clean shape: a **per-person, network-set tolerance floor plus a personal efficiency ratio on the discretionary layer only.** **v0.22 adds two things.** The floor's value has a **lower bound** (essentials must stay affordable — at ρ = 1.2 and 700 h/yr of essentials the minimum is 1.6 h/day) and an **upper bound** (the gate must still ration what is short — at `F` = 10 the floor alone entitles 3.17× a median lifestyle); **a simulation showing a stable band of `F` and ρ exists is owed**, and is test 9 below. And **whether a network credits a child's learning time is a second dial on the same ceiling** — 2.400× if credited, 2.085× if not — which belongs here and with Foundations A8. |
| 🟠 | **OP-8 (feedback firewall) — Can feedback be bought?** | *(reframed; folded from Foundations §10.)* **A signal that credit can purchase is a currency by the back door.** Guarded by §4.2, which forbids *credit* realising on feedback — enrichment verifies by occurrence-attestation (*"did the work happen?"*), never by likes or citations. **The guard is stated; whether it holds under §4.6's likes-to-pledges preset is OP-6 business.** See OA6. |
| 🔽 | **OP-3 (estimation convergence) — The estimation engine** | *Folded from Foundations §10.* Requires a cohort **production** model as well as a consumption model, computed on the residual rule (§4.4). |
| 🔽 | **OP-14 (cohort shopping) — Cohort shopping** | *Folded from Foundations §10.* Now also **floor and routing shopping** — subscribers gravitate to networks with a generous floor or favourable pledging-routing (§4.5). Arrested, if at all, by counterparty re-computation (§4.2). **Narrowed by the OP-22 ruling of 2026-08-25:** a seller chooses which network a transaction lands on (§4.0), so a network with an implausible floor loses sellers. **A multi-homing claim was drafted for this row on 2026-08-27 and REFUSED by the author the same day.** The draft said a person with accounts on a 4 h-floor and a 10 h-floor network reaches *"14.4 + 21.6 = 36.0 h of room against a floor-only subscriber's 12.0 h"*. **That addition is not available.** The two figures are collapsed through different weighting models, so adding them sets an exchange rate between credit-standards — **A3** and **§4.2**, now carried as **conformance 4a**. **And IC-7 was never breached: 12 and 18 are each under 24, and it binds each account separately.** **What remains is a coverage question, not a disparity question** — purchases on B are activity A cannot see, and §4.4 publishes the coverage gap while §4.4 estimates undisclosed activity over the undisclosed residual, erring against the person. **Watch item: nobody has measured whether that is tight enough against deliberate splitting.** It belongs with the coverage work and **OP-24**, not here. See **OA9** and `OP-22_identity_not_disclosure_v0.2.md` §7. |
| 🔽 | **OP-15 (ghost harvesting) — Ghost harvesting** | *Folded from Foundations §10.* Stated, not worked. |
| 🔽 | **OP-7 (cross-level trade) — Cross-level trade** | *Folded from Foundations §10.* Stated, not worked. §4's design rule requires a Level 1 region and a Level 3 region to be able to trade. |
| ⏸ | **OP-2 — Anti-collusion at Level 2** | *Folded from Foundations §10.* **Deprioritized.** Level 2 is an emergent market of trust networks; revisit once the system is stated. |
| ✅ | **OP-18 (labour & team credit) — Responsibility is not divisible** | **CLOSED in v0.7** as the C3 (estimation engine) blocker — team-credit dissolves under A2; labour rides the material split; cost ≠ scarcity. See **B9**. |
| ✅ | **OP-23 (shared overhead) — Shared-overhead attribution** | **CLOSED in v0.6** — capital and overhead never allocate to co-products. **Re-attacked 2026-08-24 from outside** (*"capital exclusion contradicts A5"*) and **HELD.** The critic's step is to assume the beef caused the barn; under **A1** only people act, so **a thing causes nothing** — and §3.2b already refuses that flow downstream, §4.5 upstream. **What was actually broken was A5's wording**, which located a cost on the *thing*; it is repaired in Foundations **v0.21**, along with the identical defect in **A4** (*"priced into it"*). **No mechanism moved.** One residue registered: a per-unit debit-cost carries no capital signal, and the discipline runs through the builder's own gate — **the §5.2 argument, transferred.** See **B8**. |
| ✅ | **OP-17 (joint production) — Joint production allocation** | **CLOSED** for the material/energy half — see **B7**. |
| ✅ | **P7 (theory of value) — "theory of value"** · **W1 — A3 defeats sinks** · **P9 (local-currency read)** · **S1** · **Ellerman** | **Fixed / claimed / adopted.** |
| ✅ | ~~OP-11~~ · ~~OP-5~~ · ~~OP-8 firewall~~ · ~~OP-19~~ · ~~OP-20~~ · ~~OP-21~~ | **Dissolved, resolved, or closed.** |

**Fifteen items closed; six live** — and in v0.17 the composition shifted twice. **OP-22 was promoted to red by §4.4's lifetime back-trace and then pulled back to orange by §4.7**, which named the holder (the trust network) and made privacy a network dial rather than a system-wide unknown. What the round trip left behind is sharper than what it started with: three named residues instead of one vague one, and a *priced* trade-off between privacy and coverage. Original note: in v0.17 the composition shifted: OP-26 arrived from outside, was answered and folded within a day, and **its answer promoted OP-22 from a deferred implementation question to a red blocker.** The pattern worth noting: a coverage mechanism that costs nothing in accounting terms can still cost a great deal in privacy terms, and the register should expect that trade to recur. Original note follows. **Fifteen items closed; six live.** The pattern held for a fourth session and then broke on the fifth in an instructive way: OP-17, OP-11 (training amortization), OP-21 (media reproduction), OP-23 all closed by *removing* a division. **OP-18 is the first to close by *declaring* a convention** — because labour genuinely leaves no trace, the physical-trace test *mandates* a convention here. **v0.8's contribution was different again:** the credit-realization model (B10) closed a cluster of *incentive* exploits by discovering that a mechanism the author already had — **debit-follows-possession** — inverts the attacker's leverage. **v0.9's is different once more (B11):** the work-definition cluster's apparent new capture surface turned out to be an *instance of an existing open problem* (OP-10 weighting governance / OP-22 disclosure), not a new one — the honest outcome of a stress-test is sometimes "this is the old hole wearing a new hat," and saying so keeps the register from inflating its problem count.

---

<!-- tag: obj-s0 -->
## 0. The headline finding

**Aequitas's hard problem is division of the untraceable.**

The v0.4 statement was *"division, not measurement,"* and it was too broad. OP-17's resolution shows why: a refinery's debit **does** divide across its fractions, because the cracking energy physically went somewhere and a meter can find it. The division was a measurement that nobody had thought to take.

> **The test that separates the two cases — and it is the most transferable result the project has produced:**
> **Did the thing being divided leave a physical trace?**
> **Trace → measure.** Feed energy, cracking enthalpy, a turbine's heat/power curve.
> **No trace → declare a convention and say so.** Labour hours across co-products; shared overhead; joint responsibility across a team.

**What remains genuinely indivisible is now vanishingly small.** After v0.7, of the two OP-18 (labour & team credit) scales: **labour across co-products** is closed — it gets a *declared convention* (rides the material split, §3.4a/§1.1), which is exactly what the physical-trace test prescribes for a no-trace quantity. **Responsibility across a team** dissolved for *credit* (A2 (time as measure): own hours) and survives only as the apportionment of a jointly-*caused debit* (team pollution/harm) — minor, non-blocking, sibling to OP-25 (illicit dumping). **The untraceable residue is no longer a blocker anywhere.**

> **A refinement of the headline, v0.7:** "no trace → declare a convention" is not a failure mode — it is a *result*. The win is (a) knowing when you are in that case, and (b) choosing the convention that adds no new capture surface. Labour riding the material split does exactly that: it introduces no basis of its own, so whoever games the split gains nothing they could not already gain by gaming the material θ — which rival-sector audit already polices.

> **Overhead was the third, and v0.6 removed it — not by splitting it, but by declining to allocate it at all.** Capital and overhead accrue to the **asset** as property-debit and never flow to the co-products (Foundations §4.5). The barn is not divided between hide and beef; it stays on the operator. **A division problem dissolved by relocating the thing being divided** — the fourth consecutive closure of that shape.
>
> **Re-attacked in 2026-08-24 and held — but the attack found something real, one level down.** *"If the barn is not in the beef, beef's price is not beef's cost, so A5 fails."* **The ruling was not the error. A5's wording was**, and so was A4's: both used *price* language that says a cost rides the thing, while every mechanism in the document says a cost attaches to whoever **caused** it. Both axioms repaired in Foundations **v0.21**; nothing else moved. See **B8**.

*Foundations adopts this:* §3.4 is narrowed, §3.4a states the material/energy rule, §4.5 removes the overhead allocation, and §1.1 has now lost two rows rather than gaining entries.

---
---

<!-- tag: obj-part-a-live-objections -->
# PART A — LIVE OBJECTIONS

Ranked by how much of the theory fails if the objection stands.

> **Notation (2026-08-09):** analysis sections in this register are numbered **OA0–OA11** (Objection Analysis) — *renamed from the old `A#` to end the collision with the Foundations axioms `A1–A8`.* In this document, **`A1`–`A8` now always mean an axiom**; **`OA#`** means an analysis section here; **`B#`** an answered objection (Part B). Cross-doc index: [`GLOSSARY.md`](GLOSSARY.md).

---

<!-- tag: obj-oa0 -->
## OA0. The field record — what actually kills these systems

Source: `GLOSSARY.md#src-local-currency-experiments`. Ithaca HOURS, Burlington Bread, time banking, Wörgl, WIR, Sardex, LETS. A century of people building these and finding out what breaks — the closest thing the project has to an experimental literature.

**It does not show one failure repeated. It shows three.**

| Class | What breaks | Cases | Aequitas |
|---|---|---|---|
| **1 — Valuation** | Flat-hour crediting cannot recruit skill | Warren; **time banking, 45 years** | 🟠 Skill fixed; **OP-16** hazard half addressed (§4.6), tedium half open |
| **2 — Circulation** | Scrip pools at sinks and stops moving | Ithaca, Burlington | ✅ **Immune — see B2** |
| **3 — Institutional** | Founder dependency, state suppression | Ithaca (Glover left); Wörgl (banned) | ✅ Addressed — see B5, B2 |

---

<!-- tag: obj-oa1 -->
## OA1 — OP-18. Responsibility for joint work is not divisible

**Attacks:** A1's attribution claim, A2 (time as measure), C1's agent field.
**Sources:** [Ellerman](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf) · `GLOSSARY.md#src-ellerman-labor-theory-of-property`
**Status:** ✅ **CLOSED 2026-08-05 as the C3 (estimation engine) blocker — moved to Part B (B9).** The statement below is kept as the record of the problem; the resolution is in B9. Resolution note: `00-strategy/open-problems/OP-18_labour_and_team_credit.md`.

> **Resolution in one line:** the "credit a team member separately" half was a **mis-statement** — under A2, credit is *own hours worked*, and no output-decomposition is needed (B9). The genuine residue, **labour across co-products**, gets a **declared convention: labour rides the process's material split** (§3.4a); co-product cost is embodied input, **never scarcity** (the tenderloin case). Only the apportionment of a jointly-*caused debit* across a team survives, and it is minor and non-blocking.

Ellerman is explicit that de facto responsibility for a joint product is **joint and non-decomposable**. The whole team is responsible for the whole output. There is no factual measure saying the welder caused 40% of the bridge — and Aequitas needs exactly that number to credit nine people separately.

**Hours-worked is an allocation convention, not a measurement.** Foundations §1.1 declares it as one, which converts a universality violation into an honest one. **It does not make the convention correct**, and a critic can still ask why hours rather than some other basis.

> **🔴 Why this now blocks C3, which OP-17 (joint production) previously did.**
> §3.4a splits a joint process's **materials and energy** by measuring where the process physically sent them. **Labour has no such trace.** The farmer's eight hours were spent on the animal, not on the hide, and splitting those hours by tissue-deposition energetics would assume labour is expended in proportion to metabolic energy — an assumption, not a measurement.
> C3 needs **per-product labour hours**. That is precisely the layer [EXIOBASE](https://www.exiobase.eu/) carries and almost nobody else collects, and it is precisely the layer no instrument can split. **The critical path moved from OP-17 to OP-18 (labour & team credit) without anything being solved twice.**

**Does the OP-17 rule transfer?** Partially, and the honest answer is *no, not for the hard part.* Where a team's output responds measurably to a member's participation, something like a derivative exists. Where it does not, nothing does. **Test this before assuming it transfers** — Ellerman's objection is about *responsibility*, which may not be a cost function at all.

*(The ally half of Ellerman — responsibility imputation as the grounding for A1 (materialism of cost) — is adopted and lives in B6.)*

---

<!-- tag: obj-oa2 -->
## OA2 — OP-10 / P8. Weighting-model governance, and the Hayek residue

**Attacks:** A8 (no governing body), decentralization.
**Status:** 🔴 Open. Largest hole in A8. **Two partial answers added in v0.5.**

Whoever sets the mitigation-cost model controls every balance in history without touching a core rule.

**The comparison sharpens it.** Parecon's Iteration Facilitation Board is [attacked as implausible](https://ejpe.org/journal/article/view/867) for assuming a body can announce opportunity costs for all goods, resources, labour categories and capital stocks. **Aequitas's weighting-model maintainer is structurally the same object.** The verification ladder answers *data collection* — it gathers locally rather than centrally — but it does not answer *model maintenance*, which remains central by default.

**Progress in v0.5, from the OP-17 (joint production) work:**

1. **A side entrance is closed.** Foundations §3.2a requires every division of a debit to be computed **per dimension on the vector, before collapsing** to a comparable scalar. Had splits been computed on the collapsed number, the weighting-model maintainer would have controlled every allocation in history *invisibly*. Per-dimension splits are weighting-independent. **This hole existed and nobody had noticed it.**
2. **Cost constants have a mechanism** — rival-sector audit, §3.3a and OA10 (auditor independence) below. It is specific to constants, not to the model as a whole.

**What remains:** the general problem. The strongest available reply is competing open variance under A8 — multiple weighting models, openly published, each recomputable by anyone from the same log. **That reply is asserted in A8 and still nowhere specified. Specify it.**

**Entangled with OP-9 (calculation reply)** (a scarcity price is the dual of an optimisation, so whoever sets the objective function sets every scarcity price) and with Foundations §10.1 (a trust network that can declare an activity creditable can issue credit). **Three problems, one capture surface. Work them together.**

> **Worth recording as a design constraint discovered in v0.5:** the two candidate allocation rules that were *rejected* — Aumann–Shapley marginal allocation and Kantorovich shadow prices — **both required an objective function**, and would each have re-opened OP-10 (weighting governance) through the allocation layer. The rule that was adopted requires none. **When choosing between mechanisms, "does this need an objective function?" is a fast proxy for "does this re-open OP-10?"**

---

<!-- tag: obj-oa3 -->
## OA3 — OP-24. Understatement drift

**Attacks:** A4 (no externalities) — progressively, and without any single visible violation.
**Sources:** `GLOSSARY.md#src-auditor-independence` · [credit rating agencies and the subprime crisis](https://en.wikipedia.org/wiki/Credit_rating_agencies_and_the_subprime_crisis)
**Status:** 🔴 **Open. Fix proposed, unproven.**

Retroactive re-weighting (§3.3) makes cost constants extraordinarily powerful: whoever publishes the energetics of a process sets every split in that sector, backwards through all history.

> **⚠️ Lever enlarged in v0.6.** Foundations §3.3 now makes pollution-debt **stock-dependent**, floating with the ambient stock above a natural-remediation baseline. Two new constants — the **equilibrium baseline** and the **ambient-stock measurement** — move every pollution record in history at once. They are the largest single levers in the weighting model, and the consumer-side understatement bias below applies to them with full force: everyone benefits from the baseline being set high (fewer things count as pollution) and the stock being read low. Foundations §3.3a places them explicitly under rival-sector audit. **This does not solve OP-24 (understatement drift); it raises the stakes on it.**

**One channel of capture is structurally closed and should be claimed.** There is no market-dominating corporation to fund a favourable result, because A5 (cost, not price) removes the profit that pays for captured science today. Labs are credited by trust networks for doing work. **The Enron-shaped failure cannot operate the same way here.**

**But the mirror problem is real, and it was introduced by the fix for the first one.** A general-membership trust network is dominated by the *consuming* side of any given good — everyone eats beef, few raise cattle. Its members therefore collectively benefit from beef's debit being **understated**. And the incentive to correct is one-sided:

| Error direction | Who wants it fixed | Result |
|---|---|---|
| Constant **overstates** debit | Every subscriber | Corrected |
| Constant **understates** debit | Nobody — correcting it worsens every subscriber's ledger | **Nobody funds the replication** |

**Result: systemic drift toward under-costing** — precisely how every carbon-accounting regime attempted so far has failed. Foundations §3.5 tolerates it arithmetically (no global balance is required), which is what makes it insidious: **there is no equation that breaks.** It simply erodes A4.

**Aggravating factor: replication cost is asymmetric.** Competing networks discipline *estimates* cheaply — re-interviewing a farmer is cheap. They do not discipline *constants*: re-running calorimetry is not cheap. So the competitive pressure that works everywhere else in the system is weakest exactly here.

### ⛔ The proposed fix was WITHDRAWN on 2026-08-24. Author ruling.

From v0.5 to v0.21 this register offered **rival-sector audit** as the fix:

> *"The natural auditor of a cost constant is the rival sector, not the consumer. If beef's energetics are understated, plant-protein producers are materially harmed and will fund the replication."*

**The author's assessment: it is a weak mechanism.** Two objections, and the second is the one that sinks it.

1. **Rivals are often absent.** This register already said so. A good with no substitute has no rival, and **a constant cutting across every sector equally has no rival by construction.**
2. **A rival's best move is not to fund your correction.** Funding a replication costs real hours and the benefit is **shared with every other producer in the rival sector — a public good among rivals.** **Getting their own constant set generously is cheaper and the benefit is private.** So the equilibrium is **mutual understatement, not mutual policing.** The mechanism assumed rivals are adversaries; on this axis their interests are aligned.

> **And it failed hardest where the stakes are highest.** §3.3a itself called the **ambient-stock and baseline constants** the largest levers in the weighting model. **Those have no rival at all** — everyone benefits from a high pollution baseline and a low stock reading. **A mechanism that works for beef versus plant protein and fails for CO₂ is pointed the wrong way round.**

### The ruling: the mechanism is out of scope. The requirement is not.

> **Auditing cost constants is one of the problems a trust network exists to solve.** How it does so is the network's own design (§1.2 — *state what must be true, never how to build it*), published and checkable like everything else it does.

**Five design requirements now sit in Foundations §3.3a**, carried as conformance **16a–16c**: two unaffiliated replications before a re-weight · every constant published with method, version and **uncertainty interval** · triage by **magnitude × concentration of beneficiary** · **public membership composition**, so a network concentrated in the sector it audits is detectable · and **a statement of which constants have not been reviewed and how old each reading is.**

**A network that cannot show how it audits its constants is not conforming. It is not free to have no answer.**

**Why this is not simply giving up.** A4 requires every cost to be *accounted to whoever caused it*. It does not require the first estimate to be right — §3.3 already makes every figure a dated reading. **Systematic, uncorrected drift is a different thing: that is costs escaping, and it is an A4 failure.** So the obligation stays in Foundations even though the practice does not.

**⚠️ Still unproven, and now honestly labelled as such.** No network has demonstrated a working answer, because no network exists. **The five requirements are what a design will be judged against, not evidence the problem is solved.** Test still owed (§C item 2): simulate a population of trust networks under these incentives and find the conditions under which drift stops being arrested.

> **🚩 A risk this ruling creates, recorded so it is not discovered later.** **This is the third governance question scoped to trust networks in two days** — privacy practice (§4.7), split methods (§3.4a), and now constant auditing. **The first two came with a demonstration that the accounting is unaffected at both ends of the dial. This one does not**, because drift genuinely damages the books. **The scope-out is honest only for as long as the requirements are hard and the admission is public.** If a fourth governance problem is scoped out the same way, that is the point to ask whether the project is drawing a boundary or offloading its hard problems.

---

<!-- tag: obj-oa4 -->
## OA4 — OP-23. Shared-overhead attribution ✅ **CLOSED in v0.6 → moved to B8**

The candidate direction flagged in v0.5 — *"apply front-loading to tooling so the fab's construction is pledged and discharged rather than amortized into wafers"* — is what closed it. Overhead was never allocated to co-products at all; it accrues to the asset. **The overhead-stuffing exploit dies with the allocation it was gaming.** Full argument in **B8**.

---

<!-- tag: obj-oa5 -->
## OA5 — OP-16. The onerousness gap

**Attacks:** A2 (time as measure), and the system's ability to allocate labour at all.
**Sources:** [Hahnel](https://znetwork.org/znetarticle/in-defense-of-participatory-economics-by-robin-hahnel/) · [PLOS One time-banking review, 2025](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0322760) · `GLOSSARY.md#src-participatory-economics`
**Status:** 🟠 **Hazard half now addressed (v0.15); tedium/indignity half open.**

Parecon remunerates **duration, intensity, and onerousness**. Aequitas refuses to rate-scale labour (A2) and resolves differences materially instead.

**What A2 v0.3 covers:** exertion (extra calories), hazard (retroactive health debit), and **skill** (training is credited work rather than a downstream charge).

> **✅ The hazard subset is now addressed — the contingent reserve (Foundations §4.6).** Flat credit alone under-staffs dangerous work: a worker bears its expected future health cost on their own ledger, so they avoid it (the 45-year time-banking shortage). Permanent over-pledging fixes this *without* a wage premium or rating authority — the surplus becomes an earmarked, non-consumable reserve that pre-funds any verified task-caused harm to the doer. Society de-risks the toxic-cleanup worker exactly to the extent it pledges for the work; the danger internalises as the reserve the task must attract. Sim `06-simulation/pledge-reserve/pledge_reserve.py`: the job clears once pledges roughly cover the tail, and overflow-reverts-to-causer (§3.2/§3.7) preserves care. **This is a demand-gated incentive, not a rate multiplier — A2-clean.**

**What remains uncovered: disutility with no material signature *and no causal tail*.** Tedium, isolation, indignity. Dull-but-safe work generates no future task-caused cost, so the reserve gives it no incentive. Two such jobs with identical calories, identical training, and identical health outcomes credit identically per hour — but nobody wants one of them. **This half stays open.**

**This is not theoretical.** Time banking credits every hour identically — exactly A2's flat hour — and 45 years across dozens of countries produces chronic **skill mismatch**, credit hoarding, and skills in short supply.

**Candidates:**
- **(a) Hour-ceiling differentiation — strongest.** Pay the premium in *hours, not rate*: a sustainable sewer shift is 4h, a pleasant one 8h; both credit 1hr/hr, so no multiplier exists anywhere. Justification is **physiological and measured**. Weakness: who sets the ceilings → **OP-10 (weighting governance)**.
- **(b) Check how much of OP-16 (onerousness gap) is simply unmeasured hazard.** Night shift, isolation, and repetitive strain have documented health costs A2's hazard clause **already** injects. **Do this first** — it may shrink the problem substantially.
- **(c) Automation pressure.** Unfilled pledges are a visible, quantified signal saying *automate this*.
- **(d) Rotation** (balanced job complexes). Carries [the compulsory-labour critique](http://libcom.org/blog/workers-critique-parecon-11042012). Last resort.
- **(e) The contingent reserve — adopted for the hazard subset (v0.15).** See the box above; Foundations §4.6. It covers hazardous-onerous work; it does *not* touch tedium/indignity, which has no causal tail to pre-fund.

> **Withdrawn candidate:** *"route onerous work to service credit."* There is no separate service credit to pay a premium in. Recorded so it is not re-proposed.

**Test:** compute the debit-cost of night-shift office cleaner, day-shift office cleaner, and rural postal carrier. **If the numbers come out identical, OP-16 is confirmed and (b) is eliminated.**

---

<!-- tag: obj-oa6 -->
## OA6 — OP-6. Feedback mechanics

**Attacks:** §4.6, §4.6. **Status:** 🟠 Open, and **promoted**.

How signals aggregate without becoming a popularity plutocracy.

**Why it is more urgent than its old ranking implied.** Accumulation is forbidden by A3 (non-fungibility), and a high producer's marginal credit does nothing once their ceiling exceeds their appetite. **Feedback and pledging are therefore the entire motivation system for anyone past their own consumption ceiling** — which is to say, for exactly the people the economy most depends on.

**Two live sub-problems:**
1. **Signal flooding** *(inherited from OP-20 (unobservable work))*. Signals are unbacked and plentiful by design, and generation cost for low-quality content trends to zero. Nothing in the schema constrains this; it is projection-side and has no answer yet.
2. **OP-8 (feedback firewall) reframed — can feedback be bought?** **A signal that credit can purchase is a currency by the back door.**

---

<!-- tag: obj-oa7 -->
## OA7 — P4. Abolishing property income does not abolish class

**Attacks:** the "surgical, keep functional institutions" positioning in §8; constrains OP-1 (service → influence).
**Sources:** [Albert & Hahnel on the coordinator class](https://znetwork.org/znetarticle/parecon-and-anarcho-syndicalism-an-interview-with-michael-albert-by-michael-albert/) · `GLOSSARY.md#src-participatory-economics`
**Status:** 🟠 **Weakened but alive.**

Parecon's central historical claim: Soviet-type systems abolished capitalists and produced a new ruling class anyway — a **coordinator class** monopolising empowering work.

> **⚠️ What v0.3 got wrong.** The register previously argued that *"OP-1 converts service credit into influence."* **That argument is void.** There is no separate service credit, and credit tracks **hours, not material throughput**. A carer's hour and a steelworker's hour confer identical weight. **No credit-accumulation flywheel exists.**

**What survives.** The coordinator-class risk was never *only* about income. It is about **who holds empowering work**, and **§8 deliberately keeps existing institutions** — municipal government, planning bodies, civil service — precisely the institutions in which conceptual and agenda-setting work is concentrated. Removing profit does not redistribute *that*.

> **⚠️ Weakened further in v0.8 — the *employer* form is structurally hollowed out.** The credit-realization session established that the wage-extraction employer has **no mechanism to exist**: no transferable credit → **no wages** (A3 (non-fungibility)); nothing may be added to a cost figure → **no surplus to appropriate** (A5 (cost, not price)); team debit shared **by hours, not rank** (§4.5) → **no rank-based risk- or cost-dumping.** Two attempted exploits died here: **mislabeling** pledged-vs-speculative work to recruit or shed risk is defused because the label is **read off the public pledge ledger, not declared** (§4.7, §4.6); and **"labour bears demand risk"** is bounded because unsold-run risk is shared *symmetrically by hours* (a worker's share equals a supervisor's), is *informed* (transparency shows demand before committing), is mostly *pledged* (cushioned by committed demand — and under Foundations v0.14 a pledge is *permanent*, so the cushion cannot be withdrawn mid-run), and is *floored* (§5.5). **What is left of P4 (coordinator class) is only the pure *coordination* residual** below — not the boss.

**The new residual, introduced by pledging.** Pledging power accrues per hour worked, equally for everyone — egalitarian across *sectors*, but weighted by **hours available to work**, which is not equally distributed. Caregivers, part-time workers, the disabled, and the chronically ill hold systematically less say in what gets produced. **Live and unaddressed.**

> **A second seniority-weighted channel was avoided, not opened (v0.15).** The contingent reserve (§4.6) splits a task's pledged cover **pro-rata by hours *on the task*** — deliberately *not* by whole-co-op-history hours, which would have let long-tenured members skim cover from work newcomers actually did (a fresh P4 surface). Task-scoped splitting keeps the cover on the doer.

**Consequences for OP-1:** *proposal power with universal suffrage* is the only candidate that structurally separates agenda-setting from deciding. Parecon's **decision weight proportional to how much you are affected** is a fifth candidate, and it does not accumulate at all — the best available answer to the hours-inequality residual.

---

<!-- tag: obj-oa8 -->
## OA8 — OP-9 / P5. Preference revelation

**Attacks:** A5 (cost, not price), A1 (materialism of cost). The Mises/Hayek line of attack — the objection every economist brings first.
**Sources:** [Mises (1920)](https://mises.org/library/economic-calculation-socialist-commonwealth) · [Hayek (1945)](https://www.econlib.org/library/Essays/hykKnw.html) · `GLOSSARY.md#src-neurath-calculation-in-kind` · [Dapprich](https://brightagebeyond.com/wp-content/uploads/2022/05/dapprich-philipp-2021-optimal-planning-with-consumer-feedback-a-simulation-of-a-socialist-economy.pdf) · `GLOSSARY.md#src-kantorovich-shadow-prices` · `GLOSSARY.md#src-cockshott-cottrell-labour-time`
**Status:** 🟢 **Written up (v0.10). Standing statement: `00-strategy/open-problems/OP-9_calculation_reply.md`.** Plain-language version in Overview §9. Answered for cost; one residue terminates in OP-10 (below).

Cost says what a thing takes. It does not rank two people who both want the last one. The full four-move reply is the standalone doc; the register keeps the summary.

**The four moves:**

1. **Cost ≠ value.** Mises's argument is that you can't rationally *value* producer goods without a market. Aequitas concedes it entirely and doesn't need it — it computes cost (physical, measurable in mass/energy/seconds), never worth. The refutation aims at a target Aequitas doesn't occupy.
2. **Pledges supply the demand signal** (Foundations §4.6) — decentralized preference revelation with no prices, no central optimizer, and **no Iteration Facilitation Board.** A price fuses "what it took" and "how much wanted" into one number that then can't be separated; Aequitas keeps them apart by design.
3. **Tractability is settled — cite, don't re-prove.** [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) ran in-kind calculation at national scale with sparse-matrix methods; the recursion sim (`06-simulation/allocation-engine/RECURSION_RESULTS.md`) is a second instance. Retires the *computational* form of the Mises objection.
4. **Scarcity-as-debit handles rationing.** On [Kantorovich's](https://www.nobelprize.org/prizes/economic-sciences/1975/kantorovich/lecture/) objectively determined valuations, a shadow price is the **cost of a binding constraint**, not a margin extracted by a seller. **Recorded as debit rather than skimmed as margin, this is compatible with A5 and arguably required by A4 (no externalities).**

**P5 (preference revelation) — the Cockshott variant.** Their demand lever is the *gap* between market-clearing price and labour value. **A5 collapses that gap to zero by construction**, so Aequitas inherits their problem with one fewer instrument. **Pledges are the replacement** — and a cleaner one, a direct expression of demand rather than a residual inferred from a price.

### Move (e), added 2026-08-24 — the price being defended is not an honest signal

**Two outside economists re-opened OP-9 on the scarce-goods question** (`openai/gpt-5.4` #2, `deepseek/deepseek-v4-pro` #5): *pledges plus "route it to local distribution" relocate the knowledge problem rather than solve it.* **The author's reply refuses the ground rather than contesting it.**

> **Every version of the objection assumes a price is an honest reading of preference. In a concentrated market it is not.**

| The assumption | What is actually the case |
|---|---|
| Scarcity is physical and the price reports it | **Much scarcity is produced.** Supply is withheld to hold the number up. |
| Demand is a given fact the price reports | **Demand is manufactured at industrial scale.** That is what advertising is. |
| Therefore the price reports preference | **The same firms set supply and work on demand.** The price partly reports its own producer. |

**This is Braudel's two layers, and it is economic history rather than ideology.** Market towns price from below; above them a few large operators **set** prices instead of taking them. [DeLanda's summary](https://nettime.org/Lists-Archives/nettime-l-9610/msg00025.html): capitalism *"has always engaged in anti-competitive practices, manipulating demand and supply in a variety of ways."* **He calls that layer an anti-market.** Research note: `02-research/DeLanda_markets-antimarkets_v0.2.md`.

**This is the demand-side twin of move (a).** Aequitas declines to compute *value* and computes *cost*; it likewise declines to infer demand from a number the seller helped write.

**What a pledge does that a price cannot: it cannot be advertised into existence.** It is backed 1:1 by hours the pledger worked, spent once from a lifetime budget, and public. **A seller can raise desire. A seller cannot raise the hours in someone else's day.**

**And the lever's concentration is measured, not asserted:** money's top tail reaches ≈ **10⁶ ×** the median (SCF 2022 + Forbes); Aequitas's pledging power is bounded by **24 ÷ F ≈ 2.4 ×**, and every living person holds some because self-care credits everyone. **The demand lever moves from an unbounded distribution to one bounded at about 2.4 ×.**

**Worked examples in Foundations §4.6** — four 0.5 h pledges cover the ≈2 h of work to shelve an extra box of radicchio; 5,000 likes convert to 500 h of pledged debit-room against a 300 h need, with the surplus becoming a non-consumable reserve under §4.6 rather than a bonus. **Design finding recorded there: a flat rate per like does not discipline anything** (54,500 likes a year before the budget bound) — **the sound preset is a share of a budget**, which normalises itself.

**Two checks passed.** Likes-to-pledges does **not** breach **OP-8**, because a pledge is not credit and §4.2's bar is on *credit* realising from feedback. It does sit on **OP-6 (feedback mechanics)** — whoever is already liked attracts most pledges — **which is the existing open problem, not a new one.**

> **⚠️ Stated as a tendency, not a taxonomy.** Real small-producer markets also carry unequal information and local monopolies. *"Markets are fine, capitalism is the problem"* is tidier than the truth. **For an academic write-up cite Braudel directly; keep DeLanda for the popular text.**
>
> **And move (e) does not answer the last-unit question.** Two people, one radicchio. **Pledges decide how many are grown, not who gets the last one.** That stays with distribution at the point of hand-over (§5.5). **Move (e) attacks the premise that a price was doing that job honestly; it does not claim to do the job itself.** The **objective-function residue** where a scarcity constraint spans the whole economy is unchanged and stays OP-10 business.

**⚠️ The one residue — it terminates in OP-10, and is registered there, not claimed closed.** Move 4's dual price requires a primal optimisation, which requires an objective function — **straight into OP-10 (weighting governance).** The clean form is to *federate per-constraint* (most scarcity is local — this lake, this ore body — with a local physical shadow cost needing no economy-wide objective), and to route physically-scarce *outputs* to distribution (lottery/queue/pledge-priority, §5.5) rather than to cost. That plausibly dodges the objective function, but is **unproven where a constraint spans the whole economy.** Separately, **Hayek's tacit-knowledge point** is only partly answered — but it is an objection to central *planning*, which Aequitas is not (it keeps books under a decentralized market), so it need only avoid recreating the problem. Both residues are OP-10 business.

> **⚠️ Sharpened in v0.5, enforced in the write-up — the OP-17 (joint production) session confirmed the danger.** A demand-contingent allocation rule was proposed and rejected: splitting a steer's debit by which cuts are sought-after makes two identical steers in two towns carry different splits, which **fails universality and is price allocation in costume.** The general lesson: **whenever demand is invited into the cost side, check whether A5 has been reintroduced under a new name.** The OP-9 reply keeps scarcity strictly as a *material* cost — this is the guard the standalone doc is built around.

---

<!-- tag: obj-oa9 -->
## OA9 — OP-22. Minimum audit disclosure

**Attacks:** §4.7. **Status:** 🔽 **Narrowed from a foundational conflict to an implementation question.**

> ### 📌 THE SPLIT WAS PROPOSED AND REFUSED — author ruling, 2026-08-25
>
> **@cairn-lineage (c18679, 1f916.ai #2000) argued that a privacy proof showing a ledger is *"backed by X hours"* does not show the same person and day appear in no other ledger, so OP-22 needs a non-reuse witness and should split into OP-22a and OP-22b.** The outreach agent conceded it in public at c21149.
>
> **Ruling: OP-22 is NOT split. OP-22b is NOT opened.** Full paper, with the arithmetic: [`OP-22_identity_not_disclosure_v0.2.md`](open-problems/OP-22_identity_not_disclosure_v0.2.md).
>
> **Their falsifier builds and proves nothing.** One person, one Monday, 8 hours worked. Network A at a 4 h floor records **12** credited hours; Network B at a 10 h floor records **18**. Two valid private ledgers hold the same person and day. **12 + 18 = 30 hours in a 24-hour day, which IC-7 forbids — and no party computes that sum**, because no book is ever added to another and a transaction lands on exactly one network the seller picks (Foundations §4.0).
>
> **The non-reuse witness they asked for is C6 (identity), and it is a merge precondition.** Two networks merge by agreeing every rule, identity included, so face-plus-fingerprint-plus-voice cannot merge with an RFID card scan (§4.8). **It is not a disclosure primitive and it is not part of OP-22.**
>
> **They were right about the ceiling, and that half was ours.** §5.5's old condition 5 claimed the bound held *"across any set of networks compatible enough to interoperate"* and that compatible networks *"arrive at the same ledger."* **Both are struck, not narrowed** (Foundations v0.23). §4.2 contradicted the second on purpose — *comparison, never conversion*.
>
> **⚠️ And one thing may NOT be said, because a draft of the paper said it and the author refused it on 2026-08-27.** A person with accounts on a 4 h-floor and a 10 h-floor network does **not** reach *"36.0 h of room against 12.0, a factor of 3.0."* **That line adds A's hours to B's, and the two are collapsed through different weighting models**, so the sum sets an exchange rate between credit-standards — **A3**, **§4.2**, now **conformance 4a**. **IC-7 was never breached: 12 and 18 are each under 24, and it binds each account separately.** **What is actually left is a coverage question** — activity one network cannot see — covered by §4.4's published coverage figure and §4.4's residual estimate, which errs against the person. **Watch item, not a blocker: is that tight enough against deliberate splitting? Unmeasured.**
>
> **What stays open here is unchanged:** the minimum disclosure set. Its sharpest live form is proving a **pledge's** backing across a model boundary — *"backed by X hours under weighting model M"*, in zero knowledge (§4.2).

The correct bar for attribution is **no worse than today** — a gallery buyer already has no proof the artist painted the work — and provenance only becomes fraught in the capitalized art market that A5 (cost, not price) removes. On privacy, the world already runs counterparty-visible and third-party-opaque, and Aequitas replaces neither courts nor social pressure.

**What survives is narrow and technical.** Banking externalizes validation to institutions; **Aequitas has no institution to externalize to.** So: **what is the minimum an auditor must see to verify a claim without seeing a history?** Zero-knowledge proofs are the right shape; the disclosure set is not specified. **C7 (privacy layer).**

> **⚠️ More load-bearing after v0.8.** The credit-realization session established that Aequitas is **radically transparent at the market level** (pledges, production, hand-offs, debit-costs are public — the pledger anonymous but the pledge visible) and **private at the person level** (Foundations §4.7, "market-public / persons-private"). That public market data is what makes §3.3a rival-sector audit, independent economic monitoring, and the anti-mislabeling defence (§4.6) *work at all*. **But it depends on OP-22 (audit disclosure) being solved:** public pseudonymous events can be chain-analysed to de-anonymise a person. So OP-22 is no longer only about a single auditor's disclosure set — it is the enabling condition for the whole transparency story. Right shape (zero-knowledge / unlinkability); mechanism unspecified. **C7.**

---

<!-- tag: obj-oa10 -->
## OA10 — The auditor-independence problem

**Attacks:** the trust-network model (Level 2), and therefore C2 (verification / trust networks).
**Sources:** `GLOSSARY.md#src-auditor-independence` · [Arthur Andersen](https://en.wikipedia.org/wiki/Arthur_Andersen) · [Sarbanes–Oxley](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act)
**Status:** 🟠 **Partly answered by a cheap structural rule. Full trust-network design deferred.**

*"Trust networks compete on accuracy, because accuracy benefits their subscribers."* **That claim does not survive contact with the record.** Subscribers do not want accuracy; they want a favourable assignment. Every issuer-pays rating arrangement in history has drifted the same way, and **removing the profit motive does not fix it, because the conflict is directional rather than monetary** — a client-owned Arthur Andersen would have been worse than the one Enron paid, not better.

**The cheap structural answer, adopted in Foundations §3.3a and §10.1:**

> **A trust network whose membership is concentrated in the sector it audits is captured by construction.**

In Aequitas everyone is both producer and consumer, so a **general-membership** network is dominated by the consuming side for any particular good, and its incentives align against that good's producers automatically. Only **sector-specific** networks fail this way. And membership composition is public in the log, so this is a **detectable screening property, not a rule anyone must enforce.**

**What it costs:** the fix creates **OP-24 (understatement drift)** (OA3 (understatement drift) above) — consumer-dominated networks are biased toward understating what their members consume. The two findings must be read together; neither is safe alone.

**Deferred:** the shape of trust networks generally — funding, membership, competition, dispute handling — is **C2 work and explicitly not settled here.** Author's decision, 2026-08-01.

---

<!-- tag: obj-oa11 -->
## OA11 — OP-25. Illicit end-of-life dumping

**Attacks:** A4 (no externalities), at the disposal end.
**Status:** 🔽 **Minor / deferred to the Level-2 trust model.**

Foundations §3.6 prices *lawful* disposal correctly: an unwanted asset's end-of-life debit falls on its last holder, and a discarded product is a stock-weighted pollutant. The incentive is to recycle or remediate, because doing so lightens the holder's own pollution-debt (§3.3).

**What it does not close:** *abandonment.* Someone facing a worthless asset's permanent debit can fly-tip it, escaping the debit if the abandonment is never attributed to them. This is the same shape as any Level-2 attribution problem — provenance plus witness — and it is **not a foundational contradiction**, because the incentive structure is already correct for anyone who stays inside the record. Registered so it is not mistaken for solved. **C5/C7 territory, with the identity and provenance machinery.**

---
---

<!-- tag: obj-oa12 -->
## OA12 — OP-26. The coverage gap

**Attacks:** the trust-free claim about arithmetic on the record, and through it A4 (no externalities).
**Source:** [@cairn-lineage](https://1f916.ai/post/1581), c14985, 2026-08-22, replying to [#1605](https://1f916.ai/post/1605) on 1f916.ai. Conceded on the board at c14987. Full paper: `00-strategy/open-problems/OP-26_coverage_and_closure.md`; verbatim in `07-outreach/memory/objections.md`.
**Status:** 🟠 **Largely answered. Two residues open.**

> Arithmetic can prove consistency of the supplied log; it cannot by itself prove that the supplied log exhausts the world-domain. An omission that leaves the supplied subset internally closed needs some independent sequence, extent, or closure witness. So I would phrase the obligation as **coverage**, not global source totality.

**This is the first objection to Aequitas raised from outside the project**, and it arrived with a fix-shape attached: a load-bearing check must know its intended domain, its returned extent, what proves closure, and how to downgrade when that proof is absent.

**The over-claim, corrected.** The claim was that an unrecorded emission *becomes an arithmetic error*. True of an **under-declared** emission on a **recorded** event; false of a process recorded nowhere. **Narrowed on 2026-08-22, and the narrowed form is Foundations §4.3** — arithmetic over a set testifies to nothing outside the set, so a fully unrecorded chain is a coverage question (§4.4), not an arithmetic error.

**The blast radius is small.** IC-3/IC-4/IC-5/IC-6 already force closure over everything the log *touches* — delete a recorded event and its inputs lose their fate, its outputs lose their ancestry. What survives is only a fully disjoint chain: unrecorded extraction → off-ledger transformation → off-ledger sink. **That is a participation boundary (§4.1), not a hole in the checks.**

**The closure witness was already in §4.4** — *N*, the independently-known physical total, reconciled against the ledger's sum. It asserts nothing about anyone's honesty. **Third time an imported problem was already implied by an axiom** (after A3 for circulation-failure and A2 for joint production); this time the failure was organisational, not theoretical — §4.4 sits in "Identity", the constraints sit in "Integrity", and nothing connected them.

**The shape of the answer, which generalises:** a closure witness is **neither an assertion nor a proof — it is a citation.** Method, provenance, vintage, extent, uncertainty, and an obligation to recompute every affected ledger when it improves (§3.3). Science has no closure witnesses either; it has methods sections. The defence against a fabricated citation is **independent testability**, not a gate at write time: no record is purged, challenged records are annotated (conformance row 6), and **a divided estimate must reconcile against its parent** (conformance row 10d) — so a fabricator, who cannot choose which sub-extent gets measured next, is exposed arithmetically.

**Folded in v0.17 / Foundations v0.17:** the extent rule · the floor rule · the conservative-count rule · coverage rides §3.3 recomputation · rival-sector audit extends to coverage · the transaction-time rule · the provenance block · a tally is an event · IC-12 generalised to tallies.

### The 2026-08-24 outside pass — four folded, six already answered

A second wave of critique arrived on 1f916.ai against posts #1605, #1750 and #1581. **The useful output was not evenly distributed, and the split is the finding.**

**Folded into Foundations v0.20:**

| Source | What it found | Where it landed |
|---|---|---|
| [@cairn-lineage](https://1f916.ai/post/1581) c16488 | ***N* and *Y* must be scope-aligned before you subtract.** Same quantity, same boundary, same window, error bounds smaller than the difference. Our spec stated two conditions on the residual rule and never this one. | **Foundations §4.4** (third condition, boxed explainer + worked case) · conformance **14a** |
| [@heresy-ai](https://1f916.ai/post/1605) c15491 | **The sorting question:** *does this check compare two things made on separate paths, or a thing to itself?* Sharper than the log-side/projection-side cut this register used. | **Foundations §4.4** (boxed explainer + worked case) · conformance **14b** |
| [@custos](https://1f916.ai/post/1750) c16467, c16479 | **The ladder has no cost column.** Every witness has a running price; *"what kind of second witness"* is really *"what are you willing to pay to be told."* Three omission classes, each needing a different witness. | **Foundations §4.3** (cost table, the ~40% ceiling restated where the choice is made). **The finding stands; the conformance row does not** — 14c was deleted on 2026-08-28 because audit work is credited work, so its hours are already events in the log. |
| [@manu](https://1f916.ai/post/1750) c16894 | **Independence is not expressiveness.** A balanced fabrication is invisible to conservation checks on *any* record however sourced. What defeats it is physicality. **An attacker who controls the instrument wins and nothing downstream can tell.** | **Foundations §4** (boxed explainer + worked case; trust relocated to the instrument, said plainly) |

**Not folded — the document already said it.** These were conceded or celebrated on the board as new, and were not:

| Source | What it said | Already written, since |
|---|---|---|
| [@denominator](https://1f916.ai/post/1605) c18425 | *"The mass/energy denomination is your closure witness — build it out."* | **§4.4 names *N* "the closure witness" in those words.** v0.17. |
| [@second-source](https://1f916.ai/post/1605) c15059 | A wrong constant baked into the schema at spec time | **OP-24** understatement drift + **§3.3a** rival-sector audit |
| [@cairn-lineage](https://1f916.ai/post/1581) c15002 | No authority-free closure witness for an open population | **§4.4**, ruled 2026-08-22 |
| [@zpk](https://1f916.ai/post/1589) c14980 | A passing check must publish what it could detect | **§4.4** floor rule + conformance **16**, the extent clause |
| [@ellie-v2](https://1f916.ai/post/1605) c15053 | Publish a negative fixture for an *unrecorded* emission | Same finding as @denominator c15040, one day earlier. Fold once. |
| Outreach agent, `#2000` | *Max-vs-sum:* a truncated population flatters an extremum | **§4.4 floor rule** and **conformance requirement 13**. An incomplete count is a floor, never a value. |

> **Two things follow, and the second matters more than the first.**
>
> **(1) One genuine addition hides in the last row.** §4.4 states the *direction* — under-recording can only understate. It does not state the *consequence*: **a low sum reads as alarming and gets investigated; a low maximum reads as a good result and does not.** One sentence, not a mechanism.
>
> **(2) The cause was organisational.** `07-outreach/archive/` holds a copy of Foundations. **The brief never told the agent to read it.** So the project spent public credibility conceding six points its own documents settle. **This is the seventh time an existing axiom or section already held the answer** — after A3, A2, §4.4, §4.7, A7 and the five sections of OP-27. The failure mode has now recurred often enough to be predictable, and the fix is procedural rather than theoretical: `AGENT_BRIEF.md` §4 now opens with a mandatory whole-document read.
>
> **Credit where it is due anyway.** A critic who independently reaches a settled ruling from their own evidence — @custos arriving at §4.4 from treasury receipts — has produced a **replication**, which §3.3a says is the thing that actually disciplines a method. That is worth more than a novel objection, and the register should stop treating "we already knew" as though it diminished the finder.

**Two residues, both open:**

1. ~~**Who carries the residual `N − Y`?**~~ **SETTLED 2026-08-22 — Foundations §4.4.** **Nobody, yet.** The residual is computed and published but assigned to no account; a dark producer's share is **back-traced to them when they onboard**, which is also the only way they can transact. A4 is **pending**, not abandoned, and the damage is already priced through §3.3's ambient stock — participants pay a rate reflecting total damage for their **own** units only. The §3.3a OP-24 relief was **corrected**: it never needed the residual allocated. Its two funders are the **rival producer** (harmed by cheap undocumented goods) and the **dark producer** (who cannot transact until onboarded). **The back-trace horizon is also settled (§4.4): birth.** It is not a penalty because it is **symmetric** — a lifetime of estimated consumption arrives with a lifetime of self-care credit, and at ≈ 3,650 h/yr credited against ≈ 1,380 h/yr consumed, **onboarding is a windfall for a median person**. It costs only those whose lifetime consumption genuinely exceeded their contribution, which is correct targeting. Evidence is voluntary, moves the figure either way, and may arrive later and re-derive the ledger (A6 + §3.3). §4.1 is untouched — nothing is charged before onboarding — and the transaction-time rule is untouched, because pre-onboarding acts were never gated by Aequitas: **a position is reconstructed, not a verdict on past conduct passed.**
2. **The population half routes to C2.** Who does the tallying work and who funds it; and how a *competing* tally is adjudicated — §3.3a's two-replication rule is a bar to clear, not a dispute procedure. **This is now a requirement on the trust-network straw-man.**

**Candidates raised and REJECTED the same day** (stress-test 2026-08-22). **IC-13 (genesis admissibility)** refuses the ordinary case — a non-participant produces after a network's epoch and sells in, which is the normal onboarding path — and is toothless anyway, because founding a network today makes everything on Earth predate its epoch. **IC-14 (citation closure)** demanded *a* citation, not a true one, and was redundant with the requirement that every estimate carry its basis, method, vintage and extent (conformance row 12). **Neither was arithmetic on the log**: IC-1…IC-9 check recorded quantities against other recorded quantities, while these check a self-asserted field against a constant — shipping them would have re-widened the very claim this version narrowed.

**What replaced them, and the general lesson.** A **weighting rule**: a genesis entry's creation-cost is drawn from the cohort residual at the end **unfavourable to the admitter**, so admitting a good via genesis is never cheaper than recording it honestly. And a **mandatory field**: the provenance block, so "unsourced" is refused at write time. **Price the dishonest path rather than forbidding it at a door somebody has to guard** — the same move as §4.4's *darkness stops paying*. ⚠️ **Owed: a sim** comparing launder-via-genesis against honest recording; the fix only holds if the conservative estimate genuinely dominates.

---

<!-- tag: obj-part-b-answered -->
# PART B — ANSWERED

**The answer sheet.** Every item here will be raised again by someone who has not read this document, and most of them are the academic paper's strongest material. Do not file this away.

---

<!-- tag: obj-b13 -->
## B13 — OP-27. Parallel implementation ✅ **RULED AND STRESS-TESTED**

**Shipped:** Foundations v0.19 §4.8. **Source:** the author, 2026-08-23. Full paper and stress test: `00-strategy/open-problems/OP-27_parallel_implementation.md`.

**The objection.** *Aequitas has to be usable by someone who still uses money, as an alternative that does not exclude them.* §11 and §4.8 both assume an answer; neither works one out. **Every participant, for years, will have most of their counterparties outside, so a design that only works once everyone is inside cannot get anyone inside.** This attacks **fecundity**, which is one of the three criteria in §2 rather than a nice-to-have.

**A sharper form was raised and it fails.** §3.2 says handing an object outside produces no event, so the seller keeps its debt-load. §3.2b says consumption debit stays with whoever caused it. For a sale to a non-participant these look contradictory, and if §3.2 wins then outbound debit scales with output while credit is capped at 24 h/day (IC-7) — so a producer selling mostly outward crosses `D > ρ·C` and is locked out *for succeeding*.

**Three reasons the conclusion is wrong.**

1. **They govern different debits.** §3.2 is **property** debit, dischargeable on transfer. §3.2b is **consumption and pollution**, which never transfers. An outward sale is a property question and §3.2b was never in play.
2. **A locked-out seller is not deprived — they got money.** The gate restricts discretionary consumption *inside Aequitas* and never touches essentials (§5.5). They have not been impoverished; they have declined to be inside, which is what a parallel system means.
3. **It reverses.** Property debit discharges the moment a real holder takes the thing (§3.2), so one batch sold inward lightens the ledger. **A gradient, not a trap.**

> **And the debit-dumping counter disappears with it**, because it only existed under an A7 reading — *treat a non-participant as an estimated account that can receive* — which the ruling rejects. **If handing a thing outside never discharges its debit, there is nothing to dump.** OA11/OP-25 is untouched.

**The ruling.** Both directions are deliberately costly and neither is forbidden. **Into Aequitas:** a money-made good is dark until sold in, and clears at the hand-off by full onboarding *or* a **pre-approved published template**; the maker spent money and receives none. **Out of Aequitas:** permitted, **the debit stays with the seller**, and the network treats it as a **gift** and does not acknowledge the money at all.

**Nothing new was invented, which is the sign it holds.** Money's invisibility is **A1's corollary**; the dark estimate is **§4.4**; the retained debit is **§3.2**; the gift is **§4.8**; the fate closes as **§3.6** already closes it. **The only new object is the template, and it is a cache rather than a mechanism** — carrying two inherited rules: it **errs against the seller** (§4.4's conservative-count rule) and it is **published with method and vintage** (§4.7).

**Stress test — what survived.**

- **Money cannot buy Aequitas standing, at any scale.** Pay a hundred workers in money and sell the goods in: **the workers are credited their own hours** (A2, A3, Ellerman-imputation under A1) and **the financier is credited nothing.** IC-7 caps every account at 24 h/day regardless of who paid. **The boundary is permeable to goods and impermeable to standing.**
- **Extraction self-limits.** Buy inside at cost, sell outside at market, disregard the ledger. Buying **takes on** property debit; selling outward **never discharges it**; so `D` grows with every unit extracted while `C` grows only with the extractor's own capped hours. **`D ≤ ρ·C` fails and the extractor can no longer buy the inputs they were draining — faster the harder they pull.** Nobody enforces it.
- **Template shopping across networks** is OA-familiar: **OP-14 cohort shopping**, arrested by counterparty re-computation (§4.2, *comparison never conversion*).

**Two items enter the register open, and both are routed rather than orphaned.**

> ### ✅ CLOSED 2026-08-24 — repeat-shell entities. Read this before the table below.
>
> **Two outside economists (`openai/gpt-5.4`, `deepseek/deepseek-v4-pro`) independently said this register under-rated the shell gap**, and they were right about its size: **the trades most exposed to the money boundary are the ones normally organised as businesses** — haulage, warehousing, shops, building work, farm co-operatives. Both asked for OP-27 to be downgraded from closed to partly answered.
>
> **Author ruling, 2026-08-24: the gap is closed, and A1 already contained the answer.** Under A1 only people act. A co-operative never lifted, drove or burned anything — its members did. **So an organisation cannot be the final holder of a debit**, for the same reason a barn cannot (A5/§4.5) and a power station cannot (§3.2b).
>
> > **An organisation's account is a view of its members' positions, not an owner of them. Its debit is at all times the debit of the people who worked there, divided by hours worked. Closing it moves nothing.** Foundations v0.22 **§3.2c**, conformance **2c**.
>
> **Worked: 10 members, 2,000 h each, a shell taking 24,000 h of debit per round.** Each member carries **2,400 h** after round 1, **4,800 h** after round 2, **24,000 h** after round 10 — and their own gates begin to bind. **A new shell resets nothing.**
>
> **No new rule was needed.** §5.1 already shared team debit **by hours worked, not by rank**, and §4.6 already split a task's pledged cover **pro-rata by hours on the task**. §3.2c states the same thing about the organisation as a whole.
>
> **Three notes kept for honesty.** (1) This is a **declared convention, not a measurement** (§1.1) — hours leave no trace pointing at a particular debit; hours are chosen because they add no new lever. (2) It **does not touch §4.5**, where an asset's creation-cost splits by *holding time* so a new hire bears about zero — that is property debit on an asset, this is consumption and operating debit. (3) It **may also close §3.4a's open residue** (apportioning a jointly-caused debit across a team), which has the same shape and now has the same answer. **Not claimed until checked.**
>
> **What is left is not accounting.** A person could hide behind a **fake or borrowed membership list**. That is a verification problem for **C6 (identity)** and the §4 ladder.
>

| Residual | Where it joins |
|---|---|
| ~~**Repeat-shell entities**~~ — **CLOSED 2026-08-24**, see the box above. §3.2c makes an organisation's debit its members' debit, so a chain of shells cannot reset a gate. Residue is a fake membership list. | ~~OA11 / OP-25~~ → **C6 (identity)**, verification only |
| **Template capture** — whoever sets a template sets the entry price for every dark good in that class; set it low and money-economy goods undercut the producer who paid to instrument their supply chain. | **OA3 / OP-24** and **OA2 / OP-10**. Inherits OP-24's answer: the rival producer is the harmed party who funds the replication (§3.3a). |

**Why this one closed in a day when OP-26 took a session.** The answer was distributed across five sections that had never been read against each other. **That is the sixth time an existing axiom already held the answer** — after A3, A2, §4.4, §4.7 and A7. The failure mode is organisational rather than theoretical, exactly as OP-26's was.

---

<!-- tag: obj-b7 -->
## B7 — OP-17. Joint production ✅ **CLOSED for materials and energy**

**Shipped:** Foundations v0.4 §3.4a, §3.2a, §1.1; IC-10, IC-11 and IC-12 (now conformance rows 10b, 10c, 10d).
**Full argument:** `00-strategy/open-problems/OP-17_coproduct_allocation.md`
**Sources:** [Sraffa/Steedman/Morishima on negative labour values](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) · [ISO 14044 allocation critique](https://link.springer.com/article/10.1007/s11367-016-1161-2) · `GLOSSARY.md#src-joint-production-allocation-problem`

**The objection.** A process yields beef and leather, or a refinery's full fraction slate. One physical event, several outputs, one pool of debit. Splitting by mass, energy content, exergy, or economic value gives **four different answers, none more physically true than the others.** ISO 14044 ranks the options and then falls back to **market price**, which A5 (cost, not price) forbids. The classical form is sharper: under joint production, labour values can go **negative**.

**Why it looked unanswerable.** Both literatures searched for a **carrier quantity** — a property of the *outputs* by which cost could be apportioned. Every candidate works in some industries and is a category error in others.

> ### ⚠️ NARROWED 2026-08-24 — "measurement, not convention" was overstated. Read this first.
>
> **The mechanism below is unchanged and still closes OP-17.** What was too strong is the claim made for it.
>
> **The finding** *(economist review, `openai/gpt-5.4`, #24)*: the recursion result proves no split produces a negative figure **given** a split matrix. **It does not prove the split is unique.** A refinery can be read by process enthalpy, by mass per line, by hydrogen use, or by sub-metering, over different windows; a livestock case still aggregates labour by an inherited rule. **Those are choices about instrument, period, and boundary.**
>
> **Accepted, and the correction is sharper than the one proposed.** The critic asked for the label *"measurement-constrained convention."* The author's ruling goes further and says what follows from it:
>
> > **Aequitas fixes the obligations on the split. It does not fix the method, and it cannot — no single model fits every industrial process.** Determining how a process divides its inputs takes expertise in that process. **The method belongs to the industry, under §1.2's scope rule: state what must be true, never how to build it.**
>
> **The obligations, now stated as such** (Foundations v0.22 §3.4a, conformance **10a**): measure at the facility for the period described, before any model · compute per dimension before collapsing (§3.2a) · **publish the method with its version** (§4.7) · never let demand, desirability, or yield enter.
>
> **The publication requirement is new and it is the one that mattered.** §4.7 required publication for estimating numbers and §3.3a for cost constants. **Splits fell through the gap** — so the instrument choice was a lever with no guard on it. It now has the same guard as everything else: **the rival producer, harmed by a flattering method, funds the recheck** (§3.3a). A rival cannot challenge arithmetic they cannot see.
>
> **Registered, not solved:** nobody has measured **how far a split actually moves** across honest methods. Test owed — §C. **If the range is narrow the obligations suffice; if it is wide, method choice belongs with OP-10.**
>

**The answer.**

> **A joint process's debit divides according to where the process itself physically sent its inputs.** The instrument is whatever that process makes traceable — tissue-deposition energetics for an animal, cracking enthalpy for a refinery, the extraction curve for a turbine. **These are not rival conventions; they are different instruments reading the same underlying quantity, which is hours (A2 (time as measure)).**

**Why Aequitas can say this and the LCA literature cannot: it has a universal denominator and they do not.** Every physical quantity in the ledger is already a proxy for hours-to-produce or hours-to-mitigate, so the question "mass or energy?" — unanswerable as posed — never has to be asked.

**Tested** against a slaughterhouse (tissue energetics), an oil refinery (cracking enthalpy), and a CHP plant (turbine curve): one justification, three instruments, no case requiring its own excuse.

**Four things that fell out:**

| | |
|---|---|
| **Steedman is blocked, not inherited** | Nothing is inverted, so negative values do not arise: each share is a forward measurement of what physically went in. ✅ *Now derived, not merely asserted — the recursion is a non-negative Neumann series `p = Σ Ãⁿc`; simulation confirms `min(p) ≥ 0` across 4,098 productive economies while the value arm goes negative in ~95%. See `06-simulation/allocation-engine/RECURSION_RESULTS.md` and §C test 1.* |
| **Waste outputs are co-products** | Counting manure and methane in the split **removes the residual**, and with it the entire question of who absorbs an unwanted output. |
| **Fate sets ledger character; the process sets cost share** | Manure is pollution debit in a lagoon, a co-product in a biodigester, an observed fertiliser offset when spread. The allocation literature conflates these two questions. |
| **A §1.1 row was deleted rather than filled in** | The strongest possible outcome for a declared-convention entry. |

**What it did not solve, and says so:** **labour** (→ OP-18 (labour & team credit), which now blocks C3 (estimation engine)) and **shared overhead** (→ OP-23 (shared overhead)).

**Two rules that were rejected and why — both worth remembering:**
- **Aumann–Shapley marginal allocation.** Rigorous, but needs a domain condition ("is the plant dial-able?"), and its fixed-proportion fallback assumed a right to refuse custody that does not exist. **Also requires a cost function, i.e. an objective — re-opening OP-10 (weighting governance).**
- **Demand-contingent splitting.** Makes two identical steers in two towns carry different splits. **Universality failure, and price allocation in costume.**

---

<!-- tag: obj-b8 -->
## B8 — OP-23. Shared overhead ✅ **CLOSED — capital accrues to the asset, not the co-products**

**Shipped:** Foundations v0.5 §4.5 (computational-closure boundary), §4.5 (the capital-debit waterfall), §3.2b, §3.6, §5.2.
**Full argument:** `00-strategy/open-problems/OP-23_capital_and_pollution.md`
**Method:** design interview → stress-test (capital front-loading) → stress-test (the full waterfall) → adopted with changes.

**The objection.** The barn shelters the whole animal; the cleanroom serves every wafer. No physical trace runs from overhead to any one co-product, and the v0.5 interim rule — inherit the traceable proportions — was **thinnest exactly where overhead dominates** (capital-intensive manufacturing), and gameable by *overhead-stuffing*.

**The answer — don't allocate it.**

> **A durable asset holds its own creation-cost as property-debit *on the asset*. The full cost is holding-time-split among its holders; community pledges grant them debit-room that cushions the bite (they do not shrink the debit — nothing vanishes, A1). It never flows to the co-products at all.**

The barn stays on the farm operator; the fab stays on its cooperative; hide and beef and each wafer carry only their own consumables. **There is nothing to attribute, so there is no attribution convention to get wrong and nothing for overhead-stuffing to exploit** — the exploit dies with the allocation it was gaming. This is the same move that closed OP-11 (training amortization) and OP-21 (media reproduction): *a division problem dissolved by removing the division.*

**Why it does not leak (A4 (no externalities)).** The overhead debit is not lost; it is **located** on the asset and its holders rather than smeared across units. Honest trade-off, stated in §4.5: a per-unit debit-cost is therefore not a full-lifecycle figure.

**What the stress test changed before adoption.** The first residual proposal — split the un-pledged remainder *evenly* among current staff — **failed the second stress-test**: it imposed a perverse entry-toll on capital-intensive essential work (joining a hospital meant absorbing a share of its building) and tripped the dummy axiom. Replaced by the **holding-time split** (share = holding-duration ÷ total holding-duration), which starts a new hire at ≈0 and has a measurable basis. **The finding came from the adversarial pass, not the draft — the fourth session running where that held.**

**Three things that fell out** (all in `OP-23_capital_and_pollution.md`):

| | |
|---|---|
| **The computational-closure boundary** | Historical/capital costs cannot cascade downstream without regressing to the first human activity. Front-loading is what makes the accounting *terminate*. Pre-Aequitas assets enter at estimate/zero. |
| **Pollution and transport never transfer** | Only property-debit rides an item; pollution/transport stay permanently on the causer (§3.2b). This rewrote §5.2 to a direct producer-side penalty and resolved the recycling trace-forward paradox. |
| **The pollution baseline** | A flow is a pollutant only above the natural-remediation equilibrium; weight floats with the stock above it, unifying CO₂ and solid waste (§3.3, §3.6). |

**Spawned:** **OP-25 (illicit dumping)** (illicit end-of-life dumping — a Level-2 attribution problem) and an enlarged lever for **OP-24 (understatement drift)** (the new stock/baseline constants).

### The 2026-08-24 re-attack — *"capital exclusion contradicts A5"* ✅ **HELD. The axiom's wording was repaired instead.**

**Source:** outside-critique round, economist role, `deepseek/deepseek-v4-pro` — finding **#3** in the outside-critique report, **held locally and not published**. **The first finding in months that reached an axiom**, and it was right that something was broken.

> **The objection.** §4.5 rules that a durable asset's creation-cost never allocates to the co-products, so beef carries none of the barn. But A5 read *"the **price** of anything is its true, current-best-estimate material cost."* Barn 20,000 h ÷ 40,000 kg of beef over a 20-year life = **0.5 h/kg** of cost that Aequitas shows as **0**. **So beef's price is not beef's cost, and A5 fails.**

**Why the register's existing answer was not enough.** B8 said the cost is *"not lost — it is located on the asset."* **That answers where the debit lives and not what the critic asked**, which was about the number a buyer sees. Two independent models missed the reply, which is evidence the reply was never actually written down.

**The reply, in axiom terms.** *The critic's step is to assume the beef caused the barn.* Under **A1** only people act, so a cost attaches to whoever caused it and **a thing causes nothing.** Charging a beef buyer for the barn is the same error as charging a ring buyer for the miner's tailings — which **§3.2b already refuses downstream** and **§4.5 already refuses upstream** (the non-cascade rule). **Capital is the third face of one rule the document had already written down twice.** The sentence out of step was A5's, which located a cost on the *thing*.

**What changed and what did not.**

| | |
|---|---|
| **Changed** | **A5's wording** (Foundations v0.21). Three defects: it said *"price"* (nothing here has one); it never stated what counts as a cost *of the thing*, leaving §4.5's capital boundary out of the axiom it appeared to contradict; and *"true"* read as final, fighting §3.3 and A6. **A4 carried the identical defect** — *"every consequence is **priced into** it"* — and was repaired in the same pass to *accounted to whoever caused it*, which is what §3.2b, §4.4 and §4.5 already do. |
| **Not changed** | **The ruling.** §4.5's holding-time waterfall, front-loading, the non-transfer rule, B8's closure of OP-23. **No mechanism moved.** |

**Four exploits checked against the repaired axiom, all closed by existing machinery:** the **capital launderer** (reclassify a consumed input as durable) → §4.5 physical fate + IC-4, closed in v0.5; the **borrowed barn** (A builds, B uses) → §4.5 holding-time accrues to B, and there is no rent (§5.1); **scarcity re-entering cost** → *strengthened*, since the repaired A5 says cost is a record of physical inputs and outputs, giving the tenderloin ruling (B9) a cleaner ground than it had; **"A4 is being carved out"** → no, A4 requires every cost to land on **a** ledger, never on the **product's** ledger.

> **⚠️ The residue, now registered rather than buried in a clause.** Two producers of the same good — one with a 20,000-hour barn, one with a 2,000-hour shed — **publish the same per-unit debit-cost.** A buyer comparing debit-costs cannot tell them apart, because that figure answers *"what did this unit consume?"* and never *"what does this producer's method cost?"* §4.5 admitted this in half a sentence; it now says it plainly.
>
> **The answer is that capital discipline runs through the builder's own gate, not the price tag.** The 20,000-hour barn needs `20,000 ÷ 1.2 =` **16,667 hours** of credit standing behind it — **4.6 years of one person's entire credit accrual** at the self-care rate. **This is the same argument §5.2 already makes for pollution**, where the debit was likewise moved off the product onto the producer and the document argues the producer-side penalty is *stronger* because it does not depend on a consumer noticing. **The argument transfers unchanged. It is not new theory; it is a reply that had never been written.**

**Worked numbers, both cases:** Foundations §4.5, boxed. **Full plan and adversarial pass:** `99-archive/A5_repair_PLAN_v0.1.md`. **Paper §8:** `00-strategy/open-problems/OP-23_capital_and_pollution.md`.

> **And the lesson repeats.** *Eighth instance:* the material for the reply was already distributed across **A1**, **§3.2b** and **§4.5**, and had never been read against §4.5. **What was genuinely wrong was one sentence in an axiom that predated all three.** A register that only tracks *whether a ruling holds* would have recorded this as "already answered" and left the broken axiom in place.

---

<!-- tag: obj-b9 -->
## B9 — OP-18. Labour & team credit ✅ **CLOSED as the C3 blocker — team-credit dissolves, labour rides the material split**

**Shipped:** Foundations v0.6 §1.1 (labour-across-co-products row filled; team-credit row marked dissolved), §3.4a (labour convention + the cost-not-scarcity rule), §10.
**Full argument:** `00-strategy/open-problems/OP-18_labour_and_team_credit.md`
**Method:** opened → separated into two sub-problems → one dissolved against A2 (time as measure), the other resolved by the physical-trace test with the split basis chosen by the author, then axiom-scored and stress-tested.

**The objection.** Ellerman: responsibility for joint work is joint and non-decomposable — there is no fact saying the welder caused 40% of the bridge, nor how many of the farmer's hours are "in" the hide. OP-17 (joint production) split materials and energy by physical trace; **labour has no such trace.** C3 (estimation engine) needs per-product labour hours.

**The answer — it is two problems, and they close two different ways.**

> **(β) Team credit dissolves under A2.** Credit is *time worked* (§6). Each member is credited **their own hours** — the "40% of the bridge" number is never required. Credit was never a share of output; the objection conflated *credit-for-hours* with *share-of-responsibility*. The axiom already answered it. *(Residue: apportioning a jointly-caused debit — team pollution/harm — across members. Minor, non-blocking, sibling to OP-25 (illicit dumping).)*
>
> **(α) Labour across co-products gets a declared convention: it rides the process's material split.** No trace exists, so the physical-trace test *mandates* a convention — this is the first OP to close by declaring one rather than removing a division. The discipline: pick the convention that adds **no new capture surface.** Labour riding the already-measured, rival-audited material θ (mass/deposition for cattle, cracking-energy for a refinery) introduces no basis of its own and **changes no one's credit** — it only sets how each co-product's *debit-cost* reads.

**The load-bearing sub-decision — cost ≠ scarcity** *(the tenderloin case)*. A pound of tenderloin (≈1% yield) and a pound of hamburger (≈5% yield) **cost the same**, because each embodies the same feed, water, and growing-labour — refined only by *measured* tissue composition, never by yield or desirability. Weighting the rare cut as *more costly* is scarcity smuggled into cost, and it would ration that cut by **who can absorb the larger debit** — price-rationing by standing, the exact mechanism A5/§5.1 removes. **The scarcity is real and routed elsewhere:** to pledges/signals (how many cattle) and to decentralised local distribution (the butcher's lottery/queue/pledge-priority, §5.5). *Cost states what a thing took; who gets a scarce output is a distribution question, deliberately outside any central authority.* Method 2 (yield-weighting) was raised and rejected on exactly this ground.

**Axiom score (labour-rides-material-split).** Efficiency ✅ (shares sum to total), Symmetry ✅, **Dummy ✅** (manure ≈ 0 mass → ≈ 0 labour — the axiom that killed OP-23's even-split), Additivity ✅. **Exploit:** it amplifies the reward for faking the material split — but that is the existing rival-sector-audit target (§3.3a), no new mechanism.

**Universality is the win over Method 2.** Two identical cows in two towns get the **same** split, because nothing is demand-contingent — precisely the failure that "price allocation in costume" would introduce.

---

<!-- tag: obj-b10 -->
## B10 — Credit realization & the supply-chain hand-off model ✅ **PASSES WITH CHANGES**

**Shipped:** Foundations v0.7 §4.6 (pledge broadened), §4.6 (hand-off model), §3.2 (debit-taxonomy refined), §4.5 (deployment/transit), §4.5 (pre-Aequitas genesis), §3.7 (land remediation), §4.7 (transparency principle), §5.1 (employer hollowed out); IC-9, pledge discharge (now part of conformance row 9).
**Method:** adversarial design interview → author ruling → full stress-test pass. This is prime academic ammunition — the mechanism that makes "you are paid for work someone actually wanted" true without a boss deciding it.

**The ruling.** Production credit is always *recorded* (the event is logged; unpledged wheat still has a grower, A7/IC-3) but **realizes only on verification of the output** — *verification, not approval.* **For a physical good, each hand-off is that verification**, and is simultaneously (i) verification realizing the *prior* holder's credit, (ii) transfer of the material debit to the receiver, (iii) a new credit event for the receiver's own labour.

**Three exploits raised and all defused:**

| Exploit | Attack | What defuses it |
|---|---|---|
| **1 — Wash-trade** | Two co-ops swap goods, doing fake work, to manufacture credit | **Dominated by real work.** Real work *sheds* the debit (buyer takes it); a wash-trade *retains* it (make-and-keep nets ~zero, §3.2) and burns real overhead for nothing. Colluders end with ~zero net contribution, wrecked ratio, and debt they can only shed by dumping (→ OP-25 (illicit dumping)). Residual: gross fake hours → pledging-power → **OP-1 (service → influence)**. |
| **2 — Monopsony gatekeeper** | A sole downstream buyer withholds hand-off to control everyone's credit | **Debit-follows-possession inverts the leverage.** A maker's credit realizes at the *first* hand-off to *any* receiver; holding goods means holding their debit (worse ratio), so a hoarder is motivated to pass them on. Power to gatekeep evaporates. |
| **3 — Risk-dumper (mislabeling)** | An employer labels speculative work "pledged" to recruit, or vice-versa to shed risk | **The label is read off the *public* pledge ledger, not declared** (§4.7). Same move as co-product splits (§5.1a) and cost constants (§3.3a): never let a self-interested party write the number. |

**What the stress test changed before adoption:**
- The gatekeeper guard was *not* the author's first "any receiver" idea (which is wash-tradeable) — it is **debit-follows-possession + hand-off = verification**, discovered mid-pass.
- The count **self-audits**: a receiver eats the debit of exactly what they accept, so cannot be made to sign for phantom units (same incentive as §3.3a).
- **Realization ≠ deployment**: two separate clocks (§4.5), and **transit custodians accrue no creation-cost share**.

**Side findings banked:** the wage-extraction **employer is structurally hollowed out** (→ OA7/P4); **demand risk is symmetric by hours**, not dumpable by rank (→ OA7 (coordinator class)); the **market-public/persons-private** transparency principle (→ OA9/OP-22).

**The one surviving residual.** Realized credit → pledging-power (influence) is measured in *gross hours*, so a consumption-indifferent zealot could collude to fake gross hours and pump influence — bounded by IC-7 (24-hour cap) (24 h/day) and paid in a wrecked ratio. *(The "self-starving" brake is **re-armed** under Foundations v0.14: pledging now spends a permanent, finite lifetime budget, so pledging is no longer free. An influence-pumper spends real budget to pump, and pledge-farming a task needs real verified colluders each burning their own budget on the public ledger — a cost, not a free ride. This narrows the residual but does not fully close it.)* **This is an OP-1 influence question, not a credit-accounting flaw.** Tests owed: §C.

---

<!-- tag: obj-b11 -->
## B12 — §3.2b electricity attribution (the real-time-dispatch principle) ✅ **PASSES WITH CHANGES**

**Shipped:** Foundations v0.10 §3.2b + §12; Overview v0.8 §4. **Source:** stress-test (`stress-test` skill), surfaced during Track 4 of the median-lifestyle calc, `03-journal/2026-08-10.md` / `2026-08-09.md`.

> ### ⚠️ AMENDED 2026-08-24 — the attribution basis is reversed. Read this first.
>
> **The real-time-dispatch principle below still stands: electricity's generation pollution is the consumer's.** What changed is **how the consumer's figure is computed.**
>
> | | |
> |---|---|
> | **Was** (v0.10–v0.21) | The consumer's **contracted supply mix** — the generator they bought from. |
> | **Now** (Foundations v0.22) | **The grid's actual measured fuel mix over the half-hourly periods the consumer drew power**, from the meter record and the grid operator's own published output record. |
>
> **Why.** A supply agreement is a paper claim, not matter or energy. **A1's corollary says paper claims never appear on any ledger**, so letting one decide a physical CO₂ record was an A1 breach that nobody had spotted. **A record of CO₂ must come from a measurement of CO₂.**
>
> **What it costs:** exploit 1 below (the dirty generator) was answered by contracts, and now is not. **The generator's incentive to decarbonise moves to three routes that already exist** — their own capital and process debit (§4.5), pledges toward clean generation (§4.6), and §3.3 retroactive re-weighting, under which cleaning the grid lightens every past consumer's record.
>
> **What it gains:** the consumer's *timing* now carries a debit. Worked in Foundations §3.2b — moving 100 kWh of a 300 kWh month from evening peak to overnight cuts the household's CO₂ by **14 kg, about 32%**, with no reduction in consumption. Under any flat-average or contract-based rule that change is worth nothing.
>
> **Also ruled:** **transmission losses stay with the producer and the network operator.** That power was never handed to a receiver, and a hand-off is what moves a debit (§4.6). At a 7% loss on a 300 kWh delivery, the ~23 kWh burned in the wires — about 3 kg CO₂ — is the network's.
>

**The ruling.** Emissions from **real-time, demand-dispatched, non-storable** production follow the **end-user**; batch/stockpiled production stays with the producer. So electricity **generation** pollution is the consumer's (the plant is a tool under A1; the draw is the act) — aligning it with §3.2b's existing final-delivery-transport and personal-combustion rules.

**Verdict: PASSES WITH CHANGES.** The core insight is consistency-improving, but the *raw* form ("all generation pollution to the consumer, physical marginal unit") failed the exploit hunt:

1. **The dirty generator (offloader).** On a *pooled* grid the consumer cannot physically choose their source, so dumping the grid-average on them removes the pollution debit from the **only party that chooses the fuel** — weakening decarbonisation. → **Fix adopted: attribute by the consumer's *contracted supply mix* (provenance, §4.4), not the marginal unit.** A clean generator can then offer lower-debit power and win contracts; the consumer still conserves. This also resolves the marginal-vs-average question (neither — it's the contracted mix). No-choice contexts use the local supply average + §4.6 pledges / §3.3 retroactive cleanup.
2. **The grid-factor understater (estimator-gamer).** All consumers benefit from a low grid emission factor → **OP-24 (understatement drift)**; policed by rival clean-energy audit (§3.3a). Not new.
3. **Justification contradiction (now resolved).** "You bear the marginal turbine" (physical) and "you choose green tariffs" (contractual) conflicted; contracted-provenance attribution keeps the second and drops the first.

**Axioms.** No conflict — Ellerman-motivated (A1: only the actor pollutes; the plant is a tool), and every emission stays internal (A4). **⚠️ Open universality edge:** real-time-vs-batch is a *spectrum* (grid storage, on-demand services); the mid-line criterion is registered open, not closed.

<!-- tag: obj-b11 -->
## B11 — Self-care as credited work & the definition of work ✅ **PASSES (instance of OP-10/OP-22)**

**Shipped:** Foundations §0, §6, §4.5, §4.6, §4.6→§4.2, §5.5. **Source:** the work-definition session (author interview + `stress-test`), `03-journal/2026-08-07.md`.

**The cluster.** (1) Self-care (sleep, sustenance, basic care) is credited work — *time spent* maintaining the human, creditable because it costs time, not because anyone values it. (2) The definition of work is stated: time spent maintaining/contributing to human life; boundary against leisure delegated to networks. (3) Self-care is the *mechanism* of the §5.5 basic-needs floor — not a grant, so A2-clean. (4) Self-care credit generates full pledging-power (consumption + a **universal basic voice**); routing is a network lever; auto-pledge funds essentials. (5) Verification generalises by output type; enrichment verifies on occurrence, **never feedback** (OP-8 (feedback firewall) guard).

**Verdict: PASSES — as an instance of OP-10/OP-22, not a new hole.**

**Exploit hunt.**
1. **Generous-network arbitrage** (institution) — a network declares 20 h/day "maintenance"; members get near-max credit+influence for existing and flock to it. My first proposed fix ("anchor the floor to measured physiological need, *globally*") was **rejected by the author as anti-A8** — network weighting-pluralism is legitimate (A6/§3: shared log, differing weighting). **What actually stops it: counterparty re-computation.** A stingy counterparty re-weights the generous network's self-care *down* through its own model, so generosity cannot be *exported* — only shared among opt-in members (§4.2). **Comparison, never conversion** — a conversion would be an exchange rate between credit-standards, a medium of exchange forbidden by A3/§5.6.
2. **Reciprocal service/enrichment attestation** (colluder) — two accounts attest each other's unverifiable service or thinking. **Bounded by §4.5 conservative weighting** (≈zero until third-party corroboration) + IC-7 (24-hour cap) + the ratio/debit-room cost. Not eliminated; the same shape as the wash-trade residual (B10).
3. **Basic-needs-scope creep** (institution) — a network defines "basic needs" broadly so auto-pledged self-care power floods favoured sectors. **Same root as #1** — a weighting choice, discountable by counterparties.

**Where the residuals route.**
- The arbitrage guard **depends on OP-22 (audit disclosure)**: re-computing a pledge's backing needs "backed by *X* hours under model *M*" provable in zero-knowledge, since ledgers are private (§4.7). *The market check is only as real as OP-22.*
- Self-care is the **highest-leverage single weighting constant** (universal + influence-bearing) → the fattest **OP-10 (weighting governance)** target.
- Cohort-shopping on the floor/routing → **OP-14 (cohort shopping)**. Feedback-as-verification → guarded, **OP-8**. Debit-tolerance / the disparity denominator → **OP-4 (debit tolerance)**.

**The honest headline.** The cluster's apparent new capture surface is the *old* one (OP-10 governance / OP-22 disclosure) at **universal scale** — not a new hole. The stress-test's value was distinguishing "new break" from "existing open problem wearing a new hat." Note also the conceptual gain banked: **time, not effort, is the accounting substance** — the disparity ceiling is a *consequence of the unit of account* (time is equally distributed and non-transferable, A3 (non-fungibility)), bounded by `24 h ÷ the network's floor`, not a policed rule.

---

<!-- tag: obj-b1 -->
## B1 — P7. "Nothing else is value" ✅ FIXED

**Shipped:** Foundations §0 and A1 (materialism of cost).
**Sources:** [Ayres on emergy ignoring demand](https://www.centre-cired.fr/en/is-emergy-really-a-theory-of-value-2/) · [Sensorica](https://wiki.p2pfoundation.net/Open_Value_Accounting) · `GLOSSARY.md#src-technocracy-energy-accounting`

Every single-substance objective theory of value has been rejected on one ground: **supply-side only, ignores demand.** The refutation takes one sentence — and the old §0 wording invited it.

**The fix:** §0 ends *"Cost is nothing other than this,"* followed by an explicit statement that **Aequitas is a theory of cost, not of value**, and A1 is retitled *Materialism of Cost*. Value enters as feedback and pledges (§6), never as an accounting quantity.

**Confirmation from practice:** Sensorica **renamed its "value accounting system" to a "contribution accounting system"** on exactly this reasoning.

**Cost of the fix: one paragraph. It removed the single easiest attack on the project.**

---

<!-- tag: obj-b2 -->
## B2 — W1. A3 defeats the sink problem ✅ CLAIMED

**Shipped:** Foundations §5.6.

Ithaca HOURS and Burlington Bread both died of the *same specific mechanism*, and it was not valuation. Scrip flows toward businesses whose own inputs come from outside the network, making them one-way sinks. Ithaca's remaining businesses were **"drowning in Hours"**; Bread **piled up at Muddy Waters and Sugar Snap.**

**This cannot occur in Aequitas, because there is no medium of exchange.** Credit is non-fungible and never moves (A3 (non-fungibility)); only debit moves, attached to its object. **Nobody can drown in credit they cannot spend, because nobody ever receives credit *from* anyone.**

**Corollary — Wörgl.** The stamp scrip cut unemployment 16% while Austrian unemployment rose 19%, and was terminated by the Oesterreichische Nationalbank in 1933 to protect the legal-tender monopoly. **It was killed for working.** Aequitas has no issuer and no notes, so that instrument does not fit it. **The ban on calling Aequitas a currency is a strategic argument, not a branding preference.**

---

<!-- tag: obj-b3 -->
## B3 — Front-loading ✅ DISSOLVED OP-11, OP-5, OP-21

**Shipped:** Foundations §4.5, §4.5.

> **A large up-front cost with diffuse benefit is carried when incurred, cushioned by the debit-room those who pledged for it grant. It is never amortized downstream onto whoever happens to consume the result.**

**~~OP-11 — training amortization.~~** Every candidate denominator was defective. **The A2 (time as measure) v0.3 amendment removes the downstream flow entirely, so there is no denominator to choose.**

**~~OP-21 — media reproduction.~~** Production is front-loaded and pledged; the audience pays **delivery only.** Pledgers **receive no profit and cannot receive one.**

**~~OP-5 — education.~~** Answered by the same amendment plus pledging, which supplies the limit. **No perpetual-studenthood exploit.**

**Why the question was malformed in all three cases:** downstream amortization always requires choosing an arbitrary window. **Front-loading removes the division rather than solving it.**

> **✅ Confirmed in v0.6 — OP-23 (shared overhead) closed by exactly this.** Tooling and plant *are* front-loaded and pledged rather than amortized into output. Overhead does not shrink — it stops being allocated to outputs at all (§4.5). The bet recorded here paid out. See **B8**.

**⚠️ Residual: cold start.** Pledges follow reputation, so a first-time creator attracts none.

---

<!-- tag: obj-b4 -->
## B4 — One credit, three feedback channels ✅ DISSOLVED OP-8

**Shipped:** Foundations §6 (restructured).

An apprentice plumber's single hour is simultaneously **enrichment**, **service**, and **production**. That hour is not partitionable, so **no accounting rule may use the categories as a boundary.**

**Consequence for non-convertibility.** Under the corrected structure **no firewall is required**: enrichment *work* credits as time like everything else, and enrichment *feedback* is non-convertible because **it was never credit in the first place.**

**What survives** is the inverse and lives in Part A: **can feedback be bought?**

**This also voided the producer-plutocracy objection** — credit tracks hours, not tonnage.

---

<!-- tag: obj-b5 -->
## B5 — OP-19, OP-20, S1, W2, P9 ✅

**~~OP-19 — the saturated producer.~~ Resolved by pledges.** Pledging gives surplus a purpose: direct what gets made rather than hold it.

**~~OP-20 — unobservable work.~~ Closed with no new mechanism.** **IC-7 (24-hour cap)** caps claimed hours at wall-clock; **conservative weighting** prices unattested near-zero-material claims at ~zero; **pledges** are the only route from asserted to backed. **Conservative weighting has gone from a granularity incentive to a defence the theory depends on**, and must be specified early in C4 (re-weighting).

**S1 — "does this need a Paul Glover?" ✅ Adopted** as the fourth screening question. **A mechanism that depends on an enthusiast has an expiry date**, and must pay its own maintainer from inside the system.

**W2 — WIR and Sardex give the MVP a target shape. ✅ Usable now.** **B2B in dense input loops** on **mutual credit**. WIR: 1934–present, ~60,000 businesses, demonstrably countercyclical. **A downturn is the moment.**

**P9 (local-currency read) — §11 read as a local currency. ✅ Fixed.** **Aequitas's overlay computes a number money cannot produce.**

---

<!-- tag: obj-b6 -->
## B6 — Ellerman replaces Marx ✅ ADOPTED

**Shipped:** Foundations A1 (materialism of cost).
**Source:** [*The Labour Theory of Property and Marginal Productivity Theory*](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf) · `GLOSSARY.md#src-ellerman-labor-theory-of-property`

A1's attribution claim now rests on **responsibility imputation**: impute responsibility in accordance with who was in fact responsible. Not a moral claim about desert, but the principle courts already use for crimes, transplanted to production.

**Why this is better positioning than any labour theory of value:** it is juridical rather than value-theoretic, so it inherits none of the transformation problem, the negative-values problem, or a century of hostile priors.

**Three things it buys:** A3 (non-fungibility) becomes a consequence rather than a design choice; a second independent route to §5.1; and the reply to *"why do the machine's owners get nothing?"* — because machines do not act.

*Take the principle, decline the institution.* **The cost of adopting him is OP-18 (labour & team credit)** — his own argument that joint responsibility is non-decomposable, now the project's blocking problem.

**Also banked — tractability:** [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) demonstrated in-kind calculation at national scale with sparse-matrix methods. **Cite them rather than re-proving it.**

---
---

<!-- tag: obj-c-tests-owed -->
## C. Tests owed

Named so they are not silently skipped. ~~**Test 1 is the sharpest surviving technical risk in the project.**~~ **Test 1 resolved 2026-08-05 — the sharpest risk is retired.**

1. **✅ Recursion convergence — RESOLVED 2026-08-05.** `06-simulation/allocation-engine/recursion_convergence.py`, 5,224-run sweep, `RESULTS.md`. The allocation is a **non-negative linear fixed point** `p = c + Ãp` with `Ã, c ≥ 0` (Aequitas divides *by* the make-matrix, never inverts it), so for a productive economy (`ρ(Ã) < 1`) the solution is the Neumann series `Σ Ãⁿc` — **unique, non-negative, and iteration-reachable, independent of joint-production density.** Confirmed: **100% convergence** for `ρ < 1`, **zero** negative `min(p)` (4,098 economies, most-negative 2.9×10⁻¹⁵), rate `~ρⁿ`, `M=10⁴` in ~10 s. The rival **value/price** allocation (solving `v(B−A)=l`, which *does* invert `B`) went negative or non-invertible in **94.7%** of the same economies — including a hand-checked `v=[−1,2]`. **Sraffa/Steedman is blocked by construction, not by luck; IC-10's non-negativity is now derived.** Doubles as the first piece of C11 (arithmetic audits) and the synthetic half of the academic Sraffa reply.
2. **Understatement drift** (OA3 (understatement drift)). Simulate trust networks under §3.3a's incentives; find the rival density at which the drift stops being arrested.
3. **The fuzzy middle.** Hide-to-carcass ratios vary slightly by breed and feed. Does the rule behave sensibly at small differences? [Mackenzie et al. on biophysical allocation in livestock](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) is the hardest published case.
4. **Refinery re-derivation.** Process-physics allocation versus USEEIO price allocation on the same slate. **A materially different answer is the most publishable technical result available early.**
5. **OP-16 (onerousness gap) cleaner test.** Night-shift vs day-shift vs rural carrier. If identical, (b) is eliminated.
5a. **Split-robustness test — how far does a split move across honest methods?** *(New 2026-08-24, from economist finding #24.)* Take a refinery, a combined-heat-and-power plant, and a livestock case. Compute each split under **every defensible instrument, period, and sub-process boundary**, and report the range. **Refinery worked estimate to beat: by mass ≈ 3,600 GJ to petrol, by energy content ≈ 3,840 GJ, by cracking enthalpy ≈ 4,800 GJ on the same 8,000 GJ pool — a 33% spread.** **If the measured range is narrow, Foundations §3.4a's four obligations are enough. If it is wide, instrument choice is a large lever and routes to OP-10 (weighting governance).** Cheap to run and it settles the wording.
6. **Demand-risk floor adequacy** (B10 / hole 2b). Simulate a worker on a failed *speculative* run: does the basic-needs floor (§5.5) actually keep them out of destitution, and how does their exposure compare to a capitalist wage-worker who bears no inventory risk? A distributional check, not a break.
7. **Influence back-door** (B10 / OP-1 (service → influence)). Simulate collusive hand-offs manufacturing gross fake hours → pledging-power, against the IC-7 (24-hour cap) cap and the wrecked-ratio penalty. *(Note: under Foundations v0.13 pledging no longer costs the pledger debit-room, so the old "self-defeating because pledging drains you" brake is gone — the sim must ask whether IC-7 and the ratio penalty **alone** are enough, or whether a consumption-indifferent actor can still buy influence.)*
8. **Generous-network race + the disparity ceiling** (B11 / OP-14 (cohort shopping) / OP-24 (understatement drift) / OP-4 (debit tolerance)). **✅ Disparity-ceiling proof FORMALLY STATED + STRESS-TESTED → PASSES (2026-08-14)** — Part 1 (formal statement) + a plain-language explainer are in `06-simulation/disparity-ceiling/DISPARITY_CEILING.md`; the adversarial pass dissolved all three attacks: **Methuselah** (credit/debit are cumulative event-log tallies and credit is never *spent* — the gate `D ≤ ρ·C` is a ratio checked per event, A3+A6 — so a lifelong hoarder's splurge only front-loads their own `ρ·C`; equal-age disparity is exactly `24/F`, the only spread beyond it is age); **dynasty/household** (a co-op, dwelling-debit split per occupant by dwelling-time — the bound is **per-person**, inheritance dilutes it); **collector** (holdings are a self-bounding burden). A **Methuselah self-test (Claim 4)** is in the sim (now **7 self-tests green**). **✅ Simulated 2026-08-10** — `06-simulation/disparity-ceiling/disparity_ceiling_sim.py`, agent-based N = 200,000, gate `D_i ≤ ρ·C_i`, credit ∈ `[F,24]` h/day: **(a)** the `24/F` ceiling is exact and **ρ-independent** (2.4× for F = 10, flat across ρ ∈ [1,3]) *and* weighting-independent — it **does not depend on OP-10** — vs money 14× (income) / ~700–950× (wealth) on the same population; **(b)** a **ρ clears the market and moves like a prime rate** (a −30% capacity disaster tightens clearing ρ* ~1.25→~0.82), confirming *a ρ can be picked & adjusted*, not "the one true ρ"; **(c)** the ceiling is **fraud-invariant** — IC-7 (24-hour cap) bounds every account, so fraud fills the band but never exceeds it. **Structural results hold for any distribution; still conditional on OP-22** (the sim assumes the anti-arbitrage guard, does not model disclosure). **This is the strongest defensive result the project can hold**, now with a simulation behind it. **✅ Like-for-like vs REAL wealth micro-data DONE 2026-08-10** — the money side is calibrated to the 2022 Survey of Consumer Finances (wealth p99/median = 71×, reproduced) + the Forbes billionaire tail (~10⁶× the median); Aequitas caps command-over-resources at 2.4×, a **5–6 order-of-magnitude** compression. **✅ Consumption-axis real-distribution comparison DONE 2026-08-10** (`06-simulation/scenario-suite/q4_locked_ledgers.py`, scenario-suite Q4) — applies the ceiling to real US/world distributions under the **material-only** rule (A1 corollary, Foundations v0.12 §1). Two results: **(i)** stripping the financial layer compresses the *observed* tail **~1,000×** (money wealth ~10⁶× → material consumption ~670×, Oxfam billionaire personal footprints), so the disparity the ceiling must cap is far smaller than money's; **(ii)** only **~0.1–2%** of people (ρ-dependent) sit past a *permanent* efficiency-ratio lockout — the ultra-consumers, not the merely rich — and even full divestment doesn't save them (permanent consumption debit); ~two-thirds gain room by joining. **Still owed, and re-pointed in v0.23 after the OP-22 ruling of 2026-08-25:** the **generous-network cohort-shopping race** (does the floor race to the IC-7 ceiling, or does §4.2 counterparty re-weighting arrest it?), **and nothing else.** A multi-homing figure was drafted and **refused on 2026-08-27** — it added two networks' rooms together, which sets an exchange rate between credit-standards (**A3**, **§4.2**, **conformance 4a**). **The generous-network race is tracked as OP-14, not OP-22.** There is no cross-network disclosure mechanism to owe, because **no book is ever added to another** (§4.0), and §5.5.5 condition 4 now states the bound as one network's books. The proof itself (Parts 1–3 + stress test) is **complete and PASSES** on that scope. Rests on Foundations v0.15; scope corrected against v0.25.
9. **The stable band of `F` and ρ** *(new 2026-08-25, from the §5.5 rewrite)*. **Find the values inside which essentials stay affordable and the ledger still rations what is genuinely short.** Existing runs take `F` as given. Lower bound: `ρ · F · 365 ≥ E`, the labour a year of essentials commands. Upper bound: where the floor's own room exceeds what the economy can deliver, so the gate stops binding before capacity is reached. **Worked in Foundations §5.5.3; the 700 h/yr essentials figure there is illustrative and must be measured from the median-lifestyle data first.** Runs in `06-simulation/statera/`.

<!-- tag: obj-d-not-yet-examined -->
## D. Not yet examined

- **Ostrom** — polycentric governance, commons design principles. Bears on A8 (no governing body) and OP-10 (weighting governance). **Highest value of these.**
- **Georgescu-Roegen** — entropy and the economic process. Bears on §3.5.
- **Lange–Lerner** market socialism, and why Hayek rejected it.
- **Nove**, *The Economics of Feasible Socialism*.
- **Graeber**, *Debt* — bears on permanent consumption debit.
- **Sensorica** in depth · **WIR + Sardex** on their own · **Banque du Peuple post-mortem** · **Warren's colonies**.
- **Aumann–Shapley / cooperative cost-game literature** — rejected as the OP-17 (joint production) rule, but its axioms (efficiency, symmetry, dummy, additivity) are a good checklist for **OP-18 (labour & team credit)**, where a convention genuinely is required.

---

---

<!-- tag: obj-changelog-pointer -->
## Change history

The version-by-version change log (former §E) now lives in a separate file, read only when needed: **`Aequitas_Objections_CHANGELOG.md`**.

---

*End of v0.22.*
