# resolution-tax

> **Version:** 0.1
> **Date:** 2026-10-19

**How far apart are two producers of one good, same physical process, when one can afford to read the chain finely and the other cannot?**

Builds on [`../chain-resolution/`](../chain-resolution/), which proved a coarse reading is a ceiling. This asks who pays that ceiling, by producer scale and chain length.

| | |
|---|---|
| **Status** | Complete. 7/7 self-tests pass |
| **Result** | Typical early-leaving good: best-to-worst spread about 2× at every chain length. Mean and tail grow with ln(n) |
| **Biggest caveat** | Who pays is set by an affordability cap I chose. See RESULTS section 5 |
| **Write-up** | [`RESULTS.md`](RESULTS.md) |

```bash
python 06-simulation/resolution-tax/resolution_tax.py
python 06-simulation/resolution-tax/resolution_tax.py --test
```

Files: `resolution_tax.py` (model, sweep, tests) · `RESULTS.md` · `run_output.txt` (the run quoted in RESULTS).
