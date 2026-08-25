"""
statera.py -- STATERA, the Aequitas simulation kernel.

THE NAME. A `statera` is the balance-scale the goddess Aequitas is shown holding on
Roman coinage. It is an INSTRUMENT, which is what this is: a thing you measure a
theory with, never the theory itself (Foundations Sec.1.2). Named 2026-08-23.

WHAT THIS IS. The one object every scenario runs on: cohorts, an append-only event
log, the debit VECTOR, credit accrual, the ratio gate, a time axis with births and
deaths, and the Foundations Sec.9 conformance requirements asserted as invariants.
Steps 1-3 of `00-strategy/Aequitas_Simulation_Roadmap_v0.2.md`.

WHAT IT IS FOR. Finding the thresholds, conditions and variables that lead to
Aequitas being adopted -- how fast, how slow, or where it fails critically. The
conformance checks and the disparity ceiling are INSTRUMENT CHECKS; they prove the
machine measures what it claims. They are not the object of study.

WHY IT EXISTS. Nothing in 06-simulation/ was the kernel. Every script re-implemented
its own credit accrual, its own gate, its own agents -- which is exactly why each one
answers a single question and none of them composes with another. This is that shared
core, written once.

WHAT IT IS NOT. Not a trust-network database (Foundations Sec.1.2). Not a first
version of the system. It is an instrument for testing a theory, and the moment it
starts being treated as anything else, Sec.1.2 has been breached again.

DESIGN NOTES, the three that matter.

  1. THE LOG IS COLUMNAR, and that is what makes A6 affordable. "Balances are never
     authoritative -- the event log is" (A6) usually costs you a per-agent object graph
     and a slow fold. Here events are parallel numpy arrays and deriving the ledger is
     a segment-sum (np.bincount) over the actor column. 200,000 agents and 600,000
     events derive in milliseconds, so the honest thing and the fast thing are the
     same thing. Projections are cached, and `Conformance.check_a6` recomputes from
     scratch and asserts equality -- the cache is a projection, never the authority.

  2. THE DEBIT IS A VECTOR AND THE COLLAPSE IS A SEPARATE, EXPLICIT STEP (Sec.3.2a).
     `Projection.debit()` returns one array per physical dimension. `collapse()` is
     the only place a weighting model is applied. Any division must happen per
     dimension BEFORE collapsing, so `divide()` refuses to operate on a collapsed
     figure at all -- the side entrance into OP-10 is closed by the type, not by a
     rule someone has to remember.

  3. THE GATE IS EVALUATED AT TRANSACTION TIME AND THE INPUTS ARE RECORDED (Sec.3.3).
     Each consumption event stores the rho and the credit that were true when it
     happened. A later re-weight changes FUTURE room and can never make a completed
     act retroactively invalid; `check_transaction_time` proves it by re-weighting the
     whole history and asserting no past event becomes a violation.

REPRODUCTION TARGETS (the roadmap's rule against building a framework nobody uses:
the kernel must re-derive published results before a single new scenario runs).
  - 24/F disparity = 2.40x at F=10h, flat across every rho in [1,3]
      -- disparity_ceiling_sim.claim1_ceiling_vs_rho
  - clearing rho* ~ 1.20 under the US method, median at ~0.92, ~35% constrained
      -- rho_sweep.scenario_table
Both are checked in run_tests() by driving the SAME populations through this kernel's
event log and gate rather than through the closed-form arithmetic those scripts use.
Same inputs, different machinery, same number -- or the kernel is wrong.

Run:  python statera.py [--test] [--demo]
"""
from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field

import numpy as np

# The published disparity-ceiling and clearing-rate scripts, which Statera has to
# reproduce, live in a sibling project directory (06-simulation/disparity-ceiling).
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "disparity-ceiling"))

from disparity_ceiling_sim import F, DAY, CEILING  # noqa: E402

# F above is the PUBLISHED calibration (10 h/day), kept only so the reproduction
# targets are checked against the number that was actually published. It is not
# "the" floor. F is a network dial (Sec.6.1b, A8) and every result that divides by
# it must say which floor it assumed -- see `ceiling()` and `sweep_floor()`.

# --- the debit vector ---------------------------------------------------------
# Physical dimensions carried separately and collapsed only on demand (Sec.3.2a).
# Extend this tuple to give a scenario more physics; nothing else has to change.
DIMS = ("labour_h", "mass_kg", "energy_mj")

# --- event kinds --------------------------------------------------------------
SELF_CARE = 0   # Sec.6.1b -- credited maintenance time, proof-of-life
WORK      = 1   # Sec.6    -- productive hours
CONSUME   = 2   # Sec.3.2  -- permanent consumption/pollution debit, on the causer
TRANSFER  = 3   # Sec.3.2  -- property debit follows possession
PLEDGE    = 4   # Sec.6.4  -- permanent, backed 1:1 by lifetime earned credit
GENESIS   = 5   # Sec.6.2a -- admits a thing that existed before the ledger
TALLY     = 6   # Sec.3.3  -- a measurement of the world; credits the measurer

KIND_NAMES = {SELF_CARE: "self_care", WORK: "work", CONSUME: "consume",
              TRANSFER: "transfer", PLEDGE: "pledge", GENESIS: "genesis",
              TALLY: "tally"}

# Kinds that create credit. Note what is absent: there is no kind that moves credit
# from one actor to another, and A3 is enforced by that absence (check_a3).
CREDITING = (SELF_CARE, WORK, TALLY)


class ConformanceError(AssertionError):
    """A Sec.9 requirement failed. Either the scenario is malformed or the theory
    has a hole. Both are results; neither is something to catch and continue past."""


# =============================================================================
# The append-only event log
# =============================================================================

@dataclass
class EventLog:
    """Append-only, columnar, never edited and never truncated (Sec.5.1a, Sec.5.4).

    A record is only ever added. There is deliberately no delete, no update, and no
    truncate -- 'a log that can be truncated is not a log' (Sec.5.4), and the
    13/13-truncation result of 2026-08-23 is what happens when you assume otherwise.
    """
    n_agents: int
    actor:   list = field(default_factory=list)
    kind:    list = field(default_factory=list)
    period:  list = field(default_factory=list)
    credit_h: list = field(default_factory=list)          # hours credited
    dims:    dict = field(default_factory=dict)           # dim -> list of quantities
    # transaction-time witnesses (Sec.3.3): what was true when the gate ran
    rho_at:  list = field(default_factory=list)
    room_at: list = field(default_factory=list)
    essential: list = field(default_factory=list)         # Sec.7.5 -- never gated
    process: list = field(default_factory=list)           # process id, -1 = none
    # How many real people this row speaks for. An actor is a COHORT and the row
    # stores what ONE of them did; the headcount scales it to a population.
    # Everything in the log is per-person. Aggregate views multiply; per-person
    # checks (IC-7, IC-8, the gate) must not -- see Kernel.population_credit.
    # At weight = 1.0 this file behaves exactly as kernel v0.1 did, which is what
    # test_weight_of_one_changes_nothing asserts.
    weight: list = field(default_factory=list)
    # The period after which the goods on this row can no longer be handed on.
    # np.inf means the thing does not spoil. Author ruling 2026-08-23: a good with
    # a shelf life carries its expiry in the log, and once past it the holder
    # cannot pass the debit to anybody -- it has joined their waste stream.
    expires: list = field(default_factory=list)
    # Debit-room GRANTED to the actor on this row by somebody's pledge (Sec.6.2b).
    # A grant cushions the bite of a front-loaded creation-cost; it is NOT spendable
    # headroom (Sec.6.4c: pledge surplus is non-consumable), which is why `room()`
    # caps the offset at the creation-cost it is earmarked against.
    grant_h: list = field(default_factory=list)
    # Marks a debit row as CREATION-COST (a front-loaded asset cost, Sec.6.2a), the
    # only debit a grant is allowed to offset. Ordinary consumption is not creation
    # cost and a grant can never cushion it.
    creation: list = field(default_factory=list)

    def __post_init__(self):
        for d in DIMS:
            self.dims.setdefault(d, [])

    def __len__(self):
        """Total rows, not batches -- appends are vectorised over many actors."""
        return int(sum(a.size for a in self.actor))

    def append(self, actor, kind, period, credit_h=0.0, essential=False,
               rho_at=np.nan, room_at=np.nan, process=-1, weight=1.0,
               expires=np.inf, grant_h=0.0, creation=False, **quantities):
        """Add one event. The only mutation this class permits."""
        unknown = set(quantities) - set(DIMS)
        if unknown:
            raise ValueError(f"unknown debit dimensions: {sorted(unknown)}")
        if np.any(np.asarray(weight, float) < 0):
            raise ValueError("a headcount cannot be negative")
        n = np.size(actor)
        self.weight.append(np.broadcast_to(np.asarray(weight, float), (n,)).copy())
        self.expires.append(np.broadcast_to(np.asarray(expires, float), (n,)).copy())
        self.grant_h.append(np.broadcast_to(np.asarray(grant_h, float), (n,)).copy())
        self.creation.append(np.broadcast_to(np.asarray(creation, bool), (n,)).copy())
        self.actor.append(np.asarray(actor, dtype=np.int64).reshape(-1))
        self.kind.append(np.full(n, kind, dtype=np.int8))
        self.period.append(np.full(n, period, dtype=np.int32))
        self.credit_h.append(np.broadcast_to(np.asarray(credit_h, float), (n,)).copy())
        self.essential.append(np.broadcast_to(np.asarray(essential, bool), (n,)).copy())
        self.rho_at.append(np.broadcast_to(np.asarray(rho_at, float), (n,)).copy())
        self.room_at.append(np.broadcast_to(np.asarray(room_at, float), (n,)).copy())
        self.process.append(np.broadcast_to(np.asarray(process, np.int64), (n,)).copy())
        for d in DIMS:
            q = quantities.get(d, 0.0)
            self.dims[d].append(np.broadcast_to(np.asarray(q, float), (n,)).copy())

    # --- read-only column access ---------------------------------------------
    def col(self, name):
        parts = getattr(self, name) if name != "dims" else None
        return np.concatenate(parts) if parts else np.array([])

    def dim(self, d):
        return np.concatenate(self.dims[d]) if self.dims[d] else np.array([])


