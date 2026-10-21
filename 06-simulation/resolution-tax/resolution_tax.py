"""
Resolution tax -- how far apart are two producers of ONE good, same physical
process, when one can afford to read the chain finely and the other cannot?

REQUEST sr-20260905-sweep-producers-of-one-good-by-scale-and-by-.
Source objection: coywolf c40752, "3.4a's coarse-reading-is-a-ceiling result
errs against the producer ... a charge on whoever cannot buy instruments."

THE RULE UNDER TEST (Foundations 3.4a). A co-product carries the cost of the
steps it passed through, divided by its own mass. A producer reads the chain as
OPAQUE BLOCKS; a product that passed any step of a block carries the whole
block. Cuts between blocks are instruments. More cuts, finer reading, lower
figure, never higher (the ceiling theorem, chain-resolution/).

WHAT THIS ADDS. chain-resolution swept every partition of one chain. It did not
ask WHO can afford which partition. Here a plant has a fixed physical process
(n steps, m co-products leaving at different steps) and many producers of it at
different scales. Each producer can afford b cuts, b rising with scale. The
published figure of the good is read per producer. We measure the spread.

DECLARED, so it can be argued with (none of it is in Foundations):
  * step costs: lognormal, sigma = SIGMA, rescaled so a chain totals 100 h
  * each of the m co-products leaves after a step drawn uniformly from 1..n
  * the good measured is a random one of the m
  * instruments cost H hours per cut per year; a producer of Q kg a year works
    L = Q * L_PER_KG hours and spends fraction S of them on instruments, so
    it buys b = floor(S * L / H) cuts. Q is log-uniform over [Q_LO, Q_HI]
  * cut placement: PLANT-WIDE GREEDY (the cut that lowers the summed charge of
    all m co-products most is bought first). Alternative: RANDOM placement.
  * instrument cost is NOT in the published figure (Foundations 4.3: the setup
    price sits on the asset and is never divided into the goods). It is
    reported separately, as hours per kg, so the reader can see what the
    figure leaves out.

Run:   python resolution_tax.py            # full run, then self-tests
       python resolution_tax.py --test     # self-tests only
"""

from __future__ import annotations

import argparse
import math
import os
import random
import statistics as st
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "chain-resolution"))

SEED = 20261019
SIGMA = 0.8
CHAIN_H = 100.0
M_DEFAULT = 4
H_DEFAULT = 40.0        # hours per cut per year
S_DEFAULT = 0.02        # share of own labour a producer will spend on instruments
L_PER_KG = 0.05         # labour hours per kg, whole plant
Q_LO, Q_HI = 1e2, 1e7   # kg per year
N_PRODUCERS = 200
N_PROCESSES = 500
N_GRID = (2, 3, 5, 8, 12, 20, 30)


# ---------------------------------------------------------------------------
# The model
# ---------------------------------------------------------------------------

def draw_process(rng: random.Random, n: int, m: int):
    """One physical process: step costs (h) and the exit step of each co-product.

    Exit e means the product passed steps 1..e (1-indexed). Masses are drawn so
    the per-kg figure is defined; they cancel in every ratio reported.
    """
    raw = [math.exp(rng.gauss(0.0, SIGMA)) for _ in range(n)]
    tot = sum(raw)
    cost = [CHAIN_H * r / tot for r in raw]
    exits = [rng.randint(1, n) for _ in range(m)]
    mass = [math.exp(rng.gauss(0.0, 0.7)) * 100.0 for _ in range(m)]
    return cost, exits, mass


def charged_hours(cost, exit_step: int, cuts: frozenset) -> float:
    """Hours charged to a product that exits after `exit_step`, given the cuts.

    A cut at j separates step j from step j+1. The product carries every step up
    to the end of the block holding its exit step: the first cut at or after the
    exit, or the end of the chain.
    """
    n = len(cost)
    end = n
    for j in sorted(cuts):
        if j >= exit_step:
            end = j
            break
    return sum(cost[:end])


