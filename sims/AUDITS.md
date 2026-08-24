# C11 — Arithmetic Audits (IC-1 … IC-12)

Companion write-up for [`arithmetic_audits.py`](arithmetic_audits.py).
Tracks **EventLog v0.7** ([`Aequitas_EventLog_v0.8.md`](../docs/Aequitas_EventLog_v0.8.md)) and **Foundations v0.16** ([`Aequitas_Foundations_v0.19.md`](../docs/Aequitas_Foundations_v0.19.md)).

---

## What it is

The EventLog spec defines **twelve integrity constraints** (IC-1 … IC-12) that must hold over any Aequitas event log. This module makes all twelve *runnable*: it builds one small, hand-verifiable synthetic log, runs each IC as pure computation, and — for each IC — injects a **deliberate single-point violation** to prove the check actually fires.

The headline property (EventLog §7.1): **IC-1 … IC-9 need no trust model, no reputation, no authority — only the ability to recompute.** An unrecorded emission is not an enforcement problem; it is an arithmetic error the log itself reports.

```bash
python arithmetic_audits.py            # build log, run all checks, print the report
python arithmetic_audits.py --test     # self-tests only (pytest-free)
```

**The verdict now declares its own extent (EventLog v0.8 §7.4).** `print_extent_block()` prints `(result, domain, extent, closure-basis)` beside the pass/fail lines, and for this scenario the closure basis is **NONE** — no reservoir reconciliation, no external counterparty, no independent total *N*, and two origin termini (`G1`, `G2`) that the log cannot re-derive from its own bytes. Five blind spots are named explicitly, the first being that a process recorded **nowhere** is invisible to every check here. **This was added because OP-26 punished exactly the claim this module used to make**: a bare `12/12` reads as completeness when it only ever meant consistency. Read the verdict as *12/12 over that extent, with no closure basis.*

**Status: 12/12 clean checks pass, 12/12 injected violations caught**, plus the two v0.4 projection properties demonstrated. Reuses (does **not** rebuild) the recursion sim's proven forward solver for IC-10's recursive layer.

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
- **Joint production is in the sandwich.** Milling (grain → flour + bran) is the co-product case (EventLog §10.4). Its **mass** split (7:3) is read from the event's own outputs; its **energy** split (0.62:0.38) comes from the process-energetics model — *not* the mass ratio, because milling energy goes into size-reduction, not sieving.
- **No event carries a split fraction.** There is no field for one (§9); the split is computed at projection time (§7.1a).

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

**Log-side (IC-1…IC-9)** is pure arithmetic on records. **Projection-side (IC-10…IC-12)** is still pure arithmetic and still needs no trust model, but is computed against a weighting/process-energetics model — the first constraints in the spec that check a *projection*. IC-10's recursive layer (every input's own debit is itself a joint split) is the [recursion sim](recursion_convergence.py) result re-run on the scenario economy: `ρ(Ã) = 0.98 < 1`, `min(p) ≥ 0`.

---

## What the v0.4 rework changed

This module was first built in the C11 session, then fell **behind the theory** when the credit-realization interview bumped the four core docs. The rework re-aligned it:

1. **Data-first co-product split (§7.1a).** The split (`theta`) is no longer a stored field on the event. It is computed at projection time: **from the event's own measured output masses** where the dimension is metered, falling back to the published process-energetics model only for a dimension the event did not measure (here, energy). Because there is **no field for a split fraction (§9)**, a self-serving split has nowhere to live — so the projection-side violations (IC-10, IC-11) now live in the **energetics model**, the only place a chosen number exists.

2. **Genesis is a distinct origin-terminus, not a reservoir (§2.2, IC-3).** The two pre-Aequitas assets (tool, spare part) enter by a **genesis entry** — no reservoir input, no parcel ancestry — with the *estimator* credited for the estimation work. IC-1/IC-2 exempt genesis (it admits pre-existing mass); IC-3 accepts a genesis root as legitimate but distinct from a reservoir extraction.

3. **A pledge is a permanent, non-revocable grant of debit-room, drawn 1:1 from the pledger's finite lifetime budget — not a promise to buy (§5.1, IC-9; Foundations v0.14).** It moves no debit by itself and cannot be withdrawn; an undischarged pledge that reaches expiry **burns** (its budget is lost, never returned). The scenario carries all cases: an **object-backed** pledge (the tool repair yields a held object, whose debit follows possession under IC-5 to whoever accepts it — here the pledger, but **not required** to be), a **public-good** pledge (mowing a verge — no held object, no property-debit moves), an **outstanding** (undischarged) pledge, and a **burned** pledge (reached expiry unspent — its budget is gone but, being a *permanent* spend, it **still counts** against IC-8). **IC-8 is cumulative**: the sum of *all* an account's pledges (discharged, outstanding, burned) may not exceed its *lifetime* earned credit. **IC-9 catches** a pledge discharged by an event occurring *after* it expired — it had already burned, so it cannot discharge.

4. **Entity-record continuity, not a within-event id match (Q1).** Parcels are persistent records with a lifecycle; "survival" through an event is the record continuing (a transfer, or a debit-increasing repair keeps the same record), not a coincidence of the same id on both sides.

5. **IC-4 fixed and made non-vacuous.** Fate closure is only as good as the reservoir registry (§13 item 4). Releasing to an **unregistered** reservoir now reads as `unaccounted`. The old test — *deleting* the bran-disposal event — was conceptually wrong: that merely leaves the bran legitimately **held**, a valid fate. The genuine violation is a release to an un-named endpoint.

### Two new projection properties (demonstrated, not pass/fail ICs)

- **Credit realization (§7.3).** Credit is always *recorded* (A7/IC-3 — unpledged wheat still has a grower), but it *realizes* only on **verification of the output**; for a physical good the verifying event is the **hand-off** (a receiver accepting custody attests the goods exist). Every producer in the clean chain realizes — each output is handed off or accepted by a distinct party. A maker who keeps their output with no hand-off is `UNREALIZED` (their credit simply is not counting yet — no rule is broken).
- **Creation-cost holding-time (§2.2, Foundations §6.2b).** The clock starts at the **deployment marker**, so the genesis→deployment gap accrues no share, and a pre-deployment **transit custodian accrues nothing** — a carrier who held 1,000 toasters for two days did not make them.

---

## Why this matters / what it feeds

- It turns the spec's strongest technical claim — *"externalities have nowhere to hide because the log is physical and admits conservation checks"* — from prose into a program that **fails loudly** on each class of tampering.
- It is cheap and trust-model-free: no social graph, no reputation, no authority.
- It is the synthetic half of **C2** (material-superiority demonstration) and a second independent exercise of the recursion sim's solver.

**Open / honest limits.** Numbers are illustrative but internally exact. The economy is a toy; the energetics model is a placeholder standing in for the real process-energetics registry (EventLog §13 item 10, where OP-24 lives). The `collapse`-to-scalar weighting model — OP-10, the top blocker — is deliberately *not* exercised here: every split is per-dimension, before any collapse (§3.1).
