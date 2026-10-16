"""
Household consolidation -- how much does a two-adult household save, under the
max rule for fractional holdings, by routing co-products of one joint process
to ONE member instead of two?

THE REQUEST (sr-20261014-over-a-realistic-household-basket-two-adults).
Wubbitys c100994 on #8335: under max, two people holding 10% cuts (one of the
beef, one of the hide) carry 0.8 + 0.8 = 1.6 h; one person holding both carries
0.8 h. The lever exists. This file sizes it over a realistic basket.

THE RULE (Foundations §3.4a, conformance row 10i). For each parcel (each step
of a chain), per dimension, an account carries the step's cost times the
LARGEST mass fraction f_p of any co-product p that passed that step. Pieces of
one co-product add. The rule itself is `fractional_holdings.debit`, imported
unchanged; nothing here re-implements it.

THE SAVING, per process:
    S = debit(A) + debit(B) - debit(A and B merged into one account)

PARCEL IDENTITY (§3.4a, "Where a parcel's identity comes from"). A saving
exists only where A's and B's co-products point back at the SAME parcel. The
share of the smaller holding that does is `q`, the co-occurrence share. It is
not a choice the household makes; it is a fact of the supply chain. q = 1 is
the ceiling; shop-bought beef and imported leather sit near q = 0.

UNITS. Hours are domestic-plus-import embodied labour, the same unit as the
1,380 h/yr anchor (§3.5). Parcel size cancels: a household's fraction of a
parcel scales as 1/size and the parcel's cost as size. Self-test 6 checks it.

Run:   python 06-simulation/household-consolidation/household_consolidation.py
Test:  python 06-simulation/household-consolidation/household_consolidation.py --test
"""

import os
import random
import statistics
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "fractional-holdings"))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "chain-resolution"))

from chain_resolution import Chain, Step, DENSITY_KG_L, LITRES_PER_BBL  # noqa: E402
from fractional_holdings import debit, new_account  # noqa: E402
from refinery_slice import PROCESS_ENERGY_TBTU, YIELD_BBL  # noqa: E402

SEED = 20261016
N_DRAWS = 20000
TOL = 1e-9
HOUSEHOLD_DEBIT_H = 2 * 1380.0       # §3.5 anchor, two median adults. One reading.
GAL_L = 3.785

# ---------------------------------------------------------------------------
# Parameters: (low, central, high). Every one is DECLARED, with its basis.
# ---------------------------------------------------------------------------

P = {
    # steer -- whole-chain embodied labour per animal, raising to packaging.
    # Basis: ERM-scale ~0.06-0.16 h per kg retail beef x 250 kg (TRACK1 food
    # group 20 h/cap domestic; Track 3 adds imports). DECLARED range.
    "steer_h":        (15.0, 25.0, 40.0),
    # share of that chain both beef and hide pass: raising, feed, kill, hide-off
    "steer_shared":   (0.60, 0.75, 0.85),
    "beef_kg":        (250.0, 250.0, 250.0),     # chain-resolution steer
    "leather_per_hide_kg": (4.0, 5.0, 6.0),       # ~4.5 m2 x 1.2 mm x 0.9 g/cm3
    "hh_beef_kg":     (40.0, 54.0, 62.5),         # 2 adults; 62.5 = a quarter steer
    "hh_leather_kg":  (0.3, 1.0, 2.0),            # shoes, belts, a bag
    # refinery -- household petrol carry under NO division (whole chain
    # against petrol's own mass). Basis: ~0.7 jobs per $1M of gasoline final
    # demand x 1,800 h x ~$1,700 producer value = 2.1 h at value division,
    # x 1.97 (1 / petrol's value share of the refinery_slice slate) = 4.1 h.
    "gas_carry_h":    (2.0, 4.1, 16.0),
    "crude_share":    (0.30, 0.50, 0.70),         # of petrol's carry, crude input
    "hh_gas_gal":     (400.0, 900.0, 1500.0),
    "grill_lpg_kg":   (9.0, 36.0, 90.0),
    "heat_lpg_kg":    (700.0, 1041.0, 2080.0),    # 500-1,000 gal propane heating
    "heat_oil_kg":    (1300.0, 2000.0, 2700.0),   # 400-800 gal heating oil
    # co-occurrence share q: of the smaller holding, the share drawn from the
    # same parcels as the other. DECLARED, not measured.
    "q_lpg":          (0.05, 0.20, 1.00),         # ~1/3 of US propane is refinery LPG
    "q_heat_oil":     (0.20, 0.50, 1.00),
    "q_shop_beef":    (0.0, 0.0, 1e-6),           # see README: ~2e-7 h by count
}


