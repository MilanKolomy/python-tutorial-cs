.. _tut-morecontrol:

****************************************
Další nástroje pro řízení toku programu
****************************************

Kromě právě představeného příkazu :keyword:`while` používá Python několik
dalších nástrojů, s nimiž se seznámíme v této kapitole.


.. _tut-if:

:keyword:`!if` – podmíněné příkazy
===================================

Nejznámějším typem příkazu je patrně :keyword:`if`. Například::

   >>> x = int(input("Please enter an integer: "))
   Please enter an integer: 42
   >>> if x < 0:
   ...     x = 0
   ...     print('Negative changed to zero')
   ... elif x == 0:
   ...     print('Zero')
   ... elif x == 1:
   ...     print('Single')
   ... else:
   ...     print('More')
   ...
   More

Částí :keyword:`elif` může být libovolný počet včetně nuly a část
:keyword:`else` je nepovinná. Klíčové slovo :keyword:`!elif` je zkrácením
„else if“ a pomáhá omezit nadměrné odsazování. Posloupnost :keyword:`!if` ...
:keyword:`!elif` ... :keyword:`!elif` ... nahrazuje příkazy ``switch`` nebo
``case`` známé z jiných jazyků.

Porovnáváte-li tutéž hodnotu s několika konstantami nebo kontrolujete konkrétní
typy či atributy, může se vám hodit také příkaz :keyword:`!match`. Podrobnosti
najdete v části :ref:`tut-match`.

.. _tut-for:

:keyword:`!for` – cykly
==========================

.. index::
   pair: statement; for

Příkaz :keyword:`for` se v Pythonu poněkud liší od toho, na co můžete být
zvyklí z C nebo Pascalu. Namísto procházení aritmetické posloupnosti čísel
(jako v Pascalu) nebo možnosti určit krok iterace i podmínku ukončení (jako v C)
prochází příkaz :keyword:`!for` v Pythonu prvky libovolné sekvence (seznamu nebo
řetězce) v pořadí, v jakém se v ní nacházejí. Například:

.. One suggestion was to give a real C example here, but that may only serve to
   confuse non-C programmers.

::

   >>> # Measure some strings:
   >>> words = ['cat', 'window', 'defenestrate']
   >>> for w in words:
   ...     print(w, len(w))
   ...
   cat 3
   window 6
   defenestrate 12

Kód, který mění kolekci během jejího procházení, může být obtížné napsat
správně. Obvykle je přímočařejší procházet kopii kolekce nebo vytvořit kolekci
novou::

    # Create a sample collection
    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

    # Strategy:  Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

    # Strategy:  Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status


.. _tut-range:

Funkce :func:`range`
==========================

Potřebujete-li procházet posloupnost čísel, přijde vhod vestavěná funkce
:func:`range`. Generuje aritmetické posloupnosti::

    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4

Zadaný koncový bod nikdy není součástí vygenerované posloupnosti; ``range(10)``
vytvoří 10 hodnot, tedy platné indexy prvků sekvence délky 10. Rozsah může
začínat jiným číslem a lze zadat také jiný přírůstek (i záporný; někdy se mu
říká „krok“)::

    >>> list(range(5, 10))
    [5, 6, 7, 8, 9]

    >>> list(range(0, 10, 3))
    [0, 3, 6, 9]

    >>> list(range(-10, -100, -30))
    [-10, -40, -70]

Chcete-li procházet indexy sekvence, můžete zkombinovat :func:`range`
a :func:`len` takto::

   >>> a = ['Mary', 'had', 'a', 'little', 'lamb']
   >>> for i in range(len(a)):
   ...     print(i, a[i])
   ...
   0 Mary
   1 had
   2 a
   3 little
   4 lamb

Ve většině takových případů je však vhodnější použít funkci :func:`enumerate`,
viz :ref:`tut-loopidioms`.

Při prostém vypsání rozsahu se stane zvláštní věc::

   >>> range(10)
   range(0, 10)

Objekt vrácený funkcí :func:`range` se v mnoha ohledech chová jako seznam, ve
skutečnosti jím však není. Při procházení postupně vrací prvky požadované
posloupnosti, ale samotný seznam nevytváří, čímž šetří místo.

Takovému objektu říkáme :term:`iterovatelný <iterable>`, tedy vhodný jako vstup
pro funkce a konstrukce, které očekávají něco, z čeho mohou postupně získávat
prvky až do jejich vyčerpání. Viděli jsme, že takovou konstrukcí je příkaz
:keyword:`for`; příkladem funkce přijímající iterovatelný objekt je :func:`sum`::

    >>> sum(range(4))  # 0 + 1 + 2 + 3
    6

Později se setkáme s dalšími funkcemi, které iterovatelné objekty vracejí nebo
je přijímají jako argumenty. V kapitole :ref:`tut-structures` podrobněji
probereme :func:`list`.

.. _tut-break:

Příkazy :keyword:`!break` a :keyword:`!continue`
=====================================================

