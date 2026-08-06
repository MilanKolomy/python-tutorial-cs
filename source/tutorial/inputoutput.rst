.. _tut-io:

****************
Vstup a výstup
****************

Výstup programu lze prezentovat několika způsoby. Data mohou být vypsána ve
formě čitelné pro člověka nebo zapsána do souboru pro pozdější použití. Tato
kapitola se zabývá některými z těchto možností.


.. _tut-formatting:

Pokročilejší formátování výstupu
================================

Dosud jsme se setkali se dvěma způsoby výpisu hodnot: *výrazovými příkazy* a
funkcí :func:`print`. (Třetím způsobem je použití metody
:meth:`~io.TextIOBase.write` souborových objektů; na soubor standardního výstupu
lze odkazovat jako na ``sys.stdout``. Další informace naleznete v referenční
příručce knihovny.)

Často budete chtít mít nad formátováním výstupu větší kontrolu než při pouhém
výpisu hodnot oddělených mezerami. Výstup lze formátovat několika způsoby.

* Chcete-li použít :ref:`formátované řetězcové literály <tut-f-strings>`, začněte
  řetězec znakem ``f`` nebo ``F`` před úvodní uvozovkou či trojicí uvozovek.
  Uvnitř řetězce můžete mezi znaky ``{`` a ``}`` zapsat výraz Pythonu, který
  může odkazovat na proměnné nebo literálové hodnoty.

  ::

     >>> year = 2016
     >>> event = 'Referendum'
     >>> f'Results of the {year} {event}'
     'Results of the 2016 Referendum'

* Metoda řetězců :meth:`str.format` vyžaduje více ruční práce. Znaky ``{`` a
  ``}`` nadále označují místo, kam bude dosazena proměnná, a umožňují zadat
  podrobné formátovací pokyny, musíte však také dodat formátované údaje.
  Následující blok kódu obsahuje dva příklady formátování proměnných:


  ::

     >>> yes_votes = 42_572_654
     >>> total_votes = 85_705_149
     >>> percentage = yes_votes / total_votes
     >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
     ' 42572654 YES votes  49.67%'

  Všimněte si, že hodnota ``yes_votes`` je doplněna mezerami a znaménko minus
  se zobrazí pouze u záporných čísel. Příklad také vypíše hodnotu ``percentage``
  vynásobenou 100, se dvěma desetinnými místy a následovanou znakem procenta
  (podrobnosti viz :ref:`formatspec`).


* Nakonec můžete veškeré zpracování řetězců provést sami pomocí vytváření
  výřezů a zřetězení a vytvořit libovolné rozvržení. Řetězcový typ nabízí také
  několik užitečných metod pro doplnění řetězců na danou šířku sloupce.

Pokud nepotřebujete propracovaný výstup, ale chcete pouze rychle zobrazit
některé proměnné při ladění, můžete libovolnou hodnotu převést na řetězec pomocí
funkcí :func:`repr` nebo :func:`str`.

Funkce :func:`str` má vracet reprezentace hodnot, které jsou poměrně dobře
čitelné pro člověka, zatímco :func:`repr` má vytvářet reprezentace čitelné
interpretem (nebo způsobit :exc:`SyntaxError`, pokud odpovídající syntaxe
neexistuje). U objektů bez zvláštní reprezentace určené pro člověka vrátí
:func:`str` stejnou hodnotu jako :func:`repr`. Mnoho hodnot, například čísla
nebo struktury jako seznamy a slovníky, má při použití obou funkcí stejnou
reprezentaci. Zejména řetězce mají dvě odlišné reprezentace.

Několik příkladů::

   >>> s = 'Hello, world.'
   >>> str(s)
   'Hello, world.'
   >>> repr(s)
   "'Hello, world.'"
   >>> str(1/7)
   '0.14285714285714285'
   >>> x = 10 * 3.25
   >>> y = 200 * 200
   >>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
   >>> print(s)
   The value of x is 32.5, and y is 40000...
   >>> # The repr() of a string adds string quotes and backslashes:
   >>> hello = 'hello, world\n'
   >>> hellos = repr(hello)
   >>> print(hellos)
   'hello, world\n'
   >>> # The argument to repr() may be any Python object:
   >>> repr((x, y, ('spam', 'eggs')))
   "(32.5, 40000, ('spam', 'eggs'))"

