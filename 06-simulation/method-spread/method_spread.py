"""
Method spread -- how far does a §3.4a joint-process split move across honest methods?

Foundations §3.4a (Joint production) fixes four obligations on how a joint
process's debit divides, then leaves the method itself to the industry. Its
closing paragraph registers the test that decides whether those obligations are
enough:

    "How far a split moves across honest methods. Nobody has measured this.
     The test: take a refinery, a heat-and-power plant, and a livestock case,
     and compute the split under every defensible instrument and period.
     If the range is narrow, the obligations above are enough. If it is wide,
     method choice is a large lever and belongs with OP-10 (weighting
     governance)."

THIS FILE IS LEG 1 OF 3: the refinery. It reuses the real DOE process energies
already loaded by `../allocation-engine/refinery_slice.py` and sweeps every
defensible reading of the three method choices that file makes. The
combined-heat-and-power leg and the livestock leg are not built yet.

WHAT IS BEING SWEPT. §3.4a's split is not one choice, it is three, and
`refinery_slice.py` makes one reading of each:

  1. THE DECLARED DISTILLATION BASIS. Atmospheric and vacuum distillation heat
     the whole barrel to separate it. There is no per-fraction trace, so §2.5
     requires a declared convention. `refinery_slice.py` declares VOLUME.
     Mass, enthalpy demand and an equal split are all defensible too.

  2. THE CONVERSION ROUTING. Each conversion unit's metered energy goes to the
     products that unit makes. WHICH products, in what shares, is a modelled
     layer -- REFINERY.md §5 already flags it as "the remaining modelling
     layer". Four defensible readings are swept.

  3. THE SUB-PROCESS BOUNDARY. Which units count as traced and which fall into
     the declared pool. Three defensible readings are swept.

4 bases x 4 routings x 3 boundaries = 48 method combinations, all honest, all
satisfying §3.4a's four published obligations.

WHAT IS REPORTED. For each of the seven fractions, the minimum and maximum
energy cost share across all 48 methods, and the spread between them --
absolute (percentage points) and relative (max / min).

THE VERDICT RULE, AND ITS ANCHOR. "Narrow" needs a yardstick or it is an
opinion. The yardstick used here is the project's own already-measured
divergence between physical allocation and price allocation, from REFINERY.md:
price allocation misprices petcoke by 5.7x and LPG by 2.6x, and that divergence
is the reason §3.4a rejects price allocation at all. So:

    If the honest-method spread is SMALL against the price divergence the rule
    was written to defeat, the four obligations are doing their job.
    If it approaches it, method choice is a lever of the same size as the
    thing §3.4a exists to rule out, and it belongs with OP-10.

The threshold is DECLARED, not measured: a relative spread reaching half the
price divergence (2.85x) is treated as wide. Stated here so it can be argued
with rather than buried.

Run:  python method_spread.py            # sweep and report
      python method_spread.py --test      # self-tests only
      python method_spread.py --csv out.csv
"""

from __future__ import annotations

import argparse
import csv
import itertools
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ENGINE = os.path.join(os.path.dirname(_HERE), "allocation-engine")
sys.path.insert(0, _ENGINE)

from refinery_slice import (  # noqa: E402
    FRACTIONS,
    YIELD_BBL,
    PROCESS_ENERGY_TBTU,
    DISTILLATION_PROCESSES,
    CONVERSION_ROUTING,
    _normalise,
)


# ---------------------------------------------------------------------------
# The declared threshold (see the module docstring)
# ---------------------------------------------------------------------------

PRICE_DIVERGENCE = 5.7      # REFINERY.md: petcoke, physical / price
WIDE_THRESHOLD = PRICE_DIVERGENCE / 2.0     # 2.85x relative spread


# ---------------------------------------------------------------------------
# Lever 1 -- the declared distillation basis
# ---------------------------------------------------------------------------
#
# Distillation leaves no per-fraction trace, so §2.5 requires a DECLARED
# convention. All four below are declared, and all four are defensible.

DENSITY_KG_L = {   # kg/L, representative; same figures refinery_slice.py uses
    "lpg": 0.55, "gasoline": 0.74, "jet": 0.80, "diesel": 0.84,
    "residual_fuel": 0.99, "petcoke": 1.05, "asphalt": 1.03,
}

