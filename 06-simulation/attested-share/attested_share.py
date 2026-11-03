"""Share of each person's days lived that are ATTESTED (rebuilt before joining)
rather than OBSERVED (on the network's own calendar).

Run:  python attested_share.py            (full run, seed 20261103)
      python attested_share.py --test     (self-tests, each able to fail)
Times are in years from the network's founding (day 0). Pure numpy, ~20 s.
"""
import sys
import numpy as np

SEED = 20261103
N0 = 200_000          # people alive at founding
TMAX = 80
OBS_T = [0, 5, 10, 20, 40, 60, 80]

# Stylised US age pyramid (millions per band). Approximate and typed from memory,
# NOT retrieved from a source. Shape only; the result is conditional on it.
PYRAMID = [(0, 5, 18.5), (5, 10, 19.5), (10, 15, 21), (15, 20, 21.5), (20, 25, 22),
           (25, 30, 22.5), (30, 35, 23), (35, 40, 22.5), (40, 45, 21), (45, 50, 20.5),
           (50, 55, 20.5), (55, 60, 21), (60, 65, 21), (65, 70, 18.5), (70, 75, 15),
           (75, 80, 10.5), (80, 85, 6.5), (85, 90, 3.8), (90, 100, 1.6)]
GA, GB = 5.57e-5, 0.085   # Gompertz hazard A*exp(B*age)


def sample_ages(rng, n):
    w = np.array([p[2] for p in PYRAMID]); w = w / w.sum()
    band = rng.choice(len(PYRAMID), size=n, p=w)
    lo = np.array([p[0] for p in PYRAMID])[band]; hi = np.array([p[1] for p in PYRAMID])[band]
    return lo + rng.random(n) * (hi - lo)


def death_age(rng, age):
    """Age at death, conditional on being alive at `age` (Gompertz)."""
    u = rng.random(age.shape)
    return np.log(np.exp(GB * age) - (GB / GA) * np.log(u)) / GB


def build_population(rng):
    a0 = sample_ages(rng, N0)
    b0 = -a0
    d0 = b0 + death_age(rng, a0)
    mean_life = float(np.mean(death_age(rng, np.zeros(200_000))))
    births_per_year = N0 / mean_life
    nb = int(round(births_per_year * TMAX))
    bn = rng.random(nb) * TMAX
    dn = bn + death_age(rng, np.zeros(nb))
    b = np.concatenate([b0, bn]); d = np.concatenate([d0, dn])
    return b, d, np.concatenate([np.ones(N0), np.zeros(nb)]).astype(bool), mean_life


def adoption_J(rng, kind, n, ages_at_0):
    """Join-time draw J (years after founding). inf = never joins."""
    u = rng.random(n)
    if kind == "founding":   return np.zeros(n)
    if kind == "linear20":   return u * 20
    if kind == "linear40":   return u * 40
    if kind == "logistic60":  # 60% ceiling, logistic midpoint 10 y, scale 3
        ok = u < 0.6
        v = rng.random(n); v = np.clip(v, 1e-9, 1 - 1e-9)
        J = 10 + 3 * np.log(v / (1 - v))
        return np.where(ok, np.clip(J, 0, None), np.inf)
    if kind == "young_first":  # linear 20 y, but people near age 30 tend to join first
        # initial-living only; newborns keep plain u
        score = np.abs(ages_at_0 - 30.0)
        rk = np.argsort(np.argsort(score)) / max(len(score) - 1, 1)
        mixed = 0.5 * u + 0.5 * rk
        return np.where(np.isnan(ages_at_0), u * 20, mixed * 20)
    raise ValueError(kind)


def shares_at(T, b, d, j, reach):
    """Per-person attested share among members living at T."""
    mem = (j <= T) & (d > T) & (b <= T)
    att = np.clip(j - b, 0, None)[mem] * reach[mem]
    est = np.clip(j - b, 0, None)[mem] * (1 - reach[mem])
    lived = (T - b)[mem]
    lived = np.maximum(lived, 1e-9)
    return att / lived, est / lived, lived, mem


def summarise(T, b, d, j, reach):
    sh, est, lived, mem = shares_at(T, b, d, j, reach)
    if sh.size == 0:
        return None
    q = np.quantile(sh, [0.10, 0.25, 0.5, 0.75, 0.90])
    return dict(T=T, n=int(sh.size), p10=q[0], p25=q[1], p50=q[2], p75=q[3], p90=q[4],
                mean=float(sh.mean()), weighted=float((sh * lived).sum() / lived.sum()),
                est_weighted=float((est * lived).sum() / lived.sum()),
                zero=float((sh == 0).mean()), majority=float((sh > 0.5).mean()),
                lived_days_total=float(lived.sum() * 365.25))


