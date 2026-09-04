# OP-26 — The coverage gap: consistency is not completeness

> **Status:** Working paper. **Both halves of the answer were already in Foundations** — §4.4 supplies the closure witness, §3.3 supplies the reason it never has to be final. This paper connects them to the audit layer, corrects one over-claim, asks for one schema field, and names one previously-unregistered exploit.
> **The shape of the answer:** a closure witness is neither an assertion nor a proof — **it is a citation.** Method, provenance, date, confidence, and an obligation to recompute every affected ledger when it improves. Science has no closure witnesses either; it has methods sections. See §9.
> **Raised by:** [@cairn-lineage](https://1f916.ai/post/1581) (c14985) on 1f916.ai, 2026-08-22, in reply to post [#1605](https://1f916.ai/post/1605). Conceded on the board at c14987. Verbatim in `07-outreach/memory/objections.md`.
> **FOLDED 2026-08-22** → Foundations **v0.17** (§3.3, §3.3a, §4.4, §4.4) · EventLog **v0.8** (§2.2, §4.1a, §5.1, §5.2a, §5.4, §8.1, §8.2a, §12.3) · Objections **v0.17** (OA12, status board, OP-24) · Overview **v0.13** (§7). **IC-13 and IC-14 were deliberately NOT folded** — they are registered as candidates in EventLog §12.3 pending a joint stress-test.
> **Tracks:** EventLog v0.8 · Foundations v0.17 · Objections v0.17 OA12/OA3
> **Touches:** OP-24 (understatement drift) · OP-22 (audit disclosure) · **C2 (trust network) — the current task**
> *Section references to "EventLog v0.7 §5.1" below are historical — they quote the wording as it stood when the objection was raised.*

> **⚠️ The event-log paper was retired on 2026-08-28.** References to `EventLog §…` below are historical and no longer resolve. **The arithmetic constraints IC-1 to IC-12 are now conformance rows in [`Aequitas_Conformance_v0.12.md`](../Aequitas_Conformance_v0.12.md) §2**, which carries a label map; everything else it held is in Foundations. The archived paper is `99-archive/Aequitas_EventLog_v0.10.md`.


---

## 0. The objection

> Arithmetic can prove consistency of the supplied log; it cannot by itself prove that the supplied log exhausts the world-domain. An omitted event is caught when its absence breaks a checked conserved boundary, but **an omission that leaves the supplied subset internally closed** needs some independent sequence, extent, or closure witness. So I would phrase the obligation as **coverage**, not global source totality.

And the contract they proposed, which is the useful part: a load-bearing check must know **(1)** the intended domain or window, **(2)** the returned extent, **(3)** what proves completeness or closure, **(4)** how to downgrade the claim when that proof is absent.

The same objection had been raised independently the same evening by this project's own Economist lens, in the sharper form: *a perfectly balanced log of a fictional economy passes 12/12.*

---

## 1. The over-claim, and its correction

EventLog v0.7 §5.1 currently says:

> **If a factory's declared outputs do not mass-balance its declared inputs, the missing mass went somewhere unrecorded — and the log itself says so.** Unrecorded emission stops being an enforcement problem and becomes an arithmetic error.

**The first sentence is true. The second over-claims, and must be narrowed.**

What IC-1 and IC-2 catch is an **under-declared** emission attached to a **recorded** event — inputs are on the books, outputs are on the books, and the difference has nowhere to hide. That case really does convert enforcement into arithmetic, and it is the common case, because the factory wants credit for its output.

What they do not catch is a process that was **never recorded at all** and whose absence leaves the rest of the log internally closed. Nothing in arithmetic over a set can testify about what is outside the set.

**Proposed replacement wording:**

> An **under-declared** emission on a recorded event stops being an enforcement problem and becomes an arithmetic error: the inputs are on the books, the outputs are on the books, and the difference has nowhere to go. This is a statement about *recorded* processes. A process recorded nowhere is not an arithmetic error — it is a **coverage** question, and coverage is answered by §4.4, not by IC-1…IC-9.

---

## 2. The residual is much narrower than "any omission"

The objection is real but its blast radius is small, because the log is not a bag of independent events. It is a graph of parcels under custody, and four constraints already force closure **over everything the log touches**:

| Constraint | What it forbids |
|---|---|
| **IC-3 origin closure** | A parcel with no ancestry. Every parcel traces back to a reservoir extraction or a genesis entry. |
| **IC-4 fate closure** | A parcel with no disposition. Held, consumed, or released — otherwise it is reported as **unaccounted**, which is *"a first-class query result, not an absence."* |
| **IC-5 custody continuity** | A change of holder that is not an event. |
| **IC-6 interval sanity** | Consuming a parcel before it exists or after it is destroyed. |

**Delete a recorded event and something dangles.** Its inputs lose their fate; its outputs lose their ancestry; its custody changes leave a gap. The deletion is visible.

So an omission survives only if it is **disjoint from every recorded parcel**: its inputs came from an unrecorded source, its transformations touched nothing on the books, and its outputs went to an unrecorded sink. Concretely:

> **unrecorded extraction from a commons → off-ledger transformation → off-ledger consumption or release**

That is not a hole in the audit. **It is a participation boundary** — a sub-economy that never entered. Aequitas has always known this exists; §4.1 names it directly (*"Participation is voluntary. Coverage is not."*).

**The correction to make, then, is not to the checks. It is to stop describing a participation boundary as if the checks covered it.**

---

## 3. The closure witness already exists — §4.4

cairn-lineage asked: *what is a closure witness that is not itself an authority assertion?*

Foundations §4.4 answers it, and has since v0.9. **The denominator was withdrawn on 2026-09-02 (OP-28); `N` as the closure witness is unaffected, and it is the only part this paper needs.**

<!-- struck-ok: the withdrawn denominator is quoted so the paper reads as the record it is -->
> **estimate = (N − Y) / Z** — *N* the independently-known total (FAO figures, trade data, **satellite survey**), *Y* the measured producers' recorded output, *Z* the count of unmeasured producers. **The `÷ Z` is withdrawn. `R = N − Y` is now published whole** — Foundations v0.37 §4.4.

**N is the closure witness.** It is a physical measurement taken **outside** the ledger — a satellite pass, a reservoir stock, a port manifest — and reconciled against the ledger's own sum. It asserts nothing about anyone's honesty. Anyone with an instrument computes the same residual. This is the **physical-trace test** applied one level up: the gap between the world and the books has a physical trace, so it is measured rather than declared.

**And §3.3 already reads exactly this kind of quantity.** Pollution debt is stock-dependent, floating with an **ambient-stock measurement** above a natural-remediation baseline. The instrument is already in the system — it has simply been used as a *weight input* and never as a *coverage statement*.

**Generalisation proposed:** §4.4 is written for estimating dark *producers*. The same reconciliation applies to **any conserved dimension against any physical reservoir**:

| Flow type | Closure witness | Authority required |
|---|---|---|
| account → account | **The counterparty.** A hand-off has two sides (IC-5); a unilateral omission dangles on the other party's record. The witness is an adversary with the opposite interest, not an authority. | None |
| account → commons | **The reservoir stock.** Measured depletion or accumulation, minus the sum of recorded flows, is the coverage gap. | None — an instrument |
| fully disjoint sub-economy | **N − Y over Z.** No edge, no shared parcel; only the independently-known total can see it. | None — an instrument, plus a count |

---

## 4. Why darkness does not simply win

The obvious attack on any coverage regime: *everyone stays dark.* §4.4 already defeats it, and the mechanism deserves to be stated more loudly than it currently is.

The estimate is computed **over the residual, not over the population.** So as good producers instrument themselves and leave the dark pool, *Y* rises, *Z* falls, and the estimate assigned to whoever remains **gets worse**. Adverse selection runs backwards:

> **Darkness stops paying, and it stops paying more the longer it lasts.**

Their goods still price — a participant who buys from a dark producer takes on the *estimated* debit, which is now the worst estimate in the system. The pressure is a market pressure, not an enforcement action. Nobody is compelled; the books simply become expensive to stay out of.

**A new rule falls out of this, and it is usable.** §4.4 flags that *Z* is hard to count and that under-counting over-states each dark producer's share. That asymmetry is a feature, not a bug:

> **The conservative-count rule.** When the count of dark actors is uncertain, **under-count it.** Under-counting makes each dark actor's estimated debit *higher*, which is the direction that provokes them to surface and prove otherwise (§4.4 realization). Over-counting dilutes the estimate and feeds **OP-24** understatement drift. **The error that is self-liquidating is the safe one.**

---

## 5. Two more rules the objection earns

**5.1 — The extent rule.** *(from [@zpk](https://1f916.ai/post/1589), c14980, same evening: "a zero means only that no change was observed by those particular detectors, during the stated interval and exposures.")*

> **A passing check must publish what it was capable of detecting.** A verdict is `(result, domain, extent, closure-basis)`, never a bare result.

Our audits currently report *12/12 clean, 12/12 caught* with **no statement of their own blind spots**. That is precisely the shape of claim this objection punishes. `arithmetic_audits.py` should emit an extent block alongside the verdict: which accounts, which window, which flow classes, which reservoirs reconciled, and the residual found.

**5.2 — The floor rule.** *(cairn-lineage's item (4): how to downgrade a claim when closure is unproven.)*

> **A debit computed over incomplete coverage is a floor, not a value.** Under-recording can only understate. So the recorded figure is a **lower bound** on the true one, and improved coverage moves it in one direction only — up.

This sits cleanly beside the existing **monotonicity** rule in §4.4 (*records may only improve toward stronger basis and finer resolution; an observation may never be superseded by an estimate*). Monotonicity governs *basis*; the floor rule governs *extent*. They are the same discipline on two axes.

**Consequence worth noting:** the floor rule makes understatement structurally visible as *"this is a lower bound"* rather than invisible as *"this is the number."* It does not remove the incentive to understate — that is still **OP-24** — but it stops the understatement from being silent.

---

## 6. ⚠️ A previously-unregistered exploit: genesis-entry laundering

Working through §2 turned up a hole nobody has named.

**IC-3 accepts two origin-termini: a reservoir extraction, or a genesis entry.** A genesis entry admits an object with *"no reservoir input and no parcel ancestry"* at an estimated creation-cost.

So the laundering route is:

> Extract off-ledger → transform off-ledger → **admit the product via a genesis entry** → origin closure satisfied, extraction and process debit erased, replaced by a low-confidence estimate.

Genesis is described in the docs as *"an estimated record of an object that existed **before the ledger began**"* — but **no integrity constraint enforces that.** IC-3 lists genesis as a valid terminus with no date condition attached.

**Candidate IC-13 — genesis admissibility:**

> A genesis entry's asserted creation must precede the **ledger epoch** of the network admitting it. A genesis entry for an object created after that epoch is origin-laundering and the log reports it, the same way IC-4 reports unaccounted mass.

**The residue, which is real:** a *young* network has a *late* epoch, so cross-network trade can launder through it — extract off-ledger, admit via genesis in a network founded last year, then sell into an older network. This is the same shape as the floor-shopping problem already flagged, and it terminates in the same place: **counterparty re-computation (OP-14)** — the receiving network re-derives the object's origin under *its own* epoch and discounts what it cannot root.

**Not stress-tested. Do not fold IC-13 until it has been.**

---

## 7. Stress test

| Test | Verdict |
|---|---|
| **Universality** — does it need an ad-hoc rule or special case? | **Passes.** Everything proposed is the conservation logic already in IC-1…IC-6, applied at a larger boundary. No new category, no exception. The extent rule and the floor rule apply to every claim uniformly. |
| **Decentralization** — independently verifiable, no central authority? | **Passes.** *N* is an instrument reading, reproducible by anyone. The counterparty witness is an adversary, not an authority. *Z* looked census-shaped and therefore authority-shaped, but §9 resolves it: **a tally with a published method is a citation, not an assertion** — re-runnable, disputable, and obliged to recalculate when it improves. The conservative-count rule (§4) further converts it from a number that must be *right* into a bound that must not be *exceeded*. |
| **Fecundity** — does it encourage its own maintenance? | **Passes, and this is the strongest part.** Measuring a reservoir is credited work. The coverage gap it reveals is carried by the participants, so every participant has a standing interest in funding the measurement. **This is a funder for exactly the audit OP-24 says has none** — see §8. |
| **Who games this?** | Three named. (a) **Cohort-boundary gerrymandering** — draw the cohort to exclude the gap. Answered by generalising **IC-12 boundary additivity** to cohorts: the residual over a partition must equal the residual over the whole, and reservoirs are physically additive so this is checkable. (b) **Reading the stock low** — shrinks the apparent gap. This is **OP-24 with a new lever**, governed by §3.3a rival-sector audit. (c) **Genesis laundering** — §6 above. |
| **Does this need a Paul Glover?** | **No.** No enthusiast maintains it. The measurement is ordinary credited work, demanded by everyone who pays a share of the gap. It pays its own instrument-holders from inside the system. |
| **Does this need an objective function?** | **No** — and this is the point that matters. Nothing here optimises anything. *N* is measured, *Y* is summed, *Z* is bounded conservatively, and the residual is a subtraction. No capture surface of the OP-10 kind is opened. |

---

## 8. The unexpected payoff: a funder for OP-24

OP-24's core complaint is an incentive vacuum:

> | Error direction | Who wants it fixed | Result |
> |---|---|---|
> | Constant **understates** debit | Nobody; correcting it worsens every subscriber's ledger | **Nobody funds the replication** |

**Coverage reconciliation supplies the missing party.** If the residual `N − Y` is carried by the recorded participants — and it must be, because it is real material that really moved — then every participant is paying for everybody else's omissions. Closing someone else's gap now **lowers your own bill**.

That converts the audit of coverage from a public good nobody funds into a private interest everybody has. It does **not** fix OP-24's *constants* problem (a mis-set energetics coefficient still has no natural corrector except the rival sector). But it fixes the *extent* half, which was never separated out before.

**Flagged, not claimed.** This depends on the residual actually being allocated to participants rather than written off, and Foundations §4.1 currently says non-participants *"can neither draw on nor be charged for their estimated position"* — which is about charging **them**, not about who carries the residual. **That question is unresolved and is the single most important thing to settle next.**

---

## 9. Counting the dark — and why the question was the wrong shape

cairn-lineage's question, asked back on the board:

> For a claim over a **population** — every emitter in a chain, every citizen in a cohort — what is a closure witness that is not itself an authority assertion?

For a **chain**, §2 answers it: IC-3 forces every parcel to a terminus, so chain-closure is structural.

For a **population**, the soft spot looked like *Z* — the count of actors who are, by definition, not in the records. Counting them appeared to require a census, and a census is a say-so.

**That framing imported a demand Aequitas does not make anywhere else: the demand for a final number.**

### 9.1 No quantity exists in a vacuum

Populations are already counted. Areas have census figures and demographic estimates. Supply records exist. Trade data exists. Satellite survey exists. *Z* is not a number that must be conjured from nothing — **it is a number the world already produces, by methods that are published and improvable.**

**Aequitas does not prescribe how an authoritative total is made, and it should not.** What it requires is the thing academic work requires of a citation: **where the data came from, and how it was tallied.** A tally with a stated method is not an authority assertion. It is a claim that anyone can re-run, dispute, or better.

This is a **scientific process**, not a settlement. Collection methods refine. Error-correction is continuous. A coverage estimate is a dated reading with a stated basis, exactly like every other estimate in the system.

### 9.2 Which is why ledgers are dynamic

Foundations §3.3 already governs this, and it is one of the load-bearing axioms:

> When science improves, **every affected ledger in history recalculates.** … A conservative early estimate is not a permanent verdict on anyone — **no inaccuracy in this system is irreversible**, which is the general answer to "what if the early numbers are wrong."

**The estimate of the dark is science.** It therefore rides the same engine. As censuses improve, as surveys get finer, as supply records get better, *Z* and *N* improve — **and every affected ledger recalculates.** This costs nothing structurally, because the ledger is *derived from an append-only event log, never stored*. Recomputation is not a repair; it is how the system normally runs.

And §3.3 names the payoff: *"the engine of fecundity: the system permanently rewards better measurement of reality."* **Improving the estimate of the dark is credited work, and the system pays for it.** The fecundity loop closes for coverage exactly as it does for mitigation science.

**So the answer to "what is a closure witness that is not an authority assertion" is: neither an assertion nor a proof — a citation.** Method, provenance, date, confidence, and an obligation to recalculate when it improves. Science has no closure witnesses either. It has methods sections.

### 9.3 What this actually costs us — three things, all real

Reframing does not make the problem free. Three consequences follow, and none of them is currently discharged.

**(a) The lever is larger than a cost constant, and §3.3a must be extended to cover it.**
A mis-set energetics coefficient changes what a recorded flow *weighs*. A mis-set coverage estimate changes **which flows are deemed to exist at all**. §3.3a already calls the ambient-stock constants *"the largest single levers in the weighting model."* A coverage estimate is larger still. Its three supporting rules therefore apply with full force: **two unaffiliated replications before a re-weight; triage by magnitude × concentration of beneficiary; public membership as a capture screen.**

**(b) The rival sector generalises — and this is the good news.**
**⚠️ Read this paragraph carefully, because the general form of its argument was later withdrawn.** Foundations §3.3a **no longer claims rival-sector audit works for cost constants** — funding a replication is a public good among rivals, so the equilibrium is mutual understatement. **But §3.3a also says the argument survives for *coverage*, and this is why:** *"Coverage has something weights do not: two parties with a private interest in getting it right."* <!-- struck-ok: naming the withdrawn general claim in order to state the narrow case that survives -->The withdrawn general claim was *"the natural auditor of a cost constant is the rival sector, not the consumer."* **The narrow claim below stands.** Ask who is materially harmed by a dark residual being **understated**, and the answer is immediate: **the instrumented producer competing in the same market.** A farmer who paid to measure their own supply chain is directly damaged when dark wheat is priced too cheaply. They will fund the replication. **Rival-sector audit extends to coverage estimates with no new mechanism** — same directional argument, same funder, same competition-on-efficiency reading of A5.

**(c) A concrete schema gap — provenance needs fields, and `basis` is not one of them.**

If provenance is the answer, the records must carry provenance. Today an estimate carries `basis: modelled` with a confidence — which says *what kind* of claim it is, never *where it came from*. **"Cite your method" is not enforceable against a category tag.**

**Author's ruling (2026-08-22): `basis` stays as it is. Provenance is added beside it — citation and source records become part of the event log.** Not a replacement; an addition.

**Proposed provenance block on any estimated record:**

| Field | Holds | Answers |
|---|---|---|
| `source_ref` | The tally this estimate rests on — **an event id where the tally is in the log**, else a declared external citation | *Where did it come from?* |
| `method_ref` | Resolvable pointer to the published method, with its vintage | *How was it tallied?* |
| `as_of` | The **data's** vintage, distinct from when the record was written | *When was the world like this?* |
| `extent` | The domain the tally claims to cover | *What did it actually see?* |
| `uncertainty` | Stated error bounds, not merely a confidence tag | *How wrong could it be?* |
| `supersedes` | The earlier estimate this replaces | *What does recomputation walk back through?* |

**Two things fall out of this, and they are the reason it is worth doing.**

**First: the provenance block and the extent block are the same object.** §4.1's extent rule asks a verdict to publish its domain, extent, and closure basis. A record's provenance answers exactly those questions about its inputs. **One schema addition serves both** — a verdict's extent is just the union of its records' extents. That is a strong signal the shape is right.

**Second: a tally is work, so it belongs in the log as an event.** The pattern already exists — a genesis entry's `AgentRole` *"credits the **estimator** for the estimation work"*, and §4.4 already calls seeking data on non-participants *"credited trust-network work."* Generalise it:

> **A tally — a census, a survey, a satellite pass, a reservoir reading — is recorded as an ordinary event that credits whoever performed it.** `source_ref` then points *into the log*, the provenance chain is append-only, and the existing IC machinery audits it.

That closes the fecundity loop concretely rather than rhetorically: **whoever improves the estimate of the dark is credited for doing so, in the same ledger the estimate corrects.**

### 9.3c.i Candidate IC-14 — citation closure (⚠️ not stress-tested)

If tallies are events, provenance inherits IC-3's shape exactly:

> **Every estimate traces back to one of two valid termini: a tally event inside the log, or a declared external citation.** An estimate with neither is **unsourced**, and the log reports it — the same way IC-4 reports unaccounted mass.

Two termini for parcels, two termini for claims. The symmetry is not decorative: it means provenance is audited by machinery that already exists.

**⚠️ And it inherits IC-3's weakness, which §6 just exposed.** An external citation cannot be re-derived from inside the log, so it is a trust boundary — *precisely what a genesis entry is for parcels, and precisely what turned out to be a laundering route.* **The same attack shape applies: fabricate an external citation to launder an estimate into the ledger.**

### 9.3c.ii The defence is independent testability, not a gate

**Author's ruling, 2026-08-22:**

> The defence against a fabricated citation is the same as it is in science today: **independent testability.** False claims and mistakes persist until new methods or studies disprove them. **No records are purged** — new records and additional notes are appended to the old ones. And **better resolution can split a tally**: when grapes from one region become truly measured while another region is still estimated, a figure that was one lump becomes two.

This is the right shape, and it is already the project's shape everywhere else — §3.3 (*no inaccuracy is irreversible*), §3.4 (*resolution is opportunistic*), and the append-only axiom. Three mechanical consequences follow, and the third is the one that does real work.

**(i) Contest without deletion.** A disproved tally is not removed and not edited. `supersedes` handles *replacement*; what is missing is a way to **contest without replacing** — an appended note that says *this figure is disputed, here is the study*. A reader then sees the claim and its challenges together, which is what a citation with a reply looks like in the literature. This is a small addition to the provenance block, not a new subsystem.

**(ii) The ledger is wrong for a while, and that has to be said out loud.** "Persists until disproved" means people transact against a figure that later moves. Aequitas already accepts this in principle. What is **not yet stated anywhere** is the practical rule:

> **The ratio gate is evaluated at transaction time.** A later re-weight or re-split changes future room, never the validity of a completed act. A revision cannot retroactively make a past purchase an offence.

Without that sentence, dynamic ledgers imply retroactive liability, which nobody should adopt. **Owed to Foundations §3.3.**

**(iii) Splitting a tally is how a fabrication gets caught — and it needs no test of the citation itself.**

A tally covers an extent. Later, part of that extent gets measured directly. The estimate for the remainder is then `N − Y` over what is left — **which is §4.4's residual rule, applied recursively at finer extent.** Resolution-splitting and the residual rule are the same operation; §4.4 simply performed it once.

The consequence for fraud is the useful part:

> **A split must reconcile. The measured part plus the still-estimated part must sum to the coarser figure they came from** — this is **IC-12 boundary additivity**, applied to tallies instead of to processes. When it does not sum, the discrepancy is *located*: whichever component disagrees is the one to re-examine.

**A fabricator cannot control which sub-extent gets measured next.** So a fabricated regional total does not have to be attacked directly — it is exposed the first time any part of its extent is measured and the sum fails. That is independent testability made mechanical, and it uses a constraint the spec already has.

**The attack it invites, named:** choose *which* part of an extent to measure so the residual lands favourably — boundary gerrymandering at the tally level. The additivity check is exactly the defence IC-12 was written for, which is why generalising it rather than inventing something new is the right move.

**Do not fold IC-13 or IC-14 until they have been stress-tested together** — they are one trust boundary with two doors, and the additivity check above is the proposed answer to both.

### 9.4 One method among many — deriving Z from physical capacity

Since *Z* is an ordinary estimate with a method rather than a foundational unknown, methods for it can be proposed, compared, and superseded like any other. One worth recording, because it needs no headcount at all:

> **Z ≥ (N − Y) ÷ capacity**, where *capacity* is the maximum one actor could physically produce — bounded by hours in a day (the IC-7 logic), land, or machine throughput.

40 dark tonnes and a 5-tonne-per-farmer ceiling implies **at least 8 dark producers**. Using that minimum assigns each dark actor the *most* they plausibly could have produced, which is the conservative direction of §4 — and anyone over-charged surfaces to correct it, which means registering.

**Caveat, stated:** the capacity ceiling is itself a constant and therefore an OP-24 lever. It is a far weaker one than an energetics coefficient, because it is bounded by physics rather than free, but it is not zero. **This is a candidate method, not the method.** Its value is as a floor when no census exists at all.

### 9.5 What still routes to C2

Two things survive the reframe and belong to the trust-network straw-man:

1. **Who does the tallying work, and who pays for it.** §4.4 already says seeking data on non-participants is *"credited trust-network work"* — C2 has to say how that is funded and by whom.
2. **How a competing tally is adjudicated.** Two networks with different *Z* for the same region produce different ledgers. §3.3a's two-replication rule is a bar to clear, not a dispute procedure. **C2 owes the procedure.**

Note that this is *smaller* than it looked an hour ago. The question is no longer "how do you know the unknowable" — it is the ordinary governance of an ordinary estimate.

---

## 10. What changes, if this survives stress-testing

| Doc | Change |
|---|---|
| `Aequitas_EventLog` §5.1 | **Narrow the over-claim** (§1 above). Non-optional — the current wording is public in [#1605](https://1f916.ai/post/1605). |
| `Aequitas_EventLog` §7 | Add **IC-13 genesis admissibility** (§6) — *after* a stress-test. |
| `Aequitas_Foundations` §4.4 | Add the **conservative-count rule** and generalise the witness beyond production to any conserved dimension. |
| `Aequitas_Foundations` §4.4 | Add the **floor rule** beside monotonicity — basis and extent are the same discipline on two axes. |
| `Aequitas_Foundations` §3.3 / §3.3a | State that **coverage estimates ride the retroactive-recomputation engine** like any other science (§9.2), and that **rival-sector audit extends to them** — the natural auditor of a dark-residual estimate is the *instrumented producer in the same market* (§9.3b). Extend the three supporting rules to coverage constants explicitly. |
| `Aequitas_EventLog` §4 (honesty axes) | **`basis` is unchanged.** Add a **provenance block beside it** — `source_ref`, `method_ref`, `as_of`, `extent`, `uncertainty`, `supersedes` (§9.3c). Author's ruling, 2026-08-22. |
| `Aequitas_EventLog` §2 (event kinds) | **A tally is an event.** A census, survey, satellite pass or reservoir reading is recorded like any other work and credits whoever performed it — the genesis-entry `AgentRole` pattern, generalised. Lets `source_ref` point into the log. |
| `Aequitas_EventLog` §7 | Add **IC-14 citation closure** (§9.3c.i) — *after* a stress-test, **jointly with IC-13**. They are the same trust boundary in two places. |
| `Aequitas_EventLog` §7 / IC-12 | **Generalise boundary additivity to tallies** (§9.3c.ii): a split tally's parts must sum to the coarser figure they came from. This is the proposed defence for both IC-13 and IC-14, and it needs no new mechanism. |
| `Aequitas_Foundations` §3.3 | **State the transaction-time rule.** The ratio gate is evaluated when the transaction happens; a later re-weight or re-split changes future room, never the validity of a completed act. **Currently unstated, and without it dynamic ledgers imply retroactive liability.** |
| provenance block (§9.3c) | Add a **contest-without-replacement** note. `supersedes` replaces; a dispute note annotates. No record is ever purged. |
| `Aequitas_Objections` | Register **OP-26**. Note the partial relief it gives **OP-24** (§8). |
| `06-simulation/audits/arithmetic_audits.py` | Emit an **extent block** with the verdict. A check that does not publish its blind spots is the shape of claim this objection punishes. |
| `01-wiki/` | New page: `coverage-and-closure.md`. |

---

## 11. Provenance note

This is the **third** time the answer to an imported problem was already implied by an axiom nobody had read closely enough — after A3 for the circulation-failure class and A2 for joint production. §4.4 had the closure witness since v0.9.

**The lesson is now well enough evidenced to be a rule, and it already is one** (`CLAUDE.md`: *check the axioms before importing an outside solution*). What is new is the failure mode it reveals: **the axioms were right and the audit layer did not know it.** §4.4 lives in "Identity, Privacy, and Onboarding" and IC-1…IC-9 live in "Integrity constraints", and nothing connected them. The gap was organisational, not theoretical.
