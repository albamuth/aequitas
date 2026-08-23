# Aequitas Foundations — Amendment Record

> Version-by-version change history for `Aequitas_Foundations_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the main document so it is read only when tracing **when and why** something changed. The main doc's header carries a one-line summary of the current version; everything below is the archive.

---
<!-- tag: fnd-v0-17-2026-08-22 -->
### v0.17 (2026-08-22) - coverage folded (OP-26): consistency is not completeness

No axiom changed. Triggered by the **first objection to Aequitas raised from outside the project** - [@cairn-lineage](https://1f916.ai/post/1581) (c14985) on 1f916.ai, against post [#1605](https://1f916.ai/post/1605): *arithmetic can prove consistency of the supplied log; it cannot prove the log exhausts the world-domain.* Conceded on the board (c14987). Full paper: `OP-26_coverage_and_closure.md`.

1. **3.3 - coverage estimates ride the retroactive-recomputation engine.** Added: how many actors sit outside the records is not conjured from nothing - censuses, supply records, trade data and satellite survey already produce it by published, improvable methods. **Aequitas does not prescribe how an authoritative total is made; it requires what a citation requires - where the data came from and how it was tallied.** A coverage figure is therefore a dated reading with a stated basis, and when the science improves every affected ledger recalculates (free, because A6 derives rather than stores). The fecundity loop closes for coverage: improving the estimate of the dark is credited work, recorded as a **tally event** (EventLog 2.2).
2. **3.3 - the transaction-time rule, previously unstated anywhere.** `D <= rho*C` is evaluated **at the moment of the transaction**. A later re-weight, re-split, or coverage revision changes *future* debit-room and never retroactively invalidates a completed act. Without this, a dynamic ledger implies retroactive liability, which nobody should adopt.
3. **3.3a - rival-sector audit extends to coverage, with no new mechanism.** The natural auditor of an understated dark-residual is the **instrumented producer competing in the same market**, who is materially harmed when undocumented produce prices too cheaply. Also noted: a coverage figure is a **larger lever than a cost constant** - it changes which flows are deemed to exist at all - so the three supporting rules (two unaffiliated replications, triage by magnitude x beneficiary concentration, public-membership capture screen) apply with full force.
4. **3.3a - OP-24 gains partial relief.** If the residual `N - Y` is carried by recorded participants, closing someone else's coverage gap lowers your own bill, so the audit of **extent** has a funder even though the audit of **weight** still does not. WARNING - **conditional and flagged:** 5.1 forbids charging non-participants but says nothing about who bears the residual. Unresolved; next item on OP-26.
5. **5.1a - the floor rule, beside monotonicity.** A quantity computed over incomplete coverage is a **floor, not a value**; improved coverage moves it in one direction only. Monotonicity governs *basis*, the floor rule governs *extent*. Also stated: **a record is never purged or edited, only annotated** - falsehood is not prevented at write time, it is made permanent, traceable, and arithmetically exposed once any part of its extent is measured.
6. **5.1b - the witness generalises, and the conservative-count rule.** *N* is named as the **closure witness**: a physical total measured outside the ledger and reconciled against the ledger's sum, asserting nothing about anyone's honesty. Table of three witness classes (counterparty / reservoir stock / `(N-Y)/Z`). **Conservative-count rule:** when *Z* is uncertain, **under-count it** - the self-liquidating error is the safe one. The residual rule is stated as **continuous**, splitting as extents become measured, with parts reconciling against the parent (EventLog 7.2a). One candidate method recorded: `Z >= (N - Y) / capacity`, needing no headcount.

**Deliberately NOT folded:** IC-13 (genesis admissibility) and IC-14 (citation closure) - candidates only, EventLog v0.8 12.3, pending a joint stress-test.

**Same-day amendments (2026-08-22, sessions 2-3):**

7. **5.1c - the residual is held, not allocated (NEW SECTION).** Author's ruling. A coverage gap is computed and published but is **debit on nobody**. When a dark producer onboards, their share is **back-traced from records that already exist** - the ambient-stock reading of 3.3 and the independently-known total of 5.1b - and assigned to **the actual causer**. Until they onboard they cannot transact at all. **A4 is pending, not abandoned**: the cost is held as a computable claim awaiting a claimant, rather than written off or charged to innocent participants (which would contradict 3.2's "stays with whoever caused it" and be collective punishment in the sense 3.3 already rejects). The damage is priced meanwhile through the ambient stock - participants pay a rate reflecting *total* damage on their *own* units only. The gap is expressed as a **published coverage figure** (the extent rule at regional scale), which a counterparty can discount under OP-14. **Open and flagged in the section: how far back the back-trace reaches** - charging years of past emissions would contradict 5.1 and the transaction-time rule and would make onboarding a punishment.
8. **3.3a - the OP-24 relief CORRECTED.** As folded earlier the same day it read: *"if the residual is carried by the recorded participants ... closing someone else's coverage gap lowers your own bill."* **That premise is false under 5.1c** - the residual is carried by nobody. The relief survives on different and better grounds: coverage has **two funders a weighting constant lacks** - the **rival producer**, materially harmed when undocumented produce prices too cheaply, and the **dark producer themselves**, who cannot transact until onboarded. **Neither requires the residual to be allocated.**
9. **IC-13 / IC-14 stress-tested and REJECTED** the same day (EventLog v0.8 12.3a). Replaced by the author's **origin-evidence ruling** - a good must show its logistical origin-chain record and the seller must be onboarded; absent records the cost is estimated as all dark production is, so the producer **forfeits their efficiency gains and inherits the pool's averaged pollution**. No date is tested. Owed to Foundations 6.2a and 5.1b on the next fold.
10. **5.1d - the back-trace horizon is birth (NEW SECTION).** Author's ruling. A person onboarding has their position reconstructed **from birth**, and **symmetrically** - a lifetime of estimated consumption arrives with a lifetime of self-care credit. The arithmetic is the argument: ~3,650 h/yr credited for being alive against ~1,380 h/yr of embodied consumption, so per year of life credit runs ~2.6x consumption and **onboarding is a windfall for a median person**. It costs only those whose lifetime consumption genuinely exceeded their contribution - correct targeting. Evidence (residences, jobs, commuting distance, vehicles, mileage) is **voluntary**, moves the figure in **either** direction, and **may arrive at any later date**, re-deriving the ledger under A6 and 3.3 with no new machinery. Two conditions folded with it: estimates for undisclosed periods are computed over the **undisclosed residual** (5.1b's rule generalised from producers to periods within a life, so selective disclosure is expected and self-correcting rather than an exploit), and estimates **err against the estimated party on both sides** so evidence always pays - with the **self-care floor exempt**, because it is credited by proof-of-life and not estimated at all. Neither 5.1 nor the transaction-time rule is contradicted: nothing is charged before onboarding, and pre-onboarding acts were never gated, so **a position is reconstructed, not a verdict on past conduct passed**.
11. **WARNING - this escalates OP-22 and the register was updated to match.** A full back-trace is a **life dossier**. Disclosure is voluntary but the incentive runs toward it, so the system pressures people to assemble exactly the record a surveillance state would want. 5.3's market-public/persons-private principle now has to hold across a lifetime. **OP-22 promoted from a deferred C7 implementation question to a red blocker** in Objections v0.17. Registered, not solved.
12. **5.3a - privacy is a network choice (NEW SECTION).** Author's ruling, and it closes the gap 5.3 left open. 5.3's bank analogy had no bank; **the trust network is the bank**. It does the tallying, so it holds what is private, so it decides the practice. **Aequitas states principles and does not dictate implementation**; inter-network compatibility is negotiated between networks. The working shape is the payment intermediary - the intermediary knows both sides, the counterparties know a token and an outcome - and radical transparency is an equally legitimate setting. **This is the third dial of the same kind as rho and the self-care floor**: Aequitas reads it and never sets it, because a global privacy constant would be the central authority A8 forbids. **Opacity is priced, not forbidden** - a counterparty discounts what it cannot verify (OP-14), so a privacy practice becomes a property of a network's output, the same shape as 5.1c's coverage figure. Three residues flagged in the section: **(a) the network becomes the most information-rich actor in the system** and 3.3a's public-membership screen addresses sector capture, not information capture - P4/OP-10 shaped and unanswered; **(b) privacy has a measured coverage cost** - `residual_unravelling.py` puts the threshold at roughly 40% of a median unit's debit, past which the residual rule stops working, so the privacy/coverage trade-off now has a number; **(c) a network's choice binds members who did not make it** - entry, exit and record portability across a privacy boundary go to C2. **OP-22 accordingly moves red -> orange**: who decides is settled, the minimum disclosure set is not.
13. **5.3b - what a trust network owes, and what "funding" one means (NEW SECTION).** Author's ruling; it advances C2 directly. Three parts. **(i) The tally is an algorithm and the algorithm is published.** This is what makes 3.3's citation requirement enforceable - against a human process "cite your method" is an aspiration, against a published algorithm it is a version number, and `method_ref` (EventLog 4.1a) gets something concrete to point at. A trustworthy network publishes every estimating number, every method, and **anonymised data covering all participants**; disclosure about institutions and businesses is its own call (the 5.3a dial applied to entities). Flagged: publishing more to earn trust also publishes more to **de-anonymise** - a second axis, distinct from 5.3a's verification-cost curve. What the rule buys is a **sharper bound on information capture**: a fully-publishing network's remaining advantage is exactly that **it holds the linkage** between anonymised rows and people. **(ii) "Funding" is not a budget - it is recognition.** There is no treasury and no allocation. Audit work is work; recording is never gated (A7, 6.4a), so the credit was never scarce. **What is scarce is demand (pledges) and verification (6.4a).** This **dissolves OP-24's *funding* half** while leaving its *incentive* half untouched. **(iii) The bootstrap is a genesis entry pointed at the network itself** - founding work admitted after the fact as an estimated record, open to supersession, exactly as 6.2a already handles pre-ledger assets and 5.1d handles pre-ledger positions. **WARNING:** founding credit is the one record written with no counterparty, no rival network and no prior ledger - the single case nothing contemporaneous can check. Bounded by IC-7's wall-clock cap, by public re-computation (OP-14), and by the 24/F ceiling since credit is non-transferable (A3) - **bounded, not closed.** C2 should specify what a founding record must disclose.
14. **7.5 - the disparity ceiling re-scoped, and condition 4 corrected.** The section listed **four** conditions and said condition 4 was handled by IC-7: *"IC-7 caps a day at 24 h."* **IC-7 caps per account per NETWORK.** Multi-network accounts are legitimate (5.3a), goods are anchored physically (one custody chain, IC-5) but **self-care credit is not** - it is credited by proof-of-life and needs no output - so a person on *k* networks accrues the floor *k* times and reaches `k x 24/F`. **A fifth condition is added (cross-network uniqueness attested), the bound is stated as *per network*, and the honest-statement line names all three prerequisites.** The defence is federation: on merge, duplicate records collapse, and a network accepting inflated credit damages its own books. **The same re-scoping is applied to the influence axis in 10 (OP-1)**, which carried the identical unscoped claim. *This is the second over-claim of the same shape found on 2026-08-22, after EventLog 7.1 - a bound proved inside a boundary and stated without the boundary. Both are now corrected in public.*

---

<!-- tag: fnd-v0-16-2026-08-17 -->
### v0.16 (2026-08-17) — empirical calibration folded (median lifestyle, cross-country efficiency, ρ-sweep)

No mechanism or axiom changed. This bump **anchors §3.5 and §7.5 to measured numbers** from a session of societal-scale accounting (`06-simulation/`), and calibrates the ρ prime-rate.

1. **§3.5 — the "scarce factor is not labour" callout gains a measured anchor.** Added: the **labour a median US lifestyle commands ≈ 1,380 h/yr** (`MEDIAN_LIFESTYLE_RESULT.md`; bottom-up from BLS ERM × PCE + EXIOBASE imports + §6.2b durables + own-pollution remediation — measured, not a blanket ratio), ≈ ⅓ of the ~3,650 h/yr self-care credit each human earns → the labour dimension has large slack. Plus **Q6 cross-country efficiency** (`Q6.md`): the US commands **50–80% more embodied labour and 2.5–4× the CO₂ per capita** than Germany/Sweden/France/Japan/Spain for a comparable-or-better standard. Framed as the positive form of A4/A5 — the wasteful method is dearer in the ledger, so the accounting rewards efficiency without a mandate.
2. **§7.5 — the ρ prime-rate bullet is recalibrated, and a new efficiency-crosses-post-scarcity bullet added.** Baseline clears at **ρ\* ≈ 1.2** (median gets ~92% of desired); disaster tightens to ~0.68, growth loosens to ~2.2, pollution to ~1.0 (`rho_sweep.py`, `RHO_SWEEP.md`). New load-bearing finding: **the same society is mildly constrained under the US production method but tips into post-scarcity under German/Spanish efficiency — efficiency, not extra labour, crosses the threshold**, while the `24/F` ceiling holds throughout. Absolute ρ\* is OP-10-illustrative; directions are robust.
3. **Fixed a dangling pointer** in §7.5: `median_lifestyle_RESULTS.md` → `MEDIAN_LIFESTYLE_RESULT.md`.

---

<!-- tag: fnd-v0-15-2026-08-14 -->
### v0.15 (2026-08-14) — disparity-ceiling proof completed + stress-tested (PASSES)

The `24/F` disparity ceiling (§7.5), already simulated (2026-08-10), now has a **formal statement** with a plain-language explainer (`06-simulation/DISPARITY_CEILING.md`) and a **passed adversarial pass**. §7.5 updated:

1. **The ratio-gate precision (new, load-bearing).** Added an explicit statement that credit and debit are **cumulative running tallies (A6)** and **credit is never spent** (a purchase adds to debit, never decrements credit — A3, not a currency), so the gate `D ≤ ρ·C` is a *ratio re-checked per event*, not a drawn-down balance. This is what defeats the **Methuselah** attack (hoard a lifetime of credit, splurge it): a splurge only front-loads one's own `ρ·C`, and equal-age disparity is exactly `24/F` — the only spread beyond it is age. Resolves the objection with no separate "rate gate"; it is just A3 + A6.
2. **Stress-test resolutions folded** — Methuselah (above), dynasty/household (a co-op; dwelling-debit splits per occupant by dwelling-time; the bound is **per-person**, inheritance dilutes it, §6.2b), collector (holdings are a self-bounding burden).
3. **Coupling to v0.14 noted** — making pledged surplus non-consumable (§6.4c) closed the one transfer channel that could have breached A3's non-transferability. The disparity ceiling and the pledge-permanence ruling are one mechanism.
4. **Claim 4 (Methuselah self-test)** added to the sim (now 7 self-tests green); §7.5's simulated-results list gains a hoarding-invariance bullet.

---

<!-- tag: fnd-v0-14-2026-08-14 -->
### v0.14 (2026-08-14) — pledges made permanent; the contingent reserve

Reverses v0.13's revocable-pledge model after a stress-test + simulation (`06-simulation/pledge_reserve.py`, `PLEDGE_RESERVE.md`). Revocability was found too volatile and gameable: a doer who consumed against pledged debit-room could be stranded by a later withdrawal, and the withdrawal threat chilled exactly the hazardous work society most wants financed.

**1. §6.2b / §6.4 / §6.4a — pledges are now PERMANENT and non-revocable.** A person's **lifetime pledging-budget equals their lifetime earned credit, spent down once**; pledging still never diminishes credit itself. The 1:1 cap (IC-8) is now read cumulatively (all pledges ever ≤ all credit ever). Because a pledged hour is a real, unrecoverable sacrifice, the influence guard is re-armed: nobody pledges for free (tightening OP-1), and pledge-farming requires real verified colluders burning their own budgets on a public ledger. "Retractable at any time" is struck throughout; the pledger's discipline is now *at pledge time*, and receivers can *rely* on granted room. Demand risk (a run may go unsold) remains; only *withdrawal* risk is removed.

**2. §6.4c (new) — the contingent reserve.** A task can attract more pledged hours than it costs. The surplus is **not** consumable (that would be profit under A5, and a consumption-concentration channel). It becomes an earmarked, non-spendable **contingent reserve** that activates only against a **verified task-caused future cost** (doer injury/illness, resurfaced remediation, third-party harm). Rules folded in: pledge shares split **pro-rata by hours on the task** (closes the P4 seniority-skim); **causation by physical-trace**, diffuse/latent harm by the §5.1b cohort convention; **overflow reverts to the causer** (§3.2/§3.7) so the reserve is a buffer not a shield (moral-hazard guard); **abandoned-task pledges burn**, and unused reserve lapses — **resolving C5's reversion question in the negative (nothing reverts).** This gives the **hazard half of OP-16** a demand-gated incentive with no wage premium, rate-scaling, or rating authority; the tedium/indignity half stays open.

**3. Cross-references** re-threaded to Objections v0.15 / EventLog v0.7 / Overview v0.11.

---

<!-- tag: fnd-v0-13-2026-08-11 -->
### v0.13 (2026-08-11) — pledge mechanics corrected; presentation cleanup

Author correction. One mechanism clarification (pledges) plus two formatting passes. The correction removes a mis-statement that had stood since v0.5.

**1. §6.2b / §6.4 / §6.4a — a pledge is a revocable grant of debit-room, not a costly debit-absorption.** The prior text (§6.2b step 1) said "a pledge is *costly*: the pledger absorbs a share of the debit against their own debit-room" and drew the creation-cost *down*. That is wrong. A pledge does **not** spend or transfer the pledger's credit, does **not** shrink the asset's debit, and is **not** a promise to buy. It is **virtual credit conferred on the receiver** — it expands the receiving person/cooperative's debit-room so a fixed cost bites less — backed 1:1 by the pledger's own balance, which never moves and is never earmarked. The pledger's only cost is opportunity: committed pledging-power cannot be pledged elsewhere. Consequences folded through:
   - The full creation-cost stays on the asset and is holding-time-split among holders (nothing may vanish, A1); pledges **cushion** the bite rather than reducing the debit. The "100k − 50k = 50k residual" example is reframed accordingly.
   - Pledges are **retractable at any time.** Withdrawal contracts the holders' debit-room and re-exposes the full holding-time share — so a cooperative leans on pledges hardest at start-up and aims to outgrow the dependence, and the pledger's continued approval is what keeps the cushion. "Pledged production assures the run / guarantees a receiver" is downgraded to "softens, not eliminates, demand risk."
   - **Purchase is a separate possession act.** Taking the resulting good loads its property-debit on whoever accepts it, against their own debit-room (§3.2), pledge or no pledge. This dissolves the old fractional-reserve "some pledger can't take the goods" framing; the 1:1 cap now reads as "pledging-power granted ≤ credit backing it."
   - Training/front-loading language ("discharged by whoever pledged") corrected to "carried up front, cushioned by pledger-granted debit-room."

**2. Presentation — inline version-notes stripped.** Decorative "*(new in v0.5)*", "*(amended v0.3)*", "*(reframed v0.9)*"-style tags were removed from section bodies and headers (48 of them); the full change history lives here in §12 and in `99-archive/`, so the notes are redundant clutter. The §10/§12 version references that carry substantive "what changed when" content are kept.

**3. Presentation — table of contents added** at the top (`<!-- tag: fnd-toc -->`), and the header's multi-version "Prior:" recap block removed (it duplicated §12).

*No stress-test required: this corrects an over-claim toward a weaker, axiom-cleaner mechanism (a pledge grants tolerance, it does not move credit or debit), and the formatting passes touch no mechanism. Downstream references (EventLog IC-8 "pledge backing", the wiki pledge page, Objections) still describe the old "absorbs debit" model and want a cascade — parked in NEXT.md.*

<!-- tag: fnd-v0-12-2026-08-10 -->
### v0.12 (2026-08-10) — scenario-suite fold (A1 corollary, §3.5, §7.5)

No mechanism change. Folds one explicit axiom corollary and two societal-scale empirical results from the five-sim scenario suite (`06-simulation/`, plan `scenario_suite_METHOD.md`).

**1. A1 — financial instruments carry no debit (corollary, stated explicitly).** Stocks, bonds, currencies, crypto, options are the "abstract, issued, or fiat quantity" A1 already excludes, so they never appear on a ledger; only the underlying *material* is accounted, on whoever physically holds/operates it (§3.2/§6.2b). Not a loophole — material stays on the operators by holding time, never on the paper. Prompted by the author's clarification during the Q4 build.

**2. §7.5 — the disparity ceiling gains real-distribution backing** (`q4_locked_ledgers.py`). Material-only, the observed inequality tail compresses **~1,000×** (money wealth ~10⁶× median → material consumption ~670×), and only **~0.1–2%** sit past a permanent efficiency-ratio lockout (the ultra-consumers, not the merely rich); ~two-thirds gain room by joining. This is the like-for-like-vs-real-wealth comparison §7.5/§C-test-8 owed, on the consumption axis.

**3. §3.5 — labour is not the scarce factor** (`q1_autarky.py`, `q5_reallocation.py`). Self-care credit (~3.4× productive labour) makes hours abundant; the system binds against *materials and energy*. Autarkic-US ceiling = the energy transition + critical minerals, not labour; the world's essential deficits are covered ~50–100× by reallocating captured/wasted hours. No axiom strain — it sharpens what §3.5 (debit outruns credit) already implies.

*No stress-test required: these are supporting empirical results and an A1-clean corollary, not new mechanisms. The suite sims each carry passing self-tests and cited sources; world figures are indicative.*

<!-- tag: fnd-v0-11-2026-08-10 -->
### v0.11 (2026-08-10) — the disparity ceiling, simulated (§7.5)

No mechanism change. §7.5 gains a **"Now simulated"** note pointing at `06-simulation/disparity_ceiling_sim.py` (agent-based, N = 200,000). Three within-model results: **(1)** the `24/F` ceiling is exact and **ρ-independent** (and weighting-independent — does not depend on OP-10), vs money's 14×–950× on the same population; **(2)** a **ρ clears the market and moves like a prime rate** under shocks (a −30% capacity disaster tightens clearing ρ* from ~1.25 to ~0.82); **(3)** the ceiling is **fraud-invariant** because IC-7 caps every account at 24 h/day. **Still conditional on OP-22** (assumed, not modelled); structural results hold for any distribution, clearing-ρ* values illustrative; real-wealth micro-data comparison still owed (Objections v0.12 §C test 8). Anchored on the median-lifestyle work (`06-simulation/median_lifestyle_RESULTS.md`).

<!-- tag: fnd-v0-10-2026-08-10 -->
### v0.10 (2026-08-10) — electricity attribution (§3.2b): the real-time-dispatch principle

**§3.2b — real-time, demand-dispatched, non-storable production has its emissions follow the end-user; batch/stockpiled production stays with the producer.** This puts electricity **generation** pollution on the **consumer** (the plant is a tool under A1; the draw is the act), aligning it with the section's existing final-delivery-transport and personal-combustion rules — an earlier informal reading had parked it on the generator, the inconsistency now corrected.

**Attribution is by the consumer's contracted supply mix (provenance, §5.1b), not the physical marginal unit** — this resolves the marginal-vs-average question and, decisively, preserves *both* incentives: consumer conservation and generator decarbonisation (a captive-consumer grid-average would have stripped the fuel-choice incentive from the generator). No-choice contexts fall back to the local supply average + §6.4 pledges / §3.3 retroactive cleanup.

**Stress-tested → PASSES WITH CHANGES** (Objections v0.11 B12): the provenance fix replaced a raw "all generation pollution to the consumer." The grid emission factor is a §3.3a cost constant (rival-audited, OP-24). **⚠️ Open universality edge:** real-time-vs-batch is a spectrum (grid storage, on-demand services) — the mid-line criterion is a registered open question, not closed. No axiom conflict — the change is Ellerman-motivated (A1) and keeps every emission internal (A4).

<!-- tag: fnd-v0-9-2026-08-09 -->
### v0.9 (2026-08-09) — legibility fold (debit-taxonomy schematic + named Front-Loading Rule)

Product of the external critique (2026-08-09), whose #1 priority was to make the §3.2 debit taxonomy legible to implementers. **No mechanism changed; this is a presentation fold.**

**1. §3.2 — schematic diagram embedded.** A visual of the taxonomy (`01-wiki/assets/debit-taxonomy.svg`, master page `01-wiki/debit-taxonomy.md`): DEBIT-as-vector → property (embodied-material *dischargeable* vs creation-cost/labour *holding-time-permanent*) and consumption/pollution (*never discharged, stays on the causer*), plus the two cross-cutting rules — self-work identity and non-cascade (§3.2b = §6.2a).

**2. §6.2a — the front-loading principle named and boxed as "The Front-Loading Rule."** The already-stated rule is consolidated into one referenceable box gathering §6.2 (training), §6.2a (the principle + computational closure + pre-Aequitas), §6.2b (the capital-debit waterfall), and objections B3 (dissolves OP-11/OP-5/OP-21) / B8 (closes OP-23). Companion consolidation in the wiki master page.

**3. §0 / §7.5 — the disparity ceiling reframed as conditional** *(critique #9)*. Earlier drafts stated the `24 h ÷ floor` bound as an arithmetic certainty. It is corrected to a **conditional** result: it holds only if (1) the self-care floor stays in a narrow band, (2) floor-shopping is arrested by counterparty re-computation (OP-14), (3) OP-22 is solved so that re-computation is implementable, and (4) no fraud manufactures gross hours (OP-1). The honest headline is now *"if OP-22 is solved and floors stay in-band, then the ceiling is `24 h ÷ floor`, within-model."* Still the strongest defensive result the theory reaches — but the certainty framing is dropped. This unblocks the demoted disparity-ceiling proof, which must be stated conditionally.

**4. Housekeeping.** Stale wiki page `property-debit.md` corrected from the pre-v0.7 "releases entirely on transfer" model to the two-component model.

<!-- tag: fnd-v0-8-2026-08-07 -->
### v0.8 (2026-08-07) — the work-definition session

Product of scoping the disparity-ceiling result, which forced the first explicit statement of *what makes an activity creditable work*. Author interview, then stress-tested (`stress-test` skill: **PASSES** as an instance of OP-10/OP-22, not a new hole). Objections v0.9 B11.

**1. §0/§6 — time, not effort, is the accounting substance** *(stressed)*. Credit measures *time spent* — the finite resource each human holds in exactly equal measure (24 h/day) and cannot hoard, lend, or transfer (A3 (non-fungibility)). Effort/hazard/skill resolve as *material* costs (A2 (time as measure)), never as a time-multiplier. **This dissolves "is sleep really labour?": you spent the time, exertion is irrelevant.**

**2. §6 — the definition of work, stated at last.** Work = time a human spends maintaining or contributing to human life and society, creditable *because it costs the human time*, not because a third party values it. The boundary against §6.5a leisure is necessary-maintenance-vs-discretionary, a per-network weighting choice (§10.1).

**3. §6.1b — self-care is credited work, and it is the §7.5 floor's mechanism** (not a grant — which would have breached A2). Same shape as the subsistence identity (§3.2); a credit stream sized to the cost-of-living debit stream, answering the "debt outruns credit" worry. Verified by proof-of-life (§6.4a), so it covers the newborn/old/sick/disabled — being *alive*, not able to work, is the qualification.

**4. §6.4 / §7.5 — self-care credit generates full pledging-power** (consumption *and* influence = a **universal basic voice**), bounding influence disparity to the same ceiling as consumption. Routing (auto-pledge to basic-needs / unpledged / split) is a trust-network A8 (local governance) lever; **auto-pledging mechanically funds essential provision.**

**5. §6.4a → §6.4b — verification generalises by output type.** Hand-off is only the *goods* case: service → client attestation, enrichment → occurrence-attestation, self-care → proof-of-life. **Enrichment must verify on "did the work occur?", never on feedback** (that re-opens OP-8 (feedback firewall)). Trust networks design/audit each; §6.6 backstops. **Anti-arbitrage guard: counterparty re-computation through its own model (A6/§3) — comparison, never conversion** (conversion = an exchange rate = A3/§7.6 collapse); **depends on OP-22 (audit disclosure).**

**6. §0/§7.5 — the disparity-ceiling engine.** Disparity is bounded because *time is equally distributed and non-transferable*, not because IC-7 (24-hour cap) polices it. Ceiling = **`24 h ÷ the network's self-care floor`** (a small constant, not a fixed one), within-model. §10 updated: OP-1 (service → influence) (universal basic voice), OP-4 (debit tolerance) (denominator of the ceiling; no global ratio), OP-8 (feedback≠verification), OP-10 (weighting governance) (self-care = highest-leverage constant), OP-14 (cohort shopping) (floor/routing shopping), OP-22 (gates the anti-arbitrage guard).

