"""
Export `arithmetic_audits.py` as INERT DATA -- files a reader can open in a text
editor and check by hand, with no Python and no trust in this repository.

Why this exists
---------------
@twelve-minute-window, comment c15176 on post #1605 (2026-08-23), conceded in
full in `07-outreach/memory/objections.md`:

    "What you shipped is a program that contains the log, contains the
    constraints, contains the injections, and prints a verdict. To check you, I
    must run your implementation on your data and read your summary line."

Their fix, in three items:
    1. the events, parcels, accounts and pledges as JSON, no code;
    2. each constraint stated in arithmetic, not in Python;
    3. the expected verdict for the clean log and for each injected log, with
       the specific quantity that fails to balance and by how much.

This script produces items 1 and 3. Item 2 is `constraints.md`, written by hand
-- mathematics cannot be mechanically exported from an implementation, and
faking that was refused.

What it writes (every file is overwritten in place, so re-running is safe)
-------------------------------------------------------------------------
    fixture.json            the scenario as data: events, flows, agents,
                            pledges, reservoirs, energetics model, clock, and
                            the parcel records the replay derives
    worked_arithmetic.json  every quantity each constraint sums, on the CLEAN
                            log, so the arithmetic can be redone by hand
    expected_verdicts.json  the clean verdict plus all 12 injected logs: what
                            changed, which checks fire, what fails to balance,
                            and by how much
    expected_verdicts.md    the same thing as readable tables

Two independent computations are compared in here on purpose. The `check_*`
functions shipped in `arithmetic_audits.py` give the PASS/FAIL verdict. The
`q_*` functions in this file re-derive the same quantities straight from the
arithmetic written in `constraints.md`. Where they disagree, the disagreement
is written into the output rather than smoothed over -- see the
`implementation_notes` block of `expected_verdicts.json`.

Run (from anywhere; paths are resolved from this file's own location):

    python 06-simulation/audits/audits_inert/generate.py
"""

from __future__ import annotations

import copy
import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SIMDIR = HERE.parent
sys.path.insert(0, str(SIMDIR))

import arithmetic_audits as aa  # noqa: E402

TOL = aa.TOL
DAY = aa.DAY
HOUR = aa.HOUR
WINDOW = 24 * HOUR


# ---------------------------------------------------------------------------
# serialisation
# ---------------------------------------------------------------------------

def as_day(t: float) -> float:
    """TAI seconds -> days, for readers who would rather not divide by 86400."""
    return round(t / DAY, 6)


def flow_d(f) -> dict:
    return {
        "endpoint_kind": f.endpoint_kind,
        "endpoint_id": f.endpoint_id,
        "substance": f.substance,
        "magnitude": f.magnitude,
        "unit": f.unit,
        "custody": f.custody,
    }


def role_d(r) -> dict:
    return {
        "account": r.account,
        "role": r.role,
        "start_s": r.start,
        "end_s": r.end,
        "start_day": as_day(r.start),
        "end_day": as_day(r.end),
        "hours": r.hours,
    }


def event_d(e) -> dict:
    return {
        "id": e.id,
        "process": e.process,
        "start_s": e.start,
        "end_s": e.end,
        "start_day": as_day(e.start),
        "end_day": as_day(e.end),
        "is_genesis": aa.is_genesis(e),
        "is_deployment": aa.is_deployment(e),
        "dissipation_j": e.dissipation_j,
        "inputs": [flow_d(f) for f in e.inputs],
        "outputs": [flow_d(f) for f in e.outputs],
        "agents": [role_d(r) for r in e.agents],
    }


def pledge_d(p) -> dict:
    return {
        "id": p.id,
        "pledger": p.pledger,
        "hours": p.hours,
        "timestamp_s": p.timestamp,
        "timestamp_day": as_day(p.timestamp),
        "expires_at_s": p.expires_at,
        "expires_at_day": as_day(p.expires_at),
        "discharged_by": p.discharged_by,
    }


def parcel_d(log, p) -> dict:
    return {
        "id": p.id,
        "substance": p.substance,
        "created_by": p.created_by,
        "created_at_s": p.created_at,
        "created_at_day": None if p.created_at is None else as_day(p.created_at),
        "destroyed_by": p.destroyed_by,
        "destroyed_at_s": p.destroyed_at,
        "destroyed_at_day": None if p.destroyed_at is None else as_day(p.destroyed_at),
        "origin_reservoirs": list(p.origin_reservoirs),
        "origin_genesis": p.origin_genesis,
        "status_at_now": log.parcel_status(p.id),
    }


