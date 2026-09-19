#!/usr/bin/env python3
"""
The consumption gate, minimal and current.
=============================================================================

WHY THIS FILE EXISTS
--------------------
`stable_band.py` used to import its kernel from `06-simulation/statera/`.
**Statera was retired on 2026-09-18** (author ruling) because it encodes the
pledge rule withdrawn that day: its `room()` capped a pledge's grant at the
recipient's own creation-cost and never let it become spendable, which the
ruling replaced.

This module is the part `stable_band.py` actually exercised, re-implemented
against the CURRENT spec. It is deliberately small and does one thing.

THE GATE
--------
    D <= rho * (C + P)

    C  cumulative credit, in hours. Never decremented by a purchase (A3).
    D  cumulative debit, collapsed to hours.
    P  COMMITTED pledged room granted to this account by other people.
    rho the network's debit tolerance (A8: a network sets it, Aequitas does not).

`P` defaults to zero everywhere, which is the case `stable_band.py` runs.
`pledge_band.py` does not use it either: it expresses a pledge density `p` as
an effective tolerance `rho*(1+p)`, which is exact, so the `P` column stays
zero there too. It is present because the gate has the term.

WHAT THIS IS NOT
----------------
Not a simulator. There is no event log, no cohort birth or death, no vector
debit, no weighting model, no re-weighting, no chains. Statera had all of
those. **If a future study needs them it needs a new simulator, not this.**
"""

import numpy as np

DAY = 24.0


class ConformanceError(AssertionError):
    """A rule that is never configurable was broken."""


class Dials:
    """Network-level settings. Aequitas uses these and never sets them (A8)."""

    def __init__(self, rho=1.2, floor_h=10.0):
        self.rho = float(rho)
        self.floor_h = float(floor_h)


class Kernel:
    """Agents, two running totals, and the gate."""

    def __init__(self, n_agents, credit_rate, dials=None):
        rate = np.asarray(credit_rate, float)
        if np.any(rate < 0) or np.any(rate > DAY):
            raise ConformanceError("IC-7: a credit rate outside [0, 24] h/day")
        self.n = int(n_agents)
        self.rate = rate
        self.dials = dials or Dials()
        self.C = np.zeros(self.n)          # credit, hours
        self.D = np.zeros(self.n)          # debit, hours
        self.P = np.zeros(self.n)          # COMMITTED pledged room, hours
        self.period = 0

    # --- credit -------------------------------------------------------------
    def accrue(self, days=1.0):
        """One period of credit.

        Split into the self-care floor and the productive remainder, which is
        what the two rows mean, even though they sum to `rate * days`. Keeping
        them apart is what makes `test_the_floor_is_really_the_floor` able to
        fail.
        """
        floor = np.minimum(self.rate, self.dials.floor_h) * days
        work = np.maximum(self.rate - self.dials.floor_h, 0.0) * days
        self.C += floor + work
        self.period += 1

    def grant(self, hours):
        """Commit pledged room to these accounts. Permanent, never returned."""
        h = np.asarray(hours, float)
        if np.any(h < 0):
            raise ConformanceError("committed room cannot be negative")
        self.P += h

    # --- the gate -----------------------------------------------------------
    def room(self):
        """Discretionary room remaining: rho*(C + P) - D.

        A ratio re-checked at every event, never a balance drawn down. A
        purchase adds to D and takes nothing from C, so nobody can run a stored
        lump down to zero -- there is no stored lump.
        """
        return self.dials.rho * (self.C + self.P) - self.D

    def consume(self, request_h, essential=False):
        """Attempt consumption. Returns (admitted, refused), in hours.

        Essentials are never gated: the ratio governs the discretionary layer
        only, or it would fall hardest on the newborn, the old and the sick.
        """
        request = np.asarray(request_h, float)
        if essential:
            admitted = request
        else:
            admitted = np.clip(np.minimum(request, self.room()), 0.0, None)
        self.D += admitted
        return admitted, request - admitted


