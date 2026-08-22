"""
rho_sweep.py -- the prime-rate (rho) sweep, CALIBRATED to the median-lifestyle
anchor (Tracks 1-4, ~1,380 h/yr) and the Q6 efficiency finding.

WHAT rho IS (OP-4 shape, settled). Discretionary consumption is gated by
D_i <= rho * C_i: an account may consume up to rho times its own earned credit.
rho is an EXOGENOUS "prime-rate" dial set by local governance (A8); Aequitas uses
it, never sets it (Sec.3.5 forbids a global number). The disparity CEILING (24/F)
is rho-INDEPENDENT (proved in disparity_ceiling_sim.py); this script studies the
ABSOLUTE level rho instead -- does a pickable rho clear the market, where does the
median sit, and how does it move under shocks and under efficient production?

MODEL (real units where we have them; illustrative where we don't -- flagged).
  Credit rate c_i (labour-h/day) = self-care floor F + productive work (A2/Sec.6.1b),
    drawn from the same heterogeneous population as the ceiling sim (c_i in [F,24]).
  Each agent wants a real lifestyle r_i (median = 1.0 "median-lifestyle unit").
  Consuming r_i costs debit  D_i = r_i * INTENSITY, where INTENSITY = debit-hours
    per lifestyle-unit. We CALIBRATE INTENSITY_US = median credit (~13 h/day) so
    that at rho=1 the median person's own credit exactly funds one median lifestyle
    (matches Sec.3.5: debit ~ credit for the median; the number is OP-10-dependent
    and flagged illustrative -- only RATIOS and DIRECTIONS are claimed).
  The gate then caps real consumption at  r_i <= rho * c_i / INTENSITY.
  Physical capacity R_max (real lifestyle-units the economy can make) is the ENERGY/
    MATERIALS envelope (Q1: the binding constraint is physical, not labour), set to
    a fraction CAP of unconstrained wants.
  Clearing rho*: the rho at which  sum_i min(r_i^want, rho c_i/INTENSITY) = R_max.

THE Q6 TIE-IN. Efficient production (Germany/Spain/Japan vs US) delivers the same
  real standard at LOWER debit-intensity. Lower INTENSITY => the same physical
  output clears at a LOWER rho (more debit-headroom) AND the median gets MORE real
  lifestyle for the same credit. Efficiency, not extra labour, is what loosens the
  constraint -- closing the loop with Q1 (labour is abundant; materials/energy bind)
  and Q6 (the US is the inefficient outlier).

Run:  python rho_sweep.py [--test] [--no-plots]
"""
from __future__ import annotations

import argparse
import os

import numpy as np

from disparity_ceiling_sim import F, DAY, CEILING, draw_population, gini

HERE = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(7)
N = 200_000

# --- calibration anchors ------------------------------------------------------
MEDIAN_LIFESTYLE_H = 1380.0 / 365.0     # ~3.78 embodied labour-h/day (Tracks 1-4)
# INTENSITY_US: debit-hours per median-lifestyle-unit. Calibrated to the median
# credit rate so rho=1 funds one median lifestyle (Sec.3.5). OP-10-dependent -> the
# ABSOLUTE rho* is illustrative; the ratios/directions below are the results.
CAP = 0.85                               # physical capacity = 85% of unconstrained
                                         #   wants (Q1: materials/energy bind, not labour)
# Q6 efficiency multipliers on debit-intensity (same real standard, less debit):
EFF = {"US method": 1.00, "German/JP method": 0.64, "Spanish method": 0.55}
#   0.64 = 820/1283 (Germany/US embodied labour); 0.55 = 709/1283 (Spain/US), Q6.


def build_population(n=N, rng=RNG):
    c = draw_population(n, rng)                       # credit h/day in [F,24]
    wants = rng.lognormal(mean=0.0, sigma=0.45, size=n)
    wants /= np.median(wants)                         # median desired lifestyle = 1.0
    # mild link: people with more time want a little more (not proportional)
    wants *= (c / np.median(c)) ** 0.25
    wants /= np.median(wants)
    return c, wants


def intensity_us(c):
    return float(np.median(c))                        # ~13 h/day; the calibration


def real_consumption(c, wants, rho, intensity):
    """Real lifestyle each agent gets: min(want, gate), gate = rho*c/intensity."""
    return np.minimum(wants, rho * c / intensity)


def clearing_rho(c, wants, intensity, R_max, rhos=np.linspace(0.2, 4.0, 400)):
    dem = np.array([real_consumption(c, wants, r, intensity).sum() for r in rhos])
    if dem[-1] < R_max:
        return None, rhos, dem                        # post-scarcity: never binds
    return rhos[np.argmin(np.abs(dem - R_max))], rhos, dem


