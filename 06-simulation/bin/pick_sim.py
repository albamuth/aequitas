#!/usr/bin/env python3
"""
Pick tonight's simulation request and print it as a prompt block.

The rule, ruled 2026-09-15:

    Take the request the author pinned. If none is pinned, take the OLDEST
    request whose status is still `requested`.

Oldest-first is deliberate. A picker that chooses "the most useful" drifts
toward whatever is easiest to code, and nobody can predict which night will
produce which result.

Where the requests come from (changed 2026-10-14, when the agent moved to a
cloud session):

    1. 06-simulation/SIM_QUEUE.yaml  -- the committed copy. The cloud agent
       runs in a fresh clone and this is the only source it has.
    2. 07-outreach/memory/index.yaml -- the live index, present only on the
       author's machine. Used when the queue file is absent.

`--export` writes the queue file FROM the live index. The author runs it
locally and commits the result, after filing or closing a request.

A request that a report in 06-simulation/log/SIM-*.md already names is
skipped, so a night cannot re-run last night's request just because the
queue has not been refreshed yet.

The pin lives in 06-simulation/PINNED_SIM.txt -- one sim id, or nothing.
Blank lines and lines starting with # are ignored, so the file can carry its
own instructions. A pinned id is taken even if a report already names it;
pinning is the author's way of saying "again".

Usage:
    python bin/pick_sim.py              # print the block
    python bin/pick_sim.py --id-only    # print just the chosen id
    python bin/pick_sim.py --list       # every open request, oldest first
    python bin/pick_sim.py --export     # refresh SIM_QUEUE.yaml from the index

Exit codes:
    0  a request was chosen (or --list / --export succeeded)
    3  nothing to do -- no open requests, or the pinned id does not exist
    1  no source could be read
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FATAL: PyYAML is not installed. `pip install pyyaml`", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[2]          # repo root
INDEX = ROOT / "07-outreach" / "memory" / "index.yaml"
QUEUE = ROOT / "06-simulation" / "SIM_QUEUE.yaml"
PIN = ROOT / "06-simulation" / "PINNED_SIM.txt"
LOG = ROOT / "06-simulation" / "log"
OPEN_STATUSES = {"requested"}
SIM_ID = re.compile(r"\bsr-\d{8}-[a-z0-9-]+")

QUEUE_HEADER = """\
# The open simulation requests, as the cloud night agent sees them.
#
# The agent runs in a fresh cloud clone of this repository. The outreach
# memory (07-outreach/memory/index.yaml) is never committed, so the agent
# cannot read it. This file is the committed copy of the open requests.
#
# REFRESH IT from the local index, then commit:
#
#     python 06-simulation/bin/pick_sim.py --export
#
# That rewrites this file with every request whose status is `requested`,
# oldest first, in the same shape as the index. Run it after filing a
# request and after closing one with `memory.py answer-sim`.
#
# Same shape as the index: one entry per sim id under `sim_requests`,
# with `date`, `status`, `question`, `why`, and optionally `from`.
# The picker takes the author's pin (PINNED_SIM.txt) if there is one,
# else the oldest entry here that no report in log/SIM-*.md has run yet.