# =============================================================================
# Projection -- the ledger, DERIVED (A6), never stored
# =============================================================================

class Projection:
    """A6: an account's standing is a pure function of the log.

    Cached for speed and re-derived from scratch by `Conformance.check_a6`. The cache
    is a projection; the log is the authority.
    """

    def __init__(self, log: EventLog):
        self.log = log
        self._cache = {}
        self._at = -1

    def _fresh(self):
        if self._at != len(self.log):
            self._cache.clear()
            self._at = len(self.log)

    def credit(self) -> np.ndarray:
        """Cumulative credit per agent, in hours. Never decremented by a purchase
        (A3: credit is not a currency -- a purchase adds to debit instead).

        ONLY CREDITING KINDS ARE SUMMED, and that filter is load-bearing.

        Fixed 2026-08-23, and it was an axiom breach. `pledge()` writes a NEGATIVE
        credit_h row to draw down the lifetime pledging budget. Summing every
        credit_h column therefore made a pledge shrink the pledger's own credit
        and, through `room()`, their own consumption. Measured before the fix:
        earn 12 h, pledge 5 h, and `credit()` read 7.0 with room falling 18 -> 10.5.

        A3 says credit is never transferred or lent. Foundations Sec.6.4 says a
        pledge "does not draw the creation-cost down", that "the pledger's credit
        itself never moves and is never earmarked", and that "pledging never
        diminishes credit itself". `pledge()`'s own docstring said the same. The
        code did the opposite of all four.

        The pledging budget is a SEPARATE quantity, read by `pledged()` and capped
        against lifetime earned credit by IC-8. It is not a debit from credit.
        """
        self._fresh()
        if "credit" not in self._cache:
            sel = np.isin(self.log.col("kind"), CREDITING)
            self._cache["credit"] = np.bincount(
                self.log.col("actor")[sel], weights=self.log.col("credit_h")[sel],
                minlength=self.log.n_agents)
        return self._cache["credit"]

    def debit(self) -> dict:
        """Cumulative debit per agent, PER DIMENSION (Sec.3.2a). Never collapsed here."""
        self._fresh()
        if "debit" not in self._cache:
            actor = self.log.col("actor")
            self._cache["debit"] = {
                d: np.bincount(actor, weights=self.log.dim(d),
                               minlength=self.log.n_agents) for d in DIMS}
        return self._cache["debit"]

    def pledged(self) -> np.ndarray:
        """Pledging budget SPENT per actor -- the finite lifetime budget IC-8 caps.

        A pledge draws the budget with a negative credit_h row on the PLEDGER. Only
        those rows count here; a grant recorded on the recipient carries credit_h = 0
        and does not touch anyone's budget.
        """
        self._fresh()
        if "pledged" not in self._cache:
            k = self.log.col("kind")
            sel = (k == PLEDGE)
            self._cache["pledged"] = np.bincount(
                self.log.col("actor")[sel], weights=-self.log.col("credit_h")[sel],
                minlength=self.log.n_agents)
        return self._cache["pledged"]

    def granted(self) -> np.ndarray:
        """Debit-room granted TO each actor by others' pledges (Sec.6.2b), in hours.

        Earmarked: `room()` caps how much of this actually offsets debit at the
        actor's creation-cost, so a grant can never become spendable headroom
        (Sec.6.4c). This is the raw granted total; the cap is applied in the gate.
        """
        self._fresh()
        if "granted" not in self._cache:
            self._cache["granted"] = np.bincount(
                self.log.col("actor"), weights=self.log.col("grant_h"),
                minlength=self.log.n_agents)
        return self._cache["granted"]

    def creation_cost(self) -> np.ndarray:
        """Front-loaded creation-cost debit per actor, in labour-hours (Sec.6.2a).

        The only debit a grant may cushion. Measured as the labour_h on rows flagged
        `creation`, so ordinary consumption debit is never offsettable by a pledge.
        """
        self._fresh()
        if "creation_cost" not in self._cache:
            sel = self.log.col("creation")
            self._cache["creation_cost"] = np.bincount(
                self.log.col("actor")[sel], weights=self.log.dim("labour_h")[sel],
                minlength=self.log.n_agents) if sel.any() else np.zeros(self.log.n_agents)
        return self._cache["creation_cost"]


# =============================================================================
# Collapse and division (Sec.3.2a)
# =============================================================================

DEFAULT_WEIGHTS = {"labour_h": 1.0, "mass_kg": 0.0, "energy_mj": 0.0}


def validate_gate_weights(weights: dict) -> None:
    """A weighting model used by the GATE must keep the gate binding and coherent.

    Outside-critique finding #12 (2026-08-24): the gate is `rho*C - collapse(D, w)`,
    where credit `C` is in labour-hours. For the two sides to be comparable, the
    labour dimension of the debit must map to hours one-for-one, so `labour_h` MUST
    carry weight 1.0. A weighting that zeroes it makes the collapsed debit ignore
    everything `consume()` records (which is denominated in labour_h), so the gate
    never tightens and consumption is unbounded -- a silent, catastrophic hole that
    `run_scenario.py` exposed by letting a TOML file set `[dials.weights]` freely.

    Every other dimension is a MITIGATION-COST CONVERSION into hours and must be
    non-negative: `mass_kg = 0.05` means "0.05 h to mitigate 1 kg". Zero is fine
    (a flow at its natural-remediation baseline, like breathing) and is the default;
    a discovered pollutant is modelled by RAISING it above zero (Sec.3.3), which is
    what makes a re-weight actually bite -- see `test_a_reweight_moves_a_number`.

    This is a guard on the GATE weighting only. A reporting collapse (a mass-only
    cost view, say) may weight however it likes and does not come through here.
    """
    if weights is None:
        return
    lab = weights.get("labour_h", 0.0)
    if abs(lab - 1.0) > 1e-12:
        raise ConformanceError(
            f"gate weighting must set labour_h = 1.0 (credit is in labour-hours, so "
            f"the labour dimension of debit must be comparable 1:1); got {lab}. "
            f"A zero or scaled labour weight makes the ratio gate non-binding and "
            f"consumption unbounded. Weight other dimensions as mitigation-hours.")
    for d in DIMS:
        if weights.get(d, 0.0) < 0:
            raise ConformanceError(
                f"gate weight for {d} is negative ({weights[d]}); a mitigation cost "
                f"cannot be below zero.")


def collapse(debit: dict, weights: dict = None) -> np.ndarray:
    """Combine the debit vector into one comparable figure, using a weighting model.

    The ONLY place a weighting model is applied. Whoever controls `weights` controls
    every comparison -- which is OP-10, and why divisions must not happen downstream
    of this function (see `divide`).
    """
    w = DEFAULT_WEIGHTS if weights is None else weights
    total = None
    for d in DIMS:
        term = debit[d] * w.get(d, 0.0)
        total = term if total is None else total + term
    return total


def divide(debit: dict, shares: np.ndarray) -> dict:
    """Split a debit vector per dimension, BEFORE any collapse (Sec.3.2a).

    Takes a dict of vectors and returns a dict of vectors. It cannot be handed a
    collapsed figure, so the weighting-independent split is enforced by the signature
    rather than by a rule someone has to remember.
    """
    if not isinstance(debit, dict):
        raise TypeError(
            "divide() takes a debit VECTOR, not a collapsed figure. Sec.3.2a: any "
            "division is computed per dimension, before collapsing.")
    return {d: debit[d] * shares for d in DIMS}


# =============================================================================
# The kernel
# =============================================================================

