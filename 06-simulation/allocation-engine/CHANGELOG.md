# Allocation engine — change history

> Newest entry first. What the project is: [`README.md`](README.md). What it found: [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — four scripts gathered into one folder

`06-simulation/` was a flat directory of about 94 files. The solver, the engine, the real-data loader and the refinery slice moved into `06-simulation/allocation-engine/` together, because each imports the one before it and splitting them would have created cross-folder imports for no gain.

**One file was renamed.** `06-simulation/RESULTS.md` — which was always the *recursion* results doc, not a results doc for the whole directory — became [`RECURSION_RESULTS.md`](RECURSION_RESULTS.md). The name [`RESULTS.md`](RESULTS.md) now holds a summary covering all four pieces, with the original left untouched underneath it. Every reference elsewhere in the repository was repointed.

**One code comment lost its history.** `refinery_slice.py` opened its data section with *"(numbers pass, 2026-08-06). The ENERGY dimension now uses the REAL…"*. The dating and the "now" moved here, as the 2026-08-13 entry. The data description stayed, because it describes the code as it stands.

**No import paths changed** — the four scripts already sat together in the flat directory and still do. One script elsewhere imports the solver, [`../audits/arithmetic_audits.py`](../audits/arithmetic_audits.py), and was pointed at this folder.

**Verified after the move:** all four `--test` runs pass.

---

### 2026-08-13 — the refinery gets real energy data

[`refinery_slice.py`](refinery_slice.py) had been running on representative energy figures. The energy dimension now uses the per-process onsite energies from the [U.S. Department of Energy's 2015 Petroleum Refining Bandwidth Study](https://www.energy.gov/eere/amo/articles/bandwidth-study-us-petroleum-refining), Table 4-2: nine processes, 2,163 trillion British thermal units per year, split into a declared distillation channel and a measured conversion channel routed by standard refinery flow.

Volume yields are the standard [Energy Information Administration](https://www.eia.gov/dnav/pet/pet_pnp_pct_dc_nus_pct_a.htm) refinery-yield proportions. **Materials, labour and prices remain representative and are flagged in the script** — the bandwidth study covers process energy only, so those three dimensions are the next refinement.

Six faithfulness gates pass. Physical and price allocations diverge by up to about 6× on the same slate.

---

### 2026-08-06 — the estimation engine and the refinery slice built

[`estimation_engine.py`](estimation_engine.py), five self-tests: per-product debit vectors for a 12-good economy with two joint processes, labour attributed by the rule that it rides the material split, and the residual cohort estimator.

[`exiobase_loader.py`](exiobase_loader.py): the same solver fed a real input-output table, reproducing the reference implementation's multipliers to 5.68 × 10⁻¹⁴.

[`refinery_slice.py`](refinery_slice.py) first built, on representative data.

Journal entry: [`../../03-journal/2026-08-06.md`](../../03-journal/2026-08-06.md).

---

### 2026-08-05 — the recursion result

[`recursion_convergence.py`](recursion_convergence.py) and [`RECURSION_RESULTS.md`](RECURSION_RESULTS.md). 5,224 runs. **The recursion converges and every share is non-negative for every productive economy tested; the rival value/price allocation goes negative or non-invertible in about 95% of the same economies.**

This closed the project's sharpest surviving technical risk. Foundations §3.4a's non-negativity stopped being an assertion and became a derivation.

Journal entry: [`../../03-journal/2026-08-05.md`](../../03-journal/2026-08-05.md).
