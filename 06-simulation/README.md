# 06-simulation — the code, and what it found

> **Version:** 0.1
> **Date:** 2026-09-16

> **You should be able to read this page and know where everything is without opening anything else.**
> New here, and want the tour rather than the index? Read [`Simulations_in_Plain_Language.md`](Simulations_in_Plain_Language.md) — a sceptic's walk through every sim, asking of each one *could this have failed?*

---

## The projects

Every command below is run **from inside that project's folder**. Every project has a `README.md` (what it is), a `RESULTS.md` (the numbers, so you need not re-run), and a `CHANGELOG.md` (when and why it changed).

| Project | What it answers | Run it | Status |
|---|---|---|---|
| **[`99-superseded/statera/`](99-superseded/statera/README.md)** | The kernel. Agents, an append-only event log, the debit vector, credit accrual, the ratio gate, the conformance checks. | — | ⛔ **RETIRED 2026-09-18** (author ruling). Its `room()` encodes the pledge rule withdrawn that day: the grant was capped at the recipient's own creation-cost and never became spendable. **Do not learn the gate from it.** The current gate is `D ≤ ρ·(C + P)`, in [`stable-band/gate.py`](stable-band/gate.py). |
| **[`disparity-ceiling/`](disparity-ceiling/README.md)** | How far apart can two people's consumption get? And where should the consumption dial ρ sit? | `python disparity_ceiling_sim.py --test`<br>`python rho_sweep.py --test` | ✅ Stated, simulated, stress-tested. A **conditional** result. |
| **[`median-lifestyle/`](median-lifestyle/README.md)** | What does a normal life cost, in hours of human labour? Four measured tracks plus a cross-country comparison. | `python track1_embodied_hours.py --test`<br>(one script per track) | ✅ Done. **The project's real-world anchor.** |
| **[`essentials-basket/`](essentials-basket/README.md)** | How many hours of work does a year of essentials take? This is `E` in Foundations §5.5.3, the floor's lower bound. | `python essentials.py --test` | ✅ Done 2026-09-24. Narrow and broad baskets. |
| **[`allocation-engine/`](allocation-engine/README.md)** | Does the cost recursion converge, and is every share non-negative? Then: per-product costs from a real economy, and a refinery where physical and price allocation disagree. | `python recursion_convergence.py --test`<br>`python estimation_engine.py --test`<br>`python refinery_slice.py --test` | ✅ Done. Closed the project's sharpest technical risk. |
| **[`audits/`](audits/README.md)** | The twelve event-log integrity constraints, made runnable — and each one shown to actually fire. | `python arithmetic_audits.py --test` | ✅ Closed. Plus `audits_inert/`, the same audits **as data**, checkable without running code. |
| **[`scenario-suite/`](scenario-suite/README.md)** | Five societal questions: autarky, captured labour, plastic, who is locked out, wasteful-to-essential reallocation. | `python q1_autarky.py --test`<br>(one script per question) | ✅ Answers stand. **Each script carries its own gate**, so none depends on the retired kernel. |
| **[`residual-unravelling/`](residual-unravelling/README.md)** | Does staying unmeasured stop paying? Tests the rule that cohort estimates are computed over the residual, never the population. | `python residual_unravelling.py --test` | ✅ Passes, with one measured limit. |
| **[`pledge-reserve/`](pledge-reserve/README.md)** | Why would anyone take the hazardous job in a system with no wage premium? | `python pledge_reserve.py --test` | ✅ Built. Answers the hazard half of the onerousness gap. |
| **[`stable-band/`](stable-band/README.md)** | Is there a band of the floor `F` and the tolerance ρ inside which essentials stay affordable **and** the ledger still rations? | `python stable_band.py --test` | ✅ **Done 2026-08-28; re-measured 2026-10-27** with demand tied to 1,380 h/yr. At the US method the band closes at `F` = 2 on the broad basket. |
| **[`cross-network-splitting/`](cross-network-splitting/README.md)** | Can a person split their consumption across two trust networks to keep each book's figure low, and does the residual estimate catch them? | `python cross_network_splitting.py --test` | ✅ **Done 2026-08-28.** Answers @cairn-lineage's open half. Registered with **OP-22**. |
| **[`correlated-miss/`](correlated-miss/README.md)** | How far does `R = N − Y` move when the outside total and the network's own books share a blind spot? | `python correlated_miss.py --test` | ✅ **Done 2026-08-29.** Answers @cairn-lineage c21187. **OP-26**, **OP-24**. |
| **[`ic-recompute-cost/`](ic-recompute-cost/README.md)** | What does it cost a stranger to re-run IC-1 to IC-9 over a real-economy-sized event log? | `python ic_recompute_cost.py --test` | ✅ **Done 2026-08-29.** Answers the Futurist lens, 2026-08-22. |
| **[`producer-side-splitting/`](producer-side-splitting/README.md)** | One producer routes output through two networks and leaves both networks' `Z`. What does that do to the leftover estimate, and can either network see it from its own books? | `python producer_side_splitting.py --test` | ✅ **Done 2026-08-31.** Answers @cairn-lineage c27820. Registered with **OP-28**. |
| **[`residual-attribution/`](residual-attribution/README.md)** | Three rules have been proposed for assigning the leftover `N − Y` to people instead of holding it. Are any of them witnesses, or are they all guesses? | `python residual_attribution.py --test` | ✅ **Done 2026-08-31.** Answers @cairn-lineage c30285. Foundations **§4.4**. |
| **[`ceiling-rubric/`](ceiling-rubric/README.md)** | Score our own headline statistic as a detector: does it fire on a known omission, stay quiet on a clean case, and what witnesses that the tested population is complete? | `python ceiling_rubric.py --test` | ⛔ **Void as evidence, 2026-09-23.** Its clean baseline puts people at the 24-hour wall, which Foundations §5.5.5 says nobody reaches. Code kept. Was: done 2026-08-31, for @cairn-lineage c33046. |
| **[`method-spread/`](method-spread/README.md)** | How far did a §3.4a joint-process split move across honest methods? | `python method_spread.py --test` | ⚠️ **Superseded 2026-09-03.** The split rule it measured was withdrawn. **Kept because it is the measurement that caused the withdrawal.** |
| **[`chain-resolution/`](chain-resolution/README.md)** | If a joint process's cost is not divided, what does reading the chain more finely change — and do the books inflate? | `python chain_resolution.py --test` | ✅ **Done 2026-09-03.** Answers the author ruling of the same day. Foundations **§3.4a**, **§2.5**, **A3**. |
| **[`fractional-holdings/`](fractional-holdings/README.md)** | One account holds part of several co-products of one process. What does it carry? | `python fractional_holdings.py --test` | ✅ **Done 2026-10-13.** "Max" passes; the rivals fail row 10c. Nightcheck decision 5.3. Foundations **§3.4a**. |
| **[`household-consolidation/`](household-consolidation/README.md)** | How much does a two-adult household save under max by putting co-products of one process on one account? | `python household_consolidation.py --test` | ✅ **Done 2026-10-16.** 8/8 self-tests; code matches the hand figures: 0.12 h/yr typical (0.004% of household debit), under 1% at every swept corner. Nothing in the documents moves. Foundations **§3.4a**. |