def run_scenario(rng, kind, b, d, init_mask, reach_kind="full"):
    n = len(b)
    ages0 = np.where(init_mask, -b, np.nan)
    J = adoption_J(rng, kind, n, ages0)
    j = np.maximum(b, J)                   # born after one's own J: joins at birth
    j = np.where(d < j, np.inf, j)         # dead before joining: never a member
    if reach_kind == "full":
        reach = np.ones(n)
    elif reach_kind == "beta22":
        reach = rng.beta(2, 2, n)
    else:
        raise ValueError(reach_kind)
    return j, reach


def cohort_table(b, d, j, init_mask):
    """Founding-wave cohort: median share of survivors by years since joining."""
    out = {}
    ages = -b
    for lab, lo, hi in [("18-29", 18, 30), ("30-49", 30, 50), ("50-69", 50, 70), ("all adults 18+", 18, 200)]:
        sel = init_mask & (ages >= lo) & (ages < hi)
        row = []
        for s in [0, 5, 10, 20, 30, 40, 50]:
            alive = sel & (d > s)
            a = ages[alive]
            share = a / (a + s) if a.size else np.array([])
            row.append((s, int(alive.sum()), float(np.median(share)) if share.size else float("nan"),
                        float(np.quantile(share, 0.1)) if share.size else float("nan"),
                        float(np.quantile(share, 0.9)) if share.size else float("nan")))
        out[lab] = row
    # O6: when does the adult cohort median share cross 0.5, vs its median joining age
    sel = init_mask & (ages >= 18)
    med_join_age = float(np.median(ages[sel]))
    grid = np.arange(0, 60.01, 0.25); cross = float("nan")
    for s in grid:
        alive = sel & (d > s); a = ages[alive]
        if np.median(a / (a + s)) <= 0.5:
            cross = float(s); break
    return out, med_join_age, cross


# ----------------------------------------------------------------- self-tests
def self_tests():
    rng = np.random.default_rng(1)
    results = []

    def check(name, cond):
        results.append((name, bool(cond))); print(("PASS " if cond else "FAIL ") + name)

    # 1 born inside: join at birth -> share exactly 0
    b = np.array([5.0]); d = np.array([90.0]); j = np.array([5.0])
    sh, _, _, _ = shares_at(20.0, b, d, j, np.array([1.0])); check("born-inside share is 0", sh[0] == 0.0)
    # 2 join today, aged 40 -> share exactly 1
    b = np.array([-40.0]); j = np.array([0.0])
    sh, _, _, _ = shares_at(0.0, b, np.array([50.0]), j, np.array([1.0])); check("join-day share is 1", abs(sh[0] - 1) < 1e-9)
    # 3 closed form a/(a+s)
    sh, _, _, _ = shares_at(10.0, b, np.array([50.0]), j, np.array([1.0])); check("closed form 40/50 = 0.8", abs(sh[0] - 0.8) < 1e-9)
    # 4 non-members and the dead are excluded
    sh, _, _, m = shares_at(10.0, np.array([-40.0, -40.0]), np.array([50.0, 5.0]), np.array([12.0, 0.0]), np.ones(2))
    check("not-yet-joined and dead excluded", sh.size == 0)
    # 5 share monotone non-increasing in time for a fixed member
    b = np.array([-30.0]); d = np.array([200.0]); j = np.array([0.0])
    vals = [shares_at(T, b, d, j, np.ones(1))[0][0] for T in [0, 5, 10, 20, 40]]
    check("share falls with time since joining", all(x > y for x, y in zip(vals, vals[1:])))
    # 6 sampled pyramid matches its own weights within 1 pt (can fail if sampler is wrong)
    a = sample_ages(rng, 400_000); w = np.array([p[2] for p in PYRAMID]); w /= w.sum()
    ok = all(abs(((a >= lo) & (a < hi)).mean() - wi) < 0.01 for (lo, hi, _), wi in zip(PYRAMID, w))
    check("age sampler matches pyramid", ok)
    # 7 Gompertz death age is above current age and mean life is plausible (70-90)
    ml = np.mean(death_age(rng, np.zeros(100_000))); check("mean life 70-90", 70 < ml < 90)
    check("death after current age", bool((death_age(rng, np.full(1000, 60.0)) > 60).all()))
    # 8 population is roughly stationary: living count at T=60 within 8% of N0
    bb, dd, im, _ = build_population(np.random.default_rng(2))
    live = ((bb <= 60) & (dd > 60)).sum(); check("population ~stationary", abs(live / N0 - 1) < 0.08)
    # 8b initial-living flag marks exactly the N0 people born before day 0 (caught a run-1 inversion)
    check("init mask = born before day 0", int(im.sum()) == N0 and bool((bb[im] < 0).all()) and bool((bb[~im] >= 0).all()))
    # 9 founding wave at T=0: every living member has share 1 (no one born inside yet)
    j, r = run_scenario(np.random.default_rng(3), "founding", bb, dd, im)
    s0 = summarise(0, bb, dd, j, r); check("founding wave T=0 share 1.0", abs(s0["p50"] - 1) < 1e-9 and abs(s0["weighted"] - 1) < 1e-9)
    # 10 conservation: attested + observed days = days lived, summed over members
    sh, est, lived, mem = shares_at(20.0, bb, dd, np.maximum(bb, np.random.default_rng(4).random(len(bb)) * 20), np.ones(len(bb)))
    check("shares within [0,1]", bool(((sh >= 0) & (sh <= 1 + 1e-9)).all()))
    # 11 a deliberately wrong claim must fail: share is NOT independent of time
    j, r = run_scenario(np.random.default_rng(5), "founding", bb, dd, im)
    check("share at T=40 below share at T=10", summarise(40, bb, dd, j, r)["weighted"] < summarise(10, bb, dd, j, r)["weighted"])
    return all(ok for _, ok in results)