class Conformance:
    """The invariants, asserted every period."""

    @staticmethod
    def ic7_day_is_24_hours(k):
        if np.any(k.rate > DAY + 1e-9):
            raise ConformanceError("IC-7: more than 24 h of activity in 24 h")

    @staticmethod
    def credit_only_rises(k):
        if np.any(k.C < -1e-9):
            raise ConformanceError("credit went negative")

    @staticmethod
    def debit_only_rises(k):
        if np.any(k.D < -1e-9):
            raise ConformanceError("debit went negative")

    @staticmethod
    def gate_was_respected(k):
        if np.any(k.room() < -1e-6):
            raise ConformanceError("an account is past its own gate")

    @staticmethod
    def pledged_room_is_backed(k):
        """IC-8: committed room across the network cannot exceed earned credit."""
        if k.P.sum() > k.C.sum() + 1e-6:
            raise ConformanceError("IC-8: committed room exceeds earned credit")

    @classmethod
    def run_all(cls, k):
        cls.ic7_day_is_24_hours(k)
        cls.credit_only_rises(k)
        cls.debit_only_rises(k)
        cls.gate_was_respected(k)
        cls.pledged_room_is_backed(k)


# =============================================================================
# self-tests -- each can fail
# =============================================================================

def test_ic7_rejects_an_impossible_rate():
    try:
        Kernel(1, np.array([25.0]))
    except ConformanceError:
        print("[ok] IC-7 rejects a credit rate above 24 h/day")
        return
    raise AssertionError("IC-7 did not fire")


def test_the_gate_actually_binds():
    k = Kernel(1, np.array([10.0]), Dials(rho=1.2, floor_h=10.0))
    k.accrue(1.0)                                  # C = 10
    admitted, refused = k.consume(np.array([100.0]))
    assert abs(admitted[0] - 12.0) < 1e-9, admitted
    assert abs(refused[0] - 88.0) < 1e-9, refused
    print(f"[ok] the gate binds: asked 100 h at rho=1.2 on 10 h of credit, "
          f"admitted {admitted[0]:.1f}")


def test_a_purchase_does_not_reduce_credit():
    k = Kernel(1, np.array([10.0]), Dials(rho=1.2, floor_h=10.0))
    k.accrue(1.0)
    before = k.C.copy()
    k.consume(np.array([5.0]))
    assert np.array_equal(k.C, before), (before, k.C)
    print("[ok] a purchase adds to debit and takes nothing from credit (A3)")


def test_committed_room_widens_the_gate():
    k = Kernel(1, np.array([10.0]), Dials(rho=1.2, floor_h=10.0))
    k.accrue(1.0)
    r0 = k.room()[0]
    k.grant(np.array([10.0]))
    r1 = k.room()[0]
    assert abs(r1 - r0 - 12.0) < 1e-9, (r0, r1)
    print(f"[ok] 10 h of committed room widens the gate by rho*10 = "
          f"{r1 - r0:.1f} h, not by 10")


def test_ic8_can_fail():
    k = Kernel(1, np.array([10.0]), Dials(rho=1.2, floor_h=10.0))
    k.accrue(1.0)                                  # C = 10
    k.grant(np.array([50.0]))                      # more room than credit backs
    try:
        Conformance.run_all(k)
    except ConformanceError:
        print("[ok] IC-8 fires when committed room exceeds earned credit")
        return
    raise AssertionError("IC-8 did not fire")


def test_the_floor_is_really_the_floor():
    """Someone who does nothing still accrues, and someone who works accrues more."""
    k = Kernel(2, np.array([10.0, 18.0]), Dials(rho=1.2, floor_h=10.0))
    k.accrue(1.0)
    assert abs(k.C[0] - 10.0) < 1e-9, k.C
    assert abs(k.C[1] - 18.0) < 1e-9, k.C
    print("[ok] the floor credits a floor-only life 10 h and a working one 18 h")


def run_tests():
    test_ic7_rejects_an_impossible_rate()
    test_the_gate_actually_binds()
    test_a_purchase_does_not_reduce_credit()
    test_committed_room_widens_the_gate()
    test_ic8_can_fail()
    test_the_floor_is_really_the_floor()
    print("\nAll self-tests passed.")


if __name__ == "__main__":
    run_tests()