---

## The nightly simulation agent — one request a night, on the author's machine

**A Windows scheduled task on the author's machine, 04:00 daily.** The agent works through the outreach agent's open simulation requests, one a night, and leaves a report for the author to read in the morning.

> **It runs simulations and publishes nothing. The 03:00 outreach agent posts in public and runs no simulations.** That separation was ruled on 2026-08-25 and this agent keeps it. The agent has no git and no token. After it exits, the launcher commits `06-simulation/` to the private repository, and only there.

| | |
|---|---|
| **Where it runs** | This machine, inside the private project, from the task **Aequitas simulation nightly** ([`bin/install_sim_task.ps1`](bin/install_sim_task.ps1)) |
| **When** | **04:00 local**, daily, one hour after the outreach run, whose own limit is one hour. The two never overlap |
| **The launcher** | [`bin/run_sim_night.ps1`](bin/run_sim_night.ps1): picks the request, builds the prompt, runs the agent at Sonnet-level effort, then commits |
| **What it may write** | Inside `06-simulation/` only, never `data/`. **Never `00-strategy/`, never `07-outreach/`** |
| **Which request** | The author's pin in [`PINNED_SIM.txt`](PINNED_SIM.txt) if there is one, else **the oldest open request** that no report in `log/` has run |
| **Where the requests come from** | **The outreach agent's live index**, `07-outreach/memory/index.yaml`, which it fills with `memory.py request-sim`. [`SIM_QUEUE.yaml`](SIM_QUEUE.yaml) is a committed copy for readers of the public mirror; the picker falls back to it only if the index is absent |
| **The budget** | **One hour of wall clock, 1 GB of new files.** The task kills the run at the hour. The agent estimates first and reports a request that does not fit as Blocked, with the cost, instead of running it |
| **What it needs** | numpy, scipy, PyYAML, openpyxl on this machine. **`data/` is here**, read in place |
| **Closing a request** | **The author does it**, after reading the report. The agent is forbidden from running `answer-sim` |
| **Its brief** | [`SIM_AGENT_BRIEF.md`](SIM_AGENT_BRIEF.md): the boundary, the budget, and the two rules that decide whether a run is worth anything |
| **Its prompt** | [`SIM_NIGHTLY_PROMPT.md`](SIM_NIGHTLY_PROMPT.md), with the request and the date substituted by the launcher |
| **Its report** | `log/SIM-<date>.md`. The raw transcript is `log/runs/run-<stamp>.txt` |
| **After it exits** | The launcher stages `06-simulation/`, commits `sim night <date>`, and pushes to the private repository if `bin/consistency.py` passes. The public mirror is untouched until the author runs `sync_archive.ps1` |

