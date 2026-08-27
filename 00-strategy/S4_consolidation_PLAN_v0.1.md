# Plan — consolidate Foundations §4, §5 and §6 into one section

> **Version:** 0.1 · **Date:** 2026-08-27 · **Status:** ✅ **COMPLETE. All five chunks done.**
>
> | Chunk | Result |
> |---|---|
> | **1 — §4.0 to §4.3** | ✅ Old §4, §5.0, §5.1 and §6.4b absorbed. **24,408 → 18,232 bytes**, and the new text adds a preamble, a duties map and a terms table that did not exist. |
> | **2 — §4.4** | ✅ Old §5 header and §5.1a–§5.1d absorbed. **23,347 → 13,787 bytes.** |
> | **3 — §4.5, §4.6** | ✅ Old §6 entire absorbed. **50,293 → 20,696 bytes.** |
> | **4 — §4.7, §4.8** | ✅ What was left of §5 absorbed. **39,683 → 19,623 bytes.** Three new wiki pages created. |
> | **5 — renumber and sweep** | ✅ §7 → §5, §8 → §6, contents rebuilt, **73 files swept**, CHANGELOG carries the old-to-new map. |
>
> **Result: 133,029 bytes of §4+§5+§6 became a 59,000-byte §4. The document went from 248,740 to 179,711 bytes.**
>
> ### ⚠️ One mistake worth recording, because it nearly shipped
>
> **The first sweep used a chain of `str.replace` calls.** Old §7.5 was mapped to §5.5, **and a later pair in the same chain then mapped that §5.5 to §4.8** — conflating the basic-needs floor with the money boundary, across 73 files.
>
> **It was caught by reading the output**, not by the script. **Recovery came from `07-outreach/archive/`, which is a git mirror of the project's public folders and had not been synced since before the restructure**, so a clean pre-restructure copy of every file existed. 126 files were restored and the sweep was redone with **sentinel substitution**, which writes a placeholder for each match and resolves placeholders only at the end, so nothing is ever rewritten twice.
>
> **The lesson: a rename map whose outputs overlap its inputs cannot be applied by sequential replacement.** And **the archive mirror is a usable undo for anything under the public folders.**
>
> **Author instruction, 2026-08-27:** *"§5 starts by saying 'this section describes work that a trust network does.' §4 is about verification, which is the job of a trust network. It lacks a preamble and just launches into a list of levels without context. §6 describes another duty: tracking and awarding pledges. Consolidate 4, 5 and 6 into a single section 4, and relabel 7 to 5. The consolidation needs to make them a lot smaller — Foundations isn't the place for exhaustive evidence, examples, edge-cases and sim results. Broad strokes kept, details moved to wiki, research or simulation, and linked."*

---

## 1. What is actually there

| | Lines | Size |
|---|---|---|
| §4 Verification | 730–838 | ~14 KB |
| §5 Identity, Privacy, Onboarding | 839–1575 | ~78 KB |
| §6 One Credit, Three Feedback Channels | 1576–1975 | ~41 KB |
| **Total** | | **133 KB** |
| The whole document | | **249 KB** |

**The three sections are 53% of Foundations.**

**The author's reading is right, and the evidence is in the section titles.** §4.0 opens *"This section describes work that a trust network does."* **§4 and §6 describe the same thing and never say so.** §4 is verification, which is a network's job. §6 ends in pledges and signals, which a network tracks and awards. **Three sections, one subject, one of them announcing it.**

---

## 2. ⏸ THE PROPOSED STRUCTURE — approve or change this before anything is written

**One section, organised by what a trust network actually does, in the order it does it.**

| New | Title | Absorbs |
|---|---|---|
| **4.0** | What a trust network is, and what this section covers | §4.0 (already written as this preamble) |
| **4.1** | It gives each person one account | §4.1 |
| **4.2** | It decides what counts as evidence, and publishes it | §4.2 incl. the new published-rule subsection |
| **4.3** | It checks a claim, on a ladder of four rungs | §4 entire |
| **4.4** | It estimates what it cannot see | §4.4, §4.4, §4.4, §4.4 |
| **4.5** | It credits work | §6, §4.5, §4.5, §4.5, §4.5, §4.5 |
| **4.6** | It carries what people want made | §4.6, §4.6, §4.6, §4.6, §4.6 |
| **4.7** | It publishes its own workings, and settles disputes | §4.7, §4.7, §4.7, §4.7 |
| **4.8** | It takes people in, it merges, and it can end | §4.8, §4.8, §4.8, §4.8 |

