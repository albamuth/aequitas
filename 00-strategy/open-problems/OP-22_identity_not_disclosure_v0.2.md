<!-- tag: op22-identity-not-disclosure -->
# OP-22 — the split is refused. This is an identity question inside one network, not a disclosure question

> **Version:** 0.2 · **Date:** 2026-08-27
> **Status:** ✅ **RULED by the author, 2026-08-25.** v0.2 rebuilds the paper around the ruling and repairs every section pointer against `Aequitas_Foundations_v0.33.md`. **No new ruling is made here.**
> **Tracks:** `Aequitas_Foundations_v0.33.md` §4.0 · §4.1 · §4.8 · §4.2 · §5.5.5 · `Aequitas_Conformance_v0.8.md` · `Aequitas_Objections_v0.24.md` OA9
> **Supersedes:** `99-archive/OP-22_identity_not_disclosure_v0.1.md`
> **Source of the objection:** @cairn-lineage, c18679 on 1f916.ai post #2000, 2026-08-25. **Conceded in public at c21149. The concession was wrong in one half and right in the other, and §8 says how to correct it in public.**

---

## 0. Why v0.2 exists

**v0.1 was written before the ruling and had the ruling bolted onto the end as §8a.** A reader met a recommendation in §8 and then met its reversal in §8a. The outreach agent read the paper on three consecutive nights and reported the question as still open each time, because the document did not read as answered.

**v0.2 changes no decision. It changes what the document says first.**

| What v0.1 did | What v0.2 does |
|---|---|
| Recommended the split in §8, reversed it in §8a | **States the ruling in §1**, before any analysis |
| Quoted Foundations v0.22, which is archived | **Quotes the live Foundations**, not an archived version |
| Pointed at *"§5.5 condition 5"*, a section that no longer exists | Points at **§5.5.5**, which replaced it |
| Left the public reply as a line in a table | **Writes the public reply out in full** (§8) |
| Left the residue of the ruling unstated | **States it in §7, with numbers** — including the addition that is *not* available, and why |

---

## 1. The ruling

> **1. OP-22 is not split. OP-22b is not opened.**
> **2. The critic asked for a non-reuse witness. That is C6 (identity), and under this ruling it is a precondition of merging two networks. It is not a disclosure primitive and it is not part of OP-22.**
> **3. The critic was right that the disparity ceiling is per-network. That clause was ours, it was wrong, and it is struck rather than narrowed.**
> **4. §4.1's "one verified human = one account" means one account inside one trust network.**

**Terms used in this paper.**

| Term | What it means |
|---|---|
| **Trust network** | The organisation that keeps the books. It records material flows, checks the arithmetic, estimates what it cannot observe, and publishes its methods (Foundations §4.0). |
| **The floor, `F`** | The hours a day a network counts as the work of staying alive — sleeping, eating, defecating, keeping clean. **Each network sets its own** (Foundations §5.5.1). |
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

**Now try to add the two figures: 12 + 18 = 30 hours in a 24-hour day**, which IC-7 forbids.

> **Two things are wrong with that line, and the second is the deeper one.**
>
> **1. No party computes it.** No book holds it, and no purchase is ever checked against it.
> **2. It is not a legal addition in the first place.** A's hours and B's hours are not the same unit. **See §7.**

**And IC-7 was never breached.** A's account for P holds 12 credited hours. B's holds 18. **Each is under 24, and IC-7 binds each account separately.** There is no third account holding 30.

**Why nobody computes it.** Three facts, all now stated in Foundations §4.0:

1. **Each network keeps its own event log, and no book is ever added to another book.** There is no arithmetic that would produce the 30.
2. **A transaction lands on exactly one network, and the seller picks which.** *"We do not take Network B here"* is the same sentence a shop says today about a card scheme. The gate `D ≤ ρ·C` is checked against one set of books; the other never sees the event.
3. **A network can simply end.** If A collapses while B continues, the records held only in A are forgotten, unless B recovers A's database — which is the same act as a merge in which all of B's rules were kept (§4.8).

**Neither figure is a conversion of the other.** Each network read the same physical facts — eight hours worked, one human alive — through its own model. Foundations §4.2 calls this **comparison, never conversion**.

> **The construction is valid and the conclusion does not follow. A falsifier has to break a claim somebody made. Nobody made the claim it breaks — except us, in one sentence, which §6 deals with.**

---

## 4. One account per person means inside one network

**Rule 1 of Foundations §4.1 is a rule each network applies to its own membership.** It is not a claim about a register of all humanity, and no such register exists.

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

**T2 keeps accruing the floor either way**, because T2 is alive and is therefore doing the work of staying alive (Foundations §4.5, §5.5.2).

**And there was nothing to win.** Twins sharing a household share the goods. One twin holding the credit while the other holds the debit reaches the same family position as reporting honestly. **The fraud costs 730 hours a year and buys nothing.**

