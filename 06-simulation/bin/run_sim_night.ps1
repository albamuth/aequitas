<#
    Nightly Aequitas simulation run. 04:00 local, on the author's machine.

    History: local task 2026-09-15 to 2026-10-13; a cloud Routine on
    2026-10-14 only; back to a local task from 2026-10-15 (author ruling:
    the cloud round trip through the public mirror cost more than it saved).

    The 03:00 outreach agent posts in public and does NOT run simulations
    (ruled 2026-08-25). This is the other half: it runs them and never posts.

    The guard here is NOT Claude's permission system. It is that the agent
    has nothing to publish with: no board key, no token, no git, and a brief
    that forbids writing outside 06-simulation\. Loosening the permission
    flag below cannot cause anything to become public. The commit and push
    at the end run AFTER the agent has exited, go to the PRIVATE repository
    only, and stage 06-simulation\ only.

    Permissions (author ruling 2026-10-16, PLAN-2026-10-16 5.1): the agent
    runs at the repository root, whose .claude\settings.json allows nothing,
    so until 2026-10-16 every python call it made was refused at 04:00 with
    nobody awake to approve it. Its allow and deny lists now live in
    bin\sim_agent_settings.json, in this folder, and are passed to the CLI
    with --settings. The root settings are untouched and an interactive
    session at the root is unaffected.

    Run by hand:  powershell -ExecutionPolicy Bypass -File bin\run_sim_night.ps1
    No agent:     ... -NoAgent      builds and checks the prompt, does not invoke Claude
    Preflight:    ... -WhatIfOnly   stops after the checks
#>

