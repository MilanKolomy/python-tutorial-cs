# Neoficiální český překlad tutorialu Pythonu 3.14.6

Zdrojové dokumenty jsou v `source/`, původní neupravené soubory v
`upstream-cpython/Doc/tutorial/`. Adresář `upstream-cpython/` je pouze referenční
a nesmí se upravovat.

## Příprava prostředí

V PowerShellu z kořene projektu:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Kontrola a sestavení HTML

```powershell
.\.venv\Scripts\python.exe .\scripts\check_code_blocks.py
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build_html.ps1
```

Výsledné stránky jsou v `outputs/html/index.html`.

Externí odkazy do ostatních částí dokumentace Pythonu řeší rozšíření
`sphinx.ext.intersphinx`. Projekt používá lokální kopii oficiálního inventáře
Pythonu 3.14.6 v `source/_intersphinx/python-3.14.6.inv`, takže běžné sestavení
HTML nevyžaduje připojení k internetu. Při přechodu na jinou verzi Pythonu je
nutné aktualizovat inventář i položku `intersphinx_mapping` v `source/conf.py`.

## Sestavení PDF

PDF vyžaduje distribuci TeXu s příkazy `lualatex` a `latexmk`:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build_pdf.ps1
```

Sphinx vytvoří dočasné soubory v `work/latex/`; hotové PDF skript uloží jako
`outputs/pdf/python-tutorial-cs.pdf`.

Původní dokumentace a ukázkový kód jsou copyright © Python Software Foundation
a podléhají licenci PSF. Jde o neoficiální český překlad pro osobní studijní
účely.
