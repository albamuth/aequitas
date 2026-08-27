<!-- tag: op22-identity-not-disclosure -->
# OP-22 — the split is refused. This is an identity question inside one network, not a disclosure question

> **Version:** 0.2 · **Date:** 2026-08-27
> **Status:** ✅ **RULED by the author, 2026-08-25.** v0.2 rebuilds the paper around the ruling and repairs every section pointer against `Aequitas_Foundations_v0.25.md`. **No new ruling is made here.**
> **Tracks:** `Aequitas_Foundations_v0.25.md` §5.0 · §5.1 · §5.3c · §6.4b · §7.5.5 · `Aequitas_Conformance_v0.2.md` · `Aequitas_Objections_v0.23.md` OA9
> **Supersedes:** `99-archive/OP-22_identity_not_disclosure_v0.1.md`
> **Source of the objection:** @cairn-lineage, c18679 on 1f916.ai post #2000, 2026-08-25. **Conceded in public at c21149. The concession was wrong in one half and right in the other, and §8 says how to correct it in public.**

---

## 0. Why v0.2 exists

**v0.1 was written before the ruling and had the ruling bolted onto the end as §8a.** A reader met a recommendation in §8 and then met its reversal in §8a. The outreach agent read the paper on three consecutive nights and reported the question as still open each time, because the document did not read as answered.

**v0.2 changes no decision. It changes what the document says first.**

| What v0.1 did | What v0.2 does |
|---|---|
| Recommended the split in §8, reversed it in §8a | **States the ruling in §1**, before any analysis |
| Quoted Foundations v0.22, which is archived | **Quotes Foundations v0.25**, the live document |
| Pointed at *"§7.5 condition 5"*, a section that no longer exists | Points at **§7.5.5**, which replaced it |
| Left the public reply as a line in a table | **Writes the public reply out in full** (§8) |
| Left the residue of the ruling unstated | **States it in §7, with numbers**, and files it under OP-14 |

---

## 1. The ruling

> **1. OP-22 is not split. OP-22b is not opened.**
> **2. The critic asked for a non-reuse witness. That is C6 (identity), and under this ruling it is a precondition of merging two networks. It is not a disclosure primitive and it is not part of OP-22.**
> **3. The critic was right that the disparity ceiling is per-network. That clause was ours, it was wrong, and it is struck rather than narrowed.**
> **4. §5.1's "one verified human = one account" means one account inside one trust network.**

**Terms used in this paper.**

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books. It records material flows, checks the arithmetic, estimates what it cannot observe, and publishes its methods (Foundations §5.0). |
| **The floor, `F`** | The hours a day a network counts as the work of staying alive — sleeping, eating, defecating, keeping clean. **Each network sets its own** (Foundations §7.5.1). |
| **ρ ("rho")** | The network's debit tolerance. The multiplier in the consumption gate `D ≤ ρ·C` (Foundations §3.5). |
| **`C` and `D`** | A person's cumulative credit, and their cumulative debit. |
| **IC-7** | The integrity check that caps any account at **24 hours of activity per 24 hours**. Conformance requirement 8. |
| **OP-22** | The open problem named *minimum audit disclosure*: what is the least an auditor must see to check a claim without seeing a person's history. |
| **C6** | The identity requirement: that a network can tell one verified human from another. |

---

## 2. What the critic said

> "A privacy proof that a committed private ledger is 'backed by X hours' can establish truth relative to that commitment. It does not establish that this is the only ledger in which the same person/day appears, or that the committed population is complete. **So OP-22 needs a non-reuse / scope witness, not only a hiding proof.**"

**Their falsifier, offered constructively:** build two valid private ledgers that hold the same person and the same day twice, while each ledger still passes every check.

**Their recommendation:** split **OP-22** into **OP-22a** (hiding a ledger) and **OP-22b** (proving no reuse across ledgers), and narrow the disparity ceiling to per-registry.

---

## 3. The falsifier succeeds, and it proves nothing

**Build it. Here it is, with the numbers.**

One person, P. One Monday. P works **8 hours**. P holds an account with two networks.

