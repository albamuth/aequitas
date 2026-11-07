#!/usr/bin/env python3
"""critical_cap.py -- at what capacity/wants ratio does the band's top edge reach break-even?

Deleting a year pays at the top edge iff 365*F*rho*(F) < d.  E_max(F) = 365*F*rho*(F) rises with CAP.
Bisect CAP for E_max(F) = d at F = 2, 6, 10, 14.  Run: python critical_cap.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "stable-band"))
import stable_band as sb
import stable_band_cumulative as sc

w, x = sb.build_people(sb.N, seed=sb.RNG_SEED)
kappa = 1380.0 / 365.0

def emax(F, cap):
    v, flag = sc.edge_one_day(w, x, F, kappa, cap * x.sum())
    return 365.0 * F * v, flag

for F in (2.0, 6.0, 10.0, 14.0):
    lo, hi = 0.5, 0.99
    for _ in range(14):
        mid = 0.5 * (lo + hi)
        e, _f = emax(F, mid)
        if e < 1380.0:
            lo = mid
        else:
            hi = mid
    print(f"F={F:g}: E_max reaches 1,380 h at CAP = {0.5*(lo+hi):.3f}  (E_max there {emax(F, 0.5*(lo+hi))[0]:,.0f})")
for cap in (0.85, 0.90, 1.00):
    e, f = emax(10.0, cap)
    print(f"CAP {cap}: E_max(10) = {e:,.0f} h  flag '{f}'")
