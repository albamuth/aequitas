# 00-strategy — what is in here, and what to read first

**This folder holds the theory.** Nothing here is code, and nothing here is a plan for code.

**How it is laid out.**

| Where | What is in it |
|---|---|
| Here, at the top | **The core documents** — `Aequitas_*.md`, each with a companion `_CHANGELOG.md` — plus `GLOSSARY.md` and this page |
| [`open-problems/`](open-problems/) | **One paper per open problem.** The `OP-*` files |
| [`papers/`](papers/) | **Settled working papers the core documents still cite by name** |

**A finished plan is not a paper.** Once a plan's work has landed in the core documents, the plan goes to `../99-archive/`.

**If you read one thing, read `Aequitas_Foundations_v*.md`, and read all of it.** The reason is at the bottom of this page and it is not a style preference.

---

## Start here — pick the row that matches you

| You are | Read, in this order | Cost |
|---|---|---|
| **An agent starting a work session** | **Foundations, whole**, then `../NEXT.md` | ~200 KB. Budget for it. |
| **A person new to the project** | `Aequitas_Overview_v*.md`, then `Aequitas_Strategy_v*.md` | ~85 KB |
| **Answering an objection someone raised** | `Aequitas_Objections_v*.md` **first** | ~100 KB |
| **Building an implementation** | `Aequitas_Conformance_v*.md`, then the Foundations sections its rows point at | ~10 KB, plus what you follow |
| **Answering ONE question, and not proposing anything** | **`Aequitas_Question_Index.md` first.** Keyed by the question, not by the section. **Three verdicts: REFUSED, ANSWERED, OPEN** | ~17 KB |
| **Stuck on an abbreviation** | `GLOSSARY.md` | look-up only |
| **Tracing when something changed** | the matching `*_CHANGELOG.md` | look-up only |

> **⚠️ Never hard-code a version number.** Always take the **highest** version of a file by globbing `Aequitas_Foundations_v*.md`. This project's own instructions once pointed at `v0.4` while the file had reached `v0.17`. **A hard-coded pointer in the rule that forbids hard-coded pointers.** Do not repeat it.

---

## The five core documents

These are versioned, and they move **in lockstep**. When one is bumped, every document it touches is bumped with it. Old versions go to `../99-archive/` and are never deleted.

| File | Holds | Size |
|---|---|---|
| **`Aequitas_Foundations_v*.md`** | **The system itself.** The eight axioms (§1), the ledger model (§3), verification (§4), identity and coverage (§5), credit and pledges (§6), and consequences (§7). **It ends at §8, which is a pointer table.** Truncated on 2026-08-25: the conformance list, the open problems and the adoption reading moved to the three files below. **Everything else in this folder is downstream of this file.** | ~190 KB |
| **`Aequitas_Conformance_v*.md`** | **What must be true for an implementation to *be* Aequitas.** Numbered requirements, each pointing back at the section of Foundations that argues for it. **It also carries the arithmetic constraints IC-1 … IC-12.** **§4 records what is deliberately *not* a requirement, and why.** **Audience: implementers.** Not a schema, not a protocol, not a product. | ~8 KB |
| **`Aequitas_Objections_v*.md`** | **The objections register.** Every serious attack on the theory, who made it, which axiom it hits, and its status. **Part B is the answered ones, and it is not an archive** — it is the argument sheet, and every item will be raised again by someone who has not read it. | ~100 KB |
| **`Aequitas_Overview_v*.md`** | **The plain-language version.** No economics background needed. Where it and Foundations differ, **Foundations wins.** | ~65 KB |
| **`Aequitas_Strategy_v*.md`** | **The roadmap.** What is being built, in what order, and why. | ~21 KB |

---

## The changelogs

Each core document has a companion `_CHANGELOG.md`. **All version history lives there, and none of it lives in the document.**

The documents used to open with a wall of `Supersedes` and `Prior (v0.18)` blocks — history in the exact place a reader starts. That was moved out on 2026-08-24. **A core document now opens on its contents.**

`Aequitas_Foundations_CHANGELOG.md` · `Aequitas_Objections_CHANGELOG.md` · `Aequitas_Conformance_CHANGELOG.md` · `Aequitas_Overview_CHANGELOG.md` · `Aequitas_Strategy_CHANGELOG.md`

**Read a changelog only when you need to know *when* or *why* something changed.** Never read one to learn what the system currently says.

---

## `open-problems/` — one paper per problem

These are the long-form workings behind a ruling. **Each one is already summarised in Foundations and in the register.** Open a paper only when the summary is not enough.

Most are closed. The status line at the top of each file says which.