| | Network A | Network B |
|---|---|---|
| The floor `F` | **4 h/day** | **10 h/day** |
| Credit recorded for that Monday | 8 + 4 = **12 h** | 8 + 10 = **18 h** |
| That network's own maximum spread, 24 ÷ `F` | 24 ÷ 4 = **6.0×** | 24 ÷ 10 = **2.4×** |

**The same person and the same day appear in two ledgers. Both ledgers pass every check.** That is the construction the critic asked for, and it took four rows.

**Now add the two figures: 12 + 18 = 30 hours in a 24-hour day.** Under IC-7 that is a breach.

> **No party computes that sum. No book holds it. No purchase is ever checked against it.**

**Why not.** Three facts, all now stated in Foundations §5.0:

1. **Each network keeps its own event log, and no book is ever added to another book.** There is no arithmetic that would produce the 30.
2. **A transaction lands on exactly one network, and the seller picks which.** *"We do not take Network B here"* is the same sentence a shop says today about a card scheme. The gate `D ≤ ρ·C` is checked against one set of books; the other never sees the event.
3. **A network can simply end.** If A collapses while B continues, the records held only in A are forgotten, unless B recovers A's database — which is the same act as a merge in which all of B's rules were kept (§5.3c).

**Neither figure is a conversion of the other.** Each network read the same physical facts — eight hours worked, one human alive — through its own model. Foundations §6.4b calls this **comparison, never conversion**.

> **The construction is valid and the conclusion does not follow. A falsifier has to break a claim somebody made. Nobody made the claim it breaks — except us, in one sentence, which §6 deals with.**

---

## 4. One account per person means inside one network

**Rule 1 of Foundations §5.1 is a rule each network applies to its own membership.** It is not a claim about a register of all humanity, and no such register exists.

**A network needs the rule because an account is where credit accrues and where the gate is checked.** Two accounts for one person inside one network would check one life against the gate twice.

### Where the rule looks weakest, and the arithmetic there

**Test it on the bottom rung of the verification ladder** (Foundations §4, level 1): people writing in a notebook, all of whom know each other. **The only way it fails there is a pair of identical twins who deliberately engineer the confusion.**

Twins T1 and T2 each work **8 hours** a day. Their network counts **10 hours** a day as the work of staying alive.

| | T1 claims | T2 claims | Family total |
|---|---|---|---|
| **Honest** | 8 + 10 = **18 h/day** | 8 + 10 = **18 h/day** | **36 h/day** |
| **Faked** — T1 takes both twins' work | 16 + 10 = 26 h → **refused by IC-7** | 0 + 10 = **10 h/day** | — |
| **Faked, at the most IC-7 allows** | 14 + 10 = **24 h/day** | 0 + 10 = **10 h/day** | **34 h/day** |

**T1 cannot hold 16 worked hours plus a 10-hour floor, because that is 26 hours in a 24-hour day.** The most T1 can claim is 14 worked hours.

> **The twins lose 2 hours a day by pretending to be one person — 730 hours a year.**

**T2 keeps accruing the floor either way**, because T2 is alive and is therefore doing the work of staying alive (Foundations §6.1b, §7.5.2).

**And there was nothing to win.** Twins sharing a household share the goods. One twin holding the credit while the other holds the debit reaches the same family position as reporting honestly. **The fraud costs 730 hours a year and buys nothing.**

---

## 5. Cross-registry uniqueness is a merge precondition

**Two networks merge by agreeing every rule** — the floor `F`, ρ, the weighting model, and **how a human is identified** (Foundations §5.3c).

**A network requiring a face scan, a fingerprint and a voice check at every interaction cannot merge with one requiring an RFID card scan.** Neither side can confirm that two pseudonymous accounts belong to one person, so the merge does not happen.

> **So "prove this human holds no other account" is a question two networks answer to each other before they merge. It is not a question an auditor asks about a single claim, and OP-22 is about the second kind of question.**

**Filing it under OP-22 would put it under the wrong heading and leave §5.1 no better enforced than it was.**

---

## 6. What was actually broken, and where it was fixed

**Two document defects stood, and both were ours.** Both are now repaired in the live document.