def fixture_d(log) -> dict:
    """The whole scenario as inert data."""
    accounts = sorted(log.accounts())
    return {
        "clock": {
            "now_s": log.now,
            "now_day": as_day(log.now),
            "seconds_per_day": DAY,
            "seconds_per_hour": HOUR,
            "note": "All timestamps are absolute TAI seconds. day(d, h) = d*86400 + h*3600.",
        },
        "reservoirs_registered": sorted(log.reservoirs),
        "energetics_model": log.energetics,
        "accounts": [
            {
                "account": a,
                "earned_hours": log.earned_hours(a),
                "cumulative_pledged_hours": sum(pl.hours for pl in log.pledges
                                                if pl.pledger == a),
            }
            for a in accounts
        ],
        "events": [event_d(e) for e in log.events],
        "pledges": [pledge_d(p) for p in log.pledges],
        "derived_parcels": [parcel_d(log, log.parcels[k]) for k in log.parcels],
    }


def diffable(log) -> dict:
    """The parts an injection can touch, keyed so a diff stays readable even
    when an injection re-orders the event list by changing a timestamp."""
    return {
        "events": {e.id: event_d(e) for e in log.events},
        "pledges": {p.id: pledge_d(p) for p in log.pledges},
        "reservoirs_registered": sorted(log.reservoirs),
        "energetics_model": log.energetics,
        "now_s": log.now,
    }


def diff(a, b, path: str = "") -> list[dict]:
    out: list[dict] = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            out += diff(a.get(k, "<absent>"), b.get(k, "<absent>"),
                        f"{path}.{k}" if path else str(k))
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(max(len(a), len(b))):
            out += diff(a[i] if i < len(a) else "<absent>",
                        b[i] if i < len(b) else "<absent>", f"{path}[{i}]")
    elif a != b:
        out.append({"path": path, "clean": a, "injected": b})
    return out


# ---------------------------------------------------------------------------
# the quantities each constraint sums -- re-derived here from `constraints.md`,
# NOT read out of the shipped check's message string
# ---------------------------------------------------------------------------

def q_ic1(log) -> dict:
    rows, fails = [], []
    for ev in log.events:
        if aa.is_genesis(ev):
            rows.append({"event": ev.id, "exempt": True, "reason": "genesis entry"})
            continue
        m_in = sum(f.magnitude for f in ev.inputs if f.unit == "kg")
        m_out = sum(f.magnitude for f in ev.outputs if f.unit == "kg")
        r = m_in - m_out
        rows.append({"event": ev.id, "exempt": False, "mass_in_kg": m_in,
                     "mass_out_kg": m_out, "residual_kg": r,
                     "holds": abs(r) <= TOL})
        if abs(r) > TOL:
            fails.append({"where": ev.id, "quantity": "mass in - mass out",
                          "expected": 0.0, "actual": r, "off_by": r, "unit": "kg"})
    return {"rows": rows, "failures": fails}


def q_ic2(log) -> dict:
    rows, fails = [], []
    for ev in log.events:
        if aa.is_genesis(ev):
            rows.append({"event": ev.id, "exempt": True, "reason": "genesis entry"})
            continue
        e_in = sum(f.magnitude for f in ev.inputs if f.unit == "J")
        e_out = sum(f.magnitude for f in ev.outputs if f.unit == "J")
        r = e_in - (e_out + ev.dissipation_j)
        rows.append({"event": ev.id, "exempt": False, "energy_in_J": e_in,
                     "energy_out_J": e_out, "dissipation_J": ev.dissipation_j,
                     "residual_J": r, "holds": abs(r) <= TOL})
        if abs(r) > TOL:
            fails.append({"where": ev.id,
                          "quantity": "energy in - (energy out + dissipation)",
                          "expected": 0.0, "actual": r, "off_by": r, "unit": "J"})
    return {"rows": rows, "failures": fails}


def _traces(log, pid: str, seen: frozenset) -> bool:
    """IC-3's predicate, written from the arithmetic in `constraints.md`."""
    if pid in seen:
        return False
    seen = seen | {pid}
    p = log.parcels.get(pid)
    if p is None or p.created_by is None:
        return False
    if p.origin_genesis:
        return True
    if p.origin_reservoirs:
        return all(r in log.reservoirs for r in p.origin_reservoirs)
    ev = next((e for e in log.events if e.id == p.created_by), None)
    if ev is None:
        return False
    parents = [f.endpoint_id for f in ev.inputs if f.is_parcel]
    if not parents:
        return False
    return all(_traces(log, q, seen) for q in parents)


def q_ic3(log) -> dict:
    rows, fails = [], []
    for pid, p in log.parcels.items():
        ok = _traces(log, pid, frozenset())
        if p.origin_genesis:
            term = "genesis"
        elif p.origin_reservoirs:
            term = "reservoir " + ", ".join(p.origin_reservoirs)
        else:
            term = "via parcel ancestry"
        rows.append({"parcel": pid, "terminus": term, "traces_to_a_valid_root": ok})
        if not ok:
            fails.append({"where": pid, "quantity": "count of valid origin termini",
                          "expected": 1, "actual": 0, "off_by": 1,
                          "unit": "termini (a count, not a balance)"})
    return {"rows": rows, "failures": fails}