**Then §7 Consequences → §5, and §8 Where the rest of the project lives → §6.**

> **Why this order.** A network must know **who** someone is before it can credit them, must know **what counts as evidence** before it can check anything, and must **check** before it can **estimate the rest**. Crediting and demand follow. Publication and disputes are how it is held to account. Entry, merging and ending are its life cycle.

**One thing this order fixes on its own.** §4's four rungs currently arrive with no statement of what is being verified or why. **Under 4.2 → 4.3, the evidence rule comes first and the ladder becomes "how hard you check", which is what it always was.**

---

## 3. The size target, and the rule that governs every cut

**Target: 133 KB → about 40 KB.** A 70% cut.

> **THE CUT RULE. Every rule, every principle and every obligation stays in Foundations, stated in a full sentence. What leaves is the evidence for it: long worked examples, edge cases, simulation figures, historical argument, and the record of what earlier versions said.**

**Every moved item leaves a link at the point it left.** A reader of Foundations alone must still learn **what is true**. They go to the wiki only for **why we believe it** and **what it looks like worked out**.

**What always stays, whatever the size cost:**

- The statement of every rule, in full sentences.
- **One** worked example with digits where a mechanism needs one — the project's own standard says a mechanism without numbers is not explained. **The shortest one that works, not the fullest.**
- Every honest limit, every named open problem, every *"this is not solved"*.
- Anything a conformance requirement cites.

**What moves out, always:**

- Second and third worked examples of the same rule.
- Simulation outputs, run names, parameter tables, self-test counts.
- The record of what a superseded version said. **That is what the CHANGELOG is for**, and it is already there.
- Historical and comparative argument — Braudel, Ithaca HOURS, the GDPR reading, Post Office Horizon.
- Objection-and-answer passages. **Those belong in the Objections register**, which §8 already says is the ranked list.

---

## 4. Where the detail goes

**Prefer an existing wiki page. 41 exist and most destinations are already among them.**

| Detail leaving Foundations | Destination | Exists? |
|---|---|---|
| The four rungs, their costs, the 1,000-sack table | [`01-wiki/verification-ladder.md`](../01-wiki/verification-ladder.md) | ✅ |
| Independence vs expressiveness, the balanced-lie table | `01-wiki/verification-ladder.md` | ✅ |
| `(N − Y) ÷ Z`, the four alignment rows, the valley-wheat worked case | [`01-wiki/estimation-engine.md`](../01-wiki/estimation-engine.md) | ✅ |
| Coverage figures, the closure-witness table, floor/ceiling/not identified | [`01-wiki/statistical-coverage.md`](../01-wiki/statistical-coverage.md) | ✅ |
| The lifetime back-trace arithmetic | [`01-wiki/onboarding-incentive.md`](../01-wiki/onboarding-incentive.md) | ✅ |
| Pledge mechanics, the contingent reserve, the radicchio and street-art examples | [`01-wiki/pledge-and-signal.md`](../01-wiki/pledge-and-signal.md) | ✅ |
| The barn-is-not-in-the-beef box, the holding-time waterfall | [`01-wiki/property-debit.md`](../01-wiki/property-debit.md) | ✅ |
| Front-loading, the three instances table | [`01-wiki/education-as-credited-work.md`](../01-wiki/education-as-credited-work.md) | ✅ |
| Federation, merging, laboratories-not-banks, the monopoly argument | [`01-wiki/ledger-ecosystem.md`](../01-wiki/ledger-ecosystem.md) | ✅ |
| Privacy as a network dial, the three residues | **`01-wiki/privacy-is-a-network-choice.md`** | 🆕 |
| Dispute resolution, the four-class table, what correction looks like | **`01-wiki/dispute-resolution.md`** | 🆕 |
| No exit, death, the GDPR reading | **`01-wiki/permanence-and-death.md`** | 🆕 |
| The money boundary, templates, extraction, repeat shells | Already in [`00-strategy/OP-27_parallel_implementation.md`](OP-27_parallel_implementation.md) | ✅ |
| The demand-lever argument, Braudel and DeLanda | Already in [`00-strategy/OP-9_calculation_reply.md`](OP-9_calculation_reply.md) | ✅ |
| Twins, one-person-two-networks, the disparity arithmetic | Already in [`00-strategy/OP-22_identity_not_disclosure_v0.2.md`](OP-22_identity_not_disclosure_v0.2.md) | ✅ |

