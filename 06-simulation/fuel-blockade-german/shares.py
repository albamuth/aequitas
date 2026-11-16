#!/usr/bin/env python3
"""
shares.py -- fossil-energy share of total input, per German product line, from EXIOBASE 3.10.2 pxp 2022.

Reads 06-simulation/data/exiobase/IOT_2022_pxp.zip in place (never copied). Writes only a small cache
(de_fossil_shares.npz, a few KB) next to this file.

  direct share d_p    = sum over fossil products f (all 49 regions) of Z[f, DE_p] / x[DE_p]
  upstream share t_p  = d (I - A_DD)^-1, capped at 1  (adds domestic upstream fossil purchases; sensitivity)
  line share          = weighted mean of d_p over the line's products, weights = German household final demand
                        (fallback x[DE_p] when the line has no household demand)

Run:  python shares.py            (builds cache, prints the line table; about 1-2 minutes)
      python shares.py --test     (self-tests)
"""
from __future__ import annotations

import itertools
import os
import sys
import zipfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ZIP = os.path.join(os.path.dirname(HERE), "data", "exiobase", "IOT_2022_pxp.zip")
CACHE = os.path.join(HERE, "de_fossil_shares.npz")
NS = 200

FOSSIL = (list(range(19, 31)) + list(range(63, 84)) + [127, 128, 132] + list(range(141, 145)) + [146])

# line -> product indices (EXIOBASE product order, 0-based)
LINES = {
    "food": list(range(0, 15)) + [18] + list(range(42, 53)),
    "clothing": [54, 55, 56],
    "shelter services": [167],
    "utilities": list(range(127, 139)) + [139, 140, 146, 148],
    "drugs": [89],
    "housing structure": [149],
    "chemicals paper plastics": [61, 85, 89, 95],
    "furniture and other goods": [96, 98, 116, 118, 119, 120, 124],
    "care": [174],
    "schooling": [173],
    "land transport services": [156, 157],
    "post and telecoms": [163],
}
# goods essentials hours (US method, h/yr): essentials-basket/RESULTS.md. housing structure 31 (E 523) or 61 (E 553).
ESS_HOURS = {"food": 131, "clothing": 121, "shelter services": 38, "utilities": 21, "drugs": 30,
             "housing structure": None, "chemicals paper plastics": 73, "furniture and other goods": 78}
SERV_HOURS = {"care": 253, "schooling": 87, "land transport services": 59, "post and telecoms": 13}


def _names():
    z = zipfile.ZipFile(ZIP)
    return [l.decode().split("\t")[1] for l in itertools.islice(z.open("unit.txt"), 1, NS + 1)]


def _regions():
    z = zipfile.ZipFile(ZIP)
    with z.open("x.txt") as f:
        f.readline()
        regs = []
        for l in f:
            r = l.split(b"\t", 1)[0].decode()
            if not regs or regs[-1] != r:
                regs.append(r)
    return regs


def build():
    z = zipfile.ZipFile(ZIP)
    regs = _regions()
    k = regs.index("DE")
    # x for DE
    with z.open("x.txt") as f:
        f.readline()
        xs = np.array([float(l.split(b"\t")[2]) for l in itertools.islice(f, k * NS, (k + 1) * NS)])
    # Z: fossil rows (all regions) and DE rows, DE columns only
    fossil_rows = {r * NS + p for r in range(len(regs)) for p in FOSSIL}
    de_rows = set(range(k * NS, (k + 1) * NS))
    need = fossil_rows | de_rows
    c0 = 2 + k * NS
    foss_sum = np.zeros(NS)
    zdd = np.zeros((NS, NS))
    with z.open("Z.txt") as f:
        for _ in range(3):
            f.readline()
        for i, line in enumerate(f):
            if i not in need:
                continue
            v = np.array(line.split(b"\t")[c0:c0 + NS], dtype=float)
            if i in fossil_rows:
                foss_sum += v
            if i in de_rows:
                zdd[i - k * NS] = v
    # Y: DE household final demand (category 0) for DE rows
    yh = np.zeros(NS)
    with z.open("Y.txt") as f:
        for _ in range(3):
            f.readline()
        for i, line in enumerate(f):
            if i < k * NS:
                continue
            if i >= (k + 1) * NS:
                break
            yh[i - k * NS] = float(line.split(b"\t")[2 + 7 * k])
    # energy extension, DE columns
    en = {}
    with z.open("energy/F.txt") as f:
        for _ in range(3):
            f.readline()
        for line in f:
            if not line.strip():
                continue
            parts = line.rstrip(b"\n").split(b"\t")
            en[parts[0].decode()] = np.array(parts[1 + k * NS:1 + (k + 1) * NS], dtype=float)
    np.savez(CACHE, x=xs, foss=foss_sum, zdd=zdd, yh=yh, en_emis=en["Energy use - Emission relevant"],
             en_gross=en["Energy use - Gross"])
    return load()


