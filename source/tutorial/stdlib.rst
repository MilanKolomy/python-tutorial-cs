.. _tut-brieftour:

**************************************
Stručná prohlídka standardní knihovny
**************************************


.. _tut-os-interface:

Rozhraní operačního systému
===========================

Modul :mod:`os` poskytuje desítky funkcí pro komunikaci s operačním systémem::

   >>> import os
   >>> os.getcwd()      # Return the current working directory
   'C:\\Python314'
   >>> os.chdir('/server/accesslogs')   # Change current working directory
   >>> os.system('mkdir today')   # Run the command mkdir in the system shell
   0

Používejte zápis ``import os`` namísto ``from os import *``. Zabráníte tak tomu,
aby :func:`os.open` zastínila vestavěnou funkci :func:`open`, která pracuje
výrazně odlišně.

.. index:: pair: built-in function; help

Vestavěné funkce :func:`dir` a :func:`help` jsou užitečnými interaktivními
pomůckami při práci s rozsáhlými moduly, jako je :mod:`os`::

   >>> import os
   >>> dir(os)
   <returns a list of all module functions>
   >>> help(os)
   <returns an extensive manual page created from the module's docstrings>

Pro běžnou správu souborů a adresářů poskytuje modul :mod:`shutil` rozhraní
vyšší úrovně, které se snadněji používá::

   >>> import shutil
   >>> shutil.copyfile('data.db', 'archive.db')
   'archive.db'
   >>> shutil.move('/build/executables', 'installdir')
   'installdir'


.. _tut-file-wildcards:

Žolíky v názvech souborů
========================

Modul :mod:`glob` poskytuje funkci pro vytváření seznamů souborů vyhledáváním v
adresářích pomocí žolíků::

   >>> import glob
   >>> glob.glob('*.py')
   ['primes.py', 'random.py', 'quote.py']


.. _tut-command-line-arguments:

Argumenty příkazového řádku
============================

Běžné pomocné skripty často potřebují zpracovávat argumenty příkazového řádku.
Tyto argumenty jsou uloženy jako seznam v atributu *argv* modulu :mod:`sys`.
Uvažujme například následující soubor :file:`demo.py`::

   # File demo.py
   import sys
   print(sys.argv)

Toto je výstup spuštění ``python demo.py one two three`` na příkazovém řádku::

   ['demo.py', 'one', 'two', 'three']

Modul :mod:`argparse` poskytuje propracovanější mechanismus zpracování argumentů
příkazového řádku. Následující skript získá jeden či více názvů souborů a
nepovinný počet řádků, které se mají zobrazit::

    import argparse

    parser = argparse.ArgumentParser(
        prog='top',
        description='Show top lines from each file')
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('-l', '--lines', type=int, default=10)
    args = parser.parse_args()
    print(args)

Při spuštění na příkazovém řádku pomocí ``python top.py --lines=5 alpha.txt
beta.txt`` skript nastaví ``args.lines`` na ``5`` a ``args.filenames`` na
``['alpha.txt', 'beta.txt']``.


.. _tut-stderr:

Přesměrování chybového výstupu a ukončení programu
==================================================

Modul :mod:`sys` má také atributy pro *stdin*, *stdout* a *stderr*. Poslední z
nich je užitečný pro vypisování varování a chybových hlášení, která tak zůstanou
viditelná i po přesměrování *stdout*::

   >>> sys.stderr.write('Warning, log file not found starting a new one\n')
   Warning, log file not found starting a new one

Nejpřímějším způsobem ukončení skriptu je použití ``sys.exit()``.


.. _tut-string-pattern-matching:

Porovnávání řetězců se vzory
=============================

Modul :mod:`re` poskytuje nástroje regulárních výrazů pro pokročilé zpracování
řetězců. Pro složité porovnávání a úpravy nabízejí regulární výrazy stručná a
optimalizovaná řešení::

   >>> import re
   >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
   ['foot', 'fell', 'fastest']
   >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
   'cat in the hat'

