#!/usr/bin/env python3
"""
Pick tonight's simulation request and print it as a prompt block.

The rule, ruled 2026-09-15:

    Take the request the author pinned. If none is pinned, take the OLDEST
    request whose status is still `requested`.

Oldest-first is deliberate. A picker that chooses "the most useful" drifts
toward whatever is easiest to code, and nobody can predict which night will
produce which result.

The pin lives in 06-simulation/PINNED_SIM.txt -- one sim id, or nothing.
Blank lines and lines starting with # are ignored, so the file can carry its
own instructions.

Usage:
    python bin/pick_sim.py              # print the block
    python bin/pick_sim.py --id-only    # print just the chosen id
    python bin/pick_sim.py --list       # every open request, oldest first

Exit codes:
    0  a request was chosen
    3  nothing to do -- no open requests, or the pinned id does not exist
    1  the index could not be read
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FATAL: PyYAML is not installed. `pip install pyyaml`", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[2]          # repo root
INDEX = ROOT / "07-outreach" / "memory" / "index.yaml"
PIN = ROOT / "06-simulation" / "PINNED_SIM.txt"
OPEN_STATUSES = {"requested"}


def read_pin():
    """The pinned sim id, or None. Comments and blank lines are skipped."""
    if not PIN.exists():
        return None
    for raw in PIN.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            return line
    return None


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


def block(sid, body, how, n_open):
    """The text handed to the agent. Plain, and it defines its own terms."""
    b = body or {}
    out = [
        "TONIGHT'S SIMULATION REQUEST",
        "",
        f"  id        {sid}",
        f"  filed     {b.get('date') or 'unknown'}",
        f"  chosen by {how}",
        f"  open      {n_open} request(s) unanswered, including this one",
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id-only", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    try:
        index = yaml.safe_load(INDEX.read_text(encoding="utf-8"))
    except Exception as e:                                   # noqa: BLE001
        print(f"FATAL: could not read {INDEX}: {e}", file=sys.stderr)
        return 1

    rows = open_requests(index)

    if a.list:
        if not rows:
            print("no open simulation requests")
            return 3
        for sid, body in rows:
            print(f"{(body or {}).get('date') or '??????????'}  {sid}")
        return 0

    if not rows:
        print("NOTHING TO DO. No simulation request has status `requested`.")
        return 3

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
        sid, body = rows[0]
        how = "oldest open request (no pin set)"

    if a.id_only:
        print(sid)
        return 0

    print(block(sid, body, how, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
