.. _tut-modules:

*******
Moduly
*******

Po ukončení a opětovném spuštění interpretu Pythonu se vytvořené definice
(funkce a proměnné) ztratí. Delší program je proto vhodnější připravit v textovém
editoru a výsledný soubor použít jako vstup interpretu. Tomu se říká vytvoření
*skriptu*. S rostoucí délkou programu jej možná budete chtít kvůli snazší údržbě
rozdělit do několika souborů. Také můžete chtít používat užitečnou funkci ve
více programech, aniž byste její definici do každého z nich kopírovali.

Python proto umožňuje uložit definice do souboru a používat je ve skriptu nebo
v interaktivní instanci interpretu. Takový soubor se nazývá *modul*; jeho
definice lze *importovat* do jiných modulů nebo do *hlavního* modulu (souboru
proměnných dostupných ve skriptu prováděném na nejvyšší úrovni a v režimu
kalkulačky).

Modul je soubor obsahující definice a příkazy Pythonu. Název souboru tvoří název
modulu s příponou :file:`.py`. Uvnitř modulu je jeho název jako řetězec dostupný
v globální proměnné ``__name__``. Vytvořte například ve svém oblíbeném editoru
v aktuálním adresáři soubor :file:`fibo.py` s následujícím obsahem::

   # Fibonacci numbers module

   def fib(n):
       """Write Fibonacci series up to n."""
       a, b = 0, 1
       while a < n:
           print(a, end=' ')
           a, b = b, a+b
       print()

   def fib2(n):
       """Return Fibonacci series up to n."""
       result = []
       a, b = 0, 1
       while a < n:
           result.append(a)
           a, b = b, a+b
       return result

Nyní spusťte interpret Pythonu a importujte modul následujícím příkazem::

   >>> import fibo

Tím se názvy funkcí definovaných v ``fibo`` nepřidají přímo do aktuálního
:term:`jmenného prostoru <namespace>` (podrobnosti viz :ref:`tut-scopes`);
přidá se do něj pouze název modulu ``fibo``. Přes název modulu lze přistupovat
k funkcím::

   >>> fibo.fib(1000)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
   >>> fibo.fib2(100)
   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
   >>> fibo.__name__
   'fibo'

Chcete-li funkci používat často, můžete ji přiřadit lokálnímu názvu::

   >>> fib = fibo.fib
   >>> fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


.. _tut-moremodules:

Více o modulech
===============