Modul :mod:`string` prostřednictvím třídy :class:`string.Template` podporuje
jednoduchý způsob vytváření šablon založený na regulárních výrazech. Nabízí tak
další způsob dosazování hodnot do řetězců, který používá zástupné symboly jako
``$x`` a nahrazuje je hodnotami ze slovníku. Tato syntaxe se snadno používá,
nabízí však podstatně menší kontrolu nad formátováním.

.. index::
   single: formatted string literal
   single: interpolated string literal
   single: string; formatted literal
   single: string; interpolated literal
   single: f-string
   single: fstring

.. _tut-f-strings:

Formátované řetězcové literály
-------------------------------

:ref:`Formátované řetězcové literály <f-strings>` (zkráceně také f-řetězce)
umožňují vložit hodnotu výrazů Pythonu do řetězce. Řetězci se přidá prefix ``f``
nebo ``F`` a výrazy se zapisují jako ``{expression}``.

Za výrazem může následovat nepovinný specifikátor formátu. Ten poskytuje větší
kontrolu nad způsobem formátování hodnoty. Následující příklad zaokrouhlí číslo
pí na tři desetinná místa::

   >>> import math
   >>> print(f'The value of pi is approximately {math.pi:.3f}.')
   The value of pi is approximately 3.142.

Celé číslo uvedené za ``':'`` určuje minimální šířku daného pole ve znacích.
To je užitečné pro zarovnání sloupců. ::

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
   >>> for name, phone in table.items():
   ...     print(f'{name:10} ==> {phone:10d}')
   ...
   Sjoerd     ==>       4127
   Jack       ==>       4098
   Dcab       ==>       7678

Jiné modifikátory lze použít k převodu hodnoty před jejím formátováním.
``'!a'`` použije :func:`ascii`, ``'!s'`` použije :func:`str` a ``'!r'`` použije
:func:`repr`::

   >>> animals = 'eels'
   >>> print(f'My hovercraft is full of {animals}.')
   My hovercraft is full of eels.
   >>> print(f'My hovercraft is full of {animals!r}.')
   My hovercraft is full of 'eels'.

Specifikátor ``=`` lze použít k rozvinutí výrazu na jeho text, znak rovnosti a
následně reprezentaci vyhodnoceného výrazu:

   >>> bugs = 'roaches'
   >>> count = 13
   >>> area = 'living room'
   >>> print(f'Debugging {bugs=} {count=} {area=}')
   Debugging bugs='roaches' count=13 area='living room'

Další informace o specifikátoru ``=`` naleznete v části
:ref:`samodokumentující výrazy <bpo-36817-whatsnew>`. Přehled těchto
formátovacích specifikací obsahuje referenční příručka :ref:`formatspec`.

.. _tut-string-format:

Řetězcová metoda format()
--------------------------

Základní použití metody :meth:`str.format` vypadá takto::

   >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
   We are the knights who say "Ni!"

Složené závorky a znaky v nich (nazývané formátovací pole) jsou nahrazeny
objekty předanými metodě :meth:`str.format`. Číslem v závorkách lze odkázat na
pozici objektu předaného metodě :meth:`str.format`. ::

   >>> print('{0} and {1}'.format('spam', 'eggs'))
   spam and eggs
   >>> print('{1} and {0}'.format('spam', 'eggs'))
   eggs and spam

Pokud metoda :meth:`str.format` používá argumenty klíčových slov, na jejich
hodnoty se odkazuje názvem argumentu. ::

   >>> print('This {food} is {adjective}.'.format(
   ...       food='spam', adjective='absolutely horrible'))
   This spam is absolutely horrible.

Poziční argumenty a argumenty klíčových slov lze libovolně kombinovat::

   >>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
   ...                                                    other='Georg'))
   The story of Bill, Manfred, and Georg.

Máte-li velmi dlouhý formátovací řetězec, který nechcete rozdělovat, je vhodné
odkazovat na formátované proměnné názvem namísto jejich pozice. Stačí předat
slovník a k přístupu ke klíčům použít hranaté závorky ``'[]'``. ::

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
   ...       'Dcab: {0[Dcab]:d}'.format(table))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

Totéž lze provést předáním slovníku ``table`` jako argumentů klíčových slov
pomocí zápisu ``**``. ::

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

To je zvláště užitečné v kombinaci s vestavěnou funkcí :func:`vars`, která vrací
slovník obsahující všechny lokální proměnné::

   >>> table = {k: str(v) for k, v in vars().items()}
   >>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
   >>> print(message.format(**table))
   __name__: __main__; __doc__: None; __package__: None; __loader__: ...

