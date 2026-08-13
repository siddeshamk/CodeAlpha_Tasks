Write-Host "=============================================="
Write-Host "   NETSENTINEL SECURITY SCAN"
Write-Host "=============================================="

$Root = Split-Path -Parent $PSScriptRoot
$Output = Join-Path $PSScriptRoot "..\results\security_scan.txt"

Write-Host ""
Write-Host "Running Bandit..."
Write-Host ""

py -m bandit `
    -r "$Root\..\core" "$Root\..\main.py" "$Root\..\config.py" `
    -f txt `
    -o $Output

Write-Host ""
Write-Host "=============================================="
Write-Host "Scan complete."
Write-Host "Report:"
Write-Host $Output
Write-Host "=============================================="