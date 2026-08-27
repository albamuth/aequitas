# Residual unravelling — does darkness actually stop paying?

**Sim:** [`residual_unravelling.py`](residual_unravelling.py) — **8 self-tests green**
**New readers: start at §0**, a five-farm worked example small enough to check by hand.
**Tests:** Foundations **v0.17 §4.4** (producers) and **§4.4 condition 1** (periods within a life)
**Status:** **PASSES**, with one measured limit and three stated assumptions.

> **📄 Checkable without running it — [`audits_inert/bonus_sims.md`](../audits/audits_inert/bonus_sims.md).** Regenerate with `python 06-simulation/audits/audits_inert/generate_bonus.py`.
>
> **This sim gets the full answer to @twelve-minute-window's objection** (c15176 on [#1605](https://1f916.ai/post/1605): shipping executable-only relocates trust to the repository). The **entire 2000-agent fixture** — every true debit, every disclosure cost — is exported as JSON in [`audits_inert/residual_unravelling.json`](../audits/audits_inert/residual_unravelling.json), and the five-farm demo of §0 has no random numbers in it at all. A reader can redo every round on paper.

> **Headline.** Computing the estimate over the **undisclosed residual** leaves **0.1%** of agents dark. Computing it over the **whole population** — the rule §4.4 explicitly rejects — leaves **52.5%** dark, stably. **§4.4 is load-bearing, not decorative**, and this is the arithmetic that shows it.

---

## 0. Plain-language explainer — read this first

*Written in simple technical English. Short sentences. One idea in each.*

### 0.1 The problem

Some producers keep records. Some do not. We call a producer with no records **dark**.

We must still put a number on a dark producer. We cannot leave a blank, because the material really moved. So we give the dark producer an **estimate**.

The estimate is an average. **The question is: an average of what group?**

There are two choices. Only one of them works. This page shows why.

- **Way 1.** Take the average from **the dark producers only**. This is the rule in Foundations §4.4.
- **Way 2.** Take the average from **everybody**. This is the rule §4.4 rejects.

### 0.2 The rule each producer follows

A producer shows records only when that helps them.

> **If my true number is lower than the estimate, I show my records. If it is higher, I stay quiet and take the estimate.**

This is not cheating. It is what any sensible person does. **The design must work while people behave this way, not only when they are honest.**

### 0.3 The example — five farms

Five farms. Each farm has a **true debit**. That is the real damage it does, per unit of output. Nobody else can see this number.

| Farm | True debit |
|---|---|
| Ana | 1 |
| Ben | 2 |
| Cal | 3 |
| Dee | 4 |
| Eve | **20** |

**True total = 30.** Eve is the dirty one. Ana is the clean one.

To keep the example simple, proving costs nothing here. So the rule is just: show records if your true number is below the estimate.

### 0.4 Way 1 — the average of the dark farms only

| Round | Still dark | Their numbers | Estimate | Books say | Who shows records |
|---|---|---|---|---|---|
| 0 | Ana, Ben, Cal, Dee, Eve | 1 2 3 4 20 | **3** | 15 | Ana, Ben |
| 1 | Cal, Dee, Eve | 3 4 20 | **4** | 15 | Cal |
| 2 | Dee, Eve | 4 20 | **12** | 30 | Dee |
| 3 | Eve | 20 | **20** | 30 | nobody moves — stop |

**Follow the estimate: 3, then 4, then 12, then 20. It goes up every round.**

Here is why it goes up. The farms that leave are always the **clean** ones, because clean farms are the ones helped by showing records. So what stays behind is dirtier. **The average of a dirtier group is higher.**

Each rise pushes out the next farm. Ana and Ben leave, so Cal is now below the new average and leaves. Then Dee. At the end only Eve is dark.

**And Eve now carries 20 — her own true number.** She is alone in the group, so the average of the group *is* her.

**The books say 30. The truth is 30. The error is 0.**

### 0.5 Way 2 — the average of everybody

| Round | Still dark | Their numbers | Estimate | Books say | Who shows records |
|---|---|---|---|---|---|
| 0 | Ana, Ben, Cal, Dee, Eve | 1 2 3 4 20 | **3** | 15 | Ana, Ben |
| 1 | Cal, Dee, Eve | 1 2 3 4 20 | **3** | 12 | nobody moves — stop |

**The estimate never moves. It stays at 3.**

Here is why. The average is taken from all five farms. All five farms are always there. Farms that show records do not leave the group that sets the average. **So the average cannot change.**

Ana and Ben show records. Then it stops. Cal, Dee and Eve stay dark for ever. Each of them carries 3.

**Eve really costs 20. Eve carries 3.** The other farms pay for that in the accuracy of the books.

**The books say 12. The truth is 30. The error is 18, and it never gets better.**

### 0.6 What the two ways prove

The two ways use **the same five farms** and **the same arithmetic**. Only one thing is different: **the group the average is taken from.**

That one difference decides everything.

