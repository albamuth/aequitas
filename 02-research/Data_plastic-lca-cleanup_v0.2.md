# Plastic — the Energy to Make It and the Cost to Clean It Up

**Version:** 0.2
**Type:** data-source note
**Retrieved:** 2026-08-10
**Feeds:** the plastic-pollution scenario ([`06-simulation/scenario-suite/plastic_debt.py`](../06-simulation/scenario-suite/plastic_debt.py) and [`PLASTIC.md`](../06-simulation/scenario-suite/PLASTIC.md)).

**Why it matters.** This note supplies the real-world numbers behind Aequitas's treatment of plastic as a lasting debt. Two Aequitas rules are in play:
- **A pollutant costs more the more of it is already out there** — because the more there is, the more work it takes to deal with. See [Foundations §3.5](../00-strategy/Aequitas_Foundations_v0.28.md).
- **Recycled material is cheaper because it never carried the original mining/drilling pollution** — that stayed with whoever first extracted it. See [Foundations §3.6](../00-strategy/Aequitas_Foundations_v0.28.md#36-end-of-life-recycling-and-product-as-pollution).

The gap between the energy to make *new* plastic and the energy to *recycle* it, plus the cost of cleaning plastic out of the ocean, drive the headline finding: **cleaning plastic out of the ocean takes roughly 70 times the work of making it new, and microplastic can't be cleaned up at scale at all — so its debt is effectively permanent.**

## Sources

*A note on units: "MJ/kg" is megajoules of energy per kilogram — how much energy it takes to make one kilo of the material. "t" is a metric tonne. "$/ton" is dollars to clean up one tonne. The four plastics listed are the common ones: PET (drink bottles), HDPE and LDPE (tougher and softer packaging), PP (tubs and caps).*

| Fact used | Value | Source |
|---|---|---|
| Energy to make **new** plastic | PET ~69, HDPE ~76, PP ~73, LDPE ~78 MJ/kg | [Franklin/APR 2018 life-cycle report](https://plasticsrecycling.org/wp-content/uploads/2024/08/2018-APR-LCI-report.pdf); PlasticsEurope eco-profiles |
| Energy *saved* by recycling instead | PET 79%, HDPE 88%, PP 88% | [Franklin/APR life-cycle assessment, 2020](https://www.wastedive.com/news/apr-recycled-plastics-reduce-energy-consumption-ghg-emissions/547027/); [Recycling Today](https://www.recyclingtoday.com/news/apr-life-cycle-impact-assessment-recycled-pet-hdpe-pp/) |
| Plastic floating in the Great Pacific Garbage Patch | ~79,000 t (~1.8 trillion pieces) | [Lebreton et al. 2018, *Scientific Reports*](https://www.nature.com/articles/s41598-018-22939-w) |
| Cost to clear that patch | $7.5 billion → ~$95,000 per tonne | [The Ocean Cleanup](https://theoceancleanup.com/press/press-releases/the-great-pacific-garbage-patch-can-be-cleaned-for-7-5-billion/) |
| Typical US landfill dumping fee | ~$55 per tonne | [Environmental Research & Education Foundation](https://erefdn.org/) |

*("Life-cycle assessment" = adding up a product's total footprint from raw material through disposal. The Great Pacific Garbage Patch is the largest of the ocean plastic accumulations, between California and Hawaii.)*

## Follow-ups (queued)

- **A plastics-specific supply-chain solve** to replace the rough economy-average conversion (0.010 hours of labour per dollar) with a real "hours of work embodied in a tonne of plastic" figure. The *ratios* in the finding are solid; only the absolute hours-per-tonne would tighten. (This connects to the supply-chain engine — see [Estimation-engine data sources](../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources).)
- **Chemical recycling (breaking plastic back down with heat) net energy** — the literature ranges from about 0.4 to 0.9 of the energy of making new plastic; one solid study would replace the modelled 0.55.
- **Microplastic clean-up** — confirm that no scalable removal technology exists (which is what justifies treating its debt as effectively unbounded), and watch for emerging methods that would put a finite, if enormous, number on it.

## Related

- [Estimation-engine data sources](../00-strategy/GLOSSARY.md#src-estimation-engine-data-sources) · [retroactive-reweighting](../01-wiki/retroactive-reweighting.md) · [material-flow-value](../01-wiki/material-flow-value.md)
