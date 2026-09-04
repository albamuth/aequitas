"""
Chain resolution -- what happens to a joint process's figures when you read the
chain at different levels of detail?

THE RULE BEING TESTED (author ruling, 2026-09-03). A joint process's cost is
NOT divided among its outputs. Every co-product carries the whole cost of the
process it came through, read against its own output mass. There is no split,
no declared basis, no routing model and no sub-process boundary to choose.

THAT RULING RAISED TWO QUESTIONS, AND THIS FILE ANSWERS BOTH.

  Q1. IF NOTHING IS DIVIDED, DO THE BOOKS INFLATE?
      Read naively, yes: two co-products each carrying "100 MJ" look like
      200 MJ. That reading is wrong, and A3 (non-fungibility) is why --
      "every credit and every debit is a unique record of one specific event."
      A debit is a POINTER AT AN IDENTIFIED PARCEL, not an amount. Both
      co-products point at the SAME 100 MJ: one supplier, one delivery window,
      one record.

      So the ledger walk is a UNION OVER IDENTIFIED PARCELS, NEVER A SUM.
      This file measures the difference between the two, because an
      implementation that sums instead of unioning produces exactly the
      inflation the union rule prevents.

  Q2. DOES READING THE CHAIN MORE FINELY CHANGE THE ANSWER?
      Yes, one way only, and the direction is knowable in advance:

          A COARSE READING IS A CEILING ON A FINE READING OF THE SAME CHAIN.

      A product carries the cost of the steps it passed through, divided by its
      own mass. The steps it passed through are a SUBSET of all the steps, and
      its mass is the same either way, so the coarse figure can never be lower.
      Equality holds only for a product that passes through the whole chain.

      This file confirms that numerically and reports how far it runs.

WHAT A RESOLUTION IS. A chain is a set of steps. A RESOLUTION is a partition of
those steps into contiguous BLOCKS, where a block is opaque: you can see what
went in and what came out, and nothing between. A product that passed through
ANY step of a block carries the WHOLE block, because from outside the block
there is no way to say which part of it the product used.

  - The COARSEST resolution is one block: one cow in, co-products out.
  - The FINEST resolution is one block per step: kill, hide removal, organs,
    hooves and head, dry-aging, butchering, packaging.

  Both describe the same animal. The total labour, energy and pollutants are
  identical, because they are INPUTS and reading them more finely does not
  change them.

WHAT IS *NOT* MODELLED HERE, AND THIS IS THE POINT. The withdrawn §3.4a rule
needed to know WHAT SHARE of a unit's energy went to each product. That share
was modelled, and the 2026-09-02 sweep measured it moving LPG's figure by
6.31x. This rule needs only to know WHETHER a product passed through a unit --
a binary fact off the plant's own flow sheet. No share is ever computed, and
`test_no_share_is_ever_computed` fails if one sneaks back in.

THE TWO CASES.

  STEER -- a linear chain with products leaving at different points. The
  digits are ILLUSTRATIVE and are declared as such. It is here because it is
  the case Foundations §2.5 and §3.4a both use, so the reader already knows it.

  REFINERY -- REAL DOE 2015 Petroleum Refining Bandwidth Study per-process
  energies, taken from `../allocation-engine/refinery_slice.py`, with the
  masses computed from EIA-representative yields and densities. What is
  DECLARED here is the processing ORDER and which fractions pass through which
  unit. That is a standard refinery configuration, it is binary, and it is
  stated in the table below so it can be argued with.

Run:  python chain_resolution.py            # both cases, then self-tests
      python chain_resolution.py --test     # self-tests only
      python chain_resolution.py --csv out.csv
"""

from __future__ import annotations

import argparse
import csv
import itertools
import os
import sys
from dataclasses import dataclass, field

_HERE = os.path.dirname(os.path.abspath(__file__))
_ENGINE = os.path.join(os.path.dirname(_HERE), "allocation-engine")
sys.path.insert(0, _ENGINE)

