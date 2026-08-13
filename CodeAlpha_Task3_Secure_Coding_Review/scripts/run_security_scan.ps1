Write-Host "=============================================="
Write-Host "   NETSENTINEL SECURITY SCAN"
Write-Host "=============================================="

$RepoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

$Task1 = Join-Path $RepoRoot "CodeAlpha_Task1_Basic_Network_Sniffer"

$Output = Join-Path $PSScriptRoot "..\results\security_scan.txt"

Write-Host ""
Write-Host "Scanning Task 1 source code..."
Write-Host ""

py -m bandit `
    -r "$Task1\core" "$Task1\main.py" "$Task1\config.py" `
    -f txt `
    -o $Output

Write-Host ""
Write-Host "=============================================="
Write-Host "Scan complete."
Write-Host "Report:"
Write-Host $Output
Write-Host "=============================================="