**Commands you will actually use:**

```bash
python 06-simulation/bin/pick_sim.py --list     # every open request, oldest first; marks the ones with a report
python 06-simulation/bin/pick_sim.py            # what tonight would pick
python 06-simulation/bin/pick_sim.py --export   # refresh SIM_QUEUE.yaml, the public copy, when you next sync
```

**In the morning:** read `log/SIM-<date>.md`, then run the `answer-sim` command the report ends with. The night's commit is already on `main`. A night not worth keeping is reverted with `git revert`.

**To pin one**, put its id on its own line in [`PINNED_SIM.txt`](PINNED_SIM.txt). **To clear the pin**, delete that line.

**Install or move the task:** `powershell -ExecutionPolicy Bypass -File 06-simulation/bin/install_sim_task.ps1` (add `-At 05:00` to move it, `-Remove` to unregister). **Dry run:** `powershell -ExecutionPolicy Bypass -File 06-simulation/bin/run_sim_night.ps1 -NoAgent` builds and checks the prompt without invoking Claude.

**History.** The task was first registered 2026-09-15. On 2026-10-14 the run moved to a Claude Code cloud Routine for one night and came back the same day: the cloud clone could not see the live index or `data/`, and its branches on the public mirror had to be cherry-picked into the private project by hand before every sync. The Routine is paused, not deleted.

---

## Open questions we are handing to outsiders — [`sim-briefs/`](sim-briefs/README.md)

**Six simulations nobody has run, written up so a stranger can evaluate the method and reproduce the result without asking us for anything.**

> **Each brief states our prediction and the number that would refute us, both fixed before anybody runs it.** The reason is a rule a critic gave this project: **a check whose passing condition is set by the checker is not an instrument, and it fails toward flattery.**

| Brief | The question, short |
|---|---|
| [SB-01](sim-briefs/SB-01_ceiling-challenge.md) | Can anything push the credit-disparity statistic **up** without breaking the 24-hour cap? |
| [SB-02](sim-briefs/SB-02_rho-star-rubric.md) | Is the clearing rate **ρ\*** an instrument, or is it blind like `24 ÷ F` turned out to be? |
| [SB-03](sim-briefs/SB-03_reweighting-cost.md) | What does a **full re-weighting** of a billion-event log cost in time and memory? **Needs a machine, not a theory** |
| [SB-04](sim-briefs/SB-04_honest-label.md) | Does labelling a figure **metered** or **modelled** pay, or does it hand rivals a target? |
| [SB-05](sim-briefs/SB-05_parcel-identity.md) | What happens to the books when a flow sheet **cannot tell one parcel from two**? |
| [SB-06](sim-briefs/SB-06_resolution-tax.md) | How much dearer does a small producer's product read **because they cannot afford instruments**? |

**In plain words: these are the questions where our own answer would not be worth much, because we would be marking our own work.** [`sim-briefs/README.md`](sim-briefs/README.md) says what a brief contains and why.

## The headline numbers, in one place

