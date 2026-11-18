#!/usr/bin/env python3
"""
census.py -- sr-20261105 part 2: every .py under 06-simulation (not data/, not
99-superseded/, not log/) that assigns a NAMED ANCHOR, and how many of them have
an assertion that fails when that anchor is scaled, and how many pin a literal.

DEFINITIONS (declared before running)
  anchor assignment   an assignment, anywhere in the file, whose target name matches
                      ANCHOR_NAME, or whose right-hand side contains the numeric
                      literal 1380 (the median-lifestyle anchor, Foundations 3.5),
                      and whose value is a number (int/float or arithmetic of them).
  denominator         scripts with >= 1 anchor assignment.
  REACHED (static)    an assert statement (or an `if ...: raise AssertionError`) in
                      the file mentions the anchor name, directly or through a
                      same-file function that mentions it (call-graph closure).
                      An UPPER bound: reaching is not failing.
  FAILS WHEN SCALED   (dynamic, the strict reading) load the module without running
                      __main__, check its test functions pass unscaled, set each
                      numeric module-level anchor to x2 and x0.5 one at a time, run
                      the same tests, and require an AssertionError. Only scripts
                      with a __main__ guard and no file-writing call are loaded.
  PINS A LITERAL      an assert whose comparison holds a numeric literal that is not a
                      small structural constant (0, 1, 2, 3, 4, 5, 10, 100, or |x|<1e-3).
                      A HEURISTIC: a tolerance can look like a pin.

Run:  python census.py
"""
from __future__ import annotations

import ast
import importlib.util
import os
import re
import signal
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"data", "99-superseded", "log", "__pycache__", "tmp"}
ANCHOR_NAME = re.compile(r"(ANCHOR|KAPPA|MEDIAN_LIFESTYLE|PAST_RATE)", re.I)
STRUCTURAL = {0, 1, 2, 3, 4, 5, 10, 100}
WRITE_CALLS = {"write_text", "write_bytes", "savez", "savez_compressed", "save", "to_csv",
               "dump", "mkdir", "makedirs", "remove", "unlink", "rename"}
TEST_NAME = re.compile(r"^(test_|self_test|run_tests$|selftest)")


def py_files():
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            if f.endswith(".py"):
                yield os.path.join(d, f)


def is_number_expr(node):
    try:
        v = ast.literal_eval(node)
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    except Exception:
        pass
    ok = False
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            ok = True
        elif not isinstance(n, (ast.BinOp, ast.UnaryOp, ast.operator, ast.unaryop,
                                ast.Constant, ast.Name, ast.Load)):
            return False
    return ok


def has_1380(node):
    return any(isinstance(n, ast.Constant) and isinstance(n.value, (int, float))
               and float(n.value) == 1380.0 for n in ast.walk(node))


def targets(a):
    t = a.targets if isinstance(a, ast.Assign) else [a.target]
    return [x.id for x in t if isinstance(x, ast.Name)]


def anchors_in(tree):
    """-> (set of anchor names, set of module-level numeric anchor names)."""
    names, top = set(), set()
    for a in ast.walk(tree):
        if isinstance(a, (ast.Assign, ast.AnnAssign)) and a.value is not None:
            numeric = is_number_expr(a.value)
            # a NAMED anchor may be derived (KAPPA_ANCHOR = sb.MEDIAN_H / 365.0); an
            # unnamed one must be the bare literal 1380 in a numeric expression.
            derived = isinstance(a.value, (ast.BinOp, ast.Attribute, ast.Name, ast.UnaryOp))
            for n in targets(a):
                if (ANCHOR_NAME.search(n) and (numeric or derived)) or (numeric and has_1380(a.value)):
                    names.add(n)
    for a in tree.body:
        if isinstance(a, (ast.Assign, ast.AnnAssign)) and a.value is not None:
            for n in targets(a):
                if n in names and not isinstance(a.value, ast.Name):
                    try:
                        compile(ast.Expression(a.value), "<x>", "eval")
                        top.add(n)
                    except Exception:
                        pass
    return names, top


