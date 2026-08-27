# Residual unravelling — results

> **Read this instead of re-running.** From `python residual_unravelling.py --test`, last verified 2026-08-24.
> The argument in full: [`UNRAVELLING.md`](UNRAVELLING.md). The whole fixture as data: [`../audits/audits_inert/residual_unravelling.json`](../audits/audits_inert/residual_unravelling.json).

---

## The headline

> **Computing the estimate over the undisclosed residual leaves 0.1% of agents dark. Computing it over the whole population — the rule Foundations §4.4 explicitly rejects — leaves 52.5% dark, stably.**

**§4.4 is load-bearing, not decorative,** and that pair of numbers is the whole demonstration.

## The mechanism, in numbers

| What | Value |
|---|---|
| Estimate applied to the undisclosed, first round | **0.995** |
| Estimate applied to the undisclosed, last round | **18.23** |
| True median debit of who stays dark | **18.23** |
| Population median | **0.995** |
| Books' error over the run | **738.2 → 0.0** (true total 2,728.4) |

**The pool does not merely shrink — it worsens.** That is the mechanism, not a side effect. As anyone whose true cost is below the estimate discloses and leaves, the average of who remains rises, so the estimate rises, so the next tier finds disclosure worth it.

**Who stays dark is the dirty tail.** Their true debit is 18.23 against a population median of 0.995. That is exactly who should carry a pessimistic estimate. **Working, not failing.**

## The five-farm example, checkable on paper

No random numbers. Residual basis: estimate goes **3 → 4 → 12 → 20**, final error **0**. Population basis: estimate stays **flat at 3**, final error **18**.

## Erring against the estimated party buys speed, not reach

Foundations §4.4 condition 2 says estimates should err against the estimated party. Turning that on gives the **same residue in 7 rounds instead of 13**. It is a speed dial, not a reach dial.

## ⚠️ The measured limit — a design constraint, not a reassurance

**Disclosure cost is the one parameter that defeats unravelling on its own.**

| Verification cost, as a share of a median unit's debit | Outcome |
|---|---|
| up to ≈ **0.4** | robust; the pool unravels |
| **0.8** | **collapses to 96.4% dark** |

> **If verification costs more than the error it corrects, darkness becomes stable again.** Cheap verification is a **precondition** for the coverage argument, not a nicety. This routes straight into OP-22 (minimum audit disclosure) and the trust-network work.

## Three stated assumptions

1. **Market access is not modelled.** The real penalty for staying dark — you cannot transact at all — is far larger than what is modelled here, so these figures are a **lower bound** on the pull to disclose.
2. **Agents are myopic.** They compare this round's estimate against their own cost. Foresight would unravel the pool *faster*.
3. **This shows incentive-compatibility, not fairness.** It says darkness stops paying. It does not say the estimates are just.

## What would falsify this

- A cost distribution where the residual-basis estimate does *not* rise monotonically.
- A population where the population-basis control does as well as the residual basis. That would make §4.4 optional.
- A verification cost below 0.4 at which the pool still stabilises.

## Figures

None. This project produces text and JSON.
