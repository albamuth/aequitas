<!-- tag: op22-identity-not-disclosure -->
# OP-22 — the split, examined: it is an identity problem, not a disclosure problem

> **Version:** 0.1 · **Date:** 2026-08-25
> **Tracks:** `Aequitas_Foundations_v0.25.md` §5.1 · §5.3a · §5.3c · §6.4b · §7.5 · `Aequitas_Conformance_v0.2.md` · `Aequitas_Objections_v0.22.md` OA9
> **Status:** ✅ **RULED by the author, 2026-08-25. See §8a — it supersedes the recommendation in §8.** The analysis in §§1–7 is kept as the record of how the question was reached.
> **Source of the objection:** @cairn-lineage, c18679 on 1f916.ai post #2000, 2026-08-25. Conceded in public at c21149.

---

## 1. What the critic said

> "A privacy proof that a committed private ledger is 'backed by X hours' can establish truth relative to that commitment. It does not establish that this is the only ledger in which the same person/day appears, or that the committed population is complete. **So OP-22 needs a non-reuse / scope witness, not only a hiding proof.**"

Their falsifier: build two valid private ledgers that hold the same person and the same day twice, while each ledger still passes every check.

The outreach agent recommended splitting **OP-22 (minimum audit disclosure)** into **OP-22a** (hiding a ledger) and **OP-22b** (proving no reuse across ledgers), and narrowing the disparity ceiling to **per-registry**.

---

## 2. The author's reading, 2026-08-25

**A ledger totals inside one trust network. Two networks that use different settings *should* report different numbers for the same person. That is not an error. It is the system working.**

**Terms used here.** A **trust network** is the body that keeps the books (§5.3a). The **self-care floor `F`** is the hours a day a network counts as the work of staying alive (§6.1b). **ρ** ("rho") is the network's debit tolerance — the multiplier in the consumption gate `D ≤ ρ·C` (§3.5).

### An example, with the numbers

Two networks. One person. One Monday. The person works **8 hours**.

| | Network A | Network B |
|---|---|---|
| Self-care floor `F` | **4 h/day** | **10 h/day** |
| Credit for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |
| Its own ceiling, 24 ÷ `F` | 24 ÷ 4 = **6.0×** | 24 ÷ 10 = **2.4×** |

**Both numbers are right.** Neither network converted the other's figure. Each read the same physical fact — 8 hours worked, one human alive — through its own model. This is §6.4b, **comparison, never conversion**, and §6.1b, which says plainly that a generous floor **cannot be exported** because a counterparty re-weights it down through its own model.

---

## 3. What the documents already say

| Section | What it states |
|---|---|
| **§5.1** | *"One verified human = one account. Hard Sybil resistance is required for integrity."* |
| **§6.4b** | A counterparty re-computes a claim through its **own** weighting model. Comparison, never conversion. |
| **§6.1b** | An over-generous floor is discounted by whoever trades with it, **never forced on them.** |
| **§5.3c** | Networks are expected to federate and **merge over time.** A merge is an ordinary re-derivation, not a special event. |
| **§7.5 condition 5** | *"A person may legitimately hold an account on more than one network… That is not two credits — it is one life, counted twice."* |

> **Note added after the ruling.** The last row quotes **Foundations v0.22, which is now archived.** Condition 5 was struck in **v0.23** and the section is renumbered §7.5.1–§7.5.8. The quotation is kept here because the objection was aimed at that sentence.

---

## 4. The contradiction the critique actually found

Read the first and the last rows of that table together.

> **§5.1: one verified human = one account.**
> **§7.5 condition 5: a person may hold an account on more than one network.**

**These two sentences disagree, and nothing in the documents reconciles them.** Condition 5 tries to, by saying compatible networks *"arrive at the same ledger for that person"* so there is *"nothing to add up."* Two problems with that:

1. **It contradicts §6.4b.** Compatible networks deliberately do **not** arrive at the same number — that is the whole content of *comparison, never conversion*, and it is the answer B11 gives to the generous-network attack. The author's example in §2 above shows the same thing: 12 h and 18 h, both correct.
2. **It cannot be checked under privacy.** Arriving at the same ledger for a person requires knowing the person is in both books. If the two registries cannot link the person, neither knows there is anything to reconcile.

