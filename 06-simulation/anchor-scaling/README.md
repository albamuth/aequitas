# anchor-scaling

Scale-the-anchor self-test (request `sr-20261105-add-a-scale-the-anchor-self-test-to-rho-swee`) and a census of which scripts assert something that responds to their anchor.

| File | What it does | Run |
|---|---|---|
| `scale_the_anchor.py` | Runs `rho_sweep_anchor.py` (99 cells) and `stable_band_kappa.py` (one-day and cumulative edges) at κ × 0.5, × 1, × 2 | `python scale_the_anchor.py` |
| `census.py` | AST census of every script under 06-simulation that assigns a named anchor: static data flow, dynamic ×2 / ×0.5 mutation in a child process (60 s limit), pinned-literal heuristic | `python census.py` (~2 min) |
| `RESULTS.md` | Question, declared outcomes, numbers, limits | |

The self-tests themselves live in the two scripts they test: `rho_sweep_anchor.py` (self-test 6) and `stable_band_kappa.py` (`test_scale_the_anchor`). Each can fail: scale κ only in the cumulative case and the second fails by 44.8% at F = 10, ×2.
