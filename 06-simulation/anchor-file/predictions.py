"""
predictions.py -- evaluate predictions.json against measured rho*, and log the result.

predictions_log.jsonl is append-only:
  line 1  {"type": "registered", "predictions_sha256": ..., "date": ...}   written once
  later   {"type": "result", "run": ..., "id": ..., "observed": ..., "passed": ...}

If predictions.json no longer matches the registered sha256, `evaluate` raises
PredictionsEditedError. The file is therefore a commitment, not a test the
author can quietly retune.

`measure(F, shock, anchor_value)` is supplied by the caller (it runs the sweep).
"""
from __future__ import annotations

import hashlib
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PRED_PATH = os.path.join(HERE, "predictions.json")
LOG_PATH = os.path.join(HERE, "predictions_log.jsonl")


class PredictionsEditedError(RuntimeError):
    pass


def _sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read().replace(b"\r\n", b"\n")).hexdigest()


def _registered(log_path):
    if not os.path.exists(log_path):
        return None
    with open(log_path, "r", encoding="utf-8") as fh:
        first = fh.readline().strip()
    if not first:
        return None
    rec = json.loads(first)
    return rec["predictions_sha256"] if rec.get("type") == "registered" else None


def evaluate(measure, pred_path=PRED_PATH, log_path=LOG_PATH, run_id=None, write_log=True):
    sha = _sha(pred_path)
    reg = _registered(log_path)
    if reg is None:
        if write_log:
            with open(log_path, "a", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps({"type": "registered", "predictions_sha256": sha,
                                     "date": time.strftime("%Y-%m-%d")}) + "\n")
    elif reg != sha:
        raise PredictionsEditedError(
            f"predictions.json sha256 {sha} != registered {reg}: the file was edited.")
    with open(pred_path, "r", encoding="utf-8") as fh:
        preds = json.load(fh)["predictions"]
    run_id = run_id or time.strftime("%Y-%m-%dT%H:%M:%S")
    out = []
    for p in preds:
        if p["kind"] == "cell":
            obs = measure(p["F"], p["shock"], p["anchor"])
            ok = obs is not None and p["lo"] <= obs <= p["hi"]
        elif p["kind"] == "order":
            obs = [measure(p["F"], p["shock"], a) for a in p["anchors"]]
            ok = all(o is not None for o in obs) and all(x <= y for x, y in zip(obs, obs[1:]))
        elif p["kind"] == "spread":
            a, b = (measure(p["F"], p["shock"], x) for x in p["anchors"])
            obs = None if a is None or b is None else round(b - a, 4)
            ok = obs is not None and p["lo"] <= obs <= p["hi"]
        else:
            raise ValueError(p["kind"])
        out.append((p, obs, bool(ok)))
    if write_log:
        with open(log_path, "a", encoding="utf-8", newline="\n") as fh:
            for p, obs, ok in out:
                fh.write(json.dumps({"type": "result", "run": run_id, "id": p["id"],
                                     "observed": obs, "passed": ok}) + "\n")
    return out
