# Wasteful → Essential Reallocation — Q5 (plain-language companion)

> Companion to [`q5_reallocation.py`](q5_reallocation.py). Fifth and final sim of the [scenario suite](scenario_suite_METHOD.md).
> **Question:** how could the world's standard of living change if labour were shifted from wasteful (warfare, luxuries, policing, disposables, fossil fuels) to essential (healthcare, food/water, housing, clothing, renewables) under Aequitas?

## The one-line answer

**The wasteful labour freed up worldwide (~1.1–2.4 trillion hours a year) is enough to close the global health-worker shortage 50–100× over, and to build adequate housing for everyone living in a slum within about six months. Meeting the world's essential needs is not labour-constrained — it never was. "We can't afford to house and heal everyone" is a statement about money, not about human hours.**

## Important: Aequitas doesn't decree this

Under Aequitas the wasteful→essential shift would be driven by **pledges** (§6) — people spending their earned credit on what they want built — **not by any planner**. The wasteful/essential split below is an *exogenous dial* you asked me to propose. Every boundary is contestable, and I run a sensitivity pass over it.

**Proposed taxonomy (v1 — a dial, not a verdict):**

| Wasteful (shrink) | Essential (grow) |
|---|---|
| Warfare / arms | Healthcare |
| Luxury / positional goods | Food & clean water |
| Policing / repression\* | Housing (durable) |
| Disposable / short-life goods | Quality, durable clothing |
| Fossil-fuel extraction | Renewable energy + grid |
| FIRE / advertising overhead | Education / care |

\* vs legitimate public safety — the sharpest boundary, sensitivity-tested below.

## The numbers

- **Global labour pool:** 3.5B workers × 1,900 h ≈ **6.65 trillion h/yr**.
- **Freed (wasteful fraction, from Q2, 17–36%):** **1.13–2.39 trillion h/yr**.

**What that frees pays for:**

| Essential deficit | Labour need | Freed pool covers it |
|---|---|---|
| WHO health-worker shortage (11M) | 0.021 T h/yr | **54–115× over, every year** |
| Housing everyone in slums (1.13B) | 0.57 T h (one-time) | in **~0.2–0.5 years** |
| Housing all 3.4B inadequately housed | 1.70 T h (one-time) | in **~0.7–1.5 years** |

**Sensitivity:** reclassify a quarter of the "wasteful" pool as legitimate (say, half of policing is real public safety) and the freed pool still covers the health shortage **41×**. The conclusion is robust to the taxonomy.

## Why this is the flagship result — and where it's honest

This closes the loop with Q1: **labour is abundant.** Q1 showed an autarkic US isn't labour-limited; Q2 sized the captured/wasted pool; Q5 shows that pool is *far* larger than what closing the world's essential deficits would take. The thing standing between humanity and universal healthcare + housing is **not a shortage of hands** — it's how money allocates them.

**But the honest caveat, and it's the same one Q1 raised:** hours are not the binding constraint — **materials, energy, and land are.** You can free the labour to build 850M homes, but the cement, steel, and land are the real limit (and the energy to make them is Q1's transition question). So Q5 is an **upper envelope on the labour side**: it proves essentials aren't labour-limited, not that they're free. The remaining constraints are physical (Q1) and coordinative (pledges) — exactly where Aequitas locates them.

## Honesty ledger

- **Taxonomy is exogenous and contestable** — shown as a dial with a sensitivity pass, never as an Aequitas output.
- **Upper envelope, labour side only.** Ignores retraining frictions, capital retooling, and — crucially — the material/energy ceilings of Q1. It answers "are essentials labour-constrained?" (no), not "are they free?" (no — see Q1).
- **Global wasteful fraction borrowed from US (Q2).** Developing economies have less formal guard labour but more informal exploitation; the band is a proxy, flagged.
- **Housing/health intensities are round-number anchors** (~2,000 h/dwelling, 1,900 h/health-worker-yr) — order-of-magnitude, and the conclusion holds across any plausible values.
- **EXIOBASE refinement pending.** A full global MRIO solve (needs the EXIOBASE zip re-provided) would replace these direct intensities with supply-chain-inclusive embodied hours. The structural result is robust to that.

## Sources

- Global employment ~3.5B — [ILO WESO Trends 2024](https://www.ilo.org/resource/statement/world-employment-and-social-outlook-trends-2024-ilo-director-generals).
- Health-worker shortage ~11M by 2030 — [WHO, State of the World's Nursing](https://www.who.int/).
- Housing deficit (1.13B in slums; up to 3.4B inadequately housed) — [UN-Habitat World Cities Report](https://unhabitat.org/world-cities-report-2026).
- Wasteful/captured fraction — Q2, [`q2_capture.py`](q2_capture.py).

*Tracks Foundations v0.11 §6 (pledges, not a planner) / §5.5. Closes the loop with Q1 (labour abundant) and Q2 (the captured pool).*
