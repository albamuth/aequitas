"""
run_scenario.py -- run a STATERA scenario from a settings file you can hand-edit.

WHAT THIS IS. The human-facing front door to `statera.py`. You write a small TOML
file describing a population, some dials, and how long to run; this reads it and
prints a table. No Python required to use it.

    python run_scenario.py scenarios/baseline.toml
    python run_scenario.py scenarios/baseline.toml --check     # validate only

THE ONE HARD RULE, AND IT IS THE SAME ONE THE GUI WILL HAVE.

    THIS FILE CONTAINS NO RULES.

It reads settings, calls Statera, and formats what comes back. If it ever computes
a standing, a gate, or a split by itself there are two implementations of Aequitas
and they will drift. A second implementation is a second theory.

WHY TOML AND NOT JSON. Because a settings file a human edits should be able to
explain itself, and JSON cannot carry a comment. Every dial in `scenarios/` is
documented in the file beside the value it sets.

UNKNOWN KEYS ARE AN ERROR. Never ignored. Silently accepting a typo is how a
scenario quietly stops testing what its author thought it tested.
"""
from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path

import numpy as np

from statera import (Kernel, Dials, Conformance, ConformanceError, DIMS, DAY,
                     collapse, ceiling, draw_population)

# =============================================================================
# The schema -- every key a scenario may carry, and nothing else
# =============================================================================

SCHEMA = {
    "name":       {"type": str,   "required": True},
    "seed":       {"type": int,   "required": True},
    "periods":    {"type": int,   "required": True},
    "period":     {"keys": {"days": float}},
    "population": {"keys": {"n": int, "mode": str, "headcount_each": float}},
    "dials":      {"keys": {"rho": float, "floor_h": float},
                   "tables": {"weights": {d: float for d in DIMS}}},
    "want":       {"keys": {"mode": str, "hours_per_day": float}},
    "report":     {"keys": {"every": int, "cohorts": bool}},
    "cohort":     {"array": {"name": str, "rate_h": float, "headcount": float,
                             "born": int, "lifespan": float}},
}

POPULATION_MODES = ("draw", "cohorts")
WANT_MODES = ("unbounded", "fixed", "none")


class ScenarioError(ValueError):
    """The file is malformed. Say which key and why, never 'invalid scenario'."""


def _check_keys(got: dict, allowed, where: str):
    unknown = set(got) - set(allowed)
    if unknown:
        raise ScenarioError(
            f"{where}: unknown key(s) {sorted(unknown)}. "
            f"Allowed here: {sorted(allowed)}. "
            f"Unknown keys are an error so a typo cannot silently change a run.")


def load(path: Path) -> dict:
    """Read and validate. Every failure names the key and says what was expected."""
    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as e:
        raise ScenarioError(f"{path.name} is not valid TOML: {e}") from None

    _check_keys(raw, SCHEMA, path.name)
    for key, spec in SCHEMA.items():
        if spec.get("required") and key not in raw:
            raise ScenarioError(
                f"{path.name}: '{key}' is required. "
                + ("A run that cannot be repeated exactly is not a scenario."
                   if key == "seed" else ""))
    for key, spec in SCHEMA.items():
        if key not in raw or "keys" not in spec:
            continue
        allowed = set(spec["keys"]) | set(spec.get("tables", {}))
        _check_keys(raw[key], allowed, f"{path.name} [{key}]")
        for tname, tspec in spec.get("tables", {}).items():
            if tname in raw[key]:
                _check_keys(raw[key][tname], tspec, f"{path.name} [{key}.{tname}]")
    for c in raw.get("cohort", []):
        _check_keys(c, SCHEMA["cohort"]["array"], f"{path.name} [[cohort]]")

    pop_mode = raw.get("population", {}).get("mode", "draw")
    if pop_mode not in POPULATION_MODES:
        raise ScenarioError(f"population.mode must be one of {POPULATION_MODES}")
    want_mode = raw.get("want", {}).get("mode", "unbounded")
    if want_mode not in WANT_MODES:
        raise ScenarioError(f"want.mode must be one of {WANT_MODES}")
    if pop_mode == "cohorts" and not raw.get("cohort"):
        raise ScenarioError(
            "population.mode = 'cohorts' but no [[cohort]] tables were given")
    if raw["periods"] < 1:
        raise ScenarioError("periods must be at least 1")
    return raw


