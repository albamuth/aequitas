# Declared before the full run (written 2026-10-17, after the self-tests passed, before `python labelling_game.py` ran)

Headline cell: N=20, d=0.15, m=0.4, q=0.3, q/q'=6, g=0.2, attack cost alpha=0.05 (a = alpha*g/N), no collusion.

| # | Kind | Statement | Fails if |
|---|---|---|---|
| D1 | **Level** | The d at which a lone deviant stops gaining on an all-labelling population ("stay" threshold) is within a factor of 2 of the brief's prior q*g*m = 0.024, so in [0.012, 0.048] | it lies outside that band |
| D2 | **Level** | The transfer-conserving worked example (brief's 2-producer case) leaves labelling ahead by 1.0 to 2.0 points, not the 4.3 the brief's loss-only arithmetic gives | gap outside 1.0-2.0 points |
| D3 | Change | Labelling is **not** a free win: in the headline cell a lone labeller does worse than the unlabelled residents (Delta(1) < 0), because every rival can aim at the one target | Delta(1) >= 0 |
| D4 | Change | The "stay" threshold falls as q/q' falls toward 1 but the lone-labeller ("invade") threshold stays far above it: the two thresholds differ by more than 3x at q/q'=6 | ratio of thresholds <= 3 |
| D5 | Refutation test | Over the brief's suggested ranges, among cells where an attack on a labeller is worth launching, the start-at-p=0.5 dynamics end below p=0.5 in **more than half** of cells | fraction <= 0.5 (then the brief's refutation threshold is not crossed) |
| D6 | Change | Collusion among rivals (c = 0.5) lowers both thresholds | either threshold does not fall |

Prediction behind D3/D4: bistability. Once everyone labels, labelling holds; from p=0 it cannot start.
