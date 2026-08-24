"""
chains.py -- the five exemplar chains, recorded into STATERA.

WHAT THIS IS. Step 4 of `STATERA_PLAN_v0.2.md`. Five worked supply chains --
housing, transport, food, healthcare, entertainment -- covering 82% of what a
person materially consumes. Each one is modelled process by process so that the
mechanisms it exercises are actually run rather than asserted.

    python chains.py --test
    python chains.py --demo

WHAT `Chain` IS. A RECORDER, NOT A SECOND ENGINE. It appends correctly-shaped
events into a Statera log and the ordinary `Conformance` checks then police them.
It computes no standing, no gate, and no split of its own. If it ever did, there
would be two implementations of Aequitas and they would drift.

WHY CHAINS AND NOT COEFFICIENTS. A coefficient asserts a number. A chain produces
one, and while producing it, it has to satisfy four closure rules that a single
aggregate figure never touches:

    IC-1 / IC-2   mass and energy balance across every process
    IC-3          every parcel came from somewhere -- a reservoir or a genesis entry
    IC-4          every parcel went somewhere -- product, co-product, or pollution
    Sec.6.4a      a maker's credit realises when a receiver accepts the goods

WHAT THE NUMBERS ARE. PLACEHOLDERS, AND LABELLED AS SUCH. Every figure below
carries `basis="invented"` unless a source is named. Their job in step 4 is to
exercise the machinery. Calibration against real physical data is step 5, and it
is blocked on a download (Sec.4 of the plan). NOTHING HERE IS A RESULT ABOUT THE
WORLD, and the demo says so on its own face.

THE SIGN CONVENTION, and it is the same one the kernel already uses:

    positive  = this actor TOOK IT ON
    negative  = this actor PASSED IT ON

So a process that takes 10 kg and makes 8 kg of product plus 2 kg of waste
records -10, +8, +2 and sums to zero. Conservation and debit are then the same
arithmetic read two ways, which is why no separate bookkeeping is needed.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field

import numpy as np

from statera import (Kernel, Dials, Conformance, ConformanceError, EventLog,
                     DIMS, DAY, F, WORK, CONSUME, TRANSFER, GENESIS, PLEDGE,
                     collapse)

TOL = 1e-6


class ChainError(ValueError):
    """A chain is malformed. Say which process and which dimension."""


# =============================================================================
# The recorder
# =============================================================================

@dataclass
class Chain:
    """Builds a physically-closed supply chain inside a Statera log."""
    k: Kernel
    name: str
    basis: str = "invented"          # Sec.5.1a: measured | modelled | invented
    source: str = "placeholder figures, step 4"
    _pid: int = field(default=0, init=False)
    steps: list = field(default_factory=list, init=False)

    # --- origin (IC-3) ------------------------------------------------------
    def extract(self, operator: int, labour_h: float, note: str = "", **dims):
        """A parcel enters from a reservoir -- the earth, a well, a forest.

        Deliberately NOT process-tagged. A reservoir extraction is a legitimate
        terminus for backward origin-tracing (IC-3) alongside a genesis entry, so
        there is no counterparty row for it to balance against. Matter appearing
        here did not come from nowhere; it came from the world, which is what an
        origin terminus means.
        """
        self._credit(operator, labour_h, f"extract {note}")
        self.k.log.append(np.array([operator]), GENESIS, self.k.period,
                          weight=self.k.weight[operator], **_pos(dims))
        self.steps.append(("extract", note, dict(dims), labour_h))
        return self

    # --- transformation (IC-1, IC-2, IC-4) ----------------------------------
    def process(self, operator: int, labour_h: float, takes: dict, makes: dict,
                pollutes: dict = None, note: str = ""):
        """One physical transformation, and it must balance in every conserved
        dimension.

        `pollutes` is not an afterthought and not a separate category. Sec.3.4a:
        waste outputs are co-products like any other, and counting them is what
        removes the question of who absorbs an unwanted output. A process whose
        mass does not balance is one that forgot its waste.
        """
        pollutes = pollutes or {}
        for d in ("mass_kg", "energy_mj"):
            got = (sum(v.get(d, 0.0) for v in makes.values())
                   + pollutes.get(d, 0.0) - takes.get(d, 0.0))
            if abs(got) > TOL:
                raise ChainError(
                    f"{self.name} / '{note}': {d} does not balance by {got:+.4g}. "
                    f"In {takes.get(d, 0.0):g}, out "
                    f"{sum(v.get(d, 0.0) for v in makes.values()):g} product + "
                    f"{pollutes.get(d, 0.0):g} waste. A process that will not "
                    f"balance has usually forgotten where its waste went (IC-4).")

        self._credit(operator, labour_h, f"process {note}")
        pid = self._pid
        self._pid += 1
        w = self.k.weight[operator]
        self.k.log.append(np.array([operator]), CONSUME, self.k.period, process=pid,
                          weight=w, **_neg(takes))
        for out, q in makes.items():
            self.k.log.append(np.array([operator]), TRANSFER, self.k.period,
                              process=pid, weight=w, **_pos(q))
        if pollutes:
            # Sec.3.2b: this one never transfers. It is permanent on the causer,
            # and `handoff` has no way to move it.
            self.k.log.append(np.array([operator]), CONSUME, self.k.period,
                              process=pid, weight=w, **_pos(pollutes))
        self.steps.append(("process", note, dict(takes), labour_h))
        return self

    # --- hand-off (Sec.6.4a, Sec.3.2) ---------------------------------------
    def handoff(self, frm: int, to: int, labour_h: float = 0.0, note: str = "",
                expires: float = np.inf, **dims):
        """Property debit follows possession -- unless the goods have expired.

        Three things at once (Sec.6.4a): the receiver's acceptance verifies the
        goods are real, the embodied material moves to them, and any carrying
        labour is credited to whoever did it. Pollution is not among the things
        that can be passed, by construction -- there is no argument to name it.

        `expires` is the last period at which this parcel can still be handed on.
        PAST IT THE HAND-OFF IS REFUSED. The goods have joined the last holder's
        waste stream, and getting rid of them is `dispose`, which is a service and
        not a transfer of property.

        WHY A HARD REFUSAL AND NOT A PRICED PATH (corrected 2026-08-23). An
        earlier version recorded the movement with zero quantities, reasoning that
        this system prices costly paths rather than forbidding them, and that
        compost or a food bank might be legitimate reasons to move expired goods.
        Both parts of that were wrong.

          * Compost is not a hand-off. WASTE DISPOSAL IS A SERVICE WITH A COST
            (Sec.3.6: recyclers are credited for the work of reducing pollutants),
            so it has its own event shape and never needed this one.
          * A food bank relying on gifted day-old bread is a symptom of the exact
            scarcity Aequitas claims to remove. Essential provision is
            unconditional (Sec.7.5). If somebody needs charity for bread, the
            system has failed, and modelling the failure as a feature is backwards.
          * And "a prohibition needs somebody at the door" confused A RULE THAT
            FORBIDS with AN INSTITUTION THAT ENFORCES. IC-7 forbids a 25-hour day
            and no institution guards it: the check is the enforcement and anybody
            can run it. That is the A8-clean shape of a prohibition, and this is
            one -- `Conformance.check_no_expired_discharge` makes a log carrying
            such a transfer non-conformant for everyone who recomputes it.
        """
        if np.isfinite(expires) and self.k.period > expires:
            raise ChainError(
                f"{self.name} / '{note}': these goods expired at period "
                f"{expires:g} and it is now {self.k.period}. They are the holder's "
                f"waste stream now and custody cannot be handed on. Getting rid of "
                f"them is `dispose`, which is a service with a cost.")
        if labour_h:
            self._credit(frm, labour_h, f"carry {note}")
        w_from, w_to = self.k.weight[frm], self.k.weight[to]
        self.k.log.append(np.array([frm]), TRANSFER, self.k.period,
                          weight=w_from, expires=expires, **_neg(dims))
        self.k.log.append(np.array([to]), TRANSFER, self.k.period,
                          weight=w_to, expires=expires, **_pos(dims))
        self.steps.append(("handoff", note, dict(dims), labour_h))
        return self

    # --- waste disposal (Sec.3.6) -------------------------------------------
    def dispose(self, holder: int, processor: int, labour_h: float,
                recycled: bool = False, note: str = "", **dims):
        """Getting rid of waste. A SERVICE BOUGHT, not a hand-off of property.

        Author ruling 2026-08-23. Three things happen and none of them is a
        property transfer:

          1. The processor is CREDITED for the work (Sec.3.6: recyclers are
             credited for reducing pollutants).
          2. The holder TAKES ON the cost of that work, like any service.
          3. The material itself does not move -- unless it is genuinely recycled.

        `recycled` is the one case where matter does move on, and Sec.3.6 rule 3
        governs it: the ATOMS carry their property debit forward and re-enter as a
        low-cost co-input, but they do NOT carry prior producers' pollution, which
        never transferred in the first place (Sec.3.2b). Landfill is not recycling:
        there the last holder keeps the lot.
        """
        self._credit(processor, labour_h, f"dispose {note}")
        self.k.log.append(np.array([holder]), CONSUME, self.k.period,
                          weight=self.k.weight[holder], labour_h=float(labour_h))
        if recycled and dims:
            self.k.log.append(np.array([holder]), TRANSFER, self.k.period,
                              weight=self.k.weight[holder], **_neg(dims))
            self.k.log.append(np.array([processor]), TRANSFER, self.k.period,
                              weight=self.k.weight[processor], **_pos(dims))
        self.steps.append(("dispose" + (" (recycled)" if recycled else ""),
                           note, dict(dims), labour_h))
        return self

    # --- fate (IC-4) --------------------------------------------------------
    def consumed_by(self, who: int, note: str = "", **dims):
        """Something NOT previously handed over is consumed. Adds debit.

        Use this for a service: a patient receives care, and no object changed
        hands beforehand. Do NOT use it for a good the actor already holds -- that
        is `terminus`, and confusing the two double-counts.
        """
        self.k.log.append(np.array([who]), CONSUME, self.k.period,
                          weight=self.k.weight[who], **_pos(dims))
        self.steps.append(("consume", note, dict(dims), 0.0))
        return self

    # NOTE, 2026-08-23. There is deliberately no `consumed`/`terminus`/`discarded`
    # method here, and an earlier draft that had one was wrong.
    #
    # AUTHOR RULING: THE CUSTODY CHAIN ENDING IS THE FATE. A loaf of bread in a
    # plastic bag needs no 'eaten' event and no 'thrown away' event. Both the loaf
    # and the bag took resources; both chains stop at the consumer; that is enough
    # to put both on the consumer's ledger. Hand the bread on instead and log the
    # resale, and the debit moves like any property.
    #
    # This is Foundations Sec.3.6 rule 1, which already said it: if nobody will
    # take a thing on, its last holder has consumed it and holds its debit
    # forever, 'as if it were food'.
    #
    # It also retires a limitation this file recorded yesterday -- that Statera
    # cannot tell property debit from consumption debit. IT DOES NOT NEED TO.
    # Whether a thing was eaten or is merely still owned changes nothing about
    # whose ledger it sits on, and the only question the accounting ever asks is
    # whose ledger. What DOES still transfer separately is producer-side pollution
    # (Sec.3.2b), and that is modelled by never handing it on.

    # --- internals ----------------------------------------------------------
    def _credit(self, operator: int, hours: float, note: str):
        if hours <= 0:
            return
        cap = DAY * self.k.dials.days_per_period
        if hours > cap + 1e-9:
            raise ChainError(
                f"{self.name} / '{note}': {hours:g} h credited to one account in a "
                f"{self.k.dials.days_per_period:g}-day period, over the IC-7 cap of "
                f"{cap:g} h. Spread the work over more people or more periods.")
        self.k.log.append(np.array([operator]), WORK, self.k.period,
                          credit_h=hours, weight=self.k.weight[operator])

    def cost_to(self, who: int) -> float:
        """Collapsed debit standing on one actor. Reporting, not a rule."""
        return float(collapse(self.k.proj.debit(), self.k.dials.weights)[who])


def _pos(d: dict) -> dict:
    return {k: abs(float(v)) for k, v in d.items() if k in DIMS}


def _neg(d: dict) -> dict:
    return {k: -abs(float(v)) for k, v in d.items() if k in DIMS}


# =============================================================================
# Front-loading (Sec.6.2, Sec.6.2a) -- the rule three of the five chains test
# =============================================================================

def frontload(k: Kernel, bearer: int, cost_h: float, pledger: int = None,
              pledged_h: float = 0.0, note: str = ""):
    """A large up-front cost with a diffuse benefit, carried WHERE IT IS INCURRED.

    THE POINT IS WHAT THIS FUNCTION DOES NOT RETURN. It hands back no per-unit
    figure, because there is none: nothing here is ever divided by a number of
    patients, viewers, or years. That absence is the Front-Loading Rule
    (Sec.6.2a), and it is what dissolved OP-11, OP-5, OP-21 and OP-23.

    Pledges cushion the bite without shrinking the debit -- nothing may vanish
    (A1). They grant debit-room, drawn permanently from the PLEDGER's finite
    lifetime budget (Sec.6.4, IC-8).

    THE PLEDGE IS RECORDED ON THE PLEDGER, NOT THE BEARER, and getting this wrong
    is how the first draft of this file failed. It pledged 8,000 hours in the
    trainee doctor's own name, and IC-8 refused the whole chain: cumulative
    pledges may never exceed LIFETIME EARNED CREDIT, and a student has not earned
    any. That is the correct answer and it is the point. Society pledges for
    doctors to exist; the student is who the pledges are spent ON.
    """
    k.log.append(np.array([bearer]), CONSUME, k.period, labour_h=float(cost_h),
                 weight=k.weight[bearer])
    if pledged_h:
        if pledger is None:
            raise ChainError("a pledge needs a pledger who has earned the credit")
        k.log.append(np.array([pledger]), PLEDGE, k.period,
                     credit_h=-float(pledged_h), weight=k.weight[pledger])
    return None          # deliberately. There is no per-unit number to hand back.


# =============================================================================
# The five chains
# =============================================================================
# Actor slots used by every chain below.
FARMER, CARRIER, SHOP, EATER = 0, 1, 2, 3
BUILDER, HOLDER_A, HOLDER_B = 4, 5, 6
REFINER, DRIVER = 7, 8
DOCTOR, TEACHER, PATIENT = 9, 10, 11
CREW, PROJECTIONIST, VIEWER = 12, 13, 14
PLEDGERS = 15
N_ACTORS = 16


def _world(rho=1.5, floor_h=F, days=365.0, warmup=120) -> Kernel:
    """A small world with one exemplar per role, headcount 1.

    `warmup` periods of accrual run first, because a pledge must be backed 1:1 by
    LIFETIME earned credit (IC-8). A society that has never worked cannot pledge
    for anything, and the front-loading chains need somebody who can.
    """
    # Respiration is switched off in these worlds ON PURPOSE. Every living person
    # really does exhale ~1 kg of CO2 a day and Statera records it by default
    # (A1). But these chains are isolating GOODS flows, and 120 warm-up years of
    # breathing would put ~44,000 kg on every actor and swamp every kilogram
    # assertion below. Turning it off here is a choice about a test fixture, not a
    # claim that breathing is free.
    k = Kernel(N_ACTORS, np.full(N_ACTORS, 12.0),
               Dials(rho=rho, floor_h=floor_h, days_per_period=days,
                     metabolic_co2_kg_per_day=0.0))
    for _ in range(warmup):
        k.accrue(days=days)
        k.period += 1
    return k


def food_chain(k: Kernel) -> Chain:
    """Wheat -> flour -> bread, and the farmer keeps the runoff.

    Tests Sec.3.4a (a joint process splits by where its inputs physically went)
    and Sec.3.2b (pollution stays permanently on its causer and never rides the
    product to the shopper).
    """
    c = Chain(k, "food")
    c.extract(FARMER, labour_h=40.0, note="grow wheat",
              mass_kg=1000.0, energy_mj=500.0)
    # One process, three outputs: flour, bran, and nitrogen runoff. All counted.
    c.process(FARMER, labour_h=8.0, note="mill",
              takes={"mass_kg": 1000.0, "energy_mj": 500.0},
              makes={"flour": {"mass_kg": 780.0, "energy_mj": 100.0},
                     "bran":  {"mass_kg": 200.0, "energy_mj": 20.0}},
              pollutes={"mass_kg": 20.0, "energy_mj": 380.0})   # runoff + waste heat
    c.handoff(FARMER, CARRIER, labour_h=2.0, note="to the carrier", mass_kg=780.0)
    c.handoff(CARRIER, SHOP, labour_h=1.0, note="to the shop", mass_kg=780.0)
    # The bread and its bag reach the eater and the chain stops there. No 'eaten'
    # event and no 'thrown away' event: the chain ENDING is what puts both on the
    # eater's ledger (Sec.3.6 rule 1).
    c.handoff(SHOP, EATER, note="sold", mass_kg=780.0,
              expires=k.period + 1)          # bread keeps for one period
    return c


def housing_chain(k: Kernel) -> Chain:
    """A house built, then held by two people in turn.

    Tests Sec.6.2b (creation-cost splits by holding time, each holder's share
    permanent) and Sec.3.2 (embodied material discharges on transfer).
    """
    c = Chain(k, "housing")
    c.extract(BUILDER, labour_h=200.0, note="materials",
              mass_kg=150_000.0, energy_mj=400_000.0)
    c.process(BUILDER, labour_h=1800.0, note="build",
              takes={"mass_kg": 150_000.0, "energy_mj": 400_000.0},
              makes={"house": {"mass_kg": 145_000.0, "energy_mj": 0.0}},
              pollutes={"mass_kg": 5_000.0, "energy_mj": 400_000.0})
    c.handoff(BUILDER, HOLDER_A, note="first owner", mass_kg=145_000.0)
    c.handoff(HOLDER_A, HOLDER_B, note="sold on", mass_kg=145_000.0)
    return c


def transport_chain(k: Kernel) -> Chain:
    """Crude -> petrol -> a journey, and the driver owns the tailpipe.

    Tests Sec.3.2b's non-cascade: the refinery's process emissions stay on the
    refinery, the combustion emissions fall on whoever burns the fuel, and
    neither reaches the person receiving goods a truck delivered.
    """
    c = Chain(k, "transport")
    c.extract(REFINER, labour_h=30.0, note="crude",
              mass_kg=3000.0, energy_mj=126_000.0)
    c.process(REFINER, labour_h=20.0, note="refine",
              takes={"mass_kg": 3000.0, "energy_mj": 126_000.0},
              makes={"petrol": {"mass_kg": 2400.0, "energy_mj": 105_000.0}},
              pollutes={"mass_kg": 600.0, "energy_mj": 21_000.0})
    c.handoff(REFINER, DRIVER, note="fuelled up", mass_kg=2400.0)
    # Burning it is the driver's act, and the CO2 is the driver's forever.
    c.process(DRIVER, labour_h=60.0, note="drive",
              takes={"mass_kg": 2400.0, "energy_mj": 0.0},
              makes={},
              pollutes={"mass_kg": 2400.0, "energy_mj": 0.0})
    return c


def healthcare_chain(k: Kernel):
    """Train a doctor, then treat a thousand patients.

    THE SHARP TEST OF THE WHOLE STEP. Sec.6.2: the doctor's education is carried
    when it happens and never amortised onto whoever they later treat. Returns
    the figures the test needs to prove the education is absent.
    """
    c = Chain(k, "healthcare")
    training_h = 10_000.0
    # Teaching is real work and the teacher is credited for it.
    c._credit(TEACHER, 3000.0, "teach")
    frontload(k, DOCTOR, cost_h=training_h, pledger=PLEDGERS, pledged_h=8000.0,
              note="medical school")

    visits = 1000
    per_visit_labour = 0.5
    per_visit_materials = {"mass_kg": 0.2, "energy_mj": 3.0}
    for _ in range(visits):
        c.process(DOCTOR, labour_h=per_visit_labour, note="visit",
                  takes=dict(per_visit_materials),
                  makes={},
                  pollutes=dict(per_visit_materials))
    c.consumed_by(PATIENT, note="care received",
                  labour_h=per_visit_labour * visits)
    bill = per_visit_labour * visits
    return c, dict(training_h=training_h, visits=visits, bill_h=bill,
                   amortised_h=bill + training_h)


def entertainment_chain(k: Kernel):
    """Make a film, then show it a million times.

    Sec.6.2a's media case: the viewer pays DELIVERY ONLY -- the projectionist's
    hours, the power, the bandwidth. Not the film.
    """
    c = Chain(k, "entertainment")
    production_h = 500_000.0
    frontload(k, CREW, cost_h=production_h, pledger=PLEDGERS, pledged_h=450_000.0,
              note="production")

    showings = 1_000_000
    per_showing_labour = 0.002          # projectionist time per viewing
    c._credit(PROJECTIONIST, per_showing_labour * showings, "project")
    c.consumed_by(VIEWER, note="watched", energy_mj=0.5 * showings)
    ticket = per_showing_labour
    return c, dict(production_h=production_h, showings=showings,
                   ticket_h=ticket,
                   amortised_h=ticket + production_h / showings)


ALL_CHAINS = ("food", "housing", "transport", "healthcare", "entertainment")


# =============================================================================
# Holding-time split (Sec.6.2b) -- reporting arithmetic, no ledger writes
# =============================================================================

def holding_shares(holding_periods: dict) -> dict:
    """Each holder's permanent share of an asset's creation-cost.

    share = their holding-duration / total holding-duration over the asset's life
    (Sec.6.2b, Sec.1.1). Holding-duration is a PHYSICAL TRACE, which is why this
    is a measured convention rather than an invented one -- and it passes the
    checks an even split fails: zero holding time gives zero share (dummy), and
    equal holding time gives equal shares (symmetry).
    """
    total = float(sum(holding_periods.values()))
    if total <= 0:
        raise ChainError("an asset with no holding time has no shares to split")
    return {who: dur / total for who, dur in holding_periods.items()}


def creation_cost_shares(holding_periods: dict, single_use: bool) -> dict:
    """Who carries a thing's making-cost. Two rules, and the test between them is
    Sec.6.2a's: DOES THE THING SURVIVE THE PROCESS?

    A house survives being lived in. Its cost splits across everyone who held it,
    by how long (Sec.6.2b).

    A loaf of bread does not survive being eaten, and neither does the bag it came
    in. Author ruling 2026-08-23: SINGLE-USE GOODS ARE NOT SPREAD OVER TIME OF
    OWNERSHIP. Opening the bag is putting it into service, nobody resells an
    opened loaf, and the whole cost lands on the one person who used it.

    Spreading a loaf's cost by holding time would be absurd in the direction that
    matters: it would make a shopper who ate the bread quickly owe less than one
    who left it on the counter for a week.
    """
    if not single_use:
        return holding_shares(holding_periods)
    if not holding_periods:
        raise ChainError("a single-use good still needs somebody who used it")
    last = list(holding_periods)[-1]
    return {who: (1.0 if who == last else 0.0) for who in holding_periods}


# =============================================================================
# Tests
# =============================================================================

def test_every_chain_closes():
    """IC-1 to IC-4 on all five, plus the whole Sec.9 set."""
    for name in ALL_CHAINS:
        k = _world()

        builder = globals()[f"{name}_chain"]
        out = builder(k)
        c = out[0] if isinstance(out, tuple) else out
        Conformance.run_all(k)
        assert len(c.steps) > 0
    print(f"[ok] all five chains close: mass and energy balance, every parcel has "
          f"an origin and a fate")


def test_an_unbalanced_process_is_refused():
    """The check is not decorative: forget the waste and the chain will not build."""
    k = _world()

    c = Chain(k, "broken")
    try:
        c.process(FARMER, labour_h=1.0, note="mill without waste",
                  takes={"mass_kg": 1000.0},
                  makes={"flour": {"mass_kg": 780.0}})      # 220 kg unaccounted
    except ChainError as e:
        assert "220" in str(e) or "does not balance" in str(e)
        print("[ok] a process that loses 220 kg is refused at build time (IC-1)")
        return
    raise AssertionError("an unbalanced process was accepted")


def test_the_doctors_education_is_not_in_the_bill():
    """Sec.6.2, and the whole reason healthcare is one of the five chains.

    A thousand visits from a doctor whose training cost 10,000 hours. The bill is
    the doctor's time and the clinic's materials. It is not one-thousandth of a
    medical degree.
    """
    k = _world()

    _, r = healthcare_chain(k)
    assert abs(r["bill_h"] - 500.0) < TOL
    assert abs(r["amortised_h"] - 10_500.0) < TOL
    inflation = r["amortised_h"] / r["bill_h"]
    assert inflation > 20.0
    # And the training really is on the ledger -- it was carried, not waived.
    doctor_debit = collapse(k.proj.debit(), k.dials.weights)[DOCTOR]
    assert doctor_debit >= r["training_h"] - TOL, "the training vanished (A1)"
    print(f"[ok] the doctor's education is absent from the bill: {r['bill_h']:.0f} h "
          f"for {r['visits']:,} visits, not {r['amortised_h']:.0f} h "
          f"({inflation:.0f}x) -- and the {r['training_h']:,.0f} h is still on the "
          f"ledger, carried when it happened")


def test_the_films_production_is_not_in_the_ticket():
    """Sec.6.2a's media case. The viewer pays for the projector, not the film."""
    k = _world()

    _, r = entertainment_chain(k)
    assert abs(r["ticket_h"] - 0.002) < 1e-9
    assert abs(r["amortised_h"] - 0.502) < 1e-9
    crew_debit = collapse(k.proj.debit(), k.dials.weights)[CREW]
    assert crew_debit >= r["production_h"] - TOL, "the production vanished (A1)"
    print(f"[ok] the film's production is absent from the ticket: {r['ticket_h']:.4f} h "
          f"delivery, not {r['amortised_h']:.4f} h "
          f"({r['amortised_h'] / r['ticket_h']:.0f}x) -- and the "
          f"{r['production_h']:,.0f} h sits where it was incurred")


