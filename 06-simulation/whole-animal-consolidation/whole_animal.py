"""
Whole-animal consolidation -- hours on the shared steps of ONE whole lamb and
ONE whole chicken, and the saving S a two-adult household gets by putting the
meat on one member and the fleece (or feathers) on the other.

THE REQUEST (sr-20261017-hours-on-the-shared-steps-of-raising-and-sla).
Extends ../household-consolidation/. The max rule is `fractional_holdings.debit`
and the saving is `household_consolidation.saving`, both imported unchanged.

THE CLOSED FORM. For two holdings of different co-products of one parcel,
    S = min(f_meat, f_fleece) x (hours of the steps BOTH co-products passed).
A whole animal bought by the household has f = 1 on both, so S = the shared
hours of one animal, whatever the flock size (parcel size cancels).

WHAT IS NOT MEASURED. Every hour figure below is a DECLARED (low, central,
high) range from the author's memory of published ranges, NOT re-read from a
source tonight (no network). See RESULTS.md, "What this does not show".

Run:   python 06-simulation/whole-animal-consolidation/whole_animal.py
Test:  python 06-simulation/whole-animal-consolidation/whole_animal.py --test
"""

import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.dirname(_HERE)
for sub in ("household-consolidation", "fractional-holdings", "chain-resolution"):
    sys.path.insert(0, os.path.join(_SIM, sub))

from chain_resolution import Chain, Step  # noqa: E402
from household_consolidation import saving, HOUSEHOLD_DEBIT_H  # noqa: E402

SEED = 20261020
N_DRAWS = 20000
TOL = 1e-9
BAR_H = 0.01 * HOUSEHOLD_DEBIT_H     # 1% of 2,760 h = 27.6 h, the public guess

# (low, central, high). Hours are DIRECT labour per animal unless stated.
LAMB = {
    # raising
    "ewe_h_per_year":   (2.0, 7.0, 15.0),      # whole-flock labour per ewe-year
    "lambs_per_ewe":    (0.95, 1.20, 1.60),    # lambs sold per ewe-year
    "feed_h":           (0.2, 0.5, 1.5),       # growing the hay/grain for ewe-share + lamb
    "haul_h":           (0.05, 0.10, 0.30),    # farm to plant
    # slaughter, steps BOTH meat and fleece/pelt pass
    "kill_skin_h":      (0.2, 0.5, 1.2),
    # steps meat only (do not change S; reported for the whole-chain total)
    "meat_only_h":      (0.3, 0.6, 1.0),
    # steps fleece only
    "fleece_only_h":    (0.10, 0.15, 0.40),    # shearing / skirting
    # indirect (input industries) multiplier on direct hours
    "indirect_mult":    (1.0, 1.6, 2.5),
    "f_meat":           (1.0, 1.0, 1.0),       # whole lamb, per the request
    "f_fleece":         (1.0, 1.0, 1.0),
    "animals_per_year": (1.0, 1.0, 2.0),
}

CHICKEN = {
    "grow_h":           (0.003, 0.006, 0.020),  # contract-grower labour per bird
    "catch_haul_h":     (0.001, 0.003, 0.008),
    "hatch_breeder_h":  (0.001, 0.003, 0.006),
    "feed_h":           (0.003, 0.006, 0.012),  # ~4.5 kg feed x 0.0007-0.0027 h/kg
    "kill_scald_pick_h": (0.008, 0.020, 0.040),  # plant steps before evisceration
    "meat_only_h":      (0.015, 0.030, 0.060),  # eviscerate, chill, pack
    "feather_only_h":   (0.0, 0.002, 0.01),
    "indirect_mult":    (1.0, 1.6, 2.5),
    "f_meat":           (1.0, 1.0, 1.0),
    "f_fleece":         (1.0, 1.0, 1.0),
    "animals_per_year": (26.0, 52.0, 104.0),    # one bird a week is central
}


def central(P):
    return {k: v[1] for k, v in P.items()}


def draw(P, rng):
    """Triangular, mode at the central value. A sweep, not a distribution of truth."""
    return {k: (lo if lo == hi else rng.triangular(lo, hi, mid)) for k, (lo, mid, hi) in P.items()}


def lamb_shared_h(p, kill_shared=True):
    raising = p["ewe_h_per_year"] / p["lambs_per_ewe"] + p["feed_h"] + p["haul_h"]
    kill = p["kill_skin_h"] if kill_shared else 0.0
    return (raising + kill) * p["indirect_mult"]