Modul může kromě definic funkcí obsahovat i proveditelné příkazy. Ty slouží
k inicializaci modulu a provedou se pouze *poprvé*, kdy se název modulu objeví
v příkazu importu. [#]_
(Provedou se také tehdy, je-li soubor spuštěn jako skript.)

Každý modul má vlastní soukromý jmenný prostor, který všechny funkce definované
v modulu používají jako globální. Autor modulu proto může používat globální
proměnné bez obav z náhodných kolizí s globálními proměnnými uživatele. Pokud
víte, co děláte, můžete ke globálním proměnným modulu přistupovat zápisem
``modname.itemname``, stejně jako k jeho funkcím.

Moduly mohou importovat jiné moduly. Je zvykem, nikoli povinností, umístit
všechny příkazy :keyword:`import` na začátek modulu či skriptu. Názvy modulů
importované na nejvyšší úrovni (mimo funkce a třídy) se přidají do globálního
jmenného prostoru modulu.

Varianta příkazu :keyword:`import` importuje názvy z modulu přímo do jmenného
prostoru importujícího modulu. Například::

   >>> from fibo import fib, fib2
   >>> fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Název modulu, z něhož se importuje, se tím do lokálního jmenného prostoru
nezavede (v příkladu tedy není definováno ``fibo``).

Existuje dokonce varianta importující všechny názvy definované modulem::

   >>> from fibo import *
   >>> fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Ta importuje všechny názvy kromě názvů začínajících podtržítkem (``_``).
Programátoři v Pythonu ji většinou nepoužívají, protože do interpretu zavádí
neznámou množinu názvů a může skrýt již definované položky.

Import ``*`` z modulu nebo balíčku se obecně nedoporučuje, protože často vede
k obtížně čitelnému kódu. V interaktivní relaci jej však lze použít pro úsporu
psaní.

Následuje-li za názvem modulu :keyword:`!as`, naváže se název uvedený za
:keyword:`!as` přímo na importovaný modul.

::

   >>> import fibo as fib
   >>> fib.fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Ve výsledku se modul importuje stejně jako pomocí ``import fibo``, pouze je
dostupný pod názvem ``fib``.

Obdobně lze :keyword:`!as` použít také společně s :keyword:`from`::

   >>> from fibo import fib as fibonacci
   >>> fibonacci(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


.. note::

   Z důvodu efektivity se každý modul v jedné relaci interpretu importuje pouze
   jednou. Po změně modulů proto musíte interpret restartovat; chcete-li
   interaktivně testovat pouze jeden modul, použijte :func:`importlib.reload`,
   například ``import importlib; importlib.reload(modulename)``.


.. _tut-modulesasscripts:

Spouštění modulů jako skriptů
--------------------------------

Spustíte-li modul Pythonu pomocí ::

   python fibo.py <arguments>

provede se kód modulu stejně jako při importu, ale ``__name__`` bude nastaveno
na ``"__main__"``. Přidáním následujícího kódu na konec modulu::

   if __name__ == "__main__":
       import sys
       fib(int(sys.argv[1]))

lze proto soubor používat jako skript i importovatelný modul, protože kód
zpracovávající příkazový řádek se spustí pouze tehdy, je-li modul proveden jako
„hlavní“ soubor:

.. code-block:: shell-session

   $ python fibo.py 50
   0 1 1 2 3 5 8 13 21 34

Při importu modulu se kód nespustí::

   >>> import fibo
   >>>

Tento postup se často používá k vytvoření pohodlného uživatelského rozhraní
modulu nebo k testování (spuštění modulu jako skriptu provede sadu testů).


.. _tut-searchpath:

Vyhledávací cesta modulů
-------------------------

.. index:: triple: module; search; path

Při importu modulu :mod:`!spam` interpret nejprve hledá vestavěný modul tohoto
názvu. Jejich názvy uvádí :data:`sys.builtin_module_names`. Pokud jej nenajde,
hledá soubor :file:`spam.py` v adresářích z proměnné :data:`sys.path`.
:data:`sys.path` se inicializuje z těchto umístění:

* Adresář obsahující vstupní skript (nebo aktuální adresář, není-li zadán soubor).
* :envvar:`PYTHONPATH` (seznam názvů adresářů se stejnou syntaxí jako shellová
  proměnná :envvar:`PATH`).
* Výchozí hodnota závislá na instalaci (podle konvence zahrnuje adresář
  ``site-packages`` zpracovávaný modulem :mod:`site`).

Další podrobnosti obsahuje :ref:`sys-path-init`.

.. note::
   Na souborových systémech podporujících symbolické odkazy se adresář
   obsahující vstupní skript určí až po následování odkazu. Adresář obsahující
   symbolický odkaz se tedy do vyhledávací cesty modulů **nepřidá**.

Po inicializaci mohou programy v Pythonu :data:`sys.path` měnit. Adresář
obsahující spuštěný skript se umístí na začátek vyhledávací cesty před cestu ke
standardní knihovně. Skripty z tohoto adresáře se proto načtou namísto stejně
pojmenovaných modulů z knihovny. Není-li nahrazení záměrné, jde o chybu. Více
informací obsahuje :ref:`tut-standardmodules`.

.. %
    Do we need stuff on zip files etc. ? DUBOIS

.. _tut-pycache:

„Kompilované“ soubory Pythonu
------------------------------

Pro urychlení načítání ukládá Python kompilovanou verzi každého modulu do
mezipaměti v adresáři ``__pycache__`` pod názvem
:file:`module.{version}.pyc`. Verze kóduje formát kompilovaného souboru a obvykle
obsahuje číslo verze Pythonu. V CPythonu 3.3 by se například zkompilovaný
``spam.py`` uložil jako ``__pycache__/spam.cpython-33.pyc``. Tato konvence
umožňuje souběžnou existenci modulů z různých vydání a verzí Pythonu.

Python porovnává datum změny zdrojového souboru s kompilovanou verzí a zjišťuje,
zda není zastaralá a nepotřebuje znovu zkompilovat. Proces je zcela automatický.
Kompilované moduly jsou navíc nezávislé na platformě, takže lze tutéž knihovnu
sdílet mezi systémy s různými architekturami.

Python mezipaměť nekontroluje ve dvou případech. Modul načtený přímo
z příkazového řádku vždy znovu zkompiluje a výsledek neuloží. Mezipaměť také
nekontroluje, pokud neexistuje zdrojový modul. Pro distribuci bez zdrojů (pouze
kompilovanou) musí být kompilovaný modul ve zdrojovém adresáři a zdrojový modul
nesmí existovat.

Několik tipů pro zkušené uživatele:

* Přepínači :option:`-O` a :option:`-OO` příkazu Python lze zmenšit kompilovaný
  modul. ``-O`` odstraní příkazy assert, ``-OO`` navíc řetězce __doc__. Některé
  programy na nich mohou záviset, proto je používejte jen tehdy, víte-li, co
  děláte. „Optimalizované“ moduly mají značku ``opt-`` a bývají menší. Budoucí
  vydání mohou účinky optimalizace změnit.

* Program načtený ze souboru ``.pyc`` neběží rychleji než ze souboru ``.py``;
  rychlejší je pouze jeho načtení.

* Modul :mod:`compileall` dokáže vytvořit soubory .pyc pro všechny moduly
  v adresáři.

* Podrobnější popis procesu včetně vývojového diagramu rozhodování obsahuje
  :pep:`3147`.


.. _tut-standardmodules:

Standardní moduly
=================

.. index:: pair: module; sys

Python se dodává s knihovnou standardních modulů popsanou v samostatné
Referenční příručce knihovny Pythonu (dále „Referenční příručka knihovny“).
Některé moduly jsou vestavěné do interpretu a zpřístupňují operace, které nejsou
součástí jádra jazyka, ale jsou vestavěny kvůli efektivitě nebo přístupu
k základním prostředkům operačního systému, například systémovým voláním.
Jejich množina závisí na konfiguraci a platformě; modul :mod:`winreg` je třeba
dostupný pouze ve Windows. Zvláštní pozornost si zaslouží :mod:`sys`, vestavěný
v každém interpretu Pythonu. Proměnné ``sys.ps1`` a ``sys.ps2`` určují řetězce
primární a sekundární výzvy::

   >>> import sys
   >>> sys.ps1
   '>>> '
   >>> sys.ps2
   '... '
   >>> sys.ps1 = 'C> '
   C> print('Yuck!')
   Yuck!
   C>


Tyto dvě proměnné jsou definované pouze v interaktivním režimu interpretu.

Proměnná ``sys.path`` je seznam řetězců určující vyhledávací cestu modulů.
Inicializuje se výchozí cestou z proměnné prostředí :envvar:`PYTHONPATH`, nebo
vestavěnou výchozí hodnotou, není-li :envvar:`PYTHONPATH` nastavena. Můžete ji
měnit běžnými operacemi se seznamem::

   >>> import sys
   >>> sys.path.append('/ufs/guido/lib/python')


.. _tut-dir:

Funkce :func:`dir`
========================

Vestavěná funkce :func:`dir` zjišťuje názvy definované modulem. Vrací seřazený
seznam řetězců::

   >>> import fibo, sys
   >>> dir(fibo)
   ['__name__', 'fib', 'fib2']
   >>> dir(sys)  # doctest: +NORMALIZE_WHITESPACE
   ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
    '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
    '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
    '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
    '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
    'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
    'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
    'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
    'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
    'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
    'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
    'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
    'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
    'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
    'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
    'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
    'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
    'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
    'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
    'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
    'warnoptions']

Bez argumentů vypíše :func:`dir` aktuálně definované názvy::

   >>> a = [1, 2, 3, 4, 5]
   >>> import fibo
   >>> fib = fibo.fib
   >>> dir()
   ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Vypíše všechny druhy názvů: proměnné, moduly, funkce a podobně.

.. index:: pair: module; builtins

:func:`dir` nevypisuje názvy vestavěných funkcí a proměnných. Jejich seznam
získáte ze standardního modulu :mod:`builtins`, v němž jsou definovány::

   >>> import builtins
   >>> dir(builtins)  # doctest: +NORMALIZE_WHITESPACE
   ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
    'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
    'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
    'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
    'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
    'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
    'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
    'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
    'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
    'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
    'NotImplementedError', 'OSError', 'OverflowError',
    'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
    'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
    'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
    'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
    'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
    'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
    'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
    '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
    'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
    'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
    'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
    'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
    'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
    'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
    'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
    'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
    'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
    'zip']

