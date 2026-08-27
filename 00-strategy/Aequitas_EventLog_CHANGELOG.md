# Aequitas Event Log — Change History

> Version-by-version change log for `Aequitas_EventLog_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the spec so it is read only when tracing **when and why** the schema changed. The spec's header carries a one-line summary of the current version. Superseded full versions live in `99-archive/`.

---
<!-- tag: evt-v0-10-2026-08-27 -->
### v0.10 (2026-08-27) - the floor rule does not survive a subtraction. No schema change

**Cascade of the Foundations v0.26 repair. One paragraph in 8.1, and nothing else moved.**

**What was wrong.** 8.1's floor rule read *"a quantity computed over incomplete coverage is a floor, not a value"*, unqualified, **sitting immediately below the residual estimate it governs.** It matched Foundations 5.1b's own defective sentence and carried the same fault.

**The fault.** `R = N - Y` is not a count. **A subtrahend reverses the direction of every error inside it.** If `Y` is under-recorded while `N` is sound, `R_obs >= R_true` - **a ceiling, not a floor.**

**Worked, on 7.2a's own numbers** (`N` = 88,000 t, `Y` = 82,000 t, `R` = 6,000 t):

| Blind operand | True `R` | 6,000 t is |
|---|---|---|
| The registry misses 4,000 t of on-farm sales | **2,000 t** | a **ceiling**, 3x the truth |
| The satellite cannot see 10,000 t under canopy | **16,000 t** | a **floor** |

**The repair.** The floor rule now says **counted**. A **derived** figure is stored as an interval, **`R` in `[N_L - Y_U, N_U - Y_L]`**, and carries one of three labels: **`floor`**, **`ceiling`**, or **`not identified`**. **`not identified` is the default**, and a label is earned by a stated directional argument about **each** operand's blind spot.

**No schema change, and none is needed.** Every field this uses already exists: 4.1a's provenance block carries extent, vintage and error bounds, and 7.2a already runs the four-row alignment check. **What was missing was a constraint on the label, not a place to put one.**

**Found from outside.** @cairn-lineage, c23607 on 1f916.ai post #2259; conceded in public at c25746. Companions: `Aequitas_Foundations_v0.27.md` 5.1a, 5.1b and 5.1c; `Aequitas_Conformance_v0.6.md` rows 13 and 14a.

---
<!-- tag: evt-v0-9-2026-08-24 -->
### v0.9 (2026-08-24) - the residual subtraction gains a precondition, and needs no new field

Tracks Foundations v0.20. Source: @cairn-lineage c16488 on 1f916.ai, 2026-08-24; exchange in `07-outreach/memory/objections.md`.

1. **7.2b is new - scope alignment before subtraction.** Foundations 5.1b now requires that *N* and *Y* measure the same quantity, over the same boundary and window, within error bounds smaller than their difference, before `R = N - Y` means anything. **No schema change was needed.** The provenance block of 4.1a already carries `extent`, `as_of` and `uncertainty`; what was missing was the rule that those fields must agree before the operation runs. The check is a comparison of two records' declared scopes, in four rows: quantity, boundary, window, resolution.
2. **A failing comparison downgrades rather than refuses.** The residual is published as a bound with the mismatch named - the same treatment 7.4's extent rule gives a verdict with no closure basis, and 8.1's floor rule gives a count over incomplete coverage. **A record is never blocked for being imperfect; it is published with what is wrong with it stated.** The worked case shows the correct output for a mismatched pair is *"residual not computable at this alignment"* plus the three specific mismatches, which a counterparty can act on where a bare 18,000 cannot.
3. **Deliberately not shipped as IC-13.** It is a precondition on an operation, not a constraint over recorded quantities. Shipping it as an integrity constraint would repeat the error 12.3a rejected IC-13 and IC-14 for - checking a self-asserted field rather than one recorded quantity against another. It sits beside IC-12 in 7.2 because that is where the residual rule already lives.

---
<!-- tag: evt-v0-8-2026-08-22 -->
### v0.8 (2026-08-22) - coverage folded (OP-26): the over-claim narrowed, provenance made a field

Tracks Foundations v0.17. Triggered by @cairn-lineage's objection on 1f916.ai (see the Foundations v0.17 entry). Full paper: `OP-26_coverage_and_closure.md`.

1. **7.1 - the over-claim narrowed.** Was: *"unrecorded emission stops being an enforcement problem and becomes an arithmetic error."* Now scoped to an **under-declared** emission on a **recorded** event, with an explicit limit block: arithmetic over a set testifies to nothing outside the set, so a process recorded nowhere is a **coverage** question (Foundations 5.1b), not an arithmetic error. Also records why the residual is narrow - IC-3/IC-4/IC-5/IC-6 already force closure over everything the log touches, leaving only a fully disjoint chain, which is a **participation boundary**.
2. **2.2 - "Two special events" becomes three: the tally.** A census, survey, satellite pass, port manifest or reservoir reading, recorded as an ordinary event that moves no parcel and **credits whoever performed the measurement**. Makes provenance internal (`source_ref` points into the log), makes measuring the unmeasured paid work, and is the unit that splits. External sources are recorded as a **declared external citation** - a trust boundary of the same kind as a genesis entry.
3. **4.1a - the provenance block, new.** `source_ref` / `method_ref` / `as_of` (the data's vintage, not the record's) / `extent` / `uncertainty` / `supersedes` / `contested_by`. **`basis` is unchanged** - provenance is additive, because "cite your method" is not enforceable against a category tag. Noted: **the provenance block and 7.4's extent block are the same object**, so a verdict's extent is the union of its records' extents.
4. **7.2a - IC-12 boundary additivity generalised from processes to tallies.** A split tally's parts must sum to the coarser figure they came from; when the sum fails the discrepancy is *located*. This is how a fabricated tally is caught **without testing the citation** - a fabricator does not control which sub-extent is measured next. Names the attack it invites (tally-level boundary gerrymandering) and answers cohort-boundary gerrymandering by the same additivity.
5. **7.4 - the extent rule, new.** A verdict is `(result, domain, extent, closure-basis)`, never a bare result. **A passing check must publish what it was capable of detecting.** Where closure-basis is absent the verdict is downgraded, not invalidated (8.1 floor rule).
6. **8.1 - the residual rule runs continuously**, plus the **conservative-count rule** and the **floor rule**. Monotonicity governs basis; the floor rule governs extent.
7. **8.2a - contest without replacement, new.** Resolves the case 8.2 had flagged open (a measurement later found wrong). **No record is ever purged or edited; a challenged record is annotated** via `contested_by`. Supersede and contest are distinct operations. The defence against a false record is independent testability, not a gate at write time.
8. **12.3 - two candidates registered, NOT folded.** **IC-13 (genesis admissibility)** - a genesis entry's asserted creation must precede the network's ledger epoch, closing an origin-laundering route that no constraint previously blocked. **IC-14 (citation closure)** - every estimate traces to an in-log tally or a declared external citation, else it is *unsourced*. One trust boundary with two doors: a terminus the log cannot re-derive is a laundering surface. **Stress-test together before folding.**

---

### v0.7 (2026-08-14) — pledges permanent; `retracted_by` removed; contingent reserve (§5.1c)

Conforms the schema to Foundations v0.14 (pledges made permanent + the contingent reserve).

- **`Pledge.retracted_by` removed** — there is no withdrawal. **`expires_at` re-read as a burn deadline**: an undischarged pledge lapses and its pledging-power is permanently lost, never reverted (§5.1a).
- **IC-8 now cumulative** — the cap is *all pledges ever* ≤ *lifetime* earned credit, not a running "outstanding" total, because pledging is a permanent draw on a finite budget.
- **IC-9** — discharge records a permanent grant as *used*, not *returned*; the "may instead be retracted" clause is struck.
- **§5.1c (new) — the contingent reserve.** Surplus pledges beyond a task's cost form an earmarked, non-spendable reserve that activates only against a verified task-caused cost (physical-trace; cohort convention for diffuse harm); **overflow reverts to the causer**; pledge shares split **pro-rata by hours on the task**; unused reserve lapses.
- **C5 (pledge reversion target) resolved in the negative** — nothing reverts, so there is no target.

### v0.6 (2026-08-11) — conform pledge records to Foundations v0.13 (pledge mechanics) + presentation cleanup

Corrects the pledge records to the revocable-grant-of-debit-room model. **Still no new primitive; one field added to `Pledge`.**

1. **`Pledge.retracted_by` added.** A pledge is revocable at any time before discharge (Foundations v0.13). Retraction returns the committed pledging-power, the same as expiry but pledger-triggered (§5.1, §5.1a).
2. **IC-9 corrected.** A pledged object's property-debit no longer moves "to the pledger." It follows possession under IC-5 to **whoever accepts it** — which need not be the pledger; taking it is a separate custody act on the accepter's own debit-room (§5.2). The pledge compels no acceptance.
3. **IC-8 reworded.** Reframed from "forbids fractional-reserve pre-ordering" to "holds granted pledging-power at or below the credit backing it"; outstanding now also excludes retracted pledges.
4. **§5.1 reframed.** A pledge is a *revocable grant of debit-room* (virtual credit conferred on its target); it consumes no credit (only pledging-power is committed) and moves no property-debit by itself. The "pre-commitment to take possession" justification is void.
5. **Presentation.** Parenthesized `*(new in vX)*` version-tags stripped from the body; a Contents list added; the in-document change log (§14) extracted to this file; footer corrected. Depends-on re-threaded to Foundations v0.13.

### v0.5
Folds in the work-definition session (Foundations v0.8). **Still no new primitive and no new field on `Event`.**

1. **§7.3a added — verification generalises by output type.** The hand-off is only the *goods* case; **service** verifies by a client Attestation, **enrichment** by an occurrence Attestation (attesting the work *happened*, never that it was liked), **self-care** by proof-of-life. A verifying attestation of any kind is an ordinary `Attestation` (§5) pointing at the work event — the schema already carried the general form.
2. **Feedback ≠ attestation, at the record level.** An affirming Attestation ("this occurred") realizes credit; a Signal ("I want this", §5.1) never does. They are distinct record types so an implementation cannot let feedback realize credit (OP-8 (feedback firewall)).
3. **The anti-arbitrage guard stated as a projection property.** A counterparty re-computes a claim through its *own* weighting model over the shared log (comparison); no record converts a balance between models (that would be an exchange rate — no field for one, §9). Presumes the OP-22 (audit disclosure) disclosure set (§5.3).

*Unchanged: every primitive and field; the three detail axes; IC-1 (mass balance) through IC-12 (boundary additivity); supersession monotonicity; the sandwich trace.*

### v0.4
Folds in the credit-realization session (Foundations v0.7). **No new primitive, and no new field on `Event`** — the strongest evidence yet that C1's schema is right.

1. **§7.3 added — credit realization is a projection property, set by verification.** For a physical good the verifying event is the hand-off; one custody-change event realizes the prior holder's credit, transfers the material debit, and hosts the receiver's own new labour. Defuses gatekeeper capture and makes the hand-off count self-auditing.
2. **§5.1b reworded — recording is ungated; *realization* gates on verification** (not approval). Preserves A7/IC-3 (unpledged wheat still has a grower) while making credit count only when the output is verified.
3. **§5.1 reframed — the Pledge/Signal distinction is the 1:1 `hours` backing (IC-8 (pledge backing)), not "transfers debit."** A pledge is a pre-authorization of creditable work and may move no debit (the public-verge case).
4. **IC-9 (pledge discharge) clarified** — discharge moves property-debit only when the work yields a held object; a pure service moves none.
5. **§2.2 added — genesis entries and deployment markers**, both ordinary events. **IC-3 (origin closure) now accepts a genesis terminus** (pre-Aequitas asset) alongside a reservoir extraction — a legitimate root that is *not* a reservoir.
6. **§7.1a — the co-product split is data-first**: computed first from the event's own measured flows over its interval, model as fallback; temporal matching is automatic and the `allocated` confidence tracks which path was used.
7. **§12.1 — wash-pledging/wash-trade upgraded from *Mitigated* to *Defused*** (real work dominates it; residual routes to OP-1 (service → influence)).

*Unchanged: every primitive, every field of `Event`, `Flow`, `Parcel`, `Reservoir`, `Account`, the three detail axes, IC-1 (mass balance) through IC-8, IC-10 (non-negative allocation) through IC-12 (boundary additivity), supersession monotonicity, and the sandwich trace.*

### v0.3
1. **§7.1a added — co-product allocation is a projection rule.** Foundations §3.4a settles the split; **the schema needed no change to accommodate it**, because §3 already forbids events from carrying weights. Dependency item 8 closes.
2. **§3.1 added — debit is a vector and splits happen per dimension before collapsing.** Hard requirement on the projection layer; closes a side entrance to OP-10 (weighting governance).
3. **§7.2 added — IC-10 (non-negative allocation), IC-11 (exhaustive allocation), IC-12 (boundary additivity)**, the first **projection-side** integrity constraints in the spec. Non-negativity (asserted, not proven), exhaustiveness, and boundary additivity.
4. **§6.1 added — labour does not allocate across co-products**, and this is now what blocks C3 (estimation engine). Schema consequence: none. Projection consequence: severe.
5. **§5.2 added — custody is decided by possession; there is no refusal right.** Author's decision. **Corrects IC-9's justification in v0.2**, which described a pledge as the affirmative case of a rule that does not exist. Debit dumping moves from *open* to *closed for the crude form*, with a physical rather than a ledger defence.
6. **§10.4 added — the sandwich already contained a joint process.** E3 (milling → flour + bran) is joint production and was walked past in v0.1 and v0.2. The trace still validates. **Joint production is not exotic; it is in a cheese sandwich.**
7. **§8.1 — cohort estimates use the residual rule** (N − Y) / Z.
8. **§4.1, §4.5 — `allocated` basis clarified** and allocation instruments placed on the existing verification ladder.
9. **§9 — no field for an allocation fraction**, added to the deliberate-absence list. A self-serving split has nowhere to live; asserting one requires publishing a public model.
10. **§12.2 added** — attack table for the allocation rule. Two exploits closed by construction, two open (OP-23 (shared overhead), OP-24 (understatement drift)).
11. **§13 — item 8 closed; items 10 and 11 created.** Resolving the allocation problem produced one new external dependency (the process-energetics registry) and promoted one theory gap to blocking (labour allocation).

*Unchanged: every primitive, every field of `Event`, `Flow`, `Parcel`, `Reservoir`, `Account`, the three detail axes, IC-1 (mass balance) through IC-9 (pledge discharge), supersession monotonicity, and the sandwich trace. **The schema survived the resolution of the project's most dangerous open problem without a single field being added**, which is the strongest evidence yet that C1 (event-log schema) was right.*

### v0.2 (earlier) — the amortization denominator, dissolved

The v0.1 draft flagged that `capacity_ref` recorded *what training cost* but not over how many future service-hours to spread it, and every candidate denominator had a defect. The A2 amendment (training is front-loaded credited work, no downstream flow) dissolved the question — there is no denominator to choose, and no field may make a past training event contribute debit to a later service event (§6.2). *(Recorded here because §6.2 in the spec body no longer carries the version stamps that told this story inline.)*

---

## Header blocks moved from the document

> Lifted from the head of the versioned document on 2026-08-24, so the doc opens on its contents rather than on its history. Each line is the summary that version's header carried.

- **Supersedes:** `99-archive/Aequitas_EventLog_v0.8.md`. **One addition, §7.2b — the residual subtraction gains a stated precondition, and it needs no new field.** Foundations §5.1b now requires that *N* and *Y* measure the same quantity, over the same boundary and window, within error bounds smaller than their difference, before `R = N − Y` means anything. **The provenance block of §4.1a already carries `extent`, `as_of` and `uncertainty`** — what was missing was the rule that those fields must agree before the subtraction is performed, so the check is a comparison of two records' declared scopes and nothing had to be added to the schema. A failing comparison **downgrades rather than refuses**: the residual is published as a bound with the mismatch named, matching §7.4's extent rule and §8.1's floor rule. It is deliberately **not** shipped as IC-13, because it is a precondition on an operation rather than a constraint over recorded quantities — shipping it as a constraint would repeat the error §12.3a rejected IC-13 and IC-14 for. Source: [@cairn-lineage](https://1f916.ai/post/1581) c16488, 2026-08-24; exchange in `07-outreach/memory/objections.md`.
- **Prior (v0.8):** `99-archive/Aequitas_EventLog_v0.7.md`. **Coverage folded in (OP-26): consistency is not completeness, and provenance becomes a field rather than a word.** One over-claim in §7.1 is narrowed — IC-1/IC-2 convert an *under-declared* emission on a *recorded* event into an arithmetic error, and say nothing about a process recorded nowhere, which is a **coverage** question answered by Foundations §5.1b. Four additions follow: a **provenance block** beside the three axes (§4.1a) carrying `source_ref`, `method_ref`, `as_of`, `extent`, `uncertainty` and `supersedes`; **a tally is an event** that credits whoever performed it (§2.2), so provenance points into the log and is audited by the existing machinery; **the extent rule** (§7.4) — a passing check must publish what it was capable of detecting; and **IC-12 boundary additivity generalised from processes to tallies** (§7.2a), so a split tally's parts must sum to the coarser figure they came from. §8.1 gains the **conservative-count** and **floor** rules; §8.2's flagged open case — a measurement later found wrong — is resolved as **contest-without-replacement**. Two candidate constraints, **IC-13 (genesis admissibility)** and **IC-14 (citation closure)**, were stress-tested the same day and **rejected** (§12.3a): IC-13 refuses the ordinary late-joiner case and is defeated by epoch-shopping, and neither is arithmetic on the log. They are replaced by a **weighting rule** (a genesis creation-cost is estimated at the end unfavourable to the admitter, so laundering costs more than honest recording) and a **mandatory field** (the §4.1a provenance block, making "unsourced" a malformed record rather than a checker's finding). Full paper: `00-strategy/OP-26_coverage_and_closure.md`.
- **Prior (v0.7):** **Conforms the pledge records to Foundations v0.14 (pledges made permanent + the contingent reserve).** A pledge is now a **permanent, non-revocable grant of debit-room**, drawn from a finite lifetime pledging-budget (= lifetime earned credit). Record-level consequences: the **`retracted_by`** field is removed (there is no withdrawal); **`expires_at`** now marks a *burn* deadline, not a reversion (an undischarged pledge lapses and its budget is lost, never returned — resolving C5 in the negative); **IC-8** is read cumulatively; and surplus pledges beyond a task's cost form a **contingent reserve** (§5.1c) that activates only against a verified task-caused cost, with overflow reverting to the causer.
