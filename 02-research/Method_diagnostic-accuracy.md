# Method — sensitivity and specificity of a test

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | |
|---|---|
| **Citation** | Altman, D. G., & Bland, J. M. (1994). Diagnostic tests 1: Sensitivity and specificity. *BMJ*, 308(6943), 1552. [doi:10.1136/bmj.308.6943.1552](https://pmc.ncbi.nlm.nih.gov/articles/PMC2540489/) |

## What it says

| Term | What it means |
|---|---|
| **Sensitivity** | Of the cases that really have the condition, the share the test flags |
| **Specificity** | Of the cases that really do not, the share the test leaves alone |

**A test is judged on both.** A test that never flags anything has perfect specificity and zero sensitivity.

**A worked example, with numbers.** 100 people have a disease and 900 do not. A test flags 80 of the 100 and 45 of the 900.

| | Value |
|---|--:|
| Sensitivity | 80 ÷ 100 = **0.80** |
| Specificity | (900 − 45) ÷ 900 = **0.95** |

## Why it matters to Aequitas

**`ceiling_rubric.py` scores the statistic `max(c)/F` on these two legs, plus coverage.** Its headline — specificity passes *"because it never moves"* — is the textbook case above: **perfect specificity bought with no sensitivity.** This source supplies the method. **It does not supply the threshold `0.005` at which the rubric counts a move as a flag.**

**Used by:** `06-simulation/ceiling-rubric/README.md`, *Test sources*.
