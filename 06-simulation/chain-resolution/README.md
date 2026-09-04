# chain-resolution

**If a joint process's cost is not divided, what does reading the chain more finely change — and do the books inflate?**

The author ruling of 2026-09-03 withdrew the Foundations §3.4a split. **Every co-product now carries the whole cost of the process it came through, read against its own output mass.** This run answers the two questions that ruling raised.

| | |
|---|---|
| **Status** | ✅ **Complete for its two cases.** 8/8 self-tests pass |
| **Result 1** | **A coarse reading is a ceiling on a fine reading, always.** Confirmed on 1,152 product-resolution pairs, no exception. Equality only for a product that passes the whole chain |
| **Result 2** | **The books do not inflate.** The union over identified parcels is **exactly** the chain total at all 192 resolutions swept. **A naive sum overstates it by up to 7.00× and changes with resolution** |
| **Replaces** | [`../method-spread/`](../method-spread/), whose question no longer exists |
| **Full write-up** | [`RESULTS.md`](RESULTS.md) |

## Run it

```bash
python 06-simulation/chain-resolution/chain_resolution.py
```

```bash
python 06-simulation/chain-resolution/chain_resolution.py --test
```

```bash
python 06-simulation/chain-resolution/chain_resolution.py --csv 06-simulation/chain-resolution/chain_resolution.csv
```

## The one line to take away

**A product carries the cost of the steps it passed through, divided by its own mass.** Those steps are a subset of all the steps and the mass is unchanged, **so a coarser reading can only ever charge more.** A producer wanting a lower figure has to buy more measurement.

## What it reuses

Real DOE 2015 Petroleum Refining Bandwidth Study per-process energies, already loaded by [`../allocation-engine/refinery_slice.py`](../allocation-engine/refinery_slice.py). **No new data was gathered.**

**What it needs that the withdrawn rule did not have:** only **whether** a product passed through a unit — binary, off a flow sheet. The withdrawn rule needed **what share** of that unit's energy the product took, and that share is what moved LPG by 6.31×.

## Files

| File | What it is |
|---|---|
| `chain_resolution.py` | The model, both cases, the resolution sweep, and eight self-tests |
| `RESULTS.md` | The write-up, with the theorem and the five things it does not show |
| `chain_resolution.csv` | Every product, dimension and resolution extreme |
