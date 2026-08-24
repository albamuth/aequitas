# Arithmetic audits — results

> **Read this instead of re-running.** From `python arithmetic_audits.py --test`, last verified 2026-08-24.
> Full detail: [`AUDITS.md`](AUDITS.md). Every number as data: [`audits_inert/`](audits_inert/).

---

## The headline

> **All twelve integrity constraints pass on the clean log, and all twelve injected violations are caught.** The realisation and holding-time properties hold. The verdict declares its own extent.

Concretely: 13 events, 12 checks, 12 deliberate single-point violations, 12 catches.

## What each class of check buys

| Checks | Class | What they need |
|---|---|---|
| **IC-1 to IC-9** | Log-side | Nothing but the ability to recompute. No trust model, no reputation, no authority, no outside data. |
| **IC-10 to IC-12** | Projection-side | Still plain arithmetic, but computed against a published process-energetics model. |

**The property worth keeping:** for IC-1 to IC-9, an under-declared emission on a recorded event stops being an enforcement problem and becomes an arithmetic error that the log itself reports.

IC-10 (non-negative allocation) reuses the solver from [`../allocation-engine/`](../allocation-engine/), which already derived non-negativity across 4,098 economies. This project inherits that rather than re-asserting it. IC-12 (boundary additivity) is demonstrated here for the first time.

## The extent block — what a passing check could *not* see

Added 2026-08-22. The report now prints, on its own face:

- **Closure basis: NONE on every axis.** Nothing here is checked against an independently measured physical total.
- **Two origin termini** (`G1`, `G2`) declared un-re-derivable.
- **Five blind spots named**, the first being that **a process recorded nowhere is invisible to every check in this file.**

This exists because a critic was right: arithmetic over a log proves the recorded events consistent and testifies to nothing outside it. The headline claim now travels with that caveat attached.

## What would falsify this

- Any of the twelve checks passing on a log carrying its matching injected violation. That would mean the check is vacuous.
- Any of the twelve failing on the clean log. That would mean the fixture or the constraint is wrong.
- A violation class that the fixture cannot express. That is the interesting failure, and it is what `audits_inert/`'s published fixture invites a stranger to find.

## Figures

None. This project produces text and data, not plots. The data is in [`audits_inert/`](audits_inert/): `fixture.json`, `worked_arithmetic.json`, `expected_verdicts.json`, and their markdown companions.
