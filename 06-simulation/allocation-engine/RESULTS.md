# Allocation engine — results

> **Read this instead of re-running.** From the four `--test` runs, last verified 2026-08-24.
> This is the summary layer. The three original write-ups are kept in full beside it: [`RECURSION_RESULTS.md`](RECURSION_RESULTS.md), [`ESTIMATION.md`](ESTIMATION.md), [`REFINERY.md`](REFINERY.md).

---

## 1. The recursion converges, and every share is non-negative

> **Verdict: PASS.** The recursion converges and the allocation is non-negative for **every productive economy tested**. The rival value/price allocation goes negative or non-invertible in about **95%** of the same economies.

This is the sharpest technical risk the project had, and it is closed. **Foundations §3.4a's non-negativity (IC-10) is now derived, not asserted.**

| Check | Result |
|---|---|
| Hand-computed 2×2 economy | 11 iterations, gap 3.7 × 10⁻¹² |
| Steedman's counterexample | value allocation **v = [−1, 2]** (negative); physical allocation **p = [0.324, 0.235]** (clean) |
| Per-dimension solve | the forward operator is shared across dimensions; split-before-collapse gap 2.1 × 10⁻¹⁴ |
| A non-productive economy | correctly diverges |
| Sweep size | **5,224 runs** in `results.csv`; the non-negativity claim rests on 4,098 productive ones |

**Why it works, in one line.** Aequitas splits by physically measured fractions that cannot be negative, so the per-unit cost vector solves a non-negative fixed point. Steedman's negatives come from inverting a value make-matrix. **Aequitas never inverts one.**

## 2. Cost is not scarcity

From the 12-good synthetic economy.

> **A tenderloin and a hamburger of equal tissue composition cost the same per kilogram** in materials and labour, because the material split is by mass, not by yield or desirability.

The rejected alternative — weighting by yield or price — is implemented alongside purely to show it is distinguishable. It **inflates the tenderloin 20×**, which would ration the prized cut by who can absorb the larger debit. That is the thing the axioms forbid.

Two more results from the same run:

- **Labour rides the material split.** Labour has no per-product physical trace, so it reuses the material dimension's split. The code makes this an identity rather than a comment, and a test asserts the resulting operators are bit-identical.
- **Split before you collapse.** Shared-operation dimensions commute; energy does not. So the division has to happen per dimension, before collapsing — which is Foundations §3.2a, checked rather than assumed.
- **The residual estimate worsens as good producers leave.** The dark estimate falls 23.3 → 10.0 in this fixture as producers instrument. Studied properly in [`../residual-unravelling/`](../residual-unravelling/).

## 3. The engine reproduces accepted footprints on real data

`exiobase_loader.py` feeds a real input-output table through the same solver.

| Check | Result |
|---|---|
| Against the reference implementation's own multipliers | **max gap 5.68 × 10⁻¹⁴** |
| Productive and non-negative on real structure | yes |
| Identity reduction for a product-by-product table | exact, gap **0.0** |

**So the Aequitas engine reproduces standard footprints where the standard method applies, and extends them where joint production is explicit.**

> **⚠️ Honest limit.** The small test table carries only value-added and two emission rows. It does **not** carry the employment-hours or energy extensions that full EXIOBASE has — which are the whole reason EXIOBASE was chosen. So this demonstrates the pipeline and the equivalence on the stressors that exist. **The real labour and energy numbers arrive only when the full table is loaded.**

## 4. Physical and price allocation genuinely disagree

The refinery is the first case where joint production is real and the answer is not forced.

> **Physical and price allocations diverge by up to about 6× on the same fraction slate.** Gasoline takes **55% of the energy** against **47% of the volume**. Petroleum coke is systematically under-costed by price.

Six faithfulness gates pass, including: the physical split is **price-independent**, so demand cannot enter cost; and labour rides the material split at a constant 0.001471 hours per kilogram across every fraction.

The energy dimension uses real per-process energies from the [U.S. Department of Energy's 2015 Petroleum Refining Bandwidth Study](https://www.energy.gov/eere/amo/articles/bandwidth-study-us-petroleum-refining) (Table 4-2, nine processes, 2,163 trillion British thermal units per year). Materials, labour and prices are still representative and are flagged as such in the script.

**Why this one matters most.** A monetary input-output table has *already* price-allocated its joint production, so it can only ever agree with price. This is the first case that could disagree, and it does.

## What would falsify all of this

- A productive economy where the recursion fails to converge, or where any share comes out negative.
- A physical split that changes when demand changes. That would mean value has leaked into cost.
- A refinery slate where the physical and price allocations agree closely. That would make the whole distinction academic.
- Reproduction against full EXIOBASE failing where it succeeds against the small table.

## Figures

| File | Shows |
|---|---|
| `results_iters_vs_rho.png` | Iterations to converge against how productive the economy is |
| `results_minp_vs_rho.png` | The smallest share found, against the same |
| `results_rate_vs_rho.png` | Convergence rate |
| `results_value_vs_aequitas.png` | Where the value allocation goes negative and the physical one does not |
