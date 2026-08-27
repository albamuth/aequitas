# Median lifestyle — what a normal life costs in hours

> **Status:** ✅ The four tracks are done and green. This is the project's real-world anchor, ≈ **1,380 hours per year**.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Assembled result:** [`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

## The question

Aequitas credit is human time. So "what does a lifestyle cost" means: how many person-hours of labour are embodied in everything a median US adult consumes in a year?

That number is what makes every other result concrete. The disparity ceiling is a ratio; this is what the ratio is a ratio *of*.

## The four tracks, plus two extras

Each is a separate tested script. They are added together in [`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md).

| Track | Question | Scripts | Write-up |
|---|---|---|---|
| **1 — domestic** | Hours worked **in the US** embodied in what a person consumes | [`track1_embodied_hours.py`](track1_embodied_hours.py) · [`track1_labour.py`](track1_labour.py) · [`track1_by_category.py`](track1_by_category.py) | [`TRACK1.md`](TRACK1.md) |
| **2 — durables** | Housing structure, which is booked as investment and so missing from track 1 | [`track2_housing.py`](track2_housing.py) · [`track2_durables.py`](track2_durables.py) | in `MEDIAN_LIFESTYLE_RESULT.md` |
| **3 — imports** | Hours worked **abroad** embodied in what a person imports | [`track3_imports.py`](track3_imports.py) — **this is the Track 3 answer** | [`TRACK3.md`](TRACK3.md) |
| **4 — own pollution** | Hours to remediate the pollution the person causes **by their own action** | [`track4_pollution.py`](track4_pollution.py) · [`track4_carbon_intensity.py`](track4_carbon_intensity.py) | [`TRACK4.md`](TRACK4.md) |
| **6 — efficiency** | Which rich countries deliver a comparable life for fewer hours | [`track6_country_labour.py`](track6_country_labour.py) · [`track6_efficiency.py`](track6_efficiency.py) | [`Q6.md`](Q6.md) |
| **mean, not median** | What everyone *would* have if consumption were shared evenly | [`average_household.py`](average_household.py) · [`average_footprint.py`](average_footprint.py) | in `MEDIAN_LIFESTYLE_RESULT.md` |

**There is no track 5.** The numbering follows the method plan, which had a track that was folded into another.

**Q6 is not part of the Q1–Q5 scenario suite** despite the name. It came later, from track 6, and lives here. The scenario suite is in [`../scenario-suite/`](../scenario-suite/).

## Run it

```bash
python track1_embodied_hours.py --test
python track2_housing.py --test
python track3_imports.py --test         # uses the cached track3_result.json
python track4_pollution.py --test
python track6_efficiency.py --test      # uses the cached track6_country_result.json
python track6_country_labour.py --show  # prints from cache; no argument re-parses EXIOBASE
```

Needs `numpy`, `openpyxl`, and `pymrio` for the import tracks.

## Data

**The Bureau of Labor Statistics tables live in the shared `../data/` folder**, not in this project, because the Statera kernel will need them too. **That folder is 288 MB and is not published; download the tables from [the BLS programme page](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm) to reproduce this.** The scripts reach up one level to find them.

> **⚠️ The Bureau of Labor Statistics withdrew the Employment Requirements matrices on 2026-02-06.** The copies in `../data/erm_full/` were recovered through the **[Internet Archive](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm)** and are the only ones we have. **Do not delete them.**

The EXIOBASE table (`../data/exiobase/IOT_2022_pxp.zip`, 234 MB) takes one to three minutes to parse, so the two scripts that use it cache their answers in `track3_result.json` and `track6_country_result.json`. Those caches are checked in, and the self-tests read them.

### Two files here are not tracks, and one of them is broken

| File | What it is | State |
|---|---|---|
| [`track3_exiobase.py`](track3_exiobase.py) | **Not the Track 3 answer.** It was superseded on 2026-08-17 when `track3_imports.py` was rebuilt to do the full EXIOBASE solve itself. It stays only because `average_footprint.py` imports its machinery for a different question. **Never cite it for Track 3, and never show its number beside `track3_imports.py`'s.** | superseded, retained as plumbing |
| [`average_footprint.py`](average_footprint.py) | The **environmental** footprint of the average person — CO₂, materials, land, water, energy. Same EXIOBASE machinery, different satellites. A different question from the four tracks. | works; needs the 234 MB zip as an argument, no `--test` |
| [`average_household.py`](average_household.py) | The **mean** lifestyle rather than the median — what everyone would have if consumption were shared evenly. | **🔴 broken.** Calls `track4_pollution.compute`, which was renamed when Track 4 was rewritten on 2026-08-17. Left visibly broken rather than guessed at. |

## Known broken

**`average_household.py` does not run.** It calls `track4_pollution.compute()`, which no longer exists — track 4 was rewritten on 2026-08-17 and the mean-not-median script was never updated to match. **This broke before the folder reorganisation and is unrelated to it.** The fix is to call `track4_pollution.totals()` and adjust for the changed return shape.

## Superseded work

[`archive/`](archive/) holds the **top-down v1 estimate** — `median_lifestyle.py`, `MEDIAN_LIFESTYLE.md` and three figures. It was rejected as unsound: it *assumes* the labour allocation rather than measuring it, misses labour carried forward in durables, and mixes data years. **It is kept as a rough sanity bracket, and the two methods do corroborate each other.** Never quote it as a result.
