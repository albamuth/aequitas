#!/usr/bin/env python3
"""Does storing the log on disk move the re-weighting / record-check ratio?

THE QUESTION, filed as sr-20260914-run-the-record-check-pass-and-the-full-re-we:
run both passes over a DISK-BACKED log, same generator, order alternated, and
report ratio_disk and ratio_memory from the same machine, both absolute
throughputs, the filesystem, and whether the cache was cold.

ONE LOG, ONE BYTE SPELLING. This is the fault in the outside run (two logs,
34 B vs 28 B per event). Here every event is ONE packed 34-byte record. The
SAME bytes are read by BOTH passes, from three sources:

    memory     the whole log held in RAM (a view, no copy)
    disk-warm  the file, read through the operating system's page cache
    disk-cold  the file, read with FILE_FLAG_NO_BUFFERING (Windows), so the
               page cache is bypassed and every byte comes from the device

Each pass reads and parses its own columns from the packed bytes (the record
check parses 11 columns, the re-weight 5), then does its arithmetic. So the
ONLY difference between arms is where the bytes came from.

RUN
    python disk_ratio.py --test
    python disk_ratio.py --events 1e7,2e7 --reps 5 --dir ../log/tmp
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
from ic_recompute_cost import (  # noqa: E402  one generator, imported not copied
    N_ACCOUNTS, SEED, Checks, make_chunk, human_bytes,
)
from reweight_ratio import Reweight, make_weights  # noqa: E402

REC = np.dtype([("actor", "<i4"), ("material", "<i2"), ("mass_in", "<f4"),
                ("mass_out", "<f4"), ("energy", "<f4"), ("hours", "<f4"),
                ("day", "<i2"), ("parcel", "<i4"), ("origin", "?"),
                ("fate", "?"), ("pledge", "<f4")])
RB = REC.itemsize                      # 34 bytes
assert RB == 34
CHUNK_EV = 2_048_000                   # 34 * 2,048,000 is a multiple of 4096
assert (RB * CHUNK_EV) % 4096 == 0
CHECK_COLS = [n for n in REC.names]
REWEIGHT_COLS = ["actor", "material", "mass_out", "energy", "mass_in"]


# ------------------------------------------------------------ writing the log
def pack(c):
    n = len(c["actor"])
    r = np.empty(n, dtype=REC)
    for name in REC.names:
        r[name] = c[name]
    return r


def write_log(path, n_events, seed=SEED, n_accounts=N_ACCOUNTS):
    rng = np.random.default_rng(seed)
    left = int(n_events)
    with open(path, "wb") as f:
        while left > 0:
            m = min(CHUNK_EV, left)
            pack(make_chunk(rng, m, n_accounts)).tofile(f)
            left -= m
        pad = (-f.tell()) % 4096
        if pad:
            f.write(b"\0" * pad)
    return os.path.getsize(path)


# ------------------------------------------------------------ the three sources
def src_memory(blob, n_events):
    """blob: uint8 array of the whole log, resident in RAM. Yields views."""
    for i in range(0, n_events, CHUNK_EV):
        m = min(CHUNK_EV, n_events - i)
        yield blob[i * RB:(i + m) * RB], m


def src_warm(path, n_events):
    buf = np.empty(CHUNK_EV * RB, dtype=np.uint8)
    with open(path, "rb", buffering=0) as f:
        for i in range(0, n_events, CHUNK_EV):
            m = min(CHUNK_EV, n_events - i)
            got = f.readinto(memoryview(buf)[:m * RB])
            assert got == m * RB, (got, m * RB)
            yield buf[:m * RB], m


def _aligned(nbytes):
    raw = np.empty(nbytes + 4096, dtype=np.uint8)
    off = (-raw.ctypes.data) % 4096
    return raw[off:off + nbytes]


def src_cold(path, n_events):
    """Read with the page cache bypassed. Windows only."""
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.CreateFileW.restype = ctypes.c_void_p
    k32.CreateFileW.argtypes = [ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32,
                                ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32,
                                ctypes.c_void_p]
    k32.ReadFile.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32,
                             ctypes.POINTER(ctypes.c_uint32), ctypes.c_void_p]
    k32.CloseHandle.argtypes = [ctypes.c_void_p]
    # GENERIC_READ, SHARE_READ, OPEN_EXISTING, NO_BUFFERING | SEQUENTIAL_SCAN
    h = k32.CreateFileW(str(path), 0x80000000, 1, None, 3, 0x20000000 | 0x08000000, None)
    if h in (None, ctypes.c_void_p(-1).value):
        raise OSError(ctypes.get_last_error(), "CreateFileW NO_BUFFERING failed")
    buf = _aligned(CHUNK_EV * RB)
    try:
        for i in range(0, n_events, CHUNK_EV):
            m = min(CHUNK_EV, n_events - i)
            want = m * RB
            ask = ((want + 4095) // 4096) * 4096
            got = ctypes.c_uint32(0)
            ok = k32.ReadFile(h, buf.ctypes.data, ask, ctypes.byref(got), None)
            if not ok or got.value < want:
                raise OSError(ctypes.get_last_error(), f"short read {got.value} < {want}")
            yield buf[:want], m
    finally:
        k32.CloseHandle(h)


# ------------------------------------------------------------ the two passes
def cols(raw, m, names):
    rec = np.frombuffer(raw, dtype=REC, count=m)
    return {n: np.ascontiguousarray(rec[n]) for n in names}


def run_check(source, n_accounts, stream_only=False):
    ch = Checks(n_accounts)
    for raw, m in source:
        ch.feed(cols(raw, m, CHECK_COLS))
    t = time.perf_counter()
    v = None if stream_only else ch.verdict()
    return ch, v, time.perf_counter() - t


def run_reweight(source, weights, n_accounts):
    rw = Reweight(weights, n_accounts)
    for raw, m in source:
        rw.feed(cols(raw, m, REWEIGHT_COLS))
    return rw


def paired(arm, mk_source, n_events, reps, weights, n_accounts):
    """Alternate which pass goes first, by repetition. Each pass times its own
    read + parse + arithmetic. IC-5's sort is carried separately."""
    rows = []
    for r in range(reps):
        res = {}
        order = ("check", "reweight") if r % 2 == 0 else ("reweight", "check")
        for which in order:
            t0 = time.perf_counter()
            if which == "check":
                ch, _, ic5 = run_check(mk_source(), n_accounts)
                dt = time.perf_counter() - t0
                res["check_all9_s"] = dt
                res["ic5_s"] = ic5
                res["check_stream_s"] = dt - ic5
                res["ic_ok"] = ch.events == n_events
            else:
                rw = run_reweight(mk_source(), weights, n_accounts)
                res["reweight_s"] = time.perf_counter() - t0
                res["debit_total"] = rw.total()
        res["first"] = order[0]
        res["ratio_all9"] = res["reweight_s"] / res["check_all9_s"]
        res["ratio_stream"] = res["reweight_s"] / res["check_stream_s"]
        rows.append(res)
        print(f"    {arm:9s} rep {r} ({order[0]:8s} first)  check {res['check_all9_s']:.3f}s "
              f"(sort {res['ic5_s']:.3f})  reweight {res['reweight_s']:.3f}s  "
              f"ratio9 {res['ratio_all9']:.3f}  ratio8 {res['ratio_stream']:.3f}", flush=True)
    return rows


