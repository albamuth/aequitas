# Declared before running — children arms (request sr-20261031-re-run-stable-band-cumulative-py-kappa-tied-)

Written 2026-11-16, before the first run of `stable_band_children.py`.

**Inputs held fixed (as in `stable_band_kappa.py`):** 60,000 people, seed 7; kappa = 1,380/365 = 3.7808; `R_max` = 0.85 × sum(wants) = 56,446 real units; ages from the five-band pyramid, age seeds 11–15; joiner credit `C0 = F·365·age`; M = 100 yearly periods; everyone joins in period 0; nobody ages, dies or is born during the run.

**Arm 0 (control).** Past debit = 1,380 × age. Nothing else.
**Arm 1.** Past debit = 1,380 × max(0, age − 18). Under-18s still request their own wants under their own gate.
**Arm 2.** Arm 1, and every person under 18 requests 0. Their summed requests are split in equal shares across the adults (age ≥ 18) and added to each adult's own request. Refused amounts are lost (not re-offered).

## Outcomes declared

| # | Kind | Statement | Fails if |
|---|---|---|---|
| L1 | **Level** | Arm 0 reproduces the published ρ*_L: 1.017 / 0.330 / 0.253 at F = 2 / 10 / 14, each within ±0.01 | any cell is off by more than 0.01 |
| L2 | **Level** | Arm 1 ρ*_L at F = 10 lies in 0.15–0.30 | outside that range |
| L3 | **Level** | Arm 1 ρ*_L at F = 2 lies in 0.55–0.95, and at F = 14 in 0.12–0.24 | outside either range |
| D1 | Change | Arm 1 ρ*_L is below arm 0 at all three F, by more than 0.02 | any F fails |
| D2 | Change | Arm 2 ρ*_L is at or above arm 1 at all three F (the kids' guaranteed 22% of wants is replaced by gated adult demand) | any F has arm 2 < arm 1 − 0.005 |
| D3 | Change | The period that sets ρ*_L is period 1 in all arms | any arm is set by a later period |
| N1 | Narrow band | At F = 2 the narrow-basket lower edge is 0.71–0.90. Declared: the band **closes** in arm 1 (ρ*_L < 0.71) | ρ*_L ≥ 0.71 in arm 1 |

**Reasoning, so the cells can be checked.** In arm 1 a 40-year-old carries 30,360 h of past debit instead of 55,200 h. At ρ = 0.33 the stored room goes from −7,020 h to about +19,000 h. Under-18s, whose debit is 0, are admitted in full for decades. That is a fixed 22% of wants, so the adults must be rationed harder, and ρ*_L has to fall.
