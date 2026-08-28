"""
residual_unravelling.py -- does the residual rule actually make darkness stop paying?

Two claims were folded into Foundations v0.17 on the strength of an argument, with
no arithmetic behind them. This module supplies the arithmetic.

  CLAIM 1 (Foundations 5.1b).  Cohort estimates computed over the UNMEASURED RESIDUAL
    make darkness stop paying: as good producers instrument themselves and leave the
    dark pool, the estimate applied to whoever remains gets worse, so the incentive to
    leave strengthens over time.

  CLAIM 2 (Foundations 5.1d, condition 1).  The same rule applied one level down --
    to PERIODS AND DIMENSIONS WITHIN A SINGLE LIFE -- makes selective disclosure
    self-correcting rather than an exploit. Someone who documents only their flattering
    years should NOT be able to free-ride indefinitely on an average their own silence
    inflates.

Both are the same mechanism at two scales, so one model serves both. Read "agent" as
a producer for Claim 1 and as a life-period for Claim 2.

THE MODEL. Each agent has a true per-unit debit t_i, drawn from a lognormal (a few
heavy polluters, most near the mode -- the shape real emission distributions take).
Every round:
  1. The estimate applied to undisclosed agents is computed FROM THE UNDISCLOSED ONES
     ONLY, at a chosen percentile (the "err against the estimated party" rule,
     5.1d condition 2 -- percentile 50 is the plain mean-ish case, 75 errs against).
  2. Each undisclosed agent discloses iff disclosing lowers what it carries, i.e.
     t_i < estimate, net of a per-agent disclosure cost c_i (instrumenting is real work).
  3. Repeat until no one moves.

THE CONTROL THAT MATTERS. The same model is run with the estimate computed over the
WHOLE POPULATION instead of the residual -- the rule 5.1b explicitly rejects. If
darkness stops paying under both, the residual rule is not doing any work and 5.1b
is decoration. It is not: see H3.

WHAT THIS DOES NOT MODEL. Market access. The origin-evidence ruling of 2026-08-22 (Foundations 4.8)
says a producer cannot transact at all without onboarding, which swamps every incentive
modelled here. That makes this sim a LOWER BOUND on the pressure to disclose: it asks
whether the accounting alone suffices, deliberately ignoring the much larger stick.

Run:  python residual_unravelling.py
      python residual_unravelling.py --test
      python residual_unravelling.py --plot
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass, field

# ----------------------------------------------------------------------------
# parameters
# ----------------------------------------------------------------------------

N_AGENTS = 2000
SEED = 20260822

# Lognormal true-debit distribution. mu/sigma are in log space; sigma=0.8 gives a
# realistic right skew (a small number of agents far above the median).
LOG_MU = 0.0
LOG_SIGMA = 0.8

# Disclosure cost, in the same units as debit: instrumenting a supply chain or
# digging out twenty-year-old mileage records is real work and is not free.
COST_MEAN = 0.05
COST_SIGMA = 0.03

MAX_ROUNDS = 200


@dataclass
class Agent:
    idx: int
    true_debit: float
    cost: float
    disclosed: bool = False


@dataclass
class RoundState:
    round_no: int
    estimate: float
    n_disclosed: int
    n_dark: int
    dark_mean_true: float
    carried_total: float


@dataclass
class RunResult:
    basis: str                 # "residual" | "population"
    percentile: int
    rounds: list[RoundState] = field(default_factory=list)
    agents: list[Agent] = field(default_factory=list)

    @property
    def final(self) -> RoundState:
        return self.rounds[-1]

    @property
    def n_dark(self) -> int:
        return self.final.n_dark

    @property
    def dark_fraction(self) -> float:
        return self.final.n_dark / len(self.agents)


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def percentile(xs: list[float], p: int) -> float:
    """Linear-interpolated percentile. p in [0, 100]. Empty -> 0.0."""
    if not xs:
        return 0.0
    s = sorted(xs)
    if len(s) == 1:
        return s[0]
    k = (len(s) - 1) * (p / 100.0)
    lo = math.floor(k)
    hi = math.ceil(k)
    if lo == hi:
        return s[int(k)]
    return s[lo] * (hi - k) + s[hi] * (k - lo)


def make_agents(n: int = N_AGENTS, seed: int = SEED) -> list[Agent]:
    rng = random.Random(seed)
    out = []
    for i in range(n):
        t = math.exp(rng.gauss(LOG_MU, LOG_SIGMA))
        c = max(0.0, rng.gauss(COST_MEAN, COST_SIGMA))
        out.append(Agent(i, t, c))
    return out


# ----------------------------------------------------------------------------
# the model
# ----------------------------------------------------------------------------

def run(basis: str = "residual", pct: int = 50, agents: list[Agent] | None = None,
        max_rounds: int = MAX_ROUNDS) -> RunResult:
    """
    basis == "residual"    -> estimate computed over UNDISCLOSED agents only (5.1b)
    basis == "population"  -> estimate computed over ALL agents (the rejected rule)
    pct                    -> percentile of that set used as the estimate
    """
    if agents is None:
        agents = make_agents()
    agents = [Agent(a.idx, a.true_debit, a.cost) for a in agents]   # fresh copy
    res = RunResult(basis=basis, percentile=pct, agents=agents)

    for r in range(max_rounds):
        dark = [a for a in agents if not a.disclosed]
        if basis == "residual":
            pool = [a.true_debit for a in dark]
        elif basis == "population":
            pool = [a.true_debit for a in agents]
        else:
            raise ValueError("basis must be 'residual' or 'population'")

        est = percentile(pool, pct)

        carried = sum(a.true_debit if a.disclosed else est for a in agents)
        res.rounds.append(RoundState(
            round_no=r,
            estimate=est,
            n_disclosed=len(agents) - len(dark),
            n_dark=len(dark),
            dark_mean_true=(sum(a.true_debit for a in dark) / len(dark)) if dark else 0.0,
            carried_total=carried,
        ))

        # An agent discloses iff its true figure, plus the cost of proving it,
        # is better than the estimate it would otherwise carry.
        movers = [a for a in dark if a.true_debit + a.cost < est]
        if not movers:
            break
        for a in movers:
            a.disclosed = True

    return res


# ----------------------------------------------------------------------------
# hypotheses
# ----------------------------------------------------------------------------

def h1_dark_pool_worsens(res: RunResult) -> bool:
    """H1: the estimate applied to the undisclosed rises monotonically."""
    ests = [s.estimate for s in res.rounds]
    return all(b >= a - 1e-12 for a, b in zip(ests, ests[1:]))


def h2_unravels(res: RunResult, threshold: float = 0.5) -> bool:
    """H2: under the residual rule, most of the population ends up disclosed."""
    return res.dark_fraction < threshold


def h3_population_basis_is_stable(res_pop: RunResult, res_res: RunResult) -> bool:
    """H3: the rejected population-basis rule leaves strictly more agents dark."""
    return res_pop.dark_fraction > res_res.dark_fraction


# ----------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------

def report() -> None:
    line = "=" * 78
    print(line)
    print("RESIDUAL UNRAVELLING -- does darkness stop paying?")
    print("Foundations v0.17 5.1b (producers) and 5.1d cond. 1 (periods within a life)")
    print(line)

    agents = make_agents()
    truths = [a.true_debit for a in agents]
    print(f"\n{N_AGENTS} agents, lognormal true debit "
          f"(median {percentile(truths, 50):.3f}, mean {sum(truths)/len(truths):.3f}, "
          f"p90 {percentile(truths, 90):.3f}, max {max(truths):.3f})")
    print(f"disclosure cost ~ N({COST_MEAN}, {COST_SIGMA}), truncated at 0")

    print("\n" + line)
    print("A. RESIDUAL BASIS, estimate at the median of the undisclosed (5.1b as written)")
    print(line)
    a = run("residual", 50, agents)
    _trace(a)

    print("\n" + line)
    print("B. RESIDUAL BASIS, estimate at p75 -- 'err against the estimated party'")
    print("   (5.1d condition 2 / the conservative-count rule)")
    print(line)
    b = run("residual", 75, agents)
    _trace(b)

    print("\n" + line)
    print("C. CONTROL -- POPULATION BASIS, the rule 5.1b explicitly rejects")
    print(line)
    c = run("population", 50, agents)
    _trace(c)

    print("\n" + line)
    print("VERDICT")
    print(line)
    checks = [
        ("H1  residual estimate rises monotonically (A)", h1_dark_pool_worsens(a)),
        ("H1  residual estimate rises monotonically (B)", h1_dark_pool_worsens(b)),
        ("H2  residual basis unravels the pool (A)", h2_unravels(a)),
        ("H2  residual basis unravels the pool (B)", h2_unravels(b)),
        ("H3  population basis leaves MORE dark than residual", h3_population_basis_is_stable(c, a)),
    ]
    for label, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")

    print(f"\n  residual/median  -> {a.dark_fraction:6.1%} still dark after {len(a.rounds)} rounds")
    print(f"  residual/p75     -> {b.dark_fraction:6.1%} still dark after {len(b.rounds)} rounds")
    print(f"  population/median-> {c.dark_fraction:6.1%} still dark after {len(c.rounds)} rounds")

    dark_a = [x.true_debit for x in a.agents if not x.disclosed]
    if dark_a:
        print(f"\n  Who stays dark under the residual rule: true debit "
              f"min {min(dark_a):.3f}, median {percentile(dark_a, 50):.3f} "
              f"-- against a population median of {percentile(truths, 50):.3f}.")
        print("  The residue is the genuinely dirty tail, which is exactly who should")
        print("  be carrying a pessimistic estimate. That is the mechanism working,")
        print("  not the mechanism failing.")

    print("\n" + line)
    print("READ THIS BEFORE QUOTING THE NUMBERS")
    print(line)
    print("""
  1. Market access is NOT modelled. The origin-evidence ruling of 2026-08-22 (Foundations 4.8) bars a
     dark producer from transacting at all. That stick is far larger than anything here,
     so these figures are a LOWER BOUND on the pressure to disclose.
  2. Agents are myopic -- they compare this round's estimate, not the estimate they
     expect after everyone else moves. Foresight would unravel the pool FASTER, so
     myopia is the conservative assumption.
  3. The disclosure cost is a guess. It is the only free parameter that can stop
     unravelling on its own: raise it far enough and nobody moves. See --sweep-cost.
  4. Nothing here says the residual rule is FAIR, only that it is INCENTIVE-COMPATIBLE.
     Fairness of the estimate applied to the residue is a different question and is
     answered in 5.1d condition 2 and the self-care-floor exemption.
