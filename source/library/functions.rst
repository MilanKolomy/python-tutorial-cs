.. XXX document all delegations to __special__ methods
.. _built-in-funcs:

Vestavěné funkce
================

Interpret Pythonu obsahuje řadu vestavěných funkcí a typů, které jsou vždy
dostupné. Zde jsou uvedeny v abecedním pořadí.

+---------------------------------------------------------------------------------------------------+
|                                        Vestavěné funkce                                           |
+=========================+=======================+=======================+=========================+
| |  **A**                | |  **E**              | |  **L**              | |  **R**                |
| |  :func:`abs`          | |  :func:`enumerate`  | |  :func:`len`        | |  |func-range|_        |
| |  :func:`aiter`        | |  :func:`eval`       | |  |func-list|_       | |  :func:`repr`         |
| |  :func:`all`          | |  :func:`exec`       | |  :func:`locals`     | |  :func:`reversed`     |
| |  :func:`anext`        | |                     | |                     | |  :func:`round`        |
| |  :func:`any`          | |  **F**              | |  **M**              | |                       |
| |  :func:`ascii`        | |  :func:`filter`     | |  :func:`map`        | |  **S**                |
| |                       | |  :func:`float`      | |  :func:`max`        | |  |func-set|_          |
| |  **B**                | |  :func:`format`     | |  |func-memoryview|_ | |  :func:`setattr`      |
| |  :func:`bin`          | |  |func-frozenset|_  | |  :func:`min`        | |  :func:`slice`        |
| |  :func:`bool`         | |                     | |                     | |  :func:`sorted`       |
| |  :func:`breakpoint`   | |  **G**              | |  **N**              | |  :func:`staticmethod` |
| |  |func-bytearray|_    | |  :func:`getattr`    | |  :func:`next`       | |  |func-str|_          |
| |  |func-bytes|_        | |  :func:`globals`    | |                     | |  :func:`sum`          |
| |                       | |                     | |  **O**              | |  :func:`super`        |
| |  **C**                | |  **H**              | |  :func:`object`     | |                       |
| |  :func:`callable`     | |  :func:`hasattr`    | |  :func:`oct`        | |  **T**                |
| |  :func:`chr`          | |  :func:`hash`       | |  :func:`open`       | |  |func-tuple|_        |
| |  :func:`classmethod`  | |  :func:`help`       | |  :func:`ord`        | |  :func:`type`         |
| |  :func:`compile`      | |  :func:`hex`        | |                     | |                       |
| |  :func:`complex`      | |                     | |  **P**              | |  **V**                |
| |                       | |  **I**              | |  :func:`pow`        | |  :func:`vars`         |
| |  **D**                | |  :func:`id`         | |  :func:`print`      | |                       |
| |  :func:`delattr`      | |  :func:`input`      | |  :func:`property`   | |  **Z**                |
| |  |func-dict|_         | |  :func:`int`        | |                     | |  :func:`zip`          |
| |  :func:`dir`          | |  :func:`isinstance` | |                     | |                       |
| |  :func:`divmod`       | |  :func:`issubclass` | |                     | |  **_**                |
| |                       | |  :func:`iter`       | |                     | |  :func:`__import__`   |
+-------------------------+-----------------------+-----------------------+-------------------------+

.. použití :func:`dict` by vytvořilo odkaz na jinou stránku, proto se používají
   místní cíle s náhradními texty, aby byl výstup v tabulce jednotný

.. |func-dict| replace:: ``dict()``
.. |func-frozenset| replace:: ``frozenset()``
.. |func-memoryview| replace:: ``memoryview()``
.. |func-set| replace:: ``set()``
.. |func-list| replace:: ``list()``
.. |func-str| replace:: ``str()``
.. |func-tuple| replace:: ``tuple()``
.. |func-range| replace:: ``range()``
.. |func-bytearray| replace:: ``bytearray()``
.. |func-bytes| replace:: ``bytes()``

.. function:: abs(number, /)

   Vrátí absolutní hodnotu čísla. Argumentem může být celé číslo, číslo
   s plovoucí řádovou čárkou nebo objekt implementující metodu
   :meth:`~object.__abs__`.
   Je-li argumentem komplexní číslo, vrátí se jeho velikost.


.. function:: aiter(async_iterable, /)

   Vrátí :term:`asynchronní iterátor <asynchronous iterator>` pro
   :term:`asynchronní iterovatelný objekt <asynchronous iterable>`.
   Odpovídá volání ``x.__aiter__()``.

   Poznámka: Na rozdíl od :func:`iter` nemá :func:`aiter` variantu se dvěma
   argumenty.

   .. versionadded:: 3.10

.. function:: all(iterable, /)

   Vrátí ``True``, pokud jsou všechny prvky *iterovatelného objektu* pravdivé
   (nebo pokud je iterovatelný objekt prázdný). Odpovídá zápisu::

      def all(iterable):
          for element in iterable:
              if not element:
                  return False
          return True


.. awaitablefunction:: anext(async_iterator, /)
                       anext(async_iterator, default, /)

   Při vyhodnocení vrátí další položku zadaného
   :term:`asynchronního iterátoru <asynchronous iterator>`, případně hodnotu
   *default*, pokud byla zadána a iterátor je vyčerpán.

   Jde o asynchronní variantu vestavěné funkce :func:`next`, která se chová
   obdobně.

   Funkce zavolá metodu :meth:`~object.__anext__` objektu *async_iterator*,
   která vrátí :term:`awaitable objekt <awaitable>`. Jeho vyhodnocení poskytne
   další hodnotu iterátoru. Je-li zadána hodnota *default*, vrátí se
   při vyčerpání iterátoru; jinak se vyvolá výjimka
   :exc:`StopAsyncIteration`.

   .. versionadded:: 3.10

.. function:: any(iterable, /)

   Vrátí ``True``, pokud je alespoň jeden prvek *iterovatelného objektu*
   pravdivý. Je-li iterovatelný objekt prázdný, vrátí ``False``. Odpovídá
   zápisu::

      def any(iterable):
          for element in iterable:
              if element:
                  return True
          return False


.. function:: ascii(object, /)

   Podobně jako :func:`repr` vrátí řetězec obsahující tisknutelnou reprezentaci
   objektu, znaky mimo ASCII však v řetězci vráceném funkcí :func:`repr`
   escapuje pomocí sekvencí ``\x``, ``\u`` nebo ``\U``. Vytvoří tak řetězec
   podobný výsledku funkce :func:`repr` v Pythonu 2.


.. function:: bin(integer, /)

   Převede celé číslo na binární řetězec s prefixem "0b". Výsledkem je platný
   výraz Pythonu. Není-li *integer* objektem třídy :class:`int`, musí definovat
   metodu :meth:`~object.__index__`, která vrací celé číslo. Několik příkladů:

      >>> bin(3)
      '0b11'
      >>> bin(-10)
      '-0b1010'

   Podle toho, zda chcete prefix "0b" zahrnout, můžete použít některý
   z následujících způsobů.

      >>> format(14, '#b'), format(14, 'b')
      ('0b1110', '1110')
      >>> f'{14:#b}', f'{14:b}'
      ('0b1110', '1110')

   Reprezentaci záporných hodnot pomocí dvojkového doplňku nabízí také
   :func:`enum.bin`.

   Další informace najdete také u funkce :func:`format`.


.. class:: bool(object=False, /)

   Vrátí booleovskou hodnotu, tedy ``True`` nebo ``False``. Argument se převede
   pomocí standardního :ref:`vyhodnocení pravdivosti <truth>`. Je-li argument
   nepravdivý nebo vynechaný, vrátí ``False``; jinak vrátí ``True``. Třída
   :class:`bool` je podtřídou :class:`int` (viz :ref:`typesnumeric`) a nelze ji
   dále odvozovat. Jejími jedinými instancemi jsou ``False`` a ``True``
   (viz :ref:`typebool`).

   .. index:: pair: booleovská hodnota; typ

   .. versionchanged:: 3.7
      Parametr je nyní pouze poziční.

.. function:: breakpoint(*args, **kws)

   Tato funkce v místě volání spustí debugger. Konkrétně zavolá
   :func:`sys.breakpointhook` a přímo mu předá ``args`` a ``kws``. Ve výchozím
   nastavení volá ``sys.breakpointhook()`` funkci :func:`pdb.set_trace`, která
   neočekává žádné argumenty. V takovém případě jde čistě o usnadnění práce,
   díky němuž nemusíte explicitně importovat :mod:`pdb` ani psát tolik kódu pro
   vstup do debuggeru. :func:`sys.breakpointhook` však lze nastavit na jinou
   funkci a :func:`breakpoint` ji automaticky zavolá, takže můžete vstoupit do
   zvoleného debuggeru.
   Není-li :func:`sys.breakpointhook` dostupná, funkce vyvolá
   :exc:`RuntimeError`.

   Výchozí chování funkce :func:`breakpoint` lze změnit proměnnou prostředí
   :envvar:`PYTHONBREAKPOINT`.
   Podrobnosti o použití najdete u :func:`sys.breakpointhook`.

   Pokud byla :func:`sys.breakpointhook` nahrazena, není toto chování zaručeno.

   .. audit-event:: builtins.breakpoint breakpointhook breakpoint

   .. versionadded:: 3.7

.. _func-bytearray:
.. class:: bytearray(source=b'')
           bytearray(source, encoding, errors='strict')
   :noindex:

   Vrátí nové pole bajtů. Třída :class:`bytearray` je měnitelná sekvence celých
   čísel v rozsahu 0 <= x < 256. Poskytuje většinu obvyklých metod měnitelných
   sekvencí popsaných v :ref:`typesseq-mutable` a také většinu metod typu
   :class:`bytes`, viz :ref:`bytes-methods`.

   Nepovinným parametrem *source* lze pole inicializovat několika způsoby:

   * Jde-li o *řetězec*, musíte zadat také parametr *encoding* (a volitelně
     *errors*); :func:`bytearray` poté řetězec převede na bajty pomocí
     :meth:`str.encode`.

   * Jde-li o *celé číslo*, pole bude mít zadanou velikost a inicializuje se
     nulovými bajty.

   * Jde-li o objekt vyhovující :ref:`rozhraní bufferu <bufferobjects>`, použije
     se k inicializaci pole bajtů buffer objektu určený pouze pro čtení.

   * Jde-li o *iterovatelný objekt*, musí poskytovat celá čísla v rozsahu
     ``0 <= x < 256``, která se použijí jako počáteční obsah pole.

   Bez argumentu se vytvoří pole o velikosti 0.

   Viz také :ref:`binaryseq` a :ref:`typebytearray`.


.. _func-bytes:
.. class:: bytes(source=b'')
           bytes(source, encoding, errors='strict')
   :noindex:

   Vrátí nový objekt "bytes", který je neměnnou sekvencí celých čísel v rozsahu
   ``0 <= x < 256``. :class:`bytes` je neměnnou variantou :class:`bytearray` —
   má stejné metody, které objekt nemění, a stejné chování při indexování
   a vytváření výřezů.

   Argumenty konstruktoru se proto interpretují stejně jako u
   :func:`bytearray`.

   Objekty bytes lze vytvářet také pomocí literálů, viz :ref:`strings`.

   Viz také :ref:`binaryseq`, :ref:`typebytes` a :ref:`bytes-methods`.


.. function:: callable(object, /)

   Vrátí :const:`True`, pokud se argument *object* jeví jako volatelný, jinak
   :const:`False`. Vrátí-li funkce ``True``, může volání přesto selhat; vrátí-li
   však ``False``, volání objektu *object* nikdy neuspěje. Třídy jsou volatelné
   (volání třídy vrátí novou instanci); instance jsou volatelné, pokud jejich
   třída obsahuje metodu :meth:`~object.__call__`.

   .. versionadded:: 3.2
      Funkce byla nejprve v Pythonu 3.0 odstraněna a v Pythonu 3.2 znovu
      přidána.


.. function:: chr(codepoint, /)

   Vrátí řetězec představující znak se zadaným kódovým bodem Unicode.
   Například ``chr(97)`` vrátí řetězec ``'a'``, zatímco ``chr(8364)`` vrátí
   řetězec ``'€'``. Jde o inverzní funkci k :func:`ord`.

   Platný rozsah argumentu je od 0 do 1 114 111 (0x10FFFF v šestnáctkové
   soustavě). Hodnota mimo tento rozsah vyvolá :exc:`ValueError`.