def central():
    return {k: v[1] for k, v in P.items()}


def draw(rng):
    """Uniform over each declared range. A sweep, not a distribution of truth."""
    return {k: rng.uniform(lo, hi) for k, (lo, _, hi) in P.items()}


# ---------------------------------------------------------------------------
# Chains, calibrated in hours per parcel
# ---------------------------------------------------------------------------


def steer_chain(p):
    """One steer. Shared steps (raising + kill + hide-off), then beef-only steps."""
    sh = p["steer_h"] * p["steer_shared"]
    rest = p["steer_h"] - sh
    steps = [Step("raise_kill_hide", labour_h=sh), Step("beef_only", labour_h=rest)]
    return Chain(
        name="steer_h", note="calibrated hours", steps=steps,
        mass_kg={"beef": p["beef_kg"], "leather": p["leather_per_hide_kg"]},
        passes={"beef": {"raise_kill_hide", "beef_only"}, "leather": {"raise_kill_hide"}},
    )


REF_ORDER = ["atm_distillation", "vac_distillation", "coking", "fcc",
             "hydrocracking", "reforming", "alkylation", "hydrotreating"]
REF_PASSES = {   # chain-resolution's declared passage table, plus the crude parcel
    "lpg":      {"crude_in", "atm_distillation", "fcc", "alkylation"},
    "gasoline": {"crude_in", "atm_distillation", "fcc", "reforming", "alkylation",
                 "hydrotreating"},
    "diesel":   {"crude_in", "atm_distillation", "vac_distillation", "hydrocracking",
                 "hydrotreating"},
}


def refinery_chain(p, hh_gas_kg):
    """One 100 bbl crude parcel. Step hours split by DOE process energy (a proxy,
    declared), calibrated so the household's petrol carries p['gas_carry_h']."""
    mass = {f: YIELD_BBL[f] * LITRES_PER_BBL * DENSITY_KG_L[f] for f in REF_PASSES}
    gas_steps_h = p["gas_carry_h"] * mass["gasoline"] / hh_gas_kg
    crude_h = p["crude_share"] * gas_steps_h
    e = {s: PROCESS_ENERGY_TBTU[s] for s in REF_ORDER}
    e_gas = sum(e[s] for s in REF_PASSES["gasoline"] if s in e)
    per_e = (1 - p["crude_share"]) * gas_steps_h / e_gas
    steps = [Step("crude_in", labour_h=crude_h)] + [Step(s, labour_h=e[s] * per_e) for s in REF_ORDER]
    return Chain(name="refinery_h", note="calibrated hours", steps=steps,
                 mass_kg=mass, passes=dict(REF_PASSES))


# ---------------------------------------------------------------------------
# The household arithmetic
# ---------------------------------------------------------------------------


def account(chain, holdings):
    a = new_account(chain)
    for prod, frac in holdings.items():
        a["held"][prod] += frac
    return a


def saving(chain, hold_a, hold_b, q=1.0, rule="max"):
    """S for one process. `q` scales the overlap: the share of each holding that
    points at the same parcels. Modelled as the shared part (q) plus a disjoint
    remainder (1 - q) that sits on separate parcels and cannot be consolidated."""
    def lab(acct):
        return debit(chain, acct, rule)["labour_h"]
    sa = {k: v * q for k, v in hold_a.items()}
    sb = {k: v * q for k, v in hold_b.items()}
    merged = dict(sa)
    for k, v in sb.items():
        merged[k] = merged.get(k, 0.0) + v
    s = lab(account(chain, sa)) + lab(account(chain, sb)) - lab(account(chain, merged))
    split_total = lab(account(chain, hold_a)) + lab(account(chain, hold_b))
    return s, split_total


