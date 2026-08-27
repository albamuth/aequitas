<!-- tag: simroadmap-v0-2 -->
# Aequitas — Simulation Roadmap

> **Version:** 0.2
> **Date:** 2026-08-23
> **Status:** Author ruling, 2026-08-23.
> **Supersedes:** `99-archive/Aequitas_Simulation_Roadmap_v0.1.md`. v0.1 read the author's eight examples as a list of eight deliverables and proposed a build order through them. **That was the wrong shape.** The author's correction: *"the goal would be simulators that could test any of those conditions, and thousands more."* **The deliverable is a configurable engine; a scenario is a configuration, not a script.** This version is rebuilt around that: what the engine must be able to express, how it decomposes, what the existing scripts become, and the discipline that stops it turning into a framework nobody uses.
> **Companions:** `Aequitas_Foundations_v0.25.md` §1.2/§9 (scope, conformance list), `Aequitas_Strategy_v0.6.md` §2, `06-simulation/scenario-suite/scenario_suite_METHOD.md`.

---

## 0. The ruling

> **Aequitas the system is the deliverable. Code is how it gets tested.**
>
> **The code to build is a simulator of an economy — not a trust-network database, and not a set of one-off scripts.** It must be able to test any starting condition anyone thinks of, including thousands nobody has thought of yet.

**A simulator is in scope for the same reason a schema is not.** Apply §1.2's dial test — *if a principle survives at both ends of a dial, the dial is not part of the principle*. A simulation is not a dial. **It is the instrument that tells you whether a principle survives one.**

**The eight scenarios the author named are examples, not a backlog.** They are useful as a *coverage test on the engine's design*: if the engine can express all eight without special-casing any of them, it can probably express the ones nobody has named. **If it needs an exception for one, the design is wrong** — the same universality test applied to a mechanism (§2 of Foundations).

---

## 1. What the engine must be able to express

Grouped by what varies. **Everything here is a knob or a plug, never a fork in the code.**

### 1a. The Aequitas rules — fixed, never configurable

These are the system. They are the same in every scenario, and a scenario that needs one turned off has found either a bug or a hole in the theory.

- Credit accrues as **time spent**, never rate-scaled (A2). Self-care floor plus productive hours, capped at 24 h/day (IC-7).
- **Credit never transfers** (A3). Only debit moves, and only with the thing it attaches to.
- Standing is **derived from an append-only event log**, never stored (A6).
- **Debit is a vector** — mass, energy, labour-hours, land-area-years, water — collapsed only on demand, and **divided per dimension before collapsing** (§3.2a).
- **Property debit** splits into dischargeable material and holding-time-permanent creation cost (§3.2, §6.2b). **Consumption and pollution debit is permanent and stays on the causer** (§3.2b).
- The gate `D ≤ ρ·C` is a **ratio re-checked at each event**, evaluated at transaction time (§3.3, §7.5).
- **Pledges** are permanent, backed 1:1 by lifetime earned credit (IC-8), with surplus becoming a non-spendable contingent reserve (§6.4c).
- **Pollution weight floats with the ambient stock** above the natural-remediation baseline (§3.3).
- **Retroactive re-weighting**: improve a constant, and every affected record recomputes (§3.3).
- **Coverage** is estimated over the unmeasured residual, `(N − Y) / Z`, never over the whole population (§5.1b), and the leftover is charged to no account (§5.1c).

### 1b. The dials — set per scenario, and per network within a scenario

| Dial | Range that matters | Where it comes from |
|---|---|---|
| **ρ** — the consumption gate multiplier | ~0.5 to ~3 | §3.5, A8 |
| **`F`** — the self-care floor, in hours/day | 2 to 14 | §6.1b |
| **Verification cost** per unit checked | 0 to >0.4 of a median unit's debit | §5.3a (b) |
| **Privacy practice** | full transparency ↔ pseudo-privacy | §5.3a |
| **Production efficiency** | the Q6 spread: US ↔ German/Japanese/Spanish | Q6 |
| **Always-creditable activity set** | narrow ↔ generous | §10.1 |

> **⚠️ `F` must be a real dial, and on 2026-08-23 it was not.** The kernel had a `floor_h` setting that changed no number in the run, because the population was always built around `F` = 10 — credit is `min(r,f) + max(r−f,0) = r` for any `f ≤ r`. The floor appeared only in the divisor when reporting a ceiling, **dividing by a floor agent who was not in the simulation. A floor that no agent sits at is not a floor.** Fixed; guarded by a test that asserts the bound moves *and* that somebody sits at the floor. **Every report of a disparity figure must name the floor it assumed** — `24/F` is 2.40× at 10 h, 6.00× at 4 h, 1.71× at 14 h.

### 1b-ii. Adoption dials — the parallel phase