def test_pollution_stays_on_the_producer():
    """Sec.3.2b: the farmer keeps the runoff after the bread reaches the eater."""
    k = _world()

    food_chain(k)
    Conformance.run_all(k)
    d = k.proj.debit()["mass_kg"]
    assert d[FARMER] > 0, "the farmer shed the runoff by selling the flour"
    assert abs(d[EATER] - 780.0) < TOL, "the eater did not take on the bread"
    assert abs(d[CARRIER]) < TOL and abs(d[SHOP]) < TOL, \
        "a middleman kept property debit after passing the goods on"
    print(f"[ok] pollution stays on its causer: the farmer holds {d[FARMER]:.0f} kg "
          f"after the bread reaches the eater, and the carrier and shop hold 0")


def test_holding_time_splits_a_house_in_half():
    """Foundations Sec.6.2b's own worked example, run.

    A holds one year, passes to B, B holds one year, disposal. Each holds 50% of
    the creation-cost, permanently.
    """
    shares = holding_shares({HOLDER_A: 1.0, HOLDER_B: 1.0})
    assert abs(shares[HOLDER_A] - 0.5) < 1e-12
    assert abs(shares[HOLDER_B] - 0.5) < 1e-12
    # Dummy: zero holding time, zero share -- which is what kills the entry-toll
    # an even split would put on a new hire at a hospital or a water plant.
    s2 = holding_shares({HOLDER_A: 30.0, HOLDER_B: 0.0})
    assert s2[HOLDER_B] == 0.0
    # A 30-year veteran among 200 staff over a 60-year facility.
    # Foundations Sec.6.2b puts this at "approximately 0.25%". Computed exactly it
    # is 30 / (30 + 199*60) = 0.2506%, because the veteran worked 30 of the 60
    # years rather than all of them. The doc's figure is a rounding, not an error.
    veteran = holding_shares({0: 30.0, 1: 199 * 60.0})[0]
    assert abs(veteran - 0.0025) < 5e-5
    print(f"[ok] holding time splits a house 50/50, gives a new hire 0%, and leaves "
          f"a 30-year veteran of a 60-year facility {veteran * 100:.2f}%")