def chicken_shared_h(p):
    d = p["grow_h"] + p["catch_haul_h"] + p["hatch_breeder_h"] + p["feed_h"] + p["kill_scald_pick_h"]
    return d * p["indirect_mult"]


def chain_for(shared_h, meat_only_h, other_only_h, flock_n, other="fleece"):
    """A flock-year of `flock_n` animals. Each step's hours are per flock."""
    steps = [Step("shared", labour_h=shared_h * flock_n),
             Step("meat_only", labour_h=meat_only_h * flock_n),
             Step(other + "_only", labour_h=other_only_h * flock_n)]
    return Chain(name="whole_animal", note="calibrated hours", steps=steps,
                 mass_kg={"meat": 20.0 * flock_n, other: 2.5 * flock_n},
                 passes={"meat": {"shared", "meat_only"}, other: {"shared", other + "_only"}})


def S_one_animal(shared_h, meat_only_h, other_only_h, f_meat=1.0, f_other=1.0,
                 flock_n=50, rule="max", other="fleece"):
    """S for one animal's co-products, via the unchanged max rule. A holding of
    fraction f of one animal is f/flock_n of the flock's output."""
    c = chain_for(shared_h, meat_only_h, other_only_h, flock_n, other)
    s, split = saving(c, {"meat": f_meat / flock_n}, {other: f_other / flock_n}, 1.0, rule)
    return s, split


def run_species(P, kind):
    shared = lamb_shared_h if kind == "lamb" else chicken_shared_h
    other = "fleece" if kind == "lamb" else "feathers"
    ofld = "fleece_only_h" if kind == "lamb" else "feather_only_h"

    def one(p):
        sh = shared(p)
        mo = p["meat_only_h"] * p["indirect_mult"]
        oo = p[ofld] * p["indirect_mult"]
        s, _ = S_one_animal(sh, mo, oo, p["f_meat"], p["f_fleece"], other=other)
        return s, sh

    return one


def pct(h):
    return 100.0 * h / HOUSEHOLD_DEBIT_H


# ---------------------------------------------------------------------------
# Self-tests. Each can fail.
# ---------------------------------------------------------------------------


def test_closed_form_matches_max_rule():
    rng = random.Random(SEED)
    for _ in range(3000):
        sh, mo, oo = rng.uniform(0.01, 30), rng.uniform(0, 5), rng.uniform(0, 3)
        fm, fo = rng.random(), rng.random()
        s, _ = S_one_animal(sh, mo, oo, fm, fo, flock_n=rng.choice([1, 10, 200]))
        assert abs(s - min(fm, fo) * sh) < 1e-7, (sh, fm, fo, s)
    return "3,000 random animals: imported max rule = min(f) x shared hours (code check)"


def test_flock_size_cancels():
    a, _ = S_one_animal(7.0, 1.0, 0.2, flock_n=1)
    b, _ = S_one_animal(7.0, 1.0, 0.2, flock_n=500)
    assert abs(a - b) < TOL and abs(a - 7.0) < TOL, (a, b)
    return f"whole animal, flock of 1 and of 500: S = {a:.2f} h = the shared hours"


def test_sum_rule_saves_nothing():
    s, _ = S_one_animal(7.0, 1.0, 0.2, rule="sum")
    assert abs(s) < 1e-12, s
    return "sum rule: S = 0.000 h (control)"


def test_half_holding_halves_s():
    s1, _ = S_one_animal(8.0, 1.0, 0.2, 1.0, 1.0)
    s2, _ = S_one_animal(8.0, 1.0, 0.2, 0.5, 1.0)
    assert abs(s2 - s1 / 2) < TOL, (s1, s2)
    return f"meat holding halved: S {s1:.2f} -> {s2:.2f} h"


def test_only_meat_split_saves_nothing():
    c = chain_for(7.0, 1.0, 0.2, 50)
    s, _ = saving(c, {"meat": 0.5 / 50}, {"meat": 0.5 / 50}, 1.0)
    assert abs(s) < TOL, s
    return "meat split between two adults, nobody holds fleece: S = 0"


def test_hand_values():
    """Hand arithmetic fixed before the first run (see DECLARED.md)."""
    lc = central(LAMB)
    sl = lamb_shared_h(lc)
    assert abs(sl - 11.0933333) < 1e-4, sl         # (7/1.2 + 0.5 + 0.1 + 0.5) x 1.6
    cc = central(CHICKEN)
    sc = chicken_shared_h(cc)
    assert abs(sc - 0.0608) < 1e-6, sc             # (0.006+0.003+0.003+0.006+0.020) x 1.6
    assert abs(52 * sc - 3.1616) < 1e-6
    return f"lamb central {sl:.3f} h; chicken central {sc:.4f} h; 52 birds {52 * sc:.3f} h"


