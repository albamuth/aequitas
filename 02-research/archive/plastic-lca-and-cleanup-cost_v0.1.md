# Research stub — Plastic LCA energy & cleanup cost

> Retrieved 2026-08-10. Feeds Q3 of the scenario suite ([`06-simulation/scenario-suite/plastic_debt.py`](../../06-simulation/scenario-suite/plastic_debt.py), [`PLASTIC.md`](../../06-simulation/scenario-suite/PLASTIC.md)).
> **Why it matters:** supplies the real anchors for the labour debt of plastic (§3.3 stock rule / §3.6 recycling). The virgin-vs-recycled energy gap and the GPGP cleanup cost drive the headline "ocean cleanup ≈ 70× production, microplastic unbounded."

## Sources

| Fact used | Value | Source |
|---|---|---|
| Virgin cumulative energy demand | PET ~69, HDPE ~76, PP ~73, LDPE ~78 MJ/kg | [Franklin/APR 2018 LCI report](https://plasticsrecycling.org/wp-content/uploads/2024/08/2018-APR-LCI-report.pdf); PlasticsEurope eco-profiles |
| Mechanical-recycling energy saving | PET 79%, HDPE 88%, PP 88% | [Franklin/APR LCA, 2020](https://www.wastedive.com/news/apr-recycled-plastics-reduce-energy-consumption-ghg-emissions/547027/); [Recycling Today](https://www.recyclingtoday.com/news/apr-life-cycle-impact-assessment-recycled-pet-hdpe-pp/) |
| GPGP total floating mass | ~79,000 t (≈80,000 t; 1.8T pieces) | [Lebreton et al. 2018, *Sci. Reports* s41598-018-22939-w](https://www.nature.com/articles/s41598-018-22939-w) |
| Cost to clear the GPGP | $7.5B → ~$95,000/ton | [The Ocean Cleanup press release](https://theoceancleanup.com/press/press-releases/the-great-pacific-garbage-patch-can-be-cleaned-for-7-5-billion/) |
| US average landfill tipping fee | ~$55/ton | [EREF](https://erefdn.org/) |

## Follow-ups (queued)
- **Plastics-sector EEIO solve** to replace the economy-average 0.010 h/$ bridge with a real embodied-hours multiplier (§3.4a data-first). The ratios are robust; only the absolute h/ton would tighten.
- **Chemical recycling (pyrolysis) net energy** — literature spans ~0.4–0.9 of virgin; a single defensible LCA would replace the modelled 0.55.
- **Microplastic remediation** — confirm no scalable removal tech exists (justifies the "unbounded" treatment); watch for emerging methods that would put a finite (if huge) number on it.
