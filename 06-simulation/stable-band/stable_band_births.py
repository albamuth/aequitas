#!/usr/bin/env python3
"""
stable_band_births.py -- the births arm of stable_band_cumulative.py.

Request sr-20261102-births-arm-of-stable-band-cumulative-py-kapp (filed 2026-11-02).
Extends stable_band_kappa.py (kappa = 1,380/365, US method). Declared inputs and
outcomes: BIRTHS_DECLARED.md, written before the first run.

WHAT IS NEW
    Births and deaths over M = 100 yearly periods. The runner DECLARES the birth
    rate and the death schedule and prints both (and what they imply).
    Children follow Pledges.md ruling 7 (13.1): no debit, floor credit from
    birth, no requests below the consent age.

    A person is a row. Row i enters at period e_i with age a0_i and leaves after
    period x_i. Age at the start of period t is a0_i + (t - e_i). Demography does
    not depend on rho, so it is drawn once per seed (common random numbers) and
    the rho bisection only re-runs the gate.

Run:  python stable_band_births.py [--test]
"""
from __future__ import annotations

import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import stable_band as sb                                      # noqa: E402
import stable_band_cumulative as sc                           # noqa: E402
from gate import Kernel, Dials, Conformance                   # noqa: E402

KAPPA = sb.MEDIAN_LIFESTYLE_H_YR / 365.0                      # 3.7808, US method
M = sc.M_PRIMARY                                              # 100
CONSENT_AGE = 18.0
BIRTH_RATE = 0.012                                            # per living person per year
BIRTH_RATES_SENS = (0.008, 0.016)
MAX_AGE = 100.0
# (age from, age to, chance of dying in one year), by age at the start of the year
DEATH_SCHEDULE = ((0, 18, 0.0004), (18, 35, 0.0010), (35, 50, 0.0025),
                  (50, 65, 0.0080), (65, 85, 0.0350), (85, 100, 0.1500))
DEMOG_SEED_OFFSET = 100                                       # demography seed = age seed + 100
POOL = 200_000
FLOORS = sc.FLOORS_ASKED


# ----------------------------------------------------------------------------
# demography
# ----------------------------------------------------------------------------

def hazard(age):
    h = np.zeros_like(age, dtype=float)
    for lo, hi, p in DEATH_SCHEDULE:
        h[(age >= lo) & (age < hi)] = p
    h[age >= MAX_AGE] = 1.0
    return h


def life_expectancy_at_birth():
    """Exact, from the schedule: sum over ages of the chance of being alive."""
    s, e0 = 1.0, 0.0
    for a in range(int(MAX_AGE)):
        e0 += s * (1.0 - 0.5 * float(hazard(np.array([a], float))[0]))
        s *= 1.0 - float(hazard(np.array([a], float))[0])
    return e0