def household(p, kind, default="separated"):
    """Return (S, carry of these goods when split) in h/yr for one household type.

    kind: 'typical' (petrol + grill propane, shop beef and leather),
          'lpg_heat', 'oil_heat', 'farm_share' (one steer's beef and its hide).
    default: 'separated' = A holds one co-product, B the other (the lever's
             ceiling); 'mixed' = each adult holds half of every co-product.
    """
    out_s, out_split = 0.0, 0.0
    gas_kg = p["hh_gas_gal"] * GAL_L * DENSITY_KG_L["gasoline"]
    ref = refinery_chain(p, gas_kg)
    second = {"typical": ("lpg", p["grill_lpg_kg"], p["q_lpg"]),
              "farm_share": ("lpg", p["grill_lpg_kg"], p["q_lpg"]),
              "lpg_heat": ("lpg", p["heat_lpg_kg"], p["q_lpg"]),
              "oil_heat": ("diesel", p["heat_oil_kg"], p["q_heat_oil"])}[kind]
    prod, kg, q = second
    f_gas = gas_kg / ref.mass_kg["gasoline"]
    f_two = kg / ref.mass_kg[prod]
    hold = _assign({"gasoline": f_gas, prod: f_two}, default)
    s, split = saving(ref, hold[0], hold[1], q)
    out_s, out_split = out_s + s, out_split + split

    st = steer_chain(p)
    f_beef = p["hh_beef_kg"] / p["beef_kg"]
    f_leath = p["hh_leather_kg"] / p["leather_per_hide_kg"]
    q_st = 1.0 if kind == "farm_share" else p["q_shop_beef"]
    hold = _assign({"beef": f_beef, "leather": f_leath}, default)
    s, split = saving(st, hold[0], hold[1], q_st)
    return out_s + s, out_split + split


def _assign(fracs, default):
    prods = list(fracs)
    if default == "separated":
        return {prods[0]: fracs[prods[0]]}, {prods[1]: fracs[prods[1]]}
    half = {k: v / 2 for k, v in fracs.items()}
    return dict(half), dict(half)


KINDS = ("typical", "lpg_heat", "oil_heat", "farm_share")


# ---------------------------------------------------------------------------
# Self-tests. Each one can fail.
# ---------------------------------------------------------------------------


def one_block_steer(hours=8.0):
    return Chain(name="one_block", note="Wubbitys", steps=[Step("all", labour_h=hours)],
                 mass_kg={"beef": 250.0, "hide": 40.0},
                 passes={"beef": {"all"}, "hide": {"all"}})


def test_reproduces_wubbitys():
    c = one_block_steer()
    s, split = saving(c, {"beef": 0.1}, {"hide": 0.1})
    assert abs(split - 1.6) < TOL and abs(s - 0.8) < TOL, (split, s)
    return f"split {split:.2f} h, merged {split - s:.2f} h, saving {s:.2f} h"


def test_sum_rule_saves_nothing():
    rng = random.Random(SEED)
    for _ in range(2000):
        p = draw(rng)
        for kind in KINDS:
            gas_kg = p["hh_gas_gal"] * GAL_L * DENSITY_KG_L["gasoline"]
            ref = refinery_chain(p, gas_kg)
            s, _ = saving(ref, {"gasoline": rng.random() * 1e-6}, {"lpg": rng.random() * 1e-6},
                          rng.random(), rule="sum")
            assert abs(s) < 1e-12, s
    return "8,000 random households: sum-rule saving 0 every time"


