# The simulations, in plain language

> **One page, fifteen projects.** Each entry says what the code is for, the arithmetic it runs, one worked example with real digits, what it found, and **which part of the theory it tests**.
>
> **This is the tour. [`README.md`](README.md) is the index**, and every project's own `RESULTS.md` carries the conditions and the caveats. **No number here should be quoted without them.**

---

## The words every entry uses

| Term | What it means |
|---|---|
| **`F`** | **The floor.** Hours a day a trust network credits for the work of staying alive. A dial the network sets. At `F` = 10 that is 3,650 h a year |
| **ρ** ("rho") | **The debit tolerance.** The multiplier in the consumption gate `D ≤ ρ·C` |
| **`C`, `D`** | A person's cumulative **credit** (hours the books recorded as work) and **debit** (what their consumption is reckoned to cost) |
| **IC-7** | The check that caps any account at **24 hours of activity in 24 hours** |
| **`N`, `Y`, `Z`** | An outside physical total for a region · what a network's own producers recorded · the count of producers it has **not** measured |
| **`R`** | The leftover, `N − Y`. **Charged to nobody** |

**A median US lifestyle commands about 1,380 hours of other people's labour a year.** That figure is measured, not assumed, and half the entries below lean on it.

---

# A. The kernel

### 1. `statera/` — one engine the other scenarios run on

**Tests:** the whole accounting — an append-only event log, the debit vector, credit accrual, the gate, the conformance checks.
**Maths:** every position is recomputed from the log; nothing is stored. The gate is `D ≤ ρ·C`, re-checked per event.
**Worked:** re-derive four numbers the older scripts published, through different machinery. Disparity at `F` = 10 → **2.4000×** (spread 8.88 × 10⁻¹⁶) against a published 2.40×; clearing rate **1.20** against 1.20; median gets **0.92×** a full lifestyle; **35%** held below their wants.
**Result:** all four reproduce exactly. **A change in them would be a bug, not a finding.**
**Points at:** Foundations §3.1 (the log), §3.0 (the gate).

---

# B. What the theory claims about people

### 2. `disparity-ceiling/` — how far apart can two people get?

**Tests:** the bound `24 ÷ F`.
**Maths:** the most anyone can be credited is 24 h/day (IC-7); the least is `F`. Consumption is `ρ·c`, so the ratio is `(ρ·24)/(ρ·F)`. **ρ cancels.**
**Worked:** at `F` = 10 → `24 ÷ 10` = **2.40×**. A very hard working life — 12 h of work a day, 300 days a year, ages 20 to 70 — reaches **1.62×**. Money's top tail runs to about **10⁶×**.
**Result:** the bound is exact and does not move with ρ or with the weighting model. **Quote 1.6, not 2.4: 2.4 is a wall nobody reaches.**
**Limit:** it is a statement about **one network's own books** and nothing wider. **And it bounds; it does not witness** — see entry 15.
**Points at:** Foundations §5.5.5, §5.5.7.

### 3. `median-lifestyle/` — what does a normal life actually cost?

**Tests:** whether human hours are the binding constraint.
**Maths:** add four tracks — domestic embodied labour, housing annualised, labour embodied in imports, and remediating your own pollution.
**Worked:** 612 + 45 + imports (≈47% of the total) + ≈18 → **≈ 1,350–1,400 h/yr**, against the **3,650 h/yr** everyone earns by being alive.
**Result:** **a median lifestyle costs about one third of one person's annual credit.** Cross-country: the US spends **50–80% more labour and 2.5–4× the carbon** than Germany, Sweden, France, Japan or Spain for a comparable life and shorter lifespans.
**Limit:** at US production efficiency the deployable hours **do not** close — 0.43 to 0.87 of what is needed. Abundance comes from the method, not from more hours.
**Points at:** Foundations §3.5.

### 4. `stable-band/` — is there a workable pair of dials?

