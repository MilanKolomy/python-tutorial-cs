.. _tut-informal:

**********************************
Neformální úvod do Pythonu
**********************************

V následujících příkladech se vstup a výstup rozlišují přítomností či
nepřítomností výzev (:term:`>>>` a :term:`...`): chcete-li příklad zopakovat,
musíte napsat vše, co následuje za zobrazenou výzvou; řádky, které výzvou
nezačínají, jsou výstupem interpretu. Sekundární výzva na samostatném řádku
v příkladu znamená, že musíte zadat prázdný řádek; tím se ukončuje víceřádkový
příkaz.

.. only:: html

   Ke zkopírování a vložení vstupních řádků do interpretu můžete použít tlačítko
   „Copy“ (zobrazí se v pravém horním rohu při najetí ukazatelem nebo klepnutí
   na ukázku kódu), které odstraní výzvy a vynechá výstup.

.. index:: single: # (hash); comment

Mnohé příklady v této příručce, včetně těch zadávaných na interaktivní výzvě,
obsahují komentáře. Komentář v Pythonu začíná znakem mřížky ``#`` a pokračuje
do konce fyzického řádku. Může se nacházet na začátku řádku nebo za prázdnými
znaky či kódem, nikoli však uvnitř řetězcového literálu. Znak mřížky uvnitř
řetězcového literálu je prostě znakem mřížky. Protože komentáře slouží
k objasnění kódu a Python je neinterpretuje, můžete je při zadávání příkladů
vynechat.

Několik příkladů::

   # this is the first comment
   spam = 1  # and this is the second comment
             # ... and now a third!
   text = "# This is not a comment because it's inside quotes."


.. _tut-calculator:

Použití Pythonu jako kalkulačky
===============================

Vyzkoušejme několik jednoduchých příkazů Pythonu. Spusťte interpret a počkejte
na primární výzvu ``>>>``. (Nemělo by to trvat dlouho.)


.. _tut-numbers:

Čísla
-------

Interpret funguje jako jednoduchá kalkulačka: můžete do něj zadat výraz a on
vypíše jeho hodnotu. Syntaxe výrazů je přímočará: operátory ``+``, ``-``, ``*``
a ``/`` lze použít k aritmetickým operacím a závorky (``()``) k seskupování.
Například::

   >>> 2 + 2
   4
   >>> 50 - 5*6
   20
   >>> (50 - 5*6) / 4
   5.0
   >>> 8 / 5  # division always returns a floating-point number
   1.6

Celá čísla (například ``2``, ``4`` a ``20``) jsou typu :class:`int`, zatímco
čísla s desetinnou částí (například ``5.0`` a ``1.6``) jsou typu
:class:`float`. O číselných typech se více dozvíme později v tutorialu.

Dělení (``/``) vždy vrací číslo s plovoucí desetinnou čárkou. Pro
:term:`celočíselné dělení <floor division>` s celočíselným výsledkem můžete
použít operátor ``//``; zbytek po dělení vypočítáte pomocí ``%``::

   >>> 17 / 3  # classic division returns a float
   5.666666666666667
   >>>
   >>> 17 // 3  # floor division discards the fractional part
   5
   >>> 17 % 3  # the % operator returns the remainder of the division
   2
   >>> 5 * 3 + 2  # floored quotient * divisor + remainder
   17

