"""Does labelling a published figure "metered" or "modelled" pay, or does it hand rivals a target?

Answers SB-04 / sr-20260904-does-a-producer-who-labels-each-published-fi.
Run from this folder:  python labelling_game.py --test   |   python labelling_game.py

One good, N producers, one round repeated. Each producer is Labelled (L) or Unlabelled (U).
  shares   : demand splits in inverse proportion to the effective figure; U is discounted by (1+d).
  attack   : each rival may spend a to challenge ONE producer. It aims at the type with the
             higher expected prize q_T*g*s_T and attacks only if that prize exceeds a.
             A success moves g of the target's remaining endowment to the attacker.
  payoff   : final trade share minus attack costs paid.
q_L = q*m (the label exposes the modelled share m), q_U = (q/ratio)*m.  a = alpha*g/N.
"""
import argparse
import json
import math
import sys
from dataclasses import dataclass, replace

import numpy as np

SEED = 20261017


@dataclass(frozen=True)
class P:
    N: int = 20
    d: float = 0.15
    m: float = 0.4
    q: float = 0.3
    ratio: float = 6.0      # q / q'
    g: float = 0.2
    alpha: float = 0.05     # attack cost a = alpha*g/N ; alpha=0 is the free-attack artefact
    c: float = 0.0          # share of rivals who collude and never attack
    target: str = "value"   # "value": aim at the best prize ; "uniform": aim blind


def shares(p, nL):
    nU = p.N - nL
    sL = 1.0 / (nL + nU / (1.0 + p.d))
    return (sL, sL / (1.0 + p.d))


def qtypes(p):
    return (min(1.0, p.q * p.m), min(1.0, p.q / p.ratio * p.m))


def atk_cost(p):
    return p.alpha * p.g / p.N


def attack_plan(p, nL):
    """plan[X][T] = probability an attacker of type X aims at type T (rest: does not attack)."""
    n = (nL, p.N - nL)
    s = shares(p, nL)
    q = qtypes(p)
    v = [q[T] * p.g * s[T] for T in (0, 1)]
    a = atk_cost(p)
    plan = {}
    for X in (0, 1):
        elig = [n[T] - (1 if T == X else 0) for T in (0, 1)]
        pr = [0.0, 0.0]
        if sum(elig) > 0:
            if p.target == "value":
                cand = [T for T in (0, 1) if elig[T] > 0]
                best = max(v[T] for T in cand)
                tied = [T for T in cand if v[T] >= best - 1e-12 * max(best, 1e-300)]
                tot = sum(elig[T] for T in tied)
                if best > a:
                    for T in tied:
                        pr[T] = elig[T] / tot
            else:
                tot = sum(elig)
                probs = [elig[T] / tot for T in (0, 1)]
                if sum(probs[T] * v[T] for T in (0, 1)) > a:
                    pr = probs
        plan[X] = pr
    return plan


def expected_payoffs(p, nL):
    """Exact expectation of the round (see README for the derivation). Returns (payL, payU, total_cost)."""
    N = p.N
    n = (nL, N - nL)
    s = shares(p, nL)
    q = qtypes(p)
    a = atk_cost(p)
    plan = attack_plan(p, nL)
    F = [[(1 - p.c) * n[X] * plan[X][T] for T in (0, 1)] for X in (0, 1)]
    surv, A, B = [1.0, 1.0], [0.0, 0.0], [0.0, 0.0]
    for T in (0, 1):
        if n[T] == 0:
            continue
        sv = 1.0
        for X in (0, 1):
            f = F[X][T]
            if f <= 0:
                continue
            if X == T:
                if n[T] < 2:
                    continue
                sv *= (1 - p.g * q[T] / (n[T] - 1)) ** (f * (n[T] - 1) / n[T])
            else:
                sv *= (1 - p.g * q[T] / n[T]) ** f
        surv[T] = sv
        A[T] = F[0][T] + F[1][T]
        B[T] = n[T] * s[T] * (1 - sv)
    pay, cost = [float("nan")] * 2, 0.0
    for X in (0, 1):
        if n[X] == 0:
            continue
        booty = sum(plan[X][T] * B[T] / A[T] for T in (0, 1) if plan[X][T] > 0 and A[T] > 0)
        atk = sum(plan[X])
        pay[X] = s[X] * surv[X] + (1 - p.c) * (booty - a * atk)
        cost += n[X] * (1 - p.c) * a * atk
    return pay[0], pay[1], cost