class Demog:
    """People over M periods. Rows, entry period, last period, starting age,
    work hours and wants, plus the per-period list of who is alive."""

    def __init__(self, w0, x0, ages0, birth_rate, seed, M=M, deaths=True):
        rng = np.random.default_rng(seed)
        n0 = len(w0)
        pw, px = sb.build_people(POOL, seed=seed + 1000)      # pool for the newborns
        self.work = [w0]; self.wants = [x0]
        a0 = [np.asarray(ages0, float)]
        ent = [np.ones(n0, int)]
        ext = [np.full(n0, M, int)]                            # last period alive
        self.births = np.zeros(M, int); self.deaths = np.zeros(M, int)
        alive_n = np.zeros(M, int)
        # live bookkeeping on concatenated arrays, grown once per period
        A0 = a0[0]; E = ent[0]; X = ext[0]
        W = w0; XW = x0
        used = 0
        for t in range(1, M + 1):
            alive = (E <= t) & (X >= t)
            idx = np.flatnonzero(alive)
            alive_n[t - 1] = idx.size
            if deaths:
                age_t = A0[idx] + (t - E[idx])
                die = rng.random(idx.size) < hazard(age_t)
                X[idx[die]] = t                                # dies at the end of period t
                self.deaths[t - 1] = int(die.sum())
            nb = int(rng.binomial(idx.size, birth_rate)) if birth_rate > 0 else 0
            if nb:
                self.births[t - 1] = nb
                A0 = np.concatenate([A0, np.zeros(nb)])
                E = np.concatenate([E, np.full(nb, t + 1, int)])
                X = np.concatenate([X, np.full(nb, M, int)])
                W = np.concatenate([W, pw[used:used + nb]])
                XW = np.concatenate([XW, px[used:used + nb]])
                used += nb
        self.a0, self.e, self.x, self.work, self.wants = A0, E, X, W, XW
        self.M = M
        self.alive_n = alive_n
        self.idx = []
        self.age = []
        for t in range(1, M + 1):
            ii = np.flatnonzero((E <= t) & (X >= t))
            self.idx.append(ii)
            self.age.append(A0[ii] + (t - E[ii]))
        # a newborn row has a0 = 0 and enters at period e >= 2; the born-after-M ones are never alive

    def crude_rates(self):
        return self.deaths.sum() / self.alive_n.sum(), self.births.sum() / self.alive_n.sum()


# ----------------------------------------------------------------------------
# the gate, through the kernel
# ----------------------------------------------------------------------------

def run_path(dm, F, rho, ruling7, cap="req", past_rate=sc.PAST_RATE, kappa=KAPPA,
             R_fixed=None, check=True):
    """Return (admitted real units per period, capacity per period, requesters per period)."""
    n_rows = len(dm.a0)
    C = np.zeros(n_rows); D = np.zeros(n_rows)
    # joiner past: floor every day lived; debit from the consent age only under ruling 7
    C0 = F * 365.0 * dm.a0
    if ruling7:
        D0 = past_rate * np.maximum(dm.a0 - CONSENT_AGE, 0.0)
    else:
        D0 = past_rate * dm.a0
    entered = np.zeros(n_rows, bool)
    adm = np.empty(dm.M); capv = np.empty(dm.M); nreq = np.empty(dm.M, int)
    for t in range(1, dm.M + 1):
        ii = dm.idx[t - 1]; age = dm.age[t - 1]
        new = ii[~entered[ii]]
        C[new] = C0[new]; D[new] = D0[new]; entered[new] = True
        adult = age >= CONSENT_AGE
        wk = dm.work[ii]
        if ruling7:
            rate = np.where(adult, np.minimum(F + wk, sb.DAY), F)   # a child accrues the floor only
            requester = adult
        else:
            rate = sb.credit_rate(wk, F)
            requester = np.ones(ii.size, bool)
        k = Kernel(ii.size, rate, Dials(rho=float(rho), floor_h=float(F)))
        k.C = C[ii].copy(); k.D = D[ii].copy()
        k.accrue(days=365.0)
        room_before = np.maximum(k.room(), 0.0)
        req = np.where(requester, dm.wants[ii] * kappa * 365.0, 0.0)
        admitted, _ = k.consume(req)
        if check:
            if np.any(admitted > room_before + 1e-6):
                raise AssertionError("admitted more than the gate allowed")
            if ruling7 and np.any(admitted[~requester] != 0):
                raise AssertionError("a child was admitted debit")
            Conformance.ic7_day_is_24_hours(k)
            Conformance.credit_only_rises(k)
            Conformance.debit_only_rises(k)
            Conformance.pledged_room_is_backed(k)
        C[ii] = k.C; D[ii] = k.D
        adm[t - 1] = admitted.sum() / (kappa * 365.0)
        nreq[t - 1] = int(requester.sum())
        if cap == "req":
            capv[t - 1] = sb.CAP * dm.wants[ii][requester].sum()
        elif cap == "all":
            capv[t - 1] = sb.CAP * dm.wants[ii].sum()
        else:
            capv[t - 1] = R_fixed
    return adm, capv, nreq


