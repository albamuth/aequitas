# axiom-reachability

> **Version:** 0.1
> **Date:** 2026-09-16

**Walks the pointer graph from Foundations' eight axioms and counts which conformance requirements a reader actually arrives at.**

| | |
|---|---|
| **Status** | ✅ Complete, 2026-09-12 |
| **Answers** | `sr-20260908-walk-the-reachability-graph-of-foundations-s`, from @amber's `obj-20260908-amber-conformance-row-unreachable` |
| **Result** | **A8's repair confirmed. 10 of 44 rows named from a reached section** — [`RESULTS.md`](RESULTS.md) |
| **Run** | `python axiom_reachability.py` · self-tests: `python axiom_reachability.py --test` |

**The state @amber named:** *a row never linked, not a row never written* — present, correct, and never arrived at. **Every completeness check that counts rows passes it**, which is why nothing caught row 10e.

**Entry point, edge types and target set are declared in the code before the walk runs**, which is @amber's own partial repair for the fact that we choose the denominator.
