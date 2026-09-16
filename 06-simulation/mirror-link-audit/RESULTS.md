# How many published links point at something unpublished

> **Version:** 0.1
> **Date:** 2026-09-16

> **Run: 2026-09-12.** Answers `sr-20260907-enumerate-every-outbound-relative-link-in-th`, filed 2026-09-07 from @amber's finding `obj-20260907-amber-dead-links-to-unpublished-archive`.
> **Code:** [`mirror_link_audit.py`](mirror_link_audit.py) · **Transcript:** [`RUN.txt`](RUN.txt)
> **7 self-tests, each able to fail. All pass.**

---

## The question

> *"Enumerate every outbound relative link in the PUBLIC core documents and count how many resolve to a path that is not in `latest-mirror`. Report the count and the denominator, not a list of instances."*

**@amber asked for a rate rather than a chore list, and they were right to.** A list of broken links is something to fix once. **A rate can be compared against a later run, or against anybody else's repository.**

---

## The answer

| | |
|---|--:|
| Published markdown files | **176** |
| Relative links in them | **1,270** ← the denominator |
| **Links a reader cannot follow** | **18** |
| **Rate** | **1.42%** |

> **In plain words: about one link in seventy, in the documents an outside critic actually reads, leads nowhere.**

---

## Why `bin/consistency.py` does not catch these

**It resolves links against the working tree, and every one of these 18 targets exists on the author's disk.** That is the right check for an author and it passes: *1,566 links, 0 broken.*

**A reader on GitHub sees only `07-outreach/latest-mirror/`.** A link whose target exists locally and is absent from the mirror **resolves for the author and 404s for everybody else.**

> **Two different questions, and only one of them is about the reader.**

---

## Where they are

| File | Count |
|---|--:|
| **`00-strategy/Aequitas_Foundations.md`** | **4** |
| `00-strategy/Aequitas_Foundations_DISTILLED.md` | 4 *(generated from the above — the same four)* |
| `06-simulation/median-lifestyle/median_lifestyle_METHOD.md` | 2 |
| `06-simulation/median-lifestyle/RESULTS.md` | 2 |
| Six other files, one each | 6 |

## What they point at, and the three causes

| Target | Times | Why it fails |
|---|--:|---|
| `../03-journal/` · `../04-use-cases/` · `../05-marketing/` · `../07-outreach/` | 8 | **Foundations §6's directory table.** These folders are not in the mirror |
| `99-superseded/` and files inside it | 7 | **Deliberately unpublished.** The project's own naming rule keeps superseded material out |
| `../bin/consistency.py`, `chain_resolution.csv`, `method_spread.csv` | 3 | Tooling and data that the mirror does not carry |

**In plain words: none of these is a typo. Every one is a link into a folder the project has decided not to publish.**

---

## 🔴 The four in Foundations are the ones that matter

**Foundations §6 is titled *Where the rest of the project lives*, and it is a table of links.** Four of its rows point at folders no reader can open:

| Row | Target |
|---|---|
| *A dated development log* | `../03-journal/` |
| *End-user scenarios* | `../04-use-cases/` |
| *Public-facing material* | `../05-marketing/` |
| *The outreach agent …* | `../07-outreach/` |

*(Each row is a live markdown link in Foundations. The targets are written here as plain code spans on purpose — reproducing them as links would make this file fail the same check it is reporting on, which it did on the first draft.)*

**The same section already handles this correctly one row further down**, for `99-archive/`:

> *"Held locally and not published, **so there is no link to follow**. Nothing in it is current."*

> **So the document already knows the rule and applies it to one folder out of five.** The repair is to do to those four rows what was done to that one: **name the folder in plain text and drop the link.**

---

## ⚠️ What this does not show

**1. It counts links, not usefulness.** A link that resolves can still point at the wrong thing. **This measures reachability and nothing else.**

**2. Anchors are stripped, not checked.** `foo.md#some-section` is counted as resolvable when `foo.md` exists, even if that heading does not. **`bin/consistency.py` check [5] covers section references separately** and reports 1,357 of them all resolving.

**3. Only markdown is scanned.** A link inside a `.py` docstring or a `.csv` header is not counted.

**4. The rate is of this repository on this date.** It moves every time the mirror is synced, and it is only meaningful beside the denominator.

---

## What the number is for

**A rate lets the next run say whether this got better or worse.** The figure to beat is **18 / 1,270 = 1.42%**, and **the four in Foundations are worth more than the other fourteen put together**, because Foundations is the document an outside critic is sent to first.

**Credit: @amber, `obj-20260907-amber-dead-links-to-unpublished-archive`.** They asked for the denominator, which is the half that makes it a measurement.
