# Allocation engine — turning a physical economy into per-product costs

> **Status:** ✅ All four pieces built and green. Components C3 and OP-3; answers Objections §C tests 1 and 4.
> **Results:** [`RESULTS.md`](RESULTS.md) · **Change history:** [`CHANGELOG.md`](CHANGELOG.md)

## What this is

Four scripts, one pipeline, built in that order over 2026-08-05 to 08-13. They share a folder because each imports the one before it.

**The problem they solve.** Foundations §3.4a says a joint process divides its cost by where the process physically sent its inputs. But every input is itself the output of another joint process, so a product's cost is defined recursively. Two things were asserted and unproven:

1. **Does the recursion terminate?** Even with cycles — the corn-and-iron structure economists argue about.
2. **Is every share non-negative?** Steedman showed that value-based joint-production systems can produce negative aggregate values. Does a physical allocation escape that?

## The four pieces

| Script | What it does | Write-up |
|---|---|---|
| [`recursion_convergence.py`](recursion_convergence.py) | **The solver.** Builds synthetic economies, runs the physical allocation and a rival value/price allocation on the same data, and reports convergence and non-negativity. | [`RECURSION_RESULTS.md`](RECURSION_RESULTS.md) · [`recursion_convergence_SPEC.md`](recursion_convergence_SPEC.md) |
| [`estimation_engine.py`](estimation_engine.py) | **The engine.** Produces a per-product debit vector — materials, energy, labour kept separate — for a 12-good economy with two joint processes. | [`ESTIMATION.md`](ESTIMATION.md) |
| [`exiobase_loader.py`](exiobase_loader.py) | **The real-data plug.** Feeds a real environmentally-extended input-output table into the same solver, and checks the answer against the reference implementation. | in `ESTIMATION.md` |
| [`refinery_slice.py`](refinery_slice.py) | **The hard case.** One refinery, one crude input, many products. Physical split against price allocation on real energy data. | [`REFINERY.md`](REFINERY.md) · [`refinery_slice_PLAN.md`](refinery_slice_PLAN.md) |

"EEIO" means environmentally-extended input-output — a published table of who buys what from whom, with physical flows attached. "MRIO" is the multi-region version. [EXIOBASE](https://www.exiobase.eu/) is the one used here, because it uniquely reports embodied labour in **hours**.

## Run it

```bash
python recursion_convergence.py --test    # self-tests, seconds
python recursion_convergence.py           # the full sweep -> results.csv + four plots (slow)
python estimation_engine.py --test
python exiobase_loader.py --test          # uses pymrio's small built-in table
python refinery_slice.py --test
```

Needs `numpy` and `scipy`; `exiobase_loader.py` needs [`pymrio`](https://pymrio.readthedocs.io/); the plots need `matplotlib`. **The self-tests need no downloaded data.** `exiobase_loader.py --test` runs against `pymrio.load_test()`, a tiny table with the real EXIOBASE structure.

## Data files here

| File | What it is |
|---|---|
| `results.csv` | The full 5,224-run convergence sweep. Regenerate with `python recursion_convergence.py`. |
| `results_quick.csv` | A short sweep, for a fast check. |
| `results_*.png` | Four figures from the sweep. |
| `estimation_debit_vectors.csv` | The 12-good economy's per-product debit vectors. |
| `refinery_allocation.csv` | The refinery's fraction slate under both allocations. |

## Who depends on this

[`../audits/arithmetic_audits.py`](../audits/arithmetic_audits.py) imports the solver for IC-10 rather than rebuilding it — the non-negativity result proved here across 4,098 economies is inherited, not re-asserted.