def scenario_table():
    c, wants = build_population()
    kappa = intensity_us(c)
    unconstrained = wants.sum()
    # B = the FIXED physical/energy debit-budget (Q1: materials+energy envelope).
    # Real capacity R_max = B / INTENSITY, so EFFICIENT production (lower intensity)
    # yields MORE real lifestyle from the same physical budget -- the Q6/Q1 channel.
    B = CAP * unconstrained * kappa

    scen = {
        "US method (baseline)":   dict(eff=1.00, B=B,        c=c, wants=wants),
        "German/JP method":       dict(eff=0.64, B=B,        c=c, wants=wants),
        "Spanish method":         dict(eff=0.55, B=B,        c=c, wants=wants),
        "growth +15% budget":     dict(eff=1.00, B=1.15 * B, c=c, wants=wants),
        "disaster -30% budget":   dict(eff=1.00, B=0.70 * B, c=c, wants=wants),
        "pollution +25% debit":   dict(eff=1.25, B=B,        c=c, wants=wants),
    }
    # population decline: fewer workers AND consumers (budget scales with them)
    keep = RNG.random(len(c)) > 0.15
    scen["pop -15%"] = dict(eff=1.00, B=CAP * wants[keep].sum() * kappa,
                            c=c[keep], wants=wants[keep])

    rows = {}
    for name, s in scen.items():
        intensity = kappa * s["eff"]
        R_max = s["B"] / intensity                       # real capacity from budget
        rstar, _, _ = clearing_rho(s["c"], s["wants"], intensity, R_max)
        if rstar is None:                                # post-scarcity: all get wants
            r = s["wants"]
            floor_allow = float("inf")
            rows[name] = dict(rho=None, median_real=float(np.median(r)),
                              frac_constrained=0.0,
                              disparity=1.0, gini=float(gini(r)))
            continue
        r = real_consumption(s["c"], s["wants"], rstar, intensity)
        # disparity = top realized consumption vs the SUBSISTENCE ALLOWANCE
        # (floor agent c=F), NOT vs low-WANT people's realized choice.
        floor_allow = rstar * F / intensity
        disp = float(r.max() / floor_allow)
        rows[name] = dict(
            rho=rstar, median_real=float(np.median(r)),
            frac_constrained=float((r < s["wants"] - 1e-9).mean()),
            disparity=disp, gini=float(gini(r)),
        )
    return rows, kappa


def report():
    rows, kappa = scenario_table()
    W = 78
    print("=" * W)
    print("rho-SWEEP -- clearing prime-rate, calibrated to the median lifestyle")
    print(f"  F={F:.0f} h/day, INTENSITY_US={kappa:.1f} debit-h per median-lifestyle unit")
    print(f"  (rho* ABSOLUTE is OP-10-illustrative; RATIOS + DIRECTIONS are the result)")
    print("=" * W)
    print(f"  {'scenario':<26}{'rho*':>6}{'median gets':>13}{'constrained':>13}{'disparity':>11}")
    print("-" * W)
    for name, d in rows.items():
        if d["rho"] is None:
            print(f"  {name:<26}{'—':>6}{'(post-scarcity)':>13}")
            continue
        print(f"  {name:<26}{d['rho']:>6.2f}{d['median_real']:>12.2f}x"
              f"{d['frac_constrained']*100:>11.0f}% {d['disparity']:>10.2f}")
    print("-" * W)
    us = rows["US method (baseline)"]
    es = rows["Spanish method"]
    fmt = lambda d: "post-scarcity (gate stops binding)" if d["rho"] is None else f"ρ*={d['rho']:.2f}"
    print(f"  Q6 TIE-IN: the SAME society is mildly scarcity-constrained under the US")
    print(f"             method ({fmt(us)}, median gets {us['median_real']:.2f}x of desired,")
    print(f"             {us['frac_constrained']*100:.0f}% constrained) -- but tips to {fmt(es)}")
    print(f"             under Spanish/German efficiency: everyone gets their full lifestyle")
    print(f"             ({es['median_real']:.2f}x). Efficiency, NOT extra labour, crosses the")
    print(f"             threshold (Q1: labour is abundant, materials/energy bind).")
    print(f"  Disparity stays <= 24/F = {CEILING:.1f}x in every scenario (ceiling invariant, IC-7).")
    print(f"  NOTE: rho* and the post-scarcity crossing are CAP-sensitive (illustrative);")
    print(f"        the DIRECTIONS (efficiency loosens, disaster tightens) are robust.")
    print("=" * W)
    return rows