def simulate(p, nL, R, rng, fixed_order=False):
    """Monte Carlo of the same round, R independent rounds. Returns dict of arrays."""
    N = p.N
    types = np.array([0] * nL + [1] * (N - nL))
    sL, sU = shares(p, nL)
    endow = np.tile(np.where(types == 0, sL, sU), (R, 1))
    booty = np.zeros((R, N))
    cost = np.zeros((R, N))
    colluder = rng.random((R, N)) < p.c
    order = np.tile(np.arange(N), (R, 1)) if fixed_order else np.argsort(rng.random((R, N)), axis=1)
    plan = attack_plan(p, nL)
    pr0 = np.array([plan[0][0], plan[1][0]])
    pr1 = np.array([plan[0][1], plan[1][1]])
    q = np.array(qtypes(p))
    a = atk_cost(p)
    nT = np.array([nL, N - nL])
    off = np.array([0, nL])
    rows = np.arange(R)
    for k in range(N):
        j = order[:, k]
        X = types[j]
        u = rng.random(R)
        tgtT = np.where(u < pr0[X], 0, np.where(u < pr0[X] + pr1[X], 1, -1))
        act = (tgtT >= 0) & ~colluder[rows, j]
        T = np.where(tgtT >= 0, tgtT, 0)
        selfin = X == T
        cnt = np.maximum(nT[T] - selfin.astype(int), 1)
        r = (rng.random(R) * cnt).astype(int)
        r = np.where(selfin & (r >= j - off[T]), r + 1, r)
        tgt = np.minimum(off[T] + r, N - 1)
        succ = act & (rng.random(R) < q[T])
        amt = np.where(succ, p.g * endow[rows, tgt], 0.0)
        endow[rows, tgt] -= amt
        booty[rows, j] += amt
        cost[rows, j] += np.where(act, a, 0.0)
    final = endow + booty - cost
    return {"final": final, "gross": endow + booty, "types": types}


def type_means(sim):
    f, t = sim["final"], sim["types"]
    out = []
    for T in (0, 1):
        if (t == T).any():
            x = f[:, t == T].mean(axis=1)
            out.append((float(x.mean()), float(x.std(ddof=1) / math.sqrt(len(x)))))
        else:
            out.append((float("nan"), float("nan")))
    return out


def delta_curve(p):
    """Delta(nL) = payoff(L) - payoff(U) for nL = 1..N-1 (both types present)."""
    return np.array([(lambda r: r[0] - r[1])(expected_payoffs(p, k)) for k in range(1, p.N)])


def attack_active(p):
    return any(attack_plan(p, k)[X][0] > 0 for k in range(1, p.N) for X in (0, 1))


def final_nL(p, curve, start=None):
    nL = p.N // 2 if start is None else start
    for _ in range(4 * p.N):
        if nL <= 0 or nL >= p.N:
            break
        dl = curve[nL - 1]
        if dl > 1e-15:
            nL += 1
        elif dl < -1e-15:
            nL -= 1
        else:
            break
    return nL


def classify(curve):
    lo, hi = curve[0], curve[-1]          # lone labeller ; lone deviant from all-labelled
    if lo > 0 and hi > 0 and (curve > 0).all():
        return "label-wins"
    if lo < 0 and hi < 0 and (curve < 0).all():
        return "label-collapses"
    if lo < 0 < hi:
        return "bistable"                  # stable once established, cannot invade
    if lo > 0 > hi:
        return "mixed"
    return "other"


def dstar(p, which, dmax=3.0, step=0.0025):
    """Smallest d at which Delta>0 : which='stay' (Delta at nL=N-1) or 'invade' (nL=1). nan if never."""
    k = p.N - 1 if which == "stay" else 1
    f = lambda d: (lambda r: r[0] - r[1])(expected_payoffs(replace(p, d=d), k))
    d_prev, f_prev = 0.0, f(0.0)
    if f_prev > 1e-15:
        return 0.0
    d = step
    while d <= dmax + 1e-12:
        fd = f(d)
        if fd > 1e-15:
            lo, hi = d_prev, d
            for _ in range(40):
                mid = 0.5 * (lo + hi)
                if f(mid) > 1e-15:
                    hi = mid
                else:
                    lo = mid
            return hi
        d_prev, d = d, d + step
    return float("nan")