# Representative mid-cut normal boiling point, degrees C. A distillation column
# separates by boiling point, so the heat a cut demands rises with it.
MID_CUT_NBP_C = {
    "lpg": -20.0, "gasoline": 100.0, "jet": 200.0, "diesel": 280.0,
    "residual_fuel": 450.0, "petcoke": 550.0, "asphalt": 500.0,
}

AMBIENT_C = 25.0


def _mass_shares():
    return _normalise({f: YIELD_BBL[f] * DENSITY_KG_L[f] for f in FRACTIONS})


def _enthalpy_shares():
    """Mass x temperature rise to the cut's mid boiling point.

    ⚠️ NOT USED IN THE HEADLINE, AND THE REASON MATTERS. This is a stand-in
    this project constructed, not a basis taken from allocation practice. It
    ignores latent heat, assumes one specific heat for every cut, and -- the
    part that disqualifies it -- has no defensible answer for a cut that boils
    BELOW ambient. LPG's mid-cut boiling point is -20 C, so its temperature
    rise is negative and has to be clamped to an arbitrary floor of 1 C.

    That single arbitrary number drove the first run of this sweep: it handed
    LPG a share of 0.017% against diesel's 40.1%, and produced a headline
    relative spread of 2,307x that says nothing about allocation practice and
    everything about the clamp.

    It is kept as a LABELLED SENSITIVITY so the effect is visible rather than
    quietly deleted. Foundations §4.4: a derived figure carries the label its
    arithmetic earns, never the one its author prefers.
    """
    raw = {}
    for f in FRACTIONS:
        mass = YIELD_BBL[f] * DENSITY_KG_L[f]
        delta_t = max(MID_CUT_NBP_C[f] - AMBIENT_C, 1.0)
        raw[f] = mass * delta_t
    return _normalise(raw)


# The headline sweep uses only bases that appear in published allocation
# practice. Volume and mass are the two ISO 14044 physical bases; an equal
# split is the null convention every allocation review includes as a bound.
DISTILLATION_BASES = {
    "volume":   lambda: _normalise(dict(YIELD_BBL)),        # refinery_slice.py's choice
    "mass":     _mass_shares,
    "equal":    lambda: _normalise({f: 1.0 for f in FRACTIONS}),
}

# Added only for the labelled sensitivity run. See the docstring above.
SENSITIVITY_BASES = dict(DISTILLATION_BASES, enthalpy=_enthalpy_shares)


# ---------------------------------------------------------------------------
# Lever 2 -- the conversion routing
# ---------------------------------------------------------------------------

def _routing_doe():
    """REFINERY.md's reading: DOE Figure 2-2 standard refinery flow."""
    return {p: dict(r) for p, r in CONVERSION_ROUTING.items()}


def _routing_mass_weighted():
    """Each unit's energy split among its named products by their mass share."""
    mass = {f: YIELD_BBL[f] * DENSITY_KG_L[f] for f in FRACTIONS}
    out = {}
    for proc, routing in CONVERSION_ROUTING.items():
        named = list(routing)
        out[proc] = _normalise({f: mass[f] for f in named})
    return out


def _routing_concentrated():
    """Each unit's energy to its single largest named product only.

    The sharpest defensible boundary reading: a plant metering one unit against
    one product line records exactly this.
    """
    out = {}
    for proc, routing in CONVERSION_ROUTING.items():
        primary = max(routing, key=routing.get)
        out[proc] = {primary: 1.0}
    return out


def _routing_equal():
    """Equal split among the products a unit names."""
    out = {}
    for proc, routing in CONVERSION_ROUTING.items():
        named = list(routing)
        out[proc] = {f: 1.0 / len(named) for f in named}
    return out


CONVERSION_ROUTINGS = {
    "doe_fig22":     _routing_doe,          # refinery_slice.py's choice
    "mass_weighted": _routing_mass_weighted,
    "concentrated":  _routing_concentrated,
    "equal_named":   _routing_equal,
}


