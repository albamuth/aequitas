# Pledge reserve — why anyone would take the nasty job

> **Status:** ✅ Built and green, 5 self-tests. Answers the **hazard half** of OP-16 (the onerousness gap). The tedium half is still open.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Full write-up:** [`PLEDGE_RESERVE.md`](PLEDGE_RESERVE.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

## The question

Somebody has to clean the toxic site. A market pays a wage premium for nasty work. Aequitas has no wage and no profit — price equals cost, and an hour is an hour whoever works it. So either onerous work goes chronically understaffed, which is what 45 years of time banking found, or there is an incentive that does not break an axiom.

## The mechanism being tested

A **pledge** is a permanent, non-revocable grant of debit-room. Pledges on a task first cushion that task's labour and material cost, shared out by hours worked **on the task** — not by whole-career seniority, which would be a different problem.

Any **surplus is not consumable.** Banking it as spendable room would re-create a channel for accumulating consumption advantage. Instead the surplus becomes a **contingent reserve**: earmarked, non-spendable room that activates only against a verified future cost traceable to that task — the worker's injury, the site needing remediation again, harm to a third party.

Two guards are built in and both are tested:

- **G1, overflow reverts to the causer.** The reserve is a buffer, not a shield. When it is exhausted, the remaining task-caused debit falls back on the doer. Without G1 the reserve licenses carelessness.
- **G2, causation by physical trace.** A claim draws on the reserve only if the harm left a trace linking it to the task. Diffuse harm with no individual trace is handled by a stated convention, never by an open claim.

## Run it

```bash
python pledge_reserve.py            # the model, the report, and two figures
python pledge_reserve.py --test     # self-tests only
```

Needs `numpy`; the figures need `matplotlib`.

## What is in here

| Path | What it is |
|---|---|
| [`pledge_reserve.py`](pledge_reserve.py) | The model. Two claims plus a fraud dial. |
| [`PLEDGE_RESERVE.md`](PLEDGE_RESERVE.md) | The write-up: the question, the ruling, the guards, the result. |
| `pr_fig1_clearing.png` | Supply against reserve coverage — where the job clears. |
| `pr_fig2_care.png` | Care taken, shield against buffer. |

## The open piece

**The causation claim is not settled.** Deciding whether *this* task caused *that* harm has no clean analogue in the rest of the system, and it routes to ordinary recourse rather than to an Aequitas mechanism. It is registered as a residue on Foundations §4.6, not closed.
