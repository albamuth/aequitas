# Pledge reserve — change history

> Newest entry first. What the project is: [`README.md`](README.md). What it found: [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — moved into its own folder. Nothing else changed.

`pledge_reserve.py`, `PLEDGE_RESERVE.md` and the two figures moved from the flat `06-simulation/` directory into `06-simulation/pledge-reserve/`. The script has no local imports and reads no shared data, so no code was touched.

**Verified after the move:** `python pledge_reserve.py --test` — five checks pass.

---

### 2026-08-14 — built, and the pledge model reversed

[`pledge_reserve.py`](pledge_reserve.py) and [`PLEDGE_RESERVE.md`](PLEDGE_RESERVE.md), five self-tests, two figures.

**Pledges became permanent and non-revocable**, reversing the revocable model that had stood until then. Revocability let a worker who had already consumed against a pledge be stranded when it was withdrawn, and it was gameable.

**Surplus-as-profit was rejected on the axioms.** Banking excess pledges as spendable room re-creates a channel for accumulating consumption advantage. The surplus became a contingent reserve instead: earmarked, non-spendable, and released only against a verified task-caused cost.

**Two guards were added because the first version failed without them.** G1 sends overflow back to the causer, so the reserve is a buffer rather than a shield; without it, coverage licenses carelessness. G2 requires a physical trace linking the harm to the task; without it, an open claim drains the reserve.

Journal entry: [`../../03-journal/2026-08-14.md`](../../03-journal/2026-08-14.md).
