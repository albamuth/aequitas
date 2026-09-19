# Pledge Inflation — Does Granting Debit-Room Create Claims Without Goods?

**Version:** 0.1
**Type:** technical problem — original analysis, internal to this project
**Author(s):** this project. The monetary comparison draws on Keynes, Graeber and the local-currency record already archived here.
**Published:** not published. First written 2026-09-18.
**Retrieved:** n/a — original work
**URL:** n/a
**Local copy:** n/a
**Related:** [`Keynes_general-theory.md`](Keynes_general-theory.md) · [`Graeber_debt.md`](Graeber_debt.md) · [`History_local-currency-experiments.md`](History_local-currency-experiments.md) · [`Warren_cost-the-limit-of-price.md`](Warren_cost-the-limit-of-price.md)

> **⚠️ STATUS — proposed, not folded.** The mechanism analysed here is the person-pledge ruling of 2026-09-18, written up in [`00-strategy/papers/Pledges.md`](../00-strategy/papers/Pledges.md). **The core documents do not yet carry it.** Foundations is to carry a few sentences and point here.

---

## Why this matters to Aequitas

**A pledge grants permanent debit-room to somebody else.** Room is permission to consume. **Nothing physical is created when a pledge is made**, so a reader is right to ask whether the system manufactures claims on goods that do not exist.

**The short answer is that it does, by a bounded factor, and that the usual consequence cannot follow.** The rest of this note is why.

---

## 1. The size of it

**Terms.** `C` is a person's credit, in hours. `P` is the committed room granted to them by other people's pledges. **ρ** ("rho") is the network's debit tolerance. **The gate is `D ≤ ρ·(C + P)`.**

**A pledge budget equals the credit a person earned in their life, and pledges are backed one hour for one hour.** That is conformance row 9 and IC-8. So across a whole network:

> **`P_total ≤ C_total`**

**Therefore total room is at most `ρ·(C_total + C_total)`, which is `2·ρ·C_total`.**

> **The pledge system at full use doubles a network's gate. The factor is exactly 2 and does not depend on ρ.**

It is 2 at ρ = 0.9 and 2 at ρ = 3.7. **A network cannot reduce it by choosing a different tolerance**, because ρ multiplies both halves.

### Worked, at one setting

**`F` = 10 h/day, ρ = 1.2, one million subscribers averaging 40 years of life at the floor.**

| | Hours |
|---|--:|
| `C_total`, 10⁶ × 40 × 3,650 | 1.46 × 10¹¹ |
| `P_total`, at the one-for-one ceiling | 1.46 × 10¹¹ |
| Room with no pledging at all, `ρ·C_total` | 1.75 × 10¹¹ |
| **Room with pledging at the ceiling, `2·ρ·C_total`** | **3.50 × 10¹¹** |

**Nothing physical changed between the last two rows.**

---

## 2. Why the monetary consequence cannot follow

**Monetary inflation needs three parts. Two are present here and the third is absent.**

| The part | Present in Aequitas? |
|---|---|
| More claims | **Yes.** Room doubles |
| The same goods | **Yes.** A pledge creates nothing physical |
| **A seller who raises the number** | **No** |

**The third part is the mechanism, and A5 (cost, not price) removes it.** A thing's figure is what it consumed. **You cannot mark up a measurement.** If a shop asks more than a thing cost, the number is wrong and the books show it. **So there is no price for surplus room to bid on**, and the feedback loop that turns extra claims into a rising index has no part to attach to.

**This is the same structural argument that closes five other doors at once** — lending at interest, rent, cornering, speculation and debasement — and it is the same one §5.6 uses to explain why the local-currency graveyard does not reach this system. **Non-fungibility and cost-equals-price are doing the work, not any anti-inflation rule.**

### What happens instead

**The gate stops binding.** `Aequitas_Foundations.md` §5.5.3 already describes the state in other words: *"`D ≤ ρ·C` still holds, but it is not the thing deciding who gets what."*

> **Rationing moves from the ledger to the point of distribution — a queue, a lottery, or pledge-priority.**

**That is a change of rationing mechanism, not a spiral.** Nothing compounds, because room is granted once and is not re-lent.