Pokud potřebujete pouze jednoduché operace, jsou vhodnější řetězcové metody,
protože se snáze čtou a ladí::

   >>> 'tea for too'.replace('too', 'two')
   'tea for two'


.. _tut-mathematics:

Matematika
===========

Modul :mod:`math` zpřístupňuje funkce podkladové knihovny jazyka C pro
matematické operace s plovoucí řádovou čárkou::

   >>> import math
   >>> math.cos(math.pi / 4)
   0.70710678118654757
   >>> math.log(1024, 2)
   10.0

Modul :mod:`random` poskytuje nástroje pro náhodný výběr::

   >>> import random
   >>> random.choice(['apple', 'pear', 'banana'])
   'apple'
   >>> random.sample(range(100), 10)   # sampling without replacement
   [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
   >>> random.random()    # random float from the interval [0.0, 1.0)
   0.17970987693706186
   >>> random.randrange(6)    # random integer chosen from range(6)
   4

Modul :mod:`statistics` počítá základní statistické vlastnosti číselných dat
(průměr, medián, rozptyl atd.)::

    >>> import statistics
    >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    >>> statistics.mean(data)
    1.6071428571428572
    >>> statistics.median(data)
    1.25
    >>> statistics.variance(data)
    1.3720238095238095

Projekt SciPy <https://scipy.org> nabízí mnoho dalších modulů pro numerické
výpočty.

.. _tut-internet-access:

Přístup k internetu
===================

Pro přístup k internetu a zpracování internetových protokolů existuje řada
modulů. Mezi nejjednodušší patří :mod:`urllib.request` pro načítání dat z URL a
:mod:`smtplib` pro odesílání pošty::

   >>> from urllib.request import urlopen
   >>> with urlopen('https://docs.python.org/3/') as response:
   ...     for line in response:
   ...         line = line.decode()             # Convert bytes to a str
   ...         if 'updated' in line:
   ...             print(line.rstrip())         # Remove trailing newline
   ...
         Last updated on Nov 11, 2025 (20:11 UTC).

   >>> import smtplib
   >>> server = smtplib.SMTP('localhost')
   >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
   ... """To: jcaesar@example.org
   ... From: soothsayer@example.org
   ...
   ... Beware the Ides of March.
   ... """)
   >>> server.quit()

(Druhý příklad vyžaduje poštovní server spuštěný na localhostu.)


.. _tut-dates-and-times:

Datum a čas
===============

Modul :mod:`datetime` poskytuje třídy pro jednoduchou i složitou manipulaci s
datem a časem. Podporuje aritmetiku data a času, implementace se však zaměřuje
na efektivní získávání jednotlivých složek pro formátování výstupu a další
zpracování. Modul podporuje také objekty se znalostí časového pásma. ::

   >>> # dates are easily constructed and formatted
   >>> import datetime as dt
   >>> now = dt.date.today()
   >>> now
   datetime.date(2003, 12, 2)
   >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
   '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

   >>> # dates support calendar arithmetic
   >>> birthday = dt.date(1964, 7, 31)
   >>> age = now - birthday
   >>> age.days
   14368


.. _tut-data-compression:

Komprese dat
================

Běžné formáty archivace a komprese dat přímo podporují mimo jiné moduly
:mod:`zlib`, :mod:`gzip`, :mod:`bz2`, :mod:`lzma`, :mod:`zipfile` a
:mod:`tarfile`. ::

   >>> import zlib
   >>> s = b'witch which has which witches wrist watch'
   >>> len(s)
   41
   >>> t = zlib.compress(s)
   >>> len(t)
   37
   >>> zlib.decompress(t)
   b'witch which has which witches wrist watch'
   >>> zlib.crc32(s)
   226805979


.. _tut-performance-measurement:

Měření výkonu
=======================

Někteří uživatelé Pythonu se začnou intenzivně zajímat o relativní výkon různých
přístupů ke stejnému problému. Python poskytuje měřicí nástroj, který na takové
otázky rychle odpoví.

