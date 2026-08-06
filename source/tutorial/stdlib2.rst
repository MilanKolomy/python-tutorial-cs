.. _tut-brieftourtwo:

**************************************************
Stručná prohlídka standardní knihovny --- část II
**************************************************

Tato druhá prohlídka se věnuje pokročilejším modulům, které podporují potřeby
profesionálního programování. V malých skriptech se tyto moduly objevují zřídka.


.. _tut-output-formatting:

Formátování výstupu
===================

Modul :mod:`reprlib` poskytuje variantu funkce :func:`repr` přizpůsobenou pro
zkrácené zobrazení velkých nebo hluboce vnořených kontejnerů::

   >>> import reprlib
   >>> reprlib.repr(set('supercalifragilisticexpialidocious'))
   "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

Modul :mod:`pprint` nabízí propracovanější kontrolu nad výpisem vestavěných i
uživatelsky definovaných objektů ve formě čitelné interpretem. Pokud je výsledek
delší než jeden řádek, „úhledný výpis“ přidá zalomení řádků a odsazení, aby byla
struktura dat zřetelnější::

   >>> import pprint
   >>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
   ...     'yellow'], 'blue']]]
   ...
   >>> pprint.pprint(t, width=30)
   [[[['black', 'cyan'],
      'white',
      ['green', 'red']],
     [['magenta', 'yellow'],
      'blue']]]

Modul :mod:`textwrap` formátuje odstavce textu tak, aby se vešly do zadané šířky
obrazovky::

   >>> import textwrap
   >>> doc = """The wrap() method is just like fill() except that it returns
   ... a list of strings instead of one big string with newlines to separate
   ... the wrapped lines."""
   ...
   >>> print(textwrap.fill(doc, width=40))
   The wrap() method is just like fill()
   except that it returns a list of strings
   instead of one big string with newlines
   to separate the wrapped lines.

Modul :mod:`locale` zpřístupňuje databázi formátů dat specifických pro jednotlivé
kultury. Atribut grouping formátovací funkce tohoto modulu umožňuje přímo
formátovat čísla s oddělovači skupin číslic::

   >>> import locale
   >>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
   'English_United States.1252'
   >>> conv = locale.localeconv()          # get a mapping of conventions
   >>> x = 1234567.8
   >>> locale.format_string("%d", x, grouping=True)
   '1,234,567'
   >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
   ...                      conv['frac_digits'], x), grouping=True)
   '$1,234,567.80'


.. _tut-templating:

Používání šablon
================

Modul :mod:`string` obsahuje všestrannou třídu :class:`~string.Template` se
zjednodušenou syntaxí vhodnou pro úpravy koncovými uživateli. Uživatelé tak
mohou aplikaci přizpůsobit, aniž by museli měnit její kód.

Formát používá názvy zástupných symbolů tvořené znakem ``$`` a platným
identifikátorem Pythonu (alfanumerickými znaky a podtržítky). Uzavření zástupného
symbolu do složených závorek umožňuje, aby za ním bez mezery následovaly další
alfanumerické znaky. Zápis ``$$`` vytvoří jeden escapovaný znak ``$``::

   >>> from string import Template
   >>> t = Template('${village}folk send $$10 to $cause.')
   >>> t.substitute(village='Nottingham', cause='the ditch fund')
   'Nottinghamfolk send $10 to the ditch fund.'

Metoda :meth:`~string.Template.substitute` vyvolá :exc:`KeyError`, pokud
zástupný symbol nebyl dodán ve slovníku ani jako argument klíčového slova. V
aplikacích podobných hromadné korespondenci mohou být uživatelská data neúplná,
a proto může být vhodnější metoda :meth:`~string.Template.safe_substitute` ---
při chybějících datech ponechá zástupné symboly beze změny::

   >>> t = Template('Return the $item to $owner.')
   >>> d = dict(item='unladen swallow')
   >>> t.substitute(d)
   Traceback (most recent call last):
     ...
   KeyError: 'owner'
   >>> t.safe_substitute(d)
   'Return the unladen swallow to $owner.'