def edge(dm, F, ruling7, cap="req", R_fixed=None, **kw):
    def ok(r):
        a, c, _ = run_path(dm, F, r, ruling7, cap, R_fixed=R_fixed, check=False, **kw)
        return bool(np.all(a <= c + 1e-9))
    return sc.bisect_edge(ok)


# ----------------------------------------------------------------------------
# self-tests -- each can fail
# ----------------------------------------------------------------------------

def _small(n=6000, seed=3):
    w, x = sb.build_people(n, seed=seed)
    return w, x


def test_no_demography_reproduces_the_kappa_cumulative_path():
    """Arm A with no births or deaths must equal stable_band_cumulative.run_path."""
    w, x = _small()
    ages = sc.draw_ages(len(w), 11)
    dm = Demog(w, x, ages, 0.0, 1, M=12, deaths=False)
    for F, rho in ((10.0, 0.5), (2.0, 1.5), (14.0, 0.3)):
        a, c, _ = run_path(dm, F, rho, ruling7=False, cap="req")
        b = sc.run_path(w, x, ages, F, rho, KAPPA, 12)
        assert np.allclose(a, b, rtol=1e-9, atol=1e-6), (F, rho, a[:3], b[:3])
    print("[ok] no births, no deaths, published children: identical to stable_band_cumulative")


def test_published_fixed_edges():
    """Arm A on the full population reproduces the published edges."""
    w, x = sb.build_people()
    ages = sc.draw_ages(len(w), 11)
    dm = Demog(w, x, ages, 0.0, 1, deaths=False)
    for F, pub in ((2.0, 1.017), (10.0, 0.330), (14.0, 0.253)):
        e, fl = edge(dm, F, False)
        assert fl == "" and abs(e - pub) <= 0.01, (F, e, pub)
    print("[ok] arm A reproduces 1.017 / 0.330 / 0.253 within 0.01")


def test_a_child_carries_no_debit_and_has_floor_credit():
    w, x = _small(n=2000)
    dm = Demog(w, x, np.full(len(w), 30.0), 0.02, 4, M=25)
    assert dm.births.sum() > 100
    F, rho = 10.0, 1.0
    # replay by hand for the first newborn row and check its books at every age
    row = len(w)                                                  # first newborn row
    e = int(dm.e[row])
    n_rows = len(dm.a0)
    # re-run the path and capture C, D of that row through a tiny copy of the loop
    C = np.zeros(n_rows); D = np.zeros(n_rows); entered = np.zeros(n_rows, bool)
    seen = []
    for t in range(1, dm.M + 1):
        ii = dm.idx[t - 1]; age = dm.age[t - 1]
        new = ii[~entered[ii]]
        C[new] = F * 365.0 * dm.a0[new]; D[new] = 0.0; entered[new] = True
        adult = age >= CONSENT_AGE
        wk = dm.work[ii]
        rate = np.where(adult, np.minimum(F + wk, sb.DAY), F)
        k = Kernel(ii.size, rate, Dials(rho=rho, floor_h=F))
        k.C = C[ii].copy(); k.D = D[ii].copy(); k.accrue(365.0)
        req = np.where(adult, dm.wants[ii] * KAPPA * 365.0, 0.0)
        k.consume(req)
        C[ii] = k.C; D[ii] = k.D
        if row in set(ii.tolist()):
            j = int(np.flatnonzero(ii == row)[0])
            seen.append((float(age[j]), float(C[row]), float(D[row])))
    assert len(seen) >= 2 and e >= 2
    kids = [(a, c, d) for a, c, d in seen if a < CONSENT_AGE]
    grown = [(a, c, d) for a, c, d in seen if a >= CONSENT_AGE]
    assert len(kids) >= 5 and len(grown) >= 1, (len(kids), len(grown))
    for a, c, d in kids:
        assert d == 0.0, ("a child has debit", a, d)
    for a, c, d in seen:
        if a < CONSENT_AGE:   # credit is the floor only while a child
            assert abs(c - F * 365.0 * (a + 1.0)) < 1e-6, ("floor credit wrong", a, c)
    assert grown[0][2] > 0.0, "debit must start at the consent age"
    print(f"[ok] a newborn carries 0 debit and F x 365 x age credit for {len(kids)} years, "
          f"and debit starts only at {grown[0][0]:g}")


