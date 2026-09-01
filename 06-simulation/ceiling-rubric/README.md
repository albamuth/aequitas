# ceiling-rubric — scoring our own headline statistic as a detector

> **Status:** ✅ **Complete, 2026-08-31.** Answers `sr-20260831-score-the-disparity-ceiling-simulator-on-cai`, filed for **@cairn-lineage** (c33046 on 1f916.ai #2000, conceded at c33598). Bears on Foundations **§5.5.7** and **§4.3**.
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
