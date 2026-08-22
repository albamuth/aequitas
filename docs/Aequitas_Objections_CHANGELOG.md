# Aequitas Objections — Change History

> Version-by-version change log for `Aequitas_Objections_vX.Y.md` (the highest-versioned file in `00-strategy/`). Split out of the register so it is read only when tracing **when and why** an objection's status changed. The register's header carries a one-line summary of the current version; Part B holds the answered objections themselves (which are *not* history — see the note there). Superseded full versions live in `99-archive/`.

---
<!-- tag: obj-v0-17-2026-08-22 -->
### v0.17 (2026-08-22) - OP-26 (coverage gap) registered and largely answered

1. **New: OA12 - OP-26, the coverage gap.** The **first objection to Aequitas sourced from outside the project** ([@cairn-lineage](https://1f916.ai/post/1581), c14985, 1f916.ai, against [#1605](https://1f916.ai/post/1605); conceded at c14987). Arithmetic proves the recorded events consistent and testifies to nothing outside the log. Largely answered: the closure witness was already Foundations 5.1b's independently-known total *N*, present since v0.9 and never wired to the audit layer. **Third time an imported problem was already implied by an axiom** - this time the failure was organisational, not theoretical.
2. **Status board: OP-26 added at orange**, and **OP-24 annotated with partial relief** - the audit of *extent* has a funder even though the audit of *weight* does not, conditional on who carries the residual.
3. **Two residues left open on OP-26:** (a) who carries the residual `N - Y` - the OP-24 relief depends on it; (b) the population half routes to **C2** - who does the tallying work, who funds it, and how a competing tally is adjudicated (3.3a's two-replication rule is a bar, not a procedure).
4. **Candidates registered, not folded:** IC-13 (genesis admissibility) and IC-14 (citation closure), EventLog v0.8 12.3.

---

### v0.16 (2026-08-14) — disparity-ceiling proof completed + stress-tested (§C test 8 → PASSES)

Conformed to Foundations v0.15. §C test 8 upgraded from "simulated" to **formally stated + stress-tested → PASSES**:

- **Part 1 (formal statement)** now exists (`06-simulation/DISPARITY_CEILING.md`) with a plain-language explainer.
- **Adversarial pass folded** — the three attacks are dissolved in-line: **Methuselah** (credit is a cumulative record gated as a ratio, never *spent* — A3+A6 — so a splurge only front-loads one's own `ρ·C`; equal-age disparity = `24/F`, only age exceeds it), **dynasty/household** (co-op, per-person bound, inheritance dilutes), **collector** (holdings self-bound).
- **Claim 4 (Methuselah self-test)** added to the sim (now 7 green).
- The **proof itself is marked complete/PASSES**; the only remaining owed item on test 8 is the generous-network cohort-shopping race, which is the **OP-22-conditional** cross-network part.

### v0.15 (2026-08-14) — pledges permanent + the contingent reserve; OP-16 hazard half addressed

Conformed to Foundations v0.14. Register-level changes:

1. **OP-16 (onerousness gap) — hazard half addressed.** Added the contingent reserve (Foundations §6.4c) as candidate (e) and the adopted resolution for hazardous-onerous work: over-pledging pre-funds any verified task-caused harm to the doer, giving a demand-gated incentive with no rate-scaling or rating authority. Status → 🟠 "hazard half addressed; tedium/indignity half open." Live-set row and the §1 valuation row updated. Sim `06-simulation/pledge_reserve.py`.
2. **OP-1 (service → influence) — "self-starving" brake re-armed.** Permanent pledging spends a finite lifetime budget, so pledging is no longer free; the influence-back-door residual (B10) narrows (pumping and pledge-farming now cost real, visible budget) but is not fully closed.
3. **P4 (coordinator class).** Noted that the reserve's pro-rata-**by-task-hours** split deliberately avoids opening a seniority-weighted cover-skim; fixed the stale "a pledge is revocable" aside in the employer-hollowed-out box.
4. **C5 (pledge reversion)** resolved in the negative (unspent pledges burn) — recorded via EventLog v0.7 / Foundations v0.14.

### v0.14 (2026-08-11) — conformed to Foundations v0.13 (pledge mechanics) + presentation cleanup

1. **Pledge model corrected wherever it appears.** A pledge is a *revocable grant of debit-room* (virtual credit, backed 1:1 by the pledger's own balance), not a costly debit-absorption and not a promise to buy. Fixed: **B8** ("drawn down by pledges first" → full cost holding-time-split, pledges cushion the bite), **B3** (front-loading "discharged by pledgers" → carried, cushioned), **B10** (the influence-back-door residual), the **status board** OP-1 row, and **§C test 7**.
2. **The "self-starving" brake is retracted.** The OP-1 influence back-door was said to be partly self-limiting because *pledging costs the pledger debit-room* (old §6.2b). Under Foundations v0.13 it does not, so that brake is gone — the residual now leans only on IC-7 and the wrecked ratio. Noted in B10, the status board, and §C test 7 so the influence sim tests the weaker guard.
3. **Presentation.** Decorative `*(new in vX)*` header tags stripped (§0, OA3, OA10, OA11); a Contents list added; the in-document change log (§E) extracted to this file; the stale `*End of v0.8.*` footer corrected. Tracks pointers re-threaded to Foundations v0.13 / EventLog v0.6.

### v0.13
1. **§C test 8 — consumption-axis real-distribution comparison DONE** (`06-simulation/q4_locked_ledgers.py`, scenario-suite Q4). Material-only (A1 corollary): observed inequality tail compresses ~1,000× (wealth ~10⁶× → consumption ~670×); only ~0.1–2% permanently locked; ~two-thirds gain by joining. No new objection — supporting evidence for the §7.5 ceiling.
2. **Standing suite result recorded:** labour is abundant, materials/energy bind (Q1 autarky, Q5 reallocation) — bears on §3.5.
3. **Tracks pointer → Foundations v0.12; `scenario_suite_METHOD.md` added.** Header cross-refs re-threaded.

### v0.12
1. **§C test 8 (disparity-ceiling proof) moved "owed" → "SIMULATED."** `06-simulation/disparity_ceiling_sim.py` establishes the `24/F` ceiling as exact + ρ-independent + weighting-independent (not OP-10-dependent), a market-clearing ρ that tightens under shocks (prime-rate behaviour), and fraud-invariance (IC-7). Folded into Foundations v0.11 §7.5. Still conditional on OP-22; generous-network race + real-wealth-microdata comparison still owed.
2. **Tracks pointer → Foundations v0.11; DISPARITY_CEILING.md added.**

### v0.11
1. **B12 added — §3.2b electricity attribution / the real-time-dispatch principle, PASSES WITH CHANGES.** Electricity generation pollution → the consumer (non-storable, demand-dispatched; plant = tool, A1), aligning it with final-delivery-transport + personal-combustion. The raw "marginal-unit to consumer" was caught weakening decarbonisation on a pooled grid; **fix: attribute by contracted supply mix (provenance §5.1b)**, preserving both conservation and decarbonisation incentives. Grid emission factor → OP-24 / §3.3a. Universality edge (real-time-vs-batch spectrum) flagged open.
2. **Tracks pointer → Foundations v0.10.**

### v0.10
1. **OP-9 (calculation reply) / P5 (preference revelation) written up and downgraded 🟠→🟢.** The standing statement is the new `00-strategy/OP-9_calculation_reply.md`; the plain-language version folded into Overview v0.6 §9. **OA8 rewritten** as the four-move summary: cost≠value defeats Mises · pledges reveal demand (no board) · tractability cited (Cockshott & Cottrell + recursion sim) · scarcity-as-debit rations without a margin (Kantorovich).
2. **The one residue is honestly labelled, not closed.** Scarcity-as-debit's objective-function edge and Hayek's tacit-knowledge point **both terminate in OP-10 (weighting governance)** and are registered there — OP-9 is "answered for cost," not "closed." No axiom change; no new hole.
3. **Status board: OP-9 moves to answered (🟢).** Sixteen closed/answered, five live headline blockers unchanged (OP-10, OP-24, OP-16, OP-6, OP-1/P4).

### v0.9
1. **B11 added — self-care as credited work & the definition of work, PASSES** (as an instance of OP-10/OP-22, not a new hole). Weighting-pluralism is legitimate (A6/§3); the anti-arbitrage guard is counterparty re-computation — comparison, never conversion — depending on OP-22 (audit disclosure). A global anchor was proposed and **rejected as anti-A8.**
2. **OP-1 (service → influence) gains the universal-basic-voice result** — self-care credit → influence bounds influence disparity to `24h ÷ floor` (a feature); routing is a network lever.
3. **OP-4 (debit tolerance) promoted** — now the denominator of the disparity ceiling and the self-care floor magnitude; no global debit:credit ratio (§3.5/A8); per-person local floor + personal ratio.
4. **OP-22 more load-bearing again** — it now also gates the anti-arbitrage guard.
5. **OP-10 (weighting governance) gains its highest-leverage instance** (self-care = universal + influence-bearing constant); **OP-14 (cohort shopping)** gains floor/routing shopping; **OP-8 (feedback firewall)** sharpened (feedback ≠ verification).
6. **Status board: fifteen closed, six live.** §C gains one test (generous-network race + disparity ceiling).

### v0.8
1. **B10 added — the credit-realization & supply-chain hand-off model, PASSES WITH CHANGES.** Hand-off gates credit *realization* (verification, not approval); every hand-off = verify prior holder + transfer debit + new credit event. All three exploits (wash-trade, monopsony gatekeeper, risk-dumper) defused; the guard for the gatekeeper is debit-follows-possession, discovered mid-pass.
2. **P4 (coordinator class) (OA7 (coordinator class)) weakened further.** The wage-extraction employer is structurally hollowed out (no wages A3 (non-fungibility), no surplus A5 (price ≡ cost), no rank-based dumping §6.2b); mislabeling defused by the public pledge ledger; demand risk symmetric-by-hours and floored. Only the coordination residual survives.
3. **OP-1 (service → influence) gains the influence back-door** — the one surviving residual (gross fake hours → pledging-power) routes here, not to credit accounting.
4. **OP-22 (audit disclosure) (OA9 (audit disclosure)) made more load-bearing** — the market-public/persons-private transparency principle depends on it.
5. **Status board: fourteen closed, six live.** §C gains two tests (demand-risk floor adequacy; influence back-door).

### v0.7
1. **OP-18 (labour & team credit) closed as the C3 (estimation engine) blocker and moved to Part B as B9.** Team-credit dissolves under A2 (time as measure) (own hours); labour-across-co-products rides the material split by declared convention; co-product cost is embodied input, not scarcity (the tenderloin case; Method 2 yield-weighting rejected as price-rationing).
2. **§0 narrowed to near-nothing** — the untraceable residue is no longer a blocker anywhere; only jointly-caused team debit survives, minor. First OP to close by *declaring* a convention rather than removing a division — the physical-trace test mandates one when there is genuinely no trace.
3. **Status board: thirteen closed, six live.** OP-10 (weighting governance) is now the top blocking problem.
4. **§C Test 1 (recursion convergence) resolved** by `06-simulation/recursion_convergence.py` — the sim that cleared the materials/energy split this OP-18 work extends to labour.

### v0.6
1. **OP-23 (shared overhead) closed and moved to Part B as B8.** Capital and overhead accrue to the asset and never allocate to co-products (§6.2b); the interim inherited-proportions convention was deleted, and the overhead-stuffing exploit died with it.
2. **§0 narrowed again** — the indivisible set drops from three items to two (both OP-18 (labour & team credit)). Overhead left by relocation, not by splitting.
3. **OP-25 (illicit dumping) added (OA11 (illicit dumping))** — illicit end-of-life dumping, a Level-2 attribution problem, explicitly minor.
4. **OP-24's lever enlarged (OA3 (understatement drift))** — the new stock-dependence and equilibrium-baseline constants (§3.3) are the largest single levers in the weighting model and sharpen, not solve, the understatement problem.
5. **OA4 (shared overhead) (OP-23) converted to a tombstone** pointing at B8; B3 and the status board updated to record the closure.

### v0.5
1. **OP-17 (joint production) closed and moved to Part B as B7**, with the rejected alternatives recorded so they are not re-proposed.
2. **§0 narrowed** — from *"division, not measurement"* to **"division of the untraceable,"** with the physical-trace test that separates the cases. This is the session's most transferable result.
3. **OP-18 (labour & team credit) promoted to blocking (OA1 (responsibility analysis)).** It inherits C3 (estimation engine) from OP-17: materials and energy now split, labour does not.
4. **OP-24 (understatement drift) added (OA3 (understatement drift))** — understatement drift. **OP-23 (shared overhead) added (OA4 (shared overhead))** — shared overhead.
5. **OA10 (auditor independence) added** — the auditor-independence problem, with the general-membership screening rule as a partial answer and full trust-network design explicitly deferred to C2 (verification / trust networks).
6. **OA2 (weighting governance) (OP-10 (weighting governance)) updated** — a side entrance closed by §3.2a (split before collapse), and a fast proxy recorded: *"does this need an objective function?"* Both rejected allocation rules did.
7. **OA8 (preference revelation) (OP-9 (calculation reply)) sharpened** with the demand-contingency warning from the OP-17 session.
8. **§C created** — tests owed, promoted out of the old "not yet examined" section so they are schedulable work rather than reading.