def test_the_dead_leave_and_the_count_adds_up():
    w, x = _small(n=3000)
    dm = Demog(w, x, sc.draw_ages(len(w), 12), 0.012, 5, M=60)
    n0 = len(w)
    for t in range(1, 60):
        expected = dm.alive_n[t - 1] + dm.births[t - 1] - dm.deaths[t - 1]
        assert dm.alive_n[t] == expected, (t, dm.alive_n[t], expected)
    ii = dm.idx[-1]
    assert np.all(dm.x[ii] >= 60)
    dead = np.flatnonzero(dm.x < 60)
    assert dead.size == dm.deaths[:59].sum()
    print("[ok] alive(t+1) = alive(t) + births - deaths, for 59 periods; the dead never reappear")


def test_realised_death_rate_matches_the_schedule():
    """With a stationary-age population the realised deaths must match the
    schedule's own expectation. Fails if hazard() or the draw is wrong."""
    n = 200_000
    rng = np.random.default_rng(0)
    ages = rng.random(n) * 100.0
    exp = hazard(ages).mean()
    w, x = sb.build_people(n, seed=9)
    dm = Demog(w, x, ages, 0.0, 6, M=1)
    got = dm.deaths[0] / n
    assert abs(got - exp) < 4 * np.sqrt(exp / n) + 1e-4, (got, exp)
    print(f"[ok] realised death rate {got:.5f} vs schedule {exp:.5f} (uniform ages 0-100)")


def test_the_rationing_test_can_fail_and_pass():
    w, x = _small()
    dm = Demog(w, x, sc.draw_ages(len(w), 11), BIRTH_RATE, 7, M=20)
    for r7 in (False, True):
        a_lo, c_lo, _ = run_path(dm, 10.0, 0.02, r7)
        a_hi, c_hi, _ = run_path(dm, 10.0, 4.0, r7)
        assert np.all(a_lo <= c_lo) and np.any(a_hi > c_hi), (r7, a_lo.max(), a_hi.max())
    print("[ok] rho 0.02 rations and rho 4.0 does not, with and without ruling 7")


def test_bisection_assumes_monotone_in_rho():
    """The boolean 'all periods ration' must be True-then-False along a rho grid."""
    w, x = _small()
    dm = Demog(w, x, sc.draw_ages(len(w), 11), BIRTH_RATE, 8, M=30)
    for F in (2.0, 10.0):
        for r7 in (False, True):
            seq = []
            for r in np.arange(0.05, 3.0, 0.05):
                a, c, _ = run_path(dm, F, r, r7, check=False)
                seq.append(bool(np.all(a <= c + 1e-9)))
            flips = sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1])
            assert flips <= 1, (F, r7, seq)
    print("[ok] the rationing boolean flips at most once along rho (bisection is valid)")


def test_ruling7_changes_the_answer():
    """If ruling 7 did nothing, arms A and C would match. They must not."""
    w, x = _small()
    dm = Demog(w, x, sc.draw_ages(len(w), 11), 0.0, 1, M=30, deaths=False)
    ea, _ = edge(dm, 10.0, False)
    ec, _ = edge(dm, 10.0, True)
    assert abs(ea - ec) > 0.02, (ea, ec)
    print(f"[ok] ruling 7 moves the fixed-population edge: {ea:.3f} -> {ec:.3f}")