Podtřídy třídy Template mohou určit vlastní oddělovač. Nástroj pro dávkové
přejmenování v prohlížeči fotografií může například používat znak procenta pro
zástupné symboly aktuálního data, pořadového čísla obrázku nebo formátu souboru::

   >>> import time, os.path
   >>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
   >>> class BatchRename(Template):
   ...     delimiter = '%'
   ...
   >>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
   Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

   >>> t = BatchRename(fmt)
   >>> date = time.strftime('%d%b%y')
   >>> for i, filename in enumerate(photofiles):
   ...     base, ext = os.path.splitext(filename)
   ...     newname = t.substitute(d=date, n=i, f=ext)
   ...     print('{0} --> {1}'.format(filename, newname))

   img_1074.jpg --> Ashley_0.jpg
   img_1076.jpg --> Ashley_1.jpg
   img_1077.jpg --> Ashley_2.jpg

Dalším využitím šablon je oddělení logiky programu od podrobností různých
výstupních formátů. Díky tomu lze dosazovat vlastní šablony pro soubory XML,
prosté textové sestavy a webové sestavy HTML.


.. _tut-binary-formats:

Práce s rozvržením záznamů binárních dat
========================================

Modul :mod:`struct` poskytuje funkce :func:`~struct.pack` a
:func:`~struct.unpack` pro práci s formáty binárních záznamů proměnné délky.
Následující příklad ukazuje, jak procházet informace v hlavičkách souboru ZIP
bez použití modulu :mod:`zipfile`. Kódy balení ``"H"`` a ``"I"`` představují
dvoubajtová, respektive čtyřbajtová celá čísla bez znaménka. Znak ``"<"``
označuje standardní velikost a pořadí bajtů od nejméně významného
(little-endian)::

   import struct

   with open('myfile.zip', 'rb') as f:
       data = f.read()

   start = 0
   for i in range(3):                      # show the first 3 file headers
       start += 14
       fields = struct.unpack('<IIIHH', data[start:start+16])
       crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

       start += 16
       filename = data[start:start+filenamesize]
       start += filenamesize
       extra = data[start:start+extra_size]
       print(filename, hex(crc32), comp_size, uncomp_size)

       start += extra_size + comp_size     # skip to the next header


.. _tut-multi-threading:

Vícevláknové zpracování
=======================

Vlákna jsou technikou pro oddělení úloh, které na sobě sekvenčně nezávisí. Lze
jimi zlepšit odezvu aplikací, které přijímají vstup uživatele, zatímco jiné
úlohy běží na pozadí. Souvisejícím použitím je souběžné provádění vstupně-
výstupních operací a výpočtů v jiném vlákně.

Následující kód ukazuje, jak může vysokoúrovňový modul :mod:`threading` spouštět
úlohy na pozadí, zatímco hlavní program pokračuje v běhu::

   import threading, zipfile

   class AsyncZip(threading.Thread):
       def __init__(self, infile, outfile):
           super().__init__()
           self.infile = infile
           self.outfile = outfile

       def run(self):
           with zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED) as f:
               f.write(self.infile)
           print('Finished background zip of:', self.infile)

   background = AsyncZip('mydata.txt', 'myarchive.zip')
   background.start()
   print('The main program continues to run in foreground.')

   background.join()    # Wait for the background task to finish
   print('Main program waited until background was done.')

Hlavní výzvou vícevláknových aplikací je koordinace vláken, která sdílejí data
nebo jiné prostředky. Modul threading k tomu poskytuje řadu synchronizačních
primitiv včetně zámků, událostí, podmínkových proměnných a semaforů.

