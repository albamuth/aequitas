"""
anchor_sweep.py -- rho* at anchor = 1,350 / 1,380 / 1,400 and F = 2, 10, 14,
on both instruments, plus the tests that the anchor plumbing can fail.

Instrument A: disparity-ceiling/rho_sweep_anchor.py, baseline (no shock) clearing rate.
Instrument B: stable-band/stable_band_kappa.py, one-day edge and cumulative edge
              (mean of the declared age seeds). The cumulative edge scales BOTH
              kappa and the joiner's past debit with the anchor.

Run:  python anchor_sweep.py [--skip-stable-band] [--test]
Seeds are the instruments' own (population seed 7; age seeds sc.AGE_SEEDS).
"""
from __future__ import annotations

import os
import sys
import tempfile
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.normpath(os.path.join(HERE, ".."))
for sub in ("anchor-file", "disparity-ceiling", "stable-band"):
    sys.path.insert(0, os.path.join(SIM, sub))

import numpy as np                                           # noqa: E402
import anchor as A                                           # noqa: E402
import predictions as P                                      # noqa: E402
import rho_sweep_anchor as rs                                # noqa: E402

ANCHORS = (1350.0, 1380.0, 1400.0)
FLOORS = (2.0, 10.0, 14.0)


def sweep_a():
    out = {}
    for F in FLOORS:
        c, w = rs.build_population(F)
        unc = w.sum()
        for v in ANCHORS:
            k = A.kappa(A.load(value=v))
            dem = rs.demand_curve(c, w, kappa=k)
            out[(F, v)] = rs.clearing(dem, rs.CAP * unc)[0]
    return out


def sweep_b():
    import stable_band_kappa as sbk
    sc = sbk.sc
    w, x, kappa_old, R = sbk.setup()
    out = {}
    for F in FLOORS:
        for v in ANCHORS:
            k = A.kappa(A.load(value=v))
            od, fo, cv, cf = sbk.both_edges(w, x, R, F, k, past_rate=v)
            out[(F, v)] = (od, cv.mean(), cv.std())
    return out


def tests():
    n = 0
    # T1: a predictions file edited after registration is refused.
    with tempfile.TemporaryDirectory() as d:
        pp, lp = os.path.join(d, "p.json"), os.path.join(d, "log.jsonl")
        shutil.copy(P.PRED_PATH, pp)
        P.evaluate(lambda F, s, a: 0.33, pred_path=pp, log_path=lp)
        with open(pp, "a", encoding="utf-8") as fh:
            fh.write(" ")
        try:
            P.evaluate(lambda F, s, a: 0.33, pred_path=pp, log_path=lp)
        except P.PredictionsEditedError:
            n += 1
            print("[ok] T1 an edited predictions file is refused")
        else:
            raise AssertionError("edited predictions file was accepted")
    # T2: a prediction can fail (measure returns a wild value, result logged as failed).
    with tempfile.TemporaryDirectory() as d:
        pp, lp = os.path.join(d, "p.json"), os.path.join(d, "log.jsonl")
        shutil.copy(P.PRED_PATH, pp)
        res = P.evaluate(lambda F, s, a: 0.9, pred_path=pp, log_path=lp)
        assert any(not ok for _, _, ok in res)
        n += 1
        print(f"[ok] T2 predictions can fail: {sum(not ok for _, _, ok in res)}/{len(res)} fail at a wild value")
    # T3: the digest pin fires on a changed anchor file.
    with open(A.ANCHOR_PATH, "rb") as fh:
        raw = fh.read()
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "a.json")
        with open(p, "wb") as fh:
            fh.write(raw.replace(b"1350.0", b"1349.0", 1))
        try:
            A.load(path=p)
        except A.AnchorDigestError:
            n += 1
            print("[ok] T3 a changed interval fails the digest pin")
        else:
            raise AssertionError("digest pin did not fire")
    # T4: the loaded file value drives kappa (no typed 1380 behind it).
    assert abs(A.kappa(A.load(value=1400.0)) * 365 - 1400.0) < 1e-9
    assert A.load()["overridden"] is False and A.load(value=1400.0)["overridden"] is True
    n += 1
    print("[ok] T4 kappa follows the anchor value and an override is flagged")
    # T5: neither sim file types the anchor as a literal assignment any more.
    import re
    for rel in ("disparity-ceiling/rho_sweep_anchor.py", "stable-band/stable_band_kappa.py"):
        src = open(os.path.join(SIM, rel), encoding="utf-8").read()
        bad = [m.group(0) for m in re.finditer(r"^[A-Z_]+\s*=\s*1,?380(\.0)?\b.*$", src, re.M)]
        assert not bad, (rel, bad)
    n += 1
    print("[ok] T5 no module-level 1380 assignment in the two sim files")
    print(f"[ok] {n}/5 anchor-plumbing tests green")


def main():
    if "--test" in sys.argv:
        tests()
        return
    a = A.load()
    print(f"anchor v{a['version']} value {a['value']:g} interval "
          f"{a['interval']['low']:g}-{a['interval']['high']:g} sha256 {a['sha256']}")
    print("unrecomputable-from-public-files inputs: see median_lifestyle_anchor.json 'inputs'")
    da = sweep_a()
    print("\nA. rho_sweep_anchor.py baseline rho* (grid step 0.01)")
    print(f"  {'F':>4} | " + " | ".join(f"anchor {int(v):>5}" for v in ANCHORS) + " | span | x(1350/1380 scale) | x(1400/1380 scale)")
    for F in FLOORS:
        r = [da[(F, v)] for v in ANCHORS]
        s1, s2 = r[1] * 1350 / 1380, r[1] * 1400 / 1380
        print(f"  {int(F):>4} | " + " | ".join(f"{x:>12.2f}" for x in r)
              + f" | {r[2]-r[0]:.2f} | {s1:>17.3f} | {s2:>17.3f}")
    if "--skip-stable-band" in sys.argv:
        return
    db = sweep_b()
    print("\nB. stable_band_kappa.py one-day edge | cumulative edge mean (sd over age seeds)")
    print(f"  {'F':>4} | " + " | ".join(f"anchor {int(v):>5}" for v in ANCHORS))
    for F in FLOORS:
        print(f"  {int(F):>4} | " + " | ".join(
            f"{db[(F, v)][0]:.3f} | {db[(F, v)][1]:.3f} ({db[(F, v)][2]:.4f})" for v in ANCHORS))
    print("\nrelative step 1380->1400 (should be 1400/1380 - 1 = +1.45%) and 1350->1380 (+2.22%):")
    for F in FLOORS:
        o = [db[(F, v)][0] for v in ANCHORS]
        print(f"  F={int(F):>2} one-day  {o[1]/o[0]-1:+.2%}  {o[2]/o[1]-1:+.2%}")


if __name__ == "__main__":
    main()
