# The Labour Debt of Plastic — Q3 (plain-language companion)

> Companion to [`plastic_debt.py`](plastic_debt.py). First sim of the [scenario suite](scenario_suite_METHOD.md).
> **Question:** what is the labour debt of plastic pollution (cleanup time per ton), and what does recycling cost?

## The one-line answer

**Cleaning a tonne of plastic out of the ocean costs about 950 hours of human work — roughly 70× the labour to make it new, and 240× the labour to recycle it. And that's the *lucky* case: microplastic can't be cleaned up at all with any technology we have, so its debt is effectively unbounded — it just sits on whoever last held it, forever, until someone invents a way to remove it.**

That gap is the whole argument. It's why "you own the end of a thing's life" (Foundations §3.6) isn't a moral scold — it's arithmetic.

## The numbers

Debit in Aequitas is a **vector** (§3.2a), so we report two components — the physical energy, and the labour.

**Energy (MJ per kg) — the measured LCA quantity:**

| Resin | Virgin | Mechanically recycled | Energy saved |
|---|---|---|---|
| PET | 69 | 14.5 | 79% |
| HDPE | 76 | 9.1 | 88% |
| PP | 73 | 8.8 | 88% |
| LDPE | 78 | 9.4 | 88% |

Recycling uses **~12–21% of virgin energy**. Chemical recycling (pyrolysis) is far hungrier (~55% of virgin here — wide uncertainty).

**Labour (hours per ton) — via the project's standard cost→labour bridge (≈0.010 h/$):**

| Stage | h/ton |
|---|---|
| Managed landfill | 0.6 |
| Mechanical recycling *(recycler is credited)* | 4 |
| Chemical recycling | 10 |
| Virgin production | 13 |
| Coastal cleanup | 50 |
| **Ocean macro-cleanup (GPGP)** | **950** |
| **Microplastic** | **unbounded** |

## Why this is the §3.3 stock rule, not a special case

Foundations §3.3: a flow is only *pollution* above the rate nature clears it on its own, and its weight tracks the **total remediation** (removal + the damage it does while it sits there). Plastic's natural clearance over human timescales is **~zero** — it persists for centuries. So a discarded plastic is *always* above baseline, and its carried debt is ~the **full cleanup cost, permanently, on the last holder** until someone actually removes it. For ocean macro-debris that's ~950 h/ton. For microplastic there is no scalable removal, so the debt never clears.

**Recycling discharges that debt for a few hours** and hands the material back as a low-cost co-input that never carried the driller's pollution (that stayed with the driller, §3.2b/§3.6). Two wins in one: a fraction of the energy, and none of the extraction pollution.

## What falls out for free (no rule, no regulator)

- **Buy durable, not disposable** — a cheap wrapper whose ~950 h/ton disposal debt you'll carry is not the cheap option.
- **Fund recycling / cleanup** — it *lightens your own* accumulated pollution-debt (§3.3), retroactively.
- **The gradient does the work** — nobody has to ban single-use plastic; the accounting makes it expensive to the person who ends up holding it.

## Honesty ledger (what to flag before quoting these)

- **Cost→labour bridge is a Level-1 reading.** Hours come from `$/ton × economy-average 0.010 h/$` — a ballpark, not a plastics-sector EEIO solve. Refine later with the estimation engine's plastics sector (§3.4a data-first). The **ratios** (ocean ≫ production ≫ recycling) are robust to the bridge; the absolute h/ton are ±.
- **Ocean cost is derived**: $7.5B ÷ 79,000 t (GPGP). Real cleanup cost varies enormously by location and debris type; coastal is cheaper, dispersed microplastic infinitely dearer.
- **Chemical-recycling energy is uncertain** (~0.4–0.9 of virgin in the literature); shown as a single mid.
- **Microplastic "unbounded" is deliberate** — never report a finite headline number for it; the point is that the debt doesn't clear.

## Sources

- Virgin cumulative energy demand & recycling savings — [Franklin Associates / APR *Life Cycle Impacts for Postconsumer Recycled Resins: PET, HDPE, PP* (2018)](https://plasticsrecycling.org/wp-content/uploads/2024/08/2018-APR-LCI-report.pdf) and the [2020 revision summary](https://www.wastedive.com/news/apr-recycled-plastics-reduce-energy-consumption-ghg-emissions/547027/) (PET 79%, HDPE 88%, PP 88%).
- Great Pacific Garbage Patch mass ~79,000 t — [Lebreton et al. 2018, *Scientific Reports* s41598-018-22939-w](https://www.nature.com/articles/s41598-018-22939-w).
- $7.5B to clear the GPGP — [The Ocean Cleanup press release](https://theoceancleanup.com/press/press-releases/the-great-pacific-garbage-patch-can-be-cleaned-for-7-5-billion/).
- US average landfill tipping fee (~$55/ton) — [Environmental Research & Education Foundation (EREF)](https://erefdn.org/).

*Tracks Foundations v0.11 §3.2a / §3.3 / §3.6.*
