.. _tut-structures:

****************
Datové struktury
****************

Tato kapitola podrobněji popisuje některé věci, které jste se již naučili,
a přidává také několik nových.

.. _tut-morelists:

Více o seznamech
================

Datový typ :ref:`seznam <typesseq-list>` nabízí několik dalších metod. Zde jsou
všechny metody objektů seznamu:

.. method:: list.append(value, /)
   :noindex:

   Přidá prvek na konec seznamu. Odpovídá zápisu ``a[len(a):] = [x]``.


.. method:: list.extend(iterable, /)
   :noindex:

   Rozšíří seznam přidáním všech prvků z iterovatelného objektu. Odpovídá
   zápisu ``a[len(a):] = iterable``.


.. method:: list.insert(index, value, /)
   :noindex:

   Vloží prvek na zadanou pozici. Prvním argumentem je index prvku, před který
   se má nový prvek vložit; ``a.insert(0, x)`` jej tedy vloží na začátek seznamu
   a ``a.insert(len(a), x)`` odpovídá ``a.append(x)``.


.. method:: list.remove(value, /)
   :noindex:

   Odstraní první prvek seznamu, jehož hodnota se rovná *value*. Pokud takový
   prvek neexistuje, vyvolá :exc:`ValueError`.


.. method:: list.pop(index=-1, /)
   :noindex:

   Odstraní prvek na zadané pozici v seznamu a vrátí jej. Není-li index zadán,
   ``a.pop()`` odstraní a vrátí poslední prvek seznamu. Je-li seznam prázdný
   nebo index mimo jeho rozsah, vyvolá :exc:`IndexError`.


.. method:: list.clear()
   :noindex:

   Odstraní ze seznamu všechny prvky. Odpovídá ``del a[:]``.


.. method:: list.index(value[, start[, stop]])
   :noindex:

   Vrátí index prvního výskytu hodnoty *value* v seznamu, číslovaný od nuly.
   Pokud takový prvek neexistuje, vyvolá :exc:`ValueError`.

   Nepovinné argumenty *start* a *end* se interpretují stejně jako v zápisu
   výřezu a omezují hledání na určitou podsekvenci seznamu. Vrácený index se
   počítá vzhledem k začátku celé sekvence, nikoli vzhledem k argumentu *start*.


.. method:: list.count(value, /)
   :noindex:

   Vrátí počet výskytů hodnoty *value* v seznamu.


.. method:: list.sort(*, key=None, reverse=False)
   :noindex:

   Seřadí prvky seznamu na místě (argumenty lze použít k přizpůsobení řazení;
   jejich vysvětlení obsahuje :func:`sorted`).


.. method:: list.reverse()
   :noindex:

   Obrátí pořadí prvků seznamu na místě.


.. method:: list.copy()
   :noindex:

   Vrátí mělkou kopii seznamu. Odpovídá ``a[:]``.


Příklad používající většinu metod seznamu::

    >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    >>> fruits.count('apple')
    2
    >>> fruits.count('tangerine')
    0
    >>> fruits.index('banana')
    3
    >>> fruits.index('banana', 4)  # Find next banana starting at position 4
    6
    >>> fruits.reverse()
    >>> fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
    >>> fruits.append('grape')
    >>> fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
    >>> fruits.sort()
    >>> fruits
    ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
    >>> fruits.pop()
    'pear'