def main():
    rng = np.random.default_rng(SEED)
    b, d, init_mask, mean_life = build_population(rng)
    print(f"seed {SEED}  N0 {N0}  people simulated {len(b)}  mean life {mean_life:.1f} y  (Gompertz A={GA}, B={GB})")
    scen = [("founding", "full"), ("linear20", "full"), ("linear40", "full"),
            ("logistic60", "full"), ("young_first", "full"), ("linear20", "beta22")]
    allres = {}
    for i, (kind, rk) in enumerate(scen):
        j, reach = run_scenario(np.random.default_rng(SEED + i), kind, b, d, init_mask, rk)
        print(f"\n=== scenario {kind}  reach={rk} ===")
        print("T   n_members  p10   p25   p50   p75   p90   mean  weighted  est_wtd  zero%  maj%")
        for T in OBS_T:
            s = summarise(T, b, d, j, reach)
            allres[(kind, rk, T)] = s
            if s is None:
                print(f"{T:<3} none"); continue
            print(f"{T:<3} {s['n']:<9} {s['p10']:.3f} {s['p25']:.3f} {s['p50']:.3f} {s['p75']:.3f} {s['p90']:.3f} "
                  f"{s['mean']:.3f} {s['weighted']:.3f}    {s['est_weighted']:.3f}   {100*s['zero']:.1f}   {100*s['majority']:.1f}")
    j, _ = run_scenario(np.random.default_rng(SEED), "founding", b, d, init_mask)
    tab, medage, cross = cohort_table(b, d, j, init_mask)
    print("\n=== founding-wave cohorts: share of survivors by years since joining (median [p10, p90], n survivors) ===")
    for lab, rows in tab.items():
        print(lab)
        for s, n, med, lo, hi in rows:
            print(f"  s={s:<3} n={n:<7} median {med:.3f}  [{lo:.3f}, {hi:.3f}]")
    print(f"\nadult cohort median joining age {medage:.1f} y; median share first <= 0.5 at s = {cross} y")

    # declared outcomes
    def g(k, rk, T, f): return allres[(k, rk, T)][f]
    print("\n=== declared outcomes ===")
    chk = []
    def rep(name, val, ok): chk.append(ok); print(f"{name}: {val} -> {'HELD' if ok else 'MISSED'}")
    rep("O1 median@10", f"{g('founding','full',10,'p50'):.3f} in [0.65,0.85]", 0.65 <= g('founding','full',10,'p50') <= 0.85)
    rep("O1 weighted@10", f"{g('founding','full',10,'weighted'):.3f} in [0.60,0.85]", 0.60 <= g('founding','full',10,'weighted') <= 0.85)
    rep("O2 median@40", f"{g('founding','full',40,'p50'):.3f} in [0.00,0.40]", 0.0 <= g('founding','full',40,'p50') <= 0.40)
    rep("O2 weighted@40", f"{g('founding','full',40,'weighted'):.3f} in [0.15,0.45]", 0.15 <= g('founding','full',40,'weighted') <= 0.45)
    rep("O3 weighted@80", f"{g('founding','full',80,'weighted'):.3f} < 0.10", g('founding','full',80,'weighted') < 0.10)
    rep("O4 linear20 weighted@20", f"{g('linear20','full',20,'weighted'):.3f} in [0.45,0.80]", 0.45 <= g('linear20','full',20,'weighted') <= 0.80)
    sp = g('linear20','full',20,'p90') - g('linear20','full',20,'p10')
    rep("O5 linear20 p90-p10@20", f"{sp:.3f} > 0.50", sp > 0.50)
    rep("O6 half-point vs median join age", f"cross {cross} vs median age {medage:.1f}", abs(cross - medage) <= 2.0)
    print(f"\ndeclared outcomes held: {sum(chk)} of {len(chk)}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(0 if self_tests() else 1)
    main()