"""


def read_pin():
    """The pinned sim id, or None. Comments and blank lines are skipped."""
    if not PIN.exists():
        return None
    for raw in PIN.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            return line
    return None


def load(path):
    """Parse one YAML source. Raises on a missing or unreadable file."""
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_source():
    """(index, which) -- the queue file if present, else the live index."""
    for path in (QUEUE, INDEX):
        if path.exists():
            return load(path), path
    raise FileNotFoundError(f"neither {QUEUE} nor {INDEX} exists")


def open_requests(index):
    """Every unanswered request, oldest first, ties broken by id."""
    sims = index.get("sim_requests") or {}
    rows = [
        (sid, body)
        for sid, body in sims.items()
        if (body or {}).get("status") in OPEN_STATUSES
    ]
    rows.sort(key=lambda r: (str((r[1] or {}).get("date") or ""), r[0]))
    return rows


def reported_ids():
    """Every sim id a report in log/SIM-*.md names. Those nights are done."""
    found = set()
    for report in LOG.glob("SIM-*.md"):
        found.update(SIM_ID.findall(report.read_text(encoding="utf-8", errors="replace")))
    return found


def block(sid, body, how, n_open, source):
    """The text handed to the agent. Plain, and it defines its own terms."""
    b = body or {}
    out = [
        "TONIGHT'S SIMULATION REQUEST",
        "",
        f"  id        {sid}",
        f"  filed     {b.get('date') or 'unknown'}",
        f"  chosen by {how}",
        f"  open      {n_open} request(s) unanswered, including this one",
        f"  source    {source.relative_to(ROOT).as_posix()}",
        "",
        "  THE QUESTION",
        f"    {b.get('question') or '(none recorded)'}",
        "",
        "  WHY IT WAS ASKED",
        f"    {b.get('why') or '(none recorded)'}",
        "",
    ]
    if b.get("from"):
        out += [f"  It came from the record: {b['from']}", ""]
    out += [
        "  WHEN YOU ARE DONE, the author runs this. You do not:",
        f"    python 07-outreach/bin/memory.py answer-sim {sid} --file <your RESULTS file>",
    ]
    return "\n".join(out)


def export():
    """Write SIM_QUEUE.yaml from the live index. Author's machine only."""
    if not INDEX.exists():
        print(f"FATAL: --export needs the live index at {INDEX}, which is not here.\n"
              f"Run this on the machine that holds 07-outreach/.", file=sys.stderr)
        return 1
    rows = open_requests(load(INDEX))
    keep = ("date", "status", "question", "why", "from")
    sims = {
        sid: {k: (body or {}).get(k) for k in keep if (body or {}).get(k) is not None}
        for sid, body in rows
    }
    text = QUEUE_HEADER + yaml.safe_dump(
        {"sim_requests": sims}, sort_keys=False, allow_unicode=True, width=78
    )
    QUEUE.write_text(text, encoding="utf-8")
    print(f"wrote {len(sims)} open request(s) to {QUEUE.relative_to(ROOT).as_posix()}")
    print("commit it, or the cloud agent will not see the change.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id-only", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--export", action="store_true",
                    help="refresh SIM_QUEUE.yaml from 07-outreach/memory/index.yaml")
    a = ap.parse_args()

    if a.export:
        return export()

    try:
        index, source = load_source()
    except Exception as e:                                   # noqa: BLE001
        print(f"FATAL: could not read the requests: {e}", file=sys.stderr)
        return 1

    rows = open_requests(index)
    done = reported_ids()

    if a.list:
        if not rows:
            print("no open simulation requests")
            return 3
        for sid, body in rows:
            mark = "  (report exists)" if sid in done else ""
            print(f"{(body or {}).get('date') or '??????????'}  {sid}{mark}")
        return 0

    pin = read_pin()
    if pin:
        match = next((r for r in rows if r[0] == pin), None)
        if match is None:
            print(
                f"FATAL: PINNED_SIM.txt names `{pin}`, which is not an open request.\n"
                f"Clear the pin or fix the id. Open ids: "
                f"python 06-simulation/bin/pick_sim.py --list",
                file=sys.stderr,
            )
            return 3
        sid, body = match
        how = "the author's pin in 06-simulation/PINNED_SIM.txt"
    else:
        fresh = [r for r in rows if r[0] not in done]
        if not fresh:
            if rows:
                print(
                    "NOTHING TO DO. Every open request already has a report in "
                    "06-simulation/log/. Refresh the queue (pick_sim.py --export) "
                    "or pin one to run it again."
                )
            else:
                print("NOTHING TO DO. No simulation request has status `requested`.")
            return 3
        sid, body = fresh[0]
        how = "oldest open request without a report (no pin set)"

    if a.id_only:
        print(sid)
        return 0

    print(block(sid, body, how, len(rows), source))
    return 0


if __name__ == "__main__":
    sys.exit(main())
