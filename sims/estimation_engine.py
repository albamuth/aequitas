"""
Aequitas estimation engine -- C3 / OP-3, synthetic first deliverable.

Goal: produce a per-product *debit vector* (materials, energy, labour) for a
handful of goods, using the OP-17/§3.4a joint-production split and the OP-18
labour rule, on a small hand-built economy -- structured so a real EEIO table
(EXIOBASE) drops into exactly the same solver later.

What this demonstrates, end to end:

  1. Per-product debit vectors from a make/use/theta economy, one solve per
     physical dimension, reusing the proven forward operator from
     `recursion_convergence.py` (p = c + A~ p, A~ >= 0, non-negativity for free).

  2. The OP-18 labour rule -- "labour rides the process's own material split"
     (Foundations §3.4a, v0.6). Labour has no per-product physical trace, so it
     is NOT given its own theta; it reuses the material dimension's theta. The
     code makes this an identity, not a comment: Theta['labour'] IS
     Theta['materials'], and a test asserts the resulting A~ are bit-identical.

  3. Cost != scarcity (the load-bearing v0.6 sub-decision). A tenderloin (~1%
     yield) and hamburger (~5% yield) of equal tissue composition cost the SAME
     per kg in materials and labour -- because the material split is by mass, not
     yield or desirability. The rejected "Method 2" (yield/price weighting) is
     implemented alongside purely to show it is distinguishable and that it would
     price-ration the prized cut by who can absorb the larger debit (A5 breach).

  4. The residual cohort rule (N - Y) / Z (§5.1b) for unmeasured producers, with
     its adverse-selection property: the dark-producer estimate worsens as good
     producers instrument and leave the residual, so darkness stops paying.

  5. Split-before-collapse (§3.2a): energy has its own measured theta (lean vs
     fat differ in deposition energy), so materials and energy are genuinely
     separate linear systems -- you divide per dimension, then collapse. Only
     labour shares an operator with materials, by the OP-18 rule.

Run:  python estimation_engine.py            # build economy, print report
      python estimation_engine.py --test      # self-tests only
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field

import numpy as np
import scipy.sparse as sp

# reuse the validated forward solver rather than re-deriving it
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recursion_convergence import (  # noqa: E402
    Economy,
    build_forward,
    solve_direct,
    spectral_radius,
)


# ---------------------------------------------------------------------------
# A multi-dimension economy: one make/use structure, several physical resources
# ---------------------------------------------------------------------------

@dataclass
class MultiDimEconomy:
    """One make/use structure carrying several physical debit dimensions.

    products : list[str]           product names, index i = 0..M-1
    processes: list[str]           process names, index k = 0..N-1
    A        : (M x N) sparse      units of product i USED by process k per run
    B        : (M x N) sparse      units of product i MADE by process k per run
    direct   : dict[dim -> (N,)]   direct resource input of each process, per run
                                   e.g. direct['energy'][k] = MJ burned by k itself
    theta    : dict[dim -> (M x N) sparse]
                                   physical split fraction of process k's total
                                   dimension-`dim` debit assigned to co-product i.
                                   Each process column sums to 1 over its outputs.

    Invariant enforced at construction: theta['labour'] IS theta['materials']
    (the SAME object) -- the OP-18 rule. Labour never gets its own basis.
    """
    products: list
    processes: list
    A: sp.spmatrix
    B: sp.spmatrix
    direct: dict
    theta: dict
    units: dict = field(default_factory=dict)

    @property
    def M(self):
        return len(self.products)

    @property
    def N(self):
        return len(self.processes)

    def dims(self):
        return list(self.direct.keys())


# ---------------------------------------------------------------------------
# The core: solve one physical dimension through the forward operator
# ---------------------------------------------------------------------------

def solve_dimension(econ: MultiDimEconomy, dim: str):
    """Per-unit embodied debit of one dimension for every product.

    Wraps the process's make/use/theta into the `Economy` the proven
    `build_forward` expects, using this dimension's direct resource as `l` and
    this dimension's theta as the split. Returns (p, rho, A_tilde, c):

        p[i]   : per-unit embodied `dim` debit of product i (>= 0 for rho < 1)
        rho    : spectral radius of A~ (must be < 1 for a productive economy)

    Because A~ depends only on (A, B, theta) and NOT on the resource vector,
    two dimensions that share a theta share an A~ exactly -- which is precisely
    how the OP-18 labour rule is realised (labour reuses the material theta).
    """
    sub = Economy(
        M=econ.M, N=econ.N,
        A=econ.A, B=econ.B,
        l=np.asarray(econ.direct[dim], dtype=float),
        Theta=econ.theta[dim],
        meta=dict(kind="estimation", dim=dim),
    )
    A_tilde, c = build_forward(sub)
    rho = spectral_radius(A_tilde)
    if rho >= 1.0:
        raise ValueError(f"non-productive economy (rho={rho:.3f}) for dim={dim!r}")
    p = solve_direct(A_tilde, c)
    return p, rho, A_tilde, c


def debit_vectors(econ: MultiDimEconomy):
    """Full per-product debit vector: {dim -> p[dim]} for every dimension.

    This is the C3 deliverable in one object -- for each product, its embodied
    materials, energy, and labour, kept SEPARATE (never pre-collapsed, §3.2a).
    """
    return {dim: solve_dimension(econ, dim)[0] for dim in econ.dims()}


def collapse(vectors: dict, weights: dict):
    """Collapse a per-dimension debit vector to one comparable figure on demand.

    weights is the current weighting model (the OP-10 object -- whoever sets
    these moves every balance; kept explicit and external for exactly that
    reason). collapse(...) is only ever applied to COMPARE, never before a split.
    """
    dims = list(vectors.keys())
    total = np.zeros_like(next(iter(vectors.values())))
    for d in dims:
        total = total + weights[d] * vectors[d]
    return total


# ---------------------------------------------------------------------------
# The rejected Method 2 (yield / desirability weighting) -- for contrast only
# ---------------------------------------------------------------------------

def method2_yield_weighted(econ: MultiDimEconomy, process_idx: int,
                           desirability: dict):
    """Cost per unit of a joint process's co-products under the REJECTED rule.

    Method 2 weights each co-product's cost share by yield-scarcity or
    desirability instead of by the physical split. Implemented purely to show it
    is (a) computable and (b) different -- it inflates the rare, prized cut, which
    rations it by who can absorb the larger debit (price-rationing by standing,
    the A5/§7.1 mechanism Aequitas removes). See Foundations §3.4a (v0.6).

    Returns {product -> material cost per unit} for the co-products of one
    process, so it can be compared directly with the physical-split answer.
    """
    k = process_idx
    B = econ.B.tocsc()
    prods = B[:, k].nonzero()[0]
    made = np.asarray(B[prods, k].todense()).ravel()
    # total material pool routed to this process's outputs (direct only, for a
    # clean single-process contrast -- upstream embodied is identical either way)
    pool = econ.direct["materials"][k]
    w = np.array([desirability[econ.products[i]] for i in prods], dtype=float)
    w = w / w.sum()                       # desirability shares
    share = w * pool                      # Method-2 cost assigned to each output
    return {econ.products[i]: float(share[j] / made[j])
            for j, i in enumerate(prods)}


# ---------------------------------------------------------------------------
# Residual cohort estimation  (N - Y) / Z   (§5.1b)
# ---------------------------------------------------------------------------

def residual_estimate(N_total: float, measured_outputs, Z_unmeasured: int):
    """Per-producer estimate for the dark (unmeasured, non-participant) producers.

        estimate = (N - Y) / Z
            N : independently known total (FAO / trade / satellite)
            Y : sum of measured participants' recorded output
            Z : count of producers still outside Aequitas

    Averages cover only the UNMEASURED residual, never the whole population --
    that is what makes darkness stop paying (see `adverse_selection_demo`).
    """
    Y = float(np.sum(measured_outputs))
    if Z_unmeasured <= 0:
        return 0.0
    return max(0.0, (N_total - Y) / Z_unmeasured)


def adverse_selection_demo(N_total, true_outputs, join_order):
    """Show the residual estimate worsening as GOOD producers instrument.

    Starts with everyone dark; participants join one at a time in `join_order`
    (best producers first). Each step recomputes the dark-producer estimate over
    the shrinking residual. Because good producers leave the pool, the estimate
    for the remaining dark producers *falls* -- so a below-average producer who
    stays dark is increasingly under-credited by hiding. Returns a list of
    (n_joined, dark_count, per_dark_estimate).
    """
    true_outputs = list(true_outputs)
    joined = []
    trace = []
    # step 0: nobody measured
    trace.append((0, len(true_outputs),
                  residual_estimate(N_total, [], len(true_outputs))))
    for n, idx in enumerate(join_order, start=1):
        joined.append(true_outputs[idx])
        dark = len(true_outputs) - len(joined)
        est = residual_estimate(N_total, joined, dark)
        trace.append((n, dark, est))
    return trace


# ---------------------------------------------------------------------------
# The hand-built demonstration economy
# ---------------------------------------------------------------------------

def demo_economy() -> MultiDimEconomy:
    """A small, economically legible economy with two joint processes.

    12 products, 6 processes. The star is cattle raising -- a joint process
    yielding two beef cuts (tenderloin, hamburger), hide, tallow, bone, manure,
    and enteric methane from one pool of feed, water, energy and labour. There is
    a genuine inter-industry cycle (farming burns diesel + electricity; the power
    plant burns diesel; the refinery burns electricity), so the recursion is
    exercised, not just a DAG.

    Numbers are illustrative but internally consistent; the point is the
    STRUCTURE and the split rules, which are exactly what real EEIO data replaces.
    """
    products = [
        "grain", "electricity", "diesel", "water",     # 0-3 upstream
        "tenderloin", "hamburger", "hide", "tallow",   # 4-7 cattle outputs
        "bone", "manure", "methane",                   # 8-10 cattle outputs
        "leather",                                      # 11 downstream
    ]
    units = {
        "grain": "kg", "electricity": "MJ", "diesel": "MJ", "water": "kg",
        "tenderloin": "kg", "hamburger": "kg", "hide": "kg", "tallow": "kg",
        "bone": "kg", "manure": "kg", "methane": "kg", "leather": "kg",
    }
    processes = ["grain_farming", "power_plant", "refinery",
                 "water_pumping", "cattle_raising", "tannery"]
    P = {p: i for i, p in enumerate(products)}
    K = {k: j for j, k in enumerate(processes)}
    M, N = len(products), len(processes)

    # ---- make matrix B[i,k]: what each process produces per run --------------
    make = {
        "grain_farming": {"grain": 100.0},
        "power_plant":   {"electricity": 1000.0},
        "refinery":      {"diesel": 1000.0},
        "water_pumping": {"water": 1000.0},
        # cattle: masses (kg) per run -- yields differ by two orders across cuts
        "cattle_raising": {
            "tenderloin": 1.0,    # ~1% -- prized, scarce
            "hamburger":  5.0,    # ~5% -- ordinary
            "hide":       7.0,
            "tallow":    10.0,
            "bone":      12.0,
            "manure":    55.0,    # the bulk output
            "methane":   10.0,    # enteric -- waste co-product
        },
        "tannery":       {"leather": 6.0},
    }

    # ---- use matrix A[i,k]: what each process consumes per run ---------------
    use = {
        "grain_farming": {"diesel": 30.0, "electricity": 10.0, "water": 200.0},
        "power_plant":   {"diesel": 250.0},
        "refinery":      {"electricity": 80.0},
        "water_pumping": {"electricity": 40.0},
        "cattle_raising": {"grain": 90.0, "water": 400.0, "electricity": 20.0},
        "tannery":        {"hide": 6.0, "water": 100.0, "electricity": 15.0},
    }

    # ---- direct resource inputs per process, per run ------------------------
    # materials (kg of raw feedstock the process itself introduces),
    # energy (MJ the process burns on-site), labour (hours).
    direct = {
        "materials": np.zeros(N),
        "energy":    np.zeros(N),
        "labour":    np.zeros(N),
    }
    direct_spec = {
        #                    materials(kg) energy(MJ) labour(hr)
        "grain_farming":    (50.0,         40.0,      8.0),
        "power_plant":      (5.0,          60.0,      3.0),
        "refinery":         (10.0,         50.0,      4.0),
        "water_pumping":    (2.0,          20.0,      2.0),
        "cattle_raising":   (30.0,         70.0,      25.0),   # labour-heavy
        "tannery":          (8.0,          35.0,      12.0),
    }
    for name, (mat, ene, lab) in direct_spec.items():
        k = K[name]
        direct["materials"][k] = mat
        direct["energy"][k] = ene
        direct["labour"][k] = lab

    # ---- theta: the physical split of each joint process --------------------
    # MATERIAL theta = by mass (deposition). For the two beef cuts of equal
    # tissue composition this is proportional to the mass made, so cost per kg
    # comes out EQUAL across cuts -- cost != scarcity.
    theta_mat = _theta_from(make, P, N, basis="mass")

    # ENERGY theta = its own measured basis: lean tenderloin and fatty tallow /
    # methane carry different deposition energy per kg, so energy theta is NOT
    # proportional to mass. This is the legitimate §3.4a refinement, and it makes
    # materials and energy genuinely separate linear systems (split per dim).
    energy_basis = {
        "tenderloin": 2.2,   # lean muscle, high metabolic deposition cost / kg
        "hamburger":  1.6,
        "hide":       0.8,
        "tallow":     1.2,
        "bone":       0.5,
        "manure":     0.3,
        "methane":    3.0,   # energetically expensive enteric loss / kg
    }
    theta_ene = _theta_from(make, P, N, basis="custom",
                            per_output={"cattle_raising": energy_basis})

    # LABOUR theta -- the OP-18 rule: labour has no per-product trace, so it
    # RIDES the material split. Not a copy: the SAME object.
    theta_lab = theta_mat

    theta = {"materials": theta_mat, "energy": theta_ene, "labour": theta_lab}

    A = _sparse_from(use, P, K, M, N)
    B = _sparse_from(make, P, K, M, N)

    econ = MultiDimEconomy(products, processes, A, B, direct, theta, units)
    # enforce the OP-18 invariant explicitly
    assert econ.theta["labour"] is econ.theta["materials"], \
        "OP-18: labour theta must BE the material theta"
    return econ


def scale_process_output(econ: MultiDimEconomy, process_name: str, factor: float):
    """Return a copy of `econ` with one process's OUTPUT mass scaled by `factor`,
    every input (A, direct resources) held fixed.

    Models a single animal that came out +/-10% for identical feed, water,
    energy, and labour (A6: the ledger is derived per event, not from a stored
    average). Theta is preserved -- scaling all of a process's outputs by the
    same factor leaves the normalised split unchanged, i.e. same composition,
    only size differs. (A composition shift -- the extra mass going to fat rather
    than muscle -- is the separate Theta question, Objections §C Test 3.)
    """
    k = econ.processes.index(process_name)
    Bcsc = econ.B.tocsc()
    B = econ.B.tolil(copy=True)
    for i in Bcsc[:, k].nonzero()[0]:
        B[i, k] = float(Bcsc[i, k]) * factor
    return MultiDimEconomy(econ.products, econ.processes, econ.A, B.tocsr(),
                           econ.direct, econ.theta, econ.units)


def _sparse_from(spec, P, K, M, N):
    rows, cols, data = [], [], []
    for kname, outs in spec.items():
        k = K[kname]
        for pname, amt in outs.items():
            rows.append(P[pname]); cols.append(k); data.append(float(amt))
    return sp.coo_matrix((data, (rows, cols)), shape=(M, N)).tocsr()


def _theta_from(make, P, N, basis="mass", per_output=None):
    """Build a normalised split-fraction matrix from a make spec.

    basis="mass"   : theta proportional to units made (mass deposition proxy).
    basis="custom" : theta proportional to units made * per-output weight, using
                     `per_output[process][product]` where given (else weight 1).
    Each process column is renormalised to sum to 1 over its outputs.
    """
    per_output = per_output or {}
    M = len(P)
    rows, cols, data = [], [], []
    for kname, outs in make.items():
        # column index: recover k from any product's presence -- use order
        # of processes is fixed by caller, so map via the make dict ordering.
        pass
    # need K mapping; rebuild from make insertion order == process order
    Knames = list(make.keys())
    K = {name: j for j, name in enumerate(Knames)}
    for kname, outs in make.items():
        k = K[kname]
        weights = {}
        ow = per_output.get(kname, {})
        for pname, amt in outs.items():
            w = amt * ow.get(pname, 1.0) if basis == "custom" else amt
            weights[pname] = w
        tot = sum(weights.values())
        for pname, w in weights.items():
            rows.append(P[pname]); cols.append(k); data.append(w / tot)
    return sp.coo_matrix((data, (rows, cols)), shape=(M, N)).tocsr()


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report(econ: MultiDimEconomy):
    vecs = debit_vectors(econ)
    # a plausible collapse weighting (the OP-10 object, kept external & flagged)
    weights = {"materials": 1.0, "energy": 0.05, "labour": 1.0}
    total = collapse(vecs, weights)

    print("=" * 74)
    print("AEQUITAS ESTIMATION ENGINE -- per-product debit vectors (synthetic)")
    print("=" * 74)
    print(f"{'product':<12} {'unit':<5} {'materials':>10} {'energy':>10} "
          f"{'labour':>9} {'collapsed':>11}")
    print("-" * 74)
    for i, name in enumerate(econ.products):
        print(f"{name:<12} {econ.units[name]:<5} "
              f"{vecs['materials'][i]:>10.4f} {vecs['energy'][i]:>10.4f} "
              f"{vecs['labour'][i]:>9.4f} {total[i]:>11.4f}")
    print("-" * 74)
    print("collapse weights (OP-10 weighting model -- external by design): "
          f"{weights}")

    # the cost != scarcity headline
    ti, hi = econ.products.index("tenderloin"), econ.products.index("hamburger")
    print("\nCOST != SCARCITY  (Foundations §3.4a, v0.6)")
    print(f"  tenderloin (1% yield): materials={vecs['materials'][ti]:.4f}/kg, "
          f"labour={vecs['labour'][ti]:.4f}/kg")
    print(f"  hamburger  (5% yield): materials={vecs['materials'][hi]:.4f}/kg, "
          f"labour={vecs['labour'][hi]:.4f}/kg")
    print("  -> equal per kg in materials & labour: the rare cut is NOT more "
          "costly.")
    m2 = method2_yield_weighted(
        econ, econ.processes.index("cattle_raising"),
        desirability={"tenderloin": 20.0, "hamburger": 5.0, "hide": 3.0,
                      "tallow": 1.0, "bone": 0.5, "manure": 0.2, "methane": 0.1})
    print(f"  REJECTED Method 2 (yield/desirability): tenderloin="
          f"{m2['tenderloin']:.4f}/kg vs hamburger={m2['hamburger']:.4f}/kg "
          f"({m2['tenderloin']/m2['hamburger']:.1f}x) -- price-rationing by "
          "standing.")

    # the residual cohort demo
    print("\nRESIDUAL COHORT RULE  (N - Y) / Z   (§5.1b)")
    true_outputs = [40, 30, 25, 20, 15, 10]     # heterogeneous grain producers
    N_total = float(sum(true_outputs))          # independently known total (FAO)
    join_best_first = sorted(range(len(true_outputs)),
                             key=lambda i: -true_outputs[i])
    trace = adverse_selection_demo(N_total, true_outputs, join_best_first)
    print("  best producers instrument first; estimate for remaining dark "
          "producers:")
    for n, dark, est in trace:
        note = "  <- darkness pays less as good producers leave" if n == 1 else ""
        print(f"    joined={n}  dark={dark:>2}  per-dark estimate="
              f"{est:>7.2f}{note}")
    print("=" * 74)
    return vecs, total


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def test_nonnegative_and_finite():
    """Every per-product debit is finite and >= 0 (the proven structural result,
    now exercised on a real multi-dimension economy)."""
    econ = demo_economy()
    vecs = debit_vectors(econ)
    for dim, p in vecs.items():
        assert np.all(np.isfinite(p)), f"{dim}: non-finite debit"
        assert np.min(p) >= -1e-12, f"{dim}: negative debit {np.min(p)}"
    print(f"[ok] non-negative & finite across {list(vecs)} "
          f"(min={min(np.min(p) for p in vecs.values()):.2e})")


def test_op18_labour_rides_materials():
    """OP-18: labour reuses the material operator EXACTLY.

    Because theta['labour'] IS theta['materials'], the assembled A~ for the two
    dimensions must be bit-identical -- labour introduces no new split basis and
    therefore no new capture surface. Only the direct resource (c) differs."""
    econ = demo_economy()
    _, _, At_mat, c_mat = solve_dimension(econ, "materials")
    _, _, At_lab, c_lab = solve_dimension(econ, "labour")
    gap = abs(At_mat - At_lab).max()
    assert gap == 0.0, f"labour A~ must equal material A~ exactly, gap={gap}"
    assert not np.allclose(c_mat, c_lab), "c should differ (different resource)"
    # and energy, with its own theta, must NOT share the operator
    _, _, At_ene, _ = solve_dimension(econ, "energy")
    assert abs(At_mat - At_ene).max() > 1e-9, \
        "energy has its own theta -> different operator (split per dimension)"
    print("[ok] OP-18: labour A~ == material A~ exactly; energy A~ differs "
          "(per-dimension split)")


def test_cost_not_scarcity():
    """Two beef cuts of equal composition cost the SAME per unit in materials and
    labour, regardless of yield; Method 2 makes them differ."""
    econ = demo_economy()
    vecs = debit_vectors(econ)
    ti = econ.products.index("tenderloin")
    hi = econ.products.index("hamburger")
    for dim in ("materials", "labour"):
        assert abs(vecs[dim][ti] - vecs[dim][hi]) < 1e-9, \
            f"{dim}: cuts should cost the same per kg ({vecs[dim][ti]} vs {vecs[dim][hi]})"
    m2 = method2_yield_weighted(
        econ, econ.processes.index("cattle_raising"),
        desirability={"tenderloin": 20.0, "hamburger": 5.0, "hide": 3.0,
                      "tallow": 1.0, "bone": 0.5, "manure": 0.2, "methane": 0.1})
    assert m2["tenderloin"] > 3 * m2["hamburger"], \
        "Method 2 should inflate the prized cut (that is why it is rejected)"
    print(f"[ok] cost != scarcity: cuts equal per kg (materials & labour); "
          f"Method 2 inflates tenderloin {m2['tenderloin']/m2['hamburger']:.1f}x")


def test_split_before_collapse():
    """§3.2a: collapsing across dimensions is done AFTER each per-dimension solve.

    For dimensions that share an operator (materials & labour, OP-18) the two
    orders agree exactly. For dimensions with different theta (energy) they do
    NOT, which is the whole reason the rule is split-THEN-collapse, not the
    reverse. This test pins both facts."""
    econ = demo_economy()
    p_mat, _, At_mat, c_mat = solve_dimension(econ, "materials")
    p_lab, _, At_lab, c_lab = solve_dimension(econ, "labour")
    # shared operator -> collapse-first equals solve-first
    w_mat, w_lab = 1.0, 2.5
    collapse_first = solve_direct(At_mat, w_mat * c_mat + w_lab * c_lab)
    solve_first = w_mat * p_mat + w_lab * p_lab
    assert np.max(np.abs(collapse_first - solve_first)) < 1e-8, \
        "shared-operator dims must agree under either order"
    # different operator (energy) -> cannot collapse c's before solving
    p_ene, _, At_ene, c_ene = solve_dimension(econ, "energy")
    wrong = solve_direct(At_mat, c_mat + c_ene)      # illegally reuse mat operator
    right = p_mat + p_ene                            # correct: per-dim solve, sum
    assert np.max(np.abs(wrong - right)) > 1e-6, \
        "energy uses a different theta; collapsing before solving must differ"
    print("[ok] split-before-collapse: shared-op dims commute; energy does not "
          "(must split per dimension)")


def test_residual_adverse_selection():
    """The dark-producer estimate falls as good producers instrument and leave."""
    true_outputs = [40, 30, 25, 20, 15, 10]
    N_total = float(sum(true_outputs))          # true total = independently known N
    order = sorted(range(len(true_outputs)), key=lambda i: -true_outputs[i])
    trace = adverse_selection_demo(N_total, true_outputs, order)
    ests = [est for _, _, est in trace]
    # each estimate is the mean of the still-dark producers; best leaving first
    # drives that mean strictly down. (Last entry is 0: no dark producers left.)
    dark_means = ests[:-1]
    assert all(dark_means[i] > dark_means[i + 1] for i in range(len(dark_means) - 1)), \
        f"estimate should fall as good producers join: {ests}"
    print(f"[ok] residual adverse selection: dark estimate falls "
          f"{ests[0]:.1f} -> {ests[-2]:.1f} as good producers instrument")


def test_per_event_yield_variance():
    """Same inputs, output mass varies +/-10% (A6: per-event, not averaged).

    A steer that comes out 10% bigger on identical feed has beef ~10% CHEAPER
    per kg -- the fixed input pool spread over more tissue. This is the efficiency
    signal (A5/§7.1), recorded faithfully rather than washed into an average.
    Three invariants are pinned:
      1. cost/kg scales as 1/factor (bigger animal -> cheaper per kg);
      2. total debit routed to each co-product is INVARIANT (fixed input pool,
         fixed physical split) -- yield moves the per-kg figure, not the pool;
      3. the farmer's labour CREDIT (hours) is untouched -- only the output's
         debit-cost moves.
    Averages (§5.1b) cover only UNMEASURED producers; a measured animal carries
    its real numbers, which is what this test exercises.
    """
    econ = demo_economy()
    ci = econ.products.index("tenderloin")
    ki = econ.processes.index("cattle_raising")
    res = {}
    for f in (0.9, 1.0, 1.1):
        e = scale_process_output(econ, "cattle_raising", f)
        p = solve_dimension(e, "materials")[0]
        mass = float(e.B.tocsc()[ci, ki])
        res[f] = dict(cost_per_kg=p[ci], total=p[ci] * mass)
    base = res[1.0]["cost_per_kg"]
    # 1. inverse scaling with yield
    assert abs(res[0.9]["cost_per_kg"] - base / 0.9) < 1e-9
    assert abs(res[1.1]["cost_per_kg"] - base / 1.1) < 1e-9
    assert res[1.1]["cost_per_kg"] < base < res[0.9]["cost_per_kg"]
    # 2. total debit per co-product invariant across yields
    totals = [res[f]["total"] for f in (0.9, 1.0, 1.1)]
    assert max(totals) - min(totals) < 1e-9, f"total debit should be fixed: {totals}"
    # 3. labour credit (the farmer's hours) unchanged by yield
    e11 = scale_process_output(econ, "cattle_raising", 1.1)
    assert econ.direct["labour"][ki] == e11.direct["labour"][ki]
    print(f"[ok] per-event yield variance: cost/kg {res[0.9]['cost_per_kg']:.4f} "
          f"(-10%) > {base:.4f} > {res[1.1]['cost_per_kg']:.4f} (+10%); "
          f"total debit invariant ({totals[0]:.4f}); labour credit unchanged")


def run_tests():
    test_nonnegative_and_finite()
    test_op18_labour_rides_materials()
    test_cost_not_scarcity()
    test_split_before_collapse()
    test_residual_adverse_selection()
    test_per_event_yield_variance()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

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
    report(demo_economy())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
