<#
    Register (or re-register) the nightly simulation run as a Windows
    Scheduled Task.

    04:00, one hour after the 1F916 outreach run at 03:00, whose own limit is
    one hour. The two never overlap.

    Runs as the current user, interactive logon, so NO PASSWORD is needed or
    stored. The task only fires while that user is logged on.

    Settings chosen on purpose, and copied from the outreach task because they
    were earned there:
      -StartWhenAvailable       a missed run (machine asleep) fires on wake
      -WakeToRun                try to wake the machine for it
      -DontStopIfGoingOnBatteries / -AllowStartIfOnBatteries   laptop-safe
      -ExecutionTimeLimit 1h    a hung night cannot run into the morning
      -MultipleInstances IgnoreNew   never two agents on one repo

    Install:     powershell -ExecutionPolicy Bypass -File bin\install_sim_task.ps1
    Change time: ... -File bin\install_sim_task.ps1 -At 05:00
    Remove:      ... -File bin\install_sim_task.ps1 -Remove
#>

param(
    [string]$TaskName = "Aequitas simulation nightly",
    [string]$At       = "04:00",
    [switch]$Remove
)

$ErrorActionPreference = "Stop"

$Root   = Split-Path -Parent $PSScriptRoot          # 06-simulation\
$Runner = Join-Path $Root "bin\run_sim_night.ps1"

if ($Remove) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    "removed: $TaskName"
    exit 0
}

if (-not (Test-Path $Runner)) { throw "runner not found: $Runner" }

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Runner`"" `
    -WorkingDirectory $Root

$trigger = New-ScheduledTaskTrigger -Daily -At $At

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -WakeToRun `
    -DontStopIfGoingOnBatteries `
    -AllowStartIfOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -MultipleInstances IgnoreNew

# Interactive logon: no credential is asked for and none is stored.
$principal = New-ScheduledTaskPrincipal `
    -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) `
    -LogonType Interactive `
    -RunLevel Limited

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Nightly Aequitas simulation run. One request a night, oldest first unless 06-simulation\PINNED_SIM.txt names one. Writes only inside 06-simulation\. Publishes nothing and closes no request -- the author runs answer-sim after reading the report." `
    -Force | Out-Null

"registered: $TaskName  daily at $At"
"runner    : $Runner"
""
"verify with:  Get-ScheduledTask -TaskName '$TaskName' | Get-ScheduledTaskInfo"
"run it now :  Start-ScheduledTask -TaskName '$TaskName'"
"dry check  :  powershell -ExecutionPolicy Bypass -File `"$Runner`" -NoAgent"
