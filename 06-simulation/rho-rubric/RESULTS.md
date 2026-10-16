# Scoring ρ\* on the detection rubric — results

> **Version:** 0.1
> **Date:** 2026-10-15
> **STATUS: NOT RUN.** The code exists and has never executed. **There are no numbers in this file.** Nothing below is evidence.

## 1. The question

> *"Score claim 2 of disparity_ceiling_sim.py - the clearing rate rho* - on the same three-way sensitivity/specificity/coverage rubric. It is the one claim in that file that genuinely varies with the draw."*

## 2. Outcomes declared before running

Full text in [`DECLARED.md`](DECLARED.md). Four are stated over a level.

| # | Statement |
|---|---|
| L1 | Clean ρ\* in [1.10, 1.30] (published ≈ 1.2) |
| L2 | S1, capacity −30%, in [0.60, 0.76] (published ≈ 0.68) |
| L3 | S3, appetite +25%, in [0.90, 1.10] (published ≈ 1.0) |
| L4 | Paired-difference σ for S1 below 0.01 |
| D2 | S4, fabricated floor accounts with typical appetite, does **not** fire |
| D3 | S5, omitted consumption, fires upward, and a pure capacity rise reproduces the same ρ\* |
| D4 | S6a, shuffling appetite between accounts, moves ρ\* (the brief expected 0.00) |
| D5 | Reordering accounts and rescaling units move ρ\* by under 1e-9 |

## 3. The numbers

**None.** Every call to Python this night was refused by the sandbox ("This command requires approval"), through both the Bash and PowerShell tools, and for both `python` and `python3`. I did not try to bypass the refusal.

## 4. What this does not show

1. **Anything about ρ\*.** The code never ran. Not even the self-tests ran, so a bug in `rho_rubric.py` is possible and undetected.
2. **The structural argument below is reasoning, not measurement.** In the artifact, appetite is `a = c · r`, so demand is `Σ c · min(r, ρ)`, and capacity is `1.15 · Σc`. An inserted account with a typical `r` raises both sides in the same proportion. If that holds, ρ\* cannot see such an account. The run exists to check this, and a reader should not treat it as found.
3. **Leg 3 (coverage witness)** is unavailable on a generator whatever the run shows. ρ\* is computed from the population it describes.
4. **Whether 1.2, 0.68 and 2.2 in Foundations §5.5.7 come from this file.** Those figures may come from `rho_sweep.py`, which uses a different model. The run's L2 would settle it.

## 5. Command and seed

```
python 06-simulation/rho-rubric/rho_rubric.py --test
python 06-simulation/rho-rubric/rho_rubric.py > 06-simulation/rho-rubric/RUN.txt
```

Seeds 1 to 30, N = 200,000, F = 10. Fault stream = seed + 10,000,000. Estimated cost: about 1 minute, under 1 MB.