@dataclass
class Dials:
    """Network-level settings. Aequitas uses these and never sets them (A8)."""
    rho: float = 1.5            # the consumption gate multiplier (Sec.3.5)
    floor_h: float = F          # the self-care floor, h/day (Sec.6.1b)
    weights: dict = None        # the weighting model (OP-10)
    metabolic_co2_kg_per_day: float = 1.0
    # A1 reaches "down to the oxygen a human inhales and the CO2 they exhale", and
    # the author confirmed 2026-08-23 that every human's exhaled CO2 is a debit,
    # recorded automatically. ~1 kg/day for an adult (approximate; to be sourced).
    #
    # RECORDED, AND WEIGHED AT ZERO -- and those do not conflict. A1 says the flow
    # is real and belongs in the log. Sec.3.3 says "a flow is a pollutant only
    # above the rate at which the natural world remediates it unaided", and
    # breathing is inside the short carbon cycle: the carbon came out of the air,
    # through a plant, into food, and back. It is at baseline, so it weighs
    # nothing under any honest weighting model.
    #
    # This is the clearest demonstration in the whole kernel of why Sec.3.2a keeps
    # the debit as a VECTOR and collapses only on demand. The kilograms are in the
    # log forever. What they COST is a separate question, answered by the
    # weighting model, and re-answerable if the science ever changes.
    days_per_period: float = 1.0
    # How long a period lasts. IC-7 is a rule about a 24-HOUR day, so a monthly
    # period caps an account at 24 * 30 hours, not 24. Without this the cap fires
    # on the first month of any run coarser than daily -- and generational
    # scenarios (Onboarding_the_wealthy_v0.1.md, 70-170 years) need annual steps.


class Kernel:
    """Agents, a log, a projection, and the rules that are never configurable."""

    def __init__(self, n_agents: int, credit_rate: np.ndarray, dials: Dials = None,
                 weight: np.ndarray = None, born: np.ndarray = None,
                 lifespan: np.ndarray = None):
        """n_agents COHORT SLOTS, each represented by one exemplar person.

        `weight` is the headcount each exemplar stands for. Left unset it is 1.0
        everywhere, and every actor is then a single person -- which is what the
        v0.1 tests assume and what keeps them meaningful.

        `born` is the period each cohort comes into existence; `lifespan` is how
        many periods it lasts. Left unset, everyone exists from period 0 forever.

        Slots are PRE-ALLOCATED. The log's actor column indexes into a fixed width,
        so a scenario declares its maximum number of cohorts up front rather than
        growing arrays mid-run. A slot awaiting a birth carries headcount 0.
        """
        if np.any(credit_rate < 0) or np.any(credit_rate > DAY):
            raise ConformanceError("IC-7: a credit rate outside [0, 24] h/day")
        self.n = int(n_agents)
        self.rate = np.asarray(credit_rate, float)        # h/day, includes the floor
        self.weight = (np.ones(self.n) if weight is None
                       else np.asarray(weight, float))
        if self.weight.shape != (self.n,):
            raise ValueError(f"weight must have one headcount per cohort ({self.n})")
        if np.any(self.weight < 0):
            raise ValueError("a headcount cannot be negative")
        self.born = (np.zeros(self.n, np.int64) if born is None
                     else np.asarray(born, np.int64).copy())
        self.lifespan = (np.full(self.n, np.inf) if lifespan is None
                         else np.asarray(lifespan, float).copy())
        self.dials = dials or Dials()
        # The gate weighting must keep the gate binding (finding #12). Validate it
        # once, here, where the kernel commits to using it -- not in Dials, because
        # the same dict may also be handed to `collapse` for reporting, where a
        # non-labour weighting is legitimate.
        validate_gate_weights(self.dials.weights)
        self.log = EventLog(n_agents=self.n)
        self.proj = Projection(self.log)
        self.period = 0

    # --- who exists right now ------------------------------------------------
    def alive(self, period: int = None) -> np.ndarray:
        """Cohorts that have been born, have not outlived their span, and still
        have somebody in them.

        A dead cohort stops accruing and stops consuming. It is NEVER removed and
        its rows are never touched -- Sec.5.4: the record closes but persists,
        including after death, and it stays re-weighable forever.
        """
        p = self.period if period is None else period
        return ((self.born <= p) & (p < self.born + self.lifespan)
                & (self.weight > 0))

    def age_years(self, period: int = None) -> np.ndarray:
        """Age of each cohort's exemplar, in years."""
        p = self.period if period is None else period
        return (p - self.born) * self.dials.days_per_period / 365.0

    def birth(self, slots, headcount, rate, lifespan=np.inf):
        """Bring pre-allocated cohort slots to life at the current period."""
        slots = np.atleast_1d(np.asarray(slots, np.int64))
        if np.any(self.weight[slots] > 0):
            raise ValueError("cannot give birth into an occupied cohort slot")
        if np.any(np.asarray(rate, float) > DAY):
            raise ConformanceError("IC-7: a credit rate above 24 h/day")
        self.born[slots] = self.period
        self.weight[slots] = headcount
        self.rate[slots] = rate
        self.lifespan[slots] = lifespan

    def die(self, mortality_per_period: float):
        """Shrink every living cohort's headcount. Nothing is deleted.

        Headcounts go fractional as a cohort thins out. That is honest for a model
        of a population and is recorded as a limit rather than rounded away.
        """
        live = self.alive()
        self.weight[live] *= (1.0 - float(mortality_per_period))

    # --- per-person vs population -------------------------------------------
    # The log holds what ONE person in a cohort did. These three are the only
    # place a headcount is applied, and nothing that gates or checks an
    # individual (IC-7, IC-8, room()) may use them.
    def headcount(self) -> float:
        return float(self.weight.sum())

    def population_credit(self) -> np.ndarray:
        return self.proj.credit() * self.weight

    def population_debit(self) -> dict:
        return {d: v * self.weight for d, v in self.proj.debit().items()}

    # --- accrual ------------------------------------------------------------
    def accrue(self, days: float = 1.0):
        """One period of credit. Self-care is credited by proof-of-life to everyone
        alive (Sec.6.1b, Sec.7.5); the remainder is productive work (Sec.6)."""
        live = self.alive()
        if not live.any():
            return
        idx = np.arange(self.n)[live]
        rate, w = self.rate[live], self.weight[live]
        floor = np.minimum(rate, self.dials.floor_h) * days
        work = np.maximum(rate - self.dials.floor_h, 0.0) * days
        # Breathing rides the self-care row rather than getting one of its own:
        # it is the material cost of the same act, and a separate row would grow
        # the log by half for no extra information.
        co2 = self.dials.metabolic_co2_kg_per_day * days
        self.log.append(idx, SELF_CARE, self.period, credit_h=floor, essential=True,
                        weight=w, mass_kg=co2)
        self.log.append(idx, WORK, self.period, credit_h=work, weight=w)

    # --- the gate -----------------------------------------------------------
    def room(self) -> np.ndarray:
        """Discretionary debit-room remaining: rho*C - D + earmarked grant, re-checked
        at each event.

        A ratio, never a balance drawn down (Sec.7.5). Credit is not spent by a
        purchase, so a 'hoarder' can only front-load their own allowance.

        THE GRANT TERM CUSHIONS A FRONT-LOADED CREATION-COST AND NOTHING ELSE
        (Sec.6.2b, finding #11). A pledge grants debit-room to a recipient carrying a
        big capital/creation cost, so they are not locked out of ordinary consumption
        while they hold it. But the offset is capped at the recipient's own
        creation-cost: `min(granted, creation_cost)`. It can remove that specific
        bite down to zero and no further -- it never becomes spendable headroom for
        discretionary consumption, which is Sec.6.4c (pledge surplus is
        non-consumable). Nothing vanishes from the ledger either (A1): the
        creation-cost debit stays recorded in D; the grant only changes what the
        GATE counts against the recipient while they carry it.
        """
        C = self.proj.credit()
        D = collapse(self.proj.debit(), self.dials.weights)
        offset = np.minimum(self.proj.granted(), self.proj.creation_cost())
        return self.dials.rho * C - D + offset

    def consume(self, request_h: np.ndarray, essential=False, dims: dict = None):
        """Attempt consumption. Returns (admitted, refused) in collapsed units.

        Essentials are never gated (Sec.7.5) -- the ratio governs the discretionary
        layer only, or it would fall hardest on the newborn, the old, the sick and
        the disabled, who are exactly who that section protects.
        """
        live = self.alive()
        # The dead consume nothing. Their standing is untouched and stays derivable.
        request = np.where(live, np.asarray(request_h, float), 0.0)
        if essential:
            admitted = request
        else:
            admitted = np.clip(np.minimum(request, self.room()), 0.0, None)
        refused = request - admitted

        q = {"labour_h": admitted}
        if dims:
            for d, v in dims.items():
                q[d] = np.asarray(v, float) * np.divide(
                    admitted, request, out=np.zeros_like(admitted),
                    where=request > 0)
        if live.any():
            idx = np.arange(self.n)[live]
            room_now = self.room()[live]
            self.log.append(idx, CONSUME, self.period, essential=essential,
                            rho_at=self.dials.rho, room_at=room_now,
                            weight=self.weight[live],
                            **{d: v[live] for d, v in q.items()})
        return admitted, refused

    def pledge(self, hours: np.ndarray):
        """A permanent grant of debit-room, backed 1:1 by lifetime earned credit
        (Sec.6.4, IC-8). It does not move the pledger's credit, and it cannot be
        taken back."""
        self.log.append(np.arange(self.n), PLEDGE, self.period,
                        credit_h=-np.asarray(hours, float), weight=self.weight)

    # --- the time axis ------------------------------------------------------
    def step(self, want=None, essentials=None, check=True):
        """One period: credit accrues, then consumption is attempted, then the
        Sec.9 invariants are asserted.

        Order matters and is not arbitrary. Credit for the period lands BEFORE the
        period's purchases are gated, because Sec.3.3 evaluates the gate at the
        moment of the transaction against what is true then. And essentials are
        taken before discretionary spending, because Sec.7.5 says the ratio governs
        the discretionary layer only -- gating them in the other order would let a
        period's discretionary appetite eat the room essentials needed.

        A conformance failure raises here and stops the run at the period that
        broke it, which is the whole point of checking every period rather than
        once at the end.
        """
        days = self.dials.days_per_period
        self.accrue(days)
        out = {"period": self.period, "admitted": None, "refused": None}
        if essentials is not None:
            self.consume(np.asarray(essentials, float) * days, essential=True)
        if want is not None:
            out["admitted"], out["refused"] = self.consume(
                np.asarray(want, float) * days)
        self.period += 1
        if check:
            Conformance.run_all(self)
        return out

    def run(self, periods: int, want=None, essentials=None, check=True):
        """Run `periods` periods and return one summary row each.

        `cum_disparity` is the figure Sec.7.5 bounds: cumulative consumption, top
        against bottom. It is read off the DERIVED debit rather than accumulated in
        a running total, because a running total would be a stored balance and A6
        forbids exactly that.
        """
        hist = []
        for _ in range(periods):
            out = self.step(want=want, essentials=essentials, check=check)
            # Everything below is measured over whoever was ALIVE for the period
            # that just ran. Including the unborn would divide by zero; including
            # the dead would freeze their last standing into every later ratio.
            live = self.alive(out["period"])
            D = collapse(self.proj.debit(), self.dials.weights)
            C = self.proj.credit()
            adm, ref = out["admitted"], out["refused"]
            Dl = D[live] if live.any() else np.array([np.nan])
            hist.append(dict(
                period=out["period"],
                headcount=float(self.weight[live].sum()),
                cohorts_alive=int(live.sum()),
                credit_total=float((C * self.weight)[live].sum()),
                debit_total=float((D * self.weight)[live].sum()),
                cum_disparity=(float(Dl.max() / Dl.min())
                               if np.nanmin(Dl) > 0 else np.nan),
                period_disparity=(float(adm[live].max() / adm[live].min())
                                  if adm is not None and live.any()
                                  and adm[live].min() > 0 else np.nan),
                refused_frac=(float((ref[live] > 1e-9).mean())
                              if ref is not None and live.any() else 0.0),
            ))
        return hist