# ----------------------------------------------------------------------------- self-tests
def run_tests():
    rng = np.random.default_rng(SEED)
    results = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok), detail))
        print(("PASS  " if ok else "FAIL  ") + name + ("  | " + detail if detail else ""))

    # T1 d=0: labelling can only lose (SB-04 test 1). Attack-active parameter draws only.
    worst, n_active = -1.0, 0
    for _ in range(300):
        pp = P(N=int(rng.integers(4, 30)), d=0.0, m=rng.uniform(0.1, 0.9), q=rng.uniform(0.1, 0.6),
               ratio=rng.choice([2.0, 6.0, 12.0]), g=rng.uniform(0.05, 0.4), alpha=rng.uniform(0.0, 0.1))
        cv = delta_curve(pp)
        worst = max(worst, cv.max())
        n_active += attack_active(pp)
    check("T1 d=0 -> Delta<=0 everywhere", worst <= 1e-12 and n_active > 100,
          f"max Delta={worst:.2e}, attack-active draws={n_active}/300")

    # T2 q=q' with blind targeting: attack does not discriminate -> labelling wins whenever d>0 (SB-04 test 2)
    bad = 0
    for _ in range(300):
        pp = P(N=int(rng.integers(4, 30)), d=rng.uniform(0.01, 0.5), m=rng.uniform(0.1, 0.9), q=rng.uniform(0.1, 0.6),
               ratio=1.0, g=rng.uniform(0.05, 0.4), alpha=rng.uniform(0.0, 0.05), target="uniform")
        bad += int((delta_curve(pp) <= 0).any())
    check("T2 q=q', blind targeting, d>0 -> labelling wins", bad == 0, f"violations={bad}/300")

    # T3 m=0: label exposes nothing -> Delta>0 for d>0, no attack happens
    bad = 0
    for _ in range(100):
        pp = P(N=int(rng.integers(4, 30)), d=rng.uniform(0.01, 0.5), m=0.0, q=rng.uniform(0.1, 0.6),
               g=rng.uniform(0.05, 0.4), alpha=0.0)
        bad += int((delta_curve(pp) <= 0).any() or attack_active(pp))
    check("T3 m=0 -> labelling wins, no attacks", bad == 0, f"violations={bad}/100")

    # T4 shares sum to 1 every round (MC), and the analytic payoffs + costs sum to 1
    pp = P(N=12, c=0.25)
    sim = simulate(pp, 5, 4000, rng)
    dev = float(np.abs(sim["gross"].sum(axis=1) - 1.0).max())
    pL, pU, cost = expected_payoffs(pp, 5)
    tot = 5 * pL + 7 * pU + cost
    check("T4 shares sum to 1", dev < 1e-12 and abs(tot - 1.0) < 1e-12, f"MC max dev={dev:.1e}, analytic total={tot:.12f}")

    # T5 two identical producers with identical choices split equally; and the test CAN fail
    pp = P(N=4, d=0.15, m=1.0, q=0.6, g=0.4, alpha=0.0)
    ok_sim = simulate(pp, 4, 200000, rng)["final"]
    diff = ok_sim[:, 0] - ok_sim[:, 3]
    z_ok = abs(diff.mean()) / (diff.std(ddof=1) / math.sqrt(len(diff)))
    bad_sim = simulate(pp, 4, 200000, rng, fixed_order=True)["final"]
    diff2 = bad_sim[:, 0] - bad_sim[:, 3]
    z_bad = abs(diff2.mean()) / (diff2.std(ddof=1) / math.sqrt(len(diff2)))
    check("T5 four identical producers: first and last earn the same; fixed attack order is detected", z_ok < 4 and z_bad > 10,
          f"z random order={z_ok:.2f}, z fixed order={z_bad:.1f}")

    # T6 analytic expectation vs Monte Carlo (type means within 4 SE and 0.0003 absolute)
    worst_z, worst_abs = 0.0, 0.0
    for pp, nL in [(P(), 10), (P(), 1), (P(), 19), (P(N=10, g=0.4, q=0.6, m=0.9), 3),
                   (P(c=0.5), 7), (P(alpha=0.0, ratio=1.0, d=0.0), 10), (P(target="uniform"), 8)]:
        pL, pU, _ = expected_payoffs(pp, nL)
        mc = type_means(simulate(pp, nL, 60000, rng))
        for (mu, se), an in zip(mc, (pL, pU)):
            if math.isnan(an):
                continue
            worst_z = max(worst_z, abs(mu - an) / max(se, 1e-12))
            worst_abs = max(worst_abs, abs(mu - an))
    check("T6 analytic == Monte Carlo", worst_z < 4.5 and worst_abs < 3e-4,
          f"worst z={worst_z:.2f}, worst abs gap={worst_abs:.1e}")

    # T7 the brief's worked example, loss-only arithmetic, and the transfer-conserving version
    pp = P(N=2, d=0.15, m=1.0, q=0.3, ratio=6.0, g=0.2, alpha=0.0)
    sL, sU = shares(pp, 1)
    loss_only = (sL - 0.3 * 0.2 * sL, sU - 0.05 * 0.2 * sU)
    pL, pU, _ = expected_payoffs(pp, 1)
    check("T7 brief worked example: 53.5/46.5 and loss-only 50.3/46.0",
          abs(sL - 0.5349) < 5e-4 and abs(loss_only[0] - 0.5028) < 5e-4 and abs(loss_only[1] - 0.4604) < 5e-4,
          f"shares {sL:.4f}/{sU:.4f}, loss-only {loss_only[0]:.4f}/{loss_only[1]:.4f}, transfer-conserving {pL:.4f}/{pU:.4f}")
    check("T7b transfer-conserving example sums to 1 and L still ahead but by less",
          abs(pL + pU - 1.0) < 1e-9 and 0 < (pL - pU) < (sL - sU) - 0.02,
          f"gap {pL - pU:.4f} vs discount-only gap {sL - sU:.4f}")

    # T8 the check has teeth: a deliberately wrong model (attack cost ignored) must disagree with MC
    pp = P(alpha=0.1)
    pL, pU, _ = expected_payoffs(pp, 10)
    mc = type_means(simulate(pp, 10, 60000, rng))
    wrong = expected_payoffs(replace(pp, alpha=0.0), 10)
    gap_right = abs(mc[0][0] - pL)
    gap_wrong = abs(mc[0][0] - wrong[0])
    check("T8 T6's tolerance rejects a wrong model", gap_right < 3e-4 < gap_wrong,
          f"gap right model={gap_right:.1e}, gap wrong model={gap_wrong:.1e}")

    n_fail = sum(1 for _, ok, _ in results if not ok)
    print(f"\n{len(results) - n_fail}/{len(results)} self-tests passed")
    return n_fail == 0


