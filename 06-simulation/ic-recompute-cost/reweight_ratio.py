#!/usr/bin/env python3
"""How much does a RE-WEIGHTING pass cost against a RECORD-CHECK pass?

THE QUESTION, filed as
sr-20260912-run-the-record-check-pass-and-the-full-re-we on 2026-09-12:

    "Run the record-check pass and the full re-weighting pass off ONE
     generator on ONE machine, with pass order alternated or randomised and
     repeated. Report the ratio, both absolute throughputs, and the machine,
     encoding, language and k."

WHY IT EXISTS

    Foundations section 3.4a carries this sentence:

        "The record-check cost was measured at 1.6 minutes for a billion
         events; the re-weighting cost was not, and must not be quoted from
         that figure."

    On 2026-09-11 this project published a prior of 1x to 5x -- re-weighting
    expected to cost the same as a record check or up to five times more.

    On 2026-09-12 @hemei (citizen #700, comment c55882) ran both passes and
    returned 0.27, which is not merely outside the prior but on the other
    side of 1.0: re-weighting came back CHEAPER than the record check.

    They flagged their own caveat rather than letting us find it. NO SINGLE
    LOG SERVED BOTH PASSES -- the two numbers came from different generators,
    so the ratio is cross-generator and a difference in the generators would
    land inside it.

    @bounded-curiosity (c54167) then killed the repair that had been proposed
    for this: "A same-machine denominator removes some shared I/O cost; it
    does not make the ratio machine-independent... portable is not invariant."
    They are right, and it is why this run reports both ABSOLUTE throughputs
    beside the ratio rather than the ratio alone.

WHAT THIS RUN DOES DIFFERENTLY

    ONE GENERATOR. This file imports make_chunk from ic_recompute_cost.py
    rather than defining its own. Every event fed to the re-weighting pass is
    the same event, from the same seeded draw, that was fed to the record
    check. That is the thing @hemei could not do and said so.

    ONE MACHINE, ONE PROCESS, ONE INTERPRETER.

    ORDER ALTERNATED. Whichever pass runs first on a freshly generated chunk
    reads it into a cold cache and pays for the other. So the order flips on
    every chunk AND on every repetition, and both orders are reported. If the
    ratio moved with order, the order effect would be the finding.

    GENERATION EXCLUDED FROM BOTH. The chunk is built once, then handed to
    each pass, and only the pass is timed.

WHAT A RE-WEIGHTING PASS IS

    Foundations section 3.3: when a cost constant improves, every affected
    ledger recalculates, backwards through history. Section 3.2a: a debit is
    a VECTOR of physical quantities, collapsed into hours only when somebody
    asks, through the current weighting model.

    So one re-weighting pass is: walk the log, and for every event, convert
    each stored physical quantity through the new weights and accumulate the
    result against the account that caused it.

        per event:  gather the weight row for the event's material
                    multiply each physical quantity by its weight
                    scatter-add the hours into that account's debit

    Three dimensions are carried -- mass, energy, and a pollution term --
    because section 3.2a's rule is that the collapse happens per dimension.
    A one-dimension version would be a cheaper pass than the document
    describes.

WHAT IS DELIBERATELY NOT IN IT

    The integrity checks. A re-weight recomputes figures; it does not re-prove
    the record. Running them inside it would be timing the record check twice
    and calling the total a re-weight.

RUN
    python reweight_ratio.py --test        self-tests, each able to fail
    python reweight_ratio.py               10^6 and 10^7, 3 repetitions
    python reweight_ratio.py --full        adds a measured 10^8
    python reweight_ratio.py --events 5e6 --reps 5
"""

import argparse
import platform
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ic_recompute_cost import (  # noqa: E402  -- ONE generator, imported not copied
    CHUNK,
    N_ACCOUNTS,
    N_MATERIALS,
    SEED,
    Checks,
    human_bytes,
    human_time,
    make_chunk,
    rule,
)

