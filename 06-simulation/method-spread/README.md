# method-spread

**How far does a Foundations §3.4a joint-process split move across honest methods?**

Foundations §3.4a fixes four obligations on how a joint process's debit divides, leaves the method to the industry, and registers this measurement as owed. **If the spread is narrow the obligations are enough. If it is wide, method choice belongs with OP-10 (weighting governance), the project's top blocking problem.**

| | |
|---|---|
| **Superseded** | ⚠️ **2026-09-03.** The §3.4a split rule this measures was withdrawn. **Kept because it is the measurement that caused the withdrawal.** See [`../chain-resolution/`](../chain-resolution/README.md) |
| **Status** | ⚠️ **Leg 1 of 3 run** — the refinery. CHP and livestock are not built |
| **Result** | **WIDE.** Five of seven fractions move by more than the declared threshold. **The modelled conversion routing carries the spread (6.31×); the declared convention is nearly inert (1.29×)** |
| **Answers** | `sr-20260902-take-a-refinery-a-combined-heat-and-power-pl` |
| **Full write-up** | [`RESULTS.md`](RESULTS.md) |

## Run it

```bash
python 06-simulation/method-spread/method_spread.py
```

```bash
python 06-simulation/method-spread/method_spread.py --test
```

```bash
python 06-simulation/method-spread/method_spread.py --csv method_spread.csv
```

## What it reuses

Real DOE 2015 Petroleum Refining Bandwidth Study per-process energies, already loaded by [`../allocation-engine/refinery_slice.py`](../allocation-engine/refinery_slice.py). **No new data was gathered.** This sweep varies the three method choices that file makes and reports how far the answer moves.

## Files

| File | What it is |
|---|---|
| `method_spread.py` | The sweep, the lever attribution, and six self-tests |
| `RESULTS.md` | The write-up, including a first run that was thrown out and why |
| `method_spread.csv` | Every method and every fraction's share |
