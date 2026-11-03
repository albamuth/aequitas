# Pledge term on the kappa-tied ledger — declared before running

> **Date:** 2026-10-31 · **Request:** `sr-20261028-run-pledge-band-py-s-pledge-term-on-the-kapp`

**Inputs, all inherited from `stable_band_kappa.py`:** κ = 1,380 / 365 = 3.7808. Capacity R_max = 56,446. Population 60,000, seed 7. Ages from `draw_ages`, age seeds 11 and 12. Everyone joins on day one. M = 100. Joiner credit F × 365 × age. Joiner debit 1,380 × age. Past work not credited.

**Pledge arms** (p is the share of the network's earned credit that has been committed, so P_total = p × C_total, as IC-8 requires):

| Arm | How P is set | Why it is there |
|---|---|---|
| **A, proportional** | P = p × C for every person, at every period | The case `pledge_band.py` assumes. The rule `rho*/(1+p)` should be exact here |
| **B, frozen at joining** | P = p × (credit at joining), never topped up | Pledges are permanent and committed once. Credit keeps growing after. The rule could fail here |
| **C, concentrated** | Backed people get P = their joining credit; the backed set is random and sized so total P = p × total C | Same p, very unequal P. The rule could fail here |

**Outcomes:**

| # | Kind | Declared |
|---|---|---|
| O1 | **Level** | One-day edge at p = 0: F = 2 in [0.95, 1.10]; F = 10 in [0.30, 0.36]; F = 14 in [0.23, 0.28]. (Prior run: 1.017 / 0.330 / 0.253) |
| O2 | **Level** | One-day publishable edge at F = 10, p = 1 in [0.155, 0.175] (half of 0.330) |
| O3 | Relation | Arm A cumulative edge = `rho*/(1+p)` within 0.005 at all 15 (F, p) cells. **Near-entailed**: with P = p × C the gate is rho(1+p)C − D, so this checks the code and not the economy. Reported, not counted as evidence |
| O4 | **Level** | Arm B at F = 10, p = 1 lies strictly between `rho*/2` = 0.165 and `rho*` = 0.330, in [0.20, 0.32] (P/C falls as credit accrues, so the late periods that set the edge see less pledge) |
| O5 | Relation | Arm C differs from arm A by more than 0.005 at p = 0.5, F = 10 in either direction |
| O6 | Relation | Publishable edge is at or below break-even 3.78/F in every cell. **Guaranteed by p ≥ 0 and the earlier run**, so it cannot fail; reported for the beside-column the request asked for |

The rule "one-day edge = rho*(F)/(1+p) still holds" is judged on the one-day row (exact by construction) and on arms A, B, C for the cumulative ledger. Arms B and C are where it can fail.
