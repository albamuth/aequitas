"""
C11 -- Arithmetic audits: IC-1 through IC-12 over a synthetic event log.

The EventLog spec (Aequitas_EventLog_v0.8.md sec.7) defines twelve integrity
constraints that must hold over any Aequitas event log. This module makes all
twelve *runnable*: it builds one small, hand-verifiable synthetic event log
(the milling/baking chain from the spec's sandwich trace, sec.10, plus two
pre-Aequitas assets entering by genesis, a deployment marker, an object-backed
pledge and a public-good pledge), runs each IC as pure computation, and -- for
each IC -- injects a deliberate violation to prove the check actually fires.

Reworked to EventLog v0.4 / Foundations v0.7 (the credit-realization session):

  * Survival is entity-record continuity, not a within-event "same id on both
    sides" match (Q1). Parcels are persistent records with a lifecycle.
  * The co-product split (theta) is NOT stored on the event. It is computed at
    projection time -- DATA-FIRST from the event's own measured output masses,
    with the published process-energetics model only as a fallback for a
    dimension the event did not measure (sec.7.1a). There is no field for an
    allocation fraction (sec.9), so a self-serving split has nowhere to live;
    the projection-side violations therefore live in the *energetics model*,
    the only place a chosen number exists.
  * Genesis is a distinct origin-terminus, NOT a reservoir (sec.2.2, IC-3): a
    pre-Aequitas object enters at an estimated creation-cost with no reservoir
    input and no parcel ancestry; its estimator is credited.
  * A pledge is a PERMANENT, non-revocable grant of debit-room, drawn 1:1 from the
    pledger's finite lifetime pledging-budget -- not a promise to buy (sec.5.1,
    Foundations v0.14). It moves no debit by itself and cannot be withdrawn; an
    undischarged pledge that reaches expiry BURNS (its budget is lost, never
    returned). When the summoned work yields a held object, the object's debit
    follows possession (IC-5) to *whoever accepts it* -- NOT necessarily the
    pledger; IC-9 no longer forces a pledged object onto the pledger. A pure
    public good moves none.
  * Credit REALIZES on verification of the output; for a good the hand-off is
    the verification (sec.7.3). A deployment marker starts holding-time (sec.2.2).

Two classes of check (EventLog sec.7.1 / sec.7.2):

  IC-1 .. IC-9   LOG-SIDE.  Pure arithmetic on the recorded events. No trust
                model, no weighting model, no external data. This is the schema's
                strongest property: an unrecorded emission stops being an
                enforcement problem and becomes an arithmetic error (sec.7.1).

  IC-10 .. IC-12 PROJECTION-SIDE.  Still pure arithmetic and still no trust model,
                but computed against a weighting/process-energetics model -- the
                first constraints in the spec that check a projection. IC-10
                (non-negative allocation) reuses the *proven* forward solver from
                recursion_convergence.py; the recursion sim already derived
                non-negativity across 4,098 economies, so C11 inherits it rather
                than re-asserting it. IC-12 (boundary additivity) is demonstrated
                here for the first time.

Plus two v0.4 projection properties that are not pass/fail ICs -- credit
realization (sec.7.3) and creation-cost holding-time from deployment (sec.2.2,
Foundations sec.6.2b) -- demonstrated in the report and pinned by self-tests.

Reuses (does NOT rebuild) the recursion sim's solver:
    Economy, build_forward, solve_direct, spectral_radius.

Run:  python arithmetic_audits.py            # build log, run all checks, report
      python arithmetic_audits.py --test     # just the self-tests (pytest-free)
"""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass, field

import numpy as np
import scipy.sparse as sp

from recursion_convergence import Economy, build_forward, solve_direct, spectral_radius


# ---------------------------------------------------------------------------
# Time helpers -- events live on distinct days so no agent's 24h window overlaps
# ---------------------------------------------------------------------------

DAY = 86_400.0
HOUR = 3_600.0


def day(d: float, hour_of_day: float = 6.0) -> float:
    """Absolute TAI-second timestamp for a given day and hour-of-day."""
    return d * DAY + hour_of_day * HOUR


# ---------------------------------------------------------------------------
# Primitives -- a minimal-but-complete rendering of the EventLog sec.2.1 schema.
# Only fields the ICs actually inspect are kept; basis/confidence/resolution/
# signatures/taxonomy-versioning are the spec's concern, not the arithmetic's.
# ---------------------------------------------------------------------------

@dataclass
class Flow:
    """One side of a material/energy movement (EventLog sec.2.1 Flow).

    endpoint_kind is "parcel" or "reservoir". A parcel flow carries `custody`
    (the holding account); a reservoir flow does not.
    """
    endpoint_kind: str          # "parcel" | "reservoir"
    endpoint_id: str
    substance: str
    magnitude: float
    unit: str                   # "kg" | "J"
    custody: str | None = None  # present only on parcel flows

    @property
    def is_parcel(self) -> bool:
        return self.endpoint_kind == "parcel"


@dataclass
class AgentRole:
    account: str
    role: str
    start: float
    end: float

    @property
    def hours(self) -> float:
        return (self.end - self.start) / HOUR


@dataclass
class Event:
    """A bounded transformation of the world (EventLog sec.2.1 Event).

    There is deliberately NO `theta` field. A co-product split is never written
    (sec.9: no field for an allocation fraction); it is computed at projection
    time, data-first from this event's own measured `outputs` (see
    `computed_theta`). `dissipation_j` is declared waste heat for the energy
    balance (IC-2).

    A genesis entry (sec.2.2) is an ordinary Event with no inputs whose
    `process` is `proc:genesis`; a deployment marker is an ordinary Event whose
    `process` is `proc:deployment`. Neither needs a new field -- see
    `is_genesis` / `is_deployment`.
    """
    id: str
    start: float
    end: float
    process: str
    inputs: list[Flow] = field(default_factory=list)
    outputs: list[Flow] = field(default_factory=list)
    agents: list[AgentRole] = field(default_factory=list)
    dissipation_j: float = 0.0


@dataclass
class Pledge:
    """A PERMANENT, non-revocable grant of debit-room: virtual credit the pledger
    puts *behind* creditable work, drawn 1:1 from their finite lifetime pledging-
    budget (EventLog sec.5.1, Foundations v0.14 sec.6.4). It consumes no credit
    and moves no debit by itself; the pledging-power is spent for good at pledge
    time -- discharged when the summoned work occurs, or BURNED if it reaches
    expiry undischarged. There is no retraction."""
    id: str
    pledger: str
    hours: float
    expires_at: float                  # undischarged past this instant => burned (budget lost, not returned)
    timestamp: float
    discharged_by: str | None = None   # event id, once the summoned work occurs


@dataclass
class Parcel:
    """A persistent entity record, derived by replaying the log; not authored
    directly. Its identity persists from its creating event until a destroying
    event -- survival through an event is *record continuity*, not a within-event
    id coincidence (Q1). Repairs keep the same record while raising its debit."""
    id: str
    substance: str
    created_by: str | None
    created_at: float | None
    destroyed_by: str | None = None
    destroyed_at: float | None = None
    origin_reservoir: str | None = None   # set if created straight from a reservoir
    origin_genesis: bool = False          # set if admitted by a genesis entry (sec.2.2)


# ---------------------------------------------------------------------------
# Two special events (EventLog sec.2.2). Neither adds a field: both are ordinary
# Events, recognised by their process taxonomy so IC-1/IC-3 and the holding-time
# projection can treat them correctly.
# ---------------------------------------------------------------------------

def is_genesis(ev: "Event") -> bool:
    """A genesis entry admits a pre-Aequitas object: no reservoir input, no
    parcel ancestry, an estimated creation-cost, the estimator credited. It is a
    distinct IC-3 origin-terminus, NOT a reservoir extraction (sec.2.2)."""
    return ev.process.startswith("proc:genesis")


def is_deployment(ev: "Event") -> bool:
    """A deployment marker records the instant a durable good enters service and
    starts its creation-cost holding-time (sec.2.2, Foundations sec.6.2b)."""
    return ev.process.startswith("proc:deployment")


