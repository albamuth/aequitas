# stable-band — the band of `F` and ρ inside which a network works

> **Status:** ✅ **Complete, 2026-08-28.** Answers Foundations §5.5.3's owed simulation. Registered against **OP-4 (debit tolerance)**.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`stable_band.py`](stable_band.py)

## What it answers

**Foundations §5.5.3 gives the floor a bound at each end and nothing in between**, and says so in its own text:

> *"⚠️ Owed: a simulation showing the stable band, and its width. Nothing in this section claims the band has been found."*

**Two dials, and Aequitas sets neither** (A8):

- **`F`, the floor** — hours a day a network credits for the work of staying alive.
- **ρ, the debit tolerance** — the multiplier in the consumption gate `D ≤ ρ·C`.

**Set them too low and people cannot afford essentials. Set them too high and the ledger stops rationing anything.** This finds where both hold.

## Run it

```bash
python stable_band.py --test      # 5 self-tests, each able to fail
python stable_band.py             # the full sweep, about 3 minutes
```

**It runs every cell through the Statera kernel's real gate and all eight conformance checks.** It imports `../statera/statera.py`; nothing needs installing beyond numpy.

## The headline

**The band exists at every floor from 1 to 14 hours a day, for every essentials basket tested. It never closes.** What binds is capacity, not affordability. **The width in ρ falls as the floor rises**, from about 3.2 at a 1.5-hour floor to 0.70 at a 14-hour floor.

**Read [`RESULTS.md`](RESULTS.md) for the tables, the three things this does not show, and why it is an instrument rather than a ceremony.**
