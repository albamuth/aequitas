<!-- tag: simroadmap-v0-1 -->
# Aequitas — Simulation Roadmap

> **Version:** 0.1
> **Date:** 2026-08-23
> **Status:** New. Author ruling, 2026-08-23.
> **Companions:** `Aequitas_Foundations_v0.18.md` §1.2/§9 (scope), `Aequitas_Strategy_v0.5.md` §2 (sims are evidence), `06-simulation/scenario_suite_METHOD.md` (the five existing societal sims).

---

## 0. The ruling

> **Aequitas the system is the deliverable. Code is how it gets tested.**
>
> **The code to build is a simulator of an economy — one or several — not a trust-network database.**

This finishes the scope fold of the same day. Foundations §1.2 and §9 said what the *documents* are for. **This says what the *code* is for**, which nothing said before.

**A simulator is in scope for the same reason a schema is not.** Apply §1.2's dial test: *if a principle survives at both ends of a dial, the dial is not part of the principle.* A simulation is not a dial at all. **It is the instrument that tells you whether a principle survives anything.** Every claim this project makes that sounds impossible is a claim a simulation can either support or kill.

---

## 1. What exists today

Real work, and more of it than the gap list suggests.

| Area | Built | What it answers |
|---|---|---|
| **The disparity ceiling** | `disparity_ceiling_sim.py` (N = 200,000), `q4_locked_ledgers.py` | `24/F` is exact, ρ-independent, fraud-invariant. Only ~0.1–2% of Americans sit past a permanent lockout. |
| **The ρ dial** | `rho_sweep.py` | A pickable ρ clears the market at ≈1.2. Moves in the intuitive direction under shocks. |
| **Cost of a median life** | `median_lifestyle.py` + Tracks 1–4 | ≈1,380 h/yr against ≈3,650 h/yr of self-care credit. |
| **Efficiency spread** | `track6_*.py`, `Q6.md` | The US commands 50–80% more embodied labour and 2.5–4× the CO₂ per person than Germany, Sweden, France, Japan, Spain. |
| **Societal feasibility** | `q1_autarky.py`, `q2_capture.py`, `q5_reallocation.py`, `plastic_debt.py` | Labour is abundant; materials and energy bind. |
| **Allocation converges** | `recursion_convergence.py` (5,224 runs) | Non-negative Neumann series; Sraffa and Steedman blocked by construction. |
| **Coverage closes** | `residual_unravelling.py` | Residual basis leaves 0.1% dark; population basis stalls at 52.5%. |
| **Pledge reserve** | `pledge_reserve.py` | Hazardous work clears at coverage ≈ cover-the-tail. |
| **Record integrity** | `arithmetic_audits.py` | IC-1 … IC-12 runnable. **Conformance-boundary work, not system work** (Strategy §3). |

---

## 2. The eight scenarios, mapped

| # | Scenario the author asked for | State | What is actually missing |
|---|---|---|---|
| 1 | **Aequitas starts in one locality and competes with money. Does it spread?** | 🔴 **Nothing** | Everything. No model of adoption, of a boundary between two economies, or of what a participant gains by joining while most people have not. |
| 2 | **Different floor numbers `F`** | 🟠 **Partial** | `F` is fixed at 10 h everywhere. **`24/F` is proved but never swept.** No model of networks choosing *different* floors, which is OP-14 floor-shopping. |
| 3 | **Worldwide, with only the gift economy as the alternative** | 🟠 **Partial** | Q1 and Q5 assume Aequitas is already everywhere. Nothing models the alternative being *nothing*, or what that does to the pull toward the records. |
| 4 | **World carbon under Aequitas vs current trends** | 🟠 **Partial** | Q6 and `track4_carbon_intensity.py` give carbon *per person, per country, today*. **There is no trajectory** — no "emissions under Aequitas vs business-as-usual over N years." |
| 5 | **Disaster or infrastructure collapse** | 🟠 **Partial** | `rho_sweep.py` re-clears once at −30% budget → ρ* = 0.68. That is a snapshot of a damaged world, **not a collapse and a recovery.** |
| 6 | **Population booms and declines** | 🟠 **Partial** | One data point: −15% population barely moves ρ*. No boom. No trajectory. |
| 7 | **A pollutant discovered that was never accounted** | 🟠 **Partial** | `rho_sweep.py` applies a +25% debit re-weight as an input. **The discovery event itself is not modelled**, and §3.3 retroactive re-weighting is component **C4, still not started.** |
| 8 | Anything else that stress-tests the system | — | See §5. |

---

## 3. The structural finding

> **Five of the eight need a time axis. Not one existing simulation has one.**

Scenarios 1, 4, 5, 6 and 7 are all questions about **what happens over time**: does adoption spread, does carbon fall, does a society recover, does a population shift bite, does a re-weighting propagate.