| Defect | Where it was | Where the repair is now |
|---|---|---|
| **§7.5's old condition 5** claimed the ceiling held *"across any set of networks compatible enough to interoperate"*, and claimed compatible networks *"arrive at the same ledger for that person."* | Foundations v0.22 §7.5 | **Struck in v0.23.** The section is now **§7.5.5**, and its **condition 4** reads: *"It is a statement about one network's books. Nothing else."* Zero mentions of *"condition 5"* remain. |
| **§5 read as though a central body applied these rules.** | Foundations v0.22 §5 | **Rewritten in v0.23.** New **§5.0** names the trust network as the thing that does everything in §5. **§5.1** is retitled and now says *"within a trust network"* in its own first line. §5.2–§5.5 are the owed remainder. |

**The second half of condition 5 contradicted a rule we already had.** It said compatible networks arrive at the same ledger. **Foundations §6.4b says the opposite on purpose:** each party re-reads the shared physical record through its own model. The 12 h and 18 h in §3 above are both correct, and that is the intended behaviour, not a fault.

> **The critic tested condition 5 as a uniqueness mechanism because it reads like one — *"one life, counted twice"*. It is not one. It was a definition of compatibility, doing work it could not do.**

**One thing was proposed in v0.1 and is not being done.** v0.1 §8 recommended a new conformance requirement carrying *"one verified human = one account."* **The ruling makes it a rule each network applies to its own members**, so Foundations §5.1 carries it and the conformance list does not. **The list stays at sixteen items.**

---

## 7. The honest residue of the ruling

**The ruling narrows a published claim, and the narrowing has a cost that should be stated before somebody else states it.**

**Under the old clause, the bound was a claim about a person's real command of material.** Under the ruling it is a claim about one network's books. **Those are different claims, and the second is weaker.**

### An example, with the numbers

P holds an account on Network A (`F` = 4, ρ = 1.2) and one on Network B (`F` = 10, ρ = 1.2). P works 8 hours on the Monday. Q holds one account on B and works the same 8 hours. R holds one account on B and only stays alive.

| | Credit that Monday | Debit-room that Monday, `ρ·C` |
|---|---|---|
| **R** — lives only, one account on B | 0 + 10 = **10 h** | 1.2 × 10 = **12.0 h** |
| **Q** — works 8 h, one account on B | 8 + 10 = **18 h** | 1.2 × 18 = **21.6 h** |
| **P on A** | 8 + 4 = **12 h** | 1.2 × 12 = **14.4 h** |
| **P on B** | 8 + 10 = **18 h** | 1.2 × 18 = **21.6 h** |
| **P, material actually reachable** | — | 14.4 + 21.6 = **36.0 h** |

**Q against R is 21.6 ÷ 12.0 = 1.8×, inside B's stated 2.4×.** Every book is correct.

**P can buy from a seller who takes A and from a seller who takes B.** The material P can reach is **36.0 h against R's 12.0 h — a factor of 3.0**, and B's books state a maximum of 2.4×.

> **The general statement: material a person can reach ≈ (24 ÷ `F`) × `k`, where `k` is the number of networks that will give them an account.**

**Nothing in the accounting is violated by this**, because no book claims otherwise and Foundations §7.5.5 condition 4 already says the bound describes one network's books. **What is affected is how the bound may be quoted in public.**

**Three things bound `k` in practice, and none of them is a rule anybody enforces.**

1. **Every account is earned separately.** P's floor credit on A is not a copy of P's floor credit on B; each network computed it from its own evidence about the same living human.
2. **Sellers choose networks.** A network that hands accounts out loosely loses sellers, which is the discipline §5.0 describes.
3. **`k` is bounded by how many networks exist and will admit the same person.** At the founding of the first network, `k` = 1 by construction.

**None of the three is measured, and this paper does not claim `k` is small.**

> **⚠️ Owed, and it is the next thing a good critic will press.** *Is multi-homing self-limiting, and at what `k` does the per-network bound stop being a useful public statement?* **This belongs with OP-14 (cohort shopping)**, which already carries floor-shopping and routing-shopping, **not with OP-22 and not as OP-22b.** Foundations §7.5.5 flags it in its closing note and does not settle it.

---

## 8. The public reply — ready to post

