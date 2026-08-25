# Statera — Amendment Record

> Version-by-version change history for [`statera.py`](statera.py) and its project page [`README.md`](README.md). Newest entry first. Read this only when tracing **when and why** something changed.
>
> **Named 2026-08-23.** Until then this was "the kernel", and the v0.1 entry below was written under that name. A *statera* is the balance-scale the goddess Aequitas holds on Roman coinage — **an instrument**, which is what this is. Files moved `kernel.py` → `statera.py` and `KERNEL*.md` → `STATERA*.md` the same day. **The v0.1 entry is left as it was written; history does not get re-threaded.**
>
> The kernel is **step 1** of [`../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md`](../../00-strategy/Aequitas_Simulation_Roadmap_v0.2.md). It is an instrument for testing the theory. It is **not** a trust-network database, and it is **not** a first version of Aequitas — see Foundations §1.2 (the scope section, *"what Aequitas is, and what is therefore out of scope"*) in [`../../00-strategy/Aequitas_Foundations_v0.19.md`](../../99-archive/Aequitas_Foundations_v0.19.md).

---

<!-- tag: sta-critique-fixes-2026-08-24 -->
### 2026-08-24 — three code fixes from the outside-critique run

The five-model outside critique (`07-outreach/critique/REPORT_v0.1.md`) found three kernel defects. All fixed. #12 and #13 were the *simulation failing to obey a spec that was already correct*; #11 implements a Foundations mechanism (§6.2b) the kernel had left out. No Foundations ruling moved.

**Finding #13 — a hand-off created or destroyed matter across different-sized cohorts.** `Chain.handoff` wrote the same per-exemplar quantity to both sides of a custody change and was **not** tagged for the conservation check, so trade between a headcount-1 producer and a headcount-100 consumer silently invented matter (100 receivers each took the full amount the one sender shed). Fixed in [`chains.py`](chains.py): the receiver's per-exemplar quantity is now scaled by `headcount(frm)/headcount(to)`, and the pair is tagged as a conservation process so `check_conservation` weighs both sides by headcount. **Scale is 1.0 when headcounts match, so every existing headcount-1 chain is byte-identical.** New test: `test_a_handoff_conserves_across_different_headcounts`.

**Finding #12 — the ratio gate could be silently made non-binding.** The gate is `rho·C − collapse(D, weights)` with credit `C` in labour-hours, but a weighting model that zeroed `labour_h` (settable straight from a scenario's `[dials.weights]` TOML) made the collapsed debit ignore everything `consume()` records, so consumption was unbounded. And the planned §7 "discovered pollutant" shock multiplied `mass_kg`'s **0.0** default weight — `1.25 × 0.0 = 0.0` — so the headline re-weight scenario would have proved nothing. Fixed in [`statera.py`](statera.py): new `validate_gate_weights` pins `labour_h = 1.0` and forbids negative mitigation weights, called at kernel construction and at scenario `--check` time ([`run_scenario.py`](run_scenario.py)). New tests: `test_a_zeroed_labour_weight_is_refused`, `test_a_reweight_moves_a_number`. [`STATERA_PLAN_v0.2.md`](STATERA_PLAN_v0.2.md) §7 gains a warning that the pollutant shock must start from a non-zero weight.

**Finding #11 — pledges granted no debit-room to a recipient.** `frontload` recorded the pledger's budget draw (IC-8) but never the *grant* Sec.6.2b confers on the bearer, so `room()` had no term for it and the Front-Loading Rule was asserted by the healthcare/entertainment chains without being run — the chains only passed because a 120-year warm-up left every actor credit-rich. Implemented as **earmarked grants** (author decision, 2026-08-24): the bearer's creation-cost row is flagged `creation=True`; a pledge records a `grant_h` on the bearer; `room()` adds `min(granted, creation_cost)`. The offset cushions that specific bite down to zero and **never becomes spendable headroom** (Sec.6.4c — pledge surplus is non-consumable), and nothing leaves the ledger (A1 — the creation-cost debit stays in `D`). New columns `grant_h` and `creation` on the log; new projections `granted()` and `creation_cost()`; new `check_grants` asserting granted room is backed by real pledging budget. New test `test_a_pledge_grants_earmarked_debit_room`: a one-year-old co-op locked out by a 30,000 h creation-cost is cushioned exactly by a matching pledge, and an over-pledge adds nothing.

