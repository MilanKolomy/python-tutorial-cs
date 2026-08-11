.. _glossary:

*************
Slovník pojmů
*************

.. Při přidávání nových hesel zachovejte abecední řazení!

.. glossary::

   ``>>>``
      Výchozí výzva Pythonu v :term:`interaktivním <interactive>` shellu. Často
      se objevuje u ukázek kódu, které lze spustit interaktivně v interpretu.

   ``...``
      Může označovat:

      * Výchozí výzvu Pythonu v :term:`interaktivním <interactive>` shellu při
        zadávání odsazeného bloku kódu, uvnitř páru odpovídajících levých a
        pravých oddělovačů (kulatých, hranatých či složených závorek nebo
        trojitých uvozovek) nebo po zadání dekorátoru.

      .. index:: single: ...; ellipsis literal

      * Podobu objektu :ref:`Ellipsis <bltin-ellipsis-object>` tvořenou třemi
        tečkami.

   abstract base class
      Abstraktní základní třídy (abstract base classes, ABC) doplňují
      :term:`kachní typování <duck-typing>` tím, že umožňují definovat rozhraní
      v případech, kdy by jiné techniky, například :func:`hasattr`, byly
      neohrabané nebo nenápadně chybné (například u :ref:`magických metod
      <special-lookup>`). ABC zavádějí virtuální podtřídy, tedy třídy, které z
      dané třídy nedědí, ale funkce :func:`isinstance` a :func:`issubclass` je
      přesto rozpoznají; viz dokumentace modulu :mod:`abc`. Python obsahuje řadu
      vestavěných ABC pro datové struktury (v modulu :mod:`collections.abc`),
      čísla (v modulu :mod:`numbers`), proudy (v modulu :mod:`io`) a vyhledávače
      a zavaděče importů (v modulu :mod:`importlib.abc`). Vlastní ABC můžete
      vytvářet pomocí modulu :mod:`abc`.

   annotate function
      Volatelný objekt, jehož zavoláním lze získat :term:`anotace <annotation>`
      objektu. Anotační funkce jsou obvykle :term:`funkce <function>` automaticky
      vytvářené jako atribut :attr:`~object.__annotate__` funkcí, tříd a modulů.
      Anotační funkce jsou podmnožinou :term:`vyhodnocovacích funkcí
      <evaluate function>`.

   annotation
      Značka přidružená k proměnné, atributu třídy, parametru funkce nebo
      návratové hodnotě, která se podle konvence používá jako :term:`typová
      nápověda <type hint>`.

      K anotacím místních proměnných nelze přistupovat za běhu, ale anotace
      globálních proměnných, atributů tříd a funkcí lze získat voláním
      :func:`annotationlib.get_annotations` nad moduly, třídami a funkcemi.

      Tuto funkcionalitu popisují hesla :term:`anotace proměnné <variable
      annotation>` a :term:`anotace funkce <function annotation>` a dokumenty
      :pep:`484`, :pep:`526` a :pep:`649`. Doporučené postupy pro práci s
      anotacemi uvádí také :ref:`annotations-howto`.

   argument
      Hodnota předaná :term:`funkci <function>` (nebo :term:`metodě <method>`)
      při jejím volání. Existují dva druhy argumentů:

      * :dfn:`argument klíčového slova`: argument, kterému ve
        volání funkce předchází identifikátor (například ``name=``), nebo
        argument předaný jako hodnota ve slovníku, jemuž předchází ``**``.
        Například ``3`` a ``5`` jsou v následujících voláních :func:`complex`
        argumenty klíčových slov::

           complex(real=3, imag=5)
           complex(**{'real': 3, 'imag': 5})

      * :dfn:`poziční argument`: argument, který není
        argumentem klíčového slova. Poziční argumenty se mohou objevit na
        začátku seznamu argumentů nebo být předány jako prvky
        :term:`iterovatelného objektu <iterable>`, kterému předchází ``*``.
        Například ``3`` a ``5`` jsou v následujících voláních poziční argumenty::

           complex(3, 5)
           complex(*(3, 5))

      Argumenty se přiřadí pojmenovaným místním proměnným v těle funkce.
      Pravidla tohoto přiřazení uvádí oddíl :ref:`calls`. Z hlediska syntaxe lze
      argument vyjádřit libovolným výrazem; vyhodnocená hodnota se přiřadí
      místní proměnné.

      Viz také heslo :term:`parametr <parameter>`, otázka FAQ o :ref:`rozdílu
      mezi argumenty a parametry <faq-argument-vs-parameter>` a :pep:`362`.

   asynchronous context manager
      Objekt, který řídí prostředí dostupné v příkazu :keyword:`async with`
      definováním metod :meth:`~object.__aenter__` a :meth:`~object.__aexit__`.
      Zaveden v :pep:`492`.

   asynchronous generator
      Funkce, která vrací :term:`iterátor asynchronního generátoru
      <asynchronous generator iterator>`. Podobá se korutinové funkci definované
      pomocí :keyword:`async def`, obsahuje však výrazy :keyword:`yield`, které
      vytvářejí posloupnost hodnot použitelnou v cyklu :keyword:`async for`.

      Obvykle se tímto pojmem rozumí funkce asynchronního generátoru, v některých
      souvislostech však může označovat *iterátor asynchronního generátoru*.
      Není-li zamýšlený význam zřejmý, použití úplných názvů zabrání nejednoznačnosti.

      Funkce asynchronního generátoru může obsahovat výrazy :keyword:`await`
      i příkazy :keyword:`async for` a :keyword:`async with`.

   asynchronous generator iterator
      Objekt vytvořený funkcí :term:`asynchronního generátoru
      <asynchronous generator>`.

      Jde o :term:`asynchronní iterátor <asynchronous iterator>`, který při
      volání metodou :meth:`~object.__anext__` vrací čekatelný objekt. Ten provádí
      tělo funkce asynchronního generátoru až k následujícímu výrazu
      :keyword:`yield`.

      Každý :keyword:`yield` dočasně pozastaví zpracování a zapamatuje si stav
      provádění (včetně místních proměnných a nedokončených příkazů try). Když
      *iterátor asynchronního generátoru* fakticky pokračuje prostřednictvím
      dalšího čekatelného objektu vráceného metodou :meth:`~object.__anext__`,
      naváže tam, kde skončil. Viz :pep:`492` a :pep:`525`.

   asynchronous iterable
      Objekt, který lze použít v příkazu :keyword:`async for`. Musí vracet
      :term:`asynchronní iterátor <asynchronous iterator>` ze své metody
      :meth:`~object.__aiter__`. Zaveden v :pep:`492`.

   asynchronous iterator
      Objekt implementující metody :meth:`~object.__aiter__` a
      :meth:`~object.__anext__`. Metoda :meth:`~object.__anext__` musí vracet
      :term:`čekatelný objekt <awaitable>`. Příkaz :keyword:`async for`
      vyhodnocuje čekatelné objekty vracené metodou :meth:`~object.__anext__`
      asynchronního iterátoru, dokud tato metoda nevyvolá výjimku
      :exc:`StopAsyncIteration`. Zaveden v :pep:`492`.

   atomic operation
      Operace, která se zdánlivě provede jako jediný nedělitelný krok: žádné jiné
      vlákno ji nemůže pozorovat napůl dokončenou a její účinky se projeví
      všechny najednou. Python nezaručuje atomicitu příkazů vysoké úrovně
      (například ``x += 1`` provádí několik operací bajtkódu, a proto atomický
      není). Atomicita je zaručena pouze tam, kde je výslovně zdokumentována.
      Viz také :term:`souběh <race condition>` a :term:`datový souběh <data race>`.

   attached thread state

      :term:`Stav vlákna <thread state>`, který je aktivní pro aktuální vlákno
      operačního systému.

      Je-li :term:`stav vlákna <thread state>` připojen, má vlákno operačního
      systému přístup k celému C API Pythonu a může bezpečně spouštět interpret
      bajtkódu.

      Pokud dokumentace funkce výslovně neuvádí jinak, pokus o volání C API bez
      připojeného stavu vlákna skončí fatální chybou nebo nedefinovaným chováním.
      Uživatel může stav vlákna připojit a odpojit výslovně prostřednictvím C API,
      nebo tak může implicitně učinit běhové prostředí, mimo jiné během blokujících
      volání v jazyce C a mezi voláními interpretu bajtkódu.

      Ve většině sestavení Pythonu připojený stav vlákna znamená, že volající
      vlastní :term:`GIL` aktuálního interpretu, takže v jednom okamžiku může mít
      připojený stav vlákna pouze jediné vlákno operačního systému. Ve
      :term:`sestaveních bez GIL <free-threaded build>` mohou vlákna držet
      připojené stavy současně, což umožňuje skutečně paralelní běh interpretu
      bajtkódu.

   attribute
      Hodnota přidružená k objektu, na kterou se obvykle odkazuje jménem pomocí
      tečkového výrazu. Má-li například objekt *o* atribut *a*, odkazuje se na něj
      jako na *o.a*.

      Pokud to objekt umožňuje, lze mu přiřadit atribut, jehož název není
      identifikátorem ve smyslu oddílu :ref:`identifiers`, například pomocí
      :func:`setattr`. Takový atribut nebude dostupný pomocí tečkového výrazu
      a je nutné jej získat funkcí :func:`getattr`.

   awaitable
      Objekt, který lze použít ve výrazu :keyword:`await`. Může jít o
      :term:`korutinu <coroutine>` nebo objekt s metodou
      :meth:`~object.__await__`. Viz také :pep:`492`.

   BDFL
      Benevolent Dictator For Life (doživotní benevolentní diktátor), známý také
      jako `Guido van Rossum <https://gvanrossum.github.io/>`_, tvůrce Pythonu.

   binary file
      :term:`Souborový objekt <file object>`, který dokáže číst a zapisovat
      :term:`objekty podobné bajtům <bytes-like object>`. Příklady binárních
      souborů jsou soubory otevřené v binárním režimu (``'rb'``, ``'wb'`` nebo
      ``'rb+'``), :data:`sys.stdin.buffer <sys.stdin>`,
      :data:`sys.stdout.buffer <sys.stdout>` a instance tříd :class:`io.BytesIO`
      a :class:`gzip.GzipFile`.

      Viz také heslo :term:`textový soubor <text file>`, které popisuje souborový
      objekt schopný číst a zapisovat objekty :class:`str`.

   borrowed reference
      V C API Pythonu je vypůjčený odkaz (borrowed reference) odkaz na objekt,
      který kód používající objekt nevlastní. Pokud je objekt zničen, stane se z
      něj neplatný ukazatel. Úklid paměti může například odstranit poslední
      :term:`silný odkaz <strong reference>` na objekt, a tím objekt zničit.

      S výjimkou případů, kdy objekt nemůže být zničen před posledním použitím
      vypůjčeného odkazu, se doporučuje voláním :c:func:`Py_INCREF` převést
      :term:`vypůjčený odkaz <borrowed reference>` přímo na :term:`silný odkaz
      <strong reference>`. Funkci :c:func:`Py_NewRef` lze použít k vytvoření
      nového :term:`silného odkazu <strong reference>`.

   bytes-like object
      Objekt podporující :ref:`bufferobjects`, který dokáže exportovat
      :term:`souvislou <contiguous>` vyrovnávací paměť jazyka C. Patří sem všechny
      objekty :class:`bytes`, :class:`bytearray` a :class:`array.array` i mnoho
      běžných objektů :class:`memoryview`. Objekty podobné bajtům lze používat při
      různých operacích s binárními daty, mezi něž patří komprese, ukládání do
      binárního souboru a odesílání přes soket.

      Některé operace vyžadují, aby byla binární data měnitelná. Dokumentace je
      často označuje jako „objekty podobné bajtům pro čtení i zápis“. Příklady
      objektů s měnitelnou vyrovnávací pamětí zahrnují :class:`bytearray` a
      :class:`memoryview` objektu :class:`bytearray`. Jiné operace vyžadují
      uložení binárních dat v neměnných objektech („objekty podobné bajtům pouze
      pro čtení“); mezi příklady patří :class:`bytes` a :class:`memoryview`
      objektu :class:`bytes`.

   bytecode
      Zdrojový kód Pythonu se kompiluje do bajtkódu, tedy vnitřní reprezentace
      programu Pythonu v interpretu CPython. Bajtkód se také ukládá do mezipaměti
      v souborech ``.pyc``, takže je druhé spuštění stejného souboru rychlejší
      (není nutné znovu kompilovat zdrojový kód do bajtkódu). Říká se, že tento
      „mezilehlý jazyk“ běží na :term:`virtuálním stroji <virtual machine>`, který
      vykonává strojový kód odpovídající každé instrukci bajtkódu. Bajtkód nemusí
      fungovat mezi různými virtuálními stroji Pythonu ani zůstat stabilní mezi
      jednotlivými vydáními Pythonu.

      Seznam instrukcí bajtkódu najdete v dokumentaci modulu
      :ref:`the dis module <bytecodes>`.

   callable
      Volatelný objekt (callable) je objekt, který lze zavolat, případně se sadou
      argumentů (viz :term:`argument`), pomocí následující syntaxe::

         callable(argument1, argument2, argumentN)

      :term:`Funkce <function>`, a tedy i :term:`metoda <method>`, je volatelným
      objektem. Volatelná je také instance třídy, která implementuje metodu
      :meth:`~object.__call__`.

   callback
      Funkce zpětného volání (callback) je podprogram předaný jako argument,
      který má být spuštěn někdy později.

   class
      Šablona pro vytváření uživatelsky definovaných objektů. Definice třídy
      obvykle obsahuje definice metod, které pracují s instancemi této třídy.

   class variable
      Proměnná definovaná ve třídě, která má být měněna pouze na úrovni třídy
      (nikoli v instanci třídy).

   closure variable
      :term:`Volná proměnná <free variable>`, na kterou odkazuje :term:`vnořený
      obor platnosti <nested scope>` a která je definována ve vnějším oboru
      platnosti, místo aby se za běhu vyhledávala v globálním nebo vestavěném
      jmenném prostoru. Lze ji definovat výslovně pomocí klíčového slova
      :keyword:`nonlocal`, aby do ní bylo možné zapisovat, nebo implicitně,
      pokud se proměnná pouze čte.

      Například ve funkci ``inner`` v následujícím kódu jsou ``x`` i ``print``
      :term:`volné proměnné <free variable>`, ale pouze ``x`` je *proměnná
      uzávěru*::

          def outer():
              x = 0
              def inner():
                  nonlocal x
                  x += 1
                  print(x)
              return inner

      Kvůli atributu :attr:`codeobject.co_freevars` (který navzdory svému názvu
      obsahuje pouze názvy proměnných uzávěru, nikoli seznam všech použitých
      volných proměnných) se někdy používá obecnější pojem :term:`volná proměnná
      <free variable>`, i když se má na mysli konkrétně proměnná uzávěru.

   complex number
      Rozšíření známého systému reálných čísel, v němž je každé číslo vyjádřeno
      jako součet reálné a imaginární části. Imaginární čísla jsou reálnými
      násobky imaginární jednotky (druhé odmocniny z ``-1``), která se v
      matematice často zapisuje jako ``i`` a v technických oborech jako ``j``.
      Python komplexní čísla přímo podporuje a používá druhý z těchto zápisů;
      imaginární část má příponu ``j``, například ``3+1j``. Komplexní obdobu
      modulu :mod:`math` poskytuje modul :mod:`cmath`. Používání komplexních čísel
      je poměrně pokročilá matematická funkce. Pokud nevíte, že je potřebujete,
      téměř jistě je můžete bez obav ignorovat.

   concurrency
      Souběžnost (concurrency) je schopnost počítačového programu zpracovávat
      několik úloh současně. Python poskytuje knihovny pro psaní programů, které
      využívají různé podoby souběžnosti. :mod:`asyncio` slouží k práci s
      asynchronními úlohami a korutinami. :mod:`threading` poskytuje přístup k
      vláknům operačního systému a :mod:`multiprocessing` k jeho procesům.
      Vícejádrové procesory mohou vlákna a procesy provádět současně na různých
      jádrech CPU (viz :term:`paralelismus <parallelism>`).

   concurrent modification
      Situace, kdy několik vláken současně mění sdílená data. Souběžná změna bez
      správné synchronizace může způsobit :term:`souběhy <race condition>` a také
      vyvolat :term:`datový souběh <data race>`, poškození dat nebo obojí.

   context
      Tento pojem má podle místa a způsobu použití různé významy. Mezi běžné
      patří:

      * Dočasný stav nebo prostředí vytvořené :term:`správcem kontextu <context
        manager>` prostřednictvím příkazu :keyword:`with`.
      * Soubor vazeb klíč–hodnota přidružený ke konkrétnímu objektu
        :class:`contextvars.Context` a zpřístupněný prostřednictvím objektů
        :class:`~contextvars.ContextVar`. Viz také :term:`kontextová proměnná
        <context variable>`.
      * Objekt :class:`contextvars.Context`. Viz také :term:`aktuální kontext
        <current context>`.

   context management protocol
      Metody :meth:`~object.__enter__` a :meth:`~object.__exit__`, které volá
      příkaz :keyword:`with`. Viz :pep:`343`.

   context manager
      Objekt, který implementuje :term:`protokol správy kontextu <context
      management protocol>` a řídí prostředí dostupné uvnitř příkazu
      :keyword:`with`. Viz :pep:`343`.

   context variable
      Proměnná, jejíž hodnota závisí na tom, který kontext je :term:`aktuální
      <current context>`. K hodnotám se přistupuje prostřednictvím objektů
      :class:`contextvars.ContextVar`. Kontextové proměnné se používají především
      k oddělení stavu mezi souběžnými asynchronními úlohami.

   contiguous
      .. index:: C-contiguous, Fortran contiguous

      Vyrovnávací paměť se považuje za souvislou právě tehdy, když je souvislá
      podle jazyka C (*C-contiguous*) nebo podle Fortranu (*Fortran contiguous*).
      Nulově rozměrné vyrovnávací paměti jsou souvislé podle C i Fortranu. V
      jednorozměrných polích musí být prvky uloženy v paměti vedle sebe v pořadí
      rostoucích indexů počínaje nulou. Při průchodu prvky vícerozměrného pole
      souvislého podle C v pořadí jejich adres v paměti se nejrychleji mění
      poslední index. U polí souvislých podle Fortranu se naopak nejrychleji mění
      první index.

   coroutine
      Korutiny jsou obecnější podobou podprogramů. Do podprogramu se vstupuje v
      jednom bodě a v jiném se opouští. Do korutiny lze vstoupit, opustit ji a
      pokračovat v ní na mnoha různých místech. Lze je implementovat příkazem
      :keyword:`async def`. Viz také :pep:`492`.

   coroutine function
      Funkce, která vrací objekt :term:`korutiny <coroutine>`. Korutinovou funkci
      lze definovat příkazem :keyword:`async def` a může obsahovat klíčová slova
      :keyword:`await`, :keyword:`async for` a :keyword:`async with`. Ta byla
      zavedena v :pep:`492`.

   CPython
      Kanonická implementace programovacího jazyka Python distribuovaná na
      webu `python.org <https://www.python.org>`_. Pojem „CPython“ se používá,
      když je tuto implementaci nutné odlišit od jiných, například Jythonu nebo
      IronPythonu.

   current context
      :term:`Kontext <context>` (objekt :class:`contextvars.Context`), který
      objekty :class:`~contextvars.ContextVar` právě používají k přístupu
      (získání nebo nastavení) k hodnotám :term:`kontextových proměnných <context
      variable>`. Každé vlákno má vlastní aktuální kontext. Frameworky pro
      spouštění asynchronních úloh (viz :mod:`asyncio`) přidružují každé úloze
      kontext, který se stane aktuálním, kdykoli úloha zahájí provádění nebo v
      něm pokračuje.

   cyclic isolate
      Podskupina jednoho nebo více objektů, které na sebe navzájem odkazují v
      cyklu odkazů, ale neodkazuje na ně žádný objekt mimo skupinu. Cílem
      :term:`cyklického úklidu paměti <garbage collection>` je tyto skupiny
      rozpoznat a přerušit cykly odkazů, aby bylo možné paměť uvolnit.

   data race
      Situace, kdy několik vláken současně přistupuje ke stejnému místu v paměti,
      alespoň jeden z těchto přístupů je zápis a vlákna svůj přístup neřídí
      žádnou synchronizací. Datové souběhy vedou k :term:`nedeterministickému
      <non-deterministic>` chování a mohou způsobit poškození dat. Správné použití
      :term:`zámků <lock>` a dalších :term:`synchronizačních primitiv
      <synchronization primitive>` datovým souběhům zabraňuje. Datový souběh může
      nastat pouze v nativním kódu, ale :term:`nativní kód <native code>` může být
      zpřístupněn prostřednictvím API Pythonu. Viz také :term:`souběh <race
      condition>` a :term:`bezpečnost ve více vláknech <thread-safe>`.

   deadlock
      Situace, kdy dvě nebo více úloh (vláken, procesů či korutin) čeká neomezeně
      dlouho, až ostatní uvolní prostředky nebo dokončí činnost, takže žádná z
      nich nemůže pokračovat. Pokud například vlákno A drží zámek 1 a čeká na
      zámek 2, zatímco vlákno B drží zámek 2 a čeká na zámek 1, budou obě čekat
      neomezeně dlouho. V Pythonu tato situace často vzniká získáváním více zámků
      v rozporném pořadí nebo cyklickými závislostmi join/await. Uváznutí lze
      zabránit tím, že se více :term:`zámků <lock>` získává vždy ve stejném
      pořadí. Viz také :term:`zámek <lock>` a :term:`reentrantní <reentrant>`.

   decorator
      Funkce vracející jinou funkci, která se obvykle používá k transformaci
      funkce pomocí syntaxe ``@wrapper``. Běžnými příklady dekorátorů jsou
      :func:`classmethod` a :func:`staticmethod`.

      Syntaxe dekorátoru je pouze syntaktický cukr; následující dvě definice
      funkcí jsou významově rovnocenné::

         def f(arg):
             ...
         f = staticmethod(f)

         @staticmethod
         def f(arg):
             ...

      Stejný koncept existuje také pro třídy, u nich se však používá méně často.
      Více informací o dekorátorech najdete v dokumentaci :ref:`definic funkcí
      <function>` a :ref:`definic tříd <class>`.

   descriptor
      Libovolný objekt definující metody :meth:`~object.__get__`,
      :meth:`~object.__set__` nebo :meth:`~object.__delete__`. Je-li atribut třídy
      deskriptorem, při vyhledávání atributu se aktivuje jeho zvláštní chování
      při vazbě. Při získání, nastavení nebo odstranění atributu pomocí *a.b* se
      obvykle ve slovníku třídy objektu *a* vyhledá objekt pojmenovaný *b*. Je-li
      však *b* deskriptorem, zavolá se příslušná metoda deskriptoru. Porozumění
      deskriptorům je klíčem k hlubšímu pochopení Pythonu, protože tvoří základ
      mnoha vlastností včetně funkcí, metod, vlastností, třídních a statických
      metod a odkazů na nadřazené třídy.

      Více informací o metodách deskriptorů najdete v oddílu :ref:`descriptors`
      nebo v :ref:`návodu k deskriptorům <descriptorhowto>`.

   dictionary
      Asociativní pole, v němž jsou libovolné klíče mapovány na hodnoty. Klíčem
      může být jakýkoli objekt s metodami :meth:`~object.__hash__` a
      :meth:`~object.__eq__`. V Perlu se nazývá hash.

   dictionary comprehension
      Stručný způsob, jak zpracovat všechny nebo některé prvky iterovatelného
      objektu a vrátit slovník s výsledky. ``results = {n: n ** 2 for n in
      range(10)}`` vytvoří slovník, v němž je klíč ``n`` mapován na hodnotu
      ``n ** 2``. Viz :ref:`comprehensions`.

   dictionary view
      Objekty vracené metodami :meth:`dict.keys`, :meth:`dict.values` a
      :meth:`dict.items` se nazývají pohledy na slovník. Poskytují dynamický
      pohled na položky slovníku, takže se v nich projeví každá změna slovníku.
      Chcete-li pohled na slovník převést na úplný seznam, použijte
      ``list(dictview)``. Viz :ref:`dict-views`.

   docstring
      Řetězcový literál uvedený jako první výraz ve třídě, funkci nebo modulu.
      Při provádění bloku příkazů je sice ignorován, kompilátor jej však rozpozná
      a uloží do atributu :attr:`~definition.__doc__` příslušné třídy, funkce nebo
      modulu. Protože je dostupný prostřednictvím introspekce, představuje
      obvyklé místo pro dokumentaci objektu.

   duck-typing
      Programátorský styl, který při rozhodování, zda objekt poskytuje správné
      rozhraní, nezkoumá jeho typ; místo toho se příslušná metoda či atribut
      jednoduše zavolá nebo použije („Pokud to vypadá jako kachna a kváká jako
      kachna, musí to být kachna.“). Důrazem na rozhraní namísto konkrétních typů
      zvyšuje dobře navržený kód svou pružnost, protože umožňuje polymorfní
      záměnu. Kachní typování se vyhýbá testům pomocí :func:`type` nebo
      :func:`isinstance`. (Lze je však doplnit :term:`abstraktními základními
      třídami <abstract base class>`.) Místo toho obvykle využívá testy funkcí
      :func:`hasattr` nebo programátorský styl :term:`EAFP`.

   dunder
      Neformální zkratka anglického „double underscore“ (dvojité podtržítko),
      používaná při hovoru o :term:`speciálních metodách <special method>`.
      Například ``__init__`` se často vyslovuje „dunder init“.

   EAFP
      „Je snazší požádat o odpuštění než o svolení“ (Easier to ask for
      forgiveness than permission). Tento běžný styl programování v Pythonu
      předpokládá existenci platných klíčů nebo atributů a zachytí výjimku, pokud
      se předpoklad ukáže jako chybný. Tento čistý a rychlý styl se vyznačuje
      častým používáním příkazů :keyword:`try` a :keyword:`except`. Je opakem
      stylu :term:`LBYL`, běžného v mnoha jiných jazycích, například v C.

   evaluate function
      Funkce, kterou lze zavolat k vyhodnocení líně vyhodnocovaného atributu
      objektu, například hodnoty aliasů typů vytvořených příkazem :keyword:`type`.

   expression
      Část syntaxe, kterou lze vyhodnotit na určitou hodnotu. Jinými slovy je
      výraz složen z prvků, jako jsou literály, názvy, přístupy k atributům,
      operátory nebo volání funkcí, které všechny vracejí hodnotu. Na rozdíl od
      mnoha jiných jazyků nejsou všechny jazykové konstrukce výrazy. Existují
      také :term:`příkazy <statement>`, které jako výrazy použít nelze, například
      :keyword:`while`. Také přiřazení jsou příkazy, nikoli výrazy.

   extension module
      Modul napsaný v C nebo C++, který ke komunikaci s jádrem Pythonu a
      uživatelským kódem používá C API Pythonu.

   f-string
   f-strings
      Řetězcové literály s předponou ``f`` nebo ``F`` se běžně nazývají
      „f-řetězce“, což je zkrácený název pro :ref:`formátované řetězcové literály
      <f-strings>`. Viz také :pep:`498`.

   file object
      Objekt, který nad podkladovým prostředkem poskytuje souborově orientované
      API (s metodami jako :meth:`!read` nebo :meth:`!write`). Podle způsobu svého
      vytvoření může souborový objekt zprostředkovávat přístup ke skutečnému
      souboru na disku nebo k jinému typu úložiště či komunikačního zařízení
      (například standardnímu vstupu a výstupu, vyrovnávací paměti, soketu,
      rouře apod.). Souborové objekty se také nazývají :dfn:`objekty podobné
      souborům` nebo :dfn:`proudy`.

      Ve skutečnosti existují tři kategorie souborových objektů: nezpracované
      :term:`binární soubory <binary file>`, :term:`binární soubory s vyrovnávací
      pamětí <binary file>` a :term:`textové soubory <text file>`. Jejich rozhraní
      definuje modul :mod:`io`. Obvyklým způsobem vytvoření souborového objektu
      je použití funkce :func:`open`.

   file-like object
      Synonymum pro :term:`souborový objekt <file object>`.

   filesystem encoding and error handler
      Kódování a obsluha chyb, které Python používá k dekódování bajtů přijatých
      od operačního systému a ke kódování Unicode předávaného operačnímu systému.

      Kódování souborového systému musí zaručit úspěšné dekódování všech bajtů
      menších než 128. Pokud tuto záruku neposkytuje, mohou funkce API vyvolat
      výjimku :exc:`UnicodeError`.

      Kódování souborového systému a jeho obsluhu chyb lze zjistit funkcemi
      :func:`sys.getfilesystemencoding` a :func:`sys.getfilesystemencodeerrors`.

      :term:`Kódování souborového systému a obsluha chyb <filesystem encoding
      and error handler>` se při spuštění Pythonu nastavují funkcí
      :c:func:`PyConfig_Read`; viz členy :c:member:`~PyConfig.filesystem_encoding`
      a :c:member:`~PyConfig.filesystem_errors` typu :c:type:`PyConfig`.

      Viz také :term:`kódování místního prostředí <locale encoding>`.

   finder
      Objekt, který se pokouší nalézt :term:`zavaděč <loader>` importovaného
      modulu.

      Existují dva druhy vyhledávačů: :term:`vyhledávače metacesty <meta path
      finder>` používané s :data:`sys.meta_path` a :term:`vyhledávače položek
      cesty <path entry finder>` používané s :data:`sys.path_hooks`.

      Mnohem podrobnější informace uvádí oddíl :ref:`finders-and-loaders` a
      dokumentace modulu :mod:`importlib`.

   floor division
      Matematické dělení, které zaokrouhluje dolů na nejbližší celé číslo.
      Operátorem celočíselného dělení je ``//``. Výraz ``11 // 4`` se například
      vyhodnotí jako ``2``, na rozdíl od hodnoty ``2.75`` vrácené skutečným
      dělením čísel s plovoucí desetinnou čárkou. Všimněte si, že ``(-11) // 4``
      je ``-3``, protože jde o hodnotu ``-2.75`` zaokrouhlenou *dolů*. Viz
      :pep:`238`.

   free threading
      Model vláken, v němž může několik vláken současně provádět bajtkód Pythonu
      v témže interpretu. Je opakem modelu s :term:`globálním zámkem interpretu
      <global interpreter lock>`, který dovoluje provádět bajtkód Pythonu vždy
      pouze jednomu vláknu. Viz :pep:`703`.

   free-threaded build

      Sestavení :term:`CPythonu <CPython>`, které podporuje :term:`běh bez GIL
      <free threading>` a před kompilací bylo nakonfigurováno volbou
      :option:`--disable-gil`.

      Viz :ref:`freethreading-python-howto`.

   free variable
      Formálně je podle :ref:`modelu provádění jazyka <bind_names>` volnou
      proměnnou každá proměnná použitá ve jmenném prostoru, která v něm není
      místní proměnnou. Příklad uvádí heslo :term:`proměnná uzávěru <closure
      variable>`. V praxi se tento pojem kvůli názvu atributu
      :attr:`codeobject.co_freevars` někdy používá také jako synonymum pro
      :term:`proměnnou uzávěru <closure variable>`.

   function
      Posloupnost příkazů, která volajícímu vrací určitou hodnotu. Lze jí také
      předat nula nebo více :term:`argumentů <argument>`, které mohou být použity
      při provádění těla funkce. Viz také :term:`parametr <parameter>`,
      :term:`metoda <method>` a oddíl :ref:`function`.

   function annotation
      :term:`Anotace <annotation>` parametru nebo návratové hodnoty funkce.

      Anotace funkcí se obvykle používají pro :term:`typové nápovědy <type
      hint>`: od následující funkce se například očekává, že přijme dva argumenty
      typu :class:`int` a vrátí rovněž hodnotu typu :class:`int`::

         def sum_two_numbers(a: int, b: int) -> int:
            return a + b

      Syntaxi anotací funkcí vysvětluje oddíl :ref:`function`.

      Tuto funkcionalitu popisuje také heslo :term:`anotace proměnné <variable
      annotation>` a :pep:`484`. Doporučené postupy pro práci s anotacemi uvádí
      :ref:`annotations-howto`.

   __future__
      :ref:`Příkaz future <future>`, ``from __future__ import <feature>``, nařídí
      kompilátoru zkompilovat aktuální modul se syntaxí nebo sémantikou, která se
      stane standardem v některém budoucím vydání Pythonu. Modul
      :mod:`__future__` dokumentuje možné hodnoty *feature*. Importem tohoto
      modulu a vyhodnocením jeho proměnných lze zjistit, kdy byla nová vlastnost
      poprvé přidána do jazyka a kdy se stane (nebo stala) výchozí::

         >>> import __future__
         >>> __future__.division
         _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

   garbage collection
      Proces uvolňování paměti, která již není používána. Python uklízí paměť
      pomocí počítání odkazů a cyklického úklidu, který dokáže rozpoznat a
      přerušit cykly odkazů. Úklid paměti lze řídit modulem :mod:`gc`.

      .. index:: single: generator

   generator
      Funkce, která vrací :term:`iterátor generátoru <generator iterator>`.
      Vypadá jako běžná funkce, obsahuje však výrazy :keyword:`yield`, které
      vytvářejí řadu hodnot použitelnou v cyklu for nebo získávanou po jedné
      funkcí :func:`next`.

      Pojem obvykle označuje funkci generátoru, v některých souvislostech však
      může znamenat *iterátor generátoru*. Není-li zamýšlený význam zřejmý,
      použití úplných názvů zabrání nejednoznačnosti.

   generator iterator
      Objekt vytvořený funkcí :term:`generátoru <generator>`.

      Každý :keyword:`yield` dočasně pozastaví zpracování a zapamatuje si stav
      provádění (včetně místních proměnných a nedokončených příkazů try). Když
      *iterátor generátoru* pokračuje, naváže tam, kde skončil (na rozdíl od
      funkcí, které při každém volání začínají znovu).

      .. index:: single: generator expression

   generator expression
      :term:`Výraz <expression>`, který vrací :term:`iterátor <iterator>`. Vypadá
      jako běžný výraz následovaný klauzulí :keyword:`!for`, jež definuje řídicí
      proměnnou cyklu a rozsah, a volitelnou klauzulí :keyword:`!if`. Celý výraz
      vytváří hodnoty pro obklopující funkci::

         >>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
         285

   generic function
      Funkce složená z více funkcí, které implementují stejnou operaci pro různé
      typy. O tom, která implementace se při volání použije, rozhoduje algoritmus
      výběru.

      Viz také heslo :term:`jednoduchý výběr <single dispatch>`, dekorátor
      :func:`functools.singledispatch` a :pep:`443`.

   generic type
      :term:`Typ <type>`, který lze parametrizovat; obvykle jde o
      :ref:`kontejnerovou třídu <sequence-types>`, například :class:`list` nebo
      :class:`dict`. Používá se pro :term:`typové nápovědy <type hint>` a
      :term:`anotace <annotation>`.

      Podrobnosti uvádějí :ref:`typy generických aliasů <types-genericalias>`,
      :pep:`483`, :pep:`484`, :pep:`585` a modul :mod:`typing`.

   GIL
      Viz :term:`globální zámek interpretu <global interpreter lock>`.

   global interpreter lock
      Mechanismus, kterým interpret :term:`CPythonu <CPython>` zajišťuje, aby
      :term:`bajtkód <bytecode>` Pythonu provádělo vždy pouze jedno vlákno.
      Zjednodušuje implementaci CPythonu tím, že objektový model (včetně
      zásadních vestavěných typů, jako je :class:`dict`) implicitně chrání před
      souběžným přístupem. Uzamčení celého interpretu usnadňuje jeho použití ve
      více vláknech, avšak za cenu velké části paralelismu, který nabízejí
      víceprocesorové počítače.

      Některé standardní i externí rozšiřující moduly jsou však navrženy tak,
      aby GIL uvolnily při výpočetně náročných úlohách, například při kompresi
      nebo hašování. GIL se také vždy uvolňuje při vstupu a výstupu.

      Od Pythonu 3.13 lze GIL zakázat konfigurační volbou sestavení
      :option:`--disable-gil`. Po sestavení Pythonu s touto volbou je nutné kód
      spustit s volbou :option:`-X gil=0 <-X>` nebo po nastavení proměnné prostředí
      :envvar:`PYTHON_GIL=0 <PYTHON_GIL>`. Tato vlastnost zvyšuje výkon
      vícevláknových aplikací a usnadňuje efektivní využití vícejádrových CPU.
      Podrobnosti uvádí :pep:`703`.

      Ve starších verzích C API Pythonu mohla funkce uvádět, že k jejímu použití
      musí být držen GIL. Tím se rozumí existence :term:`připojeného stavu vlákna
      <attached thread state>`.

   global state
      Data dostupná v celém programu, například proměnné na úrovni modulu,
      třídní proměnné nebo statické proměnné jazyka C v :term:`rozšiřujících
      modulech <extension module>`. Ve vícevláknových programech globální stav
      sdílený mezi vlákny obvykle vyžaduje synchronizaci, aby se zabránilo
      :term:`souběhům <race condition>` a :term:`datovým souběhům <data race>`.

   hash-based pyc
      Soubor mezipaměti bajtkódu, který svou platnost určuje podle hodnoty hash
      odpovídajícího zdrojového souboru namísto času jeho poslední změny. Viz
      :ref:`pyc-invalidation`.

   hashable
      Objekt je *hašovatelný*, pokud má hodnotu hash, která se po celou dobu jeho
      existence nemění (vyžaduje metodu :meth:`~object.__hash__`), a lze jej
      porovnávat s jinými objekty (vyžaduje metodu :meth:`~object.__eq__`).
      Hašovatelné objekty, které se porovnají jako shodné, musí mít stejnou
      hodnotu hash.

      Díky hašovatelnosti lze objekt použít jako klíč slovníku nebo prvek množiny,
      protože tyto datové struktury interně používají hodnotu hash.

      Většina neměnných vestavěných objektů Pythonu je hašovatelná; měnitelné
      kontejnery (například seznamy či slovníky) nikoli. Neměnné kontejnery
      (například n-tice a zmrazené množiny) jsou hašovatelné pouze tehdy, jsou-li
      hašovatelné jejich prvky. Instance uživatelsky definovaných tříd jsou ve
      výchozím nastavení hašovatelné. Všechny se porovnají jako různé (s výjimkou
      porovnání se sebou samými) a jejich hodnota hash je odvozena z jejich
      :func:`id`.

   IDLE
      Integrované vývojové a výukové prostředí (Integrated Development and
      Learning Environment) pro Python. :ref:`idle` je základní prostředí editoru
      a interpretu dodávané se standardní distribucí Pythonu.

   immortal
      *Nesmrtelné objekty* jsou implementačním detailem CPythonu zavedeným v
      :pep:`683`.

      Je-li objekt nesmrtelný, jeho :term:`počet odkazů <reference count>` se
      nikdy nemění, a proto se za běhu interpretu nikdy neuvolní. V CPythonu jsou
      nesmrtelné například :const:`True` a :const:`None`.

      Nesmrtelné objekty lze rozpoznat funkcí :func:`sys._is_immortal` nebo v C
      API funkcí :c:func:`PyUnstable_IsImmortal`.

   immutable
      Objekt s pevnou hodnotou. Mezi neměnné objekty patří čísla, řetězce a
      n-tice. Takový objekt nelze změnit; má-li být uložena jiná hodnota, musí se
      vytvořit nový objekt. Neměnné objekty hrají důležitou roli tam, kde je
      zapotřebí stálá hodnota hash, například jako klíče slovníku. Ze své podstaty
      jsou :term:`bezpečné ve více vláknech <thread-safe>`, protože jejich stav
      nelze po vytvoření změnit, čímž odpadají obavy z nesprávně synchronizované
      :term:`souběžné změny <concurrent modification>`.

   import path
      Seznam umístění (neboli :term:`položek cesty <path entry>`), v nichž
      :term:`vyhledávač založený na cestě <path based finder>` hledá moduly k
      importu. Při importu tento seznam obvykle pochází z :data:`sys.path`, u
      podbalíčků však může pocházet také z atributu ``__path__`` nadřazeného
      balíčku.

   importing
      Proces, kterým se kód Pythonu z jednoho modulu zpřístupní kódu Pythonu v
      jiném modulu.

   importer
      Objekt, který modul vyhledává i načítá; je tedy zároveň
      :term:`vyhledávačem <finder>` i :term:`zavaděčem <loader>`.

   index
      Číselná hodnota představující pozici prvku v :term:`posloupnosti
      <sequence>`.

      Indexování v Pythonu začíná nulou. Například ``things[0]`` označuje *první*
      prvek objektu ``things`` a ``things[1]`` jeho druhý prvek.

      V některých souvislostech Python umožňuje záporné indexy pro počítání od
      konce posloupnosti a indexování pomocí :term:`výřezů <slice>`.

      Viz také :term:`indexování <subscript>`.

   interactive
      Python má interaktivní interpret, což znamená, že do jeho výzvy můžete
      zadávat příkazy a výrazy, okamžitě je spouštět a prohlížet si výsledky.
      Stačí spustit ``python`` bez argumentů (případně jej vybrat v hlavní nabídce
      počítače). Jde o velmi účinný způsob zkoušení nových myšlenek a prohlížení
      modulů a balíčků (nezapomeňte na ``help(x)``). Více o interaktivním režimu
      uvádí oddíl :ref:`tut-interac`.

   interpreted
      Python je interpretovaný jazyk, nikoli kompilovaný, přestože kompilátor
      bajtkódu tuto hranici poněkud stírá. Zdrojové soubory tedy lze spouštět
      přímo, aniž by bylo nutné výslovně vytvořit a poté spustit samostatný
      spustitelný soubor. Interpretované jazyky mají obvykle kratší cyklus vývoje
      a ladění než jazyky kompilované, jejich programy však zpravidla běží
      pomaleji. Viz také :term:`interaktivní režim <interactive>`.

   interpreter shutdown
      Když interpret Pythonu obdrží požadavek na ukončení, vstoupí do zvláštní
      fáze, v níž postupně uvolňuje všechny přidělené prostředky, například
      moduly a různé zásadní vnitřní struktury. Také několikrát zavolá
      :term:`úklid paměti <garbage collection>`. To může spustit kód v
      uživatelsky definovaných destruktorech nebo funkcích zpětného volání slabých
      odkazů. Kód prováděný během ukončování může narazit na různé výjimky,
      protože prostředky, na něž spoléhá, již nemusí fungovat (běžnými příklady
      jsou knihovní moduly nebo mechanismus varování).

      Hlavním důvodem ukončení interpretu je dokončení modulu ``__main__`` nebo
      právě spuštěného skriptu.

   iterable
      Objekt schopný vracet své prvky jeden po druhém. Mezi iterovatelné objekty
      patří všechny typy posloupností (například :class:`list`, :class:`str` a
      :class:`tuple`) a některé neposloupnostní typy, jako je :class:`dict`,
      :term:`souborové objekty <file object>` a objekty libovolných vámi
      definovaných tříd s metodou :meth:`~object.__iter__` nebo metodou
      :meth:`~object.__getitem__`, která implementuje sémantiku :term:`posloupnosti
      <sequence>`.

      Iterovatelné objekty lze používat v cyklu :keyword:`for` a na mnoha dalších
      místech, kde je zapotřebí posloupnost (:func:`zip`, :func:`map`, ...).
      Předáte-li iterovatelný objekt vestavěné funkci :func:`iter` jako argument,
      vrátí pro tento objekt iterátor. Ten lze použít k jednomu průchodu sadou
      hodnot. Při práci s iterovatelnými objekty obvykle není nutné volat
      :func:`iter` ani se o iterátory starat ručně. Příkaz :keyword:`for` to udělá
      automaticky a po dobu cyklu vytvoří dočasnou nepojmenovanou proměnnou pro
      uložení iterátoru. Viz také :term:`iterátor <iterator>`, :term:`posloupnost
      <sequence>` a :term:`generátor <generator>`.

   iterator
      Objekt představující proud dat. Opakovaná volání metody iterátoru
      :meth:`~iterator.__next__` (nebo jeho předávání vestavěné funkci
      :func:`next`) vracejí postupně další položky proudu. Když již nejsou žádná
      data k dispozici, vyvolá se místo toho výjimka :exc:`StopIteration`. V tom
      okamžiku je iterátor vyčerpán a každé další volání jeho metody
      :meth:`!__next__` pouze znovu vyvolá :exc:`StopIteration`. Iterátory musí mít
      metodu :meth:`~iterator.__iter__`, která vrací samotný objekt iterátoru.
      Každý iterátor je tedy zároveň iterovatelný a lze jej použít na většině
      míst, která přijímají jiné iterovatelné objekty. Významnou výjimkou je kód,
      který se pokouší provést více průchodů. Kontejnerový objekt (například
      :class:`list`) vytvoří nový iterátor pokaždé, když jej předáte funkci
      :func:`iter` nebo použijete v cyklu :keyword:`for`. Stejný pokus s
      iterátorem pouze vrátí již vyčerpaný objekt iterátoru použitý při předchozím
      průchodu, takže se bude jevit jako prázdný kontejner.

      Více informací najdete v oddílu :ref:`typeiter`.

      .. impl-detail::

         CPython neuplatňuje důsledně požadavek, aby iterátor definoval metodu
         :meth:`~iterator.__iter__`. Také mějte na paměti, že :term:`CPython bez
         GIL <free threading>` nezaručuje :term:`bezpečné chování ve více
         vláknech <thread-safe>` při operacích s iterátory.

   key
      Hodnota, která určuje položku v :term:`mapování <mapping>`.
      Viz také :term:`indexování <subscript>`.

   key function
      Funkce klíče neboli porovnávací funkce je volatelný objekt, který vrací
      hodnotu používanou k řazení nebo uspořádání. Funkce
      :func:`locale.strxfrm` například vytváří klíč řazení zohledňující pravidla
      řazení daného místního prostředí.

      Řada nástrojů Pythonu přijímá funkce klíče, jimiž lze řídit řazení či
      seskupování prvků. Patří mezi ně :func:`min`, :func:`max`, :func:`sorted`,
      :meth:`list.sort`, :func:`heapq.merge`, :func:`heapq.nsmallest`,
      :func:`heapq.nlargest` a :func:`itertools.groupby`.

      Funkci klíče lze vytvořit několika způsoby. Například metoda
      :meth:`str.casefold` může sloužit jako funkce klíče pro řazení bez ohledu
      na velikost písmen. Funkci klíče lze také sestavit z výrazu
      :keyword:`lambda`, například ``lambda r: (r[0], r[2])``. Dalšími třemi
      konstruktory funkcí klíče jsou :func:`operator.attrgetter`,
      :func:`operator.itemgetter` a :func:`operator.methodcaller`. Příklady
      vytváření a používání funkcí klíče uvádí :ref:`návod k řazení
      <sortinghowto>`.

   keyword argument
      Viz :term:`argument`.

   lambda
      Anonymní funkce zapsaná přímo na místě, která se skládá z jediného
      :term:`výrazu <expression>` vyhodnoceného při volání funkce. Syntaxe pro
      vytvoření lambda funkce je ``lambda [parameters]: expression``.

   LBYL
      „Dvakrát měř, jednou řež“ (Look before you leap). Tento styl programování
      před voláním nebo vyhledáváním výslovně testuje vstupní podmínky. Je opakem
      přístupu :term:`EAFP` a vyznačuje se častým používáním příkazů
      :keyword:`if`.

      Ve vícevláknovém prostředí může přístup LBYL způsobit :term:`souběh <race
      condition>` mezi „měřením“ a „řezáním“. Například kód ``if key in mapping: return mapping[key]``
      může selhat, pokud jiné vlákno po testu, ale před
      vyhledáním odstraní *key* z *mapping*. Problém lze vyřešit pomocí
      :term:`zámků <lock>` nebo přístupem :term:`EAFP`. Viz také
      :term:`bezpečnost ve více vláknech <thread-safe>`.

   lexical analyzer

      Formální název pro *tokenizér*; viz :term:`token`.

   list
      Vestavěná :term:`posloupnost <sequence>` Pythonu. Navzdory svému názvu se
      více podobá poli v jiných jazycích než spojovému seznamu, protože přístup k
      prvkům má složitost *O*\ (1).

   list comprehension
      Stručný způsob zpracování všech nebo některých prvků posloupnosti a vrácení
      seznamu s výsledky. ``result = ['{:#04x}'.format(x) for x in
      range(256) if x % 2 == 0]`` vytvoří seznam řetězců obsahujících sudá šestnáctková čísla
      (0x..) v rozsahu od 0 do 255. Klauzule :keyword:`if` je volitelná. Pokud ji
      vynecháte, zpracují se všechny prvky v ``range(256)``.

   lock
      :term:`Synchronizační primitivum <synchronization primitive>`, které
      umožňuje přístup ke sdílenému prostředku vždy pouze jednomu vláknu. Vlákno
      musí před přístupem k chráněnému prostředku zámek získat a poté jej uvolnit.
      Pokusí-li se vlákno získat zámek, který již drží jiné vlákno, zablokuje se,
      dokud nebude zámek dostupný. Modul :mod:`threading` poskytuje třídu
      :class:`~threading.Lock` (základní zámek) a :class:`~threading.RLock`
      (:term:`reentrantní <reentrant>` zámek). Zámky slouží k zabránění
      :term:`souběhům <race condition>` a zajištění :term:`bezpečného
      <thread-safe>` přístupu ke sdíleným datům z více vláken. Existují také jiné
      návrhové vzory, například fronty, vzor producent–konzument a stav místní
      pro vlákno. Viz také :term:`uváznutí <deadlock>` a :term:`reentrantní
      <reentrant>`.

   lock-free
      Operace, která nezískává žádný :term:`zámek <lock>` a správnost zajišťuje
      atomickými instrukcemi CPU. Operace bez zámků lze provádět souběžně, aniž
      by se navzájem blokovaly, a nemohou je zablokovat operace držící zámky. V
      :term:`Pythonu bez GIL <free threading>` poskytují vestavěné typy, jako jsou
      :class:`dict` a :class:`list`, čtecí operace bez zámku. Jiná vlákna proto
      mohou během vícekrokových změn pozorovat mezilehlé stavy, i když tyto změny
      drží :term:`zámek objektu <per-object lock>`.

   loader
      Objekt, který načítá modul. Musí definovat metody :meth:`!exec_module` a
      :meth:`!create_module`, aby implementoval rozhraní
      :class:`~importlib.abc.Loader`. Zavaděč obvykle vrací :term:`vyhledávač
      <finder>`.
      Viz také:

      * :ref:`finders-and-loaders`
      * :class:`importlib.abc.Loader`
      * :pep:`302`

   locale encoding
      V Unixu jde o kódování místního prostředí LC_CTYPE. Lze je nastavit funkcí
      :func:`locale.setlocale(locale.LC_CTYPE, new_locale) <locale.setlocale>`.

      Ve Windows jde o kódovou stránku ANSI (například ``"cp1252"``).

      V systémech Android a VxWorks používá Python jako kódování místního
      prostředí ``"utf-8"``.

      Kódování místního prostředí lze zjistit funkcí :func:`locale.getencoding`.

      Viz také :term:`kódování souborového systému a obsluha chyb <filesystem
      encoding and error handler>`.

   magic method
      .. index:: pair: magic; method

      Neformální synonymum pro :term:`speciální metodu <special method>`.

   mapping
      Kontejnerový objekt, který podporuje vyhledávání libovolných klíčů a
      implementuje metody určené abstraktními základními třídami
      :class:`collections.abc.Mapping` nebo :class:`collections.abc.MutableMapping`;
      viz :ref:`collections-abstract-base-classes`. Příklady zahrnují :class:`dict`,
      :class:`collections.defaultdict`, :class:`collections.OrderedDict` a
      :class:`collections.Counter`.

   meta path finder
      :term:`Vyhledávač <finder>` vrácený při prohledávání :data:`sys.meta_path`.
      Vyhledávače metacesty souvisejí s :term:`vyhledávači položek cesty <path
      entry finder>`, ale liší se od nich.

      Metody implementované vyhledávači metacesty uvádí dokumentace třídy
      :class:`importlib.abc.MetaPathFinder`.

   metaclass
      Třída třídy. Definice třídy vytváří název třídy, slovník třídy a seznam
      základních tříd. Metatřída přijme tyto tři argumenty a vytvoří z nich třídu.
      Většina objektově orientovaných jazyků poskytuje výchozí implementaci.
      Python se odlišuje možností vytvářet vlastní metatřídy. Většina uživatelů
      tento nástroj nikdy nepotřebuje, pokud však potřeba nastane, mohou metatřídy
      nabídnout účinná a elegantní řešení. Používají se například k zaznamenávání
      přístupu k atributům, zajištění bezpečnosti ve více vláknech, sledování
      vytváření objektů, implementaci jedináčků a mnoha dalším úlohám.

      Více informací najdete v oddílu :ref:`metaclasses`.

   method
      Funkce definovaná uvnitř těla třídy. Je-li zavolána jako atribut instance
      této třídy, obdrží objekt instance jako svůj první :term:`argument`
      (obvykle nazývaný ``self``). Viz :term:`funkce <function>` a
      :term:`vnořený obor platnosti <nested scope>`.

   method resolution order
      Pořadí rozlišení metod (Method Resolution Order, MRO) je pořadí, v němž se
      při vyhledávání člena procházejí základní třídy. Podrobnosti algoritmu
      používaného interpretem Pythonu od vydání 2.3 uvádí
      :ref:`python_2.3_mro`.

   module
      Objekt sloužící jako organizační jednotka kódu Pythonu. Moduly mají jmenný
      prostor obsahující libovolné objekty Pythonu. Do Pythonu se načítají
      procesem :term:`importu <importing>`.

      Viz také :term:`balíček <package>`.

   module spec
      Jmenný prostor obsahující informace o importu používané k načtení modulu.
      Jde o instanci :class:`importlib.machinery.ModuleSpec`.

      Viz také :ref:`module-specs`.

   MRO
      Viz :term:`pořadí rozlišení metod <method resolution order>`.

   mutable
      :term:`Objekt <object>`, jehož stav se může během programu měnit. Ve
      vícevláknových programech vyžadují měnitelné objekty sdílené mezi vlákny
      pečlivou synchronizaci, aby se zabránilo :term:`souběhům <race condition>`.
      Viz také :term:`neměnný <immutable>`, :term:`bezpečný ve více vláknech
      <thread-safe>` a :term:`souběžná změna <concurrent modification>`.

   named tuple
      Pojem „pojmenovaná n-tice“ označuje libovolný typ nebo třídu odvozenou od
      n-tice, k jejímž indexovatelným prvkům lze přistupovat také pojmenovanými
      atributy. Typ nebo třída může mít i další vlastnosti.

      Pojmenovanými n-ticemi je několik vestavěných typů včetně hodnot vracených
      funkcemi :func:`time.localtime` a :func:`os.stat`. Dalším příkladem je
      :data:`sys.float_info`::

           >>> sys.float_info[1]                   # indexed access
           1024
           >>> sys.float_info.max_exp              # named field access
           1024
           >>> isinstance(sys.float_info, tuple)   # kind of tuple
           True

      Některé pojmenované n-tice jsou vestavěnými typy (jako příklady výše).
      Pojmenovanou n-tici lze také vytvořit běžnou definicí třídy, která dědí od
      :class:`tuple` a definuje pojmenovaná pole. Takovou třídu lze napsat ručně,
      vytvořit odvozením od :class:`typing.NamedTuple` nebo tovární funkcí
      :func:`collections.namedtuple`. Poslední dva postupy přidávají také některé
      další metody, které ručně psané nebo vestavěné pojmenované n-tice mít
      nemusejí.

   namespace
      Místo, kde je uložena proměnná. Jmenné prostory jsou implementovány jako
      slovníky. Existují místní, globální a vestavěné jmenné prostory i vnořené
      jmenné prostory v objektech (v metodách). Jmenné prostory podporují
      modularitu tím, že zabraňují konfliktům názvů. Funkce :func:`builtins.open
      <.open>` a :func:`os.open` se například odlišují svými jmennými prostory.
      Ty také zlepšují čitelnost a udržovatelnost, protože je zřejmé, který modul
      funkci implementuje. Zápis :func:`random.seed` nebo :func:`itertools.islice`
      například ukazuje, že tyto funkce implementují moduly :mod:`random`,
      respektive :mod:`itertools`.

   namespace package
      :term:`Balíček <package>`, který slouží pouze jako kontejner podbalíčků.
      Balíčky jmenného prostoru nemusejí mít fyzickou reprezentaci a zejména se
      liší od :term:`běžných balíčků <regular package>` tím, že nemají soubor
      ``__init__.py``.

      Balíčky jmenného prostoru umožňují, aby několik samostatně instalovatelných
      balíčků mělo společný nadřazený balíček. V ostatních případech se doporučuje
      použít :term:`běžný balíček <regular package>`.

      Více informací uvádí :pep:`420` a :ref:`reference-namespace-package`.

      Viz také :term:`modul <module>`.

   native code
      Kód zkompilovaný do strojových instrukcí, který běží přímo na procesoru, na
      rozdíl od kódu interpretovaného nebo spouštěného ve virtuálním stroji. V
      kontextu Pythonu nativní kód obvykle označuje kód v C, C++, Rustu nebo
      Fortranu v :term:`rozšiřujících modulech <extension module>`, který lze
      volat z Pythonu. Viz také :term:`rozšiřující modul <extension module>`.

   nested scope
      Možnost odkazovat na proměnnou v obklopující definici. Funkce definovaná
      uvnitř jiné funkce může například odkazovat na proměnné ve vnější funkci.
      Vnořené obory platnosti ve výchozím nastavení slouží pouze k odkazování,
      nikoli k přiřazování. Místní proměnné se čtou i zapisují v nejvnitřnějším
      oboru platnosti. Obdobně se globální proměnné čtou i zapisují v globálním
      jmenném prostoru. Klíčové slovo :keyword:`nonlocal` umožňuje zápis do
      vnějších oborů platnosti.

   new-style class
      Starý název podoby tříd, která se nyní používá pro všechny objekty tříd. Ve
      starších verzích Pythonu mohly novější všestranné vlastnosti, například
      :attr:`~object.__slots__`, deskriptory, vlastnosti,
      :meth:`~object.__getattribute__`, třídní a statické metody, používat pouze
      třídy nového stylu.

   non-deterministic
      Chování, při němž se výsledek programu může lišit mezi spuštěními se
      stejnými vstupy. Ve vícevláknových programech nedeterministické chování
      často vzniká v důsledku :term:`souběhů <race condition>`, kdy výsledek
      ovlivňuje relativní načasování nebo prokládání vláken. Správná synchronizace
      pomocí :term:`zámků <lock>` a dalších :term:`synchronizačních primitiv
      <synchronization primitive>` pomáhá zajistit deterministické chování.

   object
      Libovolná data se stavem (atributy nebo hodnotou) a definovaným chováním
      (metodami). Také nejvyšší základní třída každé :term:`třídy nového stylu
      <new-style class>`.

   optimized scope
      Obor platnosti, v němž kompilátor při kompilaci kódu spolehlivě zná názvy
      cílových místních proměnných, a může proto optimalizovat přístup pro čtení
      a zápis těchto názvů. Tímto způsobem jsou optimalizovány místní jmenné
      prostory funkcí, generátorů, korutin, generátorových notací a výrazů
      generátoru. Poznámka: většina optimalizací interpretu se uplatňuje ve všech
      oborech platnosti; na optimalizované obory jsou omezeny pouze ty, které
      spoléhají na známou sadu názvů místních a nemístních proměnných.

   optional module
      :term:`Rozšiřující modul <extension module>`, který je součástí
      :term:`standardní knihovny <standard library>`, ale v některých sestaveních
      :term:`CPythonu <CPython>` může chybět, obvykle kvůli chybějícím knihovnám
      třetích stran nebo nedostupnosti modulu pro danou platformu.

      Seznam volitelných modulů vyžadujících knihovny třetích stran uvádí
      :ref:`optional-module-requirements`.

   package
      :term:`Modul <module>` Pythonu, který může obsahovat podmoduly nebo
      rekurzivně podbalíčky. Technicky je balíček modulem Pythonu s atributem
      ``__path__``.

      Viz také :term:`běžný balíček <regular package>` a :term:`balíček jmenného
      prostoru <namespace package>`.

   parallelism
      Provádění více operací současně (například na několika jádrech CPU). V
      sestaveních Pythonu s :term:`globálním zámkem interpretu (GIL) <global
      interpreter lock>` provádí bajtkód Pythonu vždy pouze jedno vlákno. Využití
      více jader CPU proto obvykle vyžaduje více procesů (například modul
      :mod:`multiprocessing`) nebo nativní rozšíření, která GIL uvolňují. V
      :term:`Pythonu bez GIL <free threading>` může kód Pythonu běžet současně v
      několika vláknech na různých jádrech.

   parameter
      Pojmenovaná entita v definici :term:`funkce <function>` (nebo metody), která
      určuje :term:`argument <argument>` (nebo v některých případech argumenty),
      jejž může funkce přijmout. Existuje pět druhů parametrů:

      * :dfn:`poziční nebo klíčový`: určuje argument,
        který lze předat buď :term:`pozičně <argument>`, nebo jako
        :term:`argument klíčového slova <argument>`. Jde o výchozí druh parametru,
        například *foo* a *bar* v následující definici::

           def func(foo, bar=None): ...

      .. _positional-only_parameter:

      * :dfn:`pouze poziční`: určuje argument, který lze předat
        pouze pozičně. Pouze poziční parametry lze definovat vložením znaku ``/``
        za ně v seznamu parametrů definice funkce, například *posonly1* a
        *posonly2* v následující definici::

           def func(posonly1, posonly2, /, positional_or_keyword): ...

      .. _keyword-only_parameter:

      * :dfn:`pouze klíčový`: určuje argument, který lze předat
        pouze klíčovým slovem. Pouze klíčové parametry lze definovat vložením
        jediného proměnného pozičního parametru nebo samostatného ``*`` před ně v
        seznamu parametrů definice funkce, například *kw_only1* a *kw_only2* v
        následující definici::

           def func(arg, *, kw_only1, kw_only2): ...

      * :dfn:`proměnný poziční`: určuje, že lze předat libovolnou
        posloupnost pozičních argumentů (kromě pozičních argumentů přijímaných
        jinými parametry). Takový parametr lze definovat přidáním ``*`` před jeho
        název, například *args* v následující definici::

           def func(*args, **kwargs): ...

      * :dfn:`proměnný klíčový`: určuje, že lze předat libovolný
        počet argumentů klíčových slov (kromě argumentů klíčových slov přijímaných
        jinými parametry). Takový parametr lze definovat přidáním ``**`` před
        jeho název, například *kwargs* v předchozím příkladu.

      Parametry mohou určovat volitelné i povinné argumenty a také výchozí
      hodnoty některých volitelných argumentů.

      Viz také heslo :term:`argument`, otázka FAQ o :ref:`rozdílu mezi argumenty
      a parametry <faq-argument-vs-parameter>`, třída :class:`inspect.Parameter`,
      oddíl :ref:`function` a :pep:`362`.

   per-object lock
      :term:`Zámek <lock>` přidružený ke konkrétní instanci objektu namísto
      globálního zámku sdíleného všemi objekty. V :term:`Pythonu bez GIL
      <free threading>` používají vestavěné typy, jako jsou :class:`dict` a
      :class:`list`, zámky jednotlivých objektů. Umožňují tak souběžné operace nad
      různými objekty a zároveň řadí operace nad týmž objektem za sebe. Operace,
      které drží zámek objektu, brání pokračování jiných zamykajících operací nad
      stejným objektem, ale neblokují operace :term:`bez zámku <lock-free>`.

   path entry
      Jediné umístění na :term:`cestě importu <import path>`, které
      :term:`vyhledávač založený na cestě <path based finder>` prohledává při
      hledání modulů k importu.

   path entry finder
      :term:`Vyhledávač <finder>` vrácený volatelným objektem v
      :data:`sys.path_hooks` (tedy :term:`háčkem položky cesty <path entry hook>`),
      který dokáže vyhledávat moduly podle dané :term:`položky cesty <path
      entry>`.

      Metody implementované vyhledávači položek cesty uvádí dokumentace třídy
      :class:`importlib.abc.PathEntryFinder`.

   path entry hook
      Volatelný objekt v seznamu :data:`sys.path_hooks`, který vrátí
      :term:`vyhledávač položky cesty <path entry finder>`, pokud dokáže hledat
      moduly v dané :term:`položce cesty <path entry>`.

   path based finder
      Jeden z výchozích :term:`vyhledávačů metacesty <meta path finder>`, který
      hledá moduly na :term:`cestě importu <import path>`.

   path-like object
      Objekt představující cestu souborového systému. Objektem podobným cestě je
      buď objekt :class:`str` či :class:`bytes` představující cestu, nebo objekt
      implementující protokol :class:`os.PathLike`. Objekt podporující protokol
      :class:`os.PathLike` lze převést na cestu souborového systému typu
      :class:`str` nebo :class:`bytes` voláním funkce :func:`os.fspath`; funkce
      :func:`os.fsdecode`, respektive :func:`os.fsencode`, lze použít k zaručení
      výsledku typu :class:`str`, respektive :class:`bytes`. Zavedeno v
      :pep:`519`.

   PEP
      Návrh na vylepšení Pythonu (Python Enhancement Proposal). PEP je návrhový
      dokument, který poskytuje informace komunitě Pythonu nebo popisuje novou
      vlastnost Pythonu, jeho procesů či prostředí. PEP by měl obsahovat stručnou
      technickou specifikaci a odůvodnění navrhovaných vlastností.

      PEP představují hlavní mechanismus pro navrhování významných nových
      vlastností, shromažďování názorů komunity na určitou otázku a dokumentování
      návrhových rozhodnutí v Pythonu. Autor PEP odpovídá za dosažení shody v
      komunitě a zaznamenání nesouhlasných názorů.

      Viz :pep:`1`.

   portion
      Sada souborů v jediném adresáři (případně uložená v souboru ZIP), která
      přispívá do balíčku jmenného prostoru, jak jej definuje :pep:`420`.

   positional argument
      Viz :term:`argument`.

   provisional API
      Provizorní API je záměrně vyňato ze záruk zpětné kompatibility standardní
      knihovny. Přestože se u takových rozhraní neočekávají zásadní změny, dokud
      jsou označena jako provizorní, mohou hlavní vývojáři v případě potřeby
      provést změny narušující zpětnou kompatibilitu, včetně úplného odstranění
      rozhraní. Takové změny nebudou prováděny bezdůvodně — nastanou pouze tehdy,
      budou-li odhaleny závažné základní nedostatky přehlédnuté před zařazením API.

      I u provizorních API jsou zpětně nekompatibilní změny považovány za
      „poslední možnost“; vždy bude vyvinuto veškeré úsilí k nalezení zpětně
      kompatibilního řešení zjištěných problémů.

      Tento proces umožňuje standardní knihovně dále se vyvíjet, aniž by v ní
      problematické návrhové chyby zůstaly dlouhodobě uzamčeny. Podrobnosti uvádí
      :pep:`411`.

   provisional package
      Viz :term:`provizorní API <provisional API>`.

   Python 3000
      Přezdívka řady vydání Pythonu 3.x, vzniklá dávno v době, kdy bylo vydání
      verze 3 ještě vzdálenou budoucností. Zkracuje se také jako „Py3k“.

   Pythonic
      Myšlenka nebo část kódu, která přesně následuje běžné idiomy jazyka Python,
      namísto implementace pomocí konceptů obvyklých v jiných jazycích. Běžným
      idiomem Pythonu je například procházet všechny prvky iterovatelného objektu
      příkazem :keyword:`for`. Mnoho jiných jazyků takovou konstrukci nemá, takže
      lidé neznalí Pythonu někdy místo ní používají číselné počítadlo::

          for i in range(len(food)):
              print(food[i])

      Na rozdíl od čistšího, pythonovského způsobu::

         for piece in food:
             print(piece)

   qualified name
      Tečkovaný název zobrazující „cestu“ z globálního oboru modulu ke třídě,
      funkci nebo metodě definované v tomto modulu, jak ji definuje :pep:`3155`.
      U funkcí a tříd nejvyšší úrovně je kvalifikovaný název shodný s názvem
      objektu::

         >>> class C:
         ...     class D:
         ...         def meth(self):
         ...             pass
         ...
         >>> C.__qualname__
         'C'
         >>> C.D.__qualname__
         'C.D'
         >>> C.D.meth.__qualname__
         'C.D.meth'

      Při odkazování na moduly znamená *plně kvalifikovaný název* celou tečkovanou
      cestu k modulu včetně všech nadřazených balíčků, například
      ``email.mime.text``::

         >>> import email.mime.text
         >>> email.mime.text.__name__
         'email.mime.text'

   race condition
      Stav programu, kdy jeho chování závisí na relativním načasování nebo pořadí
      událostí, zejména ve vícevláknových programech. Souběhy mohou vést k
      :term:`nedeterministickému <non-deterministic>` chování a obtížně
      reprodukovatelným chybám. :term:`Datový souběh <data race>` je konkrétní
      druh souběhu zahrnující nesynchronizovaný přístup ke sdílené paměti.
      Programátorský styl :term:`LBYL` je k souběhům ve vícevláknovém kódu zvlášť
      náchylný. Předcházet jim pomáhá používání :term:`zámků <lock>` a dalších
      :term:`synchronizačních primitiv <synchronization primitive>`.

   reference count
      Počet odkazů na objekt. Když počet odkazů na objekt klesne na nulu, objekt
      se uvolní. Některé objekty jsou :term:`nesmrtelné <immortal>` a jejich počet
      odkazů se nikdy nemění, takže se nikdy neuvolní. Počítání odkazů obvykle
      není z kódu Pythonu viditelné, je však zásadní součástí implementace
      :term:`CPythonu <CPython>`. Programátoři mohou počet odkazů na konkrétní
      objekt získat voláním funkce :func:`sys.getrefcount`.

      V :term:`CPythonu <CPython>` se počty odkazů nepovažují za stabilní ani
      přesně definované hodnoty. Počet odkazů na objekt a způsob, jakým jej
      ovlivňuje kód Pythonu, se mohou mezi verzemi lišit.

   regular package
      Tradiční :term:`balíček <package>`, například adresář obsahující soubor
      ``__init__.py``.

      Viz také :term:`balíček jmenného prostoru <namespace package>`.

   reentrant
      Vlastnost funkce nebo :term:`zámku <lock>`, která umožňuje témuž vláknu
      funkci opakovaně volat nebo zámek opakovaně získat, aniž by došlo k chybě či
      :term:`uváznutí <deadlock>`.

      U funkcí reentrantnost znamená, že funkci lze bezpečně zavolat znovu ještě
      před dokončením předchozího volání. To je důležité, pokud může být volána
      rekurzivně nebo z obsluhy signálu. Funkce, které nejsou bezpečné ve více
      vláknech, se mohou chovat :term:`nedeterministicky <non-deterministic>`,
      jsou-li reentrantně volány ve vícevláknovém programu.

      U zámků je :class:`threading.RLock` Pythonu reentrantní, takže vlákno, které
      jej již drží, jej může získat znovu bez zablokování. Naproti tomu
      :class:`threading.Lock` reentrantní není — pokus získat jej dvakrát ze
      stejného vlákna způsobí uváznutí.

      Viz také :term:`zámek <lock>` a :term:`uváznutí <deadlock>`.

   REPL
      Zkratka anglického „read–eval–print loop“ (smyčka načti–vyhodnoť–vypiš),
      jiný název pro :term:`interaktivní <interactive>` shell interpretu.

   __slots__
      Deklarace uvnitř třídy, která šetří paměť předběžným vyhrazením prostoru
      pro atributy instancí a odstraněním slovníků instancí. Ačkoli je tato
      technika oblíbená, její správné použití je poněkud obtížné a nejlépe se
      hodí pro vzácné případy, kdy aplikace citlivá na spotřebu paměti pracuje s
      velkým počtem instancí.

   sequence
      :term:`Iterovatelný objekt <iterable>`, který pomocí celočíselných indexů a
      speciální metody :meth:`~object.__getitem__` podporuje efektivní přístup k
      prvkům a definuje metodu :meth:`~object.__len__` vracející délku
      posloupnosti. Mezi vestavěné typy posloupností patří :class:`list`,
      :class:`str`, :class:`tuple` a :class:`bytes`. Také :class:`dict` podporuje
      metody :meth:`~object.__getitem__` a :meth:`!__len__`, považuje se však za
      mapování, nikoli posloupnost, protože k vyhledávání používá libovolné
      :term:`hašovatelné <hashable>` klíče namísto celých čísel.

      Abstraktní základní třída :class:`collections.abc.Sequence` definuje mnohem
      bohatší rozhraní, které kromě metod :meth:`~object.__getitem__` a
      :meth:`~object.__len__` přidává :meth:`~sequence.count`,
      :meth:`~sequence.index`, :meth:`~object.__contains__` a
      :meth:`~object.__reversed__`. Typy implementující toto rozšířené rozhraní
      lze výslovně zaregistrovat funkcí :func:`~abc.ABCMeta.register`. Obecnější
      dokumentaci metod posloupností uvádí :ref:`běžné operace s posloupnostmi
      <typesseq-common>`.

   set comprehension
      Stručný způsob zpracování všech nebo některých prvků iterovatelného objektu
      a vrácení množiny s výsledky. ``results = {c for c in 'abracadabra' if
      c not in 'abc'}`` vytvoří množinu řetězců ``{'r', 'd'}``. Viz
      :ref:`comprehensions`.

   single dispatch
      Podoba výběru :term:`generické funkce <generic function>`, při níž se
      implementace vybírá podle typu jediného argumentu.

   slice
      Objekt typu :class:`slice`, který popisuje část :term:`posloupnosti
      <sequence>`. Objekt výřezu vzniká při použití :ref:`výřezové <slicings>`
      podoby :ref:`indexovacího zápisu <subscriptions>` s dvojtečkami uvnitř
      hranatých závorek, například ``variable_name[1:3:5]``.

   soft deprecated
      Měkce zastaralé API by se nemělo používat v novém kódu, jeho použití ve
      stávajícím kódu je však bezpečné. API zůstává zdokumentované a testované,
      nebude se však dále rozvíjet.

      Na rozdíl od běžného označení za zastaralé se při měkkém zastarání
      neplánuje odstranění API a nevydávají se varování.

      Viz `PEP 387: Soft Deprecation
      <https://peps.python.org/pep-0387/#soft-deprecation>`_.

   special method
      .. index:: pair: special; method

      Metoda, kterou Python implicitně volá k provedení určité operace nad typem,
      například sčítání. Názvy těchto metod začínají a končí dvojitým
      podtržítkem. Speciální metody dokumentuje oddíl :ref:`specialnames`.

   standard library
      Soubor :term:`balíčků <package>`, :term:`modulů <module>` a
      :term:`rozšiřujících modulů <extension module>` distribuovaných jako
      součást oficiálního balíčku interpretu Pythonu. Přesné složení se může
      lišit podle platformy, dostupných systémových knihoven nebo jiných kritérií.
      Dokumentaci najdete v :ref:`library-index`.

      Seznam všech možných názvů modulů standardní knihovny uvádí také
      :data:`sys.stdlib_module_names`.

   statement
      Příkaz je součástí bloku příkazů („bloku“ kódu). Je buď :term:`výrazem
      <expression>`, nebo jednou z několika konstrukcí s klíčovým slovem,
      například :keyword:`if`, :keyword:`while` či :keyword:`for`.

   static type checker
      Externí nástroj, který čte a analyzuje kód Pythonu a hledá problémy,
      například nesprávné typy. Viz také :term:`typové nápovědy <type hint>` a
      modul :mod:`typing`.

   stdlib
      Zkratka pro :term:`standardní knihovnu <standard library>`.

   strong reference
      V C API Pythonu je silný odkaz odkazem na objekt, který vlastní kód držící
      tento odkaz. Při vytvoření odkazu se silný odkaz získá voláním
      :c:func:`Py_INCREF` a při jeho odstranění se uvolní voláním
      :c:func:`Py_DECREF`.

      K vytvoření silného odkazu na objekt lze použít funkci
      :c:func:`Py_NewRef`. Před opuštěním oboru platnosti silného odkazu je
      obvykle nutné zavolat :c:func:`Py_DECREF`, aby jeden odkaz neunikl.

      Viz také :term:`vypůjčený odkaz <borrowed reference>`.

   subscript
      Výraz v hranatých závorkách :ref:`indexovacího výrazu <subscriptions>`,
      například ``3`` v ``items[3]``. Obvykle slouží k výběru prvku kontejneru.
      Nazývá se také :term:`klíč <key>` při indexování :term:`mapování <mapping>`
      nebo :term:`index <index>` při indexování :term:`posloupnosti <sequence>`.

   synchronization primitive
      Základní stavební prvek pro koordinaci (synchronizaci) provádění více vláken
      zajišťující :term:`bezpečný <thread-safe>` přístup ke sdíleným prostředkům
      z více vláken. Modul :mod:`threading` poskytuje několik synchronizačních
      primitiv, mezi něž patří :class:`~threading.Lock`,
      :class:`~threading.RLock`, :class:`~threading.Semaphore`,
      :class:`~threading.Condition`, :class:`~threading.Event` a
      :class:`~threading.Barrier`. Modul :mod:`queue` navíc poskytuje fronty s
      více producenty a konzumenty, které jsou zvlášť užitečné ve vícevláknových
      programech. Tato primitiva pomáhají předcházet :term:`souběhům <race
      condition>` a koordinovat běh vláken. Viz také :term:`zámek <lock>`.

   t-string
   t-strings
      Řetězcové literály s předponou ``t`` nebo ``T`` se běžně nazývají
      „t-řetězce“, což je zkrácený název pro :ref:`šablonové řetězcové literály
      <t-strings>`.

   text encoding
      Řetězec je v Pythonu posloupností kódových bodů Unicode (v rozsahu
      ``U+0000``--``U+10FFFF``). Aby jej bylo možné uložit nebo přenést, musí být
      serializován jako posloupnost bajtů.

      Serializace řetězce na posloupnost bajtů se nazývá „kódování“ a opětovné
      vytvoření řetězce z posloupnosti bajtů „dekódování“.

      Existuje řada různých :ref:`kodeků <standard-encodings>` pro serializaci
      textu, které se souhrnně označují jako „kódování textu“.

   text file
      :term:`Souborový objekt <file object>`, který dokáže číst a zapisovat
      objekty :class:`str`. Textový soubor často ve skutečnosti přistupuje k
      bajtově orientovanému proudu dat a automaticky zajišťuje :term:`kódování
      textu <text encoding>`. Příklady textových souborů jsou soubory otevřené v
      textovém režimu (``'r'`` nebo ``'w'``), :data:`sys.stdin`,
      :data:`sys.stdout` a instance :class:`io.StringIO`.

      Viz také :term:`binární soubor <binary file>`, tedy souborový objekt schopný
      číst a zapisovat :term:`objekty podobné bajtům <bytes-like object>`.

   thread state

      Informace, které běhové prostředí :term:`CPythonu <CPython>` používá při
      běhu ve vláknu operačního systému. Patří sem například aktuální výjimka,
      pokud nějaká existuje, a stav interpretu bajtkódu.

      Každý stav vlákna je svázán s jediným vláknem operačního systému, vlákna
      však mohou mít k dispozici více stavů. Současně může být nejvýše jeden z
      nich :term:`připojený <attached thread state>`.

      :term:`Připojený stav vlákna <attached thread state>` je vyžadován pro
      volání většiny C API Pythonu, pokud dokumentace funkce výslovně neuvádí
      jinak. Interpret bajtkódu běží pouze s připojeným stavem vlákna.

      Každý stav vlákna patří jedinému interpretu, ale každý interpret může mít
      mnoho stavů vláken, včetně několika pro stejné vlákno operačního systému.
      Stavy vláken více interpretů mohou být svázány se stejným vláknem, ale v
      daném okamžiku v něm může být pouze jeden :term:`připojený <attached thread
      state>`.

      Více informací uvádí :ref:`stav vlákna a globální zámek interpretu
      <threads>`.

   thread-safe
      Modul, funkce nebo třída, která se chová správně při souběžném použití více
      vlákny. Kód bezpečný ve více vláknech používá vhodná :term:`synchronizační
      primitiva <synchronization primitive>`, například :term:`zámky <lock>`, k
      ochraně sdíleného měnitelného stavu, nebo je navržen tak, aby se mu zcela
      vyhnul. V :term:`sestavení bez GIL <free threading>` používají vestavěné
      typy jako :class:`dict`, :class:`list` a :class:`set` interní zamykání,
      které zajišťuje bezpečnost mnoha operací ve více vláknech, ačkoli není
      nutně zaručena vždy. Kód, který ve více vláknech bezpečný není, může při
      použití ve vícevláknových programech narazit na :term:`souběhy <race
      condition>` a :term:`datové souběhy <data race>`.

   token

      Malá jednotka zdrojového kódu vytvářená :ref:`lexikálním analyzátorem
      <lexical>` (nazývaným také *tokenizér*). Tokeny představují názvy, čísla,
      řetězce, operátory, konce řádků a podobné prvky.

      Modul :mod:`tokenize` zpřístupňuje lexikální analyzátor Pythonu. Modul
      :mod:`token` obsahuje informace o různých typech tokenů.

   triple-quoted string
      Řetězec ohraničený třemi uvozovkami (") nebo třemi apostrofy ('). Přestože
      nenabízí žádnou funkcionalitu nedostupnou řetězcům s jednoduchými
      uvozovkami, je užitečný z několika důvodů. Umožňuje do řetězce zahrnout
      jednoduché i dvojité uvozovky bez řídicího znaku a může bez znaku
      pokračování přesahovat přes více řádků, což se hodí zejména při psaní
      dokumentačních řetězců.

   type
      Typ objektu Pythonu určuje, o jaký druh objektu jde; každý objekt má svůj
      typ. Typ objektu je dostupný jako jeho atribut :attr:`~object.__class__`
      nebo jej lze získat pomocí ``type(obj)``.

   type alias
      Synonymum typu vytvořené přiřazením typu identifikátoru.

      Aliasy typů jsou užitečné ke zjednodušení :term:`typových nápověd <type
      hint>`. Například::

         def remove_gray_shades(
                 colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
             pass

      lze učinit čitelnějším takto::

         Color = tuple[int, int, int]

         def remove_gray_shades(colors: list[Color]) -> list[Color]:
             pass

      Tuto funkcionalitu popisuje modul :mod:`typing` a :pep:`484`.

   type hint
      :term:`Anotace <annotation>`, která určuje očekávaný typ proměnné, atributu
      třídy, parametru funkce nebo návratové hodnoty.

      Typové nápovědy jsou volitelné a Python je nevynucuje, jsou však užitečné
      pro :term:`statické kontroly typů <static type checker>`. Mohou také pomoci
      vývojovým prostředím s doplňováním kódu a refaktorizací.

      K typovým nápovědám globálních proměnných, atributů tříd a funkcí, nikoli
      však místních proměnných, lze přistupovat funkcí
      :func:`typing.get_type_hints`.

      Tuto funkcionalitu popisuje modul :mod:`typing` a :pep:`484`.

   universal newlines
      Způsob interpretace textových proudů, při němž se za konec řádku považují
      všechny následující podoby: unixová konvence ``'\n'``, konvence Windows
      ``'\r\n'`` a stará konvence systému Macintosh ``'\r'``. Viz :pep:`278` a
      :pep:`3116`; další použití uvádí také :func:`bytes.splitlines`.

   variable annotation
      :term:`Anotace <annotation>` proměnné nebo atributu třídy.

      Při anotování proměnné nebo atributu třídy je přiřazení volitelné::

         class C:
             field: 'annotation'

      Anotace proměnných se obvykle používají pro :term:`typové nápovědy <type
      hint>`: od následující proměnné se například očekávají hodnoty typu
      :class:`int`::

         count: int = 0

      Syntaxi anotací proměnných vysvětluje oddíl :ref:`annassign`.

      Tuto funkcionalitu popisuje také heslo :term:`anotace funkce <function
      annotation>`, :pep:`484` a :pep:`526`. Doporučené postupy pro práci s
      anotacemi uvádí :ref:`annotations-howto`.

   virtual environment
      Kooperativně izolované běhové prostředí, které uživatelům a aplikacím
      Pythonu umožňuje instalovat a aktualizovat distribuční balíčky Pythonu,
      aniž by ovlivnili chování jiných aplikací Pythonu běžících ve stejném
      systému.

      Viz také modul :mod:`venv`.

   virtual machine
      Počítač definovaný výhradně softwarem. Virtuální stroj Pythonu provádí
      :term:`bajtkód <bytecode>` vytvořený kompilátorem bajtkódu.

   walrus operator
      Žertovné označení operátoru ``:=`` pro :ref:`přiřazovací výraz
      <assignment-expressions>`, protože při naklonění hlavy trochu připomíná
      mrože.

   Zen of Python
      Přehled návrhových zásad a filozofie Pythonu, které pomáhají porozumět
      jazyku a používat jej. Přehled zobrazíte zadáním „``import this``“ do
      interaktivní výzvy.