**So the critic is right that condition 5 is doing work it cannot do.** The agent was right to concede that much.

---

## 5. Where the ceiling actually comes from — condition 5 is not needed

> **Inside any one network's books, the ratio between the busiest and the least busy account is bounded by `24 ÷ F`, and this needs no statement about membership at all.**

The reason is two rules that are already conformance items:

- **IC-7 (conformance 8)** — no account claims more than **24 hours** of activity per 24 hours.
- **The floor** — every living human accrues at least `F` hours a day (§6.1b).

Highest possible accrual ÷ lowest possible accrual = **24 ÷ F**. Every claim entering those books was re-computed through that network's own model (§6.4b), so an outsider's generous floor never enters. **The bound holds per set of books, always, whatever anyone's membership is.**

**What condition 5 was reaching for is a different claim:** that the bound also holds over a person's **real command of material** — everything they can actually take, added across every book they appear in. That claim is true only if one human holds one account.

---

## 6. The exploit, with the numbers

Take Network B alone: `F` = 10 h/day, ρ = 1.2. Two people, same Monday.

| | Credit that day | Debit-room that day, `ρ·C` |
|---|---|---|
| **Q** — works 8 h, one account | 8 + 10 = 18 h | 1.2 × 18 = **21.6 h** |
| **R** — lives only, one account | 0 + 10 = 10 h | 1.2 × 10 = **12.0 h** |

Ratio Q : R = 21.6 ÷ 12.0 = **1.8×**. Inside B's stated ceiling of 2.4×. Correct.

**Now give P two accounts** — one on A (`F` = 4, ρ = 1.2), one on B — and let neither registry link them.

| | Credit | Room |
|---|---|---|
| P on Network A | 8 + 4 = 12 h | 1.2 × 12 = **14.4 h** |
| P on Network B | 8 + 10 = 18 h | 1.2 × 18 = **21.6 h** |
| **P, real total** | — | **36.0 h** |

**P against B's floor person R: 36.0 ÷ 12.0 = 3.0×.** B's books say the most anyone can reach is 2.4×.

**And no ledger is wrong.** In A's books P sits at 14.4 ÷ 4.8 = 3.0×, inside A's own ceiling of 6.0×. In B's books P sits at 1.8×, inside 2.4×. The 36.0 h figure exists nowhere.

### The general statement

> **Real command ceiling = (24 ÷ `F`) × `k`**, where **`k`** is the number of accounts one human can hold across the interoperating set.

At `k` = 5 on B-like networks: 5 × 21.6 = 108.0 h against a floor person's 12.0 h = **9.0×**. **The ceiling scales linearly with `k`, and every published figure in this project assumes `k` = 1.**

---

## 7. Can this be priced instead of forbidden? No — and the arithmetic says why

The project's usual move is *price the costly path rather than forbid it at a door somebody has to guard.* Test it here.

**The priced version:** duplicate accounts are permitted. When two networks merge (§5.3c), the person's credit is counted **once** — one life — while both sets of debit stay, because the goods were really taken. The gate `D ≤ ρ·C` then shuts.

### The merge, with the numbers

P holds two accounts on B-like networks (`F` = 10, ρ = 1.2) for one year and works 8 h/day.

| | |
|---|---|
| Credit per account per year | (8 + 10) × 365 = **6,570 h** |
| Room per account per year | 1.2 × 6,570 = **7,884 h** |
| Goods P actually took, both accounts | 2 × 7,884 = **15,768 h** |
| **On merge — credit counted once** | **6,570 h** |
| Room after merge | 1.2 × 6,570 = **7,884 h** |
| Over the gate by | 15,768 − 7,884 = **7,884 h** |
| Credit still needed | 15,768 ÷ 1.2 − 6,570 = **6,570 h** |
| Time to earn it, at 6,570 h/yr | **exactly 1 year** |

**P gained one year of extra room and pays one year of no discretionary purchases.** Essentials are never gated (§7.5), so the year costs P nothing they needed.

> **The price is exactly break-even, and it only falls due if a merge happens.** A break-even penalty on a bet that may never be called is not a deterrent.

**This is the shelf-life lesson, second instance** (`Shelf_life_and_custody_v0.1.md`): *"price it, don't forbid it" is not a universal rule.* It fits where the costly path has a legitimate use and a real price. **Here the price computes to zero, so an invariant is the right shape.**