Příkaz :keyword:`break` ukončí nejvnitřnější obklopující cyklus
:keyword:`for` nebo :keyword:`while`::

    >>> for n in range(2, 10):
    ...     for x in range(2, n):
    ...         if n % x == 0:
    ...             print(f"{n} equals {x} * {n//x}")
    ...             break
    ...
    4 equals 2 * 2
    6 equals 2 * 3
    8 equals 2 * 4
    9 equals 3 * 3

Příkaz :keyword:`continue` pokračuje další iterací cyklu::

    >>> for num in range(2, 10):
    ...     if num % 2 == 0:
    ...         print(f"Found an even number {num}")
    ...         continue
    ...     print(f"Found an odd number {num}")
    ...
    Found an even number 2
    Found an odd number 3
    Found an even number 4
    Found an odd number 5
    Found an even number 6
    Found an odd number 7
    Found an even number 8
    Found an odd number 9

.. _tut-for-else:
.. _break-and-continue-statements-and-else-clauses-on-loops:

Část :keyword:`!else` u cyklů
=================================

V cyklu :keyword:`!for` nebo :keyword:`!while` lze příkaz :keyword:`!break`
spojit s částí :keyword:`!else`. Pokud cyklus skončí bez provedení
:keyword:`!break`, provede se část :keyword:`!else`.

V cyklu :keyword:`for` se část :keyword:`!else` provede poté, co cyklus dokončí
poslední iteraci, tedy pokud nedošlo k jeho přerušení.

V cyklu :keyword:`while` se provede poté, co se podmínka cyklu stane nepravdivou.

U obou druhů cyklu se část :keyword:`!else` **neprovede**, pokud byl cyklus
ukončen příkazem :keyword:`break`. Její provedení samozřejmě přeskočí také jiné
způsoby předčasného ukončení cyklu, například :keyword:`return` nebo vyvolaná
výjimka.

