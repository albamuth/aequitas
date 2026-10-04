# essentials-basket — `E`, the hours behind a year of essentials

> **Version:** 0.1
> **Date:** 2026-09-24

> **Status:** ✅ **Complete, 2026-09-24.** Measures `E` in Foundations §5.5.3 (the floor's lower bound), which had only been illustrative (700 h) or swept.
> **Result:** [`RESULTS.md`](RESULTS.md) · **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`essentials.py`](essentials.py) · **History:** `CHANGELOG.md`

## What it answers

**Foundations §5.5.3 says a floor `F` works only if `ρ · F · 365 ≥ E`.** `E` is the hours of other people's work behind one person's year of essentials. This measures it.

## Run it

```bash
python essentials.py            # parse EXIOBASE and solve, about 3 minutes
python essentials.py --show     # print the cached result
python essentials.py --test     # 3 self-tests on the cached result
python logistics_chain.py       # are the peers' supply chains shorter? about 4 minutes
```

**Needs** `../data/exiobase/IOT_2022_pxp.zip`, and two results from `../median-lifestyle/`: `health_share_result.json` and `health_peer_result.json`.
