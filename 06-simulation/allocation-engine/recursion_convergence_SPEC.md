# Sim spec — Recursion convergence of the OP-17 allocation

> **Status:** ✅ **BUILT & RUN 2026-08-05 — PASS.** Written 2026-08-04. Implementation: [`recursion_convergence.py`](recursion_convergence.py); results: [`RESULTS.md`](RECURSION_RESULTS.md).
> **Answers:** Objections `§C` Test 1 and NEXT.md's current task — **both resolved.**
> **Owner note:** this was the sharpest surviving technical risk in the project. The negative result that would have invalidated §3.4a did not appear: the allocation is a non-negative Neumann series, 100% convergent for `ρ<1`, zero negatives across 4,098 economies, while the value arm goes negative in ~95%. Cleared to build C3.

---

## 1. The question, precisely

Foundations §3.4a: *a joint process's debit divides according to where the process physically sent its inputs.* But **every input is itself the output of another joint process**, so a product's per-unit debit is defined in terms of other products' per-unit debits — a **recursive** definition. Two things are asserted and unproven for a whole economy:

1. **Termination / convergence.** Does the recursion have a fixed point, and does iteration reach it? (Trivially true for one isolated process; unproven once processes feed each other, possibly in cycles — the Sraffa corn-iron structure.)
2. **Non-negativity (IC-10).** Each co-product's share is asserted ≥ 0 because "a forward measurement cannot be negative." True per process; **Steedman's result is that value-based joint-production systems can still produce negative aggregate values.** Does Aequitas's *physical* allocation avoid that?

**Hypothesis to test:** because Aequitas splits by physically-measured fractions θ ≥ 0 (not by an invertible value/price matrix), the per-unit debit vector is the solution of a **non-negative** linear fixed point `p = c + Ã p` with `Ã ≥ 0`. So whenever the economy is *productive* (spectral radius `ρ(Ã) < 1`), `p` is **unique, non-negative, and reached by simple iteration** — and Steedman's negative values do not transfer. The sim should confirm this and find where, if anywhere, it breaks.

---

## 2. Model

Products `i = 1..M`. Processes `k = 1..N`. At unit scale, process `k`:

- consumes product `i` in amount `A[i,k] ≥ 0` (input/use matrix),
- produces product `i` in amount `B[i,k] ≥ 0` (output/make matrix — **joint production ⇔ column of `B` has >1 nonzero**),
- uses direct labour `l[k] ≥ 0` hours,
- splits its total debit across its co-products by **physical fractions** `Θ[i,k] ≥ 0`, with `Σ_i Θ[i,k] = 1` and `Θ[i,k] > 0` only where `B[i,k] > 0`.

`Θ` is the instrument reading of §3.4a (tissue-deposition, cracking enthalpy, turbine curve). In the sim it is a **given nonnegative parameter**, not something to be optimised — that is the whole point of §3.4a and the reason no objective function enters (avoids re-opening OP-10).

**Per-unit debit `p[i]` (hours, by A2).** Total debit of running process `k` at unit scale is `l[k] + Σ_j A[j,k]·p[j]`. Product `i`'s share of that, per unit produced:

```
p[i]  =  Σ_k  Θ[i,k] · ( l[k] + Σ_j A[j,k]·p[j] ) / B[i,k]      (over k with B[i,k] > 0)
```

**Base case — one process per product** (`k(i)` unique). Then this is linear:

```
p  =  c + Ã p
c[i]   =  Θ[i,k] · l[k] / B[i,k]
Ã[i,j] =  Θ[i,k] · A[j,k] / B[i,k]           with k = k(i)
```

`Ã ≥ 0` by construction. Solve by (a) iteration `p ← c + Ã p` from `p=0`, and (b) direct `p = (I − Ã)⁻¹ c` for cross-check.

**Rival processes** (same product made by several processes) are a **stretch goal**: per unit, the log records which process made *that* unit, so `p` per unit is still single-process; the reported `p[i]` is the production-weighted average. Start without rivals — the recursion is fully exercised already.

---

## 3. Synthetic economy generator

Parameters (sweep these):