def names_in(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def assert_nodes(tree):
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            out.append(n)
        elif isinstance(n, ast.If) and any(
                isinstance(s, ast.Raise) and "AssertionError" in ast.dump(s) for s in n.body):
            out.append(n.test and ast.Assert(test=n.test, msg=None))
    return out


def reached(tree, anchors):
    funcs = {f.name: f for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)}
    mentions = {name: names_in(f) for name, f in funcs.items()}
    # closure: a function "touches" an anchor if it, or something it calls, names one
    touches = {n for n, m in mentions.items() if m & anchors}
    changed = True
    while changed:
        changed = False
        for n, m in mentions.items():
            if n not in touches and m & touches:
                touches.add(n)
                changed = True
    # data flow, over-approximated across the whole file: a name is tainted if it is
    # an anchor, or is assigned from an expression naming a tainted name or a
    # touching function, or is a parameter of a function called with a tainted argument.
    tainted = set(anchors) | touches
    changed = True
    while changed:
        changed = False
        for a in ast.walk(tree):
            if isinstance(a, (ast.Assign, ast.AnnAssign, ast.AugAssign)) and a.value is not None:
                if names_in(a.value) & tainted:
                    tg = a.targets if isinstance(a, ast.Assign) else [a.target]
                    for t in tg:
                        for nme in names_in(t):
                            if nme not in tainted:
                                tainted.add(nme)
                                changed = True
            elif isinstance(a, ast.For) and names_in(a.iter) & tainted:
                for nme in names_in(a.target):
                    if nme not in tainted:
                        tainted.add(nme)
                        changed = True
            elif isinstance(a, ast.Call):
                fname = a.func.id if isinstance(a.func, ast.Name) else None
                if fname in funcs:
                    params = [p.arg for p in funcs[fname].args.args]
                    for i, arg in enumerate(a.args):
                        if i < len(params) and names_in(arg) & tainted and params[i] not in tainted:
                            tainted.add(params[i])
                            changed = True
                    for kw in a.keywords:
                        if kw.arg and names_in(kw.value) & tainted and kw.arg not in tainted:
                            tainted.add(kw.arg)
                            changed = True
    hit = 0
    for a in assert_nodes(tree):
        if names_in(a) & tainted:
            hit += 1
    return hit


def pins_literal(tree):
    n_pin = 0
    for a in assert_nodes(tree):
        pinned = False
        for c in ast.walk(a):
            if isinstance(c, ast.Compare):
                for k in ast.walk(c):
                    if isinstance(k, ast.Constant) and isinstance(k.value, (int, float)) \
                            and not isinstance(k.value, bool):
                        v = abs(float(k.value))
                        if v in STRUCTURAL or v < 1e-3:
                            continue
                        pinned = True
        n_pin += pinned
    return n_pin


def writes_files(tree):
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            nm = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
            if nm in WRITE_CALLS:
                return True
            if nm == "open" and len(n.args) > 1 and isinstance(n.args[1], ast.Constant) \
                    and any(ch in str(n.args[1].value) for ch in "wax"):
                return True
    return False


class Timeout(Exception):
    pass


def _alarm(sig, frm):
    raise Timeout()


def run_tests(mod, failed=None):
    """Call every no-argument test function; call a one-argument self_tests(results)
    with mod.run() when the module has a run(). Collects names of failing tests."""
    ran = 0
    for name in dir(mod):
        fn = getattr(mod, name)
        if callable(fn) and TEST_NAME.match(name) and getattr(fn, "__module__", "") == mod.__name__:
            try:
                nargs = fn.__code__.co_argcount - len(fn.__defaults__ or ())
            except AttributeError:
                continue
            if nargs == 0:
                args = ()
            elif nargs == 1 and callable(getattr(mod, "run", None)):
                args = (mod.run(),)
            else:
                continue
            try:
                fn(*args)
            except AssertionError:
                if failed is None:
                    raise
                failed.append(name)
            ran += 1
    return ran


