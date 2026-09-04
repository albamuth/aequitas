# Results — Recursion convergence of the §3.4a allocation

> **Date:** 2026-08-05
> **Code:** [`recursion_convergence.py`](recursion_convergence.py) · **Spec:** [`recursion_convergence_SPEC.md`](recursion_convergence_SPEC.md)
> **Data:** `results.csv` (5,224 runs) · **Figures:** `results_*.png`
> **Answers:** Objections `§C` Test 1 (the sharpest surviving technical risk) and NEXT.md's current task.
> **Verdict: ✅ PASS.** The recursion converges and the allocation is non-negative for every productive economy tested; the rival value/price allocation goes negative or non-invertible in ~95% of the same economies. **§3.4a's IC-10 non-negativity is now derived, not merely asserted.** Proceed to OP-18 / C3.

---

## 1. What was at risk

> **⚠️ The rule this describes was withdrawn on 2026-09-03.** A joint process's cost is no longer divided at all — every co-product carries the whole process cost against its own output mass (Foundations §3.4a). **The convergence and non-negativity results below still stand, and stand more easily**, because no division is performed any more. The sentence below states the withdrawn rule in order to say what was tested.
<!-- struck-ok: a results file records the rule it tested on the date it ran -->

Foundations §3.4a splits a joint process's debit by *where the process physically sent its inputs* — non-negative fractions `Θ ≥ 0`. But every input is itself the output of another joint process, so a product's per-unit debit `p[i]` is defined **recursively**:

```
p[i] = Σ_k  Θ[i,k] · ( l[k] + Σ_j A[j,k]·p[j] ) / B[i,k]
```

Two things were **asserted and unproven for a whole economy** (fine for one process in isolation):

1. **Convergence / termination** — does the recursion have a fixed point that iteration reaches, even with inter-industry cycles (the Sraffa corn–iron structure)?
2. **Non-negativity (IC-10)** — each share was claimed `≥ 0` because "a forward measurement cannot be negative." Steedman (1975) showed value-based joint-production systems can produce **negative** aggregate labour values. Does the *physical* allocation escape that, or does Sraffa/Steedman re-enter through the back door?

A single reproducible negative under a productive economy would have **invalidated §3.4a** and re-opened the co-product problem. The payoff was asymmetric: a positive result is a footnote, a negative result is a demolition. Hence: test it while the answer is a week old, before C3 is built on it.

---

## 2. The result, and why it is a theorem not a coincidence

Write the recursion in matrix form. With one producing process per product (base case) the map is **linear**:

```
p = c + Ã p ,    c[i]   = Σ_k w[i,k]·Θ[i,k]·l[k]   / B[i,k]  ≥ 0
                 Ã[i,j] = Σ_k w[i,k]·Θ[i,k]·A[j,k] / B[i,k]  ≥ 0
```

where `w[i,k]` are non-negative production weights over a product's rival producers. **`Ã ≥ 0` and `c ≥ 0` by construction — Aequitas divides *by* the make quantity `B` (forward) and never inverts it.** So whenever the economy is productive (`ρ(Ã) < 1`) the solution is the Neumann series

```
p = c + Ãc + Ã²c + Ã³c + …   =   Σ_{n≥0} Ãⁿ c
```

a sum of non-negative terms. Therefore `p` is **unique, non-negative, and reached by simple iteration — for free — independent of how jointly-produced the economy is.** Non-negativity is not luck; it is a property of never forming `B⁻¹`. The simulation is the empirical confirmation of exactly this.

**Contrast with the value system.** Steedman's negatives come from solving `v(B − A) = l`, i.e. **inverting the joint make-matrix `B`**. `(B − A)⁻¹` is not sign-controlled, so `v` can go negative even when every physical input was positive. Aequitas structurally refuses that inversion.

---

## 3. Numbers

**Sweep:** products `M ∈ {10, 100, 1000, 10⁴}`; input density 0.05; `joint_frac ∈ {0, 0.25, 0.5, 1.0}`; Dirichlet split `α ∈ {1.0, 0.3}`; target `ρ ∈ {0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 1.05, 1.2}`; 30 seeds/cell (fewer at `M ≥ 1000`). **5,224 runs.**