def test_the_material_leaves_but_the_making_does_not():
    """Sec.3.2: embodied material discharges on transfer; nothing else does."""
    k = _world()

    housing_chain(k)
    Conformance.run_all(k)
    d = k.proj.debit()["mass_kg"]
    assert abs(d[HOLDER_B] - 145_000.0) < TOL, "the house did not reach its holder"
    assert abs(d[HOLDER_A]) < TOL, "the seller kept the atoms"
    assert d[BUILDER] > 0, "the builder shed the construction waste"
    print(f"[ok] the house's atoms move to the current holder ({d[HOLDER_B]:,.0f} kg) "
          f"while the builder keeps {d[BUILDER]:,.0f} kg of construction waste")


def test_ic7_stops_an_impossible_chain():
    """A chain cannot credit one account more hours than a period contains."""
    k = _world(days=1.0)
    c = Chain(k, "impossible")
    try:
        c.extract(FARMER, labour_h=100.0, note="a 100-hour day", mass_kg=1.0)
    except ChainError as e:
        assert "IC-7" in str(e)
        print("[ok] a chain crediting 100 h in a 1-day period is refused (IC-7)")
        return
    raise AssertionError("IC-7 missed an impossible chain")


def test_the_custody_chain_ending_is_the_fate():
    """No 'eaten' event, no 'thrown away' event. The chain stopping is enough.

    A loaf and its plastic bag both took resources. Both chains end at the eater,
    so both sit on the eater's ledger -- and the eater holds exactly what was
    handed to them, not double.
    """
    k = _world()
    food_chain(k)
    Conformance.run_all(k)
    d = k.proj.debit()["mass_kg"]
    assert abs(d[EATER] - 780.0) < TOL, \
        f"the eater holds {d[EATER]:.0f} kg, not the 780 kg handed to them"
    print(f"[ok] the custody chain ending IS the fate: the eater holds "
          f"{d[EATER]:.0f} kg with no 'eaten' event written anywhere")


