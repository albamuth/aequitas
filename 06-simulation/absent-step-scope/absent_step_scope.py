"""
Absent-step scope -- on a flow sheet, an absent step is either ENUMERATED-AND-ABSENT
(the plant looked and recorded "not passed") or NEVER-LOOKED-AT (no record at all).
Foundations 3.4a's passage claim is binary and carries no scope line, so a reader
sees both as the same blank. How often is each, and what does confusing them cost
in debit-hours per kg?

REQUEST sr-20260910-over-a-real-multi-step-process-flow-sheet-ho
(hemei, c50095, obj-20260910-hemei-expected-actual-passage-row).

MODEL. Extends ../chain-resolution/ (steer, DOE refinery). For every (product,
step) cell the TRUTH T is passed or not passed. The plant's sheet gives each cell
one of three records:
    1  = enumerated, passed          0  = enumerated, NOT passed (E)
    None = never looked at (N)       -- no record; reads as absent
The published passage claim is the set of cells with record 1. Absent = 0 or None.

THREE READERS, each turns the sheet into a charged-step set per product:
    TRUST    absent means not passed      (charges the cells recorded 1)
    CEILING  absent means maybe passed    (charges every step: the coarse reading)
    SCOPED   a reader who HAS a scope line: 0 means not passed, None is charged
             (3.4a's "errs against the producer" direction)
TRUST and CEILING are the two things a reader with no scope line can do.

THREE WAYS A SHEET CAN BE INCOMPLETE (which cells are never looked at):
    iid    each cell is enumerated with probability q
    tail   the sheet lists steps only up to the product's last passed step
    adv    the producer leaves out the k dearest passed steps, lists the rest

DECLARED BEFORE THE FIRST RUN (also in RESULTS.md):
  L1 (level)  Steer, hide, MJ/kg: the coarse reading is 6.25x the fine reading
              (12.50 vs 2.00). In collapsed debit-hours per kg the same gap is
              between 3.5x and 4.5x, NOT 6.25x, because labour and pollutant
              dimensions dilute the energy gap.
  L2 (level)  In 3.4a's two cases at least 40% of all (product, step) cells are
              absent from the true passage table.
  L3 (level)  Under iid incompleteness at q = 0.5, the mean over products of the
              TRUST reader's |error| lies between 15% and 60% of the true
              debit-hours per kg, on each chain.
  L4 (level)  Under iid incompleteness, the share of never-looked-at cells that
              hide a real passage equals K/M (passed cells over all cells), within
              0.02, on each chain.
  C1 (change) At q = 0.5 iid, the SCOPED reader's mean |error| is below the TRUST
              reader's, on each chain. Fails if not. (SCOPED <= CEILING is true by
              construction -- a subset of steps -- so it is NOT declared.)
  C2 (change) Under the producer-chosen omission 'adv', TRUST understates every
              product it hits and SCOPED understates none. Fails otherwise.

Run:  python absent_step_scope.py            # everything, then self-tests
      python absent_step_scope.py --test     # self-tests only
Seed: 20261028 (fixed in code; --seed to change)
"""

from __future__ import annotations

import argparse
import os
import random
import statistics as st
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_SIM = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_SIM, "chain-resolution"))

from chain_resolution import (  # noqa: E402
    DIMENSIONS, Chain, build_steer, build_refinery, product_cost,
)

SEED = 20261028
DRAWS = 2000
QS = (0.0, 0.25, 0.5, 0.75, 0.9, 1.0)

# ILLUSTRATIVE collapse weights, the same ones ../false-passage/ uses.
# Steer: hours + 0.05 h/kg pollutant + 0.002 h/MJ. The 0.002 is NOT sourced.
W_STEER = {"labour_h": 1.0, "pollutant_kg": 0.05, "energy_mj": 0.002}
# Refinery has energy only, in the DOE's native TBtu/yr against masses per 100 bbl.
# Those two scales do not match, so refinery figures are native units per kg and
# only RATIOS between readers are meaningful. It is never converted to hours.
W_REF = {"labour_h": 0.0, "pollutant_kg": 0.0, "energy_mj": 1.0}