class LogState:
    """An in-memory event log plus the parcel/custody/account state derived by
    replaying it in time order. The replay is itself a structural consistency
    pass: every check below queries this state rather than the raw events."""

    def __init__(self, events: list[Event], pledges: list[Pledge],
                 reservoirs: set[str], now: float,
                 energetics: dict[str, dict[str, float]] | None = None):
        self.events = sorted(events, key=lambda e: e.start)
        self.pledges = pledges
        self.reservoirs = reservoirs
        self.now = now
        # The process-energetics model is NOT part of the log (sec.3: the log is
        # valid independently of any weighting model). It is carried alongside so
        # the projection-side checks have a concrete model to read, and so a
        # violation can corrupt the model without touching the physical record.
        self.energetics = energetics if energetics is not None else {}
        self.parcels: dict[str, Parcel] = {}
        self._replay()

    # -- parcel bookkeeping ------------------------------------------------

    def _replay(self) -> None:
        """Build the persistent parcel records: creation, destruction, origin.

        Entity-record semantics (Q1), not a within-event id match: a parcel's
        record begins at the first event that outputs it without consuming it
        and ends at the first event that consumes it without re-emitting it. A
        parcel that appears on *both* sides of an event (a transfer, or a
        debit-increasing repair) keeps its record continuously -- it is neither
        created nor destroyed there. That continuity is what "survival" means.
        """
        for ev in self.events:
            in_ids = {f.endpoint_id for f in ev.inputs if f.is_parcel}
            out_ids = {f.endpoint_id for f in ev.outputs if f.is_parcel}

            # created this event (in outputs, and its record does not continue
            # from the inputs of this same event)
            for f in ev.outputs:
                if f.is_parcel and f.endpoint_id not in in_ids:
                    origin_res = None
                    origin_gen = is_genesis(ev)
                    # straight-from-reservoir origin: a reservoir input and no
                    # parcel ancestry (a genesis entry has neither).
                    if not origin_gen and any(not g.is_parcel for g in ev.inputs) \
                            and not in_ids:
                        origin_res = next((g.endpoint_id for g in ev.inputs
                                           if not g.is_parcel), None)
                    self.parcels[f.endpoint_id] = Parcel(
                        id=f.endpoint_id, substance=f.substance,
                        created_by=ev.id, created_at=ev.start,
                        origin_reservoir=origin_res, origin_genesis=origin_gen,
                    )

            # consumed/released this event: record ends (in inputs, not carried
            # forward in this same event's outputs)
            for f in ev.inputs:
                if f.is_parcel and f.endpoint_id not in out_ids:
                    p = self.parcels.get(f.endpoint_id)
                    if p is not None and p.destroyed_by is None:
                        p.destroyed_by = ev.id
                        p.destroyed_at = ev.start

    def events_touching(self, parcel_id: str) -> list[Event]:
        return [e for e in self.events
                if any(f.is_parcel and f.endpoint_id == parcel_id
                       for f in e.inputs + e.outputs)]

    def earned_hours(self, account: str) -> float:
        """Credited hours = sum of the account's AgentRole durations (A2/sec.6:
        credit is time worked, never rate-scaled)."""
        return sum(r.hours for e in self.events for r in e.agents
                   if r.account == account)

    def accounts(self) -> set[str]:
        return {r.account for e in self.events for r in e.agents} | \
               {p.pledger for p in self.pledges}

    def parcel_status(self, parcel_id: str, at: float | None = None) -> str:
        """held | consumed | released | unaccounted, at instant `at` (IC-4).

        Fate closure is only as good as the reservoir registry (EventLog sec.13
        item 4): a parcel dropped into a reservoir that is NOT in the registry
        has gone to an un-named endpoint -- it is `unaccounted`, exactly what
        IC-4 exists to surface -- and so is a parcel with no creation record.
        A parcel still in someone's custody is `held`; that is a valid fate, so
        merely never disposing of a durable good is not a violation.
        """
        at = self.now if at is None else at
        p = self.parcels.get(parcel_id)
        if p is None or p.created_at is None or p.created_at > at:
            return "unaccounted"
        if p.destroyed_at is not None and p.destroyed_at <= at:
            ev = next((e for e in self.events if e.id == p.destroyed_by), None)
            # released iff its destroying event sent it to a *named* (registered)
            # reservoir of the same substance; an unregistered endpoint is a
            # first-class unaccounted result.
            res_out = [f for f in (ev.outputs if ev else [])
                       if not f.is_parcel and f.substance == p.substance]
            if res_out:
                if all(f.endpoint_id in self.reservoirs for f in res_out):
                    return "released"
                return "unaccounted"          # released to an un-named reservoir
            return "consumed"
        return "held"


# ===========================================================================
# IC-1 .. IC-9  --  LOG-SIDE CHECKS (pure arithmetic, no model)
# ===========================================================================

TOL = 1e-9


def check_ic1_mass_balance(log: LogState, tol: float = TOL):
    """Sigma input mass = Sigma output mass, per event (EventLog IC-1).

    A genesis entry (sec.2.2) is exempt: it admits an already-existing object
    whose 'input' is the untracked pre-ledger past, exactly as a reservoir
    extraction introduces mass. Its closure is IC-3's job, not IC-1's."""
    for ev in log.events:
        if is_genesis(ev):
            continue
        m_in = sum(f.magnitude for f in ev.inputs if f.unit == "kg")
        m_out = sum(f.magnitude for f in ev.outputs if f.unit == "kg")
        if abs(m_in - m_out) > tol:
            return False, f"{ev.id}: mass in {m_in} != out {m_out}"
    return True, "all events mass-balance"


def check_ic2_energy_balance(log: LogState, tol: float = TOL):
    """Sigma input energy = Sigma output energy + declared dissipation (IC-2)."""
    for ev in log.events:
        if is_genesis(ev):
            continue
        e_in = sum(f.magnitude for f in ev.inputs if f.unit == "J")
        e_out = sum(f.magnitude for f in ev.outputs if f.unit == "J")
        if abs(e_in - (e_out + ev.dissipation_j)) > tol:
            return False, (f"{ev.id}: energy in {e_in} != out {e_out} "
                           f"+ dissipation {ev.dissipation_j}")
    return True, "all events energy-balance"


def check_ic3_origin_closure(log: LogState):
    """Every parcel traces backward to one of two valid termini (IC-3): a
    reservoir extraction, or a GENESIS entry for a pre-Aequitas asset (sec.2.2).

    Walk each parcel's provenance DAG: its creating event's parcel inputs are
    recursed; a registered-reservoir input or a genesis root is a valid
    terminus. A parcel with no creating event, a cycle with no root, or a
    'reservoir' input that is not in the registry, fails."""
    def traces(parcel_id: str, seen: set[str]) -> bool:
        if parcel_id in seen:
            return False                      # cycle without a root
        seen = seen | {parcel_id}
        p = log.parcels.get(parcel_id)
        if p is None or p.created_by is None:
            return False                      # phantom parcel -- no ancestry
        if p.origin_genesis:
            return True                       # admitted by a genesis entry
        if p.origin_reservoir is not None:
            return p.origin_reservoir in log.reservoirs  # named reservoir only
        ev = next((e for e in log.events if e.id == p.created_by), None)
        if ev is None:
            return False
        parent_parcels = [f.endpoint_id for f in ev.inputs if f.is_parcel]
        has_reservoir_in = any(not f.is_parcel and f.endpoint_id in log.reservoirs
                               for f in ev.inputs)
        if has_reservoir_in and not parent_parcels:
            return True
        return all(traces(pid, seen) for pid in parent_parcels) and bool(parent_parcels)

    for pid in log.parcels:
        if not traces(pid, set()):
            return False, f"parcel {pid} has no reservoir/genesis ancestry"
    return True, "every parcel traces to a reservoir or a genesis entry"


def check_ic4_fate_closure(log: LogState):
    """Every parcel is held, consumed, or released at `now` (IC-4). An
    unaccounted parcel is a first-class query result -- here, a check failure."""
    bad = [pid for pid in log.parcels
           if log.parcel_status(pid) == "unaccounted"]
    if bad:
        return False, f"unaccounted parcels: {bad}"
    return True, "every parcel is held/consumed/released"