def test_expired_goods_cannot_be_handed_on():
    """Author ruling: past its shelf life a thing joins its holder's waste stream.

    The hand-off is refused outright. Nobody guards a door -- the rule is an
    invariant anybody can check, exactly like IC-7's 24-hour cap.
    """
    k = _world()
    c = Chain(k, "stale")
    c.extract(SHOP, labour_h=1.0, note="a loaf", mass_kg=1.0)
    best_before = k.period
    k.period += 2                                   # two periods go by
    try:
        c.handoff(SHOP, EATER, note="sold stale", mass_kg=1.0, expires=best_before)
    except ChainError as e:
        assert "waste stream" in str(e)
        d = k.proj.debit()["mass_kg"]
        assert abs(d[SHOP] - 1.0) < TOL, "the shop shed the loaf anyway"
        assert abs(d[EATER]) < TOL, "the buyer took on somebody else's waste"
        print(f"[ok] a hand-off 2 periods past the date is refused; the loaf stays "
              f"on the shop ({d[SHOP]:.0f} kg) and the buyer takes {d[EATER]:.0f} kg")
        return
    raise AssertionError("expired goods were handed on")


def test_disposal_is_a_service_not_a_handoff():
    """Author ruling: getting rid of waste is a service with a cost.

    The material stays with whoever let it become waste. The processor is credited
    for the work. The holder pays for that work. No property changes hands.
    """
    k = _world()
    c = Chain(k, "bin day")
    c.extract(EATER, labour_h=0.5, note="a spoiled loaf", mass_kg=1.0)
    before = k.proj.credit()[CARRIER]
    c.dispose(EATER, CARRIER, labour_h=0.25, note="collected", mass_kg=1.0)
    Conformance.run_all(k)
    d = k.proj.debit()
    assert abs(d["mass_kg"][EATER] - 1.0) < TOL, "the eater shed the waste"
    assert abs(d["mass_kg"][CARRIER]) < TOL, "the binman took on the rubbish"
    assert abs(k.proj.credit()[CARRIER] - before - 0.25) < TOL, \
        "the disposal work was not credited"
    assert abs(d["labour_h"][EATER] - 0.25) < TOL, "the service was not charged"
    print(f"[ok] disposal is a service: the eater keeps {d['mass_kg'][EATER]:.0f} kg "
          f"and pays {d['labour_h'][EATER]:.2f} h; the collector is credited 0.25 h")


