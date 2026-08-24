# Scenario suite — five societal-scale questions

> **Status:** ✅ All five built and green, 2026-08-10. Historical: these are one-off scripts, superseded as *machinery* by the [Statera kernel](../statera/), but their **answers still stand**.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Method and design rules:** [`scenario_suite_METHOD.md`](scenario_suite_METHOD.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

## What this is

Five questions the author asked on 2026-08-10, each answered by its own script with a plain-language companion document.

| Q | Question | Script | Companion |
|---|---|---|---|
| **Q1** | What is the highest egalitarian standard the US could sustain with no imports or exports? | [`q1_autarky.py`](q1_autarky.py) | [`Q1_AUTARKY.md`](Q1_AUTARKY.md) |
| **Q2** | How much labour is captured by ownership or spent on enforcement? | [`q2_capture.py`](q2_capture.py) | [`Q2_CAPTURE.md`](Q2_CAPTURE.md) |
| **Q3** | What is the labour debt of plastic pollution? | [`plastic_debt.py`](plastic_debt.py) | [`PLASTIC.md`](PLASTIC.md) |
| **Q4** | Who is already past a permanent ledger lockout? | [`q4_locked_ledgers.py`](q4_locked_ledgers.py) | [`Q4_LOCKED.md`](Q4_LOCKED.md) |
| **Q5** | What if wasteful labour were shifted to essential work? | [`q5_reallocation.py`](q5_reallocation.py) | [`Q5_REALLOCATION.md`](Q5_REALLOCATION.md) |

**Q6 is not part of this suite** despite the name. It came a week later, from the labour-efficiency track, and lives in [`../median-lifestyle/Q6.md`](../median-lifestyle/Q6.md).

## Run it

```bash
python q1_autarky.py --test
python q2_capture.py --test
python plastic_debt.py --test
python q4_locked_ledgers.py --test     # also writes three figures
python q5_reallocation.py --test
```

Pure `numpy` where anything is needed at all; the Q4 figures need `matplotlib`. No downloaded data.

## The rule that governs every one of them

**Aequitas is a theory of cost, not value, and it has no planner.** "Highest standard of living", "wasteful against essential" and "stolen labour" are value and planning framings that Aequitas does not natively produce.

So each sim is built as one of two legitimate object types and **never as an Aequitas verdict**:

1. **A physical feasibility envelope** — what the materials and the hours permit, with no preference in it.
2. **An exogenous dial the reader can move** — a proposed taxonomy, stated as contestable, with a sensitivity pass over it.

[`scenario_suite_METHOD.md`](scenario_suite_METHOD.md) sets this out in full and is worth reading before quoting any figure from the five.

## Their status now

**The answers stand. The machinery is superseded.** Each of these five scripts re-implements its own agents, its own credit accrual and its own gate, which is why none composes with another. That duplication is the reason the [Statera kernel](../statera/) exists: one engine, and a scenario becomes a configuration file rather than a script.

**Every one of them is single-period.** There is no time axis anywhere in this folder. Anything about how a quantity moves over years has to be re-asked of Statera.