def q_ic4(log) -> dict:
    rows, fails = [], []
    for pid, p in log.parcels.items():
        st = log.parcel_status(pid)
        mass = None
        for ev in log.events_touching(pid):
            for f in ev.inputs + ev.outputs:
                if f.is_parcel and f.endpoint_id == pid and f.unit == "kg":
                    mass = f.magnitude
        rows.append({"parcel": pid, "status_at_now": st, "last_recorded_kg": mass,
                     "holds": st != "unaccounted"})
        if st == "unaccounted":
            fails.append({"where": pid,
                          "quantity": "mass whose fate the log does not name",
                          "expected": 0.0, "actual": mass, "off_by": mass,
                          "unit": "kg"})
    return {"rows": rows, "failures": fails}


def q_ic5(log) -> dict:
    rows, fails = [], []
    for pid in log.parcels:
        holder, chain = None, []
        for ev in log.events_touching(pid):
            inf = next((f for f in ev.inputs
                        if f.is_parcel and f.endpoint_id == pid), None)
            outf = next((f for f in ev.outputs
                         if f.is_parcel and f.endpoint_id == pid), None)
            before = holder
            bad = inf is not None and holder is not None and inf.custody != holder
            if bad:
                fails.append({"where": f"{pid}@{ev.id}",
                              "quantity": "declared source holder",
                              "expected": holder, "actual": inf.custody,
                              "off_by": "identity mismatch (not a numeric residual)",
                              "unit": "account name"})
            if outf is not None:
                holder = outf.custody
            elif inf is not None:
                holder = None
            chain.append({"event": ev.id, "holder_before": before,
                          "declared_in_custody": inf.custody if inf else None,
                          "declared_out_custody": outf.custody if outf else None,
                          "holder_after": holder, "holds": not bad})
        rows.append({"parcel": pid, "custody_chain": chain})
    return {"rows": rows, "failures": fails}


def q_ic6(log) -> dict:
    rows, fails = [], []
    for ev in log.events:
        for f in ev.inputs:
            if not f.is_parcel:
                continue
            p = log.parcels.get(f.endpoint_id)
            if p is None or p.created_at is None:
                rows.append({"event": ev.id, "parcel": f.endpoint_id,
                             "skipped": "no creation record -- IC-3's failure, not IC-6's"})
                continue
            early = ev.start < p.created_at - TOL
            late = (p.destroyed_at is not None and ev.start > p.destroyed_at + TOL
                    and ev.id != p.destroyed_by)
            rows.append({"event": ev.id, "parcel": f.endpoint_id,
                         "event_start_s": ev.start,
                         "parcel_created_at_s": p.created_at,
                         "parcel_destroyed_at_s": p.destroyed_at,
                         "holds": not (early or late)})
            if early:
                fails.append({"where": f"{ev.id} consumes {f.endpoint_id}",
                              "quantity": "event start - parcel creation instant",
                              "expected": ">= 0", "actual": ev.start - p.created_at,
                              "off_by": p.created_at - ev.start, "unit": "seconds early"})
            if late:
                fails.append({"where": f"{ev.id} consumes {f.endpoint_id}",
                              "quantity": "event start - parcel destruction instant",
                              "expected": "<= 0", "actual": ev.start - p.destroyed_at,
                              "off_by": ev.start - p.destroyed_at, "unit": "seconds late"})
    return {"rows": rows, "failures": fails}


def q_ic7(log) -> dict:
    rows, fails = [], []
    for acct in sorted(log.accounts()):
        roles = [r for e in log.events for r in e.agents if r.account == acct]
        worst_start, worst_busy_s = None, 0.0
        for r0 in roles:
            w0, w1 = r0.start, r0.start + WINDOW
            busy_s = sum(max(0.0, min(r.end, w1) - max(r.start, w0)) for r in roles)
            if worst_start is None or busy_s > worst_busy_s:
                worst_start, worst_busy_s = w0, busy_s
        holds = worst_busy_s <= WINDOW + TOL
        rows.append({"account": acct, "roles": len(roles),
                     "worst_window_start_s": worst_start,
                     "worst_window_busy_hours": worst_busy_s / HOUR,
                     "cap_hours": 24.0, "holds": holds})
        if not holds:
            fails.append({"where": f"{acct} in the 24 h window from t={worst_start}",
                          "quantity": "credited hours inside one 24 h window",
                          "expected": 24.0, "actual": worst_busy_s / HOUR,
                          "off_by": (worst_busy_s - WINDOW) / HOUR, "unit": "hours"})
    return {"rows": rows, "failures": fails}


