"""Where did the answer to each outside finding live?

For every finding in findings.py that had a pre-existing answer, build a query from the
critic's own words, rank every paragraph of Foundations and Conformance against it, and
classify:
    (a) the answer paragraph sits in a section the critic named
    (b) not (a), the answer paragraph ranks in the top K and shares >= MIN_SHARED query terms
    (c) otherwise: a query from the critic's words does not reach it
    (n) no answer existed before the finding (taken from the register, not tested here)

Run:      python answer_location.py            (writes results.json)
Self-test: python answer_location.py --test
"""
import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FOUNDATIONS = ROOT / "00-strategy" / "Aequitas_Foundations.md"
CONFORMANCE = ROOT / "00-strategy" / "Aequitas_Conformance.md"
sys.path.insert(0, str(HERE))
from findings import FINDINGS, EXCLUDED  # noqa: E402

KS = (5, 10, 25)          # the top-K cut-offs reported; K is the checker's choice, so all three are shown
MAIN_K = 10
MIN_SHARED = 2            # a hit must share at least this many distinct query terms
SEED = 20261022
CONTROL_DRAWS = 300

STOP = set("""
about above after again against also always among another because been before being below between both
cannot could does doing done down during each either else even ever every from further have having here
hers into itself just more most much must never next none only onto other ours over same shall should
since some such than that their them then there these they this those through thus under until upon very
well were what when where whether which while whom whose will with within without would your yours
""".split())


def stem(w):
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4 and not w.endswith("ss"):
            return w[: -len(suf)]
    return w


def tokens(text):
    out = []
    for w in re.findall(r"[a-z][a-z0-9'-]+", text.lower()):
        w = w.strip("'-")
        if len(w) < 4 or w in STOP:
            continue
        out.append(stem(w))
    return out


def ancestors(num):
    """'3.2c' -> {'§3.2c','§3.2','§3'}"""
    labels = {"§" + num}
    base = re.sub(r"[a-z]$", "", num)
    labels.add("§" + base)
    parts = base.split(".")
    for i in range(1, len(parts)):
        labels.add("§" + ".".join(parts[:i]))
    return labels


def load_paragraphs():
    """Every non-empty line of both files, with the section labels it sits under."""
    paras = []
    cur = {"§0"}
    leaf = "0"
    for path, tag in ((FOUNDATIONS, "F"), (CONFORMANCE, "C")):
        cur = {"§0"} if tag == "F" else {"conf"}
        leaf = "0" if tag == "F" else "conf"
        for ln, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"^#{2,5}\s+(.*)", line)
            if m and tag == "F":
                head = m.group(1)
                a = re.match(r"A(\d) \(", head)     # axiom headings only: 'A8 (no governing body)'
                n = re.match(r"(\d+(?:\.\d+)*[a-z]?)\.?\s", head)
                if a:
                    cur = {"A" + a.group(1), "§1"}
                    leaf = "A" + a.group(1)
                elif n:
                    cur = ancestors(n.group(1))
                    leaf = n.group(1)
                # an unnumbered sub-heading inherits the section above it
                continue
            labels = set(cur)
            lf = leaf
            if tag == "C":
                r = re.match(r"^\|\s*(\d+[a-z]?)\s*\|", line)
                if r:
                    labels = {"conf", "conf-" + r.group(1)}
                    lf = "conf-" + r.group(1)
            toks = tokens(line)
            if len(toks) < 8:
                continue
            paras.append(dict(src=tag, line=ln, text=line, toks=toks, labels=labels, leaf=lf, tag=tag))
    return paras


class BM25:
    def __init__(self, paras, k1=1.5, b=0.75):
        self.paras, self.k1, self.b = paras, k1, b
        self.tf = [Counter(p["toks"]) for p in paras]
        self.len = [len(p["toks"]) for p in paras]
        self.avg = sum(self.len) / len(self.len)
        df = Counter()
        for c in self.tf:
            df.update(c.keys())
        n = len(paras)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def score(self, qterms, i):
        s = 0.0
        tf, L = self.tf[i], self.len[i]
        for t in qterms:
            f = tf.get(t, 0)
            if f:
                s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * L / self.avg))
        return s

    def ranks_of(self, qterms, idx):
        """rank of paragraph idx (1 = best); ties do not help it."""
        mine = self.score(qterms, idx)
        if mine == 0:
            return len(self.paras) + 1      # a zero score is not reached, whatever the ties
        better = sum(1 for j in range(len(self.paras)) if self.score(qterms, j) > mine)
        return better + 1


def find_anchor(paras, anchor):
    hits = [i for i, p in enumerate(paras) if anchor in p["text"]]
    return hits


