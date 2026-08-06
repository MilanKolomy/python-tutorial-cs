.. _tut-errors:

*********************
Chyby a výjimky
*********************

Dosud jsme se o chybových hlášeních pouze zmínili, ale pokud jste si příklady
zkoušeli, pravděpodobně jste už některá viděli. Rozlišujeme (přinejmenším) dva
druhy chyb: *syntaktické chyby* a *výjimky*.


.. _tut-syntaxerrors:

Syntaktické chyby
=================

Syntaktické chyby, označované také jako chyby při syntaktické analýze, jsou
patrně nejčastějším druhem potíží při učení se Pythonu::

   >>> while True print('Hello world')
     File "<stdin>", line 1
       while True print('Hello world')
                  ^^^^^
   SyntaxError: invalid syntax

Syntaktický analyzátor zopakuje chybný řádek a zobrazí malé šipky ukazující na
místo, kde byla chyba zjištěna. Nemusí však jít o místo, které je třeba opravit.
V příkladu je chyba zjištěna u funkce :func:`print`, protože těsně před ní chybí
dvojtečka (``':'``).

Vypíše se také název souboru (v našem příkladu ``<stdin>``) a číslo řádku,
abyste věděli, kde hledat, pokud vstup pochází ze souboru.


.. _tut-exceptions:

Výjimky
==========

