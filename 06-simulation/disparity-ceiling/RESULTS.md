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
| 3 | The ceiling is invariant to fraud | **Closed-form.** Holds at **40% fraud**, because a day still has 24 hours. **This is an insensitivity, not a coverage result** — see below. |
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

> ### Claim 3 is a bound, not a detector, and the two rows below are one property
>
> **`24/F` reads no accounts.** At `F` = 10 the answer is 2.40 whatever the population contains, so *"still 2.40× at 40% fraud"* means **the arithmetic never looked**, not that anything caught the fraud. **Insert a phantom account and the figure moves by 0.00 for the same reason.**
>
> | What the run shows | What it does not show |
> |---|---|
> | The bound is **robust**: no amount of faked hours produces an outlier beyond it | That the population was **witnessed**. A reproducible detector can still reproducibly certify only the world it was shown |
>
> **In plain words: report claim 3 as robustness for the bound and blindness for the detector, in the same sentence, or it reads as flattery.** The witness for coverage is a different instrument and it is physical — Foundations §4.4's outside total `N`.
>
> *(@cairn-lineage, c33046 on 2026-08-31, conceded at c33598. The general rule was already Foundations §4.4 — a check that compares a thing to itself can find a mistake, and cannot find a hole. What was new is that our own headline statistic is an instance of it.)*

## The four conditions the result rests on

**These are the four in Foundations §5.5.5. The full statement is in [`DISPARITY_CEILING.md`](DISPARITY_CEILING.md) §4.**

| # | The condition | What it does to the number |
|---|---|---|
| 1 | **The value of `F`** | The ceiling **is** `24/F`. A 2-hour floor states a **12×** ceiling. The result is only as tight as floors are generous |
| 2 | **Whether the network credits a child's learning time** | Credit it and **2.400×** is reachable. Credit none of it and the highest anyone reaches is **2.085×** |
| 3 | **No fraud manufactures hours** | IC-7 caps a day at 24 h, but collusive hand-offs could still inflate gross hours (**OP-1**). The bound assumes that channel is controlled |
| 4 | **It is a statement about one network's books** | **Nothing else.** There is no wider figure, and none is available |

**In plain words: the ceiling is a small number only because floors are generous, and it is a statement about one set of books rather than about the world.**

> ### ⛔ WITHDRAWN 2026-08-25 — the old condition 5
>
> <!-- struck-ok: this box exists to record the withdrawal, so it must quote the withdrawn wording -->
> **This section used to carry a fifth condition and a paragraph headed *"the framing that survives"*, both claiming that two networks *"cannot be compatible unless they arrive at the same ledger for that person."*** **That is struck, not narrowed.**
>
> **Foundations §4.2 says the opposite on purpose** — *comparison, never conversion*. One person, one Monday, 8 hours worked: Network A at a 4-hour floor records **12** credited hours and Network B at a 10-hour floor records **18**, **and both are correct**. Adding them would set an exchange rate between credit-standards, which A3 forbids.
>
> **Found from outside by @cairn-lineage and conceded on 2026-08-25.** Record: Objections §OA9, and `00-strategy/open-problems/OP-22_identity_not_disclosure_v0.2.md` — *"We did not narrow the clause. We removed it."*

## What would falsify this

- An equal-age pair whose sustained consumption ratio exceeds `24/F`, **inside one network's books**.
- A fraud rate at which the ceiling moves. It should not, because fraud cannot lengthen a day — **and a run confirming that tests the arithmetic, not the population**.
- A clearing rate far from 1.20 under the same production intensity. The absolute level depends on the weighting model, so **only ratios and directions are claimed here**, never the absolute figure.

**One old falsifier is withdrawn with condition 5:** *"a pair of interoperating networks that credit the same person's floor twice and still trade."* **Two networks crediting the same person differently is the intended behaviour**, not a breach, so nothing about it could falsify the bound.

## Figures

| File | Shows |
|---|---|
| `ceiling_fig1_rho.png` | The ceiling holding flat as ρ moves |
| `ceiling_fig2_clearing.png` | The clearing behaviour |
| `ceiling_fig3_fraud.png` | The ceiling holding under fraud |
| `ceiling_fig4_frontloading.png` | Front-loaded costs not amortising |
| `rho_sweep_fig.png` | The ρ sweep against the median-lifestyle anchor |
