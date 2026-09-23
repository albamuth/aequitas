# Method — how to design and report a simulation study (ADEMP)

> **Version:** 0.1
> **Date:** 2026-09-23

**Type:** method source · **Retrieved:** 2026-09-23

| | |
|---|---|
| **Citation** | Morris, T. P., White, I. R., & Crowther, M. J. (2019). Using simulation studies to evaluate statistical methods. *Statistics in Medicine*, 38(11), 2074–2102. [doi:10.1002/sim.8086](https://onlinelibrary.wiley.com/doi/10.1002/sim.8086) |
| **Open copy** | [arXiv:1712.03198](https://arxiv.org/pdf/1712.03198) · [UCL Discovery](https://discovery.ucl.ac.uk/10066118/) |

## What it says

**A simulation study is planned and reported under five headings, ADEMP:**

| Letter | What it names |
|---|---|
| **A**ims | What the study is for |
| **D**ata-generating mechanism | How the synthetic data are drawn, and **why those settings** |
| **E**stimand | The quantity being estimated |
| **M**ethods | The procedures being evaluated |
| **P**erformance measures | How the methods are scored, **with the Monte Carlo standard error of each measure** |

**The Monte Carlo standard error (MCSE)** is the spread a performance measure shows from one set of random draws to another. **A result smaller than its MCSE is noise.**

## Why it matters to Aequitas

**Every self-test in `06-simulation/` scores a method on synthetic data, so this is the reporting standard they are held to** (ruling 2026-09-23: every test cites a source for its method).

**Two places it bites, found in Batch 1:**

1. **The D heading.** `disparity_ceiling_sim.py` draws its working population from `normal(6.0, 3.0)` with 35% non-workers. **ADEMP asks why those settings. No file says.**
2. **The P heading.** `ceiling_rubric.py` fires when the statistic moves by more than `0.005`. **ADEMP ties a performance threshold to the MCSE. The rubric's clean spread is exactly 0 because the statistic is saturated, so the MCSE is 0 and cannot justify 0.005 or any other value.**

**Used by:** `06-simulation/ceiling-rubric/README.md` and `06-simulation/disparity-ceiling/README.md`, *Test sources*.
