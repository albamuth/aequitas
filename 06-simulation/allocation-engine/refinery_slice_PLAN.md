# Refinery slice — plan (SUT / physical-split vs price allocation)

> **Status:** PLANNED, not built. **θ-basis decision LOCKED 2026-08-06 → option (A), metered process energy.** Ready to build.
> **Answers:** Objections §C **Test 4** ("refinery re-derivation — process-physics vs USEEIO price allocation; a materially different answer is the most publishable early result") and Foundations **§11(a)** (the MVP's first publishable target).
> **Reuses:** `estimation_engine.py` (`MultiDimEconomy`, per-dimension solve) and `recursion_convergence.py` (forward solver). No new solver.

---

## 1. Why this slice, and why it is different from the loader

The EXIOBASE loader validated that our engine reproduces standard EEIO footprints — but a monetary product-by-product IOT has **already price-allocated** joint production, so it can only ever agree with price allocation. This slice is the opposite: take **one genuine joint process** (a refinery: crude → full fraction slate), allocate its debit two ways on the *same physical data*, and show the answers **differ materially**:

- **Price allocation** (what USEEIO/EXIOBASE do): each fraction's share ∝ its revenue (price × yield). This is §3.4a's rejected "carrier quantity = market price", forbidden as *truth* by A5 but usable as *data* (`joint-production-allocation-problem.md`, line 56).
- **Aequitas process-physics allocation** (§3.4a): each fraction's share ∝ **where the process physically sent its energy/inputs** — the metered processing energy that routed crude into that fraction. This is the "cracking enthalpy for a refinery" instrument.

**Expected headline result:** price allocation *under*-costs high-volume/low-value fractions (fuel oil, asphalt, petcoke) and *over*-costs low-volume/high-value fractions (gasoline, jet). The physical split reverses part of that ordering — because heavy residual fractions are cheap to *sell* but their production still consumed real distillation/conversion energy. **A materially different, defensible per-fraction debit vector is the deliverable.**

---

## 2. Data needed, and candidate sources

Three vectors over ~7 fractions (LPG, gasoline, naphtha, jet/kerosene, diesel, fuel oil, asphalt/residual + petcoke):

| Vector | Role | Candidate source |
|---|---|---|
| **Yields** (vol or mass % of a barrel) | `B` (make matrix); shared by both methods | [EIA refinery yield](https://www.eia.gov/dnav/pet/pet_pnp_pct_dc_nus_pct_m.htm) — public, monthly, US average |
| **Process energy per fraction** | the **physical θ** (§3.4a) | **the missing piece** — DOE/EIA *Petroleum Refining bandwidth study*, or refinery process-unit energy intensities (atmospheric distillation + FCC + hydrocracker + reformer, MJ/bbl throughput) allocated to the fractions each unit yields |
| **Fraction prices** | the **price θ** (contrast only) | EIA spot prices (gasoline, diesel, jet, residual fuel, propane) — public |

**Crude input** enters as the process's direct material + energy (one upstream node, or exogenous). Keep the economy small and legible — a single joint refinery process is enough to make the point; upstream recursion is already proven.

---

## 3. The one decision to make before building — the physical θ basis

The §3.4a instrument for a refinery is "cracking enthalpy / where the process sent its energy." Three concrete readings, they give different work and different defensibility:

- **(A) Metered process energy per conversion unit** ✅ **CHOSEN (2026-08-06)** — allocate crude-distillation energy across all fractions, then each conversion unit's (FCC, hydrocracker, reformer, coker) metered energy to the fractions it produces. "Where the process physically sent its energy", sourceable from DOE bandwidth data. Faithful to §3.4a, defensible, real numbers.
- **(B) Thermodynamic cracking enthalpy** — closer to the spec's literal word, but ignores distillation/heating/pumping energy and is harder to source per fraction. Arguably too narrow.
- **(C) Borrow a published LCA physical-allocation factor set** — least original work; leans on someone else's θ, and most refinery LCAs themselves fall back to mass or energy-content (a *carrier quantity* §3.4a rejects). Weakest.

**This is a real fork** — it sets what data I chase and how strong the result is. Everything else in the plan is fixed.

---

## 4. Files

- **[NEW] `06-simulation/allocation-engine/refinery_slice.py`** — builds the refinery as a `MultiDimEconomy` (single joint process, rectangular `B`), computes the per-fraction debit vector under the physical θ; a `price_allocate()` function for the contrast; a comparison table + the divergence metric.
- **[NEW] `06-simulation/allocation-engine/REFINERY.md`** — write-up: the two allocations, the numbers, which fractions move and why, honest caveats (θ source resolution, US-average yields), the A5 argument (price unusable as truth).
- **[NEW] `../../00-strategy/GLOSSARY.md#src-refinery-process-energy`** — source stub for the process-energy data (closes the open to-do in `joint-production-allocation-problem.md` line 74), with citation + link + why it matters.
- **[MODIFY] `estimation_engine.py`** — only if the single-joint-process path needs a helper; expected minimal, engine already handles `Θ ≠ I`.

## 5. Test assertions (faithfulness gates)

1. **Both methods conserve** — each allocation's shares sum to the refinery's total debit (efficiency axiom). Neither creates or destroys debit.
2. **Physical split is non-negative** — inherited from the Neumann-series result; assert `min(p) ≥ 0`.
3. **Universality** — the physical split is independent of the price vector: perturb prices, physical θ unchanged (the §3.4a / B9 property that killed demand-contingent splitting).
4. **Material divergence** — price vs physical per-fraction cost differ by more than a set threshold on at least the residual fractions; report the L1 divergence and the sign of the shift (heavy fractions up under physical).
5. **Price allocation flagged `declared`, physical flagged `measured`** — the basis label rides the output (EventLog basis field; A5 keeps price as data, not truth).

## 6. Risks / open

- **θ data resolution** — DOE bandwidth data is sector-aggregate; per-fraction attribution of shared distillation energy is itself a mini-allocation (but a *measured* one — where the energy metered). Flag resolution honestly (Level 1–3 ladder).
- **This is the "fuzzy middle" cousin** — refinery configs vary (hydroskimming vs deep-conversion). US-average is a representative animal, same caveat as the cattle toy; per-refinery is the high-res version.
- **Scarcity ≠ cost still holds** — a premium fraction is not more costly for being prized (the tenderloin rule, one domain over). The plan must not let price leak into the physical θ.

---

## 6a. Scope decision — pollution excluded from v1 (2026-08-06)

**v1 tracks materials, energy, labour only. No CO₂/pollution dimension.** Rationale (author's call, spec-faithful):

- A fraction's per-unit **cost** carries **no pollution at all**, because pollution never transfers downstream (§3.2b). Two separate events, both off the cost: **refinery process CO₂** stays on the refinery org; **combustion CO₂** is debited to whoever burns the fuel later (the driver, not the receiver of delivered goods — §3.2b transport clause).
- **Why this is load-bearing, not a simplification:** passing pollution to a non-causer breaks the accounting the same way inheriting historical costs back to the first human does — it never terminates (the §6.2a computational-closure argument). Pollution-non-transfer (§3.2b, Ellerman) and computational closure (§6.2a) are the *same principle*: cost never cascades to non-causers.
- The per-fraction pollution *provenance record* (a buyer **signal**, §5.1b) is a separate object from **cost** and is out of scope for a cost test. Add CO₂ in a later pass if a signal demonstration is wanted.

## 7. Not in this slice (deferred)

- Real EXIOBASE **supply-use** tables (multi-GB, permission-gated). This standalone refinery model is the faster route to the Test-4 result because **the physical θ is not in EXIOBASE anyway** — it must be supplied from refining-engineering data regardless. EXIOBASE SUTs become relevant only for embedding the refinery in a full economy later.
- Full recursion through crude extraction (already proven; keep crude exogenous here).