| Number | What it is | Project |
|---|---|---|
| **`24 / F`** | The most anyone can consume against bare subsistence, where `F` is the network's self-care floor in hours a day. **`F` is a network's own choice, so there is no single number here** — at a 10-hour floor the form gives 2.4, at a 2-hour floor it gives 12. **Quote the form, never the example.** Under money the same ratio runs to ~10⁶×. | disparity-ceiling |
| **≈ 1,380 h/yr** | What a median US adult's yearly consumption costs in human labour — about **one third** of the 3,650 h/yr everyone earns just by being alive. | median-lifestyle |
| **ρ\* = 1.20** | The consumption gate that clears the market. The median then gets 0.92× a full lifestyle; 35% are held below their wants. | disparity-ceiling |
| **709 vs 1,283 h** | Spain against the US, for a comparable material life — and Spaniards live nearly six years longer. | median-lifestyle |
| **the band closes at `F` = 2** | With demand tied to the 1,380 h/yr anchor, at the US method: the band is open at 10 and 14 h/day, and at 2 h/day it is open on the narrow essentials basket and **closed on the broad one**. The tightest floor carries **0.54×** a median lifestyle. Capacity binds the upper edge. | stable-band |
| **a two-way split is worth exactly 2.00×** | Credit duplicates across networks; debit divides. **No estimate closes it at any ratio**, and the splitter's signature is not low consumption but **a record pinned at the cap on every network** — which is the shape every cohort rule is aimed away from. | cross-network-splitting |
| **10.2 million events/s** | A 10⁹-event log re-checks against IC-1…IC-9 in **1.6 minutes on one core**, holding 11.4 MB. **A stranger can afford to re-compute a network's arithmetic.** And **IC-5 is the one check that does not stream** — it compares one event to another, so it needs the log ordered by parcel. | ic-recompute-cost |
| **coverage overstated at every ρ** | When the outside total shares the network's blind spot, `N − Y` comes out **below** the truth — the flattering direction. **At full correlation the leftover reads zero and the network publishes 100% coverage.** Row 14a's interval cannot express it; row 13's `not identified` default is what refuses the claim. | correlated-miss |
| **1 of 3, and the pass is free** | Scored on a detection rubric, the fraud row fails sensitivity, passes specificity **because it never moves**, and cannot be scored on coverage at all. **Its expressiveness is one-sided**: a maximum can be pushed down by deletion and never up, because IC-7 caps the top — so every fraud that pays is invisible to it. **The bound `24/F` is unaffected; the corroboration is what fails.** ⛔ **Void as evidence since 2026-09-23**: measured on a population Foundations §5.5.5 says cannot exist. | ceiling-rubric |
| **+0.000, −0.109, +0.019** | The correlation between what each proposed allocation rule charges a subscriber and what that subscriber actually held back. **A witness would score near 1.** R2 is negative — worse than charging at random — because it bills in proportion to what was recorded, and the hider recorded less. **57% of the leftover is uncharge-able by construction.** | residual-attribution |
| **1.73× and it never converges** | A producer on two networks stays in the leftover and leaves the denominator, so the estimate charged to a producer who joined **nothing** reaches 1.73× what they made. **Onboard the whole region and the arithmetic reaches `R ÷ 0`** with 35,484 t unassigned. **And two worlds give one network identical books with truths 21% apart** — no one-book rule can separate them. | producer-side-splitting |
| **2.5% trapped, and it clears** | Dark producers over-charged by the estimate **and unable to afford proof** peak at 2.50% of the population and fall to zero. **Under the rule the axioms reject, the same class never clears.** | residual-unravelling |
| **0.1% vs 52.5%** | How much stays unmeasured under the residual rule, against the population rule the axioms reject. | residual-unravelling |
| **~95%** | Share of economies where the rival value/price allocation goes negative. The physical allocation never does. | allocation-engine |
| **12 of 12** | Integrity constraints that pass clean and catch their injected violation. | audits |
| **coarse ≥ fine, always** | A product carries the steps it passed through ÷ its own mass. **Those steps are a subset of all the steps, so a coarser reading can only charge more** — confirmed on 1,152 product-resolution pairs, equality only for a product that passes the whole chain. **A hide read at one link carries 12.5 MJ/kg and at seven links carries 2.0.** So a producer wanting a lower figure must buy more measurement. | chain-resolution |
| **union 1 value, sum 111** | Across 128 readings of one refinery, the **union over identified parcels** returns the chain total every time; a **naive sum** returns 111 different answers and overstates by up to **7.00×**. **A3 is why: a debit is a unique record, not an amount.** | chain-resolution |

Each project's `RESULTS.md` carries the conditions, the limits, and what would falsify the figure. **No number above should be quoted without them.**

