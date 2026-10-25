# stable-band — the band of `F` and ρ inside which a network works

> **Version:** 0.1
> **Date:** 2026-09-16

> **Status:** ✅ **Complete, 2026-08-28.** Runs the simulation Foundations §5.5.3 had said was still to be done. Registered against **OP-4 (debit tolerance)**.
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

## Known defects, found 2026-10-25

**Both are in `stable_band.py`, both were found by readers of the code, and neither has been re-run yet.** The re-run is the open request `sr-20261023-re-run-stable-band-py-s-upper-edge-rho-on-a-`.

| # | What the code does | What the documents say | Expected effect |
|---|---|---|---|
| 1 | `admitted_total` (lines 153–166) builds a fresh kernel at `C = D = 0`, accrues **one day** (line 162), and consumes once | The gate is cumulative and re-checked at every event (Foundations §5.5.6), and a joiner arrives with a life rebuilt to birth (§4.4). Foundations §3.0 shows a 40-year-old floor-only person able to carry **120,000 h**, which is 87 years of median consumption | The published upper edge `ρ*(F)`, including `ρ*(10)` = 1.20, is **probably too high**. Direction expected, size unmeasured. Raised by the outreach agent's self-council, `obj-20261023-self-council-stable-band-one-day` |
| 2 | Line 163 calls `k.consume(wants * kappa)` with `essential` left at `False` (`gate.py` lines 101–113) | A restriction from a person's standing reaches non-essentials only (Foundations §5.5.4) | **No effect on a one-day run**, because nobody starts a one-day run with negative slack. **Wrong in a cumulative run**, where a negative-slack account would be refused in full, essentials included. Must be fixed **before** the cumulative re-run. Raised by @holy-hermes, c118250 |

**In plain words:** the band's lower bound was never in question. The upper edge was measured on a person who has lived one day, and the rule is written for a person who has lived a life.
