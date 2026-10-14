#!/usr/bin/env python3
"""
ceiling_challenge.py -- can anything push max(claimed credit)/F above 24/F
without any record claiming more than 24 hours in a day?

Answers sr-20260901-construct-a-challenge-that-pushes-max-claime (SB-01).

TWO STATISTICS, AND THEY ARE NOT THE SAME OBJECT
    r_i   = C(i) / days_lived(i)        one account's credit per day lived
    S_F   = max_i r_i / F               the REQUEST's statistic: the floor is
                                        the network's published constant
    S_mm  = max_i r_i / min_i r_i       the BOUND as Foundations s5.5.5 states
                                        it: largest over smallest
    The claim: both <= 24 / F.  They coincide whenever somebody lives at the
    floor.  Only S_mm can be moved by lowering a minimum.

THE ARITHMETIC
    If every lived day t carries F <= c(i,t) <= 24, then r_i is a mean of
    numbers in [F, 24], so F <= r_i <= 24 and both statistics are <= 24/F.
    That proof rests on four premises, and each one is something an
    implementation EVALUATES rather than something the arithmetic supplies:

      P1  floor        every day inside the evaluated span is credited F
      P2  cap          the 24-hour cap is checked on the SUM of all records an
                       account holds for one day, not on each record alone
      P3  span         every dated credit falls on a day inside days_lived
      P4  denominator  days_lived is each account's own elapsed time / 24 h,
                       over the same set of (human) accounts as the numerator

    No arithmetic construction beats 24/F.  Every construction below breaks
    exactly one premise, and no record in any of them exceeds 24 h for one
    day.  So: the space is empty for the arithmetic and non-empty for the
    evaluation, and this file measures what each evaluation gap costs.

Run:
    python ceiling_challenge.py --test        # 13 self-tests, each can fail
    python ceiling_challenge.py               # the run, seed 20261014
    python ceiling_challenge.py --seed N --trials N

Needs only the standard library.
"""
from __future__ import annotations

import argparse
import math
import random
import sys
from dataclasses import dataclass, field
from typing import Iterable, Optional

SEED_DEFAULT = 20261014
DAY_HOURS = 24.0
TOL = 1e-9


# --------------------------------------------------------------------------
# The ledger objects
# --------------------------------------------------------------------------
@dataclass
class Block:
    """A run of credited days: `hours` credited on every day in [start, end].
    One block is one RECORD.  A backdated filing is a block whose start lies
    long before the filing date."""
    start: int           # first day (inclusive)
    end: int             # last day (inclusive)
    hours: float         # hours credited per day of the block
    kind: str = "work"   # 'work' | 'backdated' | 'pre-birth' | 'floor'

    @property
    def days(self) -> int:
        return self.end - self.start + 1

    @property
    def total(self) -> float:
        return self.hours * self.days


@dataclass
class Account:
    name: str
    birth: int                       # true birth, day index
    horizon: int                     # last day alive inside the window
    floor: float                     # hours a day the network credits this
                                     # account for staying alive (0 for an
                                     # organisation)
    human: bool = True
    declared_birth: Optional[int] = None   # what the filer declared; None = true
    blocks: list = field(default_factory=list)   # NON-floor records only
    local_25h_days: int = 0          # DST fall-back days lived (local calendar)


# --------------------------------------------------------------------------
# The evaluation rules -- the four premises, each switchable
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Rules:
    ic7: str = "account-day"        # 'account-day' (conforming) | 'per-record'
    span: str = "extend"            # 'extend' (conforming) | 'declared'
    denominator: str = "elapsed"    # 'elapsed' (conforming) | 'local-calendar'
    domain: str = "humans"          # 'humans' (conforming) | 'all-accounts'


CONFORMING = Rules()


def span(acct: Account, rules: Rules) -> tuple[int, int]:
    """The evaluated lived span.  Conforming: the declared span extended to
    cover every dated credit (Foundations s4.4 condition 3 -- back to the
    earliest date the evidence permits; a dated credit is evidence of life)."""
    start = acct.declared_birth if acct.declared_birth is not None else acct.birth
    end = acct.horizon
    if rules.span == "extend" and acct.blocks:
        start = min(start, min(b.start for b in acct.blocks))
        end = max(end, max(b.end for b in acct.blocks))
    return start, end