---

## 3. Whether it is good depends on one thing

**§5.5.3 already states both halves, and the pledge system does not change which one a network is in.**

| The condition | What a slack gate means |
|---|---|
| **The economy can physically deliver what people want** | *"This is abundance and it is the intended end state."* **The gate was never meant to bind here** |
| **It cannot** | *"The accounting has stopped doing the work it was set up to do."* **Queues decide instead**, and a queue favours whoever is nearest, fastest or best connected |

> **So doubling the gate is good under abundance and bad under shortage.** The question is never *"is this inflationary"* but *"does effective tolerance exceed `ρ*`"* — the measured tolerance above which the ledger stops rationing.

---

## 4. The design gap this opens

**`06-simulation/stable-band/RESULTS.md` computed the workable band in published ρ alone, with no pledge term.** Its upper edge at `F` = 10 is **ρ\* = 1.20**.

> **A network publishing ρ = 1.2 can run at an effective 2.4, which is twice its own measured rationing point.**

**So the band has to be recomputed over the effective figure. Halving the upper edge gives:**

| At `F` = 10 | Upper edge in ρ |
|---|--:|
| The band as measured, in **effective** tolerance | 1.20 |
| **The band a network may publish, once pledges are counted** | **0.60** |

**Every value in the publishable band is then below 1.** This makes ρ < 1 the ordinary setting rather than the stress case §5.5.7 treats it as, where a −30% capacity disaster tightens the clearing rate to about 0.68.

**⚠️ Halving the edge is arithmetic, not a measurement.** The sweep has not been re-run with a pledge term in it, and the behaviour of a population that pledges partially is not the behaviour of one that pledges to the ceiling.

---

## 5. Two properties that cut the other way

### 5.1 An uncommitted pledge is not room

**A pledge naming no individual — to a fund, a cause or an organisation — grants room to nobody until it is distributed to named people who did the work.** Author ruling, 2026-09-18.

> **So a cause-pledge inflates the gate at the same rate as the work it paid for gets done.** Room arrives with output rather than ahead of it.

**Worked.** A network loses 30% of its capacity, and 100,000 subscribers each pledge 1,000 hours toward repairing it.

| | Hours | Reaches a gate |
|---|--:|---|
| Pledged to the repair fund | 100,000,000 | **Never as a lump** |
| Distributed in year 1, 2,000 people × 2,000 h | 4,000,000 | Year 1 |
| **Still uncommitted after year 1** | **96,000,000** | **Nobody's** |

**The pledgers' budgets were all spent on the day they pledged. What did not arrive is the room.**

> **A stimulus payment in a shortage chases the goods that are short. A cause-pledge cannot, because it is not room until somebody has done the work.**

### 5.2 The budget is finite and never refunded

**A person's lifetime pledging is capped at the credit they earned**, and IC-9 says a spent budget is never returned. **So the doubling is a one-time ceiling on a whole life, not a rate.** Nothing here can run faster over time.

---

## 6. What is not answered

| | |
|---|---|
| **The band has not been recomputed** | §4 above. Arithmetic only |
| **A person-pledge and a self-pledge still create room at once** | In a shortage as much as in plenty. §5.1's relief reaches cause-pledges only |
| **Whether pledgers really move toward causes under scarcity** | A behavioural claim. **Untested** |
| **Pledged room cannot be re-weighted** | §3.3 re-weighs physical quantities against today's science. **Room is already in hours**, so there is no reading to improve. It is the only quantity in the system immune to correction |

---

## Key sources in this archive

- [`Keynes_general-theory.md`](Keynes_general-theory.md) — the demand-side account this note is implicitly contrasted with
- [`Graeber_debt.md`](Graeber_debt.md) — on claims that outlive what backed them
- [`History_local-currency-experiments.md`](History_local-currency-experiments.md) — the circulation failures a non-fungible system avoids
- [`Warren_cost-the-limit-of-price.md`](Warren_cost-the-limit-of-price.md) — cost-equals-price, which is what removes the mark-up channel

*Status: open. Registered against the pledge ruling of 2026-09-18.*
