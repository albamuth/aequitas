# fuel-blockade-german

Request `sr-20261111-fuel-blockade-at-the-german-method-same-popu`. Replaces the even capacity cut of `../german-prime-sweep/` with a per-line cut set by each line's fossil share of input. Imports the sweep's population, gate, E, F and solver; copies nothing from it.

- `shares.py`: fossil share per German product line from EXIOBASE 3.10.2 pxp 2022 (`../data/exiobase/IOT_2022_pxp.zip`, read in place). Caches a small `de_fossil_shares.npz`. 7 self-tests (`python shares.py --test`).
- `fuel_blockade.py`: the sweep. 7 more self-tests (`python fuel_blockade.py --test` runs all 13). Run: `python fuel_blockade.py > RESULTS_RAW.txt`.
- `DECLARED.md` (written before the run), `RESULTS.md`, `RESULTS_RAW.txt`.
- **Blocker:** the energy extension in the zip is all zeros, so the shares come from purchases in `Z.txt`, a value share. See `RESULTS.md` section 2.
- `probe.py` and `debug.py` are throwaway inspection scripts kept for the record.
- Needs a Python with numpy (do not run with `-I`).