**Tests:** whether a network can set `F` and ρ so essentials stay affordable **and** the ledger still rations.
**Maths:** the band is `ρ ∈ [ E/(365·F) , ρ*(F) ]`, where `E` is what a year of essentials commands. The largest basket a floor can carry is `E_max = 365 · F · ρ*(F)`.
**Worked:** at the tightest floor measured, `F` = 2 and ρ\* = 3.70 → `365 × 2 × 3.70` = **2,701 h/yr**, which is **1.96×** a whole median American lifestyle.
**Result:** **the band exists at every floor from 1 to 14 h/day and never closes.** Essentials are a part of a median lifestyle, not double it, so no floor in range fails on affordability. **What binds is capacity, not affordability.**
**Points at:** Foundations §5.5.3.

### 5. `pledge-reserve/` — who takes the dangerous job with no danger pay?

**Tests:** whether over-pledging can staff hazardous work without a wage premium.
**Maths:** pledges beyond a task's cost become an earmarked reserve that pays only against verified task-caused harm. Sweep the coverage fraction `c`.
**Worked:** supply rises steadily with coverage and crosses at **`c*` = 0.83** — the job staffs once the reserve pre-funds about 83% of the expected future harm.
**Result:** it clears. **And a full shield doubles the damage** — harm 500 under a complete shield against 250 under a partial buffer.
**Limit:** the integrity rests on the **physical-trace test**, not on catching fraud. Padded claims leave 0% uncovered; a weak causal trace leaves **20%** uncovered.
**Points at:** Foundations §4.6.

---

# C. Does the arithmetic hold?

### 6. `allocation-engine/` — does splitting one process's cost terminate?

**Tests:** the joint-production rule, and whether it inherits the classical negative-value result.
**Maths:** per-unit cost solves `p = c + Ãp` with `Ã, c ≥ 0`. Aequitas divides **by** the make-matrix and never inverts it, so the solution is a non-negative series.
**Worked:** a hand-computed 2×2 economy converges in **11 iterations**, gap 3.7 × 10⁻¹². On Steedman's own counterexample the value allocation gives **v = [−1, 2]** and the physical allocation gives **p = [0.324, 0.235]**.
**Result:** **100% convergence and zero negative shares across 4,098 productive economies.** The rival value/price allocation goes negative or non-invertible in about **95%** of the same ones.
**Limit:** it proves no split is negative. **It does not prove the split is unique.**
**Points at:** Foundations §3.4a, §2.5.

### 7. `audits/` — do the integrity checks actually catch anything?

**Tests:** the twelve conformance constraints, made runnable.
**Maths:** recompute each check over a clean log, then inject one deliberate single-point violation per check.
**Worked:** 13 events, 12 checks, 12 injected violations, **12 catches**.
**Result:** all twelve pass clean and all twelve fire. **IC-1 to IC-9 need nothing but the ability to recompute** — no trust model, no authority, no outside data.
**Limit:** the report prints its own extent, and it says **closure basis: NONE on every axis.** Nothing here is checked against an independently measured physical total.
**Points at:** the conformance list; Foundations §4.3.

### 8. `ic-recompute-cost/` — can a stranger afford to check?

**Tests:** *"any stranger can recompute the verdict"* — which only decentralises anything if a stranger can pay for it.
**Maths:** scale a synthetic log to 10⁶, 10⁸ and 10⁹ events; time a full pass of IC-1 to IC-9 on one core.
**Worked:** 1,000,000 accounts, 64 materials, one core, no parallelism. At **10⁸ events** all nine checks take **9.8 s** — **10.2 million events a second**, holding 11.4 MB. At **10⁹ events**, **about 1.6 minutes**.
**Result:** a stranger can afford it. **And eight of the nine checks stream; IC-5 does not** — it compares one event to another, so it needs the log ordered by parcel.
**Points at:** Foundations §4.7, §3.1.

---

# D. What the books cannot see

