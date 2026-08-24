"""
Recursion convergence of the OP-17 / §3.4a allocation rule.

Question (Foundations §3.4a): a joint process's debit divides according to where
the process physically sent its inputs (fractions theta >= 0). But every input is
itself the output of another joint process, so a product's per-unit debit p[i] is
defined recursively:

        p[i] = sum_k  theta[i,k] * ( l[k] + sum_j A[j,k]*p[j] ) / B[i,k]

Two things were asserted and unproven for a whole economy:
  1. Termination / convergence  -- does the recursion have a fixed point reached
     by iteration, even with inter-industry cycles (the Sraffa corn-iron structure)?
  2. Non-negativity (IC-10)      -- each share is asserted >= 0 because "a forward
     measurement cannot be negative". True per process; Steedman showed value-based
     joint-production systems can produce NEGATIVE aggregate values. Does the
     physical allocation escape that?

Hypothesis: because Aequitas splits by physically-measured fractions theta >= 0
(never by inverting a value/price make-matrix), the per-unit debit vector is the
solution of a NON-NEGATIVE linear fixed point  p = c + A~ p  with A~ >= 0, c >= 0.
So whenever the economy is productive (spectral radius rho(A~) < 1), p is the
Neumann series  p = sum_{n>=0} A~^n c  -- unique, non-negative, and reached by
simple iteration -- FOR FREE, independent of how jointly-produced the economy is.
Steedman's negatives require inverting B; Aequitas never does.

This module builds synthetic economies, runs the Aequitas forward allocation and a
value/price ("Steedman") allocation on the same physical data, and reports:
    iterations-to-converge and min(p) vs rho(A~), across a sweep, plus the
    concrete Steedman 2-good counterexample where value goes negative and
    Aequitas stays clean.

Run:  python recursion_convergence.py            # full sweep -> results.csv + plots
      python recursion_convergence.py --test     # just the self-tests
      python recursion_convergence.py --quick     # small fast sweep
"""

from __future__ import annotations

import argparse
import csv
import time
from dataclasses import dataclass, field

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla


# ---------------------------------------------------------------------------
# Economy container
# ---------------------------------------------------------------------------

@dataclass
class Economy:
    """A synthetic joint-production economy.

    Conventions: rows index products i = 0..M-1, columns index processes
    k = 0..N-1. All matrices are scipy.sparse (CSR/CSC), all entries >= 0.

        A[i,k] : units of product i USED by process k, per unit run of k.
        B[i,k] : units of product i MADE by process k, per unit run of k.
                 A process is *joint* iff its column of B has > 1 nonzero.
                 A product has *rivals* iff its row of B has > 1 nonzero.
        l[k]   : direct labour-hours of process k, per unit run.
        Theta[i,k] : physical split fraction of process k's total debit assigned
                 to co-product i.  Theta[i,k] > 0 only where B[i,k] > 0, and each
                 process column sums to 1 over its outputs.  This is the §3.4a
                 instrument reading (tissue-deposition, cracking enthalpy, ...),
                 a GIVEN non-negative parameter -- never optimised.
    """
    M: int
    N: int
    A: sp.spmatrix
    B: sp.spmatrix
    l: np.ndarray
    Theta: sp.spmatrix
    meta: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Building the Aequitas forward fixed-point  p = c + A~ p
# ---------------------------------------------------------------------------

def build_forward(econ: Economy):
    """Assemble the non-negative fixed-point operator for the Aequitas rule.

    For product i produced by processes {k : B[i,k] > 0}, the per-unit forward
    debit contributed by process k is

        g[i,k] = theta[i,k] * ( l[k] + sum_j A[j,k]*p[j] ) / B[i,k].

    When a product has rivals (several producing processes), the reported p[i] is
    the production-weighted average over its producers, weight w[i,k] = B[i,k] /
    sum_k' B[i,k'] (the per-unit log records which process made each unit; the
    average is over the unit mix). Substituting gives  p = c + A~ p  with

        c[i]    = sum_k w[i,k] * theta[i,k] * l[k]      / B[i,k]
        A~[i,j] = sum_k w[i,k] * theta[i,k] * A[j,k]    / B[i,k]

    Both are >= 0 by construction -- no inversion of B anywhere. Returns (A_tilde
    CSR (M x M), c (M,)).
    """
    M, N = econ.M, econ.N
    A = econ.A.tocsc()
    B = econ.B.tocsr()
    Theta = econ.Theta.tocsr()
    l = econ.l

    # production weights w[i,k] over a product's rival producers
    row_tot = np.asarray(B.sum(axis=1)).ravel()          # sum_k B[i,k]
    row_tot_safe = np.where(row_tot > 0, row_tot, 1.0)

    Bcoo = econ.B.tocoo()
    # coefficient m[i,k] = w[i,k] * theta[i,k] / B[i,k]
    theta_ik = np.asarray(Theta[Bcoo.row, Bcoo.col]).ravel()
    w_ik = Bcoo.data / row_tot_safe[Bcoo.row]
    coef = w_ik * theta_ik / Bcoo.data                    # (nnz_B,)

    # c[i] = sum_k coef[i,k] * l[k]
    c = np.zeros(M)
    np.add.at(c, Bcoo.row, coef * l[Bcoo.col])

    # A~[i,j] = sum_k coef[i,k] * A[j,k].  Build as  (coef-scaled make) @ A^T.
    # Let C be the (M x N) matrix with C[i,k] = coef for produced (i,k) pairs.
    C = sp.coo_matrix((coef, (Bcoo.row, Bcoo.col)), shape=(M, N)).tocsr()
    A_tilde = (C @ A.T).tocsr()                            # (M x N)(N x M) = M x M
    return A_tilde, c


