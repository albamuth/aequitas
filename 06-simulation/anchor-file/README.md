# anchor-file — one published anchor, read not typed

Request `sr-20261106-in-rho-sweep-anchor-py-and-stable-band-kappa`.

| File | What it is |
|---|---|
| `median_lifestyle_anchor.json` | The anchor: value 1,380 h/yr, interval 1,350–1,400, method, version, and a list of inputs with whether a stranger can fetch each |
| `anchor.py` | The only reader. `load()` hashes the JSON (LF-normalised) and raises `AnchorDigestError` if it is not the pin `PINNED_SHA256` |
| `predictions.json` | Eight predictions, including the old self-test 5. Never edited |
| `predictions.py` | Registers the file's sha256 as line 1 of `predictions_log.jsonl`, refuses a later edit, appends every outcome |
| `predictions_log.jsonl` | Append-only log. Do not edit |
| `anchor_sweep.py` | Prints rho* at anchor 1,350 / 1,380 / 1,400 and F = 2, 10, 14 on both instruments; `--test` runs 5 plumbing tests |

Changed elsewhere: `disparity-ceiling/rho_sweep_anchor.py` (reads the file; self-test 5 now runs the predictions file) and `stable-band/stable_band_kappa.py` (reads the file; two new self-tests).

```
python 06-simulation/anchor-file/anchor_sweep.py --test
python 06-simulation/anchor-file/anchor_sweep.py
python 06-simulation/disparity-ceiling/rho_sweep_anchor.py
python 06-simulation/stable-band/stable_band_kappa.py --test
```

To change the anchor on purpose: edit the JSON, recompute the sha256 (LF form), change `PINNED_SHA256`. Both edits show in one diff.
Do not run these with `python -I`: the sims import their neighbours from the script directory and numpy from the user site.
