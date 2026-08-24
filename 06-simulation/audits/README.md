# Arithmetic audits — the twelve integrity constraints, made runnable

> **Status:** ✅ **Closed and green.** Component C11, finished 2026-08-07, extended 2026-08-22.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Full write-up:** [`AUDITS.md`](AUDITS.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

## What this is

The event-log specification defines **twelve integrity constraints** (IC-1 to IC-12) that must hold over any Aequitas event log. This project makes all twelve *runnable*.

It builds one small synthetic event log you could check by hand — a milling and baking chain, two pre-Aequitas assets entering by genesis, a deployment marker, an object-backed pledge and a public-good pledge — runs each constraint as plain computation, and then **injects a deliberate violation for each one to prove the check actually fires.** A check that never fails is not a check.

## Run it

```bash
python arithmetic_audits.py            # build the log, run all checks, print the report
python arithmetic_audits.py --test     # self-tests only, no report
```

Needs `numpy` and `scipy`. It imports the solver from [`../allocation-engine/recursion_convergence.py`](../allocation-engine/recursion_convergence.py) rather than rebuilding it, and puts that folder on the import path itself.

## What is in here

| Path | What it is |
|---|---|
| [`arithmetic_audits.py`](arithmetic_audits.py) | The audit module. All twelve constraints plus the extent block. |
| [`AUDITS.md`](AUDITS.md) | The companion write-up: what each constraint does and what it cannot see. |
| [`audits_inert/`](audits_inert/) | **The audits as data.** The whole scenario, the worked arithmetic, and every expected verdict as JSON and markdown, so a reader can check the claims **without running any code**. Built 2026-08-24. See its own [`README.md`](audits_inert/README.md). |

## Why `audits_inert/` exists

A critic on the [1f916.ai](https://1f916.ai/) board pointed out that shipping runnable code moves the trust question rather than answering it: to check the claim you must first agree to run a stranger's program. `audits_inert/` answers that. Every number is exported as data, and the arithmetic is written out so it can be redone on paper.

**It is finished work and is not maintained by hand.** Regenerate it with:

```bash
python audits_inert/generate.py          # fixture, worked arithmetic, expected verdicts
python audits_inert/generate_bonus.py    # the disparity-ceiling and unravelling fixtures
```

## What it does not cover

**These checks prove the recorded events consistent with each other. They testify to nothing outside the log.** A process recorded nowhere is invisible to every one of them. That is a *coverage* question, answered elsewhere — see [`../residual-unravelling/`](../residual-unravelling/). The audit report now names its own blind spots on its face, which is what the extent block is for.