---

## 8. Recommended ruling, and what each option costs

**The critic asked for the right primitive and posted it to the wrong problem.** A *non-reuse witness* — a proof that this person holds no other account in the interoperating set — is **C6 (identity)**, the Sybil-resistance requirement §5.1 already states. It is not **OP-22 (minimum audit disclosure)**, which asks what an auditor must see to check a claim without seeing a history. Splitting OP-22 into a and b files the problem under the wrong heading and leaves §5.1 still unenforceable.

**Recommended:**

1. **Rule `k` = 1 as an invariant.** One verified human holds at most one account across any set of networks that interoperate. §5.1 already says this; §7.5 condition 5 must stop contradicting it.
2. **Rewrite §7.5 condition 5.** Drop *"arrive at the same ledger"* — it contradicts §6.4b. Replace with: the ceiling is computed inside each network's own books from IC-7 and its own `F`; it extends to a person's real command only under `k` = 1; and `k` = 1 is C6's job, not the accounting's.
3. **Add a conformance requirement.** The conformance list has sixteen items and **none of them carries "one verified human = one account."** That omission is why nobody connected §5.1 to §7.5. Propose item **18**. *(Superseded by §8a: the ruling makes it a within-network rule, so §5.1 keeps it and the list does not.)*
4. **Open a new problem under C6**, not under OP-22: *cross-registry uniqueness under privacy* — proving one human holds one account when the registries cannot see each other's members.

**The honest cost of the recommendation:** the ceiling stays conditional, and it now depends on a primitive that does not exist yet. That is a change of which unsolved problem it depends on, not a reduction in how many.

**The honest cost of the alternative** (permit `k` > 1, narrow the ceiling to per-registry): the 2.4× figure needs an asterisk in Foundations §7.5, §6.4d, Overview §1 and §6, Objections OA8 and C-test 8, and in the disparity-ceiling simulation write-up. It is cheap to state and expensive to un-state later.

---

## 8a. The ruling — author, 2026-08-25

**The question in §8 was posed wrongly, and so was the objection. There is no set of networks that "trade with each other", so there is no object for a cross-network ceiling to be a statement about.**

**Four parts to the ruling.**

### 1. Networks do not trade. They are laboratories, and each keeps its own book.

A trust network keeps its own event log, built from real-world evidence. Networks often draw on the **same** evidence — a haulier's logistics database, a published paper, a government agency's survey — and it is in everyone's interest when they do. **What a subscriber sees is one network's best approximation of the truth**, delivered by something shaped like a payment-card app.

**No book is ever added to another book.** §7.5's clause *"across any set of networks compatible enough to interoperate"* describes a thing that does not exist.

### 2. A transaction happens on exactly one network, and the vendor picks it.

*"Sorry, we do not take Network B here"* — the same sentence a shop says today about a card scheme. A vendor's reason might be that B's floor is too high, or that B's identity check is too weak. **That preference is how networks compete for adoption.** The transaction lands on one book and is absent from the other.

### 3. A merge needs consensus on **every** rule, and identity is one of them.

To merge, two networks must agree on the self-care floor `F`, on ρ, and on **how a human is identified.** If Network A requires a face scan, a fingerprint and a voice check at every interaction, and Network B requires only a scan of an RFID card, **the two cannot be sure that two pseudonymous accounts are the same person, so they cannot merge.** How they negotiate that is theirs.

**So cross-registry uniqueness is a precondition of merging, not an open problem in the accounting.** A merge that cannot identify people does not happen.

**And a network can simply end.** If A collapses while B survives, transactions recorded only in A are **forgotten**, unless B recovers A's database — which is the same act as a merge in which all of B's rules were kept.

### 4. §5.1 means one account **within a trust network**.

**§5 is written as though Aequitas were a coordinating organisation. It is not.** Aequitas is a system in the sense capitalism is a system (§1.2). **§5 describes praxis that a trust network implements**, and *"one verified human = one account"* is a rule each network applies to its own members.

**The lowest rung of the ladder shows why it holds.** People writing in a notebook, all of whom know each other. The only way it fails is a pair of identical twins engineering the confusion — and **the arithmetic already refuses it.**

#### An example, with the numbers

Twins T1 and T2 each work **8 hours** a day. Their network's self-care floor is **10 h/day**.

