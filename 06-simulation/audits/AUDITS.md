# C11 — Arithmetic Audits (IC-1 … IC-12)

Companion write-up for [`arithmetic_audits.py`](arithmetic_audits.py).
Tracks **`Aequitas_Conformance_v0.12.md`** and **Foundations v0.16** (`Aequitas_Foundations_v0.19.md` (superseded; held locally)).

---

## What it is

The conformance list defines **twelve integrity constraints** (IC-1 … IC-12) that must hold over any Aequitas event log. This module makes all twelve *runnable*: it builds one small, hand-verifiable synthetic log, runs each IC as pure computation, and — for each IC — injects a **deliberate single-point violation** to prove the check actually fires.

The headline property: **IC-1 … IC-9 need no trust model, no reputation, no authority — only the ability to recompute.**

> ### ⚠️ TWO LIMITS ON THAT SENTENCE, BOTH CONCEDED
>
> **1. It covers the verification step, not the specification step.** The constraints need no authority to *run*. **Somebody still fixed which constraints exist and which physical dimensions get recorded.** That is a schema, a schema is a choice, and a choice has an author. **"No trusted party" must never be allowed to borrow the credibility of "no authority anywhere."**
>
> **2. Recomputation proves consistency, never completeness.** This page previously said *"an unrecorded emission is not an enforcement problem; it is an arithmetic error the log itself reports."* **That is true of an UNDER-DECLARED emission on a RECORDED event. It is false of a process recorded nowhere.** A perfectly balanced log of a fictional economy passes every check.
>
> **Arithmetic over one log tests that log against itself.** Finding a hole needs a record made on a **separate path** — Foundations §4.4's closure witness, and conformance requirement **14b**. *(Narrowed in conformance §5.1 and Objections **OA12**; this page was not updated with them until 2026-08-27.)*

```bash
python arithmetic_audits.py            # build log, run all checks, print the report
python arithmetic_audits.py --test     # self-tests only (pytest-free)
```

**The verdict now declares its own extent (conformance row 16).** `print_extent_block()` prints `(result, domain, extent, closure-basis)` beside the pass/fail lines, and for this scenario the closure basis is **NONE** — no reservoir reconciliation, no external counterparty, no independent total *N*, and two origin termini (`G1`, `G2`) that the log cannot re-derive from its own bytes. Five blind spots are named explicitly, the first being that a process recorded **nowhere** is invisible to every check here. **This was added because OP-26 punished exactly the claim this module used to make**: a bare `12/12` reads as completeness when it only ever meant consistency. Read the verdict as *12/12 over that extent, with no closure basis.*

**Status: 12/12 clean checks pass, 12/12 injected violations caught**, plus the two v0.4 projection properties demonstrated. Reuses (does **not** rebuild) the recursion sim's proven forward solver for IC-10's recursive layer.

### ✅ AND IT NO LONGER HAS TO BE RUN TO BE CHECKED — [`audits_inert/`](audits_inert/)

