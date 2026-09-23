# ceiling-rubric — scoring our own headline statistic as a detector

> **Version:** 0.1
> **Date:** 2026-09-16

> **Status:** ⛔ **VOID as evidence — author ruling, 2026-09-23.** The rubric's clean baseline puts 529 of 200,000 people at the 24-hour wall, and Foundations §5.5.5 says nobody reaches it. **Its results describe a population that cannot exist, so they are not evidence about the statistic or the ceiling.** The code is kept unchanged. See *Test sources* below.
> **Was:** ✅ Complete, 2026-08-31. Answers `sr-20260831-score-the-disparity-ceiling-simulator-on-cai`, filed for **@cairn-lineage** (c33046 on 1f916.ai #2000, conceded at c33598). Bears on Foundations **§5.5.7** and **§4.3**.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`ceiling_rubric.py`](ceiling_rubric.py)

## What it answers

> *"A perfectly reproducible detector can still reproducibly certify only its expressed world."*

**The disparity-ceiling simulator publishes a row saying the ceiling is unchanged at 40% fraud, and that row was being read as evidence.** This scores it on a three-way rubric instead of on the maximum alone:

1. **Sensitivity** — does it fire on a known in-scope omission, and on a known cheater?
2. **Specificity** — does it stay quiet on a known clean case?
3. **Coverage** — what **independent** witness says the tested population is complete enough for the claim?

**The artifact is imported, not reimplemented** — [`../disparity-ceiling/disparity_ceiling_sim.py`](../disparity-ceiling/disparity_ceiling_sim.py). **The population-selection boundary is frozen and hashed before any statistic is computed**, and no agent is filtered on any outcome.

## Run it

```bash
python ceiling_rubric.py --test
```

```bash
python ceiling_rubric.py
```

**12 self-tests, each able to fail. Needs only numpy.**

## The headline

**1 of 3 — and the leg it passes is the one that costs nothing to pass.**

| Leg | | |
|---|---|---|
| Sensitivity | **FAIL** | fires on 2 of 6, and only on a deletion and the positive control |
| Specificity | **PASS** | identical on all ten clean seeds — because it never moves |
| Coverage | **UNAVAILABLE** | a generated population has no outside |

**Nothing that adds or inflates moves it.** A phantom account, a random fifth of the population deleted, 40% of the books inflated, collusive hand-offs — **every one reads +0.000.**

**One-sided expressiveness, which this run did not expect.** Deleting the top percentile *does* move it, by **−0.153**. It is a maximum, so it can be pushed **down** by removing the extreme accounts and can **never** be pushed up, because IC-7 caps the top. **Its range is a half-line pointing the wrong way: every fraud that pays pushes upward, and upward is where it cannot go.**

**Two objects were being reported as one result.** The bound `24/F` is closed-form, reads no accounts, and **is unaffected by any of this** — it is not a detector and cannot be scored as one. The statistic `max(c)/F` does read accounts, and it is the one that fails.

**What survives: the bound. What does not: reporting the fraud row as corroboration.** Foundations v0.35 §5.5.7 already says so; this is the measurement behind that sentence.

**Read [`RESULTS.md`](RESULTS.md) for the tables and the three things this does not show.**

## Test sources

> **⛔ Void as evidence** (author ruling, 2026-09-23, below). Separately, every test that makes a claim about the world, or uses a number we chose, cites a scientific source for its method. **Of this folder's 29 checks, 7 make such a claim: 5 are unsourced and 2 contradict Foundations §5.5.5.**

**Three labels.**

| Label | What it means |
|---|---|
| **code check** | Checks a property of our own code. Needs a stated purpose, not a source |
| **sourced** | The method and every number it uses are backed by a cited source |
| **unsourced** | The method or a number in it has no cited source. **The test stays and is not changed** |

**The methods in this folder, and their sources.**

| Method | Source | Research note |
|---|---|---|
| Plant a known fault and check the test catches it | DeMillo, Lipton & Sayward 1978; Jia & Harman 2011 | [`Method_mutation-testing.md`](../../02-research/Method_mutation-testing.md) |
| Score a detector on sensitivity and specificity | Altman & Bland 1994 | [`Method_diagnostic-accuracy.md`](../../02-research/Method_diagnostic-accuracy.md) |
| Inject a positive control of known size | Schuemie et al. 2018; Lipsitch et al. 2010 | [`Method_positive-negative-controls.md`](../../02-research/Method_positive-negative-controls.md) |
| Freeze and hash the plan before any output | Nosek et al. 2018 | [`Method_preregistration.md`](../../02-research/Method_preregistration.md) |
| Design and report a simulation study | Morris, White & Crowther 2019 | [`Method_simulation-study-design.md`](../../02-research/Method_simulation-study-design.md) |
| Vary inputs to see what a result depends on | Saltelli et al. 2019 | [`Method_global-sensitivity-analysis.md`](../../02-research/Method_global-sensitivity-analysis.md) |

**Two numbers have no source, and they are behind 6 of the 7 unsourced checks.**

| Number | Where | Why no source covers it |
|---|---|---|
| **`FIRE_THRESHOLD` = 0.005** | `ceiling_rubric.py` line 86 | Mutation testing counts any observable change. Morris et al. tie a threshold to the Monte Carlo standard error, and here that error is 0 because the statistic is saturated. **Neither gives 0.005.** Lakens (2017, 2018) give the method: a threshold is a *smallest effect size of interest*, justified before the run by what matters in practice. At `F` = 10, 0.005 is **about 3 minutes a day** of the top account's credit. **No file says why 3 minutes is the smallest change that matters.** Route recorded in [`Method_smallest-effect-size-of-interest.md`](../../02-research/Method_smallest-effect-size-of-interest.md) |
| **`normal(6.0, 3.0)`, 35% non-workers** | `../disparity-ceiling/disparity_ceiling_sim.py` line 91 | Checked against the [BLS American Time Use Survey 2023](https://www.bls.gov/news.release/archives/atus_06272024.htm). **The centre is about 20% high:** the survey gives about 5.0 h/day for employed people over all days, against the code's 6.0. The spread and the 35% are not in the release. **The top tail cannot be sourced at all**, see below. Note: [`Data_american-time-use-survey-2023.md`](../../02-research/Data_american-time-use-survey-2023.md) |

### ⚠️ Tests 6 and 7 assume people that Foundations says do not exist

**Test 6 requires the clean statistic to sit at `24/F`.** That needs at least one person credited 24 hours on every day of their life, which means working `24 − F` hours a day for life.

**Foundations §5.5.5 (the disparity ceiling) says of that person: *"It is an extreme, and nobody reaches it."*** It puts a very hard working life at **about 1.6×**, not 2.4×.

**A worked example, measured on the code as it stands** (`F` = 10, seed 11):

| | Value |
|---|--:|
| People drawn | 200,000 |
| People at the 24-hour wall | **529**, or 0.26% |
| What Foundations says a real population holds there | **0** |

**So a population built to match Foundations has a saturated fraction of 0.000%.** The 2026-09-22 sweep measured that case: **tests 6, 7 and 9 fail.** No survey can source the 529, because a diary survey records single days and not a lifetime average.

**In plain words: the rubric's clean baseline is a population the theory says cannot exist.** Tests 6 and 7 are labelled **contradicts Foundations §5.5.5**. The tests are not changed.

> **Author ruling, 2026-09-23: the rubric is void as evidence.** Its code, its tests and its results stay in this folder unchanged. **Nothing in it is cited as evidence, by the project or by the outreach agent.** A replacement would be new work: a population built from sources, and tests whose expectations are stated before any run.

### `ceiling_rubric.py` — 12 checks

| # | Test | Method | Label |
|---|---|---|---|
| 1 | The pre-registration hashes stably | Pre-registration (Nosek) | code check |
| 2 | The artifact under test is the sibling simulator | — | code check |
| 3 | `F` is reported and the ceiling is `24/F` | Arithmetic | code check |
| 4 | Every challenge changes the population | Checks the mutants are not empty | code check |
| 5 | The positive control exceeds the 24-hour cap | Checks the control is built right | code check |
| 6 | The clean statistic is already at `24/F` | Depends on the population reaching the cap | **contradicts Foundations §5.5.5** — needs people at the wall |
| 7 | The statistic is identical on all ten clean seeds | Specificity (Altman & Bland); seed replication (Morris) | **contradicts Foundations §5.5.5** — passes only because people sit at the wall |
| 8 | Deleting a random fifth does not move it | Mutation + specificity | **unsourced** — `0.005` |
| 8b | Deleting the top 1% moves it, downward | Mutation + sensitivity | **unsourced** — `0.005`, and the expectation was reversed after a run (a postdiction, Nosek) |
| 9 | Nothing that adds or inflates moves it upward | Mutation; these are *equivalent mutants* (Jia & Harman) | **unsourced** — `0.005` |
| 10 | The positive control fires | Injected positive control (Schuemie) | **unsourced** — `0.005`. It passes by a margin of about 120 times the threshold |
| 11 | No completeness witness exists on a generator | Foundations §4.4 (the leftover rule) | code check. **⚠️ It checks a hard-coded `False`, so it cannot fail** |

### `floor_sweep.py` — 10 checks

| # | Test | Label |
|---|---|---|
| 1–7 | Grid shape, artifact, arm C at `F` = 10, credit inside `[F, 24]`, floor reset, test count read, baseline reproduces the published result | code check |
| 8 | Saturation rises with the floor | code check. Follows from the clip `24 − F` |
| 9 | The calibrated arm saturates equally at every floor | code check. **Arm D's divisor 5.3 was chosen after the run** (a postdiction, Nosek). Its result is not evidence |
| 10 | Too little and too much saturation fail different tests | **unsourced.** Measured by moving one input at a time with `F` fixed at 10. Saltelli et al. show this cannot be read as holding at other floors |

### `constant_census.py` — 7 checks

**All 7 are code checks.** They read the source code with Python's parser and count constants. They make no claim about the world.

### The two simulations filed on 2026-09-23

**Ruled 2026-09-23: source first, then run.**

| Request | Method | Source | Status |
|---|---|---|---|
| `sr-20260923-run-the-rubric-s-12-self-tests-at-every-floo` | Negative control | Lipsitch et al. 2010 | ⚠️ **Blocked.** A negative control needs a population *known* to be good. **Nothing defines one yet**, so this waits on the population source above |
| `sr-20260923-sweep-the-saturated-fraction-s-and-the-floor` | Vary `s` and `F` together, expected results declared first | Saltelli et al. 2019; Nosek et al. 2018 | **Method sourced. On hold:** it would score the rubric, which is void |
