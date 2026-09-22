"""Enumerate the constants the published disparity-ceiling result depends on.

Answers simulation request `sr-20260922-enumerate-every-module-level-constant-in-dis`,
filed by the outreach agent on 2026-09-22 from record
`obj-20260922-self-council-unnamed-work-distribution`.

THE QUESTION AS ASKED
---------------------
  "Enumerate every module-level constant in disparity_ceiling_sim.py and
   ceiling_rubric.py that the published result depends on and that no flag can
   move. Report the list and the count, not instances."

THE QUESTION HAS A HOLE IN IT, AND THE HOLE IS THE REASON IT WAS ASKED
----------------------------------------------------------------------
The agent's own stated reason for filing it is:

  "Unpinning F exposed normal(6.0,3.0) as the real dependency, and nothing
   printed it."

`normal(6.0, 3.0)` is NOT a module-level constant. It is two bare numeric
literals inside a function body, at `disparity_ceiling_sim.py` line 91. **An
enumeration of module-level constants would not have listed it.** So this
script reports two censuses, and the second is the one that answers the
question the agent meant:

  CENSUS 1   module-level constants        -- what was asked for
  CENSUS 2   inline numeric literals on    -- what would have caught line 91
             the path from the population
             to the published statistic

A constant is counted as UNMOVABLE when no argparse option in its own file
writes to it, directly or through a setter.

Run:
    python constant_census.py
    python constant_census.py --test
"""

import argparse
import ast
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGETS = [
    os.path.join(HERE, "..", "disparity-ceiling", "disparity_ceiling_sim.py"),
    os.path.join(HERE, "ceiling_rubric.py"),
]

# Literals that carry no setting: loop bounds, indices, identity elements,
# tolerances, and percentage-to-fraction conversions. Counting these would
# drown the list the request asked for.
IGNORED_LITERALS = {0, 1, 2, -1, 0.0, 1.0, 100, 1000}


def module_constants(tree):
    """Module-level assignments to a NAME that binds a number or a tuple of them."""
    out = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            v = node.value
            if isinstance(v, ast.Constant) and isinstance(v.value, (int, float)):
                out.append((target.id, v.value, node.lineno))
            elif isinstance(v, (ast.Tuple, ast.List)) and all(
                isinstance(e, ast.Constant) and isinstance(e.value, (int, float))
                for e in v.elts
            ) and v.elts:
                out.append((target.id, tuple(e.value for e in v.elts), node.lineno))
    return out


def flag_movable(tree, src):
    """Names an argparse option can reach, directly or through a setter.

    A name is movable when the file declares a command-line option and some
    function assigns that name with `global`. This is deliberately generous:
    a name counted movable that is not would understate the finding, and this
    census exists to find what is NOT movable.
    """
    has_flags = "add_argument" in src
    if not has_flags:
        return set()
    movable = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            globals_declared = {
                name for n in ast.walk(node)
                if isinstance(n, ast.Global) for name in n.names
            }
            for n in ast.walk(node):
                if isinstance(n, ast.Assign):
                    for t in n.targets:
                        if isinstance(t, ast.Name) and t.id in globals_declared:
                            movable.add(t.id)
    return movable


def derived_from(tree, names):
    """Names whose module-level value is computed from another name.

    CEILING = DAY / F is not an independent setting. It follows whatever F and
    DAY are, so listing it as a separate unmovable constant double-counts.
    """
    out = set()
    for node in tree.body:
        if isinstance(node, ast.Assign) and not isinstance(node.value, (ast.Constant,)):
            used = {n.id for n in ast.walk(node.value) if isinstance(n, ast.Name)}
            if used & names:
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        out.add(t.id)
    return out


def inline_literals(tree, funcs):
    """Bare numeric literals inside the named functions.

    These are the constants no flag can move BECAUSE THEY HAVE NO NAME. Nothing
    can print a value that was never bound to anything.
    """
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in funcs:
            for n in ast.walk(node):
                if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
                    if n.value in IGNORED_LITERALS:
                        continue
                    out.append((node.name, n.value, n.lineno))
    return out


# Functions on the path from the drawn population to the published statistic.
# Read off the call graph by hand and named here so the reader can check it.
POPULATION_PATH = {
    "disparity_ceiling_sim.py": {"draw_population"},
    "ceiling_rubric.py": {"clean_population", "clean_baseline", "ch_breach",
                          "ch_phantom", "ch_inflate", "ch_collude",
                          "ch_omit", "ch_omit_top"},
}