def spectral_radius(A_tilde: sp.spmatrix) -> float:
    """Largest-magnitude eigenvalue of A~ (the convergence predictor).

    ARPACK's `eigs` is unreliable on small matrices (it targets large sparse
    problems, k << M), so for M up to a few hundred we use the exact dense
    eigenvalues -- cheap at that size and free of the spurious values `eigs`
    can return for, e.g., M=10.
    """
    M = A_tilde.shape[0]
    if M <= 300:
        return float(max(abs(np.linalg.eigvals(A_tilde.toarray()))))
    try:
        vals = spla.eigs(A_tilde.astype(float), k=1, which="LM",
                         return_eigenvectors=False, maxiter=5000)
        return float(abs(vals[0]))
    except (spla.ArpackNoConvergence, spla.ArpackError):
        # fall back to a power iteration on |A~|
        v = np.random.default_rng(0).random(M)
        v /= np.linalg.norm(v)
        lam = 0.0
        for _ in range(2000):
            w = A_tilde @ v
            lam_new = np.linalg.norm(w)
            if lam_new == 0:
                return 0.0
            v = w / lam_new
            if abs(lam_new - lam) < 1e-12 * max(lam_new, 1e-30):
                break
            lam = lam_new
        return float(lam)


def solve_iteration(A_tilde, c, tol=1e-10, maxit=100_000):
    """Jacobi iteration  p <- c + A~ p  from p = 0.

    Returns (p, iters, converged, rate) where rate is the fitted geometric decay
    of the residual (should track rho(A~)). Divergence (non-productive economy,
    rho >= 1) is detected by the residual blowing up or stalling.
    """
    p = np.zeros_like(c)
    resid = []
    converged = False
    for it in range(1, maxit + 1):
        p_new = c + A_tilde @ p
        d = np.max(np.abs(p_new - p))
        resid.append(d)
        p = p_new
        if not np.isfinite(d) or d > 1e18:
            return p, it, False, float("nan")
        if d < tol:
            converged = True
            break
    rate = _fit_rate(resid)
    return p, len(resid), converged, rate