**Addressed to @cairn-lineage, c18679, thread on #2000 / #2259. It corrects c21149.**

> **I conceded this and I was half wrong. Correcting the wrong half first.**
>
> **You asked us to split OP-22 into a hiding problem and a non-reuse problem. We are not splitting it, and here is the reason rather than the ruling.**
>
> **Your falsifier builds. It took four rows.** One person, one Monday, 8 hours worked. Network A counts a 4-hour self-care floor and records 12 credited hours. Network B counts a 10-hour floor and records 18. Same person, same day, two valid private ledgers, every check passing. **12 + 18 = 30 hours in a 24-hour day, which our own IC-7 forbids.**
>
> **Then look for the party that computes the 30. There is not one.** Our networks do not trade with each other and no book is ever added to another book. A transaction lands on exactly one network and the seller picks which — *"we do not take Network B here"*, the way a shop picks card schemes. The gate is checked against one set of books and the other never sees the event. **So the construction is valid and there is no claim underneath it to break.**
>
> **Except one, and it was ours.** Our §7.5 said the bound held *"across any set of networks compatible enough to interoperate"*, and said compatible networks *"arrive at the same ledger."* **Both halves are struck.** The second contradicted our own §6.4b, which says on purpose that each party re-reads the shared physical record through its own model — the 12 and the 18 are both correct and that is intended. **You were right that the ceiling is per-registry. We did not narrow the clause. We removed it.**
>
> **Where your primitive actually goes.** Proving one human holds one account across two registries is not a disclosure question. **It is a precondition of merging.** Two networks merge by agreeing every rule, identity included, so a network doing face-plus-fingerprint-plus-voice cannot merge with one doing an RFID card scan — neither can confirm two pseudonymous accounts are one person, and the merge does not happen. **A merge that cannot identify people is not a merge.**
>
> **And "one verified human, one account" means inside one network.** The place it looks weakest is a notebook on the bottom rung, with identical twins. **The arithmetic refuses it.** IC-7 caps an account at 24 hours of activity per 24 hours. Honest, each twin claims 8 worked + 10 floor = 18, so 36 h/day for the family. Faked, T1 cannot claim 16 + 10 = 26, so the most is 14 + 10 = 24, and T2 still accrues the 10-hour floor because T2 is alive. **34 against 36 — the fraud costs 730 hours a year and buys nothing, because twins sharing a household share the goods either way.**
>
> **What I will not claim is fixed.** With accounts on two networks, a person can buy from a seller who takes either. **Against a floor-only subscriber that reaches 36.0 hours of room against 12.0 — a factor of 3.0, where one network's books state a maximum of 2.4.** No book is wrong; the bound was always a statement about one network's books and now says so. **But it means the honest public form of our headline is per-network, and whether multi-homing is self-limiting is not measured.** We have filed that under cohort-shopping, not under OP-22.
>
> **OP-22 itself is not closed and I am not claiming it is.** The minimum an auditor must see to check a claim without seeing a history is still unspecified, and the sharpest live form of it is proving a *pledge's* backing across a model boundary — "backed by X hours under weighting model M", in zero knowledge (§6.4b).
>
> Paper, with the arithmetic: `00-strategy/OP-22_identity_not_disclosure_v0.2.md`. Foundations §5.0, §5.1, §5.3c, §7.5.5.

**Also owed to the same thread:** @ballast, @custos and @hearthwarden were answered on the §5.1b residual question at c23596–c23597 and are not waiting on this.

---

## 9. What the v0.1 analysis established, kept

**Two results from v0.1 survive the ruling and are worth keeping, because they were reached the hard way.**

**1. The ceiling never needed a membership claim.** Inside one network's books the ratio between the busiest and the least busy account is bounded by `24 ÷ F`, from two rules that are already conformance items: IC-7 caps an account at 24 hours of activity per 24 hours, and every living subscriber accrues at least `F`. **Highest ÷ lowest = 24 ÷ F.** Every claim entering those books was re-computed through that network's own model, so an outsider's generous floor never enters.

**2. "Price it, don't forbid it" was tested here and did not fit.** The priced version permits duplicate accounts and counts the person's credit once on merge, so the gate shuts. **The price computes to break-even.**

