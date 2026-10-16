"""
Fractional holdings -- what does one account carry when it holds PART of
several co-products of one joint process?

THE GAP (self-council, 2026-10-10, post #8335 on 1f916.ai). Foundations §3.4a
says a joint process's cost is not divided: every co-product carries the whole
cost of each step it passed through, and a ledger walk is a UNION over
identified parcels, never a sum. A SPLIT of one parcel divides it by mass. The
documents never said what a holding of 10% of the beef AND 10% of the hide
carries, because both parts point back at the same parcels.

THE RULE BEING TESTED ("max", nightcheck 2026-10-13, decision 5.3, after a
stress test). For each parcel (each step of the chain), per dimension:

    D_step = K_step x  max over products p that passed the step of  f_p

  where f_p is the mass fraction of co-product p in the account's SET, and the
  set is everything the account holds NOW plus everything it has CONSUMED.
  Fractions of one co-product ADD (two 5% pieces of beef are 10% of the beef);
  the max is taken ACROSS co-products. Consumed parts stay in the set forever.

WHY MAX (the stress test's derivation, which this file checks numerically).
Three requirements already in the documents leave no other rule:
  R1  one co-product alone carries its mass share     (§3.4a split rule)
  R2  holding more never carries less                  (monotonicity)
  R3  a whole output split into n identical bundles:
      the bundles add back to the whole                (conformance row 10c)
  For f_A >= f_B:  f_A = g(f_A,0) <= g(f_A,f_B) <= g(f_A,f_A) = f_A.

THE RIVALS, REPORTED SO THE SIZE OF EACH MISTAKE IS VISIBLE. NONE IS THE RULE.
  sum           f_A + f_B           conformance 10e forbids it
  independent   1 - prod(1 - f_p)   a probability model of which hours went where
  max_no_keep   max over HELD only  max without the consumed-parts change: the
                                    eater exploit

Run:   python 06-simulation/fractional-holdings/fractional_holdings.py
Test:  python 06-simulation/fractional-holdings/fractional_holdings.py --test
"""

import os
import random
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(_HERE), "chain-resolution"))

from chain_resolution import (  # noqa: E402
    DIMENSIONS,
    build_refinery,
    build_steer,
    buyer_union,
    contiguous_partitions,
)

TOL = 1e-9
SEED = 20261013
N_RANDOM = 4000


# ---------------------------------------------------------------------------
# One account's state, and the four ways to read it
# ---------------------------------------------------------------------------


def new_account(chain):
    return {"held": {p: 0.0 for p in chain.products},
            "eaten": {p: 0.0 for p in chain.products}}


def fractions(acct, keep_consumed=True):
    """f_p per co-product. Pieces of one co-product add."""
    return {p: acct["held"][p] + (acct["eaten"][p] if keep_consumed else 0.0)
            for p in acct["held"]}


def combine(fs, rule):
    fs = list(fs)
    if not fs:
        return 0.0
    if rule in ("max", "max_no_keep"):
        return max(fs)
    if rule == "sum":
        return sum(fs)
    if rule == "independent":
        out = 1.0
        for f in fs:
            out *= (1.0 - f)
        return 1.0 - out
    raise ValueError(rule)


def debit(chain, acct, rule="max"):
    """The account's debit vector at the finest resolution: one parcel per step."""
    f = fractions(acct, keep_consumed=(rule != "max_no_keep"))
    out = {d: 0.0 for d in DIMENSIONS}
    for step in chain.steps:
        share = combine((f[p] for p in chain.products if step.name in chain.passes[p]), rule)
        for d in DIMENSIONS:
            out[d] += getattr(step, d) * share
    return out


def total(chain):
    return {d: sum(getattr(s, d) for s in chain.steps) for d in DIMENSIONS}


def close(a, b, tol=TOL):
    return all(abs(a[d] - b[d]) <= tol * max(1.0, abs(b[d])) for d in DIMENSIONS)


def at_least(a, b, tol=TOL):
    return all(a[d] >= b[d] - tol * max(1.0, abs(b[d])) for d in DIMENSIONS)


# ---------------------------------------------------------------------------
# The cases
# ---------------------------------------------------------------------------


def cases():
    return [build_steer(), build_refinery()]


def random_account(chain, rng):
    a = new_account(chain)
    for p in chain.products:
        if rng.random() < 0.6:
            h = rng.random()
            e = rng.random() * (1.0 - h) if rng.random() < 0.5 else 0.0
            a["held"][p], a["eaten"][p] = h, e
    return a


# ---------------------------------------------------------------------------
# Self-tests. Each one can fail.
# ---------------------------------------------------------------------------