def dynamic(path, top_anchors):
    """-> status, detail.  status in {'not-run', 'no-tests', 'baseline-fails',
    'FAILS-WHEN-SCALED', 'survives-scaling'}"""
    spec = importlib.util.spec_from_file_location("_cand_" + str(abs(hash(path))), path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(path))
    signal_ok = hasattr(signal, "SIGALRM")
    try:
        if signal_ok:
            signal.signal(signal.SIGALRM, _alarm)
            signal.alarm(40)
        spec.loader.exec_module(mod)
        ran = run_tests(mod)
        if ran == 0:
            return "no-tests", ""
        killers = []
        for nm in sorted(top_anchors):
            v = getattr(mod, nm, None)
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                continue
            for f in (2.0, 0.5):
                setattr(mod, nm, v * f)
                try:
                    failed = []
                    run_tests(mod, failed)
                    if failed:
                        killers.append(f"{nm}x{f}:{'+'.join(failed)}")
                except Exception:
                    pass
                finally:
                    setattr(mod, nm, v)
        return ("FAILS-WHEN-SCALED" if killers else "survives-scaling"), ",".join(killers)
    except Timeout:
        return "not-run", "timeout"
    except AssertionError:
        return "baseline-fails", ""
    except BaseException as e:                       # noqa: BLE001
        return "not-run", type(e).__name__
    finally:
        if signal_ok:
            signal.alarm(0)
        if sys.path and sys.path[0] == os.path.dirname(path):
            sys.path.pop(0)


def main():
    t0 = time.time()
    rows, all_n = [], 0
    for p in sorted(py_files()):
        all_n += 1
        try:
            tree = ast.parse(open(p, encoding="utf-8").read())
        except Exception:
            continue
        names, top = anchors_in(tree)
        if not names:
            continue
        guard = any(isinstance(n, ast.If) and "__main__" in ast.dump(n.test) for n in tree.body)
        rows.append(dict(path=os.path.relpath(p, ROOT).replace("\\", "/"), names=sorted(names),
                         top=top, tree=tree, guard=guard, writes=writes_files(tree),
                         reached=reached(tree, names), pins=pins_literal(tree),
                         n_assert=len(assert_nodes(tree))))
    print(f"scripts scanned: {all_n}; assign a named anchor: {len(rows)}")
    for r in rows:
        if not r["guard"] or r["writes"]:
            r["dyn"], r["dyn_detail"] = "not-run", "no __main__ guard or writes files"
            continue
        try:                                          # one child per script, hard 60 s limit
            cp = subprocess.run([sys.executable, os.path.abspath(__file__), "--dyn",
                                 os.path.join(ROOT, r["path"]), ",".join(sorted(r["top"]))],
                                capture_output=True, text=True, timeout=60, cwd=tempfile.gettempdir())
            line = [x for x in cp.stdout.splitlines() if x.startswith("DYN|")]
            st, _, det = (line[-1][4:].partition("|") if line else ("not-run", "", "child crashed"))
            r["dyn"], r["dyn_detail"] = st, det
        except subprocess.TimeoutExpired:
            r["dyn"], r["dyn_detail"] = "not-run", "timeout 60s"
    n = len(rows)
    c = lambda f: sum(1 for r in rows if f(r))                      # noqa: E731
    print(f"\nDENOMINATOR: {n} scripts assign a named anchor (of {all_n} scripts)")
    print(f"  with >= 1 assert at all:                          {c(lambda r: r['n_assert'] > 0)} / {n}")
    print(f"  REACHED: an assert touches the anchor (static):   {c(lambda r: r['reached'] > 0)} / {n}")
    print(f"  FAILS WHEN SCALED (dynamic, strict):              {c(lambda r: r['dyn'] == 'FAILS-WHEN-SCALED')} / {n}")
    for st in ("survives-scaling", "no-tests", "baseline-fails", "not-run"):
        print(f"    {st:<18}                              {c(lambda r, st=st: r['dyn'] == st)} / {n}")
    print(f"  PINS A LITERAL (heuristic, >=1 pinned assert):    {c(lambda r: r['pins'] > 0)} / {n}")
    print(f"  pins a literal and nothing reaches the anchor:    "
          f"{c(lambda r: r['pins'] > 0 and r['reached'] == 0)} / {n}")
    print(f"  total assert statements in these scripts: {sum(r['n_assert'] for r in rows)}; "
          f"pinned: {sum(r['pins'] for r in rows)}; touching an anchor: {sum(r['reached'] for r in rows)}")
    print("\nper script: path | anchors | asserts | reached | pins | dynamic")
    for r in rows:
        print(f"{r['path']} | {','.join(r['names'])[:48]} | {r['n_assert']} | {r['reached']} | "
              f"{r['pins']} | {r['dyn']} {r['dyn_detail']}")
    print(f"\nelapsed {time.time() - t0:.0f}s")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--dyn":
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):          # silence the script's own prints
            st, det = dynamic(sys.argv[2], set(filter(None, sys.argv[3].split(","))))
        print(f"DYN|{st}|{det}")
    else:
        main()