Ukazuje to následující cyklus :keyword:`!for`, který hledá prvočísla::

   >>> for n in range(2, 10):
   ...     for x in range(2, n):
   ...         if n % x == 0:
   ...             print(n, 'equals', x, '*', n//x)
   ...             break
   ...     else:
   ...         # loop fell through without finding a factor
   ...         print(n, 'is a prime number')
   ...
   2 is a prime number
   3 is a prime number
   4 equals 2 * 2
   5 is a prime number
   6 equals 2 * 3
   7 is a prime number
   8 equals 2 * 4
   9 equals 3 * 3

(Ano, tento kód je správně. Podívejte se pozorně: část ``else`` patří k cyklu
``for``, **nikoli** k příkazu ``if``.)

Část ``else`` si lze představit jako protějšek příkazu ``if`` uvnitř cyklu.
Během provádění cyklu vzniká posloupnost podobná if/if/if/else. Příkaz ``if``
je uvnitř cyklu, takže se vyhodnotí několikrát. Pokud je jeho podmínka někdy
pravdivá, provede se ``break``. Není-li pravdivá nikdy, provede se část ``else``
vně cyklu.

Při použití s cyklem má část ``else`` více společného s částí ``else`` příkazu
:keyword:`try` než s příkazem ``if``: část ``else`` příkazu ``try`` se provede,
pokud nenastane výjimka, zatímco část ``else`` cyklu se provede, pokud nenastane
``break``. Více o příkazu ``try`` a výjimkách najdete v :ref:`tut-handling`.

.. index:: single: ...; ellipsis literal
.. _tut-pass:

Příkaz :keyword:`!pass`
===========================

Příkaz :keyword:`pass` nedělá nic. Lze jej použít tam, kde je příkaz vyžadován
syntakticky, ale program nemá provést žádnou akci. Například::

   >>> while True:
   ...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
   ...

Často se používá při vytváření minimálních tříd::

   >>> class MyEmptyClass:
   ...     pass
   ...

Příkaz :keyword:`pass` lze při práci na novém kódu použít také jako zástupný
obsah těla funkce nebo podmíněného příkazu, takže můžete nadále uvažovat na
abstraktnější úrovni. Příkaz :keyword:`!pass` se bez upozornění ignoruje::

   >>> def initlog(*args):
   ...     pass   # Remember to implement this!
   ...

V posledním případě mnoho lidí používá namísto :code:`pass` literál výpustky
:code:`...`. Toto použití nemá pro Python žádný zvláštní význam a není součástí
definice jazyka (mohl by zde být libovolný konstantní výraz), ale :code:`...`
se podle konvence používá také jako zástupné tělo. Viz
:ref:`bltin-ellipsis-object`.


.. _tut-match:

:keyword:`!match` – porovnávání vzorů
=====================================

Příkaz :keyword:`match` přijímá výraz a porovnává jeho hodnotu s postupnými
vzory zadanými v jednom či více blocích ``case``. Na první pohled se podobá
příkazu ``switch`` v C, Javě, JavaScriptu a mnoha dalších jazycích, bližší je
však porovnávání vzorů v jazycích jako Rust nebo Haskell. Provede se pouze první
odpovídající vzor, který navíc může z hodnoty získat její součásti (prvky
sekvence nebo atributy objektu) a uložit je do proměnných. Pokud neodpovídá
žádný případ, neprovede se žádná větev.

Nejjednodušší podoba porovnává zkoumanou hodnotu s jedním či více literály::

    def http_error(status):
        match status:
            case 400:
                return "Bad request"
            case 404:
                return "Not found"
            case 418:
                return "I'm a teapot"
            case _:
                return "Something's wrong with the internet"

Všimněte si posledního bloku: „název proměnné“ ``_`` funguje jako *žolík*
(wildcard) a odpovídá vždy.

Několik literálů lze v jediném vzoru spojit pomocí ``|`` („nebo“)::

            case 401 | 403 | 404:
                return "Not allowed"

Vzory mohou vypadat jako rozbalovací přiřazení a lze je použít k navázání
proměnných::

    # point is an (x, y) tuple
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

Tento příklad si pečlivě prostudujte. První vzor obsahuje dva literály a lze jej
chápat jako rozšíření výše uvedeného literálového vzoru. Následující dva vzory
však spojují literál a proměnnou, přičemž proměnná *naváže* hodnotu ze zkoumaného
objektu (``point``). Čtvrtý vzor zachytí dvě hodnoty, a proto se významem podobá
rozbalovacímu přiřazení ``(x, y) = point``.

Používáte-li ke strukturování dat třídy, můžete uvést název třídy následovaný
seznamem argumentů připomínajícím konstruktor, který však umožňuje zachytit
atributy do proměnných::

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def where_is(point):
        match point:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")

U některých vestavěných tříd, které určují pořadí svých atributů (například
datové třídy), můžete používat poziční parametry. Konkrétní pozice atributů ve
vzorech lze ve vlastních třídách určit také nastavením speciálního atributu
``__match_args__``. Je-li nastaven na ("x", "y"), jsou všechny následující
vzory rovnocenné (a všechny navážou atribut ``y`` na proměnnou ``var``)::

    Point(1, var)
    Point(1, y=var)
    Point(x=1, y=var)
    Point(y=var, x=1)

Doporučeným způsobem čtení vzorů je chápat je jako rozšířenou podobu toho, co
byste napsali na levou stranu přiřazení; tak lze poznat, kterým proměnným se co
přiřadí. Příkaz ``match`` přiřazuje pouze samostatným názvům (jako ``var``
výše). Názvům s tečkou (například ``foo.bar``), názvům atributů (výše ``x=``
a ``y=``) ani názvům tříd (rozpoznatelným podle následujících ``(...)``, jako
výše ``Point``) se nikdy nepřiřazuje.

Vzory lze libovolně vnořovat. Máme-li například krátký seznam bodů s přidaným
``__match_args__``, můžeme jej porovnat takto::

    class Point:
        __match_args__ = ('x', 'y')
        def __init__(self, x, y):
            self.x = x
            self.y = y

    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")

Ke vzoru lze přidat část ``if``, které se říká *stráž* (guard). Je-li stráž
nepravdivá, pokračuje ``match`` zkoušením následujícího bloku ``case``.
K zachycení hodnoty dochází ještě před vyhodnocením stráže::

    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")

Několik dalších důležitých vlastností tohoto příkazu:

- Stejně jako u rozbalovacího přiřazení mají vzory n-tic a seznamů naprosto
  stejný význam a ve skutečnosti odpovídají libovolným sekvencím. Důležitou
  výjimkou je, že neodpovídají iterátorům ani řetězcům.

- Vzory sekvencí podporují rozšířené rozbalování: ``[x, y, *rest]`` a ``(x, y,
  *rest)`` fungují podobně jako rozbalovací přiřazení. Název za ``*`` může být
  také ``_``, takže ``(x, y, *_)`` odpovídá sekvenci s alespoň dvěma prvky,
  aniž by navázal prvky zbývající.

- Vzory mapování: ``{"bandwidth": b, "latency": l}`` zachytí ze slovníku
  hodnoty ``"bandwidth"`` a ``"latency"``. Na rozdíl od vzorů sekvencí se
  nadbytečné klíče ignorují. Podporováno je také rozbalování jako ``**rest``.
  (Zápis ``**_`` by byl nadbytečný, a proto není povolen.)

- Podvzory lze zachytit pomocí klíčového slova ``as``::

      case (Point(x1, y1), Point(x2, y2) as p2): ...

  zachytí druhý prvek vstupu jako ``p2`` (pokud je vstup sekvencí dvou bodů).

- Většina literálů se porovnává podle rovnosti, jednoinstanční objekty ``True``,
  ``False`` a ``None`` se však porovnávají podle identity.

- Vzory mohou používat pojmenované konstanty. Musí jít o názvy s tečkou, aby
  nebyly interpretovány jako zachytávací proměnné::

      from enum import Enum
      class Color(Enum):
          RED = 'red'
          GREEN = 'green'
          BLUE = 'blue'

      color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

      match color:
          case Color.RED:
              print("I see red!")
          case Color.GREEN:
              print("Grass is green")
          case Color.BLUE:
              print("I'm feeling the blues :(")

Podrobnější vysvětlení a další příklady najdete v dokumentu :pep:`636`, který
je napsán formou tutorialu.

.. _tut-functions:

Definování funkcí
==================

Můžeme vytvořit funkci, která vypíše Fibonacciho posloupnost až po libovolnou
hranici::

   >>> def fib(n):    # write Fibonacci series less than n
   ...     """Print a Fibonacci series less than n."""
   ...     a, b = 0, 1
   ...     while a < n:
   ...         print(a, end=' ')
   ...         a, b = b, a+b
   ...     print()
   ...
   >>> # Now call the function we just defined:
   >>> fib(2000)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

.. index::
   single: documentation strings
   single: docstrings
   single: strings, documentation

Klíčové slovo :keyword:`def` uvádí *definici* funkce. Musí za ním následovat
název funkce a seznam formálních parametrů v závorkách. Příkazy tvořící tělo
funkce začínají na následujícím řádku a musí být odsazené.

Prvním příkazem těla funkce může být řetězcový literál; tento literál je
dokumentačním řetězcem funkce neboli :dfn:`docstringem`. (Více o dokumentačních
řetězcích najdete v části :ref:`tut-docstrings`.) Některé nástroje pomocí nich
automaticky vytvářejí online či tištěnou dokumentaci nebo umožňují interaktivní
procházení kódu. Je dobrým zvykem dokumentační řetězce do vlastního kódu
zahrnovat.

*Provedení* funkce zavede novou tabulku symbolů používanou pro její lokální
proměnné. Přesněji řečeno, všechna přiřazení proměnným ve funkci ukládají
hodnotu do lokální tabulky symbolů. Odkazy na proměnné se nejprve hledají
v lokální tabulce symbolů, poté v lokálních tabulkách obklopujících funkcí,
následně v globální tabulce symbolů a nakonec v tabulce vestavěných názvů.
Globálním proměnným a proměnným obklopujících funkcí proto nelze uvnitř funkce
přímo přiřazovat (nejsou-li globální proměnné uvedeny v příkazu
:keyword:`global` nebo proměnné obklopujících funkcí v příkazu
:keyword:`nonlocal`), lze však na ně odkazovat.

Skutečné parametry (argumenty) volání funkce se při volání vloží do lokální
tabulky symbolů volané funkce. Argumenty se tedy předávají *hodnotou*, přičemž
touto *hodnotou* je vždy *odkaz* na objekt, nikoli hodnota objektu. [#]_ Když
funkce zavolá jinou funkci nebo rekurzivně sama sebe, vytvoří se pro dané volání
nová lokální tabulka symbolů.

Definice funkce spojí v aktuální tabulce symbolů název funkce s objektem funkce.
Interpret rozpoznává objekt, na který tento název odkazuje, jako uživatelem
definovanou funkci. Na tentýž objekt funkce mohou odkazovat i jiné názvy, které
lze rovněž použít k přístupu k funkci::

   >>> fib
   <function fib at 10042ed0>
   >>> f = fib
   >>> f(100)
   0 1 1 2 3 5 8 13 21 34 55 89

Znáte-li jiné jazyky, můžete namítnout, že ``fib`` není funkce, ale procedura,
protože nevrací hodnotu. Ve skutečnosti i funkce bez příkazu :keyword:`return`
hodnotu vracejí, byť nepříliš zajímavou. Nazývá se ``None`` (jde o vestavěný
název). Pokud by byla ``None`` jedinou vypisovanou hodnotou, interpret její
výpis obvykle potlačí. Chcete-li ji přesto zobrazit, použijte :func:`print`::

   >>> fib(0)
   >>> print(fib(0))
   None

Snadno lze napsat funkci, která namísto výpisu vrátí seznam čísel Fibonacciho
posloupnosti::

   >>> def fib2(n):  # return Fibonacci series up to n
   ...     """Return a list containing the Fibonacci series up to n."""
   ...     result = []
   ...     a, b = 0, 1
   ...     while a < n:
   ...         result.append(a)    # see below
   ...         a, b = b, a+b
   ...     return result
   ...
   >>> f100 = fib2(100)    # call it
   >>> f100                # write the result
   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Tento příklad jako obvykle ukazuje několik nových vlastností Pythonu:

* Příkaz :keyword:`return` ukončí funkci a vrátí z ní hodnotu. Příkaz
  :keyword:`!return` bez výrazu vrací ``None``. Také dosažení konce funkce vrátí
  ``None``.

* Příkaz ``result.append(a)`` volá *metodu* objektu seznamu ``result``. Metoda
  je funkce, která „patří“ objektu, a zapisuje se jako ``obj.methodname``, kde
  ``obj`` je nějaký objekt (může jít o výraz) a ``methodname`` je název metody
  definované typem objektu. Různé typy definují různé metody. Metody různých
  typů mohou mít stejný název bez nejednoznačnosti. (Vlastní typy objektů
  a metody lze definovat pomocí *tříd*, viz :ref:`tut-classes`.) Metoda
  :meth:`~list.append` z příkladu je definována pro seznamy a přidá nový prvek
  na konec seznamu. V tomto příkladu odpovídá zápisu ``result = result + [a]``,
  je však efektivnější.


.. _tut-defining:

Více o definování funkcí
==========================

Lze definovat také funkce s proměnným počtem argumentů. Existují tři vzájemně
kombinovatelné podoby.


.. _tut-defaultargs:

Výchozí hodnoty argumentů
-------------------------

Nejužitečnější podobou je zadání výchozí hodnoty jednoho či více argumentů.
Vznikne tak funkce, kterou lze volat s menším počtem argumentů, než kolik jich
její definice připouští. Například::

   def ask_ok(prompt, retries=4, reminder='Please try again!'):
       while True:
           reply = input(prompt)
           if reply in {'y', 'ye', 'yes'}:
               return True
           if reply in {'n', 'no', 'nop', 'nope'}:
               return False
           retries = retries - 1
           if retries < 0:
               raise ValueError('invalid user response')
           print(reminder)

Tuto funkci lze volat několika způsoby:

* pouze s povinným argumentem:
  ``ask_ok('Do you really want to quit?')``
* s jedním z nepovinných argumentů:
  ``ask_ok('OK to overwrite the file?', 2)``
* nebo dokonce se všemi argumenty:
  ``ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')``

Příklad představuje také klíčové slovo :keyword:`in`, které testuje, zda
sekvence obsahuje určitou hodnotu.

Výchozí hodnoty se vyhodnotí v okamžiku definice funkce v jejím *definičním*
oboru platnosti, takže ::

   i = 5

   def f(arg=i):
       print(arg)

   i = 6
   f()

vypíše ``5``.

**Důležité upozornění:** Výchozí hodnota se vyhodnotí pouze jednou. To je
podstatné, pokud jde o měnitelný objekt, například seznam, slovník nebo instanci
většiny tříd. Následující funkce například hromadí argumenty předané při
postupných voláních::

   def f(a, L=[]):
       L.append(a)
       return L

   print(f(1))
   print(f(2))
   print(f(3))

Výsledkem bude ::

   [1]
   [1, 2]
   [1, 2, 3]

Nechcete-li výchozí hodnotu sdílet mezi následujícími voláními, můžete funkci
napsat takto::

   def f(a, L=None):
       if L is None:
           L = []
       L.append(a)
       return L


.. _tut-keywordargs:

Argumenty klíčových slov
------------------------

Funkce lze volat také pomocí :term:`argumentů klíčových slov <keyword argument>`
ve tvaru ``kwarg=value``. Například následující funkce::

   def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
       print("-- This parrot wouldn't", action, end=' ')
       print("if you put", voltage, "volts through it.")
       print("-- Lovely plumage, the", type)
       print("-- It's", state, "!")

přijímá jeden povinný argument (``voltage``) a tři nepovinné argumenty
(``state``, ``action`` a ``type``). Lze ji volat kterýmkoli z následujících
způsobů::

   parrot(1000)                                          # 1 positional argument
   parrot(voltage=1000)                                  # 1 keyword argument
   parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
   parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
   parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
   parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

všechna následující volání jsou však neplatná::

   parrot()                     # required argument missing
   parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
   parrot(110, voltage=220)     # duplicate value for the same argument
   parrot(actor='John Cleese')  # unknown keyword argument

Při volání funkce musejí argumenty klíčových slov následovat za pozičními
argumenty. Všechny předané argumenty klíčových slov musejí odpovídat některému
z argumentů přijímaných funkcí (například ``actor`` není platným argumentem
funkce ``parrot``), na jejich pořadí však nezáleží. To platí i pro povinné
argumenty (například ``parrot(voltage=1000)`` je rovněž platné). Žádný argument
nesmí obdržet hodnotu více než jednou. Následující příklad kvůli tomuto omezení
selže::

   >>> def function(a):
   ...     pass
   ...
   >>> function(0, a=0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: function() got multiple values for argument 'a'

Je-li posledním formálním parametrem parametr ve tvaru ``**name``, obdrží
slovník (viz :ref:`typesmapping`) se všemi argumenty klíčových slov kromě těch,
které odpovídají formálním parametrům. Lze jej zkombinovat s formálním
parametrem ve tvaru ``*name`` (popsaným v následujícím pododdílu), který obdrží
:ref:`n-tici <tut-tuples>` pozičních argumentů přesahujících seznam formálních
parametrů. (``*name`` musí být uvedeno před ``**name``.) Definujeme-li například
následující funkci::

   def cheeseshop(kind, *arguments, **keywords):
       print("-- Do you have any", kind, "?")
       print("-- I'm sorry, we're all out of", kind)
       for arg in arguments:
           print(arg)
       print("-" * 40)
       for kw in keywords:
           print(kw, ":", keywords[kw])

lze ji zavolat takto::

   cheeseshop("Limburger", "It's very runny, sir.",
              "It's really very, VERY runny, sir.",
              shopkeeper="Michael Palin",
              client="John Cleese",
              sketch="Cheese Shop Sketch")

a samozřejmě vypíše:

.. code-block:: none

   -- Do you have any Limburger ?
   -- I'm sorry, we're all out of Limburger
   It's very runny, sir.
   It's really very, VERY runny, sir.
   ----------------------------------------
   shopkeeper : Michael Palin
   client : John Cleese
   sketch : Cheese Shop Sketch

Pořadí, v němž se argumenty klíčových slov vypíší, zaručeně odpovídá pořadí,
v němž byly zadány při volání funkce.

Speciální parametry
-------------------

Ve výchozím nastavení lze argumenty funkci Pythonu předávat buď podle pozice,
nebo explicitně pomocí klíčového slova. Kvůli čitelnosti a výkonu může být
vhodné způsoby předávání omezit, aby vývojář pouhým pohledem na definici funkce
poznal, zda se položky předávají pozičně, pozičně nebo klíčovým slovem, či pouze
klíčovým slovem.

Definice funkce může vypadat takto:

.. code-block:: none

   def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
         -----------    ----------     ----------
           |             |                  |
           |        Positional or keyword   |
           |                                - Keyword only
            -- Positional only

kde ``/`` a ``*`` jsou nepovinné. Jsou-li použity, určují druh parametru podle
toho, jak lze argumenty funkci předat: pouze pozičně, pozičně nebo klíčovým
slovem a pouze klíčovým slovem. Parametry klíčových slov se označují také jako
pojmenované parametry.

------------------------------------------------
Poziční argumenty nebo argumenty klíčových slov
------------------------------------------------

Neobsahuje-li definice funkce ``/`` ani ``*``, lze argumenty funkci předat
pozičně nebo pomocí klíčového slova.

--------------------------
Pouze poziční parametry
--------------------------

Podrobněji lze některé parametry označit jako *pouze poziční*. U těchto
parametrů záleží na pořadí a nelze je předat pomocí klíčového slova. Pouze
poziční parametry se umísťují před ``/`` (lomítko), které je logicky odděluje
od ostatních parametrů. Pokud definice funkce ``/`` neobsahuje, nemá žádné
parametry určené pouze pro poziční předání.

Parametry následující za ``/`` mohou být *poziční nebo klíčové* či *pouze
klíčové*.

------------------------------
Pouze argumenty klíčových slov
------------------------------

Chcete-li parametry označit jako *pouze klíčové*, takže musejí být předány
argumentem klíčového slova, vložte v seznamu argumentů ``*`` těsně před první
parametr určený *pouze pro klíčové slovo*.

-----------------
Příklady funkcí
-----------------

Prohlédněte si následující příklady definic funkcí a věnujte pozornost značkám
``/`` a ``*``::

   >>> def standard_arg(arg):
   ...     print(arg)
   ...
   >>> def pos_only_arg(arg, /):
   ...     print(arg)
   ...
   >>> def kwd_only_arg(*, arg):
   ...     print(arg)
   ...
   >>> def combined_example(pos_only, /, standard, *, kwd_only):
   ...     print(pos_only, standard, kwd_only)


První definice funkce, ``standard_arg``, má nejběžnější podobu. Neomezuje způsob
volání a argumenty lze předávat pozičně i pomocí klíčového slova::

   >>> standard_arg(2)
   2

   >>> standard_arg(arg=2)
   2

Druhá funkce, ``pos_only_arg``, dovoluje pouze poziční parametry, protože její
definice obsahuje ``/``::

   >>> pos_only_arg(1)
   1

   >>> pos_only_arg(arg=1)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

Třetí funkce, ``kwd_only_arg``, dovoluje pouze argumenty klíčových slov, jak
ukazuje ``*`` v její definici::

   >>> kwd_only_arg(3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

   >>> kwd_only_arg(arg=3)
   3

Poslední funkce používá v jediné definici všechny tři způsoby volání::

   >>> combined_example(1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: combined_example() takes 2 positional arguments but 3 were given

   >>> combined_example(1, 2, kwd_only=3)
   1 2 3

   >>> combined_example(1, standard=2, kwd_only=3)
   1 2 3

   >>> combined_example(pos_only=1, standard=2, kwd_only=3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'


Nakonec se podívejte na definici funkce, v níž může dojít ke kolizi mezi
pozičním argumentem ``name`` a ``**kwds``, který obsahuje klíč ``name``::

    def foo(name, **kwds):
        return 'name' in kwds

Neexistuje volání, při němž by funkce vrátila ``True``, protože klíčové slovo
``'name'`` se vždy naváže na první parametr. Například::

    >>> foo(1, **{'name': 2})
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: foo() got multiple values for argument 'name'
    >>>

S použitím ``/`` (argumentů pouze pozičních) to však možné je, protože ``name``
může být pozičním argumentem a ``'name'`` zároveň klíčem mezi argumenty
klíčových slov::

    >>> def foo(name, /, **kwds):
    ...     return 'name' in kwds
    ...
    >>> foo(1, **{'name': 2})
    True

Jinými slovy, názvy pouze pozičních parametrů lze bez nejednoznačnosti použít
v ``**kwds``.

-------
Shrnutí
-------

Volba parametrů v definici funkce závisí na způsobu jejího použití::

   def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

Obecná doporučení:

* Pouze poziční parametry použijte, nechcete-li uživateli zpřístupnit jejich
  názvy. Hodí se to, když názvy parametrů nemají skutečný význam, chcete-li při
  volání funkce vynutit pořadí argumentů nebo potřebujete přijmout několik
  pozičních parametrů a libovolná klíčová slova.
* Pouze klíčové parametry použijte, když mají názvy význam a jejich explicitní
  uvedení zpřehlední definici funkce, nebo nechcete, aby uživatelé spoléhali na
  pozici předávaného argumentu.
* V API používejte pouze poziční parametry, chcete-li zabránit nekompatibilním
  změnám API při budoucím přejmenování parametru.

.. _tut-arbitraryargs:

Libovolné seznamy argumentů
---------------------------

.. index::
   single: * (asterisk); in function calls

Poslední, nejméně často používanou možností je určit, že lze funkci volat
s libovolným počtem argumentů. Tyto argumenty se zabalí do n-tice (viz
:ref:`tut-tuples`). Před proměnným počtem argumentů může být uvedeno libovolné
množství běžných argumentů včetně nuly. ::

   def write_multiple_items(file, separator, *args):
       file.write(separator.join(args))


Tyto *variadické* argumenty bývají obvykle na konci seznamu formálních
parametrů, protože zachytí všechny zbývající vstupní argumenty předané funkci.
Formální parametry uvedené za parametrem ``*args`` jsou argumenty „pouze
klíčových slov“, takže je lze použít pouze jako klíčové, nikoli poziční. ::

   >>> def concat(*args, sep="/"):
   ...     return sep.join(args)
   ...
   >>> concat("earth", "mars", "venus")
   'earth/mars/venus'
   >>> concat("earth", "mars", "venus", sep=".")
   'earth.mars.venus'

.. _tut-unpacking-arguments:

Rozbalování seznamů argumentů
-----------------------------

Opačná situace nastane, když jsou argumenty již v seznamu nebo n-tici, ale pro
volání funkce vyžadující samostatné poziční argumenty je třeba je rozbalit.
Vestavěná funkce :func:`range` například očekává samostatné argumenty *start*
a *stop*. Nejsou-li k dispozici odděleně, zapište volání funkce s operátorem
``*``, který argumenty ze seznamu nebo n-tice rozbalí::

   >>> list(range(3, 6))            # normal call with separate arguments
   [3, 4, 5]
   >>> args = [3, 6]
   >>> list(range(*args))            # call with arguments unpacked from a list
   [3, 4, 5]

.. index::
   single: **; in function calls

Stejným způsobem mohou slovníky předávat argumenty klíčových slov pomocí
operátoru ``**``::

   >>> def parrot(voltage, state='a stiff', action='voom'):
   ...     print("-- This parrot wouldn't", action, end=' ')
   ...     print("if you put", voltage, "volts through it.", end=' ')
   ...     print("E's", state, "!")
   ...
   >>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
   >>> parrot(**d)
   -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


.. _tut-lambda:

Lambda výrazy
------------------

Malé anonymní funkce lze vytvářet pomocí klíčového slova :keyword:`lambda`.
Tato funkce vrací součet svých dvou argumentů: ``lambda a, b: a+b``. Lambda
funkce lze použít všude, kde je vyžadován objekt funkce. Syntakticky jsou
omezené na jediný výraz. Z hlediska významu jde pouze o syntaktické usnadnění
běžné definice funkce. Stejně jako vnořené definice funkcí mohou lambda funkce
odkazovat na proměnné z obklopujícího oboru platnosti::

   >>> def make_incrementor(n):
   ...     return lambda x: x + n
   ...
   >>> f = make_incrementor(42)
   >>> f(0)
   42
   >>> f(1)
   43

Předchozí příklad používá lambda výraz k vrácení funkce. Další možností je
předat malou funkci jako argument. Metoda :meth:`list.sort` například přijímá
funkci třídicího klíče *key*, kterou může být lambda funkce::

   >>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
   >>> pairs.sort(key=lambda pair: pair[1])
   >>> pairs
   [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


.. _tut-docstrings:

Dokumentační řetězce
---------------------

.. index::
   single: docstrings
   single: documentation strings
   single: strings, documentation

Pro obsah a formátování dokumentačních řetězců platí několik konvencí.

První řádek by měl vždy obsahovat krátké a výstižné shrnutí účelu objektu.
Kvůli stručnosti by neměl explicitně uvádět název ani typ objektu, protože tyto
údaje jsou dostupné jinými prostředky (s výjimkou případu, kdy je názvem
sloveso popisující činnost funkce). Řádek by měl začínat velkým písmenem
a končit tečkou.

Má-li dokumentační řetězec více řádků, druhý řádek by měl být prázdný, aby
shrnutí vizuálně oddělil od zbytku popisu. Následující řádky by měly tvořit
jeden či více odstavců popisujících způsob volání objektu, jeho vedlejší účinky
a podobně.

Syntaktický analyzátor Pythonu odstraní odsazení z víceřádkových řetězcových
literálů, které slouží jako dokumentační řetězce modulů, tříd nebo funkcí.

Příklad víceřádkového dokumentačního řetězce::

   >>> def my_function():
   ...     """Do nothing, but document it.
   ...
   ...     No, really, it doesn't do anything:
   ...
   ...         >>> my_function()
   ...         >>>
   ...     """
   ...     pass
   ...
   >>> print(my_function.__doc__)
   Do nothing, but document it.

   No, really, it doesn't do anything:

       >>> my_function()
       >>>


.. _tut-annotations:

Anotace funkcí
--------------------

.. sectionauthor:: Zachary Ware <zachary.ware@gmail.com>
.. index::
   pair: function; annotations
   single: ->; function annotations
   single: : (colon); function annotations

:ref:`Anotace funkcí <function>` jsou zcela nepovinná metadata o typech
používaných uživatelsky definovanými funkcemi (více informací obsahují
:pep:`3107` a :pep:`484`).

:term:`Anotace <function annotation>` se ukládají jako slovník do atributu
:attr:`~object.__annotations__` funkce a nemají vliv na žádnou jinou část
funkce. Anotace parametru se definuje dvojtečkou za jeho názvem a následujícím
výrazem, jehož výsledkem je hodnota anotace. Anotace návratové hodnoty se
definuje literálem ``->`` následovaným výrazem mezi seznamem parametrů
a dvojtečkou označující konec příkazu :keyword:`def`. Následující příklad má
anotovaný povinný argument, nepovinný argument i návratovou hodnotu::

   >>> def f(ham: str, eggs: str = 'eggs') -> str:
   ...     print("Annotations:", f.__annotations__)
   ...     print("Arguments:", ham, eggs)
   ...     return ham + ' and ' + eggs
   ...
   >>> f('spam')
   Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
   Arguments: spam eggs
   'spam and eggs'

.. _tut-codingstyle:

Intermezzo: Styl kódu
========================

.. sectionauthor:: Georg Brandl <georg@python.org>
.. index:: pair: coding; style

Nyní, když se chystáte psát delší a složitější úseky Pythonu, je vhodná chvíle
promluvit si o *stylu kódu*. Většinu jazyků lze zapisovat (přesněji řečeno
*formátovat*) různými styly, z nichž některé jsou čitelnější než jiné. Vždy je
dobré usnadnit ostatním čtení vašeho kódu a vhodný styl tomu výrazně pomáhá.

Pro Python se průvodcem stylem dodržovaným většinou projektů stal :pep:`8`.
Prosazuje velmi čitelný a vzhledný styl kódu. Každý vývojář v Pythonu by si jej
měl někdy přečíst; zde jsou jeho nejdůležitější body:

* Používejte odsazení čtyřmi mezerami, nikoli tabulátory.

  Čtyři mezery představují dobrý kompromis mezi malým odsazením (umožňujícím
  hlubší vnoření) a velkým odsazením (které se snáze čte). Tabulátory způsobují
  nejasnosti, a proto je nejlepší je vynechat.

* Zalamujte řádky tak, aby nepřekročily 79 znaků.

  Pomáhá to uživatelům s malými displeji a na větších umožňuje zobrazit několik
  souborů s kódem vedle sebe.

* Funkce, třídy a větší bloky kódu uvnitř funkcí oddělujte prázdnými řádky.

* Je-li to možné, umísťujte komentáře na samostatné řádky.

* Používejte dokumentační řetězce.

* Používejte mezery kolem operátorů a za čárkami, nikoli však těsně uvnitř
  závorek: ``a = f(1, 2) + g(3, 4)``.

* Třídy a funkce pojmenovávejte konzistentně; podle konvence se pro třídy
  používá ``UpperCamelCase`` a pro funkce a metody ``lowercase_with_underscores``.
  První argument metody vždy pojmenovávejte ``self`` (více o třídách a metodách
  viz :ref:`tut-firstclasses`).

* Má-li se váš kód používat v mezinárodním prostředí, nepoužívejte neobvyklá
  kódování. Nejlépe vždy funguje výchozí kódování Pythonu UTF-8, případně prosté
  ASCII.

* Podobně nepoužívejte v identifikátorech znaky mimo ASCII, existuje-li sebemenší
  možnost, že budou kód číst nebo udržovat lidé hovořící jiným jazykem.


.. rubric:: Poznámky pod čarou

.. [#] Přesnějším popisem by vlastně bylo *volání odkazem na objekt*, protože
   při předání měnitelného objektu volající uvidí všechny změny, které v něm
   volaná funkce provede (například prvky vložené do seznamu).