.. decorator:: classmethod

   Převede metodu na metodu třídy.

   Metoda třídy přijímá třídu jako implicitní první argument, podobně jako
   instanční metoda přijímá instanci. Metodu třídy deklarujete tímto zápisem::

      class C:
          @classmethod
          def f(cls, arg1, arg2): ...

   Zápis ``@classmethod`` je :term:`dekorátor <decorator>` funkce — podrobnosti
   najdete v :ref:`function`.

   Metodu třídy lze volat na třídě (například ``C.f()``) i na instanci
   (například ``C().f()``). Instance se kromě určení její třídy ignoruje. Je-li
   metoda třídy volána pro odvozenou třídu, předá se objekt odvozené třídy jako
   implicitní první argument.

   Metody třídy se liší od statických metod v C++ nebo Javě. Pokud potřebujete
   statickou metodu, viz :func:`staticmethod` v této části.
   Další informace o metodách třídy najdete v :ref:`types`.

   .. versionchanged:: 3.9
      Metody třídy nyní mohou obalovat jiné
      :term:`deskriptory <descriptor>`, například :func:`property`.

   .. versionchanged:: 3.10
      Metody třídy nyní přebírají atributy metody
      (:attr:`~function.__module__`, :attr:`~function.__name__`,
      :attr:`~function.__qualname__`, :attr:`~function.__doc__` a
      :attr:`~function.__annotations__`) a mají nový atribut ``__wrapped__``.

   .. deprecated-removed:: 3.11 3.13
      Metody třídy již nemohou obalovat jiné
      :term:`deskriptory <descriptor>`, například :func:`property`.


.. function:: compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

   Zkompiluje *source* do objektu kódu nebo AST. Objekty kódu lze spustit pomocí
   :func:`exec` nebo :func:`eval`. *source* může být běžný řetězec, bajtový
   řetězec nebo objekt AST. Informace o práci s objekty AST najdete v dokumentaci
   modulu :mod:`ast`.

   Argument *filename* by měl určovat soubor, ze kterého byl kód načten. Pokud
   nebyl načten ze souboru, předejte nějakou rozpoznatelnou hodnotu (běžně se
   používá ``'<string>'``).

   Argument *mode* určuje druh kompilovaného kódu. Může mít hodnotu ``'exec'``,
   pokud *source* tvoří posloupnost příkazů, ``'eval'``, pokud jej tvoří jediný
   výraz, nebo ``'single'``, pokud jej tvoří jediný interaktivní příkaz
   (v posledním případě se vypíší příkazy výrazů, jejichž výsledkem není
   ``None``).

   Nepovinné argumenty *flags* a *dont_inherit* určují, které
   :ref:`volby kompilátoru <ast-compiler-flags>` se aktivují a které
   :ref:`budoucí vlastnosti <future>` se povolí. Není-li zadán ani jeden z nich
   (nebo jsou oba nulové), kód se zkompiluje se stejnými příznaky, které působí
   na kód volající :func:`compile`. Je-li zadán argument *flags* a *dont_inherit*
   zadán není (nebo je nulový), použijí se volby kompilátoru a příkazy future
   určené argumentem *flags* navíc k těm, které by se použily tak jako tak.
   Je-li *dont_inherit* nenulové celé číslo, použije se výhradně argument
   *flags* — příznaky okolního kódu (budoucí vlastnosti a volby kompilátoru) se
   ignorují.

   Volby kompilátoru a příkazy future se určují bity, které lze bitově spojovat
   operátorem OR a zadat tak více voleb. Bitové pole potřebné pro konkrétní
   budoucí vlastnost najdete v atributu
   :attr:`~__future__._Feature.compiler_flag` instance
   :class:`~__future__._Feature` v modulu :mod:`__future__`.
   :ref:`Příznaky kompilátoru <ast-compiler-flags>` s prefixem ``PyCF_``
   najdete v modulu :mod:`ast`.

   Argument *optimize* určuje úroveň optimalizace kompilátoru. Výchozí hodnota
   ``-1`` vybere úroveň optimalizace interpretu danou volbami :option:`-O`.
   Explicitní úrovně jsou ``0`` (bez optimalizace; ``__debug__`` je pravdivé),
   ``1`` (příkazy assert se odstraní a ``__debug__`` je nepravdivé) nebo ``2``
   (odstraní se také dokumentační řetězce).

   Pokud kompilovaný zdroj není platný, funkce vyvolá :exc:`SyntaxError` nebo
   :exc:`ValueError`.

   Chcete-li kód Pythonu zpracovat do reprezentace AST, viz :func:`ast.parse`.

   .. audit-event:: compile source,filename compile

      Vyvolá :ref:`auditní událost <auditing>` ``compile`` s argumenty
      ``source`` a ``filename``. Tuto událost může vyvolat také implicitní
      kompilace.

   .. note::

      Při kompilaci řetězce s víceřádkovým kódem v režimu ``'single'`` nebo
      ``'eval'`` musí být vstup ukončen alespoň jedním znakem nového řádku.
      Usnadňuje to rozpoznávání neúplných a úplných příkazů v modulu
      :mod:`code`.

   .. warning::

      Při kompilaci dostatečně velkého nebo složitého řetězce do objektu AST
      může kvůli omezené hloubce zásobníku kompilátoru AST dojít k pádu
      interpretu Pythonu.

   .. versionchanged:: 3.2
      Bylo povoleno použití znaků konce řádku Windows a Mac. Vstup v režimu
      ``'exec'`` již také nemusí končit novým řádkem. Byl přidán parametr
      *optimize*.

   .. versionchanged:: 3.5
      Při výskytu nulových bajtů ve *source* se dříve vyvolala
      :exc:`TypeError`.

   .. versionadded:: 3.8
      V příznacích lze nyní předat ``ast.PyCF_ALLOW_TOP_LEVEL_AWAIT`` a povolit
      tak podporu ``await``, ``async for`` a ``async with`` na nejvyšší úrovni.


.. class:: complex(number=0, /)
           complex(string, /)
           complex(real=0, imag=0)

   Převede jeden řetězec nebo číslo na komplexní číslo, případně vytvoří
   komplexní číslo z reálné a imaginární části.

   Příklady:

   .. doctest::

      >>> complex('+1.23')
      (1.23+0j)
      >>> complex('-4.5j')
      -4.5j
      >>> complex('-1.23+4.5j')
      (-1.23+4.5j)
      >>> complex('\t( -1.23+4.5J )\n')
      (-1.23+4.5j)
      >>> complex('-Infinity+NaNj')
      (-inf+nanj)
      >>> complex(1.23)
      (1.23+0j)
      >>> complex(imag=-4.5)
      -4.5j
      >>> complex(-1.23, 4.5)
      (-1.23+4.5j)

   Je-li argumentem řetězec, musí obsahovat buď reálnou část (ve stejném
   formátu jako u :func:`float`), nebo imaginární část (ve stejném formátu,
   avšak s příponou ``'j'`` či ``'J'``), případně reálnou i imaginární část
   (v tomto případě je znaménko imaginární části povinné).
   Řetězec může být obklopen prázdnými znaky a kulatými závorkami ``'('``
   a ``')'``, které se ignorují.
   Řetězec nesmí obsahovat prázdné znaky mezi ``'+'``, ``'-'``, příponou
   ``'j'`` nebo ``'J'`` a desetinným číslem.
   Například ``complex('1+2j')`` je platné, ale ``complex('1 + 2j')`` vyvolá
   :exc:`ValueError`.
   Přesněji řečeno musí vstup po odstranění závorek a úvodních i koncových
   prázdných znaků odpovídat syntaktickému pravidlu
   :token:`~float:complexvalue` v následující gramatice:

   .. productionlist:: float
      complexvalue: `floatvalue` |
                  : `floatvalue` ("j" | "J") |
                  : `floatvalue` `sign` `absfloatvalue` ("j" | "J")

   Je-li argumentem číslo, slouží konstruktor k číselnému převodu podobně jako
   :class:`int` a :class:`float`.
   U obecného objektu Pythonu ``x`` deleguje ``complex(x)`` na
   ``x.__complex__()``.
   Není-li definována :meth:`~object.__complex__`, použije se
   :meth:`~object.__float__`.
   Není-li definována ani :meth:`!__float__`, použije se
   :meth:`~object.__index__`.

   Jsou-li zadány dva argumenty nebo použity argumenty klíčových slov, může být
   každý argument libovolného číselného typu (včetně komplexního).
   Jsou-li oba argumenty reálná čísla, vrátí komplexní číslo s reálnou složkou
   *real* a imaginární složkou *imag*.
   Jsou-li oba argumenty komplexní čísla, vrátí komplexní číslo s reálnou
   složkou ``real.real-imag.imag`` a imaginární složkou
   ``real.imag+imag.real``.
   Je-li jeden z argumentů reálné číslo, použije se ve výše uvedených výrazech
   pouze jeho reálná složka.

   Viz také :meth:`complex.from_number`, která přijímá pouze jeden číselný
   argument.

   Jsou-li všechny argumenty vynechány, vrátí ``0j``.

   Komplexní typ je popsán v :ref:`typesnumeric`.

   .. versionchanged:: 3.6
      Je povoleno seskupování číslic pomocí podtržítek stejně jako v číselných
      literálech.

   .. versionchanged:: 3.8
      Na :meth:`~object.__index__` se přejde, nejsou-li definovány
      :meth:`~object.__complex__` ani :meth:`~object.__float__`.

   .. deprecated:: 3.14
      Předávání komplexního čísla jako argumentu *real* nebo *imag* je nyní
      zastaralé; mělo by se předávat pouze jako jediný poziční argument.


.. function:: delattr(object, name, /)

   Tato funkce je příbuzná s :func:`setattr`. Argumenty jsou objekt a řetězec.
   Řetězec musí být názvem jednoho z atributů objektu. Pokud to objekt dovoluje,
   funkce pojmenovaný atribut odstraní. Například ``delattr(x, 'foobar')``
   odpovídá zápisu ``del x.foobar``. *name* nemusí být identifikátorem Pythonu
   (viz :func:`setattr`).


.. _func-dict:
.. class:: dict(**kwargs)
           dict(mapping, /, **kwargs)
           dict(iterable, /, **kwargs)
   :noindex:

   Vytvoří nový slovník. Objekt :class:`dict` je třídou slovníku. Dokumentaci
   této třídy najdete u :class:`dict` a v :ref:`typesmapping`.

   Další kontejnery popisují vestavěné třídy :class:`list`, :class:`set`
   a :class:`tuple` a také modul :mod:`collections`.


.. function:: dir()
              dir(object, /)

   Bez argumentu vrátí seznam názvů v aktuálním lokálním oboru platnosti.
   S argumentem se pokusí vrátit seznam platných atributů daného objektu.

   Má-li objekt metodu :meth:`~object.__dir__`, tato metoda se zavolá a musí
   vrátit seznam atributů. Objekty implementující vlastní funkci
   :func:`~object.__getattr__` nebo :func:`~object.__getattribute__` tak mohou
   přizpůsobit způsob, jakým :func:`dir` vypisuje jejich atributy.

   Neposkytuje-li objekt :meth:`~object.__dir__`, pokusí se funkce co nejlépe
   shromáždit informace z atributu objektu :attr:`~object.__dict__`, je-li
   definován, a z objektu jeho typu. Výsledný seznam nemusí být úplný a může být
   nepřesný, pokud má objekt vlastní :func:`~object.__getattr__`.

   Výchozí mechanismus :func:`dir` se u různých typů objektů chová odlišně,
   protože se snaží poskytnout spíše nejrelevantnější než úplné informace:

   * Je-li objekt modulem, seznam obsahuje názvy atributů modulu.

   * Je-li objekt typem nebo třídou, seznam obsahuje názvy jeho atributů
     a rekurzivně také atributů jeho bází.

   * V ostatních případech seznam obsahuje názvy atributů objektu, názvy atributů
     jeho třídy a rekurzivně také atributů bázových tříd jeho třídy.

   Výsledný seznam je seřazen abecedně. Například:

      >>> import struct
      >>> dir()   # show the names in the module namespace  # doctest: +SKIP
      ['__builtins__', '__name__', 'struct']
      >>> dir(struct)   # show the names in the struct module # doctest: +SKIP
      ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
       '__initializing__', '__loader__', '__name__', '__package__',
       '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
       'unpack', 'unpack_from']
      >>> class Shape:
      ...     def __dir__(self):
      ...         return ['area', 'perimeter', 'location']
      ...
      >>> s = Shape()
      >>> dir(s)
      ['area', 'location', 'perimeter']

   .. note::

      Protože je :func:`dir` určena především pro pohodlné použití na
      interaktivní výzvě, snaží se spíše poskytnout zajímavou množinu názvů než
      přesně a konzistentně definovanou množinu. Její podrobné chování se proto
      může mezi vydáními měnit. Pokud je například argumentem třída, nejsou ve
      výsledném seznamu atributy metatřídy.