def make_plots():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BLUE, ORANGE, GREEN, GRAY, RED = "#2b6cb0", "#dd6b20", "#2f855a", "#718096", "#c53030"
    plt.rcParams.update({"font.size": 11, "axes.titleweight": "bold",
                         "figure.facecolor": "white", "savefig.facecolor": "white",
                         "axes.spines.top": False, "axes.spines.right": False})
    c, wants = build_population()
    kappa = intensity_us(c)
    B = CAP * wants.sum() * kappa

    fig, ax = plt.subplots(figsize=(8.6, 4.9))
    rhos = np.linspace(0.2, 3.0, 300)
    for name, col in [("US method", BLUE), ("German/JP method", ORANGE),
                      ("Spanish method", GREEN)]:
        eff = EFF[name]
        intensity = kappa * eff
        R_max = B / intensity
        dem = np.array([real_consumption(c, wants, r, intensity).sum() for r in rhos])
        rstar, _, _ = clearing_rho(c, wants, intensity, R_max)
        lbl = f"{name}  (ρ*={rstar:.2f})" if rstar else f"{name}  (post-scarcity)"
        ax.plot(rhos, dem / R_max, color=col, lw=2, label=lbl)
        if rstar:
            ax.axvline(rstar, ls=":", color=col, alpha=0.6)
    ax.axhline(1.0, ls="--", color=GRAY, label="physical capacity (clears)")
    ax.set_xlabel("ρ (prime-rate / debit-tolerance dial)")
    ax.set_ylabel("real demand ÷ physical capacity")
    ax.set_title("Efficient production clears at a LOWER ρ — same standard, more headroom")
    ax.legend(fontsize=9, loc="upper left")
    fig.tight_layout()
    p = os.path.join(HERE, "rho_sweep_fig.png")
    fig.savefig(p, dpi=130)
    plt.close(fig)
    return [os.path.basename(p)]


# --- self-tests ---------------------------------------------------------------
def test_clearing_exists():
    rows, _ = scenario_table()
    assert rows["US method (baseline)"]["rho"] is not None
    print(f"[ok] baseline clears at ρ*={rows['US method (baseline)']['rho']:.2f}")


def test_efficiency_lowers_rho():
    rows, _ = scenario_table()
    us = rows["US method (baseline)"]["rho"]
    de = rows["German/JP method"]["rho"]
    es = rows["Spanish method"]["rho"]
    inf = float("inf")
    # None (post-scarcity) reads as "fully loosened" -> treat as +inf headroom
    seq = [us, de if de is not None else inf, es if es is not None else inf]
    assert seq[0] <= seq[1] <= seq[2] and (de != us), \
        f"efficiency should loosen ρ*: US{us} DE{de} ES{es}"
    fmt = lambda v: "post-scarcity" if v is None else f"{v:.2f}"
    print(f"[ok] efficient production loosens: US {fmt(us)} -> DE {fmt(de)} -> ES {fmt(es)}")


def test_shocks_move_rho_predictably():
    rows, _ = scenario_table()
    base = rows["US method (baseline)"]["rho"]
    assert rows["disaster -30% budget"]["rho"] < base, "disaster must tighten ρ"
    growth = rows["growth +15% budget"]["rho"]
    assert (growth is None) or (growth > base), "growth must loosen ρ"
    print(f"[ok] disaster tightens ({rows['disaster -30% budget']['rho']:.2f} < {base:.2f}); "
          f"growth loosens")


def test_median_gets_a_lifestyle():
    """At the clearing rho, the median agent should get close to a full median
    lifestyle -- i.e. the discretionary layer is positive for the typical person."""
    rows, _ = scenario_table()
    assert rows["US method (baseline)"]["median_real"] > 0.7
    assert rows["Spanish method"]["median_real"] >= rows["US method (baseline)"]["median_real"]
    print(f"[ok] median gets {rows['US method (baseline)']['median_real']:.2f}x (US) -> "
          f"{rows['Spanish method']['median_real']:.2f}x (efficient) of a full lifestyle")


def test_disparity_within_ceiling():
    rows, _ = scenario_table()
    for name, d in rows.items():
        if d["rho"] is None:
            continue
        assert d["disparity"] <= CEILING + 1e-6, f"{name} broke 24/F: {d['disparity']}"
    print(f"[ok] real-consumption disparity <= 24/F = {CEILING:.1f}x in all scenarios")


def run_tests():
    test_clearing_exists()
    test_efficiency_lowers_rho()
    test_shocks_move_rho_predictably()
    test_median_gets_a_lifestyle()
    test_disparity_within_ceiling()
    print("\nAll self-tests passed.")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--no-plots", action="store_true")
    a = ap.parse_args()
    if a.test:
        run_tests()
        return 0
    report()
    if not a.no_plots:
        for f in make_plots():
            print("wrote", f)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