def test_recycling_moves_the_atoms_but_not_the_pollution():
    """Sec.3.6 rule 3. Landfill is not recycling."""
    k = _world()
    c = Chain(k, "recycling")
    c.extract(EATER, labour_h=0.5, note="a bottle", mass_kg=2.0)
    c.dispose(EATER, CARRIER, labour_h=0.25, recycled=True, note="reprocessed",
              mass_kg=2.0)
    Conformance.run_all(k)
    d = k.proj.debit()["mass_kg"]
    assert abs(d[EATER]) < TOL, "recycled atoms stayed with the discarder"
    assert abs(d[CARRIER] - 2.0) < TOL, "the recycler did not take the atoms on"
    print(f"[ok] recycling carries the atoms forward ({d[CARRIER]:.0f} kg to the "
          f"reprocessor) while landfill would have left them on the discarder")


def test_the_check_catches_a_forged_expired_discharge():
    """The conformance layer polices it, not only the recorder."""
    k = _world()
    k.log.append(np.array([SHOP]), TRANSFER, k.period, expires=float(k.period - 1),
                 mass_kg=-5.0, weight=1.0)          # a discharge after expiry
    try:
        Conformance.check_no_expired_discharge(k)
    except ConformanceError as e:
        assert "waste stream" in str(e)
        print("[ok] a log claiming an expired discharge is caught by the check")
        return
    raise AssertionError("an expired discharge slipped past the check")