.. function:: divmod(a, b, /)

   Přijme dvě čísla (nikoli komplexní) a vrátí dvojici čísel tvořenou jejich
   podílem a zbytkem při celočíselném dělení. U smíšených typů operandů platí
   pravidla binárních aritmetických operátorů. Pro celá čísla je výsledek stejný
   jako ``(a // b, a % b)``. Pro čísla s plovoucí řádovou čárkou je výsledkem
   ``(q, a % b)``, kde *q* obvykle odpovídá ``math.floor(a /
   b)``, může však být
   o 1 menší. V každém případě je ``q * b + a % b`` velmi blízko *a*; je-li
   ``a % b`` nenulové, má stejné znaménko jako *b* a platí ``0
   <= abs(a % b) < abs(b)``.


.. function:: enumerate(iterable, start=0)

   Vrátí objekt enumerate. *iterable* musí být sekvence,
   :term:`iterátor <iterator>` nebo jiný objekt podporující iteraci. Metoda
   :meth:`~iterator.__next__` iterátoru vráceného funkcí :func:`enumerate`
   poskytuje n-tici obsahující pořadové číslo (od hodnoty *start*, jejíž výchozí
   hodnota je 0) a hodnotu získanou iterací přes *iterable*.

      >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
      >>> list(enumerate(seasons))
      [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
      >>> list(enumerate(seasons, start=1))
      [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

   Odpovídá zápisu::

      def enumerate(iterable, start=0):
          n = start
          for elem in iterable:
              yield n, elem
              n += 1

.. _func-eval:

.. function:: eval(source, /, globals=None, locals=None)

   :param source:
      Výraz Pythonu.
   :type source: :class:`str` | :ref:`code object <code-objects>`

   :param globals:
      Globální jmenný prostor (výchozí hodnota: ``None``).
   :type globals: :class:`dict` | ``None``

   :param locals:
      Lokální jmenný prostor (výchozí hodnota: ``None``).
   :type locals: :term:`mapping` | ``None``

   :returns: Výsledek vyhodnoceného výrazu.
   :raises: Syntaktické chyby se oznamují jako výjimky.

   .. warning::

      Tato funkce spouští libovolný kód. Její volání s nedůvěryhodným vstupem
      poskytnutým uživatelem vede k bezpečnostním zranitelnostem.

   Argument *source* se zpracuje a vyhodnotí jako výraz Pythonu (technicky jako
   seznam podmínek), přičemž mapování *globals* a *locals* slouží jako globální
   a lokální jmenný prostor. Je-li zadán slovník *globals* a neobsahuje hodnotu
   pro klíč ``__builtins__``, vloží se pod tento klíč před zpracováním *source*
   odkaz na slovník vestavěného modulu :mod:`builtins`.
   Přepsáním ``__builtins__`` lze omezit nebo změnit dostupné názvy, **nejde**
   však o bezpečnostní mechanismus: spuštěný kód má stále přístup ke všem
   vestavěným objektům.
   Je-li mapování *locals* vynecháno, použije se jako výchozí slovník *globals*.
   Jsou-li obě mapování vynechána, zdroj se spustí s hodnotami *globals*
   a *locals* prostředí, ve kterém se volá :func:`eval`. Pozor, *eval()* bude mít
   přístup k :term:`vnořeným oborům platnosti <nested scope>` (nelokálním
   názvům) okolního prostředí pouze tehdy, pokud se na ně již odkazuje obor
   platnosti volající :func:`eval` (například prostřednictvím příkazu
   :keyword:`nonlocal`).

   Příklad:

      >>> x = 1
      >>> eval('x+1')
      2

   Funkci lze použít také ke spuštění libovolných objektů kódu (například
   vytvořených funkcí :func:`compile`). V takovém případě předejte místo řetězce
   objekt kódu. Pokud byl objekt kódu zkompilován s argumentem *mode* nastaveným
   na ``'exec'``, bude návratovou hodnotou :func:`eval` hodnota ``None``.

   Tip: Dynamické spouštění příkazů podporuje funkce :func:`exec`. Funkce
   :func:`globals` a :func:`locals` vracejí aktuální globální, respektive
   lokální slovník, které lze předávat pro použití funkcemi :func:`eval` nebo
   :func:`exec`.

   Je-li zadaný zdroj řetězcem, odstraní se z něj úvodní a koncové mezery
   a tabulátory.

   Funkci pro vyhodnocování řetězců s výrazy obsahujícími pouze literály nabízí
   :func:`ast.literal_eval`.

   .. audit-event:: exec code_object eval

      Vyvolá :ref:`auditní událost <auditing>` ``exec`` s objektem kódu jako
      argumentem. Mohou se vyvolat také události kompilace kódu.

   .. versionchanged:: 3.13

      Argumenty *globals* a *locals* lze nyní předávat jako klíčová slova.

   .. versionchanged:: 3.13

      Sémantika výchozího jmenného prostoru *locals* byla upravena podle popisu
      vestavěné funkce :func:`locals`.

.. index:: pair: vestavěná funkce; exec

.. function:: exec(source, /, globals=None, locals=None, *, closure=None)

   .. warning::

      Tato funkce spouští libovolný kód. Její volání s nedůvěryhodným vstupem
      poskytnutým uživatelem vede k bezpečnostním zranitelnostem.

   Tato funkce podporuje dynamické spouštění kódu Pythonu. *source* musí být
   řetězec nebo objekt kódu. Jde-li o řetězec, zpracuje se jako blok příkazů
   Pythonu, který se následně spustí (pokud nedojde k syntaktické chybě). [#]_
   Jde-li o objekt kódu, jednoduše se spustí. Spouštěný kód musí být ve všech
   případech platný jako vstup ze souboru (viz část :ref:`file-input`
   v Referenční příručce). Pamatujte, že příkazy :keyword:`nonlocal`,
   :keyword:`yield` a :keyword:`return` nelze použít mimo definice funkcí ani
   v kódu předaném funkci :func:`exec`. Návratovou hodnotou je ``None``.

   Jsou-li nepovinné části vynechány, spustí se kód ve všech případech
   v aktuálním oboru platnosti. Je-li zadáno pouze *globals*, musí jít o slovník
   (nikoli podtřídu slovníku), který se použije pro globální i lokální proměnné.
   Jsou-li zadány *globals* i *locals*, použijí se pro globální, respektive
   lokální proměnné. Zadané *locals* může být libovolný mapovací objekt.
   Pamatujte, že na úrovni modulu jsou globals a locals stejným slovníkem.

   .. note::

      Obdrží-li ``exec`` dva samostatné objekty *globals* a *locals*, spustí se
      kód tak, jako by byl vložen do definice třídy. Funkce a třídy definované
      ve spuštěném kódu proto nebudou mít přístup k proměnným přiřazeným na
      nejvyšší úrovni (protože se s proměnnými „nejvyšší úrovně“ zachází jako
      s proměnnými třídy v její definici).

   Neobsahuje-li slovník *globals* hodnotu pro klíč ``__builtins__``, vloží se
   pod něj odkaz na slovník vestavěného modulu :mod:`builtins`.
   Přepsáním ``__builtins__`` lze omezit nebo změnit dostupné názvy, **nejde**
   však o bezpečnostní mechanismus: spuštěný kód má stále přístup ke všem
   vestavěným objektům.

   Argument *closure* určuje uzávěr — n-tici buněčných proměnných. Je platný
   pouze tehdy, když je *object* objektem kódu obsahujícím
   :term:`volné proměnné uzávěru <closure variable>`. Délka n-tice musí přesně
   odpovídat délce atributu :attr:`~codeobject.co_freevars` objektu kódu.

   .. audit-event:: exec code_object exec

      Vyvolá :ref:`auditní událost <auditing>` ``exec`` s objektem kódu jako
      argumentem. Mohou se vyvolat také události kompilace kódu.

   .. note::

      Vestavěné funkce :func:`globals` a :func:`locals` vracejí aktuální globální,
      respektive lokální jmenný prostor. Lze je proto předat jako druhý a třetí
      argument funkce :func:`exec`.

   .. note::

      Výchozí *locals* se chová podle popisu funkce :func:`locals` níže.
      Potřebujete-li po návratu funkce :func:`exec` pozorovat účinky kódu na
      *locals*, předejte explicitní slovník *locals*.

   .. versionchanged:: 3.11
      Byl přidán parametr *closure*.

   .. versionchanged:: 3.13

      Argumenty *globals* a *locals* lze nyní předávat jako klíčová slova.

   .. versionchanged:: 3.13

      Sémantika výchozího jmenného prostoru *locals* byla upravena podle popisu
      vestavěné funkce :func:`locals`.


.. function:: filter(function, iterable, /)

   Vytvoří iterátor z těch prvků objektu *iterable*, pro něž je *function*
   pravdivá. *iterable* může být sekvence, kontejner podporující iteraci nebo
   iterátor. Je-li *function* rovna ``None``, předpokládá se identická funkce,
   takže se odstraní všechny nepravdivé prvky objektu *iterable*.

   ``filter(function, iterable)`` je ekvivalentní generátorovému výrazu
   ``(item for item in iterable if function(item))``, není-li function rovna
   ``None``, a výrazu ``(item for item in iterable if item)``, je-li function
   rovna ``None``.

   Doplňkovou funkci vracející prvky objektu *iterable*, pro něž je *function*
   nepravdivá, popisuje :func:`itertools.filterfalse`.


.. class:: float(number=0.0, /)
           float(string, /)

   .. index::
      single: NaN
      single: Infinity

   Vrátí číslo s plovoucí řádovou čárkou vytvořené z čísla nebo řetězce.

   Příklady:

   .. doctest::

      >>> float('+1.23')
      1.23
      >>> float('   -12345\n')
      -12345.0
      >>> float('1e-003')
      0.001
      >>> float('+1E6')
      1000000.0
      >>> float('-Infinity')
      -inf

   Je-li argument řetězec, měl by obsahovat desetinné číslo, jemuž může
   předcházet znaménko a které může být obklopeno bílými znaky. Volitelné
   znaménko může být ``'+'`` nebo ``'-'``; znaménko ``'+'`` nemá na výslednou
   hodnotu žádný vliv. Argument může být také řetězec představující NaN
   (není číslo) nebo kladné či záporné nekonečno. Přesněji řečeno musí vstup po
   odstranění počátečních a koncových bílých znaků odpovídat produkčnímu
   pravidlu :token:`~float:floatvalue` v následující gramatice:

   .. productionlist:: float
      sign: "+" | "-"
      infinity: "Infinity" | "inf"
      nan: "nan"
      digit: <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
      digitpart: `digit` (["_"] `digit`)*
      number: [`digitpart`] "." `digitpart` | `digitpart` ["."]
      exponent: ("e" | "E") [`sign`] `digitpart`
      floatnumber: `number` [`exponent`]
      absfloatvalue: `floatnumber` | `infinity` | `nan`
      floatvalue: [`sign`] `absfloatvalue`

   Na velikosti písmen nezáleží, takže například "inf", "Inf", "INFINITY" a
   "iNfINity" jsou všechno přípustné zápisy kladného nekonečna.

   Je-li argument celé číslo nebo číslo s plovoucí řádovou čárkou, vrátí se
   číslo s plovoucí řádovou čárkou se stejnou hodnotou (v rámci přesnosti
   čísel s plovoucí řádovou čárkou v Pythonu). Leží-li argument mimo rozsah
   typu float v Pythonu, vyvolá se :exc:`OverflowError`.

   U obecného objektu Pythonu ``x`` deleguje ``float(x)`` na
   ``x.__float__()``. Není-li definována :meth:`~object.__float__`, použije se
   :meth:`~object.__index__`.

   Viz také :meth:`float.from_number`, která přijímá pouze číselný argument.

   Není-li zadán žádný argument, vrátí se ``0.0``.

   Typ float popisuje oddíl :ref:`typesnumeric`.

   .. versionchanged:: 3.6
      Je povoleno seskupovat číslice podtržítky stejně jako v literálech kódu.

   .. versionchanged:: 3.7
      Parametr je nyní pouze poziční.

   .. versionchanged:: 3.8
      Na :meth:`~object.__index__` se přejde, není-li definována
      :meth:`~object.__float__`.


.. index::
   single: __format__
   single: string; format() (built-in function)

.. function:: format(value, format_spec="", /)

   Převede *value* na „formátovanou“ reprezentaci řízenou parametrem
   *format_spec*. Interpretace *format_spec* závisí na typu argumentu *value*;
   většina vestavěných typů však používá standardní syntaxi formátování:
   :ref:`formatspec`.

   Výchozí *format_spec* je prázdný řetězec, který má obvykle stejný účinek jako
   volání :func:`str(value) <str>`.

   Volání ``format(value, format_spec)`` se převede na
   ``type(value).__format__(value, format_spec)``, čímž se při hledání metody
   :meth:`~object.__format__` hodnoty obejde slovník instance.
   Výjimka :exc:`TypeError` se vyvolá, pokud hledání metody dospěje k
   :mod:`object` a *format_spec* není prázdný, nebo pokud *format_spec* či
   návratová hodnota nejsou řetězce.

   .. versionchanged:: 3.4
      ``object().__format__(format_spec)`` vyvolá :exc:`TypeError`, pokud
      *format_spec* není prázdný řetězec.


.. _func-frozenset:
.. class:: frozenset(iterable=(), /)
   :noindex:

   Vrátí nový objekt :class:`frozenset`, volitelně s prvky převzatými z
   *iterable*. ``frozenset`` je vestavěná třída. Dokumentaci této třídy uvádějí
   :class:`frozenset` a :ref:`types-set`.

   Další kontejnery popisují vestavěné třídy :class:`set`, :class:`list`,
   :class:`tuple` a :class:`dict` i modul :mod:`collections`.


.. function:: getattr(object, name, /)
              getattr(object, name, default, /)

   Vrátí hodnotu pojmenovaného atributu objektu *object*. *name* musí být
   řetězec. Je-li řetězec názvem některého atributu objektu, výsledkem je
   hodnota tohoto atributu. Například ``getattr(x, 'foobar')`` je ekvivalentní
   výrazu ``x.foobar``. Pokud pojmenovaný atribut neexistuje, vrátí se zadaná
   hodnota *default*, jinak se vyvolá :exc:`AttributeError`.
   *name* nemusí být identifikátor Pythonu (viz :func:`setattr`).

   .. note::

      Protože k :ref:`komolení soukromých názvů <private-name-mangling>` dochází
      při kompilaci, je nutné název soukromého atributu (atributu se dvěma
      počátečními podtržítky) pro získání pomocí :func:`getattr` zkomolit ručně.


.. function:: globals()

   Vrátí slovník implementující jmenný prostor aktuálního modulu. Pro kód uvnitř
   funkcí se tento prostor určí při definici funkce a zůstává stejný bez ohledu
   na to, odkud se funkce volá.


.. function:: hasattr(object, name, /)

   Argumenty jsou objekt a řetězec. Výsledkem je ``True``, pokud je řetězec
   názvem některého atributu objektu, jinak ``False``. (Implementace volá
   ``getattr(object, name)`` a zjišťuje, zda vyvolá :exc:`AttributeError`.)


.. function:: hash(object, /)

   Vrátí hodnotu otisku objektu (pokud ji má). Hodnoty otisku jsou celá čísla.
   Používají se k rychlému porovnávání klíčů při vyhledávání ve slovníku.
   Číselné hodnoty, které se porovnají jako shodné, mají stejnou hodnotu otisku
   (i když jsou různých typů, jako například 1 a 1.0).

   .. note::

      U objektů s vlastní metodou :meth:`~object.__hash__` mějte na paměti, že
      :func:`hash` zkrátí návratovou hodnotu podle bitové šířky hostitelského
      počítače.

.. function:: help()
              help(request)

   Spustí vestavěný systém nápovědy. (Tato funkce je určena k interaktivnímu
   použití.) Není-li zadán argument, spustí se interaktivní nápověda v konzoli
   interpretu. Je-li argument řetězec, vyhledá se jako název modulu, funkce,
   třídy, metody, klíčového slova nebo tématu dokumentace a v konzoli se vypíše
   stránka nápovědy. U argumentu jakéhokoli jiného druhu se vytvoří stránka
   nápovědy k danému objektu.

   Objeví-li se při volání :func:`help` v seznamu parametrů funkce lomítko (/),
   znamená to, že parametry před lomítkem jsou pouze poziční. Další informace
   uvádí :ref:`položka FAQ o pouze pozičních parametrech
   <faq-positional-only-arguments>`.

   Tuto funkci přidává do vestavěného jmenného prostoru modul :mod:`site`.

   .. versionchanged:: 3.4
      Díky změnám modulů :mod:`pydoc` a :mod:`inspect` jsou nyní uváděné
      signatury volatelných objektů úplnější a konzistentnější.


.. function:: hex(integer, /)

   Převede celé číslo na řetězec s malými šestnáctkovými číslicemi a předponou
   "0x". Není-li *integer* objektem :class:`int` Pythonu, musí definovat metodu
   :meth:`~object.__index__`, která vrací celé číslo. Několik příkladů:

      >>> hex(255)
      '0xff'
      >>> hex(-42)
      '-0x2a'

   Chcete-li převést celé číslo na řetězec s velkými nebo malými šestnáctkovými
   číslicemi, s předponou či bez ní, můžete použít některý z následujících způsobů:

     >>> '%#x' % 255, '%x' % 255, '%X' % 255
     ('0xff', 'ff', 'FF')
     >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
     ('0xff', 'ff', 'FF')
     >>> f'{255:#x}', f'{255:x}', f'{255:X}'
     ('0xff', 'ff', 'FF')

   Další informace uvádí :func:`format`.

   Převod šestnáctkového řetězce na celé číslo se základem 16 popisuje také
   :func:`int`.

   .. note::

      Šestnáctkovou řetězcovou reprezentaci čísla float získáte metodou
      :meth:`float.hex`.


.. function:: id(object, /)

   Vrátí „identitu“ objektu. Jde o celé číslo, které je po dobu života objektu
   zaručeně jedinečné a neměnné. Dva objekty s nepřekrývající se dobou života
   mohou mít stejnou hodnotu :func:`id`.

   .. impl-detail:: Jde o adresu objektu v paměti.

   .. audit-event:: builtins.id id id


.. function:: input()
              input(prompt, /)

   Je-li přítomen argument *prompt*, vypíše se na standardní výstup bez
   koncového znaku nového řádku. Funkce poté načte řádek ze vstupu, převede jej
   na řetězec (s odstraněním koncového znaku nového řádku) a vrátí jej. Při
   načtení EOF se vyvolá :exc:`EOFError`. Příklad::

      >>> s = input('--> ')  # doctest: +SKIP
      --> Monty Python's Flying Circus
      >>> s  # doctest: +SKIP
      "Monty Python's Flying Circus"

   Je-li načten modul :mod:`readline`, použije jej :func:`input` k poskytnutí
   propracovaných funkcí pro úpravu řádku a historii.

   .. audit-event:: builtins.input prompt input

      Před čtením vstupu vyvolá :ref:`auditní událost <auditing>`
      ``builtins.input`` s argumentem ``prompt``.

   .. audit-event:: builtins.input/result result input

      Po úspěšném načtení vstupu vyvolá :ref:`auditní událost <auditing>`
      ``builtins.input/result`` s výsledkem.


.. class:: int(number=0, /)
           int(string, /, base=10)

   Vrátí objekt celého čísla vytvořený z čísla nebo řetězce; nejsou-li zadány
   žádné argumenty, vrátí ``0``.

   Příklady:

   .. doctest::

      >>> int(123.45)
      123
      >>> int('123')
      123
      >>> int('   -12_345\n')
      -12345
      >>> int('FACE', 16)
      64206
      >>> int('0xface', 0)
      64206
      >>> int('01110011', base=2)
      115

   Definuje-li argument metodu :meth:`~object.__int__`, vrátí ``int(x)`` hodnotu
   ``x.__int__()``. Definuje-li argument :meth:`~object.__index__`, vrátí
   ``x.__index__()``. U čísel s plovoucí řádovou čárkou se hodnota ořízne
   směrem k nule.

   Není-li argument číslo nebo je-li zadán *base*, musí jít o řetězec či instanci
   :class:`bytes` nebo :class:`bytearray`, která představuje celé číslo v číselné
   soustavě se základem *base*. Řetězci může volitelně předcházet ``+`` nebo ``-``
   (bez mezery mezi nimi), může mít počáteční nuly, být obklopen bílými znaky a
   obsahovat mezi číslicemi jednotlivá podtržítka.

   Řetězec celého čísla o základu n obsahuje číslice, z nichž každá představuje
   hodnotu od 0 do n-1. Hodnoty 0--9 lze zapsat libovolnou desetinnou číslicí
   Unicode. Hodnoty 10--35 lze zapsat písmeny ``a`` až ``z`` (nebo ``A`` až
   ``Z``). Výchozí hodnota *base* je 10. Povolené základy jsou 0 a 2--36.
   Řetězce se základem 2, 8 a 16 mohou mít předponu ``0b``/``0B``,
   ``0o``/``0O`` nebo ``0x``/``0X`` stejně jako celočíselné literály v kódu.
   Při základu 0 se řetězec interpretuje obdobně jako :ref:`celočíselný literál
   v kódu <integers>`: skutečný základ 2, 8, 10 nebo 16 určuje předpona. Základ
   0 také nepovoluje počáteční nuly: ``int('010', 0)`` není platné, zatímco
   ``int('010')`` a ``int('010', 8)`` ano.

   Celočíselný typ popisuje oddíl :ref:`typesnumeric`.

   .. versionchanged:: 3.4
      Není-li *base* instancí :class:`int` a má-li objekt *base* metodu
      :meth:`base.__index__ <object.__index__>`, zavolá se tato metoda pro
      získání celého čísla představujícího základ. Předchozí verze používaly
      :meth:`base.__int__ <object.__int__>` namísto :meth:`base.__index__
      <object.__index__>`.

   .. versionchanged:: 3.6
      Je povoleno seskupovat číslice podtržítky stejně jako v literálech kódu.

   .. versionchanged:: 3.7
      První parametr je nyní pouze poziční.

   .. versionchanged:: 3.8
      Na :meth:`~object.__index__` se přejde, není-li definována
      :meth:`~object.__int__`.

   .. versionchanged:: 3.11
      Řetězcové vstupy a řetězcové reprezentace typu :class:`int` lze omezit,
      což pomáhá předcházet útokům typu odepření služby. Při překročení limitu
      se vyvolá :exc:`ValueError`, ať už k němu dojde během převodu řetězce na
      :class:`int`, nebo by limit překročil převod :class:`int` na řetězec. Viz
      dokumentace
      :ref:`omezení délky řetězcového převodu celých čísel
      <int_max_str_digits>`.

   .. versionchanged:: 3.14
      :func:`int` již nedeleguje na metodu :meth:`~object.__trunc__`.

.. function:: isinstance(object, classinfo, /)

   Vrátí ``True``, je-li argument *object* instancí argumentu *classinfo* nebo
   jeho (přímé, nepřímé či :term:`virtuální <abstract base class>`) podtřídy.
   Není-li *object* objektem daného typu, funkce vždy vrátí ``False``.
   Je-li *classinfo* n-ticí objektů typů (případně rekurzivně dalších takových
   n-tic) nebo :ref:`sjednocením typů <types-union>` více typů, vrátí ``True``,
   pokud je *object* instancí kteréhokoli z nich. Není-li *classinfo* typem ani
   n-ticí typů a takových n-tic, vyvolá se výjimka :exc:`TypeError`. U
   neplatného typu se :exc:`TypeError` nemusí vyvolat, uspěje-li dřívější test.

   .. versionchanged:: 3.10
      *classinfo* může být :ref:`sjednocením typů <types-union>`.


.. function:: issubclass(class, classinfo, /)

   Vrátí ``True``, je-li *class* (přímou, nepřímou či :term:`virtuální
   <abstract base class>`) podtřídou *classinfo*. Třída se považuje za podtřídu
   sebe sama. *classinfo* může být n-tice objektů tříd (případně rekurzivně
   dalších takových n-tic) nebo :ref:`sjednocení typů <types-union>`; v takovém
   případě vrátí ``True``, je-li *class* podtřídou kterékoli položky v
   *classinfo*. Ve všech ostatních případech se vyvolá výjimka :exc:`TypeError`.

   .. versionchanged:: 3.10
      *classinfo* může být :ref:`sjednocením typů <types-union>`.


.. function:: iter(iterable, /)
              iter(callable, sentinel, /)

   Vrátí objekt :term:`iterátoru <iterator>`. První argument se interpretuje
   velmi odlišně podle přítomnosti druhého argumentu. Bez druhého argumentu musí
   jediný argument být kolekce podporující protokol :term:`iterovatelného
   objektu <iterable>` (metodu :meth:`~object.__iter__`) nebo protokol sekvence
   (metodu :meth:`~object.__getitem__` s celočíselnými argumenty začínajícími
   hodnotou ``0``). Nepodporuje-li ani jeden z těchto protokolů, vyvolá se
   :exc:`TypeError`. Je-li zadán druhý argument *sentinel*, musí být první
   argument volatelný objekt. Takto vytvořený iterátor při každém volání své
   metody :meth:`~iterator.__next__` zavolá *callable* bez argumentů; rovná-li se
   vrácená hodnota hodnotě *sentinel*, vyvolá se :exc:`StopIteration`, jinak se
   hodnota vrátí.

   Viz také :ref:`typeiter`.

   Jedním z užitečných použití druhé podoby :func:`iter` je vytvoření čtečky
   bloků. Například čtení bloků pevné šířky z binárního databázového souboru až
   do dosažení konce souboru::

      from functools import partial
      with open('mydata.db', 'rb') as f:
          for block in iter(partial(f.read, 64), b''):
              process_block(block)


.. function:: len(object, /)

   Vrátí délku (počet položek) objektu. Argumentem může být sekvence (například
   řetězec, bytes, n-tice, seznam nebo range) či kolekce (například slovník,
   množina nebo neměnná množina).

   .. impl-detail::

      ``len`` vyvolá :exc:`OverflowError` u délek větších než
      :data:`sys.maxsize`, například :class:`range(2 ** 100) <range>`.


.. _func-list:
.. class:: list(iterable=(), /)
   :noindex:

   :class:`list` ve skutečnosti není funkce, ale typ měnitelné sekvence, jak
   popisují oddíly :ref:`typesseq-list` a :ref:`typesseq`.


.. function:: locals()

   Vrátí mapovací objekt představující aktuální místní tabulku symbolů, v níž
   jsou klíči názvy proměnných a hodnotami jejich právě navázané reference.

   V oboru platnosti modulu i při použití :func:`exec` nebo :func:`eval` s
   jediným jmenným prostorem vrací tato funkce stejný jmenný prostor jako
   :func:`globals`.

   V oboru platnosti třídy vrací jmenný prostor, který bude předán konstruktoru
   metatřídy.

   Při použití ``exec()`` nebo ``eval()`` s oddělenými místními a globálními
   argumenty vrací místní jmenný prostor předaný volání funkce.

   Ve všech výše uvedených případech vrátí každé volání ``locals()`` v daném
   rámci vykonávání *tentýž* mapovací objekt. Změny provedené prostřednictvím
   mapovacího objektu vráceného z ``locals()`` se projeví jako přiřazené, znovu
   přiřazené nebo odstraněné místní proměnné a přiřazení, opětovné přiřazení či
   odstranění místních proměnných okamžitě ovlivní obsah vráceného mapování.

   V :term:`optimalizovaném oboru platnosti <optimized scope>` (včetně funkcí,
   generátorů a korutin) naproti tomu každé volání ``locals()`` vrací nový
   slovník s aktuálními vazbami místních proměnných funkce a všech nelokálních
   referencí buněk. Změny vazeb názvů provedené prostřednictvím vráceného
   slovníku se v tomto případě *nezapisují* zpět do odpovídajících místních
   proměnných ani nelokálních referencí buněk. Jejich přiřazení, opětovné
   přiřazení či odstranění zároveň *neovlivní* obsah dříve vrácených slovníků.

   Volání ``locals()`` v rámci komprehenze ve funkci, generátoru nebo korutině
   odpovídá volání v obklopujícím oboru platnosti, zahrne však inicializované
   iterační proměnné komprehenze. V ostatních oborech se chová, jako kdyby
   komprehenze běžela jako vnořená funkce.

   Volání ``locals()`` v rámci generátorového výrazu odpovídá volání ve vnořené
   generátorové funkci.

   .. versionchanged:: 3.12
      Chování ``locals()`` v komprehenzi bylo upraveno podle :pep:`709`.

   .. versionchanged:: 3.13
      V rámci :pep:`667` je nyní definována sémantika změn mapovacích objektů
      vrácených touto funkcí. Chování v :term:`optimalizovaných oborech platnosti
      <optimized scope>` nyní odpovídá výše uvedenému popisu. V ostatních
      oborech zůstává kromě svého zpřesnění oproti předchozím verzím nezměněné.


.. function:: map(function, iterable, /, *iterables, strict=False)

   Vrátí iterátor, který použije *function* na každou položku objektu *iterable*
   a poskytuje výsledky. Jsou-li předány další argumenty *iterables*, musí
   *function* přijímat odpovídající počet argumentů a používá se souběžně na
   položky všech iterovatelných objektů. U více iterovatelných objektů se
   iterátor zastaví po vyčerpání nejkratšího z nich. Je-li *strict* rovno
   ``True`` a některý iterovatelný objekt se vyčerpá dříve než ostatní, vyvolá
   se :exc:`ValueError`. Pro případy, kdy jsou vstupy funkce již uspořádány do
   n-tic argumentů, viz :func:`itertools.starmap`.

   .. versionchanged:: 3.14
      Přidán parametr *strict*.


.. function:: max(iterable, /, *, key=None)
              max(iterable, /, *, default, key=None)
              max(arg1, arg2, /, *args, key=None)

   Vrátí největší položku iterovatelného objektu nebo největší ze dvou či více
   argumentů.

   Je-li zadán jeden poziční argument, měl by být :term:`iterovatelným objektem
   <iterable>`. Vrátí se jeho největší položka. Jsou-li zadány dva nebo více
   pozičních argumentů, vrátí se největší z nich.

   K dispozici jsou dva volitelné argumenty pouze klíčových slov. Argument *key*
   určuje jednoargumentovou řadicí funkci podobnou té, kterou používá
   :meth:`list.sort`. Argument *default* určuje objekt vrácený v případě, že je
   zadaný iterovatelný objekt prázdný. Je-li prázdný a *default* není zadán,
   vyvolá se :exc:`ValueError`.

   Je-li maximálních položek více, funkce vrátí první nalezenou. To odpovídá
   ostatním nástrojům zachovávajícím stabilitu řazení, například
   ``sorted(iterable, key=keyfunc, reverse=True)[0]`` a
   ``heapq.nlargest(1, iterable, key=keyfunc)``.

   .. versionchanged:: 3.4
      Přidán parametr pouze klíčového slova *default*.

   .. versionchanged:: 3.8
      *key* může být ``None``.


.. _func-memoryview:
.. class:: memoryview(object)
   :noindex:

   Vrátí objekt „pohledu do paměti“ vytvořený ze zadaného argumentu. Další
   informace uvádí :ref:`typememoryview`.


.. function:: min(iterable, /, *, key=None)
              min(iterable, /, *, default, key=None)
              min(arg1, arg2, /, *args, key=None)

   Vrátí nejmenší položku iterovatelného objektu nebo nejmenší ze dvou či více
   argumentů.

   Je-li zadán jeden poziční argument, měl by být :term:`iterovatelným objektem
   <iterable>`. Vrátí se jeho nejmenší položka. Jsou-li zadány dva nebo více
   pozičních argumentů, vrátí se nejmenší z nich.

   K dispozici jsou dva volitelné argumenty pouze klíčových slov. Argument *key*
   určuje jednoargumentovou řadicí funkci podobnou té, kterou používá
   :meth:`list.sort`. Argument *default* určuje objekt vrácený v případě, že je
   zadaný iterovatelný objekt prázdný. Je-li prázdný a *default* není zadán,
   vyvolá se :exc:`ValueError`.

   Je-li minimálních položek více, funkce vrátí první nalezenou. To odpovídá
   ostatním nástrojům zachovávajícím stabilitu řazení, například
   ``sorted(iterable, key=keyfunc)[0]`` a ``heapq.nsmallest(1,
   iterable, key=keyfunc)``.

   .. versionchanged:: 3.4
      Přidán parametr pouze klíčového slova *default*.

   .. versionchanged:: 3.8
      *key* může být ``None``.


.. function:: next(iterator, /)
              next(iterator, default, /)

   Získá další položku z :term:`iterátoru <iterator>` voláním jeho metody
   :meth:`~iterator.__next__`. Je-li zadána hodnota *default*, vrátí se při
   vyčerpání iterátoru; jinak se vyvolá :exc:`StopIteration`.


.. class:: object()

   Toto je konečná základní třída všech ostatních tříd. Obsahuje metody společné
   všem instancím tříd Pythonu. Konstruktor při zavolání vrátí nový objekt bez
   dalších vlastností. Nepřijímá žádné argumenty.

   .. note::

      Instance :class:`object` *nemají* atribut :attr:`~object.__dict__`, takže
      instanci :class:`object` nelze přiřazovat libovolné atributy.


.. function:: oct(integer, /)

  Převede celé číslo na osmičkový řetězec s předponou "0o". Výsledkem je platný
  výraz Pythonu. Není-li *integer* objektem :class:`int` Pythonu, musí definovat
  metodu :meth:`~object.__index__`, která vrací celé číslo. Například:

      >>> oct(8)
      '0o10'
      >>> oct(-56)
      '-0o70'

  Chcete-li celé číslo převést na osmičkový řetězec s předponou "0o" nebo bez
  ní, můžete použít některý z následujících způsobů.

      >>> '%#o' % 10, '%o' % 10
      ('0o12', '12')
      >>> format(10, '#o'), format(10, 'o')
      ('0o12', '12')
      >>> f'{10:#o}', f'{10:o}'
      ('0o12', '12')

  Další informace uvádí :func:`format`.

.. index::
   single: file object; open() built-in function

.. function:: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

   Otevře *file* a vrátí odpovídající :term:`souborový objekt <file object>`.
   Nelze-li soubor otevřít, vyvolá se :exc:`OSError`. Další příklady použití
   této funkce uvádí :ref:`tut-files`.

   *file* je :term:`objekt podobný cestě <path-like object>` udávající cestu
   (absolutní nebo relativní vůči aktuálnímu pracovnímu adresáři) k otevíranému
   souboru nebo celočíselný deskriptor souboru, který se má obalit. (Je-li zadán
   deskriptor souboru, při zavření vráceného I/O objektu se také zavře, pokud
   *closefd* není nastaveno na ``False``.)

   *mode* je volitelný řetězec určující režim otevření souboru. Výchozí hodnota
   ``'r'`` znamená otevření pro čtení v textovém režimu. Další běžné hodnoty
   jsou ``'w'`` pro zápis (existující soubor se nejprve zkrátí), ``'x'`` pro
   výhradní vytvoření a ``'a'`` pro připojování (na *některých* unixových
   systémech to znamená, že se *všechny* zápisy připojují na konec souboru bez
   ohledu na aktuální pozici). Není-li v textovém režimu zadáno *encoding*,
   použité kódování závisí na platformě: aktuální kódování národního prostředí
   se získá voláním :func:`locale.getencoding`. (Pro čtení a zápis nezpracovaných
   bajtů použijte binární režim a *encoding* nezadávejte.) Dostupné režimy jsou:

   .. _filemodes:

   .. index::
      pair: file; modes

   ========= ===============================================================
   Znak      Význam
   ========= ===============================================================
   ``'r'``   otevření pro čtení (výchozí)
   ``'w'``   otevření pro zápis s předchozím zkrácením souboru
   ``'x'``   otevření pro výhradní vytvoření; selže, pokud soubor již existuje
   ``'a'``   otevření pro zápis s připojováním na konec existujícího souboru
   ``'b'``   binární režim
   ``'t'``   textový režim (výchozí)
   ``'+'``   otevření pro aktualizaci (čtení i zápis)
   ========= ===============================================================

   Výchozí režim je ``'r'`` (otevření pro čtení textu, synonymum ``'rt'``).
   Režimy ``'w+'`` a ``'w+b'`` soubor otevřou a zkrátí. Režimy ``'r+'`` a
   ``'r+b'`` jej otevřou bez zkrácení.

   Jak uvádí :ref:`io-overview`, Python rozlišuje binární a textový vstup a
   výstup. Soubory otevřené v binárním režimu (argument *mode* obsahuje ``'b'``)
   vracejí obsah jako objekty :class:`bytes` bez dekódování. V textovém režimu
   (výchozím, nebo když *mode* obsahuje ``'t'``) se obsah souboru vrací jako
   :class:`str`; bajty se nejprve dekódují kódováním závislým na platformě nebo
   zadaným *encoding*.

   .. note::

      Python není závislý na pojetí textových souborů v podkladovém operačním
      systému. Veškeré zpracování provádí sám Python, a je proto nezávislé na
      platformě.

   *buffering* je volitelné celé číslo nastavující zásady bufferování. Hodnota 0
   bufferování vypne (povoleno pouze v binárním režimu), 1 zvolí řádkové
   bufferování (použitelné pouze při zápisu v textovém režimu) a celé číslo > 1
   udává velikost bufferu pevných bloků v bajtech. Takto zadaná velikost bufferu
   platí pro bufferovaný binární vstup a výstup, avšak ``TextIOWrapper`` (tedy
   soubory otevřené s ``mode='r+'``) používá další bufferování. Pro jeho vypnutí
   v ``TextIOWrapper`` zvažte příznak ``write_through`` metody
   :func:`io.TextIOWrapper.reconfigure`. Není-li argument *buffering* zadán,
   výchozí zásady fungují následovně:

   * Binární soubory se bufferují v blocích pevné velikosti; je-li dostupná
     velikost bloku zařízení, činí velikost bufferu
     ``max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)``.
     Na většině systémů bude buffer obvykle velký 128 kilobajtů.

   * „Interaktivní“ textové soubory (soubory, pro něž
     :meth:`~io.IOBase.isatty` vrací ``True``) používají řádkové bufferování.
     Ostatní textové soubory používají výše popsané zásady pro binární soubory.

   *encoding* je název kódování použitého k dekódování nebo zakódování souboru.
   Má se používat pouze v textovém režimu. Výchozí kódování závisí na platformě
   (vrací je :func:`locale.getencoding`), lze však použít libovolné
   :term:`textové kódování <text encoding>` podporované Pythonem. Seznam
   podporovaných kódování uvádí modul :mod:`codecs`.

   *errors* je volitelný řetězec určující způsob zpracování chyb kódování a
   dekódování; nelze jej použít v binárním režimu. K dispozici je řada
   standardních obslužných rutin chyb (uvedených v :ref:`error-handlers`),
   platný je však také každý název obsluhy registrovaný pomocí
   :func:`codecs.register_error`. Mezi standardní názvy patří:

   * ``'strict'`` vyvolá při chybě kódování výjimku :exc:`ValueError`. Výchozí
     hodnota ``None`` má stejný účinek.

   * ``'ignore'`` chyby ignoruje. Ignorování chyb kódování může vést ke ztrátě
     dat.

   * ``'replace'`` vloží na místo chybných dat náhradní značku (například
     ``'?'``).

   * ``'surrogateescape'`` představuje chybné bajty nízkými náhradními
     jednotkami kódu v rozsahu U+DC80 až U+DCFF. Při použití obsluhy
     ``surrogateescape`` během zápisu se tyto jednotky převedou zpět na stejné
     bajty. To je užitečné při zpracování souborů v neznámém kódování.

   * ``'xmlcharrefreplace'`` je podporováno pouze při zápisu do souboru. Znaky,
     které kódování nepodporuje, se nahradí odpovídající znakovou referencí XML
     :samp:`&#{nnn};`.

   * ``'backslashreplace'`` nahrazuje chybná data escape sekvencemi Pythonu se
     zpětným lomítkem.

   * ``'namereplace'`` (také podporováno pouze při zápisu) nahrazuje
     nepodporované znaky escape sekvencemi ``\N{...}``.

   .. index::
      single: universal newlines; open() built-in function

   .. _open-newline-parameter:

   *newline* určuje způsob zpracování znaků nového řádku z proudu. Může mít
   hodnotu ``None``, ``''``, ``'\n'``, ``'\r'`` nebo ``'\r\n'``. Funguje
   následovně:

   * Je-li při čtení z proudu *newline* rovno ``None``, zapne se režim
     univerzálních nových řádků. Vstupní řádky mohou končit ``'\n'``, ``'\r'``
     nebo ``'\r\n'`` a před vrácením volajícímu se převedou na ``'\n'``. Je-li
     hodnota ``''``, režim univerzálních nových řádků je zapnutý, ale zakončení
     řádků se vracejí bez převodu. U ostatních platných hodnot ukončuje vstupní
     řádek pouze zadaný řetězec a zakončení se vrací bez převodu.

   * Je-li při zápisu do proudu *newline* rovno ``None``, všechny zapisované
     znaky ``'\n'`` se převedou na výchozí systémový oddělovač řádků
     :data:`os.linesep`. Je-li *newline* rovno ``''`` nebo ``'\n'``, žádný
     převod neprobíhá. U ostatních platných hodnot se zapisované znaky ``'\n'``
     převedou na zadaný řetězec.

   Je-li *closefd* rovno ``False`` a byl zadán deskriptor souboru namísto názvu,
   zůstane podkladový deskriptor při zavření souboru otevřený. Je-li zadán název
   souboru, musí být *closefd* rovno ``True`` (výchozí hodnota), jinak se vyvolá
   chyba.

   Vlastní otevírací funkci lze použít předáním volatelného objektu jako
   *opener*. Podkladový deskriptor souborového objektu se pak získá voláním
   *opener* s argumenty (*file*, *flags*). *opener* musí vrátit otevřený
   deskriptor souboru (předání :mod:`os.open` jako *opener* poskytuje podobnou
   funkčnost jako předání ``None``).

   Nově vytvořený soubor je :ref:`neděditelný <fd_inheritance>`.

   Následující příklad používá parametr :ref:`dir_fd <dir_fd>` funkce
   :func:`os.open` k otevření souboru relativně vůči danému adresáři::

      >>> import os
      >>> dir_fd = os.open('somedir', os.O_RDONLY)
      >>> def opener(path, flags):
      ...     return os.open(path, flags, dir_fd=dir_fd)
      ...
      >>> with open('spamspam.txt', 'w', opener=opener) as f:
      ...     print('This will be written to somedir/spamspam.txt', file=f)
      ...
      >>> os.close(dir_fd)  # don't leak a file descriptor

   Typ :term:`souborového objektu <file object>` vráceného funkcí :func:`open`
   závisí na režimu. Při otevření souboru v textovém režimu (``'w'``, ``'r'``,
   ``'wt'``, ``'rt'`` atd.) vrací :func:`open` podtřídu :class:`io.TextIOBase`
   (konkrétně :class:`io.TextIOWrapper`). Při otevření v bufferovaném binárním
   režimu je vrácená třída podtřídou :class:`io.BufferedIOBase`. Konkrétní třída
   se liší: v binárním režimu čtení se vrací :class:`io.BufferedReader`, v
   binárním režimu zápisu a připojování :class:`io.BufferedWriter` a v režimu
   čtení i zápisu :class:`io.BufferedRandom`. Je-li bufferování vypnuto, vrací
   se nezpracovaný proud, podtřída :class:`io.RawIOBase`, konkrétně
   :class:`io.FileIO`.

   .. index::
      single: line-buffered I/O
      single: unbuffered I/O
      single: buffer size, I/O
      single: I/O control; buffering
      single: binary mode
      single: text mode
      pair: module; sys

   Viz také moduly pro práci se soubory, například :mod:`fileinput`, :mod:`io`
   (kde je deklarována :func:`open`), :mod:`os`, :mod:`os.path`, :mod:`tempfile`
   a :mod:`shutil`.

   .. audit-event:: open path,mode,flags open

   Argumenty ``mode`` a ``flags`` mohou být oproti původnímu volání změněné
   nebo odvozené.

   .. versionchanged:: 3.3

      * Přidán parametr *opener*.
      * Přidán režim ``'x'``.
      * Dříve vyvolávaná :exc:`IOError` je nyní aliasem :exc:`OSError`.
      * Pokud soubor otevíraný v režimu výhradního vytvoření (``'x'``) již
        existuje, vyvolá se nyní :exc:`FileExistsError`.

   .. versionchanged:: 3.4

      * Soubor je nyní neděditelný.

   .. versionchanged:: 3.5

      * Pokud je systémové volání přerušeno a obsluha signálu nevyvolá výjimku,
        funkce nyní systémové volání zopakuje namísto vyvolání výjimky
        :exc:`InterruptedError` (zdůvodnění viz :pep:`475`).
      * Přidána obsluha chyb ``'namereplace'``.

   .. versionchanged:: 3.6

      * Přidána podpora objektů implementujících :class:`os.PathLike`.
      * V systému Windows může otevření bufferu konzole vrátit jinou podtřídu
        :class:`io.RawIOBase` než :class:`io.FileIO`.

   .. versionchanged:: 3.11
      Režim ``'U'`` byl odstraněn.

.. function:: ord(character, /)

   Vrátí pořadovou hodnotu znaku.

   Je-li argument řetězec o jednom znaku, vrátí bod kódu Unicode tohoto znaku.
   Například ``ord('a')`` vrátí celé číslo ``97`` a ``ord('€')`` (znak eura)
   vrátí ``8364``. Jde o inverzní funkci k :func:`chr`.

   Je-li argument objekt :class:`bytes` nebo :class:`bytearray` délky 1, vrátí
   hodnotu jeho jediného bajtu. Například ``ord(b'a')`` vrátí celé číslo ``97``.


.. function:: pow(base, exp, mod=None)

   Vrátí *base* umocněné na *exp*; je-li přítomno *mod*, vrátí *base* umocněné
   na *exp* modulo *mod* (vypočítané efektivněji než
   ``pow(base, exp) % mod``). Dvouargumentová podoba ``pow(base, exp)`` odpovídá
   použití operátoru mocnění: ``base**exp``.

   Jsou-li argumenty vestavěné číselné typy se smíšenými typy operandů, použijí
   se pravidla převodu pro binární aritmetické operátory. U operandů
   :class:`int` má výsledek stejný typ jako operandy (po převodu), není-li druhý
   argument záporný; v takovém případě se všechny argumenty převedou na float a
   vrátí se výsledek typu float. Například ``pow(10, 2)`` vrátí ``100``, ale
   ``pow(10, -2)`` vrátí ``0.01``. U záporného základu typu :class:`int` nebo
   :class:`float` a neceločíselného exponentu se vrátí komplexní výsledek.
   Například ``pow(-9, 0.5)`` vrátí hodnotu blízkou ``3j``. Naproti tomu u
   záporného základu typu :class:`int` nebo :class:`float` s celočíselným
   exponentem se vrátí výsledek typu float. Například ``pow(-9, 2.0)`` vrátí
   ``81.0``.

   Jsou-li operandy *base* a *exp* typu :class:`int` a je přítomno *mod*, musí
   mít *mod* rovněž celočíselný typ a být nenulové. Je-li *mod* přítomno a *exp*
   je záporné, musí být *base* a *mod* nesoudělné. V takovém případě se vrátí
   ``pow(inv_base, -exp, mod)``, kde *inv_base* je inverze *base* modulo *mod*.

   Příklad výpočtu inverze čísla ``38`` modulo ``97``::

      >>> pow(38, -1, mod=97)
      23
      >>> 23 * 38 % 97 == 1
      True

   .. versionchanged:: 3.8
      U operandů :class:`int` nyní tříargumentová podoba ``pow`` dovoluje
      záporný druhý argument, což umožňuje výpočet modulárních inverzí.

   .. versionchanged:: 3.8
      Povoleny argumenty klíčových slov. Dříve byly podporovány pouze poziční
      argumenty.


.. function:: print(*objects, sep=' ', end='\n', file=None, flush=False)

   Vypíše *objects* do textového proudu *file*, oddělené hodnotou *sep* a
   následované hodnotou *end*. Jsou-li *sep*, *end*, *file* a *flush* uvedeny,
   musí být zadány jako argumenty klíčových slov.

   Všechny argumenty, které nejsou klíčovými slovy, se převedou na řetězce jako
   pomocí :func:`str` a zapíší do proudu oddělené hodnotou *sep* a následované
   *end*. *sep* i *end* musí být řetězce; mohou být také ``None``, což znamená
   použití výchozích hodnot. Nejsou-li zadány žádné *objects*, :func:`print`
   zapíše pouze *end*.

   Argument *file* musí být objekt s metodou ``write(string)``; není-li uveden
   nebo je-li roven ``None``, použije se :data:`sys.stdout`. Protože se
   vypisované argumenty převádějí na textové řetězce, nelze :func:`print` použít
   se souborovými objekty v binárním režimu. Pro ně použijte
   ``file.write(...)``.

   Bufferování výstupu obvykle určuje *file*. Je-li však *flush* pravdivé,
   vynutí se vyprázdnění proudu.


   .. versionchanged:: 3.3
      Přidán argument klíčového slova *flush*.


.. class:: property(fget=None, fset=None, fdel=None, doc=None)

   Vrátí atribut vlastnosti.

   *fget* je funkce pro získání hodnoty atributu. *fset* je funkce pro nastavení
   hodnoty atributu. *fdel* je funkce pro odstranění hodnoty atributu. *doc*
   vytváří dokumentační řetězec atributu.

   Typickým použitím je definice spravovaného atributu ``x``::

      class C:
          def __init__(self):
              self._x = None

          def getx(self):
              return self._x

          def setx(self, value):
              self._x = value

          def delx(self):
              del self._x

          x = property(getx, setx, delx, "I'm the 'x' property.")

   Je-li *c* instancí *C*, ``c.x`` zavolá getter, ``c.x = value`` zavolá setter
   a ``del c.x`` deleter.

   Je-li zadáno *doc*, stane se dokumentačním řetězcem atributu vlastnosti.
   Jinak vlastnost zkopíruje dokumentační řetězec *fget* (pokud existuje). Díky
   tomu lze snadno vytvářet vlastnosti pouze pro čtení použitím :func:`property`
   jako :term:`dekorátoru <decorator>`::

      class Parrot:
          def __init__(self):
              self._voltage = 100000

          @property
          def voltage(self):
              """Get the current voltage."""
              return self._voltage

   Dekorátor ``@property`` změní metodu :meth:`!voltage` na „getter“ atributu
   stejného názvu určeného pouze pro čtení a nastaví dokumentační řetězec
   *voltage* na "Get the current voltage."

   .. decorator:: property.getter
   .. decorator:: property.setter
   .. decorator:: property.deleter

      Objekt vlastnosti má metody ``getter``, ``setter`` a ``deleter``, které
      lze použít jako dekorátory. Vytvoří kopii vlastnosti a nastaví odpovídající
      přístupovou funkci na dekorovanou funkci. Nejlépe to ukáže příklad:

      .. testcode::

         class C:
             def __init__(self):
                 self._x = None

             @property
             def x(self):
                 """I'm the 'x' property."""
                 return self._x

             @x.setter
             def x(self, value):
                 self._x = value

             @x.deleter
             def x(self):
                 del self._x

      Tento kód je přesně ekvivalentní prvnímu příkladu. Doplňkovým funkcím je
      nutné dát stejný název jako původní vlastnosti (v tomto případě ``x``).

      Vrácený objekt vlastnosti má také atributy ``fget``, ``fset`` a ``fdel``
      odpovídající argumentům konstruktoru.

   .. versionchanged:: 3.5
      Dokumentační řetězce objektů vlastností jsou nyní zapisovatelné.

   .. attribute:: __name__

      Atribut uchovávající název vlastnosti. Název vlastnosti lze změnit za
      běhu.

      .. versionadded:: 3.13


.. _func-range:
.. class:: range(stop, /)
           range(start, stop, step=1, /)
   :noindex:

   :class:`range` ve skutečnosti není funkce, ale typ neměnné sekvence, jak
   popisují oddíly :ref:`typesseq-range` a :ref:`typesseq`.


.. function:: repr(object, /)

   Vrátí řetězec obsahující tisknutelnou reprezentaci objektu. U mnoha typů se
   funkce pokouší vrátit řetězec, který po předání funkci :func:`eval` vytvoří
   objekt se stejnou hodnotou. Jinak je reprezentací řetězec uzavřený v ostrých
   závorkách, který obsahuje název typu objektu a další informace, často včetně
   názvu a adresy objektu. Třída může návratovou hodnotu této funkce pro své
   instance řídit definicí metody :meth:`~object.__repr__`.
   Není-li dostupná :func:`sys.displayhook`, vyvolá tato funkce
   :exc:`RuntimeError`.

   Tato třída má vlastní reprezentaci, kterou lze vyhodnotit::

      class Person:
         def __init__(self, name, age):
            self.name = name
            self.age = age

         def __repr__(self):
            return f"Person('{self.name}', {self.age})"


.. function:: reversed(object, /)

   Vrátí obrácený :term:`iterátor <iterator>`. Argument musí být objekt s
   metodou :meth:`~object.__reversed__` nebo musí podporovat protokol sekvence
   (metodu :meth:`~object.__len__` a metodu :meth:`~object.__getitem__` s
   celočíselnými argumenty začínajícími hodnotou ``0``).


.. function:: round(number, ndigits=None)

   Vrátí *number* zaokrouhlené na přesnost *ndigits* číslic za desetinnou
   tečkou. Je-li *ndigits* vynecháno nebo rovno ``None``, vrátí celé číslo
   nejbližší vstupu.

   U vestavěných typů podporujících :func:`round` se hodnoty zaokrouhlují na
   nejbližší násobek 10 na minus *ndigits*. Jsou-li dva násobky stejně blízké,
   zaokrouhlí se k sudé možnosti (například ``round(0.5)`` i ``round(-0.5)``
   jsou ``0`` a ``round(1.5)`` je ``2``). Pro *ndigits* je platné libovolné celé
   číslo (kladné, nulové i záporné). Je-li *ndigits* vynecháno nebo rovno
   ``None``, návratovou hodnotou je celé číslo. Jinak má návratová hodnota
   stejný typ jako *number*.

   U obecného objektu Pythonu ``number`` deleguje ``round`` na
   ``number.__round__``.

   .. note::

      Chování :func:`round` pro čísla float může být překvapivé: například
      ``round(2.675, 2)`` poskytne ``2.67`` namísto očekávaných ``2.68``.
      Nejde o chybu, ale o důsledek skutečnosti, že většinu desetinných zlomků
      nelze jako float vyjádřit přesně. Další informace uvádí
      :ref:`tut-fp-issues`.


.. _func-set:
.. class:: set(iterable=(), /)
   :noindex:

   Vrátí nový objekt :class:`set`, volitelně s prvky převzatými z *iterable*.
   ``set`` je vestavěná třída. Dokumentaci této třídy uvádějí :class:`set` a
   :ref:`types-set`.

   Další kontejnery popisují vestavěné třídy :class:`frozenset`, :class:`list`,
   :class:`tuple` a :class:`dict` i modul :mod:`collections`.


.. function:: setattr(object, name, value, /)

   Jde o protějšek funkce :func:`getattr`. Argumenty jsou objekt, řetězec a
   libovolná hodnota. Řetězec může pojmenovávat existující nebo nový atribut.
   Pokud to objekt dovoluje, funkce přiřadí atributu hodnotu. Například
   ``setattr(x, 'foobar', 123)`` je ekvivalentní výrazu ``x.foobar = 123``.

   *name* nemusí být identifikátor Pythonu podle :ref:`identifiers`, pokud si
   objekt toto omezení sám nevynutí, například ve vlastní metodě
   :meth:`~object.__getattribute__` nebo pomocí :attr:`~object.__slots__`.
   Atribut, jehož název není identifikátor, nebude přístupný tečkovou notací,
   lze k němu však přistoupit například prostřednictvím :func:`getattr`.

   .. note::

      Protože k :ref:`komolení soukromých názvů <private-name-mangling>` dochází
      při kompilaci, je nutné název soukromého atributu (atributu se dvěma
      počátečními podtržítky) pro nastavení pomocí :func:`setattr` zkomolit ručně.


.. class:: slice(stop, /)
           slice(start, stop, step=None, /)

   Vrátí objekt :term:`výřezu <slice>` představující množinu indexů určenou
   výrazem ``range(start, stop, step)``. Výchozí hodnotou argumentů *start* a
   *step* je ``None``.

   Objekty výřezu vznikají také při použití :ref:`syntaxe výřezů <slicings>`.
   Například: ``a[start:stop:step]`` nebo ``a[start:stop, i]``.

   Alternativní variantu poskytuje :func:`itertools.islice`; vrací
   :term:`iterátor <iterator>`.

   .. attribute:: slice.start
                  slice.stop
                  slice.step

      Tyto atributy pouze pro čtení jsou nastaveny na hodnoty argumentů (nebo
      jejich výchozí hodnoty). Nemají žádnou další výslovnou funkci, používá je
      však NumPy a další balíčky třetích stran.

   .. versionchanged:: 3.12
      Objekty výřezu jsou nyní :term:`hashovatelné <hashable>` (pokud jsou
      hashovatelné :attr:`~slice.start`, :attr:`~slice.stop` a
      :attr:`~slice.step`).

.. function:: sorted(iterable, /, *, key=None, reverse=False)

   Vrátí nový seřazený seznam z položek objektu *iterable*.

   Má dva volitelné argumenty, které musí být zadány jako argumenty klíčových slov.

   *key* určuje funkci jednoho argumentu, která z každého prvku objektu
   *iterable* získá porovnávací klíč (například ``key=str.lower``). Výchozí
   hodnota je ``None`` (prvky se porovnávají přímo).

   *reverse* je booleovská hodnota. Je-li nastavena na ``True``, prvky seznamu
   se seřadí, jako kdyby každé porovnání proběhlo obráceně.

   Pro převod funkce *cmp* starého stylu na funkci *key* použijte
   :func:`functools.cmp_to_key`.

   Vestavěná funkce :func:`sorted` je zaručeně stabilní. Řazení je stabilní,
   pokud nemění vzájemné pořadí prvků, které se porovnají jako shodné. To je
   užitečné při víceprůchodovém řazení (například nejprve podle oddělení a poté
   podle platové třídy).

   Algoritmus řazení používá mezi položkami pouze porovnání ``<``. Přestože pro
   řazení stačí definovat metodu :meth:`~object.__lt__`, :PEP:`8` doporučuje
   implementovat všech šest :ref:`rozšířených porovnání <comparisons>`. Pomůže
   to předejít chybám při použití stejných dat s jinými nástroji pro řazení,
   například :func:`max`, které spoléhají na jinou podkladovou metodu.
   Implementace všech šesti porovnání také omezuje nejasnosti při porovnávání
   smíšených typů, jež může zavolat odraženou metodu :meth:`~object.__gt__`.

   Příklady a stručný návod k řazení uvádí :ref:`sortinghowto`.

.. decorator:: staticmethod

   Převede metodu na statickou metodu.

   Statická metoda nedostává implicitní první argument. Pro její deklaraci
   použijte následující idiom::

      class C:
          @staticmethod
          def f(arg1, arg2, argN): ...

   Podoba ``@staticmethod`` je :term:`dekorátor <decorator>` funkce; podrobnosti
   uvádí :ref:`function`.

   Statickou metodu lze volat na třídě (například ``C.f()``) i na instanci
   (například ``C().f()``). Také :term:`deskriptor <descriptor>` statické metody
   je volatelný, takže jej lze použít v definici třídy (například ``f()``).

   Statické metody v Pythonu se podobají metodám v Javě nebo C++. Variantou
   užitečnou pro tvorbu alternativních konstruktorů tříd je :func:`classmethod`.

   Stejně jako všechny dekorátory lze také ``staticmethod`` zavolat jako běžnou
   funkci a dále pracovat s jejím výsledkem. To je potřeba v případech, kdy
   potřebujete z těla třídy referenci na funkci a chcete zabránit automatickému
   převodu na metodu instance. Tehdy použijte tento idiom::

      def regular_function():
          ...

      class C:
          method = staticmethod(regular_function)

   Další informace o statických metodách uvádí :ref:`types`.

   .. versionchanged:: 3.10
      Statické metody nyní přebírají atributy metody
      (:attr:`~function.__module__`, :attr:`~function.__name__`,
      :attr:`~function.__qualname__`, :attr:`~function.__doc__` a
      :attr:`~function.__annotations__`), mají nový atribut ``__wrapped__`` a
      lze je volat jako běžné funkce.


.. index::
   single: string; str() (built-in function)

.. _func-str:
.. class:: str(*, encoding='utf-8', errors='strict')
           str(object)
           str(object, encoding, errors='strict')
           str(object, *, errors)
   :noindex:

   Vrátí verzi objektu *object* typu :class:`str`. Podrobnosti uvádí
   :func:`str`.

   ``str`` je vestavěná řetězcová :term:`třída <class>`. Obecné informace o
   řetězcích uvádí :ref:`textseq`.


.. function:: sum(iterable, /, start=0)

   Sečte zleva doprava hodnotu *start* a položky objektu *iterable* a vrátí
   součet. Položky *iterable* jsou obvykle čísla a počáteční hodnota nesmí být
   řetězec.

   Pro některé případy použití existují vhodné alternativy k :func:`sum`.
   Upřednostňovaným rychlým způsobem spojení sekvence řetězců je volání
   ``''.join(sequence)``. Pro sčítání hodnot s plovoucí řádovou čárkou s
   rozšířenou přesností viz :func:`math.fsum`\. Pro spojení řady iterovatelných
   objektů zvažte :func:`itertools.chain`.

   .. versionchanged:: 3.8
      Parametr *start* lze zadat jako argument klíčového slova.

   .. versionchanged:: 3.12 Sčítání hodnot float přešlo na algoritmus, který na
      většině sestavení poskytuje vyšší přesnost a lepší komutativitu.

   .. versionchanged:: 3.14
      Přidána specializace pro sčítání komplexních čísel používající stejný
      algoritmus jako sčítání hodnot float.


.. class:: super()
           super(type, object_or_type=None, /)

   Vrátí proxy objekt, který deleguje volání metod na rodičovskou nebo
   sourozeneckou třídu typu *type*. To je užitečné pro přístup ke zděděným
   metodám, které byly ve třídě překryty.

   *object_or_type* určuje prohledávané :term:`pořadí rozlišení metod <method
   resolution order>`. Hledání začíná třídou bezprostředně následující za
   *type*.

   Je-li například :attr:`~type.__mro__` objektu *object_or_type*
   ``D -> B -> C -> A -> object`` a hodnota *type* je ``B``, prohledává
   :func:`super` pořadí ``C -> A -> object``.

   Atribut :attr:`~type.__mro__` třídy odpovídající *object_or_type* obsahuje
   pořadí hledání metod používané funkcemi :func:`getattr` i :func:`super`.
   Atribut je dynamický a může se změnit při každé aktualizaci hierarchie
   dědičnosti.

   Je-li druhý argument vynechán, vrácený objekt super je nevázaný. Je-li druhý
   argument objekt, musí být ``isinstance(obj, type)`` pravdivé. Je-li druhý
   argument typ, musí být pravdivé ``issubclass(type2, type)`` (to je užitečné
   pro metody tříd).

   Při přímém volání uvnitř běžné metody třídy lze oba argumenty vynechat
   („bezargumentové :func:`!super`“). *type* pak bude obklopující třída a *obj*
   první argument bezprostředně obklopující funkce (obvykle ``self``). To
   znamená, že bezargumentové :func:`!super` nebude fungovat očekávaným způsobem
   uvnitř vnořených funkcí, včetně generátorových výrazů, které vnořené funkce
   vytvářejí implicitně.

   *super* má dvě typická použití. V hierarchii tříd s jednoduchou dědičností
   lze pomocí *super* odkazovat na rodičovské třídy bez jejich výslovného
   pojmenování, což usnadňuje údržbu kódu. Toto použití se blíží použití *super*
   v jiných programovacích jazycích.

   Druhým použitím je podpora kooperativní vícenásobné dědičnosti v dynamickém
   běhovém prostředí. Toto použití je specifické pro Python a nevyskytuje se ve
   staticky kompilovaných jazycích ani v jazycích podporujících pouze jednoduchou
   dědičnost. Umožňuje implementovat „diamantové diagramy“, v nichž stejnou
   metodu implementuje více základních tříd. Správný návrh vyžaduje, aby takové
   implementace měly vždy stejnou signaturu volání (protože pořadí volání se
   určuje za běhu, přizpůsobuje se změnám hierarchie tříd a může zahrnovat
   sourozenecké třídy, které před spuštěním nejsou známé).

   V obou případech vypadá typické volání nadtřídy takto::

      class C(B):
          def method(self, arg):
              super().method(arg)    # This does the same thing as:
                                     # super(C, self).method(arg)

   :func:`super` funguje kromě vyhledávání metod také pro vyhledávání atributů.
   Jedním z možných použití je volání :term:`deskriptorů <descriptor>` v
   rodičovské nebo sourozenecké třídě.

   :func:`super` je implementována jako součást procesu vazby pro výslovné
   vyhledávání atributů tečkovou notací, například
   ``super().__getitem__(name)``. Implementuje vlastní metodu
   :meth:`~object.__getattribute__`, která prohledává třídy v předvídatelném
   pořadí podporujícím kooperativní vícenásobnou dědičnost. Proto není
   :func:`super` definována pro implicitní vyhledávání pomocí příkazů nebo
   operátorů, například ``super()[name]``.

   Kromě bezargumentové podoby také není :func:`super` omezena na použití uvnitř
   metod. Dvouargumentová podoba určuje argumenty přesně a vytvoří odpovídající
   reference. Bezargumentová podoba funguje pouze uvnitř definice třídy, protože
   překladač doplní údaje potřebné ke správnému získání právě definované třídy a
   u běžných metod také k přístupu k aktuální instanci.

   Praktická doporučení k návrhu kooperativních tříd pomocí :func:`super` uvádí
   `průvodce použitím super()
   <https://rhettinger.wordpress.com/2011/05/26/super-considered-super/>`_.

   .. versionchanged:: 3.14
     Objekty :class:`super` lze nyní :mod:`serializovat modulem pickle <pickle>`
      a :mod:`kopírovat <copy>`.


.. _func-tuple:
.. class:: tuple(iterable=(), /)
   :noindex:

   :class:`tuple` ve skutečnosti není funkce, ale typ neměnné sekvence, jak
   popisují oddíly :ref:`typesseq-tuple` a :ref:`typesseq`.


.. class:: type(object, /)
           type(name, bases, dict, /, **kwargs)

   .. index:: pair: object; type

   S jedním argumentem vrátí typ objektu *object*. Návratovou hodnotou je objekt
   typu, obvykle stejný jako objekt vrácený atributem
   :attr:`object.__class__`.

   Pro testování typu objektu se doporučuje vestavěná funkce :func:`isinstance`,
   protože bere v úvahu podtřídy.

   Se třemi argumenty vrátí nový objekt typu. Jde v podstatě o dynamickou podobu
   příkazu :keyword:`class`. Řetězec *name* je názvem třídy a stane se atributem
   :attr:`~type.__name__`. N-tice *bases* obsahuje základní třídy a stane se
   atributem :attr:`~type.__bases__`; je-li prázdná, přidá se :class:`object`,
   konečný základ všech tříd. Slovník *dict* obsahuje definice atributů a metod
   pro tělo třídy; předtím, než se stane atributem :attr:`~type.__dict__`, může
   být zkopírován nebo obalen. Následující dva příkazy vytvoří shodné objekty
   :class:`!type`:

      >>> class X:
      ...     a = 1
      ...
      >>> X = type('X', (), dict(a=1))

   Viz také:

   * :ref:`Dokumentace atributů a metod tříd <class-attrs-and-methods>`.
   * :ref:`bltin-type-objects`

   Argumenty klíčových slov předané tříargumentové podobě se předají
   odpovídajícímu mechanismu metatřídy (obvykle
   :meth:`~object.__init_subclass__`) stejně jako klíčová slova v definici třídy
   (kromě *metaclass*).

   Viz také :ref:`class-customization`.

   .. versionchanged:: 3.6
      Podtřídy :class:`!type`, které nepřekrývají ``type.__new__``, již nemohou
      používat jednoargumentovou podobu k získání typu objektu.

.. function:: vars()
              vars(object, /)

   Vrátí atribut :attr:`~object.__dict__` modulu, třídy, instance nebo jiného
   objektu s atributem :attr:`!__dict__`.

   Objekty jako moduly a instance mají měnitelný atribut
   :attr:`~object.__dict__`; jiné objekty však mohou zápis do atributu
   :attr:`!__dict__` omezovat (například třídy používají
   :class:`types.MappingProxyType`, aby zabránily přímým změnám slovníku).

   Bez argumentu se :func:`vars` chová jako :func:`locals`.

   Výjimka :exc:`TypeError` se vyvolá, je-li zadán objekt, který nemá atribut
   :attr:`~object.__dict__` (například pokud jeho třída definuje atribut
   :attr:`~object.__slots__`).

   .. versionchanged:: 3.13

      Výsledek volání této funkce bez argumentu byl upraven podle popisu
      vestavěné funkce :func:`locals`.


.. function:: zip(*iterables, strict=False)

   Prochází souběžně několik iterovatelných objektů a vytváří n-tice s jednou
   položkou z každého z nich.

   Příklad::

      >>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
      ...     print(item)
      ...
      (1, 'sugar')
      (2, 'spice')
      (3, 'everything nice')

   Formálněji: :func:`zip` vrací iterátor n-tic, kde *i*-tá n-tice obsahuje
   *i*-tý prvek z každého iterovatelného argumentu.

   Jiný pohled na :func:`zip` je, že mění řádky na sloupce a sloupce na řádky.
   Podobá se to `transpozici matice
   <https://en.wikipedia.org/wiki/Transpose>`_.

   :func:`zip` je líná: prvky se nezpracují, dokud se přes iterovatelný objekt
   nezačne iterovat, například cyklem :keyword:`!for` nebo obalením do
   :class:`list`.

   Je třeba vzít v úvahu, že iterovatelné objekty předané funkci :func:`zip`
   mohou mít různou délku, někdy záměrně a někdy kvůli chybě v kódu, který je
   připravil. Python nabízí tři způsoby řešení:

   * Ve výchozím nastavení se :func:`zip` zastaví po vyčerpání nejkratšího
     iterovatelného objektu. Zbývající položky delších objektů ignoruje a zkrátí
     výsledek na délku nejkratšího::

        >>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
        [(0, 'fee'), (1, 'fi'), (2, 'fo')]

   * :func:`zip` se často používá tam, kde se předpokládá stejná délka
     iterovatelných objektů. V takovém případě se doporučuje volba
     ``strict=True``. Její výstup je stejný jako u běžné :func:`zip`::

        >>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
        [('a', 1), ('b', 2), ('c', 3)]

     Na rozdíl od výchozího chování vyvolá :exc:`ValueError`, pokud se jeden
     iterovatelný objekt vyčerpá dříve než ostatní:

        >>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  # doctest: +SKIP
        ...     print(item)
        ...
        (0, 'fee')
        (1, 'fi')
        (2, 'fo')
        Traceback (most recent call last):
          ...
        ValueError: zip() argument 2 is longer than argument 1

     ..
        Tento doctest je vypnutý, protože doctest nepodporuje zachycení výstupu
        a výjimek ve stejné jednotce kódu.
        https://github.com/python/cpython/issues/65382

     Bez argumentu ``strict=True`` se každá chyba vedoucí k různým délkám
     iterovatelných objektů potlačí a může se projevit jako obtížně odhalitelná
     chyba v jiné části programu.

   * Kratší iterovatelné objekty lze doplnit konstantní hodnotou, aby měly
     všechny stejnou délku. Provádí to :func:`itertools.zip_longest`.

   Mezní případy: S jediným iterovatelným argumentem vrací :func:`zip` iterátor
   jednoprvkových n-tic. Bez argumentů vrací prázdný iterátor.

   Tipy a triky:

   * Je zaručeno vyhodnocování iterovatelných objektů zleva doprava. To umožňuje
     idiom pro seskupení datové řady do skupin délky n pomocí
     ``zip(*[iter(s)]*n, strict=True)``. *Tentýž* iterátor se zopakuje ``n``-krát,
     takže každá výstupní n-tice obsahuje výsledky ``n`` volání iterátoru.
     Vstup se tím rozdělí na bloky délky n.

   * :func:`zip` lze spolu s operátorem ``*`` použít k rozbalení seznamu::

        >>> x = [1, 2, 3]
        >>> y = [4, 5, 6]
        >>> list(zip(x, y))
        [(1, 4), (2, 5), (3, 6)]
        >>> x2, y2 = zip(*zip(x, y))
        >>> x == list(x2) and y == list(y2)
        True

   .. versionchanged:: 3.10
      Přidán argument ``strict``.


.. function:: __import__(name, globals=None, locals=None, fromlist=(), level=0)

   .. index::
      pair: statement; import
      pair: module; builtins

   .. note::

      Jde o pokročilou funkci, která na rozdíl od
      :func:`importlib.import_module` není při běžném programování v Pythonu
      potřeba.

   Tuto funkci volá příkaz :keyword:`import`. Lze ji nahradit (importováním
   modulu :mod:`builtins` a přiřazením do ``builtins.__import__``), a změnit tak
   sémantiku příkazu :keyword:`!import`. Tento postup se však **důrazně**
   nedoporučuje, protože stejných cílů lze obvykle snáze dosáhnout importními
   háčky (viz :pep:`302`), aniž by vznikly problémy s kódem předpokládajícím
   výchozí implementaci importu. Také přímé použití :func:`__import__` se
   nedoporučuje; přednost má :func:`importlib.import_module`.

   Funkce importuje modul *name* a případně pomocí zadaných *globals* a *locals*
   určí, jak název interpretovat v kontextu balíčku. *fromlist* udává názvy
   objektů nebo podmodulů, které se mají importovat z modulu určeného parametrem
   *name*. Standardní implementace argument *locals* vůbec nepoužívá a *globals*
   používá pouze k určení kontextu balíčku příkazu :keyword:`import`.

   *level* určuje použití absolutních nebo relativních importů. ``0`` (výchozí
   hodnota) znamená provádět pouze absolutní importy. Kladné hodnoty *level*
   udávají počet rodičovských adresářů, které se mají prohledat relativně vůči
   adresáři modulu volajícího :func:`__import__` (podrobnosti viz :pep:`328`).

   Má-li proměnná *name* podobu ``package.module``, obvykle se vrátí balíček
   nejvyšší úrovně (název po první tečku), a *nikoli* modul pojmenovaný *name*.
   Je-li však zadán neprázdný argument *fromlist*, vrátí se modul pojmenovaný
   *name*.

   Například příkaz ``import spam`` vytvoří bajtkód podobný následujícímu kódu::

      spam = __import__('spam', globals(), locals(), [], 0)

   Příkaz ``import spam.ham`` vede k tomuto volání::

      spam = __import__('spam.ham', globals(), locals(), [], 0)

   Všimněte si, že :func:`__import__` zde vrací modul nejvyšší úrovně, protože
   právě tento objekt příkaz :keyword:`import` naváže na název.

   Naproti tomu příkaz ``from spam.ham import eggs, sausage as
   saus`` vede k::

      _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
      eggs = _temp.eggs
      saus = _temp.sausage

   Z :func:`__import__` se zde vrátí modul ``spam.ham``. Z tohoto objektu se
   získají importované názvy a přiřadí se příslušným názvům.

   Chcete-li jednoduše importovat modul (případně uvnitř balíčku) podle názvu,
   použijte :func:`importlib.import_module`.

   .. versionchanged:: 3.3
      Záporné hodnoty *level* již nejsou podporovány (výchozí hodnota se tím
      také mění na 0).

   .. versionchanged:: 3.9
      Při použití voleb příkazového řádku :option:`-E` nebo :option:`-I` se nyní
      ignoruje proměnná prostředí :envvar:`PYTHONCASEOK`.

.. rubric:: Poznámky pod čarou

.. [#] Překladač přijímá pouze unixovou konvenci konce řádku. Čtete-li kód ze
   souboru, použijte režim převodu nových řádků, který převede konce řádků ve
   stylu Windows nebo Mac.
