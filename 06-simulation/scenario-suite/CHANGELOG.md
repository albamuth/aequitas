# Scenario suite — change history

> Newest entry first. What the project is: [`README.md`](README.md). What it found: [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — moved into its own folder. Nothing else changed.

The five scripts, their five companion documents, the method plan and the three Q4 figures moved from the flat `06-simulation/` directory into `06-simulation/scenario-suite/`. None of the five imports another and none reads a data file, so no code was touched.

**Verified after the move:** all five `--test` runs pass.

---

### 2026-08-23 — superseded as machinery, not as answers

The ruling that the code deliverable is **one configurable simulator, never a pile of scripts** made this folder historical. Two structural findings were recorded at the time and both are about these five:

1. **Every one of them is single-period.** There is no time axis anywhere here.
2. **None of them is the kernel.** Each re-implements its own agents, its own credit accrual and its own gate, which is why none composes with another.

**The answers stand and are still cited.** The machinery is replaced by [`../statera/`](../statera/), where a scenario is a configuration file rather than a script.

Roadmap: [`../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md`](../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md).

---

### 2026-08-10 — all five built and green

Five societal-scale questions asked by the author, answered in one session. Q3 (plastic) first, then Q4 (locked ledgers), Q1 (autarky), Q2 (capture), Q5 (reallocation).

**The design rule settled here still governs any scenario added later.** Aequitas is a theory of cost, not value, and has no planner — so "highest standard of living", "wasteful against essential" and "stolen labour" are framings it does not natively produce. Each sim is therefore built either as a **physical feasibility envelope** with no preference in it, or as an **exogenous dial the reader can move**, stated as contestable and given a sensitivity pass. **Never as an Aequitas verdict.** Set out in [`scenario_suite_METHOD.md`](scenario_suite_METHOD.md).

Anchored on the median-lifestyle result in [`../median-lifestyle/`](../median-lifestyle/) and the disparity-ceiling sim in [`../disparity-ceiling/`](../disparity-ceiling/).

Journal entry: [`../../03-journal/2026-08-10.md`](../../03-journal/2026-08-10.md).