Přestože jsou tyto nástroje výkonné, i drobné chyby návrhu mohou způsobit obtížně
reprodukovatelné problémy. Upřednostňovaným přístupem ke koordinaci úloh je proto
soustředit veškerý přístup k prostředku do jediného vlákna a pomocí modulu
:mod:`queue` mu předávat požadavky z ostatních vláken. Aplikace používající
objekty :class:`~queue.Queue` pro komunikaci a koordinaci mezi vlákny se snáze
navrhují, jsou čitelnější a spolehlivější.


.. _tut-logging:

Protokolování
==============

Modul :mod:`logging` nabízí plnohodnotný a flexibilní systém protokolování. V
nejjednodušší podobě se zprávy protokolu odesílají do souboru nebo na
``sys.stderr``::

   import logging
   logging.debug('Debugging information')
   logging.info('Informational message')
   logging.warning('Warning:config file %s not found', 'server.conf')
   logging.error('Error occurred')
   logging.critical('Critical error -- shutting down')

Tím vznikne následující výstup:

.. code-block:: none

   WARNING:root:Warning:config file server.conf not found
   ERROR:root:Error occurred
   CRITICAL:root:Critical error -- shutting down

Ve výchozím nastavení jsou informační a ladicí zprávy potlačeny a výstup se
odesílá na standardní chybový výstup. Mezi další možnosti patří směrování zpráv
prostřednictvím e-mailu, datagramů, soketů nebo na server HTTP. Filtry mohou
vybírat různé směrování podle priority zprávy: :const:`~logging.DEBUG`,
:const:`~logging.INFO`, :const:`~logging.WARNING`, :const:`~logging.ERROR` a
:const:`~logging.CRITICAL`.

Systém protokolování lze konfigurovat přímo z Pythonu nebo načíst z uživatelsky
upravitelného konfiguračního souboru, a přizpůsobit jej tak bez změny aplikace.


.. _tut-weak-references:

Slabé reference
===============

Python provádí automatickou správu paměti (pro většinu objektů počítání referencí
a :term:`automatický úklid paměti <garbage collection>` k odstranění cyklů).
Paměť se
uvolní krátce po odstranění poslední reference na objekt.

Tento přístup dobře funguje ve většině aplikací, někdy je však třeba sledovat
objekty pouze po dobu, kdy je používá něco jiného. Samotné sledování bohužel
vytváří referenci, která by objekty zachovala trvale. Modul :mod:`weakref`
poskytuje nástroje pro sledování objektů bez vytvoření silné reference. Jakmile
objekt není zapotřebí, automaticky se odstraní z tabulky weakref a pro objekty
slabých referencí se zavolá zpětné volání. Typickým použitím je ukládání nákladně
vytvářených objektů do mezipaměti::

   >>> import weakref, gc
   >>> class A:
   ...     def __init__(self, value):
   ...         self.value = value
   ...     def __repr__(self):
   ...         return str(self.value)
   ...
   >>> a = A(10)                   # create a reference
   >>> d = weakref.WeakValueDictionary()
   >>> d['primary'] = a            # does not create a reference
   >>> d['primary']                # fetch the object if it is still alive
   10
   >>> del a                       # remove the one reference
   >>> gc.collect()                # run garbage collection right away
   0
   >>> d['primary']                # entry was automatically removed
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       d['primary']                # entry was automatically removed
     File "C:/python314/lib/weakref.py", line 46, in __getitem__
       o = self.data[key]()
   KeyError: 'primary'


.. _tut-list-tools:

Nástroje pro práci se seznamy
==============================

Mnoho požadavků na datové struktury lze splnit vestavěným typem seznamu. Někdy
jsou však zapotřebí alternativní implementace s jinými výkonnostními kompromisy.

