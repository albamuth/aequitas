# 06-simulation — the code, and what it found

> **You should be able to read this page and know where everything is without opening anything else.**
> New here, and want the tour rather than the index? Read [`Simulations_in_Plain_Language.md`](Simulations_in_Plain_Language.md) — a sceptic's walk through every sim, asking of each one *could this have failed?*

---

## The projects

Every command below is run **from inside that project's folder**. Every project has a `README.md` (what it is), a `RESULTS.md` (the numbers, so you need not re-run), and a `CHANGELOG.md` (when and why it changed).

| Project | What it answers | Run it | Status |
|---|---|---|---|
| **[`statera/`](statera/README.md)** | The kernel. One engine every future scenario runs on: agents, an append-only event log, the debit vector, credit accrual, the ratio gate, the conformance checks. | `python statera.py --test` | 🟢 **Live. This is the current work.** Steps 1–4 done; step 5 blocked on a data download. |
| **[`disparity-ceiling/`](disparity-ceiling/README.md)** | How far apart can two people's consumption get? And where should the consumption dial ρ sit? **Plus the negative controls: can the reported statistic express a violation at all?** | `python disparity_ceiling_sim.py --test`<br>`python rho_sweep.py --test`<br>`python ceiling_negative_controls.py` | ✅ Stated, simulated, stress-tested. A **conditional** result. |
| **[`median-lifestyle/`](median-lifestyle/README.md)** | What does a normal life cost, in hours of human labour? Four measured tracks plus a cross-country comparison. | `python track1_embodied_hours.py --test`<br>(one script per track) | ✅ Done. **The project's real-world anchor.** |
| **[`allocation-engine/`](allocation-engine/README.md)** | Does the cost recursion converge, and is every share non-negative? Then: per-product costs from a real economy, and a refinery where physical and price allocation disagree. | `python recursion_convergence.py --test`<br>`python estimation_engine.py --test`<br>`python refinery_slice.py --test` | ✅ Done. Closed the project's sharpest technical risk. |
| **[`audits/`](audits/README.md)** | The twelve event-log integrity constraints, made runnable — and each one shown to actually fire. | `python arithmetic_audits.py --test` | ✅ Closed. Plus `audits_inert/`, the same audits **as data**, checkable without running code. |
| **[`scenario-suite/`](scenario-suite/README.md)** | Five societal questions: autarky, captured labour, plastic, who is locked out, wasteful-to-essential reallocation. | `python q1_autarky.py --test`<br>(one script per question) | ✅ Answers stand. **Machinery superseded** by `statera/`. |
| **[`residual-unravelling/`](residual-unravelling/README.md)** | Does staying unmeasured stop paying? Tests the rule that cohort estimates are computed over the residual, never the population. | `python residual_unravelling.py --test` | ✅ Passes, with one measured limit. |
| **[`pledge-reserve/`](pledge-reserve/README.md)** | Why would anyone take the hazardous job in a system with no wage premium? | `python pledge_reserve.py --test` | ✅ Built. Answers the hazard half of the onerousness gap. |
| **[`stable-band/`](stable-band/README.md)** | Is there a band of the floor `F` and the tolerance ρ inside which essentials stay affordable **and** the ledger still rations? | `python stable_band.py --test` | ✅ **Done 2026-08-28.** Answers the simulation Foundations §5.5.3 says it owes. |
| **[`cross-network-splitting/`](cross-network-splitting/README.md)** | Can a person split their consumption across two trust networks to keep each book's figure low, and does the residual estimate catch them? | `python cross_network_splitting.py --test` | ✅ **Done 2026-08-28.** Answers @cairn-lineage's open half. Registered with **OP-22**. |
| **[`correlated-miss/`](correlated-miss/README.md)** | How far does `R = N − Y` move when the outside total and the network's own books share a blind spot? | `python correlated_miss.py --test` | ✅ **Done 2026-08-29.** Answers @cairn-lineage c21187. **OP-26**, **OP-24**. |
| **[`ic-recompute-cost/`](ic-recompute-cost/README.md)** | What does it cost a stranger to re-run IC-1 to IC-9 over a real-economy-sized event log? | `python ic_recompute_cost.py --test` | ✅ **Done 2026-08-29.** Answers the Futurist lens, 2026-08-22. |
| **[`producer-side-splitting/`](producer-side-splitting/README.md)** | One producer routes output through two networks and leaves both networks' `Z`. What does that do to the leftover estimate, and can either network see it from its own books? | `python producer_side_splitting.py --test` | ✅ **Done 2026-08-31.** Answers @cairn-lineage c27820. Registered with **OP-28**. |
| **[`residual-attribution/`](residual-attribution/README.md)** | Three rules have been proposed for assigning the leftover `N − Y` to people instead of holding it. Are any of them witnesses, or are they all guesses? | `python residual_attribution.py --test` | ✅ **Done 2026-08-31.** Answers @cairn-lineage c30285. Foundations **§4.4**. |
| **[`ceiling-rubric/`](ceiling-rubric/README.md)** | Score our own headline statistic as a detector: does it fire on a known omission, stay quiet on a clean case, and what witnesses that the tested population is complete? | `python ceiling_rubric.py --test` | ✅ **Done 2026-08-31.** Answers @cairn-lineage c33046. Foundations **§5.5.7**, **§4.3**. |