def hours(c: Chain, steps: set[str], w: dict) -> float:
    return sum(getattr(c.step(n), d) * w[d] for n in steps for d in DIMENSIONS)


def per_kg(c: Chain, p: str, steps: set[str], w: dict) -> float:
    return hours(c, steps, w) / c.mass_kg[p]


def last_passed_index(c: Chain, p: str) -> int:
    names = c.step_names
    return max(names.index(s) for s in c.passes[p])


# ---------------------------------------------------------------------------
# Sheets: record[p][s] in {1, 0, None}
# ---------------------------------------------------------------------------

def sheet_iid(c: Chain, q: float, rng: random.Random) -> dict:
    return {p: {s: ((1 if s in c.passes[p] else 0) if rng.random() < q else None)
                for s in c.step_names} for p in c.products}


def sheet_tail(c: Chain) -> dict:
    out = {}
    for p in c.products:
        e = last_passed_index(c, p)
        out[p] = {s: ((1 if s in c.passes[p] else 0) if i <= e else None)
                  for i, s in enumerate(c.step_names)}
    return out


def sheet_adv(c: Chain, k: int, w: dict) -> dict:
    """Producer lists everything truthfully except the k dearest passed steps."""
    out = {}
    for p in c.products:
        passed = sorted(c.passes[p], key=lambda s: -hours(c, {s}, w))
        hide = set(passed[:k])
        out[p] = {s: (None if s in hide else (1 if s in c.passes[p] else 0))
                  for s in c.step_names}
    return out


# ---------------------------------------------------------------------------
# Readers
# ---------------------------------------------------------------------------

def read(c: Chain, rec: dict, p: str, reader: str) -> set[str]:
    row = rec[p]
    if reader == "trust":
        return {s for s, v in row.items() if v == 1}
    if reader == "ceiling":
        return set(c.step_names)
    if reader == "scoped":
        return {s for s, v in row.items() if v is None or v == 1}
    raise ValueError(reader)


READERS = ("trust", "ceiling", "scoped")


def errors(c: Chain, rec: dict, w: dict) -> dict:
    """reader -> {product: (signed abs error per kg, truth per kg)}"""
    out = {r: {} for r in READERS}
    for p in c.products:
        truth = per_kg(c, p, c.passes[p], w)
        for r in READERS:
            out[r][p] = (per_kg(c, p, read(c, rec, p, r), w) - truth, truth)
    return out


def mean_abs_rel(e: dict) -> float:
    return st.mean(abs(d) / t for d, t in e.values() if t > 0)


def max_abs_rel(e: dict) -> float:
    return max(abs(d) / t for d, t in e.values() if t > 0)


def mean_abs(e: dict) -> float:
    return st.mean(abs(d) for d, _ in e.values())


# ---------------------------------------------------------------------------
# Measurements
# ---------------------------------------------------------------------------

def cell_counts(c: Chain) -> tuple[int, int]:
    m = len(c.products) * len(c.steps)
    k = sum(len(c.passes[p] & set(c.step_names)) for p in c.products)
    return m, k