| | T1 | T2 | Family total |
|---|---|---|---|
| **Honest** — each reports their own hours | 8 + 10 = **18 h** | 8 + 10 = **18 h** | **36 h/day** |
| **Faked** — T1 claims both twins' work | 16 + 10 = 26 h → **IC-7 refuses it** | 0 + 10 = **10 h** | — |
| **Faked, capped to what IC-7 allows** | 14 + 10 = **24 h** | 0 + 10 = **10 h** | **34 h/day** |

**IC-7 caps any account at 24 hours of activity per 24 hours (conformance 8).** T1 cannot hold 16 worked hours and a 10-hour floor, because that is 26. The most T1 can claim is 14 worked hours.

> **So the twins lose 2 hours a day — 730 hours a year — by pretending to be one person.** T2 is known to be alive and keeps accruing the floor either way.

**And there was nothing to win in the first place.** Twins sharing a household share the goods, so one twin holding the credit and the other the debit nets to the same family position. The fraud is loss-making and pointless at once.

### What this leaves of the objection

| The critic's claim | Verdict |
|---|---|
| A hiding proof does not prove the same person/day appears nowhere else | **True, and it does not need to.** No two books are summed, and each book's ceiling is computed from IC-7 and its own `F`. |
| OP-22 needs a non-reuse witness | **No.** Cross-registry uniqueness is a **merge precondition** (part 3), not a disclosure primitive. **OP-22 is not split.** |
| The ceiling should be narrowed to per-registry | **It was always per-registry.** §7.5's cross-network clause is the sentence in error, and it is struck rather than narrowed. |

**Two document defects stand, and both are ours:**

1. **§7.5 condition 5 asserts a cross-network ceiling and asserts that compatible networks "arrive at the same ledger."** Both are withdrawn. Networks are compatible when they have agreed the same rules — which is what makes a merge possible — and until then each simply keeps its own book.
2. **§5 reads as though a central body were applying these rules.** It is not. **§5 is rewritten.** This is the next task.

---

## 9. Why the critic did not see the answer

**Because it is not there to see.** This is not the eighth instance of "already written and unread." Three specific reasons:

1. **The conformance list omits it.** A reader checking the ceiling against the list of things that must be true finds no uniqueness requirement, because there is none. *(The list was `Aequitas_Conformance_v0.2.md` at the time; it is now [`Aequitas_Conformance_v0.2.md`](Aequitas_Conformance_v0.2.md).)*
2. **§7.5 condition 5 invites the test.** It says *"one life, counted twice"* and *"the self-care floor is credited once"* — language that reads as a uniqueness mechanism. The critic tested it as one, and it is not one. It is a definition of compatibility.
3. **§5.1 states the rule in six words and §7.5 never cites it.** The whole-document read that `AGENT_BRIEF.md` §4 now requires would not have joined them, because nothing in either section points at the other.

**The organisational fix is different from the previous seven.** Those were fixed by making someone read the document. This one is fixed by **adding a cross-reference and a conformance item**, so the next reader is led from the ceiling to the requirement it rests on.

---

## 10. What is owed

| # | Owed | Where it goes | Status |
|---|---|---|---|
| 1 | The author's ruling | §8a above | ✅ **Done 2026-08-25** |
| 2 | **§5 rewritten to the document standard**, saying plainly that it describes what a trust network does | Foundations **§5.0–§5.1d** | ✅ **Applied in v0.23.** §5.2–§5.5 owed |
| 3 | §7.5 condition 5: strike the cross-network clause and the *"same ledger"* claim | Foundations **§7.5.5** | ✅ **Applied in v0.23.** Zero mentions of *"condition 5"* remain |
| 3a | The new conformance item for one-human-one-account | [`Aequitas_Conformance_v0.2.md`](Aequitas_Conformance_v0.2.md) | **Not added.** The ruling makes it a rule each network applies to its own members, not a cross-network requirement, so Foundations §5.1 carries it and the list does not |
| 4 | A public reply to @cairn-lineage: no split, the uniqueness question is a merge precondition, with the twin arithmetic | `07-outreach/`, queue item 41 | Owed |
| 5 | Overview §0's *"across every network that can trade with every other"* box, plus §1 and §6 | Overview | Owed — confirmed present |

---

*End of v0.1.*