Následující řádky například vytvoří úhledně zarovnané sloupce celých čísel,
jejich druhých a třetích mocnin::

   >>> for x in range(1, 11):
   ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

Úplný přehled formátování řetězců pomocí :meth:`str.format` naleznete v části
:ref:`formatstrings`.


Ruční formátování řetězců
--------------------------

Zde je stejná tabulka druhých a třetích mocnin, tentokrát formátovaná ručně::

   >>> for x in range(1, 11):
   ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
   ...     # Note use of 'end' on previous line
   ...     print(repr(x*x*x).rjust(4))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

(Všimněte si, že jednu mezeru mezi jednotlivými sloupci přidala sama funkce
:func:`print`, která mezi své argumenty vždy vkládá mezery.)

Metoda řetězcových objektů :meth:`str.rjust` zarovná řetězec doprava v poli
zadané šířky tím, že jej zleva doplní mezerami. Podobně fungují metody
:meth:`str.ljust` a :meth:`str.center`. Tyto metody nic nevypisují, pouze vracejí
nový řetězec. Je-li vstupní řetězec příliš dlouhý, nezkrátí jej, ale vrátí beze
změny. Rozvržení sloupců se tím sice poruší, obvykle je to však lepší než
zkreslit hodnotu. (Pokud řetězec opravdu chcete zkrátit, můžete vždy přidat
vytvoření výřezu, například ``x.ljust(n)[:n]``.)

Další metoda :meth:`str.zfill` doplní číselný řetězec zleva nulami. Bere přitom
v úvahu znaménka plus a minus::

   >>> '12'.zfill(5)
   '00012'
   >>> '-3.14'.zfill(7)
   '-003.14'
   >>> '3.14159265359'.zfill(5)
   '3.14159265359'


Starý způsob formátování řetězců
--------------------------------

K formátování řetězců lze použít také operátor % (modulo). V zápisu
``format % values`` (kde *format* je řetězec) se převodní specifikace ``%`` v
řetězci *format* nahradí žádným, jedním nebo více prvky z *values*. Tato operace
se běžně označuje jako interpolace řetězců. Například::

   >>> import math
   >>> print('The value of pi is approximately %5.3f.' % math.pi)
   The value of pi is approximately 3.142.

Další informace naleznete v části :ref:`old-string-formatting`.


.. _tut-files:

Čtení a zápis souborů
=========================

.. index::
   pair: built-in function; open
   pair: object; file

:func:`open` vrací :term:`souborový objekt <file object>` a nejčastěji se
používá se dvěma pozičními argumenty a jedním argumentem klíčového slova:
``open(filename, mode, encoding=None)``

::

   >>> f = open('workfile', 'w', encoding="utf-8")

.. XXX str(f) is <io.TextIOWrapper object at 0x82e8dc4>

   >>> print(f)
   <open file 'workfile', mode 'w' at 80a0960>

První argument je řetězec obsahující název souboru. Druhý argument je další
řetězec s několika znaky popisujícími způsob použití souboru. *mode* může být
``'r'``, pokud se soubor bude pouze číst, ``'w'`` pro pouhý zápis (existující
soubor stejného názvu bude vymazán) a ``'a'`` otevře soubor pro přidávání;
všechna zapsaná data se automaticky připojí na konec. ``'r+'`` otevře soubor
pro čtení i zápis. Argument *mode* je nepovinný; pokud jej vynecháte,
předpokládá se ``'r'``.

Soubory se obvykle otevírají v :dfn:`textovém režimu <text mode>`. To znamená,
že se z nich čtou a zapisují se do nich řetězce kódované pomocí určitého
*kódování* (*encoding*). Není-li *encoding* uvedeno, výchozí hodnota závisí na
platformě (viz :func:`open`). Protože UTF-8 je moderním standardem de facto,
doporučuje se používat ``encoding="utf-8"``, pokud nevíte, že potřebujete jiné
kódování. Přidáním ``'b'`` k režimu se soubor otevře v :dfn:`binárním režimu
<binary mode>`. Data se v binárním režimu čtou a zapisují jako objekty
:class:`bytes`. Při otevření souboru v binárním režimu nelze *encoding* zadat.

Při čtení v textovém režimu se konce řádků specifické pro platformu (``\n`` v
Unixu, ``\r\n`` ve Windows) standardně převádějí na pouhé ``\n``. Při zápisu v
textovém režimu se výskyty ``\n`` standardně převádějí zpět na konce řádků
dané platformy. Tato skrytá úprava souborových dat je vhodná pro textové
soubory, poškodila by však binární data, například v souborech :file:`JPEG`
nebo :file:`EXE`. Při čtení a zápisu takových souborů proto vždy pečlivě
používejte binární režim.