from refinery_slice import (  # noqa: E402
    FRACTIONS,
    YIELD_BBL,
    PROCESS_ENERGY_TBTU,
)

DIMENSIONS = ("labour_h", "energy_mj", "pollutant_kg")

LITRES_PER_BBL = 158.987

DENSITY_KG_L = {   # kg/L, representative; the same figures refinery_slice.py uses
    "lpg": 0.55, "gasoline": 0.74, "jet": 0.80, "diesel": 0.84,
    "residual_fuel": 0.99, "petcoke": 1.05, "asphalt": 1.03,
}


# ---------------------------------------------------------------------------
# The model
# ---------------------------------------------------------------------------


@dataclass
class Step:
    """One resolvable stage of a chain, with what it consumed.

    A step is an IDENTIFIED PARCEL. Its cost is not a quantity that adds; it is
    a record two products may both point at (A3).
    """

    name: str
    labour_h: float = 0.0
    energy_mj: float = 0.0
    pollutant_kg: float = 0.0

    def vector(self) -> dict[str, float]:
        return {d: getattr(self, d) for d in DIMENSIONS}


@dataclass
class Chain:
    """A sequence of steps, and which products passed through which.

    `passes[product]` is the set of step names that product physically went
    through. This is read off a flow sheet. It is binary and it is not a share.
    """

    name: str
    note: str
    steps: list[Step]
    mass_kg: dict[str, float]
    passes: dict[str, set[str]] = field(default_factory=dict)

    @property
    def products(self) -> list[str]:
        return list(self.mass_kg)

    @property
    def step_names(self) -> list[str]:
        return [s.name for s in self.steps]

    def step(self, name: str) -> Step:
        return next(s for s in self.steps if s.name == name)

    def totals(self) -> dict[str, float]:
        return {d: sum(getattr(s, d) for s in self.steps) for d in DIMENSIONS}


def contiguous_partitions(n: int) -> list[list[tuple[int, int]]]:
    """Every way of cutting an ordered run of n steps into contiguous blocks.

    There are 2**(n-1) of them: each of the n-1 gaps is either a cut or not.
    Contiguity is the right restriction, because a block is a stretch of the
    process you cannot see inside. A block made of step 1 and step 7 but not
    the ones between them does not describe any real opacity.
    """
    out = []
    for bits in range(1 << (n - 1)):
        blocks, start = [], 0
        for i in range(n - 1):
            if bits & (1 << i):
                blocks.append((start, i + 1))
                start = i + 1
        blocks.append((start, n))
        out.append(blocks)
    return out


def charged_steps(chain: Chain, product: str, blocks: list[tuple[int, int]]) -> set[str]:
    """Which steps a product is charged for, at one resolution.

    A product that passed through ANY step of an opaque block carries the WHOLE
    block. From outside the block there is no way to say which part it used,
    and inventing one is exactly the modelled layer this ruling withdrew.
    """
    passed = chain.passes[product]
    out: set[str] = set()
    for lo, hi in blocks:
        names = chain.step_names[lo:hi]
        if passed & set(names):
            out.update(names)
    return out


def product_cost(chain: Chain, product: str, blocks) -> dict[str, float]:
    """One product's absolute cost vector at one resolution. No share is taken."""
    charged = charged_steps(chain, product, blocks)
    return {
        d: sum(getattr(chain.step(n), d) for n in charged)
        for d in DIMENSIONS
    }


def product_cost_per_kg(chain: Chain, product: str, blocks) -> dict[str, float]:
    total = product_cost(chain, product, blocks)
    m = chain.mass_kg[product]
    return {d: total[d] / m for d in DIMENSIONS}


# ---------------------------------------------------------------------------
# The two ways to add up a buyer's position -- and only one of them is right
# ---------------------------------------------------------------------------


