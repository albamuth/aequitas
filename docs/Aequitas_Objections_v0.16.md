<!-- tag: obj-aequitas-objections-register -->
# Aequitas — Objections Register

> **Version:** 0.16 · **Date:** 2026-08-14
> **Supersedes:** `99-archive/Aequitas_Objections_v0.15.md`. **Disparity-ceiling proof completed + stress-tested → PASSES (§C test 8).** Part 1 (formal statement) now exists with a plain-language explainer (`06-simulation/DISPARITY_CEILING.md`); the adversarial pass dissolved the Methuselah hoarder (credit is a cumulative record gated as a ratio, never *spent* — A3+A6), the dynasty/household (a co-op; per-person bound), and the collector (holdings self-bound). A Methuselah self-test (Claim 4) is in the sim (now 7 green). Only the generous-network cohort-shopping race remains owed on test 8. Tracks Foundations v0.15.
> **Prior (v0.15):** **Conformed to Foundations v0.14 (pledges made permanent + the contingent reserve).** Consequences for the register: (1) **OP-16's hazard half is now addressed** — the contingent reserve (§6.4c) gives hazardous work a demand-gated incentive without rate-scaling; the tedium/indignity half stays open. (2) **The OP-1 influence back-door's "self-starving" brake is re-armed** — permanent pledging *does* spend a finite lifetime budget, so nobody pledges for free again. (3) **The P4 seniority-skim residual is closed** by pro-rata-by-task-hours. (4) **C5 (pledge reversion) resolved in the negative** — unspent pledges burn. Sim: `06-simulation/pledge_reserve.py`.
> **Tracks:** `Aequitas_Foundations_v0.16.md` · `Aequitas_EventLog_v0.7.md` · `OP-18_labour_and_team_credit.md` · `OP-23_capital_and_pollution.md` · `OP-17_coproduct_allocation.md` · `06-simulation/RESULTS.md` · `06-simulation/DISPARITY_CEILING.md` · `06-simulation/pledge_reserve.py` · `06-simulation/scenario_suite_METHOD.md`
> **Change history:** `00-strategy/Aequitas_Objections_CHANGELOG.md`.
> **Purpose:** one place holding every serious objection to the theory, its source, the axiom it attacks, and its status.

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

