#!/usr/bin/env python3
"""
span_generosity.py -- does seller choice (Foundations 4.0 fact 2, 5.5.5) arrest a network that
recruits by estimating undocumented spans generously?

Request sr-20260919-sweep-span-estimate-generosity-across-compet.

MODEL (every input is named; the verdict depends on the two marked ASSUMED)
  K networks, identical published settings (F, rho). Network 0 adds g extra years to each joiner's
  undocumented span. The others add 0. g is per-person and NOT published.
  What a joiner gains from g (arithmetic, Foundations 4.4 cond.3 and 5.5.5):
      pledge budget  +F*365 h per extra year   (credit, no cap breach: 24/F holds per day lived)
      gate slack     +rho*F*365 - 1380 h per extra year  (negative inside the rationing band)
  What anyone can SEE: the public log shows credit dated before the account existed (backdated
  credit, 4.4 "credit is issuable backwards"). Sellers sample n_obs new accounts per network per round
  and compare the mean backdated years against the other networks.
  ASSUMED 1 (detect): a seller acts on that comparison (z-test, threshold z).
  ASSUMED 2 (info):   a fraction phi of joiners learn g before joining (pre-quote / word of mouth).
  Flagged network -> fraction r of sellers refuse it -> joiners see the refusal rate (public) and
  weigh it. Joiners choose by logit.

Run:   python span_generosity.py           full sweep -> sweep.csv, sweep_summary.json
       python span_generosity.py --test    self-tests
Seed:  base seed 20261120; replication k uses seed base+k.
"""
import argparse, csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_SEED = 20261120
K = 5
ANCHOR = 1380.0                      # median lifestyle h/yr (Foundations 3.5)
RHO_STAR = {2: 1.017, 10: 0.330, 14: 0.253}   # Foundations 4.4 table
HONEST_MEAN, HONEST_SD = 8.0, 6.0    # ASSUMED: years of backdated credit an honest joiner is given
T, JOIN, BURN = 40, 500, 20          # rounds, joiners per round, rounds ignored
TAU = 0.5                            # logit taste noise
S_SAY = 1.0                          # weight a joiner puts on pledge budget (per 1000 h)
C_REFUSE = 10.0                      # ASSUMED utility cost of a fully refused network (swept below)
W_FAKE = 0.1                         # ASSUMED worth to a joiner of a fabricated year, vs a real one


def gate_gain_per_year(F, rho):
    return rho * F * 365.0 - ANCHOR


def budget_per_year(F):
    return F * 365.0


def run(g, phi, detect, z=3.0, n_obs=200, r=0.5, F=10, F0=None, seed=0, c_ref=None):
    cr = C_REFUSE if c_ref is None else c_ref
    """Return share of joiners who chose network 0 over rounds BURN..T, and flag rate."""
    rng = np.random.default_rng(seed)
    Fs = np.full(K, float(F)); Fs[0] = F if F0 is None else F0
    gs = np.zeros(K); gs[0] = g
    refusal = np.zeros(K)
    picks0 = 0; total = 0; flags = 0
    for t in range(T):
        # sellers observe
        if detect:
            m = np.array([rng.normal(HONEST_MEAN + gs[i], HONEST_SD / np.sqrt(n_obs)) for i in range(K)])
            for i in range(K):
                others = np.delete(m, i)
                zi = (m[i] - np.median(others)) / (HONEST_SD * np.sqrt(2.0 / n_obs))
                if zi > z:
                    refusal[i] = r
                    if i == 0 and t >= BURN: flags += 1
                else:
                    refusal[i] = 0.0
        # published F is visible to the F-control: sellers refuse a floor above plausible
        # joiners choose
        informed = rng.random(JOIN) < phi
        base = S_SAY * Fs * 365.0 / 1000.0                      # published attraction, per year
        extra = W_FAKE * S_SAY * gs * Fs * 365.0 / 1000.0                 # g's attraction, seen if informed
        U = base[None, :] + informed[:, None] * extra[None, :] - cr * refusal[None, :]
        U = U / TAU + rng.gumbel(size=(JOIN, K))
        ch = U.argmax(axis=1)
        if t >= BURN:
            picks0 += int((ch == 0).sum()); total += JOIN
    return picks0 / total, flags / (T - BURN)