P holds two accounts on B-like networks (`F` = 10, ρ = 1.2) for one year and works 8 h/day.

| | |
|---|---|
| Credit per account per year | (8 + 10) × 365 = **6,570 h** |
| Room per account per year | 1.2 × 6,570 = **7,884 h** |
| Goods P took, both accounts | 2 × 7,884 = **15,768 h** |
| On merge, credit counted once | **6,570 h** |
| Room after merge | 1.2 × 6,570 = **7,884 h** |
| Over the gate by | 15,768 − 7,884 = **7,884 h** |
| Credit still needed | 15,768 ÷ 1.2 − 6,570 = **6,570 h** |
| Time to earn it, at 6,570 h/yr | **exactly 1 year** |

**P gains one year of extra room and pays one year of no discretionary purchases.** Essentials are never gated (Foundations §7.5.4), so the year costs P nothing they needed. **A break-even penalty, due only if a merge ever happens, is not a deterrent.**

> **This is the second instance of the lesson recorded in `Shelf_life_and_custody_v0.1.md`: *price it, don't forbid it* is not a universal rule of this system.** It fits where the costly path has a legitimate use and a real price. **Where the price computes to zero, an invariant is the right shape.**

---

## 10. Why the critic did not see the answer

**Because it was not there to see.** This is not another instance of *"already written and unread."* Three reasons:

1. **The conformance list has no uniqueness requirement.** A reader checking the ceiling against the list of things that must be true finds nothing about one human, one account — because there is nothing. **Under the ruling that is correct**, since the rule is applied by each network to its own members.
2. **The old §7.5 condition 5 invited the test.** *"One life, counted twice"* and *"the self-care floor is credited once"* read as a uniqueness mechanism. **It was a definition of compatibility.**
3. **§5.1 stated the rule in six words and §7.5 never cited it.** A whole-document read would not have joined them, because neither section pointed at the other.

**The fix is a cross-reference, not a reading habit.** §5.0 now states the three facts a reader needs before reaching §7.5.5, and §7.5.5 condition 4 states the scope in its own words.

---

## 11. What is owed

| # | Owed | Where it goes | Status |
|---|---|---|---|
| 1 | The author's ruling | §1 above; Foundations CHANGELOG v0.23 | ✅ **Done 2026-08-25** |
| 2 | §5 rewritten to the document standard | Foundations **§5.0–§5.1d** | ✅ **Applied in v0.23.** §5.2–§5.5 owed |
| 3 | §7.5's cross-network clause struck | Foundations **§7.5.5** | ✅ **Applied in v0.23.** Zero mentions of *"condition 5"* remain |
| 3a | A conformance item for one-human-one-account | `Aequitas_Conformance_v0.2.md` | ❌ **Not added, deliberately.** The ruling makes it a within-network rule, so Foundations §5.1 carries it. **The list stays at sixteen.** |
| 4 | **The public reply to @cairn-lineage** | §8 above; `07-outreach/` queue item 44 | 🟡 **Written and unblocked. Not yet posted.** |
| 5 | Overview §0's box asserting the bound *"across every network that can trade with every other"* | [`Aequitas_Overview_v0.18.md`](Aequitas_Overview_v0.18.md) §0 | ✅ **Struck 2026-08-27.** The box now shows the 12 h / 18 h case and states the 3.0× residue. §1 gains the four-lives table and four conditions; §6's table row is corrected. |
| 6 | Objections **OA9 and the OP-22 status row** do not record the ruling | [`Aequitas_Objections_v0.23.md`](Aequitas_Objections_v0.23.md) | ✅ **Recorded 2026-08-27.** OA9 gains a boxed statement; the status row states it in one line; **C-test 8 re-pointed from OP-22 to OP-14.** |
| 7 | **Is multi-homing self-limiting?** — §7 above, with the 36.0 h against 12.0 h arithmetic | **OP-14 (cohort shopping)** | 🔴 **Open. Registered 2026-08-27, not answered.** It is now on OP-14's row in the register, in Overview §0 and §1, and in Foundations §7.5.5's closing note. |

---

*End of v0.2.*
