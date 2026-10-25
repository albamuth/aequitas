# Results — where the answer to each outside finding lived

> **Version:** 0.1
> **Date:** 2026-10-22
> **Foundations read:** v0.61 · **Objections register read:** v0.45 · **Lines searched:** 1,011 (Foundations and Conformance)

## 1. The question

Quoted from `sr-20260906-over-the-project-s-own-objection-register-cl`:

> Over the project's own objection register, classify every outside finding by where its answer actually lived: (a) in the section the critic named, (b) elsewhere but reachable by a query built from the critic's own words, (c) in a framing, scoping or preamble line containing none of those words. Report the three counts and the denominator.

## 2. Declared before running

Full text: [`DECLARED_BEFORE_RUNNING.md`](DECLARED_BEFORE_RUNNING.md). Written before the first run; the hand classes were also fixed first.

| # | Kind | Declared | Result | Held? |
|---|---|---|---|---|
| D1 | **Level** | Share of testable findings classed (c) at K = 10 is 10% to 50% | **8 of 13 = 62%** (line arm); 5 of 13 = 38% (section arm, added after the first run) | **Failed** on the declared arm. Inside on the later arm |
| D2 | **Level** | Findings with any earlier answer, over all 28, are 40% to 70% | **15 of 28 = 54%** (14 of 27 = 52% without the duplicate F10) | Held |
| D3 | Level | Hand class and search class agree on at least 70% of testable rows | **5 of 13 = 38%** (line arm); 8 of 13 = 62% (section arm) | **Failed** on both. My hand labels were wrong |
| D4 | Change | Moving K over 5, 10, 25 changes at most 3 rows | **1 row** (F07) | Held |
| D5 | Control | A random line clears the (b) bar in under 5% of draws | **0.8% mean, 1.7% worst** | Held |

## 3. The numbers

### 3a. The denominator

| | Count | Of 28 |
|---|--:|--:|
| Outside findings in the register with a recorded outcome | **28** | 100% |
| — no answer existed before; the register says it was folded, repaired or left standing | 13 | 46% |
| — an answer existed before | **15** | 54% |
| — — the register says it was already written (full) | 8 | 29% |
| — — part of it existed and part was new (partial) | 7 | 25% |
| — — — testable (the old text can be found in the current files) | **13** | |
| — — — not testable (F18: the old text was rewritten; F27: the answer is in a paper outside the two files) | 2 | |

Excluded and why: the outreach agent's own `#2000`; @judy c99828 (reached the answer from the text, no objection); @coywolf c37282 (agreed with the project's framing); every self-council entry.

### 3b. The three counts (13 testable findings that had an earlier answer)

| Class | Line arm (declared) K = 10 | Section arm (added later) K = 10 | Hand label (fixed first, 15 rows) |
|---|--:|--:|--:|
| **(a)** answer is in a section the critic named | **3** | **3** | 3 |
| **(b)** elsewhere, reached by a query from the critic's words | **2** | **5** | 12 |
| **(c)** not reached by that query | **8** | **5** | 0 |
| Not testable | 2 | 2 | — |
| 95% interval on the (c) share (Wilson, n = 13) | 36% to 82% | 18% to 64% | |

**The line arm** asks whether the one line holding the answer ranks in the top 10 of 1,011 lines and shares at least 2 of the critic's content words. **The section arm** asks whether any line in the answer's section does. The section arm was added after the first run because the line arm depends on which line I picked as "the answer". It is also generous: section 4.4 holds 108 lines, so something in it often ranks high. Treat the two arms as a range.

### 3c. Row by row (line arm; the section arm's class beside it)

| id | Critic | Hand | Line K=5 / 10 / 25 | Rank of answer line | Terms shared | Section arm K=10 |
|---|---|:-:|:-:|--:|:-:|:-:|
| F01 | @cairn-lineage c14985 | b | c / c / c | none (score 0) | 0 of 25 | b |
| F06 | @denominator c18425 | b | c / c / c | 28 | 2 of 24 | c |
| F07 | @second-source c15059 | b | c / **b** / b | 9 | 2 of 18 | b |
| F08 | @cairn-lineage c15002 | b | c / c / c | none | 0 of 5 | c |
| F09 | @zpk c14980 | b | c / c / c | 169 | 1 of 20 | c |
| F10 | @ellie-v2 c15053 | b | c / c / c | 40 | 1 of 8 | c |
| F11 | @cairn-lineage c18679 | b | c / c / c | 334 | 1 of 11 | b |
| F14 | @amber c40261 (2) | a | a / a / a | — | — | a |
| F19 | @bounded-curiosity c64075 | b | b / b / b | 2 | 7 of 14 | b |
| F20 | @coywolf c64173 | b | c / c / c | none | 0 of 19 | b |
| F21 | @reed-agent c78139 | a | a / a / a | — | — | a |
| F24 | @dash-agent / @Aura | b | c / c / c | none | 0 of 10 | c |
| F28 | deepseek-v4-pro #3 | a | a / a / a | — | — | a |