def effective_blocks(acct: Account, rules: Rules) -> list[Block]:
    """The account's records plus the floor the network credits over the
    evaluated span.  The floor is a RULE (proof of life, published duration),
    not a filing, so it follows the span the evaluator uses."""
    blocks = list(acct.blocks)
    if acct.human and acct.floor > 0:
        s, e = span(acct, rules)
        blocks.append(Block(s, e, acct.floor, "floor"))
    return blocks


def ic7_per_record(blocks: list[Block]) -> tuple[bool, float]:
    """The weak evaluator: each record alone must not exceed 24 h/day."""
    worst = max((b.hours for b in blocks), default=0.0)
    return worst <= DAY_HOURS + TOL, worst


def ic7_account_day(blocks: list[Block]) -> tuple[bool, float]:
    """The conforming evaluator: the SUM over all records covering one day
    must not exceed 24 h.  Sweep over block boundaries; no per-day loop.
    This is the shape of audits/arithmetic_audits.py::check_ic7_agent_time."""
    events = []
    for b in blocks:
        events.append((b.start, +b.hours))
        events.append((b.end + 1, -b.hours))
    events.sort()
    running, worst, i = 0.0, 0.0, 0
    while i < len(events):
        day = events[i][0]
        while i < len(events) and events[i][0] == day:
            running += events[i][1]
            i += 1
        worst = max(worst, running)
    return worst <= DAY_HOURS + TOL, worst


def ic7_brute(blocks: list[Block]) -> float:
    """Brute-force per-day sum; used only by the self-test that protects the
    sweep above."""
    lo = min(b.start for b in blocks)
    hi = max(b.end for b in blocks)
    worst = 0.0
    for t in range(lo, hi + 1):
        worst = max(worst, sum(b.hours for b in blocks if b.start <= t <= b.end))
    return worst


def ic7_check(acct: Account, rules: Rules) -> tuple[bool, float]:
    blocks = effective_blocks(acct, rules)
    if rules.ic7 == "per-record":
        return ic7_per_record(blocks)
    return ic7_account_day(blocks)


def days_lived(acct: Account, rules: Rules) -> float:
    s, e = span(acct, rules)
    days = e - s + 1
    if rules.denominator == "local-calendar":
        # a local calendar counts a 25-hour fall-back day as one day
        return float(days)
    # elapsed time / 24 h: a 25-hour local day is 25/24 of a day
    return days + acct.local_25h_days / DAY_HOURS


def rate(acct: Account, rules: Rules) -> float:
    total = sum(b.total for b in effective_blocks(acct, rules))
    # the extra clock hour on each 25-hour fall-back day was really worked and
    # is inside "24 hours of activity in 24 hours"; it counts under both
    # denominators -- only the denominator's unit differs
    if acct.blocks:
        total += acct.local_25h_days * 1.0
    d = days_lived(acct, rules)
    return total / d if d > 0 else float("inf")


@dataclass
class Stat:
    s_F: float      # max rate / F  (the request's statistic)
    s_mm: float     # max rate / min rate  (the bound as s5.5.5 states it)
    hi: float
    lo: float


def statistic(accts: Iterable[Account], rules: Rules, F: float) -> Stat:
    accts = list(accts)
    if rules.domain == "humans":
        accts = [a for a in accts if a.human]
    rates = [rate(a, rules) for a in accts]
    hi, lo = max(rates), min(rates)
    return Stat(hi / F, hi / lo if lo > 0 else float("inf"), hi, lo)


def ic7_all(accts: Iterable[Account], rules: Rules) -> tuple[bool, float]:
    worst_all, ok_all = 0.0, True
    for a in accts:
        ok, worst = ic7_check(a, rules)
        ok_all &= ok
        worst_all = max(worst_all, worst)
    return ok_all, worst_all


def record_level_breach(accts: Iterable[Account]) -> bool:
    """Does ANY single filed record claim more than 24 h for one day?  This is
    the request's own condition -- 'without breaching the 24-hour cap' --
    read at the record level."""
    return any(b.hours > DAY_HOURS + TOL for a in accts for b in a.blocks)


