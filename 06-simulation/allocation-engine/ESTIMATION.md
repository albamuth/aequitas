# Estimation engine — synthetic first deliverable (C3 / OP-3)

> **Date:** 2026-08-06
> **Code:** [`estimation_engine.py`](estimation_engine.py) · reuses the proven solver in [`recursion_convergence.py`](recursion_convergence.py)
> **Answers:** NEXT.md current task (C3), *synthetic half* — a working per-product debit-vector pipeline into which real EEIO (EXIOBASE) data drops unchanged.
> **Status: ✅ BUILT & RUN.** Five self-tests pass; the pipeline produces materials + energy + labour debit vectors for a 12-good economy with two joint processes, labour attributed by the OP-18 rule, plus the residual cohort estimator.

---

## 1. What this is

The estimation engine turns an economy's physical structure — who makes what, who uses what, and how each joint process physically splits — into a **per-product debit vector**: for every good, its embodied *materials*, *energy*, and *labour*, kept separate and collapsed only on demand (§3.2a).

It is deliberately **not** a new solver. It wraps each physical dimension into the `Economy` that `build_forward` / `solve_direct` already handle, and solves `p = c + Ã p` once per dimension. The recursion sim proved that map converges and stays non-negative for every productive economy (`ρ(Ã) < 1`); the estimation engine inherits that result and exercises it on a legible, multi-dimension economy instead of random sweeps.

**Why synthetic first.** EXIOBASE is the real target (it already carries embodied labour hours — the reason NEXT.md says "don't build it, adopt it"). But the pipeline shape — make matrix `B`, use matrix `A`, per-dimension split `Θ`, per-process direct resource `r` — is identical whether the numbers are hand-built or read from a real MRIO table. Building the shape against a 12-good toy first means the real-data slice is a loader, not a redesign.

---

## 2. The economy

12 products, 6 processes, with a genuine inter-industry cycle (grain farming burns diesel + electricity; the power plant burns diesel; the refinery burns electricity — so the recursion is real, not a DAG).

The star is **cattle raising**: one joint process yielding `tenderloin, hamburger, hide, tallow, bone, manure, methane` from one pool of feed, water, energy, and labour. A second joint structure (a tannery consuming hide → leather) exercises a downstream cycle.

Three physical dimensions, each with its own direct-resource vector `r[k]` and its own split `Θ`:

| Dimension | Direct resource | Split basis `Θ` |
|---|---|---|
| **materials** | kg of feedstock each process introduces | **by mass / deposition** (the rival-audited §3.4a instrument) |
| **energy** | MJ each process burns on-site | **its own measured basis** — lean vs fat differ in deposition energy per kg, so *not* proportional to mass |
| **labour** | hours each process runs | **rides the material split (OP-18)** — no basis of its own |

---

## 3. What it demonstrates

### 3.1 Per-product debit vectors (the deliverable)

```
product      unit   materials     energy    labour   collapsed
tenderloin   kg        0.7685     3.3691    0.3369      1.2738
hamburger    kg        0.7685     2.4502    0.3369      1.2279
hide         kg        0.7685     1.2251    0.3369      1.1666
...
methane      kg        0.7685     4.5942    0.3369      1.3351
leather      kg        2.1594     7.6261    2.3832      4.9238
```

All vectors finite and `≥ 0` (test 1). The `collapsed` column applies an explicit weighting model (`materials:1, energy:0.05, labour:1`) — **the OP-10 object, kept external by design**, because whoever sets those weights moves every balance.

### 3.2 OP-18 — labour rides the material split

`Θ['labour']` is not a copy of the material split; it **is the same object**. Consequently the assembled operator `Ã` for labour is *bit-identical* to the material operator (test 2: `gap == 0.0`). Labour introduces **no new split basis and therefore no new capture surface** — it inherits the rival-audited material `Θ`, exactly the v0.6 claim. Energy, having its own `Θ`, gets a different operator — which is why the dimensions must be solved separately.

