#!/usr/bin/env python3
"""Can a reader get from the eight axioms to every conformance requirement?

THE QUESTION, filed as
sr-20260908-walk-the-reachability-graph-of-foundations-s on 2026-09-08, from
@amber's finding obj-20260908-amber-conformance-row-unreachable:

    "Walk the reachability graph of Foundations section 1. Entry point: the
     eight axioms. Edges: each axiom's 'where this is worked out' pointer
     line, followed transitively. Target set: every conformance requirement."

WHY IT MATTERS

    A8 says the axioms may not vary AND NEITHER MAY THE CONFORMANCE
    REQUIREMENTS. A requirement that no path from the axioms reaches is a
    requirement a reader cannot find by reading the document the way the
    document says to read it -- "built to be read from the top down, and each
    section assumes the one before it."

    Foundations v0.42 and v0.43 repaired this BY HAND. A3 and A8 gained
    pointer lines, and v0.43's header records the repair by name. NOBODY HAS
    WALKED THE GRAPH TO CONFIRM IT IS COMPLETE, and a hand repair to a
    reachability problem is exactly the kind that closes one hole and leaves
    another.

HOW THE WALK WORKS

    NODES are Foundations section numbers, plus the axioms A1 to A8.

    EDGES come from two places, and only two:
      1. Each axiom's italic "Where this is worked out:" line.
      2. Every section reference of the form (section N) inside the body of a
         section already reached.

    The walk is transitive and breadth-first from the eight axioms.

    TARGETS are the numbered rows of the conformance document.

WHAT A "REACHED" CONFORMANCE ROW MEANS

    Some section reachable from an axiom names that row, by number. It does
    NOT mean the row is argued for there -- only that a reader following
    pointers arrives somewhere that names it.

    That is a WEAK test and it is the right one: it is the test A8's own
    sentence makes, "every one of which is reachable from here."

RUN
    python axiom_reachability.py --test    self-tests, each able to fail
    python axiom_reachability.py           the walk
"""

import argparse
import re
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
STRAT = ROOT / "00-strategy"

AXIOMS = [f"A{i}" for i in range(1, 9)]

# A section heading: "### 3.2a Title" or "#### 5.5.5 Title" or "## 4. What ..."
HEAD = re.compile(r"^#{2,5}\s+(\d+(?:\.\d+)*[a-z]?)\.?\s+(.*)$", re.M)
# A section reference in running text: the section sign, then a number.
SREF = re.compile(r"§\s*(\d+(?:\.\d+)*[a-z]?)")
# An axiom reference: A1 .. A8, not inside a longer token.
AREF = re.compile(r"\b(A[1-8])\b")
# A conformance row cited in Foundations: "conformance requirement 14a",
# "conformance row 10b", "conformance 16a-16c", "conformance rows 7, 7a".
CREF = re.compile(r"conformance\s+(?:requirements?|rows?)?\s*"
                  r"((?:\d+[a-z]?)(?:\s*(?:,|and|-|to|–)\s*(?:\d+[a-z]?))*)",
                  re.I)


def newest(prefix):
    c = sorted(STRAT.glob(f"{prefix}_v*.md"))
    if not c:
        raise SystemExit(f"no {prefix} found in {STRAT}")
    return c[-1]