<!-- tag: fnd-v0-7-2026-08-06 -->
### v0.7 (2026-08-06) — credit realization & the supply-chain hand-off model

Product of an adversarial design interview (the C11 (arithmetic audits) session) with the author. Every substantive ruling was stress-tested; all three credit-realization exploits were defused and the residuals route to already-open problems (Objections v0.8 B10).

**1. §6.4 / §6.4a — credit realizes on verification; hand-off is that verification for a good.** *(substantive; near-axiomatic)* The work is always *recorded* (event logged, A7/IC-3 intact), but a credit **realizes** only when the output is verified — *verification, not approval*. For a physical good, each hand-off is verification + debit transfer + a new credit event. This **defuses the monopsony-gatekeeper capture** (a maker is credited at the first hand-off to any receiver; debit-follows-possession inverts a hoarder's leverage) and makes the count **self-auditing** (a receiver eats the debit of exactly what they accept). *Revises the v0.6 "approval never gates credit; always credited for what you materially did" to "recording is ungated; realization gates on verification."*

**2. §6.4 — pledge broadened.** A pledge is a **1:1-backed pre-authorization of creditable work**; it need not involve an object or move any debit (the grass-mowing case). The distinguishing test changes from "does it commit debit?" to "is it 1:1-backed by earned credit?" (IC-8 (pledge backing)). Pledges are deliberately messy and are the job-creating demand lever.

**3. §3.2 — the two-kinds-of-debit taxonomy refined (contradiction fixed).** Property debit has two components: embodied-**material** (transfers with the atoms) and **creation-cost/labour** (holding-time-split, each holder's share permanent, §6.2b). Resolves the v0.5 §3.2-vs-§6.2b contradiction (Bezos keeps his holding-time share after transfer). Adds: transfer to a **non-participant does not discharge**; used goods enter cheap and grow heavier with holding.

**4. §6.2b — deployment timestamp + transit-custodian rule.** Holding-time counts from **deployment** (entry into service). A **transit custodian accrues no creation-cost share** — transit adds only transport-debt; creation-cost holding-time-split starts at deployment, keeping the supply-chain model (§6.4a) from loading the making onto the carrier.

**5. §3.4a — co-product split is data-first.** Measured at the facility, per period, temporally matched (prefer day/batch); each dimension its own measured split; the physics model is fallback + auditor ballpark; finer data supersedes. Operationalises "the process allocates itself" without weakening it.

**6. §6.2a — pre-Aequitas assets expanded.** Recording is a *choice*; when recorded it is an expert *estimate* (estimator credited), at `basis: modelled`; **genesis is a distinct origin-terminus, not a reservoir**; original-construction harm does not transfer to the current holder; an auditor may create the record without consent (A7 (universal accounting)).

**7. §3.7 added — land is not owned; a building carries a remediation debt** (cost to restore its bounded space to natural state), governed by §3.3/§3.3a. Open sub-question: the "natural state" baseline of already-urban space.

**8. §5.3 — the "market-public / persons-private" transparency principle**, stated and made load-bearing (it powers §3.3a audit and §6.4a's public pledge ledger), and shown to *depend on* OP-22.

**9. §7.1 — the exploitative employer is structurally hollowed out** (no wages A3, no surplus A5 (price ≡ cost), no rank-based dumping §6.2b); the residual power is coordination = P4 (coordinator class).

**10. §10 updated** — OP-1 gains the influence-back-door sub-question; OP-22 becomes more load-bearing.

*Not changed:* every axiom A1–A8; the co-product physical-trace rule (only its *data-first ordering* is made explicit); the vector/split-before-collapse rule; the front-loading principle. *Stress-test:* Objections v0.8 B10 + §C tests owed (2b floor sim; OP-1 influence sim).

<!-- tag: fnd-v0-6-2026-08-05 -->
### v0.6 (2026-08-05) — OP-18 closed as the C3 blocker; labour & the cost-not-scarcity rule

**1. §1.1 — the two OP-18 (labour & team credit) rows.** *(substantive)* The "team credit" row is marked **dissolved (A2)**: credit is own hours worked, so no output-decomposition is ever needed to credit a team — the objection conflated credit-for-hours with share-of-output. A new row declares the genuine residue: **labour across co-products rides the process's material split** (the θ of §3.4a), a convention with a measurable basis that adds no new capture surface and changes no one's credit.

**2. §3.4a — labour covered by convention + cost ≠ scarcity.** *(substantive)* Labour has no per-product trace, so by declared convention it rides the material split. And a new consequence: **co-product cost is embodied input, never yield/scarcity** — a pound of tenderloin and a pound of hamburger cost the same, because each embodied the same feed and labour. Scarcity-weighting would ration the prized cut by who can absorb the larger debit (price-rationing, A5), so scarcity is routed to the demand side (pledges/signals) and to decentralised distribution (§7.5), never into cost. *(Method 2, yield-weighting, raised and rejected.)*

**3. §10 — OP-18 moved out of Blocking.** C3 (estimation engine) is unblocked; OP-10 becomes the top blocking problem. Residue (jointly-caused debit across a team) is minor and parked.

*Not changed:* labour is still never rate-scaled; the material split itself is still a measurement (§3.4a), only its *extension to labour* is a convention. *Confirmed by:* `06-simulation/RESULTS.md` (recursion sim), which cleared the materials/energy split this extends. *Resolution note:* `00-strategy/OP-18_labour_and_team_credit.md`.

<!-- tag: fnd-v0-5-2026-08-04 -->
### v0.5 (2026-08-04) — OP-23 resolved; capital and pollution

**1. §6.2a + §6.2b — capital front-loading and the capital-debit waterfall.** *(substantive)* A durable asset holds its own creation-cost as property-debit; community pledges draw it down first (authorization + demand brake); the residual is **holding-time-split** among holders (share = holding-duration ÷ total holding-duration, final at disposal). The decisive justification is **computational closure** — downstream amortization would regress to the first human activity — and the boundary is **capital vs. consumption**, told apart by physical fate. *Closes OP-23 (shared overhead); deletes its §1.1 row rather than filling it. Supersedes this session's interim even-split proposal.*

**2. §3.2b — only property transfers; pollution and transport never do.** *(substantive)* Only embodied-material property-debit rides an item. All pollution-debit and all transport/energy-consumption debit is **permanent on its causer** (the farmer's runoff, the miner's tailings), never transferring downstream. A1/Ellerman-grounded. Provenance records travel (§5.1b) so the consumer signal survives; only the debit is pinned to the causer.

**3. §7.2 rewritten.** The anti-pollution penalty is now **direct on the producer**, not consumer-mediated via a "dearer product" — stronger, because it does not depend on consumers noticing.

**4. §3.3 — stock-dependent re-weighting + the pollution baseline.** A flow is a pollutant only *above the natural-remediation equilibrium*; above it, weight floats with the ambient **stock** (total-remediation interpretation → rises with concentration). Unifies atmospheric CO₂ and solid waste under one rule; makes remediation retroactively lighten every holder's own debit.

**5. §3.6 — end-of-life, recycling, product-as-pollution.** Unwanted assets are consumed by their last holder; a discarded product is itself a stock-weighted pollutant; recycling traces *material* forward but not prior *process-pollution* (which never transferred), so recycled material is cleanly lower-burden. Custody phrasing corrected: no right to accept an object but refuse its debit — **not** a right to force acceptance.

**6. §3.3a, §1.1, §10 updated.** The new stock/baseline constants fall under rival-sector audit (enlarging OP-24's lever). §1.1 gains the holding-time-split convention (measurable basis) and loses the shared-overhead row. **OP-23 closed; OP-25 (illicit dumping) (illicit dumping) opened.**

*Stress-tested twice before adoption (capital front-loading; then the full waterfall) — verdict PASSES WITH CHANGES both times, all changes applied. The even-split residual was broken by the second pass and replaced by the holding-time split.* `00-strategy/OP-23_capital_and_pollution.md`.

<!-- tag: fnd-v0-4-2026-08-01 -->
### v0.4 (2026-08-01) — OP-17 resolved

**1. §3.4a added — joint production allocates itself.** *(substantive)*

> **A joint process's debit divides according to where the process itself physically sent its inputs.** The instrument varies with the process; the justification does not.

The literature searched for a **carrier quantity** — a property of the outputs by which cost could be split — and found only rules that work in one industry and fail in the next. **The allocation is a fact about the process, not a property of the outputs.** Aequitas can say this because A2 gives it a universal *denominator* (hours), so it never has to choose between mass and energy as *the* unit; both reduce to the same thing. Tested against a slaughterhouse, an oil refinery, and a CHP plant with one justification and three instruments.

*Removes:* the co-product row from §1.1 — **deleted, not filled in.** *Spawns:* OP-23, OP-24 (understatement drift). *Moves:* the labour half to OP-18.

**2. §1.1 gains a test, and it is the transferable result.** *Did the thing being divided leave a physical trace?* Trace → measure. No trace → declare a convention. This is what separates OP-17 (joint production) (solved) from OP-18 and OP-23 (genuine conventions), and it should be applied to every future division question.

**3. §3.4 narrowed.** v0.3 claimed allocation is never a resolution problem because the indeterminacy is not epistemic. **Too strong.** Allocation of *physical inputs* is epistemic and does converge. Only division of what was never physically divided is not.

**4. §3.2a added — debit is a vector, and divisions happen per dimension before collapsing.** Divide the collapsed number and the weighting-model maintainer silently controls every allocation in history. Per-dimension division is **weighting-independent**. This closes a side entrance to OP-10 that was invisible until the split rule was written.

**5. §3.3a added — rival-sector audit.** Retroactive re-weighting makes cost constants powerful enough to be worth capturing. A5 closes the classic funding-bias channel (no corporation to pay for a favourable result), but trust networks are consumer-dominated and therefore biased toward **understating** the debit of what their members consume — and nobody funds the correction of an error in their own favour. **The natural auditor of a cost constant is the rival sector.** Plus: two unaffiliated replications before re-weighting history; triage by magnitude × beneficiary concentration; and networks concentrated in the sector they audit are captured by construction.

**6. §5.1b added — the residual rule.** Estimates for unmeasured producers are computed as **(N − Y) / Z** over the *unmeasured residual only*. Over the whole population it creates adverse selection: good producers instrument, bad ones stay dark and free-ride on an average their absence inflates. Extends the discipline §5.1 already applied to cohort debit.

**7. §5.2 clarified, §7.5 strengthened.** The cost of joining without instruments is **administrative labour** — a real material cost under A1 (materialism of cost), not a penalty. And §7.5 is now recognised as **the error-tolerance of the whole accounting**: since debit binds hard and corrections arrive late, the floor is what keeps a mis-estimate from becoming destitution. Watch item added: fixed onboarding costs consolidate industries.

**8. §4, §7.1, §9, §10, §11 updated for consistency** — instrument selection is a ladder question; competition-on-efficiency is load-bearing for §3.3a; the academic paper gains a Sraffa/ISO reply; the MVP's product-costing is unblocked for materials and energy and gated on OP-18 for labour.

<!-- tag: fnd-v0-3-2026-08-01 -->
### v0.3 (2026-08-01)

**1. A2 amended — training is front-loaded, not charged downstream.** *(substantive)*

> **Old (v0.1–v0.2):** *"Skilled labor → the training (time + materials of schooling) is a real cost that flows downstream into the debit of the service recipient."*
> **New:** training is credited work in its own right, and its cost is discharged during the training years by those who pledged for it. Nothing flows downstream.

Reasons, in descending force:

- **The old rule answered a pricing question and left the incentive question open.** It made the doctor's service expensive; it never made becoming a doctor rational. In a system that deliberately removes material gain as a motive, that gap is fatal — and it is precisely the gap that 45 years of time banking evidence says causes chronic skill shortage.
- **The benefit of education is diffuse, so its cost should be.** Assigning it to one patient decades later is arbitrary. That arbitrariness *was* OP-11 (training amortization): every candidate amortization window had a defect, because the question was malformed.
- **Pledging supplies the limiting mechanism the old rule lacked.**

*Not changed:* labour is still never rate-scaled; hard and hazardous labour still resolve materially.
*Dissolves:* **OP-11**, and most of OP-5 (education cost). *Improves:* the skill half of **OP-16 (onerousness gap)**.

**2. §6 restructured — one credit, three feedback channels.** Production / service / enrichment are not credit types. Non-convertibility holds *because feedback was never credit*, requiring no firewall. **OP-8 reframed.**

**3. §0 and A1 reframed — a theory of cost, not of value.** **4. A1 grounded in Ellerman's responsibility imputation.** **5. §6.4 added — pledges and signals.** **6. §3.5 added — the books never balance.** **7. §1.1 added — named conventions.** **8. §3.4 split.** **9. §7.6 added.** **10. §11 hardened.** **11. §2** gains the fourth screening question.

**12. §6.2a added — the front-loading principle, generalized.** Closes OP-21 (media reproduction) and confirms the shape of the OP-11 dissolution. **13. OP-20 (unobservable work) closed (§6.6).** **14. OP-22 narrowed sharply.** **15. §6.5a added — not all work is capturable.**

<!-- tag: fnd-v0-2-2026-07-31 -->
### v0.2 (2026-07-31) — A7 amended

Symmetric estimation of credit and debit for every human, with realization gated on a verified account and observed supersession; credit issuable retroactively. Decisive reason: the original A7 was inconsistent with C1's origin closure — a non-participant's wheat had no creditable grower, so the books described material appearing from nowhere, contradicting A1. Full argument retained in `99-archive/Aequitas_Foundations_v0.2.md` §12.