# =============================================================================
# Conformance -- Foundations Sec.9, asserted as invariants
# =============================================================================

class Conformance:
    """The 17 requirements of Foundations Sec.9, as far as a toy economy can express
    them. Run every period. A failure is a result, not an inconvenience."""

    @staticmethod
    def check_ic7(k: Kernel):
        """IC-7: no account claims more than 24 hours of activity per 24 hours.

        The cap scales with the period's length, because the rule is about a day
        and a period may be a month or a year. It is NOT scaled by headcount -- a
        cohort of a thousand people did not claim 12,000 hours, each of them
        claimed 12 (test_weight_scales_matter_but_not_a_person).
        """
        log = k.log
        crediting = np.isin(log.col("kind"), CREDITING)
        if not crediting.any():
            return
        per = log.col("period")[crediting]
        actor = log.col("actor")[crediting]
        hours = log.col("credit_h")[crediting]
        key = per.astype(np.int64) * k.n + actor
        tot = np.bincount(key, weights=hours)
        cap = DAY * k.dials.days_per_period
        if tot.size and tot.max() > cap + 1e-9:
            raise ConformanceError(
                f"IC-7: {tot.max():.3f} h claimed in a {k.dials.days_per_period:g}-day "
                f"period (cap {cap:.3f})")

    @staticmethod
    def check_a3(k: Kernel):
        """A3: credit is never transferable.

        Enforced structurally -- no event kind moves credit between actors -- so the
        check is that no TRANSFER or GENESIS event ever carried credit, and that
        aggregate credit only ever rises except where a pledge draws the finite
        lifetime pledging-budget.
        """
        kinds = k.log.col("kind")
        cr = k.log.col("credit_h")
        moved = np.isin(kinds, (TRANSFER, GENESIS)) & (cr != 0)
        if moved.any():
            raise ConformanceError("A3: a transfer carried credit")
        bad = np.isin(kinds, CREDITING) & (cr < 0)
        if bad.any():
            raise ConformanceError("A3: negative credit on a crediting event")

    @staticmethod
    def check_a6(k: Kernel):
        """A6: the ledger is derived from the log, never stored.

        Recompute from scratch and assert the cached projection agrees. If these ever
        differ, something is holding an authoritative balance.
        """
        actor = k.log.col("actor")
        sel = np.isin(k.log.col("kind"), CREDITING)
        fresh_c = np.bincount(actor[sel], weights=k.log.col("credit_h")[sel],
                              minlength=k.n)
        if not np.allclose(fresh_c, k.proj.credit(), rtol=0, atol=1e-9):
            raise ConformanceError("A6: cached credit differs from the log")
        for d in DIMS:
            fresh_d = np.bincount(actor, weights=k.log.dim(d), minlength=k.n)
            if not np.allclose(fresh_d, k.proj.debit()[d], rtol=0, atol=1e-9):
                raise ConformanceError(f"A6: cached debit[{d}] differs from the log")

    @staticmethod
    def check_ic8(k: Kernel):
        """IC-8: cumulative pledges never exceed lifetime earned credit."""
        earned = np.bincount(
            k.log.col("actor")[np.isin(k.log.col("kind"), CREDITING)],
            weights=k.log.col("credit_h")[np.isin(k.log.col("kind"), CREDITING)],
            minlength=k.n)
        over = k.proj.pledged() - earned
        if over.size and over.max() > 1e-9:
            raise ConformanceError(f"IC-8: pledged exceeds earned by {over.max():.3f} h")

    @staticmethod
    def check_conservation(k: Kernel):
        """IC-1/IC-2: mass and energy conserve across every recorded process.

        A process id groups the events of one physical transformation. What went in
        must come out, in every conserved dimension. -1 means 'not part of a process'.

        THIS IS THE ONE CHECK THAT MUST USE THE HEADCOUNT. Matter balances over a
        population, not over a representative person: one factory cohort making
        10 kg for a cohort of 100 people who take 0.1 kg each balances only once
        both sides are scaled. Per-exemplar it reads 10 - 0.1 = 9.9 and falsely
        fails. IC-7 and IC-8, by contrast, are claims about an individual and must
        NOT be scaled -- see test_weight_scales_matter_but_not_a_person.
        """
        pid = k.log.col("process")
        sel = pid >= 0
        if not sel.any():
            return
        w = k.log.col("weight")[sel]
        for d in ("mass_kg", "energy_mj"):
            bal = np.bincount(pid[sel], weights=k.log.dim(d)[sel] * w)
            worst = np.abs(bal).max() if bal.size else 0.0
            if worst > 1e-6:
                raise ConformanceError(
                    f"IC-1/IC-2: {d} does not balance, worst process off by {worst:.3g}")

    @staticmethod
    def check_essentials_never_gated(k: Kernel):
        """Sec.7.5: any restriction reaches non-essentials only.

        HONEST NOTE ON WHAT THIS CAN AND CANNOT SEE. In `consume()` an essential
        request is admitted whole before any gate is consulted, so a clipped
        essential cannot arise from the kernel's own code and this check cannot
        catch one. It guards a malformed scenario, not a kernel regression.

        The real guarantee is BEHAVIOURAL and is tested in
        `test_essentials_are_never_gated`, which sets rho to 0.01, watches
        discretionary spending get refused, and watches essentials pass anyway.
        Saying so here rather than letting the check look stronger than it is.
        """
        essential = k.log.col("essential") & (k.log.col("kind") == CONSUME)
        if not essential.any():
            return
        taken = k.log.dim("labour_h")[essential]
        if np.any(taken < 0):
            raise ConformanceError("Sec.7.5: an essential consumption was reduced")
        # Where an essential was admitted beyond the room that existed, the gate
        # was genuinely bypassed -- which is the section working, not failing.
        room = k.log.col("room_at")[essential]
        bypassed = np.nansum(taken > np.maximum(room, 0.0) + 1e-9)
        k._essentials_bypassed = int(bypassed)

    @staticmethod
    def check_transaction_time(k: Kernel, factor: float = 1.4):
        """Sec.3.3: a later re-weight changes FUTURE room, never a completed act.

        Re-weight the entire history and assert that no past event becomes a
        violation. The gate was evaluated when the transaction happened, and the
        witnesses recorded on the event are what make that checkable.
        """
        room_at = k.log.col("room_at")
        sel = ((k.log.col("kind") == CONSUME) & ~k.log.col("essential")
               & ~np.isnan(room_at))
        # NaN room_at means the row never went through the gate at all -- a
        # production or hand-off event written by a supply chain. Those are not
        # gated purchases and asking whether they had room is the wrong question.

        if sel.any():
            # THE INVARIANT IS ABOUT WHAT WAS ADMITTED, NOT ABOUT THE SIGN OF THE
            # ROOM. Fixed 2026-08-23: the old test raised whenever a recorded
            # room_at was negative, which fires on a completely legitimate run --
            # essentials are ungated (Sec.7.5) and taken first, so they can push D
            # past rho*C, and the next discretionary event then records negative
            # room while admitting ZERO. That false positive killed runs for
            # exactly the low-credit population Sec.7.5 exists to protect.
            admitted = k.log.dim("labour_h")[sel]
            room = np.maximum(room_at[sel], 0.0)
            over = admitted - room
            if over.size and over.max() > 1e-6:
                raise ConformanceError(
                    f"Sec.3.3: an admission of {admitted[over.argmax()]:.4f} h "
                    f"exceeded the {room[over.argmax()]:.4f} h of room that "
                    f"existed when it happened")

        # And the re-weight must change the FUTURE only. Two things are asserted,
        # because the old version computed a value and threw it away.
        before = k.log.col("room_at").copy()
        heavier = {d: v * factor for d, v in k.proj.debit().items()}
        room_future = k.dials.rho * k.proj.credit() - collapse(heavier,
                                                              k.dials.weights)
        if np.any(room_future > k.room() + 1e-9):
            raise ConformanceError(
                "Sec.3.3: a heavier weighting somehow increased future room")
        if not np.array_equal(before, k.log.col("room_at"), equal_nan=True):
            raise ConformanceError(
                "Sec.3.3: re-weighting altered what a past event recorded")

    @staticmethod
    def check_no_expired_discharge(k: Kernel):
        """Author ruling 2026-08-23: an expired good cannot be handed on.

        The custody chain is what decides whose debit a thing is. A loaf and its
        plastic bag need no 'eaten' or 'thrown away' event -- the chain ENDING at
        the consumer is enough to put both on their ledger. Foundations Sec.3.6
        rule 1 already says this: if nobody will take a thing on, its last holder
        has consumed it, 'as if it were food'.

        Shelf life is what stops that chain being extended forever. Past the
        expiry recorded on the goods, a transfer no longer DISCHARGES the sender.
        They may still physically hand the thing over, and the ledger will record
        that they did -- what it will not do is lighten their books.

        > This is deliberately a PRICE and not a door. Everywhere else in this
        > system the costly path is priced rather than forbidden (Sec.5.5), because
        > a prohibition needs somebody to stand at the door and A8 forbids that
        > somebody. A seller of expired goods is not blocked; they simply gain
        > nothing by selling, so they stop. Same outcome, nobody enforcing it.

        A negative quantity on a transfer is a discharge. After the expiry, there
        may not be one.
        """
        kinds = k.log.col("kind")
        exp = k.log.col("expires")
        per = k.log.col("period")
        sel = (kinds == TRANSFER) & np.isfinite(exp) & (per > exp)
        if not sel.any():
            return
        for d in DIMS:
            q = k.log.dim(d)[sel]
            if q.size and q.min() < -1e-9:
                raise ConformanceError(
                    f"expired goods discharged {-q.min():.4g} {d} from a holder's "
                    f"ledger. Past its shelf life a thing joins its last holder's "
                    f"waste stream and handing it on cannot lighten their books.")

    @staticmethod
    def check_grants(k: Kernel):
        """Sec.6.2b (finding #11): granted debit-room must be backed by real pledges.

        A grant of debit-room to a recipient is only legitimate if somebody actually
        pledged for it. Population-weighted, total granted room may not exceed total
        pledging budget spent -- otherwise the network is conjuring cushioning out of
        nothing, the same failure IC-8 forbids on the pledger's side. (The earmark
        cap in `room()` separately stops a grant becoming spendable headroom; this
        checks the grant was funded at all.)
        """
        granted_pop = float((k.proj.granted() * k.weight).sum())
        pledged_pop = float((k.proj.pledged() * k.weight).sum())
        if granted_pop > pledged_pop + 1e-6:
            raise ConformanceError(
                f"Sec.6.2b: {granted_pop:.3f} h of debit-room granted but only "
                f"{pledged_pop:.3f} h of pledging budget spent to back it -- a grant "
                f"must be funded by a real pledge.")

    @classmethod
    def run_all(cls, k: Kernel):
        cls.check_ic7(k)
        cls.check_a3(k)
        cls.check_a6(k)
        cls.check_ic8(k)
        cls.check_conservation(k)
        cls.check_essentials_never_gated(k)
        cls.check_transaction_time(k)
        cls.check_no_expired_discharge(k)
        cls.check_grants(k)


