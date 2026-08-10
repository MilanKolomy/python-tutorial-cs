$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    throw "Chybí .venv. Vytvořte je a nainstalujte requirements.txt."
}
& $python (Join-Path $PSScriptRoot "build_pdf.py") --all
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