def place_cuts_greedy(cost, exits, b: int) -> frozenset:
    """Plant-wide greedy: each cut is the one that most lowers the summed charge
    of all co-products. Only a cut at some exit step can lower anything."""
    n = len(cost)
    cuts: set[int] = set()
    candidates = sorted({e for e in exits if e < n})
    for _ in range(min(b, len(candidates))):
        base = sum(charged_hours(cost, e, frozenset(cuts)) for e in exits)
        best, best_gain = None, 0.0
        for c in candidates:
            if c in cuts:
                continue
            gain = base - sum(charged_hours(cost, e, frozenset(cuts | {c})) for e in exits)
            if gain > best_gain + 1e-12:
                best, best_gain = c, gain
        if best is None:
            break
        cuts.add(best)
    return frozenset(cuts)


def place_cuts_random(cost, exits, b: int, rng: random.Random) -> frozenset:
    n = len(cost)
    gaps = list(range(1, n))
    rng.shuffle(gaps)
    return frozenset(gaps[: min(b, len(gaps))])


def cuts_afforded(q_kg: float, h_per_cut: float, share: float) -> int:
    return int(math.floor(share * q_kg * L_PER_KG / h_per_cut))


def simulate(n: int, *, m=M_DEFAULT, h=H_DEFAULT, share=S_DEFAULT,
             placement="greedy", n_proc=N_PROCESSES, n_prod=N_PRODUCERS,
             seed=SEED):
    """Return one record per process: the good's figure per producer, as ratios
    to the truth (finest reading), plus absolute h/kg."""
    rng = random.Random(seed * 1000 + n * 10 + m)
    out = []
    for _ in range(n_proc):
        cost, exits, mass = draw_process(rng, n, m)
        g = rng.randrange(m)                      # the good under study
        truth_h = charged_hours(cost, exits[g], frozenset(range(1, n)))
        coarse_h = charged_hours(cost, exits[g], frozenset())
        per_kg = mass[g]
        figs, bs = [], []
        cache: dict[int, float] = {}
        for _p in range(n_prod):
            q = math.exp(rng.uniform(math.log(Q_LO), math.log(Q_HI)))
            b = cuts_afforded(q, h, share)
            bs.append(b)
            if placement == "greedy":
                key = b
                if key not in cache:
                    cache[key] = charged_hours(
                        cost, exits[g], place_cuts_greedy(cost, exits, b))
                figs.append(cache[key])
            else:
                figs.append(charged_hours(
                    cost, exits[g], place_cuts_random(cost, exits, b, rng)))
        out.append({
            "n": n, "truth_h": truth_h, "coarse_h": coarse_h, "mass": per_kg,
            "figs_h": figs, "b": bs,
            "terminal": exits[g] == n,
        })
    return out


# ---------------------------------------------------------------------------
# Summaries
# ---------------------------------------------------------------------------

def summarise(recs):
    """Per-process spread = worst figure / best figure over its producers."""
    spreads, abs_gap, med_tax, share_tax15 = [], [], [], []
    for r in recs:
        best, worst = min(r["figs_h"]), max(r["figs_h"])
        spreads.append(worst / best)
        abs_gap.append((worst - best) / r["mass"])
        med = st.median(r["figs_h"])
        med_tax.append(med / r["truth_h"])
        share_tax15.append(sum(1 for f in r["figs_h"] if f / r["truth_h"] > 1.5)
                           / len(r["figs_h"]))
    def q(xs, p):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(p * len(xs)))]
    return {
        "spread_mean": st.mean(spreads), "spread_median": st.median(spreads),
        "spread_p10": q(spreads, 0.10), "spread_p90": q(spreads, 0.90),
        "spread_sd": st.pstdev(spreads),
        "gap_h_per_kg_median": st.median(abs_gap),
        "median_producer_tax": st.mean(med_tax),
        "share_over_1p5": st.mean(share_tax15),
        "terminal_share": st.mean(1.0 if r["terminal"] else 0.0 for r in recs),
        "worst_h_per_kg_median": st.median(max(r["figs_h"]) / r["mass"] for r in recs),
        "best_h_per_kg_median": st.median(min(r["figs_h"]) / r["mass"] for r in recs),
    }