Při práci se souborovými objekty je vhodné používat klíčové slovo
:keyword:`with`. Výhodou je, že se soubor po dokončení bloku správně zavře, i
když se v některém okamžiku vyvolá výjimka. Použití :keyword:`!with` je také
podstatně kratší než zápis odpovídajících bloků
:keyword:`try`\ -\ :keyword:`finally`::

    >>> with open('workfile', encoding="utf-8") as f:
    ...     read_data = f.read()

    >>> # We can check that the file has been automatically closed.
    >>> f.closed
    True

Pokud klíčové slovo :keyword:`with` nepoužíváte, měli byste voláním
``f.close()`` soubor zavřít a okamžitě uvolnit všechny systémové prostředky,
které využívá.

.. warning::
   Volání ``f.write()`` bez použití klíčového slova :keyword:`!with` nebo bez
   volání ``f.close()`` **může** způsobit, že argumenty funkce ``f.write()``
   nebudou zcela zapsány na disk, přestože program úspěšně skončí.

..
   See also https://bugs.python.org/issue17852

Po zavření souborového objektu, ať už příkazem :keyword:`with`, nebo voláním
``f.close()``, všechny pokusy o použití tohoto objektu automaticky selžou. ::

   >>> f.close()
   >>> f.read()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: I/O operation on closed file.


.. _tut-filemethods:

Metody souborových objektů
--------------------------

Ve zbývajících příkladech této části se předpokládá, že již byl vytvořen
souborový objekt s názvem ``f``.

Obsah souboru se čte voláním ``f.read(size)``, které načte určité množství dat
a vrátí je jako řetězec (v textovém režimu) nebo objekt typu :class:`bytes` (v binárním
režimu). *size* je nepovinný číselný argument. Pokud se *size* vynechá nebo je
záporné, načte a vrátí se celý obsah souboru; pokud je soubor dvakrát větší než
paměť počítače, je to váš problém. Jinak se načte a vrátí nejvýše *size* znaků
(v textovém režimu) nebo *size* bajtů (v binárním režimu). Po dosažení konce
souboru vrátí ``f.read()`` prázdný řetězec (``''``). ::

   >>> f.read()
   'This is the entire file.\n'
   >>> f.read()
   ''

``f.readline()`` načte ze souboru jeden řádek. Znak nového řádku (``\n``)
zůstává na konci řetězce a vynechá se pouze na posledním řádku souboru, pokud
soubor znakem nového řádku nekončí. Návratová hodnota je díky tomu jednoznačná:
vrátí-li ``f.readline()`` prázdný řetězec, bylo dosaženo konce souboru, zatímco
prázdný řádek je reprezentován řetězcem ``'\n'`` obsahujícím jediný znak nového
řádku. ::

   >>> f.readline()
   'This is the first line of the file.\n'
   >>> f.readline()
   'Second line of the file\n'
   >>> f.readline()
   ''

Při čtení řádků ze souboru lze procházet souborový objekt cyklem. Tento způsob
je paměťově úsporný, rychlý a vede k jednoduchému kódu::

   >>> for line in f:
   ...     print(line, end='')
   ...
   This is the first line of the file.
   Second line of the file

Chcete-li načíst všechny řádky souboru do seznamu, můžete také použít
``list(f)`` nebo ``f.readlines()``.

``f.write(string)`` zapíše obsah *string* do souboru a vrátí počet zapsaných
znaků. ::

   >>> f.write('This is a test\n')
   15

Objekty jiných typů je nutné před zápisem převést -- buď na řetězec (v textovém
režimu), nebo na objekt typu :class:`bytes` (v binárním režimu)::

   >>> value = ('the answer', 42)
   >>> s = str(value)  # convert the tuple to string
   >>> f.write(s)
   18

``f.tell()`` vrátí celé číslo udávající aktuální pozici souborového objektu v
souboru. V binárním režimu je vyjádřena jako počet bajtů od začátku souboru, v
textovém režimu jako abstraktní číslo.