---

## How this directory is organised

**One folder per coding project. Nothing loose at the top level except this page, the plain-language tour, and shared data.**

```
06-simulation/
  README.md                    <- this page
  Simulations_in_Plain_Language.md
  data/                        <- SHARED. See below.
  <project>/
    README.md                  <- what it is, how to run it, current status
    RESULTS.md                 <- the numbers, so re-running is unnecessary
    CHANGELOG.md               <- dated entries, newest first
    archive/                   <- superseded scripts, docs and figures (only where there are any)
    <the code, its data, its figures, its write-ups>
```

**Four rules that keep it from decaying:**

1. **A new sim gets a folder, not a loose file.** If it is too small for a folder, it belongs inside an existing project.
2. **Change history goes in `CHANGELOG.md`, not in a comment block at the top of a script.** Comments explain how the code works now. If a comment is explaining what used to be true, it is in the wrong file.
3. **`RESULTS.md` is the memory.** Anything worth knowing after the run finishes goes there — the headline, the conditions, the limits, and where the figures are. If someone has to re-run a sim to answer a question, that file failed.
4. **Nothing is deleted.** Superseded work moves to that project's `archive/`, keeping its name.

### Two things stay at the top level

**`data/` is shared and stays here. It is 288 MB and is deliberately not published**, so the links below go to the original sources instead. It holds the **[Bureau of Labor Statistics Employment Requirements matrices](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm)**, the **[BLS input-output tables](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm)**, and the 234 MB **[EXIOBASE](https://www.exiobase.eu/)** multi-region table. **Anyone can rebuild it from those three sources.** `median-lifestyle/` uses them today and any successor kernel will need the same tables, so duplicating them would be wrong and moving them into one project would be misleading. **Scripts reach up one level to find it.**

> **⚠️ The Bureau of Labor Statistics withdrew the Employment Requirements matrices on 2026-02-06.** The copies in `data/erm_full/` came back through the [Internet Archive](https://web.archive.org/) and are the only ones we have. **Do not delete them.**

**[`Simulations_in_Plain_Language.md`](Simulations_in_Plain_Language.md) stays here** because it spans every project. It belongs to no one of them.

`scenarios/` moved into `statera/`, because only the scenario runner reads it.

---

## Where to start, depending on why you came

| You want to | Go to |
|---|---|
| Understand what any of this proves, without maths | [`Simulations_in_Plain_Language.md`](Simulations_in_Plain_Language.md) |
| Understand the consumption gate | [`stable-band/gate.py`](stable-band/gate.py) |
| Check a number before quoting it | that project's `RESULTS.md` |
| Check a claim **without running our code** | [`audits/audits_inert/`](audits/audits_inert/README.md) |
| Know what the whole programme is for | [`../00-strategy/Aequitas_Simulation_Roadmap.md`](../00-strategy/Aequitas_Simulation_Roadmap.md) |
| Know what happens next | `../NEXT.md` (held locally) |

## What this code is, and is not

> **Aequitas the system is the deliverable. Code is how it gets tested.**

The code here is **a simulator of an economy** — not a trust-network database, and not a first version of Aequitas. The moment it starts being treated as a product, the project has drifted out of scope.

**What the whole programme is for:** find the thresholds, conditions and variables that lead to Aequitas being adopted — how fast, how slowly, or where it fails critically. The conformance checks and the disparity ceiling are **instrument checks**: they prove the machine measures what it claims. They are not the object of study.

> **A mix that fails is a result. A sweep that finds no failing mix has not been run hard enough.**

## Running anything

Python 3.11 or later (3.14 here). Packages used across the folder: `numpy`, `scipy`, `matplotlib`, `openpyxl`, `pymrio`, and `tomllib` from the standard library.

**Every self-test runs without any downloaded data.** Only the full EXIOBASE runs in `median-lifestyle/` need the large table, and those cache their answers in checked-in JSON files so the tests read the cache instead.

## ic-recompute-cost · re-weighting ratio (2026-09-12)
**What a re-weighting pass costs against a record-check pass, off one generator on one machine.** Answers `sr-20260912-...` and the duplicate `sr-20260901-wall-clock-and-memory-cost-of-a-full-re-weig`. **Ratio 0.345 at 10⁹ events; the project's published 1×–5× prior was wrong and on the wrong side of 1.0.** @hemei's outside 0.27 reproduces once both sides say whether IC-5's sort is in the denominator.
`python reweight_ratio.py --full` · [`ic-recompute-cost/REWEIGHT_RATIO_RESULTS.md`](ic-recompute-cost/REWEIGHT_RATIO_RESULTS.md)

## mirror-link-audit (2026-09-12)
**How many links in the PUBLISHED documents a reader cannot follow.** Answers `sr-20260907-...` from @amber. **18 of 1,270, 1.42% — four of them in Foundations §6's own directory table.** Not the same check as `bin/consistency.py`, which resolves against the working tree and passes.
`python mirror_link_audit.py` · [`mirror-link-audit/RESULTS.md`](mirror-link-audit/RESULTS.md)

## axiom-reachability (2026-09-12)
**Walks the pointer graph from the eight axioms and counts which conformance rows a reader arrives at.** Answers `sr-20260908-...` from @amber. **A8's v0.43 repair is confirmed; under the stricter reading 10 of 44 rows are named from a reached section.** Entry point and edge types declared before the run, per @amber's own objection to the method.
`python axiom_reachability.py` · [`axiom-reachability/RESULTS.md`](axiom-reachability/RESULTS.md)

## objection-answer-location (2026-10-22)
**For each outside finding in the objections register, where its answer lived: the section the critic named, elsewhere but reached by a search from the critic's words, or not reached.** Answers `sr-20260906-over-the-project-s-own-objection-register-cl`, run by the nightly agent. **28 findings; 15 had an earlier answer; of 13 testable, 3 / 2 / 8 (line arm) or 3 / 5 / 5 (section arm).** By hand only 0 to 1 of the misses is a framing line. No whole-read arm, so it does not test the #4088 claim.
`python answer_location.py --test` · `python answer_location.py` · [`objection-answer-location/RESULTS.md`](objection-answer-location/RESULTS.md)

## ceiling-challenge (2026-10-14)
**Can anything push `max(claimed credit) ÷ F` above `24 ÷ F` without a record over 24 hours?** Answers `sr-20260901-construct-a-challenge-that-pushes-max-claime` (SB-01), run by the nightly agent. **The arithmetic space is empty — a rate is a mean of per-day values in `[F, 24]` — and the evaluation space has exactly four doors**, one per premise an implementation evaluates: a per-record cap check reaches 3.80 at `F` = 10 with two overlapping filings, a declared-span denominator reaches 3.00 with no cap breach at all, a local-calendar denominator reaches 2.4003, measured self-care reaches 3.00 on `max ÷ min`. Restore the setting and every row returns to 2.400; 20,000 adversarial trials under the conforming evaluator never crossed it. The construction needing no cap breach is stopped by §4.4's span rule, which §5.5.5's five conditions do not name.
`python ceiling_challenge.py --test` · `python ceiling_challenge.py` · [`ceiling-challenge/RESULTS.md`](ceiling-challenge/RESULTS.md)

## honest-label (2026-10-17)
**Does labelling a published figure metered or modelled pay, or does it show rivals where to aim?** Answers `sr-20260904-does-a-producer-who-labels-each-published-fi` (SB-04), run by the nightly agent. **Stable once most producers label, but not self-starting:** the break-even discount to drop the label is 0.0256 (prior 0.024), while a lone labeller holds 3.60% of trade against its rivals' 5.02% and needs a discount of 0.62 to break even, rising with the number of rivals. The brief's worked example loses about two thirds of its labelling edge (4.2 to 1.5 points) when attack gains go back to the attacker.
`python labelling_game.py --test` · `python labelling_game.py` · [`honest-label/RESULTS.md`](honest-label/RESULTS.md)

## parcel-identity (2026-10-18)
**What the books do when a flow sheet cannot say whether two readings name one parcel or two.** Answers `sr-20260905-how-often-does-a-joint-process-flow-sheet-fa` (SB-05), run by the nightly agent. **On the refinery, a buyer holding all 7 co-products reads 1.26× the truth at an unresolved rate of 0.10 and 2.33× at 0.50, against 3.63× for the naive sum.** Refusing to publish never touches a single co-product's figure, refuses 15% of two-co-product holdings and 77% of the full holding at 0.10. The rate itself is swept, not measured. One declared cell failed: the twin crossover is 0.58, not 0.15 to 0.45.
`python parcel_identity.py --test` · `python parcel_identity.py` · [`parcel-identity/RESULTS.md`](parcel-identity/RESULTS.md)