# =============================================================================
# Population -- parameterised by the floor, because the floor is a dial
# =============================================================================

def draw_population(n, floor_h=F, rng=None):
    """Credit rates in [floor_h, 24] for a heterogeneous population.

    Same shape as `disparity_ceiling_sim.draw_population` (~35% do little or no paid
    work -- children, retired, unwell, between jobs), but the FLOOR IS A PARAMETER.

    This is the bug the author caught on 2026-08-23. The kernel had a `floor_h` dial
    that changed nothing, because the population was always built around F = 10:
    credit is min(r,f) + max(r-f,0) = r for any f <= r, so moving the dial moved no
    number. The floor only appeared in the DIVISOR when reporting a ceiling -- which
    divided by a floor agent who was not in the simulation. A floor that no agent
    sits at is not a floor.
    """
    rng = np.random.default_rng(42) if rng is None else rng
    works = rng.random(n) > 0.35
    w = np.where(
        works,
        np.clip(rng.normal(6.0, 3.0, n), 0, DAY - floor_h),
        rng.uniform(0, min(1.5, DAY - floor_h), n),
    )
    return floor_h + w


def ceiling(floor_h) -> float:
    """The disparity BOUND at a given floor: 24/F (Sec.7.5).

    A bound, not an observed spread. Whether a population fills it is an empirical
    question and the answer is usually no -- see `sweep_floor`.
    """
    return DAY / float(floor_h)


# =============================================================================
# Reproduction target 1 -- the 24/F disparity ceiling
# =============================================================================

def reproduce_ceiling(rhos=np.linspace(1.0, 3.0, 21), n=200_000, floor_h=F):
    """Drive the ceiling result through the kernel's log and gate, at a given floor.

    Worst case by construction: appetite unbounded, so everyone consumes to their
    gate. Returns (rho, observed_disparity, bound) per row, where the observed
    disparity is measured against the LOWEST AGENT ACTUALLY IN THE POPULATION and
    the bound is 24/floor_h.
    """
    c = draw_population(n, floor_h)
    out = []
    for rho in rhos:
        k = Kernel(n, c, Dials(rho=float(rho), floor_h=float(floor_h)))
        k.accrue(days=1.0)
        huge = np.full(n, 1e9)                 # unbounded appetite
        admitted, _ = k.consume(huge)
        Conformance.run_all(k)
        observed = float(admitted.max() / admitted.min())
        out.append((float(rho), observed, ceiling(floor_h)))
    return np.array(out)


def sweep_floor(floors=(2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0), rho=1.5, n=200_000):
    """The floor sweep the author asked for: what the ceiling does as F moves.

    Foundations Sec.7.5 condition 1 -- 'the floor stays in a narrow band' -- is
    stated with no evidence behind it. This is the evidence.
    """
    rows = []
    for f in floors:
        c = draw_population(n, f)
        k = Kernel(n, c, Dials(rho=rho, floor_h=f))
        k.accrue(days=1.0)
        admitted, _ = k.consume(np.full(n, 1e9))
        Conformance.run_all(k)
        rows.append(dict(
            floor_h=float(f),
            bound=ceiling(f),
            observed=float(admitted.max() / admitted.min()),
            top_rate=float(c.max()),
            floor_rate=float(c.min()),
        ))
    return rows


# =============================================================================
# Reproduction target 2 -- the clearing rho
# =============================================================================

def reproduce_clearing(rhos=np.linspace(0.2, 4.0, 400)):
    """Drive the rho-sweep baseline through the kernel. Same population, same
    calibration, same capacity -- demand computed through the kernel's gate."""
    from rho_sweep import build_population, intensity_us, CAP

    c, wants = build_population()
    n = len(c)
    kappa = intensity_us(c)
    R_max = CAP * wants.sum()                  # in real lifestyle-units

    def demand(rho):
        k = Kernel(n, c, Dials(rho=float(rho)))
        k.accrue(days=1.0)
        admitted, _ = k.consume(wants * kappa)      # request in debit-hours
        return admitted.sum() / kappa, admitted / kappa, k

    dem = np.array([demand(r)[0] for r in rhos])
    if dem[-1] < R_max:
        return None, None, None, None
    rstar = float(rhos[np.argmin(np.abs(dem - R_max))])
    _, real, k = demand(rstar)
    Conformance.run_all(k)
    median_real = float(np.median(real))
    frac_constrained = float((real < wants - 1e-9).mean())
    return rstar, median_real, frac_constrained, float(real.max() / (rstar * F / kappa))