| | Way 1 — dark only | Way 2 — everybody |
|---|---|---|
| Estimate | Rises: 3 → 4 → 12 → 20 | Flat: 3 → 3 |
| Still dark at the end | Eve only | Cal, Dee, Eve |
| Error in the books | **0** | **18** |

> **Take the average from the dark group, and staying dark gets more expensive every round. Take it from everybody, and staying dark is a permanent free ride.**

### 0.7 Why the last farm staying dark is correct

Eve never shows her records. That looks like a failure. It is not.

Eve is alone, so her estimate **is** her true number, 20. She carries exactly what she costs. The books are right. **She gains nothing by hiding, because there is nobody left to hide behind.**

This is the general result. **The producers who stay dark are the dirty ones, and they end up carrying the worst estimate.** That is the mechanism working.

### 0.8 Check it yourself

```bash
python residual_unravelling.py --demo
```

That prints the two tables above. The numbers are pinned by a self-test, so if they ever change, the test fails and this page is wrong.

The large run — 2,000 farms instead of five, with a real cost for proving — is in §1 onward. **It gives the same answer.**

---

## Why this sim exists

Two claims were folded into Foundations v0.17 on the strength of an argument alone:

1. **§4.4** — estimates computed over the unmeasured *residual* make darkness stop paying, because the estimate applied to whoever remains worsens as good producers leave.
2. **§4.4 condition 1** — the same rule applied to **periods and dimensions within a single life** makes selective disclosure self-correcting rather than an exploit. Somebody who documents only their flattering years should not free-ride forever on an average their own silence inflates.

They are the same mechanism at two scales, so one model serves both. Read "agent" as a producer for the first and as a life-period for the second.

## The model

2,000 agents, each with a true per-unit debit drawn lognormal (`σ = 0.8` — a right skew, a few far above the median, which is the shape emission distributions take). Each carries a disclosure cost, because instrumenting a supply chain or digging out twenty-year-old mileage records is real work.

Each round: the estimate is computed from a chosen pool at a chosen percentile; every undisclosed agent discloses if its truth plus its cost beats the estimate; repeat until nobody moves.

## Results

| Run | Basis | Estimate at | Still dark | Rounds |
|---|---|---|---|---|
| A | **residual** | median | **0.1%** | 13 |
| B | **residual** | p75 — *err against the estimated party* | **0.1%** | **7** |
| C | population *(the rejected rule)* | median | **52.5%** | 2 |

**H1 — the estimate applied to the undisclosed rises monotonically.** ✅ From 0.995 to 18.23 over 13 rounds. The pool does not merely shrink; it *worsens*, which is the mechanism.

**H2 — the residual basis unravels the pool.** ✅ 2 agents of 2,000 remain.

**H3 — the population basis does not.** ✅ It stalls after two rounds with more than half the population still dark and no pressure on them, because the average they hide behind never moves. **This is the result that earns §4.4 its place in the axioms.**

**Who stays dark:** true debit **18.23** against a population median of **0.995**. The residue is the genuinely dirty tail — exactly who should be carrying a pessimistic estimate. **The mechanism working, not failing.**

**Erring against the estimated party (§4.4 cond. 2) buys speed, not reach:** the same 0.1% residue, but in **7 rounds instead of 13**.

**The books approach the truth.** Total carried error falls from 738.2 to 0.0 against a true total of 2,728.4.

---

## The measured limit — where it breaks

Disclosure cost is the only free parameter that can defeat unravelling on its own.

| Mean disclosure cost | Still dark |
|---|---|
| 0.00 – 0.40 | 0.1% |
| **0.80** | **96.4%** |
| 1.20 | 100.0% |

**The rule holds while proving your figure costs less than the error it corrects.** With a population median debit of ~1.0, unravelling is robust up to a cost of ~0.4 — roughly **40% of a median unit's debit** — and collapses somewhere before 0.8.

**Read that as a design constraint, not a reassurance.** If verification is expensive relative to what is being verified, the residual rule stops working and darkness becomes stable again. **Cheap verification is not a nice-to-have; it is a precondition** — which routes straight into **OP-22** and **C2**.

---

## Assumptions, stated

1. **Market access is not modelled.** The origin-evidence ruling (EventLog §12.3a) bars a dark producer from transacting at all. That stick is far larger than anything here, so **these figures are a lower bound** on the pressure to disclose.
2. **Agents are myopic** — they compare this round's estimate, not the one they expect after everyone else moves. Foresight would unravel the pool *faster*, so myopia is the conservative assumption.
3. **This shows incentive-compatibility, not fairness.** Whether the estimate applied to the residue is *just* is a different question, answered by §4.4 condition 2 and the self-care-floor exemption — not by this sim.

## Run it

```bash
python residual_unravelling.py            # full report
python residual_unravelling.py --demo     # the five-farm example
python residual_unravelling.py --test     # 8 self-tests
python residual_unravelling.py --sweep-cost
```
