"""
EXIOBASE loader -- C3 / OP-3, real-data slice.

Feeds a real EEIO table (EXIOBASE, via `pymrio`) into the SAME forward solver the
synthetic pipeline uses, producing a per-commodity debit vector (one embodied
figure per physical stressor) for every sector-in-region.

Built against `pymrio.load_test()` -- pymrio's built-in multi-regional IO table,
which has the *real EXIOBASE structure and API* (a technical-coefficient matrix A
plus satellite/extension accounts) but is tiny and needs no multi-GB download.
Pointing this at a downloaded full EXIOBASE 3 is a one-call swap (see `load_real`
docstring); the mapping and solve code below do not change.

Why this reuses everything: a product-by-product IOT is square (industry k makes
product k), so in the make/use language of the synthetic engine it is the
degenerate case  B = I,  Theta = I.  Under that, the forward operator reduces to

        A~ = A^T,   p = (I - A^T)^{-1} s

which is exactly the standard Leontief total-intensity multiplier
`M = S (I - A)^{-1}`.  The self-test asserts our p equals pymrio's own `.M` to
machine precision -- i.e. the Aequitas engine reproduces accepted EEIO footprints
on real-structured data, then extends them (per-dimension vectors, OP-18 labour
rule) where joint production is explicit.

IMPORTANT HONESTY NOTE. The *test* MRIO carries only `factor_inputs` (Value
Added, money) and `emissions` (two stressors, kg). It does NOT carry the
employment-hours or energy extensions that real EXIOBASE has -- which are the
whole reason EXIOBASE was chosen (it uniquely reports embodied labour hours). So
this slice demonstrates the pipeline and the pymrio-equivalence on the kg
stressors that exist, and wires the labour/energy dimensions structurally; the
real *numbers* for labour and energy arrive only when full EXIOBASE is loaded.

Run:  python exiobase_loader.py            # load test MRIO, report + cross-check
      python exiobase_loader.py --test      # self-tests only
"""

from __future__ import annotations

import argparse
import os
import sys

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recursion_convergence import (  # noqa: E402
    Economy, build_forward, solve_direct, spectral_radius,
)
from estimation_engine import MultiDimEconomy  # noqa: E402

import pymrio  # noqa: E402


# ---------------------------------------------------------------------------
# Stressor -> debit-dimension mapping
# ---------------------------------------------------------------------------
#
# Each entry maps a debit dimension name to (extension_name, stressor_row_label)
# in the pymrio IOSystem. This is the ONE place that differs between the test
# MRIO and real EXIOBASE.
#
# The test MRIO exposes two kg emission stressors; we read them as two
# material/pollution dimensions (genuinely in kg, so genuinely material debit).

TEST_MRIO_DIMS = {
    "emis_air_kg":   ("emissions", ("emission_type1", "air")),
    "emis_water_kg": ("emissions", ("emission_type2", "water")),
}

# For real EXIOBASE 3 the extensions and stressor labels differ. Approximate map
# (verify exact labels against the downloaded system's `.get_extensions()` /
# `.<ext>.get_rows()` -- names vary by EXIOBASE version, so this is a template,
# not a hard-coded guarantee):
#
# REAL_EXIOBASE_DIMS = {
#     "labour_hours": ("employment", "Employment: Hours"),   # <- the hours EXIOBASE uniquely carries
#     "energy_TJ":    ("energy",     "Energy Carrier Net Total"),
#     "material_kg":  ("material",   "Domestic Extraction Used: Total"),
#     "co2_kg":       ("air_emissions", "CO2 - combustion - air"),
# }
#
# With that map and `load_real(...)`, everything below runs unchanged, and the
# OP-18 rule (labour rides the material split) becomes active wherever the table
# is a supply-use table with explicit joint production (Theta != I). A
# product-by-product IOT has already resolved joint production via an
# industry/commodity-technology *assumption* -- exactly the arbitrary carrier
# choice Aequitas replaces -- so the physical-split story only bites on SUTs.
# That deeper slice is flagged for follow-up, not attempted here.


# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------

def load_test():
    """pymrio's built-in test MRIO, fully calculated. Real structure, no download."""
    return pymrio.load_test().calc_all()


def load_real(storage_folder, year=None):
    """Load a downloaded full EXIOBASE 3 system. NOT called by default.

    Downloading EXIOBASE is a multi-GB, permission-gated step:
        import pymrio
        pymrio.download_exiobase3(storage_folder=<dir>, system='pxp', years=[2011])
        io = pymrio.parse_exiobase3(path=<the .zip or folder>)
        io.calc_all()
    Then feed `io` to `mrio_to_economy(io, REAL_EXIOBASE_DIMS)`. The rest is
    identical to the test path.
    """
    io = pymrio.parse_exiobase3(path=storage_folder)
    return io.calc_all()


# ---------------------------------------------------------------------------
# Adapt an MRIO into the forward-solver's economy
# ---------------------------------------------------------------------------

def mrio_to_economy(io, dims_map):
    """Wrap a calculated pymrio IOSystem as a MultiDimEconomy (B = Theta = I).

    Products/processes are the (region, sector) columns of A, in table order.
    `direct[dim]` is the sector's DIRECT stressor intensity per unit output
    (pymrio's `.S`), which plays the role of the synthetic engine's `l`.

    All Theta are the SAME identity object, so the OP-18 invariant
    (theta['labour'] is theta['materials']) holds trivially -- there is no joint
    production in an IOT to split.
    """
    A_df = io.A
    labels = list(A_df.columns)                 # [(region, sector), ...]
    n = len(labels)
    A = sp.csr_matrix(A_df.values.astype(float))    # A[i,j] = input i per unit output j
    ident = sp.identity(n, format="csr")

    direct, units = {}, {}
    for dim, (ename, key) in dims_map.items():
        ext = getattr(io, ename)
        s_row = ext.S.loc[key]                  # direct intensity per unit output
        direct[dim] = np.asarray(s_row.values, dtype=float)
        try:
            units[dim] = str(ext.unit.iloc[0, 0])
        except Exception:
            units[dim] = "?"

    products = [f"{r}/{s}" for (r, s) in labels]
    theta = {dim: ident for dim in direct}      # identity for every dimension
    prod_units = {p: "unit-output" for p in products}
    econ = MultiDimEconomy(products, products, A, ident, direct, theta, prod_units)
    econ_meta = dict(labels=labels, dim_units=units)
    return econ, econ_meta


