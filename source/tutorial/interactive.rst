.. _tut-interacting:

**************************************************
Interaktivní úpravy vstupu a nahrazování historie
**************************************************

Některé verze interpretu Pythonu podporují úpravy aktuálního vstupního řádku a
nahrazování z historie podobně jako shelly Korn a GNU Bash. Tato funkce je
implementována pomocí knihovny `GNU Readline`_, která podporuje různé způsoby
úprav. Knihovna má vlastní dokumentaci, kterou zde nebudeme opakovat.


.. _tut-keybindings:

Doplňování tabulátorem a úpravy historie
========================================

Doplňování názvů proměnných a modulů se při spuštění interpretu
:ref:`automaticky aktivuje <rlcompleter-config>`, takže klávesa :kbd:`Tab`
vyvolá funkci doplňování. Ta prohledává názvy příkazů Pythonu, aktuální lokální
proměnné a dostupné názvy modulů. U výrazů s tečkami, jako je ``string.a``,
vyhodnotí výraz až po poslední ``'.'`` a navrhne doplnění z atributů výsledného
objektu. Pokud je součástí výrazu objekt s metodou
:meth:`~object.__getattr__`, může se tím spustit kód definovaný aplikací.
Výchozí konfigurace také ukládá historii do souboru :file:`.python_history` v
uživatelském adresáři. Historie bude znovu dostupná při příštím interaktivním
sezení interpretu.


.. _tut-commentary:

Alternativy k interaktivnímu interpretu
===========================================

Tato funkce představuje oproti dřívějším verzím interpretu obrovský pokrok,
některá přání však zůstávají: bylo by vhodné navrhovat správné odsazení na
pokračovacích řádcích (syntaktický analyzátor ví, zda má následovat token
:data:`~token.INDENT`). Mechanismus doplňování by mohl používat tabulku symbolů
interpretu. Užitečný by byl také příkaz pro kontrolu, nebo dokonce navrhování,
odpovídajících závorek, uvozovek atd.

Jednou z dlouhodobě dostupných rozšířených alternativ interaktivního interpretu
je IPython_, který nabízí doplňování tabulátorem, procházení objektů a pokročilou
správu historie. Lze jej také důkladně přizpůsobit a vkládat do jiných aplikací.
Dalším podobným rozšířeným interaktivním prostředím je bpython_.


.. _GNU Readline: https://tiswww.case.edu/php/chet/readline/rltop.html
.. _IPython: https://ipython.org/
.. _bpython: https://bpython-interpreter.org/
