"""
anchor.py -- the one reader of the median-lifestyle anchor file.

Every sim that needs the 1,380 h/yr anchor imports `load()` from here instead of
typing the number. `load()` hashes median_lifestyle_anchor.json (line endings
normalised to LF, so Windows and Linux checkouts agree) and raises AnchorDigestError
if the digest is not PINNED_SHA256. Changing the file means changing the pin in
this file, which shows in a diff, and invalidates every earlier run's logged digest.

A sim may override the value only through `load(value=...)`, which keeps the
digest check on the file and records the override in the returned dict
("overridden": True). That is how a sweep at 1,350 / 1,400 stays honest.
"""
from __future__ import annotations

import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ANCHOR_PATH = os.path.join(HERE, "median_lifestyle_anchor.json")
PINNED_SHA256 = "1d53b2f36d3df2671e97cf0f710f96c799377a5545218df9140aeaf294a4e970"


class AnchorDigestError(RuntimeError):
    pass


def digest(path: str = ANCHOR_PATH) -> str:
    with open(path, "rb") as fh:
        raw = fh.read().replace(b"\r\n", b"\n")
    return hashlib.sha256(raw).hexdigest()


def load(value: float | None = None, path: str = ANCHOR_PATH,
         pinned: str = PINNED_SHA256) -> dict:
    got = digest(path)
    if got != pinned:
        raise AnchorDigestError(
            f"anchor file digest {got} != pinned {pinned}; "
            "the published anchor changed. Re-pin deliberately or restore the file.")
    with open(path, "r", encoding="utf-8") as fh:
        a = json.load(fh)
    a["sha256"] = got
    a["overridden"] = value is not None
    a["file_value"] = a["value"]
    if value is not None:
        a["value"] = float(value)
    return a


def kappa(a: dict) -> float:
    """debit-h/day per median-lifestyle unit = value / 365."""
    return a["value"] / 365.0