def check_ic5_custody_continuity(log: LogState):
    """Exactly one holder at any instant; every handoff's claimed source holder
    matches the parcel's actual current holder (IC-5)."""
    for pid, p in log.parcels.items():
        holder = None
        for ev in log.events_touching(pid):
            in_flow = next((f for f in ev.inputs
                            if f.is_parcel and f.endpoint_id == pid), None)
            out_flow = next((f for f in ev.outputs
                             if f.is_parcel and f.endpoint_id == pid), None)
            if in_flow is not None:
                if holder is not None and in_flow.custody != holder:
                    return False, (f"{pid}@{ev.id}: claims holder "
                                   f"{in_flow.custody}, actually {holder}")
            if out_flow is not None:
                holder = out_flow.custody          # created or transferred to
            elif in_flow is not None:
                holder = None                      # consumed / released
    return True, "custody chains are single-valued and continuous"


def check_ic6_interval_sanity(log: LogState):
    """No event consumes a parcel before it exists or after it is destroyed."""
    for ev in log.events:
        for f in ev.inputs:
            if not f.is_parcel:
                continue
            p = log.parcels.get(f.endpoint_id)
            if p is None or p.created_at is None:
                continue                           # IC-3's problem, not IC-6's
            if ev.start < p.created_at - TOL:
                return False, f"{ev.id} consumes {f.endpoint_id} before it exists"
            if p.destroyed_at is not None and ev.start > p.destroyed_at + TOL \
                    and ev.id != p.destroyed_by:
                return False, f"{ev.id} consumes {f.endpoint_id} after destruction"
    return True, "no event acts on a parcel outside its lifetime"


def check_ic7_agent_time(log: LogState, window: float = 24 * HOUR):
    """No account is credited > 24h of work per 24h window (IC-7)."""
    for acct in log.accounts():
        roles = [r for e in log.events for r in e.agents if r.account == acct]
        # a maximal-overlap 24h window must start at some role's start
        for r0 in roles:
            w_start, w_end = r0.start, r0.start + window
            busy = sum(max(0.0, min(r.end, w_end) - max(r.start, w_start))
                       for r in roles)
            if busy > window + TOL:
                return False, (f"{acct}: {busy/HOUR:.1f}h in a 24h window "
                               f"from {w_start}")
    return True, "no account exceeds 24h work per 24h"


def check_ic8_pledge_backing(log: LogState):
    """Cumulative pledged hours <= lifetime earned credit (IC-8, Foundations v0.14).
    Pledging is a PERMANENT draw on a finite lifetime budget, so the cap is on the
    SUM of ALL pledges the account has ever made -- discharged, outstanding, and
    burned alike -- not on a running 'outstanding' total. (A discharged or burned
    pledge still spent its pledging-power for good.)"""
    for acct in log.accounts():
        cumulative = sum(pl.hours for pl in log.pledges if pl.pledger == acct)
        earned = log.earned_hours(acct)
        if cumulative > earned + TOL:
            return False, (f"{acct}: cumulative pledges {cumulative}h "
                           f"> lifetime earned {earned}h")
    return True, "no account over-pledges its lifetime earned credit"


def check_ic9_pledge_discharge(log: LogState):
    """Pledge discharge (IC-9, Foundations v0.14 / EventLog v0.7). A pledge is a
    permanent grant of debit-room, not a promise to take an object:

      * A discharged pledge references a real event (the summoned work).
      * That discharge event may not occur AFTER the pledge expired: once expiry
        passes undischarged, the pledge has BURNED, so it cannot later discharge.
        (Burned and discharged are mutually exclusive terminal states -- the
        permanent-model analogue of the old discharged-vs-retracted contradiction.)
      * If the event yields a HELD OBJECT, the object's property-debit follows
        possession under IC-5 to *whoever accepts it* -- which NEED NOT be the
        pledger; taking it is a separate custody act on the accepter's own room.
      * A pure service or public good (mowing a verge) yields no held object and
        moves no property-debit -- also valid.

    (There is no retraction under the permanent model; a pledge never binds the
    pledger to accept anything.)"""
    for pl in log.pledges:
        if pl.discharged_by is None:
            continue
        ev = next((e for e in log.events if e.id == pl.discharged_by), None)
        if ev is None:
            return False, f"pledge {pl.id} discharged by unknown event"
        if ev.start > pl.expires_at + TOL:
            return False, (f"pledge {pl.id}: discharged by {ev.id} at {ev.start} "
                           f"after expiry {pl.expires_at} -- it had already burned")
    return True, "discharges reference real events, none after a burn; no object forced on the pledger"


# ===========================================================================
# IC-10 .. IC-12  --  PROJECTION-SIDE CHECKS (arithmetic against a model)
# ===========================================================================

DIMENSIONS = ("mass", "energy")

# Published process-energetics model (EventLog sec.7.1a fallback). Keyed by
# process taxonomy, giving each output SUBSTANCE's share of a dimension the
# event did not meter per output. Milling energy goes mostly into size-reduction
# of the endosperm, and separating bran is largely sieving -- so the ENERGY
# split is not the mass split (sec.10.4): not 0.70/0.30 but a milling-energetics
# figure. This model, not the log, is the only place a chosen split number
# lives, so it is where a projection-side violation is injected.
DEFAULT_ENERGETICS: dict[str, dict[str, float]] = {
    "proc:milling": {"sub:wheat.flour": 0.62, "sub:wheat.bran": 0.38},
}


def computed_theta(ev: Event, dim: str,
                   energetics: dict[str, dict[str, float]]) -> dict[str, float] | None:
    """The co-product split for one dimension, DATA-FIRST (sec.7.1a) and never
    read from a stored field (there is none, sec.9).

    Returns {output_parcel_id: share}, or None when the event is not a
    co-producing process (fewer than two held outputs -> the single product
    trivially takes all of every dimension).

      * `mass` is measured: the split *is* the event's own output-mass fractions.
      * a dimension the event did not meter per output (here `energy`) falls back
        to the published process-energetics model for its `process`; with no
        model it inherits the mass split as the best available reading.
    """
    parcels = [f for f in ev.outputs if f.is_parcel]
    if len(parcels) < 2:
        return None
    mass_total = sum(f.magnitude for f in parcels if f.unit == "kg")
    mass_split = ({f.endpoint_id: f.magnitude / mass_total for f in parcels}
                  if mass_total > 0 else None)
    if dim == "mass":
        return mass_split
    model = energetics.get(ev.process)
    if model is None:
        return mass_split
    return {f.endpoint_id: model.get(f.substance, 0.0) for f in parcels}


def log_to_economy(log: LogState):
    """Bridge the log's *production* events to an Economy for the forward solver.

    Each production event (one with agent labour and parcel outputs) becomes a
    process column; each distinct output/input substance becomes a product row.
    A[i,k]/B[i,k] are the used/made masses; l[k] the direct labour-hours;
    Theta[i,k] the event's projected split. This is the same (A,B,Theta,l)
    structure recursion_convergence.py proved non-negative. Returns
    (Economy, products) where products maps substance -> row index."""
    prod_events = [e for e in log.events
                   if e.agents and any(f.is_parcel for f in e.outputs)
                   and not is_genesis(e)]      # genesis admits, it does not produce
    substances = []
    for e in prod_events:
        for f in e.inputs + e.outputs:
            if f.is_parcel and f.substance not in substances:
                substances.append(f.substance)
    idx = {s: i for i, s in enumerate(substances)}
    M, N = len(substances), len(prod_events)
    A = sp.lil_matrix((M, N))
    B = sp.lil_matrix((M, N))
    Theta = sp.lil_matrix((M, N))
    l = np.zeros(N)
    for k, e in enumerate(prod_events):
        l[k] = sum(r.hours for r in e.agents)
        for f in e.inputs:
            if f.is_parcel:
                A[idx[f.substance], k] += f.magnitude
        # the material operator uses the DATA-FIRST mass split (sec.7.1a),
        # computed from this event's own measured outputs -- not a stored field
        mass_theta = computed_theta(e, "mass", log.energetics)
        for f in e.outputs:
            if not f.is_parcel:
                continue
            B[idx[f.substance], k] += f.magnitude
            if mass_theta is not None and f.endpoint_id in mass_theta:
                Theta[idx[f.substance], k] = mass_theta[f.endpoint_id]
            else:
                Theta[idx[f.substance], k] = 1.0
    econ = Economy(M=M, N=N, A=A.tocsr(), B=B.tocsr(), l=l, Theta=Theta.tocsr())
    return econ, idx