# =============================================================================
# Building the kernel -- settings in, Statera out. No arithmetic of our own.
# =============================================================================

def build(scn: dict) -> Kernel:
    dials_in = scn.get("dials", {})
    dials = Dials(
        rho=float(dials_in.get("rho", 1.5)),
        floor_h=float(dials_in.get("floor_h", 10.0)),
        weights=dials_in.get("weights") or None,
        days_per_period=float(scn.get("period", {}).get("days", 1.0)),
    )
    pop = scn.get("population", {})
    mode = pop.get("mode", "draw")

    if mode == "draw":
        n = int(pop.get("n", 20_000))
        rng = np.random.default_rng(scn["seed"])
        rate = draw_population(n, dials.floor_h, rng=rng)
        weight = np.full(n, float(pop.get("headcount_each", 1.0)))
        born = np.zeros(n, np.int64)
        lifespan = np.full(n, np.inf)
    else:
        rows = scn["cohort"]
        n = len(rows)
        rate = np.array([float(c["rate_h"]) for c in rows])
        weight = np.array([float(c.get("headcount", 1.0)) for c in rows])
        born = np.array([int(c.get("born", 0)) for c in rows], np.int64)
        lifespan = np.array([float(c.get("lifespan", np.inf)) for c in rows])

    return Kernel(n, rate, dials, weight=weight, born=born, lifespan=lifespan)


def wants_for(scn: dict, k: Kernel):
    w = scn.get("want", {})
    mode = w.get("mode", "unbounded")
    if mode == "none":
        return None
    if mode == "unbounded":
        return np.full(k.n, 1e9)          # everyone consumes to their gate
    return np.full(k.n, float(w.get("hours_per_day", 4.0)))


# =============================================================================
# Reporting
# =============================================================================

def _fmt(x, width=12):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "-".rjust(width)
    if abs(x) >= 1e6:
        return f"{x:,.3e}".rjust(width)
    return f"{x:,.1f}".rjust(width)