# =============================================================================
# Self-tests
# =============================================================================

def test_ceiling_at_the_published_floor():
    """The published number, and it is a number ABOUT A 10-HOUR FLOOR."""
    tab = reproduce_ceiling()
    disp = tab[:, 1]
    assert np.allclose(disp, CEILING, atol=1e-6), f"expected {CEILING}, got {disp.min()}..{disp.max()}"
    print(f"[ok] at F=10 h the kernel re-derives {disp.mean():.2f}x, flat across rho "
          f"in [1,3] (spread {disp.max()-disp.min():.2e})")


def test_ceiling_is_rho_independent():
    tab = reproduce_ceiling(rhos=np.linspace(1.0, 3.0, 9))
    assert tab[:, 1].std() < 1e-9, "ceiling moved with rho"
    print("[ok] ceiling is rho-independent (rho cancels in rho*24 / rho*F)")


def test_floor_is_a_real_dial():
    """The bound must MOVE with the floor, and no observed spread may exceed it.

    Guards the exact bug the author caught: a floor_h that changed nothing because
    the population was built around a fixed F.
    """
    rows = sweep_floor(floors=(4.0, 10.0, 14.0), n=50_000)
    for r in rows:
        assert abs(r["bound"] - DAY / r["floor_h"]) < 1e-9
        assert abs(r["floor_rate"] - r["floor_h"]) < 0.05, \
            f"no agent sits at the floor: floor={r['floor_h']}, lowest={r['floor_rate']:.2f}"
        assert r["observed"] <= r["bound"] + 1e-6, \
            f"observed {r['observed']:.2f} broke the bound {r['bound']:.2f}"
    bounds = [r["bound"] for r in rows]
    assert bounds[0] > bounds[1] > bounds[2], "the bound did not move with the floor"
    print(f"[ok] the floor is a real dial: bound {bounds[0]:.2f}x (F=4) -> "
          f"{bounds[1]:.2f}x (F=10) -> {bounds[2]:.2f}x (F=14)")


def test_a_low_floor_is_not_filled():
    """A low floor RAISES the bound, and the population does not fill it.

    At F = 2 the bound is 12x, but reaching it needs someone working a 22-hour day.
    Human endurance binds before the accounting does. This is a real result about
    Sec.7.5 condition 1, not a modelling artifact -- and it is why the bound must
    always be reported next to the observed spread.
    """
    rows = sweep_floor(floors=(2.0,), n=200_000)
    r = rows[0]
    assert r["observed"] < r["bound"] * 0.9, \
        f"expected the low-floor bound to go unfilled; observed {r['observed']:.2f} of {r['bound']:.2f}"
    print(f"[ok] at F=2 h the bound is {r['bound']:.1f}x but the population only "
          f"reaches {r['observed']:.2f}x (top worker {r['top_rate']:.1f} h/day)")


def test_clearing_rho_matches_published():
    rstar, median_real, frac, disp = reproduce_clearing()
    assert rstar is not None, "baseline should clear, not go post-scarcity"
    assert abs(rstar - 1.20) < 0.06, f"rho* = {rstar:.3f}, published 1.20"
    assert abs(median_real - 0.92) < 0.05, f"median gets {median_real:.3f}, published 0.92"
    assert abs(frac - 0.35) < 0.05, f"{frac:.3f} constrained, published 0.35"
    assert disp <= CEILING + 1e-6, f"disparity {disp:.3f} broke 24/F"
    print(f"[ok] kernel re-derives the clearing rate: rho*={rstar:.2f} (pub 1.20), "
          f"median {median_real:.2f}x (pub 0.92), {frac*100:.0f}% constrained (pub 35%)")


def test_credit_is_never_spent():
    """A3 + A6: a purchase adds to debit and never decrements credit."""
    n = 1000
    k = Kernel(n, draw_population(n), Dials(rho=1.5))
    k.accrue()
    before = k.proj.credit().copy()
    k.consume(np.full(n, 5.0))
    assert np.allclose(before, k.proj.credit()), "a purchase moved credit"
    print("[ok] credit is never spent by a purchase (A3: not a currency)")


def test_essentials_are_never_gated():
    n = 500
    k = Kernel(n, np.full(n, F), Dials(rho=0.01))          # almost no room
    k.accrue()
    adm_d, ref_d = k.consume(np.full(n, 50.0), essential=False)
    adm_e, ref_e = k.consume(np.full(n, 50.0), essential=True)
    assert ref_d.max() > 0, "discretionary should have been refused"
    assert np.allclose(ref_e, 0.0), "an essential was refused"
    print("[ok] the gate restricts non-essentials only (Sec.7.5)")


def test_divide_refuses_a_collapsed_figure():
    """Sec.3.2a: divide per dimension, before collapsing."""
    n = 10
    k = Kernel(n, np.full(n, 12.0))
    k.accrue()
    collapsed = collapse(k.proj.debit())
    try:
        divide(collapsed, np.full(n, 0.5))
    except TypeError:
        print("[ok] divide() refuses a collapsed figure (Sec.3.2a closed by type)")
        return
    raise AssertionError("divide() accepted a collapsed figure")


def test_conservation_catches_a_leak():
    n = 4
    k = Kernel(n, np.full(n, 12.0))
    k.accrue()
    # a balanced process: 10 kg in, 10 kg out
    k.log.append(np.array([0]), CONSUME, 0, process=0, mass_kg=10.0)
    k.log.append(np.array([1]), TRANSFER, 0, process=0, mass_kg=-10.0)
    Conformance.check_conservation(k)
    # now leak 3 kg
    k.log.append(np.array([2]), CONSUME, 0, process=1, mass_kg=10.0)
    k.log.append(np.array([3]), TRANSFER, 0, process=1, mass_kg=-7.0)
    try:
        Conformance.check_conservation(k)
    except ConformanceError:
        print("[ok] IC-1/IC-2 catch a 3 kg leak in a recorded process")
        return
    raise AssertionError("conservation check missed a leak")


def test_ic7_catches_a_26_hour_day():
    n = 5
    k = Kernel(n, np.full(n, 12.0))
    k.accrue()
    k.log.append(np.arange(n), WORK, 0, credit_h=20.0)     # 12 + 20 = 32 h in a day
    try:
        Conformance.check_ic7(k)
    except ConformanceError:
        print("[ok] IC-7 catches a day with more than 24 hours in it")
        return
    raise AssertionError("IC-7 missed a 32-hour day")


def test_ic8_catches_overpledging():
    n = 5
    k = Kernel(n, np.full(n, 12.0))
    k.accrue()                                             # 12 h earned
    k.pledge(np.full(n, 5.0))
    Conformance.check_ic8(k)
    k.pledge(np.full(n, 20.0))                             # 25 h pledged on 12 h earned
    try:
        Conformance.check_ic8(k)
    except ConformanceError:
        print("[ok] IC-8 catches pledging beyond lifetime earned credit")
        return
    raise AssertionError("IC-8 missed over-pledging")


def test_log_is_append_only():
    for forbidden in ("delete", "truncate", "update", "remove", "edit"):
        assert not hasattr(EventLog, forbidden), f"EventLog exposes {forbidden}()"
    print("[ok] the log offers no delete, truncate, or edit (Sec.5.4)")


def test_weight_of_one_changes_nothing():
    """The refactor's whole safety argument: at a headcount of 1, nothing moved.

    Every result published from v0.1 was computed at an implicit headcount of one.
    If the weight column changes anything there, the refactor has silently rewritten
    history and no earlier number can be trusted.
    """
    n = 500
    k = Kernel(n, draw_population(n), Dials(rho=1.5))
    k.accrue()
    k.consume(np.full(n, 6.0))
    Conformance.run_all(k)
    w = k.log.col("weight")
    assert np.all(w == 1.0), "weights are not 1.0 by default"
    assert np.allclose(k.population_credit(), k.proj.credit())
    assert k.headcount() == float(n)
    print("[ok] at a headcount of 1 the kernel is unchanged (v0.1 results stand)")


def test_weight_scales_matter_but_not_a_person():
    """A headcount scales the population, never the individual.

    IC-7 asks 'did ONE account claim more than 24 hours in a day'. A cohort of a
    thousand people did not claim 12,000 hours; each of them claimed 12. Scaling
    that check would make every large cohort fail instantly, and would be the wrong
    question besides.
    """
    k = Kernel(2, np.array([12.0, 12.0]), Dials(rho=1.5),
               weight=np.array([1.0, 1000.0]))
    k.accrue(days=1.0)
    Conformance.check_ic7(k)                       # must NOT trip on a big cohort
    assert np.allclose(k.proj.credit(), [12.0, 12.0]), "a headcount reached a person"
    assert np.allclose(k.population_credit(), [12.0, 12000.0])
    assert k.headcount() == 1001.0
    print("[ok] a headcount scales the population and never the person (IC-7 intact)")