def check_ic10_nonneg_allocation(log: LogState):
    """No output's allocated share is negative, in any dimension (IC-10).

    Two layers: (a) every event's theta is non-negative -- the direct condition;
    (b) the recursive per-unit debit vector p solved through the *proven* forward
    operator is non-negative even though every input is itself a joint split.
    Layer (b) is the recursion sim's result, re-run on the scenario economy."""
    for ev in log.events:                              # (a) direct, every dim
        for dim in DIMENSIONS:
            th = computed_theta(ev, dim, log.energetics)
            if th is None:
                continue
            for pid, share in th.items():
                if share < -TOL:
                    return False, f"{ev.id}[{dim}]: theta[{pid}] = {share} < 0"
    econ, _ = log_to_economy(log)                      # (b) recursive
    A_tilde, c = build_forward(econ)
    rho = spectral_radius(A_tilde)
    if rho >= 1.0 - 1e-9:
        return False, f"economy not productive (rho={rho:.3f}); solver undefined"
    p = solve_direct(A_tilde, c)
    if float(np.min(p)) < -TOL:
        return False, f"recursive debit vector has a negative: min(p)={np.min(p)}"
    return True, f"theta>=0 and recursive min(p)={float(np.min(p)):.4f}>=0 (rho={rho:.3f})"


def check_ic11_exhaustive_allocation(log: LogState):
    """Per joint event, per dimension, the allocated shares sum to the event's
    input total for that dimension -- i.e. the computed theta sums to 1 over the
    event's outputs (IC-11). Nothing is created or lost in the split.

    The measured-mass split is exhaustive by construction; a model-derived
    dimension is only as exhaustive as its published energetics model, which is
    exactly what this check polices."""
    for ev in log.events:
        for dim in DIMENSIONS:
            th = computed_theta(ev, dim, log.energetics)
            if th is None:
                continue
            s = sum(th.values())
            if abs(s - 1.0) > TOL:
                return False, (f"{ev.id}[{dim}]: theta sums to {s}, not 1 "
                               f"(dimension unallocated)")
    return True, "every joint split is exhaustive (theta sums to 1) in each dim"


def _milling_debit(l_grind: float, l_sieve: float | None,
                   theta_flour: float, theta_bran: float, staged: bool):
    """Solve per-unit debit of flour and bran for a milling process, either as
    one whole process or as grind->sieve stages. Both include the same upstream
    cultivation so grain carries a real debit. Returns (p_flour, p_bran)."""
    if not staged:
        # products: grain(0) flour(1) bran(2); processes: cultivation(0) milling(1)
        M, N = 3, 2
        A = sp.lil_matrix((M, N)); B = sp.lil_matrix((M, N)); Th = sp.lil_matrix((M, N))
        l = np.array([6.0, l_grind])                  # l_grind carries whole milling labour
        B[0, 0] = 10.0; Th[0, 0] = 1.0                # cultivation -> grain 10
        A[0, 1] = 10.0                                # milling uses grain 10
        B[1, 1] = 7.0; Th[1, 1] = theta_flour         # -> flour 7
        B[2, 1] = 3.0; Th[2, 1] = theta_bran          # -> bran 3
        econ = Economy(M, N, A.tocsr(), B.tocsr(), l, Th.tocsr())
        p = solve_direct(*build_forward(econ))
        return p[1], p[2]
    # staged: products grain(0) meal(1) flour(2) bran(3); procs cultivation(0) grind(1) sieve(2)
    M, N = 4, 3
    A = sp.lil_matrix((M, N)); B = sp.lil_matrix((M, N)); Th = sp.lil_matrix((M, N))
    l = np.array([6.0, l_grind, l_sieve])
    B[0, 0] = 10.0; Th[0, 0] = 1.0                    # cultivation -> grain 10
    A[0, 1] = 10.0; B[1, 1] = 10.0; Th[1, 1] = 1.0    # grind: grain 10 -> meal 10
    A[1, 2] = 10.0                                    # sieve uses meal 10
    B[2, 2] = 7.0; Th[2, 2] = theta_flour             # -> flour 7
    B[3, 2] = 3.0; Th[3, 2] = theta_bran              # -> bran 3
    econ = Economy(M, N, A.tocsr(), B.tocsr(), l, Th.tocsr())
    p = solve_direct(*build_forward(econ))
    return p[2], p[3]


def check_ic12_boundary_additivity(log: LogState | None = None, tol: float = 1e-9,
                                   staged_theta: tuple[float, float] | None = None):
    """Allocating a process stage-by-stage yields the same per-unit debit as
    allocating it whole (IC-12) -- the defence against boundary gerrymandering.

    Whole milling: grain -> flour+bran, 2h labour, theta (0.7, 0.3).
    Staged:  grind (grain->meal, 1h) then sieve (meal->flour+bran, 1h, same theta).
    Total staged labour (1+1) = whole (2), so an honest split must match. A
    manipulated `staged_theta` diverges and the check catches it."""
    st = staged_theta if staged_theta is not None else (0.7, 0.3)
    pf_w, pb_w = _milling_debit(2.0, None, 0.7, 0.3, staged=False)
    pf_s, pb_s = _milling_debit(1.0, 1.0, st[0], st[1], staged=True)
    df, db = abs(pf_w - pf_s), abs(pb_w - pb_s)
    if df > tol or db > tol:
        return False, (f"whole vs staged diverge: flour {pf_w:.5f} vs {pf_s:.5f} "
                       f"(d={df:.2e}), bran {pb_w:.5f} vs {pb_s:.5f} (d={db:.2e})")
    return True, (f"whole==staged: flour {pf_w:.5f}, bran {pb_w:.5f} "
                  f"(max d={max(df, db):.1e})")


# ===========================================================================
# v0.4 PROJECTION PROPERTIES  --  demonstrated, not pass/fail ICs
#   Credit realization (sec.7.3) and creation-cost holding-time (sec.2.2).
# ===========================================================================

def realization_status(log: LogState):
    """For each production event, is the maker's credit REALIZED? (sec.7.3)

    Credit is always *recorded* (A7/IC-3 -- unpledged wheat still has a grower),
    but it *realizes* -- begins counting toward the maker's position -- only on
    verification of the output. For a physical good the verifying event is the
    hand-off: a receiver, by accepting custody and the property-debit, attests
    the goods exist. So a maker's event realizes iff one of its held outputs is
    already in, or is later handed to, the custody of an account other than the
    maker. This is a projection property, not an integrity constraint: an
    unrealized maker has not broken a rule, their credit simply is not counting
    yet.

    Returns a list of (event_id, [makers], realized, note)."""
    out = []
    for ev in log.events:
        held = [f for f in ev.outputs if f.is_parcel]
        if not ev.agents or not held:
            continue                                  # not a production event
        makers = {r.account for r in ev.agents}
        realized, note = False, "maker still holds the output; unverified"
        for f in held:                                # (i) accepted on making
            if f.custody not in makers:
                realized, note = True, f"accepted by {f.custody} at making"
                break
        if not realized:                              # (ii) later hand-off
            for f in held:
                for e2 in log.events:
                    if e2.start < ev.end:
                        continue
                    if any(g.is_parcel and g.endpoint_id == f.endpoint_id
                           and g.custody not in makers for g in e2.outputs):
                        realized, note = True, f"handed off at {e2.id}"
                        break
                if realized:
                    break
        out.append((ev.id, sorted(makers), realized, note))
    return out


