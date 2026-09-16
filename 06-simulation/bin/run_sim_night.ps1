<#
    Nightly Aequitas simulation run. 04:00 local.

    The 03:00 outreach agent posts in public and does NOT run simulations
    (ruled 2026-08-25). This is the other half: it runs them and never posts.

    The guard here is NOT Claude's permission system. It is that this agent
    has nothing to publish with -- no board key, no git push, and a brief
    that forbids writing outside 06-simulation\. Loosening the permission
    flag below cannot cause anything to become public.

    Run by hand:  powershell -ExecutionPolicy Bypass -File bin\run_sim_night.ps1
    No agent:     ... -NoAgent      builds and checks the prompt, does not invoke Claude
    Preflight:    ... -WhatIfOnly   stops after the checks
#>

param(
    [switch]$WhatIfOnly,
    [switch]$NoAgent,      # everything except invoking Claude; leaves the exact
                           # prompt at log\tmp\prompt-<stamp>.md
    [string]$Model = "opus"
)

$ErrorActionPreference = "Stop"

$Root       = Split-Path -Parent $PSScriptRoot      # 06-simulation\
$RepoRoot   = Split-Path -Parent $Root              # repository root
$PromptFile = Join-Path $Root "SIM_NIGHTLY_PROMPT.md"
$BriefFile  = Join-Path $Root "SIM_AGENT_BRIEF.md"
$LogDir     = Join-Path $Root "log"
$RunLogDir  = Join-Path $LogDir "runs"
$Stamp      = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd_HHmmss")
$Today      = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
$RunLog     = Join-Path $RunLogDir "run-$Stamp.txt"

New-Item -ItemType Directory -Force -Path $RunLogDir | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $LogDir "tmp") | Out-Null

# The agent's paths are all repo-root-relative, so that is where it runs.
Set-Location $RepoRoot

"=== sim preflight $Stamp ===" | Tee-Object -FilePath $RunLog

foreach ($f in @($PromptFile, $BriefFile)) {
    if (-not (Test-Path $f)) {
        "FATAL: missing $f" | Tee-Object -FilePath $RunLog -Append
        exit 1
    }
}

# --- pick tonight's request ----------------------------------------------
# Windows PowerShell 5.1 decodes a native command's stdout using the console
# codepage, not UTF-8. python prints UTF-8, so without the two lines below a
# "·" arrives as "┬╖". The outreach runner lost a whole night to this on
# 2026-08-26: the agent reported its brief as missing when it was unreadable.
$prevConsoleOut = [Console]::OutputEncoding
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
$env:PYTHONIOENCODING = "utf-8"

$prev = $ErrorActionPreference
$ErrorActionPreference = "Continue"

$ReqOut = Join-Path $LogDir "tmp\request-$Stamp.txt"
& python 06-simulation\bin\pick_sim.py 2>&1 | Set-Content -Path $ReqOut -Encoding utf8
$pickRc = $LASTEXITCODE

$ErrorActionPreference = $prev
[Console]::OutputEncoding = $prevConsoleOut

$SimRequest = (Get-Content -Raw -Encoding UTF8 -Path $ReqOut)

if ($pickRc -eq 3) {
    "NOTHING TO DO -- no open simulation request." | Tee-Object -FilePath $RunLog -Append
    $SimRequest | Tee-Object -FilePath $RunLog -Append
    "Not invoking Claude. This is a clean no-op, not a failure." | Tee-Object -FilePath $RunLog -Append
    exit 0
}
if ($pickRc -ne 0) {
    "PICKER FAILED (exit $pickRc):" | Tee-Object -FilePath $RunLog -Append
    $SimRequest | Tee-Object -FilePath $RunLog -Append
    exit 1
}

$SimRequest | Tee-Object -FilePath $RunLog -Append

if ($WhatIfOnly) {
    "WhatIfOnly: preflight passed, not invoking Claude." | Tee-Object -FilePath $RunLog -Append
    exit 0
}

# --- build the prompt ----------------------------------------------------
# -Encoding UTF8 is not optional. Get-Content in 5.1 defaults to the ANSI
# codepage and the prompt file is UTF-8, so "§4" arrives as "Â§4" without it.
$prompt = (Get-Content -Raw -Encoding UTF8 -Path $PromptFile) -replace "<SIM_REQUEST>", $SimRequest
$prompt = $prompt -replace "<TODAY>", $Today

$PromptOut = Join-Path $LogDir "tmp\prompt-$Stamp.md"
Set-Content -Path $PromptOut -Value $prompt -Encoding utf8
"prompt handed to agent: $PromptOut" | Tee-Object -FilePath $RunLog -Append

# Assert every placeholder was substituted. The outreach runner learned this
# the hard way: an unsubstituted <SIM_TRANSCRIPT> reached the agent and could
# not be reproduced afterwards, because nothing had kept the prompt.
$leftover = ([regex]'<[A-Z][A-Z0-9_]{2,}>').Matches($prompt) |
            ForEach-Object { $_.Value } | Select-Object -Unique
if ($leftover.Count -gt 0) {
    "FATAL: $($leftover.Count) placeholder(s) never substituted:" | Tee-Object -FilePath $RunLog -Append
    $leftover | ForEach-Object { "  $_" | Tee-Object -FilePath $RunLog -Append }
    exit 1
}

if ($NoAgent) {
    "NoAgent: prompt built and checked, Claude NOT invoked." | Tee-Object -FilePath $RunLog -Append
    "Read the prompt the agent would have got: $PromptOut" | Tee-Object -FilePath $RunLog -Append
    exit 0
}

# --- the run -------------------------------------------------------------
# acceptEdits: file writes proceed without a prompt, so a 4am run does not
# stall on a dialog nobody is awake to answer. The boundary is the brief and
# the fact that this agent has no key, no remote and nothing to publish with.
# The prompt goes in on STDIN, not as an argument: Windows caps a whole
# command line at 32,767 characters and a prompt can exceed that silently.
$claudeArgs = @(
    "-p",
    "--model", $Model,
    "--permission-mode", "acceptEdits",
    "--output-format", "text"
)

"=== run $Stamp ($($prompt.Length) prompt chars) ===" | Tee-Object -FilePath $RunLog -Append

# No 2>&1, and ErrorActionPreference relaxed for the native call. 5.1 wraps a
# native exe's stderr in ErrorRecords, so one harmless warning would otherwise
# abort the whole run under -ErrorActionPreference Stop.
$prev = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$prompt | & claude @claudeArgs | Tee-Object -FilePath $RunLog -Append
$code = $LASTEXITCODE
$ErrorActionPreference = $prev

"=== exit $code ===" | Tee-Object -FilePath $RunLog -Append

# --- what to look at afterwards ------------------------------------------
$report = Join-Path $LogDir "SIM-$Today.md"
if (Test-Path $report) {
    "report: $report" | Tee-Object -FilePath $RunLog -Append
} else {
    "NO REPORT WRITTEN -- the agent skipped the one thing it owes." |
        Tee-Object -FilePath $RunLog -Append
}

# The author closes the request, never the agent. Say so in the run log too,
# so the instruction survives even if the report was never written.
"To close tonight's request, read the report and then run the answer-sim" |
    Tee-Object -FilePath $RunLog -Append
"command it prints. The agent is forbidden from running it." |
    Tee-Object -FilePath $RunLog -Append

exit $code