# ----------------------------------------------------------------------------- the run
def p_crit(curve):
    """Smallest labelled share from which labelling grows (first nL with Delta>0), None if never."""
    for i, x in enumerate(curve):
        if x > 1e-15:
            return (i + 1) / (len(curve) + 1)
    return None


def grid_run(N=20):
    ds = [0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]
    ms = [0.1, 0.25, 0.4, 0.6, 0.9]
    qs = [0.05, 0.15, 0.30, 0.45, 0.60]
    ratios = [1.0, 3.0, 6.0, 12.0]
    gs = [0.05, 0.10, 0.20, 0.30, 0.40]
    alphas = [0.02, 0.05, 0.10, 0.20]
    out = {}
    for c in (0.0, 0.5):
        if N != 20 and c != 0.0:
            continue
        cells = []
        for d in ds:
            for m in ms:
                for q in qs:
                    for ratio in ratios:
                        for g in gs:
                            for al in alphas:
                                pp = P(N=N, d=d, m=m, q=q, ratio=ratio, g=g, alpha=al, c=c)
                                cv = delta_curve(pp)
                                act = attack_active(pp)
                                cells.append((d, m, q, ratio, g, al, act, classify(cv),
                                              final_nL(pp, cv) / pp.N, bool(cv[-1] > 0), bool(cv[0] > 0), p_crit(cv)))
        out[c] = cells
    return out


