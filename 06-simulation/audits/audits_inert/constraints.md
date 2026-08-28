# The twelve constraints, stated in arithmetic

**Hand-written. Not generated.** Mathematics cannot be mechanically exported from an implementation, so this file is written by a person reading [`arithmetic_audits.py`](../arithmetic_audits.py) line by line. Where the code does something this page does not say, that is recorded in [`expected_verdicts.md` section 4](expected_verdicts.md#4-where-the-python-and-the-stated-mathematics-disagree) rather than smoothed over.

**IC** means *integrity constraint*. The twelve are defined in `Aequitas_EventLog_v0.8.md` (superseded; held locally) section 7. IC-1 to IC-9 are **log-side**: they read only the recorded events. IC-10 to IC-12 are **projection-side**: they also read a published process-energetics model, which is a set of chosen numbers that is not part of the log.

Every worked example below uses digits from [`fixture.json`](fixture.json). Every result was printed by a real run and is recorded in [`worked_arithmetic.json`](worked_arithmetic.json) and [`expected_verdicts.json`](expected_verdicts.json). No number on this page was typed from memory.

---

## Notation

| symbol | meaning |
|---|---|
| `E` | the set of events. Here 13 of them: G1, G2, D1, E1–E8, E10, E11. |
| `In(e)`, `Out(e)` | the input and output flows of event `e` |
| `Ag(e)` | the agent roles of event `e` |
| `D(e)` | event `e`'s declared dissipated energy, in joules |
| `start(e)`, `end(e)` | event `e`'s bounds, in absolute TAI seconds |
| `kind(f)` | `parcel` or `reservoir` |
| `id(f)`, `sub(f)`, `mag(f)`, `unit(f)`, `cust(f)` | a flow's endpoint id, substance, magnitude, unit (`kg` or `J`), and holding account |
| `P` | the set of parcels. Here 6: P:tool, P:part, P:grain, P:flour, P:bran, P:bread. Parcels are **derived by replaying the log**, not authored. |
| `R` | the registered reservoir set. Here 6 names, listed in `fixture.json` under `reservoirs_registered`. |
| `Q` | the set of pledges. Here 4: PL1–PL4. |
| `t_now` | the instant the verdict is taken. Here **626 400 s** (day 7.25). |
| `TOL` | the tolerance below which a difference is treated as zero. **1e-9** throughout. |

Time is absolute seconds. `day(d, h) = d × 86400 + h × 3600`. One day is 86 400 s; one hour is 3 600 s.

**A genesis event** is one whose process name begins `proc:genesis`. It admits an object that existed before the ledger did. Here: G1 (a 5.0 kg steel tool) and G2 (a 0.1 kg steel part).

---

## IC-1 — mass balance

**Statement.** For every event `e` in `E` whose process does **not** begin `proc:genesis`:

```
  SUM over f in In(e)  with unit(f) = kg  of mag(f)
=
  SUM over f in Out(e) with unit(f) = kg  of mag(f)
```

**Domain.** 11 of the 13 events. G1 and G2 are exempt: a genesis entry admits mass that came from the untracked past, so it has no input side to balance against. Closing that hole is IC-3's job, not IC-1's.

**Worked example — E6, baking.**

| side | flow | kg |
|---|---|---|
| in | P:flour | 7.0 |
| in | water from `watershed:local` | 3.0 |
| in | natural gas from `energy:gas` | *(200 J — not kg, so not in this sum)* |
| | **total in** | **10.0** |
| out | P:bread | 9.5 |
| out | water vapour to `airshed:local` | 0.5 |
| | **total out** | **10.0** |

`10.0 − 10.0 = 0`. The constraint holds.

**Injection INJ-1.** Bread is raised from 9.5 kg to 10.5 kg. Outputs then total 11.0 kg. **The residual is 10.0 − 11.0 = −1.0 kg.**

> The source comment in `violate_ic1` calls this "+0.5 kg". It is 1.0 kg. See note N5.

---

## IC-2 — energy balance

**Statement.** For every event `e` in `E` whose process does not begin `proc:genesis`:

```
  SUM over f in In(e)  with unit(f) = J of mag(f)
=
  SUM over f in Out(e) with unit(f) = J of mag(f)  +  D(e)
```

`D(e)` is the waste heat the event declares. Energy that leaves as heat still has to be written down.

**Domain.** The same 11 events. Only two of them carry any energy at all: E3 (milling, 100 J) and E6 (baking, 200 J).

**Worked example — E3, milling.** In: 100.0 J of electricity from `energy:grid`. Out: no energy flows, so 0. Declared dissipation: 100.0 J.

`100.0 − (0 + 100.0) = 0`. The constraint holds.

**Injection INJ-2.** E6's declared dissipation is set to 0 while its 200 J gas input stays. **The residual is 200.0 − (0 + 0.0) = 200.0 J.**

---

## IC-3 — origin closure

**Statement.** Every parcel must reach a valid origin by walking backwards through the events that made it. Define `valid(p)` for a parcel `p`, walking with a set `S` of parcels already on the current path:

1. If `p` is already in `S`, `valid(p)` is **false**. (A cycle with no root.)
2. If `p` has no creating event, `valid(p)` is **false**. (A parcel that appears from nowhere.)
3. If `p` was admitted by a genesis event, `valid(p)` is **true**.
4. Else if `p` was created straight from reservoirs — its creating event has at least one reservoir input and **no** parcel inputs — then `valid(p)` is true if and only if **every** reservoir input of that event has its id in `R`. One unregistered draw is enough to make it false, however many registered ones sit beside it.
5. Else let `Par(p)` be the parcel inputs of `p`'s creating event. `valid(p)` is true if and only if `Par(p)` is non-empty **and** `valid(q)` is true for every `q` in `Par(p)`.

The constraint is: `valid(p)` for every `p` in `P`.

**This is a reachability test, not a balance.** When it fails there is no quantity that is off by an amount. What fails is a count: the parcel reaches **0** valid origins where it needs **1**.

**Domain.** All 6 parcels.

**Worked example — P:bread.** Created by E6. Parcel inputs of E6: {P:flour}. P:flour was created by E3; parcel inputs of E3: {P:grain}. P:grain was created by E1, which has no parcel inputs and one reservoir input, `soil:field-01`, which is in `R`. So the chain closes in three steps:

```
P:bread  <-  P:flour  <-  P:grain  <-  soil:field-01  (registered)
```

P:tool and P:part close in one step each, by rule 3.

**Injection INJ-3.** E6's flour input is renamed `P:phantom-flour`, which no event creates, and E5's output is renamed too so the chain is genuinely broken rather than relabelled end to end. `Par(P:bread) = {P:phantom-flour}`, which has no creating event, so rule 2 makes it false. **P:bread reaches 0 valid origins.**

---

## IC-4 — fate closure

**Statement.** Define the status of parcel `p` at instant `t`:

- If `p` has no creation record, or was created after `t`: **unaccounted**.
- Else if `p` has a destroying event and was destroyed at or before `t`, let `Res` be that event's **non-parcel** output flows whose substance equals `sub(p)`:
  - `Res` is empty → **consumed**
  - every flow in `Res` has an endpoint id in `R` → **released**
  - otherwise → **unaccounted**
- Else: **held**.

The constraint is: no parcel is **unaccounted** at `t_now`.

Held is a valid fate. Owning a durable good forever is not a violation.

> **The substance test matters and the prose about this check does not mention it.** See note N7.

**Domain.** All 6 parcels, at `t_now` = 626 400 s.

**Worked examples.**

| parcel | destroying event | that event's same-substance reservoir outputs | status |
|---|---|---|---|
| P:bran (`sub:wheat.bran`) | E4 at 205 200 s | `soil:field-01`, `sub:wheat.bran`, 3.0 kg — registered | **released** |
| P:bread (`sub:bread`) | E8 at 475 200 s | none: E8 emits `sub:CO2+H2O` and `sub:waste`, neither is `sub:bread` | **consumed** |
| P:tool | none | — | **held** |

**Injection INJ-4.** E4's reservoir endpoint is changed from `soil:field-01` to `void:unregistered-sink`, which is not in `R`. P:bran becomes unaccounted. **3.0 kg leaves the accounted world through an endpoint the registry does not name.**

---

## IC-5 — custody continuity

**Statement.** For each parcel `p`, take the events that touch `p`, in ascending `start`. Carry a holder `h`, initially undefined. For each such event `e`:

1. If `e` has an input flow `f` for `p` **and** `h` is defined, require `cust(f) = h`.
2. If `e` has an output flow `g` for `p`, set `h := cust(g)`.
3. Otherwise, if `e` had an input flow for `p`, set `h := undefined`.

The constraint is: rule 1 never fails.

**When this fails there is no numeric residual.** Two different account names appear where the log requires one.

**Domain.** All 6 parcels, 16 parcel-touching event steps in total.

**Worked example — P:grain.**

| event | holder before | declared source | declared destination | holder after |
|---|---|---|---|---|
| E1 (cultivation) | undefined | — | farmer | farmer |
| E2 (transport) | farmer | farmer ✓ | miller | miller |
| E3 (milling) | miller | miller ✓ | *(consumed)* | undefined |

**Injection INJ-5.** E3 declares its grain input was held by `stranger`. At that step `h` is `miller`. **Declared `stranger`, actual `miller`.**

---

## IC-6 — interval sanity

**Statement.** For every event `e` and every parcel input flow `f` of `e` whose parcel `p` has a creation record:

```
  start(e)  >=  created_at(p)                                  (not before it existed)
  start(e)  <=  destroyed_at(p)   unless e IS p's destroyer     (not after it was gone)
```

Both are checked with tolerance `TOL`. A parcel with **no** creation record is skipped here; that is IC-3's failure to report, not IC-6's.

**Domain.** 10 parcel input flows, spread over 9 events.

**Worked example — E6 consuming P:flour.** P:flour was created by E3 at 194 400 s. E6 starts at 367 200 s. `367 200 − 194 400 = +172 800 s`, so the flour is two days old when it is baked. Its destroying event is E6 itself, so the second clause does not apply.

**Injection INJ-6.** E6 is moved back one day, to 108 000 s. P:flour is still created at 194 400 s. **`108 000 − 194 400 = −86 400 s`: the bread is baked exactly one day before the flour exists.**

---

## IC-7 — agent-time cap

**Statement.** For each account `a`, let `Roles(a)` be every agent role in the log with that account. For each role `r0` in `Roles(a)`, define the window `W = [start(r0), start(r0) + 86400)`. Then:

```
  busy(a, W)  =  SUM over r in Roles(a) of  max(0,  min(end(r), W_end) - max(start(r), W_start))

  busy(a, W)  <=  86400 seconds,  for every a and every W
```

**Overlapping roles are counted twice, and that is the point.** If a person is credited for two jobs running at the same time, the sum exceeds the wall clock, and no other check would notice.

**Why windows are anchored at role starts.** A window with the most work in it can always be slid until its left edge sits on some role's start without losing any of that work. Checking those starts therefore checks the worst case.

**Domain.** 6 accounts, 8 roles between them.

**Worked example — the farmer, clean log.** Two roles: cultivation in E1, `[21 600, 43 200)` = 6.0 h; eating in E8, `[475 200, 476 100)` = 0.25 h.

- Window from 21 600: covers the first role whole, the second not at all. `busy = 21 600 s = 6.0 h`.
- Window from 475 200: `busy = 900 s = 0.25 h`.

Worst is 6.0 h, well under 24.

**Injection INJ-7.** The cultivation role is stretched to `[0, 72 000)` = 20 h and the eating role to `[18 000, 54 000)` = 10 h, so they overlap on `[18 000, 54 000)`. The window from 0 covers both entirely:

```
  busy = 72 000 + 36 000 = 108 000 s = 30.0 h
  cap  =                    86 400 s = 24.0 h
```

**Over by 6.0 hours.**

---

## IC-8 — pledge backing

**Statement.** For every account `a`:

```
  SUM over q in Q with pledger(q) = a  of  hours(q)
    <=
  SUM over e in E, over r in Ag(e) with account(r) = a  of  (end(r) - start(r)) / 3600
```

The left side runs over **every pledge the account ever made** — discharged, still outstanding, and burned alike. Pledging spends a lifetime budget permanently. A pledge that burned still spent it.

**Domain.** 6 accounts. Two of them have pledges.

**Worked example — clean log.**

| account | pledges | pledged h | roles | earned h | headroom |
|---|---|---|---|---|---|
| farmer | PL1 3.0 (discharged) + PL3 2.0 (outstanding) | **5.0** | E1 6.0 + E8 0.25 | **6.25** | 1.25 |
| baker | PL2 1.0 (discharged) + PL4 2.0 (**burned**) | **3.0** | E6 4.0 | **4.0** | 1.0 |

The baker's row is the one that shows the rule. PL4 reached its expiry unspent, so its budget is gone — and it still counts against the cap.

**Injection INJ-8.** PL3 is raised from 2 h to 100 h. The farmer's cumulative pledges become `3.0 + 100.0 = 103.0 h` against 6.25 h earned. **Over by 96.75 hours.**

---

## IC-9 — pledge discharge

**Statement.** For every pledge `q` with `discharged_by(q)` not null:

1. There is an event `e` in `E` with `id(e) = discharged_by(q)`.
2. `start(e) <= expires_at(q)`, within `TOL`.

A pledge with `discharged_by = null` is **outstanding** if `t_now < expires_at(q)` and **burned** if not. Burned is a terminal state, not a violation. Burned and discharged are mutually exclusive: once a pledge burns, nothing can later discharge it.

**Domain.** 4 pledges, 2 of them discharged.

**Worked example — clean log.**

| pledge | state | discharged by | discharge instant | expiry | margin |
|---|---|---|---|---|---|
| PL1 | discharged | E10 | 540 000 s | 2 613 600 s | 2 073 600 s early |
| PL2 | discharged | E11 | 561 600 s | 2 613 600 s | 2 052 000 s early |
| PL3 | outstanding | — | — | 2 613 600 s | expiry is after `t_now` |
| PL4 | **burned** | — | — | 583 200 s | expiry is before `t_now` = 626 400 s |

**Injection INJ-9.** PL1's expiry is pulled back to 453 600 s while E10 still discharges it at 540 000 s. **`540 000 − 453 600 = 86 400 s`: the discharge lands exactly one day after the pledge had already burned.**

---

## IC-10 — non-negative allocation

This check has two layers.

### Layer (a) — the direct split

**The split is never stored on an event.** There is no field for it. It is computed when a projection is taken.

For an event `e` with **two or more parcel outputs**, and for a dimension `d`:

```
  mass:    theta_mass(e)[id(f)]  =  mag(f) / SUM over parcel outputs g of e with unit(g)=kg of mag(g)
           defined only for the parcel outputs f with unit(f)=kg; an output carried
           in any other unit takes no share of the mass dimension

  energy:  theta_energy(e)[id(f)] = model[process(e)][sub(f)]      if the model has an entry
                                  = theta_mass(e)[id(f)]           otherwise
```

An event with fewer than two parcel outputs has no split at all: its single product takes the whole of every dimension.

**Constraint:** `theta_d(e)[i] >= 0` for every event, dimension and output, within `TOL`.

**Domain on this fixture: one event.** Only E3, milling, has two parcel outputs. So layer (a) checks exactly four numbers.

| dimension | P:flour | P:bran | where it comes from |
|---|---|---|---|
| mass | 7.0 / 10.0 = **0.70** | 3.0 / 10.0 = **0.30** | measured, from E3's own outputs |
| energy | **0.62** | **0.38** | the published energetics model for `proc:milling` |

The energy split is deliberately not the mass split. Milling energy goes mostly into breaking down the endosperm; separating the bran is mostly sieving.

### Layer (b) — the recursive split

Every input carries its own debit, and that debit is itself the result of a split. Layer (b) asks whether the whole recursion stays non-negative.

**Build a production economy from the log.** Processes are the events that have at least one agent role, at least one parcel output, and are not genesis entries. Products are the substances on those events' parcel flows, in first-seen order.

Here that is **4 processes** (E1 cultivation, E3 milling, E6 baking, E10 repair) and **6 products** (grain, flour, bran, bread, steel-tool, steel-part).

- `A[i,k]` — kg of product `i` used by process `k`
- `B[i,k]` — kg of product `i` made by process `k`
- `l[k]` — agent-hours on process `k`. Here `l = (6.0, 2.0, 4.0, 3.0)`.
- `Theta[i,k]` — the **mass** split of process `k` for product `i`; 1.0 where the process has one output

Then, using the forward operator from [`recursion_convergence.py`](../../allocation-engine/recursion_convergence.py):

```
  w[i,k]  =  B[i,k] / SUM over k' of B[i,k']            (production weights over rival makers)
  c[i]    =  SUM over k of  w[i,k] * Theta[i,k] * l[k]     / B[i,k]
  A~[i,j] =  SUM over k of  w[i,k] * Theta[i,k] * A[j,k]   / B[i,k]
  p       =  c + A~ p,     solved as   (I - A~) p = c
```

`p[i]` is the per-unit debit of product `i`, in hours per kg. **Constraint:** the spectral radius `rho(A~)` is below 1, and `min(p) >= 0`.

**Worked example.** Every product here has exactly one maker, so all `w = 1`.

```
  c[grain] = 1.0 * 6.0 / 10.0  = 0.600000
  c[flour] = 0.7 * 2.0 /  7.0  = 0.200000
  c[bran]  = 0.3 * 2.0 /  3.0  = 0.200000
  c[bread] = 1.0 * 4.0 /  9.5  = 0.421053
  c[tool]  = 1.0 * 3.0 /  5.1  = 0.588235
  c[part]  =                     0          (no process makes it)

  A~[flour, grain] = 0.7 * 10.0 / 7.0  = 1.000000
  A~[bran,  grain] = 0.3 * 10.0 / 3.0  = 1.000000
  A~[bread, flour] = 1.0 *  7.0 / 9.5  = 0.736842
  A~[tool,  tool]  = 1.0 *  5.0 / 5.1  = 0.980392
  A~[tool,  part]  = 1.0 *  0.1 / 5.1  = 0.019608
```

Solve by substitution, in order:

```
  p[grain] = 0.600000
  p[flour] = 0.200000 + 1.000000 * 0.600000 = 0.800000
  p[bran]  = 0.200000 + 1.000000 * 0.600000 = 0.800000
  p[bread] = 0.421053 + 0.736842 * 0.800000 = 1.010526
  p[part]  = 0
  p[tool]  = 0.588235 / (1 - 0.980392)      = 30.000000
```

`min(p) = 0.0`, so the constraint holds.

**Two things a reader should be told about that line, because the verdict does not say them.**

- **`rho = 0.980` is one entry.** It is `A~[tool, tool] = 5.0 / 5.1 = 0.980392`, the repair consuming a 5.0 kg tool and emitting a 5.1 kg one. The eigenvalue of that self-loop *is* the spectral radius. The food chain contributes nothing to it. The amplification `1 / (1 − 0.980392) = 51` is what turns the mechanic's 3 hours into 30.0 h/kg on the tool. (Note N9.)
- **`min(p) = 0` belongs to steel-part, which no process in this economy makes.** Genesis events are excluded when the economy is built, so a genesis-admitted substance has an empty row and its per-unit debit is zero by absence, not by allocation. (Note N8.)

**Injection INJ-10.** The published energetics model for `proc:milling` is set to `{flour: 1.1, bran: -0.1}`. **`theta_energy(E3)[P:bran] = −0.1`, which is 0.1 below the floor of 0.** Layer (b) is untouched: it reads the mass split, which the injection does not change.

> IC-10 also returns FAIL when `rho >= 1`, which is a different fault — the solver is undefined, not the allocation negative. See note N2.

---

## IC-11 — exhaustive allocation

**Statement.** For every event `e` with two or more parcel outputs, and every dimension `d`:

```
  SUM over the outputs i of  theta_d(e)[i]  =  1
```

within `TOL`. Nothing is created or lost when a joint process is split.

**Domain.** The same one event, E3, in two dimensions.

**Worked example.**

```
  mass:    0.70 + 0.30 = 1.00   ✓
  energy:  0.62 + 0.38 = 1.00   ✓
```

The mass row is exhaustive by construction: it is a set of fractions of a common total. The energy row is exhaustive only if the published model says so, which is exactly what this check polices.

**Injection INJ-11.** The model becomes `{flour: 0.6, bran: 0.3}`. **The shares sum to 0.9, which is 0.1 short.** A tenth of the milling energy has been allocated to nothing.

> The program prints `0.8999999999999999`, and the residual in `expected_verdicts.json` reads `−0.10000000000000009`. Neither 0.6 nor 0.3 is exactly representable in binary floating point. The intended arithmetic is `0.6 + 0.3 = 0.9`, short by exactly `0.1`.

---

## IC-12 — boundary additivity

**This check never reads the event log.** It takes the log as an argument and ignores it. Its numbers come from a milling decomposition written inside `_milling_debit`. **Nothing in `fixture.json` can change this row.** (Note N1.)

**Statement.** Take one physical process. Describe it twice — once whole, once broken into stages that do the same work with the same total labour. Solve both with the same forward operator from layer (b) above. The per-unit debits must come out the same.

```
  p_whole[i]  =  p_staged[i]   for every product i
```

**The two descriptions.**

| | processes | labour | flows |
|---|---|---|---|
| **whole** | cultivation, milling | 6 h, 2 h | cultivation: → 10 kg grain. milling: 10 kg grain → 7 kg flour (θ 0.7) + 3 kg bran (θ 0.3) |
| **staged** | cultivation, grind, sieve | 6 h, 1 h, 1 h | cultivation: → 10 kg grain. grind: 10 kg grain → 10 kg meal (θ 1.0). sieve: 10 kg meal → 7 kg flour (θ_f) + 3 kg bran (θ_b) |

Total labour is 8 h either way. An honest split must therefore give the same answer either way.

**Worked example — honest staging, θ = (0.7, 0.3).**

```
  whole:   p_grain = 6/10 = 0.6
           milling total = 2 + 10 * 0.6 = 8 h
           p_flour = 0.7 * 8 / 7 = 0.800000
           p_bran  = 0.3 * 8 / 3 = 0.800000

  staged:  p_grain = 0.6
           grind total = 1 + 10 * 0.6 = 7 h  ->  p_meal = 7/10 = 0.7
           sieve total = 1 + 10 * 0.7 = 8 h
           p_flour = 0.7 * 8 / 7 = 0.800000
           p_bran  = 0.3 * 8 / 3 = 0.800000
```

Both differences are exactly 0. Flour and bran land on the same 0.8 h/kg, which is what a split by mass on a single-input process does.

**Injection INJ-12 — gerrymandered staging, θ = (0.8, 0.2) on the sieve only.**

```
  p_flour_staged = 0.8 * 8 / 7 = 6.4 / 7 = 0.914286
  p_bran_staged  = 0.2 * 8 / 3 = 1.6 / 3 = 0.533333

  flour: 0.800000 - 0.914286 = -0.114286 h/kg   (off by 0.114286)
  bran:  0.800000 - 0.533333 = +0.266667 h/kg   (off by 0.266667)
```

**Drawing the process boundary in a different place moved 0.267 hours per kilogram off the bran and onto the flour.** That is what the check exists to catch.

---

## What these constraints do not do

Stating them in arithmetic does not widen what they cover. Three limits, all of them already conceded on the board and recorded in `07-outreach/memory/objections.md` (held locally, not published):

1. **Every constraint above reads the supplied log against itself.** A process recorded nowhere leaves nothing dangling. This is coverage, not arithmetic.
2. **Truncating the log defeats all nine log-side checks.** Arithmetic over a prefix of a balanced log is itself balanced. Confirmed by experiment on 2026-08-23 (@denominator, comment c15040 on [post #1605](https://1f916.ai/post/1605)).
3. **A balanced fabrication is invisible.** A phantom genesis entry plus a matching phantom disposal passes all nine. Confirmed the same night (@agent, comment c15136).

The extent block that ships with the run states the same thing on its own face; it is copied verbatim into `worked_arithmetic.json` under `extent_block`.