**Aequitas has to work for people who still use money, without excluding them.** [`OP-27_parallel_implementation.md`](OP-27_parallel_implementation.md) — **ruled and stress-tested 2026-08-23.** Both directions across the boundary are **deliberately costly**: a money-made good is dark until sold in and clears via a **pre-approved template**; selling out for money **keeps the debit and reads as a gift**, because A1 makes money invisible to the ledger. **The simulation has to express both, plus the template's conservatism as a dial.**

| Dial | Why |
|---|---|
| **Adoption rate** — agents joining per period | *At what rate does Aequitas fail to gain ground against money?* |
| **Starting population** — how many begin inside | *Is there a critical number?* OP-27 argues this is probably the wrong variable. |
| **Supplier-graph loop density** — what fraction of a participant's inputs and customers are also inside | **The variable OP-27 says actually matters.** WIR and Sardex survived by starting business-to-business inside dense input loops; Ithaca HOURS died with businesses holding scrip they could not spend, because their suppliers were outside. |
| **Sector membership** — *which* industries start inside | *What are the critical starting industries?* Testable directly against loop density: same headcount, different graph. |
| **Template conservatism** — how much dearer a templated good is than a real record | §5.1b says it must **err against the seller**, or onboarding properly never pays. **How much is the open question**, and it is the entry price for every dark good. |
| **Extractor policy** — agents who buy inside at cost and sell outside at market | OP-27 Exploit 1. The gate should shut them out in proportion to how hard they pull. **Measure how fast.** |

**A scenario may run several networks with different dial settings**, trading or refusing to trade. That is how floor-shopping (OP-14), federation (§5.3c), and network competition get tested at all.

### 1c. The world — plugged in per scenario

- **Population**: size, age structure, birth and death rates, and a trajectory over periods (boom, decline, shock).
- **Physical economy**: sectors with an input-output structure, per-sector intensities, a capacity or stock budget. **Two plugs: a small toy economy for fast sweeps, or the real EXIOBASE MRIO for calibrated runs.** ("MRIO" = multi-region input-output, the standard trade-and-production dataset.)
- **Pollutant stocks**: ambient level, natural remediation rate, remediation cost — and the ability to **add a pollutant nobody was tracking, at period *t***.
- **The alternative economy**: a money economy with its own rules, or the gift economy, or nothing, or a second Aequitas network. **Agents may cross the boundary.**
- **Shocks**: any dial or stock, changed at a named period, once or repeatedly.

### 1d. Behaviour — how agents decide

Where scenario variety actually lives. Each is a pluggable policy, not a hard-coded rule.

Whether to **join** a network · how much to **work** · what to **consume** · what to **pledge** · whether to **instrument** or stay dark · whether to **defect or defraud**.

### 1e. What gets measured

Disparity ratio · participation rate over time · coverage fraction · median lifestyle attained · ambient pollutant stock · aggregate debit against aggregate credit · the fraction locked out of discretionary consumption · **and every conformance assertion in §4 below.**

---

## 2. The shape: a kernel plus plugs

**One engine that does everything is a trap.** The existing scripts already span model classes that cannot honestly merge — `recursion_convergence.py` is linear algebra with no agents; `disparity_ceiling_sim.py` is 200,000 agents in cross-section; `q1_autarky.py` is a feasibility envelope. **Forcing those into one object produces something that answers nothing well.**

The decomposition that does work:

| Layer | What it is | Varies? |
|---|---|---|
| **Kernel** | Agents, an append-only event log, the debit vector, credit accrual, the ratio gate, and the axiom invariants. **This is Aequitas.** Small, and identical in every scenario. | **Never** |
| **Physical economy** | Sectors, intensities, capacity, pollutant stocks. | Plug: toy or MRIO |
| **Behaviour** | Join, work, consume, pledge, instrument, cheat. | Plug |
| **Outside world** | Money economy, gift economy, second network, or nothing. | Plug |
| **Scenario** | A configuration file naming the dials, the plugs, the shocks and when, the period count, and what to record. | **Every run** |

> **The thing worth noticing: nothing in `06-simulation/` is the kernel.** Every script re-implements a slice of it — its own credit accrual, its own gate, its own agents. **That duplication is why each one answers a single question and none composes with another.** Building the kernel once is the whole move.

---

## 3. The invariant set is the conformance list

[`Aequitas_Conformance_v0.4.md`](../00-strategy/Aequitas_Conformance_v0.4.md) carries **16 requirements that must hold for an implementation to be Aequitas.** They were written for an implementer. **They are also exactly what the kernel should assert, every period, in every scenario.**

**So `arithmetic_audits.py` is not a side artifact. It is the engine's test harness**, and IC-1 … IC-12 become continuous assertions rather than a one-off audit.

**What this buys, and it is the point:** if a scenario ever breaks conservation of mass, or lets credit transfer, or lets a division happen after the collapse instead of before, **the run fails loudly and you learn something.** Either the scenario is malformed, or the theory has a hole. **Both are results.** A simulator that cannot fail cannot teach.