def iid_sweep(c: Chain, w: dict, rng: random.Random, draws: int = DRAWS) -> list[dict]:
    m, k = cell_counts(c)
    rows = []
    for q in QS:
        acc = {r: [] for r in READERS}
        accabs = {r: [] for r in READERS}
        n_absent = n_never = n_hidden = 0   # pooled over every sheet, not a mean of ratios
        under = {r: 0 for r in READERS}
        over = {r: 0 for r in READERS}
        cells = 0
        for _ in range(draws):
            rec = sheet_iid(c, q, rng)
            e = errors(c, rec, w)
            for r in READERS:
                acc[r].append(mean_abs_rel(e[r]))
                accabs[r].append(mean_abs(e[r]))
                for d, _ in e[r].values():
                    under[r] += d < -1e-12
                    over[r] += d > 1e-12
            cells += len(c.products)
            absent = [(p, s) for p in c.products for s, v in rec[p].items() if v != 1]
            nev = [(p, s) for p, s in absent if rec[p][s] is None]
            n_absent += len(absent)
            n_never += len(nev)
            n_hidden += sum(s in c.passes[p] for p, s in nev)
        rows.append({"q": q, "m": m, "k": k,
                     "rel": {r: (st.mean(acc[r]), st.pstdev(acc[r]),
                                 sorted(acc[r])[int(0.05 * draws)],
                                 sorted(acc[r])[int(0.95 * draws) - 1]) for r in READERS},
                     "abs": {r: (st.mean(accabs[r]), st.pstdev(accabs[r])) for r in READERS},
                     "n_share": n_never / n_absent if n_absent else float("nan"),
                     "hidden": n_hidden / n_never if n_never else float("nan"),
                     "under": {r: under[r] / cells for r in READERS},
                     "over": {r: over[r] / cells for r in READERS}})
    return rows


def structural(c: Chain, w: dict) -> dict:
    rec = sheet_tail(c)
    e = errors(c, rec, w)
    return {r: (mean_abs_rel(e[r]), max_abs_rel(e[r]), mean_abs(e[r])) for r in READERS}


def adversarial(c: Chain, w: dict, k: int) -> dict:
    rec = sheet_adv(c, k, w)
    e = errors(c, rec, w)
    hit = [p for p in c.products if len(c.passes[p]) >= 1]
    return {"e": e, "n_hit": len(hit)}


# ---------------------------------------------------------------------------
# Printing
# ---------------------------------------------------------------------------

def fmt_abs(x: float, ref: bool) -> str:
    return f"{x:.3e}" if ref else f"{x:.4f}"


def run(seed: int) -> dict:
    rng = random.Random(seed)
    cases = [("steer (illustrative digits)", build_steer(), W_STEER, False),
             ("refinery (real DOE energies)", build_refinery(), W_REF, True)]
    out: dict = {}
    for name, c, w, ref in cases:
        unit = "native units/kg" if ref else "h/kg"
        m, k = cell_counts(c)
        print("=" * 84)
        print(f"{name.upper()}   {len(c.products)} products x {len(c.steps)} steps = {m} cells, "
              f"{k} passed, {m - k} absent ({(m - k) / m:.0%})")
        print("=" * 84)
        out[name] = {"m": m, "k": k}

        # truth table
        print("  True figure per product (" + unit + "), coarse reading, coarse/true:")
        for p in c.products:
            t = per_kg(c, p, c.passes[p], w)
            co = per_kg(c, p, set(c.step_names), w)
            print(f"    {p:<15}{fmt_abs(t, ref):>13}{fmt_abs(co, ref):>13}{co / t:>8.2f}x")
        if not ref:
            for lab, ww in (("energy only", {"labour_h": 0, "pollutant_kg": 0, "energy_mj": 1.0}),
                            ("collapsed hours", w)):
                t = per_kg(c, "hide", c.passes["hide"], ww)
                co = per_kg(c, "hide", set(c.step_names), ww)
                print(f"  HIDE, {lab}: true {t:.4f}, coarse {co:.4f}, coarse/true {co / t:.3f}x")
                out["hide_" + lab] = (t, co, co / t)

        # iid sweep
        print(f"\n  IID: each cell enumerated with probability q ({DRAWS} sheets per q)")
        print(f"  {'q':>5}{'N share of absent':>19}{'N cells hiding a pass':>23}"
              f"{'TRUST err %':>16}{'CEILING err %':>16}{'SCOPED err %':>16}")
        rows = iid_sweep(c, w, rng)
        out[name]["iid"] = rows
        for r in rows:
            print(f"  {r['q']:>5.2f}{r['n_share']:>19.3f}{r['hidden']:>23.3f}"
                  + "".join(f"{100 * r['rel'][x][0]:>10.1f}±{100 * r['rel'][x][1]:<5.1f}"
                            for x in READERS))
        mid = next(r for r in rows if r["q"] == 0.5)
        print(f"\n  q = 0.5, mean |error| in absolute " + unit + ", with 5th-95th percentile of the % error:")
        for x in READERS:
            print(f"    {x:<8}{fmt_abs(mid['abs'][x][0], ref):>14}  ±{fmt_abs(mid['abs'][x][1], ref)}"
                  f"   % range {100 * mid['rel'][x][2]:.1f} to {100 * mid['rel'][x][3]:.1f}"
                  f"   understates {mid['under'][x]:.0%} / overstates {mid['over'][x]:.0%} of product-sheets")

        # tail
        s = structural(c, w)
        out[name]["tail"] = s
        print("\n  TAIL: sheet lists steps only up to each product's last passed step")
        for x in READERS:
            print(f"    {x:<8}mean |err| {100 * s[x][0]:6.1f}%   worst product {100 * s[x][1]:7.1f}%"
                  f"   mean abs {fmt_abs(s[x][2], ref)} {unit}")

        # adversarial
        print("\n  ADV: producer leaves the k dearest PASSED steps off the sheet")
        out[name]["adv"] = {}
        for kk in (1, 2):
            a = adversarial(c, w, kk)
            e = a["e"]
            tr_under = sum(d < -1e-12 for d, _ in e["trust"].values())
            tr_n = len(e["trust"])
            sc_under = sum(d < -1e-12 for d, _ in e["scoped"].values())
            worst = max(abs(d) / t for d, t in e["trust"].values())
            print(f"    k={kk}: TRUST understates {tr_under}/{tr_n} products, worst "
                  f"{100 * worst:.0f}% of true; SCOPED understates {sc_under}/{tr_n}; "
                  f"SCOPED mean |err| {100 * mean_abs_rel(e['scoped']):.0f}%")
            out[name]["adv"][kk] = (tr_under, tr_n, worst, sc_under)
        print()
    return out