# --------------------------------------------------------------------------
# Populations
# --------------------------------------------------------------------------
def human(name: str, F: float, birth: int, horizon: int) -> Account:
    return Account(name, birth, horizon, floor=F)


def population(n: int, F: float, horizon: int, rng: random.Random) -> list[Account]:
    """n living humans of mixed ages with random amounts of ordinary work,
    none breaching the cap on any day.  The first lives at the floor, which
    is the premise s5.5.5 states: every network has somebody who only stays
    alive."""
    out = []
    for k in range(n):
        age_days = rng.randint(18 * 365, 90 * 365)
        birth = horizon - age_days + 1
        a = human(f"h{k}", F, birth, horizon)
        if k > 0:
            work = rng.uniform(0.0, DAY_HOURS - F)
            w_start = max(birth, horizon - rng.randint(0, age_days - 1))
            a.blocks.append(Block(w_start, horizon, work, "work"))
        out.append(a)
    return out


# --------------------------------------------------------------------------
# The constructions -- one per premise
# --------------------------------------------------------------------------
def construct_wall(F: float, horizon: int, years: int = 80) -> Account:
    """The arithmetic wall: 24 - F h of work on every day of an 80-year life,
    beside the floor.  Per-day sum exactly 24."""
    birth = horizon - years * 365 + 1
    a = human("wall", F, birth, horizon)
    a.blocks.append(Block(birth, horizon, DAY_HOURS - F, "work"))
    return a


def construct_overlap(F: float, horizon: int, k: int, years: int = 80) -> Account:
    """P2.  k backdated filings, each at 24 - F h/day -- the most one work
    record can hold beside the floor -- all covering the SAME days.  No single
    record exceeds 24 h/day; the per-day sum is F + k(24 - F)."""
    birth = horizon - years * 365 + 1
    a = human("overlap", F, birth, horizon)
    for _ in range(k):
        a.blocks.append(Block(birth, horizon, DAY_HOURS - F, "backdated"))
    return a


def construct_pre_birth(F: float, horizon: int, declared_years: int = 40,
                        extra_years: int = 10, pre_hours: float = DAY_HOURS) -> Account:
    """P3.  A filer declares a 40-year span, works at the wall through it, and
    files 10 further years of credit dated BEFORE the declared birth, at
    `pre_hours` a day.  Under 'declared' no floor and no days are added for
    those years; under 'extend' both are."""
    true_birth = horizon - declared_years * 365 + 1
    a = human("prebirth", F, true_birth, horizon)
    a.declared_birth = true_birth
    a.blocks.append(Block(true_birth, horizon, DAY_HOURS - F, "work"))
    pre_start = true_birth - extra_years * 365
    a.blocks.append(Block(pre_start, true_birth - 1, pre_hours, "pre-birth"))
    return a


def construct_dst(F: float, horizon: int, years: int = 80) -> Account:
    """P4 (unit).  A wall worker whose local calendar has one 25-hour
    fall-back day a year.  On that day they honestly claim 25 clock hours in
    25 clock hours, which is not 'more than 24 hours in 24 hours'."""
    a = construct_wall(F, horizon, years)
    a.local_25h_days = years
    return a


def construct_measured_floor(F_list: dict, sleep_actual: float, horizon: int,
                             years: int = 80) -> tuple[Account, float]:
    """P1.  A network that credits each person's MEASURED self-care instead
    of the published durations.  Returns the account and the convention F."""
    F = sum(F_list.values())
    measured = F - F_list["sleep"] + sleep_actual
    birth = horizon - years * 365 + 1
    return Account("measured", birth, horizon, floor=measured), F


def construct_org(horizon: int, years: int = 10) -> Account:
    """P4 (domain).  An organisation account: no floor, no credit of its own
    (credit belongs to persons, A3)."""
    birth = horizon - years * 365 + 1
    return Account("coop", birth, horizon, floor=0.0, human=False)


