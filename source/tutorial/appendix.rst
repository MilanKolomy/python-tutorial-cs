.. _tut-appendix:

********
Dodatek
********


.. _tut-interac:

Interaktivní režim
==================

Interaktivní :term:`REPL` má dvě varianty. Klasický základní interpret je
podporován na všech platformách a nabízí minimální možnosti ovládání řádku.

Od Pythonu 3.13 se ve výchozím nastavení používá nový interaktivní shell. Ten
podporuje barvy, úpravy více řádků, procházení historie a režim vkládání.
Podrobnosti o vypnutí barev naleznete v části
:ref:`using-on-controlling-color`. Další funkce poskytují funkční klávesy.
:kbd:`F1` otevře interaktivní prohlížeč nápovědy :mod:`pydoc`. :kbd:`F2` umožní
procházet historii příkazového řádku bez výstupu a bez výzev :term:`>>>` a
:term:`...`. :kbd:`F3` aktivuje „režim vkládání“, který usnadňuje vložení
větších bloků kódu. Dalším stisknutím :kbd:`F3` se vrátíte k běžné výzvě.

Nový interaktivní shell ukončíte zadáním :kbd:`exit` nebo :kbd:`quit`. Za tyto
příkazy není nutné přidávat závorky volání.

Pokud nový interaktivní shell nechcete používat, lze jej vypnout proměnnou
prostředí :envvar:`PYTHON_BASIC_REPL`.

.. _tut-error:

Obsluha chyb
--------------

Když nastane chyba, interpret vypíše chybové hlášení a výpis zásobníku volání.
V interaktivním režimu se poté vrátí k primární výzvě; pokud vstup pocházel ze
souboru, po vypsání zásobníku skončí s nenulovým návratovým stavem. (Výjimky
obsloužené klauzulí :keyword:`except` v příkazu :keyword:`try` se v tomto
kontextu za chyby nepovažují.) Některé chyby jsou bezpodmínečně fatální a
způsobí ukončení s nenulovým stavem. To platí pro vnitřní nekonzistence a
některé případy vyčerpání paměti. Všechna chybová hlášení se zapisují do
standardního chybového proudu; běžný výstup provedených příkazů se zapisuje na
standardní výstup.

Zadání znaku přerušení (obvykle :kbd:`Control-C` nebo :kbd:`Delete`) při
primární či sekundární výzvě zruší vstup a vrátí se k primární výzvě. [#]_
Přerušení zadané během provádění příkazu vyvolá výjimku
:exc:`KeyboardInterrupt`, kterou lze obsloužit příkazem :keyword:`try`.


.. _tut-scripts:

Spustitelné skripty Pythonu
---------------------------

Na unixových systémech odvozených od BSD lze skripty Pythonu učinit přímo
spustitelnými podobně jako shellové skripty vložením řádku::

   #!/usr/bin/env python3

na začátek skriptu (za předpokladu, že je interpret v uživatelově
:envvar:`PATH`) a nastavením souboru jako spustitelného. ``#!`` musí být prvními
dvěma znaky souboru. Na některých platformách musí tento první řádek končit
unixovým zakončením řádku (``'\n'``), nikoli zakončením Windows (``'\r\n'``).
Znak mřížky ``'#'`` se v Pythonu používá k zahájení komentáře.

Skriptu lze nastavit spustitelný režim neboli oprávnění příkazem
:program:`chmod`.

.. code-block:: shell-session

   $ chmod +x myscript.py

V systémech Windows pojem „spustitelný režim“ neexistuje. Instalátor Pythonu
automaticky přidruží soubory ``.py`` k ``python.exe``, takže se soubor Pythonu
po dvojitém kliknutí spustí jako skript. Přípona může být také ``.pyw``; v tom
případě se běžně zobrazované okno konzole potlačí.


.. _tut-startup:

Spouštěcí soubor interaktivního režimu
--------------------------------------

Při interaktivním používání Pythonu se často hodí provést při každém spuštění
interpretu několik standardních příkazů. Stačí nastavit proměnnou prostředí
:envvar:`PYTHONSTARTUP` na název souboru obsahujícího spouštěcí příkazy. Podobá
se to souboru :file:`.profile` unixových shellů.

Tento soubor se načítá pouze v interaktivních sezeních, nikoli když Python čte
příkazy ze skriptu ani když je jako explicitní zdroj příkazů zadáno
:file:`/dev/tty` (které se jinak chová jako interaktivní sezení). Provádí se ve
stejném jmenném prostoru jako interaktivní příkazy, takže objekty, které definuje
nebo importuje, lze v interaktivním sezení používat bez kvalifikace. V tomto
souboru můžete také změnit výzvy ``sys.ps1`` a ``sys.ps2``.

Chcete-li načíst další spouštěcí soubor z aktuálního adresáře, můžete to
naprogramovat v globálním spouštěcím souboru pomocí kódu jako ``if
os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())``. Chcete-li
spouštěcí soubor použít ve skriptu, musíte to ve skriptu provést explicitně::

   import os
   filename = os.environ.get('PYTHONSTARTUP')
   if filename and os.path.isfile(filename):
       with open(filename) as fobj:
           startup_file = fobj.read()
       exec(startup_file)


.. _tut-customize:

Moduly pro přizpůsobení
-------------------------

Python poskytuje dva háčky pro přizpůsobení: :index:`sitecustomize` a
:index:`usercustomize`. Nejprve musíte zjistit umístění svého uživatelského
adresáře site-packages. Spusťte Python a proveďte tento kód::

   >>> import site
   >>> site.getusersitepackages()
   '/home/user/.local/lib/python3.x/site-packages'

Nyní můžete v tomto adresáři vytvořit soubor :file:`usercustomize.py` a vložit
do něj libovolný obsah. Ovlivní každé spuštění Pythonu, pokud není použitím volby
:option:`-s` zakázán automatický import.

:index:`sitecustomize` funguje stejně, ale obvykle jej vytváří správce počítače
v globálním adresáři site-packages a importuje se před :index:`usercustomize`.
Další podrobnosti naleznete v dokumentaci modulu :mod:`site`.


.. rubric:: Poznámky pod čarou

.. [#] Může tomu zabránit problém s balíčkem GNU Readline.
