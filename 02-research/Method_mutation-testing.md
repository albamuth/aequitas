# Method — mutation testing (inject a known fault, see if the test catches it)

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | Citation |
|---|---|
| **Origin** | DeMillo, R. A., Lipton, R. J., & Sayward, F. G. (1978). Hints on test data selection: Help for the practicing programmer. *IEEE Computer*, 11(4), 34–41. [doi:10.1109/C-M.1978.218136](https://doi.org/10.1109/C-M.1978.218136) |
| **Survey** | Jia, Y., & Harman, M. (2011). An analysis and survey of the development of mutation testing. *IEEE Transactions on Software Engineering*, 37(5), 649–678. [doi:10.1109/TSE.2010.62](https://dl.acm.org/doi/10.1109/TSE.2010.62) |

> ⚠️ The page range of the 1978 paper is given as 31–41 in one secondary listing and 34–41 in others. **Check against the journal before quoting pages.**

## What it says

**A test suite is judged by planting small, known faults ("mutants") in what it tests, and counting how many the suite detects ("kills").** A mutant the suite does not kill shows a gap in the suite.

**One known limit:** some mutants change nothing observable. They are called **equivalent mutants**, and no test can kill them. Jia & Harman treat this as a central open problem of the method.

## Why it matters to Aequitas

**`ceiling_rubric.py`'s six challenges (C1–C5) are mutants.** Each plants a known fault — phantom accounts, deletions, inflation, collusion, a 30-hour day — and checks whether the statistic `max(c)/F` moves.

**The equivalent-mutant limit is the rubric's own finding.** Inflation and collusion are capped by IC-7 (the 24-hour cap), so on a saturated population they change nothing the statistic can see. **The literature names that case; the rubric rediscovered it.**

**What the method does not supply:** the size of move that counts as a kill. The rubric uses `0.005`. **Mutation testing kills on any observable difference, so this source does not justify that number.**

**Used by:** `06-simulation/ceiling-rubric/README.md`, *Test sources*.