def q_ic8(log) -> dict:
    rows, fails = [], []
    for acct in sorted(log.accounts()):
        cum = sum(pl.hours for pl in log.pledges if pl.pledger == acct)
        earned = log.earned_hours(acct)
        rows.append({"account": acct, "cumulative_pledged_hours": cum,
                     "lifetime_earned_hours": earned,
                     "headroom_hours": earned - cum, "holds": cum <= earned + TOL})
        if cum > earned + TOL:
            fails.append({"where": acct,
                          "quantity": "cumulative pledged hours - lifetime earned hours",
                          "expected": "<= 0", "actual": cum - earned,
                          "off_by": cum - earned, "unit": "hours"})
    return {"rows": rows, "failures": fails}


def q_ic9(log) -> dict:
    rows, fails = [], []
    for pl in log.pledges:
        if pl.discharged_by is None:
            state = "burned" if pl.expires_at <= log.now else "outstanding"
            rows.append({"pledge": pl.id, "state": state, "holds": True})
            continue
        ev = next((e for e in log.events if e.id == pl.discharged_by), None)
        if ev is None:
            rows.append({"pledge": pl.id, "state": "discharged by an unknown event",
                         "holds": False})
            fails.append({"where": pl.id, "quantity": "events matching discharged_by",
                          "expected": 1, "actual": 0, "off_by": 1,
                          "unit": "events (a count, not a balance)"})
            continue
        late = ev.start - pl.expires_at
        rows.append({"pledge": pl.id, "state": "discharged",
                     "discharge_event": ev.id, "discharge_start_s": ev.start,
                     "expires_at_s": pl.expires_at, "late_by_s": late,
                     "holds": late <= TOL})
        if late > TOL:
            fails.append({"where": f"{pl.id} discharged by {ev.id}",
                          "quantity": "discharge instant - expiry instant",
                          "expected": "<= 0", "actual": late, "off_by": late,
                          "unit": "seconds after the pledge had burned"})
    return {"rows": rows, "failures": fails}


def _theta_rows(log) -> list[dict]:
    rows = []
    for ev in log.events:
        for dim in aa.DIMENSIONS:
            th = aa.computed_theta(ev, dim, log.energetics)
            if th is None:
                continue
            rows.append({"event": ev.id, "dimension": dim,
                         "theta": {k: float(v) for k, v in th.items()},
                         "sum": float(sum(th.values())),
                         "min": float(min(th.values()))})
    return rows


def q_ic10(log) -> dict:
    rows, fails = _theta_rows(log), []
    for r in rows:
        for pid, share in r["theta"].items():
            if share < -TOL:
                fails.append({"where": f"{r['event']}[{r['dimension']}] {pid}",
                              "quantity": "allocated share theta",
                              "expected": ">= 0", "actual": share,
                              "off_by": -share, "unit": "share (dimensionless)"})
    econ, idx = aa.log_to_economy(log)
    A_t, c = aa.build_forward(econ)
    rho = float(aa.spectral_radius(A_t))
    productive = rho < 1.0 - 1e-9
    p = aa.solve_direct(A_t, c) if productive else None
    rec = {
        "products_in_row_order": [s for s, _ in sorted(idx.items(), key=lambda kv: kv[1])],
        "labour_hours_per_process_l": econ.l.tolist(),
        "A_used": econ.A.toarray().tolist(),
        "B_made": econ.B.toarray().tolist(),
        "Theta_split": econ.Theta.toarray().tolist(),
        "A_tilde": A_t.toarray().tolist(),
        "c": np.asarray(c).tolist(),
        "spectral_radius_rho": rho,
        "productive_rho_lt_1": productive,
        "p_per_unit_debit_hours_per_kg": None if p is None else np.asarray(p).tolist(),
        "min_p": None if p is None else float(np.min(p)),
    }
    if not productive:
        fails.append({"where": "scenario economy", "quantity": "spectral radius rho(A~)",
                      "expected": "< 1", "actual": rho, "off_by": rho - 1.0,
                      "unit": "dimensionless"})
    elif float(np.min(p)) < -TOL:
        fails.append({"where": "scenario economy", "quantity": "min of the recursive debit vector p",
                      "expected": ">= 0", "actual": float(np.min(p)),
                      "off_by": -float(np.min(p)), "unit": "hours per kg"})
    return {"rows": rows, "recursive_layer": rec, "failures": fails}


def q_ic11(log) -> dict:
    rows, fails = _theta_rows(log), []
    for r in rows:
        d = r["sum"] - 1.0
        r["deviation_from_1"] = d
        r["holds"] = abs(d) <= TOL
        if abs(d) > TOL:
            fails.append({"where": f"{r['event']}[{r['dimension']}]",
                          "quantity": "sum of allocated shares theta",
                          "expected": 1.0, "actual": r["sum"], "off_by": d,
                          "unit": "share (dimensionless)"})
    return {"rows": rows, "failures": fails}