# ---------------------------------------------------------------------------
# Self-tests -- each one can fail
# ---------------------------------------------------------------------------

def _cases():
    return [(build_steer(), W_STEER), (build_refinery(), W_REF)]


def test_full_enumeration_is_exact() -> str:
    """q = 1: TRUST and SCOPED must be exact; CEILING must NOT be (else vacuous)."""
    rng = random.Random(11)
    for c, w in _cases():
        e = errors(c, sheet_iid(c, 1.0, rng), w)
        for x in ("trust", "scoped"):
            assert all(abs(d) < 1e-12 for d, _ in e[x].values()), f"{c.name}/{x} not exact at q=1"
        assert any(abs(d) > 1e-9 for d, _ in e["ceiling"].values()), "ceiling is exact: sweep inert"
    return "q=1: TRUST and SCOPED exact, CEILING still wrong"


def test_nothing_enumerated() -> str:
    """q = 0: TRUST charges nothing (100% understated); SCOPED equals CEILING."""
    rng = random.Random(12)
    for c, w in _cases():
        rec = sheet_iid(c, 0.0, rng)
        e = errors(c, rec, w)
        for p in c.products:
            d, t = e["trust"][p]
            assert abs(d + t) < 1e-9, f"{c.name}/{p}: TRUST at q=0 did not read zero"
            assert abs(e["scoped"][p][0] - e["ceiling"][p][0]) < 1e-9
    return "q=0: TRUST reads zero, SCOPED collapses onto the coarse reading"


def test_signs() -> str:
    """TRUST never overstates; SCOPED never understates. Random sheets."""
    rng = random.Random(13)
    for c, w in _cases():
        for _ in range(300):
            e = errors(c, sheet_iid(c, rng.random(), rng), w)
            assert all(d <= 1e-12 for d, _ in e["trust"].values()), "TRUST overstated"
            assert all(d >= -1e-12 for d, _ in e["scoped"].values()), "SCOPED understated"
    return "TRUST only understates, SCOPED only overstates, over 600 random sheets"


