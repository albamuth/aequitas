# Aequitas Strategy — Change History

> Version-by-version change log for `Aequitas_Strategy_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the roadmap so it is read only when tracing **when and why** the plan changed. The roadmap's header carries a one-line summary of the current version. Superseded full versions live in `99-archive/`.

---
<!-- tag: str-v0-6-2026-08-25 -->
### v0.6 (2026-08-25) - gains section 9, First Foothold, moved out of Foundations

**Author ruling: Foundations 11 is a discussion that should happen in Strategy.** It is a reading of the historical record on how a system like this gets a foothold, and it states nothing about what Aequitas is.

- **New section 9 - First Foothold.** Moved unchanged from Foundations 11: full-cost accounting as a parallel overlay; the warning that read cold this describes every complementary currency that died, and the distinction that saves it (**the overlay computes a number money cannot produce**); product and service debit-costing, with the refinery-versus-USEEIO target; the try-it account; and the WIR and Sardex finding that both survived by starting **B2B inside dense input loops**, countercyclically, so **a downturn is the moment.**
- **Section 9 also absorbs the document programme** from the tail of Foundations 9 - the five documents this project owes, with **item 2 now pointing at `Aequitas_Conformance_v0.2.md`.**
- **Three pointers repaired.** *"Foundations 9 carries the current list"* and the 3-month deliverable both now name `Aequitas_Conformance_v0.2.md`. The OP-10 risk row's reference to Foundations 10.1 now names **Foundations A8**, where that ruling moved. And the *"read as one more failed local currency"* row points at section 9 below rather than at Foundations 11.

**Nothing was cut and no strategic judgement changed.**

---
### v0.5 (2026-08-23) - scope fold: the goal is the system, not a protocol

**In lockstep with Foundations v0.18.** No component dropped, no sequencing changed, no axiom touched. C3 to C4 is still the critical path and governance (OP-10, OP-24, OP-16) is still the risk-first target.

**Why.** Foundations 1.2 ruled records and data collection praxis. **1 of this document was the sharpest contradiction of that ruling anywhere in the project**: it named the goal as *"a protocol specification that a competent engineer could build against"*, itemised as *"data model, verification protocol, estimation engine, transfer rules, privacy layer"* - and three of those five are exactly what 1.2 puts out of scope.

1. **1 rewritten.** The goal is now two halves: **the system**, stated and tested against scenarios; and **a conformance list**, the things that must hold for an implementation to *be* Aequitas (Foundations 9 carries it). A new paragraph names what is deliberately *not* the goal - data model, storage, transport, cryptography, privacy practice - and says plainly that the earlier framing is how the project spent nights on record-integrity work while its top blocker was governance. 1.2's dial test is added as the screen to apply before anything joins the roadmap.
2. **3 gains a reading note above the component table.** The components are not all the same kind of thing. **System work:** C3, C4, C5, C8, C9, C10, C12 - questions about how the economy behaves. **Conformance-boundary work:** C1, C2, C6, C7, C11 - where what is owed is *the requirement, not the design*. C11 is the worked case: *mass and energy must conserve across every recorded process* is the requirement; the Python that checks it and the field names it reads are praxis. **C7 is flagged as the one to watch** - "privacy layer" is an architecture name for something Foundations 5.3a already ruled a network choice, and what this project owes is OP-22's answer, not the layer.
3. **4 Phase 2 renamed** from *Completing the spec* to *Governance and the remaining mechanisms*. Contents unchanged (phases are not listed there).
4. **7 gains a risk row: scope creep into data architecture** - the one that actually happened. An outreach channel that rewards runnable code pulled two sessions into event-log integrity work. Mitigation is Foundations 1.2 + 9 and the dial test, plus watching the outreach queue specifically, **because the venue's incentive is not the project's**.
5. **8 done-criterion 1 renamed** - `Aequitas_Protocol_v1.0.md` becomes **`Aequitas_System_v1.0.md`**, by author ruling on 2026-08-23. *Protocol* named the deliverable after its smaller half. The document does not exist yet, so no file moved; `NEXT.md`'s goal line carries the same change.
6. **Header re-threaded** - Foundations v0.18, EventLog described as *record model* rather than *schema*, and the Target line restated as the system plus a conformance list.
7. **2 gains the code-deliverable ruling** *(author, same day, and it is the other half of the scope fold)*. 1 says what the documents are for; **2 now says what the code is for: a simulator of an economy, one or several, never a trust-network database.** The old line calling the sims *"figures and appendices in the whitepaper, not a separate deliverable"* is replaced - **they are the only way an axiom gets tested before someone bets a society on it.** **And it is one configurable engine, not a pile of scripts** - the author's eight example conditions are *configurations*, not deliverables, and the engine must express them plus thousands nobody has named. New companion document `Aequitas_Simulation_Roadmap_v0.2.md` carries the design. **Two structural findings: every existing societal sim is single-period** (as `rho_sweep.py` admits in its own limits), so the time axis has to be built; **and nothing in `06-simulation/` is the kernel** - each script re-implements its own credit accrual, gate and agents, which is why none composes with another. The **17-item conformance list from Foundations 9 becomes the kernel's invariant set**, asserted every period, so `arithmetic_audits.py` turns from a one-off audit into the engine's test harness.


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

---

## Header blocks moved from the document

> Lifted from the head of the versioned document on 2026-08-24, so the doc opens on its contents rather than on its history. Each line is the summary that version's header carried.

- **Supersedes:** `99-archive/Aequitas_Strategy_v0.4.md`. **Scope fold, in lockstep with Foundations v0.18.** Foundations §1.2 ruled that cost accounting is the principle while records and data collection are praxis. **§1 of this document was the sharpest contradiction of that ruling anywhere in the project** — it named the goal as *"a protocol specification that a competent engineer could build against,"* itemised as *"data model, verification protocol, estimation engine, transfer rules, privacy layer,"* and three of those five are exactly what §1.2 rules out of scope. **§1 is rewritten:** the goal is the **system**, stated and tested, plus a **conformance list** — what must hold for an implementation to be Aequitas, never how to build it (`Aequitas_Conformance_v0.2.md`). §3's component table now marks which components are system work and which are conformance-boundary work, so the distinction survives contact with the roadmap. Phase 2 is renamed off *"completing the spec."* **No component is dropped and no sequencing changes** — C3 → C4 is still the critical path, and governance (OP-10, OP-24, OP-16) is still the risk-first target. **And the deliverable is renamed:** §8's first done-criterion becomes **`Aequitas_System_v1.0.md`**, by author ruling the same day. *Protocol* named the whole thing after its smaller half; the deliverable is the economic system, and the conformance list is one section inside it.
- **Prior (v0.4):** **Roadmap refreshed to current reality** (2026-08-11), plus a presentation pass. The v0.3 critical path (`C1 → OP-18 → C3 → C4`) is retired: **OP-17 and OP-18 are closed, the recursion-convergence sim passed, C11 is closed, and the scenario suite (5 sims) + disparity-ceiling sim shipped.** The binding work is no longer *allocation/measurement* but **governance** — OP-10 (weighting model), OP-24 (understatement drift), OP-16 (onerousness). Component statuses (§3), phases (§4), sequencing (§6), risks (§7), and the done-criteria (§8) updated to match. Also: companion pointers re-threaded, inline version-notes stripped, a Contents list added, and the change log (§9) moved to `Aequitas_Strategy_CHANGELOG.md`. `../NEXT.md` remains the live task queue.