def run_tests():
    for fn in (test_no_demography_reproduces_the_kappa_cumulative_path,
               test_published_fixed_edges,
               test_a_child_carries_no_debit_and_has_floor_credit,
               test_the_dead_leave_and_the_count_adds_up,
               test_realised_death_rate_matches_the_schedule,
               test_the_rationing_test_can_fail_and_pass,
               test_bisection_assumes_monotone_in_rho,
               test_ruling7_changes_the_answer):
        fn()
    print("\nAll self-tests passed.")


# ----------------------------------------------------------------------------
# the run
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return

    w, x = sb.build_people()
    n = len(w)
    R0 = sb.CAP * float(x.sum())
    print(f"N={n:,} seed={sb.RNG_SEED} kappa={KAPPA:.4f} R_max(start)={R0:,.0f} "
          f"wants_total={x.sum():,.0f} M={M}")
    print("DECLARED  death schedule (age from, to, chance of dying in a year): "
          + "; ".join(f"{lo}-{hi}: {p}" for lo, hi, p in DEATH_SCHEDULE) + f"; all die at {MAX_AGE:g}")
    print(f"DECLARED  birth rate {BIRTH_RATE} per living person per year "
          f"(sensitivity {BIRTH_RATES_SENS});  consent age {CONSENT_AGE:g}")
    e0 = life_expectancy_at_birth()
    print(f"IMPLIED   life expectancy at birth {e0:.1f} y;  stationary crude death rate ~{1/e0:.4f}")
    print()

    seeds = sc.AGE_SEEDS
    dms = {}
    for s in seeds:
        ages = sc.draw_ages(n, s)
        dms[("fixed", s)] = Demog(w, x, ages, 0.0, s + DEMOG_SEED_OFFSET, deaths=False)
        dms[("births", s)] = Demog(w, x, ages, BIRTH_RATE, s + DEMOG_SEED_OFFSET)
    d = dms[("births", seeds[0])]
    cd, cb = d.crude_rates()
    print("== 0. demography actually drawn (age seed 11) ==")
    print(f"realised crude death rate {cd:.4f}, crude birth rate {cb:.4f}; "
          f"population t=1 {d.alive_n[0]:,}  t=25 {d.alive_n[24]:,}  t=50 {d.alive_n[49]:,}  "
          f"t=100 {d.alive_n[99]:,};  births in 100 y {d.births.sum():,}, deaths {d.deaths.sum():,}")
    print()

    print("== 1. rho*: without births (A), with births (B), and the change ==")
    arms = (("A fixed (published)", "fixed", False),
            ("B births, ruling 7", "births", True),
            ("C fixed + ruling 7", "fixed", True),
            ("D births, published children", "births", False))
    res = {}
    for F in FLOORS:
        for name, key, r7 in arms:
            vals, flags = [], set()
            for s in seeds:
                e, fl = edge(dms[(key, s)], F, r7)
                vals.append(e); flags.add(fl)
            res[(F, name)] = (np.array(vals), sorted(flags))
    print(f"{'F':>4} | {'A without births':>18} | {'B with births':>18} | {'B - A':>8} | "
          f"{'C fixed+r7':>12} | {'D births+old':>13} | {'C - A (r7)':>10} | {'D - A (turnover)':>16}")
    for F in FLOORS:
        A = res[(F, arms[0][0])][0]; B = res[(F, arms[1][0])][0]
        Cc = res[(F, arms[2][0])][0]; Dd = res[(F, arms[3][0])][0]
        print(f"{F:>4g} | {A.mean():>8.3f} (sd {A.std():.3f}) | {B.mean():>8.3f} (sd {B.std():.3f}) | "
              f"{B.mean()-A.mean():>+8.3f} | {Cc.mean():>6.3f} (sd {Cc.std():.3f}) | "
              f"{Dd.mean():>7.3f} (sd {Dd.std():.3f}) | {Cc.mean()-A.mean():>+10.3f} | {Dd.mean()-A.mean():>+16.3f}"
              f"   flags A{res[(F, arms[0][0])][1]} B{res[(F, arms[1][0])][1]}")
    print("per-seed B:", {F: [round(v, 3) for v in res[(F, arms[1][0])][0]] for F in FLOORS})
    print()

    print("== 2. the arm-B path at its own edge and at rho = one-day edge of A (age seed 11) ==")
    dB = dms[("births", seeds[0])]
    for F in FLOORS:
        eB = res[(F, arms[1][0])][0][0]
        eA = res[(F, arms[0][0])][0][0]
        for lab, r in (("B edge", eB), ("A edge", eA)):
            a_, c_, nq = run_path(dB, F, r, True)
            print(f"F={F:>4g} rho={r:.3f} ({lab}) admitted t=1 {a_[0]:>8,.0f} t=10 {a_[9]:>8,.0f} "
                  f"t=50 {a_[49]:>8,.0f} t=100 {a_[99]:>8,.0f} | capacity t=1 {c_[0]:>8,.0f} "
                  f"t=100 {c_[99]:>8,.0f} | max admitted/capacity {np.max(a_/c_):.3f} "
                  f"| requesters t=1 {nq[0]:,} t=100 {nq[99]:,}")
    print()

    print("== 2b. which period sets the edge (age seed 11): the period where admitted/capacity peaks at the edge ==")
    for F in FLOORS:
        for name, key, r7 in arms[1:3]:
            r = res[(F, name)][0][0]
            a_, c_, _ = run_path(dms[(key, seeds[0])], F, r, r7)
            q = a_ / c_
            print(f"F={F:>4g} {name:<22} rho={r:.3f}  peak period {int(np.argmax(q)) + 1}  "
                  f"(ratio {q.max():.3f}; t=1 {q[0]:.3f}, t=18 {q[17]:.3f}, t=50 {q[49]:.3f}, t=100 {q[99]:.3f})")
    print()

    print("== 3. sensitivities of arm B (age seed 11) ==")
    s0 = seeds[0]
    rows = []
    for br in BIRTH_RATES_SENS:
        dmx = Demog(w, x, sc.draw_ages(n, s0), br, s0 + DEMOG_SEED_OFFSET)
        rows.append((f"birth rate {br} (population t=100: {dmx.alive_n[99]:,})", dmx, {}))
    dm11 = dms[("births", s0)]
    # With ruling 7 the children do not request, so adult wants (~52k) sit below 56,446 and below
    # 0.85 x everybody's wants: rationing cannot fail. Those two conventions are ENTAILED, so they
    # are not run as edges. This line proves it instead of asserting it.
    adult_peak = max(float(dm11.wants[dm11.idx[t][dm11.age[t] >= CONSENT_AGE]].sum()) for t in range(M))
    print(f"entailment check: the most adult wants in any period is {adult_peak:,.0f} real units; "
          f"fixed R_max {R0:,.0f} is {'above' if R0 >= adult_peak else 'below'} it, so under "
          f"{'that' if R0 >= adult_peak else 'no'} fixed-capacity convention rationing "
          f"{'cannot fail' if R0 >= adult_peak else 'can fail'}.")
    rows.append(("past debit 1,000 h/yr", dm11, dict(past_rate=1000.0)))
    rows.append(("past debit 2,000 h/yr", dm11, dict(past_rate=2000.0)))
    for name, dmx, kw in rows:
        out = [sc.fmt(*edge(dmx, F, True, **kw)) for F in FLOORS]
        print(f"{name:<52} F=2 {out[0]:>9}  F=10 {out[1]:>9}  F=14 {out[2]:>9}")
    # arm A with the same capacity conventions is the fixed control for those rows
    out = [sc.fmt(*edge(dms[('fixed', s0)], F, False)) for F in FLOORS]
    print(f"{'(arm A, same seed, for reference)':<52} F=2 {out[0]:>9}  F=10 {out[1]:>9}  F=14 {out[2]:>9}")
    print()
    print("(<) = even rho 0.005 fails to ration: a ceiling on the edge, not a value.  "
          "(>=) = grid ended: a floor, not a value.")


if __name__ == "__main__":
    main()