def _fit_rate(resid):
    """Geometric decay rate from the tail of the residual sequence."""
    r = np.asarray(resid)
    good = r[(r > 0) & np.isfinite(r)]
    if len(good) < 5:
        return float("nan")
    tail = good[len(good) // 3:]          # drop transient
    if len(tail) < 3:
        tail = good[-3:]
    logs = np.log(tail)
    n = np.arange(len(tail))
    slope = np.polyfit(n, logs, 1)[0]
    return float(np.exp(slope))


def solve_direct(A_tilde, c):
    """Direct solve of (I - A~) p = c, for cross-checking iteration."""
    M = A_tilde.shape[0]
    lhs = (sp.identity(M, format="csc") - A_tilde.tocsc())
    return spla.spsolve(lhs, c)


# ---------------------------------------------------------------------------
# Value / price ("Steedman") allocation on the SAME physical economy
# ---------------------------------------------------------------------------

def solve_value_square(econ: Economy):
    """Textbook joint-production labour values:  v (B - A) = l,  v = l (B-A)^-1.

    Requires a square make matrix (N == M). This is exactly the construction
    Steedman used to exhibit negative labour values under joint production. We
    solve it and report min(v) and whether B-A was invertible. Compare against
    the Aequitas forward p on the same (A, B, l), which never inverts B.

    Returns dict(min_v, invertible, v) or dict(invertible=False) if not square /
    singular.
    """
    M, N = econ.M, econ.N
    if M != N:
        return {"invertible": False, "min_v": float("nan"), "reason": "not square"}
    BmA = (econ.B - econ.A).toarray()
    try:
        # v is a row vector: v (B-A) = l  ->  (B-A)^T v^T = l^T
        v = np.linalg.solve(BmA.T, econ.l)
    except np.linalg.LinAlgError:
        return {"invertible": False, "min_v": float("nan"), "reason": "singular"}
    return {"invertible": True, "min_v": float(np.min(v)), "v": v}


# ---------------------------------------------------------------------------
# Synthetic economy generators
# ---------------------------------------------------------------------------

def _rescale_to_rho(econ: Economy, target_rho: float):
    """Scale A so that rho(A~) equals target_rho exactly.

    A~ is linear in A, so rho(s*A~) = s*rho(A~); scaling the whole use matrix A
    by target/rho_raw lands rho on target. c is untouched (it depends on l only),
    so this isolates the cycle-strength knob cleanly.
    """
    A_tilde, _ = build_forward(econ)
    rho_raw = spectral_radius(A_tilde)
    if rho_raw <= 1e-12:
        return econ, rho_raw
    s = target_rho / rho_raw
    econ.A = econ.A * s
    return econ, rho_raw


def generate_base(M, density, joint_frac, target_rho, theta_alpha, seed):
    """Base case: every product made by exactly one process (no rivals).

    Products are partitioned among processes; a fraction `joint_frac` of the
    processes are joint (produce >= 2 products). Exercises the full recursion
    (inter-industry cycles via A) and joint production, with A~ guaranteed >= 0.
    """
    rng = np.random.default_rng(seed)

    # ---- partition M products into processes -----------------------------
    order = rng.permutation(M)
    groups, idx = [], 0
    while idx < M:
        make_joint = rng.random() < joint_frac and (M - idx) >= 2
        if make_joint:
            size = 2 if (M - idx) < 3 or rng.random() < 0.6 else 3
            size = min(size, M - idx)
        else:
            size = 1
        groups.append(order[idx:idx + size].tolist())
        idx += size
    N = len(groups)

    # ---- B, Theta, l -----------------------------------------------------
    rows_B, cols_B, data_B = [], [], []
    rows_T, cols_T, data_T = [], [], []
    l = rng.uniform(0.5, 1.5, size=N)
    for k, prods in enumerate(groups):
        amounts = rng.uniform(0.5, 1.5, size=len(prods))
        theta = rng.dirichlet([theta_alpha] * len(prods))
        for i, b, t in zip(prods, amounts, theta):
            rows_B.append(i); cols_B.append(k); data_B.append(b)
            rows_T.append(i); cols_T.append(k); data_T.append(t)
    B = sp.coo_matrix((data_B, (rows_B, cols_B)), shape=(M, N)).tocsr()
    Theta = sp.coo_matrix((data_T, (rows_T, cols_T)), shape=(M, N)).tocsr()

    # ---- A : each process consumes ~density*M random products ------------
    A = _random_use_matrix(M, N, density, rng)

    econ = Economy(M, N, A, B, l, Theta,
                   meta=dict(kind="base", density=density, joint_frac=joint_frac,
                             theta_alpha=theta_alpha, seed=seed,
                             target_rho=target_rho))
    econ, rho_raw = _rescale_to_rho(econ, target_rho)
    econ.meta["rho_raw"] = rho_raw
    return econ


def generate_square_joint(M, density, target_rho, theta_alpha, seed, full_joint=True):
    """Square von-Neumann joint system (N == M) with rivals, for the value arm.

    Every process produces >= 2 products and every product is made by several
    processes, so B is a genuine joint make-matrix that (B - A)^-1 can turn
    sign-indefinite -- the Steedman regime. The Aequitas forward rule runs on the
    same data without ever inverting B.
    """
    rng = np.random.default_rng(seed)
    N = M
    outdeg = 2 if full_joint else rng.integers(1, 3)

    rows_B, cols_B, data_B = [], [], []
    rows_T, cols_T, data_T = [], [], []
    l = rng.uniform(0.5, 1.5, size=N)
    for k in range(N):
        n_out = outdeg if full_joint else int(rng.integers(2, 3))
        prods = rng.choice(M, size=n_out, replace=False)
        amounts = rng.uniform(0.5, 1.5, size=n_out)
        theta = rng.dirichlet([theta_alpha] * n_out)
        for i, b, t in zip(prods, amounts, theta):
            rows_B.append(int(i)); cols_B.append(k); data_B.append(float(b))
            rows_T.append(int(i)); cols_T.append(k); data_T.append(float(t))
    B = sp.coo_matrix((data_B, (rows_B, cols_B)), shape=(M, N)).tocsr()
    Theta = sp.coo_matrix((data_T, (rows_T, cols_T)), shape=(M, N)).tocsr()

    # ensure every product has at least one producer (row of B nonzero)
    row_tot = np.asarray(B.sum(axis=1)).ravel()
    for i in np.where(row_tot == 0)[0]:
        k = int(rng.integers(0, N))
        B = B.tolil(); Theta = Theta.tolil()
        B[i, k] = rng.uniform(0.5, 1.5)
        # renormalise that process column of Theta
        Theta[i, k] = rng.uniform(0.2, 0.8)
        B = B.tocsr(); Theta = Theta.tocsr()
    Theta = _renormalise_theta(B, Theta)

    A = _random_use_matrix(M, N, density, rng)
    econ = Economy(M, N, A, B, l, Theta,
                   meta=dict(kind="square_joint", density=density,
                             theta_alpha=theta_alpha, seed=seed,
                             target_rho=target_rho))
    econ, rho_raw = _rescale_to_rho(econ, target_rho)
    econ.meta["rho_raw"] = rho_raw
    return econ


def _random_use_matrix(M, N, density, rng):
    """(M x N) non-negative use matrix; each process consumes ~density*M products."""
    n_in = max(1, int(round(density * M)))
    rows, cols, data = [], [], []
    for k in range(N):
        ins = rng.choice(M, size=min(n_in, M), replace=False)
        vals = rng.uniform(0.1, 1.0, size=len(ins))
        rows.extend(ins.tolist()); cols.extend([k] * len(ins)); data.extend(vals.tolist())
    return sp.coo_matrix((data, (rows, cols)), shape=(M, N)).tocsr()


def _renormalise_theta(B, Theta):
    """Make each process column of Theta sum to 1 over its outputs."""
    B = B.tocsc(); Theta = Theta.tocsc().tolil()
    for k in range(B.shape[1]):
        rows = B[:, k].nonzero()[0]
        if len(rows) == 0:
            continue
        vals = np.array([Theta[i, k] for i in rows], dtype=float)
        if vals.sum() <= 0:
            vals = np.ones(len(rows))
        vals = vals / vals.sum()
        for i, v in zip(rows, vals):
            Theta[i, k] = v
    return Theta.tocsr()


# ---------------------------------------------------------------------------
# The concrete Steedman counterexample (fixed, reproducible)
# ---------------------------------------------------------------------------

def steedman_2good():
    """A hand-built 2-good joint economy with NEGATIVE labour value.

    Two processes, two goods (rows = goods, cols = processes):
        make   B = [[6, 3],
                    [1, 12]]
        use    A = [[5, 0],
                    [0, 10]]
        labour l = [1, 1]
    Value system v(B-A)=l with (B-A)=[[1,3],[1,2]], det=-1,
        v = l (B-A)^-1 = [-1, 2]   <-- good 1 has NEGATIVE labour value.

    The Aequitas forward rule on the identical physical data (split by output
    share as the physical instrument) yields p >= 0. Demonstrates the contrast
    on one clean, checkable case.
    """
    B = sp.csr_matrix(np.array([[6., 3.], [1., 12.]]))
    A = sp.csr_matrix(np.array([[5., 0.], [0., 10.]]))
    l = np.array([1., 1.])
    # physical split: by output units within each process
    Bd = B.toarray()
    Theta = Bd / Bd.sum(axis=0, keepdims=True)
    econ = Economy(2, 2, A, B, l, sp.csr_matrix(Theta),
                   meta=dict(kind="steedman_2good"))
    return econ


# ---------------------------------------------------------------------------
# Per-run evaluation
# ---------------------------------------------------------------------------

def evaluate(econ: Economy, want_value=False, cross_check=True):
    """Run the iteration (and optionally direct-solve cross-check + value arm).

    `cross_check` does the (I-A~) direct solve to confirm the iteration; it is
    expensive at large M and redundant once validated at small/medium M, so the
    sweep turns it off above a size threshold.
    """
    A_tilde, c = build_forward(econ)
    rho = spectral_radius(A_tilde)

    t0 = time.perf_counter()
    p_it, iters, conv, rate = solve_iteration(A_tilde, c)
    t_iter = time.perf_counter() - t0

    # direct solve only meaningful (and only attempted) for productive economies
    direct_gap = float("nan")
    if rho < 1.0 and cross_check:
        try:
            p_dir = solve_direct(A_tilde, c)
            direct_gap = float(np.max(np.abs(p_it - p_dir)))
        except Exception:
            direct_gap = float("nan")

    row = dict(
        kind=econ.meta.get("kind"),
        M=econ.M, N=econ.N,
        density=econ.meta.get("density"),
        joint_frac=econ.meta.get("joint_frac"),
        theta_alpha=econ.meta.get("theta_alpha"),
        seed=econ.meta.get("seed"),
        target_rho=econ.meta.get("target_rho"),
        rho=rho,
        iters=iters,
        converged=int(conv),
        fitted_rate=rate,
        min_p=float(np.min(p_it)) if np.all(np.isfinite(p_it)) else float("nan"),
        max_p=float(np.max(p_it)) if np.all(np.isfinite(p_it)) else float("nan"),
        direct_gap=direct_gap,
        t_iter=t_iter,
    )

    if want_value:
        val = solve_value_square(econ)
        row["value_invertible"] = int(val.get("invertible", False))
        row["value_min_v"] = val.get("min_v", float("nan"))
        row["value_negative"] = int(val.get("invertible", False)
                                     and val.get("min_v", 0.0) < -1e-9)
    return row, p_it


# ---------------------------------------------------------------------------
# Sweep driver
# ---------------------------------------------------------------------------

RHO_TARGETS = [0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 1.05, 1.2]
JOINT_FRACS = [0.0, 0.25, 0.5, 1.0]
THETA_ALPHAS = [1.0, 0.3]     # symmetric and skewed Dirichlet


def _seeds_for(M, base_seeds):
    """Fewer seeds at large M: the science is carried by M<=1000; the biggest
    size exists only to demonstrate tractability (runs in seconds)."""
    if M >= 10_000:
        return max(3, base_seeds // 10)
    if M >= 1000:
        return max(5, base_seeds // 3)
    return base_seeds


def run_sweep(sizes, seeds_per_cell, density, out_csv, quick=False):
    rows = []
    rho_targets = RHO_TARGETS if not quick else [0.5, 0.9, 0.99, 1.2]
    joint_fracs = JOINT_FRACS if not quick else [0.0, 1.0]
    theta_alphas = THETA_ALPHAS if not quick else [1.0]

    # ---- Aequitas base-case sweep ----------------------------------------
    for M in sizes:
        seeds = _seeds_for(M, seeds_per_cell)
        cross = M <= 2000                      # direct-solve cross-check only where cheap
        # at the largest size, thin the grid -- it is a timing demo, not new science
        jfs = joint_fracs if M < 10_000 else [0.0, 1.0]
        tas = theta_alphas if M < 10_000 else theta_alphas[:1]
        rts = rho_targets if M < 10_000 else [0.5, 0.9, 0.99, 1.2]
        for jf in jfs:
            for ta in tas:
                for rt in rts:
                    for s in range(seeds):
                        econ = generate_base(M, density, jf, rt, ta,
                                             seed=1000 * s + M + int(rt * 100))
                        row, _ = evaluate(econ, want_value=False, cross_check=cross)
                        rows.append(row)

    # ---- square-joint comparison sweep (value arm on) --------------------
    val_sizes = [s for s in sizes if s <= 200]     # dense-ish invert; keep modest
    for M in val_sizes:
        for ta in theta_alphas:
            for rt in [r for r in rho_targets if r < 1.0]:
                for s in range(seeds_per_cell):
                    econ = generate_square_joint(M, density, rt, ta,
                                                 seed=7000 * s + M + int(rt * 100))
                    row, _ = evaluate(econ, want_value=True)
                    rows.append(row)

    _write_csv(rows, out_csv)
    return rows


def _write_csv(rows, path):
    if not rows:
        return
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow(r)


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def _read_csv(path):
    """Load a results CSV back into typed rows (for --replot)."""
    int_keys = {"M", "N", "seed", "iters", "converged", "value_invertible",
                "value_negative"}
    float_keys = {"density", "joint_frac", "theta_alpha", "target_rho", "rho",
                  "fitted_rate", "min_p", "max_p", "direct_gap", "t_iter",
                  "value_min_v"}
    out = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            row = {}
            for k, v in r.items():
                if k in int_keys:
                    row[k] = int(float(v)) if v not in ("", "nan") else 0
                elif k in float_keys:
                    row[k] = float(v) if v not in ("",) else float("nan")
                else:
                    row[k] = v
            out.append(row)
    return out


def make_plots(rows, prefix):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    base = [r for r in rows if r["kind"] == "base"]
    sq = [r for r in rows if r["kind"] == "square_joint"]

    # 1. iterations vs rho, coloured by joint_frac
    fig, ax = plt.subplots(figsize=(7, 5))
    conv = [r for r in base if r["converged"]]
    jfs = sorted({r["joint_frac"] for r in conv})
    cmap = plt.get_cmap("viridis")
    for n, jf in enumerate(jfs):
        pts = [r for r in conv if r["joint_frac"] == jf]
        ax.scatter([r["rho"] for r in pts], [r["iters"] for r in pts],
                   s=14, alpha=0.5, color=cmap(n / max(1, len(jfs) - 1)),
                   label=f"joint_frac={jf}")
    ax.set_xlabel(r"spectral radius  $\rho(\tilde A)$")
    ax.set_ylabel("iterations to converge (tol 1e-10)")
    ax.set_yscale("log")
    ax.set_title("Convergence speed vs cycle strength")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(f"{prefix}_iters_vs_rho.png", dpi=130)
    plt.close(fig)

    # 2. min(p) vs rho -- non-negativity (productive, converged economies only;
    #    diverged rho>=1 runs carry meaningless blown-up p and are excluded)
    fig, ax = plt.subplots(figsize=(7, 5))
    b_ok = [r for r in base if r["converged"] and r["rho"] < 1.0]
    s_ok = [r for r in sq if r["converged"] and r["rho"] < 1.0]
    ax.scatter([r["rho"] for r in b_ok], [r["min_p"] for r in b_ok],
               s=12, alpha=0.5, color="#1b7837", label="Aequitas base")
    ax.scatter([r["rho"] for r in s_ok], [r["min_p"] for r in s_ok],
               s=12, alpha=0.5, color="#2166ac", label="Aequitas square-joint")
    ax.axhline(0, color="k", lw=1.0)
    ax.set_xlabel(r"spectral radius  $\rho(\tilde A)$  (productive economies)")
    ax.set_ylabel(r"$\min_i p_i$")
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_title("Non-negativity of the Aequitas allocation "
                 r"($\min_i p_i \geq 0$ everywhere)")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(f"{prefix}_minp_vs_rho.png", dpi=130)
    plt.close(fig)

    # 3. fitted rate vs rho -- should sit on the diagonal
    fig, ax = plt.subplots(figsize=(6, 6))
    good = [r for r in base if r["converged"] and np.isfinite(r["fitted_rate"])]
    ax.scatter([r["rho"] for r in good], [r["fitted_rate"] for r in good],
               s=12, alpha=0.4, color="#762a83")
    lim = [0, 1.05]
    ax.plot(lim, lim, "k--", lw=1, label=r"rate $=\rho$")
    ax.set_xlim(lim); ax.set_ylim(lim)
    ax.set_xlabel(r"$\rho(\tilde A)$"); ax.set_ylabel("fitted geometric rate")
    ax.set_title("Convergence rate tracks the spectral radius")
    ax.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(f"{prefix}_rate_vs_rho.png", dpi=130)
    plt.close(fig)

    # 4. value arm: min(v) vs Aequitas min(p) on the same square economies.
    #    symlog x to show both the near-zero bulk and the extreme (near-singular)
    #    Steedman negatives; shaded region marks where value < 0 <= Aequitas.
    if sq:
        fig, ax = plt.subplots(figsize=(7, 5))
        vv = [r for r in sq if r.get("value_invertible")]
        xs = [r["value_min_v"] for r in vv]
        ys = [r["min_p"] for r in vv]
        ax.axvspan(-1e18, 0, color="#fddbc7", alpha=0.5, zorder=0)
        ax.scatter(xs, ys, s=16, alpha=0.6, color="#b2182b", zorder=2)
        ax.axvline(0, color="k", lw=1.0); ax.axhline(0, color="k", lw=1.0)
        ax.set_xscale("symlog", linthresh=1e-3)
        ax.set_yscale("symlog", linthresh=1e-3)
        nneg = sum(1 for x in xs if x < -1e-9)
        ax.set_xlabel(r"value arm  $\min_i v_i$  (Steedman)  —  "
                      f"{nneg}/{len(vv)} negative")
        ax.set_ylabel(r"Aequitas  $\min_i p_i$  (all $\geq 0$)")
        ax.set_title("Same economy: value allocation vs physical allocation")
        fig.tight_layout(); fig.savefig(f"{prefix}_value_vs_aequitas.png", dpi=130)
        plt.close(fig)


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def test_2x2_hand():
    """Hand-checked 2x2 joint economy: iteration == direct, and p >= 0."""
    # process 0 makes goods {0,1}; process 1 makes goods {0,1} (rivals + joint)
    B = sp.csr_matrix(np.array([[2., 1.], [1., 2.]]))
    A = sp.csr_matrix(np.array([[0.2, 0.1], [0.1, 0.2]]))
    l = np.array([1.0, 1.0])
    Bd = B.toarray()
    Theta = sp.csr_matrix(Bd / Bd.sum(axis=0, keepdims=True))
    econ = Economy(2, 2, A, B, l, Theta, meta=dict(kind="test"))
    A_tilde, c = build_forward(econ)
    p_it, iters, conv, rate = solve_iteration(A_tilde, c)
    p_dir = solve_direct(A_tilde, c)
    assert conv, "iteration did not converge"
    assert np.max(np.abs(p_it - p_dir)) < 1e-8, "iteration != direct"
    assert np.min(p_it) >= 0, "negative p in a productive economy"
    print(f"[ok] 2x2 hand: iters={iters} rate~{rate:.3f} "
          f"p={p_it.round(4)} gap={np.max(np.abs(p_it-p_dir)):.1e}")


def test_steedman_contrast():
    """The value arm goes negative; the Aequitas arm stays >= 0 on the SAME data."""
    econ = steedman_2good()
    val = solve_value_square(econ)
    A_tilde, c = build_forward(econ)
    p, iters, conv, rate = solve_iteration(A_tilde, c)
    assert val["invertible"], "Steedman B-A should be invertible"
    assert val["min_v"] < 0, f"expected a negative value, got {val['v']}"
    assert conv and np.min(p) >= 0, f"Aequitas should stay non-negative, got {p}"
    print(f"[ok] Steedman contrast: value v={np.round(val['v'],4)} "
          f"(min {val['min_v']:.3f} < 0)  |  Aequitas p={p.round(4)} "
          f"(min {np.min(p):.3f} >= 0)")


def test_per_dimension():
    """Debit is a vector: A~ is dimension-independent, so the split is identical
    per physical dimension. Solving with a second resource vector (energy in
    place of labour) uses the SAME A~; the collapsed result equals the weighted
    sum of per-dimension results. Confirms §3.2a split-before-collapse."""
    econ = generate_base(30, density=0.1, joint_frac=0.5, target_rho=0.9,
                         theta_alpha=1.0, seed=42)
    A_tilde, c_lab = build_forward(econ)
    # a second dimension: pretend each process also has 'energy' e[k];
    # its c-vector reuses the SAME coefficients, only l -> e.
    rng = np.random.default_rng(7)
    e = rng.uniform(0.5, 1.5, size=econ.N)
    econ_e = Economy(econ.M, econ.N, econ.A, econ.B, e, econ.Theta, econ.meta)
    A_tilde_e, c_ene = build_forward(econ_e)
    assert (abs(A_tilde - A_tilde_e)).max() < 1e-12, "A~ must not depend on the resource"
    p_lab = solve_direct(A_tilde, c_lab)
    p_ene = solve_direct(A_tilde, c_ene)
    # collapse with arbitrary weights (w_lab, w_ene): per-dim-then-collapse ==
    # collapse-then-solve, because the operator is shared and linear.
    w_lab, w_ene = 1.0, 3.5
    p_collapsed_first = solve_direct(A_tilde, w_lab * c_lab + w_ene * c_ene)
    p_dim_then_collapse = w_lab * p_lab + w_ene * p_ene
    gap = np.max(np.abs(p_collapsed_first - p_dim_then_collapse))
    assert gap < 1e-8, f"per-dimension != collapsed ({gap:.1e})"
    print(f"[ok] per-dimension: A~ shared across dims; "
          f"split-before-collapse gap={gap:.1e}")


def test_nonproductive_diverges():
    """rho >= 1 must be reported as divergence, not hang."""
    econ = generate_base(40, density=0.1, joint_frac=0.5, target_rho=1.2,
                         theta_alpha=1.0, seed=3)
    A_tilde, c = build_forward(econ)
    rho = spectral_radius(A_tilde)
    p, iters, conv, rate = solve_iteration(A_tilde, c, maxit=5000)
    assert rho > 1.0, f"expected rho>1, got {rho}"
    assert not conv, "non-productive economy should not converge"
    print(f"[ok] non-productive: rho={rho:.3f} -> diverged in {iters} iters (correct)")


def run_tests():
    test_2x2_hand()
    test_steedman_contrast()
    test_per_dimension()
    test_nonproductive_diverges()
    print("\nAll self-tests passed.")


# ---------------------------------------------------------------------------
# Summary of a completed sweep
# ---------------------------------------------------------------------------

def summarise(rows):
    base = [r for r in rows if r["kind"] == "base"]
    sq = [r for r in rows if r["kind"] == "square_joint"]
    prod = [r for r in base + sq if r["rho"] < 1.0]
    nonprod = [r for r in base if r["rho"] >= 1.0]

    print("\n" + "=" * 68)
    print("SWEEP SUMMARY")
    print("=" * 68)
    print(f"total runs                : {len(rows)}")
    print(f"  base (Aequitas)         : {len(base)}")
    print(f"  square-joint (+ value)  : {len(sq)}")

    conv = [r for r in prod if r["converged"]]
    print(f"\nproductive economies (rho<1): {len(prod)}")
    print(f"  converged               : {len(conv)}  "
          f"({100*len(conv)/max(1,len(prod)):.1f}%)")
    neg = [r for r in prod if np.isfinite(r["min_p"]) and r["min_p"] < -1e-9]
    print(f"  Aequitas min(p) < 0     : {len(neg)}   <-- must be 0")
    if prod:
        worst = min(prod, key=lambda r: r["min_p"] if np.isfinite(r["min_p"]) else 0)
        print(f"  most-negative min(p)    : {worst['min_p']:.3e}")
    gaps = [r["direct_gap"] for r in prod if np.isfinite(r["direct_gap"])]
    if gaps:
        print(f"  max |iter - direct|     : {max(gaps):.2e}")

    print(f"\nnon-productive economies (rho>=1): {len(nonprod)}")
    still = [r for r in nonprod if r["converged"]]
    print(f"  wrongly 'converged'     : {len(still)}   <-- must be 0")

    if sq:
        vv = [r for r in sq if r.get("value_invertible")]
        vneg = [r for r in vv if r.get("value_negative")]
        aneg = [r for r in sq if np.isfinite(r["min_p"]) and r["min_p"] < -1e-9]
        print("\nvalue-allocation (Steedman) arm, square-joint economies:")
        print(f"  invertible              : {len(vv)}/{len(sq)}")
        print(f"  value min(v) < 0        : {len(vneg)}  "
              f"({100*len(vneg)/max(1,len(vv)):.1f}% of invertible)")
        print(f"  Aequitas min(p) < 0     : {len(aneg)}   <-- must be 0")

    # timing at the largest size
    big = max((r["M"] for r in base), default=0)
    bigrows = [r for r in base if r["M"] == big and r["rho"] < 1.0]
    if bigrows:
        tmax = max(r["t_iter"] for r in bigrows)
        print(f"\ntractability: M={big}, worst iterate-solve = {tmax:.3f}s")

    print("=" * 68)

    verdict_ok = (len(neg) == 0 and len(still) == 0
                  and (not sq or len(aneg) == 0))
    if verdict_ok:
        print("VERDICT: PASS -- Aequitas allocation converges and stays "
              "non-negative for every rho<1;")
        print("         value allocation goes negative where Aequitas does not.")
    else:
        print("VERDICT: FAIL -- a counterexample appeared. Inspect the CSV. "
              "Do NOT proceed to C3.")
    print("=" * 68)
    return verdict_ok


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true", help="run self-tests only")
    ap.add_argument("--quick", action="store_true", help="small fast sweep")
    ap.add_argument("--seeds", type=int, default=None, help="seeds per sweep cell")
    ap.add_argument("--density", type=float, default=0.05)
    ap.add_argument("--out", default="results.csv")
    ap.add_argument("--noplot", action="store_true")
    ap.add_argument("--replot", action="store_true",
                    help="rebuild plots + summary from an existing CSV")
    args = ap.parse_args()

    if args.test:
        run_tests()
        return

    if args.replot:
        rows = _read_csv(args.out)
        summarise(rows)
        make_plots(rows, args.out.replace(".csv", ""))
        print(f"Replotted from {args.out}.")
        return

    print("Running self-tests first...\n")
    run_tests()
    print()

    if args.quick:
        sizes = [10, 50, 200]
        seeds = args.seeds or 5
    else:
        sizes = [10, 100, 1000, 10_000]
        seeds = args.seeds or 30

    print(f"Sweep: sizes={sizes}, seeds/cell={seeds}, density={args.density}")
    t0 = time.perf_counter()
    rows = run_sweep(sizes, seeds, args.density, args.out, quick=args.quick)
    print(f"Sweep done in {time.perf_counter()-t0:.1f}s -> {args.out} ({len(rows)} rows)")

    ok = summarise(rows)
    if not args.noplot:
        try:
            make_plots(rows, args.out.replace(".csv", ""))
            print(f"Plots written with prefix '{args.out.replace('.csv','')}'.")
        except Exception as e:
            print(f"(plotting skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
