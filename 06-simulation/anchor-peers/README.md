# anchor-peers

Recomputes the German, Japanese and Spanish median-lifestyle anchors (published 883, 883, 759 h/yr) from the every-payer Q6 ratios, and republishes the break-evens `ρ*F = anchor/365`.

```
python -I anchor_peers.py --test    # 9 self-tests
python -I anchor_peers.py           # the table
```

Reads `../median-lifestyle/q6_payers_result.json`. Results: [`RESULTS.md`](RESULTS.md).