def summarise(cells):
    n = len(cells)
    act = [x for x in cells if x[6] and x[0] > 0]
    def frac(sel, f):
        return (sum(1 for x in sel if f(x)) / len(sel)) if sel else float("nan")
    res = {"cells": n, "active_cells_d>0": len(act)}
    pc = sorted(x[11] for x in act if x[7] == "bistable")
    if pc:
        res["bistable critical mass p_crit (min, q1, median, q3, max)"] = [pc[0], pc[len(pc) // 4], pc[len(pc) // 2],
                                                                           pc[3 * len(pc) // 4], pc[-1]]
    for label, sel in (("all", [x for x in cells if x[0] > 0]), ("attack-active", act)):
        res[label] = {
            "p_final<0.5 from p0=0.5": frac(sel, lambda x: x[8] < 0.5),
            "p_final==0": frac(sel, lambda x: x[8] == 0.0),
            "p_final==1": frac(sel, lambda x: x[8] == 1.0),
            "all-L resists deviant": frac(sel, lambda x: x[9]),
            "lone L can invade": frac(sel, lambda x: x[10]),
            "class": {k: frac(sel, lambda x, k=k: x[7] == k)
                      for k in ("label-wins", "label-collapses", "bistable", "mixed", "other")},
        }
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--out", default="results.json")
    a = ap.parse_args()
    if a.test:
        sys.exit(0 if run_tests() else 1)

    rng = np.random.default_rng(SEED)
    out = {"seed": SEED}
    head = P()
    cv = delta_curve(head)
    out["headline"] = {"params": head.__dict__, "class": classify(cv), "delta_by_nL": [float(x) for x in cv],
                       "final_p_from_0.5": final_nL(head, cv) / head.N,
                       "dstar_stay": dstar(head, "stay"), "dstar_invade": dstar(head, "invade"),
                       "prior_q_g_m": head.q * head.g * head.m}
    mcs = {}
    for k in (1, 5, 10, 15, 19):
        sim = simulate(head, k, 40000, rng)
        mcs[k] = {"mc": type_means(sim), "analytic": expected_payoffs(head, k)[:2], "shares": shares(head, k)}
    out["headline_mc"] = mcs

    out["dstar_vs_ratio"] = {str(r): {"stay": dstar(replace(head, ratio=r), "stay"),
                                      "invade": dstar(replace(head, ratio=r), "invade"),
                                      "classify@d=.15": classify(delta_curve(replace(head, ratio=r)))}
                             for r in (1.0, 2.0, 3.0, 6.0, 12.0, 24.0)}
    out["dstar_vs_N"] = {str(n): {"stay": dstar(replace(head, N=n), "stay"),
                                  "invade": dstar(replace(head, N=n), "invade")} for n in (5, 10, 20, 50, 200)}
    out["dstar_vs_alpha"] = {str(al): {"stay": dstar(replace(head, alpha=al), "stay"),
                                       "invade": dstar(replace(head, alpha=al), "invade")}
                             for al in (0.0, 0.02, 0.05, 0.10, 0.15)}
    out["dstar_vs_collusion"] = {str(c): {"stay": dstar(replace(head, c=c), "stay"),
                                          "invade": dstar(replace(head, c=c), "invade")}
                                 for c in (0.0, 0.25, 0.5, 0.75, 0.9)}
    out["dstar_blind_targeting"] = {"stay": dstar(replace(head, target="uniform"), "stay"),
                                    "invade": dstar(replace(head, target="uniform"), "invade")}
    out["dstar_vs_g"] = {str(g): {"stay": dstar(replace(head, g=g), "stay"), "invade": dstar(replace(head, g=g), "invade")}
                         for g in (0.05, 0.1, 0.2, 0.3, 0.4)}
    # brief's worked example (m=1, alpha=0, N=2)
    w = P(N=2, d=0.15, m=1.0, q=0.3, ratio=6.0, g=0.2, alpha=0.0)
    sL, sU = shares(w, 1)
    pL, pU, _ = expected_payoffs(w, 1)
    out["worked_example"] = {"discount_only": [sL, sU], "brief_loss_only": [sL * 0.94, sU * 0.99],
                             "transfer_conserving": [pL, pU]}
    out["dstar_vs_ratio_blind"] = {str(r): {"stay": dstar(replace(head, ratio=r, target="uniform"), "stay"),
                                            "invade": dstar(replace(head, ratio=r, target="uniform"), "invade")}
                                    for r in (1.0, 2.0, 3.0, 6.0, 12.0, 24.0)}
    out["dstar_vs_ratio_cheap_attack"] = {
        str(al): {str(r): {"stay": dstar(replace(head, ratio=r, alpha=al), "stay"),
                           "invade": dstar(replace(head, ratio=r, alpha=al), "invade")}
                  for r in (1.0, 2.0, 3.0, 6.0, 12.0)} for al in (0.005, 0.01)}
    out["grid"] = {}
    for Ng in (10, 20, 50):
        for c, cells in grid_run(Ng).items():
            out["grid"][f"N={Ng},c={c}"] = summarise(cells)
    with open(a.out, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(json.dumps(out, indent=1, default=float))


if __name__ == "__main__":
    main()