def classify(f, paras, bm, k):
    """Return dict with mech class for one finding at cut-off k (only for testable rows)."""
    q = sorted(set(tokens(f["text"])))
    hits = find_anchor(paras, f["anchor"])
    idx = hits[0]
    p = paras[idx]
    named = set(f["named"])
    shared = len(set(p["toks"]) & set(q))
    rank = bm.ranks_of(q, idx)
    if named & p["labels"]:
        cls = "a"
    elif rank <= k and shared >= MIN_SHARED:
        cls = "b"
    else:
        cls = "c"
    # Section arm (added after the first run, see RESULTS.md): the answer is the whole leaf section,
    # so the best-ranked paragraph in that section counts. More generous than the anchor line.
    sect = [j for j, x in enumerate(paras) if x["leaf"] == p["leaf"] and x["tag"] == p["tag"]]
    best_j = min(sect, key=lambda j: bm.ranks_of(q, j))
    best_rank = bm.ranks_of(q, best_j)
    best_shared = len(set(paras[best_j]["toks"]) & set(q))
    if named & p["labels"]:
        scls = "a"
    elif best_rank <= k and best_shared >= MIN_SHARED:
        scls = "b"
    else:
        scls = "c"
    return dict(cls=cls, rank=rank, shared=shared, nq=len(q), para_labels=sorted(p["labels"]),
                para_line=p["line"], para_src=p["src"], n_hits=len(hits),
                sect_cls=scls, sect_rank=best_rank, sect_shared=best_shared, sect_n=len(sect),
                sect_leaf=p["leaf"])


def chance_rate(paras, bm, f, k, rng):
    """Control: how often does a random paragraph clear the (b) bar under this critic's query?"""
    q = sorted(set(tokens(f["text"])))
    hit = 0
    for _ in range(CONTROL_DRAWS):
        i = rng.randrange(len(paras))
        shared = len(set(paras[i]["toks"]) & set(q))
        if shared >= MIN_SHARED and bm.ranks_of(q, i) <= k:
            hit += 1
    return hit / CONTROL_DRAWS


def run():
    paras = load_paragraphs()
    bm = BM25(paras)
    rng = random.Random(SEED)
    rows = []
    for f in FINDINGS:
        row = dict(id=f["id"], critic=f["critic"], register=f["register"], prior=f["prior"],
                   hand=f["hand"], text_kind=f["text_kind"], dup_of=f.get("dup_of"))
        if f["anchor"]:
            row["mech"] = {k: classify(f, paras, bm, k) for k in KS}
            row["chance_b"] = chance_rate(paras, bm, f, MAIN_K, rng)
            ph = f.get("claimed_phrase")
            if ph:
                row["claimed_phrase_in_current_text"] = any(ph in p["text"].lower() for p in paras)
        else:
            row["mech"] = None
            row["why_untested"] = f.get("anchor_note", "no pre-existing answer to locate" if f["prior"] == "none" else "")
        rows.append(row)
    return dict(n_paragraphs=len(paras), foundations_version=_version(), rows=rows)


def _version():
    m = re.search(r"\*\*Version:\*\*\s*([0-9.]+)", FOUNDATIONS.read_text(encoding="utf-8"))
    return m.group(1) if m else "?"


def summarise(res):
    rows = res["rows"]
    out = {"n_findings": len(rows)}
    out["prior_none"] = sum(1 for r in rows if r["prior"] == "none")
    out["prior_any"] = sum(1 for r in rows if r["prior"] in ("full", "partial"))
    out["prior_full"] = sum(1 for r in rows if r["prior"] == "full")
    out["prior_partial"] = sum(1 for r in rows if r["prior"] == "partial")
    # without the duplicate row F10
    out["prior_any_dedup"] = sum(1 for r in rows if r["prior"] in ("full", "partial") and not r["dup_of"])
    tested = [r for r in rows if r["mech"]]
    out["tested"] = len(tested)
    for k in KS:
        c = Counter(r["mech"][k]["cls"] for r in tested)
        out[f"mech_k{k}"] = {x: c.get(x, 0) for x in "abc"}
        cs = Counter(r["mech"][k]["sect_cls"] for r in tested)
        out[f"sect_k{k}"] = {x: cs.get(x, 0) for x in "abc"}
    ans = [r for r in rows if r["prior"] in ("full", "partial")]
    c = Counter(r["hand"] for r in ans)
    out["hand_among_prior"] = {x: c.get(x, 0) for x in "abc"}
    agree = sum(1 for r in tested if r["hand"] == r["mech"][MAIN_K]["cls"])
    out["hand_vs_mech_agree_k10"] = [agree, len(tested)]
    out["hand_vs_sect_agree_k10"] = [sum(1 for r in tested if r["hand"] == r["mech"][MAIN_K]["sect_cls"]), len(tested)]
    out["chance_b_mean"] = sum(r["chance_b"] for r in tested) / len(tested)
    # robustness: rows whose class changes across K
    out["rows_changing_with_k"] = [r["id"] for r in tested
                                   if len({r["mech"][k]["cls"] for k in KS}) > 1]
    return out