**Kernel self-tests 24 → 27, chain tests 14 → 16, all green.**

---

<!-- tag: sta-reorg-2026-08-24 -->
### 2026-08-24 — moved into its own folder. No behaviour changed.

`06-simulation/` was a flat directory of about 94 files. It is now one folder per project. Statera's files moved from `06-simulation/` to `06-simulation/statera/`, and `scenarios/` came with them.

| Was | Is now |
|---|---|
| `06-simulation/STATERA.md` | `06-simulation/statera/README.md` |
| `06-simulation/STATERA_CHANGELOG.md` | `06-simulation/statera/CHANGELOG.md` (this file) |
| `06-simulation/scenarios/*.toml` | `06-simulation/statera/scenarios/*.toml` |

**One code change, and it is a path only.** `statera.py` imports the published disparity-ceiling calibration from `disparity_ceiling_sim`, which now lives in a sibling folder, so four lines were added to put that folder on the import path. Nothing the kernel computes was touched.

**A results summary was added** — [`RESULTS.md`](RESULTS.md) — so the headline numbers can be read without re-running anything.

**Verified after the move:** `python statera.py --test` 25 tests pass, `python chains.py --test` 14 tests pass, `python run_scenario.py scenarios/baseline.toml --check` validates. Both reproduction targets still exact.

---

<!-- tag: sta-v0-2-2026-08-23 -->
### v0.2 (2026-08-23) — a name, a time axis, five chains, and two axiom breaches fixed

**Tracks Foundations v0.19.** `statera.py` 1,176 lines / **25 tests** · `chains.py` 698 lines / **14 tests** · `run_scenario.py` 251 lines. **Both reproduction targets still exact through three refactors.**

---

#### What changed — in plain words

| New | In plain words |
|---|---|
| **A name** | Statera. The balance-scale Aequitas holds. An **instrument**. |
| **Headcounts** | One log row can now speak for many identical people. **At a headcount of 1 it behaves exactly as before**, which is what keeps the old tests meaningful. |
| **Time** | Days pass. Periods can be a day, a month, or a year. Every rule is checked **every period**. |
| **Ages** | People are born, grow older, and die. **Their records stay after death.** |
| **Five supply chains** | Housing, transport, food, healthcare, entertainment — modelled step by step. |
| **A settings file** | A human can now run it without writing Python. |
| **Shelf life** | Food goes off, and after that nobody can pass it on. |
| **Breathing** | Every person's exhaled CO₂ is on the ledger — **and costs nothing.** |

---

#### 1. Steps 1–4 of the plan, built and green

1. **The headcount column.** Everything in the log stays **per person**; aggregate views multiply. IC-7 and IC-8 are claims about an individual and are never scaled. **IC-1/IC-2 are the one check that must weigh by headcount**, because matter balances over a population: one factory making 10 kg for 100 people taking 0.1 kg each reads a false 9.9 kg leak unless both sides are scaled.
2. **The time axis.** `days_per_period` is a dial, and **IC-7's 24-hour cap scales with it** — without that, the cap fires on the first month of any run coarser than daily, and generational scenarios (70–170 years) are impossible.
3. **Ages, births, deaths.** Cohorts are pre-allocated slots with a birth period and a lifespan. Death stops accrual and consumption; **rows are never removed** (§5.4). Mortality thins a headcount without touching what one person did.
4. **Five exemplar chains.** `Chain` is a **recorder, not a second engine** — it appends into the same log and the ordinary checks police it. A process that will not balance is refused at build time.

#### 2. 🔴 Two axiom breaches, found by the white paper and fixed

**Both were found by writing the reference paper, which is the argument for writing it.**

