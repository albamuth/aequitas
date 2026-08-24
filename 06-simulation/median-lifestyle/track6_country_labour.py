"""
track6_country_labour.py -- Q6, part A: the LABOUR cost of a national lifestyle,
compared across first-world countries, from one consistent multi-regional table.

QUESTION. For each rich country, how many human labour-hours (domestic + imported,
worked ANYWHERE on Earth) are embodied in the average resident's household
consumption? Divide a material-standard indicator by that to ask: who delivers
the most material benefit per hour of labour commanded -- i.e. who is most
EFFICIENT in the Aequitas-native unit (credit = hours, A2)?

DATA. EXIOBASE 3, 2022, pxp (on disk, data/exiobase/IOT_2022_pxp.zip). 49 regions
  x 200 products. Satellites used: EMPLOYMENT HOURS (M.hr) and ENERGY (TJ, for a
  physical cross-check). Multi-regional, so imported labour is captured natively.

METHOD (compute the total-intensity vector ONCE, apply to every country).
  e   = hours-intensity per M-EUR output          (sum of the 6 hours rows / x)
  m   solves  (I - A)^T m = e     =>  m = e (I - A)^-1
      m_j = total (direct+indirect, all-region) hours embodied per M-EUR of
            final demand delivered by sector j. One solve serves all countries.
  For country c:  embodied hours = m . Y_c(households)   [M.hr]
                  per capita     = embodied hours * 1e6 / population_c
  Same machinery with the energy satellite -> embodied primary energy GJ/capita
  (physical cross-check: US should land near the ~290 GJ/cap figure).

OUTPUT. data cache track6_country_result.json for the efficiency ranking script.

Run:  python track6_country_labour.py            # parse + solve + dump (slow)
      python track6_country_labour.py --show       # print cached table
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ZIP = os.path.join(os.path.dirname(HERE), "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "track6_country_result.json")
HH = "Final consumption expenditure by households"

# 2022 mid-year population, millions (World Bank / UN order; archived in Q6.md).
POP_M = {
    "US": 333.3, "DE": 83.8, "FR": 68.0, "GB": 67.0, "IT": 59.0, "ES": 47.8,
    "SE": 10.5, "NL": 17.7, "DK": 5.9, "NO": 5.5, "FI": 5.55, "CH": 8.8,
    "AT": 9.0, "BE": 11.6, "IE": 5.1, "PT": 10.3, "PL": 37.7, "CA": 38.9,
    "AU": 26.0, "JP": 125.0, "KR": 51.6, "CZ": 10.5, "GR": 10.4,
}


def compute(save: bool = True) -> dict:
    import pymrio
    print("parsing EXIOBASE 3 (610MB Z; ~2 min)...")
    exio = pymrio.parse_exiobase3(path=ZIP)

    x = exio.x["indout"].values.astype(np.float64)
    idx = exio.Z.index
    # technical coefficients A = Z * diag(1/x), built directly (parse doesn't)
    Z = exio.Z.values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        inv_x = np.where(x > 0, 1.0 / x, 0.0)
    A = Z * inv_x[np.newaxis, :]
    del Z

    def intensity(F, match, exact=False):
        if exact:
            rows = [s for s in F.index if str(s) == match]
        else:
            rows = [s for s in F.index if str(s).startswith(match)]
        assert rows, f"no rows for {match}"
        tot = F.loc[rows].sum(axis=0).values.astype(np.float64)
        with np.errstate(divide="ignore", invalid="ignore"):
            return np.where(x > 0, tot / x, 0.0)

    e_hours = intensity(exio.employment.F, "Employment hours")   # M.hr / M-EUR
    # energy: single row "Energy use - Gross" (EXIOBASE 2022 vintage: all zeros).
    e_energy = intensity(exio.energy.F, "Energy use - Gross", exact=True)  # TJ/M-EUR
    # FOSSIL CO2 (kg): combustion + cement + lime + fossil-waste; EXCLUDE biogenic.
    F_air = exio.air_emissions.F
    co2_rows = [s for s in F_air.index if str(s) in (
        "CO2 - combustion - air",
        "CO2 - non combustion - Cement production - air",
        "CO2 - non combustion - Lime production - air",
        "CO2 - waste - fossil - air")]
    assert co2_rows, "no fossil CO2 rows"
    co2_tot = F_air.loc[co2_rows].sum(axis=0).values.astype(np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        e_co2 = np.where(x > 0, co2_tot / x, 0.0)   # kg CO2 / M-EUR

    print("solving (I-A)^T m = e  for labour and energy (two dense solves)...")
    ImA_T = (np.eye(A.shape[0]) - A).T
    m_hours = np.linalg.solve(ImA_T, e_hours)     # M.hr per M-EUR final demand
    m_energy = np.linalg.solve(ImA_T, e_energy)   # TJ  per M-EUR final demand
    m_co2 = np.linalg.solve(ImA_T, e_co2)         # kg CO2 per M-EUR final demand

    Y = exio.Y
    regions = np.array([r for r, _ in idx])
    out = {}
    for c in POP_M:
        cols = [col for col in Y.columns if col[0] == c and col[1] == HH]
        if not cols:
            continue
        y = Y[cols].sum(axis=1).values.astype(np.float64)
        emb_hours_Mhr = float(m_hours @ y)
        emb_energy_TJ = float(m_energy @ y)
        emb_co2_kg = float(m_co2 @ y)
        # domestic vs foreign hours (needs a per-country solve of x*)
        xstar = np.linalg.solve(np.eye(A.shape[0]) - A, y)
        emb_by_sector = e_hours * xstar
        is_dom = regions == c
        dom = float(emb_by_sector[is_dom].sum())
        for_ = float(emb_by_sector[~is_dom].sum())
        pop = POP_M[c] * 1e6
        out[c] = dict(
            hours_per_capita=emb_hours_Mhr * 1e6 / pop,
            energy_GJ_per_capita=emb_energy_TJ * 1e3 / pop,  # TJ=1e3 GJ (empty in 2022)
            co2_t_per_capita=emb_co2_kg / 1e3 / pop,          # kg -> t per capita
            foreign_share=for_ / (dom + for_) if (dom + for_) else 0.0,
            hh_fd_MEUR=float(y.sum()),
            population_m=POP_M[c],
        )
        print(f"  {c}: {out[c]['hours_per_capita']:.0f} h/cap, "
              f"{out[c]['co2_t_per_capita']:.1f} tCO2/cap, "
              f"foreign {out[c]['foreign_share']*100:.0f}%")
    if save:
        json.dump(out, open(CACHE, "w"), indent=2)
    return out


def show():
    r = json.load(open(CACHE))
    rows = sorted(r.items(), key=lambda kv: kv[1]["hours_per_capita"])
    W = 60
    print("=" * W)
    print("EMBODIED LABOUR & ENERGY IN HOUSEHOLD CONSUMPTION (EXIOBASE 2022)")
    print("  per capita/yr, domestic + imported")
    print("=" * W)
    print(f"  {'country':<8}{'h/cap':>8}{'GJ/cap':>9}{'foreign%':>10}")
    print("-" * W)
    for c, d in rows:
        print(f"  {c:<8}{d['hours_per_capita']:>8.0f}{d['energy_GJ_per_capita']:>9.0f}"
              f"{d['foreign_share']*100:>9.0f}%")
    print("=" * W)
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    show() if a.show and os.path.exists(CACHE) else compute()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
