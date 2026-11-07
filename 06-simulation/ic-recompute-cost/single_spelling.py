#!/usr/bin/env python3
"""One generator, ONE byte spelling, both passes, memory and disk, 1e8 and 1e9.

REQUEST sr-20260915-run-the-record-check-pass-and-the-full-re-we.

Every event is the same packed 34-byte record (disk_ratio.REC). Both passes
parse their own columns from those bytes. Three arms differ only in where the
bytes come from:

  mem-fresh   every chunk is newly generated and packed, UNTIMED, then held in
              RAM for the two timed passes. Distinct events at any length.
              (A 1e9 log is 34 GB and cannot be resident; chunks stream through
              RAM, the generation is not in either timer.)
  mem-replay  a REPLAY_CHUNKS-chunk log held in RAM and replayed round and round.
  disk-cold   the same REPLAY_CHUNKS-chunk log as a file (<= 1 GB), replayed with
              the page cache bypassed (FILE_FLAG_NO_BUFFERING, Windows).

Why replay: the budget is 1 GB of new files, and 1e8 / 1e9 events are 3.4 / 34 GB.
The cold read costs the same per byte at any length, so replaying a file measures
the read cost; but replay repeats keys, so IC-5 (the sort) sees periodic data.
mem-replay vs mem-fresh at 1e8 is the control that says whether replay distorts.

Timers: each pass times only its own read + parse + arithmetic, per chunk, with
the order of the two passes flipped chunk by chunk and rep by rep. IC-5's sort is
timed separately and added only for the nine-check ratio.

RUN
    py -3 single_spelling.py --test
    py -3 single_spelling.py --arms mem-fresh,mem-replay,disk-cold --chunks 49 --reps 3
"""

import argparse
import ctypes
import os
import platform
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ic_recompute_cost import SEED, N_ACCOUNTS, Checks, make_chunk, human_bytes  # noqa: E402
from reweight_ratio import Reweight, make_weights  # noqa: E402
from disk_ratio import (REC, RB, CHUNK_EV, CHECK_COLS, REWEIGHT_COLS, pack,  # noqa: E402
                        cols, ram_gb, fs_name, _aligned)

REPLAY_CHUNKS = 12                      # 12 * 2,048,000 * 34 B = 835.6 MB file
CHUNK_BYTES = CHUNK_EV * RB
K = 3


# ------------------------------------------------------------ the log file
def write_replay_file(path, n_chunks=REPLAY_CHUNKS, n_accounts=N_ACCOUNTS):
    """Same rng stream as mem-fresh, so the file equals fresh chunks 0..n-1."""
    rng = np.random.default_rng(SEED)
    with open(path, "wb") as f:
        for _ in range(n_chunks):
            pack(make_chunk(rng, CHUNK_EV, n_accounts)).tofile(f)
    return os.path.getsize(path)


# ------------------------------------------------------------ providers
class Fresh:
    name = "mem-fresh"

    def __init__(self, n_accounts):
        self.na = n_accounts

    def start_rep(self):
        self.rng = np.random.default_rng(SEED)

    def prepare(self, i):                       # untimed
        self.raw = pack(make_chunk(self.rng, CHUNK_EV, self.na)).view(np.uint8)

    def read(self, which, i):                   # timed: O(1), bytes already in RAM
        return self.raw, CHUNK_EV

    def end_rep(self):
        pass


class Replay:
    name = "mem-replay"

    def __init__(self, path, n_file_chunks):
        self.blob = np.fromfile(path, dtype=np.uint8)
        assert len(self.blob) == n_file_chunks * CHUNK_BYTES
        self.nf = n_file_chunks

    def start_rep(self):
        pass

    def prepare(self, i):
        pass

    def read(self, which, i):
        j = i % self.nf
        return self.blob[j * CHUNK_BYTES:(j + 1) * CHUNK_BYTES], CHUNK_EV

    def end_rep(self):
        pass