1. **A pledge was shrinking the pledger's own credit and consumption room.** `pledge()` writes a negative credit row to draw down the lifetime pledging budget, and `credit()` summed every credit column. **Measured: earn 12 h, pledge 5 h, credit reads 7.0 and room falls 18 → 10.5.** Foundations says the opposite in four places — **A3**, **§6.4** twice, and the function's own docstring. Fixed: credit sums crediting kinds only, and the pledging budget is a separate quantity capped by IC-8. **No published result was affected; nothing had ever pledged.**
2. **`check_transaction_time` was killing runs for the people §7.5 protects.** Essentials are ungated and taken first, so they can push debit past the gate; the next discretionary event then recorded negative room **while admitting zero**, and the check raised on the *sign of the room*. Fixed to test the real §3.3 invariant: an admission never exceeded the room that existed when it happened.

**Also:** the re-weight half of that check computed a value and discarded it, asserting nothing. It now asserts that a heavier weighting shrinks *future* room and leaves every recorded past event untouched. And `check_essentials_never_gated` now states in its own docstring that it is close to vacuous and that the real guarantee is behavioural.

#### 3. Custody, shelf life, and disposal — author rulings

**Full paper: [`../../00-strategy/Shelf_life_and_custody_v0.1.md`](../../00-strategy/Shelf_life_and_custody_v0.1.md).**

1. **The custody chain ending IS the fate.** A loaf and its plastic bag both took resources; both chains stop at the eater; that puts both on the eater's ledger. **No 'eaten' event and no 'thrown away' event.** This is **§3.6 rule 1** almost word for word, and it **dissolved a limitation** recorded earlier the same day — Statera does not need to tell property debit from consumption debit, because whose ledger it sits on is the only question the accounting asks.
2. **Single-use goods are not holding-time split.** §6.2a's own test: does the thing survive the process? **Split a loaf by holding time and someone who ate it quickly would owe less than someone who left it on the counter for a week.**
3. **Shelf life is §3.6 rule 1 with a clock on it.** Goods carry an expiry; past it, the hand-off is refused. **A softer "priced, not forbidden" version was built first and overturned by the author**, correctly: waste disposal is a *service* and never needed the transfer path; a food bank relying on gifted bread is a symptom of the scarcity Aequitas claims to remove; and *"a prohibition needs somebody at the door"* confused **a rule that forbids with an institution that enforces** — IC-7 forbids a 25-hour day and nobody guards it.
4. **Disposal is a service with a cost.** The material stays with whoever let it become waste, the processor is credited for the work, the holder pays for it. **Recycling is the one case where atoms move on** (§3.6 rule 3), carrying property debit forward but never prior producers' pollution.

#### 4. Breathing is on the ledger, and weighs nothing

**A1 reaches "down to the oxygen a human inhales and the CO₂ they exhale."** ~1 kg per person per day, recorded on the self-care row. **§3.3 weighs it at zero**, because respiration is inside the short carbon cycle and therefore at baseline.

> **A year of breathing records 365 kg in the log and costs 0 hours.** Both true at once — **the clearest case in the kernel for why §3.2a keeps the debit as a vector.** One collapsed number could not hold both facts.

#### 5. ⚠️ A correction to v0.1's headline low-floor figure

**v0.1 quoted a single sample size as though it were the result.** Same seed, four sample sizes, at a 2-hour floor: **10.49× / 10.76× / 10.22× / 10.63×** (N = 20k / 50k / 200k / 500k), with top workers at 21.0 / 21.5 / 20.4 / 21.3 h/day.

- **The bound never moves.** Exact at every floor and every N.
- **From `F` = 6 h upward the population fills it exactly, at every N.**
- **Below that the observed spread falls short and wanders**, and is **not monotone in N** — each sample size draws a different random stream and the maximum of a truncated normal is itself a random variable.

> **The qualitative finding is robust: below about a 6-hour floor, human endurance binds before the accounting does.** The specific figure is not, and must never be quoted without its N. **This is the third time this project has stated a bound proved inside a boundary without the boundary.**

#### 6. New capabilities worth naming