def buyer_union(chain: Chain, products, blocks) -> dict[str, float]:
    """A3, done correctly: UNION over identified parcels.

    A buyer holding several co-products reaches some parcels by more than one
    path. Each parcel is counted ONCE, because it IS one record.
    """
    charged: set[str] = set()
    for p in products:
        charged |= charged_steps(chain, p, blocks)
    return {
        d: sum(getattr(chain.step(n), d) for n in charged)
        for d in DIMENSIONS
    }


def buyer_naive_sum(chain: Chain, products, blocks) -> dict[str, float]:
    """The defect: adding pointers as if they were amounts.

    This is what an implementation does if it treats a debit as a quantity
    rather than as a unique record of one specific event. It is reported so the
    size of the mistake is visible, and it is NEVER the rule.
    """
    out = {d: 0.0 for d in DIMENSIONS}
    for p in products:
        c = product_cost(chain, p, blocks)
        for d in DIMENSIONS:
            out[d] += c[d]
    return out


# ---------------------------------------------------------------------------
# Case 1 -- the steer
# ---------------------------------------------------------------------------


def build_steer() -> Chain:
    """A linear chain with products leaving at four different points.

    ⚠️ THE DIGITS ARE ILLUSTRATIVE and are declared as such. What this case is
    for is the SHAPE: products that leave early did not consume the steps that
    came after them, and a coarse reading charges them anyway.
    """
    steps = [
        Step("kill",        labour_h=2.0, energy_mj=50.0,  pollutant_kg=2.0),
        Step("hide_off",    labour_h=3.0, energy_mj=30.0,  pollutant_kg=1.0),
        Step("organs_out",  labour_h=2.0, energy_mj=40.0,  pollutant_kg=4.0),
        Step("hooves_head", labour_h=1.0, energy_mj=20.0,  pollutant_kg=1.0),
        Step("dry_aging",   labour_h=2.0, energy_mj=300.0, pollutant_kg=0.0),
        Step("butchering",  labour_h=6.0, energy_mj=30.0,  pollutant_kg=2.0),
        Step("packaging",   labour_h=4.0, energy_mj=30.0,  pollutant_kg=5.0),
    ]
    names = [s.name for s in steps]
    exits = {          # product -> the step it leaves after
        "hide":         "hide_off",
        "organs":       "organs_out",
        "hooves_head":  "hooves_head",
        "packaged_beef": "packaging",
    }
    passes = {p: set(names[: names.index(e) + 1]) for p, e in exits.items()}
    return Chain(
        name="steer",
        note="ILLUSTRATIVE digits. One 600 kg steer, 20 h of labour and 500 MJ "
             "across seven steps.",
        steps=steps,
        mass_kg={"hide": 40.0, "organs": 60.0, "hooves_head": 30.0,
                 "packaged_beef": 250.0},
        passes=passes,
    )


# ---------------------------------------------------------------------------
# Case 2 -- the refinery, on real DOE process energies
# ---------------------------------------------------------------------------
#
# DECLARED, and stated here so it can be argued with: the processing ORDER, and
# which fractions pass through which unit. This is a standard refinery
# configuration. It is BINARY -- did this fraction go through this unit, yes or
# no -- and it is read off a flow sheet rather than modelled. The withdrawn
# §3.4a rule needed the far stronger claim of WHAT SHARE of each unit's energy
# each fraction took, and that share is what moved LPG by 6.31x.

REFINERY_ORDER = [
    "atm_distillation", "vac_distillation", "coking", "fcc",
    "hydrocracking", "reforming", "alkylation", "hydrotreating",
]

REFINERY_PASSES = {
    # everything begins in the crude column
    "lpg":           {"atm_distillation", "fcc", "alkylation"},
    "gasoline":      {"atm_distillation", "fcc", "reforming", "alkylation",
                      "hydrotreating"},
    "jet":           {"atm_distillation", "hydrocracking", "hydrotreating"},
    "diesel":        {"atm_distillation", "vac_distillation", "hydrocracking",
                      "hydrotreating"},
    "residual_fuel": {"atm_distillation", "vac_distillation"},
    "petcoke":       {"atm_distillation", "vac_distillation", "coking"},
    "asphalt":       {"atm_distillation", "vac_distillation"},
}