def slope(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def boot_slope(rows_by_n, key, rng, reps=300):
    """Bootstrap the slope of `key` against ln(n) by resampling processes."""
    ns = sorted(rows_by_n)
    out = []
    for _ in range(reps):
        ys = []
        for n in ns:
            recs = rows_by_n[n]
            samp = [recs[rng.randrange(len(recs))] for _ in recs]
            ys.append(st.mean(max(r["figs_h"]) / min(r["figs_h"]) for r in samp))
        out.append(slope([math.log(n) for n in ns], ys))
    out.sort()
    return out[int(0.025 * reps)], out[int(0.5 * reps)], out[int(0.975 * reps)]


def instrument_hours_per_kg(h, share, n):
    """What the published figure leaves out: a producer buying every needed cut
    pays at most (n-1)*h hours a year; spread over its output."""
    rows = []
    for q in (1e3, 1e4, 1e5, 1e6, 1e7):
        b = min(n - 1, cuts_afforded(q, h, share))
        rows.append((q, b, b * h / q))
    return rows


# ---------------------------------------------------------------------------
# Self-tests. Each can fail.
# ---------------------------------------------------------------------------

def test_matches_chain_resolution_on_steer() -> str:
    """My fast charge function must equal the project's tested one on all 64
    partitions of the steer, for every product."""
    import chain_resolution as cr
    c = cr.build_steer()
    names = c.step_names
    cost = [c.step(nm).labour_h for nm in names]
    n = len(names)
    checked = 0
    for blocks in cr.contiguous_partitions(n):
        cuts = frozenset(hi for lo, hi in blocks if hi < n)
        for p in c.products:
            e = max(names.index(s) for s in c.passes[p]) + 1
            theirs = cr.product_cost(c, p, blocks)["labour_h"]
            mine = charged_hours(cost, e, cuts)
            assert abs(theirs - mine) < 1e-9, f"{p} {blocks}: {theirs} != {mine}"
            checked += 1
    return f"agrees with chain-resolution on {checked} product-partition pairs"


def test_ceiling_more_cuts_never_raises() -> str:
    rng = random.Random(7)
    k = 0
    for _ in range(300):
        n = rng.randint(2, 15)
        cost, exits, _m = draw_process(rng, n, 4)
        all_gaps = list(range(1, n))
        a = frozenset(rng.sample(all_gaps, rng.randint(0, len(all_gaps))))
        extra = frozenset(a | set(rng.sample(all_gaps, rng.randint(0, len(all_gaps)))))
        for e in exits:
            assert charged_hours(cost, e, extra) <= charged_hours(cost, e, a) + 1e-9
            k += 1
    return f"adding cuts never raised a figure ({k} cases)"


def test_terminal_good_has_zero_spread() -> str:
    """A good that passes the whole chain cannot be taxed or helped."""
    rng = random.Random(3)
    for _ in range(50):
        cost, _e, _m = draw_process(rng, 9, 4)
        vals = {round(charged_hours(cost, 9, frozenset(c)), 9)
                for c in ([], [3], [2, 5], list(range(1, 9)))}
        assert len(vals) == 1, f"terminal good moved: {vals}"
    return "a terminal good reads the same at every resolution"


def test_level_equal_steps_matches_harmonic() -> str:
    """LEVEL CHECK, closed form. n equal-cost steps, one good leaving after a
    uniform step: coarse/fine = n/k, so its mean over k is H_n. Simulate it with
    SIGMA=0 and compare to the harmonic number."""
    global SIGMA
    old = SIGMA
    SIGMA = 0.0
    try:
        for n in (5, 12):
            rng = random.Random(11)
            xs = []
            for _ in range(20000):
                cost, exits, _m = draw_process(rng, n, 1)
                xs.append(charged_hours(cost, exits[0], frozenset())
                          / charged_hours(cost, exits[0], frozenset(range(1, n))))
            hn = sum(1.0 / j for j in range(1, n + 1))
            assert abs(st.mean(xs) - hn) < 0.06 * hn, f"n={n}: {st.mean(xs):.3f} vs H_n {hn:.3f}"
    finally:
        SIGMA = old
    return "equal-step coarse/fine mean equals the harmonic number H_n (n=5, 12)"


def test_steer_level_6p25() -> str:
    """LEVEL CHECK against the number Foundations 3.4a prints: hide 12.50 MJ/kg
    coarse against 2.00 fine, a ratio of 6.25."""
    import chain_resolution as cr
    c = cr.build_steer()
    n = len(c.steps)
    coarse = cr.product_cost_per_kg(c, "hide", [(0, n)])["energy_mj"]
    fine = cr.product_cost_per_kg(c, "hide", [(i, i + 1) for i in range(n)])["energy_mj"]
    assert abs(coarse - 12.5) < 1e-9 and abs(fine - 2.0) < 1e-9, (coarse, fine)
    assert abs(coarse / fine - 6.25) < 1e-9
    return "steer hide reads 12.50 coarse, 2.00 fine, 6.25x, as Foundations prints"


def test_sweep_is_not_inert() -> str:
    """NEGATIVE CONTROL. With no instruments for anyone the spread must be 1 (all
    equal). With scale-driven instruments it must exceed 1. If both were 1 the
    sweep would be measuring nothing."""
    none = simulate(8, share=0.0, n_proc=40, n_prod=30)
    assert all(max(r["figs_h"]) == min(r["figs_h"]) for r in none), "no-instrument world has spread"
    some = simulate(8, n_proc=40, n_prod=60)
    assert any(max(r["figs_h"]) > min(r["figs_h"]) + 1e-9 for r in some), "scale did nothing"
    return "no-instrument world has spread 1.00; scale world has spread above 1"


def test_greedy_beats_random_placement() -> str:
    """Greedy cuts must give a lower summed charge than random ones, on average.
    If they did not, the placement policy would be decoration."""
    rng = random.Random(9)
    g_sum = r_sum = 0.0
    for _ in range(300):
        cost, exits, _m = draw_process(rng, 12, 4)
        g = place_cuts_greedy(cost, exits, 2)
        r = place_cuts_random(cost, exits, 2, rng)
        g_sum += sum(charged_hours(cost, e, g) for e in exits)
        r_sum += sum(charged_hours(cost, e, r) for e in exits)
    assert g_sum < r_sum, (g_sum, r_sum)
    return f"greedy placement charges {g_sum / r_sum:.2f} of random placement"


TESTS = [
    test_matches_chain_resolution_on_steer,
    test_ceiling_more_cuts_never_raises,
    test_terminal_good_has_zero_spread,
    test_level_equal_steps_matches_harmonic,
    test_steer_level_6p25,
    test_sweep_is_not_inert,
    test_greedy_beats_random_placement,
]


def run_tests() -> int:
    print("\nSELF-TESTS\n" + "-" * 78)
    failed = 0
    for t in TESTS:
        try:
            print(f"  PASS  {t()}")
        except AssertionError as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print("-" * 78 + f"\n  {len(TESTS) - failed}/{len(TESTS)} passed\n")
    return failed


# ---------------------------------------------------------------------------
# Main run
# ---------------------------------------------------------------------------

def table(title, rows, header):
    print(f"\n{title}\n" + "-" * 78)
    print(header)
    for r in rows:
        print(r)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        sys.exit(1 if run_tests() else 0)

    print(f"seed {SEED}; {N_PROCESSES} processes x {N_PRODUCERS} producers per cell; "
          f"m={M_DEFAULT} co-products; H={H_DEFAULT} h/cut; S={S_DEFAULT}; "
          f"L={L_PER_KG} h/kg; Q log-uniform {Q_LO:.0e}..{Q_HI:.0e} kg/yr")

    # 1. The headline sweep over chain length
    rows, by_n = [], {}
    for n in N_GRID:
        recs = simulate(n)
        by_n[n] = recs
        s = summarise(recs)
        rows.append(
            f"{n:>4} {s['spread_mean']:>8.2f} {s['spread_median']:>8.2f} "
            f"{s['spread_p10']:>7.2f} {s['spread_p90']:>7.2f} "
            f"{s['best_h_per_kg_median']:>9.3f} {s['worst_h_per_kg_median']:>9.3f} "
            f"{s['gap_h_per_kg_median']:>9.3f} {s['median_producer_tax']:>9.2f} "
            f"{s['share_over_1p5']:>8.2f} {s['terminal_share']:>7.2f}")
    table("1. SPREAD (worst/best published figure of one good) BY CHAIN LENGTH n", rows,
          f"{'n':>4} {'mean':>8} {'median':>8} {'p10':>7} {'p90':>7} "
          f"{'best h/kg':>9} {'worst h/kg':>9} {'gap h/kg':>9} {'med/true':>9} "
          f"{'>1.5x':>8} {'terminal':>7}")
    lo, mid, hi = boot_slope(by_n, "spread", random.Random(SEED + 1))
    print(f"\n  slope of mean spread against ln(n): {mid:.3f}  (95% bootstrap {lo:.3f} .. {hi:.3f})")
    ys = [summarise(by_n[n])["spread_mean"] for n in N_GRID]
    print(f"  spread at n={N_GRID[0]}: {ys[0]:.2f}; at n={N_GRID[-1]}: {ys[-1]:.2f}")

    # 2. Same, with spread measured only over goods that are NOT terminal
    rows = []
    for n in N_GRID:
        nt = [r for r in by_n[n] if not r["terminal"]]
        s = summarise(nt)
        rows.append(f"{n:>4} {len(nt):>6} {s['spread_mean']:>8.2f} {s['spread_median']:>8.2f}")
    table("2. SAME, goods that leave early only (terminal goods have spread 1.00 by theorem)",
          rows, f"{'n':>4} {'count':>6} {'mean':>8} {'median':>8}")

    # 3. Sensitivity: price of an instrument, and placement policy
    rows = []
    for h in (4.0, 40.0, 400.0):
        for pl in ("greedy", "random"):
            s = summarise(simulate(12, h=h, placement=pl, n_proc=200, n_prod=100))
            rows.append(f"{h:>8.0f} {pl:>8} {s['spread_mean']:>8.2f} "
                        f"{s['median_producer_tax']:>9.2f} {s['share_over_1p5']:>8.2f}")
    table("3. SENSITIVITY at n=12: instrument cost H and cut placement", rows,
          f"{'H h/cut':>8} {'place':>8} {'spread':>8} {'med/true':>9} {'>1.5x':>8}")

    rows = []
    for m in (2, 4, 8):
        s = summarise(simulate(12, m=m, n_proc=200, n_prod=100))
        rows.append(f"{m:>4} {s['spread_mean']:>8.2f} {s['median_producer_tax']:>9.2f}")
    table("4. SENSITIVITY at n=12: number of co-products m", rows,
          f"{'m':>4} {'spread':>8} {'med/true':>9}")

    # 5. What the published figure leaves out
    rows = [f"{q:>10.0e} {b:>4} {hk:>12.5f}" for q, b, hk in instrument_hours_per_kg(H_DEFAULT, S_DEFAULT, 12)]
    table("5. INSTRUMENT HOURS PER KG (NOT in the published figure), n=12, full set of cuts capped by affordability",
          rows, f"{'Q kg/yr':>10} {'cuts':>4} {'h/kg':>12}")

    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
