<!-- tag: str-aequitas-overall-strategy -->
# Aequitas — Overall Strategy

> **Version:** 0.3 · **Date:** 2026-08-01
> **Target:** Implementer whitepaper (protocol specification) in ~3 months.
> **Companion docs:** `Aequitas_Foundations_v0.4.md` (axioms), `Aequitas_Objections_v0.5.md` (register), `../NEXT.md` (task queue)
> **Supersedes:** `99-archive/Aequitas_Strategy_v0.2.md`. See §9.

---

<!-- tag: str-s1 -->
## 1. The Goal

**A protocol specification that a competent engineer could build against without talking to us.**

Not a manifesto. Not a pitch. A spec: data model, verification protocol, estimation engine, transfer rules, privacy layer.

**Why this first:** the theory is only real if it's implementable. Writing the spec forces every hand-wave into a decision. Academic, civic, and public documents come later and are *easier* once the spec exists — they can cite it.

---

<!-- tag: str-s2 -->
## 2. Strategic Insight — sims are evidence, not a side project

The whitepaper's credibility rests on claims that sound impossible:

- **"Joint production allocation converges."** *(new, and now the top of the list)*
- "Estimation converges from global average to individual truth."
- "Price ≡ cost is stable and doesn't require a planner."
- "A demand signal arises from pledges alone, with no planner and no indicative prices."
- "Fraud undetected at rate *r* still cannot produce observed wealth distributions." *(the disparity ceiling)*

**Each of these must ship with a Python simulation that demonstrates it.** The sims are figures and appendices in the whitepaper, not a separate deliverable. This is what separates Aequitas from every other utopian economic proposal — *ours has results.*