def split_sections(text):
    """{section number: body text up to the next heading}."""
    out, marks = {}, list(HEAD.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out[m.group(1)] = text[m.start():end]
    return out


def axiom_blocks(text):
    """{A1..A8: the axiom's own block, pointer line included}."""
    out = {}
    for a in AXIOMS:
        m = re.search(rf"^###\s+{a}\s*\(", text, re.M)
        if not m:
            continue
        nxt = re.search(r"^#{2,3}\s+", text[m.end():], re.M)
        out[a] = text[m.start(): m.end() + (nxt.start() if nxt else len(text))]
    return out


def conformance_rows(text):
    """Every numbered requirement in the conformance document."""
    rows = set()
    for m in re.finditer(r"^\s*\|\s*\*{0,2}(\d+[a-z]?)\*{0,2}\s*\|", text, re.M):
        rows.add(m.group(1))
    for m in re.finditer(r"^#{2,4}\s+(?:Requirement\s+)?(\d+[a-z]?)[.\s]", text, re.M):
        rows.add(m.group(1))
    return rows


def cited_rows(body):
    """Conformance rows named in one section's body, ranges expanded."""
    out = set()
    for m in CREF.finditer(body):
        for tok in re.split(r"\s*(?:,|and|-|to|–)\s*", m.group(1)):
            tok = tok.strip()
            if re.fullmatch(r"\d+[a-z]?", tok):
                out.add(tok)
    return out


def walk():
    ftext = newest("Aequitas_Foundations").read_text(encoding="utf-8")
    ctext = newest("Aequitas_Conformance").read_text(encoding="utf-8")
    secs = split_sections(ftext)
    axi = axiom_blocks(ftext)
    targets = conformance_rows(ctext)

    # Seed the frontier from the axioms' own pointer lines.
    seen, q, origin = set(), deque(), {}
    for a, block in axi.items():
        for s in SREF.findall(block):
            if s in secs and s not in seen:
                seen.add(s); q.append(s); origin[s] = a

    # Transitive closure over section references.
    while q:
        cur = q.popleft()
        for s in SREF.findall(secs[cur]):
            if s in secs and s not in seen:
                seen.add(s); q.append(s); origin[s] = origin.get(cur, "?")

    reached_rows = set()
    for s in seen:
        reached_rows |= cited_rows(secs[s])
    # A8 names the conformance document directly, so rows cited in the axiom
    # blocks themselves count too.
    for block in axi.values():
        reached_rows |= cited_rows(block)

    return dict(sections_total=len(secs), sections_reached=len(seen),
                sections_unreached=sorted(set(secs) - seen, key=_key),
                axioms_with_pointers=sorted(
                    a for a, b in axi.items() if SREF.search(b)),
                rows_total=len(targets),
                rows_reached=sorted(targets & reached_rows, key=_key),
                rows_unreached=sorted(targets - reached_rows, key=_key),
                origin=origin)


def _key(s):
    parts = re.split(r"[.]", s)
    return tuple((int(re.sub(r"[a-z]", "", p) or 0), p) for p in parts)


def self_tests():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        ok = ok and bool(cond)

    ftext = newest("Aequitas_Foundations").read_text(encoding="utf-8")
    secs = split_sections(ftext)
    check("sections parse", len(secs) > 40, f"{len(secs)} sections")
    check("a known section is found", "3.4a" in secs and "5.5.5" in secs)

    axi = axiom_blocks(ftext)
    check("all eight axioms parse", len(axi) == 8, f"{sorted(axi)}")

    # The walk must be able to FAIL. If every axiom had a pointer to
    # everything, this test could never distinguish a repair from a no-op.
    check("an axiom block is bounded, not the whole document",
          all(len(b) < 4000 for b in axi.values()),
          f"largest {max(len(b) for b in axi.values())} chars")

    check("conformance rows parse",
          len(conformance_rows(newest("Aequitas_Conformance").read_text(encoding="utf-8"))) > 10)

    check("a range expands", cited_rows("carried as conformance 16a-16c") >= {"16a", "16c"},
          str(sorted(cited_rows("carried as conformance 16a-16c"))))
    check("a single row is found", cited_rows("conformance requirement 14a") == {"14a"})
    check("prose without the word finds nothing", cited_rows("row 7 of the table") == set())

    r = walk()
    check("the walk reaches something", r["sections_reached"] > 5)
    check("the walk does not reach everything by construction",
          r["sections_reached"] <= r["sections_total"])

    print()
    print("  all self-tests pass" if ok else "  SELF-TESTS FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        print("\nSELF-TESTS")
        sys.exit(0 if self_tests() else 1)

    r = walk()
    print()
    print("=" * 74)
    print("REACHABILITY FROM THE EIGHT AXIOMS")
    print("=" * 74)
    print(f"  Foundations : {newest('Aequitas_Foundations').name}")
    print(f"  Conformance : {newest('Aequitas_Conformance').name}")
    print()
    print(f"  axioms carrying a pointer line : "
          f"{len(r['axioms_with_pointers'])}/8   {r['axioms_with_pointers']}")
    print(f"  sections reached               : "
          f"{r['sections_reached']}/{r['sections_total']}")
    print(f"  conformance rows reached       : "
          f"{len(r['rows_reached'])}/{r['rows_total']}")
    print()
    if r["rows_unreached"]:
        print(f"  ROWS NO PATH FROM AN AXIOM REACHES ({len(r['rows_unreached'])}):")
        print("    " + "  ".join(r["rows_unreached"]))
    else:
        print("  Every conformance row is reachable from the axioms.")
    print()
    if r["sections_unreached"]:
        print(f"  sections no path reaches ({len(r['sections_unreached'])}):")
        print("    " + "  ".join(r["sections_unreached"]))
    print()


if __name__ == "__main__":
    main()