""")


def _trace(res: RunResult) -> None:
    print(f"  round  estimate   disclosed     dark   dark-mean-true   total-carried")
    shown = res.rounds if len(res.rounds) <= 12 else (
        res.rounds[:6] + [None] + res.rounds[-5:])
    for s in shown:
        if s is None:
            print("   ...")
            continue
        print(f"  {s.round_no:5d}  {s.estimate:8.4f}  {s.n_disclosed:9d} {s.n_dark:8d}   "
              f"{s.dark_mean_true:12.4f}   {s.carried_total:13.1f}")


DEMO_TRUE = [1.0, 2.0, 3.0, 4.0, 20.0]
DEMO_NAMES = ["Ana", "Ben", "Cal", "Dee", "Eve"]


def demo() -> dict:
    """A five-farm example small enough to check by hand.

    Five farms. Each one has a true debit -- the real damage it does per unit.
    Nobody knows these numbers except the farm itself. The books must use an
    estimate for any farm that shows no records.

        Ana 1    Ben 2    Cal 3    Dee 4    Eve 20

    A farm shows its records only when that lowers what it carries. Proving
    costs nothing in this example, so the rule is simply: show records if your
    true number is below the estimate.

    Run it two ways and compare. This is the whole argument in one page.
    """
    agents = [Agent(i, t, 0.0) for i, t in enumerate(DEMO_TRUE)]
    truth = sum(DEMO_TRUE)
    out = {}

    for basis in ("residual", "population"):
        rows = []
        ag = [Agent(a.idx, a.true_debit, a.cost) for a in agents]
        for r in range(10):
            dark = [a for a in ag if not a.disclosed]
            pool = [a.true_debit for a in (dark if basis == "residual" else ag)]
            est = percentile(pool, 50)
            books = sum(a.true_debit if a.disclosed else est for a in ag)
            movers = [a for a in dark if a.true_debit + a.cost < est]
            rows.append({
                "round": r,
                "dark_names": [DEMO_NAMES[a.idx] for a in dark],
                "pool": sorted(pool),
                "estimate": est,
                "books": books,
                "movers": [DEMO_NAMES[a.idx] for a in movers],
            })
            if not movers:
                break
            for a in movers:
                a.disclosed = True
        out[basis] = {
            "rows": rows,
            "final_dark": [DEMO_NAMES[a.idx] for a in ag if not a.disclosed],
            "final_books": rows[-1]["books"],
            "error": abs(rows[-1]["books"] - truth),
        }
    out["truth"] = truth
    return out


def print_demo() -> None:
    d = demo()
    line = "=" * 78
    print(line)
    print("FIVE FARMS -- the whole argument, small enough to check by hand")
    print(line)
    print("\nTrue debit of each farm (what it really costs the world, per unit):")
    for n, t in zip(DEMO_NAMES, DEMO_TRUE):
        print(f"    {n:4s} {t:5.1f}")
    print(f"\n    True total = {d['truth']:.0f}")
    print("\nNobody can see these numbers. A farm that shows no records is given")
    print("an ESTIMATE. A farm shows records only if that lowers what it carries.")
    print("Proving costs nothing here, so: show records if your true number is")
    print("below the estimate.\n")

    for basis, title in (("residual", "WAY 1 -- estimate from the DARK FARMS ONLY  (the rule in 5.1b)"),
                         ("population", "WAY 2 -- estimate from ALL FARMS  (the rule 5.1b rejects)")):
        b = d[basis]
        print(line)
        print(title)
        print(line)
        print(f"  {'round':>5}  {'farms still dark':<26} {'their numbers':<20} "
              f"{'estimate':>9}  {'books say':>10}  who shows records")
        for r in b["rows"]:
            pool = "[" + " ".join(f"{x:g}" for x in r["pool"]) + "]"
            print(f"  {r['round']:5d}  {', '.join(r['dark_names']) or '(none)':<26} "
                  f"{pool:<20} {r['estimate']:9.1f}  {r['books']:10.1f}  "
                  f"{', '.join(r['movers']) or '-- nobody moves, stop'}")
        print(f"\n  Still dark at the end : {', '.join(b['final_dark']) or '(none)'}")
        print(f"  Books say             : {b['final_books']:.1f}")
        print(f"  Truth                 : {d['truth']:.1f}")
        print(f"  ERROR                 : {b['error']:.1f}\n")

    print(line)
    print("WHAT THIS SHOWS")
    print(line)
    print(f"""
  WAY 1. The estimate goes up every round: 3, then 4, then 12, then 20.
  It goes up because the farms that leave are always the CLEAN ones. What is
  left behind is dirtier, so the average of what is left is higher. Each rise
  pushes out the next farm. At the end only Eve is dark, and Eve now carries
  20 -- her own true number. The books are EXACTLY right. Error {d['residual']['error']:.0f}.

  WAY 2. The estimate never moves. It is 3 in every round, because it is
  taken from all five farms and all five farms are always there. Ana and Ben
  show records. Then it stops. Cal, Dee and Eve stay dark for ever, and each
  one carries 3. Eve really costs 20 and carries 3. The books say
  {d['population']['final_books']:.0f} when the truth is {d['truth']:.0f}. Error {d['population']['error']:.0f}, and it never gets better.

  THE POINT. The two ways use the same farms and the same arithmetic. Only
  the SET the estimate is taken from is different. That one difference is the
  whole mechanism. Take the estimate from the dark farms and darkness gets
  more expensive every round. Take it from everybody and darkness is a
  permanent free ride.
