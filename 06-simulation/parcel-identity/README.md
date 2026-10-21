# parcel-identity

What happens to a joint process's books when the flow sheet cannot say whether two readings name one parcel or two. Answers `sr-20260905-how-often-does-a-joint-process-flow-sheet-fa` (SB-05, from @custos c42203). Foundations §3.4a, conformance rows 10c and 10e.

- `DECLARED.md`: the outcomes, written before the first run.
- `parcel_identity.py`: the model, five experiments, nine self-tests.
- `parcel_identity.csv`: every row of the run (79 rows).
- `RESULTS.md`: the numbers and what they do not show.

It reuses `../chain-resolution/` (the refinery and steer chains) and ties to it in a self-test, so the identified-by-construction case and this one share one truth.

```
python parcel_identity.py --test     # 9 self-tests, under 5 s
python parcel_identity.py            # full run, about 1 minute, seed 20261018
```

Needs numpy only. Writes about 20 KB.