def q_ic12(staged_theta=(0.7, 0.3)) -> dict:
    pf_w, pb_w = aa._milling_debit(2.0, None, 0.7, 0.3, staged=False)
    pf_s, pb_s = aa._milling_debit(1.0, 1.0, staged_theta[0], staged_theta[1],
                                   staged=True)
    fails = []
    for name, w, s in (("flour", pf_w, pf_s), ("bran", pb_w, pb_s)):
        if abs(w - s) > 1e-9:
            fails.append({"where": f"{name} per-unit debit",
                          "quantity": "whole-process debit - staged debit",
                          "expected": 0.0, "actual": float(w - s),
                          "off_by": float(abs(w - s)), "unit": "hours per kg"})
    return {
        "rows": [{
            "whole_theta": [0.7, 0.3],
            "staged_theta": list(staged_theta),
            "whole_labour_hours": {"cultivation": 6.0, "milling": 2.0},
            "staged_labour_hours": {"cultivation": 6.0, "grind": 1.0, "sieve": 1.0},
            "p_flour_whole": float(pf_w), "p_flour_staged": float(pf_s),
            "p_bran_whole": float(pb_w), "p_bran_staged": float(pb_s),
            "delta_flour": float(abs(pf_w - pf_s)),
            "delta_bran": float(abs(pb_w - pb_s)),
        }],
        "failures": fails,
        "note": ("IC-12 as implemented never reads the event log. It builds its "
                 "own milling decomposition inside `_milling_debit`. The fixture "
                 "does not determine this row."),
    }


QUANTS = {
    "IC-1": q_ic1, "IC-2": q_ic2, "IC-3": q_ic3, "IC-4": q_ic4, "IC-5": q_ic5,
    "IC-6": q_ic6, "IC-7": q_ic7, "IC-8": q_ic8, "IC-9": q_ic9,
    "IC-10": q_ic10, "IC-11": q_ic11,
}

IC_NAMES = {
    "IC-1": "mass balance", "IC-2": "energy balance", "IC-3": "origin closure",
    "IC-4": "fate closure", "IC-5": "custody continuity", "IC-6": "interval sanity",
    "IC-7": "agent-time cap", "IC-8": "pledge backing", "IC-9": "pledge discharge",
    "IC-10": "non-negative allocation", "IC-11": "exhaustive allocation",
    "IC-12": "boundary additivity",
}


# ---------------------------------------------------------------------------
# running every shipped check on a log
# ---------------------------------------------------------------------------

def verdict_matrix(log, staged_theta=None) -> list[dict]:
    """Run all twelve shipped checks and record each verdict verbatim."""
    out = []
    for label, check, _ in aa.CHECKS:
        ic = label.split()[0]
        ok, msg = check(log)
        out.append({"ic": ic, "name": IC_NAMES[ic],
                    "verdict": "PASS" if ok else "FAIL", "message": msg})
    ok, msg = aa.check_ic12_boundary_additivity(log, staged_theta=staged_theta)
    out.append({"ic": "IC-12", "name": IC_NAMES["IC-12"],
                "verdict": "PASS" if ok else "FAIL", "message": msg})
    return out


INJECTIONS = [
    ("INJ-1", "IC-1", aa.violate_ic1, None,
     "E6 (baking) bread output raised from 9.5 kg to 10.5 kg."),
    ("INJ-2", "IC-2", aa.violate_ic2, None,
     "E6 (baking) declared dissipation dropped from 200 J to 0 J."),
    ("INJ-3", "IC-3", aa.violate_ic3, None,
     "E6's flour input renamed to a parcel no event creates, and E5's output "
     "renamed too so the chain is broken rather than merely relabelled."),
    ("INJ-4", "IC-4", aa.violate_ic4, None,
     "E4 sends the bran to 'void:unregistered-sink', an endpoint absent from "
     "the reservoir registry."),
    ("INJ-5", "IC-5", aa.violate_ic5, None,
     "E3 (milling) declares its grain input was held by 'stranger'."),
    ("INJ-6", "IC-6", aa.violate_ic6, None,
     "E6 (baking) moved back one day, so it consumes flour before milling "
     "produces it."),
    ("INJ-7", "IC-7", aa.violate_ic7, None,
     "The farmer's two roles are stretched to 20 h and 10 h and made to "
     "overlap, claiming 30 h inside one 24 h window."),
    ("INJ-8", "IC-8", aa.violate_ic8, None,
     "Pledge PL3 raised from 2 h to 100 h."),
    ("INJ-9", "IC-9", aa.violate_ic9, None,
     "PL1's expiry pulled back to day 5, so the event that discharges it on "
     "day 6 happens after the pledge had already burned."),
    ("INJ-10", "IC-10", aa.violate_ic10, None,
     "The published energetics model for milling is set to flour 1.1, "
     "bran -0.1."),
    ("INJ-11", "IC-11", aa.violate_ic11, None,
     "The published energetics model for milling is set to flour 0.6, "
     "bran 0.3, summing to 0.9."),
    ("INJ-12", "IC-12", None, (0.8, 0.2),
     "The sieve stage is re-split 0.8 / 0.2 while the whole process keeps "
     "0.7 / 0.3. No event log is touched -- IC-12 does not read one."),
]