# k -- the number of weighting dimensions collapsed per event. Named because
# the sim request asks for it by name: the re-weighting cost is linear in k
# and a run that does not state k is not reproducible.
K_DIMENSIONS = 3


# ------------------------------------------------------------ the weights
def make_weights(seed=SEED):
    """The current weighting model: hours per physical unit, per material.

    Shape is (N_MATERIALS, k). Real values come from published cost constants
    (Foundations section 3.3a); the ARITHMETIC is what is being timed, and it
    does not depend on which numbers are in the table.
    """
    rng = np.random.default_rng(seed + 977)
    return rng.random((N_MATERIALS, K_DIMENSIONS)).astype(np.float64) * 0.05


class Reweight:
    """One account-debit vector, recomputed from the log under new weights.

    Streaming, like eight of the nine integrity checks: the memory held is a
    property of the ACCOUNT COUNT, never of the log length.
    """

    def __init__(self, weights, n_accounts=N_ACCOUNTS):
        self.w = weights
        self.debit = np.zeros(n_accounts, dtype=np.float64)
        self.events = 0

    def feed(self, c):
        """Collapse one chunk's debit vector into hours, per dimension."""
        w = self.w[c["material"]]                     # gather, (n, k)
        hours = (c["mass_out"] * w[:, 0]
                 + c["energy"] * w[:, 1]
                 + c["mass_in"] * w[:, 2])            # collapse, per dimension
        np.add.at(self.debit, c["actor"], hours)      # scatter-add
        self.events += len(c["actor"])

    def bytes_held(self):
        return self.debit.nbytes + self.w.nbytes

    def total(self):
        return float(self.debit.sum())


# ------------------------------------------------------------ the paired run
def paired_pass(n_events, reps, n_accounts=N_ACCOUNTS, chunk=CHUNK, seed=SEED,
                verbose=False, stream_only=False):
    """Run both passes over the SAME events, flipping which goes first.

    Returns one row per repetition. The order flips per repetition AND per
    chunk inside a repetition, so neither pass keeps the warm-cache advantage.
    """
    weights = make_weights(seed)
    rows = []
    for r in range(reps):
        rng = np.random.default_rng(seed)          # identical log every rep
        ch = Checks(n_accounts)
        rw = Reweight(weights, n_accounts)
        check_s = reweight_s = 0.0
        left, i = int(n_events), 0
        while left > 0:
            m = min(chunk, left)
            c = make_chunk(rng, m, n_accounts)     # generated ONCE, untimed
            check_first = ((r + i) % 2 == 0)
            if check_first:
                t0 = time.perf_counter(); ch.feed(c); t1 = time.perf_counter()
                rw.feed(c);                         t2 = time.perf_counter()
                check_s += t1 - t0; reweight_s += t2 - t1
            else:
                t0 = time.perf_counter(); rw.feed(c); t1 = time.perf_counter()
                ch.feed(c);                          t2 = time.perf_counter()
                reweight_s += t1 - t0; check_s += t2 - t1
            if stream_only:
                # IC-5 keeps every parcel/day key so it can sort them at the
                # end, which is 8 GB at 10^9 events and does not fit. Dropping
                # the keys as we go measures the EIGHT streaming checks at a
                # size the sort cannot reach. It is not a cheaper IC-5; it is
                # no IC-5, and the output says so.
                ch.pairs.clear()
            left -= m; i += 1

        # IC-5's sort is outside the streaming loop, exactly as the 2026-08-29
        # run reported it. It is carried separately here for the same reason:
        # folding a sort into a streaming rate is the error this project keeps
        # finding in other people's numbers.
        t3 = time.perf_counter()
        if not stream_only:
            ch.verdict()
        ic5_s = time.perf_counter() - t3

        rows.append(dict(rep=r,
                         first="check" if r % 2 == 0 else "reweight",
                         check_s=check_s, ic5_s=ic5_s, reweight_s=reweight_s,
                         ratio_stream=reweight_s / check_s,
                         ratio_all9=reweight_s / (check_s + ic5_s),
                         check_bytes=ch.bytes_held(),
                         reweight_bytes=rw.bytes_held(),
                         debit_total=rw.total()))
        if verbose:
            print(f"    rep {r} ({rows[-1]['first']} first): "
                  f"check {check_s:.3f}s  reweight {reweight_s:.3f}s  "
                  f"ratio {rows[-1]['ratio_stream']:.3f}")
    return rows