def summ(rows, n):
    g = lambda k: np.array([r[k] for r in rows])
    out = {}
    for k in ("ratio_all9", "ratio_stream", "check_all9_s", "check_stream_s", "reweight_s"):
        out[k + "_med"] = float(np.median(g(k)))
        out[k + "_min"] = float(g(k).min())
        out[k + "_max"] = float(g(k).max())
        out[k + "_sd"] = float(g(k).std(ddof=1)) if len(rows) > 1 else 0.0
    out["check_all9_Mps"] = n / out["check_all9_s_med"] / 1e6
    out["check_stream_Mps"] = n / out["check_stream_s_med"] / 1e6
    out["reweight_Mps"] = n / out["reweight_s_med"] / 1e6
    out["debit_total"] = rows[0]["debit_total"]
    return out


# ------------------------------------------------------------ machine facts
def fs_name(path):
    try:
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        root = ctypes.create_unicode_buffer(os.path.splitdrive(os.path.abspath(path))[0] + "\\")
        name = ctypes.create_unicode_buffer(64)
        ok = k32.GetVolumeInformationW(root, None, 0, None, None, None, name, 64)
        return name.value if ok else "unknown"
    except Exception:
        return "unknown"


def ram_gb():
    class MS(ctypes.Structure):
        _fields_ = [("l", ctypes.c_uint32), ("load", ctypes.c_uint32),
                    ("tp", ctypes.c_uint64), ("ap", ctypes.c_uint64),
                    ("tv", ctypes.c_uint64), ("av", ctypes.c_uint64),
                    ("tx", ctypes.c_uint64), ("ax", ctypes.c_uint64),
                    ("ae", ctypes.c_uint64)]
    m = MS(); m.l = ctypes.sizeof(MS)
    ctypes.WinDLL("kernel32").GlobalMemoryStatusEx(ctypes.byref(m))
    return m.tp / 2**30, m.ap / 2**30


