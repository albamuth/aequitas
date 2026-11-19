"""Recompute the German / Japanese / Spanish median-lifestyle anchors.

The US anchor (1,380 h/yr) is measured. A peer anchor is never measured here:
it is the US anchor times a Q6 ratio (peer hours / US hours).
This script (1) reproduces the published 883 and 759 from the old
household-only ratios, (2) rebuilds them from the every-payer ratios,
(3) republishes break-even rho*F = anchor / 365.

Run:   python -I anchor_peers.py          (deterministic, no seed, ~1 s)
Test:  python -I anchor_peers.py --test
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ML = os.path.join(HERE, "..", "median-lifestyle")
Q6 = os.path.join(ML, "q6_payers_result.json")
US_ANCHOR = 1380.0
PUBLISHED = {"US": 1380.0, "DE": 883.0, "JP": 883.0, "ES": 759.0}  # c69742
PUBLISHED_BE = {"US": 3.78, "DE": 2.42, "JP": 2.42, "ES": 2.08}


def load():
    return json.load(open(Q6))


def compute(q):
    us_hh, us_aic = q["US"]["HH"], q["US"]["AIC_HOURS"]
    out = {}
    for c in ("US", "DE", "JP", "ES"):
        r_old = q[c]["HH"] / us_hh              # household only (withdrawn)
        r_new = q[c]["AIC_HOURS"] / us_aic      # every payer
        out[c] = dict(hh=q[c]["HH"], aic=q[c]["AIC_HOURS"], r_old=r_old,
                      r_new=r_new, anchor_old_rounded=round(r_old, 2) * US_ANCHOR,
                      anchor_old_exact=r_old * US_ANCHOR,
                      anchor_new=r_new * US_ANCHOR,
                      be_new=r_new * US_ANCHOR / 365.0)
    return out


def audit_no_allocation():
    """True if none of the Q6 scripts contains a co-product allocation step."""
    hits = []
    for f in ("q6_payers.py", "track6_country_labour.py", "track6_efficiency.py"):
        for i, line in enumerate(open(os.path.join(ML, f), encoding="utf-8"), 1):
            if re.search(r"alloc|co-?product", line, re.I):
                hits.append((f, i, line.strip()))
    return hits


def tests(q):
    r = compute(q)
    res = []
    def t(name, ok): res.append((name, ok))
    t("old DE ratio x1380, 2dp, reproduces published 883 (+-1)",
      abs(r["DE"]["anchor_old_rounded"] - 883) <= 1)
    t("old ES ratio x1380, 2dp, reproduces published 759 (+-1)",
      abs(r["ES"]["anchor_old_rounded"] - 759) <= 1)
    for c in ("US", "DE", "ES"):
        t(f"published break-even {c} = anchor/365 to 2dp",
          round(PUBLISHED[c] / 365, 2) == PUBLISHED_BE[c])
    t("every-payer DE ratio matches Foundations 0.836 (+-0.001)",
      abs(r["DE"]["r_new"] - 0.836) <= 0.001)
    t("every-payer JP ratio matches Foundations 0.836 (+-0.001)",
      abs(r["JP"]["r_new"] - 0.836) <= 0.001)
    t("US ratio is exactly 1", abs(r["US"]["r_new"] - 1) < 1e-12)
    t("no allocation step in the Q6 scripts", not audit_no_allocation())
    return res


def main():
    q = load()
    if "--test" in sys.argv:
        bad = 0
        for n, ok in tests(q):
            print(("PASS " if ok else "FAIL ") + n); bad += (not ok)
        sys.exit(1 if bad else 0)
    r = compute(q)
    print("country  hh_h  aic_h  r_old  r_new  old_pub  old_exact  new_anchor  be_old  be_new  move%")
    for c in ("US", "DE", "JP", "ES"):
        x = r[c]
        print(f"{c:7} {x['hh']:6.0f} {x['aic']:6.0f} {x['r_old']:6.3f} {x['r_new']:6.3f} "
              f"{PUBLISHED[c]:7.0f} {x['anchor_old_exact']:9.0f} {x['anchor_new']:10.0f} "
              f"{PUBLISHED_BE[c]:6.2f} {x['be_new']:6.2f} {100*(x['anchor_new']/PUBLISHED[c]-1):+6.1f}")
    print("allocation hits:", audit_no_allocation())
    for rho_f in ("DE", "JP", "ES"):
        pass
    # sensitivity: ratio of middle fifths, DE only (middle_fifth_result.json)
    mf = json.load(open(os.path.join(ML, "middle_fifth_result.json")))
    print("middle_fifth keys sample:", list(mf)[:5])


if __name__ == "__main__":
    main()
