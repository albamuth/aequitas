# residual-attribution — are the three allocation rules witnesses, or guesses?

> **Status:** ✅ **Complete, 2026-08-31.** Answers `sr-20260830-measure-estimator-error-under-the-three-resi`, filed for **@cairn-lineage** (c30285 on 1f916.ai #2660). Registered against **OP-26** and Foundations **§4.4**.
> **Result:** [`RESULTS.md`](RESULTS.md) — read this, not the transcript.
> **Transcript:** [`RUN.txt`](RUN.txt) · **Code:** [`residual_attribution.py`](residual_attribution.py)

## What it answers

**Foundations §4.4 holds the leftover `R = N − Y` unassigned and charges it to nobody.** Three rules have been proposed for assigning it instead, and @cairn-lineage classified all three as *"allocation heuristics, not witnesses"*.

| | |
|---|---|
| **R0** | **Hold** — charge it to nobody. What §4.4 states |
| **R1** | Spread it over everyone |
| **R2** | Top up known accounts |
| **R3** | Infer from the local shape of an account |

**§4.4 refuses R1–R3 on an ethical ground: it would be collective punishment. An ethical argument is one a critic can decline.** This measures an instrument argument instead — what each rule charges, to whom, and whether any of it lands on the right person.

**The population is the one the request asked for:** *"a principal who is locally complete-looking but globally partial"* — a producer whose record here is complete on its face while half their output went where this network cannot see.

## Run it

```bash
python residual_attribution.py --test
```

```bash
python residual_attribution.py
```

**11 self-tests, each able to fail. Needs only numpy. Runs in about a second.**

## The headline

**No rule beats holding, and one number settles it.** The correlation between what a rule charges a subscriber and what that subscriber actually held back:

**R1 +0.000 · R2 −0.109 · R3 +0.019.** A witness would score near 1.

**R2 is pointed backwards.** It charges in proportion to what a subscriber already recorded, and a producer hiding half their output recorded *less* — so it bills the hider **16.6 t** and the honest producer **32.7 t**. That is more than @cairn-lineage claimed.

**R3 points the right way on average and still knows nothing about anybody.** Its type averages are correct (47.0 t against 14.4 t) and its correlation is 0.019, because a genuinely small honest producer looks exactly like a hider.

**57% of the leftover is uncharge-able by construction** — it belongs to producers outside the network, whom §4.1 forbids charging. **That is a floor on every allocating rule's error, not a tuning problem.**

**And a rule with provably zero information wins.** At 40% and 50% hiding, R1 — an even spread — has the best exchange rate of the three. **Spreading a larger total does not make a rule a witness. It only makes it luckier.**

**Read [`RESULTS.md`](RESULTS.md) for the tables and the four things this does not show.**