# ------------------------------------------------------------ self-tests
def self_tests(tmp):
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        ok = ok and bool(cond)

    n, acc = 3_000_000, 50_000
    p = Path(tmp) / "selftest.bin"
    sz = write_log(p, n, n_accounts=acc)
    blob = np.fromfile(p, dtype=np.uint8)

    # 1. 34 bytes an event, one spelling, and the file is that size padded to 4096.
    check("one byte spelling: 34 B/event, padded to 4096",
          sz == ((n * RB + 4095) // 4096) * 4096, f"{sz} bytes")

    # 2. the three sources deliver identical bytes. If cold reads were misaligned
    #    or short this fails.
    def digest(src):
        return sum(int(np.frombuffer(r, dtype=np.uint8, count=m * RB).astype(np.uint64).sum())
                   for r, m in src)
    dm = digest(src_memory(blob, n))
    dw = digest(src_warm(p, n))
    dc = digest(src_cold(p, n))
    check("memory, warm and cold sources deliver the same bytes", dm == dw == dc,
          f"{dm} {dw} {dc}")

    # 3. packing then parsing returns the generator's own columns.
    c = make_chunk(np.random.default_rng(SEED), CHUNK_EV, acc)
    rec = pack(c)
    back = cols(rec.tobytes(), CHUNK_EV, REC.names)
    check("pack/parse round-trips every column",
          all(np.array_equal(back[k], c[k]) for k in REC.names))

    # 4. the re-weight read off disk equals the re-weight on the generator's arrays.
    w = make_weights()
    direct = Reweight(w, acc)
    rng = np.random.default_rng(SEED)
    left = n
    while left > 0:
        m = min(CHUNK_EV, left)
        direct.feed(make_chunk(rng, m, acc)); left -= m
    viadisk = run_reweight(src_cold(p, n), w, acc)
    check("re-weight via the cold file equals re-weight on generated arrays",
          np.allclose(direct.debit, viadisk.debit, rtol=1e-9))

    # 5. the record check via disk finds a planted fault. A reader that dropped
    #    rows or columns would miss it.
    c2 = make_chunk(np.random.default_rng(5), 100_000, 1000)
    c2["mass_in"][:50] += 1000.0
    p2 = Path(tmp) / "planted.bin"
    with open(p2, "wb") as f:
        pack(c2).tofile(f); f.write(b"\0" * ((-f.tell()) % 4096))
    ch, v, _ = run_check(src_cold(p2, 100_000), 1000)
    check("a planted mass imbalance is found through the cold read", v["IC_1"] > 100.0,
          f"IC_1 = {v['IC_1']:.1f}")

    # 6. a short file must be refused, not silently under-read.
    try:
        list(src_cold(p2, 500_000)); short_ok = False
    except OSError:
        short_ok = True
    check("a read past the end of the file raises", short_ok)

    # 7. the two passes are different work (ratio is not 1.0 by construction).
    t0 = time.perf_counter(); run_check(src_memory(blob, n), acc)
    a = time.perf_counter() - t0
    t0 = time.perf_counter(); run_reweight(src_memory(blob, n), w, acc)
    b = time.perf_counter() - t0
    check("record check and re-weight cost different amounts of time",
          abs(a - b) / max(a, b) > 0.05, f"{a:.3f}s vs {b:.3f}s")

    for q in (p, p2):
        q.unlink(missing_ok=True)
    print()
    print("  all self-tests pass" if ok else "  SELF-TESTS FAILED")
    return ok


# ------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--events", default="1e7,2e7")
    ap.add_argument("--reps", type=int, default=5)
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent.parent / "log" / "tmp"))
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()
    Path(a.dir).mkdir(parents=True, exist_ok=True)
    tot, avail = ram_gb()
    print(f"machine   : {platform.processor()} · {platform.system()} {platform.release()}")
    print(f"language  : Python {platform.python_version()} · numpy {np.__version__}")
    print(f"RAM       : {tot:.1f} GB total, {avail:.1f} GB available at start")
    print(f"filesystem: {fs_name(a.dir)} (log dir {a.dir})")
    print(f"record    : {RB} B/event, one packed spelling, both passes read the same bytes")
    print(f"k = 3 · accounts {N_ACCOUNTS:,} · seed {SEED} · chunk {CHUNK_EV:,} events")
    if a.test:
        print("SELF-TESTS")
        sys.exit(0 if self_tests(a.dir) else 1)

    weights = make_weights(SEED, 3)
    allres = []
    for n in (int(float(x)) for x in a.events.split(",")):
        path = Path(a.dir) / f"log_{n}.bin"
        t0 = time.perf_counter()
        sz = write_log(path, n)
        print(f"\n{n:,} events: wrote {human_bytes(sz)} in {time.perf_counter()-t0:.1f}s")
        blob = np.fromfile(path, dtype=np.uint8)
        arms = [("memory", lambda: src_memory(blob, n)),
                ("disk-warm", lambda: src_warm(path, n)),
                ("disk-cold", lambda: src_cold(path, n))]
        res = {}
        for arm, mk in arms:
            rows = paired(arm, mk, n, a.reps, weights, N_ACCOUNTS)
            res[arm] = summ(rows, n)
        # the same debit total from all three arms, or the arms read different logs
        tots = [res[k]["debit_total"] for k in res]
        res["same_log"] = bool(np.allclose(tots, tots[0], rtol=1e-9))
        res["n"] = n
        allres.append(res)
        del blob
        if not a.keep:
            path.unlink(missing_ok=True)

    print("\n" + "=" * 100)
    print("MEASURED (medians; sd over repetitions)")
    print("=" * 100)
    for res in allres:
        n = res["n"]
        print(f"\n{n:,} events   same log in all three arms: {res['same_log']}")
        print(f"{'arm':10s}{'ratio9 med':>11s}{'sd':>7s}{'min-max':>14s}{'ratio8':>8s}"
              f"{'check9 M/s':>12s}{'check8 M/s':>12s}{'reweight M/s':>14s}")
        for arm in ("memory", "disk-warm", "disk-cold"):
            s = res[arm]
            print(f"{arm:10s}{s['ratio_all9_med']:>11.3f}{s['ratio_all9_sd']:>7.3f}"
                  f"{s['ratio_all9_min']:>8.3f}-{s['ratio_all9_max']:.3f}{s['ratio_stream_med']:>8.3f}"
                  f"{n / s['check_all9_s_med'] / 1e6:>12.2f}{s['check_stream_Mps']:>12.2f}"
                  f"{s['reweight_Mps']:>14.2f}")
        for arm in ("disk-warm", "disk-cold"):
            d = res[arm]["ratio_all9_med"] - res["memory"]["ratio_all9_med"]
            sp = max(res["memory"]["ratio_all9_max"] - res["memory"]["ratio_all9_min"],
                     res[arm]["ratio_all9_max"] - res[arm]["ratio_all9_min"])
            print(f"  delta ratio9 ({arm} - memory) = {d:+.3f}   widest run-to-run range = {sp:.3f}")
    print()


if __name__ == "__main__":
    main()
