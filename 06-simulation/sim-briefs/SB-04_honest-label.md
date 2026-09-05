# SB-04 — Does labelling a figure "metered" or "modelled" pay, or does it just hand rivals a target?

> **Request:** `sr-20260904-does-a-producer-who-labels-each-published-fi` · filed 2026-09-04, asked by **@coywolf** at c39152. We said in public at c40715 that we do not have the number.
> **Status:** open. **Nobody has run this.**
> **This brief is not really about Aequitas.** It is about **any producer publishing a modelled figure anywhere** — a carbon number, a nutrition panel, a supply-chain claim. **You do not need our theory to run it.**

---

## 1. The question

> **A producer publishes a cost figure and may attach a label saying which parts are *metered* and which are *modelled*. Does labelling out-compete not labelling — or does the honest label only tell a rival exactly where to attack? Sweep the share of labelling producers and report whether labelling is stable.**

## 2. What depends on it

**Foundations §4.4** requires a derived figure to carry one of three labels — **`floor`**, **`ceiling`**, or **`not identified`** — and makes `not identified` the default. **§3.3a requirement 2** requires every cost constant to be published **with its method, its version, and its uncertainty interval.**

> **Both rules assume disclosure is survivable. Neither has been tested against a rival who reads the disclosure.**

**And §3.3a already names the shape of the problem.** Correcting an *understated* figure benefits everyone and is funded by nobody, so the pressure runs one way. **This brief asks the mirror question: does honest labelling get punished?**

**If labelling is unstable, §4.4's label rule is a rule that honest producers will drop**, and the register's OP-24 gets worse rather than better.

## 3. Terms

| Symbol | What it means |
|---|---|
| **`p`** | The share of producers who label. Swept from 0 to 1 |
| **`d`** | The **discount** a counterparty applies to an unlabelled figure, because it cannot tell metered from modelled. A fraction, 0 to 1 |
| **`a`** | The **attack cost**: what a rival spends to challenge a specific modelled component |
| **`g`** | The **attack gain**: what a successful challenge is worth to the rival — the share of trade it moves |
| **`m`** | The share of a producer's figure that is **modelled** rather than metered. This is what the label exposes |
| **A producer's payoff** | Trade won, minus discount suffered, minus attack losses |

**A note on `d`.** Foundations §4.2 already says a counterparty **discounts what it cannot check**, and §4.7 says a network choosing heavy opacity finds its members' claims trade at a discount. **`d` is that mechanism, given a number.**

## 4. The model

**One good, `N` producers, one round repeated. Each producer chooses `label` or `no label`.**

**Step 1 — what a counterparty pays.** An unlabelled figure is discounted:

> **effective figure = published figure × (1 + `d`)** if unlabelled, and **× 1** if labelled.

**A higher effective figure is worse for the producer** — the good reads dearer, so it wins less trade.

**Step 2 — what a rival can attack.** A labelled producer has exposed which share `m` of their figure is modelled. **A rival may spend `a` to challenge it.** With probability `q` the challenge succeeds and moves `g` of that producer's trade to the rival.

> **An unlabelled producer cannot be attacked this precisely, because the rival does not know where to aim.** Model this as a lower success probability, `q' < q`, at the same cost `a`.

**Step 3 — trade share.** Producers split demand in inverse proportion to their effective figures. **Run to a fixed point in `p`.**

### A worked example, with the numbers

**Two producers, identical physical process, published figure 10.0 h/kg. `m` = 0.4, `d` = 0.15.**

| | Labelled | Unlabelled |
|---|--:|--:|
| Published figure | 10.0 | 10.0 |
| Effective figure after discount | **10.0** | 10.0 × 1.15 = **11.5** |
| Trade share, inverse to effective figure | 11.5 ÷ 21.5 = **53.5%** | 10.0 ÷ 21.5 = **46.5%** |

**So on the discount alone, labelling wins by 7 percentage points.**

**Now add the attack.** Say a rival's challenge succeeds with `q` = 0.3 against a label and `q'` = 0.05 without one, moving `g` = 20% of trade.

| | Labelled | Unlabelled |
|---|--:|--:|
| Expected trade lost to attack | 0.3 × 0.20 × 53.5% = **3.2 pts** | 0.05 × 0.20 × 46.5% = **0.5 pts** |
| **Net share** | **50.3%** | **46.0%** |

**In plain words: at these numbers labelling still wins, but the attack has eaten nearly half the advantage.** The question this brief asks is **where the crossover is** — the combination of `d`, `q`, `q'` and `g` at which labelling stops paying.

## 5. Inputs

**No real data required.** State: `N`, the sweep ranges for `p`, `d`, `m`, `q`, `q'`, `g`, `a`, the number of rounds, and your seed.

**Suggested ranges, not binding:** `d` ∈ [0, 0.5] · `m` ∈ [0.1, 0.9] · `q` ∈ [0.05, 0.6] · `q'` = `q`/6 · `g` ∈ [0.05, 0.4].

## 6. What an answer looks like

| `d` | `q` | `q'` | `g` | Stable `p` | Is labelling stable? |
|--:|--:|--:|--:|--:|---|
| 0.15 | 0.30 | 0.05 | 0.20 | *(yours)* | yes / no / mixed |

**Plus the crossover surface: the value of `d` at which labelling stops paying, as a function of `q ÷ q'`.**

## 7. Declared in advance

| | |
|---|---|
| **Our prior** | **Labelling is stable when `d` exceeds roughly `q · g · m`** — the discount has to be worth more than the exposure it removes. We expect a crossover to exist and to sit at a **plausible** `d`, meaning **the label rule is not free** |
| **Refutation threshold** | **If labelling is unstable across most of the plausible parameter range — say `p` collapses toward 0 in more than half the swept cells — then §4.4's label rule cannot be relied on to be followed**, and §3.3a's requirement 2 has the same problem |
| **What we do if it is crossed** | **§4.4 gains a note saying the label rule is not self-enforcing**, naming what a network would have to do to make it so. **It would also strengthen OP-24 rather than relieve it** — a conclusion against us, since §3.3a currently treats the audit of *extent* as being in better shape than the audit of *weight* |

**A result that says "labelling always wins" should be distrusted, including by us.** It is the flattering answer, and this project has published four figures that were wrong in the flattering direction.

## 8. Self-tests, each able to fail

1. **At `d` = 0, labelling can only lose.** There is no discount to escape and the label only exposes. **If the model shows labelling winning at `d` = 0, it is wrong.**
2. **At `q` = `q'`, the attack does not discriminate**, so labelling wins whenever `d` > 0.
3. **At `m` = 0 — everything metered — the label exposes nothing** and labelling wins whenever `d` > 0.
4. **Trade shares sum to 1 in every round.**
5. **Two identical producers with identical choices split trade equally.** If not, the tie-break is doing something.

## 9. Out of scope

- **Whether the underlying figures are honest.** This brief is about the *label*, not the number under it. Understatement is **OP-24**.
- **Aequitas's own accounting rules.** The model needs a published figure, a counterparty who discounts, and a rival. **It does not need our ledger.**
- **Reputation over many rounds.** A single-good repeated game is enough for a first answer. **Multi-good reputation is a better study and a different brief.**

## 10. Known ways to get this wrong

- **Making the attack free.** If `a` = 0 every rival attacks every label always, and the result is an artefact of that.
- **Letting the discount apply to the true figure rather than the published one.** The counterparty cannot see the true figure. **That is the whole reason `d` exists.**
- **Assuming the rival is a rival.** §3.3a found that rivals' interests are often **aligned** on a shared constant. **A variant where rivals collude to attack nobody is worth running and is not in our prior.**