> **🔴 The recursion sim is now the highest-value one, and it is a genuine risk rather than a demonstration.** Foundations §3.4a splits a joint process's debit by measuring where the process sent its inputs — but every input's own debit is itself a joint split, so the allocation is defined recursively **with no proof it terminates or converges.** If it does not, Sraffa re-enters through the back door and IC-10's non-negativity becomes an unsupported assertion. **This is the sharpest surviving technical risk in the project and it is cheap to test:** a sparse-matrix run over a synthetic joint-production economy, following [Cockshott & Cottrell's method](https://en.wikipedia.org/wiki/Towards_a_New_Socialism).
>
> Note the asymmetry that makes it worth doing first: **a positive result is a footnote; a negative result invalidates the answer to OP-17 (joint production).** Bad news should arrive while the answer is one week old, not three months old.

This also answers the socialist-calculation critique pre-emptively: we don't argue that computation is feasible, we show it running. Cockshott & Cottrell already did the arithmetic at national scale, so the *tractability* half is citable rather than novel — **cite them and spend the simulation budget on what is genuinely unproven.**

---

<!-- tag: str-s3 -->
## 3. What must be solved before the whitepaper can be written

| # | Component | Status | Blocking? |
|---|---|---|---|
| C1 (event-log schema) <!-- tag: str-c1 --> | **Event log data model** | **✅ v0.3** — absorbed the allocation rule with no schema change | Done |
| C2 (verification / trust networks) <!-- tag: str-c2 --> | **Verification protocol** — all 4 levels | L2 is an emergent trust market. **Now also carries the trust-network shape question (register OA10 (auditor independence)).** | Partial |
| C3 (estimation engine) <!-- tag: str-c3 --> | **Estimation engine** — global avg → cohort → individual (OP-3 (estimation convergence)) | **⛔ Blocked on OP-18 (labour & team credit).** *Materials and energy unblocked by OP-17's resolution; labour is not.* | ⛔ Yes |
| C4 (re-weighting) <!-- tag: str-c4 --> | **Re-weighting mechanism** + conservative weighting (load-bearing four times over) | Not started | ⛔ Yes |
| C5 (debit taxonomy) <!-- tag: str-c5 --> | **Debit taxonomy + transfer rules** — property vs consumption, self-work identity, **pledge discharge and reversion** | Partial. ~~Custody acceptance~~ **settled: possession decides** (C1 §5.2) | ⛔ Yes |
| C6 (identity) <!-- tag: str-c6 --> | **Identity / proof-of-personhood** — one human, one account | Not started. *Now also the defence against debit dumping.* | ⛔ Yes |
| C7 (privacy layer) <!-- tag: str-c7 --> | **Privacy layer** + minimum audit disclosure set (OP-22 (audit disclosure)) | Not started | Yes |
| C8 (influence mechanics) <!-- tag: str-c8 --> | **Influence mechanics** — OP-1 (service → influence), feedback aggregation (OP-6 (feedback mechanics)) | Partial | Partial |
| C9 (debit-tolerance formula) <!-- tag: str-c9 --> | **Debit tolerance formula** (OP-4 (debit tolerance)) | Not started. ⬆⬆ *Now a **prerequisite of the disparity-ceiling proof** (2026-08-07): the consumption-ceiling formula IS the tolerance formula, so the ceiling cannot be stated while OP-4 is "just a knob." Also the error-tolerance of the whole accounting (§7.5).* | **Yes — for the disparity proof** |
| C10 (cross-level trade) <!-- tag: str-c10 --> | **Cross-level trade** (OP-7 (cross-level trade)) | Not started | No — v2 |
| C11 (arithmetic audits) <!-- tag: str-c11 --> | **Arithmetic audits** — IC-1…**IC-12 (boundary additivity)** as runnable checks | Not started. **Now includes the first projection-side checks.** | No, but do it early |
| **C12 (energetics registry)** <!-- tag: str-c12 --> | **Process-energetics model registry** — the published per-process data the allocation rule computes from, plus replication and rival-audit rules | **New.** Created by resolving OP-17 (joint production); where **OP-24 (understatement drift)** lives | Yes, but after C3 |

**Critical path in v0.3: C1 ✅ → OP-18 → C3 → C4.**

**The critical path still runs through an open problem, and it moved without anything being solved twice.** OP-17 split a joint process's materials and energy by measurement. **Labour left no physical trace, so it did not move**, and C3 needs per-product labour hours. **OP-18 inherits the blocking position, and it is a genuine convention rather than an unfound measurement** — which means it will be *declared*, not solved.

---

<!-- tag: str-s4 -->
## 4. Three-Month Roadmap

<!-- tag: str-phase-1-core-mechanisms-weeks -->
### Phase 1 — Core mechanisms (weeks 1–4)
*The theory lives or dies here.*

- **C1 (event-log schema): Event log schema.** ✅ **Done** — v0.3.
- **OP-17 (joint production): co-product allocation.** ✅ **Done** — the process allocates itself (Foundations §3.4a).
- **🔴 Recursion convergence sim.** **Do this next.** It validates or invalidates the OP-17 answer, it is cheap, and it doubles as the first piece of C11 (arithmetic audits).
- **OP-18 (labour & team credit): labour allocation across co-products and teams.** ⛔ **The blocker.** Unlike OP-17 this is a genuine convention — the job is to choose one, justify it, and declare it in §1.1, not to find a hidden measurement. **Check the Aumann–Shapley axioms (efficiency, symmetry, dummy, additivity) as a selection checklist** — rejected as OP-17's rule, but they are exactly the right test for a convention.
- **C3 (estimation engine): Estimation engine.** Cohort hierarchy on the **residual rule** (N − Y)/Z, both sides of the ledger.
- **C11: arithmetic audits.** IC-1…IC-12 over a synthetic log.

**Exit criteria:** one median-household basket produces a true-cost figure with stated basis, confidence, and resolution — **with its materials and energy measured, and its labour split by a convention that is declared rather than hidden.**

<!-- tag: str-phase-2-completing-the-spec -->
### Phase 2 — Completing the spec (weeks 5–8)

- **C4 (re-weighting): Re-weighting**, including **conservative weighting** — now backing four separate mechanisms.
- **C12 (energetics registry): process-energetics registry** and the rival-sector audit rules. **OP-24 (understatement drift) sim** — at what rival density does understatement drift stop being arrested?
- **C5–C7:** transfer rules and pledge reversion; identity; privacy incl. OP-22's disclosure set.
- **C8 (influence mechanics):** Resolve OP-1 (service → influence) enough to specify.
- **Disparity-ceiling proof — now coupled to OP-4 (debit tolerance) / C9 (debit-tolerance formula)** *(scoped 2026-08-07)*. **If this proves out it is the strongest defensive result the project can hold.** Two ratios, not one, and they nest:
  - **Between people — the disparity ceiling.** With a **universal self-care floor** (a quantified §7.5 basic-needs floor, not credit-for-sleep — that would breach A2/§6.4a) and the IC-7 (24-hour cap) wall-clock cap, the consumption-*accrual* ratio is bounded by a small constant (**floor ÷ cap ≈ 10 h / 24 h → ~2.4×**) versus the unbounded Pareto tail under money. This is the headline.
  - **Within a person, over time — the debit tolerance (OP-4).** The consumption-ceiling formula *is* the tolerance formula, so **OP-4 must be settled to state the bound.** §3.5 rules out a single global debit:credit ratio (aggregate is always >1 and rising — thermodynamics — and a pure-ratio metric is infinite for a newborn), and A8 (local governance) rules out an expert-set global number (capture surface; fails the objective-function screen). Axiom-clean shape: a **per-person, locally-set tolerance floor + the personal efficiency ratio gating discretionary consumption only** — no central ratio.
  - **The simulation to run:** does the **discretionary layer stay positive over a lifetime** given permanent, ever-accruing consumption debit (§3.5)? And is the disparity ceiling stable under a stated fraud rate × magnitude? Compare the resulting consumption-ceiling distribution to real wealth data. *Watch: keep it descriptive — no objective function tuning the tolerance, or it re-opens OP-10 (weighting governance).*
- **Use cases as validation.** Sandwich ✅, homeowner, doctor, film studio. **Add a joint-production case explicitly** — the sandwich turned out to contain one (milling → flour + bran) and nobody noticed for two versions.

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

**In v0.3 that unknown is the recursion convergence sim, then OP-18 (labour & team credit).** The worst outcome available now is publishing an allocation rule that does not converge — which would be discovered by a reader rather than by us.

**Two screening questions worth applying to every mechanism from here:**

1. **"Does this need a Paul Glover?"** A mechanism that requires an enthusiast has an expiry date, and must pay its own maintainer from inside the system.
2. **"Does this need an objective function?"** *(new in v0.3)* Both allocation rules that were rejected for OP-17 (joint production) — Aumann–Shapley and Kantorovich shadow prices — required one, and each would have re-opened **OP-10 (weighting governance)** through the allocation layer. **It is a fast proxy for "does this create a capture surface?"**

---

<!-- tag: str-s7 -->
## 7. Known strategic risks

| Risk | Mitigation |
|---|---|
| **🔴 The allocation recursion does not converge** | Sim it in week 1. **A negative result invalidates OP-17's answer**, and it is far cheaper to find now than after C3 (estimation engine) is built on it. |
| **🔴 Understatement drift (OP-24 (understatement drift))** — costs quietly bias low and nothing corrects them | Rival-sector audit (Foundations §3.3a). **Unproven.** Sim in Phase 2. Note this erodes **A4 (no externalities)** without breaking any equation, which is what makes it insidious. |
| **OP-18 (labour & team credit) has no defensible convention** — team and labour splits stay arbitrary | Unlike OP-17 (joint production), this is *expected* to end in a declared convention. The risk is not "no answer" but "an answer a critic can dismantle." Use the cooperative-game axioms as the defence. |
| **The academic attack lands on preference revelation** (Mises/Hayek) | Largely answered: pledges + scarcity-as-debit. **Needs writing up, not inventing.** ⚠️ Guard against demand re-entering the *cost* side — the OP-17 session caught one such proposal. |
| **Read as one more failed local currency** | Foundations §7.6 and §11: no medium of exchange, so no circulation failure; the overlay computes what money cannot. |
| **Trust networks drift into issuer-pays capture** | Partly answered: a network concentrated in the sector it audits is captured by construction, and membership is public. **Full trust-network design deferred to C2 (verification / trust networks) by decision.** |
| **Scope creep into philosophy** | `NEXT.md` parking lot. |
| **Perfection paralysis** | Ship v0.x drafts. Version, don't polish. |
| **Solo bandwidth** | Sims and drafts are Claude-executable. User's scarce attention goes to decisions, not production. |
| ~~**OP-17 has no honest answer**~~ | **Retired.** It had one, and it was better than the fallback: a §1.1 row was *deleted* rather than filled in. |

---

<!-- tag: str-s8 -->
## 8. What "done" looks like at 3 months

- [ ] `Aequitas_Protocol_v1.0.md` — complete, implementable spec
- [ ] 3+ Python simulations backing its central claims, **including allocation-recursion convergence**
- [ ] 4+ worked use cases, each encodable in the schema, **at least one with joint production**
- [ ] Wiki covering every core concept
- [x] ~~An allocation convention for OP-17~~ — **better: a measurement, not a convention**
- [ ] **A declared labour-allocation convention for OP-18 (labour & team credit)**, defended against the cooperative-game axioms
- [ ] Every open problem in `Aequitas_Objections_v0.5.md` either solved, dissolved, or explicitly scoped as v2

---

<!-- tag: str-s9 -->
## 9. Changes in v0.3

1. **Critical path rewritten: C1 (event-log schema) ✅ → OP-18 (labour & team credit) → C3 (estimation engine) → C4 (re-weighting).** OP-17 (joint production) is resolved; the blocking position **moved to OP-18** because labour left no physical trace where materials and energy did.
2. **The recursion convergence sim is promoted to the single highest-value next action** — it validates the OP-17 answer, and a negative result invalidates it.
3. **C12 (energetics registry) added** — process-energetics model registry, created by resolving OP-17 and home to OP-24 (understatement drift).
4. **Two risks added** (recursion non-convergence, understatement drift), **one retired** (OP-17 unsolvable), **one reframed** (trust-network capture).
5. **Second screening question adopted: "does this need an objective function?"** Both rejected OP-17 candidates did, and each would have re-opened OP-10 (weighting governance).
6. **Phase 1 and Phase 2 reordered** around the sim and OP-18. **Joint production added to the use-case set** — the sandwich already contained one and it went unnoticed for two versions.
7. **C5 (debit taxonomy) partially settled** — custody acceptance is decided (possession governs), so it drops off C5's open list and the debit-dumping defence becomes physical rather than ledger-based.

---

*End of v0.3.*