def test_reduces_to_the_union_rule():
    """f = 1 on every product a buyer takes is the existing §3.4a union."""
    n = 0
    for c in cases():
        rng = random.Random(SEED)
        for _ in range(200):
            taken = [p for p in c.products if rng.random() < 0.5] or [c.products[0]]
            a = new_account(c)
            for p in taken:
                a["held"][p] = 1.0
            finest = [(i, i + 1) for i in range(len(c.steps))]
            assert close(debit(c, a), buyer_union(c, taken, finest)), (c.name, taken)
            n += 1
    return f"max with f = 1 equals buyer_union on {n} random selections"


def test_reduces_to_the_split_rule():
    """One co-product alone carries its mass share of every step it passed."""
    n = 0
    for c in cases():
        for p in c.products:
            for f in (0.01, 0.1, 0.37, 0.5, 1.0):
                a = new_account(c)
                a["held"][p] = f
                want = {d: f * sum(getattr(s, d) for s in c.steps if s.name in c.passes[p])
                        for d in DIMENSIONS}
                assert close(debit(c, a), want), (c.name, p, f)
                n += 1
    return f"one co-product at fraction f carries f x its own steps, {n} cases"


def test_n_bundles_add_back_to_the_whole():
    """Row 10c on a whole holding. Max passes; the rivals are measured."""
    lines = []
    for c in cases():
        K = total(c)
        dim = "labour_h" if K["labour_h"] > 0 else "energy_mj"
        for n in (2, 10):
            a = new_account(c)
            for p in c.products:
                a["held"][p] = 1.0 / n
            got = {r: n * debit(c, a, r)[dim] / K[dim] for r in ("max", "independent", "sum")}
            assert abs(got["max"] - 1.0) < 1e-9, (c.name, n, got)
            assert got["independent"] > 1.0 + 1e-6, "independent unexpectedly passes 10c"
            lines.append(f"{c.name} n={n}: max {got['max']:.2f}, independent "
                         f"{got['independent']:.2f}, sum {got['sum']:.2f} wholes")
    return "n bundles of 1/n of everything: " + "; ".join(lines)


def test_monotone():
    """Adding any mass to the set never lowers the debit."""
    n = 0
    for c in cases():
        rng = random.Random(SEED + 1)
        for _ in range(N_RANDOM):
            a = random_account(c, rng)
            before = debit(c, a)
            p = rng.choice(c.products)
            room = 1.0 - a["held"][p] - a["eaten"][p]
            a["held"][p] += rng.random() * room
            assert at_least(debit(c, a), before), (c.name, p)
            n += 1
    return f"no addition lowered a debit, {n} random additions"


def test_never_above_one_whole_per_parcel():
    """A5: no holding carries more than each parcel's own cost."""
    n = 0
    for c in cases():
        rng = random.Random(SEED + 2)
        K = total(c)
        for _ in range(N_RANDOM):
            assert at_least(K, debit(c, random_account(c, rng)))
            n += 1
    return f"every one of {n} random holdings is at most the chain total"


def test_eating_never_lowers_and_selling_stops_at_what_was_eaten():
    """The eater: hold 50% of the hide, eat 50% of the beef, sell the hide."""
    c = build_steer()
    a = new_account(c)
    a["held"]["hide"] = 0.5
    a["held"]["packaged_beef"] = 0.5
    d0 = debit(c, a)
    a["held"]["packaged_beef"], a["eaten"]["packaged_beef"] = 0.0, 0.5
    d1 = debit(c, a)
    assert close(d1, d0), "eating changed the debit"
    a["held"]["hide"] = 0.0
    kept, lost = debit(c, a, "max"), debit(c, a, "max_no_keep")
    beef_all = {d: 0.5 * sum(getattr(s, d) for s in c.steps) for d in DIMENSIONS}
    assert close(kept, beef_all), kept
    assert lost["labour_h"] == 0.0
    return (f"after selling the hide: max carries {kept['labour_h']:.1f} h for the beef "
            f"eaten; max without the consumed-parts change carries {lost['labour_h']:.1f} h")


def test_order_does_not_matter():
    """Random sequences of buy, eat and sell reaching one state give one debit."""
    n = 0
    for c in cases():
        rng = random.Random(SEED + 3)
        for _ in range(500):
            target = random_account(c, rng)
            ops = []
            for p in c.products:
                h, e = target["held"][p], target["eaten"][p]
                extra = rng.random() * 0.2 * (1.0 - h - e)
                ops += [("buy", p, h + e + extra), ("eat", p, e), ("sell", p, extra)]
            finals = []
            for _ in range(4):
                rng.shuffle(ops)
                a = new_account(c)
                pending = list(ops)
                while pending:
                    for op in list(pending):
                        kind, p, q = op
                        if kind == "buy":
                            a["held"][p] += q
                        elif a["held"][p] + 1e-12 >= q:
                            a["held"][p] -= q
                            if kind == "eat":
                                a["eaten"][p] += q
                        else:
                            continue
                        pending.remove(op)
                finals.append(debit(c, a))
            assert all(close(f, finals[0], 1e-7) for f in finals), c.name
            assert close(finals[0], debit(c, target), 1e-7), c.name
            n += 1
    return f"{n} target states, each reached by 4 shuffled sequences, one debit each"


