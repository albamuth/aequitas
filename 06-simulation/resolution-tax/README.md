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

**Part 2 (2026-10-25):** resolution spread against efficiency spread, one generator, one statistic. Request `sr-20260909-off-one-generator-measure-the-spread-in-a-co`.

```bash
python 06-simulation/resolution-tax/res_vs_eff.py
python 06-simulation/resolution-tax/res_vs_eff.py --test
```

Files: `resolution_tax.py` (model, sweep, tests) · `res_vs_eff.py` (Part 2, imports the first) · `DECLARED_res_vs_eff.md` (outcomes written before the run) · `RESULTS.md` (Part 1, then Part 2) · `run_output.txt` (Part 1 run).
