# honest-label

Does a producer who labels a published figure *metered* or *modelled* out-compete one who does not, or does the label only show rivals where to attack? Answers SB-04 ([`../sim-briefs/SB-04_honest-label.md`](../sim-briefs/SB-04_honest-label.md)), request `sr-20260904-does-a-producer-who-labels-each-published-fi`.

- `labelling_game.py` — the model, the self-tests, and the sweep. One file.
- `DECLARED.md` — the outcomes, written before the full run.
- `RESULTS.md` — the numbers and what they do not show.
- `results.json` — the run output.

```
python labelling_game.py --test
python labelling_game.py
```

Model in one paragraph: `N` producers choose label or no label. Unlabelled figures are discounted by `1+d`. Each rival may pay `a` to challenge the producer with the best expected prize; a success moves `g` of that producer's trade to the rival. Payoffs have a closed form (checked against Monte Carlo). Stability is read from the payoff gap between a labeller and a non-labeller at every mix. Status: done 2026-10-17, nightly agent.