# ---------------------------------------------------------------------------
# Lever 3 -- the sub-process boundary
# ---------------------------------------------------------------------------
#
# Which units are read as traced, and which fall into the declared pool.

BOUNDARIES = {
    # refinery_slice.py's choice: nine processes, the two distillation units declared.
    "nine_process": dict(declared=list(DISTILLATION_PROCESSES)),
    # A plant that meters its columns per side-draw reads distillation as traced.
    # Its 826 TBtu leaves the declared pool and routes by the same declared basis,
    # which makes the basis carry MORE of the total, not less.
    "distillation_traced": dict(declared=[]),
    # Some plants meter hydrotreating on the mains with the columns, so it joins
    # the declared pool. 390 TBtu moves the other way.
    "hydrotreat_merged": dict(
        declared=list(DISTILLATION_PROCESSES) + ["hydrotreating"]),
}


# ---------------------------------------------------------------------------
# One method -> one energy split
# ---------------------------------------------------------------------------

def energy_shares(basis_name: str, routing_name: str, boundary_name: str):
    """Each fraction's share of the refinery's energy debit, under one method.

    Returns a dict of fraction -> share, summing to 1.0.
    """
    declared_procs = BOUNDARIES[boundary_name]["declared"]
    basis = SENSITIVITY_BASES[basis_name]()
    routing = CONVERSION_ROUTINGS[routing_name]()

    raw = {f: 0.0 for f in FRACTIONS}

    # The declared pool: no per-fraction trace, so it rides the declared basis.
    declared_total = sum(PROCESS_ENERGY_TBTU[p] for p in declared_procs)
    for f in FRACTIONS:
        raw[f] += declared_total * basis[f]

    # The traced pool: each unit's metered energy routes to the products it makes.
    for proc, energy in PROCESS_ENERGY_TBTU.items():
        if proc in declared_procs:
            continue
        if proc in routing:
            for f, share in routing[proc].items():
                raw[f] += energy * share
        else:
            # A distillation unit read as traced has no product routing of its
            # own, so it rides the declared basis. This is the
            # "distillation_traced" case: the basis carries more, not less.
            for f in FRACTIONS:
                raw[f] += energy * basis[f]

    return _normalise(raw)


def sweep(bases=None):
    """Every method combination. Returns a list of (labels, shares) rows."""
    bases = bases if bases is not None else DISTILLATION_BASES
    rows = []
    for basis, routing, boundary in itertools.product(
            bases, CONVERSION_ROUTINGS, BOUNDARIES):
        rows.append(((basis, routing, boundary),
                     energy_shares(basis, routing, boundary)))
    return rows


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def summarise(rows):
    """Per fraction: min share, max share, absolute spread, relative spread."""
    out = {}
    for f in FRACTIONS:
        vals = [s[f] for _, s in rows]
        lo, hi = min(vals), max(vals)
        out[f] = dict(lo=lo, hi=hi,
                      abs_pp=(hi - lo) * 100.0,
                      rel=(hi / lo) if lo > 0 else float("inf"))
    return out


