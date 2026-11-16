# german-lost-crop

One line of food (fresh fruit and vegetables) loses 50% of its output at the German method. Reports the whole-economy clearing rho, the line's shortfall, and who is short under pro rata and smallest-wants-first sharing.

Extends `../german-prime-sweep/german_prime_sweep.py` (imported, not copied). Request `sr-20261111-lost-crop-at-the-german-method-same-populati`.

| File | What it is |
|---|---|
| `fruitveg_share.py` | Measures the line's share of US consumption hours from EXIOBASE (needs `06-simulation/data/exiobase`; writes `fruitveg_result.json`). Refuses to write unless it reproduces `essentials-basket`'s 131.0 h and 1,398 h |
| `german_lost_crop.py` | The run. `--test` runs 7 self-tests, each of which can fail |
| `DECLARED.md` | Outcomes declared before the run |
| `RESULTS.md`, `RESULTS_RAW.txt` | Results and raw output |

Run: `python fruitveg_share.py`, then `python german_lost_crop.py --test`, then `python german_lost_crop.py`.