| Param | Meaning | Sweep |
|---|---|---|
| `M`, `N` | products, processes (start `M=N`) | 10, 100, 1000, 10⁴ |
| `density` | fraction of `A` entries nonzero | 0.01 – 0.2 |
| `joint_frac` | fraction of processes that are joint (≥2 outputs) | 0, 0.25, 0.5, 1.0 |
| `cycle_strength` | how much inter-industry feedback (controls `ρ(Ã)`) | tune to span `ρ ∈ [0.5, 0.999]` and `ρ > 1` |
| `theta_dist` | how split fractions are drawn (Dirichlet α) | symmetric + skewed |
| `seed` | RNG seed | ≥ 30 seeds per cell |

Generate `A`, `B`, `l`, `Θ` as **sparse** matrices (`scipy.sparse`). Ensure productiveness is *controllable*: scale `A` so `ρ` of the input-coefficient matrix lands where you want, including deliberately `> 1` (non-productive) to confirm the sim reports divergence rather than hanging.

---

## 4. What to compute and report

For each generated economy:

1. **`ρ(Ã)`** — spectral radius (`scipy.sparse.linalg.eigs`, largest magnitude). The predictor.
2. **Convergence** — iterate `p ← c + Ã p`; record iterations to `‖Δp‖∞ < 1e-10`, or flag divergence. Cross-check against the direct solve.
3. **Convergence rate** — empirically `‖Δp‖` should fall like `ρ(Ã)^n`; report fitted rate vs `ρ`.
4. **Non-negativity** — `min_i p[i]`. Record any negative and the structure that produced it.
5. **Comparison arm — the publishable contrast.** Solve the *same* economy with **value/price allocation** (allocate joint debit by output value, USEEIO-style, using a random price vector or `B`-inversion `v(B−A)=l`). Record how often *that* arm produces negatives or fails to invert on economies where the Aequitas arm stays clean. This doubles as Objections Test 4 (refinery re-derivation) in synthetic form.

**Primary outputs:**

- A scatter of `iterations` and `min(p)` vs `ρ(Ã)`, across the sweep.
- The claim, confirmed or broken: *`ρ(Ã) < 1 ⟹ convergence and `min(p) ≥ 0`, independent of `joint_frac`.*
- Counterexamples, if any — the important result. A single reproducible negative under `ρ < 1` **kills §3.4a's non-negativity** and must be reported loudly with its seed.

---

## 5. Success criteria

| Result | Meaning |
|---|---|
| ✅ Aequitas arm: converges and `min(p) ≥ 0` for all `ρ < 1`, at every `joint_frac` including 1.0 | §3.4a's recursion is sound; IC-10 non-negativity is *derived*, not merely asserted. A footnote — but a load-bearing one. |
| ✅ Value arm goes negative / non-invertible where Aequitas arm doesn't | **The publishable result.** Physical allocation escapes Steedman; price allocation doesn't. |
| ❌ Any `ρ < 1` economy with `min(p) < 0` in the Aequitas arm | **Invalidates §3.4a.** Sraffa re-enters. Report immediately; do not proceed to C3. |
| Divergence for `ρ ≥ 1` | Expected and correct — a non-productive economy has no finite cost vector. |

---

## 6. Build notes

- Python, `numpy` + `scipy.sparse`. Keep everything sparse; `M=10⁴` must run in seconds to justify the "tractable at national scale" claim (Cockshott & Cottrell, [*Towards a New Socialism*](https://en.wikipedia.org/wiki/Towards_a_New_Socialism)).
- Deterministic seeds; dump every run's params + metrics to a tidy CSV for the scatter plots.
- One module `recursion_convergence.py`; a thin `__main__` that runs the sweep and writes `results.csv` + plots. Unit-test the two solvers agree on a hand-checked 2×2 joint economy before trusting the sweep.
- **Per-dimension reminder:** debit is a vector (§3.2a). The sim can run scalar `p` first (labour-hours only), then confirm the split is identical run per physical dimension — because `Θ` is weighting-independent, per-dimension and collapsed results must agree. That agreement is itself a check.

---

*When done: results → a new `02-research`-style note or a `06-simulation/allocation-engine/RECURSION_RESULTS.md`; update Objections `§C` Test 1 and NEXT.md; if it passes, it becomes the first piece of C11.*