Může být například lákavé použít při záměně hodnot zabalení a rozbalení n-tice
namísto tradičního postupu. Modul :mod:`timeit` rychle ukáže mírnou výkonnostní
výhodu::

   >>> from timeit import Timer
   >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
   0.57535828626024577
   >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
   0.54962537085770791

Na rozdíl od jemné úrovně podrobnosti modulu :mod:`timeit` poskytují moduly
:mod:`profile` a :mod:`pstats` nástroje pro rozpoznání časově kritických částí
ve větších blocích kódu.


.. _tut-quality-control:

Kontrola kvality
================

Jedním z přístupů k vývoji kvalitního softwaru je psát testy pro každou funkci
současně s jejím vývojem a během vývoje je často spouštět.

Modul :mod:`doctest` poskytuje nástroj, který prohledá modul a ověří testy
vložené do dokumentačních řetězců programu. Vytvoření testu je stejně snadné
jako zkopírování typického volání spolu s jeho výsledky do dokumentačního
řetězce. Dokumentace se tím zlepší o příklad pro uživatele a modul doctest může
ověřit, že kód nadále odpovídá dokumentaci::

   def average(values):
       """Computes the arithmetic mean of a list of numbers.

       >>> print(average([20, 30, 70]))
       40.0
       """
       return sum(values) / len(values)

   import doctest
   doctest.testmod()   # automatically validate the embedded tests

Použití modulu :mod:`unittest` není tak nenáročné jako použití :mod:`doctest`,
umožňuje však udržovat rozsáhlejší sadu testů v samostatném souboru::

   import unittest

   class TestStatisticalFunctions(unittest.TestCase):

       def test_average(self):
           self.assertEqual(average([20, 30, 70]), 40.0)
           self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
           with self.assertRaises(ZeroDivisionError):
               average([])
           with self.assertRaises(TypeError):
               average(20, 30, 70)

   unittest.main()  # Calling from the command line invokes all tests


.. _tut-batteries-included:

Včetně baterií
==================

Python vyznává filozofii „včetně baterií“ (*batteries included*). Nejlépe je to
vidět na propracovaných a robustních možnostech jeho větších balíčků. Například:

* Moduly :mod:`xmlrpc.client` a :mod:`xmlrpc.server` činí implementaci vzdáleného
  volání procedur téměř triviální. Navzdory jejich názvům není zapotřebí přímá
  znalost XML ani jeho ruční zpracování.

* Balíček :mod:`email` je knihovna pro správu e-mailových zpráv včetně MIME a
  dalších dokumentů zpráv založených na :rfc:`5322`. Na rozdíl od modulů
  :mod:`smtplib` a :mod:`poplib`, které zprávy skutečně odesílají a přijímají,
  nabízí balíček email úplnou sadu nástrojů pro vytváření a dekódování složitých
  struktur zpráv (včetně příloh) a implementaci internetového kódování a
  protokolů hlaviček.

* Balíček :mod:`json` poskytuje robustní podporu analýzy tohoto oblíbeného
  formátu pro výměnu dat. Modul :mod:`csv` podporuje přímé čtení a zápis souborů
  ve formátu hodnot oddělených čárkami (Comma-Separated Value), který běžně
  podporují databáze a tabulkové procesory. Zpracování XML podporují balíčky
  :mod:`xml.etree.ElementTree`, :mod:`xml.dom` a :mod:`xml.sax`. Tyto moduly a
  balíčky společně výrazně zjednodušují výměnu dat mezi aplikacemi v Pythonu a
  dalšími nástroji.

* Modul :mod:`sqlite3` je obalem databázové knihovny SQLite a poskytuje trvalou
  databázi, kterou lze aktualizovat a používat pomocí mírně nestandardní syntaxe
  SQL.

* Internacionalizaci podporuje řada modulů včetně :mod:`gettext`, :mod:`locale`
  a balíčku :mod:`codecs`.
