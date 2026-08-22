# Aequitas Strategy — Change History

> Version-by-version change log for `Aequitas_Strategy_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the roadmap so it is read only when tracing **when and why** the plan changed. The roadmap's header carries a one-line summary of the current version. Superseded full versions live in `99-archive/`.

---

### v0.4 (2026-08-11) — roadmap refresh + presentation/pointer pass

**Roadmap refreshed to current reality.** The v0.3 critical path (`C1 → OP-18 → C3 → C4`) is retired: OP-17 and OP-18 are closed, the recursion-convergence sim passed (Sraffa blocked by construction), C11 is closed, and the scenario suite + disparity-ceiling sim shipped. Updated: §2 (claims now ship with passing sims), §3 component table (C3 in progress/unblocked, C11 closed, C5 pledge settled to the v0.13 revocable-grant model) + critical-path line, §4 Phase 1 (mostly cleared; C3 the remaining item) and Phase 2 (disparity-ceiling proof largely done), §6 sequencing (highest-risk unknowns are now governance: OP-10/OP-24/OP-16, not measurement), §7 risks (recursion + OP-18 rows retired; OP-10 and OP-16 rows added), §8 done-criteria (sims + OP-18 convention checked off).

**Presentation.** Companion pointers re-threaded (Foundations v0.13, Objections v0.14, EventLog v0.6); inline `*(new in vX)*` version-tags stripped; a Contents list added; the in-document change log (§9) extracted to this file. `../NEXT.md` remains the live task queue.

### v0.3
1. **Critical path rewritten: C1 (event-log schema) ✅ → OP-18 (labour & team credit) → C3 (estimation engine) → C4 (re-weighting).** OP-17 (joint production) is resolved; the blocking position **moved to OP-18** because labour left no physical trace where materials and energy did.
2. **The recursion convergence sim is promoted to the single highest-value next action** — it validates the OP-17 answer, and a negative result invalidates it.
3. **C12 (energetics registry) added** — process-energetics model registry, created by resolving OP-17 and home to OP-24 (understatement drift).
4. **Two risks added** (recursion non-convergence, understatement drift), **one retired** (OP-17 unsolvable), **one reframed** (trust-network capture).
5. **Second screening question adopted: "does this need an objective function?"** Both rejected OP-17 candidates did, and each would have re-opened OP-10 (weighting governance).
6. **Phase 1 and Phase 2 reordered** around the sim and OP-18. **Joint production added to the use-case set** — the sandwich already contained one and it went unnoticed for two versions.
7. **C5 (debit taxonomy) partially settled** — custody acceptance is decided (possession governs), so it drops off C5's open list and the debit-dumping defence becomes physical rather than ledger-based.
