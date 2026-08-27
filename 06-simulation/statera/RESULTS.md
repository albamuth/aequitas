# Statera — results

> **Read this instead of re-running.** Everything below came out of `python statera.py --test` and `python chains.py --test`. Last verified 2026-08-24.
> Deeper detail: [`README.md`](README.md) (what the kernel does) · [`CHANGELOG.md`](CHANGELOG.md) (how it got here) · [`STATERA_WHITEPAPER_v0.1.md`](STATERA_WHITEPAPER_v0.1.md) (every equation with its derivation).

---

## 1. The two reproduction targets, both exact

Statera has to re-derive results the older scripts already published, through its own event log and gate rather than their closed-form arithmetic. Same inputs, different machinery, same number.

| Quantity | Statera | Published | Source of the published figure |
|---|---|---|---|
| Disparity at a 10-hour floor, flat across ρ from 1 to 3 | **2.4000×** (spread 8.88 × 10⁻¹⁶) | 2.40× | [`disparity_ceiling_sim.py`](../disparity-ceiling/disparity_ceiling_sim.py) |
| Clearing rate ρ\* | **1.20** | 1.20 | [`rho_sweep.py`](../disparity-ceiling/rho_sweep.py) |
| What the median person gets | **0.92×** a full lifestyle | 0.92× | same |
| Share held below their wants | **35%** | 35% | same |

"ρ" (rho) is the consumption gate multiplier: you may consume up to ρ times your own earned credit. "F" is the self-care floor in hours per day.

**A change that moved these four numbers would be a bug, not a finding.** They have survived three rebuilds — the headcount column, the time axis, and putting metabolic carbon dioxide on every living person's ledger.

## 2. The floor is a real dial, and a low floor is not filled

The bound is `24/F`. It is exact at every floor tested:

| Floor `F` | Bound `24/F` | Population actually reaches |
|---|---|---|
| 4 h/day | 6.00× | 6.00× |
| 10 h/day | 2.40× | 2.40× |
| 14 h/day | 1.71× | 1.71× |
| 2 h/day | 12.0× | **10.22×** (top worker 20.4 h/day) |

**Below about a 6-hour floor, human endurance binds before the accounting does.** The bound holds; the population cannot fill it.

> **⚠️ Never quote the low-floor number without its sample size.** At a 2-hour floor, the same seed at four sample sizes gives 10.49× (N = 20,000), 10.76× (N = 50,000), 10.22× (N = 200,000) and 10.63× (N = 500,000). The maximum of a truncated normal is itself a random variable, so the observed spread wanders. The *bound* is exact at every N.

## 3. Age is the only spread beyond the bound

A 60-year worker against a 20-year floor person comes out at **exactly 7.20× = 3 × 24/F**. That is time lived, not class. Foundations §5.5 asserted this; the kernel now checks it.

## 4. The bound does not drift over time

Over ten periods, credit accrues every period and the top-to-bottom ratio stays put. Measured drift: **0.0 to 8.9 × 10⁻¹⁶** — floating-point noise. Only a time axis could test this, and it holds.

## 5. The Front-Loading Rule, run rather than asserted

Training and creation costs sit where they were incurred. They are never divided by a downstream count.

| | Actual | If it were spread over the users |
|---|---|---|
| 1,000 visits from a doctor whose training cost 10,000 h | **500 h** | 10,500 h — **21× dearer** |
| 1,000,000 showings of a film that cost 500,000 h | **0.0020 h** | 0.5020 h — **251× dearer** |

Neither cost vanished. Both are still on the ledger, on the person and period that incurred them.

## 6. Breathing is recorded and weighs nothing

A year of breathing records **365 kg** of carbon dioxide in the log and costs **0 hours**. Both are true at once, because breathing sits inside the short carbon cycle and is therefore at baseline (Foundations §3.3).

This is the clearest demonstration in the kernel of why the debit is kept as a vector: a system storing one collapsed number could not hold both facts.

## 7. What would falsify all of this

- Any of the four numbers in §1 moving without a deliberate model change.
- A run where the top-to-bottom consumption ratio exceeds `24/F` at equal age.
- A conformance check failing on a log the kernel itself produced. There are 8 checks; a failure raises and stops the run at the offending event.
- A population mix the kernel cannot express. **A mix that fails is a result. A sweep that finds no failing mix has not been run hard enough.**

## 8. Honest limits

- **Every Statera figure is a labour-hours-only gate.** The default weighting puts mass and energy at 0.0, so every cost figure is a **floor, never a value**. Each scenario run prints this on its own face.
- **Every number in [`chains.py`](chains.py) is a labelled placeholder.** Calibration against real data is step 5 of the plan and is blocked on a data download (see [`README.md`](README.md)).
- **12 of Foundations' 17 conformance requirements are expressible**, up from 10. Out of reach: 6, 12, 14, 15, 16.

## 9. Figures

Statera writes no figures. The scenario runner prints a text report ending in a COVERAGE line. Figures for the results Statera reproduces live with the original scripts: [`../disparity-ceiling/`](../disparity-ceiling/) and [`../scenario-suite/`](../scenario-suite/).
