# Aequitas — Overall Strategy

> **Version:** 0.2 · **Date:** 2026-08-01
> **Target:** Implementer whitepaper (protocol specification) in ~3 months.
> **Companion docs:** `Aequitas_Foundations_v0.3.md` (axioms), `Aequitas_Objections_v0.4.md` (register), `../NEXT.md` (task queue)
> **Supersedes:** `99-archive/Aequitas_Strategy_v0.1.md`. See §9.

---

## 1. The Goal

**A protocol specification that a competent engineer could build against without talking to us.**

Not a manifesto. Not a pitch. A spec: data model, verification protocol, estimation engine, transfer rules, privacy layer.

**Why this first:** the theory is only real if it's implementable. Writing the spec forces every hand-wave into a decision. Academic, civic, and public documents come later and are *easier* once the spec exists — they can cite it.

---

## 2. Strategic Insight — sims are evidence, not a side project

The whitepaper's credibility rests on claims that sound impossible:
- "Estimation converges from global average to individual truth."
- "Price ≡ cost is stable and doesn't require a planner."
- "A demand signal arises from pledges alone, with no planner and no indicative prices."
- "Fraud undetected at rate *r* still cannot produce observed wealth distributions." *(the disparity ceiling)*

**Each of these must ship with a Python simulation that demonstrates it.** The sims are figures and appendices in the whitepaper, not a separate deliverable. This is what separates Aequitas from every other utopian economic proposal — *ours has results.*

This also answers the socialist-calculation critique pre-emptively: we don't argue that computation is feasible, we show it running. [Cockshott & Cottrell](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) already did the arithmetic at national scale with sparse-matrix methods, so the tractability half is citable rather than novel — **cite them and spend the simulation budget on what is genuinely unproven.**

*Removed in v0.2:* "collusion can be detected without a central authority." Level 2 is now treated as an emergent market of trust networks where auditing is credited work, not as a detector to be designed and demonstrated up front. Promising a detection rate was promising something no detector holds permanently.

---

## 3. What must be solved before the whitepaper can be written

| # | Component | Status | Blocking? |
|---|---|---|---|
| C1 | **Event log data model** — schema for a material-flow record | **✅ v0.2** — validates against the sandwich trace | Done |
| C2 | **Verification protocol** — all 4 levels | Reframed; L2 is an emergent trust market, not a detector | Partial |
| C3 | **Estimation engine** — global avg → cohort → individual (OP-3) | **⛔ Blocked on OP-17** | ⛔ Yes |
| C4 | **Re-weighting mechanism** + conservative weighting (now load-bearing) | Not started | ⛔ Yes |
| C5 | **Debit taxonomy + transfer rules** — property vs consumption, self-work identity, **custody acceptance, pledge discharge and reversion** | Partial (Foundations §3.2, §6.4; C1 §5.1) | ⛔ Yes |
| C6 | **Identity / proof-of-personhood** — one human, one account | Not started | ⛔ Yes |
| C7 | **Privacy layer** — private ledger with provable claims, **minimum audit disclosure set (OP-22)** | Not started | Yes |
| C8 | **Influence mechanics** — service→influence (OP-1), feedback aggregation (OP-6) | ~~Enrichment firewall~~ **dissolved**; OP-1 has a strong candidate | Partial |
| C9 | **Debit tolerance formula** (OP-4) | Not started | No — can be parameterized |
| C10 | **Cross-level trade** (OP-7) | Not started | No — can be v2 |
| **C11** | **Arithmetic audits** — IC-1…IC-9 as runnable checks over a synthetic log | **New.** Cheap; needs no trust model; makes C1 executable | No, but do it early |

**Critical path in v0.2: C1 ✅ → OP-17 → C3 → C4.**

**The critical path now runs through an open problem, not a component.** OP-17 (co-product allocation) sits between a finished schema and any publishable cost figure, and no amount of work on C3 removes it. **Resolving OP-17 is the single highest-value action available.**

---

## 4. Three-Month Roadmap

### Phase 1 — Core mechanisms (weeks 1–4)
*The theory lives or dies here.*

- **C1: Event log schema.** ✅ **Done** — v0.2, validates against the sandwich trace end to end.
- **OP-17: co-product allocation.** ⛔ **The blocker.** Choose and justify an allocation convention, then test the *same* rule against a slaughterhouse, an oil refinery, and a CHP plant. A rule needing a different justification in each is disqualified. *If no rule survives, say so in §1.1 and publish the convention as a declared convention rather than a measurement.*
- **C3: Estimation engine.** Cohort hierarchy and convergence, on both sides of the ledger. Simulate: does an account's estimate converge to truth as facts are added?
- **C11: arithmetic audits.** IC-1…IC-9 over a synthetic log. Cheap, needs no trust model, and turns C1 from a document into something executable.

**Exit criteria:** one median-household basket produces a true-cost figure with stated basis, confidence, and resolution — **and a named allocation convention.**

### Phase 2 — Completing the spec (weeks 5–8)