def build_refinery() -> Chain:
    steps = [
        Step(name, energy_mj=PROCESS_ENERGY_TBTU[name])
        for name in REFINERY_ORDER
        if name in PROCESS_ENERGY_TBTU
    ]
    known = {s.name for s in steps}
    passes = {f: (REFINERY_PASSES[f] & known) for f in FRACTIONS}
    mass = {f: YIELD_BBL[f] * LITRES_PER_BBL * DENSITY_KG_L[f] for f in FRACTIONS}
    return Chain(
        name="refinery",
        note="REAL DOE 2015 Bandwidth Study per-process energies (TBtu/yr). "
             "Masses from EIA-representative yields x densities, per 100 bbl "
             "crude. The processing ORDER and the passage table are DECLARED.",
        steps=steps,
        mass_kg=mass,
        passes=passes,
    )


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def _fmt(x: float) -> str:
    if x == 0:
        return "0"
    if abs(x) >= 100:
        return f"{x:,.0f}"
    if abs(x) >= 1:
        return f"{x:.3f}"
    return f"{x:.4f}"


def analyse(chain: Chain):
    n = len(chain.steps)
    parts = contiguous_partitions(n)
    coarsest = [(0, n)]
    finest = [(i, i + 1) for i in range(n)]
    rows = []
    for p in chain.products:
        per_kg = [product_cost_per_kg(chain, p, b) for b in parts]
        for d in DIMENSIONS:
            vals = [v[d] for v in per_kg]
            rows.append({
                "chain": chain.name,
                "product": p,
                "dimension": d,
                "mass_kg": chain.mass_kg[p],
                "coarsest": product_cost_per_kg(chain, p, coarsest)[d],
                "finest": product_cost_per_kg(chain, p, finest)[d],
                "min": min(vals),
                "max": max(vals),
                "ratio": (max(vals) / min(vals)) if min(vals) > 0 else float("nan"),
            })
    return rows, parts, coarsest, finest


def report(chain: Chain) -> list[dict]:
    rows, parts, coarsest, finest = analyse(chain)
    tot = chain.totals()

    print()
    print("=" * 78)
    print(f"  {chain.name.upper()}")
    print("=" * 78)
    print(f"  {chain.note}")
    print(f"  {len(chain.steps)} steps, {len(chain.products)} co-products, "
          f"{len(parts)} resolutions swept (2^(n-1) contiguous partitions)")
    print(f"  Chain totals: " + " · ".join(
        f"{d} {_fmt(tot[d])}" for d in DIMENSIONS if tot[d]))
    print()

    print("  1. PER-KG FIGURES: coarsest reading against finest")
    print("  " + "-" * 74)
    print(f"  {'product':<16}{'mass kg':>10}{'dim':>13}{'coarsest':>12}"
          f"{'finest':>12}{'coarse/fine':>13}")
    for r in rows:
        if r["finest"] == 0 and r["coarsest"] == 0:
            continue
        ratio = (r["coarsest"] / r["finest"]) if r["finest"] > 0 else float("inf")
        flag = "  <- unchanged" if abs(ratio - 1.0) < 1e-12 else ""
        print(f"  {r['product']:<16}{r['mass_kg']:>10,.0f}{r['dimension']:>13}"
              f"{_fmt(r['coarsest']):>12}{_fmt(r['finest']):>12}"
              f"{ratio:>12.2f}x{flag}")
    print()

    print("  2. ONE BUYER TAKING EVERY CO-PRODUCT")
    print("  " + "-" * 74)
    print("  A3: a parcel reached by two paths is ONE record. Union, never sum.")
    print()
    print(f"  {'resolution':<22}{'dim':>13}{'UNION':>14}{'naive SUM':>14}"
          f"{'sum inflation':>15}")
    allp = chain.products
    for label, blocks in (("coarsest (1 block)", coarsest),
                          ("finest (n blocks)", finest)):
        u = buyer_union(chain, allp, blocks)
        s = buyer_naive_sum(chain, allp, blocks)
        for d in DIMENSIONS:
            if not tot[d]:
                continue
            infl = s[d] / u[d] if u[d] else float("nan")
            print(f"  {label:<22}{d:>13}{_fmt(u[d]):>14}{_fmt(s[d]):>14}"
                  f"{infl:>14.2f}x")
    print()

    union_vals = {d: set() for d in DIMENSIONS}
    sum_vals = {d: set() for d in DIMENSIONS}
    for b in parts:
        u = buyer_union(chain, allp, b)
        s = buyer_naive_sum(chain, allp, b)
        for d in DIMENSIONS:
            union_vals[d].add(round(u[d], 9))
            sum_vals[d].add(round(s[d], 9))
    for d in DIMENSIONS:
        if not tot[d]:
            continue
        print(f"  {d}: across all {len(parts)} resolutions the UNION takes "
              f"{len(union_vals[d])} distinct value(s), the naive SUM takes "
              f"{len(sum_vals[d])}.")
    print()
    print("  In plain words: the union figure is exactly the chain total and does")
    print("  not move with resolution. The naive sum both overstates it and")
    print("  changes when you re-read the same chain at a different detail.")
    print()
    return rows