## The headline numbers, in one place

| Number | What it is | Project |
|---|---|---|
| **2.40×** | The most anyone can consume against bare subsistence, at a 10-hour self-care floor. Under money the same ratio runs to ~10⁶×. | disparity-ceiling |
| **≈ 1,380 h/yr** | What a median US adult's yearly consumption costs in human labour — about **one third** of the 3,650 h/yr everyone earns just by being alive. | median-lifestyle |
| **ρ\* = 1.20** | The consumption gate that clears the market. The median then gets 0.92× a full lifestyle; 35% are held below their wants. | disparity-ceiling |
| **20,000 phantoms move it by 0.00** | The negative controls on our own headline statistic. **Truncate the log or splice a 40 h/day cheater and it fires. Pad the population with people who never existed and it does not.** The blindness is specific: it sees insertion and truncation, never padding. | disparity-ceiling |
| **709 vs 1,283 h** | Spain against the US, for a comparable material life — and Spaniards live nearly six years longer. | median-lifestyle |
| **the band never closes** | A workable pair of `F` and ρ exists at every floor from 1 to 14 h/day. **Capacity binds, not affordability** — even the tightest floor carries an essentials basket costing almost twice a median lifestyle. | stable-band |
| **a two-way split is worth exactly 2.00×** | Credit duplicates across networks; debit divides. **No estimate closes it at any ratio**, and the splitter's signature is not low consumption but **a record pinned at the cap on every network** — which is the shape every cohort rule is aimed away from. | cross-network-splitting |
| **10.2 million events/s** | A 10⁹-event log re-checks against IC-1…IC-9 in **1.6 minutes on one core**, holding 11.4 MB. **A stranger can afford to re-compute a network's arithmetic.** And **IC-5 is the one check that does not stream** — it compares one event to another, so it needs the log ordered by parcel. | ic-recompute-cost |
| **coverage overstated at every ρ** | When the outside total shares the network's blind spot, `N − Y` comes out **below** the truth — the flattering direction. **At full correlation the leftover reads zero and the network publishes 100% coverage.** Row 14a's interval cannot express it; row 13's `not identified` default is what refuses the claim. | correlated-miss |
| **1 of 3, and the pass is free** | Scored on a detection rubric, the fraud row fails sensitivity, passes specificity **because it never moves**, and cannot be scored on coverage at all. **Its expressiveness is one-sided**: a maximum can be pushed down by deletion and never up, because IC-7 caps the top — so every fraud that pays is invisible to it. **The bound `24/F` is unaffected; the corroboration is what fails.** | ceiling-rubric |
| **+0.000, −0.109, +0.019** | The correlation between what each proposed allocation rule charges a subscriber and what that subscriber actually held back. **A witness would score near 1.** R2 is negative — worse than charging at random — because it bills in proportion to what was recorded, and the hider recorded less. **57% of the leftover is uncharge-able by construction.** | residual-attribution |
| **1.73× and it never converges** | A producer on two networks stays in the leftover and leaves the denominator, so the estimate charged to a producer who joined **nothing** reaches 1.73× what they made. **Onboard the whole region and the arithmetic reaches `R ÷ 0`** with 35,484 t unassigned. **And two worlds give one network identical books with truths 21% apart** — no one-book rule can separate them. | producer-side-splitting |
| **2.5% trapped, and it clears** | Dark producers over-charged by the estimate **and unable to afford proof** peak at 2.50% of the population and fall to zero. **Under the rule the axioms reject, the same class never clears.** | residual-unravelling |
| **0.1% vs 52.5%** | How much stays unmeasured under the residual rule, against the population rule the axioms reject. | residual-unravelling |
| **~95%** | Share of economies where the rival value/price allocation goes negative. The physical allocation never does. | allocation-engine |
| **12 of 12** | Integrity constraints that pass clean and catch their injected violation. | audits |

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