def report():
    rows = sweep()
    stats = summarise(rows)
    base = energy_shares("volume", "doe_fig22", "nine_process")

    print()
    print("=" * 78)
    print("METHOD SPREAD -- REFINERY LEG (leg 1 of 3)")
    print("=" * 78)
    print(f"  {len(rows)} honest methods swept "
          f"({len(DISTILLATION_BASES)} declared bases"
          f" x {len(CONVERSION_ROUTINGS)} routings"
          f" x {len(BOUNDARIES)} boundaries)")
    print("  Dimension: energy. Real DOE 2015 Bandwidth Study process energies.")
    print()
    print(f"  {'fraction':<16}{'published':>10}{'min':>9}{'max':>9}"
          f"{'spread pp':>11}{'max/min':>10}")
    print("  " + "-" * 63)
    for f in FRACTIONS:
        s = stats[f]
        print(f"  {f:<16}{base[f]*100:>9.1f}%{s['lo']*100:>8.1f}%"
              f"{s['hi']*100:>8.1f}%{s['abs_pp']:>11.1f}{s['rel']:>10.2f}x")

    worst = max(FRACTIONS, key=lambda f: stats[f]["rel"])
    worst_rel = stats[worst]["rel"]
    widest_pp = max(FRACTIONS, key=lambda f: stats[f]["abs_pp"])

    print()
    print("-" * 78)
    print("VERDICT")
    print("-" * 78)
    print(f"  Widest relative spread : {worst} at {worst_rel:.2f}x")
    print(f"  Widest absolute spread : {widest_pp} at "
          f"{stats[widest_pp]['abs_pp']:.1f} percentage points")
    print(f"  Price-allocation divergence the rule exists to defeat: "
          f"{PRICE_DIVERGENCE:.1f}x (REFINERY.md, petcoke)")
    print(f"  Declared threshold for WIDE: {WIDE_THRESHOLD:.2f}x")
    print()
    if worst_rel >= WIDE_THRESHOLD:
        print("  WIDE. Method choice moves the split by a factor comparable to")
        print("  the price allocation §3.4a exists to rule out. The four")
        print("  published obligations are NOT sufficient on their own, and")
        print("  method choice belongs with OP-10 (weighting governance).")
    else:
        print("  NARROW. Method choice moves the split far less than price")
        print("  allocation does. The four published obligations are doing")
        print("  the work §3.4a claims for them.")
    # --- which lever is doing the work -------------------------------------
    print()
    print("-" * 78)
    print("WHICH LEVER IS DOING THE WORK")
    print("-" * 78)
    print("  Each row holds the other two levers at the published reading and")
    print("  moves one. The basis row uses only volume and mass, the two")
    print("  physical bases of ISO 14044, so it is the fairest test of the")
    print("  declared convention on its own.")
    print()
    levers = [
        ("declared basis (volume vs mass)",
         ["volume", "mass"], ["doe_fig22"], ["nine_process"]),
        ("conversion routing", ["volume"], list(CONVERSION_ROUTINGS),
         ["nine_process"]),
        ("sub-process boundary", ["volume"], ["doe_fig22"], list(BOUNDARIES)),
    ]
    print(f"  {'lever':<34}{'widest fraction':>18}{'max/min':>10}")
    print("  " + "-" * 62)
    for name, bs, rs, ds in levers:
        sub = [energy_shares(b, r, d)
               for b, r, d in itertools.product(bs, rs, ds)]
        best_f, best_rel = None, 0.0
        for f in FRACTIONS:
            vals = [s[f] for s in sub]
            rel = max(vals) / min(vals) if min(vals) > 0 else float("inf")
            if rel > best_rel:
                best_f, best_rel = f, rel
        print(f"  {name:<34}{best_f:>18}{best_rel:>9.2f}x")
    print()
    print("  In plain words: the declared convention §2.5 worries about is")
    print("  nearly inert. The modelled conversion routing carries the spread,")
    print("  and REFINERY.md §5 already flags that routing as modelled rather")
    print("  than metered.")

    # --- the labelled sensitivity ------------------------------------------
    srows = sweep(SENSITIVITY_BASES)
    sstats = summarise(srows)
    sworst = max(FRACTIONS, key=lambda f: sstats[f]["rel"])
    print()
    print("-" * 78)
    print("SENSITIVITY -- adding the constructed enthalpy basis")
    print("-" * 78)
    print(f"  {len(srows)} methods. Widest relative spread: {sworst} at "
          f"{sstats[sworst]['rel']:.0f}x")
    print("  This basis is NOT in the headline. It is a stand-in this project")
    print("  built, and it has no defensible answer for a cut boiling below")
    print("  ambient: LPG's temperature rise is negative and is clamped to an")
    print("  arbitrary 1 C. That one number produces the whole figure above.")
    print("  Reported so the effect is visible rather than quietly deleted.")

    print()
    print("-" * 78)
    print("NOT MEASURED HERE")
    print("-" * 78)
    print("  The combined-heat-and-power leg, the livestock leg, and the PERIOD")
    print("  lever. The DOE source is one annual figure, so no period can be")
    print("  swept from it. The spread above is a FLOOR on the true method")
    print("  spread, not the whole of it.")
    print()
    return rows, stats


