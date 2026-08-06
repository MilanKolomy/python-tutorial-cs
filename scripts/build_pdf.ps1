$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
    throw "Chybí .venv. Vytvořte je a nainstalujte requirements.txt."
}
$latexDir = Join-Path $projectRoot "work\latex"
$pdfDir = Join-Path $projectRoot "outputs\pdf"

New-Item -ItemType Directory -Force -Path $latexDir, $pdfDir | Out-Null

& $python -m sphinx -b latex (Join-Path $projectRoot "source") $latexDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Push-Location $latexDir
try {
    & latexmk -lualatex -interaction=nonstopmode -halt-on-error "python-tutorial-cs.tex"
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
} finally {
    Pop-Location
}

Copy-Item (Join-Path $latexDir "python-tutorial-cs.pdf") `
    (Join-Path $projectRoot "outputs\pdf\python-tutorial-cs.pdf") -Force