# ---------------------------------------------------------------------------
# cross-check: does the arithmetic in constraints.md agree with the Python?
# ---------------------------------------------------------------------------

def cross_check(log, staged_theta, matrix) -> list[dict]:
    """Compare, per IC, the shipped check's verdict against whether the
    independently re-derived quantities in this file found a failure."""
    out = []
    by_ic = {r["ic"]: r for r in matrix}
    for ic, fn in QUANTS.items():
        q = fn(log)
        stated_fails = bool(q["failures"])
        python_fails = by_ic[ic]["verdict"] == "FAIL"
        out.append({"ic": ic, "python_verdict": by_ic[ic]["verdict"],
                    "stated_arithmetic_finds_a_failure": stated_fails,
                    "agree": stated_fails == python_fails})
    q12 = q_ic12(staged_theta or (0.7, 0.3))
    out.append({"ic": "IC-12", "python_verdict": by_ic["IC-12"]["verdict"],
                "stated_arithmetic_finds_a_failure": bool(q12["failures"]),
                "agree": bool(q12["failures"]) == (by_ic["IC-12"]["verdict"] == "FAIL")})
    return out


IMPLEMENTATION_NOTES = [
    {
        "id": "N1",
        "where": "check_ic12_boundary_additivity, arithmetic_audits.py",
        "finding": "IC-12 takes the event log as its first argument and never "
                   "uses it. Its numbers come from a milling decomposition "
                   "hard-coded inside `_milling_debit`: cultivation 6 h making "
                   "10 kg of grain, then either one 2 h milling step or a 1 h "
                   "grind plus a 1 h sieve. Nothing in fixture.json can change "
                   "the IC-12 row.",
        "consequence": "A reader checking IC-12 must check the numbers in "
                       "constraints.md section IC-12, not the fixture.",
    },
    {
        "id": "N2",
        "where": "check_ic10_nonneg_allocation, arithmetic_audits.py",
        "finding": "IC-10 returns FAIL for two different reasons: a negative "
                   "allocated share, and an economy whose spectral radius is "
                   "not below 1 so the solver is undefined. Only the first is "
                   "a negative allocation.",
        "consequence": "A FAIL on IC-10 does not by itself mean a share went "
                       "negative. The message distinguishes them; the verdict "
                       "does not.",
    },
    {
        "id": "N6",
        "where": "check_ic2_energy_balance docstring",
        "finding": "The docstring states the constraint without its genesis "
                   "exemption. The code exempts genesis entries from IC-2 as "
                   "well as from IC-1.",
        "consequence": "constraints.md states the exemption for both.",
    },
    {
        "id": "N7",
        "where": "LogState.parcel_status, arithmetic_audits.py",
        "finding": "'Released' requires the destroying event to emit a "
                   "reservoir flow whose SUBSTANCE equals the parcel's own "
                   "substance. The prose describes it only as being sent to a "
                   "named reservoir.",
        "consequence": "Load-bearing on this fixture. E8 turns bread into CO2, "
                       "water and sewage, none of them 'sub:bread', so the "
                       "bread reads as consumed rather than released. Both are "
                       "valid fates, so IC-4 still passes.",
    },
    {
        "id": "N8",
        "where": "log_to_economy + check_ic10_nonneg_allocation",
        "finding": "IC-10 reports min(p) = 0.0000 and passes. The zero belongs "
                   "to sub:steel-part, which no process in the derived economy "
                   "makes: `log_to_economy` excludes genesis events, so a "
                   "genesis-admitted substance has an all-zero row in B, an "
                   "all-zero row in A~, and c = 0. Its per-unit debit is zero "
                   "because it has no producer, not because a split came out "
                   "at zero.",
        "consequence": "'min(p) >= 0' is true and is weaker than it looks on "
                       "this fixture. The estimated creation-cost that a "
                       "genesis entry is supposed to carry does not reach the "
                       "IC-10 projection at all.",
    },
    {
        "id": "N9",
        "where": "log_to_economy, the E10 repair event",
        "finding": "The reported spectral radius rho = 0.980 is one number: "
                   "A~[steel-tool, steel-tool] = theta * A / B = 1.0 * 5.0 / "
                   "5.1 = 0.98039..., the repair consuming a 5.0 kg tool and "
                   "emitting a 5.1 kg tool. Every other entry of A~ is smaller. "
                   "The amplification 1 / (1 - 0.98039) = 51 is what turns the "
                   "mechanic's 3 hours into a per-unit tool debit of 30.0 h/kg.",
        "consequence": "The rho quoted beside the IC-10 verdict describes the "
                       "repair loop, not the food chain. It is close to 1 for a "
                       "structural reason a reader should be told, not because "
                       "the economy is near collapse.",
    },
]


