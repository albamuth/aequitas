# Lost crop at the German method

Request `sr-20261111-lost-crop-at-the-german-method-same-populati`. Run 2026-11-15.
Code: `german_lost_crop.py` (7 self-tests), `fruitveg_share.py` (1 self-test on the data). Raw output: `RESULTS_RAW.txt`. Declared outcomes: `DECLARED.md`.

## 1. The question

> Lost crop at the German method. Same population, gate and settings as german-prime-sweep/german_prime_sweep.py. One food line (fruit and vegetables, as the essentials basket defines food eaten at home) loses 50% of its output, everything else at baseline (capacity 101.7% of wants). Report: the clearing rho of the whole economy, or 'none below 4.0'; the shortfall in that line in units and as a share of the line's demand; the share of people who get less than their want of that line if it is shared pro rata, and if it goes to the smallest wants first. Declare before running: no clearing rho exists below 4.0, because the lost line is a small share of total output; the shortage is a distribution question (Foundations 3.4a, 4.6), and lowering rho would cut every person's non-essentials to ration one line.

## 2. Declared before running (full text in `DECLARED.md`)

| # | Statement | Kind | Result |
|---|---|---|---|
| 1 | Line shortfall = 49.15% of the line's demand | Level (arithmetic of the input) | Held. A check on the code, not a finding |
| 2 | g, the line's share of one lifestyle unit, is 0.5% to 2.5% | Level, measured | **Held**: 1.160% (16.2 h of 1,398 h) |
| 3 | No clearing rho below 4.0 at every F, both E, every age seed; holds while g < g* (expected g* about 3.3%) | Level | **Held**: g = 1.16%, g* = 3.34% (F = 10, 14) and 3.36% (F = 2) |
| 4 | Essentials first: the line is admitted in full at rho = 0 | Level | **Held** |
| 5 | Pro rata: 100% of people get less than their want | Level (arithmetic of "pro rata") | Held. Could not fail |
| 6 | Smallest first: 25% to 40% of people get less | Level | **Held**: 31.7% |
| 7 | Gating the line (E = 0) cuts at least 10x more units elsewhere than the line's own shortfall | Ratio | **Held**: 60.5x |
| 8 | The request's claim holds | Verdict | **Held, on the declared line and the declared model** |

**Honest note on timing.** `fruitveg_share.py` was started in the background before `DECLARED.md` was written. It had finished, but I had not read its output when I wrote the declarations. Outcome 2 was a prediction from US food-at-home hours (131 h), not from the result.

## 3. The numbers

**The line.** Fresh fruit and vegetables is EXIOBASE 3 (2022) product 4, "Vegetables, fruit, nuts", bought by US households. Hours behind it: **16.2 h/yr** (12.4% of the 131.0 h of food eaten at home, 1.160% of all 1,398 h of US consumption). Same method and data as `essentials-basket`, which the script reproduces to within 1 h before it writes anything. Processed fruit and vegetables sit inside "Food products nec" and are not in the line.

**Unit.** One median German lifestyle-year = 1,380 × 0.836 = **1,153.7 debit-h/yr**. The line's share g is the same at the German method, because the German ratio scales every line alike.

**Line shortfall and sharing** (F = 10; population seeds 7 to 11; the spread is across those seeds):

| | Value |
|---|---|
| Total wants W | 221,563 units |
| Line demand, g × W | **2,570.6 units** (= 2.97 million debit-h/yr) |
| Line supply, 0.5 × 1.017 × demand | 1,307.1 units |
| **Shortfall** | **1,263.4 units = 49.15% of the line's demand** (= 1.46 million debit-h/yr) |
| Median person's line want | 13.4 debit-h/yr; the median person is short 6.6 h/yr under pro rata |
| **Pro rata: share who get less than their want** | **100.00%** (200,000 of 200,000; each gets 50.85% of their want) |
| **Smallest wants first: share who get less** | **31.74%** (63,493 of 200,000); min 31.70%, max 31.77% across 5 seeds |
| Smallest first: share who get nothing | 31.74% (the one marginal person who gets part is under 0.001%) |

F = 2: 31.02% (30.99 to 31.05). F = 14: 31.81% (31.77 to 31.83).

**Whole-economy clearing rho** (capacity = 1.017 × W × (1 − 0.5 g) = **1.0111 × W**, which is 224,112 units against 221,652 wanted at F = 10):

| F | E = 437.2 h | E = 462.3 h | Admitted units at rho 4.0, as a share of wants | g* |
|---|---|---|---|---|
| 2 | **none below 4.0** | **none below 4.0** | 0.9999 | 3.356% |
| 10 | **none below 4.0** | **none below 4.0** | 1.0000 | 3.343% |
| 14 | **none below 4.0** | **none below 4.0** | 1.0000 | 3.343% |

Each cell is 3 age seeds (11, 12, 13), and all 3 returned "none" in every row. g* is the line share above which aggregate capacity drops below what the gate admits at rho 4.0.

