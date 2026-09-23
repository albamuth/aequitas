# Method — the smallest effect size of interest (how to justify a detection threshold)

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | Citation |
|---|---|
| **Primer** | Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science*, 8(4), 355–362. [doi:10.1177/1948550617697177](https://journals.sagepub.com/doi/10.1177/1948550617697177) |
| **Tutorial, with a section on justifying the threshold** | Lakens, D., Scheel, A. M., & Isager, P. M. (2018). Equivalence testing for psychological research: A tutorial. *Advances in Methods and Practices in Psychological Science*, 1(2), 259–269. [doi:10.1177/2515245918770963](https://journals.sagepub.com/doi/10.1177/2515245918770963) |

## What it says

**To claim "no meaningful change", a study first states the smallest change it would count as meaningful.** This is the **smallest effect size of interest (SESOI)**. It is set before the data are seen, and it is justified by something outside the data: what matters in practice, what an instrument can resolve, or what earlier work found.

**"We saw no significant change" is not the same claim.** Without a stated SESOI there is no way to tell *"no effect"* from *"too small a study to see one"*.

## Why it matters to Aequitas

**`ceiling_rubric.py`'s `FIRE_THRESHOLD` = 0.005 is a SESOI in all but name.** Tests 8 and 9 say a change *"does not move it"*, and that is an equivalence claim. **This source says how to justify such a number. It does not supply the number.**

**A worked example of what a justification would have to say.** At `F` = 10 the statistic is `max(c) ÷ 10`.

| Change in the statistic | Change in the top account's credit |
|--:|--:|
| 0.005 | 0.005 × 10 = **0.05 h/day, about 3 minutes a day** |
| 0.153 (the measured top-1% deletion) | **1.53 h/day** |

**A justification would say why 3 minutes a day is the smallest change worth detecting.** For example: that credit is recorded to the minute, or that a smaller change has no effect on anybody's gate. **No file says either today.** So `0.005` stays **unsourced**, and this note records the route to sourcing it.

**Used by:** `06-simulation/ceiling-rubric/README.md`, *Test sources*.