class ColdReader:
    """Sequential cache-bypassed reader that wraps to the start of the file."""

    def __init__(self, path, n_file_chunks):
        self.path, self.nf, self.pos = path, n_file_chunks, 0
        self.k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k = self.k32
        k.CreateFileW.restype = ctypes.c_void_p
        k.CreateFileW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32,
                                  ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32,
                                  ctypes.c_void_p]
        k.ReadFile.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32,
                               ctypes.POINTER(ctypes.c_uint32), ctypes.c_void_p]
        k.CloseHandle.argtypes = [ctypes.c_void_p]
        self.buf = _aligned(CHUNK_BYTES)
        self.h = None
        self._open()

    def _open(self):
        h = self.k32.CreateFileW(str(self.path), 0x80000000, 1, None, 3,
                                 0x20000000 | 0x08000000, None)
        if h in (None, ctypes.c_void_p(-1).value):
            raise OSError(ctypes.get_last_error(), "CreateFileW NO_BUFFERING failed")
        self.h, self.pos = h, 0

    def next(self):
        if self.pos == self.nf:                 # wrap: reopen at offset 0
            self.k32.CloseHandle(self.h)
            self._open()
        got = ctypes.c_uint32(0)
        ok = self.k32.ReadFile(self.h, self.buf.ctypes.data, CHUNK_BYTES,
                               ctypes.byref(got), None)
        if not ok or got.value != CHUNK_BYTES:
            raise OSError(ctypes.get_last_error(), f"short read {got.value}")
        self.pos += 1
        return self.buf, CHUNK_EV

    def close(self):
        if self.h:
            self.k32.CloseHandle(self.h)
            self.h = None


class Cold:
    name = "disk-cold"

    def __init__(self, path, n_file_chunks):
        self.path, self.nf = path, n_file_chunks

    def start_rep(self):
        # one cursor per pass, so each pass really reads the file itself
        self.rd = {"check": ColdReader(self.path, self.nf),
                   "reweight": ColdReader(self.path, self.nf)}

    def prepare(self, i):
        pass

    def read(self, which, i):
        return self.rd[which].next()

    def end_rep(self):
        for r in self.rd.values():
            r.close()


# ------------------------------------------------------------ one rep
def one_rep(provider, n_chunks, rep, weights, n_accounts):
    provider.start_rep()
    ch, rw = Checks(n_accounts), Reweight(weights, n_accounts)
    check_s = reweight_s = 0.0
    wall0 = time.perf_counter()
    try:
        for i in range(n_chunks):
            provider.prepare(i)
            order = ("check", "reweight") if (rep + i) % 2 == 0 else ("reweight", "check")
            for which in order:
                t0 = time.perf_counter()
                raw, m = provider.read(which, i)
                if which == "check":
                    ch.feed(cols(raw, m, CHECK_COLS))
                    check_s += time.perf_counter() - t0
                else:
                    rw.feed(cols(raw, m, REWEIGHT_COLS))
                    reweight_s += time.perf_counter() - t0
        wall = time.perf_counter() - wall0
        t3 = time.perf_counter()
        v = ch.verdict()
        ic5_s = time.perf_counter() - t3
    finally:
        provider.end_rep()
    n = n_chunks * CHUNK_EV
    row = dict(n=n, check_stream_s=check_s, ic5_s=ic5_s, reweight_s=reweight_s,
               wall_s=wall, events=ch.events, debit_total=rw.total(),
               ic5_dups=int(v["IC_5"]), ic1=float(v["IC_1"]))
    row["ratio8"] = reweight_s / check_s
    row["ratio9"] = reweight_s / (check_s + ic5_s)
    return row


def run_arm(provider, n_chunks, reps, weights, n_accounts, label=""):
    rows = []
    for r in range(reps):
        row = one_rep(provider, n_chunks, r, weights, n_accounts)
        rows.append(row)
        print(f"  {provider.name:10s} {label}rep {r}: N={row['n']:,}  check8 {row['check_stream_s']:.2f}s  "
              f"sort {row['ic5_s']:.2f}s  reweight {row['reweight_s']:.2f}s  "
              f"ratio8 {row['ratio8']:.3f}  ratio9 {row['ratio9']:.3f}", flush=True)
    return rows


def summarise(rows):
    g = lambda k: np.array([r[k] for r in rows])
    n = rows[0]["n"]
    s = {"n": n, "reps": len(rows)}
    for k in ("ratio8", "ratio9"):
        s[k + "_med"], s[k + "_min"], s[k + "_max"] = (float(np.median(g(k))), float(g(k).min()),
                                                       float(g(k).max()))
        s[k + "_sd"] = float(g(k).std(ddof=1)) if len(rows) > 1 else float("nan")
    s["check8_Mps"] = n / float(np.median(g("check_stream_s"))) / 1e6
    s["check9_Mps"] = n / float(np.median(g("check_stream_s") + g("ic5_s"))) / 1e6
    s["reweight_Mps"] = n / float(np.median(g("reweight_s"))) / 1e6
    s["check8_s"] = float(np.median(g("check_stream_s")))
    s["ic5_s"] = float(np.median(g("ic5_s")))
    s["reweight_s"] = float(np.median(g("reweight_s")))
    return s