def creation_cost_holding_time(log: LogState, parcel_id: str):
    """Creation-cost holding-time shares for a durable good (sec.2.2, Foundations
    sec.6.2b): the clock starts at the good's DEPLOYMENT marker, and any custody
    held *before* deployment -- genesis admission, transit carriers -- accrues
    NO creation-cost share. A carrier who held 1,000 toasters for two days did
    not make them.

    Returns (deploy_start, {account: holder_seconds}); ({}, None) if the parcel
    has no deployment marker (creation-cost holding-time is undefined for it)."""
    deploy = next((e for e in log.events if is_deployment(e)
                   and any(f.is_parcel and f.endpoint_id == parcel_id
                           for f in e.outputs)), None)
    if deploy is None:
        return None, {}
    spells: list[tuple[str, float, float]] = []
    holder, since = None, None
    for ev in log.events_touching(parcel_id):
        for f in ev.outputs:
            if f.is_parcel and f.endpoint_id == parcel_id:
                if holder is not None and since is not None:
                    spells.append((holder, since, ev.start))
                holder, since = f.custody, ev.start
    if holder is not None and since is not None:
        spells.append((holder, since, log.now))
    d0 = deploy.start
    shares: dict[str, float] = {}
    for acct, s, e in spells:
        s2 = max(s, d0)                               # nothing before deployment counts
        if e > s2:
            shares[acct] = shares.get(acct, 0.0) + (e - s2)
    return d0, shares


# ===========================================================================
# THE SYNTHETIC SCENARIO
# ===========================================================================
#
# Agents:  estimator, farmer, miller, baker, mechanic, gardener
# Chain:   [genesis: tool, part] -> deploy tool -> cultivate -> mill (JOINT:
#          flour+bran) -> bake (bread+vapour) -> sell -> consume; plus a pledged
#          tool repair (object-backed pledge) and a pledged public-verge mow
#          (public-good pledge that moves no debit).
# Every non-genesis event mass-balances; energy inputs are declared as
# dissipated heat. No event carries a split fraction -- the co-product split is
# computed data-first at projection time (sec.7.1a). Numbers are illustrative
# but internally exact and hand-verifiable.

def build_scenario() -> LogState:
    reservoirs = {"soil:field-01", "airshed:local", "watershed:local",
                  "sewer:local", "energy:grid", "energy:gas"}   # NO genesis reservoir

    events: list[Event] = []

    # -- G1/G2 genesis: pre-Aequitas assets (tool, spare part) enter with NO
    #    reservoir input and NO parcel ancestry (sec.2.2). The parcel is rooted
    #    at the genesis event itself -- a distinct IC-3 terminus, not a reservoir.
    #    The estimator is credited for the estimation work.
    events.append(Event(
        id="G1", start=day(0, 1), end=day(0, 1.5), process="proc:genesis",
        outputs=[Flow("parcel", "P:tool", "sub:steel-tool", 5.0, "kg", custody="farmer")],
        agents=[AgentRole("estimator", "role:estimation", day(0, 1), day(0, 1.5))],
    ))
    events.append(Event(
        id="G2", start=day(0, 2), end=day(0, 2.1), process="proc:genesis",
        outputs=[Flow("parcel", "P:part", "sub:steel-part", 0.1, "kg", custody="mechanic")],
        agents=[AgentRole("estimator", "role:estimation", day(0, 2), day(0, 2.1))],
    ))

    # -- D1 deployment marker: the tool enters service; this instant starts its
    #    creation-cost holding-time (sec.2.2, Foundations sec.6.2b). Pure marker:
    #    identical parcel in and out, no agent, no transformation.
    events.append(Event(
        id="D1", start=day(0, 3), end=day(0, 3), process="proc:deployment",
        inputs=[Flow("parcel", "P:tool", "sub:steel-tool", 5.0, "kg", custody="farmer")],
        outputs=[Flow("parcel", "P:tool", "sub:steel-tool", 5.0, "kg", custody="farmer")],
    ))

    # -- E1 cultivation: soil reservoir -> grain (farmer, 6h)
    events.append(Event(
        id="E1", start=day(0, 6), end=day(0, 12), process="proc:agri.cultivation",
        inputs=[Flow("reservoir", "soil:field-01", "sub:wheat.grain", 10.0, "kg")],
        outputs=[Flow("parcel", "P:grain", "sub:wheat.grain", 10.0, "kg", custody="farmer")],
        agents=[AgentRole("farmer", "role:cultivation", day(0, 6), day(0, 12))],
    ))

    # -- E2 transport grain farmer -> miller (pure custody change)
    events.append(Event(
        id="E2", start=day(1, 6), end=day(1, 7), process="proc:transport",
        inputs=[Flow("parcel", "P:grain", "sub:wheat.grain", 10.0, "kg", custody="farmer")],
        outputs=[Flow("parcel", "P:grain", "sub:wheat.grain", 10.0, "kg", custody="miller")],
    ))

    # -- E3 milling: grain + grid energy -> flour + bran  (JOINT; miller 2h)
    #    No split fraction is written. The mass split is read from these very
    #    outputs (7:3); the ENERGY split comes from the process-energetics model.
    events.append(Event(
        id="E3", start=day(2, 6), end=day(2, 8), process="proc:milling",
        inputs=[Flow("parcel", "P:grain", "sub:wheat.grain", 10.0, "kg", custody="miller"),
                Flow("reservoir", "energy:grid", "sub:electricity", 100.0, "J")],
        outputs=[Flow("parcel", "P:flour", "sub:wheat.flour", 7.0, "kg", custody="miller"),
                 Flow("parcel", "P:bran", "sub:wheat.bran", 3.0, "kg", custody="miller")],
        agents=[AgentRole("miller", "role:milling", day(2, 6), day(2, 8))],
        dissipation_j=100.0,
    ))

    # -- E4 bran -> compost reservoir (fate = released to a NAMED reservoir)
    events.append(Event(
        id="E4", start=day(2, 9), end=day(2, 9), process="proc:compost",
        inputs=[Flow("parcel", "P:bran", "sub:wheat.bran", 3.0, "kg", custody="miller")],
        outputs=[Flow("reservoir", "soil:field-01", "sub:wheat.bran", 3.0, "kg")],
    ))

    # -- E5 transport flour miller -> baker
    events.append(Event(
        id="E5", start=day(3, 6), end=day(3, 7), process="proc:transport",
        inputs=[Flow("parcel", "P:flour", "sub:wheat.flour", 7.0, "kg", custody="miller")],
        outputs=[Flow("parcel", "P:flour", "sub:wheat.flour", 7.0, "kg", custody="baker")],
    ))

    # -- E6 baking: flour + water + gas -> bread + vapour  (baker 4h)
    events.append(Event(
        id="E6", start=day(4, 6), end=day(4, 10), process="proc:baking",
        inputs=[Flow("parcel", "P:flour", "sub:wheat.flour", 7.0, "kg", custody="baker"),
                Flow("reservoir", "watershed:local", "sub:water", 3.0, "kg"),
                Flow("reservoir", "energy:gas", "sub:natural-gas", 200.0, "J")],
        outputs=[Flow("parcel", "P:bread", "sub:bread", 9.5, "kg", custody="baker"),
                 Flow("reservoir", "airshed:local", "sub:water-vapour", 0.5, "kg")],
        agents=[AgentRole("baker", "role:baking", day(4, 6), day(4, 10))],
        dissipation_j=200.0,
    ))

    # -- E7 sale bread baker -> farmer
    events.append(Event(
        id="E7", start=day(5, 6), end=day(5, 6), process="proc:sale",
        inputs=[Flow("parcel", "P:bread", "sub:bread", 9.5, "kg", custody="baker")],
        outputs=[Flow("parcel", "P:bread", "sub:bread", 9.5, "kg", custody="farmer")],
    ))

    # -- E8 consumption: bread -> CO2/H2O airshed + waste sewer (farmer)
    events.append(Event(
        id="E8", start=day(5, 12), end=day(5, 13), process="proc:consumption",
        inputs=[Flow("parcel", "P:bread", "sub:bread", 9.5, "kg", custody="farmer")],
        outputs=[Flow("reservoir", "airshed:local", "sub:CO2+H2O", 9.0, "kg"),
                 Flow("reservoir", "sewer:local", "sub:waste", 0.5, "kg")],
        agents=[AgentRole("farmer", "role:eating", day(5, 12), day(5, 12.25))],
    ))

    # -- E10 repair (object-backed pledge PL1): tool + part -> repaired tool,
    #    custody stays farmer (mechanic 3h; tool debit increases, part consumed
    #    into it). The repaired tool -- a HELD object -- happens to land with the
    #    pledger here, but IC-9 no longer requires that (v0.14): debit follows
    #    possession to whoever accepts it, pledger or not.
    events.append(Event(
        id="E10", start=day(6, 6), end=day(6, 9), process="proc:repair",
        inputs=[Flow("parcel", "P:tool", "sub:steel-tool", 5.0, "kg", custody="farmer"),
                Flow("parcel", "P:part", "sub:steel-part", 0.1, "kg", custody="mechanic")],
        outputs=[Flow("parcel", "P:tool", "sub:steel-tool", 5.1, "kg", custody="farmer")],
        agents=[AgentRole("mechanic", "role:repair", day(6, 6), day(6, 9))],
    ))

    # -- E11 public-good work (public-good pledge PL2): gardener mows a public
    #    verge; clippings go to a reservoir. NO held object -> discharge moves no
    #    property-debit (sec.5.1/IC-9). Demonstrates the work-not-debit pledge.
    events.append(Event(
        id="E11", start=day(6, 12), end=day(6, 13), process="proc:groundskeeping",
        inputs=[Flow("reservoir", "soil:field-01", "sub:grass", 2.0, "kg")],
        outputs=[Flow("reservoir", "soil:field-01", "sub:grass-clippings", 2.0, "kg")],
        agents=[AgentRole("gardener", "role:mowing", day(6, 12), day(6, 13))],
    ))

    pledges = [
        # object-backed: PL1 summons the repair. The repaired tool's debit follows
        # possession (IC-5) to whoever accepts it -- here the farmer, but IC-9 does
        # not require that; a pledge never binds the pledger to take the object.
        Pledge(id="PL1", pledger="farmer", hours=3.0,
               expires_at=day(30), timestamp=day(5, 18), discharged_by="E10"),
        # public good: PL2 summons the mow; no object, so no property-debit moves.
        Pledge(id="PL2", pledger="baker", hours=1.0,
               expires_at=day(30), timestamp=day(6, 6), discharged_by="E11"),
        # still outstanding (undischarged, not yet expired): under the cumulative
        # IC-8 it counts along with the farmer's discharged PL1.
        Pledge(id="PL3", pledger="farmer", hours=2.0,
               expires_at=day(30), timestamp=day(6, 18), discharged_by=None),
        # BURNED: PL4 reached expiry (day 6.5) undischarged, so its pledging-power
        # is lost for good. Permanent model -> it STILL counts against the baker's
        # cumulative IC-8 budget (the spend was permanent, not returned).
        Pledge(id="PL4", pledger="baker", hours=2.0,
               expires_at=day(6.5), timestamp=day(6, 6), discharged_by=None),
    ]

    return LogState(events, pledges, reservoirs, now=day(7),
                    energetics=copy.deepcopy(DEFAULT_ENERGETICS))