def summarise(rows):
    rs = np.array([r["ratio_stream"] for r in rows])
    ra = np.array([r["ratio_all9"] for r in rows])
    return dict(
        ratio_stream_med=float(np.median(rs)),
        ratio_stream_min=float(rs.min()), ratio_stream_max=float(rs.max()),
        ratio_all9_med=float(np.median(ra)),
        check_s_med=float(np.median([r["check_s"] for r in rows])),
        ic5_s_med=float(np.median([r["ic5_s"] for r in rows])),
        reweight_s_med=float(np.median([r["reweight_s"] for r in rows])),
    )


# ------------------------------------------------------------ self-tests
def self_tests():
    """Every one of these can fail, and two of them have."""
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        ok = ok and bool(cond)

    n, acc = 200_000, 50_000

    # 1. Same events reach both passes. If the generator were re-drawn between
    #    them this fails, and a cross-generator ratio is exactly the fault
    #    @hemei flagged in their own run.
    rng1 = np.random.default_rng(SEED)
    rng2 = np.random.default_rng(SEED)
    a, b = make_chunk(rng1, n, acc), make_chunk(rng2, n, acc)
    same = all(np.array_equal(a[k], b[k]) for k in a)
    check("one generator: the same seed gives the same events", same)

    # 2. The re-weight is deterministic under a fixed weighting model.
    w = make_weights()
    r1, r2 = Reweight(w, acc), Reweight(w, acc)
    r1.feed(a); r2.feed(a)
    check("re-weighting is deterministic", np.allclose(r1.debit, r2.debit))

    # 3. Chunking must not change the answer. This is the streaming claim.
    r3 = Reweight(w, acc)
    for i in range(0, n, 37_000):
        r3.feed({k: v[i:i + 37_000] for k, v in a.items()})
    check("re-weighting streams: chunked == whole",
          np.allclose(r1.debit, r3.debit, rtol=1e-9),
          f"max delta {np.abs(r1.debit - r3.debit).max():.3e}")

    # 4. NEW weights must give a DIFFERENT answer. Without this the pass could
    #    be a no-op and every timing below would be meaningless.
    r4 = Reweight(make_weights(SEED + 1), acc)
    r4.feed(a)
    check("new weights move the figure",
          not np.allclose(r1.debit, r4.debit),
          f"totals {r1.total():.1f} vs {r4.total():.1f}")

    # 5. Memory is flat in the log and grows with accounts only.
    small, big = Reweight(w, acc), Reweight(w, acc)
    small.feed({k: v[:1000] for k, v in a.items()})
    big.feed(a)
    check("re-weighting memory is flat in the log",
          small.bytes_held() == big.bytes_held(),
          human_bytes(big.bytes_held()))

    # 6. The two passes are not the same work. If the re-weight accidentally
    #    ran the checks, the ratio would be 1.0 by construction.
    ch = Checks(acc); ch.feed(a)
    check("the two passes hold different state",
          ch.streaming_bytes() != small.bytes_held(),
          f"check {human_bytes(ch.streaming_bytes())} vs "
          f"reweight {human_bytes(small.bytes_held())}")

    # 7. Order must not decide the answer, only possibly the timing.
    rows = paired_pass(400_000, reps=2, n_accounts=acc, chunk=100_000)
    check("pass order does not change the result",
          abs(rows[0]["debit_total"] - rows[1]["debit_total"]) < 1e-6,
          f"{rows[0]['debit_total']:.6f} vs {rows[1]['debit_total']:.6f}")

    # 8. k is load-bearing and must be stated. A one-dimension collapse is a
    #    cheaper pass than Foundations section 3.2a describes.
    check("k is stated", K_DIMENSIONS == 3, f"k = {K_DIMENSIONS}")

    print()
    print("  all self-tests pass" if ok else "  SELF-TESTS FAILED")
    return ok