**`data/` is shared and stays here. It is 288 MB and is deliberately not published**, so the links below go to the original sources instead. It holds the **[Bureau of Labor Statistics Employment Requirements matrices](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm)**, the **[BLS input-output tables](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm)**, and the 234 MB **[EXIOBASE](https://www.exiobase.eu/)** multi-region table. **Anyone can rebuild it from those three sources.** `median-lifestyle/` uses them today and `statera/` will need the same tables at step 5, so duplicating them would be wrong and moving them into one project would be misleading. **Scripts reach up one level to find it.**

> **⚠️ The Bureau of Labor Statistics withdrew the Employment Requirements matrices on 2026-02-06.** The copies in `data/erm_full/` came back through the [Internet Archive](https://web.archive.org/) and are the only ones we have. **Do not delete them.**

**[`Simulations_in_Plain_Language.md`](Simulations_in_Plain_Language.md) stays here** because it spans every project. It belongs to no one of them.

`scenarios/` moved into `statera/`, because only the scenario runner reads it.

---

## Where to start, depending on why you came

| You want to | Go to |
|---|---|
| Understand what any of this proves, without maths | [`Simulations_in_Plain_Language.md`](Simulations_in_Plain_Language.md) |
| Work on the current task | [`statera/README.md`](statera/README.md) |
| Check a number before quoting it | that project's `RESULTS.md` |
| Check a claim **without running our code** | [`audits/audits_inert/`](audits/audits_inert/README.md) |
| Know what the whole programme is for | [`../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md`](../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md) |
| Know what happens next | `../NEXT.md` (held locally) |

## What this code is, and is not

> **Aequitas the system is the deliverable. Code is how it gets tested.**

The code here is **a simulator of an economy** — not a trust-network database, and not a first version of Aequitas. The moment it starts being treated as a product, the project has drifted out of scope.

**What the whole programme is for:** find the thresholds, conditions and variables that lead to Aequitas being adopted — how fast, how slowly, or where it fails critically. The conformance checks and the disparity ceiling are **instrument checks**: they prove the machine measures what it claims. They are not the object of study.

> **A mix that fails is a result. A sweep that finds no failing mix has not been run hard enough.**

## Running anything

Python 3.11 or later (3.14 here). Packages used across the folder: `numpy`, `scipy`, `matplotlib`, `openpyxl`, `pymrio`, and `tomllib` from the standard library.

**Every self-test runs without any downloaded data.** Only the full EXIOBASE runs in `median-lifestyle/` need the large table, and those cache their answers in checked-in JSON files so the tests read the cache instead.