def per_unit_debit(econ: MultiDimEconomy, dim: str):
    """Per-unit embodied debit of one dimension for every product (sector-region).

    Reuses build_forward/solve_direct directly -- the same operator proven in
    recursion_convergence.py. Returns (p, rho).
    """
    sub = Economy(econ.M, econ.N, econ.A, econ.B,
                  np.asarray(econ.direct[dim], float), econ.theta[dim])
    A_tilde, c = build_forward(sub)
    rho = spectral_radius(A_tilde)
    p = solve_direct(A_tilde, c)
    return p, rho


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(io=None):
    io = io or load_test()
    econ, meta = mrio_to_economy(io, TEST_MRIO_DIMS)
    dims = econ.dims()

    print("=" * 78)
    print("EXIOBASE LOADER -- real EEIO structure through the Aequitas solver")
    print("=" * 78)
    print(f"source        : pymrio test MRIO  ({len(set(r for r, _ in meta['labels']))} "
          f"regions x {len(set(s for _, s in meta['labels']))} sectors "
          f"= {econ.M} product-regions)")
    print(f"structure     : product-by-product IOT  ->  B = Theta = I "
          f"(no explicit joint production)")
    print(f"dimensions    : {[f'{d} [{meta['dim_units'][d]}]' for d in dims]}")

    vecs, rhos = {}, {}
    for d in dims:
        vecs[d], rhos[d] = per_unit_debit(econ, d)
    print(f"rho(A~)       : {rhos[dims[0]]:.4f}  (productive; same operator every dim)")

    # show one region's 8 sectors
    region = meta["labels"][0][0]
    rows = [(i, s) for i, (r, s) in enumerate(meta["labels"]) if r == region]
    print(f"\nper-unit embodied debit, region '{region}':")
    header = f"{'sector':<14}" + "".join(f"{d:>16}" for d in dims)
    print(header)
    print("-" * len(header))
    for i, s in rows:
        print(f"{s:<14}" + "".join(f"{vecs[d][i]:>16.5f}" for d in dims))
    print("-" * len(header))

    # cross-check against pymrio's own multipliers
    ok, worst = crosscheck(io, econ, TEST_MRIO_DIMS)
    print(f"\ncross-check vs pymrio .M multipliers: "
          f"{'PASS' if ok else 'FAIL'}  (max |gap| = {worst:.2e})")
    print("  -> the Aequitas forward solver reproduces standard EEIO footprints "
          "exactly.")
    print("\nNOTE: test MRIO lacks employment-hours & energy extensions. Real "
          "EXIOBASE\n      adds them via REAL_EXIOBASE_DIMS -- same loader, same "
          "solve; the\n      OP-18 labour rule activates on supply-use tables "
          "(Theta != I).")
    print("=" * 78)
    return vecs


def crosscheck(io, econ, dims_map):
    """Assert our per-unit debit equals pymrio's precomputed multipliers `.M`."""
    worst = 0.0
    for dim, (ename, key) in dims_map.items():
        p, _ = per_unit_debit(econ, dim)
        m_row = np.asarray(getattr(io, ename).M.loc[key].values, dtype=float)
        worst = max(worst, float(np.max(np.abs(p - m_row))))
    return worst < 1e-9, worst


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def test_reproduces_pymrio_multipliers():
    """The core validation: forward solve == pymrio .M to machine precision."""
    io = load_test()
    econ, _ = mrio_to_economy(io, TEST_MRIO_DIMS)
    ok, worst = crosscheck(io, econ, TEST_MRIO_DIMS)
    assert ok, f"forward solve should match pymrio multipliers, max gap {worst:.2e}"
    print(f"[ok] reproduces pymrio .M multipliers (max gap {worst:.2e})")


def test_nonnegative_and_productive():
    """Real EEIO table is productive (rho<1) and all embodied debit is >= 0."""
    io = load_test()
    econ, _ = mrio_to_economy(io, TEST_MRIO_DIMS)
    for d in econ.dims():
        p, rho = per_unit_debit(econ, d)
        assert rho < 1.0, f"{d}: non-productive rho={rho}"
        assert np.min(p) >= -1e-12, f"{d}: negative debit {np.min(p)}"
    print("[ok] productive (rho<1) and non-negative on real EEIO structure")


def test_identity_reduction():
    """B = Theta = I really does reduce the operator to A^T (the Leontief case)."""
    io = load_test()
    econ, _ = mrio_to_economy(io, TEST_MRIO_DIMS)
    d = econ.dims()[0]
    sub = Economy(econ.M, econ.N, econ.A, econ.B,
                  np.asarray(econ.direct[d], float), econ.theta[d])
    A_tilde, _ = build_forward(sub)
    gap = abs(A_tilde - econ.A.transpose().tocsr()).max()
    assert gap < 1e-12, f"A~ should equal A^T for an IOT, gap={gap}"
    print(f"[ok] identity reduction: A~ == A^T for product-by-product IOT "
          f"(gap {gap:.1e})")


def run_tests():
    test_reproduces_pymrio_multipliers()
    test_nonnegative_and_productive()
    test_identity_reduction()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true", help="run self-tests only")
    args = ap.parse_args()
    if args.test:
        run_tests()
        return 0
    print("Running self-tests first...\n")
    run_tests()
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