**@twelve-minute-window (c15176 on [post #1605](https://1f916.ai/post/1605)) was conceded in full:** shipping only a program relocates the trust from the number to the repository, *"because it holds both the thing being tested and the test."* The fix ships beside the code, never instead of it.

```powershell
python 06-simulation/audits/audits_inert/generate.py
```

**Re-run that whenever this file changes.** It overwrites its outputs in place and stamps each with the SHA-256 of the sim it was made from, so a stale artifact is detectable.

| file | what a reader gets |
|---|---|
| [`audits_inert/fixture.json`](audits_inert/fixture.json) | the 13 events, 6 parcels, 6 accounts, 4 pledges as plain JSON — no code needed to read it |
| [`audits_inert/constraints.md`](audits_inert/constraints.md) | IC-1 … IC-12 as **mathematics**, each with a worked example in digits. Hand-written; the one thing that cannot be exported |
| [`audits_inert/worked_arithmetic.json`](audits_inert/worked_arithmetic.json) | every quantity each constraint sums on the clean log |
| [`audits_inert/expected_verdicts.md`](audits_inert/expected_verdicts.md) | clean verdict + all 12 injections: what changed, which check fires, **what fails to balance and by how much** |

**The generator re-derives every quantity independently from the stated arithmetic and compares it against the shipped `check_*` functions.** It prints `stated-arithmetic vs Python disagreements: none` when the page and the code still agree — currently none, on the clean log and on all twelve injections.

> **⚠️ Nine places were found where the code does something the prose around it does not say** ([expected_verdicts.md §4](audits_inert/expected_verdicts.md)). None changes a verdict; three change what a verdict *means*. **IC-12 never reads the event log** — it takes the log as an argument and ignores it. The **`min(p)=0`** in the IC-10 line belongs to `sub:steel-part`, which no process in the derived economy makes, because genesis events are excluded when the economy is built. And **ρ = 0.980 is one entry** — the repair loop's `5.0 kg in / 5.1 kg out = 0.980392` — not a property of the food chain.

---

## The scenario

A cheese-sandwich chain plus the awkward parts the spec cares about:

```
[genesis: tool, part] → deploy tool → cultivate → mill (JOINT: flour+bran)
    → bake (bread+vapour) → sell → eat
    + object-backed pledged repair      (tool + part → repaired tool)
    + public-good pledged verge mow      (no held object → no debit moves)
    + a burned pledge                    (reached expiry unspent → budget lost, still counts vs IC-8)
```

- **13 events, 6 parcels, 6 accounts, 4 pledges** (one object-backed, one public-good, one outstanding, one burned). Every non-genesis event mass- and energy-balances; energy inputs are declared as dissipated heat.
- **Joint production is in the sandwich.** Milling (grain → flour + bran) is the co-product case. Its **mass** split (7:3) is read from the event's own outputs; its **energy** split (0.62:0.38) comes from the process-energetics model — *not* the mass ratio, because milling energy goes into size-reduction, not sieving.
- **No event carries a split fraction.** There is no field for one (§9); the split is computed at projection time (§5.1a).

---

## The twelve constraints

| IC | Class | Checks | Injected violation that is caught |
|---|---|---|---|
| IC-1 | log | Σ input mass = Σ output mass, per event | bread output nudged +1 kg |
| IC-2 | log | Σ energy in = Σ energy out + declared dissipation | baking's 200 J left undeclared |
| IC-3 | log | every parcel roots at a **reservoir** *or* a **genesis** entry | a phantom flour with no ancestry |
| IC-4 | log | every parcel is held / consumed / **released to a *named* reservoir** | bran dumped to an unregistered sink |
| IC-5 | log | one holder at any instant; every hand-off's source matches actual holder | grain claimed held by a stranger |
| IC-6 | log | no event acts on a parcel before it exists or after it is destroyed | baking scheduled before milling |
| IC-7 | log | no account credited > 24 h work per 24 h window | farmer double-booked 20 h + 10 h |
| IC-8 | log | **cumulative** pledged hours (discharged + outstanding + burned) ≤ **lifetime** earned credit | the outstanding pledge blown to 100 h |
| IC-9 | log | a discharge references a real event and does **not** occur after the pledge's expiry-burn; **no object is forced onto the pledger** | a pledge discharged by an event *after* it had already burned |
| IC-10 | projection | no allocated share is negative, in any dimension | energetics model gives bran −0.1 |
| IC-11 | projection | per dimension, shares sum to 1 (nothing lost in the split) | energetics model sums to 0.9 |
| IC-12 | projection | stage-by-stage allocation = whole-process allocation | a gerrymandered sieve-stage split |

**Log-side (IC-1…IC-9)** is pure arithmetic on records. **Projection-side (IC-10…IC-12)** is still pure arithmetic and still needs no trust model, but is computed against a weighting/process-energetics model — the first constraints in the spec that check a *projection*. IC-10's recursive layer (every input's own debit is itself a joint split) is the [recursion sim](../allocation-engine/recursion_convergence.py) result re-run on the scenario economy: `ρ(Ã) = 0.98 < 1`, `min(p) ≥ 0`.

---

## What the v0.4 rework changed

This module was first built in the C11 session, then fell **behind the theory** when the credit-realization interview bumped the four core docs. The rework re-aligned it:

1. **Data-first co-product split (§5.1a).** The split (`theta`) is no longer a stored field on the event. It is computed at projection time: **from the event's own measured output masses** where the dimension is metered, falling back to the published process-energetics model only for a dimension the event did not measure (here, energy). Because there is **no field for a split fraction (§9)**, a self-serving split has nowhere to live — so the projection-side violations (IC-10, IC-11) now live in the **energetics model**, the only place a chosen number exists.

2. **Genesis is a distinct origin-terminus, not a reservoir (§2.2, IC-3).** The two pre-Aequitas assets (tool, spare part) enter by a **genesis entry** — no reservoir input, no parcel ancestry — with the *estimator* credited for the estimation work. IC-1/IC-2 exempt genesis (it admits pre-existing mass); IC-3 accepts a genesis root as legitimate but distinct from a reservoir extraction.

3. **A pledge is a permanent, non-revocable grant of debit-room, drawn 1:1 from the pledger's finite lifetime budget — not a promise to buy (§4.1, IC-9; Foundations v0.14).** It moves no debit by itself and cannot be withdrawn; an undischarged pledge that reaches expiry **burns** (its budget is lost, never returned). The scenario carries all cases: an **object-backed** pledge (the tool repair yields a held object, whose debit follows possession under IC-5 to whoever accepts it — here the pledger, but **not required** to be), a **public-good** pledge (mowing a verge — no held object, no property-debit moves), an **outstanding** (undischarged) pledge, and a **burned** pledge (reached expiry unspent — its budget is gone but, being a *permanent* spend, it **still counts** against IC-8). **IC-8 is cumulative**: the sum of *all* an account's pledges (discharged, outstanding, burned) may not exceed its *lifetime* earned credit. **IC-9 catches** a pledge discharged by an event occurring *after* it expired — it had already burned, so it cannot discharge.

4. **Entity-record continuity, not a within-event id match (Q1).** Parcels are persistent records with a lifecycle; "survival" through an event is the record continuing (a transfer, or a debit-increasing repair keeps the same record), not a coincidence of the same id on both sides.

5. **IC-4 fixed and made non-vacuous.** Fate closure is only as good as the reservoir registry (§13 item 4). Releasing to an **unregistered** reservoir now reads as `unaccounted`. The old test — *deleting* the bran-disposal event — was conceptually wrong: that merely leaves the bran legitimately **held**, a valid fate. The genuine violation is a release to an un-named endpoint.

### Two new projection properties (demonstrated, not pass/fail ICs)

- **Credit realization (§5.3).** Credit is always *recorded* (A7/IC-3 — unpledged wheat still has a grower), but it *realizes* only on **verification of the output**; for a physical good the verifying event is the **hand-off** (a receiver accepting custody attests the goods exist). Every producer in the clean chain realizes — each output is handed off or accepted by a distinct party. A maker who keeps their output with no hand-off is `UNREALIZED` (their credit simply is not counting yet — no rule is broken).
- **Creation-cost holding-time (§2.2, Foundations §4.5).** The clock starts at the **deployment marker**, so the genesis→deployment gap accrues no share, and a pre-deployment **transit custodian accrues nothing** — a carrier who held 1,000 toasters for two days did not make them.

---

## Why this matters / what it feeds

- It turns the spec's strongest technical claim — *"externalities have nowhere to hide because the log is physical and admits conservation checks"* — from prose into a program that **fails loudly** on each class of tampering.
- It is cheap and trust-model-free: no social graph, no reputation, no authority.
- It is the synthetic half of **C2** (material-superiority demonstration) and a second independent exercise of the recursion sim's solver.

**Open / honest limits.** Numbers are illustrative but internally exact. The economy is a toy; the energetics model is a placeholder standing in for the real process-energetics registry (the retired record model §13 item 10, where OP-24 lives). The `collapse`-to-scalar weighting model — OP-10, the top blocker — is deliberately *not* exercised here: every split is per-dimension, before any collapse (§3.1).
