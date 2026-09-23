# Method — sensitivity analysis, and why one-at-a-time is not enough

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | |
|---|---|
| **Citation** | Saltelli, A., Aleksankina, K., Becker, W., Fennell, P., Ferretti, F., Holst, N., Li, S., & Wu, Q. (2019). Why so many published sensitivity analyses are false: A systematic review of sensitivity analysis practices. *Environmental Modelling & Software*, 114, 29–39. [doi:10.1016/j.envsoft.2019.01.012](https://www.sciencedirect.com/science/article/pii/S1364815218302822) |
| **Open copy** | [arXiv:1711.11359](https://arxiv.org/abs/1711.11359) |

## What it says

**Most published sensitivity analyses move one input at a time (OAT) and hold the others fixed.** That explores a thin line through the input space and leaves most of it unseen. **Where inputs interact, OAT misses the interaction.** The authors recommend **global** methods, which vary all inputs together across their ranges.

**A worked example, with numbers.** Two inputs, each tested at 10 values.

| Design | Points tested | Share of the 10 × 10 grid seen |
|---|--:|--:|
| One at a time, from one centre point | 10 + 10 − 1 = **19** | **19%** |
| Full grid | 10 × 10 = **100** | **100%** |

## Why it matters to Aequitas

| Where | What this source says |
|---|---|
| `floor_sweep.py` — moves `F` with the population fixed, then moves the spread with `F` fixed at 10 | **Two OAT scans.** The window `s` ∈ [0.002%, 0.797%] is measured at one floor only. **This source says it cannot be read as holding at other floors** |
| Sim request `sr-20260923-sweep-the-saturated-fraction-s-and-the-floor` — `s` and `F` varied independently | **Closer to what this source recommends** |

**Used by:** `06-simulation/ceiling-rubric/README.md`, *Test sources*.
