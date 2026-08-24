# Residual unravelling — change history

> Newest entry first. What the project is: [`README.md`](README.md). What it found: [`RESULTS.md`](RESULTS.md).

---

### 2026-08-24 — moved into its own folder. Nothing else changed.

`residual_unravelling.py` and `UNRAVELLING.md` moved from the flat `06-simulation/` directory into `06-simulation/residual-unravelling/`. The script has no local imports and reads no data files, so no code was touched.

One script elsewhere imports this one — [`../audits/audits_inert/generate_bonus.py`](../audits/audits_inert/generate_bonus.py) — and was pointed at the new folder.

**Verified after the move:** `python residual_unravelling.py --test` — eight checks pass.

---

### 2026-08-24 — the fixture published as data

The whole 2,000-agent fixture exported to [`../audits/audits_inert/residual_unravelling.json`](../audits/audits_inert/residual_unravelling.json), with the arithmetic written out in `bonus_sims.md`. Every true debit and every disclosure cost is now readable without running the model.

---

### 2026-08-22 — built and green

Eight self-tests. Tests Foundations §5.1b (producers) and §5.1d condition 1 (periods within a life), which are one mechanism at two scales.

**Two claims had been folded into Foundations v0.17 on the strength of an argument, with no arithmetic behind them.** This supplied the arithmetic, and both hold.

**The control run is what makes it a result.** The same model computed over the whole population — the rule §5.1b rejects — leaves 52.5% dark, stably, against 0.1% on the residual basis.

**One limit was measured rather than assumed:** above a verification cost of about 0.4 of a median unit's debit, unravelling stops working. That number is now cited wherever the coverage argument is made.

Journal entry: [`../../03-journal/2026-08-22.md`](../../03-journal/2026-08-22.md).