def test_shorn_live_is_smaller():
    lc = central(LAMB)
    assert lamb_shared_h(lc, kill_shared=False) < lamb_shared_h(lc, kill_shared=True)
    d = lamb_shared_h(lc) - lamb_shared_h(lc, False)
    assert abs(d - lc["kill_skin_h"] * lc["indirect_mult"]) < 1e-9
    return f"fleece shorn before slaughter drops {d:.2f} h from the shared steps"


TESTS = [test_closed_form_matches_max_rule, test_flock_size_cancels,
         test_sum_rule_saves_nothing, test_half_holding_halves_s,
         test_only_meat_split_saves_nothing, test_hand_values, test_shorn_live_is_smaller]


def run_tests():
    failed = 0
    for t in TESTS:
        try:
            print(f"PASS  {t.__name__}: {t()}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} self-tests pass")
    return 1 if failed else 0


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))]


def main():
    print(f"Household debit denominator {HOUSEHOLD_DEBIT_H:,.0f} h/yr; 1% bar = {BAR_H:.1f} h\n")
    rng = random.Random(SEED)
    out = {}
    for kind, P in (("lamb", LAMB), ("chicken", CHICKEN)):
        one = run_species(P, kind)
        c = central(P)
        s_c, sh_c = one(c)
        lo = {k: v[0] for k, v in P.items()}
        hi = {k: v[2] for k, v in P.items()}
        # corners: every hour parameter at the end that raises S (animals_per_year at its own end)
        raise_hi = {k: (v[2] if k not in ("lambs_per_ewe",) else v[0]) for k, v in P.items()}
        raise_lo = {k: (v[0] if k not in ("lambs_per_ewe",) else v[2]) for k, v in P.items()}
        s_hi, _ = one(raise_hi)
        s_lo, _ = one(raise_lo)
        draws = [draw(P, rng) for _ in range(N_DRAWS)]
        per_animal = [one(d)[0] for d in draws]
        per_year = [one(d)[0] * d["animals_per_year"] for d in draws]
        n_c = c["animals_per_year"]
        print(f"== {kind} ==")
        print(f"central: shared hours/animal {sh_c:.4f}; S/animal {s_c:.4f}; "
              f"animals/yr {n_c:g}; S/yr {s_c * n_c:.3f} h = {pct(s_c * n_c):.3f}% of debit")
        print(f"corner low : S/animal {s_lo:.4f}; S/yr {s_lo * lo['animals_per_year']:.3f}")
        print(f"corner high: S/animal {s_hi:.4f}; S/yr {s_hi * hi['animals_per_year']:.3f} "
              f"= {pct(s_hi * hi['animals_per_year']):.3f}%")
        print(f"draws S/animal p5 {q(per_animal, .05):.4f} p50 {q(per_animal, .5):.4f} "
              f"p95 {q(per_animal, .95):.4f} max {max(per_animal):.4f}")
        print(f"draws S/animal share >= bar: {sum(x >= BAR_H for x in per_animal) / N_DRAWS:.4f}")
        print(f"draws S/yr     p5 {q(per_year, .05):.3f} p50 {q(per_year, .5):.3f} "
              f"p95 {q(per_year, .95):.3f} max {max(per_year):.3f}  "
              f"share >= bar: {sum(x >= BAR_H for x in per_year) / N_DRAWS:.4f}")
        out[kind] = (s_c, n_c)
        if kind == "lamb":
            sh_live = lamb_shared_h(c, kill_shared=False)
            print(f"variant fleece shorn live (kill not shared): S/animal {sh_live:.3f} h "
                  f"= {pct(sh_live):.3f}%")
            for fm, ff in ((0.6, 1.0), (0.6, 0.7)):
                print(f"variant f_meat {fm}, f_fleece {ff}: S/animal {min(fm, ff) * sh_c:.3f} h")
            n = 2
            print(f"variant 2 lambs/yr, both paired: {2 * s_c:.3f} h = {pct(2 * s_c):.3f}%")
        else:
            print(f"variant per bird in minutes: {s_c * 60:.2f} min")
    print(f"\nseed {SEED}, {N_DRAWS} triangular draws per species over the declared ranges")


if __name__ == "__main__":
    sys.exit(run_tests() if "--test" in sys.argv else main())