def test_single_use_lands_whole_on_its_user():
    """Sec.6.2a's test: does the thing survive the process?"""
    house = creation_cost_shares({HOLDER_A: 1.0, HOLDER_B: 1.0}, single_use=False)
    assert abs(house[HOLDER_A] - 0.5) < 1e-12
    loaf = creation_cost_shares({SHOP: 5.0, EATER: 1.0}, single_use=True)
    assert loaf[EATER] == 1.0 and loaf[SHOP] == 0.0
    print("[ok] a house splits 50/50 by holding time; a loaf lands 100% on whoever "
          "opened it, however briefly they held it")


def run_tests():
    test_every_chain_closes()
    test_the_custody_chain_ending_is_the_fate()
    test_expired_goods_cannot_be_handed_on()
    test_disposal_is_a_service_not_a_handoff()
    test_recycling_moves_the_atoms_but_not_the_pollution()
    test_the_check_catches_a_forged_expired_discharge()
    test_single_use_lands_whole_on_its_user()
    test_an_unbalanced_process_is_refused()
    test_ic7_stops_an_impossible_chain()
    test_pollution_stays_on_the_producer()
    test_the_material_leaves_but_the_making_does_not()
    test_holding_time_splits_a_house_in_half()
    test_the_doctors_education_is_not_in_the_bill()
    test_the_films_production_is_not_in_the_ticket()
    print("\nAll chain tests passed.")