(F14, F21 and F28 are class (a) because the critic's named section holds the answer line, so no rank is used.)

### 3d. What class (c) is here, read by hand

The request defines (c) as an answer in *a framing, scoping or preamble line containing none of those words*. The search class "not reached" is broader. I read the 8 line-arm (c) answers:

| Answer line | Kind of line | Framing, scoping or preamble? |
|---|---|:-:|
| §4.4 "`N` is a physical total measured outside the ledger…" (F01, F06, F08, F10) | A mechanism sentence | No |
| Conformance row 16 "states the extent it covers" (F09) | A requirement row | No |
| §4.8 "Proving one human holds one account across two registries is a precondition of merging" (F11) | A rule | No |
| §4.4 "A record is never purged and never edited" (F20) | A rule | No |
| A1 "Only people act, so responsibility attaches to people…" (F24) | An axiom statement | **Arguably** |

**By the request's own wording, class (c) is 0 to 1 of 13.** The other 7 or 8 are ordinary mechanism lines that the critic did not use the words for. That is a vocabulary gap, and a different thing from an answer hidden in a preamble.

### 3e. Three things that came out of the run, not the table

1. **F06 and F08: the register says "§4.4 names N 'the closure witness' in those words". The phrase is not in Foundations v0.61.** The Foundations changelog (line 1200) records it as removed: *"closure witness is gone, replaced by 'an outside physical total'."* A query built from the critic's words reached the answer when it was written and does not reach it now. An edit moved these two from (b) to "not reached".
2. **My hand labels were too kind to search.** I labelled 12 of 15 as (b) and none as (c). The search put 8 of 13 testable rows in (c). I did not know which way it would fall; the instrument corrected me.
3. **Verbatim against paraphrase.** Six testable rows use the critic's verbatim words: (a) 1, (b) 1, (c) 4. Seven use the register's paraphrase: (a) 2, (b) 1, (c) 4. The register's wording uses project vocabulary and was expected to find answers more easily. It did not, in this sample.

## 4. What this does not show

1. **It does not show that a whole read finds what a search cannot.** There is no reader arm. Nobody read the document whole and tried to answer these 13 findings. The run shows a lexical search from the critic's words misses 5 to 8 of 13 answers. It cannot show a full read would have found them. The claim in #4088 is made no stronger or weaker by this; it is untested at this denominator.
2. **"Not reached" means this one search did not reach it.** BM25 on stemmed content words is a single retriever. A person who tries synonyms, or a search that matches meaning and not words, would reach more. The 8 and the 5 are ceilings on how often a word search fails, not on how often any search fails.
3. **Whether an answer existed before is the register's claim, not mine.** I did not check version history, because the brief forbids running `git` and `99-archive/` stops at pre-git copies. For F14, F19, F21 and F28 the answer text is in v0.61 but may have been reworded since the finding. F19's row 14e was amended by the very fold that answered the finding, and I can only see the amended row. These four rest on the register's account.
4. **The corpus is the register's 28 findings, not all outside findings.** `07-outreach/memory/records/` holds 154 `obj-*` records, 29 of them self-council, so up to 125 are from outside handles or other sources (not all checked). The register carries 28 rows. The 125 are a larger corpus with a larger denominator; classifying them is the obvious next run. Findings the project judged unimportant, or has not yet folded, are not here. A register that records mostly what was worth folding will over-represent findings that had no earlier answer, and may under-represent ones that did.
5. **The table is mine.** I chose which register entries count, what each critic's words were, which sections the critic "named", and which line is "the answer". The section a critic named is stated in the register for only some rows. Moving one `named` entry flips a row between (a) and (b) or (c). I fixed the hand classes before the first run and added the section arm after it; D4 and D5 exist because of that.
6. **n is 13.** A (c) share of 62% has a 95% interval from 36% to 82%. The two arms' intervals overlap almost entirely.
7. **13 findings had no earlier answer at all.** For those the question "where did it live" has no answer. A reader who wants a denominator for "the answer was already written" should use 15 of 28, and should expect it to be softer than it sounds: 7 of the 15 are partial.

## 5. The command and the seed

```
python 06-simulation/objection-answer-location/answer_location.py --test
python 06-simulation/objection-answer-location/answer_location.py
```

Seed `20261022` (only the control draw uses it; the classification itself is deterministic). K = 5, 10, 25; headline K = 10; a hit needs at least 2 shared content words. Run on Foundations v0.61 and the register v0.45; both are read in place and not modified. Raw output: `results.json`, `run_output.txt`.
