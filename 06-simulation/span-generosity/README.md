# span-generosity

Does seller choice arrest a network that recruits by generous span estimates? Request `sr-20260919-sweep-span-estimate-generosity-across-compet`.

- Run: `python span_generosity.py`  (self-tests: `--test`)
- Output: `RUN.txt`, `sweep.csv`, `sweep_summary.json`. Findings: `RESULTS.md`.
- Seed 20261120 + replication number.
- Self-tests T1–T6 each can fail (Foundations figure −175 h, baseline share, lever exists, detection arrests, blind joiners unmoved, weak sampler misses).
