# Declared before running — deletion payoff across the conforming band

> **Date:** 2026-11-05. Written before `deletion_payoff.py` was run in full. Known beforehand: the three published edges (ρ\* = 1.017 / 0.330 / 0.253 at F = 2 / 10 / 14, CAP 0.85, anchor 1,380). Nothing else was known.

**Anchor check.** The median-lifestyle anchor has not moved: Foundations v0.67 (2026-11-04) still reads 1,380 h/yr. The range 1,162–1,380 (care covered or not) and 1,296 (adequate provision) are run as sensitivities.

| # | Kind | Declared | Could it fail? |
|---|---|---|---|
| O1 | **Level** | E_max = 365·F·ρ\*(F) at CAP 0.85 lies in [600, 1,350] h/yr at every F from 1 to 14 | Yes. A value above 1,380 would put the band's top edge above break-even |
| O2 | **Level** | At CAP 0.85, d = 1,380, broad-lower basket (826 h): deleting a year pays on the gate in ≥ 95% of the open band (width-weighted) | Yes, if ρ\* crossed 3.78/F anywhere |
| O3 | **Level** | The share of the 27 floors (F = 1..14) where the broad band is open is between 50% and 90% | Yes. Published: closed at F = 2 for broad, open at 10 and 14 |
| O4 | **Relation** | Raising CAP from 0.85 to 0.95 lowers the paying share, or leaves it at 100%. It never raises it | Yes. The sweep could rise if ρ\* moved the wrong way |
| O5 | **Relation** | Raising the filer's yearly debit d from 1,380 to 2,760 gives a share of 100%. Lowering d to 690 gives a share below the d = 1,380 share | Yes |
| O6 | **Entailment test** | The statistic side (credit per day) is positive for every filer with any past work, whatever ρ and F. **If so it is model-entailed and the "pays on both" share equals the gate share.** | Yes: it fails if the statistic ever falls for a worker deleting a floor-only year |

**What would change a reading.** If O2 fails, the counter-incentive is not a corner case of the lowest floors and 5.5.5 needs a fifth condition on ρ·F. If O2 holds at 100%, the break-even 3.78 lies above every conforming ρ·F at the US method, and the exploit is open across the whole band, not at its edge.
