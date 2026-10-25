# false-passage

Measures what a producer gains by claiming a co-product left the chain earlier than it did (Foundations 3.4a, "what remains open"), and which published checks can see it.

- Extends `../chain-resolution/` (steer, DOE refinery). Needs only the Python standard library.
- Run: `python 06-simulation/false-passage/false_passage.py` (seed 20261024; `--seed N` changes it, `--test` runs self-tests only).
- Self-tests: 7. Each can fail (honest record must pass every detector; totals check must fire when a step is orphaned; ceiling must stay blind to downward lies; own meter must not catch; sub-threshold lie must be missed).
- Results: `RESULTS.md`. Raw output: `RUN.txt`.
