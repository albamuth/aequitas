# Statera — the Aequitas simulation kernel

> **Version:** 0.2 · **Date:** 2026-08-23 · **Tracks Foundations v0.22.**
> **Status: live. This is the current work** — the kernel every future scenario runs on.
> **Results:** [`RESULTS.md`](RESULTS.md) — the headline numbers, so you need not re-run.
> **Change history:** [`CHANGELOG.md`](CHANGELOG.md), which carries a plain-language account of what the kernel can and cannot do.
> **Design and build order:** [`STATERA_PLAN_v0.2.md`](STATERA_PLAN_v0.2.md) · **Reference paper:** [`STATERA_WHITEPAPER_v0.1.md`](STATERA_WHITEPAPER_v0.1.md)
> **Also here:** [`LAB_DESIGN_v0.1.md`](LAB_DESIGN_v0.1.md) (the shippable front end, awaiting sign-off) · [`SUBSECTOR_CANDIDATES_v0.1.md`](SUBSECTOR_CANDIDATES_v0.1.md) (every consumption split considered, with its magnitude).
>
> **Next step: step 5 of the plan — consumer types from real data.** Blocked on a download: the Bureau of Labor Statistics Consumer Expenditure demographic tables are not in [`../data/`](../data/), only the single US average.

**The name.** A *statera* is the balance-scale the goddess Aequitas is shown holding on Roman coinage. **It is an instrument** — a thing you measure a theory with, never the theory itself (Foundations §1.2, the scope section).

| File | Lines | Tests | Run it |
|---|---|---|---|
| [`statera.py`](statera.py) — the kernel | 1,176 | **25** | `python statera.py --test` |
| [`chains.py`](chains.py) — the five exemplar chains | 698 | **14** | `python chains.py --test` |
| [`run_scenario.py`](run_scenario.py) — the human front door | 251 | — | `python run_scenario.py scenarios/baseline.toml` |

---

## What the whole programme is for

> **Find the thresholds, conditions and variables that lead to Aequitas being adopted — how fast, how slow, or where it fails critically.**

**The conformance checks and the disparity bound are instrument checks.** They prove the machine measures what it claims. **They are not the object of study.** A run that shows the bound holding for the twelfth time teaches nothing new; a run that finds a population Aequitas cannot carry teaches a great deal.

**What it is not:** a trust-network database, or a first version of Aequitas.

---

## The two reproduction targets — both still exact

**The rule against building a framework nobody uses: the kernel must re-derive published results before a single new scenario runs.** Both are driven through Statera's own event log and gate, not through the closed-form arithmetic the original scripts use. **Same inputs, different machinery, same number.**

| | Statera | published |
|---|---|---|
| disparity **at `F` = 10 h**, flat across ρ ∈ [1,3] | **2.4000** (spread 8.88 × 10⁻¹⁶) | 2.40× |
| ρ\* | **1.20** | 1.20 |
| median gets | **0.92×** | 0.92× |
| constrained | **35%** | 35% |

**These survived three refactors** — the headcount column, the time axis, and adding metabolic CO₂ to every living person. **A change that moved them would be a bug, not a finding.**

---

## What Statera can do

| | |
|---|---|
| **An append-only event log** | Only ever added to. No delete, no truncate, no edit (§5.4) |
| **A ledger derived on demand** | Never stored. A segment sum over the actor column. **200,000 agents and 600,000 events derive in about 10 ms** |
| **Cohorts with headcounts** | One row speaks for many identical people. **At a headcount of 1 it is the v0.1 kernel exactly** — one code path, two settings |
| **A time axis** | Periods of any length. Credit accrues, the gate is re-checked, every invariant is asserted **every period** |
| **Ages, births and deaths** | Born, aged, dead on a schedule. **Records persist after death** (§5.4) |
| **The debit vector** | Hours, kilograms, megajoules kept apart and collapsed only on demand (§3.2a) |
| **The ratio gate** | `D ≤ ρ·C`, re-checked at every event, with ρ and the room recorded on the event |
| **Essentials never gated** | §7.5. Verified behaviourally at ρ = 0.01 |
| **Shelf life** | Goods carry an expiry. Past it, custody cannot be handed on |
| **Waste disposal as a service** | The material stays with whoever let it become waste; the processor is credited for the work |
| **Five exemplar supply chains** | Housing, transport, food, healthcare, entertainment |
| **8 conformance checks** | A failure raises and **stops the run at the offending event** |

---

## The results

### 1. The disparity bound holds, and it does not drift

Ten periods, unbounded appetite, three floors:

| floor `F` | bound `24/F` | observed | drift over 10 periods |
|---|---|---|---|
| 4 h | 6.00× | 5.75× | **8.9 × 10⁻¹⁶** |
| 10 h | 2.40× | **2.4000×** | **0** |
| 14 h | 1.71× | 1.7143× | **0** |

> **Credit accumulates every period and the top-to-bottom ratio stays put to floating-point precision.** Only a time axis could test that.

### 2. Age is the only spread beyond the bound — now checked, not asserted

**§7.5 has always claimed it.** A 60-year maximum worker against a 20-year subsistence person:

```
525,600 h  ÷  73,000 h  =  7.20×  =  3 (the age ratio) × 2.40 (the rate bound)
```

**Exact.** `python run_scenario.py scenarios/generational.toml`

### 3. A low floor raises the bound, and the population does not fill it

**⚠️ Corrected 2026-08-23. The earlier write-up quoted a single sample size as though it were the result.** It is not. Here is the same seed at four sample sizes:

| floor `F` | bound | N = 20,000 | N = 50,000 | N = 200,000 | N = 500,000 |
|---|---|---|---|---|---|
| 2 h | **12.00×** | 10.49× | 10.76× | 10.22× | 10.63× |
| 4 h | **6.00×** | 5.75× | 5.88× | 5.61× | 5.81× |
| 6 h | **4.00×** | 4.00× | 4.00× | 4.00× | 4.00× |
| 10 h | **2.40×** | 2.40× | 2.40× | 2.40× | 2.40× |

**Three things to read off it, and only two of them are results.**

1. **The bound never moves.** Exact at every floor and every sample size. **This is the claim.**
2. **From `F` = 6 h upward the population fills the bound exactly, at every N.** A 24-hour worker is only 18 hours above a 6-hour floor and the population reaches it.
3. **Below `F` = 6 h the observed spread falls short — and it wanders.** It is **not monotone in N**, because each sample size draws an entirely different random stream and the maximum of a truncated normal is itself a random variable.

> **So the finding is qualitative and robust: below about a 6-hour floor, human endurance binds before the accounting does.** Reaching a 12× spread needs somebody working a 22-hour day.
>
> **The specific figure is not robust and must never be quoted without its N.** *"The most anyone manages is 21.5 h/day"* was one draw at N = 50,000. **This is the third time this project has stated a bound proved inside a boundary without the boundary.**

### 4. The Front-Loading Rule, run rather than asserted

| | actual | if it were amortised |
|---|---|---|
| 1,000 patient visits, doctor trained for 10,000 h | **500 h** | 10,500 h — **21× dearer** |
| 1,000,000 showings of a film costing 500,000 h | **0.0020 h** | 0.5020 h — **251× dearer** |

**Neither cost vanished.** Both sit on the ledger where they were incurred, cushioned by pledges, **never divided by a number of patients or viewers — because that number is always arbitrary.**

### 5. Breathing is recorded and weighs nothing

**A1 reaches "down to the oxygen a human inhales and the CO₂ they exhale."** Statera records ~1 kg per person per day. **§3.3 weighs it at zero**, because respiration is inside the short carbon cycle and therefore at baseline.

```
a year of breathing records 365 kg in the log and costs 0 h
```

> **Both true at once, and that is the clearest case in the kernel for why §3.2a keeps the debit as a vector.** One collapsed number could not hold both facts.

---

## What the conformance layer catches

**Each was tested by deliberately breaking it.**

| Check | Requirement | Caught in test |
|---|---|---|
| **IC-7** | ≤ 24 h per 24 h, **scaled to the period's length** | a 32-hour day; 760 h inside a 30-day period |
| **IC-8** | pledges ≤ lifetime earned credit, 1:1 | 25 h pledged on 12 h earned |
| **IC-1 / IC-2** | mass and energy conserve per process, **weighted by headcount** | a 3 kg leak; a 9.9 kg false leak that only appears unweighted |
| **A3** | credit never transfers, and **a pledge never moves the pledger's credit** | a transfer carrying credit |
| **A6** | ledger derived, never stored | cache disagreeing with the log |
| **§3.2a** | divide per dimension, before collapsing | `divide()` on a collapsed figure |
| **§3.3** | the gate is judged at transaction time; a re-weight changes only the future | an admission exceeding the room that existed |
| **§7.5** | essentials never gated | ρ = 0.01 refuses discretionary, admits essentials |
| **§5.4** | append-only | `EventLog` exposes no delete, truncate, or edit |
| **shelf life** | expired goods cannot be handed on | a log claiming an expired discharge |

**A failure raises `ConformanceError` and stops the run.** Either the scenario is malformed or the theory has a hole — **both are results.** A simulator that cannot fail cannot teach.

---

## Honest limits

- **The economy is still a toy.** One aggregate consumption good with a debit intensity. **The five exemplar chains are built but their numbers are labelled placeholders** — calibration against real physical data is step 5 and is blocked on a download.
- **Every published figure is a labour-hours-only gate.** The default weighting puts mass and energy at 0.0, so all of it is a **floor, never a value** (§5.1a, §9 requirement 13). Every scenario run prints this on its own face.
- **No behaviour layer.** Agents request and are gated. Nobody joins, leaves, pledges strategically, or cheats.
- **No money side**, so §5.5 parallel implementation cannot be tested.
- **12 of the 17 conformance requirements in §9 are expressible.** Up from 10 — requirement 2 (causer attribution) arrived with the chains, and requirement 13 (publish a floor) with the scenario runner. **Still out of reach: 6** (annotate, never delete — needs a contest event), **12** (basis, method, vintage, extent), **14, 15** (residual estimation and the unallocated leftover — both need dark producers), and **16** (published methods, which is a documentation duty rather than a runtime one).
- **Zero spread inside a cohort.** All reported spread is between types and ages, never within one.
- **The absolute numbers inherit their calibration.** ρ\* depends on OP-10 and is illustrative. **What is claimed here is that Statera reproduces them, not that they are settled.**

---

## Next

**Step 5 — consumer types from real demographic data.** Blocked on downloading the BLS Consumer Expenditure demographic tables. *Done when the population's mean want reproduces 1,380 h/yr and the locale dial reproduces the cross-country spread.*

*Tracks Foundations v0.22: A1, A3, A6, A7; §3.2, §3.2a, §3.2b, §3.3, §3.4a, §3.6, §5.1a, §5.4, §6.1b, §6.2, §6.2a, §6.2b, §6.4, §6.4a, §7.5, §9; IC-1, IC-2, IC-3, IC-4, IC-7, IC-8.*