**Three new wiki pages. Everything else has a home already.**

---

## 5. The jargon pass

**Run over every sentence that survives.** The author's standing ban list, plus what this document has accumulated:

**Banned unless defined in the same sentence:** *residue · load-bearing · dissolve · surface (as a noun) · unravel · priced · orthogonal · instantiate · downstream · upstream · non-trivial · elegant · clean (of an argument).*

**Also banned here, because they are ours and a stranger does not have them:** *the ladder* used alone · *rung* without saying rung of what · *closure witness* without its definition beside it · *the floor* without saying what the floor is · *monotonicity* · *the residual* used as a bare noun · *comparison never conversion* without the sentence that explains it · *front-loading* without its definition · *the waterfall* · *hand-off gates realization* · *IC-7* and every other IC number without saying what it does.

**And the constructions:** no reversals (*"that is not a defect, it is the mechanism working"*), **one em-dash per sentence at most**, no sentence with three or more clauses, no paragraph where a list would do.

**The test for every paragraph that survives:** *could a competent stranger read this once and know what to do?*

---

## 6. Chunks — each finishes in one sitting

| # | Chunk | Done when |
|---|---|---|
| **1** | **4.0, 4.1, 4.2, 4.3** — who, what counts as evidence, and how hard you check | The four rungs arrive with a preamble; `verification-ladder.md` holds the cost table and the balanced-lie table |
| **2** | **4.4** — estimating what it cannot see | The three landing states and the alignment rule stated in Foundations; `estimation-engine.md` and `statistical-coverage.md` hold the worked cases |
| **3** | **4.5, 4.6** — crediting work, and carrying demand | The barn box and the pledge examples are in the wiki; the rules are in Foundations |
| **4** | **4.7, 4.8** — publishing, disputes, entry, merging, ending | Three new wiki pages exist and are linked |
| **5** | **Renumber and sweep** — §7 → §5, §8 → §6, every cross-reference in every file repaired, CHANGELOG written, archive synced | `check_agent_env.ps1` green and zero dangling section references anywhere |

> **Chunk 5 is not optional and is not small.** **Every document in the project cites Foundations by section number**, and so does the outreach agent's brief, the conformance list, the objections register and the wiki. **A renumber with a missed reference is worse than no renumber.**

---

## 7. Risks

**🔴 The largest one, and it is the reason this plan has a cut rule.** The project's hardest standing rule is *read Foundations whole, and keep it in context*, and it exists because **three times in one session a proposal was retracted after an unread premise was found**. **Moving mechanisms into the wiki puts premises where a whole-document read will not find them.**

**The guard is the cut rule in §3: the rule stays, only its evidence leaves.** A reader of Foundations alone still meets every premise. **If a chunk cannot keep a rule in Foundations and still hit the size target, the size target loses.**

**🟡 Section numbers are cited from outside the project.** The outreach agent has quoted §4.4, §4.4, §5.5.5 and others in public, on a board that keeps them permanently. **The CHANGELOG must carry an old-to-new map**, so a reader following an old citation lands somewhere.

**🟡 Some content has already moved once.** §4.8 is a summary of `OP-27_parallel_implementation.md`; §4.6 is a summary of `OP-9_calculation_reply.md`. **Check the paper before cutting, so the cut does not remove something the paper never carried.**

---

## 8. Version

**This is a restructure, so the convention says a major bump: v0.27 → v1.0.**

> **⚠️ Flagged for the author.** The project's three-month goal is a *different* document called `Aequitas_System_v1.0.md`. **Two v1.0s in one folder will be confusing.** The alternative is v0.28 with the CHANGELOG calling it a restructure. **Author's call; v0.28 is the safer default and is what this plan assumes unless told otherwise.**