.. _tut-packages:

Balíčky
========

Balíčky strukturují jmenný prostor modulů Pythonu pomocí „tečkovaných názvů
modulů“. Název :mod:`!A.B` například označuje podmodul ``B`` v balíčku ``A``.
Stejně jako moduly zbavují své autory starostí s globálními názvy proměnných
jiných modulů, tečkované názvy zbavují autory vícemodulových balíčků, jako jsou
NumPy nebo Pillow, starostí s názvy modulů ostatních balíčků.

Předpokládejme, že chcete navrhnout kolekci modulů („balíček“) pro jednotné
zpracování zvukových souborů a dat. Existuje mnoho formátů zvukových souborů
(obvykle rozpoznaných podle přípony, například :file:`.wav`, :file:`.aiff`
a :file:`.au`), takže možná budete vytvářet a udržovat rostoucí kolekci modulů
pro převody mezi formáty. Se zvukovými daty lze také provádět řadu operací
(míchání, přidání ozvěny, ekvalizace či vytvoření umělého sterea), pro něž
budete psát další moduly. Možná struktura balíčku v hierarchickém souborovém
systému vypadá takto:

.. code-block:: text

   sound/                          Top-level package
         __init__.py               Initialize the sound package
         formats/                  Subpackage for file format conversions
                 __init__.py
                 wavread.py
                 wavwrite.py
                 aiffread.py
                 aiffwrite.py
                 auread.py
                 auwrite.py
                 ...
         effects/                  Subpackage for sound effects
                 __init__.py
                 echo.py
                 surround.py
                 reverse.py
                 ...
         filters/                  Subpackage for filters
                 __init__.py
                 equalizer.py
                 vocoder.py
                 karaoke.py
                 ...