# ===========================================================================
# VIOLATION GENERATORS -- each returns a copy of the scenario with ONE defect,
# proving the matching check fires. Deep-copied so the clean log is untouched.
# ===========================================================================

def _find(log: LogState, event_id: str) -> Event:
    return next(e for e in log.events if e.id == event_id)


def violate_ic1(log):
    log = copy.deepcopy(log)
    _find(log, "E6").outputs[0].magnitude = 10.5      # bread 9.5 -> 10.5, +0.5 kg
    return log


def violate_ic2(log):
    log = copy.deepcopy(log)
    _find(log, "E6").dissipation_j = 0.0              # 200 J in, undeclared
    return log


def _rebuild(log: LogState) -> LogState:
    """Re-replay a mutated deep copy, preserving the reservoir registry, clock,
    and energetics model."""
    return LogState(log.events, log.pledges, log.reservoirs, log.now, log.energetics)


def violate_ic3(log):
    log = copy.deepcopy(log)
    # baking consumes a phantom flour with no creating event
    _find(log, "E6").inputs[0].endpoint_id = "P:phantom-flour"
    _find(log, "E5").outputs[0].endpoint_id = "P:phantom-orphan"  # break the link
    return _rebuild(log)


def violate_ic4(log):
    log = copy.deepcopy(log)
    # bran released to a reservoir that is NOT in the registry -> gone to an
    # un-named endpoint -> unaccounted (sec.13 item 4). Deleting E4 instead would
    # merely leave the bran 'held' by the miller, which is a valid fate.
    _find(log, "E4").outputs[0].endpoint_id = "void:unregistered-sink"
    return _rebuild(log)


def violate_ic5(log):
    log = copy.deepcopy(log)
    _find(log, "E3").inputs[0].custody = "stranger"   # claims grain held by wrong acct
    return _rebuild(log)


def violate_ic6(log):
    log = copy.deepcopy(log)
    _find(log, "E6").start = day(1, 6)                # bake before milling exists
    _find(log, "E6").end = day(1, 10)
    return _rebuild(log)


def violate_ic7(log):
    log = copy.deepcopy(log)
    # farmer double-booked: a 20h role and a 10h role that OVERLAP -> 30h of work
    # claimed in a single 24h window (two places at once), which wall-clock forbids.
    _find(log, "E1").agents[0].start = day(0, 0)
    _find(log, "E1").agents[0].end = day(0, 20)       # 20h
    _find(log, "E8").agents[0].start = day(0, 5)
    _find(log, "E8").agents[0].end = day(0, 15)       # 10h, overlapping [5,15]
    return _rebuild(log)


def violate_ic8(log):
    log = copy.deepcopy(log)
    # PL3 is the outstanding (undischarged) pledge; over-pledge it far past the
    # farmer's earned credit (6.25 h).
    pl3 = next(pl for pl in log.pledges if pl.id == "PL3")
    pl3.hours = 100.0
    return log


def violate_ic9(log):
    log = copy.deepcopy(log)
    # Contradictory terminal state under the permanent model: a pledge discharged
    # by an event that occurs AFTER it expired -- it had already burned, so it
    # cannot discharge. (Withholding a pledged object from the pledger is NOT a
    # violation -- debit follows possession to whoever accepts it.)
    pl1 = next(pl for pl in log.pledges if pl.id == "PL1")
    pl1.expires_at = day(5)          # PL1 is discharged by E10 at day 6 -> after burn
    return log


def violate_ic10(log):
    # The split is never on the event (sec.9), so the violation lives in the only
    # place a chosen number does: the process-energetics model. A negative energy
    # share is a misdrawn boundary, never a co-product with less than nothing.
    log = copy.deepcopy(log)
    log.energetics["proc:milling"] = {"sub:wheat.flour": 1.1, "sub:wheat.bran": -0.1}
    return log


def violate_ic11(log):
    log = copy.deepcopy(log)
    log.energetics["proc:milling"] = {"sub:wheat.flour": 0.6, "sub:wheat.bran": 0.3}  # 0.9
    return log


# IC-12's violation is a parameter to its check (manipulated staged theta),
# since it operates on the milling decomposition rather than the event log.

# ===========================================================================
# DRIVER
# ===========================================================================

CHECKS = [
    ("IC-1  mass balance",        check_ic1_mass_balance,        violate_ic1),
    ("IC-2  energy balance",      check_ic2_energy_balance,      violate_ic2),
    ("IC-3  origin closure",      check_ic3_origin_closure,      violate_ic3),
    ("IC-4  fate closure",        check_ic4_fate_closure,        violate_ic4),
    ("IC-5  custody continuity",  check_ic5_custody_continuity,  violate_ic5),
    ("IC-6  interval sanity",     check_ic6_interval_sanity,     violate_ic6),
    ("IC-7  agent-time",          check_ic7_agent_time,          violate_ic7),
    ("IC-8  pledge backing",      check_ic8_pledge_backing,      violate_ic8),
    ("IC-9  pledge discharge",    check_ic9_pledge_discharge,    violate_ic9),
    ("IC-10 non-neg allocation",  check_ic10_nonneg_allocation,  violate_ic10),
    ("IC-11 exhaustive alloc",    check_ic11_exhaustive_allocation, violate_ic11),
]


