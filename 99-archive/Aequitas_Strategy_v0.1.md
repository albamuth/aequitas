# Aequitas — Overall Strategy

> **Version:** 0.1 · **Date:** 2026-07-31
> **Target:** Implementer whitepaper (protocol specification) in ~3 months.
> **Companion docs:** `Aequitas_Foundations_v0.2.md` (axioms), `../NEXT.md` (task queue)

---

## 1. The Goal

**A protocol specification that a competent engineer could build against without talking to us.**

Not a manifesto. Not a pitch. A spec: data model, verification protocol, estimation engine, transfer rules, privacy layer.

**Why this first:** the theory is only real if it's implementable. Writing the spec forces every hand-wave into a decision. Academic, civic, and public documents come later and are *easier* once the spec exists — they can cite it.

---

## 2. Strategic Insight — sims are evidence, not a side project

The whitepaper's credibility rests on claims that sound impossible:
- "Collusion can be detected without a central authority."
- "Estimation converges from global average to individual truth."
- "Price ≡ cost is stable and doesn't require a planner."

**Each of these must ship with a Python simulation that demonstrates it.** The sims are figures and appendices in the whitepaper, not a separate deliverable. This is what separates Aequitas from every other utopian economic proposal — *ours has results.*

This also answers the socialist-calculation critique pre-emptively: we don't argue that computation is feasible, we show it running.

---

## 3. What must be solved before the whitepaper can be written

| # | Component | Status | Blocking? |
|---|---|---|---|
| C1 | **Event log data model** — schema for a material-flow record | Not started | ⛔ Yes |
| C2 | **Verification protocol** — all 4 levels, esp. L2 anti-collusion (OP-2) | Not started | ⛔ Yes |
| C3 | **Estimation engine** — global avg → cohort → individual (OP-3) | Not started | ⛔ Yes |
| C4 | **Re-weighting mechanism** — how a science update propagates through history | Not started | ⛔ Yes |
| C5 | **Debit taxonomy + transfer rules** — property vs consumption, self-work identity | Partial (Foundations §3.2) | ⛔ Yes |
| C6 | **Identity / proof-of-personhood** — one human, one account | Not started | ⛔ Yes |
| C7 | **Privacy layer** — private ledger with provable claims | Not started | Yes |
| C8 | **Credit type mechanics** — service→influence (OP-1), Enrichment firewall (OP-6/8) | Open problems | Partial |
| C9 | **Debit tolerance formula** (OP-4) | Not started | No — can be parameterized |
| C10 | **Cross-level trade** (OP-7) | Not started | No — can be v2 |

**Critical path: C1 → C2 → C3 → C4.** Everything else can proceed in parallel or be deferred.

---

## 4. Three-Month Roadmap

### Phase 1 — Core mechanisms (weeks 1–4)
*The theory lives or dies here.*

- **C1: Event log schema.** What exactly is one record? Actors, materials, energy, time, attestations, provenance links.
- **C2: OP-2 anti-collusion.** Design the social-graph audit. **Simulate it:** generate honest networks + colluding rings, measure detection rate. *If this fails, the project needs a fundamental rethink — better to know in week 3 than month 9.*
- **C3: Estimation engine.** Cohort hierarchy and convergence. Simulate: does an account's estimate converge to truth as facts are added?

**Exit criteria:** OP-2 has a working detection mechanism with simulation results, or a documented reason it can't and a fallback.

### Phase 2 — Completing the spec (weeks 5–8)

- **C4: Re-weighting.** How a mitigation-cost update recalculates all affected history. Simulate at scale for feasibility.
- **C5–C7:** Debit transfer rules, identity, privacy layer.
- **C8:** Resolve OP-1 (service→influence) enough to specify; firewall Enrichment (OP-8).
- **Use cases as validation.** Write the sandwich trace, the homeowner, the doctor, the film studio. Each must be expressible in the C1 schema. *If a use case can't be encoded, the schema is wrong.*

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

**Attack the highest-risk unknown first, always.**

OP-2 (anti-collusion) before anything cosmetic. The worst outcome is spending three months on polish and discovering in month four that decentralized verification doesn't work. Risk-first sequencing means bad news arrives early and cheap.

---

## 7. Known strategic risks

| Risk | Mitigation |
|---|---|
| **OP-2 is unsolvable** — social graphs can't defeat collusion | Front-loaded to Phase 1. Fallback: specify minimum viable centralization and be honest about it. |
| **Scope creep into philosophy** | `NEXT.md` parking lot. The whitepaper is a spec, not a treatise. |
| **Enrichment leaks into currency** (OP-8) | Explicit firewall clause in spec; adversarial review in Phase 3. |
| **Estimation is politically toxic** — "you assigned me a debt I didn't consent to" | Frame carefully: assignment is *modeling*, not obligation. Only account-holders have real standing. Needs a dedicated section. |
| **Perfection paralysis** | Ship v0.x drafts. Version, don't polish. |
| **Solo bandwidth** | Sims and drafts are Claude-executable. User's scarce attention goes to decisions, not production. |

---

## 8. What "done" looks like at 3 months

- [ ] `Aequitas_Protocol_v1.0.md` — complete, implementable spec
- [ ] 3+ Python simulations backing its central claims
- [ ] 4+ worked use cases, each encodable in the schema
- [ ] Wiki covering every core concept
- [ ] All 8 open problems either solved or explicitly scoped as v2

---

*End of v0.1.*