def report(scn: dict, k: Kernel, hist: list) -> None:
    d = k.dials
    print("=" * 78)
    print(f"STATERA -- {scn['name']}")
    print("=" * 78)
    print(f"  seed {scn['seed']} · {k.n:,} cohorts · {len(hist)} periods of "
          f"{d.days_per_period:g} day(s)")
    print(f"  rho {d.rho:.2f} · floor {d.floor_h:.1f} h/day · "
          f"headcount {k.headcount():,.0f}")
    print()
    # "% refused" only means something against a finite appetite. Under
    # want.mode = "unbounded" everyone asks for more than exists, so it is
    # trivially 100% and reporting it as a finding would be a lie by column.
    want_mode = scn.get("want", {}).get("mode", "unbounded")
    show_refused = want_mode == "fixed"
    head = f"  {'period':>6}{'headcount':>12}{'credit h':>14}{'debit h':>14}{'top:bottom':>12}"
    print(head + ("   refused" if show_refused else ""))
    print("  " + "-" * (len(head) + (10 if show_refused else 0) - 2))
    every = max(1, int(scn.get("report", {}).get("every", 1)))
    for r in hist:
        if r["period"] % every and r is not hist[-1]:
            continue
        disp = r["cum_disparity"]
        disp_s = "-".rjust(12) if np.isnan(disp) else f"{disp:.4f}x".rjust(12)
        line = (f"  {r['period']:>6}{r['headcount']:>12,.0f}"
                f"{_fmt(r['credit_total'], 14)}{_fmt(r['debit_total'], 14)}{disp_s}")
        if show_refused:
            line += f"{r['refused_frac'] * 100:>9.0f}%"
        print(line)
    if every > 1:
        print(f"  (every {every}th period shown; all {len(hist)} were run and checked)")

    obs = [r["cum_disparity"] for r in hist if not np.isnan(r["cum_disparity"])]
    bound = ceiling(d.floor_h)
    print()
    print(f"  CONFORMANCE   every Foundations Sec.9 check asserted at every period "
          f"-- all passed")
    if want_mode == "unbounded":
        print(f"  APPETITE      unbounded -- everyone consumes to their gate. This is "
              f"the worst case,")
        print(f"                so '% refused' is trivially 100 and is not reported. "
              f"Set want.mode")
        print(f"                to 'fixed' to see who actually goes short.")
    if obs:
        drift = max(obs) - min(obs)
        filled = "filled" if abs(obs[-1] - bound) < 1e-6 else "NOT filled"
        print(f"  BOUND         24/F = {bound:.2f}x · observed {obs[-1]:.4f}x "
              f"({filled}) · drift {drift:.1e}")
    # Required by Foundations Sec.9 requirement 13 and Sec.5.1a: a quantity
    # computed over incomplete coverage is published as a FLOOR, with the gap
    # named. This line is not politeness; a run that cannot state its own
    # coverage is not reporting an Aequitas figure.
    # The CREDIT spread, which is what Sec.7.5 bounds when nobody has bought
    # anything yet. Reading max/min off a derived array is reporting, not a rule,
    # so it belongs here rather than in the kernel.
    live = k.alive(k.period - 1)
    C = k.proj.credit()[live]
    if C.size > 1 and C.min() > 0:
        spread = float(C.max() / C.min())
        print(f"  CREDIT SPREAD top {C.max():,.0f} h against bottom {C.min():,.0f} h "
              f"= {spread:.2f}x")
        if spread > bound + 1e-6:
            mult = spread / bound
            print(f"                That is {mult:.2f}x the rate bound of {bound:.2f}x, "
                  f"and the excess is AGE:")
            print(f"                time lived, not class (Foundations Sec.7.5).")

    w = d.weights or {"labour_h": 1.0}
    priced = [dim for dim in DIMS if w.get(dim, 0.0) != 0.0]
    print(f"  COVERAGE      this run prices {priced} only. Every cost figure "
          f"here is a FLOOR, never a value.")

    if scn.get("report", {}).get("cohorts") and k.n <= 20:
        names = [c.get("name", f"cohort {i}")
                 for i, c in enumerate(scn.get("cohort", []))] or \
                [f"cohort {i}" for i in range(k.n)]
        # Age at the END of the run: 60 periods lived is 60 years old, not 59.
        # `alive` above is masked at period-1 (who was alive FOR the last period);
        # the two indices are different questions and must not be shared.
        ages = k.age_years(k.period)
        D = collapse(k.proj.debit(), d.weights)
        print()
        print(f"  {'cohort':<24}{'age':>6}{'credit h':>14}{'debit h':>14}{'ratio':>9}")
        print("  " + "-" * 65)
        for i in range(k.n):
            r = D[i] / k.proj.credit()[i] if k.proj.credit()[i] > 0 else np.nan
            r_s = "-".rjust(9) if np.isnan(r) else f"{r:.2f}".rjust(9)
            print(f"  {names[i][:23]:<24}{ages[i]:>6.0f}"
                  f"{k.proj.credit()[i]:>14,.0f}{D[i]:>14,.0f}{r_s}")
    print("=" * 78)


# =============================================================================

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("scenario", type=Path, help="path to a .toml scenario")
    ap.add_argument("--check", action="store_true",
                    help="validate the file and stop; do not run")
    a = ap.parse_args()

    if not a.scenario.exists():
        print(f"no such scenario: {a.scenario}", file=sys.stderr)
        return 2
    try:
        scn = load(a.scenario)
    except ScenarioError as e:
        print(f"\n  ✗ {e}\n", file=sys.stderr)
        return 2
    if a.check:
        print(f"  ✓ {a.scenario.name} is valid: '{scn['name']}', "
              f"{scn['periods']} periods, seed {scn['seed']}")
        return 0

    k = build(scn)
    try:
        hist = k.run(scn["periods"], want=wants_for(scn, k))
    except ConformanceError as e:
        # A failure is a result. Say which requirement and at which period.
        print(f"\n  ✗ CONFORMANCE FAILED at period {k.period}: {e}\n",
              file=sys.stderr)
        return 1
    report(scn, k, hist)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