# ---------------------------------------------------------------- self-tests
def selftest():
    paras = load_paragraphs()
    bm = BM25(paras)
    fails = []

    def check(name, cond):
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            fails.append(name)

    # 1. every anchor is found exactly once (fails if a document edit moves the text)
    for f in FINDINGS:
        if f["anchor"]:
            n = len(find_anchor(paras, f["anchor"]))
            check(f"anchor for {f['id']} found exactly once (found {n})", n == 1)

    # 2. a paragraph's own words must put it first (the ranker works at all)
    probe = max(paras, key=lambda p: len(set(p["toks"])))
    q = sorted(set(probe["toks"]))
    i = paras.index(probe)
    check("a paragraph queried with its own words ranks first", bm.ranks_of(q, i) == 1)

    # 3. a query of only stop-words and short words reaches nothing
    check("stop-word query yields no terms", tokens("the and with from that this") == [])

    # 4. an unrelated query must not rank the N paragraph in the top 10
    n_idx = find_anchor(paras, "is a physical total measured outside the ledger")[0]
    q2 = sorted(set(tokens("sourdough bread fermentation temperature crust")))
    check("unrelated query ranks the N paragraph below 10", bm.ranks_of(q2, n_idx) > 10)

    # 5. the control: a random paragraph clears the (b) bar rarely (a bar that anything clears is no bar)
    rng = random.Random(1)
    rates = [chance_rate(paras, bm, f, MAIN_K, rng) for f in FINDINGS if f["anchor"]]
    check(f"chance rate of a random paragraph clearing (b) is under 5% (max {max(rates):.3f})",
          max(rates) < 0.05)

    # 6. the (a) rule can fail: with the named list emptied, no row is class (a)
    n_a = 0
    for f in FINDINGS:
        if f["anchor"]:
            g = dict(f, named=[])
            n_a += classify(g, paras, bm, MAIN_K)["cls"] == "a"
    check("with named sections removed, no row is class (a)", n_a == 0)

    # 6b. section labelling: the N paragraph sits in 4.4 (a mislabel as an axiom once put it in A7)
    n_par = paras[find_anchor(paras, "is a physical total measured outside the ledger")[0]]
    check("the N paragraph is labelled section 4.4, not an axiom", n_par["leaf"] == "4.4")
    a8 = paras[find_anchor(paras, "neither may the conformance requirements")[0]]
    check("the A8 clause is labelled A8 and section 1", a8["leaf"] == "A8" and "§1" in a8["labels"])

    # 7. the table is complete: no finding is both 'prior none' and carrying an anchor
    bad = [f["id"] for f in FINDINGS if f["prior"] == "none" and f["anchor"]]
    check("no 'prior none' finding carries an anchor", not bad)

    print("ALL PASS" if not fails else f"{len(fails)} FAILED")
    return 0 if not fails else 1


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(selftest())
    res = run()
    res["summary"] = summarise(res)
    res["excluded"] = EXCLUDED
    (HERE / "results.json").write_text(json.dumps(res, indent=1, default=list), encoding="utf-8")
    print(json.dumps(res["summary"], indent=1))
    print()
    print(f"{'id':4} {'prior':8} {'hand':4} " + " ".join(f"k{k:<3}" for k in KS)
          + "  rank shared  | section arm: cls rank shared n_paras leaf | critic")
    for r in res["rows"]:
        if r["mech"]:
            m = r["mech"]
            print(f"{r['id']:4} {r['prior']:8} {r['hand']:4} "
                  + " ".join(f"{m[k]['cls']:4}" for k in KS)
                  + f"  {m[MAIN_K]['rank']:4} {m[MAIN_K]['shared']:3}/{m[MAIN_K]['nq']:<3}"
                  + f" | {m[MAIN_K]['sect_cls']} {m[MAIN_K]['sect_rank']:4} {m[MAIN_K]['sect_shared']:2}"
                  + f" {m[MAIN_K]['sect_n']:3} {m[MAIN_K]['sect_leaf']:8} | {r['critic']}")
        else:
            print(f"{r['id']:4} {r['prior']:8} {r['hand']:4} {'-':4} {'-':4} {'-':4}  {r['critic']}")
