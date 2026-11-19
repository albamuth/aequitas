# Peer anchors recomputed — German, Japanese, Spanish

> **Version:** 0.1
> **Date:** 2026-11-19

## 1. The question

> *Recompute the German/Japanese 883 h/yr and Spanish 759 h/yr median-lifestyle anchors under the current joint-production rule, the same way the 1,380 h/yr US anchor was recomputed on 2026-09-04. Report whether the three move together or separately, and republish the three break-even values rho\*F = anchor/365.*

Request `sr-20260919-recompute-the-german-japanese-883-h-yr-and-s`.

## 2. Declared before running

| # | Outcome | Kind |
|---|---|---|
| L1 | **Level.** The German every-payer anchor falls in 1,100–1,200 h/yr, the Spanish in 900–1,000 h/yr. Foundations §5.5.3 quotes "1,150 to 1,200" for German or Japanese. | Size of a number |
| L2 | **Level.** The German break-even `ρ*F` is at least 3.0 h/day (published: 2.42). | Size of a number |
| C1 | The joint-production rule moves no peer anchor, because the Q6 scripts have no allocation step (same result as the US audit of 2026-09-05). | Change |
| C2 | The 883 and 759 figures are reproduced by 1,380 × the old household-only ratio, rounded to 2 decimals. If not, their origin is unknown. | Could fail |
| C3 | German and Japanese move together (within 1% of each other). Spain moves by a different percentage (more than 3 points apart). | Change |

## 3. The numbers

Source: `06-simulation/median-lifestyle/q6_payers_result.json` (EXIOBASE 3, 2022, hours per person per year). The ratio is peer hours ÷ US hours.

| | Household-only hours | Every-payer hours | Old ratio | **New ratio** | Published anchor | Old ratio × 1,380 (exact) | **New anchor** | Move |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| US | 1,283 | 1,283 | 1.000 | **1.000** | 1,380 | 1,380 | **1,380** | 0.0% |
| Germany | 820 | 1,072 | 0.639 | **0.836** | 883 | 882 | **1,153** | +30.6% |
| Japan | 862 | 1,073 | 0.672 | **0.836** | 883 | 927 | **1,154** | +30.7% |
| Spain | 709 | 882 | 0.553 | **0.688** | 759 | 763 | **949** | +25.0% |

**Break-even `ρ*F = anchor ÷ 365`, in hours of floor per day:**

| | Published (c69742) | **Recomputed** | Change |
|---|--:|--:|--:|
| US | 3.78 | **3.78** | 0 |
| Germany | 2.42 | **3.16** | +0.74 |
| Japan | 2.42 | **3.16** | +0.74 |
| Spain | 2.08 | **2.60** | +0.52 |

Worked: Germany, 1,072 ÷ 1,283 = 0.836; 0.836 × 1,380 = 1,153 h; 1,153 ÷ 365 = 3.16.

**Order of the three is kept** (US > Germany = Japan > Spain). **The gaps shrink.** Germany's break-even was 64% of the US figure (2.42 ÷ 3.78) and is now 84%. Spain's was 55% and is now 69%.

**Spread.** One sensitivity, by hand from `MIDDLE_FIFTH.md`: using the middle-fifth hours (Germany 1,048, US 1,104) the ratio is 0.949, anchor 1,310 h, break-even 3.59. So the German break-even runs 3.16 (ratio of averages) to 3.59 (ratio of middle fifths). Japan and Spain are not in the middle-fifth table. The US anchor itself has the unaudited upstream convention noted in `median-lifestyle/ANCHOR_UNDER_NO_DIVISION.md` §4.

### Outcomes against results

| # | Result |
|---|---|
| L1 | **Held.** Germany 1,153; Spain 949. |
| L2 | **Held.** 3.16 ≥ 3.0, and it moved 0.74 from the published value. |
| C1 | **Held.** Self-test: no `alloc` or `co-product` text in `q6_payers.py`, `track6_country_labour.py`, `track6_efficiency.py`. |
| C2 | **Held for Germany and Spain, failed for Japan.** 883 = 1,380 × 0.64 and 759 = 1,380 × 0.55. Japan's own old ratio is 0.672, which gives 927, not 883. The published Japanese figure was the German one reused. |
| C3 | **Held.** Germany +30.6%, Japan +30.7%, Spain +25.0%. |

**Together or separately.** Germany and Japan move together, and by the same arithmetic: their every-payer hours differ by 1 h. Spain moves separately and less, because its ratio rose from 0.553 to 0.688 and not to 0.836.

## 4. What this does not show

1. **It does not measure a peer anchor.** Every peer figure is the US anchor scaled by a Q6 hours ratio. The US anchor adds durables, imported labour and own-pollution (Tracks 2, 3, 4) that no peer run has. Foundations §5.5.3 already says "scaled from the Q6 ratios and not measured separately". No one has built Track 1–4 for Germany, Japan or Spain.
2. **Spain's figure is a floor.** `q6_payers.py` marks Spain "data gap": its shop work is missing from the data. The true Spanish anchor is higher than 949 by an unknown amount, so 2.60 is a lower bound on its break-even.
3. **The joint-production rule was checked by reading code, not by re-running a split.** EXIOBASE is a product-by-product table. Its own treatment of secondary products is somebody else's convention, as in `ANCHOR_UNDER_NO_DIVISION.md` §4. This run did not measure how far it can move a figure.
4. **The exploit sizes (650, 153, 29 h/yr) were not recomputed.** The request does not say how they were derived from the anchors, and no file I found reproduces them. If they are linear in the anchor they move by the same 25–31%. That is a guess, not a result.
5. **It does not say which ratio is right** for a "median adult" anchor. Average ratio and middle-fifth ratio differ by 0.11 for Germany. The US anchor used a 0.80 median-to-average factor in Track 1 (`TRACK1.md`), which the middle-fifth work puts at 0.86. Applying a median factor to the US and not the peers would mix bases.
6. **Direction of flattery.** The stale 883 and 759 sat 20–25% below the every-payer figures, so they made the efficient methods look cheaper than the measurement says. The recomputed values are higher, so that flattery is removed. It does not prove the new figures are free of it.

## 5. Command and seed

```
python -I 06-simulation/anchor-peers/anchor_peers.py --test
python -I 06-simulation/anchor-peers/anchor_peers.py
```

Deterministic. No seed. Reads `06-simulation/median-lifestyle/q6_payers_result.json` and `middle_fifth_result.json`. Takes about 1 second. Writes nothing. 9 self-tests, run on 2026-11-19, all pass.