def test_splitting_across_accounts_never_pays():
    """The splitter: one holding divided between two accounts."""
    n, worst = 0, 0.0
    for c in cases():
        rng = random.Random(SEED + 4)
        for _ in range(N_RANDOM):
            whole = random_account(c, rng)
            a, b = new_account(c), new_account(c)
            for p in c.products:
                for part in ("held", "eaten"):
                    s = rng.random()
                    a[part][p] = whole[part][p] * s
                    b[part][p] = whole[part][p] * (1.0 - s)
            one, da, db = debit(c, whole), debit(c, a), debit(c, b)
            two = {d: da[d] + db[d] for d in DIMENSIONS}
            assert at_least(two, one)
            dim = "labour_h" if one["labour_h"] > 0 else "energy_mj"
            if one[dim] > 0:
                worst = max(worst, two[dim] / one[dim])
            n += 1
    return f"split never lowered the total, {n} random splits; it raised it up to {worst:.2f}x"


def test_per_parcel_not_per_process():
    """Change 2: the hide must not reach steps it never passed."""
    c = build_steer()
    a = new_account(c)
    a["held"]["packaged_beef"], a["held"]["hide"] = 0.1, 0.5
    per_step = debit(c, a)["energy_mj"]
    whole = 0.5 * total(c)["energy_mj"]
    assert per_step < whole - 1.0
    return (f"10% beef + 50% hide: per step {per_step:.1f} MJ; one max over the whole "
            f"process {whole:.1f} MJ")


def test_resolution_still_only_lowers():
    """A coarse reading stays a ceiling on a fine one, now for fractional holdings."""
    n = 0
    for c in cases():
        rng = random.Random(SEED + 5)
        parts = contiguous_partitions(len(c.steps))
        fine = debit(c, random_account(c, rng))
        for _ in range(300):
            a = random_account(c, rng)
            fine = debit(c, a)
            blocks = rng.choice(parts)
            f = fractions(a)
            coarse = {d: 0.0 for d in DIMENSIONS}
            for lo, hi in blocks:
                names = c.step_names[lo:hi]
                share = max([f[p] for p in c.products if c.passes[p] & set(names)] or [0.0])
                for s in c.steps[lo:hi]:
                    for d in DIMENSIONS:
                        coarse[d] += getattr(s, d) * share
            assert at_least(coarse, fine)
            n += 1
    return f"coarse >= fine on {n} random holding-resolution pairs"


TESTS = [
    test_reduces_to_the_union_rule,
    test_reduces_to_the_split_rule,
    test_n_bundles_add_back_to_the_whole,
    test_monotone,
    test_never_above_one_whole_per_parcel,
    test_eating_never_lowers_and_selling_stops_at_what_was_eaten,
    test_order_does_not_matter,
    test_splitting_across_accounts_never_pays,
    test_per_parcel_not_per_process,
    test_resolution_still_only_lowers,
]


def run_tests():
    failed = 0
    for t in TESTS:
        try:
            print(f"PASS  {t.__name__}: {t()}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(TESTS) - failed}/{len(TESTS)} self-tests pass")
    return 1 if failed else 0


def main():
    c = build_steer()
    print("Steer, ILLUSTRATIVE digits (chain-resolution case 1). Labour per holding:\n")
    print(f"{'holding':34} {'max':>7} {'indep':>7} {'sum':>7} {'no-keep':>8}")
    rows = [
        ("10% beef, 10% hide", {"packaged_beef": 0.1, "hide": 0.1}, {}),
        ("10% beef, 50% hide", {"packaged_beef": 0.1, "hide": 0.5}, {}),
        ("10% of every co-product", {p: 0.1 for p in c.products}, {}),
        ("50% hide held, 50% beef eaten", {"hide": 0.5}, {"packaged_beef": 0.5}),
        ("50% beef eaten, hide sold", {}, {"packaged_beef": 0.5}),
    ]
    for label, held, eaten in rows:
        a = new_account(c)
        a["held"].update(held)
        a["eaten"].update(eaten)
        vals = [debit(c, a, r)["labour_h"] for r in ("max", "independent", "sum", "max_no_keep")]
        print(f"{label:34} " + " ".join(f"{v:7.2f}" for v in vals[:3]) + f" {vals[3]:8.2f}")
    print(f"\nWhole steer: {total(c)['labour_h']:.1f} h. Run with --test for the self-tests.")


if __name__ == "__main__":
    sys.exit(run_tests() if "--test" in sys.argv else main())