**Where the verdict flips** (F = 10, E = 437.2; units are lifestyle units; 3 age seeds):

| g | Capacity / wants | Clearing rho |
|---|---|---|
| 0.5% | 1.0145 | none below 4.0 |
| **1.16% (measured)** | **1.0111** | **none below 4.0** |
| 3.3% | 1.0002 | none below 4.0 |
| 3.4% | 0.9997 | 0.888 |
| 6% | 0.9865 | 0.498 |
| 10% | 0.9661 | 0.404 |
| 20% | 0.9153 | 0.309 |

The whole food-at-home line is 9.4% of consumption (131.0 of 1,398 h), so **losing half of all food eaten at home** would have a clearing rho of about 0.40 to 0.42. The claim "no rho below 4.0" depends on the lost line being under 3.3% of one lifestyle unit. It is not a statement about food in general.

**Can any rho move the line?** (F = 10, age seed 11; line admitted ÷ line demand at rho = 0, 0.3, 1.2, 4.0)

| Convention | E = 437.2 | Line-clearing rho | What it means |
|---|---|---|---|
| **A. Essentials first** (food inside E, charged first, ungated; Foundations 5.5.4) | 1.000, 1.000, 1.000, 1.000 | **none**: the ungated part alone (100%) exceeds the line's supply (50.85%) | **No rho touches the line.** The shortfall is the same at every rho |
| B. Proportional inside E (line admitted at the person's overall fraction f) | 0.480, 0.869, 1.000, 1.000 | 0.114 (E = 462.3: 0.086) | Under this convention a very low rho would ration the line |
| C. Gated, E = 0 (the line is ordinary discretionary goods; **contradicts 5.5.4**) | 0.000, 0.827, 1.000, 1.000 | 0.192 | Priced only to test the request's last clause |

**What lowering rho would cost, under C** (rho = 0.192): the whole economy admits 145,235 of 221,652 units. **76,417 units are cut in all lines to ration a line short by 1,263.9 units: 60.5 times the shortfall.** 32.14% of people are admitted nothing above services. Under A that cost is not paid, because rho cannot reach the line. Under B at rho 0.114 the cut is not computed here.

## 4. What this does not show

1. **It does not show food is really fixed in E.** Convention A puts the line inside the essentials rule, which is what Foundations 5.5.4 and the basket say. If a network drew E narrower than food, the line would be gated and Convention C applies. The two give opposite answers to "can rho ration it" (never, against 0.192). The run does not say which a network would choose.
2. **Wants for the line are assumed proportional to each person's overall want** (w_i × g). Nothing in the data says a person who wants twice the lifestyle wants twice the fruit. The 31.7% (smallest first) depends on that: it is the share of people holding the smallest 50.85% of total want under the model's lognormal wants (sigma 0.45). A flatter want distribution for fruit would raise it. Not run.
3. **The aggregate adds units across lines.** "Capacity = 1.0111 × wants" counts a surplus of televisions as able to offset missing pears. Physically it cannot: other lines' 1.7% surplus cannot be turned into fruit. The aggregate result ("none below 4.0") is the request's own definition and says only that the gate has nothing to ration overall. It says nothing about the 49.15% hole in the one line, which stays whatever rho is.
4. **The line is only fresh produce.** Processed fruit and vegetables cannot be separated in EXIOBASE. g = 1.16% understates "fruit and vegetables" as a shopper means it. Section 3 sweeps g, and the verdict holds up to 3.3%, about three times the measured value.
5. **The 50% loss is taken from the line's baseline capacity of 101.7%, not from a 100% harvest.** That gives a supply of 50.85% of demand. A loss of 50% of what was actually harvested at 101.7% is the same. A loss of 50% of what people wanted would be 51.7% supply. The 1.7% slack is the input.
6. **No substitution.** People are not allowed to eat other foods (E, still unspent, buys other food lines) in place of the lost fruit. Other food lines have 1.7% spare at most, so substitution would barely help, but it was not run.
7. **One year, ages from the sweep, joiners with rebuilt pasts.** Year 2 and any effect on what next year's crop is were not simulated. The population is the US-calibrated one with German scaling, as in the neighbour run.
8. **US hours for the line, German scaling.** The 0.836 ratio is applied to every line alike. A German-measured fruit and vegetable share was not computed. Foundations 3.5 says the peer ratios were not measured separately.
9. **The pro rata share (100%) is arithmetic, not a finding.** Any partial supply shared evenly leaves everyone short.

## 5. Command and seed

```
python 06-simulation/german-lost-crop/fruitveg_share.py          # ~3 min, reads data/exiobase in place
python 06-simulation/german-lost-crop/german_lost_crop.py --test  # 7 self-tests
python 06-simulation/german-lost-crop/german_lost_crop.py         # full run, about 3 min
```

Population seed 7 (N 200,000, sigma 0.45) for sections B, C, D; population seeds 7 to 11 for the sharing figures; age seeds 11, 12, 13 (B and D use 11 to 13; C uses 11). Output saved in `RESULTS_RAW.txt`.
