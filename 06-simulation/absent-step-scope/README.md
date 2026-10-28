# absent-step-scope

Splits an absent step on a flow sheet into **enumerated-and-absent** (recorded "not passed") and **never-looked-at** (no record), and measures the debit-per-kg error a reader makes when the sheet does not say which is which (Foundations 3.4a, passage claim).

- Extends `../chain-resolution/` (steer, DOE refinery). Python standard library only.
- Run: `python 06-simulation/absent-step-scope/absent_step_scope.py` (seed 20261028; `--seed N` changes it, `--test` runs self-tests only). Runs in well under the nightly budget.
- Self-tests: 8. Each can fail (q=1 exact, q=0 reads zero, error signs, ceiling cross-checked against `chain_resolution`, the 6.25x recomputed, closed-form shares, adversary wins, readers distinguishable).
- Results: `RESULTS.md`. Raw output: `RUN.txt`.