""")


def sweep_cost() -> None:
    """The one parameter that can defeat unravelling on its own."""
    print("=" * 78)
    print("COST SWEEP -- at what disclosure cost does unravelling stall?")
    print("=" * 78)
    print(f"  {'cost_mean':>10}  {'dark_frac':>10}  {'rounds':>7}")
    global COST_MEAN
    saved = COST_MEAN
    try:
        for cm in (0.0, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.2):
            COST_MEAN = cm
            r = run("residual", 50, make_agents())
            print(f"  {cm:10.2f}  {r.dark_fraction:10.1%}  {len(r.rounds):7d}")
    finally:
        COST_MEAN = saved
    print("\n  Unravelling is robust while proving your figure costs less than the gap")
    print("  between your truth and the pool estimate. It stalls when proof costs more")
    print("  than the error it corrects -- which is the right place for it to stall.")


# ----------------------------------------------------------------------------
# self-tests
# ----------------------------------------------------------------------------

def test_percentile():
    assert abs(percentile([1, 2, 3, 4], 50) - 2.5) < 1e-9
    assert percentile([], 50) == 0.0
    assert percentile([7], 90) == 7
    assert abs(percentile([0, 10], 75) - 7.5) < 1e-9
    print("[ok] percentile")


def test_h1_monotone():
    a = run("residual", 50)
    assert h1_dark_pool_worsens(a), "residual estimate must never fall"
    print(f"[ok] H1 estimate rises monotonically "
          f"({a.rounds[0].estimate:.3f} -> {a.final.estimate:.3f})")


def test_h2_unravels():
    a = run("residual", 50)
    assert h2_unravels(a), f"expected unravelling, got {a.dark_fraction:.1%} dark"
    print(f"[ok] H2 residual basis unravels: {a.dark_fraction:.1%} still dark")


def test_h3_control_differs():
    """The load-bearing test: the rejected rule must behave WORSE."""
    ag = make_agents()
    res = run("residual", 50, ag)
    pop = run("population", 50, ag)
    assert h3_population_basis_is_stable(pop, res), (
        f"population basis left {pop.dark_fraction:.1%} dark, "
        f"residual left {res.dark_fraction:.1%} -- the residual rule is doing no work")
    print(f"[ok] H3 control: population basis {pop.dark_fraction:.1%} dark vs "
          f"residual {res.dark_fraction:.1%} -- 5.1b earns its place")


def test_conservative_percentile_helps():
    """5.1d condition 2: erring against the estimated party should unravel further."""
    ag = make_agents()
    lo = run("residual", 50, ag)
    hi = run("residual", 75, ag)
    assert hi.dark_fraction <= lo.dark_fraction + 1e-12, (
        "erring against the estimated party should not leave MORE agents dark")
    print(f"[ok] conservative estimate helps: p50 {lo.dark_fraction:.1%} dark, "
          f"p75 {hi.dark_fraction:.1%} dark")


def test_residue_is_the_dirty_tail():
    """Whoever stays dark should be worse than the population median, not better."""
    a = run("residual", 50)
    dark = [x.true_debit for x in a.agents if not x.disclosed]
    allt = [x.true_debit for x in a.agents]
    if not dark:
        print("[ok] residue empty -- pool fully unravelled")
        return
    assert percentile(dark, 50) > percentile(allt, 50), (
        "the agents who stay dark should be the dirty tail, not the clean one")
    print(f"[ok] residue is the dirty tail: dark median {percentile(dark, 50):.3f} "
          f"> population median {percentile(allt, 50):.3f}")


def test_carried_total_falls():
    """Disclosure should move the books toward the truth, not away from it."""
    a = run("residual", 50)
    true_total = sum(x.true_debit for x in a.agents)
    start_err = abs(a.rounds[0].carried_total - true_total)
    end_err = abs(a.final.carried_total - true_total)
    assert end_err < start_err, "disclosure must reduce the gap between books and truth"
    print(f"[ok] books approach truth: error {start_err:.1f} -> {end_err:.1f} "
          f"(true total {true_total:.1f})")


def test_demo_matches_hand_calculation():
    """The five-farm example is pinned. If these numbers move, the doc is wrong."""
    d = demo()
    assert d["truth"] == 30.0
    res_est = [r["estimate"] for r in d["residual"]["rows"]]
    assert res_est == [3.0, 4.0, 12.0, 20.0], res_est
    assert d["residual"]["final_dark"] == ["Eve"]
    assert d["residual"]["error"] == 0.0
    pop_est = [r["estimate"] for r in d["population"]["rows"]]
    assert pop_est == [3.0, 3.0], pop_est
    assert d["population"]["final_dark"] == ["Cal", "Dee", "Eve"]
    assert d["population"]["final_books"] == 12.0
    assert d["population"]["error"] == 18.0
    print("[ok] five-farm demo: residual estimate 3->4->12->20, error 0; "
          "population estimate flat at 3, error 18")


def run_tests():
    test_percentile()
    test_h1_monotone()
    test_h2_unravels()
    test_h3_control_differs()
    test_conservative_percentile_helps()
    test_residue_is_the_dirty_tail()
    test_carried_total_falls()
    test_demo_matches_hand_calculation()
    print("\nAll self-tests passed.")


# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--sweep-cost", action="store_true")
    ap.add_argument("--demo", action="store_true",
                    help="five-farm worked example, checkable by hand")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    if args.demo:
        print_demo()
        return 0
    report()
    if args.sweep_cost:
        print()
        sweep_cost()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
