# Implementation plan — source every self-test in the literature

> **Ruling, 2026-09-23:** *"We cannot 'fix' a test just to make it pass. The point of the tests are science. For all the tests, we need to show sources in science literature that justifies the methodology."* Scope ruled the same day: **all 43 files at once.**
> Recorded in full in `07-outreach/log/PLAN-2026-09-23.md`, *Author rulings*.

## 0. What this plan does and does not do

| It does | It does not |
|---|---|
| Give every self-test a written method and a cited source | **Change any test so it passes** |
| Mark each test **sourced**, **code check**, or **unsourced** | Delete an unsourced test |
| Put the sources in each project's own `README.md` | Touch a core document |

**Terms.**

| Term | What it means |
|---|---|
| **Self-test** | A check a simulation file runs against itself with `--test` |
| **Sourced** | The test's method is backed by a cited, linked paper or textbook |
| **Code check** | The test checks a property of the code, not a claim about the world. Example: *"the pre-registration hashes stably"* (`ceiling_rubric.py` test 1). **Needs a stated purpose, not literature** (ruled 2026-09-23) |
| **Unsourced** | Neither of the above. **The test stays, is flagged, and is not cited as evidence until sourced** |

## 1. The scale

**43 files in 23 folders, about 290 checks.** Three files sit in `99-superseded/` folders.

| Batch | Folder | Files | Checks |
|--:|---|--:|--:|
| 1 | `ceiling-rubric/` | 3 | 29 |
| 1 | `disparity-ceiling/` | 2 | 12 |
| 2 | `stable-band/` | 4 | 24 |
| 2 | `scenario-suite/` | 6 | 30 |
| 3 | `median-lifestyle/` (current) | 9 | 33 |
| 4 | `allocation-engine/` · `chain-resolution/` · `method-spread/` | 6 | 34 |
| 5 | `residual-attribution/` · `residual-unravelling/` · `producer-side-splitting/` · `cross-network-splitting/` · `correlated-miss/` | 5 | 43 |
| 6 | `ic-recompute-cost/` · `pledge-reserve/` · `axiom-reachability/` · `mirror-link-audit/` | 5 | 30 |
| 7 | **`99-superseded/`** — `statera/` (2 files), `median-lifestyle/99-superseded/` (1 file) | 3 | 48 |

**Batch 1 done 2026-09-23:** 41 checks — 30 code checks, 1 sourced, 10 unsourced. Tables in `ceiling-rubric/README.md` and `disparity-ceiling/README.md`.

**In plain words: seven batches, each one sitting.** Batch 1 goes first because the outreach agent is arguing about those tests in public now.

## 2. The method, per test

1. **Read the test.** Write its method in one sentence: what it changes, what it expects, and why.
2. **Classify it:** sourced, code check, or unsourced.
3. **For a method test, find the source.** Use the `research` skill. Every source gets a stub in `02-research/` with citation, retrieval date, and link.
4. **Where the expectation used a number we chose** (example: `FIRE_THRESHOLD` = 0.005), the source must justify **that number** or the test is unsourced.
5. **Never edit a test's expectation during this work.** A test the literature contradicts is flagged for a ruling.

**A worked example, from Batch 1.**

| Test | Method in one sentence | Likely field to search | Our own number in it |
|---|---|---|---|
| `ceiling_rubric.py` 10 — *the positive control fires* | Inject a known fault (30 h/day) and require the instrument to detect it | Positive controls in experimental design; mutation testing in software | None |
| `ceiling_rubric.py` 8b — *deleting the top percentile moves the statistic* | Delete the top 1% and require a change larger than 0.005 | Sensitivity analysis; influence of extreme values on a maximum | **0.005**, and **1%** |

## 3. Files

| | File | Change |
|---|---|---|
| **[MODIFY]** | 23 × `06-simulation/<project>/README.md` | Add a **Test sources** table: test · method · classification · citation |
| **[NEW]** | `02-research/<Author>_<topic>.md`, one per source | Research stubs |
| **[MODIFY]** | `06-simulation/README.md` | One column on the landing table: *tests sourced / total* |
| **[MODIFY]** | 23 × `06-simulation/<project>/CHANGELOG.md` | One line each |
| **[MODIFY]** | `NEXT.yaml` → `python bin/next.py --render` | Seven batches as tasks |
| **[NEW]** | `06-simulation/test_sources_check.py` | Fails if any file with a self-test has no **Test sources** table. Wired into `bin/consistency.py` |
| **[DELETE]** | none | |

**No `.py` self-test is edited.**

## 4. Rulings owed before Batch 1 starts

1. ~~**Code checks.**~~ **Ruled 2026-09-23: purpose only.** A test of the code itself gets a one-sentence purpose and the label *code check*. **A literature source is needed only where a test makes a claim about the world or uses a number we chose.**
2. ~~**The outreach agent.**~~ **Ruled 2026-09-23: stop citing.** The agent cites no result from `ceiling-rubric/` as evidence until its README carries a **Test sources** table. Written into `AGENT_BRIEF.md` §8.
3. ~~**The two sims filed on 09-23.**~~ **Ruled 2026-09-23: source first, then run.** Their methods join Batch 1.