def load():
    if not os.path.exists(CACHE):
        return build()
    d = np.load(CACHE)
    return {k: d[k] for k in d.files}


def shares(data=None):
    d = data or load()
    x = d["x"]
    with np.errstate(divide="ignore", invalid="ignore"):
        direct = np.where(x > 0, d["foss"] / x, 0.0)
        A = np.where(x[None, :] > 0, d["zdd"] / x[None, :], 0.0)
    direct = np.clip(direct, 0.0, 1.0)
    up = np.clip(direct @ np.linalg.inv(np.eye(NS) - A), 0.0, 1.0)
    return direct, up


def line_share(prod_share, idx, data=None):
    d = data or load()
    w = d["yh"][idx]
    if w.sum() <= 0:
        w = d["x"][idx]
    return float((prod_share[idx] * w).sum() / w.sum()) if w.sum() > 0 else 0.0


def non_ess_share(prod_share, data=None):
    d = data or load()
    used = set(i for v in LINES.values() for i in v)
    idx = [i for i in range(NS) if i not in used and d["yh"][i] > 0]
    w = d["yh"][idx]
    return float((prod_share[idx] * w).sum() / w.sum()), len(idx), float(w.sum())


def all_line_shares(which="direct", data=None):
    d = data or load()
    direct, up = shares(d)
    ps = direct if which == "direct" else up
    out = {n: line_share(ps, idx, d) for n, idx in LINES.items()}
    ne, n_prod, w = non_ess_share(ps, d)
    out["non-essentials"] = ne
    return out


# ---------------------------------------------------------------- self-tests
def _spearman(a, b):
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def run_tests():
    d = load()
    names = _names()
    x = d["x"]
    direct, up = shares(d)
    # 1 the fossil list names what it should
    for i in (19, 27, 28, 66, 71, 127, 128, 132, 146):
        assert any(w in names[i] for w in ("Coal", "Anthracite", "Crude", "Natural gas", "Gasoline", "Diesel", "Electricity by coal",
                                           "Electricity by gas", "petroleum", "gaseous", "Distribution")), names[i]
    assert "Electricity by nuclear" in names[129] and 129 not in FOSSIL and 84 not in FOSSIL and 145 not in FOSSIL
    print("[ok] 1. fossil list: coal, crude, gas, petroleum, coal/gas/oil power, gas mains in; nuclear, biogas out")
    # 2 shares are fractions and the table is not trivial
    assert 0 <= direct.min() and direct.max() <= 1 and (direct > 0).sum() > 50 and (direct == 0).sum() > 10
    print(f"[ok] 2. direct shares in [0,1]; {(direct > 0).sum()} of {NS} products buy some fossil energy")
    # 3 the energy extension on disk is empty (the blocker). If it is ever populated this test fails and the
    #   request's own source should be used instead of the Z-matrix substitute.
    assert float(np.abs(d["en_emis"]).sum() + np.abs(d["en_gross"]).sum()) == 0.0, "energy table now has data: use it"
    print("[ok] 3. energy/F.txt DE columns are all zero (emission-relevant and gross): the requested table is not usable")
    # 3b ranking sanity inside the substitute: a coal power plant buys far more fossil input than a wind farm
    assert direct[127] > 3 * max(direct[131], 1e-9), (direct[127], direct[131])
    print(f"[ok] 3b. electricity by coal direct share {direct[127]:.3f} against wind {direct[131]:.4f}")
    # 4 sanity: petroleum refining buys far more fossil than clothing
    assert direct[66] > 10 * max(direct[55], 1e-9), (direct[66], direct[55])
    print(f"[ok] 4. motor gasoline direct share {direct[66]:.3f} against clothing {direct[55]:.4f}")
    # 5 upstream share is never below direct share
    assert np.all(up >= direct - 1e-12)
    print("[ok] 5. adding domestic upstream never lowers a share")
    # 6 line weights sum to something real
    for n, idx in LINES.items():
        assert (d["yh"][idx].sum() > 0) or (x[idx].sum() > 0), n
    print("[ok] 6. every line has household demand or output to weight by")
    print("\nAll self-tests passed.")


if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        if "--rebuild" in sys.argv and os.path.exists(CACHE):
            os.remove(CACHE)
        d = load()
        for which in ("direct", "up"):
            print(f"\nline fossil share ({which}):")
            for n, v in all_line_shares(which, d).items():
                print(f"  {n:28s} {v:7.4f}")