param(
    [switch]$WhatIfOnly,
    [switch]$NoAgent,      # everything except invoking Claude; leaves the exact
                           # prompt at log\tmp\prompt-<stamp>.md
    [string]$Model = "sonnet"   # author ruling 2026-10-16 (nightcheck 5.3 A). The 2026-10-15 move to Opus rested on the guess that Sonnet caused the python refusals; the Opus run of 2026-10-16 was refused the same way. The cause was the working folder (see bin\sim_agent_settings.json), so the cheaper model is back
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

# --- find the claude CLI -------------------------------------------------
# Resolved before the -NoAgent exit, so a dry run checks the CLI too. The
# packaged .exe is preferred over the npm shim, because on 2026-09-19 the shim
# was the part that went missing and the outreach run logged "exit 0" with no
# output. See 07-outreach\bin\run_night.ps1 for the full account.
$claudeCmd = $null
$packaged = Join-Path $env:APPDATA "npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe"
if (Test-Path $packaged) { $claudeCmd = $packaged }
if (-not $claudeCmd) {
    $claudeCmd = (Get-Command claude -ErrorAction SilentlyContinue |
                  Select-Object -First 1 -ExpandProperty Source)
}
if (-not $claudeCmd) {
    "FATAL: the claude CLI is not on PATH and the npm fallback is absent." | Tee-Object -FilePath $RunLog -Append
    "Repair: npm install -g @anthropic-ai/claude-code" | Tee-Object -FilePath $RunLog -Append
    exit 1
}
"claude CLI: $claudeCmd  (model $Model)" | Tee-Object -FilePath $RunLog -Append

if ($NoAgent) {
    "NoAgent: prompt built and checked, Claude NOT invoked." | Tee-Object -FilePath $RunLog -Append
    "Read the prompt the agent would have got: $PromptOut" | Tee-Object -FilePath $RunLog -Append
    exit 0
}

# --- the run -------------------------------------------------------------
# acceptEdits: file writes proceed without a prompt, so a 4am run does not
# stall on a dialog nobody is awake to answer. The boundary is the brief and
# the fact that this agent has no key, no token and nothing to publish with.
# The prompt goes in on STDIN, not as an argument: Windows caps a whole
# command line at 32,767 characters and a prompt can exceed that silently.
$SettingsFile = Join-Path $Root "bin\sim_agent_settings.json"
if (-not (Test-Path $SettingsFile)) {
    "FATAL: $SettingsFile is missing. Without it every python call is refused. Not invoking Claude." |
        Tee-Object -FilePath $RunLog -Append
    exit 1
}
"permissions: $SettingsFile" | Tee-Object -FilePath $RunLog -Append
$claudeArgs = @(
    "-p",
    "--model", $Model,
    "--permission-mode", "acceptEdits",
    "--settings", $SettingsFile,
    "--output-format", "text"
)

"=== run $Stamp ($($prompt.Length) prompt chars) ===" | Tee-Object -FilePath $RunLog -Append

# No 2>&1, and ErrorActionPreference relaxed for the native call. 5.1 wraps a
# native exe's stderr in ErrorRecords, so one harmless warning would otherwise
# abort the whole run under -ErrorActionPreference Stop. $code starts at a
# sentinel so a throw cannot leave a stale 0 behind.
$prev = $ErrorActionPreference
$ErrorActionPreference = "Continue"
$code = 99
try {
    $prompt | & $claudeCmd @claudeArgs | Tee-Object -FilePath $RunLog -Append
    $code = $LASTEXITCODE
} catch {
    "FATAL: invoking the claude CLI threw: $($_.Exception.Message)" | Tee-Object -FilePath $RunLog -Append
    $code = 98
}
$ErrorActionPreference = $prev

"=== exit $code ===" | Tee-Object -FilePath $RunLog -Append

# --- what to look at afterwards ------------------------------------------
$report = Join-Path $LogDir "SIM-$Today.md"
if (Test-Path $report) {
    "report: $report" | Tee-Object -FilePath $RunLog -Append
} elseif ($code -ne 0) {
    "NO REPORT WRITTEN -- the claude CLI exited $code before the agent ran. Read the line above '=== exit' for the reason (auth, session limit)." |
        Tee-Object -FilePath $RunLog -Append
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

# --- stamp every result the moment it exists ------------------------------
# Author ruling 2026-10-15 (nightcheck 5.4 A, from @coywolf c101111/c106315):
# a Delivered date set by the party it flatters is not a date. The launcher,
# not the agent and not the author, hashes tonight's report and every
# RESULTS.md written in the last 24 h into log\HASHES.txt. The commit below
# carries the line, and the outreach agent posts it on the board, whose own
# timestamp then fixes the date. memory.py hashes reads this file.
$HashFile = Join-Path $LogDir "HASHES.txt"
$since = (Get-Date).AddHours(-24)
$toStamp = @()
if (Test-Path $report) { $toStamp += Get-Item $report }
$toStamp += Get-ChildItem -Path $Root -Recurse -Filter "RESULTS.md" -File |
            Where-Object { $_.LastWriteTime -gt $since -and $_.FullName -notmatch "\\(log|archive|99-superseded)\\" }
            # The pattern above is a backslash, then one of three folder names, then a
            # backslash. On 2026-10-16 it read `"\(log|...)\\"`: a single `\(` is an
            # escaped literal paren, which left the `)` unmatched, .NET threw
            # "Too many )'s" under -ErrorActionPreference Stop, and the run died here
            # with no HASHES.txt and no git block.
foreach ($f in $toStamp) {
    $h   = (Get-FileHash -Algorithm SHA256 -Path $f.FullName).Hash.ToLower()
    $rel = ("06-simulation/" + $f.FullName.Substring($Root.Length + 1)) -replace "\\", "/"
    Add-Content -Path $HashFile -Encoding UTF8 -Value ("{0}`t{1}`t{2}" -f $Stamp, $h, $rel)
    "stamped $rel $($h.Substring(0,16))..." | Tee-Object -FilePath $RunLog -Append
}

# --- commit the night's work to the PRIVATE repo -------------------------
# Author ruling 2026-10-14, same as the outreach run (07-outreach\bin\run_night.ps1).
#   1. Only 06-simulation\ is staged, and log\tmp\ is git-ignored. The brief
#      forbids the agent writing anywhere else, and this block would not
#      carry it if it did.
#   2. This runs AFTER the agent has exited. The agent has no git and no
#      token. The token is read by bin\_git_push_token.ps1 from the project
#      root, exactly as sync_archive.ps1 does.
#   3. Push only if bin\consistency.py exits 0. Otherwise the commit stays
#      local and the run log says so. A git problem never changes the exit
#      code. The public mirror is never touched here; sync_archive.ps1
#      carries 06-simulation\ to it when the author next runs that.
$prev = $ErrorActionPreference
$ErrorActionPreference = "Continue"
"=== git ===" | Tee-Object -FilePath $RunLog -Append
$remote = (& git remote get-url origin)
if ($remote -notmatch "aequitas-foundations") {
    "git: origin is not aequitas-foundations ($remote). Not committing." | Tee-Object -FilePath $RunLog -Append
}
else {
    & git add -- 06-simulation 2>$null
    $staged = @(& git diff --cached --name-only)
    $outside = @($staged | Where-Object { $_ -notlike "06-simulation/*" })
    if ($outside.Count -gt 0) {
        # Cannot happen with the add above, but the check is cheap and the
        # consequence of a wrong path is publishing by accident.
        & git reset -q
        "git: refused -- staged paths outside 06-simulation/: $($outside -join ', ')" | Tee-Object -FilePath $RunLog -Append
    }
    elseif ($staged.Count -eq 0) {
        "git: nothing to commit under 06-simulation\." | Tee-Object -FilePath $RunLog -Append
    }
    else {
        & git commit -q -m "sim night ${Today}: run $Stamp ($($staged.Count) files)"
        if ($LASTEXITCODE -ne 0) {
            "git: commit FAILED. Files are staged, not committed." | Tee-Object -FilePath $RunLog -Append
        }
        else {
            "git: committed $(& git rev-parse --short HEAD) ($($staged.Count) files)." | Tee-Object -FilePath $RunLog -Append
            & python (Join-Path $RepoRoot "bin\consistency.py") > $null 2>&1
            if ($LASTEXITCODE -ne 0) {
                "git: NOT pushed. bin\consistency.py did not exit 0. Run it, fix, then bin\push_project.ps1." | Tee-Object -FilePath $RunLog -Append
            }
            else {
                $Pusher    = Join-Path $RepoRoot "bin\_git_push_token.ps1"
                $TokenFile = Join-Path $RepoRoot ".secrets\gh_token.txt"
                & powershell -NoProfile -ExecutionPolicy Bypass -File $Pusher -RepoDir $RepoRoot -TokenFile $TokenFile 2>&1 |
                    Tee-Object -FilePath $RunLog -Append
                if ($LASTEXITCODE -ne 0) { "git: push FAILED. The private repo is ahead of GitHub. Run bin\push_project.ps1." | Tee-Object -FilePath $RunLog -Append }
                else { "git: pushed to $remote." | Tee-Object -FilePath $RunLog -Append }
            }
        }
    }
}
$ErrorActionPreference = $prev

exit $code