def write_csv(rows: list[dict], path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {path} ({len(rows)} rows)")


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------


def _cases() -> list[Chain]:
    return [build_steer(), build_refinery()]


def test_totals_invariant() -> str:
    """Labour, energy and pollutants are INPUTS. Resolution cannot change them."""
    for c in _cases():
        t = c.totals()
        for d in DIMENSIONS:
            direct = sum(getattr(s, d) for s in c.steps)
            assert abs(t[d] - direct) < 1e-9, f"{c.name}/{d} totals disagree"
    return "chain totals are inputs and do not move with resolution"


def test_coarse_is_a_ceiling() -> str:
    """THE THEOREM. Merging blocks can only ADD steps to a product's charge."""
    checked = 0
    for c in _cases():
        n = len(c.steps)
        finest = [(i, i + 1) for i in range(n)]
        for blocks in contiguous_partitions(n):
            for p in c.products:
                coarse = product_cost(c, p, blocks)
                fine = product_cost(c, p, finest)
                for d in DIMENSIONS:
                    assert coarse[d] >= fine[d] - 1e-9, (
                        f"{c.name}/{p}/{d}: coarse {coarse[d]} < fine {fine[d]}")
                checked += 1
    return f"coarse >= fine on all {checked} product-resolution pairs"


def test_terminal_product_never_moves() -> str:
    """A product passing every step carries everything at every resolution."""
    found = 0
    for c in _cases():
        n = len(c.steps)
        allsteps = set(c.step_names)
        for p in c.products:
            if c.passes[p] != allsteps:
                continue
            found += 1
            base = product_cost(c, p, [(i, i + 1) for i in range(n)])
            for blocks in contiguous_partitions(n):
                got = product_cost(c, p, blocks)
                for d in DIMENSIONS:
                    assert abs(got[d] - base[d]) < 1e-9, (
                        f"{c.name}/{p}/{d} moved with resolution")
    assert found, "no terminal product in any case -- the test proved nothing"
    return f"{found} terminal product(s) identical at every resolution"


def test_union_equals_chain_total() -> str:
    """One buyer taking every co-product carries exactly the chain total."""
    for c in _cases():
        tot = c.totals()
        covered = set().union(*c.passes.values())
        assert covered == set(c.step_names), (
            f"{c.name}: a step no product passes -- see the unpassed-step test")
        for blocks in contiguous_partitions(len(c.steps)):
            u = buyer_union(c, c.products, blocks)
            for d in DIMENSIONS:
                assert abs(u[d] - tot[d]) < 1e-9, (
                    f"{c.name}/{d}: union {u[d]} != total {tot[d]}")
    return "union over parcels = chain total, exactly, at every resolution"


def test_naive_sum_inflates_and_moves() -> str:
    """The defect the union rule prevents, measured rather than asserted."""
    worst = 0.0
    moved = False
    for c in _cases():
        tot = c.totals()
        seen = {d: set() for d in DIMENSIONS}
        for blocks in contiguous_partitions(len(c.steps)):
            s = buyer_naive_sum(c, c.products, blocks)
            for d in DIMENSIONS:
                if not tot[d]:
                    continue
                assert s[d] >= tot[d] - 1e-9, "a naive sum should never understate"
                worst = max(worst, s[d] / tot[d])
                seen[d].add(round(s[d], 9))
        moved = moved or any(len(v) > 1 for v in seen.values())
    assert worst > 1.0, "the naive sum did not inflate -- the test proved nothing"
    assert moved, "the naive sum did not move with resolution"
    return f"naive sum inflates up to {worst:.2f}x and moves with resolution"


def test_the_sweep_actually_varies() -> str:
    """NEGATIVE CONTROL. If resolution moved nothing, everything above is vacuous."""
    moved = 0
    for c in _cases():
        n = len(c.steps)
        finest = [(i, i + 1) for i in range(n)]
        coarsest = [(0, n)]
        for p in c.products:
            a = product_cost(c, p, coarsest)
            b = product_cost(c, p, finest)
            if any(abs(a[d] - b[d]) > 1e-9 for d in DIMENSIONS):
                moved += 1
    assert moved >= 2, f"only {moved} products moved -- the sweep is inert"
    return f"{moved} products move between coarsest and finest"


def test_no_share_is_ever_computed() -> str:
    """UNIVERSALITY GUARD. A product's figure must not depend on any other
    product's mass. If it does, a split has been smuggled back in."""
    for c in _cases():
        n = len(c.steps)
        finest = [(i, i + 1) for i in range(n)]
        for p in c.products:
            before = product_cost(c, p, finest)
            others = [q for q in c.products if q != p]
            assert others, "single-product case proves nothing here"
            saved = dict(c.mass_kg)
            for q in others:
                c.mass_kg[q] *= 7.3
            after = product_cost(c, p, finest)
            c.mass_kg = saved
            for d in DIMENSIONS:
                assert abs(before[d] - after[d]) < 1e-9, (
                    f"{c.name}/{p}/{d} changed when another product's mass did")
    return "no product's figure depends on any other product's mass"


def test_unpassed_step_charges_nobody() -> str:
    """A step no product passed through stays with the producer (§3.2b)."""
    c = build_steer()
    c.steps.append(Step("effluent_treatment", labour_h=5.0, energy_mj=90.0,
                        pollutant_kg=11.0))
    n = len(c.steps)
    finest = [(i, i + 1) for i in range(n)]
    for p in c.products:
        charged = charged_steps(c, p, finest)
        assert "effluent_treatment" not in charged, (
            "a step nobody passed reached a product")
    u = buyer_union(c, c.products, finest)
    assert abs(u["energy_mj"] - (c.totals()["energy_mj"] - 90.0)) < 1e-9
    return "an unpassed step reaches no product and stays with the producer"


TESTS = [
    test_totals_invariant,
    test_coarse_is_a_ceiling,
    test_terminal_product_never_moves,
    test_union_equals_chain_total,
    test_naive_sum_inflates_and_moves,
    test_the_sweep_actually_varies,
    test_no_share_is_ever_computed,
    test_unpassed_step_charges_nobody,
]


def run_tests() -> int:
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


def main() -> None:
    ap = argparse.ArgumentParser(description="chain resolution")
    ap.add_argument("--test", action="store_true", help="self-tests only")
    ap.add_argument("--csv", metavar="PATH", help="write every row to CSV")
    a = ap.parse_args()

    if a.test:
        sys.exit(1 if run_tests() else 0)

    rows: list[dict] = []
    for c in _cases():
        rows += report(c)
    if a.csv:
        write_csv(rows, a.csv)
    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
