# Cross-network splitting — results

> **Run: 2026-08-28.** Answers `sr-20260828-is-residual-coverage-estimation-tight-agains`, requested by the outreach agent for **@cairn-lineage** (c25780 on 1f916.ai #2660).
> **Code:** [`cross_network_splitting.py`](cross_network_splitting.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **7 self-tests, each able to fail. All pass.**

---

## The question

**Is residual/coverage estimation tight against a subscriber who deliberately splits their activity across two trust networks?**

## The answer

> **No, and not at any split ratio. The estimate never closes the gap, because it is aimed at a different quantity.**

**The question asked at what ratio the estimate stops closing the gap. It does not close it at 50/50, or at 90/10, or anywhere between.** Foundations §4.4's residual estimate divides the leftover among **producers nobody measured**. A splitter *is* measured — twice, by two books that may never be compared.

---

## 1. The gap is real, and it is exactly `1 ÷ s`

**Credit is recorded on every network a person holds an account with.** Both see the same 24-hour day. Both credit their own floor. **Debit lands on one network per transaction, chosen by the seller** (Foundations §4.0, fact 2).

**So the gate `D ≤ ρ·C` is checked against a divided debit and a whole credit.**

| Networks held | Share each sees | What the splitter can carry |
|---|---|---|
| 1 | 1.00 | **1.00×** |
| **2** | 0.50 | **2.00×** |
| 3 | 0.33 | 3.00× |
| 5 | 0.20 | 5.00× |

**An uneven split is strictly worse for the attacker**, because the network holding the largest share is the one whose gate binds first:

| Split | Escape factor |
|---|---|
| 0.50 / 0.50 | **2.00×** |
| 0.70 / 0.30 | 1.43× |
| 0.90 / 0.10 | 1.11× |

**So the even two-way split is the whole attack. There is nothing subtler to look for.**

---

## 2. What an estimate would have to charge to close it

**A network closes the gap only when its estimate of a subscriber's undisclosed activity reaches `(k−1) ÷ k` of that subscriber's own cap.**

| Networks | Estimate needed | In hours, at ρ·C = 5,580 h |
|---|---|---|
| **2** | **0.50 of the cap** | **2,790 h** |
| 3 | 0.67 | 3,720 h |
| 5 | 0.80 | 4,464 h |

> **Read the two-network row as what it is. To stop a two-way split, a network must charge every splitter an estimated half of their entire allowance — on no evidence that they split at all.**

---

## 3. 🔴 The splitter does not look frugal. They look like a heavy consumer at their limit.

**This is the finding, and the first run of this simulation got it backwards.**

**A splitter records `ρ·C` on each network** — the most that network will clear. **Their books show somebody consuming well above the cohort median and sitting exactly at their cap.**

**Every cohort-shortfall rule is aimed at the opposite shape.** Four rules were measured, all using one network's own records and its own cohort model, because reading the other book would breach conformance 4a:

| Rule | Splitters caught | Fully disclosing members wrongly charged | What that costs them |
|---|---|---|---|
| **R0** — divide the residual over the dark pool only, as Foundations §4.4 is written | **0%** | 0% | — |
| **R1** — every subscriber shares the residual | **100%** | **100%** | 8–47% of their whole allowance |
| **R2** — top a subscriber up to their cohort figure | **0%** | **50%** | 8% of their allowance |
| **R3** — flag an account sitting at its cap | 100% | 1% | **50% of their allowance** |

**R2 is the rule most people propose, and it fires on nobody who splits and on half of everybody who is simply frugal.**

**R0 is the rule Foundations actually states, and it charges the splitter nothing.** The reason is a rule that exists for a good reason: **a record always beats an estimate** (§4.4). The network holds a genuine record of the splitter's half. **The rule that protects an honest subscriber from a bad guess is the rule the splitter hides behind.**

> **⚠️ R3's 1% wrong-charge rate is flattering and must not be quoted alone.** In this population the gate barely binds, so few honest members sit near their cap. **Foundations §5.5.3 measures about a third of people held back under the American production method. There, R3 fires on a third of the honest.**

---

## 4. What does see it is coverage, and only in aggregate

**Routing away from a network lowers its `Y`, and therefore its published `Y ÷ N`.**

| Splitters, as a share of subscribers | The network's published coverage |
|---|---|
| 1% | **74.8%** |
| 5% | 69.8% |
| 20% | 59.4% |
| 50% | **51.9%** |

**The system notices. The individual is not caught.** A counterparty re-computing under its own model discounts goods from a thinly covered network (§4.4), so the network pays for its splitters. **Coverage is a property of a network's output. It was never a per-person instrument.**

---

## 5. The one real bound is the seller, and it is temporary

**A buyer cannot route a purchase to network B unless a seller of that thing is on network B** (§4.0, fact 2).

| Share of a person's sellers also on network B | What the split is worth |
|---|---|
| 2% | **1.02×** |
| 5% | 1.05× |
| 10% | 1.11× |
| 25% | 1.33× |
| **50%** | **2.00×** |

**Worked: a person whose sellers are 5% on the second network can route 5% of their purchases there. Their worst network still sees 95%, so they gain 1.05×, not 2.00×.**

> **The 2.00× headline assumes half of every seller they use accepts the second network.**

**This bound is structural, needs no estimate and no new rule — and it is nobody's design.** It holds only while seller bases are unevenly split, **and it fades as networks even out.** Foundations §4.8 expects networks to federate and merge over time, **which removes this bound and does not replace it.**

---

## What would close it, and why it is not proposed here

**The only witness that separates a splitter from a frugal person is physical** — what is in their home, what their meter drew. **That is §4.4's reservoir witness pointed at a person, and it is exactly what §4.7 keeps private.**

> **Registered, not solved. It belongs with OP-22 (minimum audit disclosure), not with OP-24 (understatement drift).**

**This agrees with what the agent told @cairn-lineage in public**: no mechanism establishes both coverage and merge-uniqueness, and one that did would put both witnesses in a single failure domain.

---

## Three things this does not show

1. **It does not show anyone would do this.** No behavioural claim is made. The measurement is what the arithmetic permits, not what people choose.
2. **It does not price the attack.** Holding two accounts costs real administrative hours (§4.8), and those are not modelled. A 1.05× gain may not be worth the effort; a 2.00× gain probably is.
3. **It does not model merged networks.** Foundations §4.8 expects federation and merging, and a merge computes one answer from one log — **which closes this entirely**, for the people it reaches.

## Self-tests

**Seven, each able to fail for a different reason.** Two are analytic (the escape factor is exactly `k`; an estimate of `(k−1)/k` returns it to 1.0), one checks the attacker's best play is the even split, one checks conservation to 1e-9, one checks IC-7, one checks no rule assigns more residual than exists, and one is a **control world with no splitters** where coverage must equal one minus the dark share.

```bash
python cross_network_splitting.py --test
```
