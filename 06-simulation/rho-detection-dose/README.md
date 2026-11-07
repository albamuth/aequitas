# rho-detection-dose

Detection-dose curve for the clearing rate ρ\*: how many fabricated floor accounts does it take before the paired move in ρ\* clears k paired standard deviations, for three declared debit dispersions.

- **Request:** `sr-20260915-produce-a-detection-dose-curve-for-rho-for-e`
- **Model:** imported from [`../rho-rubric/rho_rubric.py`](../rho-rubric/rho_rubric.py) (exact ρ\* solver, claim-2 population). Only the σ parameter, the dose sweep and the two noise bars are new.
- **Declared first:** [`DECLARED.md`](DECLARED.md). The run prints its sha256 prefix before any statistic.

## Run

```
python 06-simulation/rho-detection-dose/detection_dose.py --test      # 8 self-tests, a few seconds
python 06-simulation/rho-detection-dose/detection_dose.py > 06-simulation/rho-detection-dose/RUN.txt
python 06-simulation/rho-detection-dose/detection_dose.py --n 20000 --seeds 6 --blocks 1   # quick look
```

Needs numpy. Do not run with `python -I` on this machine: isolated mode hides the user-site numpy.

Cost: N = 200,000, 3 σ × 2 blocks × 30 seeds × 3 arms × 11 doses, six processes. Output under 100 KB.

Files: `detection_dose.py`, `DECLARED.md`, `RUN.txt` (raw output), `RESULTS.md`.