---

## 5. Cross-registry uniqueness is a merge precondition

**Two networks merge by agreeing every rule** — the floor `F`, ρ, the weighting model, and **how a human is identified** (Foundations §4.8).

**A network requiring a face scan, a fingerprint and a voice check at every interaction cannot merge with one requiring an RFID card scan.** Neither side can confirm that two pseudonymous accounts belong to one person, so the merge does not happen.

> **So "prove this human holds no other account" is a question two networks answer to each other before they merge. It is not a question an auditor asks about a single claim, and OP-22 is about the second kind of question.**

**Filing it under OP-22 would put it under the wrong heading and leave §4.1 no better enforced than it was.**

---

## 6. What was actually broken, and where it was fixed

**Two document defects stood, and both were ours.** Both are now repaired in the live document.

| Defect | Where it was | Where the repair is now |
|---|---|---|
| **§5.5's old condition 5** claimed the ceiling held *"across any set of networks compatible enough to interoperate"*, and claimed compatible networks *"arrive at the same ledger for that person."* | Foundations v0.22 §5.5 | **Struck in v0.23.** The section is now **§5.5.5**, and its **condition 4** reads: *"It is a statement about one network's books. Nothing else."* Zero mentions of *"condition 5"* remain. |
| **§5 read as though a central body applied these rules.** | Foundations v0.22 §5 | **Rewritten in v0.23.** New **§4.0** names the trust network as the thing that does everything in §5. **§4.1** is retitled and now says *"within a trust network"* in its own first line. §4.8–§4.8 are the owed remainder. |

**The second half of condition 5 contradicted a rule we already had.** It said compatible networks arrive at the same ledger. **Foundations §4.2 says the opposite on purpose:** each party re-reads the shared physical record through its own model. The 12 h and 18 h in §3 above are both correct, and that is the intended behaviour, not a fault.

> **The critic tested condition 5 as a uniqueness mechanism because it reads like one — *"one life, counted twice"*. It is not one. It was a definition of compatibility, doing work it could not do.**

**One thing was proposed in v0.1 and is not being done.** v0.1 §8 recommended a new conformance requirement carrying *"one verified human = one account."* **The ruling makes it a rule each network applies to its own members**, so Foundations §4.1 carries it and the conformance list does not. **The list did not gain a row for it.** *(It gained a different row on 2026-08-27 — **4a**, comparison never conversion — for the reason in §7.)*

---

## 7. What the ruling narrows, and the addition that is not available

**The ruling narrows a published claim, and the narrowing should be stated before somebody else states it.**

**Under the old clause, the bound was offered as a claim about a person's real command of material.** Under the ruling it is a claim about one network's books. **Those are different claims, and the second is weaker.**

### The arithmetic that looks available and is not

**Terms used here.** Two figures are **commensurable** when they are measured in the same unit and may be added or compared directly. They are **incommensurable** when they are not.

P holds an account on Network A (`F` = 4, ρ = 1.2) and one on Network B (`F` = 10, ρ = 1.2). P works 8 hours on the Monday. R holds one account on B and only stays alive.

| | Credit that Monday | Debit-room that Monday, `ρ·C` |
|---|---|---|
| **R** — lives only, on B | 0 + 10 = **10 h** | 1.2 × 10 = **12.0 h** |
| **P on A** | 8 + 4 = **12 h** | 1.2 × 12 = **14.4 h** |
| **P on B** | 8 + 10 = **18 h** | 1.2 × 18 = **21.6 h** |

**The obvious next line is `14.4 + 21.6 = 36.0`, and it is not a permitted line.** An earlier draft of this paper wrote it and called it a factor of 3.0 against R. **That was wrong, and the error is kept on the page, because it is the error this theory is built to refuse.**

> **A's hours and B's hours are not the same unit.**

**Why they are not.** A debit is a vector — kilograms, joules, labour-hours, land-area-years — and it becomes a single figure only when a network **collapses** it through its own weighting model (Foundations §3.2a). **A and B run different models**, so the same physical basket collapses to a different number in each. **Writing `14.4 + 21.6` sets one A-hour equal to one B-hour.** That is an exchange rate between two credit-standards, and Foundations §4.2 forbids it by name:

> *"Converting a balance from one model into another would be an exchange rate between credit-standards — a medium of exchange, which A3 and the circulation-failure analysis (§5.6) forbid."*

**This is now conformance requirement 4a** ([`Aequitas_Conformance_v0.8.md`](../Aequitas_Conformance_v0.8.md)), added because the rule lived only in §4.2's prose and a project paper walked straight past it.

**And no account anywhere holds more than 24 hours in a day.** A recorded 12. B recorded 18. **IC-7 binds each account separately, and neither breached it.** There is no account holding 30, and none holding 36.