I syntakticky správný příkaz nebo výraz může při pokusu o provedení způsobit
chybu. Chyby zjištěné za běhu se nazývají *výjimky* a nemusejí být nutně
fatální: brzy se naučíte, jak je v programech v Pythonu obsluhovat. Většina
výjimek však programy obsluhována není a vede k chybovým hlášením, jako jsou
následující::

   >>> 10 * (1/0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       10 * (1/0)
             ~^~
   ZeroDivisionError: division by zero
   >>> 4 + spam*3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       4 + spam*3
           ^^^^
   NameError: name 'spam' is not defined
   >>> '2' + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       '2' + 2
       ~~~~^~~
   TypeError: can only concatenate str (not "int") to str

Poslední řádek chybového hlášení uvádí, co se stalo. Výjimky mají různé typy a
typ je součástí hlášení: v příkladu jde o :exc:`ZeroDivisionError`,
:exc:`NameError` a :exc:`TypeError`. Řetězec vypsaný jako typ výjimky je názvem
vestavěné výjimky, která nastala. To platí pro všechny vestavěné výjimky, ale
nemusí to platit pro uživatelsky definované výjimky (jde však o užitečnou
konvenci). Standardní názvy výjimek jsou vestavěné identifikátory, nikoli
rezervovaná klíčová slova.

Zbytek řádku uvádí podrobnosti odpovídající typu výjimky a její příčině.

Předchozí část chybového hlášení ukazuje kontext, ve kterém výjimka nastala,
formou výpisu zásobníku volání. Obecně obsahuje zdrojové řádky, nezobrazí však
řádky načtené ze standardního vstupu.

Část :ref:`bltin-exceptions` uvádí vestavěné výjimky a jejich význam.


.. _tut-handling:

Obsluha výjimek
===================

Lze psát programy, které obsluhují vybrané výjimky. Následující příklad žádá
uživatele o vstup, dokud nezadá platné celé číslo, ale umožňuje mu program
přerušit (pomocí :kbd:`Control-C` nebo prostředku podporovaného operačním
systémem). Přerušení vyvolané uživatelem je signalizováno výjimkou
:exc:`KeyboardInterrupt`. ::

   >>> while True:
   ...     try:
   ...         x = int(input("Please enter a number: "))
   ...         break
   ...     except ValueError:
   ...         print("Oops!  That was no valid number.  Try again...")
   ...

Příkaz :keyword:`try` funguje následovně.

* Nejprve se provede *klauzule try* (příkaz či příkazy mezi klíčovými slovy
  :keyword:`try` a :keyword:`except`).

* Pokud žádná výjimka nenastane, *klauzule except* se přeskočí a provádění
  příkazu :keyword:`try` skončí.

* Pokud během provádění klauzule :keyword:`try` nastane výjimka, zbytek klauzule
  se přeskočí. Odpovídá-li její typ výjimce uvedené za klíčovým slovem
  :keyword:`except`, provede se *klauzule except* a provádění poté pokračuje za
  blokem try/except.

* Pokud nastane výjimka, která neodpovídá výjimce uvedené v *klauzuli except*,
  předá se vnějším příkazům :keyword:`try`. Nenajde-li se žádná obsluha, jde o
  *neošetřenou výjimku* a provádění se zastaví s chybovým hlášením.

Příkaz :keyword:`try` může mít více *klauzulí except*, které určují obsluhu
různých výjimek. Provede se nejvýše jedna obsluha. Obsluhy zachycují pouze
výjimky, které nastanou v odpovídající *klauzuli try*, nikoli v jiných obsluhách
téhož příkazu :keyword:`!try`. *Klauzule except* může uvádět více výjimek,
například::

   ... except RuntimeError, TypeError, NameError:
   ...     pass

Třída v klauzuli :keyword:`except` odpovídá výjimkám, které jsou instancemi této
třídy nebo některé z jejích odvozených tříd (nikoli však naopak --- *klauzule
except* uvádějící odvozenou třídu neodpovídá instancím jejích základních tříd).
Následující kód například vypíše B, C, D v tomto pořadí::

   class B(Exception):
       pass

   class C(B):
       pass

   class D(C):
       pass

   for cls in [B, C, D]:
       try:
           raise cls()
       except D:
           print("D")
       except C:
           print("C")
       except B:
           print("B")

Kdyby bylo pořadí *klauzulí except* obrácené (s ``except B`` jako první), kód by
vypsal B, B, B --- spustí se první odpovídající *klauzule except*.

Výjimka může mít přidružené hodnoty, označované také jako její *argumenty*.
Přítomnost a typy argumentů závisejí na typu výjimky.

*Klauzule except* může za názvem výjimky uvést proměnnou. Ta se naváže na
instanci výjimky, která obvykle obsahuje atribut ``args`` uchovávající
argumenty. Vestavěné typy výjimek pro usnadnění definují
:meth:`~object.__str__`, která vypíše všechny argumenty bez přímého přístupu k
``.args``. ::

   >>> try:
   ...     raise Exception('spam', 'eggs')
   ... except Exception as inst:
   ...     print(type(inst))    # the exception type
   ...     print(inst.args)     # arguments stored in .args
   ...     print(inst)          # __str__ allows args to be printed directly,
   ...                          # but may be overridden in exception subclasses
   ...     x, y = inst.args     # unpack args
   ...     print('x =', x)
   ...     print('y =', y)
   ...
   <class 'Exception'>
   ('spam', 'eggs')
   ('spam', 'eggs')
   x = spam
   y = eggs

Výstup metody :meth:`~object.__str__` výjimky se vypíše jako poslední část
(„podrobnosti“) hlášení o neošetřené výjimce.

:exc:`BaseException` je společnou základní třídou všech výjimek. Jedna z jejích
podtříd, :exc:`Exception`, je základní třídou všech nefatálních výjimek. Výjimky,
které nejsou podtřídami :exc:`Exception`, se obvykle neobsluhují, protože
signalizují, že by měl program skončit. Patří mezi ně :exc:`SystemExit`, kterou
vyvolává :meth:`sys.exit`, a :exc:`KeyboardInterrupt`, která se vyvolá, když chce
uživatel program přerušit.

:exc:`Exception` lze použít jako zástupný typ, který zachytí (téměř) vše. Je
však vhodné co nejpřesněji určit typy výjimek, které chceme obsloužit, a
umožnit neočekávaným výjimkám, aby se šířily dál.

Nejběžnějším vzorem pro obsluhu :exc:`Exception` je výjimku vypsat nebo
zaznamenat do protokolu a poté ji znovu vyvolat (takže ji může obsloužit také
volající)::

   import sys

   try:
       f = open('myfile.txt')
       s = f.readline()
       i = int(s.strip())
   except OSError as err:
       print("OS error:", err)
   except ValueError:
       print("Could not convert data to an integer.")
   except Exception as err:
       print(f"Unexpected {err=}, {type(err)=}")
       raise

Příkaz :keyword:`try` ... :keyword:`except` má nepovinnou *klauzuli else*, která
musí následovat za všemi *klauzulemi except*. Je užitečná pro kód, který se má
provést, pokud *klauzule try* nevyvolá výjimku. Například::

   for arg in sys.argv[1:]:
       try:
           f = open(arg, 'r')
       except OSError:
           print('cannot open', arg)
       else:
           print(arg, 'has', len(f.readlines()), 'lines')
           f.close()

Použití klauzule :keyword:`!else` je lepší než přidání dalšího kódu do klauzule
:keyword:`try`, protože zabraňuje neúmyslnému zachycení výjimky, kterou
nevyvolal kód chráněný příkazem :keyword:`!try` ... :keyword:`!except`.

Obsluhy výjimek nezachycují pouze výjimky, které nastanou přímo v *klauzuli
try*, ale také výjimky uvnitř funkcí volaných z této klauzule, a to i nepřímo.
Například::

   >>> def this_fails():
   ...     x = 1/0
   ...
   >>> try:
   ...     this_fails()
   ... except ZeroDivisionError as err:
   ...     print('Handling run-time error:', err)
   ...
   Handling run-time error: division by zero


.. _tut-raising:

Vyvolávání výjimek
==================

Příkaz :keyword:`raise` umožňuje programátorovi vynutit vyvolání určené výjimky.
Například::

   >>> raise NameError('HiThere')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       raise NameError('HiThere')
   NameError: HiThere

Jediný argument příkazu :keyword:`raise` určuje výjimku, která se má vyvolat.
Musí jít buď o instanci výjimky, nebo o třídu výjimky (třídu odvozenou od
:class:`BaseException`, například :exc:`Exception` nebo některou z jejích
podtříd). Je-li předána třída výjimky, implicitně se vytvoří její instance
voláním konstruktoru bez argumentů::

   raise ValueError  # shorthand for 'raise ValueError()'

Potřebujete-li zjistit, zda byla výjimka vyvolána, ale nechcete ji obsluhovat,
umožňuje jednodušší tvar příkazu :keyword:`raise` výjimku znovu vyvolat::

   >>> try:
   ...     raise NameError('HiThere')
   ... except NameError:
   ...     print('An exception flew by!')
   ...     raise
   ...
   An exception flew by!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise NameError('HiThere')
   NameError: HiThere


.. _tut-exception-chaining:

Řetězení výjimek
==================

Pokud uvnitř části :keyword:`except` nastane neošetřená výjimka, připojí se k ní
právě obsluhovaná výjimka a obě budou zahrnuty v chybovém hlášení::

    >>> try:
    ...     open("database.sqlite")
    ... except OSError:
    ...     raise RuntimeError("unable to handle error")
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
        open("database.sqlite")
        ~~~~^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'
    <BLANKLINE>
    During handling of the above exception, another exception occurred:
    <BLANKLINE>
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
        raise RuntimeError("unable to handle error")
    RuntimeError: unable to handle error

K vyjádření, že je jedna výjimka přímým důsledkem jiné, umožňuje příkaz
:keyword:`raise` použít nepovinnou klauzuli :keyword:`from<raise>`::

    # exc must be exception instance or None.
    raise RuntimeError from exc

To může být užitečné při převádění výjimek. Například::

    >>> def func():
    ...     raise ConnectionError
    ...
    >>> try:
    ...     func()
    ... except ConnectionError as exc:
    ...     raise RuntimeError('Failed to open database') from exc
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
        func()
        ~~~~^^
      File "<stdin>", line 2, in func
    ConnectionError
    <BLANKLINE>
    The above exception was the direct cause of the following exception:
    <BLANKLINE>
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
        raise RuntimeError('Failed to open database') from exc
    RuntimeError: Failed to open database

Automatické řetězení výjimek lze také vypnout pomocí idiomu ``from None``::

    >>> try:
    ...     open('database.sqlite')
    ... except OSError:
    ...     raise RuntimeError from None
    ...
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
        raise RuntimeError from None
    RuntimeError

Další informace o mechanismu řetězení naleznete v části
:ref:`bltin-exceptions`.


.. _tut-userexceptions:

Uživatelsky definované výjimky
==============================

Programy mohou pojmenovat vlastní výjimky vytvořením nové třídy výjimky (další
informace o třídách v Pythonu viz :ref:`tut-classes`). Výjimky by měly být
zpravidla přímo či nepřímo odvozeny od třídy :exc:`Exception`.

Třídy výjimek mohou dělat cokoli, co jiné třídy, obvykle však zůstávají
jednoduché a často nabízejí pouze několik atributů, pomocí nichž mohou obsluhy
výjimek získat informace o chybě.

Názvy většiny výjimek končí slovem „Error“, podobně jako názvy standardních
výjimek.

Mnoho standardních modulů definuje vlastní výjimky pro oznamování chyb, které
mohou nastat v jimi definovaných funkcích.


.. _tut-cleanup:

Definování úklidových akcí
==========================

Příkaz :keyword:`try` má další nepovinnou klauzuli určenou k definování
úklidových akcí, které se musí provést za všech okolností. Například::

   >>> try:
   ...     raise KeyboardInterrupt
   ... finally:
   ...     print('Goodbye, world!')
   ...
   Goodbye, world!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise KeyboardInterrupt
   KeyboardInterrupt

Je-li přítomna klauzule :keyword:`finally`, provede se jako poslední úloha před
dokončením příkazu :keyword:`try`. Klauzule :keyword:`!finally` se provede bez
ohledu na to, zda příkaz :keyword:`!try` vyvolá výjimku. Následující body
popisují složitější případy, kdy výjimka nastane:

* Nastane-li výjimka během provádění klauzule :keyword:`!try`, může ji obsloužit
  klauzule :keyword:`except`. Pokud ji žádná klauzule :keyword:`!except`
  neobslouží, po provedení klauzule :keyword:`!finally` se výjimka znovu vyvolá.

* Výjimka může nastat během provádění klauzule :keyword:`!except` nebo
  :keyword:`!else`. I v tomto případě se po provedení klauzule
  :keyword:`!finally` znovu vyvolá.

* Pokud klauzule :keyword:`!finally` provede příkaz :keyword:`break`,
  :keyword:`continue` nebo :keyword:`return`, výjimky se znovu nevyvolají. To
  může být matoucí, a proto se takový postup nedoporučuje. Od verze 3.14 na něj
  kompilátor upozorňuje pomocí :exc:`SyntaxWarning` (viz :pep:`765`).

* Pokud příkaz :keyword:`!try` dospěje k příkazu :keyword:`break`,
  :keyword:`continue` nebo :keyword:`return`, klauzule :keyword:`!finally` se
  provede těsně před provedením daného příkazu :keyword:`!break`,
  :keyword:`!continue` nebo :keyword:`!return`.

* Pokud klauzule :keyword:`!finally` obsahuje příkaz :keyword:`!return`, vrácená
  hodnota bude pocházet z příkazu :keyword:`!return` v klauzuli
  :keyword:`!finally`, nikoli z příkazu :keyword:`!return` v klauzuli
  :keyword:`!try`. To může být matoucí, a proto se takový postup nedoporučuje.
  Od verze 3.14 na něj kompilátor upozorňuje pomocí :exc:`SyntaxWarning` (viz
  :pep:`765`).

Například::

   >>> def bool_return():
   ...     try:
   ...         return True
   ...     finally:
   ...         return False
   ...
   >>> bool_return()
   False

Složitější příklad::

   >>> def divide(x, y):
   ...     try:
   ...         result = x / y
   ...     except ZeroDivisionError:
   ...         print("division by zero!")
   ...     else:
   ...         print("result is", result)
   ...     finally:
   ...         print("executing finally clause")
   ...
   >>> divide(2, 1)
   result is 2.0
   executing finally clause
   >>> divide(2, 0)
   division by zero!
   executing finally clause
   >>> divide("2", "1")
   executing finally clause
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       divide("2", "1")
       ~~~~~~^^^^^^^^^^
     File "<stdin>", line 3, in divide
       result = x / y
                ~~^~~
   TypeError: unsupported operand type(s) for /: 'str' and 'str'

Jak vidíte, klauzule :keyword:`finally` se provede za všech okolností. Výjimku
:exc:`TypeError` vyvolanou dělením dvou řetězců klauzule :keyword:`except`
neobslouží, a proto se po provedení klauzule :keyword:`!finally` znovu vyvolá.

V reálných aplikacích je klauzule :keyword:`finally` užitečná k uvolňování
externích prostředků (například souborů nebo síťových spojení) bez ohledu na to,
zda bylo jejich použití úspěšné.


.. _tut-cleanup-with:

Předdefinované úklidové akce
============================

Některé objekty definují standardní úklidové akce, které se mají provést, když
objekt již není zapotřebí, bez ohledu na to, zda operace používající objekt
uspěla, či selhala. Následující příklad se pokusí otevřít soubor a vypsat jeho
obsah na obrazovku. ::

   for line in open("myfile.txt"):
       print(line, end="")

Problém tohoto kódu spočívá v tom, že po dokončení dané části kódu ponechá
soubor po neurčenou dobu otevřený. U jednoduchých skriptů to nevadí, ale ve
větších aplikacích to může být problém. Příkaz :keyword:`with` umožňuje používat
objekty, jako jsou soubory, způsobem, který zajišťuje jejich vždy včasný a
správný úklid. ::

   with open("myfile.txt") as f:
       for line in f:
           print(line, end="")

Po provedení příkazu je soubor *f* vždy zavřen, i když při zpracování řádků
nastal problém. Objekty, které podobně jako soubory poskytují předdefinované
úklidové akce, na tuto skutečnost upozorňují ve své dokumentaci.


.. _tut-exception-groups:

Vyvolávání a obsluha více nesouvisejících výjimek
==================================================

Existují situace, kdy je nutné oznámit několik výjimek, které nastaly. Často se
to stává v systémech pro souběžné zpracování, kde může paralelně selhat
několik úloh, existují však i jiné případy, kdy je vhodné pokračovat v provádění
a shromáždit více chyb namísto vyvolání první výjimky.

Vestavěná výjimka :exc:`ExceptionGroup` obaluje seznam instancí výjimek, aby je
bylo možné vyvolat společně. Sama je výjimkou, takže ji lze zachytit stejně jako
jakoukoli jinou výjimku. ::

   >>> def f():
   ...     excs = [OSError('error 1'), SystemError('error 2')]
   ...     raise ExceptionGroup('there were problems', excs)
   ...
   >>> f()
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 1, in <module>
     |     f()
     |     ~^^
     |   File "<stdin>", line 3, in f
     |     raise ExceptionGroup('there were problems', excs)
     | ExceptionGroup: there were problems (2 sub-exceptions)
     +-+---------------- 1 ----------------
       | OSError: error 1
       +---------------- 2 ----------------
       | SystemError: error 2
       +------------------------------------
   >>> try:
   ...     f()
   ... except Exception as e:
   ...     print(f'caught {type(e)}: {e}')
   ...
   caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
   >>>

Použitím ``except*`` namísto ``except`` můžeme selektivně obsloužit pouze
výjimky ve skupině, které odpovídají určitému typu. V následujícím příkladu s
vnořenou skupinou výjimek každá klauzule ``except*`` vybere ze skupiny výjimky
určitého typu, zatímco všechny ostatní nechá šířit do dalších klauzulí a
nakonec znovu vyvolat. ::

   >>> def f():
   ...     raise ExceptionGroup(
   ...         "group1",
   ...         [
   ...             OSError(1),
   ...             SystemError(2),
   ...             ExceptionGroup(
   ...                 "group2",
   ...                 [
   ...                     OSError(3),
   ...                     RecursionError(4)
   ...                 ]
   ...             )
   ...         ]
   ...     )
   ...
   >>> try:
   ...     f()
   ... except* OSError as e:
   ...     print("There were OSErrors")
   ... except* SystemError as e:
   ...     print("There were SystemErrors")
   ...
   There were OSErrors
   There were SystemErrors
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 2, in <module>
     |     f()
     |     ~^^
     |   File "<stdin>", line 2, in f
     |     raise ExceptionGroup(
     |     ...<12 lines>...
     |     )
     | ExceptionGroup: group1 (1 sub-exception)
     +-+---------------- 1 ----------------
       | ExceptionGroup: group2 (1 sub-exception)
       +-+---------------- 1 ----------------
         | RecursionError: 4
         +------------------------------------
   >>>

Výjimky vnořené do skupiny výjimek musí být instance, nikoli typy. V praxi totiž
zpravidla půjde o výjimky, které již program vyvolal a zachytil podle
následujícího vzoru::

   >>> excs = []
   ... for test in tests:
   ...     try:
   ...         test.run()
   ...     except Exception as e:
   ...         excs.append(e)
   ...
   >>> if excs:
   ...    raise ExceptionGroup("Test Failures", excs)
   ...


.. _tut-exception-notes:

Obohacování výjimek poznámkami
===============================

Když je vytvořena výjimka určená k vyvolání, obvykle se inicializuje informacemi
popisujícími vzniklou chybu. V některých případech je užitečné přidat informace
až po zachycení výjimky. K tomu mají výjimky metodu ``add_note(note)``, která
přijme řetězec a přidá jej do seznamu poznámek výjimky. Standardní zobrazení
výpisu zásobníku zahrnuje za výjimkou všechny poznámky v pořadí, v jakém byly
přidány. ::

   >>> try:
   ...     raise TypeError('bad type')
   ... except Exception as e:
   ...     e.add_note('Add some information')
   ...     e.add_note('Add some more information')
   ...     raise
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise TypeError('bad type')
   TypeError: bad type
   Add some information
   Add some more information
   >>>

Při shromažďování výjimek do skupiny můžeme například chtít přidat kontextové
informace k jednotlivým chybám. V následujícím příkladu má každá výjimka ve
skupině poznámku uvádějící, kdy daná chyba nastala. ::

   >>> def f():
   ...     raise OSError('operation failed')
   ...
   >>> excs = []
   >>> for i in range(3):
   ...     try:
   ...         f()
   ...     except Exception as e:
   ...         e.add_note(f'Happened in Iteration {i+1}')
   ...         excs.append(e)
   ...
   >>> raise ExceptionGroup('We have some problems', excs)
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 1, in <module>
     |     raise ExceptionGroup('We have some problems', excs)
     | ExceptionGroup: We have some problems (3 sub-exceptions)
     +-+---------------- 1 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operation failed')
       | OSError: operation failed
       | Happened in Iteration 1
       +---------------- 2 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operation failed')
       | OSError: operation failed
       | Happened in Iteration 2
       +---------------- 3 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operation failed')
       | OSError: operation failed
       | Happened in Iteration 3
       +------------------------------------
   >>>