- **`run_scenario.py` + TOML scenarios.** A settings file a human edits, with comments explaining each dial. **Unknown keys are an error, never ignored.** Every report ends with a **COVERAGE line calling its own figures a floor** — conformance requirement 13, built in rather than bolted on.
- **12 of the 16 conformance requirements are now expressible, up from 10.** Requirement 2 (causer attribution) arrived with the chains; requirement 13 (publish a floor) with the runner. **Still out of reach: 6, 12, 14, 15, 16.**

---

<!-- tag: krn-v0-1-2026-08-23 -->
### v0.1 (2026-08-23) — the kernel exists

**Tracks Foundations v0.19.** 793 lines. 12 self-tests, all pass. Run: `python statera.py --test`.

---

#### What the kernel does — in plain words

**The kernel is one shared engine. Every future test scenario runs on it.**

| It does this | In plain words |
|---|---|
| Keeps an **event log** | A list of things that happened. You can only add to it. You cannot delete or edit. |
| **Builds accounts on demand** | It never saves a balance. It adds up the list each time you ask. |
| **Gives credit for hours** | Two kinds: self-care hours (the work of staying alive) and work hours. |
| **Keeps cost in 3 separate units** | Hours, kilograms, megajoules. It squashes them into one number only when you ask it to. |
| **Runs the gate** | You may consume up to `rho × your credit`, minus what you already owe. `rho` (the gate dial) is a number the trust network picks. |
| **Never blocks essentials** | Food and care pass the gate even when `rho` is 0.01. |
| **Checks 8 rules every run** | If a rule breaks, the run stops and shouts. |
| **Re-proves 2 old results** | The 2.40× spread at a 10-hour floor, and the clearing rate `rho*` = 1.20. |
| **Makes the floor `F` a real dial** | `F` is the self-care floor in hours per day. Fixed this version. Before, moving it changed nothing. |

**What it cannot do yet:**

- **Only one time step.** No days passing. This is the next job.
- **Toy economy.** One product. No industries, no supply chains.
- **No agent behaviour.** People ask and get gated. Nobody joins, leaves, or cheats.
- **No money side.** No second economy to trade with, so Foundations §5.5 (parallel implementation — trading across the money boundary) cannot be tested.
- **7 of the 17 rules** in `Aequitas_Conformance_v0.2.md` (the conformance list — the things that must be true for an implementation to be Aequitas) cannot be tested yet. Missing: numbers 2, 6, 12, 13, 14, 15 and 16 — causer attribution, annotate-never-delete, basis and extent, the floor rule, residual estimation, and published methods.

---

#### 1. Why it was built

**Nothing in `06-simulation/` was the kernel.** Every script wrote its own credit accrual, its own gate, and its own agents. That is why each script answers one question and none of them join up. This is the shared core, written once.

#### 2. The three design decisions

1. **The log is columnar, and that is what makes A6 (derived, not stored) affordable.** Events are parallel numpy arrays. Deriving the ledger is a segment sum (`np.bincount`) over the actor column. **200,000 agents and 600,000 events derive in milliseconds**, so the honest thing and the fast thing are the same thing. `Conformance.check_a6` recomputes from scratch and asserts the cache agrees — the cache is a projection, the log is the authority.
2. **The debit is a vector and the collapse is a separate, explicit step (§3.2a).** `collapse()` is the only place a weighting model is applied. `divide()` refuses a collapsed figure and raises `TypeError`. **The side entrance into OP-10 (weighting governance) is closed by the type signature, not by a rule someone has to remember.**
3. **The gate records what was true when it ran (§3.3, the transaction-time rule).** Each consumption event stores the `rho` and the room that held at that moment. `check_transaction_time` re-weights the whole history and asserts no past event becomes a violation.

#### 3. The two reproduction targets, both hit exactly

The roadmap's guard against building a framework nobody uses: **the kernel must re-derive published results before a single new scenario runs.** Both are driven through the kernel's own log and gate, not through the closed-form arithmetic the original scripts use.

