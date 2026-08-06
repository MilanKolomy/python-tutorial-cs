$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    throw "Chybí .venv. Vytvořte je a nainstalujte requirements.txt."
}

& $python -m sphinx -E -a -W --keep-going -b html `
    (Join-Path $projectRoot "source") `
    (Join-Path $projectRoot "outputs\html")

if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
