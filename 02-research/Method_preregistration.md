# Method — pre-registration (fix the plan before seeing the result)

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | |
|---|---|
| **Citation** | Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences*, 115(11), 2600–2606. [doi:10.1073/pnas.1708274114](https://www.pnas.org/doi/10.1073/pnas.1708274114) |

## What it says

**A prediction is a test only if it was stated before the data were seen.** A result explained after seeing the data is a **postdiction**. It can suggest a hypothesis. **It cannot confirm one.** Mixing the two up makes findings look stronger than they are.

## Why it matters to Aequitas

| Where | What this source says about it |
|---|---|
| `ceiling_rubric.py` freezes and hashes its settings (`PREREG`) before computing anything | **The method this source recommends** |
| `floor_sweep.py` arm D: divisor 5.3, read off the results after three arms had run | **A postdiction.** It shows a population exists that passes. **It confirms nothing** |
| Test 8b's expectation, reversed after a first run showed it wrong | **A postdiction.** The new expectation needs its own justification |
| Sim request `sr-20260923-sweep-the-saturated-fraction-s-and-the-floor`, which declares each test's expected class before the run | **The method this source recommends** |

**Used by:** `06-simulation/ceiling-rubric/README.md`, *Test sources*. Author ruling 2026-09-23: *"We cannot 'fix' a test just to make it pass."*
