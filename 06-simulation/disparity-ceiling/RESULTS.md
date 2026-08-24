# Disparity ceiling — results

> **Read this instead of re-running.** From `python disparity_ceiling_sim.py --test` and `python rho_sweep.py --test`, last verified 2026-08-24.
> The argument in full: [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md) and [`RHO_SWEEP.md`](RHO_SWEEP.md). The arithmetic as data: [`../audits/audits_inert/bonus_sims.md`](../audits/audits_inert/bonus_sims.md).

---

## The headline

> **The ratio between the most anyone can sustainably consume and a bare-subsistence allowance is 24/F.** At a 10-hour self-care floor that is **2.40×**. Under money the same ratio runs to roughly **10⁶×** and compounds without limit.

*F* is the network's self-care floor in hours per day. The bound is a small number, and it does not move with the tolerance dial ρ or with the weighting model.

## The four claims and where they stand

| # | Claim | Verdict |
|---|---|---|
| 1 | The ceiling is `24/F` | **Closed-form.** Exact at every floor tested. |
| 2 | A clearing rate exists | **Simulated.** ρ\* ≈ **1.20**, resolved no finer than one grid step of 0.0176. |
| 3 | The ceiling is invariant to fraud | **Closed-form.** Holds at **40% fraud**, because a day still has 24 hours. |
| 4 | Front-loaded costs do not amortise | **Closed-form.** |

## The numbers

| Result | Value |
|---|---|
| Equal-age disparity at F = 10 h | **2.40×**, at every ρ from 1 to 3 |
| Disparity at 40% fraud | **still 2.40×** |
| A hoard-then-splurge attempt | attempted 14,400 h, **allowed 1,440 h** |
| A 20-year-old against a 60-year-old | **7.2× = 3 × 24/F** — time lived, not class |
| Clearing rate ρ\* | **1.20** |
| What the median person gets at ρ\* | **0.92×** of a full lifestyle |
| Share held below their wants | **35%** |
| Under efficient (non-US) production | median reaches **1.00×** |
| After a disaster | ρ\* tightens to **0.68**; growth loosens it |

**In every scenario the real-consumption disparity stays at or under 24/F = 2.4×.**

## The five conditions the result rests on

The ceiling is a **conditional** result. Condition 5 was added on 2026-08-22 and corrects an error in condition 4.

**Condition 4 used to claim that IC-7 already capped multi-network accrual. It does not.** IC-7 caps hours per account per network, and self-care credit has no physical anchor — proof of life needs no output. Condition 5 replaces that with **cross-network uniqueness attestation**, and the headline reads **24/F per network**.

> **The framing that survives.** Two networks counting the same person are counting the same thing. They cannot be compatible unless they arrive at the same ledger for that person, so a compatible pair produces **one** ledger seen from two places and the floor is credited **once**. An incompatible pair simply does not trade, and what remains is a coverage gap, not a breached bound.

## What would falsify this

- An equal-age pair whose sustained consumption ratio exceeds `24/F`.
- A fraud rate at which the ceiling moves. It should not, because fraud cannot lengthen a day.
- A pair of interoperating networks that credit the same person's floor twice and still trade.
- A clearing rate far from 1.20 under the same production intensity. The absolute level depends on the weighting model, so **only ratios and directions are claimed here**, never the absolute figure.

## Figures

| File | Shows |
|---|---|
| `ceiling_fig1_rho.png` | The ceiling holding flat as ρ moves |
| `ceiling_fig2_clearing.png` | The clearing behaviour |
| `ceiling_fig3_fraud.png` | The ceiling holding under fraud |
| `ceiling_fig4_frontloading.png` | Front-loaded costs not amortising |
| `rho_sweep_fig.png` | The ρ sweep against the median-lifestyle anchor |
