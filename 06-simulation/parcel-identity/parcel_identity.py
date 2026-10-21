"""
Parcel identity -- what happens to a joint process's books when the flow sheet
cannot say whether two readings name one parcel or two?

Answers sim request sr-20260905-how-often-does-a-joint-process-flow-sheet-fa
(SB-05, from @custos c42203). Foundations §3.4a, conformance rows 10c, 10e.

THE MODEL
  A GROUP is a set of readings that a flow sheet could confuse. Two kinds:
    shared -- one true parcel, read by m paths (m-1 links to the first reading)
    twin   -- two true parcels of equal quantity, one reader each (1 link)
  Each link is UNRESOLVED with probability p (the rate `u`, or a size-weighted
  version of it). A resolved link is read correctly. An unresolved link is
  read by the policy:
    naive -- counts every reading (the defect of row 10e; reported for scale)
    P1    -- assume distinct   (an unresolved shared link counts again)
    P2    -- assume same       (an unresolved twin link is merged away)
    P3    -- refuse            (`not identified` if any link in the walk is open)
    P4    -- the rule now in row 10e: publish the resolved union and report the
             unresolved parcels under row 7. Read here as the interval [P2, P1].

  Truth T counts each true parcel once. Overstatement = books / T.

Run:  python parcel_identity.py --test
      python parcel_identity.py            # full run, writes parcel_identity.csv
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import os
import sys
from dataclasses import dataclass

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "chain-resolution"))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "allocation-engine"))

import chain_resolution as cr  # noqa: E402

SEED = 20261018
TRIALS = 4000
U_GRID = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]


@dataclass
class Group:
    q: float                 # quantity of ONE true parcel (energy, MJ)
    readers: tuple           # products that read it
    kind: str = "shared"     # "shared" or "twin"


# ---------------------------------------------------------------------------
# Building groups from the project's own chains
# ---------------------------------------------------------------------------


def groups_from_chain(chain: cr.Chain, dim: str = "energy_mj") -> list[Group]:
    out = []
    for s in chain.steps:
        q = getattr(s, dim)
        readers = tuple(p for p in chain.products if s.name in chain.passes[p])
        if q > 0 and readers:
            out.append(Group(q=q, readers=readers))
    return out


def add_twins(groups: list[Group], products: list[str], k: int,
              rng: np.random.Generator) -> list[Group]:
    """k hypothetical twin pairs. Quantity is resampled from the case's own
    parcel quantities, readers are two distinct random products."""
    qs = [g.q for g in groups if g.kind == "shared"]
    out = list(groups)
    for _ in range(k):
        a, b = rng.choice(len(products), size=2, replace=False)
        out.append(Group(q=float(rng.choice(qs)),
                         readers=(products[a], products[b]), kind="twin"))
    return out


# ---------------------------------------------------------------------------
# The walk for one holding, as arrays
# ---------------------------------------------------------------------------


def holding_arrays(groups: list[Group], holding: frozenset):
    """Per group touched by the holding: quantity, links, kind flag.

    Returns q, n_links, is_twin. A twin with only one reader in the holding has
    no link and is not ambiguous (n_links = 0)."""
    q, n, tw = [], [], []
    for g in groups:
        m = sum(1 for r in g.readers if r in holding)
        if m == 0:
            continue
        q.append(g.q)
        n.append(m - 1)
        tw.append(g.kind == "twin")
    return np.array(q, float), np.array(n, int), np.array(tw, bool)


def exact(q, n, tw):
    """Truth, naive and the resolved figure at u = 0, with no randomness."""
    truth = float(q.sum() + (q * n)[tw].sum())
    naive = float((q * (n + 1)).sum())
    return truth, naive


def link_probs(q, n, tw, u, mode):
    """Per-group unresolved probability, with a link-weighted mean of u.

    mode: "flat"      every link has probability u
          "big_dark"  weight proportional to quantity (big parcels undocumented)
          "small_dark" weight proportional to 1/quantity (small ones undocumented)
    Probabilities clip at 1, so the realised mean can fall below u; the
    realised mean is returned so it is reported rather than assumed."""
    if mode == "flat":
        p = np.full(len(q), u)
    else:
        w = q if mode == "big_dark" else 1.0 / q
        links = n.astype(float)
        if links.sum() == 0:
            return np.full(len(q), u), u
        wbar = (w * links).sum() / links.sum()
        p = np.minimum(1.0, u * w / wbar)
    links = n.astype(float)
    realised = float((p * links).sum() / links.sum()) if links.sum() else u
    return p, realised


def simulate(q, n, tw, u, mode, trials, rng):
    """Monte Carlo over which links are unresolved. Returns per-trial arrays."""
    truth, naive = exact(q, n, tw)
    p, realised = link_probs(q, n, tw, u, mode)
    # U[t, g] = number of unresolved links of group g in trial t
    U = rng.binomial(n[None, :], p[None, :], size=(trials, len(q)))
    base = q.sum()
    # shared: P1 counts every unresolved link again, P2 never does.
    # twin:   P1 always counts the second reading (right), P2 only if resolved.
    p1 = base + (q * U)[:, ~tw].sum(axis=1) + (q * n)[tw].sum()
    p2 = base + (q * (n - U))[:, tw].sum(axis=1)
    refuse = (U > 0).any(axis=1)
    return {"truth": truth, "naive": naive, "p1": p1, "p2": p2,
            "refuse": refuse, "realised_u": realised}


def summarise(r):
    T = r["truth"]
    o1, o2 = r["p1"] / T, r["p2"] / T
    return {
        "p1_mean": o1.mean(), "p1_sd": o1.std(), "p1_p95": np.quantile(o1, .95),
        "p1_max": o1.max(),
        "p2_mean": o2.mean(), "p2_sd": o2.std(), "p2_min": o2.min(),
        "p3_unreportable": r["refuse"].mean(),
        "naive": r["naive"] / T,
        "p4_width": (r["p1"] / r["p2"]).mean(),
        "p1_abs_err": np.abs(r["p1"] - T).mean(),
        "p2_abs_err": np.abs(r["p2"] - T).mean(),
        "realised_u": r["realised_u"],
    }


# ---------------------------------------------------------------------------
# The cases
# ---------------------------------------------------------------------------


def cases():
    return {"refinery": cr.build_refinery(), "steer": cr.build_steer()}


def analytic_p1(q, n, tw, u):
    """Closed form for the mean P1 overstatement with flat u and no twins."""
    truth, _ = exact(q, n, tw)
    return 1.0 + u * float((q * n)[~tw].sum()) / truth


def analytic_unreportable(n, u):
    return 1.0 - (1.0 - u) ** int(n.sum())


# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------


def experiment_sweep(rng):
    rows = []
    for name, ch in cases().items():
        groups = groups_from_chain(ch)
        full = frozenset(ch.products)
        q, n, tw = holding_arrays(groups, full)
        for u in U_GRID:
            s = summarise(simulate(q, n, tw, u, "flat", TRIALS, rng))
            rows.append({"experiment": "sweep_full_holding", "case": name,
                         "mode": "flat", "u": u, **s})
    return rows


def experiment_holding_size(rng):
    """P3 unreportable share against the number of co-products held."""
    rows = []
    ch = cr.build_refinery()
    groups = groups_from_chain(ch)
    for k in range(1, len(ch.products) + 1):
        for u in (0.05, 0.10, 0.20, 0.50):
            shares, p1s, links = [], [], []
            for combo in itertools.combinations(ch.products, k):
                q, n, tw = holding_arrays(groups, frozenset(combo))
                r = simulate(q, n, tw, u, "flat", 1500, rng)
                shares.append(r["refuse"].mean())
                p1s.append((r["p1"] / r["truth"]).mean())
                links.append(int(n.sum()))
            rows.append({"experiment": "holding_size", "case": "refinery",
                         "k": k, "u": u, "holdings": len(shares),
                         "p3_unreportable_mean": float(np.mean(shares)),
                         "p3_unreportable_min": float(np.min(shares)),
                         "p3_unreportable_max": float(np.max(shares)),
                         "p1_mean": float(np.mean(p1s)),
                         "links_mean": float(np.mean(links))})
    return rows


def experiment_size_correlation(rng):
    rows = []
    ch = cr.build_refinery()
    groups = groups_from_chain(ch)
    q, n, tw = holding_arrays(groups, frozenset(ch.products))
    for u in (0.05, 0.10, 0.20, 0.30):
        base = None
        for mode in ("flat", "big_dark", "small_dark"):
            r = simulate(q, n, tw, u, mode, TRIALS * 2, rng)
            s = summarise(r)
            excess = s["p1_mean"] - 1.0
            if mode == "flat":
                base = excess
            rows.append({"experiment": "size_correlation", "case": "refinery",
                         "mode": mode, "u": u, "realised_u": s["realised_u"],
                         "p1_mean": s["p1_mean"], "p1_excess": excess,
                         "excess_vs_flat": excess / base if base else float("nan"),
                         "p3_unreportable": s["p3_unreportable"]})
    return rows


def experiment_twin_crossover(rng):
    """Add K twin pairs; find where P2's absolute error passes P1's."""
    rows = []
    ch = cr.build_refinery()
    base_groups = groups_from_chain(ch)
    q0, n0, tw0 = holding_arrays(base_groups, frozenset(ch.products))
    shared_links = int(n0.sum())
    for u in (0.1, 0.3):
        for k in (0, 2, 5, 10, 15, 20, 25, 30, 40, 60, 100):
            rr = np.random.default_rng(SEED + k)       # same twins at each u
            groups = add_twins(base_groups, ch.products, k, rr)
            q, n, tw = holding_arrays(groups, frozenset(ch.products))
            s = summarise(simulate(q, n, tw, u, "flat", TRIALS, rng))
            t = k / (shared_links + k)
            rows.append({"experiment": "twin_crossover", "case": "refinery",
                         "u": u, "twin_pairs": k, "twin_share_of_links": t,
                         "twin_share_of_quantity":
                             float(q[tw].sum() * 2 / (q.sum() + q[tw].sum())) if k else 0.0,
                         "p1_mean": s["p1_mean"], "p2_mean": s["p2_mean"],
                         "p1_abs_err": s["p1_abs_err"], "p2_abs_err": s["p2_abs_err"],
                         "p2_worse": s["p2_abs_err"] > s["p1_abs_err"]})
    return rows


def crossover_estimate(rows, u):
    """Linear interpolation of the twin share at which p2_abs_err = p1_abs_err."""
    pts = [(r["twin_share_of_links"], r["p2_abs_err"] - r["p1_abs_err"])
           for r in rows if r["u"] == u]
    pts.sort()
    for (t0, d0), (t1, d1) in zip(pts, pts[1:]):
        if d0 <= 0 < d1:
            return t0 + (t1 - t0) * (-d0) / (d1 - d0)
    return None


def experiment_synthetic(rng, n_chains=2000):
    """Exploratory: random chains, closed form (no Monte Carlo needed).

    Slope = sum q(m-1) / sum q over parcels. u50 = u at which P3 refuses half
    the full-holding figures."""
    slopes, u50s, links = [], [], []
    for _ in range(n_chains):
        S = int(rng.integers(6, 13))
        P = int(rng.integers(3, 9))
        q = rng.lognormal(0.0, 1.0, size=S)
        reach = rng.random((S, P)) < 0.5
        reach[0, :] = True                       # everything starts in step 0
        for p in range(P):                       # every product reads something
            if not reach[:, p].any():
                reach[rng.integers(0, S), p] = True
        m = reach.sum(axis=1)
        keep = m > 0
        q, m = q[keep], m[keep]
        slopes.append(float((q * (m - 1)).sum() / q.sum()))
        L = int((m - 1).sum())
        links.append(L)
        u50s.append(1 - 0.5 ** (1 / L) if L else float("nan"))
    a = lambda x: np.array(x, float)
    return {"chains": n_chains,
            "slope_mean": float(np.mean(slopes)),
            "slope_p5": float(np.quantile(slopes, .05)),
            "slope_p95": float(np.quantile(slopes, .95)),
            "u50_median": float(np.nanmedian(u50s)),
            "u50_p5": float(np.nanquantile(a(u50s), .05)),
            "u50_p95": float(np.nanquantile(a(u50s), .95)),
            "links_median": float(np.median(links))}


# ---------------------------------------------------------------------------
# Self-tests -- each able to fail
# ---------------------------------------------------------------------------


def _refinery():
    ch = cr.build_refinery()
    g = groups_from_chain(ch)
    return ch, g, holding_arrays(g, frozenset(ch.products))


def test_zero_rate_is_exact():
    ch, g, (q, n, tw) = _refinery()
    rng = np.random.default_rng(1)
    twg = add_twins(g, ch.products, 10, np.random.default_rng(2))
    for gg in (g, twg):
        qq, nn, tt = holding_arrays(gg, frozenset(ch.products))
        r = simulate(qq, nn, tt, 0.0, "flat", 200, rng)
        T = r["truth"]
        assert np.allclose(r["p1"], T) and np.allclose(r["p2"], T), "u=0 not exact"
        assert not r["refuse"].any(), "P3 refused at u=0"
    return "u = 0: P1 = P2 = truth in every trial, P3 never refuses (with and without twins)"


def test_ties_to_chain_resolution():
    ch, g, (q, n, tw) = _refinery()
    finest = [(i, i + 1) for i in range(len(ch.steps))]
    union = cr.buyer_union(ch, ch.products, finest)["energy_mj"]
    naive = cr.buyer_naive_sum(ch, ch.products, finest)["energy_mj"]
    truth, nv = exact(q, n, tw)
    assert abs(truth - union) < 1e-6, f"truth {truth} != chain-resolution union {union}"
    assert abs(nv - naive) < 1e-6, f"naive {nv} != chain-resolution sum {naive}"
    assert int(n.max()) + 1 == 7, "worst parcel should be read by 7 paths (7.00x)"
    return (f"truth = chain_resolution union ({union:,.0f}); naive = its sum "
            f"({naive:,.0f}, {naive/union:.3f}x); worst parcel read 7 times")


def test_policy_order_with_twins():
    ch, g, _ = _refinery()
    rng = np.random.default_rng(3)
    gg = add_twins(g, ch.products, 30, np.random.default_rng(4))
    q, n, tw = holding_arrays(gg, frozenset(ch.products))
    r = simulate(q, n, tw, 0.4, "flat", 3000, rng)
    T = r["truth"]
    assert (r["p2"] <= T + 1e-9).all(), "P2 overstated -- policies swapped"
    assert r["p2"].min() < T - 1e-6, "P2 never understated -- twins inert"
    shared_only = simulate(*holding_arrays(g, frozenset(ch.products)), 0.4, "flat", 3000, rng)
    assert (shared_only["p1"] >= shared_only["truth"] - 1e-9).all(), "P1 understated"
    assert shared_only["p1"].max() > shared_only["truth"] * 1.2, "P1 never overstated"
    return "P2 <= truth <= P1 per trial, and each actually departs from truth"


def test_matches_analytic():
    ch, g, (q, n, tw) = _refinery()
    rng = np.random.default_rng(5)
    for u in (0.1, 0.5):
        r = simulate(q, n, tw, u, "flat", 20000, rng)
        o = r["p1"] / r["truth"]
        se = o.std() / math.sqrt(len(o))
        want = analytic_p1(q, n, tw, u)
        assert abs(o.mean() - want) < 4 * se, f"u={u}: sim {o.mean():.4f} vs {want:.4f}"
        sh = r["refuse"].mean()
        wu = analytic_unreportable(n, u)
        assert abs(sh - wu) < 4 * math.sqrt(wu * (1 - wu) / len(o)) + 1e-9, (
            f"u={u}: refuse {sh:.4f} vs {wu:.4f}")
    return "MC mean P1 and P3 refusal match closed forms at u = 0.1 and 0.5 (4 s.e.)"


def test_full_unresolved_equals_naive():
    ch, g, (q, n, tw) = _refinery()
    r = simulate(q, n, tw, 1.0, "flat", 50, np.random.default_rng(6))
    assert np.allclose(r["p1"], r["naive"]), "P1 at u=1 should equal the naive sum"
    assert np.allclose(r["p2"], r["truth"]), "P2 at u=1 with no twins should equal truth"
    return "u = 1, no twins: P1 = naive sum, P2 = truth (the sweep's two ends)"


def test_scale_invariance():
    ch, g, (q, n, tw) = _refinery()
    a = simulate(q, n, tw, 0.3, "flat", 500, np.random.default_rng(7))
    b = simulate(q * 37.0, n, tw, 0.3, "flat", 500, np.random.default_rng(7))
    assert np.allclose(a["p1"] / a["truth"], b["p1"] / b["truth"]), "ratio moved with scale"
    assert np.allclose(b["p1"], 37.0 * a["p1"]), "figure did not scale"
    return "scaling every quantity by 37 scales every figure and leaves every ratio alone"


def test_single_product_needs_no_identity():
    ch, g, _ = _refinery()
    for p in ch.products:
        q, n, tw = holding_arrays(g, frozenset([p]))
        assert n.sum() == 0, f"{p}: a single path has a link"
    return "no single co-product's figure involves a link (nothing to be unresolved)"


def test_closure():
    ch, g, _ = _refinery()
    for gg in g:
        assert set(gg.readers) <= set(ch.products), "reader outside the process"
    return "every group's readers are products of the process"


def test_size_weighting_bites_and_is_reported():
    ch, g, (q, n, tw) = _refinery()
    rng = np.random.default_rng(8)
    flat = simulate(q, n, tw, 0.05, "flat", 20000, rng)
    big = simulate(q, n, tw, 0.05, "big_dark", 20000, rng)
    small = simulate(q, n, tw, 0.05, "small_dark", 20000, rng)
    ef, eb, es = (x["p1"].mean() / x["truth"] - 1 for x in (flat, big, small))
    assert eb > ef > es, f"order wrong: big {eb:.4f}, flat {ef:.4f}, small {es:.4f}"
    assert abs(big["realised_u"] - 0.05) < 1e-9 and abs(small["realised_u"] - 0.05) < 1e-9, (
        "unclipped realised rate should equal u")
    return "size-weighting changes P1 in the expected order and keeps the link-mean rate at u"


TESTS = [test_zero_rate_is_exact, test_ties_to_chain_resolution,
         test_policy_order_with_twins, test_matches_analytic,
         test_full_unresolved_equals_naive, test_scale_invariance,
         test_single_product_needs_no_identity, test_closure,
         test_size_weighting_bites_and_is_reported]


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
# Main
# ---------------------------------------------------------------------------


def fmt(x):
    return f"{x:.3f}" if isinstance(x, float) else str(x)


def show(rows, cols):
    print("  " + "".join(f"{c:>16}" for c in cols))
    for r in rows:
        print("  " + "".join(f"{fmt(r[c]):>16}" for c in cols))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--csv", default=os.path.join(_HERE, "parcel_identity.csv"))
    a = ap.parse_args()
    if a.test:
        sys.exit(1 if run_tests() else 0)

    rng = np.random.default_rng(SEED)
    out = []

    print("\n1. SWEEP, one buyer holding every co-product (flat u)")
    sw = experiment_sweep(rng)
    out += sw
    for case in ("refinery", "steer"):
        print(f"\n  {case}")
        show([r for r in sw if r["case"] == case],
             ["u", "naive", "p1_mean", "p1_sd", "p1_p95", "p1_max", "p2_mean",
              "p3_unreportable", "p4_width"])

    print("\n2. P3 unreportable share by number of co-products held (refinery, all combinations)")
    hs = experiment_holding_size(rng)
    out += hs
    show([r for r in hs if r["u"] in (0.05, 0.10, 0.20)],
         ["k", "u", "holdings", "links_mean", "p3_unreportable_mean",
          "p3_unreportable_min", "p3_unreportable_max", "p1_mean"])

    print("\n3. SIZE-CORRELATED RESOLUTION (refinery, full holding)")
    sc = experiment_size_correlation(rng)
    out += sc
    show(sc, ["mode", "u", "realised_u", "p1_mean", "p1_excess", "excess_vs_flat",
              "p3_unreportable"])

    print("\n4. TWIN CROSSOVER (refinery + hypothetical twin pairs)")
    tc = experiment_twin_crossover(rng)
    out += tc
    show(tc, ["u", "twin_pairs", "twin_share_of_links", "twin_share_of_quantity",
              "p1_mean", "p2_mean", "p1_abs_err", "p2_abs_err"])
    for u in (0.1, 0.3):
        print(f"  crossover twin share at u = {u}: {crossover_estimate(tc, u)}")

    print("\n5. SYNTHETIC CHAINS (exploratory, closed form)")
    syn = experiment_synthetic(np.random.default_rng(SEED + 1))
    for k, v in syn.items():
        print(f"  {k:>14}: {fmt(v)}")
    out.append({"experiment": "synthetic", **syn})

    keys = sorted({k for r in out for k in r})
    with open(a.csv, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=keys)
        w.writeheader()
        w.writerows(out)
    print(f"\n  wrote {a.csv} ({len(out)} rows)")
    sys.exit(1 if run_tests() else 0)


if __name__ == "__main__":
    main()