**Every societal sim in `06-simulation/` is a single-period model.** `rho_sweep.py` says so in its own honest-limits section: *"Static one-period clearing; no dynamics/expectations. A multi-period version is a later refinement."* The shared engine behind Q1, Q2 and Q5 is an input-output feasibility envelope — it computes what is possible at one moment, never what unfolds.

**So the gap is not eight more scripts. It is one missing capability, and then most of these are scenarios on top of it.**

**Worked example of the difference.** `rho_sweep.py` says a −30% capacity disaster gives ρ* = 0.68, and the median person still gets 0.62 of their desired lifestyle. That is a true and useful statement about **a world already 30% poorer**. It cannot tell you the thing anyone actually wants to know: *in month three, is the region eating?* For that you need periods, a stock that draws down, credit accruing at the floor while production is halved, and the ratio gate re-checked each period. **None of that machinery exists.**

---

## 4. Proposed build order

**Cheapest first, and each one finishes in a sitting or two.**

### Step 1 — Sweep the floor `F` *(smallest, hardens the headline)*

**Why first:** Foundations §7.5 states the disparity ceiling as **conditional**, and condition 1 is *"the floor stays in a narrow band."* A 10 h floor gives 2.4×. **A 2 h floor gives 12×.** That sentence is in the document with no evidence behind it.

Extend `disparity_ceiling_sim.py` to sweep `F` from 2 h to 14 h, and add a second population where networks pick *different* floors and trade. **Output: the shape of the ceiling as floors vary, and whether OP-14 floor-shopping actually bites.** Serves OP-4 and OP-14 directly.

### Step 2 — The adoption sim *(scenario 1, and it builds the time axis)*

**Do not build "a dynamics engine" in the abstract.** Build the adoption question, which forces periods into existence, and let the other four dynamic scenarios ride the spine it creates.

Two economies side by side, one on money and one on Aequitas, with agents who may join, leave, or trade across the boundary each period. **The joining incentive is already computed and is the thing to test:** §5.1d says onboarding is a windfall for a median person — roughly 146,000 hours of estimated credit against 55,000 hours of estimated consumption at age forty. **Does that pull enough people, fast enough, to reach a working density?**

**It has a validation target, which is rare.** WIR has run since 1934 with ~60,000 businesses; Sardex reached 4,000+; Ithaca HOURS died when its founder left. A model that cannot reproduce those three outcomes is wrong.

### Step 3 — Ride the spine

Once periods exist, four scenarios are configurations rather than new engines:

| Scenario | What it becomes |
|---|---|
| **Collapse and recovery** (5) | Cut the physical budget at period *t*, run forward, watch the floor and the ratio gate. |
| **Population boom and decline** (6) | Vary the agent count over periods, both directions. |
| **Carbon trajectory** (4) | Run the Q6 efficiency finding forward against a business-as-usual arm. |
| **Pollutant discovery** (7) | Inject a re-weight at period *t* and let §3.3 propagate it backwards through history while the transaction-time rule protects completed acts. **This one doubles as the first test of component C4.** |

### Step 4 — Gift economy as the only alternative *(scenario 3)*

The adoption sim with the money arm removed. Cheapest once step 2 exists.

---

## 5. Candidates the author did not list, worth considering

| Candidate | Why |
|---|---|
| **OP-10 under adversaries** | The **top blocker.** Can a coalition capture the weighting model when publication and replication are the only guards, and the consuming side of every market outnumbers the producing side? This is the current task and it has no sim. |
| **OP-16, the boring-work gap** | Nothing allocates labour to tedious necessary jobs. Test the hour-ceiling candidate: does paying the premium in time off actually staff the job? |
| **OP-6, feedback flooding** | Does cheap abundant signalling degrade into a popularity contest? |
| **The verification-cost cliff** | `residual_unravelling.py` found darkness becomes stable once verification costs ~40% of a median unit's debit. **That number decides whether coverage works at all**, and it rests on one sim. |

---

## 6. What this means for the outreach agent

**Its asks change.** Until now it invited strangers to run record-integrity checks, and it got a record-integrity audience — post #1750 drew six replies, and **every one was about truncation, hashes and witnesses. None was about the economy.**

> **What to ask for from here: run, extend, or attack a simulation of the economy.**

Three are runnable and finished today: the **`24/F` disparity ceiling**, the **≈1,380 h/yr** median-lifestyle anchor, and the **Q6 efficiency spread**. Each is an economics claim with a script behind it, which is exactly the currency that board trades in. **The board rewards runnable artifacts — so give it a runnable artifact about the economy.**

---

## 7. What is still not in scope

Unchanged by this document, and worth restating because a simulator is the kind of thing that grows:

- **A trust-network database.** Not ours (§1.2).
- **A production implementation of anything.** A simulator is an instrument for testing the theory, **not a first version of the system.**
- **Anything whose result depends on a design choice rather than a principle.** Apply the dial test before adding a scenario.
