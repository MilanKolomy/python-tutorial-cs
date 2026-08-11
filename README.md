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
.\.venv\Scripts\python.exe .\scripts\check_functions_source.py
.\.venv\Scripts\python.exe .\scripts\check_glossary_source.py
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build_html.ps1
```

Výsledné stránky jsou v `outputs/html/index.html`.

Kontrola vestavěných funkcí porovnává bloky kódu, inline kód, signatury,
direktivy, cíle odkazů, štítky a URL s přesným zdrojem CPythonu 3.14.6.
Kontrola slovníku navíc ověřuje zachování anglických názvů hesel a indexových
direktiv, aby odkazy z tutorialu zůstaly stabilní.

Externí odkazy do ostatních částí dokumentace Pythonu řeší rozšíření
`sphinx.ext.intersphinx`. Projekt používá lokální kopii oficiálního inventáře
Pythonu 3.14.6 v `source/_intersphinx/python-3.14.6.inv`, takže běžné sestavení
HTML nevyžaduje připojení k internetu. Při přechodu na jinou verzi Pythonu je
nutné aktualizovat inventář i položku `intersphinx_mapping` v `source/conf.py`.

## GitHub Actions a GitHub Pages

Workflow `.github/workflows/pages.yml` při každém pushi do větve `main` stáhne
přesný referenční commit CPythonu, zkontroluje bloky kódu, vestavěné funkce i
slovník pojmů, sestaví HTML bez varování a publikuje výsledek přes GitHub Pages.
U pull requestů provede pouze kontrolu a sestavení bez publikace. Workflow lze
spustit také ručně na kartě Actions.

## Sestavení PDF

PDF se vytváří ze stejných RST souborů jako HTML. Je potřeba:

- projektové prostředí `.venv` se Sphinxem 8.2.3;
- distribuce TeXu s příkazy `lualatex` a `makeindex` v systémové proměnné `PATH`.

Ve Windows je vhodný [MiKTeX](https://miktex.org/download) nebo
[TeX Live](https://tug.org/texlive/windows.html). Při instalaci MiKTeXu povolte
automatickou instalaci chybějících balíčků. Po instalaci otevřete nový PowerShell
a ověřte příkazy `lualatex --version` a `makeindex --version`.

Dostupné kapitoly vypíšete příkazem:

```powershell
.\.venv\Scripts\python.exe .\scripts\build_pdf.py --list
```

Celý tutorial sestavíte takto:

```powershell
.\.venv\Scripts\python.exe .\scripts\build_pdf.py --all
```

Jednu nebo více kapitol lze vybrat opakováním volby `--chapter`:

```powershell
.\.venv\Scripts\python.exe .\scripts\build_pdf.py --chapter introduction
.\.venv\Scripts\python.exe .\scripts\build_pdf.py --chapter introduction --chapter controlflow
```

Celý tutorial se uloží jako `outputs/pdf/python-tutorial-cs-3.14.6.pdf`.
Jedna kapitola dostane číslo a bezpečný název, například
`outputs/pdf/03-neformalni-uvod-do-pythonu.pdf`. Výběr více kapitol používá název
například `outputs/pdf/python-tutorial-cs-kapitoly-03-04.pdf`.

Při každém spuštění skript znovu vytvoří pouze svůj pracovní adresář `work/pdf/`.
Zdrojové RST soubory, `upstream-cpython/`, HTML výstup ani jiná část `work/` se
nemění. Hotové PDF v `outputs/pdf/` se nahradí až po úspěšném sestavení.

Pokud skript hlásí chybějící Sphinx, spusťte jej Pythonem z `.venv` a znovu
nainstalujte `requirements.txt`. Při chybějícím `lualatex` nebo `makeindex`
dokončete instalaci TeXu a otevřete nový terminál. Podrobnosti o případné chybě
LuaLaTeXu zůstávají v `work/pdf/latex/python-tutorial-cs.log`.

Původní PowerShell příkaz pro celý tutorial zůstává dostupný jako zkratka:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\build_pdf.ps1
```

Původní dokumentace a ukázkový kód jsou copyright © Python Software Foundation
a podléhají licenci PSF. Jde o neoficiální český překlad pro osobní studijní
účely.