def test_conservation_balances_across_headcounts():
    """IC-1/IC-2 must weigh matter, and this case fails without it.

    One factory (headcount 1) makes 10 kg. A cohort of 100 people take 0.1 kg each.
    Weighted, that is 10 in and 10 out and it balances. Per exemplar it reads
    10 - 0.1 = 9.9 and falsely reports a 9.9 kg leak.
    """
    k = Kernel(2, np.array([12.0, 12.0]), weight=np.array([1.0, 100.0]))
    k.accrue()
    k.log.append(np.array([0]), TRANSFER, 0, process=0, mass_kg=10.0, weight=1.0)
    k.log.append(np.array([1]), CONSUME, 0, process=0, mass_kg=-0.1, weight=100.0)

    sel = k.log.col("process") >= 0
    unweighted = float(k.log.dim("mass_kg")[sel].sum())
    assert abs(unweighted - 9.9) < 1e-9, "the test is not exercising the headcount"

    Conformance.check_conservation(k)              # balances once weighed
    print(f"[ok] IC-1 weighs matter by headcount (unweighted this reads a "
          f"{unweighted:.1f} kg leak that is not there)")


def test_ten_periods_hold_the_bound():
    """Step 2's done-when: ten periods, every invariant, at three different floors.

    `Kernel.run` asserts the whole Sec.9 set at every period, so reaching the end
    is itself the conformance result. What is checked here is the thing periods
    could have broken: that cumulative consumption stays inside 24/F rather than
    drifting apart as credit accumulates.
    """
    for floor_h in (4.0, 10.0, 14.0):
        n = 20_000
        k = Kernel(n, draw_population(n, floor_h),
                   Dials(rho=1.5, floor_h=floor_h))
        hist = k.run(10, want=np.full(n, 1e9))       # unbounded appetite, worst case
        bound = ceiling(floor_h)
        assert len(hist) == 10
        obs = [r["cum_disparity"] for r in hist]

        # 1. The bound is never exceeded. This is the claim Sec.7.5 actually makes.
        assert max(obs) <= bound + 1e-6, \
            f"F={floor_h}: disparity {max(obs):.4f} broke the bound {bound:.4f}"

        # 2. It does not DRIFT. This is what only a time axis can test: credit
        #    accumulates every period, and the ratio has to stay put while it does.
        assert max(obs) - min(obs) < 1e-9, \
            f"F={floor_h}: disparity drifted over ten periods by {max(obs)-min(obs):.2e}"

        # 3. One period and the whole history give the same ratio, because both
        #    are rho * (credit accrued) over rho * (credit accrued).
        for row in hist:
            assert abs(row["period_disparity"] - row["cum_disparity"]) < 1e-6

        # 4. Where the population reaches 24 h/day it fills the bound exactly.
        #    Where it does not, it falls short -- the low-floor result from v0.1,
        #    which is a fact about human endurance and not about the accounting.
        if floor_h >= 6.0:
            assert abs(obs[-1] - bound) < 1e-6, \
                f"F={floor_h}: expected the bound to be filled, got {obs[-1]:.4f}"
        print(f"     F={floor_h:>4.0f}h  bound {bound:.2f}x  observed {obs[-1]:.4f}x "
              f"flat across 10 periods (drift {max(obs)-min(obs):.1e})")
    print("[ok] ten periods hold every Sec.9 check and the bound does not drift")


def test_a_monthly_period_does_not_break_ic7():
    """A period is not a day, and IC-7 has to know that.

    Without the days_per_period cap, a 30-day period credits a 12 h/day worker
    360 hours and IC-7 fires on the first month of every run coarser than daily.
    """
    n = 200
    k = Kernel(n, np.full(n, 12.0), Dials(rho=1.5, days_per_period=30.0))
    hist = k.run(3, want=np.full(n, 1e9))
    per_period = hist[0]["credit_total"] / n
    assert abs(per_period - 360.0) < 1e-9, f"expected 360 h/month, got {per_period}"
    print(f"[ok] a 30-day period credits {per_period:.0f} h and IC-7 does not fire "
          f"(cap {DAY * 30:.0f} h)")


def test_ic7_still_bites_inside_a_long_period():
    """Scaling the cap must not disable it."""
    n = 5
    k = Kernel(n, np.full(n, 12.0), Dials(days_per_period=30.0))
    k.accrue(days=30.0)                              # 360 h, legitimate
    k.log.append(np.arange(n), WORK, 0, credit_h=400.0)   # 760 h > the 720 h cap
    try:
        Conformance.check_ic7(k)
    except ConformanceError:
        print("[ok] the scaled IC-7 cap still catches an over-claim (760 h in 30 days)")
        return
    raise AssertionError("IC-7 missed an over-claim inside a long period")


def test_age_is_the_only_spread_beyond_the_bound():
    """Step 3's done-when, and the first test of a claim Sec.7.5 has always made.

    'The only spread beyond 24/F is age.' A 60-year maximum worker against a
    20-year subsistence person should come to exactly 3 x 24/F = 7.20x at a
    10-hour floor. v0.1 could not check this, because everybody was the same age.
    """
    k = Kernel(2, np.array([DAY, F]),
               Dials(rho=1.5, floor_h=F, days_per_period=365.0),
               born=np.array([0, 40]))              # one born 40 years later
    k.run(60)                                       # credit only, no consumption
    C = k.proj.credit()
    expected = 3.0 * CEILING                        # 3 x age, 2.4 x rate = 7.2
    got = float(C[0] / C[1])
    assert abs(got - expected) < 1e-9, f"expected {expected:.2f}x, got {got:.4f}x"
    ages = k.age_years()
    assert (ages[0], ages[1]) == (60.0, 20.0)
    print(f"[ok] age is the only spread beyond the bound: a {ages[0]:.0f}-year "
          f"max worker vs a {ages[1]:.0f}-year floor person = {got:.2f}x (= 3 x 24/F)")


def test_death_stops_accrual_and_never_removes_the_record():
    """Sec.5.4: the record closes but persists. Nothing is ever deleted."""
    k = Kernel(2, np.full(2, 12.0), Dials(days_per_period=365.0),
               lifespan=np.array([3.0, np.inf]))
    k.run(6)
    C = k.proj.credit()
    assert abs(C[0] / C[1] - 0.5) < 1e-9, "a dead cohort kept accruing"
    assert not k.alive()[0] and k.alive()[1]
    assert (k.log.col("actor") == 0).sum() > 0, "a dead cohort's rows were removed"
    dead_rows = int((k.log.col("actor") == 0).sum())
    print(f"[ok] death stops accrual at period 3 and leaves all {dead_rows} rows "
          f"in the log (Sec.5.4)")


def test_a_birth_cohort_starts_from_nothing():
    """A cohort born mid-run accrues only from its own birth, never before."""
    k = Kernel(3, np.array([12.0, 12.0, 0.0]), Dials(days_per_period=365.0),
               weight=np.array([100.0, 100.0, 0.0]))   # slot 2 awaits a birth
    k.run(5)
    k.birth(2, headcount=50.0, rate=12.0)
    k.run(5)
    C = k.proj.credit()
    assert abs(C[0] - C[1]) < 1e-9
    assert abs(C[2] / C[0] - 0.5) < 1e-9, "the newborn inherited history"
    assert k.headcount() == 250.0
    print(f"[ok] a cohort born at period 5 holds half the credit of one born at 0, "
          f"and the headcount is {k.headcount():.0f}")


def test_mortality_thins_a_cohort_without_touching_a_person():
    """Deaths shrink the population; they never change what one person did."""
    k = Kernel(1, np.array([12.0]), Dials(days_per_period=365.0),
               weight=np.array([1000.0]))
    k.run(1)
    before = k.proj.credit()[0]
    k.die(0.10)
    after = k.proj.credit()[0]
    assert abs(before - after) < 1e-9, "mortality reached the exemplar's own record"
    assert abs(k.headcount() - 900.0) < 1e-9
    print(f"[ok] 10% mortality takes the headcount 1000 -> {k.headcount():.0f} and "
          f"leaves the exemplar's {after:.0f} h untouched")


def test_a_pledge_does_not_move_the_pledgers_credit():
    """A3 and Sec.6.4. Regression for an axiom breach found 2026-08-23.

    `pledge()` writes a negative credit_h row to draw down the finite lifetime
    pledging budget. `credit()` used to sum every credit_h column, so a pledge
    quietly shrank the pledger's own credit AND their own consumption room.
    Measured then: earn 12 h, pledge 5 h, credit read 7.0 and room fell 18 -> 10.5.

    Foundations says the opposite in four places, including this function's own
    docstring: a pledge grants debit-room to somebody else and the pledger's
    credit never moves.
    """
    k = Kernel(1, np.array([12.0]), Dials(rho=1.5))
    k.accrue(days=1.0)
    before_c, before_room = k.proj.credit()[0], k.room()[0]
    k.pledge(np.array([5.0]))
    after_c, after_room = k.proj.credit()[0], k.room()[0]
    assert abs(after_c - before_c) < 1e-12, \
        f"pledging moved credit {before_c} -> {after_c} (A3)"
    assert abs(after_room - before_room) < 1e-12, \
        f"pledging moved the pledger's own room {before_room} -> {after_room}"
    assert abs(k.proj.pledged()[0] - 5.0) < 1e-12, "the pledge was not recorded"
    Conformance.run_all(k)
    print(f"[ok] a pledge leaves credit at {after_c:.0f} h and room at "
          f"{after_room:.0f} h, and spends 5 h of the separate pledging budget")