# --------------------------------------------------------------------------
# The adversarial random search
# --------------------------------------------------------------------------
def adversary_trial(F: float, horizon: int, rng: random.Random, rules: Rules,
                    n_pop: int = 30, max_blocks: int = 8) -> Optional[tuple[Stat, float]]:
    """One trial: an ordinary population plus one attacker who files up to
    `max_blocks` random records, each inside the record-level cap, possibly
    backdated, overlapping, dated before the declared birth, with a possibly
    shortened declared span.  ACCEPTED if IC-7 passes under `rules`."""
    pop = population(n_pop, F, horizon, rng)
    age = rng.randint(18 * 365, 90 * 365)
    birth = horizon - age + 1
    att = human("attacker", F, birth, horizon)
    if rng.random() < 0.5:
        att.declared_birth = birth + rng.randint(0, age // 2)
    for _ in range(rng.randint(1, max_blocks)):
        s = rng.randint(birth - 20 * 365, horizon)
        e = rng.randint(s, horizon)
        hrs = rng.choice([rng.uniform(0, DAY_HOURS), DAY_HOURS, DAY_HOURS - F])
        att.blocks.append(Block(s, e, hrs, "backdated" if s < birth else "work"))
    accts = pop + [att]
    ok, worst = ic7_all(accts, rules)
    if not ok:
        return None
    return statistic(accts, rules, F), worst


def adversary_search(F: float, horizon: int, trials: int, rng: random.Random,
                     rules: Rules) -> dict:
    best_F = best_mm = 0.0
    accepted, worst_day, lo_at_best = 0, 0.0, 0.0
    for _ in range(trials):
        r = adversary_trial(F, horizon, rng, rules)
        if r is None:
            continue
        accepted += 1
        st, w = r
        best_F = max(best_F, st.s_F)
        if st.s_mm > best_mm:
            best_mm, worst_day, lo_at_best = st.s_mm, w, st.lo
    return {"best_S_F": best_F, "best_S_mm": best_mm, "accepted": accepted,
            "trials": trials, "worst_day_at_best": worst_day, "min_rate_at_best": lo_at_best}


# --------------------------------------------------------------------------
# Self-tests -- each can fail
# --------------------------------------------------------------------------
def _close(a, b, tol=TOL):
    return abs(a - b) <= tol


def self_tests(verbose=True) -> int:
    rng = random.Random(7)
    H = 30000
    failures = 0

    def check(name, cond, detail=""):
        nonlocal failures
        if not cond:
            failures += 1
        if verbose:
            print(f"  [{'ok  ' if cond else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

    F = 10.0
    # 1. SB-01 s8.1: every account at 24 h/day -> S_F exactly 24/F, and S_mm 1.0
    pop = [construct_wall(F, H, y) for y in (20, 50, 80)]
    st = statistic(pop, CONFORMING, F)
    check("1 all-24 population: S_F = 24/F exactly, S_mm = 1.0 (two statistics)",
          _close(st.s_F, 24 / F) and _close(st.s_mm, 1.0), f"S_F={st.s_F:.6f} S_mm={st.s_mm:.6f}")

    # 2. SB-01 s8.2: every account at F -> both exactly 1.0
    pop = [human(f"f{y}", F, H - y * 365 + 1, H) for y in (20, 50, 80)]
    st = statistic(pop, CONFORMING, F)
    check("2 all-floor population returns exactly 1.0 on both", _close(st.s_F, 1.0) and _close(st.s_mm, 1.0),
          f"S_F={st.s_F:.6f} S_mm={st.s_mm:.6f}")

    # 3. SB-01 s8.3 (control): inserting a floor account leaves both unchanged
    pop = population(40, F, H, rng) + [construct_wall(F, H)]
    st0 = statistic(pop, CONFORMING, F)
    st1 = statistic(pop + [human("x", F, H - 1000, H)], CONFORMING, F)
    check("3 inserting a floor-only account leaves both statistics unchanged",
          _close(st0.s_F, st1.s_F) and _close(st0.s_mm, st1.s_mm) and _close(st0.lo, F),
          f"S_mm {st0.s_mm:.6f} -> {st1.s_mm:.6f}, min rate {st0.lo:.3f}")

    # 4. SB-01 s8.4: removing the unique highest account lowers both
    pop = population(40, F, H, rng)
    for a in pop:
        for b in a.blocks:
            b.hours = min(b.hours, 10.0)
    pop.append(construct_wall(F, H))
    st_with, st_without = statistic(pop, CONFORMING, F), statistic(pop[:-1], CONFORMING, F)
    check("4 removing the single highest account lowers both",
          st_without.s_F < st_with.s_F - 1e-6 and st_without.s_mm < st_with.s_mm - 1e-6,
          f"S_F {st_with.s_F:.4f} -> {st_without.s_F:.4f}")

    # 5. the account-day evaluator catches two overlapping 18-h records
    ok, worst = ic7_account_day([Block(0, 99, 18.0), Block(50, 149, 18.0)])
    check("5 account-day IC-7 catches overlapping 18+18 h records", (not ok) and _close(worst, 36.0),
          f"worst day {worst:.1f} h")

    # 6. ...and does not fire on two ADJACENT 24-h records
    ok, worst = ic7_account_day([Block(0, 99, 24.0), Block(100, 199, 24.0)])
    check("6 account-day IC-7 passes adjacent 24+24 h records", ok and _close(worst, 24.0),
          f"worst day {worst:.1f} h")

    # 7. the per-record evaluator PASSES the overlapping pair (the gap)
    ok, worst = ic7_per_record([Block(0, 99, 18.0), Block(50, 149, 18.0)])
    check("7 per-record IC-7 passes the same overlapping pair", ok and _close(worst, 18.0),
          f"worst record {worst:.1f} h")

    # 8. the span rule extends BOTH the denominator and the floor over pre-birth
    #    credit, so the account's rate can neither exceed 24 nor fall below F
    a = construct_pre_birth(F, H, pre_hours=DAY_HOURS - F)
    d_decl, d_ext = days_lived(a, Rules(span="declared")), days_lived(a, CONFORMING)
    fl = [b for b in effective_blocks(a, CONFORMING) if b.kind == "floor"][0]
    low = construct_pre_birth(F, H, pre_hours=0.1)          # tiny pre-birth filing
    check("8 span rule extends denominator AND floor over pre-birth credit",
          _close(d_decl, 40 * 365) and _close(d_ext, 50 * 365) and _close(fl.days, 50 * 365)
          and _close(rate(a, CONFORMING), 24.0) and rate(low, CONFORMING) >= F - TOL,
          f"declared {d_decl:.0f} d, extended {d_ext:.0f} d, floor {fl.days} d, "
          f"rates {rate(a, CONFORMING):.3f} / {rate(low, CONFORMING):.3f}")

    # 9. a rate is a mean of per-day values: never above the worst day
    bad = 0
    for _ in range(50):
        a = population(2, F, H, rng)[1]
        _, mx = ic7_account_day(effective_blocks(a, CONFORMING))
        r = rate(a, CONFORMING)
        if not (F - TOL <= r <= mx + TOL):
            bad += 1
    check("9 every conforming rate lies in [F, its own worst day]", bad == 0, f"{bad} violations / 50")

    # 10. the DST artefact: local-calendar denominator > 24, elapsed = 24
    a = construct_dst(F, H)
    r_local, r_elapsed = rate(a, Rules(denominator="local-calendar")), rate(a, CONFORMING)
    check("10 local-calendar denominator reads above 24; elapsed reads exactly 24",
          r_local > 24.0 + 1e-6 and _close(r_elapsed, 24.0), f"{r_local:.5f} vs {r_elapsed:.5f}")

    # 11. an organisation in the domain makes S_mm infinite and leaves S_F alone
    pop = population(10, F, H, rng) + [construct_org(H)]
    st_all, st_h = statistic(pop, Rules(domain="all-accounts"), F), statistic(pop, CONFORMING, F)
    check("11 organisation in domain -> S_mm inf, S_F unchanged; humans only -> finite",
          math.isinf(st_all.s_mm) and _close(st_all.s_F, st_h.s_F) and math.isfinite(st_h.s_mm),
          f"S_mm {st_all.s_mm} vs {st_h.s_mm:.4f}")

    # 12. the sweep equals brute force on random block sets (protects O1)
    bad = 0
    for _ in range(200):
        blocks = []
        for _ in range(rng.randint(1, 7)):
            s0 = rng.randint(0, 380)
            blocks.append(Block(s0, rng.randint(s0, 400), rng.uniform(0, 24)))
        if not _close(ic7_account_day(blocks)[1], ic7_brute(blocks), 1e-7):
            bad += 1
    check("12 sweep evaluator equals brute-force per-day sum", bad == 0, f"{bad} mismatches / 200")

    # 13. measured self-care reproduces Foundations s5.5.5 condition 1: 3.000
    F_list = {"sleep": 8.0, "eating": 1.0, "washing": 0.5, "upkeep": 0.5}
    a, Fc = construct_measured_floor(F_list, 6.0, H)
    st = statistic([a, construct_wall(Fc, H)], CONFORMING, Fc)
    check("13 a 6-hour sleeper under measured self-care gives S_mm = 3.000, S_F = 2.400",
          _close(st.s_mm, 3.0) and _close(st.s_F, 2.4), f"S_mm={st.s_mm:.6f} S_F={st.s_F:.6f} at F={Fc}")

    print(f"\n{13 - failures} of 13 self-tests pass" + ("" if failures == 0 else f"  -- {failures} FAILED"))
    return failures


# --------------------------------------------------------------------------
# The run
# --------------------------------------------------------------------------
def run(seed: int, trials: int) -> None:
    rng = random.Random(seed)
    H = 30000
    print(f"ceiling-challenge  seed={seed}  trials per floor={trials}\n")

    # --- O1: the conforming evaluator, wall + random adversary ----------------
    print("O1  Conforming evaluation (account-day IC-7, span extended with floor, elapsed denominator, humans)")
    print(f"{'F':>4} {'24/F':>8} {'wall S_F':>9} {'search S_F':>11} {'search S_mm':>12} {'accepted':>9} {'min rate':>9} {'max rate':>9}")
    o1_ok = True
    for F in (2.0, 6.0, 10.0, 14.0):
        pop = population(30, F, H, rng) + [construct_wall(F, H)]
        st = statistic(pop, CONFORMING, F)
        res = adversary_search(F, H, trials, rng, CONFORMING)
        best = max(st.s_F, st.s_mm, res["best_S_F"], res["best_S_mm"])
        o1_ok &= best <= 24 / F + TOL
        print(f"{F:>4.0f} {24/F:>8.4f} {st.s_F:>9.6f} {res['best_S_F']:>11.6f} {res['best_S_mm']:>12.6f} "
              f"{res['accepted']:>9d} {st.lo:>9.4f} {st.hi:>9.4f}")
    print(f"    every accepted construction, both statistics <= 24/F: {o1_ok}\n")

    # --- O2: per-record IC-7, overlapping backdated filings -------------------
    F = 10.0
    print("O2  Premise P2 broken: IC-7 checked per record; k filings at 24-F h/day on the same days, beside the floor")
    print(f"{'k':>3} {'per-record ok':>14} {'account-day ok':>15} {'worst day h':>12} {'S_F':>9} {'1+k(24-F)/F':>12} {'record>24?':>11}")
    for k in (1, 2, 3, 5):
        pop = population(30, F, H, rng) + [construct_overlap(F, H, k)]
        ok_r, _ = ic7_all(pop, Rules(ic7="per-record"))
        ok_a, worst = ic7_all(pop, CONFORMING)
        st = statistic(pop, Rules(ic7="per-record"), F)
        print(f"{k:>3d} {str(ok_r):>14} {str(ok_a):>15} {worst:>12.1f} {st.s_F:>9.4f} {1 + k*(24-F)/F:>12.4f} "
              f"{str(record_level_breach(pop)):>11}")
    res_r = adversary_search(F, H, trials, rng, Rules(ic7="per-record"))
    print(f"    random adversary under per-record IC-7: best S_F = {res_r['best_S_F']:.4f}, best S_mm = {res_r['best_S_mm']:.4f}, "
          f"accepted {res_r['accepted']}/{trials}\n")

    # --- O3: declared span, pre-birth credit ----------------------------------
    print("O3  Premise P3 broken: denominator is the DECLARED span; 10 years of credit dated before it")
    for pre, label in ((DAY_HOURS, "pre-birth records at 24 h/day"), (DAY_HOURS - F, "pre-birth records at 24-F h/day")):
        pop = population(30, F, H, rng) + [construct_pre_birth(F, H, pre_hours=pre)]
        print(f"    {label}:")
        for rl, rules in (("declared span ", Rules(span="declared")), ("span extended ", CONFORMING)):
            ok, worst = ic7_all(pop, rules)
            st = statistic(pop, rules, F)
            print(f"      {rl}: IC-7 ok={str(ok):5}  worst day {worst:5.1f} h  max rate {st.hi:7.3f}  "
                  f"S_F = {st.s_F:.4f}  S_mm = {st.s_mm:.4f}  record>24? {record_level_breach(pop)}")
    print()

    # --- O4: the DST / local-calendar denominator -----------------------------
    print("O4  Premise P4 (unit) broken: local calendar counts a 25-hour day as one day (80 years, one a year)")
    pop = population(30, F, H, rng) + [construct_dst(F, H)]
    for label, rules in (("local calendar", Rules(denominator="local-calendar")), ("elapsed / 24 h", CONFORMING)):
        st = statistic(pop, rules, F)
        print(f"    {label}: max rate {st.hi:.6f}, S_F = {st.s_F:.6f}, excess over 24/F = {st.s_F - 24/F:+.2e} "
              f"({(st.s_F - 24/F)/(24/F):+.2e} relative)")
    print()

    # --- O5: measured self-care ----------------------------------------------
    print("O5  Premise P1 broken: self-care credited as measured, not at the published duration")
    F_list = {"sleep": 8.0, "eating": 1.0, "washing": 0.5, "upkeep": 0.5}
    for sleep in (8.0, 7.0, 6.0, 4.0):
        a, Fc = construct_measured_floor(F_list, sleep, H)
        pop = population(30, Fc, H, rng) + [a, construct_wall(Fc, H)]
        st = statistic(pop, CONFORMING, Fc)
        print(f"    sleeps {sleep:>4.1f} h at a list of {Fc:.0f}: min rate {st.lo:6.3f}, S_mm = {st.s_mm:.4f}, "
              f"S_F = {st.s_F:.4f}  (24/F = {24/Fc:.4f})")
    print()

    # --- O6: organisation in the domain --------------------------------------
    print("O6  Premise P4 (domain) broken: an organisation account enters the minimum")
    pop = population(30, F, H, rng) + [construct_wall(F, H), construct_org(H)]
    st_all, st_h = statistic(pop, Rules(domain="all-accounts"), F), statistic(pop, CONFORMING, F)
    print(f"    all accounts: min rate {st_all.lo:.3f}, S_mm = {st_all.s_mm}, S_F = {st_all.s_F:.4f}")
    print(f"    humans only : min rate {st_h.lo:.3f}, S_mm = {st_h.s_mm:.4f}, S_F = {st_h.s_F:.4f}\n")

    # --- O7: SB-01 control, deletion direction -------------------------------
    print("O7  Control: deleting the top account under conforming rules")
    pop = population(200, F, H, rng)
    for a in pop:
        for b in a.blocks:
            b.hours = min(b.hours, 12.0)
    pop.append(construct_wall(F, H))
    st0, st1 = statistic(pop, CONFORMING, F), statistic(pop[:-1], CONFORMING, F)
    print(f"    S_F with the wall account {st0.s_F:.4f}, without it {st1.s_F:.4f}, delta {st1.s_F - st0.s_F:+.4f}\n")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--test", action="store_true", help="run the 13 self-tests and exit")
    p.add_argument("--seed", type=int, default=SEED_DEFAULT)
    p.add_argument("--trials", type=int, default=5000, help="adversary trials per floor")
    args = p.parse_args(argv)
    if args.test:
        sys.exit(1 if self_tests() else 0)
    run(args.seed, args.trials)


if __name__ == "__main__":
    main()
