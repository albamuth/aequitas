#!/bin/bash
# SessionStart hook for Claude Code cloud sessions.
#
# The simulations are plain Python on numpy/scipy, and the request picker
# needs PyYAML. A cloud container starts with none of that guaranteed, so
# install it before the agent's first command. Local sessions are left
# alone: the author's machine already has what it needs.
#
# Idempotent: pip skips what is already there. Synchronous on purpose, so
# the 04:00 agent cannot start running a sim before scipy exists.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

export PIP_DISABLE_PIP_VERSION_CHECK=1
export PIP_ROOT_USER_ACTION=ignore

# pymrio is deliberately absent: it is only used with 06-simulation/data/,
# which is never committed and so never present in a cloud clone.
python3 -m pip install --quiet numpy scipy pyyaml openpyxl

python3 - << 'PY'
import numpy, scipy, yaml, openpyxl
print(f"session-start: numpy {numpy.__version__}, scipy {scipy.__version__}, "
      f"pyyaml {yaml.__version__}, openpyxl {openpyxl.__version__}")
PY