**Each network's books are correct and complete about what that network saw.** A saw 8 hours worked and one human alive, and read them through a 4-hour floor. B saw the same two physical facts and read them through a 10-hour floor. **Foundations §4.2 calls this comparison, never conversion.** Neither figure is a translation of the other, and there is nothing to reconcile.

### What is actually left, stated correctly

**P's purchases on B are activity that A cannot see.** That is not a new problem and it does not need a new name. **It is the ordinary coverage case, and Foundations already treats it in two places.**

| The situation | The rule that already covers it | What it does |
|---|---|---|
| A's books do not cover everything P did | **§4.4** — a network publishes a coverage figure saying what proportion of its extent it actually measured | The gap becomes a stated quality of A's own output, and a counterparty discounts thinly covered claims |
| P leaves activity undisclosed to A | **§4.4, conditions 1 and 2** — an estimate for undisclosed activity is computed over the **undisclosed residual**, and it **errs against the estimated party** | The more P leaves dark, the worse A's estimate of P gets, so **supplying evidence always pays** |

> **A person who splits their consumption across two networks is a person leaving activity undisclosed, and the residual rule already points the error against them. Nothing needed to be invented.**

**⚠️ The honest limit of that answer.** **Nobody has measured whether the residual rule is tight enough against a subscriber who splits deliberately rather than incidentally.** It is a **coverage** question, belonging with §4.4–§4.4 and **OP-24 (understatement drift)**. **It is a watch item, not an open blocker, and it is not OP-22b.**

### What may and may not be said in public about the bound

| May be said | May not be said |
|---|---|
| *"Inside one network's books, the spread between the busiest and the least busy account cannot exceed 24 ÷ `F`."* | *"A person's total command of material across all networks is bounded by 24 ÷ `F`."* |
| *"A very hard working life reaches about 1.6×; 2.4× is a wall nobody reaches."* | **Any figure produced by adding or comparing two networks' numbers. There is no such figure.** |

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
> **Except one, and it was ours.** Our §5.5 said the bound held *"across any set of networks compatible enough to interoperate"*, and said compatible networks *"arrive at the same ledger."* **Both halves are struck.** The second contradicted our own §4.2, which says on purpose that each party re-reads the shared physical record through its own model — the 12 and the 18 are both correct and that is intended. **You were right that the ceiling is per-registry. We did not narrow the clause. We removed it.**
>
> **Where your primitive actually goes.** Proving one human holds one account across two registries is not a disclosure question. **It is a precondition of merging.** Two networks merge by agreeing every rule, identity included, so a network doing face-plus-fingerprint-plus-voice cannot merge with one doing an RFID card scan — neither can confirm two pseudonymous accounts are one person, and the merge does not happen. **A merge that cannot identify people is not a merge.**
>
> **And "one verified human, one account" means inside one network.** The place it looks weakest is a notebook on the bottom rung, with identical twins. **The arithmetic refuses it.** IC-7 caps an account at 24 hours of activity per 24 hours. Honest, each twin claims 8 worked + 10 floor = 18, so 36 h/day for the family. Faked, T1 cannot claim 16 + 10 = 26, so the most is 14 + 10 = 24, and T2 still accrues the 10-hour floor because T2 is alive. **34 against 36 — the fraud costs 730 hours a year and buys nothing, because twins sharing a household share the goods either way.**
>
> **One more thing, because I nearly got it wrong in the other direction.** My first draft of this reply said a person with two accounts reaches *"36.0 hours of room against 12.0, a factor of 3.0"*, by adding A's room to B's. **That line is not available and I have cut it.** A's hours and B's hours are not the same unit: a debit is a vector and becomes one figure only when a network collapses it through its own weighting model, so **adding them sets an exchange rate between two credit-standards** — a medium of exchange, which our A3 forbids. **There is no account holding 30 hours and none holding 36.** IC-7 binds each account separately and neither breached it. **We have added the rule to our conformance list rather than leaving it in prose, because prose did not stop me.**
>
> **What is actually left is a coverage question, and it already has a home.** Purchases I make on B are activity A cannot see. **A publishes a coverage figure saying how much of its extent it measured (§4.4), and estimates undisclosed activity over the undisclosed residual, erring against the person (§4.4)** — so leaving activity dark gets worse for you the longer you do it. **What nobody has measured is whether that is tight enough against someone splitting deliberately.** That is a watch item on our coverage work, not a second privacy problem.
>
> **And the honest public form of our headline is per-network.** Inside one network's books the spread cannot exceed 24 ÷ F. **There is no figure for "across all networks", because producing one would need the addition I have just told you we cannot do.**
>
> **OP-22 itself is not closed and I am not claiming it is.** The minimum an auditor must see to check a claim without seeing a history is still unspecified, and the sharpest live form of it is proving a *pledge's* backing across a model boundary — "backed by X hours under weighting model M", in zero knowledge (§4.2).
>
> Paper, with the arithmetic: `00-strategy/open-problems/OP-22_identity_not_disclosure_v0.2.md`. Foundations §4.0, §4.1, §4.8, §5.5.5.

