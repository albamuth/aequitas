# Statera — the Aequitas simulation kernel

**A technical reference for the instrument.**

> **Version:** 0.1 · **Date:** 2026-08-23
> **Describes:** [`statera.py`](statera.py), 1,185 lines, 22 self-tests.
> **Tracks:** [`../../00-strategy/Aequitas_Foundations_v0.19.md`](../../99-archive/Aequitas_Foundations_v0.19.md).
> **Run:** `python statera.py --test` · `python statera.py --demo`
> **Change history:** [`STATERA_CHANGELOG.md`](CHANGELOG.md). No version notes appear in this document's body.

**Every number in this paper was read off a run made on 2026-08-23, not copied from another document.** Where a run and a document disagree, §9 says so and gives both.

---

## Contents

- [1. What Statera is](#1-what-statera-is)
- [2. What the programme is for](#2-what-the-programme-is-for)
- [3. What the kernel holds](#3-what-the-kernel-holds)
- [4. Credit accrual and the self-care floor](#4-credit-accrual-and-the-self-care-floor)
- [5. The debit vector, and collapsing it](#5-the-debit-vector-and-collapsing-it)
- [6. Divide per dimension, before collapsing](#6-divide-per-dimension-before-collapsing)
- [7. The ratio gate](#7-the-ratio-gate)
- [8. The disparity bound 24/F, derived](#8-the-disparity-bound-24f-derived)
- [9. The age term](#9-the-age-term)
- [10. Cohorts — one row, many people](#10-cohorts--one-row-many-people)
- [11. Conservation of mass and energy](#11-conservation-of-mass-and-energy)
- [12. The 24-hour cap, scaled to the period](#12-the-24-hour-cap-scaled-to-the-period)
- [13. Pledge backing](#13-pledge-backing)
- [14. The residual rule — stated, not built](#14-the-residual-rule--stated-not-built)
- [15. Dollars into hours](#15-dollars-into-hours)
- [16. The clearing rate](#16-the-clearing-rate)
- [17. What a run prints](#17-what-a-run-prints)
- [18. Where the code and the documents disagree](#18-where-the-code-and-the-documents-disagree)
- [19. Honest limits](#19-honest-limits)
- [20. Sources](#20-sources)

---

## 1. What Statera is

**Statera is an instrument. It measures a theory against scenarios.**

A *statera* is the balance-scale the goddess Aequitas holds on Roman coinage. The name was chosen on 2026-08-23 for exactly that reason: **you measure a thing with a balance, and the balance is never the thing.**

| Statera **is** | Statera **is not** |
|---|---|
| One shared engine every scenario runs on | A trust-network database |
| A way to test whether a mechanism in the theory survives contact with a population | A first version of Aequitas |
| A thing that can fail, and reports failure as a result | A demonstration, a product, or a protocol |

The distinction comes from Foundations §1.2 — the scope section, which rules that Aequitas is a set of principles about how cost is accounted for, and that software, storage and protocol are the implementer's business. **A simulation kernel that starts being treated as a prototype ledger has breached that scope.**

Statera exists because nothing else in `06-simulation/` was the kernel. Every prior script wrote its own credit accrual, its own gate, and its own agents. That is why each answers one question and none of them join up.

---

## 2. What the programme is for

> **We are looking for the thresholds, conditions and variables that lead to Aequitas being adopted — how fast, how slow, or where it fails critically.**
> — the author, 2026-08-23

**This re-aims everything below.**

- The conformance checks are **instrument checks**. They show the machine measures what it claims.
- The disparity bound `24/F` is an **instrument check**. Re-deriving it for the twelfth time teaches nothing.
- **The object of study is adoption.** Which starting populations catch. Which stall. What the critical mass is. Where the whole thing dies.

**A scenario earns its place by bearing on adoption.** A run that finds a population Aequitas cannot carry teaches more than a run that confirms a bound.

Adoption is generational. [`Onboarding_the_wealthy_v0.1.md`](../../00-strategy/Onboarding_the_wealthy_v0.1.md) works on a **70-to-170-year** timescale, because that is how long one year of billionaire-scale consumption takes to clear against the human maximum accrual rate. **So the period length is a dial, not a constant** — see §12.

---

## 3. What the kernel holds

Four objects, and nothing else.

| Object | What it is |
|---|---|
| **`EventLog`** | Append-only, columnar. Parallel numpy arrays, one per field. Offers no `delete`, `truncate`, `update`, `remove` or `edit` — asserted by `test_log_is_append_only`. |
| **`Projection`** | The ledger, derived from the log by a segment-sum over the actor column. Cached, and the cache is re-checked against a from-scratch recompute every period. |
| **`Kernel`** | Agents, dials, the time axis, the gate. |
| **`Conformance`** | Seven checks from `Aequitas_Conformance_v0.4.md` (the conformance requirements), run at the end of every period. A failure raises and stops the run. |

### The event kinds

```
SELF_CARE = 0   credited maintenance time, verified by proof-of-life
WORK      = 1   productive hours
CONSUME   = 2   consumption or pollution debit, permanent, on the causer
TRANSFER  = 3   property debit follows possession
PLEDGE    = 4   a permanent grant of debit-room
GENESIS   = 5   admits a thing that existed before the ledger
TALLY     = 6   a measurement of the world; credits the measurer
```

**Only `SELF_CARE`, `WORK` and `TALLY` create credit.** Note what is missing: there is no kind that moves credit from one actor to another. Axiom A3 (non-fungibility — credit is never transferable) is enforced by that absence, not by a rule someone has to remember.

### The physical dimensions

```python
DIMS = ("labour_h", "mass_kg", "energy_mj")
```

Extend the tuple to give a scenario more physics. Nothing else has to change.

### Why the log is columnar

Axiom A6 (derived, not stored) says balances are never authoritative and the event log is. That normally costs a per-agent object graph and a slow fold.

**Measured, on this machine, 2026-08-23:** 200,000 agents, **600,000 events**, credit and full debit vector re-derived from scratch in **9.7 ms**. The honest way and the fast way are the same way.

---

## 4. Credit accrual and the self-care floor

**Credit is hours. One period of accrual splits every person's rate into a floor part and a work part.**

For agent *i* with credit rate `r_i` in hours per day, a network floor `F` in hours per day, and a period of `Δ` days:

```latex
\text{self-care}_i \;=\; \min(r_i,\,F)\cdot \Delta
\qquad
\text{work}_i \;=\; \max(r_i - F,\,0)\cdot \Delta
```

```latex
C_i \;=\; \sum_{e \,\in\, \text{log}_i,\; \text{kind}(e)\,\in\,\{\text{SELF\_CARE},\,\text{WORK},\,\text{TALLY}\}} h_e
```

Two consequences.

1. **The two parts always sum to `r_i · Δ` for any `F ≤ r_i`.** This is why the floor was silently doing nothing before 2026-08-23: moving `F` moved no number, because the population was always built around `F` = 10. `draw_population` now takes the floor as a parameter, so an agent genuinely sits at it. **A floor no agent sits at is not a floor.**
2. **Self-care is flagged `essential`.** It is credited by proof-of-life to everyone alive, which is Foundations §6.1b (self-care is credited work) and §7.5 (the basic-needs floor). It is not a grant.

### Worked example

A person works a 16-hour day. The network floor is 10 hours. One day passes.

| Part | Arithmetic | Hours |
|---|---|---|
| Self-care | `min(16, 10) × 1` | **10** |
| Work | `max(16 − 10, 0) × 1` | **6** |
| **Credit for the day** | | **16** |

**Run output:** `{'self_care': 10.0, 'work': 6.0}`.

---

## 5. The debit vector, and collapsing it

**A debit is not one number. It is one number per physical dimension.**

```latex
\mathbf{D}_i \;=\; \bigl(D_i^{\text{labour\_h}},\; D_i^{\text{mass\_kg}},\; D_i^{\text{energy\_mj}}\bigr),
\qquad
D_i^{d} \;=\; \sum_{e \,\in\, \text{log}_i} q_e^{d}
```

Combining it into one comparable figure is a separate, explicit step, and it is the only place a weighting model is applied:

```latex
\widehat{D}_i \;=\; \sum_{d \,\in\, \text{DIMS}} w_d \cdot D_i^{d}
```

`collapse()` is that step. Foundations §3.2a (debit is a vector, collapsed on demand) is the source. **Whoever controls `w` controls every comparison in the system** — which is open problem OP-10 ([weighting governance](../../00-strategy/GLOSSARY.md#op-10)), the project's top blocker.

### The default weights, and why they matter for reading any current result

```python
DEFAULT_WEIGHTS = {"labour_h": 1.0, "mass_kg": 0.0, "energy_mj": 0.0}
```

**Every published Statera figure so far was computed with mass and energy weighted at zero.** The dimensions are carried, conserved and checked, but they do not enter the gate. This is stated here rather than buried: the gate in every run to date is a pure labour-hours gate.

### Worked example

One debit vector: **2.0 labour-hours, 50 kg, 900 MJ.** Two networks running different weighting models.

| Model | `w` for hours / kg / MJ | Collapsed figure |
|---|---|---|
| A | 1.0 / 0.02 / 0.001 | `2.0 + 1.0 + 0.9` = **3.9 h** |
| B | 1.0 / 0.10 / 0.004 | `2.0 + 5.0 + 3.6` = **10.6 h** |

**The same physical record reads as 3.9 hours or 10.6 hours depending on the model.** The record itself did not change. Only the weights did, and §6 is what keeps that from reaching an allocation.

---

## 6. Divide per dimension, before collapsing

Foundations §3.2a states one rule immediately after the vector: **any division of a debit is computed on the vector, per dimension, before collapsing.**

```latex
\text{divide}(\mathbf{D},\,\theta) \;=\; \bigl(\theta \cdot D^{d}\bigr)_{d \,\in\, \text{DIMS}}
```

In `statera.py`, `divide()` takes a dict of arrays and returns a dict of arrays. **Hand it a collapsed number and it raises `TypeError`.** The rule is enforced by the function signature, not by anyone's memory.

### Worked example — the same split under two weighting models

Take the vector from §5 and split it 70 / 30.

| | labour_h | mass_kg | energy_mj |
|---|---|---|---|
| Whole | 2.0 | 50 | 900 |
| **70% share** | **1.4** | **35** | **630** |
| 30% share | 0.6 | 15 | 270 |

Now collapse the 70% share under both models:

| Model | Whole | 70% share | Share ÷ whole |
|---|---|---|---|
| A (1.0 / 0.02 / 0.001) | 3.9 | 2.73 | **0.70** |
| B (1.0 / 0.10 / 0.004) | 10.6 | 7.42 | **0.70** |

**Two networks that disagree about what a kilogram weighs still compute the same split.** They disagree only about the size of the total. Divide after collapsing and the split itself would move with the weights, which hands the whole allocation history to whoever maintains the model.

---

## 7. The ratio gate

**Discretionary consumption is gated by a ratio, never by a balance drawn down.**

```latex
D_i \;\le\; \rho \cdot C_i
\qquad\Longrightarrow\qquad
\text{room}_i \;=\; \rho\,C_i \;-\; \widehat{D}_i
```

```latex
\text{admitted}_i \;=\;
\begin{cases}
\text{request}_i & \text{if the request is essential}\\[4pt]
\max\bigl(0,\;\min(\text{request}_i,\;\text{room}_i)\bigr) & \text{otherwise}
\end{cases}
```

Three properties.

- **Credit is never spent by a purchase.** A purchase adds to `D`; it never decrements `C`. This is axiom A3 again, and it is what kills the "hoard for a lifetime, splurge in one lump" attack. A hoarder can only front-load their own `ρ·C`. Asserted by `test_credit_is_never_spent`.
- **Essentials are never gated.** Foundations §7.5 restricts non-essentials only, because a gate on essentials falls hardest on the newborn, the old, the sick and the disabled — exactly who that section protects. Asserted by `test_essentials_are_never_gated` at ρ = 0.01.
- **`ρ` is a dial the network sets, and Aequitas never sets.** Axiom A8 (no governing body).

Each consumption event stores the `ρ` and the room that held when it happened. Foundations §3.3 calls this the transaction-time rule: **a later re-weight changes future room and never the validity of a completed act.**

### Worked example

Three people, one day, floor `F` = 10 h/day, `ρ` = 1.5, unbounded appetite.

| Person | Rate `r` | Credit `C` after one day | Room `ρC − D` | Admitted |
|---|---|---|---|---|
| At the floor | 10 h/day | 10 h | `1.5 × 10 − 0` = 15 | **15 h** |
| Middling | 16 h/day | 16 h | `1.5 × 16 − 0` = 24 | **24 h** |
| At the human maximum | 24 h/day | 24 h | `1.5 × 24 − 0` = 36 | **36 h** |

**Top against floor: 36 ÷ 15 = 2.40×.** Run output: `admitted: [15. 24. 36.] ratio top/floor: 2.4`.

---

## 8. The disparity bound `24/F`, derived

**The bound is `24 ÷ F`, and `ρ` cancels out of it.** Here is why, in four lines.

Start from the accrual identity in §4. For any floor `F ≤ r_i`, one period of `Δ` days gives:

```latex
C_i \;=\; \bigl[\min(r_i,F) + \max(r_i-F,0)\bigr]\Delta \;=\; r_i\,\Delta
```

With appetite unbounded and no prior debit, everyone consumes to their gate:

```latex
D_i \;=\; \min(\text{appetite}_i,\; \rho\,C_i) \;=\; \rho\,r_i\,\Delta
```

The credit rate is bounded below by the floor and above by the day, because IC-7 ([the 24-hour cap](../../00-strategy/GLOSSARY.md#ic-7)) caps any account at 24 hours of activity per 24 hours:

```latex
r_i \;\in\; [F,\; 24]
```

So the widest consumption ratio the accounting admits is:

```latex
\frac{\max_i D_i}{\min_i D_i}
\;=\;
\frac{\rho \cdot 24 \cdot \Delta}{\rho \cdot F \cdot \Delta}
\;=\;
\boxed{\dfrac{24}{F}}
```

**`ρ` appears in the numerator and the denominator and cancels. So does `Δ`.** The bound is a fact about the range of possible credit rates, not about the gate setting or the period length.

### It does not drift over time

Over `t` periods, cumulative debit is `D_i(t) = t·ρ·r_i·Δ`, so the ratio stays `24/F` exactly. **Run output, 10 periods, unbounded appetite:**

```
     F=   4h  bound 6.00x  observed 5.7452x flat across 10 periods (drift 8.9e-16)
     F=  10h  bound 2.40x  observed 2.4000x flat across 10 periods (drift 0.0e+00)
     F=  14h  bound 1.71x  observed 1.7143x flat across 10 periods (drift 0.0e+00)
```

### It does not move with `ρ`

**Run output, N = 200,000, `ρ` swept over 21 points in [1, 3]:**

```
[ok] at F=10 h the kernel re-derives 2.40x, flat across rho in [1,3] (spread 8.88e-16)
```

A spread of 8.88 × 10⁻¹⁶ is floating-point noise and nothing else.

### The bound is not the observed spread, and both must be reported

`24/F` is what an adversary could reach if they could manufacture hours. **Whether a real population fills it is a separate, empirical question, and at a low floor the answer is no.**

**Demo run, `ρ` = 1.5, N = 50,000:**

| Floor `F` | Bound `24/F` | Observed | Top worker |
|---|---|---|---|
| 2 h | **12.00×** | 10.76× | 21.5 h/day |
| 4 h | **6.00×** | 5.88× | 23.5 h/day |
| 6 h | **4.00×** | 4.00× | 24.0 h/day |
| 8 h | **3.00×** | 3.00× | 24.0 h/day |
| 10 h | **2.40×** | 2.40× | 24.0 h/day |
| 12 h | **2.00×** | 2.00× | 24.0 h/day |
| 14 h | **1.71×** | 1.71× | 24.0 h/day |

**Below about a 6-hour floor, human endurance binds before the accounting does.** Reaching a 12× spread at `F` = 2 needs somebody working a 22-hour day, and nobody in this population manages it. Foundations §7.5 sets a first condition on the bound: *"the floor stays in a narrow band."* **That is a slightly weaker worry than it reads.**

> ⚠️ **The observed column depends on the sample size, and not in the direction you would guess.** Same seed (42), same code, different N, at `F` = 2 h:
>
> | N | Top worker | Observed spread |
> |---|---|---|
> | 20,000 | 20.98 h/day | 10.49× |
> | 50,000 | 21.52 h/day | **10.76×** |
> | 200,000 | 20.43 h/day | **10.22×** |
>
> **The bound never moves. The observed spread wanders by half a turn.** Every observed figure in this paper therefore carries its N and its seed. What is robust is that bound and observation come apart at a low floor, not the exact figure at which they do.

---

## 9. The age term

Foundations §7.5 claims that **age is the only spread beyond `24/F`**. It has an arithmetic form, and Statera can now check it, because credit accrues from birth.

```latex
\frac{C_{\text{old, max}}}{C_{\text{young, floor}}}
\;=\;
\underbrace{\frac{a_{\text{old}}}{a_{\text{young}}}}_{\text{age ratio}}
\;\times\;
\underbrace{\frac{24}{F}}_{\text{rate ratio}}
```

### Worked example

A 60-year maximum worker against a 20-year subsistence person, at `F` = 10 h/day, annual periods.

| | Arithmetic | Credit |
|---|---|---|
| 60-year worker at 24 h/day | `60 × 365 × 24` | **525,600 h** |
| 20-year person at the 10 h floor | `20 × 365 × 10` | **73,000 h** |
| Ratio | `525,600 ÷ 73,000` | **7.20×** |
| Predicted | `(60/20) × (24/10)` = `3 × 2.4` | **7.20×** |

**Run output:** `[ok] age is the only spread beyond the bound: a 60-year max worker vs a 20-year floor person = 7.20x (= 3 x 24/F)`.

The kernel agrees with the theory to the last digit. **If it had not, either the model or §7.5 would have been wrong, and both are results.**

---

## 10. Cohorts — one row, many people

**The log stores what one person did. A headcount says how many people that row speaks for.**

Every row carries a `weight` column. The rule is one line:

```latex
X^{\text{population}}_i \;=\; w_i \cdot X^{\text{person}}_i
\qquad
\text{Headcount} \;=\; \sum_i w_i
```

**Aggregate figures multiply by the headcount. Per-person checks must not.** IC-7 asks whether *one* account claimed more than 24 hours in a day. A cohort of a thousand people did not claim 12,000 hours; each of them claimed 12. Scaling that check would make every large cohort fail instantly, and would be the wrong question besides.

| Uses the headcount | Must not use the headcount |
|---|---|
| `population_credit()`, `population_debit()`, `headcount()` | IC-7 (the 24-hour cap) |
| Mass and energy conservation (§11) | IC-8 (pledge backing) |
| Every reported total | `room()` and the gate |

### Worked example

A cohort of **60,000** adults. The exemplar works a 16-hour day at a 10-hour floor. The period is 30 days.

| Reading | Arithmetic | Result |
|---|---|---|
| The exemplar's credit | `(10 + 6) × 30` | **480 h** — this is what IC-7 checks |
| The cohort's credit | `480 × 60,000` | **28,800,000 h** |
| Headcount | | **60,000** |

**Run output:** `exemplar credit [480.] population credit [28800000.] headcount 60000.0`.

### Why this is not a fudge

The log is still append-only. It is still the only authority. A standing is still derived by adding rows up. **Nothing is stored as a balance.** The only change is that one row speaks for many identical people.

**And at `weight = 1.0` the cohort kernel is the individual kernel** — one code path, two settings, asserted by `test_weight_of_one_changes_nothing`.

### Why cohorts exist at all

| Design | Rows for 20 years at monthly steps |
|---|---|
| 200,000 individuals × 240 months × 3 events | **144,000,000** — about 9 GB. Will not run. |
| ~1,900 cohorts × 240 months × 3 events | **1,368,000** — about 90 MB. Runs anywhere. |

Deaths shrink a cohort's headcount and never touch the exemplar's record. **Run output:** `[ok] 10% mortality takes the headcount 1000 -> 900 and leaves the exemplar's 4380 h untouched` — 4,380 hours being 12 h/day over 365 days.

---

## 11. Conservation of mass and energy

**Matter balances over a population, not over a representative person.** This is the one check that must use the headcount.

For every process *p* and every conserved dimension *d*:

```latex
\sum_{e \,:\, \text{process}(e) = p} w_e \cdot q_e^{d} \;=\; 0
\qquad d \in \{\text{mass\_kg},\; \text{energy\_mj}\}
```

This is IC-1 ([mass balance](../../00-strategy/GLOSSARY.md#ic-1)) and IC-2 ([energy balance](../../00-strategy/GLOSSARY.md#ic-2)). A process id groups the events of one physical transformation. What went in must come out. A process id of −1 means the event is not part of a recorded process.

**Labour-hours are deliberately not conserved.** Hours are not a conserved physical quantity, and asserting that they balance would be false physics.

### Worked example — the case that fails without the headcount

One factory cohort of **1** person makes 10 kg. A consumer cohort of **100** people take 0.1 kg each.

| Reading | Arithmetic | Result |
|---|---|---|
| Per exemplar, unweighted | `10 − 0.1` | **9.9 kg** — a leak that is not there |
| Weighted by headcount | `10 × 1 + (−0.1) × 100` | **0.0 kg** — balances |

**Run output:** `unweighted balance 9.9 weighted 0.0`.

### And it catches a real leak

Two processes. Process 0 moves 10 kg in and 10 kg out. Process 1 moves 10 kg in and only 7 kg out.

**Run output:** `[ok] IC-1/IC-2 catch a 3 kg leak in a recorded process`.

---

## 12. The 24-hour cap, scaled to the period

IC-7 says **no account claims more than 24 hours of activity per 24 hours.** The rule is about a day. A period may be a month or a year.

```latex
\sum_{\substack{e \,\in\, \text{log}_i,\; \text{period}(e)=t \\ \text{kind}(e)\,\in\,\text{CREDITING}}} h_e
\;\;\le\;\; 24 \cdot \Delta
```

where `Δ` is `days_per_period`. **Without the scaling, IC-7 fires on the first month of any run coarser than daily** — and generational scenarios need annual steps.

### Worked example

A 12 h/day worker, a 30-day period.

| | Arithmetic | Hours |
|---|---|---|
| Legitimate claim | `12 × 30` | **360** |
| The cap | `24 × 30` | **720** |
| Verdict | 360 ≤ 720 | **passes** |

**Run output:** `[ok] a 30-day period credits 360 h and IC-7 does not fire (cap 720 h)`.

**And scaling the cap does not disable it.** Add a 400-hour claim on top of the legitimate 360 and the total is 760 against a cap of 720.

**Run output:** `[ok] the scaled IC-7 cap still catches an over-claim (760 h in 30 days)`.

---

## 13. Pledge backing

A pledge is a permanent grant of debit-room, backed one-for-one by lifetime earned credit. It is Foundations §6.4 (pledges and signals), and the constraint is IC-8 ([pledge backing](../../00-strategy/GLOSSARY.md#ic-8)).

```latex
P_i \;=\; \sum_{\substack{e \,\in\, \text{log}_i \\ \text{kind}(e)=\text{PLEDGE}}} \!\!\!\! -h_e
\qquad\qquad
P_i \;\le\; \sum_{\substack{e \,\in\, \text{log}_i \\ \text{kind}(e)\,\in\,\text{CREDITING}}} \!\!\!\! h_e
```

**Note which sum sits on the right.** IC-8 is checked against *earned* credit, meaning the sum over crediting kinds only. It is not checked against the net credit projection. Foundations §6.4 explains why the cap must be exactly one-for-one: let it exceed and you get more permanent debit-room granted across the network than the grantors' credit can stand behind.

### Worked example

A person earns 12 hours in a day, then pledges.

| Step | Pledged | Earned | Verdict |
|---|---|---|---|
| Pledge 5 h | 5 | 12 | **passes** |
| Pledge 20 h more | 25 | 12 | **fails, over by 13 h** |

**Run output:** `IC-8: pledged exceeds earned by 13.000 h`, and `[ok] IC-8 catches pledging beyond lifetime earned credit`.

> ⚠️ **A pledge in `statera.py` also reduces the pledger's consumption room, and Foundations says it should not.** See §18, item 1. Nothing published so far is affected, because no scenario in the kernel pledges.

---

## 14. The residual rule — stated, not built

**This relation is in the theory and is not in `statera.py`.** It is stated here because the adoption programme in §2 runs on it, and because a reader should not have to guess which equations the kernel implements.

Foundations §5.1b (the residual rule) estimates an unmeasured producer's output as the independently-known total, minus what measured producers actually recorded, divided among those who remain dark:

```latex
\hat{y} \;=\; \frac{N - Y}{Z}
```

| Symbol | Meaning |
|---|---|
| `N` | The independently-known total — an FAO figure, trade data, satellite survey. Foundations calls this the **closure witness**. |
| `Y` | What measured producers actually recorded. |
| `Z` | The count of producers still unmeasured. |

**Computed over the whole population instead, this creates adverse selection.** Better-than-average producers instrument to prove it, worse-than-average stay dark and free-ride on an average their own absence inflates. **Over the residual, the estimate worsens as good producers leave, so darkness stops paying.**

Foundations adds the **conservative-count rule**: when `Z` is uncertain, under-count it. Under-counting raises each dark actor's estimated share, which is the direction that provokes them to come forward.

### Worked example — the adoption direction

A region's independently-measured total is 1,000 units, spread across 100 dark actors. From [`Onboarding_the_wealthy_v0.1.md`](../../00-strategy/Onboarding_the_wealthy_v0.1.md) §4:

| Participants | `Y` measured | `Z` still dark | `(N − Y)/Z` per dark actor |
|---|---|---|---|
| 0 | 0 | 100 | **10.0** |
| 40 low-consumers | 200 | 60 | **13.3** |
| 80 low-consumers | 440 | 20 | **28.0** |

**The last twenty face nearly three times the first estimate, and none of them did anything.** They stayed while the well-documented left.

**Nobody receives a bill.** Foundations §5.1c holds the residual unassigned: it is computed, published, and charged to no account until its causer onboards. **The pressure is a published number that gets worse the longer you wait.**

**What is needed to build this:** a non-participant pool, a per-cohort join decision, a verification-cost dial, and generational time. Items 1–6 of [`Onboarding_the_wealthy_v0.1.md`](../../00-strategy/Onboarding_the_wealthy_v0.1.md) §8 name them all.

---

## 15. Dollars into hours

**Household surveys report dollars. Aequitas accounts in hours, kilograms and megajoules.** Something has to bridge them, and the bridge is an intensity table.

```latex
\text{hours} \;=\; \text{spend}\;[\$] \;\times\; \kappa_s \;\left[\frac{\text{h}}{\$}\right]
\qquad \text{the dollars cancel}
```

`κ_s` is the intensity for sector *s*: how much labour sits behind one dollar of spending there, directly and through the whole supply chain. Full method: [Labour and pollution intensity](../../00-strategy/GLOSSARY.md#src-labour-and-pollution-intensity).

### Worked example

| | |
|---|---|
| Food spend, [BLS Consumer Expenditure Survey 2023](https://www.bls.gov/news.release/cesan.nr0.htm) | **$9,985** |
| Intensity | **0.0179 h per dollar** |
| Embodied labour | **≈ 178 hours** |

The economy-wide average that anchors it:

| | Arithmetic | Result |
|---|---|---|
| Average intensity | `1,380 h ÷ $77,280` | **0.01786 h per dollar** |
| The same figure inverted | `1 ÷ 0.01786` | **$56.00 of spend per embodied hour** |

The 1,380 h/yr median-lifestyle figure comes from [`MEDIAN_LIFESTYLE_RESULT.md`](../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md); the $77,280 from the CE 2023 news release above.

> ⚠️ **One average across a whole economy is exactly the mistake to avoid.** Food is more labour-intensive than the average. A pension contribution has no labour behind it at all and is struck by axiom A1 (materialism of cost) before it starts, because a financial claim is not matter or energy. **The intensity has to be per sector.**

**The US labour intensities come from the BLS Employment Requirements Matrix (ERM)** — the table giving hours needed per million dollars of final demand, by industry. It is on disk at `06-simulation/data/erm_full/`. [BLS pulled it on 2026-02-06](https://www.bls.gov/emp/data/input-output-matrix.htm) *(link unverified)* and the project recovered it through the [Internet Archive Wayback Machine](https://web.archive.org/). **Treat every BLS download as perishable.**

**Everything computed this way is a floor and never a ceiling**, for two independent reasons that happen to point the same way:

1. Input–output tables split physical impacts by dollars, which under-counts cheap heavy flows — waste, bulk materials, land.
2. The basket has coverage gaps.

That is Foundations §5.1a's floor rule and conformance requirement 13, and it means **there is one honest statement to make, not two competing ones.**

### What the kernel actually uses

**`statera.py` does not read an intensity table.** For the clearing reproduction it imports a single calibration constant from [`rho_sweep.py`](../disparity-ceiling/rho_sweep.py):

```latex
\kappa \;=\; \operatorname{median}_i(r_i) \;=\; 13.784 \ \text{debit-hours per median-lifestyle unit per day}
```

**Run output:** `kappa (median credit rate, h/day) 13.783972837371179`.

This is chosen so that at `ρ` = 1 the median person's own credit exactly funds one median lifestyle. **It is a calibration, not a measurement.** A want of `r` lifestyle units requests `r · κ` debit-hours; the admitted hours divide back by `κ` to give real lifestyle received.

---

## 16. The clearing rate

**A `ρ` exists at which aggregate demand equals what the economy can physically make.** Statera re-derives it through its own event log and gate, rather than through the closed-form arithmetic `rho_sweep.py` uses.

```latex
\text{Find } \rho^{*} \text{ such that }
\sum_i \frac{1}{\kappa}\min\!\bigl(\text{want}_i \cdot \kappa,\; \rho^{*} C_i\bigr)
\;=\; R_{\max}
```

```latex
R_{\max} \;=\; \text{CAP} \cdot \sum_i \text{want}_i
```

`CAP` = 0.85 is the physical capacity as a fraction of unconstrained wants, on the finding that **materials and energy bind before labour does** (Foundations §3.5).

### Worked example — the numbers from a live run

| | Value |
|---|---|
| Population | 200,000 |
| Intensity `κ` | 13.784 debit-h per lifestyle unit |
| Unconstrained wants | 221,652 lifestyle units |
| `R_max` = `0.85 × 221,652` | **188,404 lifestyle units** |
| **Clearing `ρ*`** | **1.20** |
| Median person receives | **0.918×** their desired lifestyle |
| Share held below their wants | **35.5%** |
| Subsistence allowance `ρ*·F/κ` = `1.20 × 10 ÷ 13.784` | 0.871 lifestyle units |
| Top consumption ÷ subsistence allowance | **2.40×** — the bound holds |

**Run output:** `[ok] kernel re-derives the clearing rate: rho*=1.20 (pub 1.20), median 0.92x (pub 0.92), 35% constrained (pub 35%)`.

> **The absolute `ρ*` is illustrative and depends on OP-10 (weighting governance).** What is claimed here is that the kernel reproduces it through different machinery, not that the number is settled. **Same inputs, different machinery, same number — or the kernel is wrong.** That is the roadmap's guard against building a framework nobody uses.

---

## 17. What a run prints

Two commands, run on 2026-08-23.

### `python statera.py --test`

**All 22 self-tests pass.** Each conformance check was tested by deliberately breaking it.

```
[ok] the log offers no delete, truncate, or edit (Sec.5.4)
[ok] at a headcount of 1 the kernel is unchanged (v0.1 results stand)
[ok] a headcount scales the population and never the person (IC-7 intact)
[ok] IC-1 weighs matter by headcount (unweighted this reads a 9.9 kg leak that is not there)
[ok] a 30-day period credits 360 h and IC-7 does not fire (cap 720 h)
[ok] the scaled IC-7 cap still catches an over-claim (760 h in 30 days)
     F=   4h  bound 6.00x  observed 5.7452x flat across 10 periods (drift 8.9e-16)
     F=  10h  bound 2.40x  observed 2.4000x flat across 10 periods (drift 0.0e+00)
     F=  14h  bound 1.71x  observed 1.7143x flat across 10 periods (drift 0.0e+00)
[ok] ten periods hold every Sec.9 check and the bound does not drift
[ok] age is the only spread beyond the bound: a 60-year max worker vs a 20-year floor person = 7.20x (= 3 x 24/F)
[ok] death stops accrual at period 3 and leaves all 6 rows in the log (Sec.5.4)
[ok] a cohort born at period 5 holds half the credit of one born at 0, and the headcount is 250
[ok] 10% mortality takes the headcount 1000 -> 900 and leaves the exemplar's 4380 h untouched
[ok] credit is never spent by a purchase (A3: not a currency)
[ok] the gate restricts non-essentials only (Sec.7.5)
[ok] divide() refuses a collapsed figure (Sec.3.2a closed by type)
[ok] IC-1/IC-2 catch a 3 kg leak in a recorded process
[ok] IC-7 catches a day with more than 24 hours in it
[ok] IC-8 catches pledging beyond lifetime earned credit
[ok] ceiling is rho-independent (rho cancels in rho*24 / rho*F)
[ok] at F=10 h the kernel re-derives 2.40x, flat across rho in [1,3] (spread 8.88e-16)
[ok] the floor is a real dial: bound 6.00x (F=4) -> 2.40x (F=10) -> 1.71x (F=14)
[ok] at F=2 h the bound is 12.0x but the population only reaches 10.22x (top worker 20.4 h/day)
[ok] kernel re-derives the clearing rate: rho*=1.20 (pub 1.20), median 0.92x (pub 0.92), 35% constrained (pub 35%)

All self-tests passed.
```

### `python statera.py --demo`

Both reproduction targets hit exactly. The full sweep table appears in §8; the clearing figures in §16. The conformance line reads:

```
  3. CONFORMANCE             600,000 events, 200,000 agents
     all Sec.9 assertions checked and passing
```

### A failure is a result

**`ConformanceError` stops the run at the period that broke it.** Either the scenario is malformed or the theory has a hole. Both are results, and neither is something to catch and continue past.

---

## 18. Where the code and the documents disagree

**Six disagreements, found while writing this paper. All are recorded rather than repaired, because this paper does not edit the code.**

### 1. A pledge reduces the pledger's consumption room, and Foundations says it must not

`Kernel.pledge()` appends a `PLEDGE` event carrying `credit_h = −hours`. `Projection.credit()` sums every credit column regardless of kind. **So a pledge decrements the credit projection, and `room() = ρ·C − D` shrinks with it.**

**Measured:** a person earns 12 h, pledges 5 h, and `proj.credit()` reads **7.0**. At `ρ` = 1.5 their consumption room falls by 7.5 hours.

Foundations §6.4 says the opposite in three places:
- *"a person's lifetime pledging-budget equals their lifetime earned credit, spent down once (pledging never diminishes credit itself)"*
- *"The pledger's credit itself never moves and is never earmarked"*
- The docstring of `pledge()` in `statera.py` itself: *"It does not move the pledger's credit."*

**Effect on published results: none.** No scenario in the kernel pledges, and IC-8 is checked against earned credit rather than the projection, so the check is correct. **Effect on any future scenario that pledges: the pledger is charged twice** — once from the pledging budget, and again from their consumption room.

### 2. The transaction-time check fires on an event that admitted nothing

`Conformance.check_transaction_time` raises if any recorded room was negative. But room can go negative legitimately, because essentials are never gated: essential consumption can push `D` above `ρ·C`, and `step()` takes essentials before discretionary spending.

**Reproduced:** four people at the 10-hour floor, `ρ` = 0.5, essentials of 20 h/day, a discretionary want of 1 h/day.

```
ConformanceError raised: Sec.3.3: an event was admitted with no room
room_at column: [nan nan nan nan nan nan nan nan  5.  5.  5.  5. -15. -15. -15. -15.]
```

**Nothing was admitted.** The discretionary request was clipped to zero, exactly as it should be. The check reads the recorded room and raises anyway. **This will stop any scenario where essential consumption exceeds `ρ·C`** — which is precisely the population Foundations §7.5 exists to protect.

### 3. The re-weight half of the transaction-time check asserts nothing

The same function computes a re-weighted history and then discards it:

```python
heavier = {d: v * factor for d, v in k.proj.debit().items()}
_ = collapse(heavier, k.dials.weights)   # future room shrinks; history stands
```

**No assertion follows.** The docstring claims that re-weighting the whole history leaves no past event a violation. **That claim is not actually tested.** The check that does run is the recorded-room check in item 2.

### 4. The essentials check is close to vacuous

`check_essentials_never_gated` raises if an essential consumption row carries negative `labour_h`. For an essential request, `admitted = request`, so the value is non-negative unless a scenario passes a negative request. **The real property is asserted by `test_essentials_are_never_gated`, not by the running check.**

### 5. The results documents describe an older, smaller kernel

| Document says | The code is |
|---|---|
| [`STATERA.md`](README.md): *"12 self-tests green"*, one period only, `kernel.py` | 22 self-tests, a full time axis with births and deaths, `statera.py` |
| [`STATERA_CHANGELOG.md`](CHANGELOG.md): *"793 lines. 12 self-tests"* | **1,185 lines. 22 self-tests.** |
| [`STATERA.md`](README.md) footer: *"Tracks Foundations v0.18"* | Header of the same file says v0.19 |

**Every link in the three Statera documents points at `kernel.py`, `KERNEL.md`, `KERNEL_CHANGELOG.md` and `KERNEL_PLAN_v0.2.md`.** None of those files exists. The rename to `statera.py` / `STATERA*.md` happened on 2026-08-23 and the internal links were not cascaded. [`Data_consumer-segmentation-archetypes_v0.1.md`](../../02-research/Data_consumer-segmentation-archetypes_v0.1.md) carries the same stale path.

### 6. The low-floor narrative is quoted at one sample size

[`STATERA.md`](README.md) and [`STATERA_CHANGELOG.md`](CHANGELOG.md) both say *"reaching 12× needs somebody working a 22-hour day and the most anyone manages is 21.5."* That is the N = 50,000 draw, and it reproduces exactly. **At N = 200,000 the same code gives a top worker of 20.4 h/day and an observed spread of 10.22×.** The finding survives; the specific digits do not travel. Table in §8.

### Equations I could not verify against the code

| Relation | Status |
|---|---|
| `(N − Y)/Z`, the residual rule | **Not in `statera.py`.** Stated in §14 from Foundations §5.1b. Implemented separately in [`residual_unravelling.py`](../residual-unravelling/residual_unravelling.py), which this paper did not audit. |
| Dollars-to-hours, `spend × intensity` | **Not in `statera.py`.** The kernel uses a single calibration constant (§15), not an intensity table. The method lives in [`median_lifestyle.py`](../median-lifestyle/archive/median_lifestyle.py) and its method note. |
| The `~40%` verification-cost stall threshold | Quoted in Foundations §5.3a from [`residual_unravelling.py`](../residual-unravelling/residual_unravelling.py). Not reachable from Statera and not re-run here. |

---

## 19. Honest limits

### 19.1 The 17 conformance requirements — what Statera can and cannot check

`Aequitas_Conformance_v0.4.md` lists 16 requirements that must hold for an implementation to be Aequitas. Statera asserts some as running invariants, satisfies some structurally without asserting them, and cannot express the rest.

| # | Requirement | Status in Statera |
|---|---|---|
| 1 | Every credit and debit records a real material or energy flow | **Structural.** Every quantity is hours, kilograms or megajoules. No check asserts it. |
| 2 | Flows attribute to whoever **caused** them | ❌ **Not expressible.** No causer model exists. |
| 3 | Labour is never rate-scaled | **Structural.** No multiplier exists anywhere in the code. No check asserts it. |
| 4 | Credit is never transferable | ✅ `check_a3`, plus the absence of any credit-moving event kind. |
| 5 | Standing derived from an append-only record, never stored | ✅ `check_a6` recomputes from scratch every period and asserts the cache agrees. |
| 6 | Records never destroyed or edited; a disputed record is annotated | ⚠️ **Half.** `EventLog` exposes no delete or edit. **There is no `CONTEST` event kind and no annotation mechanism.** |
| 7 | Mass and energy conserve; every parcel has an origin and a fate | ⚠️ **Half.** IC-1 and IC-2 (balance) are checked per process. **IC-3 (origin closure) and IC-4 (fate closure) are not checked at all.** |
| 8 | No account claims more than 24 hours per 24 hours | ✅ `check_ic7`, scaled by days per period. |
| 9 | Cumulative pledges never exceed lifetime earned credit | ✅ `check_ic8`. |
| 10 | A debit is a vector; divide per dimension before collapsing | ✅ Enforced by the `divide()` signature. |
| 11 | The gate is evaluated at the moment of the transaction | ⚠️ **Half.** The witnesses are recorded. The re-weight assertion is a no-op (§18, item 3), and the running check false-positives (§18, item 2). **Nothing in any scenario is ever revised mid-run.** |
| 12 | Every estimate carries basis, method, vintage and extent | ❌ **Not expressible.** No such fields exist on the log. |
| 13 | Incomplete coverage is published as a floor, with the gap named | ❌ **Not expressible.** No coverage model exists. |
| 14 | Coverage estimated over the unmeasured residual, never the whole population | ❌ **Not expressible.** See §14. |
| 15 | The coverage leftover is computed, published, and charged to no account | ❌ **Not expressible.** |
| 16 | Every estimating number and method is published | ❌ **Not expressible in code.** A documentation obligation. |
| 17 | Essential provision is never gated | ✅ Behaviourally, by `consume(essential=True)`. The running check is close to vacuous (§18, item 4). |

**Summary: 6 asserted as running invariants, 2 satisfied structurally without assertion, 3 half-covered, 6 not expressible.**

**Six requirements are not expressible: 2, 12, 13, 14, 15 and 16. All six need the same missing thing — a model of the world outside the ledger.** Dark producers, an independently-known total, a coverage figure. That is one build, not six.

### 19.2 What the instrument cannot say anything about

- **The economy is a toy.** One aggregate consumption good with a debit intensity. No sectors, no supply chains, no input-output structure, no pollutant stocks. The five exemplar chains in [`STATERA_PLAN_v0.2.md`](STATERA_PLAN_v0.2.md) §5 are design, not code.
- **Mass and energy are weighted zero by default (§5).** Every current result is a labour-hours result.
- **No behaviour layer.** Agents request and are gated. **Nobody joins, leaves, pledges, instruments, or cheats.** That is the whole adoption question in §2, and none of it is built.
- **No money boundary.** There is no second economy to trade with, so Foundations §5.5 (parallel implementation) cannot be tested.
- **Nothing is ever re-weighted mid-run.** The shock that would make requirement 11 a real test does not exist yet.
- **Everyone inside a cohort is identical.** The model cannot show inequality within a type. All spread it reports is spread between types and ages.
- **Headcounts go fractional** as mortality thins a cohort. That is honest for a population model and is recorded as a limit rather than rounded away.
- **A cohort exemplar cannot cheat on its own.** Fraud and collusion scenarios need `weight = 1.0` individual agents. The code supports it; long runs will not use it.

### 19.3 What the numbers inherit

- **`ρ*` = 1.20 is illustrative.** It depends on the weighting model, which is OP-10, exactly as [`RHO_SWEEP.md`](../disparity-ceiling/RHO_SWEEP.md) says. What Statera claims is that it reproduces the figure through different machinery.
- **The observed spread depends on N and on the seed (§8).** The bound does not.
- **The low-floor finding is a property of the population model** — 35% doing little paid work, the rest centred on about 6 hours with a 3-hour spread. A society with genuinely different working hours fills the bound differently.
- **The disparity bound is conditional, and Foundations says so.** §7.5 lists five conditions, of which the sharpest is OP-22 ([minimum audit disclosure](../../00-strategy/GLOSSARY.md#op-22)) — proving a claim is backed without exposing the history behind it. **Statera assumes that guard is implementable. It does not model it.**
- **Every cost figure the programme will produce is a floor, never a value** (§15). Two independent errors point the same way. Foundations §5.1a and conformance requirement 13 both require it to be said on the face of the result.

---

## 20. Sources

### Project documents

| Document | What it carries |
|---|---|
| [`Aequitas_Foundations_v0.19.md`](../../99-archive/Aequitas_Foundations_v0.19.md) | The theory. Axioms A1–A8 in §1; the debit vector in §3.2a; the transaction-time rule in §3.3; the residual rule in §5.1b; the self-care floor in §6.1b; pledges in §6.4; the basic-needs floor and the disparity bound in §7.5; the 17 conformance requirements in §9. |
| [`GLOSSARY.md`](../../00-strategy/GLOSSARY.md) | Every acronym, and the research source index. Link to its anchors rather than to research files directly. |
| [`Aequitas_Simulation_Roadmap_v0.2.md`](../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md) | The build order Statera implements steps 1–3 of. |
| [`Onboarding_the_wealthy_v0.1.md`](../../00-strategy/Onboarding_the_wealthy_v0.1.md) | The adoption arithmetic and the six things a run needs. |
| [`STATERA_PLAN_v0.2.md`](STATERA_PLAN_v0.2.md) | The current design, five settled decisions, build order. |
| [`SUBSECTOR_CANDIDATES_v0.1.md`](SUBSECTOR_CANDIDATES_v0.1.md) | The 27 categories, 5 modifiers, and the basket arithmetic. |
| [`MEDIAN_LIFESTYLE_RESULT.md`](../median-lifestyle/MEDIAN_LIFESTYLE_RESULT.md) | The 1,380 h/yr anchor. |
| [`RHO_SWEEP.md`](../disparity-ceiling/RHO_SWEEP.md) | The clearing-rate result and its calibration caveats. |
| [`DISPARITY_CEILING.md`](../disparity-ceiling/DISPARITY_CEILING.md) | The formal statement of `24/F` and its stress test. |

### Research notes

| Note | Bears on |
|---|---|
| [Labour and pollution intensity](../../00-strategy/GLOSSARY.md#src-labour-and-pollution-intensity) | §15 — the dollars-to-hours method, and why every figure is a floor. |
| [Consumer segmentation and archetypes](../../00-strategy/GLOSSARY.md#src-consumer-segmentation-archetypes) | §10 — where cohorts come from, and the rule that an archetype may name a cohort but never supply a number. |
| [Cross-country labour efficiency](../../00-strategy/GLOSSARY.md#src-cross-country-labour-efficiency) | §16 — what the locale dial must reproduce. |
| [Estimation-engine data sources](../../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources) | §15 — the price-split ruling. |
| [Joint-production problem](../../00-strategy/GLOSSARY.md#src-joint-production-allocation-problem) | §6 — why divide-before-collapse matters. |

### Outside sources

| Source | Used for | Link |
|---|---|---|
| **BLS Consumer Expenditure Survey 2023** | $77,280 average annual expenditure; the $9,985 food line. | [News release](https://www.bls.gov/news.release/cesan.nr0.htm) · [tables](https://www.bls.gov/cex/tables.htm) |
| **BLS Employment Requirements Matrix** | US labour intensity by sector. Withdrawn 2026-02-06 and recovered from the archive. | [Program page](https://www.bls.gov/emp/data/input-output-matrix.htm) *(unverified)* · [Wayback Machine](https://web.archive.org/) |
| **Stadler et al., EXIOBASE 3 (2018)** | Hours worked at supply-chain scale for 44 countries. The only mainstream model that carries labour. | [Journal of Industrial Ecology](https://onlinelibrary.wiley.com/doi/10.1111/jiec.12715) |
| **USEEIO, US EPA** | 389 US sectors tagged with land, water, energy, minerals and pollution per dollar. | [EPA](https://www.epa.gov/land-research/us-environmentally-extended-input-output-useeio-models) |
| **Poore & Nemecek (2018)** | Where food categories separate — 38,700 farms, 40 products. | [Our World in Data](https://ourworldindata.org/environmental-impacts-of-food) · [paper](https://www.science.org/doi/10.1126/science.aaq0216) *(paywalled)* |
| **Federal Reserve Survey of Consumer Finances 2022** | The US wealth distribution the ceiling is compared against. | [SCF](https://www.federalreserve.gov/econres/scfindex.htm) *(unverified)* |
| **Ellerman, labour theory of property** | The attribution principle under A1 — only humans act, so responsibility imputes to people. | [Paper](http://et.worldeconomicsassociation.org/files/WEA-ET-5-1-Ellerman.pdf) |
| **Cockshott & Cottrell** | That in-kind calculation at national scale is computationally feasible. | [Towards a New Socialism](https://en.wikipedia.org/wiki/Towards_a_New_Socialism) |
| **Weisz & Duchin (2006)** | Physical input–output tables, the method Aequitas actually wants. | [Ecological Economics](https://www.sciencedirect.com/science/article/abs/pii/S092180090500248X) |
| **EIA RECS / CBECS** | Residential and commercial energy per square foot, in physical units. | [RECS](https://www.eia.gov/consumption/residential/) · [CBECS](https://www.eia.gov/consumption/commercial/) |
| **CMS National Health Expenditure Accounts** | Health spend by source of funds — the reason the survey basket sees about one-sixth of healthcare. | [CMS](https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data) *(unverified)* |

---

*Statera v0.1. The instrument, not the theory.*