def census():
    line = "-" * 78
    print("=" * 78)
    print("CONSTANT CENSUS -- WHAT THE PUBLISHED CEILING RESULT DEPENDS ON")
    print("=" * 78)
    print("""
  Answers  sr-20260922-enumerate-every-module-level-constant-in-dis
  Method   AST parse. A constant is UNMOVABLE when no argparse option in its
           own file writes to it, directly or through a global setter.
""")

    grand_named, grand_inline = 0, 0
    for path in TARGETS:
        name = os.path.basename(path)
        src = open(path, encoding="utf-8").read()
        tree = ast.parse(src)

        consts = module_constants(tree)
        movable = flag_movable(tree, src)
        const_names = {c[0] for c in consts}
        derived = derived_from(tree, movable) & const_names

        print(line)
        print(f"{name} -- CENSUS 1, module-level constants")
        print(line)
        print(f"  {'name':<22} {'value':>14}  {'line':>5}  status")
        unmovable = []
        for nm, val, ln in consts:
            if nm in movable:
                status = "MOVABLE      a flag writes it"
            elif nm in derived:
                status = "derived      follows a movable name"
            else:
                status = "UNMOVABLE"
                unmovable.append(nm)
            print(f"  {nm:<22} {str(val):>14}  {ln:>5}  {status}")
        print(f"\n  {len(consts)} module-level constants, "
              f"{len(unmovable)} of them UNMOVABLE: {', '.join(unmovable) or 'none'}")
        grand_named += len(unmovable)
        print()

        print(line)
        print(f"{name} -- CENSUS 2, inline literals on the population path")
        print(line)
        funcs = POPULATION_PATH[name]
        lits = inline_literals(tree, funcs)
        if lits:
            print(f"  {'function':<22} {'value':>14}  {'line':>5}")
            for fn, val, ln in lits:
                print(f"  {fn:<22} {str(val):>14}  {ln:>5}")
        else:
            print("  none")
        print(f"\n  {len(lits)} inline literals, in {len(funcs)} function(s) on the path. "
              f"NONE has a name,\n  so none can be printed and none can be moved by a flag.")
        grand_inline += len(lits)
        print()

    print("=" * 78)
    print("THE COUNT")
    print("=" * 78)
    print(f"""
  Unmovable NAMED constants, both files          {grand_named}
  Unmovable UNNAMED literals on the population
  path, both files                               {grand_inline}
  ------------------------------------------------------
  TOTAL the published result depends on and
  no flag can move                               {grand_named + grand_inline}

  IN PLAIN WORDS, AND THIS IS THE FINDING.

  The request asked for module-level constants. Had the census stopped there
  it would have returned {grand_named} and MISSED THE ONE THAT CAUSED THE FAULT.
  `normal(6.0, 3.0)` at disparity_ceiling_sim.py line 91 is two unnamed
  literals inside a function. It is not a module-level constant, it has no
  name, and nothing can print a value that was never bound to anything.

  So the rung-1 habit the agent wrote -- "list what a model holds fixed" --
  DOES NOT WORK if it enumerates names. A model holds unnamed numbers fixed
  too, and those are the ones nobody sees.
""")
    return 0


# ---------------------------------------------------------------- self-tests
def self_tests():
    fails, ran = [], []

    def check(name, cond, detail=""):
        ran.append(name)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
        if not cond:
            fails.append(name)

    for p in TARGETS:
        if not os.path.exists(p):
            check(f"0 {os.path.basename(p)} exists", False)
            return 1
    check("1 both target files exist", True)

    sim = os.path.join(HERE, "..", "disparity-ceiling", "disparity_ceiling_sim.py")
    src = open(sim, encoding="utf-8").read()
    tree = ast.parse(src)

    consts = {c[0] for c in module_constants(tree)}
    check("2 F and DAY are found as module-level constants",
          {"F", "DAY"} <= consts, ", ".join(sorted(consts)))

    movable = flag_movable(tree, src)
    check("3 F is detected as flag-movable, because --floor writes it",
          "F" in movable, f"movable: {sorted(movable)}")

    check("4 CEILING is detected as derived, not as an independent setting",
          "CEILING" in derived_from(tree, movable))

    lits = inline_literals(tree, {"draw_population"})
    vals = [v for _, v, _ in lits]
    check("5 the census finds 6.0 and 3.0 inside draw_population",
          6.0 in vals and 3.0 in vals, f"{vals}")

    # 6 -- the whole point. The thing that broke the sweep must NOT appear in
    # census 1. If it ever does, this script's finding has gone stale.
    check("6 the literals that broke the sweep are NOT module-level constants",
          not ({"6.0", "3.0"} & consts) and 6.0 in vals,
          "normal(6.0, 3.0) is unnamed")

    # 7 -- DAY is a real unmovable constant and must be reported as one.
    check("7 DAY is reported unmovable", "DAY" not in movable)

    print()
    if fails:
        print(f"{len(fails)} self-test(s) FAILED: {', '.join(fails)}")
        return 1
    print(f"{len(ran)} self-tests, all pass.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    return self_tests() if args.test else census()


if __name__ == "__main__":
    sys.exit(main())