### 3.3 Cost ≠ scarcity (the load-bearing v0.6 sub-decision)

Because the material split is by mass and `B` is in mass units, cost-per-kg = `Θ_i · pool / B_i = pool / Σ B` — **constant across every co-product**. The tenderloin (1% yield) and hamburger (5% yield) cost the **same per kg** in materials and labour (test 3). A prized, scarce cut is *not* more costly.

*(Pure mass is the **low-resolution estimator** — §3.4a: "mass is an estimator, correct where composition is uniform and a low-resolution reading where it is not." It flattens *all* co-products to equal per-kg material cost. The composition refinement — where lean vs fat genuinely differ — is carried by the **energy** dimension below, which is exactly the spec's "refined only by measured tissue composition (lean vs fat differ in deposition energy), never by yield.")*

The rejected **Method 2** (yield/desirability weighting) is implemented alongside purely to show it is distinguishable: it inflates the tenderloin **20×**, which would ration the rare cut by *who can absorb the larger debit* — price-rationing by standing, the exact A5/§5.1 mechanism Aequitas removes. Scarcity is real and routes to the demand side (pledges) and decentralised distribution, never to cost.

### 3.4 Split-before-collapse (§3.2a)

Materials and labour share an operator (OP-18), so collapse-then-solve equals solve-then-collapse exactly. Energy does **not** share it, so collapsing energy and materials *before* solving gives the wrong answer (test 4). This is the whole reason the rule is **divide per dimension, then collapse** — pinned as a passing/failing assertion, not a comment.

### 3.5 Residual cohort rule `(N − Y) / Z` (§4.4)

The estimator for an unmeasured ("dark") producer is the independently-known total minus measured output, over the count still dark. It equals the **average of the remaining dark producers**, so when the best producers instrument and leave the residual first, the estimate **falls** (test 5):

```
joined=0  dark=6  per-dark estimate=23.33
joined=1  dark=5  per-dark estimate=20.00   <- darkness pays less as good producers leave
...
joined=5  dark=1  per-dark estimate=10.00
```

Darkness stops paying — the adverse-selection property that makes onboarding individually rational.

### 3.6 Per-event yield variance (A6 — measured, not averaged)

Real animals vary: two steers on identical feed, water, energy, and labour can come out ±10% in mass. The ledger is derived **per event** (A6), not from a stored average, so the actual output mass is recorded and the cost self-adjusts. `scale_process_output` scales the cattle carcass while holding every input fixed; test 6 pins three invariants:

```
cost/kg   0.8538 (-10%)  >  0.7685 (base)  >  0.6986 (+10%)
total debit per co-product: 0.7685  (invariant across all yields)
labour credit: unchanged
```

1. **Cost per kg scales as `1/yield`** — the bigger steer's beef is ~9% *cheaper per kg*, because the fixed input pool is spread over more tissue. That is the efficiency signal (A5/§5.1), recorded faithfully rather than washed into an average.
2. **Total debit routed to each co-product is invariant** — yield moves the per-kg figure, not the pool (fixed inputs, fixed physical split).
3. **The farmer's labour credit is untouched** — they are credited their hours regardless; only the output's *debit-cost* moves.

Averages (§4.4) cover only **unmeasured** producers; a measured animal carries its real numbers. This needs **no new rule** — A6 already implies it. (The separate question — whether the extra 10% deposits as muscle or fat, shifting `Θ` itself — is the "fuzzy middle", Objections §C Test 3, and remains a real-data question.)

---

## 4. Honest caveats

- **The economy is illustrative, not empirical.** Masses, energies, and labour hours are internally consistent but invented. The result being demonstrated is the *pipeline and the split rules*, not any beef number.
- **`Θ` is given, not derived.** Same standing caveat as the recursion sim (Objections §C Test 3, the "fuzzy middle"): whether real biophysical split fractions behave well at small breed/feed differences is still owed, and is a real-data question.
- **The collapse weights are placeholders and are the OP-10 problem.** They are surfaced explicitly rather than buried precisely so that C4 (re-weighting) and OP-10 governance attach to a visible object.
- **Cohort `N` must be independently known.** The demo sets `N` = true total; in reality `N` comes from FAO/trade/satellite data and only exists for major commodities, and the dark count `Z` must be defensible (§4.4's two conditions).

---

## 5. Real-data slice — EXIOBASE via pymrio

> **Code:** [`exiobase_loader.py`](exiobase_loader.py) · built 2026-08-06 · 3 self-tests pass

The real-data slice feeds an actual EEIO table into the **same forward solver**, via `pymrio` (the standard EXIOBASE parser). It is built against `pymrio.load_test()` — pymrio's built-in multi-regional IO table, which has the real EXIOBASE structure and API (technical-coefficient matrix `A` + satellite extension accounts) but is tiny and needs no multi-GB download. Pointing it at a downloaded full EXIOBASE 3 is a one-call swap (`load_real`, `REAL_EXIOBASE_DIMS`); the mapping and solve code do not change.

**The mapping insight — a product-by-product IOT is the degenerate make/use case.** Industry `k` makes product `k`, so `B = I` and `Θ = I`. Under that the forward operator reduces to `Ã = Aᵀ`, `p = (I − Aᵀ)⁻¹ s` — exactly the Leontief total-intensity multiplier `M = S(I − A)⁻¹`. Test 1 asserts our `p` equals pymrio's own `.M` to **machine precision** (max gap ~5.7×10⁻¹⁴): the Aequitas engine reproduces accepted EEIO footprints, then extends them (per-dimension vectors, OP-18 labour rule) where joint production is explicit.

```
per-unit embodied debit, region 'reg1':
sector             emis_air_kg   emis_water_kg
electricity          111.89712         1.28844   <- highest embodied emissions
mining                25.99883         0.57476
food                  10.86485         0.69812
...
```

**Honest limits of the test MRIO.** It carries only `factor_inputs` (Value Added, money) and `emissions` (two kg stressors) — **not** the employment-hours or energy extensions that real EXIOBASE has, which are the whole reason EXIOBASE was chosen (it uniquely reports embodied labour hours). So this slice demonstrates (a) the pipeline on a real table structure and (b) exact pymrio-equivalence on the kg stressors that exist; the real *numbers* for labour and energy arrive only when full EXIOBASE is downloaded (`REAL_EXIOBASE_DIMS`, permission-gated multi-GB). Money is deliberately **not** dressed up as a labour proxy — that would import exactly the value-quantity Aequitas rejects.

**Also honest — and this is the load-bearing caveat:** a product-by-product IOT (especially a *monetary* one) has already resolved joint production via an industry/commodity-technology *assumption*, i.e. **price allocation** — precisely the arbitrary carrier choice §3.4a replaces. So **reproducing pymrio's `.M` is agreement with price allocation, which is expected and is a solver-validation, NOT the project's headline result.** The spec's actual publishable target is the *opposite*: Objections §C **Test 4** / Foundations §11(a) — re-derive a **refinery's fraction slate under process-physics allocation and show it differs materially from USEEIO's price allocation.** That requires **physical units + explicit joint production** (`Θ ≠ I`) — EXIOBASE's supply-use / physical layer, not the monetary IOT. The loader is the validated stepping stone to that; it is not that demonstration, and must not be read as "Aequitas = EEIO, nothing new."

## 6. What this unblocks / what's next

- **Full-EXIOBASE swap:** `pymrio.download_exiobase3(...)` → `load_real(...)` → `mrio_to_economy(io, REAL_EXIOBASE_DIMS)`. Same loader, real labour-hours and energy numbers. Multi-GB, permission-gated.
- **SUT slice:** feed EXIOBASE supply-use tables so `Θ ≠ I` and the §3.4a physical split + OP-18 labour rule act on real joint production.
- **Feeds C2** (material-superiority demonstration) once real vectors exist.
- **Surfaces OP-10 concretely:** the `collapse` weighting model is now a real object in code — the top blocking problem has something to attach to.