### 9. `residual-unravelling/` — does staying unmeasured stop paying?

**Tests:** §4.4's rule that an estimate is computed over the **undisclosed leftover**, never over the whole population.
**Maths:** each round, estimate `R ÷ Z`; producers better than the estimate join and leave the pool, so the estimate rises for whoever remains.
**Worked:** the estimate applied to the undisclosed starts at **0.995** and ends at **18.23**, which is exactly the true median debit of whoever is still dark.
**Result:** **0.1% stay dark under the residual rule. 52.5% stay dark, stably, under the population rule the axioms reject.** §4.4 is load-bearing.
**Limit:** unravelling collapses once verification costs more than about **40%** of a median unit's debit, which makes cheap verification a precondition.
**Points at:** Foundations §4.4.

### 10. `correlated-miss/` — what if both instruments are blind in the same place?

**Tests:** whether the leftover `R = N − Y` is a lower bound when `N` and `Y` miss the same producers.
**Maths:** vary the correlation between the two blind spots and compare the published `R` against the true one.
**Worked:** **at full correlation the two instruments compute `N − Y = 0` and the network publishes 100% coverage over an extent it has not covered.**
**Result:** the error runs in the **flattering** direction at every level tested. **The published interval cannot express a shared blind spot**, because it is built from two blind spots stated separately — and a shared blind spot is not two.
**What refuses it:** the `not identified` default, and only if it is obeyed.
**Points at:** Foundations §4.4.

### 11. `cross-network-splitting/` — can a buyer split across two networks?

**Tests:** the consumption gate when one person holds two accounts.
**Maths:** credit is recorded on **both** networks (both see the same 24-hour day); debit lands on **one** per transaction, chosen by the seller. So the gate is checked against a divided debit and a whole credit.
**Worked:** with two networks and an even split, each sees half the debit → the escape factor is `1 ÷ 0.5` = **2.00×**. A 90/10 split is worth only **1.11×**.
**Result:** **no estimate closes it, at any ratio.** And the splitter does not look frugal — they sit **at the cap on every network**, which is the opposite shape every cohort rule looks for.
**What does see it:** the network's own coverage figure, falling from **74.8% to 51.9%** as splitters go from 1% to 50%. **The system notices; the individual is not caught.**
**Points at:** Foundations §4.1, §4.0.

### 12. `producer-side-splitting/` — and what does that do to the denominator?

**Tests:** `Z`, when a producer routes output through two networks and both remove them from it.
**Maths:** the hidden slice stays in the numerator `R`; the producer leaves the denominator `Z`. **Numerator up, denominator down.**
**Worked:** at 50% multi-homing, `R ÷ Z` charges a producer who joined nothing **1.73×** what they actually made. At 1% it is 1.01×.
**Result:** **it does not converge.** Onboard every producer in the region and the arithmetic reaches **`R ÷ 0`** with 35,484 t still unassigned and coverage stuck at 85%.
**The decisive test:** two constructed worlds give one network **identical** `Y`, `|registered|`, `N`, `n`, `Z` and `R` — to the last decimal — with truths **21% apart**. **No supersession rule computed from one book can separate them.**
**Points at:** Foundations §4.4, §4.2; **OP-28**.

### 13. `residual-attribution/` — should the leftover be shared out at all?

**Tests:** three proposed rules for assigning `R` to people, against holding it unassigned.
**Maths:** score each rule by what it binds correctly, what it charges to somebody who hid nothing, and **its correlation with the truth**.
**Worked:** correlation between charge and true hidden output — **R1 spread +0.000 · R2 top-up −0.109 · R3 shape +0.019.** A witness would score near 1.
**Result:** **none of the three is a witness, and R2 is inverted** — it charges in proportion to what was recorded, and the hider recorded less, so it bills the hider **16.6 t** and the honest producer **32.7 t**.
**A floor nobody can tune:** **57%** of the leftover belongs to producers outside the network, whom §4.1 forbids charging. Every allocating rule mis-charges at least that much.
**Points at:** Foundations §4.4, §4.1.