| Claim | Result |
|---|---|
| **Convergence for `ρ < 1`** | **4,098 / 4,098 = 100%.** No productive economy failed to converge. |
| **Independent of joint production** | Converged **849/849, 840/840, 840/840, 849/849** at `joint_frac = 0, 0.25, 0.5, 1.0`. Fully-joint economies converge exactly as reliably as non-joint ones. |
| **Non-negativity (Aequitas)** | **0 negatives.** Most-negative `min(p)` over all productive runs = **2.9 × 10⁻¹⁵** — floating-point zero. |
| **Divergence for `ρ ≥ 1`** | **0 / 1,126** non-productive economies wrongly reported as converged. The sim reports divergence, does not hang. |
| **Convergence rate law** | Fitted geometric decay of `‖Δp‖` matches `ρ(Ã)` to a **median 5.8 × 10⁻⁹** (`ρ < 0.999`). `‖Δp‖ ~ ρⁿ` confirmed. |
| **Two solvers agree** | Iteration vs direct `(I − Ã)⁻¹c`: max **relative** gap **3.3 × 10⁻¹⁰** across all productive runs. |
| **Tractability** | `M = 10⁴` solves in **≈ 10 s** — the "national scale is computable" claim (Cockshott & Cottrell), on a laptop, in Python. |

### The publishable contrast — value vs physical allocation on the *same* economy

720 square joint-production economies (`N = M`, every process joint, products with rival producers), each solved **both** ways:

| | Value / price allocation (Steedman) | Aequitas physical allocation |
|---|---|---|
| Non-invertible `(B − A)` | **18 / 720** | — (never inverts) |
| `min(v) < 0` among invertible | **664 / 702 = 94.6%** | — |
| **Fails (negative *or* non-invertible)** | **682 / 720 = 94.7%** | **0 / 720** |
| `min(p) < 0` | — | **0** |

**Physical allocation escapes Steedman; price allocation does not.** This is Objections `§C` Test 4 (refinery re-derivation) in synthetic, general form.

### The concrete counterexample (hand-checked, reproducible)

Two goods, two joint processes, `B = [[6,3],[1,12]]`, `A = [[5,0],[0,10]]`, `l = [1,1]`:

- **Value system** `v = l(B − A)⁻¹ = [−1, 2]` — good 1 has a **negative labour value**.
- **Aequitas** on the identical physical data → `p = [0.324, 0.235]`, both **positive**.

(Self-test `test_steedman_contrast`, runs in `--test`.)

---

## 4. Figures

| File | Shows |
|---|---|
| `results_minp_vs_rho.png` | `min(p) ≥ 0` for every productive economy, both base and square-joint, across `ρ ∈ [0.5, 0.999]` (symlog). |
| `results_rate_vs_rho.png` | Fitted convergence rate lands on the `rate = ρ` diagonal — the `ρⁿ` law. |
| `results_iters_vs_rho.png` | Iterations-to-converge rising as `ρ → 1`, coloured by `joint_frac` (curves overlap → joint production doesn't change the picture). |
| `results_value_vs_aequitas.png` | Same economies: value `min(v)` spread far negative (symlog) while Aequitas `min(p) ≥ 0`. |

---

## 5. Honest caveats

- **Base case = one producing process per product.** Rivals (a product made by several processes) are handled as a production-weighted average, exercised in the square-joint arm; the log's per-unit provenance makes each *unit* single-process, so this is faithful, not a simplification of the accounting.
- **`Θ` is a given parameter, not derived.** That is the whole point of §3.4a — the process's physics supplies `Θ`; the sim's job was the recursion, not the instrument. Whether real biophysical `Θ` behaves well at small breed/feed differences is a *separate* owed test (Objections §C Test 3, the "fuzzy middle").
- **Near-critical economies have astronomically large `p`.** As `ρ → 1`, `p` blows up like `1/(1−ρ)` — the Leontief-inverse singularity. This is **correct**: an economy that barely reproduces itself embeds near-infinite labour per unit. It is why the raw absolute solver-gap looked large (`p` itself ~10²⁰); the *relative* gap stayed at 10⁻¹⁰.
- **The value arm's negatives are partly driven by near-singular random `(B − A)`.** Even discounting the extreme cases, the qualitative claim — physical allocation is structurally sign-safe, price allocation is not — holds by construction, not just empirically.

---

## 6. Consequences for the project

1. **§3.4a's non-negativity is upgraded from *asserted* to *derived*.** Update Foundations §3.4a IC-10 note and Objections `§C` Test 1 → resolved, Objections line 306's ⚠️ caveat cleared.
2. **This is the first concrete piece of C11** (arithmetic audits over a synthetic log) and the synthetic half of the academic paper's Sraffa/Steedman reply (Roadmap §9.2).
3. **OP-18 is unblocked as the next critical-path item.** The recursion is sound *given* the split fractions; supplying labour's split across co-products/teams is the remaining genuine convention, and it is a human-attribution problem, not a physics one.

*Bad news did not arrive. The answer held.*