**[PART B — ANSWERED](#part-b--answered)**

  - [B7 — OP-17. Joint production](#b7--op-17-joint-production--closed-for-materials-and-energy)
  - [B8 — OP-23. Shared overhead](#b8--op-23-shared-overhead--closed--capital-accrues-to-the-asset-not-the-co-products)
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
| 🔴 | **OP-10 (weighting governance) / P8 (weighting governance) — Weighting-model governance** | Open. One side entrance closed (§3.2a); cost constants have a mechanism (§3.3a); the general problem stands. **Now the top blocking problem.** |
| 🔴 | **OP-24 (understatement drift) — Understatement drift** | Errors favouring subscribers have no funder. Attacks A4 (no externalities). **Lever enlarged in v0.6** by the stock/baseline constants. |
| 🟠 | **OP-16 (onerousness gap) — Onerousness gap** | **Hazard half addressed** by the contingent reserve (§6.4c, v0.15); skill half fixed by A2 v0.3. **Tedium/indignity half open.** |
| 🟠 | **OP-6 (feedback mechanics) — Feedback mechanics** | Promoted; also carries signal flooding. |
| 🟠 | **P4 (coordinator class) — Coordinator class** | **Weakened again in v0.8.** Credit-accumulation form dead; **wage-extraction employer now structurally hollowed out** (no wages A3 (non-fungibility), no surplus A5 (price ≡ cost), no rank-based dumping); mislabeling defused (public pledge ledger). Only the *coordination* residual (who holds empowering work; hours-inequality in pledging) survives. |
| 🟠 | **OP-1 (service → influence) — Service → influence** | **Carries the credit-realization residual** (gross fake hours from collusive hand-offs — bounded by IC-7 (24-hour cap) and paid in a wrecked ratio; B10). The old "self-starving" brake is gone — pledging no longer costs the pledger debit-room (Foundations v0.13), so it no longer starves an influence-pumper. The flip side: self-care credit → a **universal basic voice** bounding influence disparity to `24h ÷ floor` (a feature); routing is a network lever, backing checkable only via OP-22 (audit disclosure). See B10/B11. |
| 🟢 | **OP-9 (calculation reply) / P5 (preference revelation) — Socialist-calculation reply** | **Written up (v0.10)** → `OP-9_calculation_reply.md`. Cost≠value defeats Mises; pledges reveal demand; tractability cited; scarcity-as-debit rations without a margin. **Answered for cost; the scarcity objective-function edge and the Hayek tacit-knowledge residue terminate in OP-10.** See OA8. |
| 🔽 | **OP-22 — Minimum audit disclosure** | Narrowed to a C7 (privacy layer) implementation question — **more load-bearing again after v0.9:** it powers the market-public/persons-private principle *and* the anti-arbitrage guard (a lax network's credit is only discountable if backing is provable in zero-knowledge). See B11. |
| ✅ | **Credit-realization / hand-off model** | **PASSES WITH CHANGES (v0.8).** All three exploits (wash-trade, gatekeeper, risk-dumper) defused; residuals route to OP-1/OP-22/OP-25. See **B10**. |
| ✅ | **Work-definition / self-care cluster** | **PASSES (v0.9).** Self-care is credited *time* (the §7.5 floor's mechanism, not a grant); verification generalises by output type; self-care → universal basic voice. Not a new hole — an instance of OP-10/OP-22. See **B11**. |
| 🔽 | **OP-25 (illicit dumping) — Illicit end-of-life dumping** | **New.** §3.6 prices lawful disposal; abandonment attribution is a Level-2 problem. |
| ✅ | **OP-18 (labour & team credit) — Responsibility is not divisible** | **CLOSED in v0.7** as the C3 (estimation engine) blocker — team-credit dissolves under A2; labour rides the material split; cost ≠ scarcity. See **B9**. |
| ✅ | **OP-23 (shared overhead) — Shared-overhead attribution** | **CLOSED in v0.6** — capital and overhead never allocate to co-products. See **B8**. |
| ✅ | **OP-17 (joint production) — Joint production allocation** | **CLOSED** for the material/energy half — see **B7**. |
| ✅ | **P7 (theory of value) — "theory of value"** · **W1 — A3 defeats sinks** · **P9 (local-currency read)** · **S1** · **Ellerman** | **Fixed / claimed / adopted.** |
| ✅ | ~~OP-11~~ · ~~OP-5~~ · ~~OP-8 firewall~~ · ~~OP-19~~ · ~~OP-20~~ · ~~OP-21~~ | **Dissolved, resolved, or closed.** |

**Fifteen items closed; six live.** The pattern held for a fourth session and then broke on the fifth in an instructive way: OP-17, OP-11 (training amortization), OP-21 (media reproduction), OP-23 all closed by *removing* a division. **OP-18 is the first to close by *declaring* a convention** — because labour genuinely leaves no trace, the physical-trace test *mandates* a convention here. **v0.8's contribution was different again:** the credit-realization model (B10) closed a cluster of *incentive* exploits by discovering that a mechanism the author already had — **debit-follows-possession** — inverts the attacker's leverage. **v0.9's is different once more (B11):** the work-definition cluster's apparent new capture surface turned out to be an *instance of an existing open problem* (OP-10 weighting governance / OP-22 disclosure), not a new one — the honest outcome of a stress-test is sometimes "this is the old hole wearing a new hat," and saying so keeps the register from inflating its problem count.

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

> **Overhead was the third, and v0.6 removed it — not by splitting it, but by declining to allocate it at all.** Capital and overhead accrue to the **asset** as property-debit and never flow to the co-products (Foundations §6.2b). The barn is not divided between hide and beef; it stays on the operator. **A division problem dissolved by relocating the thing being divided** — the fourth consecutive closure of that shape.

*Foundations adopts this:* §3.4 is narrowed, §3.4a states the material/energy rule, §6.2b removes the overhead allocation, and §1.1 has now lost two rows rather than gaining entries.

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
| **1 — Valuation** | Flat-hour crediting cannot recruit skill | Warren; **time banking, 45 years** | 🟠 Skill fixed; **OP-16** hazard half addressed (§6.4c), tedium half open |
| **2 — Circulation** | Scrip pools at sinks and stops moving | Ithaca, Burlington | ✅ **Immune — see B2** |
| **3 — Institutional** | Founder dependency, state suppression | Ithaca (Glover left); Wörgl (banned) | ✅ Addressed — see B5, B2 |

---

<!-- tag: obj-oa1 -->
## OA1 — OP-18. Responsibility for joint work is not divisible

**Attacks:** A1's attribution claim, A2 (time as measure), C1's agent field.
**Sources:** [Ellerman](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf) · `GLOSSARY.md#src-ellerman-labor-theory-of-property`
**Status:** ✅ **CLOSED 2026-08-05 as the C3 (estimation engine) blocker — moved to Part B (B9).** The statement below is kept as the record of the problem; the resolution is in B9. Resolution note: `00-strategy/OP-18_labour_and_team_credit.md`.

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

**Attacks:** A8 (local governance), decentralization.
**Status:** 🔴 Open. Largest hole in A8. **Two partial answers added in v0.5.**

Whoever sets the mitigation-cost model controls every balance in history without touching a core rule.

**The comparison sharpens it.** Parecon's Iteration Facilitation Board is [attacked as implausible](https://ejpe.org/journal/article/view/867) for assuming a body can announce opportunity costs for all goods, resources, labour categories and capital stocks. **Aequitas's weighting-model maintainer is structurally the same object.** The verification ladder answers *data collection* — it gathers locally rather than centrally — but it does not answer *model maintenance*, which remains central by default.

**Progress in v0.5, from the OP-17 (joint production) work:**

1. **A side entrance is closed.** Foundations §3.2a requires every division of a debit to be computed **per dimension on the vector, before collapsing** to a comparable scalar. Had splits been computed on the collapsed number, the weighting-model maintainer would have controlled every allocation in history *invisibly*. Per-dimension splits are weighting-independent. **This hole existed and nobody had noticed it.**
2. **Cost constants have a mechanism** — rival-sector audit, §3.3a and OA10 (auditor independence) below. It is specific to constants, not to the model as a whole.

**What remains:** the general problem. The strongest available reply is competing local variance under A8 — multiple weighting models, openly published, each recomputable by anyone from the same log. **That reply is asserted in A8 and still nowhere specified. Specify it.**

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

**One channel of capture is structurally closed and should be claimed.** There is no market-dominating corporation to fund a favourable result, because A5 (price ≡ cost) removes the profit that pays for captured science today. Labs are credited by trust networks for doing work. **The Enron-shaped failure cannot operate the same way here.**

**But the mirror problem is real, and it was introduced by the fix for the first one.** A general-membership trust network is dominated by the *consuming* side of any given good — everyone eats beef, few raise cattle. Its members therefore collectively benefit from beef's debit being **understated**. And the incentive to correct is one-sided:

| Error direction | Who wants it fixed | Result |
|---|---|---|
| Constant **overstates** debit | Every subscriber | Corrected |
| Constant **understates** debit | Nobody — correcting it worsens every subscriber's ledger | **Nobody funds the replication** |

**Result: systemic drift toward under-costing** — precisely how every carbon-accounting regime attempted so far has failed. Foundations §3.5 tolerates it arithmetically (no global balance is required), which is what makes it insidious: **there is no equation that breaks.** It simply erodes A4.

**Aggravating factor: replication cost is asymmetric.** Competing networks discipline *estimates* cheaply — re-interviewing a farmer is cheap. They do not discipline *constants*: re-running calorimetry is not cheap. So the competitive pressure that works everywhere else in the system is weakest exactly here.

**Proposed fix — rival-sector audit (Foundations §3.3a):**

> **The natural auditor of a cost constant is the rival sector, not the consumer.** If beef's energetics are understated, plant-protein producers are materially harmed and will fund the replication. Consumers police neither direction; rivals police both.

Plus three supporting rules: two unaffiliated replications before a constant may re-weight history; triage weighted by **magnitude × concentration of beneficiary** rather than magnitude alone (materiality thresholds alone *help* an attacker, whose job becomes making a falsification look immaterial); and networks concentrated in the sector they audit are captured by construction, which is **detectable from public membership composition.**

**Why the fix is unproven.** It assumes a rival sector exists and is dense enough to fund replication. For beef versus plant protein, plausible. For a good with no substitute, or a constant that cuts across all sectors equally, there is no rival and no auditor. **Test: simulate a population of trust networks with this incentive structure and measure at what rival density the drift stops being arrested.**

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

> **✅ The hazard subset is now addressed — the contingent reserve (Foundations §6.4c).** Flat credit alone under-staffs dangerous work: a worker bears its expected future health cost on their own ledger, so they avoid it (the 45-year time-banking shortage). Permanent over-pledging fixes this *without* a wage premium or rating authority — the surplus becomes an earmarked, non-consumable reserve that pre-funds any verified task-caused harm to the doer. Society de-risks the toxic-cleanup worker exactly to the extent it pledges for the work; the danger internalises as the reserve the task must attract. Sim `06-simulation/pledge_reserve.py`: the job clears once pledges roughly cover the tail, and overflow-reverts-to-causer (§3.2/§3.7) preserves care. **This is a demand-gated incentive, not a rate multiplier — A2-clean.**

**What remains uncovered: disutility with no material signature *and no causal tail*.** Tedium, isolation, indignity. Dull-but-safe work generates no future task-caused cost, so the reserve gives it no incentive. Two such jobs with identical calories, identical training, and identical health outcomes credit identically per hour — but nobody wants one of them. **This half stays open.**

**This is not theoretical.** Time banking credits every hour identically — exactly A2's flat hour — and 45 years across dozens of countries produces chronic **skill mismatch**, credit hoarding, and skills in short supply.

**Candidates:**
- **(a) Hour-ceiling differentiation — strongest.** Pay the premium in *hours, not rate*: a sustainable sewer shift is 4h, a pleasant one 8h; both credit 1hr/hr, so no multiplier exists anywhere. Justification is **physiological and measured**. Weakness: who sets the ceilings → **OP-10 (weighting governance)**.
- **(b) Check how much of OP-16 (onerousness gap) is simply unmeasured hazard.** Night shift, isolation, and repetitive strain have documented health costs A2's hazard clause **already** injects. **Do this first** — it may shrink the problem substantially.
- **(c) Automation pressure.** Unfilled pledges are a visible, quantified signal saying *automate this*.
- **(d) Rotation** (balanced job complexes). Carries [the compulsory-labour critique](http://libcom.org/blog/workers-critique-parecon-11042012). Last resort.
- **(e) The contingent reserve — adopted for the hazard subset (v0.15).** See the box above; Foundations §6.4c. It covers hazardous-onerous work; it does *not* touch tedium/indignity, which has no causal tail to pre-fund.

> **Withdrawn candidate:** *"route onerous work to service credit."* There is no separate service credit to pay a premium in. Recorded so it is not re-proposed.

**Test:** compute the debit-cost of night-shift office cleaner, day-shift office cleaner, and rural postal carrier. **If the numbers come out identical, OP-16 is confirmed and (b) is eliminated.**

---

<!-- tag: obj-oa6 -->
## OA6 — OP-6. Feedback mechanics

**Attacks:** §6.3, §6.4. **Status:** 🟠 Open, and **promoted**.

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

> **⚠️ Weakened further in v0.8 — the *employer* form is structurally hollowed out.** The credit-realization session established that the wage-extraction employer has **no mechanism to exist**: no transferable credit → **no wages** (A3 (non-fungibility)); price ≡ cost → **no surplus to appropriate** (A5 (price ≡ cost)); team debit shared **by hours, not rank** (§6.2b) → **no rank-based risk- or cost-dumping.** Two attempted exploits died here: **mislabeling** pledged-vs-speculative work to recruit or shed risk is defused because the label is **read off the public pledge ledger, not declared** (§5.3, §6.4a); and **"labour bears demand risk"** is bounded because unsold-run risk is shared *symmetrically by hours* (a worker's share equals a supervisor's), is *informed* (transparency shows demand before committing), is mostly *pledged* (cushioned by committed demand — and under Foundations v0.14 a pledge is *permanent*, so the cushion cannot be withdrawn mid-run), and is *floored* (§7.5). **What is left of P4 (coordinator class) is only the pure *coordination* residual** below — not the boss.

**The new residual, introduced by pledging.** Pledging power accrues per hour worked, equally for everyone — egalitarian across *sectors*, but weighted by **hours available to work**, which is not equally distributed. Caregivers, part-time workers, the disabled, and the chronically ill hold systematically less say in what gets produced. **Live and unaddressed.**

> **A second seniority-weighted channel was avoided, not opened (v0.15).** The contingent reserve (§6.4c) splits a task's pledged cover **pro-rata by hours *on the task*** — deliberately *not* by whole-co-op-history hours, which would have let long-tenured members skim cover from work newcomers actually did (a fresh P4 surface). Task-scoped splitting keeps the cover on the doer.

**Consequences for OP-1:** *proposal power with universal suffrage* is the only candidate that structurally separates agenda-setting from deciding. Parecon's **decision weight proportional to how much you are affected** is a fifth candidate, and it does not accumulate at all — the best available answer to the hours-inequality residual.

---

<!-- tag: obj-oa8 -->
## OA8 — OP-9 / P5. Preference revelation

**Attacks:** A5 (price ≡ cost), A1 (materialism of cost). The Mises/Hayek line of attack — the objection every economist brings first.
**Sources:** [Mises (1920)](https://mises.org/library/economic-calculation-socialist-commonwealth) · [Hayek (1945)](https://www.econlib.org/library/Essays/hykKnw.html) · `GLOSSARY.md#src-neurath-calculation-in-kind` · [Dapprich](https://brightagebeyond.com/wp-content/uploads/2022/05/dapprich-philipp-2021-optimal-planning-with-consumer-feedback-a-simulation-of-a-socialist-economy.pdf) · `GLOSSARY.md#src-kantorovich-shadow-prices` · `GLOSSARY.md#src-cockshott-cottrell-labour-time`
**Status:** 🟢 **Written up (v0.10). Standing statement: `00-strategy/OP-9_calculation_reply.md`.** Plain-language version in Overview §9. Answered for cost; one residue terminates in OP-10 (below).

Cost says what a thing takes. It does not rank two people who both want the last one. The full four-move reply is the standalone doc; the register keeps the summary.

**The four moves:**

1. **Cost ≠ value.** Mises's argument is that you can't rationally *value* producer goods without a market. Aequitas concedes it entirely and doesn't need it — it computes cost (physical, measurable in mass/energy/seconds), never worth. The refutation aims at a target Aequitas doesn't occupy.
2. **Pledges supply the demand signal** (Foundations §6.4) — decentralized preference revelation with no prices, no central optimizer, and **no Iteration Facilitation Board.** A price fuses "what it took" and "how much wanted" into one number that then can't be separated; Aequitas keeps them apart by design.
3. **Tractability is settled — cite, don't re-prove.** [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) ran in-kind calculation at national scale with sparse-matrix methods; the recursion sim (`06-simulation/RESULTS.md`) is a second instance. Retires the *computational* form of the Mises objection.
4. **Scarcity-as-debit handles rationing.** On [Kantorovich's](https://www.nobelprize.org/prizes/economic-sciences/1975/kantorovich/lecture/) objectively determined valuations, a shadow price is the **cost of a binding constraint**, not a margin extracted by a seller. **Recorded as debit rather than skimmed as margin, this is compatible with A5 and arguably required by A4 (no externalities).**

**P5 (preference revelation) — the Cockshott variant.** Their demand lever is the *gap* between market-clearing price and labour value. **A5 collapses that gap to zero by construction**, so Aequitas inherits their problem with one fewer instrument. **Pledges are the replacement** — and a cleaner one, a direct expression of demand rather than a residual inferred from a price.

**⚠️ The one residue — it terminates in OP-10, and is registered there, not claimed closed.** Move 4's dual price requires a primal optimisation, which requires an objective function — **straight into OP-10 (weighting governance).** The clean form is to *federate per-constraint* (most scarcity is local — this lake, this ore body — with a local physical shadow cost needing no economy-wide objective), and to route physically-scarce *outputs* to distribution (lottery/queue/pledge-priority, §7.5) rather than to cost. That plausibly dodges the objective function, but is **unproven where a constraint spans the whole economy.** Separately, **Hayek's tacit-knowledge point** is only partly answered — but it is an objection to central *planning*, which Aequitas is not (it keeps books under a decentralized market), so it need only avoid recreating the problem. Both residues are OP-10 business.

> **⚠️ Sharpened in v0.5, enforced in the write-up — the OP-17 (joint production) session confirmed the danger.** A demand-contingent allocation rule was proposed and rejected: splitting a steer's debit by which cuts are sought-after makes two identical steers in two towns carry different splits, which **fails universality and is price allocation in costume.** The general lesson: **whenever demand is invited into the cost side, check whether A5 has been reintroduced under a new name.** The OP-9 reply keeps scarcity strictly as a *material* cost — this is the guard the standalone doc is built around.

---

<!-- tag: obj-oa9 -->
## OA9 — OP-22. Minimum audit disclosure

**Attacks:** §5.3. **Status:** 🔽 **Narrowed from a foundational conflict to an implementation question.**

The correct bar for attribution is **no worse than today** — a gallery buyer already has no proof the artist painted the work — and provenance only becomes fraught in the capitalized art market that A5 (price ≡ cost) removes. On privacy, the world already runs counterparty-visible and third-party-opaque, and Aequitas replaces neither courts nor social pressure.

**What survives is narrow and technical.** Banking externalizes validation to institutions; **Aequitas has no institution to externalize to.** So: **what is the minimum an auditor must see to verify a claim without seeing a history?** Zero-knowledge proofs are the right shape; the disclosure set is not specified. **C7 (privacy layer).**

> **⚠️ More load-bearing after v0.8.** The credit-realization session established that Aequitas is **radically transparent at the market level** (pledges, production, hand-offs, debit-costs are public — the pledger anonymous but the pledge visible) and **private at the person level** (Foundations §5.3, "market-public / persons-private"). That public market data is what makes §3.3a rival-sector audit, independent economic monitoring, and the anti-mislabeling defence (§6.4a) *work at all*. **But it depends on OP-22 (audit disclosure) being solved:** public pseudonymous events can be chain-analysed to de-anonymise a person. So OP-22 is no longer only about a single auditor's disclosure set — it is the enabling condition for the whole transparency story. Right shape (zero-knowledge / unlinkability); mechanism unspecified. **C7.**

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

<!-- tag: obj-part-b-answered -->
# PART B — ANSWERED

**The answer sheet.** Every item here will be raised again by someone who has not read this document, and most of them are the academic paper's strongest material. Do not file this away.

---

<!-- tag: obj-b7 -->
## B7 — OP-17. Joint production ✅ **CLOSED for materials and energy**

**Shipped:** Foundations v0.4 §3.4a, §3.2a, §1.1; EventLog v0.3 IC-10/IC-11/IC-12.
**Full argument:** `00-strategy/OP-17_coproduct_allocation.md`
**Sources:** [Sraffa/Steedman/Morishima on negative labour values](https://www.scienceopen.com/hosted-document?doi=10.13169/worlrevipoliecon.14.1.0063) · [ISO 14044 allocation critique](https://link.springer.com/article/10.1007/s11367-016-1161-2) · `GLOSSARY.md#src-joint-production-allocation-problem`

**The objection.** A process yields beef and leather, or a refinery's full fraction slate. One physical event, several outputs, one pool of debit. Splitting by mass, energy content, exergy, or economic value gives **four different answers, none more physically true than the others.** ISO 14044 ranks the options and then falls back to **market price**, which A5 (price ≡ cost) forbids. The classical form is sharper: under joint production, labour values can go **negative**.

**Why it looked unanswerable.** Both literatures searched for a **carrier quantity** — a property of the *outputs* by which cost could be apportioned. Every candidate works in some industries and is a category error in others.

**The answer.**

> **A joint process's debit divides according to where the process itself physically sent its inputs.** The instrument is whatever that process makes traceable — tissue-deposition energetics for an animal, cracking enthalpy for a refinery, the extraction curve for a turbine. **These are not rival conventions; they are different instruments reading the same underlying quantity, which is hours (A2 (time as measure)).**

**Why Aequitas can say this and the LCA literature cannot: it has a universal denominator and they do not.** Every physical quantity in the ledger is already a proxy for hours-to-produce or hours-to-mitigate, so the question "mass or energy?" — unanswerable as posed — never has to be asked.

**Tested** against a slaughterhouse (tissue energetics), an oil refinery (cracking enthalpy), and a CHP plant (turbine curve): one justification, three instruments, no case requiring its own excuse.

**Four things that fell out:**

| | |
|---|---|
| **Steedman is blocked, not inherited** | Nothing is inverted, so negative values do not arise: each share is a forward measurement of what physically went in. ✅ *Now derived, not merely asserted — the recursion is a non-negative Neumann series `p = Σ Ãⁿc`; simulation confirms `min(p) ≥ 0` across 4,098 productive economies while the value arm goes negative in ~95%. See `06-simulation/RESULTS.md` and §C test 1.* |
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

**Shipped:** Foundations v0.5 §6.2a (computational-closure boundary), §6.2b (the capital-debit waterfall), §3.2b, §3.6, §7.2.
**Full argument:** `00-strategy/OP-23_capital_and_pollution.md`
**Method:** design interview → stress-test (capital front-loading) → stress-test (the full waterfall) → adopted with changes.

**The objection.** The barn shelters the whole animal; the cleanroom serves every wafer. No physical trace runs from overhead to any one co-product, and the v0.5 interim rule — inherit the traceable proportions — was **thinnest exactly where overhead dominates** (capital-intensive manufacturing), and gameable by *overhead-stuffing*.

**The answer — don't allocate it.**

> **A durable asset holds its own creation-cost as property-debit *on the asset*. The full cost is holding-time-split among its holders; community pledges grant them debit-room that cushions the bite (they do not shrink the debit — nothing vanishes, A1). It never flows to the co-products at all.**

The barn stays on the farm operator; the fab stays on its cooperative; hide and beef and each wafer carry only their own consumables. **There is nothing to attribute, so there is no attribution convention to get wrong and nothing for overhead-stuffing to exploit** — the exploit dies with the allocation it was gaming. This is the same move that closed OP-11 (training amortization) and OP-21 (media reproduction): *a division problem dissolved by removing the division.*

**Why it does not leak (A4 (no externalities)).** The overhead debit is not lost; it is **located** on the asset and its holders rather than smeared across units. Honest trade-off, stated in §6.2b: a per-unit debit-cost is therefore not a full-lifecycle figure.

**What the stress test changed before adoption.** The first residual proposal — split the un-pledged remainder *evenly* among current staff — **failed the second stress-test**: it imposed a perverse entry-toll on capital-intensive essential work (joining a hospital meant absorbing a share of its building) and tripped the dummy axiom. Replaced by the **holding-time split** (share = holding-duration ÷ total holding-duration), which starts a new hire at ≈0 and has a measurable basis. **The finding came from the adversarial pass, not the draft — the fourth session running where that held.**

**Three things that fell out** (all in `OP-23_capital_and_pollution.md`):

| | |
|---|---|
| **The computational-closure boundary** | Historical/capital costs cannot cascade downstream without regressing to the first human activity. Front-loading is what makes the accounting *terminate*. Pre-Aequitas assets enter at estimate/zero. |
| **Pollution and transport never transfer** | Only property-debit rides an item; pollution/transport stay permanently on the causer (§3.2b). This rewrote §7.2 to a direct producer-side penalty and resolved the recycling trace-forward paradox. |
| **The pollution baseline** | A flow is a pollutant only above the natural-remediation equilibrium; weight floats with the stock above it, unifying CO₂ and solid waste (§3.3, §3.6). |

**Spawned:** **OP-25 (illicit dumping)** (illicit end-of-life dumping — a Level-2 attribution problem) and an enlarged lever for **OP-24 (understatement drift)** (the new stock/baseline constants).

---

<!-- tag: obj-b9 -->
## B9 — OP-18. Labour & team credit ✅ **CLOSED as the C3 blocker — team-credit dissolves, labour rides the material split**

**Shipped:** Foundations v0.6 §1.1 (labour-across-co-products row filled; team-credit row marked dissolved), §3.4a (labour convention + the cost-not-scarcity rule), §10.
**Full argument:** `00-strategy/OP-18_labour_and_team_credit.md`
**Method:** opened → separated into two sub-problems → one dissolved against A2 (time as measure), the other resolved by the physical-trace test with the split basis chosen by the author, then axiom-scored and stress-tested.

**The objection.** Ellerman: responsibility for joint work is joint and non-decomposable — there is no fact saying the welder caused 40% of the bridge, nor how many of the farmer's hours are "in" the hide. OP-17 (joint production) split materials and energy by physical trace; **labour has no such trace.** C3 (estimation engine) needs per-product labour hours.

**The answer — it is two problems, and they close two different ways.**

> **(β) Team credit dissolves under A2.** Credit is *time worked* (§6). Each member is credited **their own hours** — the "40% of the bridge" number is never required. Credit was never a share of output; the objection conflated *credit-for-hours* with *share-of-responsibility*. The axiom already answered it. *(Residue: apportioning a jointly-caused debit — team pollution/harm — across members. Minor, non-blocking, sibling to OP-25 (illicit dumping).)*
>
> **(α) Labour across co-products gets a declared convention: it rides the process's material split.** No trace exists, so the physical-trace test *mandates* a convention — this is the first OP to close by declaring one rather than removing a division. The discipline: pick the convention that adds **no new capture surface.** Labour riding the already-measured, rival-audited material θ (mass/deposition for cattle, cracking-energy for a refinery) introduces no basis of its own and **changes no one's credit** — it only sets how each co-product's *debit-cost* reads.

**The load-bearing sub-decision — cost ≠ scarcity** *(the tenderloin case)*. A pound of tenderloin (≈1% yield) and a pound of hamburger (≈5% yield) **cost the same**, because each embodies the same feed, water, and growing-labour — refined only by *measured* tissue composition, never by yield or desirability. Weighting the rare cut as *more costly* is scarcity smuggled into cost, and it would ration that cut by **who can absorb the larger debit** — price-rationing by standing, the exact mechanism A5/§7.1 removes. **The scarcity is real and routed elsewhere:** to pledges/signals (how many cattle) and to decentralised local distribution (the butcher's lottery/queue/pledge-priority, §7.5). *Cost states what a thing took; who gets a scarce output is a distribution question, deliberately outside any central authority.* Method 2 (yield-weighting) was raised and rejected on exactly this ground.

**Axiom score (labour-rides-material-split).** Efficiency ✅ (shares sum to total), Symmetry ✅, **Dummy ✅** (manure ≈ 0 mass → ≈ 0 labour — the axiom that killed OP-23's even-split), Additivity ✅. **Exploit:** it amplifies the reward for faking the material split — but that is the existing rival-sector-audit target (§3.3a), no new mechanism.

**Universality is the win over Method 2.** Two identical cows in two towns get the **same** split, because nothing is demand-contingent — precisely the failure that "price allocation in costume" would introduce.

---

<!-- tag: obj-b10 -->
## B10 — Credit realization & the supply-chain hand-off model ✅ **PASSES WITH CHANGES**

**Shipped:** Foundations v0.7 §6.4 (pledge broadened), §6.4a (hand-off model), §3.2 (debit-taxonomy refined), §6.2b (deployment/transit), §6.2a (pre-Aequitas genesis), §3.7 (land remediation), §5.3 (transparency principle), §7.1 (employer hollowed out); EventLog v0.4 §7.3, §5.1b, §2.2, IC-9 (pledge discharge), §12.1.
**Method:** adversarial design interview → author ruling → full stress-test pass. This is prime academic ammunition — the mechanism that makes "you are paid for work someone actually wanted" true without a boss deciding it.

**The ruling.** Production credit is always *recorded* (the event is logged; unpledged wheat still has a grower, A7/IC-3) but **realizes only on verification of the output** — *verification, not approval.* **For a physical good, each hand-off is that verification**, and is simultaneously (i) verification realizing the *prior* holder's credit, (ii) transfer of the material debit to the receiver, (iii) a new credit event for the receiver's own labour.

**Three exploits raised and all defused:**

| Exploit | Attack | What defuses it |
|---|---|---|
| **1 — Wash-trade** | Two co-ops swap goods, doing fake work, to manufacture credit | **Dominated by real work.** Real work *sheds* the debit (buyer takes it); a wash-trade *retains* it (make-and-keep nets ~zero, §3.2) and burns real overhead for nothing. Colluders end with ~zero net contribution, wrecked ratio, and debt they can only shed by dumping (→ OP-25 (illicit dumping)). Residual: gross fake hours → pledging-power → **OP-1 (service → influence)**. |
| **2 — Monopsony gatekeeper** | A sole downstream buyer withholds hand-off to control everyone's credit | **Debit-follows-possession inverts the leverage.** A maker's credit realizes at the *first* hand-off to *any* receiver; holding goods means holding their debit (worse ratio), so a hoarder is motivated to pass them on. Power to gatekeep evaporates. |
| **3 — Risk-dumper (mislabeling)** | An employer labels speculative work "pledged" to recruit, or vice-versa to shed risk | **The label is read off the *public* pledge ledger, not declared** (§5.3). Same move as co-product splits (§7.1a) and cost constants (§3.3a): never let a self-interested party write the number. |

**What the stress test changed before adoption:**
- The gatekeeper guard was *not* the author's first "any receiver" idea (which is wash-tradeable) — it is **debit-follows-possession + hand-off = verification**, discovered mid-pass.
- The count **self-audits**: a receiver eats the debit of exactly what they accept, so cannot be made to sign for phantom units (same incentive as §3.3a).
- **Realization ≠ deployment**: two separate clocks (§6.2b), and **transit custodians accrue no creation-cost share**.

**Side findings banked:** the wage-extraction **employer is structurally hollowed out** (→ OA7/P4); **demand risk is symmetric by hours**, not dumpable by rank (→ OA7 (coordinator class)); the **market-public/persons-private** transparency principle (→ OA9/OP-22).

**The one surviving residual.** Realized credit → pledging-power (influence) is measured in *gross hours*, so a consumption-indifferent zealot could collude to fake gross hours and pump influence — bounded by IC-7 (24-hour cap) (24 h/day) and paid in a wrecked ratio. *(The "self-starving" brake is **re-armed** under Foundations v0.14: pledging now spends a permanent, finite lifetime budget, so pledging is no longer free. An influence-pumper spends real budget to pump, and pledge-farming a task needs real verified colluders each burning their own budget on the public ledger — a cost, not a free ride. This narrows the residual but does not fully close it.)* **This is an OP-1 influence question, not a credit-accounting flaw.** Tests owed: §C.

---

<!-- tag: obj-b11 -->
## B12 — §3.2b electricity attribution (the real-time-dispatch principle) ✅ **PASSES WITH CHANGES**

**Shipped:** Foundations v0.10 §3.2b + §12; Overview v0.8 §4. **Source:** stress-test (`stress-test` skill), surfaced during Track 4 of the median-lifestyle calc, `03-journal/2026-08-10.md` / `2026-08-09.md`.

**The ruling.** Emissions from **real-time, demand-dispatched, non-storable** production follow the **end-user**; batch/stockpiled production stays with the producer. So electricity **generation** pollution is the consumer's (the plant is a tool under A1; the draw is the act) — aligning it with §3.2b's existing final-delivery-transport and personal-combustion rules.

**Verdict: PASSES WITH CHANGES.** The core insight is consistency-improving, but the *raw* form ("all generation pollution to the consumer, physical marginal unit") failed the exploit hunt:

1. **The dirty generator (offloader).** On a *pooled* grid the consumer cannot physically choose their source, so dumping the grid-average on them removes the pollution debit from the **only party that chooses the fuel** — weakening decarbonisation. → **Fix adopted: attribute by the consumer's *contracted supply mix* (provenance, §5.1b), not the marginal unit.** A clean generator can then offer lower-debit power and win contracts; the consumer still conserves. This also resolves the marginal-vs-average question (neither — it's the contracted mix). No-choice contexts use the local supply average + §6.4 pledges / §3.3 retroactive cleanup.
2. **The grid-factor understater (estimator-gamer).** All consumers benefit from a low grid emission factor → **OP-24 (understatement drift)**; policed by rival clean-energy audit (§3.3a). Not new.
3. **Justification contradiction (now resolved).** "You bear the marginal turbine" (physical) and "you choose green tariffs" (contractual) conflicted; contracted-provenance attribution keeps the second and drops the first.

**Axioms.** No conflict — Ellerman-motivated (A1: only the actor pollutes; the plant is a tool), and every emission stays internal (A4). **⚠️ Open universality edge:** real-time-vs-batch is a *spectrum* (grid storage, on-demand services); the mid-line criterion is registered open, not closed.

<!-- tag: obj-b11 -->
## B11 — Self-care as credited work & the definition of work ✅ **PASSES (instance of OP-10/OP-22)**

**Shipped:** Foundations §0, §6, §6.1b, §6.4, §6.4a→§6.4b, §7.5; EventLog §7.3a. **Source:** the work-definition session (author interview + `stress-test`), `03-journal/2026-08-07.md`.

**The cluster.** (1) Self-care (sleep, sustenance, basic care) is credited work — *time spent* maintaining the human, creditable because it costs time, not because anyone values it. (2) The definition of work is stated: time spent maintaining/contributing to human life; boundary against leisure delegated to networks. (3) Self-care is the *mechanism* of the §7.5 basic-needs floor — not a grant, so A2-clean. (4) Self-care credit generates full pledging-power (consumption + a **universal basic voice**); routing is a network lever; auto-pledge funds essentials. (5) Verification generalises by output type; enrichment verifies on occurrence, **never feedback** (OP-8 (feedback firewall) guard).

**Verdict: PASSES — as an instance of OP-10/OP-22, not a new hole.**

**Exploit hunt.**
1. **Generous-network arbitrage** (institution) — a network declares 20 h/day "maintenance"; members get near-max credit+influence for existing and flock to it. My first proposed fix ("anchor the floor to measured physiological need, *globally*") was **rejected by the author as anti-A8** — network weighting-pluralism is legitimate (A6/§3: shared log, differing weighting). **What actually stops it: counterparty re-computation.** A stingy counterparty re-weights the generous network's self-care *down* through its own model, so generosity cannot be *exported* — only shared among opt-in members (§6.4b). **Comparison, never conversion** — a conversion would be an exchange rate between credit-standards, a medium of exchange forbidden by A3/§7.6.
2. **Reciprocal service/enrichment attestation** (colluder) — two accounts attest each other's unverifiable service or thinking. **Bounded by §6.6 conservative weighting** (≈zero until third-party corroboration) + IC-7 (24-hour cap) + the ratio/debit-room cost. Not eliminated; the same shape as the wash-trade residual (B10).
3. **Basic-needs-scope creep** (institution) — a network defines "basic needs" broadly so auto-pledged self-care power floods favoured sectors. **Same root as #1** — a weighting choice, discountable by counterparties.

**Where the residuals route.**
- The arbitrage guard **depends on OP-22 (audit disclosure)**: re-computing a pledge's backing needs "backed by *X* hours under model *M*" provable in zero-knowledge, since ledgers are private (§5.3). *The market check is only as real as OP-22.*
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

**Shipped:** Foundations §7.6.

Ithaca HOURS and Burlington Bread both died of the *same specific mechanism*, and it was not valuation. Scrip flows toward businesses whose own inputs come from outside the network, making them one-way sinks. Ithaca's remaining businesses were **"drowning in Hours"**; Bread **piled up at Muddy Waters and Sugar Snap.**

**This cannot occur in Aequitas, because there is no medium of exchange.** Credit is non-fungible and never moves (A3 (non-fungibility)); only debit moves, attached to its object. **Nobody can drown in credit they cannot spend, because nobody ever receives credit *from* anyone.**

**Corollary — Wörgl.** The stamp scrip cut unemployment 16% while Austrian unemployment rose 19%, and was terminated by the Oesterreichische Nationalbank in 1933 to protect the legal-tender monopoly. **It was killed for working.** Aequitas has no issuer and no notes, so that instrument does not fit it. **The ban on calling Aequitas a currency is a strategic argument, not a branding preference.**

---

<!-- tag: obj-b3 -->
## B3 — Front-loading ✅ DISSOLVED OP-11, OP-5, OP-21

**Shipped:** Foundations §6.2, §6.2a; EventLog §6, §13.

> **A large up-front cost with diffuse benefit is carried when incurred, cushioned by the debit-room those who pledged for it grant. It is never amortized downstream onto whoever happens to consume the result.**

**~~OP-11 — training amortization.~~** Every candidate denominator was defective. **The A2 (time as measure) v0.3 amendment removes the downstream flow entirely, so there is no denominator to choose.**

**~~OP-21 — media reproduction.~~** Production is front-loaded and pledged; the audience pays **delivery only.** Pledgers **receive no profit and cannot receive one.**

**~~OP-5 — education.~~** Answered by the same amendment plus pledging, which supplies the limit. **No perpetual-studenthood exploit.**

**Why the question was malformed in all three cases:** downstream amortization always requires choosing an arbitrary window. **Front-loading removes the division rather than solving it.**

> **✅ Confirmed in v0.6 — OP-23 (shared overhead) closed by exactly this.** Tooling and plant *are* front-loaded and pledged rather than amortized into output. Overhead does not shrink — it stops being allocated to outputs at all (§6.2b). The bet recorded here paid out. See **B8**.

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

**Three things it buys:** A3 (non-fungibility) becomes a consequence rather than a design choice; a second independent route to §7.1; and the reply to *"why do the machine's owners get nothing?"* — because machines do not act.

*Take the principle, decline the institution.* **The cost of adopting him is OP-18 (labour & team credit)** — his own argument that joint responsibility is non-decomposable, now the project's blocking problem.

**Also banked — tractability:** [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) demonstrated in-kind calculation at national scale with sparse-matrix methods. **Cite them rather than re-proving it.**

---
---

<!-- tag: obj-c-tests-owed -->
## C. Tests owed

Named so they are not silently skipped. ~~**Test 1 is the sharpest surviving technical risk in the project.**~~ **Test 1 resolved 2026-08-05 — the sharpest risk is retired.**

1. **✅ Recursion convergence — RESOLVED 2026-08-05.** `06-simulation/recursion_convergence.py`, 5,224-run sweep, `RESULTS.md`. The allocation is a **non-negative linear fixed point** `p = c + Ãp` with `Ã, c ≥ 0` (Aequitas divides *by* the make-matrix, never inverts it), so for a productive economy (`ρ(Ã) < 1`) the solution is the Neumann series `Σ Ãⁿc` — **unique, non-negative, and iteration-reachable, independent of joint-production density.** Confirmed: **100% convergence** for `ρ < 1`, **zero** negative `min(p)` (4,098 economies, most-negative 2.9×10⁻¹⁵), rate `~ρⁿ`, `M=10⁴` in ~10 s. The rival **value/price** allocation (solving `v(B−A)=l`, which *does* invert `B`) went negative or non-invertible in **94.7%** of the same economies — including a hand-checked `v=[−1,2]`. **Sraffa/Steedman is blocked by construction, not by luck; IC-10's non-negativity is now derived.** Doubles as the first piece of C11 (arithmetic audits) and the synthetic half of the academic Sraffa reply.
2. **Understatement drift** (OA3 (understatement drift)). Simulate trust networks under §3.3a's incentives; find the rival density at which the drift stops being arrested.
3. **The fuzzy middle.** Hide-to-carcass ratios vary slightly by breed and feed. Does the rule behave sensibly at small differences? [Mackenzie et al. on biophysical allocation in livestock](https://pmc.ncbi.nlm.nih.gov/articles/PMC12971801/) is the hardest published case.
4. **Refinery re-derivation.** Process-physics allocation versus USEEIO price allocation on the same slate. **A materially different answer is the most publishable technical result available early.**
5. **OP-16 (onerousness gap) cleaner test.** Night-shift vs day-shift vs rural carrier. If identical, (b) is eliminated.
6. **Demand-risk floor adequacy** (B10 / hole 2b). Simulate a worker on a failed *speculative* run: does the basic-needs floor (§7.5) actually keep them out of destitution, and how does their exposure compare to a capitalist wage-worker who bears no inventory risk? A distributional check, not a break.
7. **Influence back-door** (B10 / OP-1 (service → influence)). Simulate collusive hand-offs manufacturing gross fake hours → pledging-power, against the IC-7 (24-hour cap) cap and the wrecked-ratio penalty. *(Note: under Foundations v0.13 pledging no longer costs the pledger debit-room, so the old "self-defeating because pledging drains you" brake is gone — the sim must ask whether IC-7 and the ratio penalty **alone** are enough, or whether a consumption-indifferent actor can still buy influence.)*
8. **Generous-network race + the disparity ceiling** (B11 / OP-14 (cohort shopping) / OP-24 (understatement drift) / OP-4 (debit tolerance)). **✅ Disparity-ceiling proof FORMALLY STATED + STRESS-TESTED → PASSES (2026-08-14)** — Part 1 (formal statement) + a plain-language explainer are in `06-simulation/DISPARITY_CEILING.md`; the adversarial pass dissolved all three attacks: **Methuselah** (credit/debit are cumulative event-log tallies and credit is never *spent* — the gate `D ≤ ρ·C` is a ratio checked per event, A3+A6 — so a lifelong hoarder's splurge only front-loads their own `ρ·C`; equal-age disparity is exactly `24/F`, the only spread beyond it is age); **dynasty/household** (a co-op, dwelling-debit split per occupant by dwelling-time — the bound is **per-person**, inheritance dilutes it); **collector** (holdings are a self-bounding burden). A **Methuselah self-test (Claim 4)** is in the sim (now **7 self-tests green**). **✅ Simulated 2026-08-10** — `06-simulation/disparity_ceiling_sim.py`, agent-based N = 200,000, gate `D_i ≤ ρ·C_i`, credit ∈ `[F,24]` h/day: **(a)** the `24/F` ceiling is exact and **ρ-independent** (2.4× for F = 10, flat across ρ ∈ [1,3]) *and* weighting-independent — it **does not depend on OP-10** — vs money 14× (income) / ~700–950× (wealth) on the same population; **(b)** a **ρ clears the market and moves like a prime rate** (a −30% capacity disaster tightens clearing ρ* ~1.25→~0.82), confirming *a ρ can be picked & adjusted*, not "the one true ρ"; **(c)** the ceiling is **fraud-invariant** — IC-7 (24-hour cap) bounds every account, so fraud fills the band but never exceeds it. **Structural results hold for any distribution; still conditional on OP-22** (the sim assumes the anti-arbitrage guard, does not model disclosure). **This is the strongest defensive result the project can hold**, now with a simulation behind it. **✅ Like-for-like vs REAL wealth micro-data DONE 2026-08-10** — the money side is calibrated to the 2022 Survey of Consumer Finances (wealth p99/median = 71×, reproduced) + the Forbes billionaire tail (~10⁶× the median); Aequitas caps command-over-resources at 2.4×, a **5–6 order-of-magnitude** compression. **✅ Consumption-axis real-distribution comparison DONE 2026-08-10** (`06-simulation/q4_locked_ledgers.py`, scenario-suite Q4) — applies the ceiling to real US/world distributions under the **material-only** rule (A1 corollary, Foundations v0.12 §1). Two results: **(i)** stripping the financial layer compresses the *observed* tail **~1,000×** (money wealth ~10⁶× → material consumption ~670×, Oxfam billionaire personal footprints), so the disparity the ceiling must cap is far smaller than money's; **(ii)** only **~0.1–2%** of people (ρ-dependent) sit past a *permanent* efficiency-ratio lockout — the ultra-consumers, not the merely rich — and even full divestment doesn't save them (permanent consumption debit); ~two-thirds gain room by joining. **Still owed:** only the **generous-network cohort-shopping race** (does the floor race to the IC-7 ceiling, or does §6.4b counterparty re-weighting arrest it?) — which is the OP-22-conditional part. The proof itself (Parts 1–3 + stress test) is **complete and PASSES**; what remains is the cross-network disclosure mechanism, tracked as **OP-22**. Rests on Foundations v0.15.

<!-- tag: obj-d-not-yet-examined -->
## D. Not yet examined

- **Ostrom** — polycentric governance, commons design principles. Bears on A8 (local governance) and OP-10 (weighting governance). **Highest value of these.**
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

The version-by-version change log (former §E) now lives in a separate file, read only when needed: **[`Aequitas_Objections_CHANGELOG.md`](Aequitas_Objections_CHANGELOG.md)**.

---

*End of v0.14.*
