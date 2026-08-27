# Median lifestyle — change history

> Newest entry first. What the project is: [`README.md`](README.md). What it found: [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — ruling: `track3_imports.py` is Track 3

**The two track-3 files contradicted each other and neither the author nor a reader could tell which was current.** Settled from the record rather than by preference:

| Evidence | Says |
|---|---|
| [`TRACK3.md`](TRACK3.md), 2026-08-17, the newest track-3 doc | Names `track3_imports.py` in its first line, with 3 self-tests green |
| [`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md), the headline result | Cites `track3_imports.py` |
| This changelog, entry of 2026-08-17 | *"Track 3 rebuilt as `track3_imports.py`, a full EXIOBASE solve replacing a wage-and-margin ballpark"* |
| `track3_result.json` | Written by `track3_imports.py`; the self-tests read it |
| `track3_exiobase.py` | 2026-08-10. No self-tests. Cannot run without the 234 MB zip passed by hand. |

**Where the confusion came from.** `track3_exiobase.py`'s own docstring said it *"replaces the wide wage/margin ballpark in track3_imports.py"*. **That was true on 2026-08-10 and stopped being true on 2026-08-17**, when `track3_imports.py` was rebuilt to do the full solve itself. The comment outlived the file it described. **Corrected in place**, with the history stated so the next reader does not repeat the question.

**`track3_exiobase.py` was not archived**, because [`average_footprint.py`](average_footprint.py) imports its `L @ Y` machinery to answer a different question — the environmental footprint rather than the labour one. It is retained as shared plumbing and is marked, at the top of the file and in the README, as **not a Track 3 answer**. Its number must never appear beside `track3_imports.py`'s.

**Recorded and not fixed:** [`average_household.py`](average_household.py) calls `track4_pollution.compute`, renamed when Track 4 was rewritten on 2026-08-17. It is a results-producing script and guessing at its intent is worse than leaving it visibly broken. Flagged in the README.

---

### 2026-08-24 — moved into its own folder; the v1 estimate archived

The tracks, their write-ups, their four figures and the two mean-not-median scripts moved from the flat `06-simulation/` directory into `06-simulation/median-lifestyle/`.

**The superseded top-down v1 estimate moved to [`archive/`](archive/)** — `median_lifestyle.py`, `median_lifestyle_charts.py`, `MEDIAN_LIFESTYLE.md` and three figures. It was already marked superseded in three current documents; this puts it where the project keeps superseded work. **Nothing was deleted.**

**Five path fixes, no behaviour change.** The data folder stayed shared at `06-simulation/data/`, because the Statera kernel will need the same tables. Five scripts built their data paths from their own location and now reach up one level: `track1_labour.py`, `track1_embodied_hours.py`, `track1_by_category.py`, `track3_imports.py`, `track6_country_labour.py`.

**Verified after the move:** track 1 (three scripts), track 2 (two), track 3, track 4 (two) and track 6 (two) all pass their self-tests. `track6_country_labour.py --show` prints from cache.

**One pre-existing breakage recorded rather than fixed:** `average_household.py` calls `track4_pollution.compute()`, which stopped existing when track 4 was rewritten on 2026-08-17. It has been broken since then, and the move did not cause it.

---

### 2026-08-17 — Q6, and the tracks rebuilt on measured data

**Q6 added** — [`track6_country_labour.py`](track6_country_labour.py), [`track6_efficiency.py`](track6_efficiency.py), [`Q6.md`](Q6.md). The finding: Spain delivers a comparable material standard on **709 hours** per person per year against the US's **1,283**, and lives nearly six years longer.

**Track 1 rebuilt** as [`track1_embodied_hours.py`](track1_embodied_hours.py) and [`track1_by_category.py`](track1_by_category.py), replacing a coarser calculation. Headline: **612 hours per capita**, with the total checked against actual 2023 personal consumption of $18.82 trillion.

**Track 3 rebuilt** as [`track3_imports.py`](track3_imports.py), a full EXIOBASE solve replacing a wage-and-margin ballpark. Result cached in `track3_result.json`, because the parse takes minutes.

**Track 4 rewritten** as the current [`track4_pollution.py`](track4_pollution.py), tracking the change to Foundations §3.2b on how electricity is treated. **This is the rewrite that broke `average_household.py`.** [`track4_carbon_intensity.py`](track4_carbon_intensity.py) replaced the economy-average shortcut with real sector multipliers: carbon capture is not an average activity, and engineered direct air capture is labour-light.

**Track 2 split** into [`track2_durables.py`](track2_durables.py) and the existing housing script, with the double-counting argument made explicit.

Journal entry: [`../../03-journal/2026-08-17.md`](../../03-journal/2026-08-17.md).

---

### 2026-08-10 — the bottom-up result assembled

[`MEDIAN_LIFESTYLE_RESULT.md`](MEDIAN_LIFESTYLE_RESULT.md) and the four figures. **≈ 1,350–1,400 hours per adult per year**, against ≈ 3,650 hours of self-care credit — about one third of one person's annual credit.

---

### 2026-08-09 — the top-down v1 estimate rejected, and rebuilt bottom-up

The original `median_lifestyle.py` applied a single blanket labour-per-dollar ratio to total spending. [`median_lifestyle_METHOD.md`](median_lifestyle_METHOD.md) rejected it on three grounds: **it assumes the labour allocation rather than measuring it, it misses labour carried forward in durables, and it mixes data years.**

The v1 files are kept in [`archive/`](archive/) as a rough sanity bracket. **The two methods corroborate each other**, which is why they are kept rather than discarded.

The replacement is bottom-up, category by category, on one internally consistent year, with every input a named constant carrying its source.

Journal entry: [`../../03-journal/2026-08-09.md`](../../03-journal/2026-08-09.md).

---

### 2026-02-06 — the data source was withdrawn

The Bureau of Labor Statistics withdrew the Employment Requirements matrices. The copies in `../data/erm_full/` were recovered through the **[Internet Archive](https://web.archive.org/web/2025/https://www.bls.gov/emp/data/input-output-matrix.htm)** and are the only ones we have. **Every track 1 figure depends on them.**