- **The disparity ceiling at a 10-hour floor:** 2.4000× at every `rho` in [1, 3]. Spread across the sweep 8.9 × 10⁻¹⁶ — floating-point noise. Matches [`disparity_ceiling_sim.py`](../disparity-ceiling/disparity_ceiling_sim.py), N = 200,000.
- **The clearing rate:** `rho*` = 1.20, median gets 0.92×, 35% constrained, disparity ≤ 2.40×. Matches [`rho_sweep.py`](../disparity-ceiling/rho_sweep.py), US production method.

#### 4. The floor `F` was not a dial, and now is — author catch, 2026-08-23

**The kernel had a `floor_h` setting that changed nothing.** The population was always built around `F` = 10. Credit is `min(r,f) + max(r−f,0) = r` for any `f ≤ r`, so moving the dial moved no number in the run. **The floor appeared only in the divisor when reporting a ceiling — dividing by a floor agent who was not in the simulation.**

> **A floor that no agent sits at is not a floor.**

`draw_population` now takes the floor as a parameter, so the lowest agent genuinely sits at `F` and the range is `[F, 24]`. Guarded by `test_floor_is_a_real_dial`, which asserts the bound moves **and** that some agent actually sits at the floor.

**This was the third instance of the project's known over-claim shape: a bound proved inside a boundary, stated without the boundary.** Every report of a disparity figure must name the floor it assumed.

#### 5. A new empirical result — a low floor is not filled

Sweep at `rho` = 1.5, N = 50,000:

| floor `F` | bound `24/F` | observed | top worker |
|---|---|---|---|
| 2 h | **12.00×** | 10.76× | 21.5 h/day |
| 4 h | **6.00×** | 5.88× | 23.5 h/day |
| 6 h | **4.00×** | 4.00× | 24.0 h/day |
| 10 h | **2.40×** | 2.40× | 24.0 h/day |
| 14 h | **1.71×** | 1.71× | 24.0 h/day |

**Below about a 6-hour floor, human endurance binds before the accounting does.** Reaching a 12× spread needs somebody working a 22-hour day, and the most anyone manages is 21.5. **So Foundations §7.5 condition 1 — *"the floor stays in a narrow band"* — is a slightly weaker worry than it reads.** Both numbers must always be reported; neither substitutes for the other.

*Honest limit: this is a property of the population model (35% doing little paid work, the rest centred on ~6 h with a 3 h spread). What is robust is that the bound and the observed spread come apart at a low floor, not the exact figure at which they do.*

#### 6. What the conformance layer catches

Each check was tested by deliberately breaking it.

| Check | Requirement | Caught in test |
|---|---|---|
| **IC-7** (the 24-hour cap) | ≤ 24 h of activity per 24 h | a 32-hour day |
| **IC-8** (pledge backing) | pledges ≤ lifetime earned credit, 1:1 | 25 h pledged on 12 h earned |
| **IC-1 / IC-2** (mass and energy conservation) | conserve per process | a 3 kg leak |
| **A3** (non-fungibility) | credit never transfers, never spent by a purchase | a transfer carrying credit |
| **A6** (derived, not stored) | ledger derived, never stored | cache disagreeing with the log |
| **§3.2a** | divide per dimension, before collapsing | `divide()` on a collapsed figure |
| **§7.5** (the basic-needs floor) | essentials never gated | `rho` = 0.01 refuses discretionary, admits essentials |
| **§5.4** (no erasure) | append-only | `EventLog` exposes no delete, truncate, or edit |

**A failure raises `ConformanceError` and stops the run.** Either the scenario is malformed or the theory has a hole — both are results. **A simulator that cannot fail cannot teach.**

#### 7. Honest limits on the numbers

**The absolute figures inherit their calibration.** `rho*` depends on OP-10 (weighting governance) and is illustrative, exactly as [`RHO_SWEEP.md`](../disparity-ceiling/RHO_SWEEP.md) says. What is claimed here is that **the kernel reproduces them**, not that they are settled.

---

*No axiom was contradicted in this version. Companion doc: [`STATERA.md`](README.md).*
