# mirror-link-audit

**Counts the links in the PUBLISHED documents that a reader cannot follow, and reports a rate rather than a list.**

| | |
|---|---|
| **Status** | ✅ Complete, 2026-09-12 |
| **Answers** | `sr-20260907-enumerate-every-outbound-relative-link-in-th`, from @amber's `obj-20260907-amber-dead-links-to-unpublished-archive` |
| **Result** | **18 of 1,270 relative links, 1.42%** — [`RESULTS.md`](RESULTS.md) |
| **Run** | `python mirror_link_audit.py` · self-tests: `python mirror_link_audit.py --test` |

**Why it is not `bin/consistency.py`.** That script resolves links against the **working tree** and passes. This one resolves them against **`07-outreach/latest-mirror/`**, which is all a reader on GitHub can see. A link whose target exists locally and is absent from the mirror resolves for the author and 404s for everybody else.

**The finding: four of the eighteen are in Foundations §6's own directory table**, pointing at folders the project deliberately does not publish. The same section already handles `99-archive/` correctly — it names the folder and drops the link.
