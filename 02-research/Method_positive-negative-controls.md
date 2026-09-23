# Method — positive and negative controls

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | Citation |
|---|---|
| **Negative controls** | Lipsitch, M., Tchetgen Tchetgen, E., & Cohen, T. (2010). Negative controls: A tool for detecting confounding and bias in observational studies. *Epidemiology*, 21(3), 383–388. [PubMed 20335814](https://pubmed.ncbi.nlm.nih.gov/20335814/) |
| **Synthetic positive controls** | Schuemie, M. J., Hripcsak, G., Ryan, P. B., Madigan, D., & Suchard, M. A. (2018). Empirical confidence interval calibration for population-level effect estimation studies in observational healthcare data. *PNAS*, 115(11), 2571–2577. [doi:10.1073/pnas.1708282114](https://www.pnas.org/doi/10.1073/pnas.1708282114) |

## What they say

| Control | What it is | What a failure means |
|---|---|---|
| **Negative control** | A case where the true effect is known to be **zero** | The method finds effects that are not there |
| **Positive control** | A case where the true effect is known and **not zero** | The method cannot see effects that are there. **A failed positive control voids the whole run** |

**Schuemie et al. build positive controls by injection:** they take a case known to have no effect and add simulated outcomes until the true effect is a known size (a relative risk of 1.5, 2 or 4). **The method is then scored on whether it recovers the size it was given.**

## Why it matters to Aequitas

| Where | Which control |
|---|---|
| `ceiling_rubric.py` C5, test 10 — one account set to 30 h/day | **An injected positive control**, the Schuemie shape |
| Sim request `sr-20260923-run-the-rubric-s-12-self-tests-at-every-floo` — the 12 tests against a known-good population | **A negative control.** ⚠️ It needs a population that is *known* good, and **no file yet says what makes one known good** |

**Used by:** `06-simulation/ceiling-rubric/README.md`, *Test sources*.