Při importování balíčku Python prohledává adresáře uvedené v ``sys.path``
a hledá v nich podadresář balíčku.

Soubory :file:`__init__.py` jsou nezbytné, aby Python považoval adresáře,
které je obsahují, za balíčky (pokud se nepoužívá :term:`jmenný balíček
<namespace package>`, což je poměrně pokročilá funkce). Tím se zabrání tomu,
aby adresáře s běžným názvem, například ``string``, neúmyslně skryly platné
moduly, které se ve vyhledávací cestě modulů nacházejí později. V nejjednodušším
případě může být :file:`__init__.py` prázdný soubor, může však také provádět
inicializační kód balíčku nebo nastavit proměnnou ``__all__``, která je popsána
později.

Uživatelé balíčku mohou z balíčku importovat jednotlivé moduly, například::

   import sound.effects.echo

Tím se načte podmodul :mod:`!sound.effects.echo`. Odkazovat na něj je nutné jeho
úplným názvem. ::

   sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

Jiný způsob importování podmodulu je::

   from sound.effects import echo

Tím se také načte podmodul :mod:`!echo`, ale zpřístupní se bez prefixu balíčku,
takže jej lze použít následovně::

   echo.echofilter(input, output, delay=0.7, atten=4)

Další možností je importovat požadovanou funkci nebo proměnnou přímo::

   from sound.effects.echo import echofilter

Opět se tím načte podmodul :mod:`!echo`, tentokrát se však přímo zpřístupní jeho
funkce :func:`!echofilter`::

   echofilter(input, output, delay=0.7, atten=4)

Při použití ``from package import item`` může být položkou buď podmodul
(nebo podbalíček) daného balíčku, nebo jiný název definovaný v balíčku,
například funkce, třída či proměnná. Příkaz ``import`` nejprve ověří, zda je
položka definována v balíčku. Pokud není, předpokládá, že jde o modul, a pokusí
se jej načíst. Jestliže jej nenajde, vyvolá se výjimka :exc:`ImportError`.

Naproti tomu při použití syntaxe jako ``import item.subitem.subsubitem`` musí
být každá položka kromě poslední balíčkem. Poslední položkou může být modul nebo
balíček, nikoli však třída, funkce či proměnná definovaná v předchozí položce.


.. _tut-pkg-import-star:

Importování \* z balíčku
------------------------

.. index:: single: __all__

Co se stane, když uživatel napíše ``from sound.effects import *``? Ideálně by
se dalo očekávat, že Python nějak prohledá souborový systém, zjistí, které
podmoduly balíček obsahuje, a všechny je importuje. To by však mohlo trvat
dlouho a importování podmodulů by mohlo mít nežádoucí vedlejší účinky, které
mají nastat pouze při jejich výslovném importování.

Jediným řešením je, aby autor balíčku poskytl jeho explicitní seznam. Příkaz
:keyword:`import` používá následující konvenci: pokud kód souboru
:file:`__init__.py` daného balíčku definuje seznam s názvem ``__all__``, považuje
se tento seznam za seznam názvů modulů, které se mají importovat při použití
``from package import *``. Při vydání nové verze balíčku musí jeho autor tento
seznam udržovat aktuální. Autoři balíčků se také mohou rozhodnout, že tuto
možnost nebudou podporovat, pokud pro importování \* ze svého balíčku nevidí
využití. Soubor :file:`sound/effects/__init__.py` by například mohl obsahovat
následující kód::

   __all__ = ["echo", "surround", "reverse"]