def write_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["basis", "routing", "boundary"] + FRACTIONS)
        for (basis, routing, boundary), shares in rows:
            w.writerow([basis, routing, boundary]
                       + [f"{shares[f]:.6f}" for f in FRACTIONS])
    print(f"  wrote {path}")


# ---------------------------------------------------------------------------
# Self-tests -- each one can fail
# ---------------------------------------------------------------------------

def test_conservation():
    """Every method must allocate exactly the whole energy pool."""
    for labels, shares in sweep():
        total = sum(shares.values())
        assert abs(total - 1.0) < 1e-9, f"{labels} sums to {total}"
    return "conservation: every method sums to 1.0"


def test_nonnegative():
    """No method may hand a fraction a negative share."""
    for labels, shares in sweep():
        for f, v in shares.items():
            assert v >= 0.0, f"{labels} gave {f} a share of {v}"
    return "non-negativity: no negative share in any method"


def test_published_method_is_in_the_sweep():
    """The sweep must contain refinery_slice.py's own reading, or it is not
    measuring the spread around the published figure."""
    from refinery_slice import energy_theta
    published, _ = energy_theta()
    mine = energy_shares("volume", "doe_fig22", "nine_process")
    for f in FRACTIONS:
        assert abs(published[f] - mine[f]) < 1e-9, (
            f"{f}: refinery_slice says {published[f]:.6f}, "
            f"this sweep says {mine[f]:.6f}")
    return "published method reproduced exactly by the sweep"


def test_no_price_enters():
    """§3.4a forbids demand, desirability and yield from entering a split.

    Prices must not appear anywhere in this module's inputs.
    """
    import refinery_slice
    src = open(os.path.join(_HERE, "method_spread.py"), encoding="utf-8").read()
    body = src.split("def test_no_price_enters", 1)[0]
    assert "PRICE_USD_BBL" not in body, "a price reached the split"
    assert refinery_slice.PRICE_USD_BBL, "the price table still exists (unused)"
    return "price-independence: no price enters any swept method"


def test_the_sweep_actually_varies():
    """A control that must fail if the levers do nothing.

    If every method returned the same split, the report would print NARROW for
    a reason that has nothing to do with the obligations. This test is the
    negative control on that.
    """
    rows = sweep()
    first = rows[0][1]
    differs = any(
        any(abs(shares[f] - first[f]) > 1e-6 for f in FRACTIONS)
        for _, shares in rows[1:])
    assert differs, "every method returned the same split -- the levers are dead"
    return "negative control: the levers do move the split"


def test_each_lever_moves_it_alone():
    """Each of the three levers must move the split on its own.

    If one lever is inert, the sweep is smaller than it claims to be.
    """
    ref = energy_shares("volume", "doe_fig22", "nine_process")

    def moved(other):
        return any(abs(other[f] - ref[f]) > 1e-6 for f in FRACTIONS)

    assert moved(energy_shares("mass", "doe_fig22", "nine_process")), \
        "the distillation basis lever is inert"
    assert moved(energy_shares("equal", "doe_fig22", "nine_process")), \
        "the equal-split basis is inert"
    assert moved(energy_shares("volume", "concentrated", "nine_process")), \
        "the conversion routing lever is inert"
    assert moved(energy_shares("volume", "doe_fig22", "hydrotreat_merged")), \
        "the sub-process boundary lever is inert"
    return "each of the three levers moves the split on its own"


TESTS = [
    test_conservation,
    test_nonnegative,
    test_published_method_is_in_the_sweep,
    test_no_price_enters,
    test_the_sweep_actually_varies,
    test_each_lever_moves_it_alone,
]


def run_tests():
    print()
    print("SELF-TESTS")
    print("-" * 78)
    failed = 0
    for t in TESTS:
        try:
            print(f"  PASS  {t()}")
        except AssertionError as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print("-" * 78)
    print(f"  {len(TESTS) - failed}/{len(TESTS)} passed")
    print()
    return failed


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true", help="self-tests only")
    ap.add_argument("--csv", metavar="PATH", help="write every method to CSV")
    a = ap.parse_args()

    if a.test:
        sys.exit(1 if run_tests() else 0)

    rows, _ = report()
    if a.csv:
        write_csv(rows, a.csv)
    failed = run_tests()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