Modul :mod:`array` poskytuje objekt :class:`~array.array`, který se podobá
seznamu, ale ukládá pouze homogenní data a činí tak úsporněji. Následující
příklad ukazuje pole čísel uložených jako dvoubajtová binární čísla bez znaménka
(kód typu ``"H"``) namísto obvyklých 16 bajtů na položku v běžném seznamu
objektů int Pythonu::

   >>> from array import array
   >>> a = array('H', [4000, 10, 700, 22222])
   >>> sum(a)
   26932
   >>> a[1:3]
   array('H', [10, 700])

Modul :mod:`collections` poskytuje objekt :class:`~collections.deque`, který se
podobá seznamu, ale nabízí rychlejší přidávání a odebírání z levé strany za cenu
pomalejšího vyhledávání uprostřed. Tyto objekty jsou vhodné k implementaci front
a prohledávání stromů do šířky::

   >>> from collections import deque
   >>> d = deque(["task1", "task2", "task3"])
   >>> d.append("task4")
   >>> print("Handling", d.popleft())
   Handling task1

::

   unsearched = deque([starting_node])
   def breadth_first_search(unsearched):
       node = unsearched.popleft()
       for m in gen_moves(node):
           if is_goal(m):
               return m
           unsearched.append(m)

Kromě alternativních implementací seznamů nabízí knihovna i další nástroje,
například modul :mod:`bisect` s funkcemi pro práci se seřazenými seznamy::

   >>> import bisect
   >>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
   >>> bisect.insort(scores, (300, 'ruby'))
   >>> scores
   [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

Modul :mod:`heapq` poskytuje funkce pro implementaci hald založených na běžných
seznamech. Položka s nejnižší hodnotou se vždy uchovává na pozici nula. To je
užitečné pro aplikace, které opakovaně přistupují k nejmenšímu prvku, ale
nechtějí pokaždé provádět úplné řazení seznamu::

   >>> from heapq import heapify, heappop, heappush
   >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   >>> heapify(data)                      # rearrange the list into heap order
   >>> heappush(data, -5)                 # add a new entry
   >>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
   [-5, 0, 1]


.. _tut-decimal-fp:

Desetinná aritmetika s plovoucí řádovou čárkou
===============================================

Modul :mod:`decimal` nabízí datový typ :class:`~decimal.Decimal` pro desetinnou
aritmetiku s plovoucí řádovou čárkou. Ve srovnání s vestavěnou binární
implementací :class:`float` je tato třída zvláště užitečná pro

* finanční aplikace a další použití vyžadující přesnou desetinnou reprezentaci,
* řízení přesnosti,
* řízení zaokrouhlování podle právních či regulatorních požadavků,
* sledování platných desetinných míst nebo
* aplikace, v nichž uživatel očekává výsledky odpovídající ručnímu výpočtu.

Výpočet pětiprocentní daně z telefonního poplatku 70 centů například poskytne v
desetinné a binární aritmetice s plovoucí řádovou čárkou odlišné výsledky.
Rozdíl se projeví při zaokrouhlení na nejbližší cent::

   >>> from decimal import *
   >>> round(Decimal('0.70') * Decimal('1.05'), 2)
   Decimal('0.74')
   >>> round(.70 * 1.05, 2)
   0.73

Výsledek :class:`~decimal.Decimal` zachová koncovou nulu a z činitelů se dvěma
platnými místy automaticky odvodí čtyři platná místa. Decimal napodobuje ruční
výpočty a vyhýbá se problémům vznikajícím tehdy, když binární čísla s plovoucí
řádovou čárkou nedokážou přesně reprezentovat desetinné hodnoty.

Přesná reprezentace umožňuje třídě :class:`~decimal.Decimal` provádět výpočty
modulo a testy rovnosti, pro které nejsou binární čísla s plovoucí řádovou
čárkou vhodná::

   >>> Decimal('1.00') % Decimal('.10')
   Decimal('0.00')
   >>> 1.00 % 0.10
   0.09999999999999995

   >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
   True
   >>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
   False

Modul :mod:`decimal` poskytuje aritmetiku s libovolnou potřebnou přesností::

   >>> getcontext().prec = 36
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857')
