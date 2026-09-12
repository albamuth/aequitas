# Can a reader get from the eight axioms to every conformance requirement?

> **Run: 2026-09-12.** Answers `sr-20260908-walk-the-reachability-graph-of-foundations-s`, filed 2026-09-08 from @amber's finding `obj-20260908-amber-conformance-row-unreachable` (c47758 on #1605).
> **Code:** [`axiom_reachability.py`](axiom_reachability.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **10 self-tests, each able to fail. All pass.**

---

## The finding being tested

**@amber named a state our documents had no word for:**

> *"Row 10e is core, invariant under A8, and unreachable from section 1 by any pointer — **a row never linked, not a row never written**, which is why every completeness check that counts rows passes it."*

**Their worked case: A8's *"where this is worked out"* line named §2.6, §2.3, §4.0 and §4.7, and did not name the conformance list** — which A8's own second clause makes invariant.

---

## The answer, in three layers, because one number would mislead

### 1. The narrow defect @amber named is fixed, and the walk confirms it

**A8's pointer line now reads:**

> *"[`Aequitas_Conformance_v0.16.md`](...) for the requirements this axiom makes invariant, **every one of which is reachable from here and from nowhere else in §1**."*

| | v0.42, when @amber looked | v0.44, measured today |
|---|---|---|
| Axioms carrying a pointer line | 8/8 | **8/8** |
| **A8's line names the conformance list** | **No** | **Yes** |

> **In plain words: the repair landed, and this is the first time anything has checked it rather than asserted it.**

### 2. Under the stricter reading, 34 of 44 rows still have no inbound edge

**The strict test: is each row NAMED, by number, in a section a reader reaches by following pointers from an axiom?**

| | |
|---|--:|
| Foundations sections reached from the axioms | **40 / 49** |
| **Conformance rows named from a reached section** | **10 / 44** |

**The 34 with no inbound edge:**

```
1  2  2a  2b  2c  2d  3  3a  4  4b  5  6  7a  9  10  10a  10d  10e  10f
10g  10h  11  12  12a  12b  12c  14  14d  15  16  16b  16d  17a  17b
```

**Row 10e — @amber's own example — is in that list.**

### 3. But one edge covers all 44 for a reader who clicks

**A8 links the conformance document itself.** So a reader following A8 arrives at a file containing every row. **They are all one click away, and none of them is hidden.**

> **So which layer is true depends on what "reachable" is asked to mean, and the two readings differ by 34 rows.**
>
> | Reading | Result |
> |---|--:|
> | *The conformance list is reachable from §1* | **True.** A8 names it |
> | *Each requirement is named where it is worked out* | **10 of 44** |

**@amber's sentence is the second reading** — *"target set: the conformance rows A8 locks."* **The repair delivered the first.**

---

## The ten rows that are reached, and what they have in common

| Row | Named in |
|---|---|
| 7 | §3.4a — closure checks for a missing mix or split |
| 8 | §5.5.5 — IC-7, the 24-hour cap |
| 10b | §3.4a — the union rule, and the 7.00× inflation a naive sum gives |
| 10c | §3.4a — children's shares add back to the parent |
| 13 | §5.5.3 — the two zero rows are floors, not values |
| 14a | §4.4 — `N` and `Y` must be scope-aligned before subtracting |
| 14b | §4.4 — a check comparing a thing to itself finds no hole |
| 16a, 16c | §3.3a — the five cost-constant audit properties |
| 4a | §4.2 — comparison, never conversion |

**Every one is a row Foundations argues for in its own body, and names while arguing.** The other 34 are stated in the conformance document and nowhere else.

---

## ⚠️ @amber's own objection to this method, which they raised before we ran it

> *"The path a stranger would walk is the path WE choose when we write the recruiting ask, so **the denominator of a reachability sweep is set by us**."*

**They are right, and their partial repair is what this run used: declare the entry point and the edge type BEFORE running, not after.**

| Declared in advance | |
|---|---|
| **Entry point** | The eight axioms, A1 to A8 |
| **Edge type 1** | Each axiom's italic *"Where this is worked out"* line |
| **Edge type 2** | Every `§N` reference in the body of a section already reached, followed transitively |
| **Target set** | Every numbered row of the current conformance document |

**This does not close their objection. It makes the choosing visible**, which is all they claimed for it.

---

## ⚠️ Three more things this does not show

**1. Nine Foundations sections are unreached, and three of those are an artefact.** `4`, `5` and `6` are top-level container headings that nothing references as a bare number — the document says §4.5, never §4. **The six real ones are §3.4, §3.7, §5.4, §5.5.2, §5.5.4 and §5.5.8.** §3.7 is land and buildings, a whole mechanism no axiom pointer reaches.

**2. "Reached" is not "argued for".** The test asks whether a reader arrives somewhere that names the row. It does not ask whether that section justifies it. **This is deliberately the weak test**, because it is the test A8's own sentence makes.

**3. A `§` reference is the only edge counted.** A section that discusses another by name, without the section sign, contributes no edge. **So the true reachable set is somewhat larger than 40 of 49, and the direction of that error is known: this run under-counts reachability.**

---

## What this leaves for the author

**Two readings of A8's sentence are live and they differ by 34 rows.** The choice is between:

- **Letting A8's sentence mean the document** — true today, and the sentence may want narrowing so it does not seem to claim more.
- **Making each row reachable** — which means Foundations naming rows it does not currently discuss, and that is a much larger edit than the v0.43 repair was.

> **Nothing here says which. It says the two are not the same and the gap is 34.**

**Credit: @amber, c47758.** They named the state, supplied the check, and stated the objection to their own check before anybody else could.
