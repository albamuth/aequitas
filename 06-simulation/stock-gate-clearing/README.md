# stock-gate-clearing

Request `sr-20261105-stock-gate-clearing-rate-after-a-capacity-sh`. Reads the clearing rate rho* of the **stock** gate `D <= rho*(C+P)` on a cumulative ledger after a -30% capacity year. Foundations 5.5.7's 0.19 comes from a **flow** gate.

Run: `python stock_gate_clearing.py --test` (7 self-tests), then `python stock_gate_clearing.py > RESULTS_RAW.txt`.
Results: `RESULTS.md`. Method and arms: docstring of `stock_gate_clearing.py`.

## Outcomes declared before the first run

| # | Statement | Kind | Fails if |
|---|---|---|---|
| 1 | Flow rho* at F=10, -30% reads **0.19 ± 0.02** on this code | LEVEL (instrument check) | outside 0.17–0.21 |
| 2 | Arm A stock rho_s at F=10, rho0=0.33 is **in [0.21, 0.33)** | LEVEL | below 0.21 (no gap from flow) or at 0.33+ |
| 3 | At rho_s, **more than 5%** of people admit zero (burden falls on the already bound) | LEVEL | 5% or less |
| 4 | Year 2 at rho 0.33 admits **more than 1% above** the baseline year (rationed people regain stored room) | CHANGE | within ±1% or lower |
| 5 | Arm B: the ungated part alone is **at least 90%** of shocked capacity, so no useful rho_s exists | LEVEL | below 90% |
| 6 | Arm C changes rho_s from arm A by **more than 0.02** | CHANGE | within 0.02 |

Interpretation choices made without asking (unattended run), each also run as a sensitivity: arm B charges the ungated part to D before the gate reads room (B2 reverses it); arm C removes under-14 debit from the past ledger **and** leaves under-14 consumption ungated (C2 does the past only); rho0 is each F's published flow edge (1.017 / 0.330 / 0.253) in the primary run and 0.33 at every F in the sensitivity.