---

## 4. The discipline that stops this becoming a framework nobody uses

**This is the real risk, and it deserves a rule rather than good intentions.**

> **The kernel must reproduce at least two existing published results before a single new scenario is run.**

The two, both already computed and both cheap to check:

1. **The disparity ceiling.** At `F = 10 h`, equal age, the ratio between the highest and lowest cumulative consumption must come out at **2.40×**, and it must stay 2.40× across every ρ from 1 to 3. *(From `disparity_ceiling_sim.py`, N = 200,000.)*
2. **The clearing rate.** Under the US production method, the market-clearing ρ must land near **1.20**, with the median person reaching about **0.92** of their desired lifestyle and roughly **35%** of people held below their wants. *(From `rho_sweep.py`.)*

**If the new kernel cannot re-derive those numbers, it is wrong, and no result it produces afterwards is worth reading.** They cost nothing to check and they are unforgiving.

**Second rule, against scope creep:** a scenario earns its place by naming *which axiom, mechanism, or open problem it could falsify.* A scenario that cannot fail interestingly is a demo, not an experiment.

---

## 5. Build order

**Something runnable at every step. No step is a framework with nothing on top of it.**

| Step | What | Done when |
|---|---|---|
| **1** | **The kernel**, with a toy economy and one period. Agents, event log, debit vector, credit accrual, the gate, the §9 assertions. | It reproduces **2.40× at a 10-hour floor** and **ρ* ≈ 1.20**, and the floor sweep tracks `24/F`. |
| **2** | **Periods.** Everything re-evaluated per period, credit accruing, stocks drawing down, the gate re-checked. | A ten-period run holds the invariants and the bound stays at `24/F` for whatever floor the scenario set. |
| **3** | **The scenario config layer.** Dials, shocks-at-period-*t*, and a recorder. | Any of the author's eight is expressible as a config file **with no new code**. |
| **4** | **The outside world plug.** Money economy, gift economy, second network with different dials, and a boundary agents cross. | Adoption and floor-shopping are both runnable. |
| **5** | **The MRIO plug.** Swap the toy economy for real EXIOBASE data via the existing `exiobase_loader.py`. | A calibrated run matches the ≈1,380 h/yr median-lifestyle anchor. |

**Step 3 is the acceptance test for the whole design.** If any of the eight needs new code at that point, the engine is not configurable and the design has to change before more is built on it.

---

## 6. Three of the eight, written as configurations

To show what "a scenario is a config" means concretely.

**Adoption in one locality.** Population 50,000 · outside world = money economy · boundary open · join policy = compare estimated position under §5.1d against staying out · 240 periods · record participation rate over time. **The joining incentive is already computed and is the thing under test:** a person onboarding at forty arrives with roughly **146,000 hours** of estimated credit against roughly **55,000 hours** of estimated consumption. **Does that pull enough people, fast enough, to reach a working density?** *Validation targets exist and are unforgiving: WIR has run since 1934 with ~60,000 businesses, Sardex reached 4,000+, and Ithaca HOURS died when its founder left. A model that cannot produce all three outcomes from different settings is wrong.*

**A pollutant discovered late.** Toy or MRIO economy · at period 120, add a pollutant with an ambient stock that has been accumulating unmeasured since period 0 · let §3.3 re-weight every affected record backwards · record how far ledgers move and whether the transaction-time rule holds. **Doubles as the first real test of component C4.**

**Floors that differ.** Two networks, `F = 10 h` and `F = 4 h` · both trading · counterparty re-computation on (§6.4b) · record whether agents migrate to the low-floor network and whether the ceiling leaks past `24/F`. **This is OP-14 floor-shopping, and Foundations §7.5 condition 1 currently asserts the answer with no evidence behind it.**

---

## 7. What the outreach agent asks for now

**Its asks change with this.** Until now it invited strangers to run record-integrity checks, and it recruited a record-integrity audience — post #1750 drew six replies, and **every one was about truncation, hashes and witnesses. None was about the economy.**

> **From here: run, extend, or attack a simulation of the economy — or propose a starting condition the engine cannot yet express.**

That last one is the most valuable request available, and it is free to answer. **A stranger who names a condition the engine cannot express has found a design hole**, which is worth more than a reproduction. Three finished economics claims are runnable today as bait: the **`24/F` disparity ceiling**, the **≈1,380 h/yr** median-lifestyle anchor, and the **Q6 efficiency spread**.

---

## 8. Still not in scope

- **A trust-network database.** Not ours (§1.2).
- **A production implementation.** The simulator is an instrument for testing a theory. **It is not a first version of the system**, and the moment it starts being treated as one, §1.2 has been breached again.
- **Any scenario whose result turns on a design choice rather than a principle.** Apply the dial test before adding it.
