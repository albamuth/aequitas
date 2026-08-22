# Aequitas Event Log — Change History

> Version-by-version change log for `Aequitas_EventLog_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the spec so it is read only when tracing **when and why** the schema changed. The spec's header carries a one-line summary of the current version. Superseded full versions live in `99-archive/`.

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