def sweep(reps=20):
    rows = []
    for detect in (False, True):
        for phi in (0.0, 0.25, 1.0):
            for g in (0, 1, 2, 3, 5, 8):
                sh = []; fl = []
                for k in range(reps):
                    a, b = run(g, phi, detect, seed=BASE_SEED + k)
                    sh.append(a); fl.append(b)
                rows.append(dict(detect=detect, phi=phi, g=g, share=np.mean(sh), sd=np.std(sh),
                                 flag=np.mean(fl)))
    return rows


def f_control(reps=20):
    """Floor-shopping control: network 0 publishes F=14 vs 10. Detection = anyone can read F."""
    out = {}
    for sellers_act in (False, True):
        sh = []
        for k in range(reps):
            rng = np.random.default_rng(BASE_SEED + k)
            Fs = np.array([14.0] + [10.0] * (K - 1))
            ref = np.zeros(K)
            if sellers_act: ref[0] = 0.5
            tot = 0; n0 = 0
            for t in range(T):
                U = (S_SAY * Fs * 365 / 1000)[None, :] - C_REFUSE * ref[None, :]
                U = U / TAU + rng.gumbel(size=(JOIN, K))
                c = U.argmax(axis=1)
                if t >= BURN: n0 += (c == 0).sum(); tot += JOIN
            sh.append(n0 / tot)
        out["sellers_refuse" if sellers_act else "no_seller_discipline"] = float(np.mean(sh))
    return out


def tests():
    # T1: the Foundations figure, -175 h per year at F=10, rho*=0.330
    assert abs(gate_gain_per_year(10, 0.330) - (-175)) < 1, gate_gain_per_year(10, 0.330)
    # T2: control, g=0 -> network 0 gets about 1/K
    s, _ = run(0, 1.0, False, seed=1)
    assert abs(s - 1 / K) < 0.03, s
    # T3: can fail the other way: informed joiners, no detection, large g -> big share
    s, _ = run(8, 1.0, False, seed=1)
    assert s > 0.5, s
    # T4: detection at g=8 flags nearly always, and pulls the share below the undetected one
    s2, fl = run(8, 1.0, True, seed=1)
    assert fl > 0.9 and s2 < s, (fl, s2, s)
    # T5: blind joiners (phi=0) are not moved by g even without detection
    s0, _ = run(8, 0.0, False, seed=1)
    assert abs(s0 - 1 / K) < 0.03, s0
    # T6: a seller test that is too weak (n_obs=4) misses a 1-year inflation (can fail)
    _, fl1 = run(1, 1.0, True, n_obs=4, seed=1)
    assert fl1 < 0.5, fl1
    print("all self-tests passed")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        tests(); sys.exit(0)
    rows = sweep()
    with open(os.path.join(HERE, "sweep.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    # minimum detectable g by n_obs
    mdg = {}
    for n in (4, 25, 200, 2000):
        for g in (0.5, 1, 2, 3, 5, 8):
            fl = np.mean([run(g, 1.0, True, n_obs=n, seed=BASE_SEED + k)[1] for k in range(20)])
            if fl > 0.5: mdg[n] = g; break
        else: mdg[n] = None
    arith = {F: dict(rho=RHO_STAR[F], budget_h_per_year=budget_per_year(F),
                     gate_gain_h_per_year=gate_gain_per_year(F, RHO_STAR[F])) for F in RHO_STAR}
    cref = {}
    for c in (0, 1, 2, 5, 10, 20):
        cref[c] = float(np.mean([run(5, 1.0, True, c_ref=c, seed=BASE_SEED + k)[0] for k in range(20)]))
    summ = dict(c_refuse_sweep_share_at_g5_phi1=cref, arith=arith, f_control=f_control(), min_detectable_g_by_n_obs=mdg)
    json.dump(summ, open(os.path.join(HERE, "sweep_summary.json"), "w"), indent=1)
    for r in rows: print({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()})
    print(json.dumps(summ, indent=1))