# ------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--full", action="store_true", help="adds a measured 10^8")
    ap.add_argument("--events", type=float, default=None)
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--stream-only", action="store_true",
                    help="drop IC-5's keys as they are made, so the eight "
                         "streaming checks can be measured at a size IC-5's "
                         "sort cannot fit. Reports no IC-5 figure.")
    a = ap.parse_args()

    print()
    rule("=")
    print("RE-WEIGHTING COST AGAINST RECORD-CHECK COST -- one generator, one machine")
    rule("=")
    print(f"machine   : {platform.processor() or platform.machine()} · "
          f"{platform.system()} {platform.release()}")
    print(f"language  : Python {platform.python_version()} · numpy {np.__version__}")
    print(f"encoding  : flat numpy arrays, int32/int16/float32 -- no serialisation")
    print(f"k         : {K_DIMENSIONS} weighting dimensions collapsed per event")
    print(f"accounts  : {N_ACCOUNTS:,} · materials: {N_MATERIALS} · "
          f"chunk: {CHUNK:,} · seed: {SEED}")
    print(f"repetitions: {a.reps}, pass order flipped per repetition and per chunk")
    print()

    if a.test:
        print("SELF-TESTS")
        sys.exit(0 if self_tests() else 1)

    sizes = [int(a.events)] if a.events else [1_000_000, 10_000_000]
    if a.full and not a.events:
        sizes.append(100_000_000)

    results = []
    for n in sizes:
        print(f"  {n:,} events ...")
        rows = paired_pass(n, a.reps, verbose=True, stream_only=a.stream_only)
        s = summarise(rows)
        s["events"] = n
        results.append(s)
        print()

    rule()
    print("MEASURED  (medians over repetitions)")
    rule()
    print(f"{'events':>14} {'record check':>14} {'re-weight':>12} "
          f"{'ratio':>8} {'check rate':>13} {'reweight rate':>15}")
    for s in results:
        n = s["events"]
        print(f"{n:>14,} {human_time(s['check_s_med']):>14} "
              f"{human_time(s['reweight_s_med']):>12} "
              f"{s['ratio_stream_med']:>8.3f} "
              f"{n / s['check_s_med'] / 1e6:>10.2f} M/s "
              f"{n / s['reweight_s_med']:>13,.0f}/s")
    print()
    print("  'record check' is the EIGHT streaming constraints. IC-5 is a sort and")
    print("  is carried separately, as the 2026-08-29 run reported it:")
    if a.stream_only:
        print("    --stream-only: IC-5 DID NOT RUN. There is no all-nine ratio to")
        print("    report here, and printing the streaming one under that name")
        print("    would be the mislabelling this project keeps finding elsewhere.")
    else:
        for s in results:
            print(f"    {s['events']:>14,}  IC-5 sort {human_time(s['ic5_s_med']):>10}"
                  f"   ratio against all nine: {s['ratio_all9_med']:.3f}")
    print()

    spread = max(s["ratio_stream_max"] - s["ratio_stream_min"] for s in results)
    print(f"  widest ratio spread across repetitions: {spread:.4f}")
    print(f"  ratio at the largest size measured    : "
          f"{results[-1]['ratio_stream_med']:.3f}")
    print()
    rule()
    print("AGAINST THE TWO PRIORS")
    rule()
    r = results[-1]["ratio_stream_med"]
    print(f"  this project's published prior : 1.0 - 5.0   "
          f"{'INSIDE' if 1.0 <= r <= 5.0 else 'OUTSIDE'}")
    print(f"  @hemei, c55882, cross-generator: 0.27        "
          f"measured here: {r:.3f}")
    print()


if __name__ == "__main__":
    main()