---

# E. What the numbers do to a society

### 14. `scenario-suite/` — five questions at national scale

**Tests:** whether the accounting produces sane answers on real distributions.
**Points at:** Foundations §3.5, §5.5.8, §3.6.

| | The question | The finding |
|---|---|---|
| **Q1** | An America that traded with nobody | Not short of labour, land, water or food. **Energy binds** — 0.19 of what a median standard needs at the current build, against land at 1.10 and water at 5.22 |
| **Q2** | Labour captured or spent on enforcement | **About 185–396 hours per adult per year**, a combined **36%** — de-duplicated, not summed |
| **Q3** | What plastic costs in hours | Ocean cleanup ≈ **950 h/tonne** — roughly **70×** the labour to make it new. **Microplastic has no figure, and that is the finding** |
| **Q4** | Who is already locked out | Strip out paper wealth and only **0.1–2%** of Americans are permanently locked out — **the ultra-consumers, not the merely rich.** Money wealth reaches ~10⁶× the median; material consumption only ~**670×** |
| **Q5** | Moving labour from wasteful to essential | The freed labour — **1.1 to 2.4 trillion hours a year** — closes the global health-worker shortage **50 to 100 times over** |

---

# F. Checking our own instruments

### 15. `ceiling-rubric/` — is our headline statistic a detector?

**Tests:** the row reporting that the ceiling does not move under fraud, scored as a detector rather than read as reassurance.
**Maths:** freeze the population rule and hash it **before** computing anything. Then inject six challenges with known ground truth and ask whether the statistic moves.
**Worked:** phantom accounts **+0.000** · a random fifth deleted **+0.000** · 40% of books inflated **+0.000** · collusive hand-offs **+0.000** · the top percentile deleted **−0.153** · an account credited at 30 h/day **+0.600**.
**Result:** **1 of 3 legs.** Sensitivity fails. Specificity passes **because the statistic never moves**, so the pass carries nothing. Coverage cannot be scored at all — a generated population has no outside.
**The finding:** its expressiveness is **one-sided**. A maximum can be pushed **down** by deletion and never **up**, because IC-7 caps the top. **Every fraud that pays pushes up, and up is where it cannot go.**
**What survives:** **the bound `24 ÷ F` is untouched.** What fails is reading the fraud row as corroboration of it. **It bounds; it does not witness.**
**Points at:** Foundations §5.5.7, §4.3.

---

## The scorecard

| Verdict | Projects |
|---|---|
| **Closed, and the claim holds** | allocation-engine · audits · ic-recompute-cost · pledge-reserve · statera |
| **Closed, and the claim is narrower than it was** | disparity-ceiling · median-lifestyle · stable-band · scenario-suite |
| **Found a real defect in our own work** | correlated-miss · residual-unravelling · ceiling-rubric |
| **Confirmed an open problem with digits** | cross-network-splitting · producer-side-splitting · residual-attribution |

**Five of the fifteen came from outside critics**, and four of those found something the documents had wrong.

---

## What none of this shows

**1. Constructed digits are not measured ones.** Every project says which of its numbers are measured and which are illustrative. **The median-lifestyle anchor and the scenario suite are built on published statistics. Most of the rest run on synthetic populations**, where the shape is the result and the magnitudes are not.

**2. A simulation has no outside.** Entry 15 is the general form: a generated population cannot supply a witness that it is complete, because the generator is the thing being checked. **On real books that witness exists and it is `N`.**

**3. Nothing here has run in a real economy**, because no trust network exists yet.

## Running any of it

Every project takes the same two commands, from inside its own folder:

```bash
python <the_script>.py --test
```

```bash
python <the_script>.py
```

**Every project's self-tests are written to be able to fail**, and several have — the failures are recorded in each `CHANGELOG.md` rather than tidied away.