| Paper | The problem | State |
|---|---|---|
| `OP-9_calculation_reply.md` | Can an economy without money-prices allocate rationally? The Mises / Hayek attack — **the first objection any economist makes.** | 🟢 Written up |
| `OP-16_authorization_stress_test.md` | Should credit-earners authorise which future work counts? Four versions, all tested. | ❌ Rejected |
| `OP-17_coproduct_allocation.md` | One process, several products, one pool of cost. How does it divide? | ✅ Closed |
| `OP-18_labour_and_team_credit.md` | Nine people build a bridge. Who is credited what? | ✅ Closed |
| `OP-23_capital_and_pollution.md` | Who carries the cost of a building or a machine? And why pollution never moves to a buyer. | ✅ Closed |
| `OP-26_coverage_and_closure.md` | **Arithmetic over a record proves the record is consistent. It cannot prove the record covers the world.** The first objection raised from outside the project. | 🟠 Largely answered |
| `OP-26_declare_dont_allocate_stress_test.md` | A proposal to declare the unrecorded gap rather than charge it to anyone. | ❌ Not adopted — it was already the rule |
| `OP-27_parallel_implementation.md` | How does a person use Aequitas while everyone around them still uses money? | ✅ Ruled and tested |

---

## `papers/` — settled working papers

**C2 is the trust network**: the body that does the tallying, holds what is private, and publishes its methods. Aequitas states principles; a trust network is who executes them.

| File | Holds |
|---|---|
| `C2_TrustNetworks_v0.1.md` | Every settled ruling about trust networks, gathered in one place. They were decided across a dozen scattered sections. |
| `Onboarding_the_wealthy_v0.1.md` | What happens when a very rich person joins? 🟡 Ruled, not yet tested. |
| `Shelf_life_and_custody_v0.1.md` | When does holding a thing stop being your responsibility? 🟡 Two parts confirmed, one new. |
| `C2_information_capture.md` | Whoever tallies, holds. Does the network become the thing this project exists to dissolve? **Read §11 first** — sections 1–10 are kept unedited because the mistake in them is instructive. |

---

## The rest

| File | Holds |
|---|---|
| `GLOSSARY.md` | **Every abbreviation, in one place.** OP-#, C#, IC-#, A#, P#, and the section references. An outside reader named abbreviation density as the single biggest barrier to reading this project. **If a term is unfamiliar, it is in here.** |
| `Aequitas_Question_Index.md` | **Every recurring question, keyed by the question.** Three tables: **REFUSED** (an axiom already rules it out, say which), **ANSWERED** (do not re-derive it), **OPEN** (say so, do not guess). **GLOSSARY resolves abbreviations; this resolves questions.** Built because five times the answer or the refutation was already written and unread |
| `Aequitas_Simulation_Roadmap_v0.2.md` | What the simulation programme is for and what it builds next. The code itself is in `../06-simulation/`, which has its own landing page. |

---

## Conventions in this folder

1. **`Name_vX.Y.md`.** Bump the minor number for an edit, the major number for a restructure.
2. **Never delete a superseded document.** It moves to `../99-archive/`. The point of versioning is that a reader can compare the old against the new.
3. **Lockstep bumps.** If a change touches three documents, all three are bumped. A header pointing at an archived version is the most common defect, so re-thread every pointer after a bump.
4. **History goes in the changelog, never in the margins of the text.** No `(new in v0.19)` notes in the body.
5. **Every named source gets a link.** A citation without a link is incomplete. If a link cannot be verified, cite it and mark it unverified rather than inventing one.

---

## ⚠️ Why Foundations must be read whole, and not searched

**A search finds a mechanism when you already know its name. It does not find the premise you are about to contradict.**

**Seven times now, the answer — or the refutation — was already written down and unread:**

| What was treated as an open problem | Where the answer already was |
|---|---|
| Local currencies fail because credit pools at sinks | **A3** — credit never moves, so it cannot pool |
| How does a joint process divide its cost? | **A2** — the yardstick is time, so no carrier quantity is needed |
| What proves a record covers the world? | **§4.4** — the closure witness, written and never wired up |
| Can a person hold their own records? | **§4.7** |
| Can the system collect less data? | **A7** — no. Universal accounting requires the records to be complete. |
| Who carries the unrecorded gap? | **§4.4** — nobody, until the causer joins |
| Six critiques conceded in public in one week | **§4.4, §4.4, §4.4, §3.3a, OP-24** |

**You cannot know which section to search for until you have read them all.** That is the whole reason for the rule. The cost is about 200 KB and it is accepted.