def test_same_coproduct_split_saves_nothing():
    c = steer_chain(central())
    for f in (0.01, 0.1, 0.3):
        s, _ = saving(c, {"beef": f}, {"beef": f})
        assert abs(s) < TOL, s
    return "beef split between two adults: saving 0 at three fractions"


def test_bounded_by_smaller_shared_carry():
    rng = random.Random(SEED + 1)
    c = steer_chain(central())
    sh = c.steps[0].labour_h
    for _ in range(4000):
        fb, fl = rng.random(), rng.random()
        s, _ = saving(c, {"beef": fb}, {"leather": fl})
        assert -TOL <= s <= min(fb, fl) * sh + TOL, (fb, fl, s)
    return "4,000 random pairs: 0 <= S <= min(f) x shared hours (code check, not evidence)"


def test_zero_overlap_zero_saving():
    p = central()
    p["q_shop_beef"], p["q_lpg"] = 0.0, 0.0
    s, _ = household(p, "typical")
    assert abs(s) < TOL, s
    return "q = 0 on both processes: saving 0"


def test_parcel_size_cancels():
    c1 = one_block_steer(8.0)
    c2 = one_block_steer(80.0)
    c2.mass_kg = {k: v * 10 for k, v in c2.mass_kg.items()}
    s1, _ = saving(c1, {"beef": 0.1}, {"hide": 0.1})
    s2, _ = saving(c2, {"beef": 0.01}, {"hide": 0.01})
    assert abs(s1 - s2) < TOL, (s1, s2)
    return f"a parcel ten times larger gives the same hours ({s1:.2f} h)"


def test_calibration_hits_petrol_carry():
    p = central()
    gas_kg = p["hh_gas_gal"] * GAL_L * DENSITY_KG_L["gasoline"]
    ref = refinery_chain(p, gas_kg)
    a = account(ref, {"gasoline": gas_kg / ref.mass_kg["gasoline"]})
    got = debit(ref, a)["labour_h"]
    assert abs(got - p["gas_carry_h"]) < 1e-6, got
    return f"household petrol carries {got:.2f} h, as declared"


def test_mixed_default_near_zero_for_steer():
    p = central()
    p["q_lpg"] = 0.0
    s, _ = household(p, "farm_share", default="mixed")
    sep, _ = household(p, "farm_share", default="separated")
    assert s < 0.05 * sep, (s, sep)
    return f"farm share: mixed default saves {s:.3f} h against {sep:.2f} h separated"


TESTS = [test_reproduces_wubbitys, test_sum_rule_saves_nothing,
         test_same_coproduct_split_saves_nothing, test_bounded_by_smaller_shared_carry,
         test_zero_overlap_zero_saving, test_parcel_size_cancels,
         test_calibration_hits_petrol_carry, test_mixed_default_near_zero_for_steer]


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


def main():
    print(f"Household debit denominator: {HOUSEHOLD_DEBIT_H:,.0f} h/yr (2 x 1,380)\n")
    print(f"{'household':12} {'S central h':>12} {'% debit':>8} {'S p5':>8} {'S p95':>8} "
          f"{'S max':>8} {'% max':>7}")
    rng = random.Random(SEED)
    draws = [draw(rng) for _ in range(N_DRAWS)]
    for kind in KINDS:
        s0, _ = household(central(), kind)
        ss = sorted(household(d, kind)[0] for d in draws)
        p5, p95, mx = ss[int(0.05 * N_DRAWS)], ss[int(0.95 * N_DRAWS)], ss[-1]
        print(f"{kind:12} {s0:12.3f} {100 * s0 / HOUSEHOLD_DEBIT_H:7.3f}% {p5:8.3f} "
              f"{p95:8.3f} {mx:8.3f} {100 * mx / HOUSEHOLD_DEBIT_H:6.3f}%")
    print(f"\nseed {SEED}, {N_DRAWS} uniform draws over the declared ranges; "
          f"median of 'typical' = {statistics.median(household(d, 'typical')[0] for d in draws):.3f} h")


if __name__ == "__main__":
    sys.exit(run_tests() if "--test" in sys.argv else main())