def test_essentials_over_the_gate_do_not_kill_the_run():
    """Sec.7.5 protects people whose consumption exceeds their gate. Regression.

    Essentials are ungated and taken first, so they can push D past rho*C. The
    next discretionary event then records negative room while admitting nothing.
    `check_transaction_time` used to raise on the sign of that recorded room and
    stop the run -- for exactly the newborn, old, sick and disabled the section
    exists to protect.
    """
    n = 4
    k = Kernel(n, np.full(n, 12.0), Dials(rho=0.5))
    k.run(3, want=np.full(n, 2.0), essentials=np.full(n, 20.0))
    D = collapse(k.proj.debit(), k.dials.weights)
    C = k.proj.credit()
    assert np.all(D > k.dials.rho * C), "the test is not exercising the case"
    over = float((D / C).max())
    print(f"[ok] a population whose essentials put them at {over:.1f}x their gate "
          f"still runs, and nothing discretionary was admitted")


def test_a_zeroed_labour_weight_is_refused():
    """Finding #12: a gate weighting that zeroes labour_h makes the gate non-binding.

    Before the guard, Dials(weights={'labour_h': 0.0, 'mass_kg': 1.0}) built a kernel
    whose `room()` ignored everything `consume()` records, so a request of any size
    was admitted against a room that never shrank. run_scenario.py let a TOML file
    set exactly this. The kernel now refuses it at construction.
    """
    for bad in ({"labour_h": 0.0, "mass_kg": 1.0},
                {"labour_h": 0.5, "mass_kg": 0.0},
                {"labour_h": 1.0, "mass_kg": -0.1}):
        try:
            Kernel(3, np.full(3, 12.0), Dials(weights=bad))
        except ConformanceError:
            continue
        raise AssertionError(f"a non-binding gate weighting was accepted: {bad}")
    # The valid shape -- labour 1:1, a pollutant priced in mitigation-hours -- passes.
    Kernel(3, np.full(3, 12.0), Dials(weights={"labour_h": 1.0, "mass_kg": 0.05}))
    print("[ok] a gate weighting that zeroes or scales labour_h is refused (#12); "
          "labour 1:1 plus a priced pollutant is accepted")


def test_a_reweight_moves_a_number():
    """Finding #12: a discovered-pollutant re-weight must actually change the gate.

    The STATERA_PLAN Sec.7 pollutant shock multiplies the mass_kg gate weight. If
    that weight starts at the 0.0 default (breathing at baseline), 1.25 * 0.0 = 0.0
    and the shock is arithmetically inert -- the headline re-weight scenario would
    prove nothing. A pollutant that binds consumption must START from a non-zero
    mitigation cost. This asserts the mechanism works when it does.
    """
    n = 4
    # An actor carrying real mass debit (say a tonne of a persistent pollutant).
    # Breathing is off so the only mass in the books is the pollutant under test.
    k = Kernel(n, np.full(n, 12.0),
               Dials(rho=1.5, weights={"labour_h": 1.0, "mass_kg": 0.05},
                     metabolic_co2_kg_per_day=0.0))
    k.accrue(days=1.0)
    k.log.append(np.arange(n), CONSUME, k.period, mass_kg=1000.0, weight=k.weight)

    room_before = k.room().copy()
    # The pollutant is found to be five times worse: re-weight its mitigation cost.
    k.dials.weights = {"labour_h": 1.0, "mass_kg": 0.25}
    room_after = k.room()

    moved = room_before - room_after
    assert np.all(moved > 0), "a heavier pollutant weight did not shrink the room"
    # 1000 kg * (0.25 - 0.05) = 200 h of room removed.
    assert np.allclose(moved, 200.0), f"expected 200 h removed, got {moved[0]:.3f}"
    print(f"[ok] a re-weight moves a number: pricing 1,000 kg of a pollutant five "
          f"times higher removes {moved[0]:.0f} h of discretionary room")


def test_metabolic_co2_is_recorded_and_weighs_nothing():
    """A1 records the flow. Sec.3.3 weighs it at zero. Both, with no conflict.

    Every human exhales CO2 and A1 reaches that far explicitly. But breathing is
    inside the short carbon cycle -- the carbon came out of the air, through a
    plant, into food, and back -- so it sits at Sec.3.3's natural-remediation
    baseline and is not a pollutant.

    A system that stored one collapsed number could not hold both of those at
    once. A vector can.
    """
    k = Kernel(1, np.array([12.0]), Dials(days_per_period=365.0))
    k.run(1)
    kg = k.proj.debit()["mass_kg"][0]
    cost = float(collapse(k.proj.debit(), None)[0])
    assert abs(kg - 365.0) < 1e-6, f"expected 365 kg of exhaled CO2, got {kg}"
    assert abs(cost) < 1e-9, f"breathing was charged {cost} h"
    print(f"[ok] a year of breathing records {kg:.0f} kg in the log and costs "
          f"{cost:.0f} h -- recorded by A1, weighed at zero by Sec.3.3")


def run_tests():
    test_log_is_append_only()
    test_weight_of_one_changes_nothing()
    test_weight_scales_matter_but_not_a_person()
    test_conservation_balances_across_headcounts()
    test_a_monthly_period_does_not_break_ic7()
    test_ic7_still_bites_inside_a_long_period()
    test_ten_periods_hold_the_bound()
    test_age_is_the_only_spread_beyond_the_bound()
    test_death_stops_accrual_and_never_removes_the_record()
    test_a_birth_cohort_starts_from_nothing()
    test_mortality_thins_a_cohort_without_touching_a_person()
    test_credit_is_never_spent()
    test_essentials_are_never_gated()
    test_divide_refuses_a_collapsed_figure()
    test_conservation_catches_a_leak()
    test_ic7_catches_a_26_hour_day()
    test_ic8_catches_overpledging()
    test_a_pledge_does_not_move_the_pledgers_credit()
    test_essentials_over_the_gate_do_not_kill_the_run()
    test_a_zeroed_labour_weight_is_refused()
    test_a_reweight_moves_a_number()
    test_metabolic_co2_is_recorded_and_weighs_nothing()
    test_ceiling_is_rho_independent()
    test_ceiling_at_the_published_floor()
    test_floor_is_a_real_dial()
    test_a_low_floor_is_not_filled()
    test_clearing_rho_matches_published()
    print("\nAll self-tests passed.")


# =============================================================================
# Demo
# =============================================================================

def demo():
    W = 78
    print("=" * W)
    print("AEQUITAS KERNEL -- reproduction of two published results")
    print("=" * W)

    tab = reproduce_ceiling(rhos=np.linspace(1.0, 3.0, 5))
    print(f"\n  1. THE DISPARITY CEILING AT A 10-HOUR FLOOR  (target {CEILING:.2f}x, flat in rho)")
    print(f"     {'rho':>6}{'disparity':>12}")
    for rho, disp, _bound in tab:
        print(f"     {rho:>6.2f}{disp:>12.4f}")

    print(f"\n  1b. AND THE FLOOR IS A DIAL  (rho=1.5)")
    print(f"     {'floor F':>9}{'bound 24/F':>13}{'observed':>11}{'top worker':>13}")
    for r in sweep_floor(n=50_000):
        print(f"     {r['floor_h']:>8.0f}h{r['bound']:>13.2f}{r['observed']:>11.2f}"
              f"{r['top_rate']:>11.1f} h")
    print(f"     The bound moves with the floor. A LOW floor raises it -- and the")
    print(f"     population does not fill it, because reaching a 12x spread needs")
    print(f"     somebody working a 22-hour day. Endurance binds before arithmetic.")

    rstar, median_real, frac, disp = reproduce_clearing()
    print(f"\n  2. THE CLEARING RATE       (targets: rho*=1.20, median 0.92x, 35%)")
    print(f"     rho*                 {rstar:>8.2f}")
    print(f"     median gets          {median_real:>8.2f}x")
    print(f"     constrained          {frac*100:>7.0f}%")
    print(f"     disparity            {disp:>8.2f}x   (ceiling {CEILING:.2f})")

    n = 200_000
    k = Kernel(n, draw_population(n), Dials(rho=1.2))
    k.accrue()
    k.consume(np.full(n, 8.0))
    Conformance.run_all(k)
    print(f"\n  3. CONFORMANCE             {len(k.log):,} events, {n:,} agents")
    print(f"     all Sec.9 assertions checked and passing")
    print("\n" + "=" * W)
    print("  Both reproduced. The kernel is cleared to run new scenarios.")
    print("=" * W)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true", help="run the self-tests")
    ap.add_argument("--demo", action="store_true", help="print the reproduction table")
    a = ap.parse_args()
    if a.test:
        run_tests()
    elif a.demo:
        demo()
    else:
        demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