def test_ceiling_matches_independent_module() -> str:
    """CEILING must equal chain_resolution's coarsest reading, computed another way."""
    for c, w in _cases():
        blocks = [(0, len(c.steps))]
        for p in c.products:
            ours = per_kg(c, p, read(c, sheet_tail(c), p, "ceiling"), w)
            vec = product_cost(c, p, blocks)
            theirs = sum(vec[d] * w[d] for d in DIMENSIONS) / c.mass_kg[p]
            assert abs(ours - theirs) < 1e-9 * max(1.0, abs(theirs)), f"{c.name}/{p}"
    return "CEILING equals chain_resolution's coarsest block, per product, both chains"


def test_steer_hide_is_6_25() -> str:
    """The request's 6.25x, recomputed. Fails if the digits or the rule drift."""
    c = build_steer()
    wE = {"labour_h": 0, "pollutant_kg": 0, "energy_mj": 1.0}
    r = per_kg(c, "hide", set(c.step_names), wE) / per_kg(c, "hide", c.passes["hide"], wE)
    assert abs(r - 6.25) < 1e-9, f"{r}"
    return f"steer hide energy coarse/fine = {r:.2f}x"


def test_iid_matches_analytic_share() -> str:
    """Measured N share of absent cells must match M(1-q) / (M(1-q) + q(M-K))."""
    rng = random.Random(14)
    for c, w in _cases():
        m, k = cell_counts(c)
        for q in (0.25, 0.5, 0.9):
            # 6000 draws: at q=0.9 the hidden-pass share has sd ~0.004, so 0.03 is ~8 sd
            row = next(r for r in iid_sweep(c, w, rng, draws=6000) if r["q"] == q)
            want = m * (1 - q) / (m * (1 - q) + q * (m - k))
            assert abs(row["n_share"] - want) < 0.03, f"{c.name} q={q}: {row['n_share']} vs {want}"
            assert abs(row["hidden"] - k / m) < 0.03, f"{c.name} q={q}: hidden {row['hidden']}"
    return "measured N share and hidden-pass share match the closed forms within 0.03"


def test_adversary_can_win_and_scope_stops_it() -> str:
    for c, w in _cases():
        a = adversarial(c, w, 1)["e"]
        assert any(d < -1e-12 for d, _ in a["trust"].values()), "adversary gained nothing"
        assert all(d >= -1e-12 for d, _ in a["scoped"].values()), "scope line let a lie through"
    return "dropping a dear passed step lowers TRUST's figure and never SCOPED's"


def test_catches_a_broken_reader() -> str:
    """Mutation check: if SCOPED ignored None cells it would equal TRUST. Prove the
    suite can tell them apart on a sheet with a hidden pass."""
    c, w = build_steer(), W_STEER
    rec = sheet_adv(c, 1, w)
    t = errors(c, rec, w)["trust"]
    s = errors(c, rec, w)["scoped"]
    assert any(abs(t[p][0] - s[p][0]) > 1e-9 for p in c.products), "TRUST == SCOPED: tests blind"
    return "TRUST and SCOPED differ on a hidden-pass sheet"


TESTS = [test_full_enumeration_is_exact, test_nothing_enumerated, test_signs,
         test_ceiling_matches_independent_module, test_steer_hide_is_6_25,
         test_iid_matches_analytic_share, test_adversary_can_win_and_scope_stops_it,
         test_catches_a_broken_reader]


def run_tests() -> int:
    print("SELF-TESTS\n" + "-" * 84)
    failed = 0
    for t in TESTS:
        try:
            print(f"  PASS  {t()}")
        except AssertionError as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print(f"  {len(TESTS) - failed}/{len(TESTS)} passed")
    return failed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--seed", type=int, default=SEED)
    a = ap.parse_args()
    if a.test:
        sys.exit(1 if run_tests() else 0)
    run(a.seed)
    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