# ------------------------------------------------------------ self-tests
def self_tests(tmp):
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        ok = ok and bool(cond)

    acc = 50_000
    nf = 2
    path = Path(tmp) / "ss_selftest.bin"
    w = make_weights(SEED, K)
    try:
        sz = write_replay_file(path, nf, acc)
        check("file is exactly 34 B/event x chunks", sz == nf * CHUNK_BYTES, f"{sz}")

        # replay wrap: chunk 0 and chunk 2 are the same bytes, chunk 1 differs
        cold = Cold(path, nf); cold.start_rep()
        d = [int(np.frombuffer(cold.read("check", i)[0], dtype=np.uint8).astype(np.uint64).sum())
             for i in range(5)]
        cold.end_rep()
        check("cold reader wraps: chunks 0,2,4 equal; 1,3 equal; 0 != 1",
              d[0] == d[2] == d[4] and d[1] == d[3] and d[0] != d[1], str(d[:3]))

        # the memory-replay and cold arms deliver the same bytes
        rep = Replay(path, nf)
        dm = [int(np.frombuffer(rep.read("check", i)[0], dtype=np.uint8).astype(np.uint64).sum())
              for i in range(5)]
        check("mem-replay and disk-cold deliver identical bytes", dm == d)

        # fresh chunks 0..nf-1 equal the file (same rng stream)
        fr = Fresh(acc); fr.start_rep()
        df = []
        for i in range(nf):
            fr.prepare(i); df.append(int(fr.read("check", i)[0].astype(np.uint64).sum()))
        check("mem-fresh chunks 0..1 equal the file's chunks", df == d[:nf])

        # all three arms give the same re-weight total over 5 chunks of the replay
        rows = [one_rep(p, 5, 0, w, acc) for p in (Replay(path, nf), Cold(path, nf))]
        direct = Reweight(w, acc)
        rng = np.random.default_rng(SEED)
        chunks = [make_chunk(rng, CHUNK_EV, acc) for _ in range(nf)]
        for i in range(5):
            direct.feed(chunks[i % nf])
        check("re-weight via replay and via cold equal the direct total",
              np.isclose(rows[0]["debit_total"], direct.total(), rtol=1e-9)
              and np.isclose(rows[1]["debit_total"], direct.total(), rtol=1e-9),
              f"{rows[0]['debit_total']:.6g} {rows[1]['debit_total']:.6g} {direct.total():.6g}")

        # a replayed log repeats keys, so IC-5 must find duplicates; fresh must not
        # (distinct parcel/day keys are 4e6*3650 so 2 fresh chunks collide rarely)
        check("IC-5 sees duplicates in the replay and the cold arm (it reads the data)",
              rows[0]["ic5_dups"] > 1_000_000 and rows[1]["ic5_dups"] == rows[0]["ic5_dups"],
              f"{rows[0]['ic5_dups']:,} {rows[1]['ic5_dups']:,}")
        fr2 = one_rep(Fresh(acc), 5, 0, w, acc)
        check("IC-5 on fresh events finds far fewer duplicates than on a replay",
              fr2["ic5_dups"] < rows[0]["ic5_dups"] / 100, f"{fr2['ic5_dups']:,}")

        # a planted fault in the file is found through the cold wrap
        c0 = make_chunk(np.random.default_rng(5), CHUNK_EV, acc)
        c0["mass_in"][:50] += 1000.0
        p2 = Path(tmp) / "ss_planted.bin"
        with open(p2, "wb") as f:
            pack(c0).tofile(f)
        r3 = one_rep(Cold(p2, 1), 3, 0, w, acc)
        check("a planted mass imbalance is found through the cold replay", r3["ic1"] > 100.0,
              f"IC_1 = {r3['ic1']:.1f}")
        p2.unlink(missing_ok=True)

        # timers do not double count: the two passes' time cannot exceed the wall
        check("check + reweight time never exceeds wall time",
              rows[0]["check_stream_s"] + rows[0]["reweight_s"] <= rows[0]["wall_s"] * 1.001,
              f"{rows[0]['check_stream_s'] + rows[0]['reweight_s']:.2f} <= {rows[0]['wall_s']:.2f}")
        check("the two passes are different work (ratio not 1 by construction)",
              abs(rows[0]["ratio8"] - 1.0) > 0.05, f"ratio8 {rows[0]['ratio8']:.3f}")
    finally:
        path.unlink(missing_ok=True)
    print()
    print("  all self-tests pass" if ok else "  SELF-TESTS FAILED")
    return ok


