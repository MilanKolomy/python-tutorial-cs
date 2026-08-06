.. _tut-using:

****************************
Používání interpretu Pythonu
****************************


.. _tut-invoking:

Spuštění interpretu
===================

Interpret Pythonu se na počítačích, pro které je dostupný, obvykle instaluje
jako |usr_local_bin_python_x_dot_y_literal|. Přidáte-li :file:`/usr/local/bin`
do vyhledávací cesty unixového shellu, můžete jej spustit zadáním příkazu:

.. code-block:: text

   python3.14

do shellu. [#]_ Volba adresáře, ve kterém se interpret nachází, je součástí
instalace, takže jsou možná i jiná umístění; poraďte se s místním znalcem
Pythonu nebo správcem systému. (Oblíbeným alternativním umístěním je například
:file:`/usr/local/python`.)

Na počítačích se systémem Windows, kde jste Python nainstalovali z obchodu
:ref:`Microsoft Store <windows-store>`, bude dostupný příkaz
|python_x_dot_y_literal|. Máte-li nainstalovaný :ref:`spouštěč py.exe
<launcher>`, můžete použít příkaz :file:`py`. Další způsoby spuštění Pythonu
najdete v části :ref:`setting-envvars`.

Zadání znaku konce souboru (:kbd:`Control-D` v Unixu, :kbd:`Control-Z` ve
Windows) na primární výzvě způsobí ukončení interpretu s nulovým návratovým
kódem. Pokud to nefunguje, můžete interpret ukončit zadáním následujícího
příkazu: ``quit()``.

Funkce interpretu pro úpravu řádku zahrnují na většině systémů interaktivní
úpravy, vyvolávání příkazů z historie a automatické doplňování kódu.
Podporu úprav příkazového řádku lze nejrychleji ověřit tak, že na výzvě Pythonu
napíšete slovo a potom stisknete šipku doleva (nebo :kbd:`Control-b`).
Pokud se kurzor pohne, jsou úpravy příkazového řádku dostupné; úvod k ovládacím
klávesám najdete v dodatku :ref:`tut-interacting`.
Pokud se zdánlivě nic nestane nebo se objeví posloupnost jako ``^[[D`` či
``^B``, úpravy příkazového řádku nejsou dostupné; znaky na aktuálním řádku
budete moci odstraňovat pouze klávesou Backspace.

Interpret pracuje do jisté míry podobně jako unixový shell: je-li spuštěn se
standardním vstupem připojeným k zařízení tty, čte a provádí příkazy
interaktivně; je-li spuštěn s názvem souboru jako argumentem nebo se souborem
jako standardním vstupem, přečte a provede z tohoto souboru *skript*.

Druhým způsobem spuštění interpretu je ``python -c command [arg] ...``, který
provede příkaz či příkazy v *command*, obdobně jako volba shellu :option:`-c`.
Protože příkazy Pythonu často obsahují mezery nebo jiné znaky, které mají pro
shell zvláštní význam, obvykle se doporučuje uzavřít celý *command* do uvozovek.

Některé moduly Pythonu lze rovněž užitečně používat jako skripty. Lze je spustit
pomocí ``python -m module [arg] ...``, což provede zdrojový soubor modulu
*module*, jako byste na příkazovém řádku uvedli jeho úplný název.

Při použití souboru se skriptem je někdy užitečné skript spustit a poté přejít
do interaktivního režimu. To lze provést předáním volby :option:`-i` před
skriptem.

Všechny volby příkazového řádku popisuje část :ref:`using-on-general`.


.. _tut-argpassing:

Předávání argumentů
-------------------

Když má interpret k dispozici název skriptu a za ním další argumenty, převede
je na seznam řetězců a přiřadí jej proměnné ``argv`` v modulu ``sys``. K tomuto
seznamu můžete přistoupit provedením ``import sys``. Seznam obsahuje alespoň
jednu položku; pokud není zadán skript ani žádné argumenty, je ``sys.argv[0]``
prázdný řetězec. Je-li jako název skriptu zadáno ``'-'`` (což znamená standardní
vstup), nastaví se ``sys.argv[0]`` na ``'-'``. Při použití :option:`-c`
*command* se ``sys.argv[0]`` nastaví na ``'-c'``. Při použití :option:`-m`
*module* se ``sys.argv[0]`` nastaví na úplný název nalezeného modulu. Volby
uvedené za :option:`-c` *command* nebo :option:`-m` *module* zpracování voleb
interpretem Pythonu nespotřebuje, ale ponechá je v ``sys.argv`` ke zpracování
příkazem nebo modulem.


.. _tut-interactive:

Interaktivní režim
------------------

Když se příkazy čtou ze zařízení tty, říká se, že je interpret v *interaktivním
režimu*. V tomto režimu si další příkaz vyžádá *primární výzvou*, obvykle třemi
znaménky větší než (``>>>``); pokračovací řádky si vyžádá *sekundární výzvou*,
kterou ve výchozím nastavení tvoří tři tečky (``...``). Před zobrazením první
výzvy interpret vypíše uvítací zprávu s číslem verze a oznámením o autorských
právech:

.. code-block:: shell-session

   $ python3.14
   Python 3.14 (default, April 4 2024, 09:25:04)
   [GCC 10.2.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

.. XXX update for new releases

Při zadávání víceřádkové konstrukce jsou zapotřebí pokračovací řádky. Jako
příklad si prohlédněte tento příkaz :keyword:`if`::

   >>> the_world_is_flat = True
   >>> if the_world_is_flat:
   ...     print("Be careful not to fall off!")
   ...
   Be careful not to fall off!


Více informací o interaktivním režimu najdete v části :ref:`tut-interac`.


.. _tut-interp:

Interpret a jeho prostředí
==========================


.. _tut-source-encoding:

Kódování zdrojového kódu
------------------------

Ve výchozím nastavení se zdrojové soubory Pythonu považují za soubory
v kódování UTF-8. V tomto kódování lze v řetězcových literálech, identifikátorech
a komentářích současně používat znaky většiny světových jazyků --- standardní
knihovna však v identifikátorech používá pouze znaky ASCII, což je konvence,
kterou by měl dodržovat každý přenositelný kód. Aby editor všechny tyto znaky
zobrazil správně, musí rozpoznat, že soubor používá UTF-8, a použít písmo, které
podporuje všechny znaky v souboru.

Chcete-li deklarovat jiné než výchozí kódování, přidejte na *první* řádek
souboru speciální komentář. Jeho syntaxe je následující::

   # -*- coding: encoding -*-

kde *encoding* označuje jedno z platných kódování podporovaných Pythonem
prostřednictvím modulu :mod:`codecs`.

Chcete-li například deklarovat použití kódování Windows-1252, měl by první
řádek souboru se zdrojovým kódem vypadat takto::

   # -*- coding: cp1252 -*-

Výjimkou z pravidla *prvního řádku* je zdrojový kód začínající
:ref:`unixovým řádkem „shebang“ <tut-scripts>`. V takovém případě se deklarace
kódování přidává na druhý řádek souboru. Například::

   #!/usr/bin/env python3
   # -*- coding: cp1252 -*-

.. rubric:: Poznámky pod čarou

.. [#] V Unixu se interpret Pythonu 3.x ve výchozím nastavení neinstaluje se
   spustitelným souborem pojmenovaným ``python``, aby nedošlo ke konfliktu se
   současně nainstalovaným spustitelným souborem Pythonu 2.x.