def extent_block(log: LogState) -> dict:
    """The extent rule (EventLog v0.8 sec.7.4): a verdict is
    (result, domain, extent, closure-basis) -- never a bare result.

    This exists because of OP-26. An earlier version of this module reported
    "12/12 clean, 12/12 caught" with no statement of its own blind spots, which
    is exactly the shape of claim the coverage objection punished: internal
    consistency read as completeness. A zero here means only that no violation
    was observed BY THESE CHECKS, OVER THIS EXTENT.

    Nothing below is a pass/fail check. It is the disclosure that has to travel
    beside the verdict.
    """
    events = log.events
    window = (min(e.start for e in events), max(e.end for e in events)) if events else (0.0, 0.0)

    # -- what dimensions were actually carried by the record ------------------
    units = sorted({f.unit for e in events for f in (e.inputs + e.outputs)})

    # -- origin termini, split by whether the log can re-derive them ----------
    genesis_events = [e.id for e in events if is_genesis(e)]
    genesis_parcels = sorted(pid for pid, p in log.parcels.items() if p.origin_genesis)
    reservoir_rooted = sorted(pid for pid, p in log.parcels.items()
                              if p.origin_reservoir is not None)

    # -- flows leaving the accounted world for a commons ----------------------
    reservoir_out = [(e.id, f.endpoint_id, f.magnitude, f.unit)
                     for e in events for f in e.outputs if not f.is_parcel]
    reservoirs_touched = sorted({r for _, r, _, _ in reservoir_out})

    return {
        "domain": {
            "accounts": sorted(log.accounts()),
            "parcels": len(log.parcels),
            "reservoirs_registered": sorted(log.reservoirs),
            "window_days": (round(window[0] / (24 * HOUR), 3),
                            round(window[1] / (24 * HOUR), 3)),
            "as_of_day": round(log.now / (24 * HOUR), 3),
        },
        "extent": {
            "events_replayed": len(events),
            "dimensions_carried": units,
            "parcels_rooted_in_a_reservoir": reservoir_rooted,
            "parcels_admitted_by_genesis": genesis_parcels,
            "reservoirs_receiving_flows": reservoirs_touched,
            "reservoir_out_flows": len(reservoir_out),
        },
        "closure_basis": {
            # The honest answers. Each is "none" for a reason worth stating.
            "reservoir_reconciliation": None,
            "counterparty_attestation_external": None,
            "population_total_N": None,
            "genesis_termini_not_re_derivable": genesis_events,
        },
        "blind_spots": [
            "Whole processes recorded NOWHERE are invisible here. IC-1..IC-9 test "
            "the supplied log against itself; a disjoint chain (unrecorded extraction "
            "-> off-ledger transformation -> off-ledger sink) leaves nothing dangling. "
            "That is a coverage question (Foundations sec.5.1b), not an arithmetic one.",
            "No reservoir stock is reconciled. Nothing here compares the sum of "
            "recorded emissions against an independently measured ambient stock, so "
            "the coverage gap for reservoir-directed flows is UNMEASURED, not zero.",
            "Genesis termini cannot be re-derived from the log's own bytes. A genesis "
            "entry is admitted on its estimate; see EventLog sec.12.3a.",
            "No external counterparty attests any hand-off here. Every custody change "
            "is internal to this synthetic log.",
            "IC-10..IC-12 read a process-energetics model. They are arithmetic, but "
            "they are not assumption-free (sec.7.2).",
        ],
    }


def print_extent_block(log: LogState) -> None:
    blk = extent_block(log)
    print("\n" + "=" * 70)
    print("EXTENT OF THIS VERDICT  (EventLog sec.7.4 -- the extent rule)")
    print("=" * 70)
    print("A passing check must publish what it was capable of detecting.\n")

    d, x, c = blk["domain"], blk["extent"], blk["closure_basis"]
    print("  DOMAIN     -- what this check was about")
    print(f"    accounts            : {', '.join(d['accounts'])}")
    print(f"    parcels             : {d['parcels']}")
    print(f"    reservoirs registered: {', '.join(d['reservoirs_registered'])}")
    print(f"    window (days)       : {d['window_days'][0]} .. {d['window_days'][1]}"
          f"   as-of {d['as_of_day']}")

    print("\n  EXTENT     -- what it actually covered")
    print(f"    events replayed     : {x['events_replayed']}")
    print(f"    dimensions carried  : {', '.join(x['dimensions_carried'])}")
    print(f"    rooted in a reservoir: {len(x['parcels_rooted_in_a_reservoir'])} "
          f"{x['parcels_rooted_in_a_reservoir']}")
    print(f"    admitted by genesis : {len(x['parcels_admitted_by_genesis'])} "
          f"{x['parcels_admitted_by_genesis']}")
    print(f"    flows to a commons  : {x['reservoir_out_flows']} "
          f"into {', '.join(x['reservoirs_receiving_flows']) or '(none)'}")

    print("\n  CLOSURE BASIS -- what warrants the claim that this extent is complete")
    print(f"    reservoir reconciliation : {c['reservoir_reconciliation'] or 'NONE'}")
    print(f"    external counterparty    : {c['counterparty_attestation_external'] or 'NONE'}")
    print(f"    independent total N      : {c['population_total_N'] or 'NONE'}")
    print(f"    un-re-derivable termini  : {c['genesis_termini_not_re_derivable'] or '(none)'}")

    print("\n  BLIND SPOTS")
    for i, b in enumerate(blk["blind_spots"], 1):
        print(f"    {i}. {b}")

    print("\n  READ THE VERDICT AS: 12/12 clean and 12/12 caught, over the extent above,")
    print("  with NO closure basis. Consistency, not completeness (Foundations sec.5.1c).")
    print("=" * 70)


def run_report(log: LogState) -> None:
    print("=" * 70)
    print("C11 -- ARITHMETIC AUDITS  (IC-1 .. IC-12 over a synthetic event log)")
    print("=" * 70)
    print(f"\nScenario: {len(log.events)} events, {len(log.parcels)} parcels, "
          f"{len(log.accounts())} accounts, {len(log.pledges)} pledge(s).")
    print("Chain: [genesis: tool, part] -> deploy tool -> cultivate -> "
          "mill(flour+bran) -> bake(bread) -> sell -> eat;")
    print("       + object-backed pledged repair, + public-good pledged mow.\n")

    print("--- LOG-SIDE (IC-1..IC-9): pure arithmetic, no trust/weighting model ---")
    for label, check, _ in CHECKS[:9]:
        ok, msg = check(log)
        print(f"  [{'PASS' if ok else 'FAIL'}] {label:26s} {msg}")

    print("\n--- PROJECTION-SIDE (IC-10..IC-12): arithmetic against a weighting model ---")
    for label, check, _ in CHECKS[9:]:
        ok, msg = check(log)
        print(f"  [{'PASS' if ok else 'FAIL'}] {label:26s} {msg}")
    ok, msg = check_ic12_boundary_additivity(log)
    print(f"  [{'PASS' if ok else 'FAIL'}] {'IC-12 boundary additivity':26s} {msg}")

    print("\n--- VIOLATION DETECTION: each defect must flip its check to FAIL ---")
    all_caught = True
    for label, check, violate in CHECKS:
        bad_log = violate(log)
        ok, msg = check(bad_log)
        caught = not ok
        all_caught &= caught
        print(f"  [{'CAUGHT' if caught else 'MISSED'}] {label:26s} {msg}")
    ok, _ = check_ic12_boundary_additivity(log, staged_theta=(0.8, 0.2))
    all_caught &= (not ok)
    print(f"  [{'CAUGHT' if not ok else 'MISSED'}] {'IC-12 boundary additivity':26s} "
          f"gerrymandered sieve-stage split (0.8,0.2) diverges from whole")

    print("\n" + "=" * 70)
    print(f"All 12 clean checks pass and all 12 violations caught: "
          f"{'YES' if all_caught else 'NO'}")
    print("=" * 70)

    print_extent_block(log)

    # -- v0.4 projection properties (demonstrated, not pass/fail ICs) -----------
    print("\n--- CREDIT REALIZATION (sec.7.3): recorded always; counts on verification ---")
    for eid, makers, realized, note in realization_status(log):
        tag = "REALIZED  " if realized else "UNREALIZED"
        print(f"  [{tag}] {eid:4s} {'/'.join(makers):20s} {note}")

    print("\n--- CREATION-COST HOLDING-TIME (sec.2.2): clock starts at deployment ---")
    d0, shares = creation_cost_holding_time(log, "P:tool")
    total = sum(shares.values()) or 1.0
    print(f"  P:tool deployed at t={d0 / DAY:.2f}d "
          f"(genesis->deployment gap accrues NO creation-cost share):")
    for acct, sec in shares.items():
        print(f"    {acct:12s} {sec / DAY:6.2f} holder-days  "
              f"({100 * sec / total:.0f}% of creation-cost)")