V Pythonu lze k výpočtu mocnin použít operátor ``**`` [#]_::

   >>> 5 ** 2  # 5 squared
   25
   >>> 2 ** 7  # 2 to the power of 7
   128

Rovnítko (``=``) slouží k přiřazení hodnoty proměnné. Po přiřazení se před
další interaktivní výzvou nezobrazí žádný výsledek::

   >>> width = 20
   >>> height = 5 * 9
   >>> width * height
   900

Není-li proměnná „definovaná“ (nemá přiřazenou hodnotu), pokus o její použití
vyvolá chybu::

   >>> n  # try to access an undefined variable
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'n' is not defined

Operace s plovoucí desetinnou čárkou jsou plně podporované; operátory
s operandy smíšených typů převedou celočíselný operand na číslo s plovoucí
desetinnou čárkou::

   >>> 4 * 3.75 - 1
   14.0

V interaktivním režimu se naposledy vypsaný výraz přiřadí proměnné ``_``.
Při používání Pythonu jako stolní kalkulačky tak lze ve výpočtech o něco snáze
pokračovat, například::

   >>> tax = 12.5 / 100
   >>> price = 100.50
   >>> price * tax
   12.5625
   >>> price + _
   113.0625
   >>> round(_, 2)
   113.06

Uživatel by měl tuto proměnnou považovat za určenou pouze pro čtení.
Nepřiřazujte jí hodnotu explicitně --- vytvořili byste nezávislou lokální
proměnnou stejného jména, která by zastínila vestavěnou proměnnou s jejím
zvláštním chováním.

Kromě typů :class:`int` a :class:`float` podporuje Python také další číselné
typy, například :class:`~decimal.Decimal` a :class:`~fractions.Fraction`.
Python má rovněž vestavěnou podporu :ref:`komplexních čísel <typesnumeric>`
a jejich imaginární část označuje příponou ``j`` nebo ``J`` (například
``3+5j``).


.. _tut-strings:

Text
----

Python dokáže kromě čísel pracovat také s textem (reprezentovaným typem
:class:`str`, takzvanými „řetězci“). Patří sem znaky „``!``“, slova
„``rabbit``“, názvy „``Paris``“, věty „``Got your back.``“ a podobně.
„``Yay! :)``“. Lze je uzavřít do jednoduchých (``'...'``) nebo dvojitých
uvozovek (``"..."``) se stejným výsledkem [#]_.

.. code-block:: pycon

   >>> 'spam eggs'  # single quotes
   'spam eggs'
   >>> "Paris rabbit got your back :)! Yay!"  # double quotes
   'Paris rabbit got your back :)! Yay!'
   >>> '1975'  # digits and numerals enclosed in quotes are also strings
   '1975'

Chceme-li uvozovku uvést jako součást řetězce, musíme ji „escapovat“ přidáním
``\`` před ni. Případně můžeme použít druhý typ uvozovek::

   >>> 'doesn\'t'  # use \' to escape the single quote...
   "doesn't"
   >>> "doesn't"  # ...or use double quotes instead
   "doesn't"
   >>> '"Yes," they said.'
   '"Yes," they said.'
   >>> "\"Yes,\" they said."
   '"Yes," they said.'
   >>> '"Isn\'t," they said.'
   '"Isn\'t," they said.'

V shellu Pythonu může definice řetězce vypadat jinak než jeho výstupní podoba.
Funkce :func:`print` vytváří čitelnější výstup: vynechá vnější uvozovky
a interpretuje escapované a speciální znaky::

   >>> s = 'First line.\nSecond line.'  # \n means newline
   >>> s  # without print(), special characters are included in the string
   'First line.\nSecond line.'
   >>> print(s)  # with print(), special characters are interpreted, so \n produces new line
   First line.
   Second line.

Nechcete-li, aby se znaky uvedené znakem ``\`` interpretovaly jako speciální,
můžete použít *surové řetězce* (raw strings) přidáním ``r`` před první
uvozovku::

   >>> print('C:\this\name')  # here \t means tab, \n means newline
   C:      his
   ame
   >>> print(r'C:\this\name')  # note the r before the quote
   C:\this\name

Surové řetězce mají jednu záludnost: nesmějí končit lichým počtem znaků ``\``.
Další informace a možnosti řešení najdete v :ref:`příslušné položce FAQ
<faq-programming-raw-string-backslash>`.

Řetězcové literály mohou zabírat více řádků. Jednou z možností jsou trojité
uvozovky: ``"""..."""`` nebo ``'''...'''``. Znaky konce řádku se do řetězce
zahrnou automaticky, tomu však lze zabránit přidáním ``\`` na konec řádku.
V následujícím příkladu není úvodní znak nového řádku zahrnut::

   >>> print("""\
   ... Usage: thingy [OPTIONS]
   ...      -h                        Display this usage message
   ...      -H hostname               Hostname to connect to
   ... """)
   Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to

   >>>

Řetězce lze zřetězit (spojit) operátorem ``+`` a opakovat operátorem ``*``::

   >>> # 3 times 'un', followed by 'ium'
   >>> 3 * 'un' + 'ium'
   'unununium'

Dva nebo více *řetězcových literálů* (tedy řetězců uzavřených v uvozovkách)
uvedených vedle sebe se automaticky zřetězí. ::

   >>> 'Py' 'thon'
   'Python'

Tato vlastnost je užitečná zejména při rozdělování dlouhých řetězců::

   >>> text = ('Put several strings within parentheses '
   ...         'to have them joined together.')
   >>> text
   'Put several strings within parentheses to have them joined together.'

Funguje to však pouze pro literály, nikoli pro proměnné nebo výrazy::

   >>> prefix = 'Py'
   >>> prefix 'thon'  # can't concatenate a variable and a string literal
     File "<stdin>", line 1
       prefix 'thon'
              ^^^^^^
   SyntaxError: invalid syntax
   >>> ('un' * 3) 'ium'
     File "<stdin>", line 1
       ('un' * 3) 'ium'
                  ^^^^^
   SyntaxError: invalid syntax

Chcete-li zřetězit proměnné nebo proměnnou a literál, použijte ``+``::

   >>> prefix + 'thon'
   'Python'

Řetězce lze *indexovat* (přistupovat k nim pomocí indexu), přičemž první znak
má index 0. Samostatný znakový typ neexistuje; znak je jednoduše řetězec délky
jedna::

   >>> word = 'Python'
   >>> word[0]  # character in position 0
   'P'
   >>> word[5]  # character in position 5
   'n'

Indexy mohou být také záporná čísla; v takovém případě se počítá zprava::

   >>> word[-1]  # last character
   'n'
   >>> word[-2]  # second-last character
   'o'
   >>> word[-6]
   'P'

Protože -0 je totéž co 0, záporné indexy začínají hodnotou -1.

Kromě indexování jsou podporovány také *výřezy* (slicing). Indexování slouží
k získání jednotlivých znaků, zatímco výřez umožňuje získat podřetězec::

   >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
   'Py'
   >>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
   'tho'

Indexy výřezu mají užitečné výchozí hodnoty: vynechaný první index má hodnotu
nula a vynechaný druhý index má hodnotu délky řetězce, z něhož se výřez vytváří. ::

   >>> word[:2]   # character from the beginning to position 2 (excluded)
   'Py'
   >>> word[4:]   # characters from position 4 (included) to the end
   'on'
   >>> word[-2:]  # characters from the second-last (included) to the end
   'on'

Všimněte si, že začátek je vždy zahrnut, zatímco konec nikoli. Díky tomu se
``s[:i] + s[i:]`` vždy rovná ``s``::

   >>> word[:2] + word[2:]
   'Python'
   >>> word[:4] + word[4:]
   'Python'

Fungování výřezů si lze zapamatovat tak, že indexy ukazují *mezi* znaky a levý
okraj prvního znaku má číslo 0. Pravý okraj posledního znaku řetězce o *n*
znacích má potom index *n*, například::

    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1

První řada čísel udává pozici indexů 0...6 v řetězci, druhá řada odpovídající
záporné indexy. Výřez od *i* do *j* tvoří všechny znaky mezi okraji označenými
*i* a *j*.

Pokud jsou oba nezáporné indexy v platném rozsahu, délka výřezu se rovná jejich
rozdílu. Například délka ``word[1:3]`` je 2.

Pokus o použití příliš velkého indexu skončí chybou::

   >>> word[42]  # the word only has 6 characters
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: string index out of range

Indexy mimo rozsah se však při vytváření výřezů zpracují bez chyby::

   >>> word[4:42]
   'on'
   >>> word[42:]
   ''

Řetězce Pythonu nelze měnit --- jsou :term:`neměnné <immutable>`.
Přiřazení na indexovanou pozici v řetězci proto skončí chybou::

   >>> word[0] = 'J'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   >>> word[2:] = 'py'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment

Potřebujete-li jiný řetězec, vytvořte nový::

   >>> 'J' + word[1:]
   'Jython'
   >>> word[:2] + 'py'
   'Pypy'

Vestavěná funkce :func:`len` vrací délku řetězce::

   >>> s = 'supercalifragilisticexpialidocious'
   >>> len(s)
   34


.. seealso::

   :ref:`textseq`
      Řetězce jsou příkladem *sekvenčních typů* a podporují operace společné
      těmto typům.

   :ref:`string-methods`
      Řetězce podporují mnoho metod pro základní transformace a vyhledávání.

   :ref:`f-strings`
      Řetězcové literály s vloženými výrazy.

   :ref:`formatstrings`
      Informace o formátování řetězců pomocí :meth:`str.format`.

   :ref:`old-string-formatting`
      Podrobnější popis starých formátovacích operací, které se vyvolají, když
      je řetězec levým operandem operátoru ``%``.


.. _tut-lists:

Seznamy
-------

Python zná několik *složených* datových typů, které slouží k seskupování jiných
hodnot. Nejuniverzálnějším z nich je *seznam*, zapisovaný jako hodnoty (prvky)
oddělené čárkami a uzavřené v hranatých závorkách. Seznamy mohou obsahovat prvky
různých typů, obvykle však mají všechny prvky stejný typ. ::

   >>> squares = [1, 4, 9, 16, 25]
   >>> squares
   [1, 4, 9, 16, 25]

Stejně jako řetězce (a všechny ostatní vestavěné :term:`sekvenční <sequence>`
typy) lze seznamy indexovat a vytvářet z nich výřezy::

   >>> squares[0]  # indexing returns the item
   1
   >>> squares[-1]
   25
   >>> squares[-3:]  # slicing returns a new list
   [9, 16, 25]

Seznamy podporují také operace, jako je zřetězení::

   >>> squares + [36, 49, 64, 81, 100]
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Na rozdíl od řetězců, které jsou :term:`neměnné <immutable>`, jsou seznamy
:term:`měnitelným <mutable>` typem, takže jejich obsah lze změnit::

    >>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
    >>> 4 ** 3  # the cube of 4 is 64, not 65!
    64
    >>> cubes[3] = 64  # replace the wrong value
    >>> cubes
    [1, 8, 27, 64, 125]

Nové prvky můžete na konec seznamu přidávat také pomocí *metody*
:meth:`list.append` (o metodách se více dozvíme později)::

   >>> cubes.append(216)  # add the cube of 6
   >>> cubes.append(7 ** 3)  # and the cube of 7
   >>> cubes
   [1, 8, 27, 64, 125, 216, 343]

Prosté přiřazení v Pythonu data nikdy nekopíruje. Přiřadíte-li seznam proměnné,
proměnná odkazuje na *existující seznam*. Jakékoli změny provedené v seznamu
prostřednictvím jedné proměnné budou viditelné přes všechny ostatní proměnné,
které na něj odkazují.::

   >>> rgb = ["Red", "Green", "Blue"]
   >>> rgba = rgb
   >>> id(rgb) == id(rgba)  # they reference the same object
   True
   >>> rgba.append("Alph")
   >>> rgb
   ["Red", "Green", "Blue", "Alph"]

Všechny operace s výřezy vracejí nový seznam obsahující požadované prvky.
Následující výřez tedy vrátí :ref:`mělkou kopii <shallow_vs_deep_copy>`
seznamu::

   >>> correct_rgba = rgba[:]
   >>> correct_rgba[-1] = "Alpha"
   >>> correct_rgba
   ["Red", "Green", "Blue", "Alpha"]
   >>> rgba
   ["Red", "Green", "Blue", "Alph"]

Do výřezů lze rovněž přiřazovat, čímž lze dokonce změnit velikost seznamu nebo
jej zcela vyprázdnit::

   >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> letters
   ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> # replace some values
   >>> letters[2:5] = ['C', 'D', 'E']
   >>> letters
   ['a', 'b', 'C', 'D', 'E', 'f', 'g']
   >>> # now remove them
   >>> letters[2:5] = []
   >>> letters
   ['a', 'b', 'f', 'g']
   >>> # clear the list by replacing all the elements with an empty list
   >>> letters[:] = []
   >>> letters
   []

Vestavěnou funkci :func:`len` lze použít také na seznamy::

   >>> letters = ['a', 'b', 'c', 'd']
   >>> len(letters)
   4

Seznamy lze vnořovat (vytvářet seznamy obsahující jiné seznamy), například::

   >>> a = ['a', 'b', 'c']
   >>> n = [1, 2, 3]
   >>> x = [a, n]
   >>> x
   [['a', 'b', 'c'], [1, 2, 3]]
   >>> x[0]
   ['a', 'b', 'c']
   >>> x[0][1]
   'b'

.. _tut-firststeps:

První kroky k programování
===============================

Python samozřejmě můžeme použít ke složitějším úlohám, než je sčítání dvou
a dvou. Počáteční část `Fibonacciho posloupnosti
<https://en.wikipedia.org/wiki/Fibonacci_sequence>`_ můžeme například zapsat
takto::

   >>> # Fibonacci series:
   >>> # the sum of two elements defines the next
   >>> a, b = 0, 1
   >>> while a < 10:
   ...     print(a)
   ...     a, b = b, a+b
   ...
   0
   1
   1
   2
   3
   5
   8

Tento příklad představuje několik nových vlastností.

* První řádek obsahuje *vícenásobné přiřazení*: proměnné ``a`` a ``b`` současně
  získají nové hodnoty 0 a 1. Na posledním řádku se tento postup použije znovu
  a ukazuje, že před provedením kteréhokoli přiřazení se nejprve vyhodnotí
  všechny výrazy na pravé straně. Výrazy na pravé straně se vyhodnocují zleva
  doprava.

* Cyklus :keyword:`while` se provádí, dokud je podmínka (zde ``a < 10``)
  pravdivá. Stejně jako v C je v Pythonu každá nenulová celočíselná hodnota
  pravdivá a nula nepravdivá. Podmínkou může být také řetězec, seznam, či
  dokonce libovolná sekvence; vše s nenulovou délkou je pravdivé, prázdné
  sekvence jsou nepravdivé. Test použitý v příkladu je jednoduché porovnání.
  Standardní porovnávací operátory se zapisují stejně jako v C: ``<`` (menší
  než), ``>`` (větší než), ``==`` (rovná se), ``<=`` (menší nebo rovno),
  ``>=`` (větší nebo rovno) a ``!=`` (nerovná se).

* *Tělo* cyklu je *odsazené*: odsazení je v Pythonu způsobem seskupování
  příkazů. Na interaktivní výzvě musíte u každého odsazeného řádku zadat
  tabulátor nebo jednu či více mezer. Složitější vstupy pro Python budete
  v praxi připravovat v textovém editoru; všechny kvalitní textové editory
  nabízejí automatické odsazování. Po interaktivním zadání složeného příkazu
  musí následovat prázdný řádek označující jeho dokončení (syntaktický analyzátor
  nedokáže odhadnout, kdy jste zadali poslední řádek). Každý řádek v základním
  bloku musí být odsazen o stejnou úroveň.

* Funkce :func:`print` vypíše hodnoty předaných argumentů. Od prostého zadání
  výrazu, jehož hodnotu chcete vypsat (jako v předchozích příkladech
  s kalkulačkou), se liší způsobem zpracování více argumentů, hodnot s plovoucí
  desetinnou čárkou a řetězců. Řetězce se vypisují bez uvozovek a mezi prvky se
  vkládá mezera, takže lze výstup pěkně formátovat, například::

     >>> i = 256*256
     >>> print('The value of i is', i)
     The value of i is 65536

  Pomocí argumentu klíčového slova *end* lze zabránit vložení nového řádku za
  výstup nebo výstup ukončit jiným řetězcem::

     >>> a, b = 0, 1
     >>> while a < 1000:
     ...     print(a, end=',')
     ...     a, b = b, a+b
     ...
     0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,


.. rubric:: Poznámky pod čarou

.. [#] Protože ``**`` má vyšší prioritu než ``-``, výraz ``-3**2`` se
   interpretuje jako ``-(3**2)`` a jeho výsledkem je ``-9``. Chcete-li získat
   ``9``, použijte ``(-3)**2``.

.. [#] Na rozdíl od některých jiných jazyků mají speciální znaky, jako je
   ``\n``, stejný význam v jednoduchých (``'...'``) i dvojitých (``"..."``)
   uvozovkách. Jediný rozdíl spočívá v tom, že uvnitř jednoduchých uvozovek
   není nutné escapovat ``"`` (ale je nutné escapovat ``\'``) a naopak.