# ---------------------------------------------------------------------------
# markdown rendering
# ---------------------------------------------------------------------------

def fmt(v) -> str:
    if isinstance(v, float):
        s = f"{v:.10g}"
        return s
    return str(v)


def render_md(payload: dict) -> str:
    L: list[str] = []
    a = L.append
    a("# Expected verdicts — `arithmetic_audits.py`")
    a("")
    a("**Generated file. Do not hand-edit.** Regenerate with:")
    a("")
    a("```")
    a("python 06-simulation/audits_inert/generate.py")
    a("```")
    a("")
    a(f"Source: `arithmetic_audits.py`, SHA-256 `{payload['provenance']['arithmetic_audits_sha256']}`.")
    a(f"Generated {payload['provenance']['generated_utc']}.")
    a("")
    a("The constraints these verdicts test are written out in "
      "[`constraints.md`](constraints.md). The data they run over is "
      "[`fixture.json`](fixture.json). Every quantity summed on the clean log "
      "is in [`worked_arithmetic.json`](worked_arithmetic.json).")
    a("")
    a("---")
    a("")
    a("## 1. The clean log")
    a("")
    a("| IC | name | verdict | what the program prints |")
    a("|---|---|---|---|")
    for r in payload["clean"]["verdicts"]:
        a(f"| {r['ic']} | {r['name']} | **{r['verdict']}** | `{r['message']}` |")
    a("")
    a("---")
    a("")
    a("## 2. The twelve injected logs")
    a("")
    a("One row per injection. **Fires** is the constraint that is supposed to "
      "catch it. **Also fires** lists any other constraint that happens to fail "
      "on the same corrupted log — a corruption is not obliged to break exactly "
      "one thing.")
    a("")
    a("| # | target | what was changed | fires | also fires |")
    a("|---|---|---|---|---|")
    for inj in payload["injections"]:
        others = [r["ic"] for r in inj["verdicts"]
                  if r["verdict"] == "FAIL" and r["ic"] != inj["target_ic"]]
        tgt = next(r for r in inj["verdicts"] if r["ic"] == inj["target_ic"])
        a(f"| {inj['id']} | {inj['target_ic']} | {inj['description']} | "
          f"**{tgt['verdict']}** | {', '.join(others) or '—'} |")
    a("")
    a("### What fails to balance, and by how much")
    a("")
    a("| # | target | where | quantity | expected | actual | off by | unit |")
    a("|---|---|---|---|---|---|---|---|")
    for inj in payload["injections"]:
        fs = inj["failing_quantities"]
        if not fs:
            a(f"| {inj['id']} | {inj['target_ic']} | — | — | — | — | — | — |")
        for f in fs:
            a(f"| {inj['id']} | {inj['target_ic']} | `{f['where']}` | "
              f"{f['quantity']} | {fmt(f['expected'])} | {fmt(f['actual'])} | "
              f"**{fmt(f['off_by'])}** | {f['unit']} |")
    a("")
    a("### The message each check prints when it fires")
    a("")
    a("| # | message |")
    a("|---|---|")
    for inj in payload["injections"]:
        tgt = next(r for r in inj["verdicts"] if r["ic"] == inj["target_ic"])
        a(f"| {inj['id']} | `{tgt['message']}` |")
    a("")
    a("---")
    a("")
    a("## 3. Exactly what each injection changes")
    a("")
    a("Derived by comparing the injected log against the clean one, field by "
      "field. Not written by hand.")
    a("")
    for inj in payload["injections"]:
        a(f"**{inj['id']} → {inj['target_ic']}**")
        a("")
        if inj["parameter_change"]:
            a(f"- not a log change: `staged_theta` = "
              f"`{inj['parameter_change']['staged_theta']}`")
        if not inj["log_diff"]:
            a("- no field of the event log differs from the clean fixture")
        for d in inj["log_diff"]:
            a(f"- `{d['path']}`: `{fmt(d['clean'])}` → `{fmt(d['injected'])}`")
        a("")
    a("---")
    a("")
    a("## 4. Where the Python and the stated mathematics disagree")
    a("")
    a("Found while writing `constraints.md` against the code. Recorded, not "
      "papered over.")
    a("")
    for n in payload["implementation_notes"]:
        a(f"**{n['id']} — {n['where']}**")
        a("")
        a(f"- *Finding:* {n['finding']}")
        a(f"- *Consequence:* {n['consequence']}")
        a("")
    a("---")
    a("")
    a("## 5. Agreement check")
    a("")
    a("For every log below, the twelve shipped `check_*` functions were run, "
      "and the quantities in `constraints.md` were re-derived independently in "
      "`generate.py`. **Agree** means both said the same thing about whether "
      "the constraint holds.")
    a("")
    a("| log | disagreements |")
    a("|---|---|")
    bad = [c["ic"] for c in payload["clean"]["cross_check"] if not c["agree"]]
    a(f"| clean | {', '.join(bad) or '**none**'} |")
    for inj in payload["injections"]:
        bad = [c["ic"] for c in inj["cross_check"] if not c["agree"]]
        a(f"| {inj['id']} | {', '.join(bad) or '**none**'} |")
    a("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def jdefault(o):
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    raise TypeError(f"not JSON-serialisable: {type(o)}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(name: str, obj) -> Path:
    p = HERE / name
    p.write_text(json.dumps(obj, indent=2, default=jdefault) + "\n",
                 encoding="utf-8")
    return p


def main() -> None:
    clean = aa.build_scenario()
    clean_diffable = diffable(clean)

    provenance = {
        "generated_utc": _dt.datetime.now(_dt.timezone.utc)
                            .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "06-simulation/audits_inert/generate.py",
        "arithmetic_audits_sha256": sha256(SIMDIR / "arithmetic_audits.py"),
        "recursion_convergence_sha256": sha256(SIMDIR.parent / "allocation-engine"
                                              / "recursion_convergence.py"),
        "why": ("@twelve-minute-window, comment c15176 on post #1605: shipping "
                "only a program relocates the trust from the number to the "
                "repository. These files let a reader check the arithmetic "
                "without running anything."),
    }

    # -- 1. the fixture -----------------------------------------------------
    fixture = {"provenance": provenance,
               "counts": {"events": len(clean.events),
                          "parcels": len(clean.parcels),
                          "accounts": len(clean.accounts()),
                          "pledges": len(clean.pledges)},
               **fixture_d(clean)}
    write_json("fixture.json", fixture)

    # -- 2. the arithmetic, worked, on the clean log ------------------------
    worked = {"provenance": provenance,
              "note": ("Every quantity each constraint sums, computed on the "
                       "clean log. Redo any of it by hand from fixture.json."),
              "by_constraint": {ic: fn(clean) for ic, fn in QUANTS.items()}}
    worked["by_constraint"]["IC-12"] = q_ic12()
    worked["extent_block"] = aa.extent_block(clean)
    write_json("worked_arithmetic.json", worked)

    # -- 3. the expected verdicts -------------------------------------------
    clean_matrix = verdict_matrix(clean)
    payload = {
        "provenance": provenance,
        "clean": {
            "verdicts": clean_matrix,
            "all_pass": all(r["verdict"] == "PASS" for r in clean_matrix),
            "cross_check": cross_check(clean, None, clean_matrix),
        },
        "injections": [],
        "implementation_notes": IMPLEMENTATION_NOTES,
    }

    for inj_id, target, violate, staged, desc in INJECTIONS:
        bad = violate(clean) if violate is not None else clean
        matrix = verdict_matrix(bad, staged_theta=staged)
        if target == "IC-12":
            q = q_ic12(staged)
        else:
            q = QUANTS[target](bad)
        payload["injections"].append({
            "id": inj_id,
            "target_ic": target,
            "target_name": IC_NAMES[target],
            "description": desc,
            "parameter_change": None if staged is None else {"staged_theta": list(staged)},
            "log_diff": diff(clean_diffable, diffable(bad)) if violate else [],
            "verdicts": matrix,
            "failing_quantities": q["failures"],
            "cross_check": cross_check(bad, staged, matrix),
        })

    write_json("expected_verdicts.json", payload)
    (HERE / "expected_verdicts.md").write_text(render_md(payload), encoding="utf-8")

    # -- console summary ----------------------------------------------------
    print(f"wrote {HERE}")
    print(f"  fixture.json            {fixture['counts']}")
    print(f"  worked_arithmetic.json  {len(worked['by_constraint'])} constraints")
    print(f"  expected_verdicts.json  clean all-pass="
          f"{payload['clean']['all_pass']}, {len(payload['injections'])} injections")
    print(f"  expected_verdicts.md")
    misses = [i["id"] for i in payload["injections"]
              if next(r for r in i["verdicts"] if r["ic"] == i["target_ic"])["verdict"] != "FAIL"]
    print(f"  injections whose target check did NOT fire: {misses or 'none'}")
    dis = [(lbl, c["ic"]) for lbl, cc in
           [("clean", payload["clean"]["cross_check"])] +
           [(i["id"], i["cross_check"]) for i in payload["injections"]]
           for c in cc if not c["agree"]]
    print(f"  stated-arithmetic vs Python disagreements: {dis or 'none'}")


if __name__ == "__main__":
    main()