- **C4: Re-weighting**, including **conservative weighting** — escalated, since OP-20's closure depends on it.
- **C5–C7:** Debit transfer rules incl. custody acceptance and pledge discharge/reversion; identity; privacy layer incl. OP-22's minimum disclosure set.
- **C8:** Resolve OP-1 enough to specify. ~~Firewall Enrichment~~ — **no firewall is required**; the live question is whether feedback can be *bought* (OP-8, reframed).
- **Disparity-ceiling proof.** With fraud undetected at rate *r* and magnitude *m*, what distribution results, and how does it compare to observed wealth data? **If this proves out it is the strongest defensive result the project can hold.**
- **Use cases as validation.** Sandwich ✅, homeowner, doctor, film studio. Each must be expressible in the C1 schema. *If a use case can't be encoded, the schema is wrong.* **The film studio is now a real test** — it exercises front-loading, pledges, and delivery-only consumer debit at once (Foundations §6.2a).

### Phase 3 — Write and harden (weeks 9–12)

- Draft the whitepaper.
- **Adversarial pass:** hostile review of every mechanism. Who games this?
- Wiki populated as a byproduct of writing (concept pages extracted from spec).
- Publish.

---

## 5. Parallel tracks (low effort, high compounding)

| Track | Cadence | Purpose |
|---|---|---|
| **Wiki** | Continuous | One concept page per mechanism as it's settled. Becomes the reference layer for all later docs. |
| **Research archive** | As needed | Prior art: LCA databases, contribution accounting, Ostrom's commons work, proof-of-personhood, reputation systems. Prevents reinventing and arms the academic paper. |
| **Journal** | Every session | Decision log. Protects against re-litigating settled questions. |
| **Use cases** | Phase 2 | Validation instrument first, marketing asset second. |
| **Marketing** | Phase 3+ | Deliberately deferred. Don't sell an unfinished idea. |

---

## 6. Sequencing principle

**Attack the highest-risk unknown first, always.** Risk-first sequencing means bad news arrives early and cheap.

**In v0.2 that unknown is OP-17, not OP-2.** The worst outcome is now spending three months building an estimation engine and discovering that no honest allocation rule exists, so every figure it publishes rests on a convention nobody chose deliberately. That is a month-one discovery, not a month-four one.

**Fourth screening question, added with Foundations v0.3: "does this need a Paul Glover?"** Ithaca HOURS died when its founder relocated. Any mechanism that requires an enthusiast to keep running has an expiry date, and must instead pay its own maintainer from inside the system.

---

## 7. Known strategic risks

| Risk | Mitigation |
|---|---|
| **OP-17 has no honest answer** — every co-product split is arbitrary | Front-loaded to Phase 1. Fallback: **declare the convention in Foundations §1.1 rather than concealing it.** A named convention is survivable; a disguised one is a universality failure. |
| **The academic attack lands on preference revelation** (Mises/Hayek) | Largely answered: pledges (§6.4) supply a decentralized demand signal, plus scarcity-as-debit on the Kantorovich framing. **Needs writing up, not inventing.** |
| **Read as one more failed local currency** | Foundations §7.6 and §11 address it directly: no medium of exchange, so no circulation failure; the overlay computes what money cannot. |
| **Scope creep into philosophy** | `NEXT.md` parking lot. The whitepaper is a spec, not a treatise. |
| ~~**Enrichment leaks into currency**~~ | **Dissolved.** Feedback was never credit, so there is nothing to firewall. Residual: can feedback be bought? (OP-8, reframed.) |
| ~~**Estimation is politically toxic**~~ | **Resolved by the A7 v0.2 amendment.** Symmetric estimation means the system describes what you contributed *and* what it cost. |
| **Founder dependency** | The fourth screening question, applied to every mechanism. Auditing-as-credited-work is the model. |
| **Perfection paralysis** | Ship v0.x drafts. Version, don't polish. |
| **Solo bandwidth** | Sims and drafts are Claude-executable. User's scarce attention goes to decisions, not production. |

---

## 8. What "done" looks like at 3 months

- [ ] `Aequitas_Protocol_v1.0.md` — complete, implementable spec
- [ ] 3+ Python simulations backing its central claims
- [ ] 4+ worked use cases, each encodable in the schema
- [ ] Wiki covering every core concept
- [ ] **An allocation convention for OP-17, chosen and defended**
- [ ] Every open problem in `Aequitas_Objections_v0.4.md` either solved, dissolved, or explicitly scoped as v2

---

## 9. Changes in v0.2

1. **Critical path rewritten.** C1 is done; the path now runs **C1 ✅ → OP-17 → C3 → C4**, through an open problem rather than a component.
2. **OP-2 deprioritized** and removed from the simulation set. Level 2 is an emergent market of trust networks where auditing is credited work — not a detector to design and demonstrate up front, since no detector stays ahead of attackers permanently.
3. **OP-17 promoted to the top risk** and to Phase 1, with a concrete disqualifying test (one rule across slaughterhouse, refinery, CHP).
4. **C11 added** — arithmetic audits over a synthetic log. Cheap, trust-model-free, and it makes C1 executable.
5. **Two risks retired** (Enrichment firewall, estimation toxicity), **three added** (OP-17 unsolvable, misread as a local currency, founder dependency).
6. **Simulation set updated** — tractability is now citable via Cockshott & Cottrell rather than something to demonstrate; the disparity ceiling and the pledge-driven demand signal replace it.
7. **Fourth screening question** adopted from Foundations v0.3 §2.

---

*End of v0.2.*
