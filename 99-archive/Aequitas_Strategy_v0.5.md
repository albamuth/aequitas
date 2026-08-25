<!-- tag: str-aequitas-overall-strategy -->
# Aequitas — Overall Strategy

> **Version:** 0.5 · **Date:** 2026-08-23
> **Target:** A statement of the system, tested against scenarios, in ~3 months — with a conformance list an implementer can build against.
> **Companion docs:** `Aequitas_Foundations_v0.23.md` (axioms), `Aequitas_Objections_v0.21.md` (register), `Aequitas_EventLog_v0.9.md` (record model), `../NEXT.md` (task queue)
> **Version history & what each version superseded:** `00-strategy/Aequitas_Strategy_CHANGELOG.md`.

---

<!-- tag: str-toc -->
## Contents

- [1. The Goal](#1-the-goal)
- [2. Strategic Insight — sims are evidence, not a side project](#2-strategic-insight--sims-are-evidence-not-a-side-project)
- [3. What must be solved before the whitepaper can be written](#3-what-must-be-solved-before-the-whitepaper-can-be-written)
- [4. Three-Month Roadmap](#4-three-month-roadmap)
- [5. Parallel tracks (low effort, high compounding)](#5-parallel-tracks-low-effort-high-compounding)
- [6. Sequencing principle](#6-sequencing-principle)
- [7. Known strategic risks](#7-known-strategic-risks)
- [8. What "done" looks like at 3 months](#8-what-done-looks-like-at-3-months)
- [Change history](#change-history)

---

<!-- tag: str-s1 -->
## 1. The Goal

**A statement of the economic system, tested against scenarios — and a conformance list a competent engineer could build against without talking to us.**

Not a manifesto. Not a pitch. **And not an architecture.**

> **Two halves, and the second one is small.**
>
> - **The system.** What Aequitas is, what must hold, and what follows. Every claim that sounds impossible ships with a simulation that demonstrates it (§2).
> - **The conformance list.** The things that must be true for an implementation to *be* Aequitas — conservation holds, the ledger is derived and never stored, credit never transfers, coverage is published with its extent, and so on. **Foundations §9 carries the current list.**

**What is deliberately not the goal.** A data model, a storage design, a transport protocol, a choice of cryptography, a privacy practice. **Foundations §1.2 rules all of these praxis**, and they belong to whoever implements. An earlier version of this section named three of them as deliverables, which is how this project spent nights on record-integrity work while its top blocker was governance.

> **The screening question, from Foundations §1.2: if a principle survives at both ends of a dial, the dial is not part of the principle.** Apply it before adding anything to the roadmap.

**Why this first:** the theory is only real if someone could implement it. Stating what must hold forces every hand-wave into a decision, and it does so **without** committing the project to design work that is not its own. Academic, civic, and public documents come later and are *easier* once the system is stated — they can cite it.

---

<!-- tag: str-s2 -->
## 2. Strategic Insight — sims are evidence, not a side project

The whitepaper's credibility rests on claims that sound impossible. Several now **ship with a passing simulation**; the rest are the remaining sim budget:

- ✅ **"Joint production allocation converges."** Recursion-convergence sim (`06-simulation/allocation-engine/recursion_convergence.py`, 5,224-run sweep) — **PASS**: the allocation is a non-negative Neumann series, 100% convergent for `ρ(Ã) < 1`, zero negative shares across 4,098 economies, while the rival value/price arm goes negative in ~95%. **Sraffa/Steedman blocked by construction.**
- ✅ **"Fraud undetected at rate *r* still cannot produce observed wealth distributions."** *(the disparity ceiling)* — `disparity_ceiling_sim.py` (N = 200,000): the `24/F` ceiling is exact, ρ-independent, and **fraud-invariant**, vs money's 10⁴–10⁶× tail. Still conditional on OP-22.
- ✅ **Societal-scale feasibility** — the five-sim scenario suite (`scenario_suite_METHOD.md`): labour is abundant, materials/energy bind.
- ◻ "Estimation converges from global average to individual truth." — C3 in progress on real EXIOBASE data.
- ◻ "Price ≡ cost is stable and doesn't require a planner." / "A demand signal arises from pledges alone." — owed.

**Each claim ships with a Python simulation that demonstrates it.** This is what separates Aequitas from every other utopian economic proposal — *ours has results.*

> **And the sims are what this project builds.** *(Author ruling, 2026-08-23.)* §1 says the deliverable is the system. **The code that serves it is a simulator of an economy — one or several — never a trust-network database.** A simulation is not a dial under the §1.2 test; **it is the instrument that tells you whether a principle survives one.**
>
> Earlier drafts of this section called the sims *"figures and appendices in the whitepaper, not a separate deliverable."* That undersold them. **They are the only way an axiom gets tested before someone bets a society on it**, and they are what the outreach agent should be asking strangers to run, extend, and attack.
>
> **And it is one configurable engine, not a pile of scripts.** The author's eight example conditions — a locality competing with money, different floors, gift-economy-only, carbon trajectories, collapse, population swings, a pollutant discovered late — are **configurations, not deliverables**. The engine must express those and thousands nobody has named. **If it needs an exception for any one of them, the design is wrong**, which is the universality test (§2 of Foundations) applied to software.
>
> **The programme: [`Aequitas_Simulation_Roadmap_v0.2.md`](Aequitas_Simulation_Roadmap_v0.2.md).** Two findings worth carrying here. **Every existing societal sim is single-period** — `rho_sweep.py` says so in its own limits — so the time axis has to be built. And **nothing in `06-simulation/` is the kernel**: each script re-implements its own credit accrual, its own gate, its own agents, which is why none of them composes with another.

This also answers the socialist-calculation critique pre-emptively: we don't argue that computation is feasible, we show it running. Cockshott & Cottrell already did the arithmetic at national scale, so the *tractability* half is citable rather than novel — **cite them and spend the remaining simulation budget on what is genuinely unproven** (governance, understatement drift, onerousness).

---

<!-- tag: str-s3 -->
## 3. What must be solved before the whitepaper can be written

> **Read this table through §1's split, because the components are not all the same kind of thing.**
>
> - **System work — most of it.** C3 (estimation engine), C4 (re-weighting), C5 (debit taxonomy), C8 (influence mechanics), C9 (debit-tolerance formula), C10 (cross-level trade), C12 (energetics registry). These are questions about how the economy behaves. They are the project.
> - **Conformance-boundary work — a narrower job than the name suggests.** C1 (event log), C2 (verification), C6 (identity), C7 (privacy layer), C11 (arithmetic audits). **What is owed here is the requirement, not the design.** C11 is the clean example: *mass and energy must conserve across every recorded process* is the requirement, and it holds at both ends of every dial. The Python that checks it, and any field name it reads, are praxis.
>
> **C7 is the one to watch.** "Privacy layer" is an architecture name for something Foundations §5.3a already ruled a **network choice**. What this project owes on it is OP-22's answer — *what is the minimum an auditor must see to verify a claim without seeing a history* — which is a requirement. **The layer itself is not ours to build.**

| # | Component | Status | Blocking? |
|---|---|---|---|
| C1 (event-log schema) <!-- tag: str-c1 --> | **Event log data model** | **✅ v0.3** — absorbed the allocation rule with no schema change | Done |
| C2 (verification / trust networks) <!-- tag: str-c2 --> | **Verification protocol** — all 4 levels | L2 is an emergent trust market. **Now also carries the trust-network shape question (register OA10 (auditor independence)).** | Partial |
| C3 (estimation engine) <!-- tag: str-c3 --> | **Estimation engine** — global avg → cohort → individual (OP-3 (estimation convergence)) | **In progress.** OP-18 closed (labour rides the material split, §3.4a), so C3 is unblocked; synthetic slice + test-MRIO loader built and the real EXIOBASE dataset is on disk. | In progress |
| C4 (re-weighting) <!-- tag: str-c4 --> | **Re-weighting mechanism** + conservative weighting (load-bearing four times over) | Not started | ⛔ Yes |
| C5 (debit taxonomy) <!-- tag: str-c5 --> | **Debit taxonomy + transfer rules** — property vs consumption, self-work identity, **pledge discharge and reversion** | Custody **settled: possession decides** (EventLog §5.2); the pledge is **settled as a permanent grant of debit-room** (Foundations v0.14); **reversion resolved — pledges are permanent and unspent ones burn, so nothing reverts.** | ✅ Reversion closed; transfer-rule detail remains |
| C6 (identity) <!-- tag: str-c6 --> | **Identity / proof-of-personhood** — one human, one account | Not started. *Now also the defence against debit dumping.* | ⛔ Yes |
| C7 (privacy layer) <!-- tag: str-c7 --> | **Privacy layer** + minimum audit disclosure set (OP-22 (audit disclosure)) | Not started | Yes |
| C8 (influence mechanics) <!-- tag: str-c8 --> | **Influence mechanics** — OP-1 (service → influence), feedback aggregation (OP-6 (feedback mechanics)) | Partial | Partial |
| C9 (debit-tolerance formula) <!-- tag: str-c9 --> | **Debit tolerance formula** (OP-4 (debit tolerance)) | Not started. ⬆⬆ *Now a **prerequisite of the disparity-ceiling proof** (2026-08-07): the consumption-ceiling formula IS the tolerance formula, so the ceiling cannot be stated while OP-4 is "just a knob." Also the error-tolerance of the whole accounting (§7.5).* | **Yes — for the disparity proof** |
| C10 (cross-level trade) <!-- tag: str-c10 --> | **Cross-level trade** (OP-7 (cross-level trade)) | Not started | No — v2 |
| C11 (arithmetic audits) <!-- tag: str-c11 --> | **Arithmetic audits** — IC-1…**IC-12 (boundary additivity)** as runnable checks | **✅ Closed** — `06-simulation/audits/arithmetic_audits.py`: 12/12 clean checks pass, 12/12 injected violations caught, incl. the projection-side IC-10…IC-12. | Done |
| **C12 (energetics registry)** <!-- tag: str-c12 --> | **Process-energetics model registry** — the published per-process data the allocation rule computes from, plus replication and rival-audit rules | **New.** Created by resolving OP-17 (joint production); where **OP-24 (understatement drift)** lives | Yes, but after C3 |

**Critical path: C1 ✅ → C3 (in progress) → C4.**

**The allocation problems that used to sit on the critical path are closed.** OP-17 split a joint process's materials and energy by measurement; OP-18 closed the labour half by *declared convention* (labour rides the material split, §3.4a) rather than an unfound measurement; the recursion-convergence sim confirmed the whole thing terminates. What is left on the build path is **C3 (estimation engine, in progress on real data) → C4 (re-weighting)**. The genuinely *unsolved* work is no longer measurement but **governance**: OP-10 (who controls the weighting model — the top blocker), OP-24 (understatement drift), and OP-16 (onerousness). Those are the risk-first targets now (§6).

---

<!-- tag: str-s4 -->
## 4. Three-Month Roadmap

<!-- tag: str-phase-1-core-mechanisms-weeks -->
### Phase 1 — Core mechanisms
*The theory lives or dies here. **Mostly cleared.***

- **C1 (event-log schema): Event log schema.** ✅ **Done** (EventLog v0.6).
- **OP-17 (joint production): co-product allocation.** ✅ **Done** — the process allocates itself (Foundations §3.4a).
- **Recursion convergence sim.** ✅ **Done — PASS** (`recursion_convergence.py`). Validated the OP-17 answer; doubles as the first piece of C11.
- **OP-18 (labour & team credit): labour allocation across co-products and teams.** ✅ **Closed** — a declared convention (labour rides the material split), axiom-scored against the Aumann–Shapley checklist and stress-tested.
- **C11: arithmetic audits.** ✅ **Closed** — IC-1…IC-12 runnable, all violations caught.
- **C3 (estimation engine): Estimation engine.** ◻ **In progress.** Cohort hierarchy on the **residual rule** (N − Y)/Z, both sides of the ledger; synthetic + test-MRIO built, now extending to real EXIOBASE data. **This is the remaining Phase-1 item.**

**Exit criteria (met on the cost side):** a median-adult basket now produces a true-cost figure in labour-hours with stated basis (`median_lifestyle_RESULTS.md`, ~1,600 h/adult·yr) — materials and energy measured, labour split by the declared convention. Remaining: fold that through the full C3 estimation engine on real data.

<!-- tag: str-phase-2-completing-the-spec -->
### Phase 2 — Governance and the remaining mechanisms (weeks 5–8)

- **C4 (re-weighting): Re-weighting**, including **conservative weighting** — now backing four separate mechanisms.
- **C12 (energetics registry): process-energetics registry** and the rival-sector audit rules. **OP-24 (understatement drift) sim** — at what rival density does understatement drift stop being arrested?
- **C5–C7:** transfer rules and pledge reversion; identity; privacy incl. OP-22's disclosure set.
- **C8 (influence mechanics):** Resolve OP-1 (service → influence) enough to specify.
- **Disparity-ceiling proof — ✅ largely done, coupled to OP-4 (debit tolerance) / C9 (debit-tolerance formula).** The strongest defensive result the project holds, now with a simulation behind it (`disparity_ceiling_sim.py`, `q4_locked_ledgers.py`): the between-people accrual ceiling is **`24 h ÷ floor` ≈ 2.4×**, exact, ρ-independent, and fraud-invariant, versus money's 10⁴–10⁶× tail; material-only, only ~0.1–2% sit past a permanent lockout. **OP-4's shape is settled** (per-person locally-set tolerance floor + personal efficiency ratio on the discretionary layer only — no global ratio). **Still owed:** the generous-network cohort-shopping race, and the whole result stays **conditional on OP-22**. *Watch, as before: no objective function tuning the tolerance, or it re-opens OP-10.*
- **Use cases as validation.** Sandwich ✅ (which turned out to contain a joint process — milling → flour + bran), plus homeowner, doctor, film studio. **Add an explicit joint-production case.**

<!-- tag: str-phase-3-write-and-harden -->
### Phase 3 — Write and harden (weeks 9–12)

- Draft the whitepaper.
- **Adversarial pass:** hostile review of every mechanism. Who games this?
- Wiki populated as a byproduct of writing.
- Publish.

---

<!-- tag: str-s5 -->
## 5. Parallel tracks (low effort, high compounding)

| Track | Cadence | Purpose |
|---|---|---|
| **Wiki** | Continuous | One concept page per mechanism as it's settled. |
| **Research archive** | As needed | Prior art. Prevents reinventing and arms the academic paper. |
| **Journal** | Every session | Decision log. Protects against re-litigating settled questions. |
| **Use cases** | Phase 2 | Validation instrument first, marketing asset second. |
| **Marketing** | Phase 3+ | Deliberately deferred. |

---

<!-- tag: str-s6 -->
## 6. Sequencing principle

**Attack the highest-risk unknown first, always.** Risk-first sequencing means bad news arrives early and cheap.

**The measurement unknowns that used to top this list — recursion convergence, then OP-18 — are resolved.** The highest-risk unknowns now are **governance**: OP-10 (who controls the weighting model, the top blocker), OP-24 (understatement drift — costs quietly bias low with no funder to correct them), and OP-16 (onerousness — tedium/indignity leave no material trace). Each is a *capture-surface* or *incentive* question rather than a physics one, and each wants a straw-man trust-network design or a sim before the whitepaper leans on it.

**Two screening questions worth applying to every mechanism from here:**

1. **"Does this need a Paul Glover?"** A mechanism that requires an enthusiast has an expiry date, and must pay its own maintainer from inside the system.
2. **"Does this need an objective function?"** Both allocation rules that were rejected for OP-17 (joint production) — Aumann–Shapley and Kantorovich shadow prices — required one, and each would have re-opened **OP-10 (weighting governance)** through the allocation layer. **It is a fast proxy for "does this create a capture surface?"**

---

<!-- tag: str-s7 -->
## 7. Known strategic risks

| Risk | Mitigation |
|---|---|
| **🔴 Weighting-model governance (OP-10 (weighting governance))** — whoever sets the cost model controls every balance in history without touching a rule | The **top blocker.** Partial answers: split-before-collapse (§3.2a), rival-sector audit for constants (§3.3a). The general problem is open; the answer is competing open variance under A8, still unspecified. Work it with OP-24 and §10.1 — three problems, one capture surface. |
| **🔴 Understatement drift (OP-24 (understatement drift))** — costs quietly bias low and nothing corrects them | Rival-sector audit (Foundations §3.3a). **Unproven.** Sim owed. Note this erodes **A4 (no externalities)** without breaking any equation, which is what makes it insidious. |
| **🔴 The onerousness gap (OP-16 (onerousness gap))** — tedium/indignity have no material signature, and nothing allocates labour to the boring necessary jobs | Half answered by A2 (exertion/hazard/skill resolve materially). Leading candidate for the rest: hour-ceiling differentiation (pay the premium in time off, not rate). All candidates speculative; check first how much is simply unmeasured hazard. |
| ~~**The allocation recursion does not converge**~~ | **Retired — the sim ran and passed.** Non-negative Neumann series, 100% convergent for `ρ(Ã) < 1`; Sraffa blocked by construction (`recursion_convergence.py`). |
| ~~**OP-18 has no defensible convention**~~ | **Retired — closed by a declared convention** (labour rides the material split), axiom-scored and stress-tested. |
| **The academic attack lands on preference revelation** (Mises/Hayek) | Largely answered: pledges + scarcity-as-debit. **Needs writing up, not inventing.** ⚠️ Guard against demand re-entering the *cost* side — the OP-17 session caught one such proposal. |
| **Read as one more failed local currency** | Foundations §7.6 and §11: no medium of exchange, so no circulation failure; the overlay computes what money cannot. |
| **Trust networks drift into issuer-pays capture** | Partly answered: a network concentrated in the sector it audits is captured by construction, and membership is public. **Full trust-network design deferred to C2 (verification / trust networks) by decision.** |
| **Scope creep into philosophy** | `NEXT.md` parking lot. |
| **🔴 Scope creep into data architecture** — the one that actually happened. An outreach channel that rewards runnable code pulled two nights into event-log integrity work while the top blocker was governance. | **Foundations §1.2 + §9.** The documents state what must be true, never how to build it. Apply the dial test before adding anything: *if a principle survives at both ends of a dial, the dial is not part of the principle.* Watch the outreach queue specifically — the venue's incentive is not the project's. |
| **Perfection paralysis** | Ship v0.x drafts. Version, don't polish. |
| **Solo bandwidth** | Sims and drafts are Claude-executable. User's scarce attention goes to decisions, not production. |
| ~~**OP-17 has no honest answer**~~ | **Retired.** It had one, and it was better than the fallback: a §1.1 row was *deleted* rather than filled in. |

---

<!-- tag: str-s8 -->
## 8. What "done" looks like at 3 months

- [ ] `Aequitas_System_v1.0.md` — the system stated and tested, plus the conformance list (Foundations §9). *Renamed from `Aequitas_Protocol_v1.0.md` on 2026-08-23: "protocol" named the deliverable after the smaller half of it.*
- [x] ~~3+ Python simulations backing its central claims, **including allocation-recursion convergence**~~ — **done and exceeded:** recursion convergence, the disparity-ceiling sim, the five-sim scenario suite, and the median-lifestyle anchor all ship.
- [ ] 4+ worked use cases, each encodable in the schema, **at least one with joint production**
- [ ] Wiki covering every core concept
- [x] ~~An allocation convention for OP-17~~ — **better: a measurement, not a convention**
- [x] ~~A declared labour-allocation convention for OP-18~~ — **done:** labour rides the material split, defended against the cooperative-game axioms (B9).
- [ ] Every open problem in `Aequitas_Objections_v0.21.md` either solved, dissolved, or explicitly scoped as v2 — **the remaining live blockers are governance: OP-10, OP-24, and OP-16's tedium/indignity half (its hazard half is addressed by the contingent reserve, §6.4c).**

---

---

<!-- tag: str-changelog-pointer -->
## Change history

The version-by-version change log (former §9) now lives in a separate file, read only when needed: **[`Aequitas_Strategy_CHANGELOG.md`](Aequitas_Strategy_CHANGELOG.md)**.

---

*End of v0.5.*