To by znamenalo, že ``from sound.effects import *`` importuje tři uvedené
podmoduly balíčku :mod:`!sound.effects`.

Mějte na paměti, že podmoduly mohou být zastíněny lokálně definovanými názvy.
Pokud byste například do souboru :file:`sound/effects/__init__.py` přidali
funkci ``reverse``, příkaz ``from sound.effects import *`` by importoval pouze
dva podmoduly ``echo`` a ``surround``, ale *nikoli* podmodul ``reverse``, protože
jej zastiňuje lokálně definovaná funkce ``reverse``::

    __all__ = [
        "echo",      # refers to the 'echo.py' file
        "surround",  # refers to the 'surround.py' file
        "reverse",   # !!! refers to the 'reverse' function now !!!
    ]

    def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
        return msg[::-1]    #     in the case of a 'from sound.effects import *'

Pokud ``__all__`` není definováno, příkaz ``from sound.effects import *``
*neimportuje* všechny podmoduly balíčku :mod:`!sound.effects` do aktuálního
jmenného prostoru. Pouze zajistí, že byl balíček :mod:`!sound.effects`
importován (případně se přitom provede inicializační kód v
:file:`__init__.py`), a poté importuje všechny názvy definované v balíčku. Patří
sem všechny názvy definované souborem :file:`__init__.py` (a podmoduly, které
tento soubor výslovně načetl). Patří sem také všechny podmoduly balíčku, které
byly výslovně načteny předchozími příkazy :keyword:`import`. Uvažujme tento kód::

   import sound.effects.echo
   import sound.effects.surround
   from sound.effects import *

V tomto příkladu se moduly :mod:`!echo` a :mod:`!surround` importují do
aktuálního jmenného prostoru, protože jsou v okamžiku provedení příkazu
``from...import`` definovány v balíčku :mod:`!sound.effects`. (Funguje to také
tehdy, když je definováno ``__all__``.)

Přestože jsou některé moduly navrženy tak, aby při použití ``import *``
exportovaly pouze názvy odpovídající určitým vzorům, v produkčním kódu se tento
způsob stále považuje za nevhodný postup.

Pamatujte, že na použití ``from package import specific_submodule`` není nic
špatného! Ve skutečnosti jde o doporučený zápis, pokud importující modul
nepotřebuje používat stejně pojmenované podmoduly z různých balíčků.


.. _intra-package-references:

Odkazy uvnitř balíčku
---------------------

Pokud jsou balíčky uspořádány do podbalíčků (jako balíček :mod:`!sound` v tomto
příkladu), lze k odkazování na podmoduly souřadných balíčků používat absolutní
importy. Pokud například modul :mod:`!sound.filters.vocoder` potřebuje použít
modul :mod:`!echo` z balíčku :mod:`!sound.effects`, může použít ``from
sound.effects import echo``.

Pomocí tvaru příkazu ``from module import name`` lze zapisovat také relativní
importy. Tyto importy používají úvodní tečky k označení aktuálního a nadřazených
balíčků, kterých se relativní import týká. Například v modulu :mod:`!surround`
byste mohli použít::

   from . import echo
   from .. import formats
   from ..filters import equalizer

Relativní importy vycházejí z názvu balíčku aktuálního modulu. Protože hlavní
modul nemá balíček, moduly určené k použití jako hlavní modul aplikace v Pythonu
musí vždy používat absolutní importy.


Balíčky ve více adresářích
--------------------------

Balíčky podporují ještě jeden speciální atribut, :attr:`~module.__path__`.
Před provedením kódu v souboru :file:`__init__.py` balíčku se tento atribut
inicializuje jako :term:`sekvence <sequence>` řetězců obsahující název adresáře,
ve kterém se daný soubor nachází. Tuto proměnnou lze upravit; taková změna
ovlivní budoucí vyhledávání modulů a podbalíčků obsažených v balíčku.

Tato funkce není často zapotřebí, lze ji však použít k rozšíření množiny modulů
nalezených v balíčku.


.. rubric:: Poznámky pod čarou

.. [#] Definice funkcí jsou ve skutečnosti také „příkazy“, které se „provádějí“;
   provedení definice funkce na úrovni modulu přidá název funkce do globálního
   jmenného prostoru modulu.
