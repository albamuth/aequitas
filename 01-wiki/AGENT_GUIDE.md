# How to answer a question about Aequitas from this wiki

> **Version:** 0.1
> **Date:** 2026-10-14

**One page plus its edges answers most questions. Do not read the 260 KB Foundations document first.**

## The four steps

1. **Find the node.** Open `graph.json` and search `nodes` for the term, the ID (`A7`, `IC-7`, `OP-10`, `C3`, `§4.4`) or a word from the question. Each node has `title`, `summary`, `type`, `status`, `file`. The `ids` a page claims resolve to it.
2. **Read that one page.** Every page defines its terms at the top, states the rule, and shows it working with real numbers. The `summary` line is the one-sentence answer; the worked example is the proof.
3. **Follow the edges before you speak.** In `graph.json`, `edges` are `{from, rel, to}`. Follow, in this order:
   - `forbids` edges *into* a `refused-proposal` node: if the question proposes that, **say which axiom refuses it and stop**. The edge comes from an axiom node or a section node; a section node has no file but lists the wiki pages that cite it under `pages`.
   - `open_under`: if the page is open under an `OP-#`, **say the problem is open and name it.** Live OPs have their own pages (`op-4`, `op-10`, `op-16`, `op-22`, `op-24`, `op-28`); the rest are rows in `open-problems`. An OP node with no page carries the register's status text verbatim; read its row. Do not supply a plausible answer.
   - `depends_on`: the rule cannot be stated without these. Read them if the question is *why*.
   - `constrained_by`: the integrity constraint or conformance row that bounds it.
   - `tested_by`: the simulation that measured it. Quote its figure with its setting (`F`, ρ, `k`).
4. **Cite the `source` edge.** Every answer names the Foundations or Conformance section that states the rule, in words a reader without the document open can follow.

## The three verdicts

| If the question lands on | Say |
|---|---|
| A `refused-proposal` node | **REFUSED.** Name the axiom. Do not stress-test it or look for a version that works |
| An `answered-question` node, or a page with `status: settled` | **ANSWERED.** Give the rule, the example, the section. Do not re-derive it |
| A page with `status: contested`, or an `open-question` node | **OPEN.** Name the OP. Do not guess |

**A page with `status: provisional` is a working rule that may change. Say so.** When an `answered-question` node points at a provisional page, the verdict is still ANSWERED: give the rule and add the caveat, with the OP it is open under.

**Where the graph and a page disagree, the page wins.** The `refused-*` and `answered-*` nodes are copied from `00-strategy/Aequitas_Question_Index.md`, which is folded less often than the wiki. A page dated later than the Index row states the current rule; say that a conflict exists.

## Where things are

| Need | Page |
|---|---|
| The eight axioms | `type: axiom` nodes, A1 to A8 |
| What a trust network does | `trust-network`, then its `implies` edges |
| Every kind of debit | `debit-taxonomy` |
| IC-1 to IC-12 | `integrity-constraints` |
| C1 to C12 | `components` |
| Every open problem | `open-problems` |
| What killed prior systems | `field-record` |
| The whole node table | `graph.md` |

**Two rules of the register.** Define an abbreviation or section reference the first time you use it. Give a worked example with digits whenever you explain a mechanism.