# ===========================================================================
# SELF-TESTS
# ===========================================================================

def _tests() -> None:
    log = build_scenario()

    # every clean check passes
    for label, check, _ in CHECKS:
        ok, msg = check(log)
        assert ok, f"clean {label} should pass but failed: {msg}"
    ok, msg = check_ic12_boundary_additivity(log)
    assert ok, f"clean IC-12 should pass: {msg}"

    # every violation is caught
    for label, check, violate in CHECKS:
        ok, msg = check(violate(log))
        assert not ok, f"{label} violation NOT caught"
    ok, _ = check_ic12_boundary_additivity(log, staged_theta=(0.8, 0.2))
    assert not ok, "IC-12 gerrymander not caught"

    # replay sanity: parcel fates are exactly as designed
    assert log.parcel_status("P:grain") == "consumed"
    assert log.parcel_status("P:bran") == "released"
    assert log.parcel_status("P:bread") == "consumed"
    assert log.parcel_status("P:tool") == "held"
    assert log.parcel_status("P:part") == "consumed"       # merged into the tool

    # genesis parcels are validly rooted without any reservoir
    assert log.parcels["P:tool"].origin_genesis and not log.parcels["P:tool"].origin_reservoir
    assert check_ic3_origin_closure(log)[0]

    # data-first split: milling mass split is READ from the outputs (7:3), and
    # differs from the model-derived energy split (sec.10.4)
    e3 = _find(log, "E3")
    th_mass = computed_theta(e3, "mass", log.energetics)
    th_energy = computed_theta(e3, "energy", log.energetics)
    assert abs(th_mass["P:flour"] - 0.7) < TOL and abs(th_mass["P:bran"] - 0.3) < TOL
    assert abs(th_energy["P:flour"] - 0.62) < TOL           # not 0.7 -- energy != mass
    assert computed_theta(_find(log, "E6"), "mass", log.energetics) is None  # single product

    # IC-8 boundary (CUMULATIVE, v0.14): the farmer's pledges sum to lifetime
    # earned. PL1 (3h, discharged) already spent budget permanently, so setting PL3
    # to (earned - PL1) makes the cumulative total exactly earned -> passes; one
    # hour over -> fails.
    l2 = copy.deepcopy(log)
    pl3 = next(pl for pl in l2.pledges if pl.id == "PL3")
    other_farmer = sum(pl.hours for pl in l2.pledges
                       if pl.pledger == "farmer" and pl.id != "PL3")
    pl3.hours = l2.earned_hours("farmer") - other_farmer   # cumulative == earned
    assert check_ic8_pledge_backing(l2)[0]
    pl3.hours += 1.0
    assert not check_ic8_pledge_backing(l2)[0]

    # IC-9 (v0.14): a clean log passes -- discharges reference real events, none
    # occurs after a burn, and no object is forced onto the pledger. The BURNED PL4
    # still counts against the baker's cumulative IC-8 budget (3h <= earned 4h).
    assert check_ic9_pledge_discharge(log)[0]
    assert check_ic8_pledge_backing(log)[0]

    # IC-10 recursive layer: the scenario economy is productive and non-negative
    econ, _ = log_to_economy(log)
    A_tilde, c = build_forward(econ)
    assert spectral_radius(A_tilde) < 1.0
    assert float(np.min(solve_direct(A_tilde, c))) >= -TOL

    # credit realization (sec.7.3): every producer in the clean chain is realized
    # (each output is handed off or accepted by a distinct party)
    rs = {eid: realized for eid, _m, realized, _n in realization_status(log)}
    assert all(rs.values()), f"unrealized in clean scenario: {rs}"
    # ... but a maker who keeps their output with no hand-off is unrealized
    solo = LogState(
        [Event(id="X1", start=day(0), end=day(0, 1), process="proc:make",
               outputs=[Flow("parcel", "P:x", "sub:x", 1.0, "kg", custody="maker")],
               agents=[AgentRole("maker", "role:make", day(0), day(0, 1))])],
        [], {"res:x"}, now=day(1))
    assert realization_status(solo)[0][2] is False

    # creation-cost holding-time (sec.2.2): the clock starts at deployment, so the
    # genesis->deployment gap accrues nothing, and a pre-deployment transit
    # custodian accrues no share.
    d0, shares = creation_cost_holding_time(log, "P:tool")
    assert d0 == day(0, 3)                               # deployment marker D1
    assert set(shares) == {"farmer"}
    assert abs(shares["farmer"] - (day(7) - day(0, 3))) < 1.0
    transit = LogState(
        [Event(id="TG", start=day(0), end=day(0), process="proc:genesis",
               outputs=[Flow("parcel", "P:t", "sub:t", 1.0, "kg", custody="carrier")],
               agents=[AgentRole("estimator", "role:estimation", day(0), day(0, 0.1))]),
         Event(id="TT", start=day(1), end=day(1), process="proc:transport",
               inputs=[Flow("parcel", "P:t", "sub:t", 1.0, "kg", custody="carrier")],
               outputs=[Flow("parcel", "P:t", "sub:t", 1.0, "kg", custody="owner")]),
         Event(id="TD", start=day(2), end=day(2), process="proc:deployment",
               inputs=[Flow("parcel", "P:t", "sub:t", 1.0, "kg", custody="owner")],
               outputs=[Flow("parcel", "P:t", "sub:t", 1.0, "kg", custody="owner")])],
        [], {"res:t"}, now=day(5))
    _d0, tshares = creation_cost_holding_time(transit, "P:t")
    assert "carrier" not in tshares and set(tshares) == {"owner"}

    # -- extent rule (EventLog sec.7.4) ---------------------------------------
    _log = build_scenario()
    blk = extent_block(_log)
    assert set(blk) == {"domain", "extent", "closure_basis", "blind_spots"}, \
        "a verdict is (result, domain, extent, closure-basis)"
    assert blk["extent"]["events_replayed"] == len(_log.events)
    assert blk["extent"]["dimensions_carried"], "must name the dimensions it saw"
    # The load-bearing assertion: this scenario HAS no closure basis, and the
    # block must say so rather than leaving the field absent or implying one.
    assert blk["closure_basis"]["reservoir_reconciliation"] is None
    assert blk["closure_basis"]["population_total_N"] is None
    assert blk["closure_basis"]["genesis_termini_not_re_derivable"], \
        "the scenario admits parcels by genesis; those termini must be disclosed"
    assert len(blk["blind_spots"]) >= 4, "a check that names no blind spot is not disclosing"
    # Flows to a commons exist and are reported, so the unmeasured coverage gap
    # is attached to something concrete rather than being an abstract caveat.
    assert blk["extent"]["reservoir_out_flows"] > 0
    print(f"[ok] extent block: {blk['extent']['events_replayed']} events, "
          f"{len(blk['closure_basis']['genesis_termini_not_re_derivable'])} "
          f"un-re-derivable termini, closure basis NONE, "
          f"{len(blk['blind_spots'])} blind spots declared")

    print("All C11 self-tests passed "
          "(12 checks pass on the clean log; 12 violations caught; "
          "realization + holding-time properties hold; the verdict declares its extent).")


def main() -> None:
    ap = argparse.ArgumentParser(description="C11 arithmetic audits (IC-1..IC-12).")
    ap.add_argument("--test", action="store_true", help="run self-tests only")
    args = ap.parse_args()
    if args.test:
        _tests()
    else:
        run_report(build_scenario())


if __name__ == "__main__":
    main()