Možná jste si všimli, že metody jako ``insert``, ``remove`` nebo ``sort``, které
seznam pouze mění, nemají vypsanou návratovou hodnotu — vracejí výchozí
``None``. [#]_ Jde o návrhový princip všech měnitelných datových struktur
v Pythonu.

Také ne všechna data lze řadit nebo porovnávat. Seznam ``[None, 'hello', 10]``
například nelze seřadit, protože celá čísla nelze porovnávat s řetězci a
``None`` s jinými typy. Některé typy navíc nemají definované uspořádání;
například ``3+4j < 5+7j`` není platným porovnáním.


.. _tut-lists-as-stacks:

Použití seznamů jako zásobníků
------------------------------

.. sectionauthor:: Ka-Ping Yee <ping@lfw.org>


Metody seznamů velmi usnadňují použití seznamu jako zásobníku, v němž se
naposledy přidaný prvek vyjme jako první („last-in, first-out“, LIFO). Prvek na
vrchol zásobníku přidáte pomocí :meth:`~list.append`. Prvek z vrcholu vyjmete
pomocí :meth:`~list.pop` bez explicitního indexu. Například::

   >>> stack = [3, 4, 5]
   >>> stack.append(6)
   >>> stack.append(7)
   >>> stack
   [3, 4, 5, 6, 7]
   >>> stack.pop()
   7
   >>> stack
   [3, 4, 5, 6]
   >>> stack.pop()
   6
   >>> stack.pop()
   5
   >>> stack
   [3, 4]


.. _tut-lists-as-queues:

Použití seznamů jako front
---------------------------

.. sectionauthor:: Ka-Ping Yee <ping@lfw.org>

Seznam lze použít také jako frontu, v níž se první přidaný prvek vyjme jako
první („first-in, first-out“, FIFO), pro tento účel však seznamy nejsou
efektivní. Přidávání a odebírání z konce seznamu je rychlé, ale vkládání nebo
odebírání z jeho začátku je pomalé, protože se všechny ostatní prvky musejí
posunout o jednu pozici.

K implementaci fronty použijte :class:`collections.deque`, která byla navržena
pro rychlé přidávání a odebírání z obou konců. Například::

   >>> from collections import deque
   >>> queue = deque(["Eric", "John", "Michael"])
   >>> queue.append("Terry")           # Terry arrives
   >>> queue.append("Graham")          # Graham arrives
   >>> queue.popleft()                 # The first to arrive now leaves
   'Eric'
   >>> queue.popleft()                 # The second to arrive now leaves
   'John'
   >>> queue                           # Remaining queue in order of arrival
   deque(['Michael', 'Terry', 'Graham'])


.. _tut-listcomps:

Generování seznamů
-------------------

Generátorová notace seznamu (list comprehension) poskytuje stručný způsob
vytváření seznamů. Běžně se používá k vytvoření seznamu, jehož každý prvek je
výsledkem operace použité na prvek jiné sekvence či iterovatelného objektu, nebo
k vytvoření podsekvence prvků splňujících určitou podmínku.

Předpokládejme například, že chceme vytvořit seznam druhých mocnin::

   >>> squares = []
   >>> for x in range(10):
   ...     squares.append(x**2)
   ...
   >>> squares
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Tím se vytvoří (nebo přepíše) proměnná ``x``, která existuje i po dokončení
cyklu. Seznam druhých mocnin můžeme bez vedlejších účinků vypočítat pomocí::

   squares = list(map(lambda x: x**2, range(10)))

nebo rovnocenně::

   squares = [x**2 for x in range(10)]

což je stručnější a čitelnější.

Generátorová notace seznamu se skládá ze závorek obsahujících výraz následovaný
částí :keyword:`!for` a poté libovolným počtem částí :keyword:`!for` nebo
:keyword:`!if`. Výsledkem je nový seznam vzniklý vyhodnocením výrazu v kontextu
následujících částí :keyword:`!for` a :keyword:`!if`. Tento zápis například
kombinuje nestejné prvky dvou seznamů::

   >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

a odpovídá::

   >>> combs = []
   >>> for x in [1,2,3]:
   ...     for y in [3,1,4]:
   ...         if x != y:
   ...             combs.append((x, y))
   ...
   >>> combs
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Všimněte si, že pořadí příkazů :keyword:`for` a :keyword:`if` je v obou
ukázkách stejné.

Je-li výrazem n-tice (například ``(x, y)`` v předchozím příkladu), musí být
uzavřena v závorkách. ::

   >>> vec = [-4, -2, 0, 2, 4]
   >>> # create a new list with the values doubled
   >>> [x*2 for x in vec]
   [-8, -4, 0, 4, 8]
   >>> # filter the list to exclude negative numbers
   >>> [x for x in vec if x >= 0]
   [0, 2, 4]
   >>> # apply a function to all the elements
   >>> [abs(x) for x in vec]
   [4, 2, 0, 2, 4]
   >>> # call a method on each element
   >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
   >>> [weapon.strip() for weapon in freshfruit]
   ['banana', 'loganberry', 'passion fruit']
   >>> # create a list of 2-tuples like (number, square)
   >>> [(x, x**2) for x in range(6)]
   [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
   >>> # the tuple must be parenthesized, otherwise an error is raised
   >>> [x, x**2 for x in range(6)]
     File "<stdin>", line 1
       [x, x**2 for x in range(6)]
        ^^^^^^^
   SyntaxError: did you forget parentheses around the comprehension target?
   >>> # flatten a list using a listcomp with two 'for'
   >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
   >>> [num for elem in vec for num in elem]
   [1, 2, 3, 4, 5, 6, 7, 8, 9]

Generátorová notace seznamu může obsahovat složité výrazy a vnořené funkce::

   >>> from math import pi
   >>> [str(round(pi, i)) for i in range(1, 6)]
   ['3.1', '3.14', '3.142', '3.1416', '3.14159']

Vnořené generování seznamů
--------------------------

Úvodním výrazem generátorové notace seznamu může být libovolný výraz, včetně
další generátorové notace seznamu.

Prohlédněte si následující matici 3×4 implementovanou jako seznam tří seznamů
délky 4::

   >>> matrix = [
   ...     [1, 2, 3, 4],
   ...     [5, 6, 7, 8],
   ...     [9, 10, 11, 12],
   ... ]

Následující generátorová notace seznamu zamění řádky a sloupce::

   >>> [[row[i] for row in matrix] for i in range(4)]
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

Jak jsme viděli v předchozí části, vnitřní generátorová notace seznamu se
vyhodnocuje v kontextu následujícího :keyword:`for`, takže příklad odpovídá::

   >>> transposed = []
   >>> for i in range(4):
   ...     transposed.append([row[i] for row in matrix])
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

což je zase totéž jako::

   >>> transposed = []
   >>> for i in range(4):
   ...     # the following 3 lines implement the nested listcomp
   ...     transposed_row = []
   ...     for row in matrix:
   ...         transposed_row.append(row[i])
   ...     transposed.append(transposed_row)
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

V praxi dávejte před složitými příkazy řízení toku přednost vestavěným funkcím.
V tomto případě se výborně hodí funkce :func:`zip`::

   >>> list(zip(*matrix))
   [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

Podrobnosti o hvězdičce na tomto řádku obsahuje :ref:`tut-unpacking-arguments`.

.. _tut-del:

Příkaz :keyword:`!del`
=============================

Prvek seznamu lze namísto jeho hodnoty odstranit také podle indexu, a to
příkazem :keyword:`del`. Tím se liší od metody :meth:`~list.pop`, která hodnotu
vrací. Příkaz :keyword:`!del` lze použít rovněž k odstranění výřezů ze seznamu
nebo k vyprázdnění celého seznamu (což jsme dříve provedli přiřazením prázdného
seznamu do výřezu). Například::

   >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
   >>> del a[0]
   >>> a
   [1, 66.25, 333, 333, 1234.5]
   >>> del a[2:4]
   >>> a
   [1, 66.25, 1234.5]
   >>> del a[:]
   >>> a
   []

:keyword:`del` lze použít také k odstranění celých proměnných::

   >>> del a

Následný odkaz na název ``a`` skončí chybou (alespoň dokud mu nebude přiřazena
jiná hodnota). S dalšími způsoby použití :keyword:`del` se setkáme později.


.. _tut-tuples:

N-tice a sekvence
====================

Viděli jsme, že seznamy a řetězce mají mnoho společných vlastností, například
indexování a vytváření výřezů. Jde o dva příklady *sekvenčních* datových typů
(viz :ref:`typesseq`). Python se neustále vyvíjí, takže mohou přibýt další
sekvenční datové typy. Existuje také jiný standardní sekvenční typ: *n-tice*.

N-tici tvoří několik hodnot oddělených čárkami, například::

   >>> t = 12345, 54321, 'hello!'
   >>> t[0]
   12345
   >>> t
   (12345, 54321, 'hello!')
   >>> # Tuples may be nested:
   >>> u = t, (1, 2, 3, 4, 5)
   >>> u
   ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
   >>> # Tuples are immutable:
   >>> t[0] = 88888
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment
   >>> # but they can contain mutable objects:
   >>> v = ([1, 2, 3], [3, 2, 1])
   >>> v
   ([1, 2, 3], [3, 2, 1])


Jak vidíte, na výstupu jsou n-tice vždy uzavřeny v závorkách, aby se vnořené
n-tice interpretovaly správně. Při vstupu je lze zadat se závorkami i bez nich,
ačkoli jsou závorky často i tak nezbytné (je-li n-tice součástí většího
výrazu). Jednotlivým prvkům n-tice nelze přiřazovat, n-tice však mohou obsahovat
měnitelné objekty, například seznamy.

Ačkoli se n-tice mohou podobat seznamům, často se používají v jiných situacích
a k jiným účelům. N-tice jsou :term:`neměnné <immutable>` a obvykle obsahují
heterogenní sekvenci prvků, k nimž se přistupuje rozbalením (viz dále v tomto
části), indexováním nebo v případě :func:`pojmenovaných n-tic
<collections.namedtuple>` dokonce atributem. Seznamy jsou :term:`měnitelné
<mutable>`, jejich prvky jsou obvykle homogenní a přistupuje se k nim
procházením seznamu.

Zvláštním případem je vytváření n-tic s 0 nebo 1 prvkem, pro něž má syntaxe
několik dodatečných zvláštností. Prázdná n-tice se vytvoří prázdným párem
závorek; n-tice s jedním prvkem se vytvoří přidáním čárky za hodnotu (uzavření
jediné hodnoty do závorek nestačí). Nevzhledné, ale účinné. Například::

   >>> empty = ()
   >>> singleton = 'hello',    # <-- note trailing comma
   >>> len(empty)
   0
   >>> len(singleton)
   1
   >>> singleton
   ('hello',)

Příkaz ``t = 12345, 54321, 'hello!'`` je příkladem *zabalení n-tice*: hodnoty
``12345``, ``54321`` a ``'hello!'`` se společně zabalí do n-tice. Možná je také
opačná operace::

   >>> x, y, z = t

Ta se příhodně nazývá *rozbalení sekvence* a funguje pro libovolnou sekvenci na
pravé straně. Rozbalení sekvence vyžaduje, aby na levé straně rovnítka bylo
stejné množství proměnných jako prvků sekvence. Vícenásobné přiřazení je tedy
ve skutečnosti pouze kombinací zabalení n-tice a rozbalení sekvence.


.. _tut-sets:

Množiny
=======

Python obsahuje také datový typ pro :ref:`množiny <types-set>`. Množina je
neuspořádaná kolekce bez duplicitních prvků. Používá se zejména k testování
členství a odstraňování duplicit. Objekty množin podporují také matematické
operace, jako jsou sjednocení, průnik, rozdíl a symetrický rozdíl.

Množiny lze vytvářet složenými závorkami nebo funkcí :func:`set`. Prázdnou
množinu je nutné vytvořit pomocí ``set()``, nikoli ``{}``; druhý zápis vytváří
prázdný slovník, tedy datovou strukturu probíranou v následující části.

Protože množiny nejsou uspořádané, mohou se při jejich procházení nebo výpisu
objevit prvky v jiném pořadí, než očekáváte.

Krátká ukázka::

   >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
   >>> print(basket)                      # show that duplicates have been removed
   {'orange', 'banana', 'pear', 'apple'}
   >>> 'orange' in basket                 # fast membership testing
   True
   >>> 'crabgrass' in basket
   False

   >>> # Demonstrate set operations on unique letters from two words
   >>>
   >>> a = set('abracadabra')
   >>> b = set('alacazam')
   >>> a                                  # unique letters in a
   {'a', 'r', 'b', 'c', 'd'}
   >>> a - b                              # letters in a but not in b
   {'r', 'd', 'b'}
   >>> a | b                              # letters in a or b or both
   {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
   >>> a & b                              # letters in both a and b
   {'a', 'c'}
   >>> a ^ b                              # letters in a or b but not both
   {'r', 'd', 'b', 'm', 'z', 'l'}

Podobně jako :ref:`generování seznamů <tut-listcomps>` je podporováno také
generování množin::

   >>> a = {x for x in 'abracadabra' if x not in 'abc'}
   >>> a
   {'r', 'd'}


.. _tut-dictionaries:

Slovníky
============

Dalším užitečným datovým typem vestavěným v Pythonu je *slovník* (viz
:ref:`typesmapping`). V jiných jazycích se slovníky někdy označují jako
„asociativní paměti“ nebo „asociativní pole“. Na rozdíl od sekvencí indexovaných
číselným rozsahem jsou slovníky indexovány *klíči*, jimiž může být libovolný
neměnný typ; řetězce a čísla mohou být klíči vždy. N-tice lze jako klíče použít,
obsahují-li pouze řetězce, čísla nebo jiné n-tice; obsahuje-li n-tice přímo či
nepřímo měnitelný objekt, klíčem být nemůže. Klíči nemohou být seznamy, protože
je lze měnit na místě přiřazením podle indexu či do výřezu nebo metodami jako
:meth:`~list.append` a :meth:`~list.extend`.

Slovník si lze nejlépe představit jako množinu dvojic *klíč: hodnota*, přičemž
klíče musejí být v rámci jednoho slovníku jedinečné. Prázdný slovník vytvoří
pár složených závorek: ``{}``. Seznam dvojic klíč:hodnota oddělených čárkami
uvnitř závorek přidá do slovníku počáteční dvojice; stejným způsobem se slovníky
zapisují na výstupu.

Hlavními operacemi se slovníkem jsou uložení hodnoty pod určitým klíčem
a získání hodnoty podle klíče. Dvojici klíč:hodnota lze také odstranit pomocí
``del``. Uložíte-li hodnotu pod již používaným klíčem, původní hodnota spojená
s tímto klíčem se zapomene.

Získání hodnoty neexistujícího klíče pomocí indexování (``d[key]``) vyvolá
:exc:`KeyError`. Chcete-li se této chybě při přístupu k možná neexistujícímu
klíči vyhnout, použijte metodu :meth:`~dict.get`, která vrátí ``None`` (nebo
zadanou výchozí hodnotu), pokud klíč ve slovníku není.

Použití ``list(d)`` na slovník vrátí seznam všech jeho klíčů v pořadí vložení
(chcete-li je seřadit, použijte ``sorted(d)``). Přítomnost konkrétního klíče ve
slovníku ověříte klíčovým slovem :keyword:`in`.

Malý příklad použití slovníku::

   >>> tel = {'jack': 4098, 'sape': 4139}
   >>> tel['guido'] = 4127
   >>> tel
   {'jack': 4098, 'sape': 4139, 'guido': 4127}
   >>> tel['jack']
   4098
   >>> tel['irv']
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   KeyError: 'irv'
   >>> print(tel.get('irv'))
   None
   >>> del tel['sape']
   >>> tel['irv'] = 4127
   >>> tel
   {'jack': 4098, 'guido': 4127, 'irv': 4127}
   >>> list(tel)
   ['jack', 'guido', 'irv']
   >>> sorted(tel)
   ['guido', 'irv', 'jack']
   >>> 'guido' in tel
   True
   >>> 'jack' not in tel
   False

Konstruktor :func:`dict` vytváří slovníky přímo ze sekvencí dvojic klíč–hodnota::

   >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

Generátorovou notací slovníku lze navíc vytvářet slovníky z libovolných výrazů
pro klíče a hodnoty::

   >>> {x: x**2 for x in (2, 4, 6)}
   {2: 4, 4: 16, 6: 36}

Jsou-li klíči jednoduché řetězce, je někdy snazší zadat dvojice pomocí
argumentů klíčových slov::

   >>> dict(sape=4139, guido=4127, jack=4098)
   {'sape': 4139, 'guido': 4127, 'jack': 4098}


.. _tut-loopidioms:

Techniky cyklů
==================

Při procházení slovníku lze klíč a odpovídající hodnotu získat současně pomocí
metody :meth:`~dict.items`. ::

   >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   >>> for k, v in knights.items():
   ...     print(k, v)
   ...
   gallahad the pure
   robin the brave

Při procházení sekvence lze poziční index a odpovídající hodnotu získat současně
pomocí funkce :func:`enumerate`. ::

   >>> for i, v in enumerate(['tic', 'tac', 'toe']):
   ...     print(i, v)
   ...
   0 tic
   1 tac
   2 toe

Chcete-li současně procházet dvě či více sekvencí, lze jejich prvky spárovat
funkcí :func:`zip`. ::

   >>> questions = ['name', 'quest', 'favorite color']
   >>> answers = ['lancelot', 'the holy grail', 'blue']
   >>> for q, a in zip(questions, answers):
   ...     print('What is your {0}?  It is {1}.'.format(q, a))
   ...
   What is your name?  It is lancelot.
   What is your quest?  It is the holy grail.
   What is your favorite color?  It is blue.

Chcete-li sekvenci procházet pozpátku, zadejte ji nejprve v dopředném směru
a poté zavolejte funkci :func:`reversed`. ::

   >>> for i in reversed(range(1, 10, 2)):
   ...     print(i)
   ...
   9
   7
   5
   3
   1

K procházení sekvence v seřazeném pořadí použijte funkci :func:`sorted`, která
vrátí nový seřazený seznam a zdroj ponechá beze změny. ::

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for i in sorted(basket):
   ...     print(i)
   ...
   apple
   apple
   banana
   orange
   orange
   pear

Použitím :func:`set` na sekvenci odstraníte duplicitní prvky. Kombinace
:func:`sorted` a :func:`set` je idiomatickým způsobem, jak procházet jedinečné
prvky sekvence v seřazeném pořadí. ::

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for f in sorted(set(basket)):
   ...     print(f)
   ...
   apple
   banana
   orange
   pear

Někdy svádí měnit seznam během jeho procházení, často je však jednodušší
a bezpečnější vytvořit seznam nový. ::

   >>> import math
   >>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
   >>> filtered_data = []
   >>> for value in raw_data:
   ...     if not math.isnan(value):
   ...         filtered_data.append(value)
   ...
   >>> filtered_data
   [56.2, 51.7, 55.3, 52.5, 47.8]


.. _tut-conditions:

Více o podmínkách
==================

Podmínky používané v příkazech ``while`` a ``if`` mohou obsahovat libovolné
operátory, nejen porovnávací.


Porovnávací operátory ``in`` a ``not in`` testují členství, tedy zda se hodnota
nachází či nenachází v kontejneru. Operátory ``is`` a ``is not`` porovnávají,
zda jsou dva objekty skutečně týmž objektem. Všechny porovnávací operátory mají
stejnou prioritu, nižší než všechny číselné operátory.

Porovnání lze řetězit. Například ``a < b == c`` testuje, zda je ``a`` menší než
``b`` a zároveň se ``b`` rovná ``c``.

Porovnání lze spojovat booleovskými operátory ``and`` a ``or`` a výsledek
porovnání (nebo jiného booleovského výrazu) lze negovat pomocí ``not``. Tyto
operátory mají nižší prioritu než porovnávací; mezi nimi má nejvyšší prioritu
``not`` a nejnižší ``or``, takže ``A and not B or C`` odpovídá ``(A and (not
B)) or C``. Požadované seskupení lze jako vždy vyjádřit závorkami.

Booleovské operátory ``and`` a ``or`` používají takzvané *zkrácené
vyhodnocování*: argumenty se vyhodnocují zleva doprava a vyhodnocování se
zastaví, jakmile je výsledek znám. Jsou-li například ``A`` a ``C`` pravdivé,
ale ``B`` nepravdivé, výraz ``A and B and C`` výraz ``C`` nevyhodnotí. Pokud se
výsledek nepoužije jako booleovská, ale obecná hodnota, je návratovou hodnotou
zkráceného operátoru poslední vyhodnocený argument.

Výsledek porovnání nebo jiného booleovského výrazu lze přiřadit proměnné.
Například ::

   >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
   >>> non_null = string1 or string2 or string3
   >>> non_null
   'Trondheim'

Na rozdíl od C se musí přiřazení uvnitř výrazů v Pythonu provést explicitně
pomocí :ref:`mrožího operátoru <why-can-t-i-use-an-assignment-in-an-expression>`
``:=``. Tím se předchází častému problému z programů v C, kdy je ve výrazu
omylem zadáno ``=`` namísto zamýšleného ``==``.


.. _tut-comparing:

Porovnávání sekvencí a jiných typů
===================================
Sekvenční objekty lze obvykle porovnávat s jinými objekty stejného sekvenčního
typu. Porovnání používá *lexikografické* uspořádání: nejprve se porovnají první
dva prvky, a pokud se liší, určí výsledek porovnání; jsou-li stejné, porovnají
se další dva prvky a tak dále, dokud se jedna ze sekvencí nevyčerpá. Jsou-li
porovnávané prvky samy sekvencemi stejného typu, provede se lexikografické
porovnání rekurzivně. Pokud jsou všechny prvky dvou sekvencí shodné, považují se
sekvence za stejné. Je-li jedna sekvence počáteční podsekvencí druhé, je kratší
sekvence menší. Lexikografické uspořádání řetězců řadí jednotlivé znaky podle
čísel jejich kódových bodů Unicode. Několik příkladů porovnání sekvencí stejného
typu::

   (1, 2, 3)              < (1, 2, 4)
   [1, 2, 3]              < [1, 2, 4]
   'ABC' < 'C' < 'Pascal' < 'Python'
   (1, 2, 3, 4)           < (1, 2, 4)
   (1, 2)                 < (1, 2, -1)
   (1, 2, 3)             == (1.0, 2.0, 3.0)
   (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

Objekty různých typů lze pomocí ``<`` nebo ``>`` porovnávat, pokud mají vhodné
porovnávací metody. Smíšené číselné typy se například porovnávají podle své
číselné hodnoty, takže 0 se rovná 0.0 a podobně. V ostatních případech interpret
namísto zavedení libovolného uspořádání vyvolá výjimku :exc:`TypeError`.


.. rubric:: Poznámky pod čarou

.. [#] Jiné jazyky mohou vracet změněný objekt, což umožňuje řetězení metod,
       například ``d->insert("a")->remove("b")->sort();``.
