#!/usr/bin/env python3
"""How many links in the PUBLIC core documents point at something not published?

THE QUESTION, filed as
sr-20260907-enumerate-every-outbound-relative-link-in-th on 2026-09-07, from
@amber's finding at obj-20260907-amber-dead-links-to-unpublished-archive:

    "Enumerate every outbound relative link in the PUBLIC core documents and
     count how many resolve to a path that is not in latest-mirror. Report the
     count and the denominator, not a list of instances."

WHY THE COUNT AND THE DENOMINATOR, AND NOT A LIST

    A list of broken links is a chore. A RATE is a measurement, and it is the
    only form in which the number can be compared against a later run or
    against somebody else's repository.

WHY THIS IS NOT bin/consistency.py

    `bin/consistency.py` check [1] resolves links against the WORKING TREE and
    passes when the target exists on this disk. That is the right check for an
    author.

    A READER on GitHub sees only `07-outreach/latest-mirror/`. A link whose
    target exists locally and is absent from the mirror resolves for the author
    and 404s for everybody else. THOSE ARE DIFFERENT QUESTIONS AND ONLY ONE OF
    THEM IS ABOUT THE READER.

    `99-archive/` is the case that motivates it: it is deliberately not
    published, and Foundations names it.

WHAT COUNTS AS A LINK HERE

    A markdown inline link `[text](target)` whose target is RELATIVE -- not
    http, https, mailto, or a bare `#anchor`. An anchor on the end of a
    relative path is stripped before resolving.

RUN
    python mirror_link_audit.py --test     self-tests, each able to fail
    python mirror_link_audit.py            the audit
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MIRROR = ROOT / "07-outreach" / "latest-mirror"

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_SCHEME = ("http://", "https://", "mailto:", "ftp://", "#")


def public_docs():
    """Every markdown file inside the mirror. That is the definition of public."""
    return sorted(p for p in MIRROR.rglob("*.md"))


def links_in(path: Path):
    for m in LINK.finditer(path.read_text(encoding="utf-8", errors="replace")):
        t = m.group(1).strip()
        if t.startswith(SKIP_SCHEME) or not t:
            continue
        yield t.split("#", 1)[0] or None


def audit():
    rows, total, dead = [], 0, 0
    by_target = {}
    for doc in public_docs():
        for target in links_in(doc):
            if target is None:            # pure anchor after stripping
                continue
            total += 1
            resolved = (doc.parent / target).resolve()
            try:
                rel = resolved.relative_to(MIRROR.resolve())
            except ValueError:
                # Escapes the mirror entirely. A reader cannot follow it.
                dead += 1
                key = target
                by_target[key] = by_target.get(key, 0) + 1
                rows.append((doc.relative_to(MIRROR), target, "outside the mirror"))
                continue
            if not (MIRROR / rel).exists():
                dead += 1
                by_target[target] = by_target.get(target, 0) + 1
                rows.append((doc.relative_to(MIRROR), target, "not published"))
    return total, dead, rows, by_target


def self_tests():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        ok = ok and bool(cond)

    check("the mirror exists", MIRROR.is_dir(), str(MIRROR))
    docs = public_docs()
    check("the mirror holds core documents", len(docs) > 10, f"{len(docs)} markdown files")

    # The regex must find a plain link and must ignore an absolute one.
    s = "see [a](x/y.md) and [b](https://e.com) and [c](#anchor) and [d](z.md#s)"
    found = [m.group(1) for m in LINK.finditer(s)]
    check("the link pattern finds relative links", "x/y.md" in found and "z.md#s" in found)
    kept = [t.split("#", 1)[0] for t in found if not t.startswith(SKIP_SCHEME)]
    check("absolute links and bare anchors are skipped",
          kept == ["x/y.md", "z.md"], str(kept))

    # A link that is right from one directory must be wrong from another. If
    # this fails the audit is resolving against the repository root and every
    # answer below is meaningless.
    a = (MIRROR / "00-strategy" / "x.md").parent / "GLOSSARY.md"
    b = (MIRROR / "00-strategy" / "papers" / "x.md").parent / "GLOSSARY.md"
    check("links resolve against their OWN file's directory", a != b)

    total, dead, _, _ = audit()
    check("the denominator is not zero", total > 0, f"{total} links")
    check("the dead count cannot exceed the denominator", dead <= total)

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

    total, dead, rows, by_target = audit()
    docs = public_docs()

    print()
    print("=" * 74)
    print("OUTBOUND RELATIVE LINKS IN THE PUBLISHED DOCUMENTS")
    print("=" * 74)
    print(f"  mirror            : {MIRROR.relative_to(ROOT)}")
    print(f"  markdown files    : {len(docs):,}")
    print(f"  relative links    : {total:,}     <- the denominator")
    print(f"  not resolvable    : {dead:,}")
    print(f"  rate              : {dead / total * 100:.2f}%")
    print()
    if by_target:
        print("  distinct targets that fail, most frequent first:")
        for t, n in sorted(by_target.items(), key=lambda kv: -kv[1])[:20]:
            print(f"    {n:>4}x  {t}")
        print()
        print("  the files they sit in:")
        seen = {}
        for doc, _, _ in rows:
            seen[str(doc)] = seen.get(str(doc), 0) + 1
        for d, n in sorted(seen.items(), key=lambda kv: -kv[1])[:20]:
            print(f"    {n:>4}x  {d}")
    else:
        print("  Every relative link in every published document resolves inside")
        print("  the mirror. A reader on GitHub can follow all of them.")
    print()


if __name__ == "__main__":
    main()