# ------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--arms", default="mem-fresh,mem-replay,disk-cold")
    ap.add_argument("--chunks", type=int, default=49, help="49 -> 100,352,000 events (~1e8); 488 -> ~1e9")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent.parent / "log" / "tmp"))
    a = ap.parse_args()
    Path(a.dir).mkdir(parents=True, exist_ok=True)
    tot, avail = ram_gb()
    print(f"machine   : {platform.processor()} - {platform.system()} {platform.release()}")
    print(f"language  : Python {platform.python_version()} - numpy {np.__version__}")
    print(f"RAM       : {tot:.1f} GB total, {avail:.1f} GB available at start")
    print(f"filesystem: {fs_name(a.dir)} (log dir {a.dir})")
    print(f"record    : {RB} B/event, ONE packed spelling, both passes parse the same bytes")
    print(f"k = {K} - accounts {N_ACCOUNTS:,} - seed {SEED} - chunk {CHUNK_EV:,} events - replay file {REPLAY_CHUNKS} chunks")
    if a.test:
        print("SELF-TESTS")
        sys.exit(0 if self_tests(a.dir) else 1)

    n_events = a.chunks * CHUNK_EV
    arms = a.arms.split(",")
    est_gb = (n_events * 8 * 2) / 2**30
    print(f"\nrequested {a.chunks} chunks = {n_events:,} events; IC-5 keys need about {est_gb:.1f} GB peak (8 B/event, x2 at the sort)")
    if est_gb > avail - 4:
        print(f"BLOCKED: {est_gb:.1f} GB peak for the IC-5 sort is more than the RAM available ({avail:.1f} GB).")
        sys.exit(2)
    weights = make_weights(SEED, K)
    path = Path(a.dir) / "ss_replay.bin"
    out = {}
    try:
        if any(x in arms for x in ("mem-replay", "disk-cold")):
            t0 = time.perf_counter()
            sz = write_replay_file(path)
            print(f"wrote replay file {human_bytes(sz)} in {time.perf_counter()-t0:.1f}s")
        for arm in arms:
            if arm == "mem-fresh":
                prov = Fresh(N_ACCOUNTS)
            elif arm == "mem-replay":
                prov = Replay(path, REPLAY_CHUNKS)
            elif arm == "disk-cold":
                prov = Cold(path, REPLAY_CHUNKS)
            else:
                raise SystemExit(f"unknown arm {arm}")
            rows = run_arm(prov, a.chunks, a.reps, weights, N_ACCOUNTS)
            out[arm] = summarise(rows)
            out[arm]["debit_total"] = rows[0]["debit_total"]
            if arm != "mem-fresh":
                del prov
    finally:
        path.unlink(missing_ok=True)

    print("\n" + "=" * 110)
    print(f"MEASURED  N = {n_events:,} events  (medians; sd over reps; Mev/s = million events a second)")
    print("=" * 110)
    print(f"{'arm':11s}{'ratio9':>8s}{'sd':>7s}{'min-max':>14s}{'ratio8':>8s}{'sd':>7s}"
          f"{'check9 Mev/s':>14s}{'check8 Mev/s':>14s}{'reweight Mev/s':>16s}{'sort s':>8s}")
    for arm, s in out.items():
        print(f"{arm:11s}{s['ratio9_med']:>8.3f}{s['ratio9_sd']:>7.3f}"
              f"{s['ratio9_min']:>8.3f}-{s['ratio9_max']:.3f}{s['ratio8_med']:>8.3f}{s['ratio8_sd']:>7.3f}"
              f"{s['check9_Mps']:>14.2f}{s['check8_Mps']:>14.2f}{s['reweight_Mps']:>16.2f}{s['ic5_s']:>8.2f}")
    if "mem-replay" in out and "disk-cold" in out:
        for k in ("ratio9", "ratio8"):
            d = out["disk-cold"][k + "_med"] - out["mem-replay"][k + "_med"]
            sp = max(out[x][k + "_max"] - out[x][k + "_min"] for x in ("mem-replay", "disk-cold"))
            print(f"  delta {k} (disk-cold - mem-replay, same bytes) = {d:+.3f}   widest range = {sp:.3f}")
    if "mem-fresh" in out and "mem-replay" in out:
        for k in ("ratio9", "ratio8"):
            d = out["mem-replay"][k + "_med"] - out["mem-fresh"][k + "_med"]
            print(f"  replay control {k} (mem-replay - mem-fresh) = {d:+.3f}")
    print()


if __name__ == "__main__":
    main()