# =============================================================================

def demo():
    W = 78
    print("=" * W)
    print("STATERA -- the five exemplar chains")
    print("=" * W)
    print("  Covering 82% of what a person materially consumes.")
    print()
    print("  *** THE NUMBERS BELOW ARE PLACEHOLDERS. ***")
    print("  Their job is to exercise the machinery, not to describe the world.")
    print("  Calibration against real physical data is step 5 and is not done.")
    print()

    print(f"  {'chain':<16}{'steps':>7}{'labour h':>12}   what it proves")
    print("  " + "-" * (W - 4))
    rows = [
        ("housing", "creation-cost splits by holding time (Sec.6.2b)"),
        ("transport", "the driver owns the tailpipe (Sec.3.2b)"),
        ("food", "one process, three outputs, waste counted (Sec.3.4a)"),
        ("healthcare", "the doctor's training is not in the bill (Sec.6.2)"),
        ("entertainment", "the viewer pays for the projector (Sec.6.2a)"),
    ]
    for name, proves in rows:
        k = _world()

        out = globals()[f"{name}_chain"](k)
        c = out[0] if isinstance(out, tuple) else out
        Conformance.run_all(k)
        hours = sum(s[3] for s in c.steps)
        print(f"  {name:<16}{len(c.steps):>7}{hours:>12,.0f}   {proves}")

    k = _world()

    _, h = healthcare_chain(k)
    k2 = _world()
    k2.accrue(days=1.0)
    _, e = entertainment_chain(k2)

    print()
    print("  THE FRONT-LOADING RULE, in two numbers")
    print("  " + "-" * (W - 4))
    print(f"  {h['visits']:,} patient visits from a doctor whose training cost "
          f"{h['training_h']:,.0f} h")
    print(f"     the bill              {h['bill_h']:>12,.2f} h")
    print(f"     if it were amortised  {h['amortised_h']:>12,.2f} h   "
          f"({h['amortised_h'] / h['bill_h']:.0f}x dearer)")
    print()
    print(f"  {e['showings']:,} showings of a film that cost "
          f"{e['production_h']:,.0f} h to make")
    print(f"     the ticket            {e['ticket_h']:>12,.4f} h")
    print(f"     if it were amortised  {e['amortised_h']:>12,.4f} h   "
          f"({e['amortised_h'] / e['ticket_h']:.0f}x dearer)")
    print()
    print("  Neither cost vanished. Both sit on the ledger where they were")
    print("  incurred, cushioned by pledges -- never divided by a number of")
    print("  patients or viewers, because that number is always arbitrary.")
    print("=" * W)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
    else:
        demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
