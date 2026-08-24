# Pledge reserve — results

> **Read this instead of re-running.** From `python pledge_reserve.py --test`, last verified 2026-08-24.
> The argument in full: [`PLEDGE_RESERVE.md`](PLEDGE_RESERVE.md).

---

## The headline

> **The hazardous job clears at a reserve coverage of c\* = 0.83** — that is, once the contingent reserve pre-funds about **83%** of the expected future cost the work is likely to cause. Below that, supply is short. Above it, the job staffs.

Supply rises steadily with coverage, so there is a single crossing point rather than a cliff.

## The three findings

| Finding | Number |
|---|---|
| **Clearing.** Supply is monotone in coverage; the demand-gated bond clears | at **c\* = 0.83** |
| **G1 keeps people careful.** A full shield against a buffer | shield (a = 0.00): harm **500**; buffer (a = 0.50): harm **250** |
| **G2 is where the integrity sits.** Fraud alone does not break it; a weak causal trace does | padded claims: uncovered **0%**; weak trace: uncovered **20%** |

**Read finding 3 carefully.** Padded claims drain the reserve but do not leave anyone uncovered, because the reserve is sized against the expected tail. **A weak causal trace does** — 20% of task-caused harm ends up uncovered. So the mechanism's integrity rests on G2, the physical-trace test, not on catching fraudsters.

**And finding 2 is the reason G1 is not optional.** Halving the shield halves the harm. A reserve that fully insulated the doer would double the damage done, which is the ordinary moral-hazard result arriving in a system that has no insurer in it.

## What would falsify this

- Supply that does not rise with coverage — that would mean the reserve is not the thing motivating anyone.
- A fraud rate at which coverage collapses. It does not in this model, which is worth suspicion: the model treats fraud as padding rather than as invention of a whole claim.
- Any setting where a full shield produces *less* harm than a buffer. That would overturn G1.

## The unresolved piece

**The causation claim.** Whether *this* task caused *that* harm is modelled here as a dial (trace strength) rather than answered. There is no analogue elsewhere in Aequitas to borrow from, and Foundations §5.3d routes it to ordinary recourse. **This sim shows the mechanism is sensitive to it, which is the useful part.**

## Figures

| File | Shows |
|---|---|
| `pr_fig1_clearing.png` | Supply against reserve coverage; the clearing point |
| `pr_fig2_care.png` | Care taken under a shield against under a buffer |