**Also owed to the same thread:** @ballast, @custos and @hearthwarden were answered on the §4.4 residual question at c23596–c23597 and are not waiting on this.

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

**P gains one year of extra room and pays one year of no discretionary purchases.** Essentials are never gated (Foundations §5.5.4), so the year costs P nothing they needed. **A break-even penalty, due only if a merge ever happens, is not a deterrent.**

> **This is the second instance of the lesson recorded in `Shelf_life_and_custody_v0.1.md`: *price it, don't forbid it* is not a universal rule of this system.** It fits where the costly path has a legitimate use and a real price. **Where the price computes to zero, an invariant is the right shape.**

---

## 10. Why the critic did not see the answer

**Because it was not there to see.** This is not another instance of *"already written and unread."* Three reasons:

1. **The conformance list has no uniqueness requirement.** A reader checking the ceiling against the list of things that must be true finds nothing about one human, one account — because there is nothing. **Under the ruling that is correct**, since the rule is applied by each network to its own members.
2. **The old §5.5 condition 5 invited the test.** *"One life, counted twice"* and *"the self-care floor is credited once"* read as a uniqueness mechanism. **It was a definition of compatibility.**
3. **§4.1 stated the rule in six words and §5.5 never cited it.** A whole-document read would not have joined them, because neither section pointed at the other.

**The fix is a cross-reference, not a reading habit.** §4.0 now states the three facts a reader needs before reaching §5.5.5, and §5.5.5 condition 4 states the scope in its own words.

---

## 11. What is owed

| # | Owed | Where it goes | Status |
|---|---|---|---|
| 1 | The author's ruling | §1 above; Foundations CHANGELOG v0.23 | ✅ **Done 2026-08-25** |
| 2 | §5 rewritten to the document standard | Foundations **§4.0–§4.4** | ✅ **Applied in v0.23.** §4.8–§4.8 owed |
| 3 | §5.5's cross-network clause struck | Foundations **§5.5.5** | ✅ **Applied in v0.23.** Zero mentions of *"condition 5"* remain |
| 3a | A conformance item for one-human-one-account | [`Aequitas_Conformance_v0.8.md`](../Aequitas_Conformance_v0.8.md) | ❌ **Not added, deliberately.** The ruling makes it a within-network rule, so Foundations §4.1 carries it. |
| 4 | **The public reply to @cairn-lineage** | §8 above; `07-outreach/` queue item **46** | 🟡 **Written and ranked first. Not yet posted.** |
<!-- struck-ok: a cascade table recording that this wording was struck -->
| 5 | Overview §0's box asserting the bound *"across every network that can trade with every other"* | [`Aequitas_Overview_v0.20.md`](../Aequitas_Overview_v0.20.md) §0 | ✅ **Struck 2026-08-27.** The box shows the 12 h / 18 h case and says plainly that the two figures **cannot be added**. §1 gains the four-lives table and four conditions; §6's table row is corrected. |
| 6 | Objections **OA9 and the OP-22 status row** do not record the ruling | [`Aequitas_Objections_v0.24.md`](../Aequitas_Objections_v0.24.md) | ✅ **Recorded 2026-08-27.** OA9 gains a boxed statement; the status row states it in one line; **C-test 8 re-pointed from OP-22 to OP-14.** |
| 7 | **The conformance list carried no row for *comparison, never conversion*** — an implementation could publish an exchange rate between its credit and a neighbouring network's and still satisfy every row | [`Aequitas_Conformance_v0.8.md`](../Aequitas_Conformance_v0.8.md) | ✅ **Added as requirement 4a, 2026-08-27**, after §7 of this paper made exactly that error. **The number 17 stays retired.** |
| 8 | **Is the residual rule tight enough against a subscriber who splits consumption across networks deliberately?** — §7 above | Coverage: **§4.4, §4.4, OP-24** | 🟡 **Watch item, 2026-08-27. Not a blocker and not OP-22b.** §4.4 already estimates undisclosed activity over the undisclosed residual and errs against the person. **Nobody has measured whether that is tight enough against deliberate splitting.** |
| 9 | **Two axioms were cited by no conformance row at all** — **A7** (universal accounting), and **A4** with §3.3 (retroactive re-weighting) | [`Aequitas_Conformance_v0.8.md`](../Aequitas_Conformance_v0.8.md) §4.8 | ✅ **Ruled in as requirements 17a and 17b, 2026-08-27.** An implementation could have accounted only for its own subscribers, or frozen its weighting model forever, and still passed every row. **Every axiom is now cited by at least one row.** |

---

*End of v0.2.*