Pozice souborového objektu se mění pomocí ``f.seek(offset, whence)``. Vypočítá
se přičtením *offset* k referenčnímu bodu, který určuje argument *whence*.
Hodnota *whence* 0 počítá od začátku souboru, 1 používá aktuální pozici v
souboru a 2 používá jako referenční bod konec souboru. *whence* lze vynechat;
výchozí hodnotou je 0, tedy referenční bod na začátku souboru. ::

   >>> f = open('workfile', 'rb+')
   >>> f.write(b'0123456789abcdef')
   16
   >>> f.seek(5)      # Go to the 6th byte in the file
   5
   >>> f.read(1)
   b'5'
   >>> f.seek(-3, 2)  # Go to the 3rd byte before the end
   13
   >>> f.read(1)
   b'd'

V textových souborech (otevřených bez ``b`` v řetězci režimu) jsou povoleny
pouze přesuny relativně k začátku souboru. Výjimkou je přesun přímo na konec
souboru pomocí ``seek(0, 2)``. Jedinými platnými hodnotami *offset* jsou hodnoty
vrácené funkcí ``f.tell()`` nebo nula. Jakákoli jiná hodnota *offset* vede k
nedefinovanému chování.

Souborové objekty mají několik dalších, méně často používaných metod, například
:meth:`~io.IOBase.isatty` a :meth:`~io.IOBase.truncate`. Úplného průvodce
souborovými objekty naleznete v referenční příručce knihovny.


.. _tut-json:

Ukládání strukturovaných dat pomocí :mod:`json`
------------------------------------------------

.. index:: pair: module; json

Řetězce lze snadno zapisovat do souboru a opět z něj číst. Čísla vyžadují o
něco více práce, protože metoda :meth:`~io.TextIOBase.read` vrací pouze řetězce.
Ty je třeba předat například funkci :func:`int`, která přijme řetězec jako
``'123'`` a vrátí jeho číselnou hodnotu 123. Chcete-li ukládat složitější datové
typy, například vnořené seznamy a slovníky, ruční analýza a serializace se
stávají komplikovanými.

Aby uživatelé nemuseli neustále psát a ladit kód pro ukládání složitých datových
typů do souborů, umožňuje Python použít oblíbený formát pro výměnu dat nazvaný
`JSON (JavaScript Object Notation) <https://json.org>`_. Standardní modul
:mod:`json` dokáže převést datové hierarchie Pythonu na řetězcové reprezentace;
tento proces se nazývá :dfn:`serializace <serializing>`. Obnovení dat z
řetězcové reprezentace se nazývá :dfn:`deserializace <deserializing>`. Mezi
serializací a deserializací může být řetězec reprezentující objekt uložen v
souboru či datech nebo odeslán síťovým spojením na vzdálený počítač.

.. note::
   Formát JSON moderní aplikace běžně používají k výměně dat. Mnoho programátorů
   jej již zná, a proto je dobrou volbou pro interoperabilitu.

Máte-li objekt ``x``, můžete jeho řetězcovou reprezentaci JSON zobrazit jediným
řádkem kódu::

   >>> import json
   >>> x = [1, 'simple', 'list']
   >>> json.dumps(x)
   '[1, "simple", "list"]'

Jiná varianta funkce :func:`~json.dumps`, nazvaná :func:`~json.dump`, jednoduše
serializuje objekt do :term:`textového souboru <text file>`. Je-li tedy ``f``
objekt :term:`textového souboru <text file>` otevřený pro zápis, můžeme provést
následující::

   json.dump(x, f)

Chceme-li objekt znovu dekódovat a ``f`` je objekt :term:`binárního souboru
<binary file>` nebo :term:`textového souboru <text file>` otevřený pro čtení::

   x = json.load(f)

.. note::
   Soubory JSON musí být kódovány v UTF-8. Při otevírání souboru JSON jako
   :term:`textového souboru <text file>` pro čtení i zápis použijte
   ``encoding="utf-8"``.

Tato jednoduchá serializační technika zvládá seznamy a slovníky, ale
serializace libovolných instancí tříd do JSON vyžaduje trochu práce navíc.
Vysvětlení obsahuje referenční dokumentace modulu :mod:`json`.

.. seealso::

   :mod:`pickle` - modul pickle

   Na rozdíl od :ref:`JSON <tut-json>` je *pickle* protokol umožňující
   serializaci libovolně složitých objektů Pythonu. Je proto specifický pro
   Python a nelze jej použít ke komunikaci s aplikacemi napsanými v jiných
   jazycích. Ve výchozím nastavení také není bezpečný: deserializace dat pickle
   z nedůvěryhodného zdroje může spustit libovolný kód, pokud data připravil
   zkušený útočník.
