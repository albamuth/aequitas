# rho-rubric — scoring the clearing rate ρ\*

> **Version:** 0.1
> **Date:** 2026-10-15
> **Status:** code written, **never run**. The night's sandbox refused every Python call (see `RESULTS.md`, Blocked).

Scores claim 2 of [`../disparity-ceiling/disparity_ceiling_sim.py`](../disparity-ceiling/disparity_ceiling_sim.py) on the sensitivity / specificity / coverage rubric. Request `sr-20260901-score-claim-2-of-disparity-ceiling-sim-py-th`, brief [`SB-02`](../sim-briefs/SB-02_rho-star-rubric.md).

| File | What it is |
|---|---|
| `DECLARED.md` | Outcomes written before any run, including four stated over a level |
| `rho_rubric.py` | Imports `draw_population` and `clearing_rho` from the artifact. Adds an exact solver, 10 faults, 3 specificity controls, paired-seed statistics |
| `RESULTS.md` | The results file (currently: nothing ran) |

**Run:** `python 06-simulation/rho-rubric/rho_rubric.py --test` (9 self-tests), then `python 06-simulation/rho-rubric/rho_rubric.py > 06-simulation/rho-rubric/RUN.txt`.
**Cost estimate:** one exact solve is a sort of 200,000 numbers, about 0.05 s. The full run is about 1,000 solves, so **about 1 minute and under 1 MB** of output.
