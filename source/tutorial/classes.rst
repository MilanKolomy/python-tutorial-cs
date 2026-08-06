.. _tut-classes:

*******
Třídy
*******

Třídy umožňují sdružovat data a funkčnost. Vytvořením nové třídy vzniká nový
*typ* objektu, jehož nové *instance* lze následně vytvářet. Ke každé instanci
třídy mohou být připojeny atributy uchovávající její stav. Instance tříd mohou
mít také metody (definované jejich třídou), které tento stav mění.

Ve srovnání s jinými programovacími jazyky přidává mechanismus tříd v Pythonu
jen minimum nové syntaxe a sémantiky. Je směsí mechanismů tříd z jazyků C++ a
Modula-3. Třídy v Pythonu poskytují všechny standardní vlastnosti objektově
orientovaného programování: dědičnost umožňuje více základních tříd, odvozená
třída může překrýt libovolnou metodu svých základních tříd a metoda může volat
stejnojmennou metodu základní třídy. Objekty mohou obsahovat libovolné množství
dat libovolného druhu. Stejně jako moduly využívají třídy dynamickou povahu
Pythonu: vytvářejí se za běhu a po vytvoření je lze dále upravovat.

V terminologii C++ jsou členy třídy (včetně datových členů) běžně *veřejné*
(s výjimkou popsanou v části :ref:`tut-private`) a všechny členské funkce jsou
*virtuální*. Stejně jako v jazyce Modula-3 neexistuje zkrácený zápis pro odkazy
na členy objektu z jeho metod: funkce metody se deklaruje s explicitním prvním
argumentem představujícím objekt, který je při volání předán implicitně. Stejně
jako ve Smalltalku jsou samotné třídy objekty. To poskytuje sémantiku pro import
a přejmenování. Na rozdíl od C++ a Modula-3 lze vestavěné typy použít jako
základní třídy, které může uživatel rozšířit. Podobně jako v C++ lze také pro
instance tříd předefinovat většinu vestavěných operátorů se speciální syntaxí
(aritmetické operátory, indexování atd.).

(Protože pro popis tříd neexistuje všeobecně přijímaná terminologie, budu
občas používat pojmy ze Smalltalku a C++. Použil bych terminologii Modula-3,
protože jeho objektově orientovaná sémantika je Pythonu bližší než sémantika
C++, ale předpokládám, že o něm slyšelo jen málo čtenářů.)


.. _tut-object:

Několik slov o názvech a objektech
==================================

Objekty mají vlastní identitu a ke stejnému objektu může být navázáno více
názvů (v různých oborech platnosti). V jiných jazycích se to označuje jako
aliasing (vytváření aliasů). Při prvním seznámení s Pythonem se tato vlastnost
obvykle neprojeví a
u neměnných základních typů (čísel, řetězců, n-tic) ji lze bezpečně ignorovat.
U měnitelných objektů, jako jsou seznamy, slovníky a většina ostatních typů,
však může mít překvapivý vliv na sémantiku kódu. Zpravidla je to programu ku
prospěchu, protože aliasy se v některých ohledech chovají jako ukazatele.
Předání objektu je například levné, protože implementace předává pouze ukazatel;
pokud funkce změní objekt předaný jako argument, volající tuto změnu uvidí. Není
proto zapotřebí dvou různých mechanismů předávání argumentů jako v Pascalu.


.. _tut-scopes:

Obory platnosti a jmenné prostory v Pythonu
===========================================

Než představíme třídy, musíme si nejprve říci něco o pravidlech oborů platnosti
v Pythonu. Definice tříd používají několik zajímavých postupů s jmennými
prostory a k jejich úplnému pochopení potřebujete vědět, jak obory platnosti a
jmenné prostory fungují. Znalost tohoto tématu se ostatně hodí každému
pokročilému programátorovi v Pythonu.

Začněme několika definicemi.

*Jmenný prostor* je mapování názvů na objekty. Většina jmenných prostorů je v
současnosti implementována jako slovníky Pythonu, což obvykle není nijak patrné
(s výjimkou výkonu) a v budoucnu se to může změnit. Příkladem jsou množina
vestavěných názvů (obsahující funkce jako :func:`abs` a názvy vestavěných
výjimek), globální názvy v modulu a lokální názvy při volání funkce. V jistém
smyslu tvoří jmenný prostor také množina atributů objektu. Důležité je, že mezi
názvy v různých jmenných prostorech neexistuje žádný vztah. Dva různé moduly
mohou například bez nejasností definovat funkci ``maximize`` --- uživatelé
modulů před její název uvedou název modulu.

Slovo *atribut* zde mimochodem označuje každý název následující za tečkou ---
například ve výrazu ``z.real`` je ``real`` atributem objektu ``z``. Přesněji
řečeno jsou odkazy na názvy v modulech odkazy na atributy: ve výrazu
``modname.funcname`` je ``modname`` objekt modulu a ``funcname`` jeho atribut.
V tomto případě existuje přímé mapování mezi atributy modulu a globálními názvy
definovanými v modulu: sdílejí stejný jmenný prostor! [#]_

Atributy mohou být pouze pro čtení nebo zapisovatelné. Ve druhém případě je
možné do atributů přiřazovat. Atributy modulů jsou zapisovatelné: můžete napsat
``modname.the_answer = 42``. Zapisovatelné atributy lze také odstranit příkazem
:keyword:`del`. Například ``del modname.the_answer`` odstraní atribut
:attr:`!the_answer` z objektu označeného názvem ``modname``.

Jmenné prostory vznikají v různých okamžicích a mají různou životnost. Jmenný
prostor obsahující vestavěné názvy se vytvoří při spuštění interpretu Pythonu a
nikdy se neodstraní. Globální jmenný prostor modulu vznikne při načtení definice
modulu a obvykle také přetrvá až do ukončení interpretu. Příkazy prováděné na
nejvyšší úrovni interpretu, ať už načtené ze skriptu, nebo zadané interaktivně,
se považují za součást modulu :mod:`__main__`, takže mají vlastní globální
jmenný prostor. (Vestavěné názvy ve skutečnosti také sídlí v modulu, který se
nazývá :mod:`builtins`.)

Lokální jmenný prostor funkce se vytvoří při jejím volání a odstraní se, když
funkce vrátí výsledek nebo vyvolá výjimku, která v ní není obsloužena. (Přesněji
by bylo vhodnější říci, že se na něj zapomene.) Každé rekurzivní volání má
samozřejmě vlastní lokální jmenný prostor.

*Obor platnosti* je textová oblast programu v Pythonu, ve které je jmenný
prostor přímo přístupný. „Přímo přístupný“ zde znamená, že se nekvalifikovaný
odkaz na název pokusí tento název v jmenném prostoru vyhledat.

Přestože jsou obory platnosti určeny staticky, používají se dynamicky. V každém
okamžiku provádění existují tři nebo čtyři vnořené obory, jejichž jmenné
prostory jsou přímo přístupné:

* nejvnitřnější obor, který se prohledává jako první, obsahuje lokální názvy,
* obory všech obklopujících funkcí, prohledávané od nejbližšího, obsahují
  nelokální, ale zároveň neglobální názvy,
* předposlední obor obsahuje globální názvy aktuálního modulu,
* nejvzdálenější obor, prohledávaný jako poslední, je jmenný prostor obsahující
  vestavěné názvy.

Je-li název deklarován jako globální, všechny odkazy a přiřazení směřují přímo
do předposledního oboru obsahujícího globální názvy modulu. K přenavázání
proměnných nalezených mimo nejvnitřnější obor lze použít příkaz
:keyword:`nonlocal`. Bez této deklarace jsou takové proměnné pouze pro čtení
(pokus o zápis jednoduše vytvoří *novou* lokální proměnnou v nejvnitřnějším
oboru a stejně pojmenovanou vnější proměnnou ponechá beze změny).

Lokální obor obvykle odkazuje na lokální názvy (textově) aktuální funkce. Mimo
funkce odkazuje lokální obor na stejný jmenný prostor jako globální obor, tedy
na jmenný prostor modulu. Definice tříd vkládají do lokálního oboru ještě další
jmenný prostor.

Je důležité si uvědomit, že obory platnosti jsou určeny textově: globálním
oborem funkce definované v modulu je jmenný prostor tohoto modulu bez ohledu na
to, odkud nebo pod jakým aliasem je funkce volána. Vlastní vyhledávání názvů
naopak probíhá dynamicky za běhu. Definice jazyka se však vyvíjí směrem ke
statickému rozlišení názvů v době „kompilace“, proto se na dynamické rozlišování
nespoléhejte! (Lokální proměnné se již nyní určují staticky.)

Zvláštností Pythonu je, že pokud není účinný příkaz :keyword:`global` nebo
:keyword:`nonlocal`, přiřazení názvů vždy směřuje do nejvnitřnějšího oboru.
Přiřazení nekopíruje data --- pouze váže názvy k objektům. Totéž platí pro
odstranění: příkaz ``del x`` odstraní vazbu ``x`` z jmenného prostoru, na který
odkazuje lokální obor. Lokální obor ve skutečnosti používají všechny operace,
které zavádějí nové názvy: zejména příkazy :keyword:`import` a definice funkcí
v něm vážou název modulu či funkce.

Příkaz :keyword:`global` označuje, že určité proměnné existují v globálním oboru
a mají se v něm přenavázat. Příkaz :keyword:`nonlocal` označuje proměnné, které
existují v obklopujícím oboru a mají se přenavázat tam.

.. _tut-scopeexample:

Příklad oborů platnosti a jmenných prostorů
-------------------------------------------

Tento příklad ukazuje, jak odkazovat na různé obory platnosti a jmenné prostory
a jak :keyword:`global` a :keyword:`nonlocal` ovlivňují vazby proměnných::

   def scope_test():
       def do_local():
           spam = "local spam"

       def do_nonlocal():
           nonlocal spam
           spam = "nonlocal spam"

       def do_global():
           global spam
           spam = "global spam"

       spam = "test spam"
       do_local()
       print("After local assignment:", spam)
       do_nonlocal()
       print("After nonlocal assignment:", spam)
       do_global()
       print("After global assignment:", spam)

   scope_test()
   print("In global scope:", spam)

Výstup ukázkového kódu je:

.. code-block:: none

   After local assignment: test spam
   After nonlocal assignment: nonlocal spam
   After global assignment: nonlocal spam
   In global scope: global spam

Všimněte si, že *lokální* přiřazení (které je výchozí) nezměnilo vazbu *spam* ve
funkci *scope_test*. Přiřazení :keyword:`nonlocal` změnilo vazbu *spam* ve
*scope_test* a přiřazení :keyword:`global` změnilo vazbu na úrovni modulu.

Je také vidět, že před přiřazením :keyword:`global` žádná předchozí vazba pro
*spam* neexistovala.


.. _tut-firstclasses:

První pohled na třídy
=======================

Třídy zavádějí trochu nové syntaxe, tři nové typy objektů a novou sémantiku.


.. _tut-classdefinition:

Syntaxe definice třídy
-----------------------

Nejjednodušší tvar definice třídy vypadá takto::

   class ClassName:
       <statement-1>
       .
       .
       .
       <statement-N>

Definice tříd se stejně jako definice funkcí (příkazy :keyword:`def`) musejí
provést, než začnou mít účinek. (Definici třídy lze například umístit do větve
příkazu :keyword:`if` nebo dovnitř funkce.)

Příkazy uvnitř definice třídy budou v praxi obvykle definicemi funkcí, jsou však
povoleny a někdy i užitečné také jiné příkazy --- vrátíme se k tomu později.
Definice funkcí uvnitř třídy mají zpravidla zvláštní tvar seznamu argumentů,
který určují konvence volání metod; i to bude vysvětleno později.

Při vstupu do definice třídy se vytvoří nový jmenný prostor, který se použije
jako lokální obor. Všechna přiřazení lokálním proměnným proto směřují do tohoto
nového prostoru. Zejména zde definice funkcí vážou názvy nových funkcí.

Při běžném opuštění definice třídy (dosažením jejího konce) se vytvoří *objekt
třídy*. Jde v podstatě o obal obsahu jmenného prostoru vytvořeného definicí
třídy; více se o objektech tříd dozvíme v následující části. Obnoví se původní
lokální obor (účinný těsně před vstupem do definice) a objekt třídy se v něm
naváže na název uvedený v záhlaví definice (:class:`!ClassName` v příkladu).


.. _tut-classobjects:

Objekty tříd
-------------

Objekty tříd podporují dva druhy operací: odkazy na atributy a vytváření
instancí.

*Odkazy na atributy* používají standardní syntaxi všech odkazů na atributy v
Pythonu: ``obj.name``. Platnými názvy atributů jsou všechny názvy, které byly v
jmenném prostoru třídy při vytvoření jejího objektu. Pokud tedy definice třídy
vypadala takto::

   class MyClass:
       """A simple example class"""
       i = 12345

       def f(self):
           return 'hello world'

pak ``MyClass.i`` a ``MyClass.f`` jsou platné odkazy na atributy, které vracejí
celé číslo, respektive objekt funkce. Do atributů třídy lze také přiřazovat,
takže hodnotu ``MyClass.i`` lze změnit přiřazením. Platným atributem je rovněž
:attr:`~type.__doc__`, který vrací dokumentační řetězec třídy:
``"A simple example class"``.

*Vytvoření instance* třídy používá zápis funkce. Stačí si představit, že objekt
třídy je funkce bez parametrů vracející novou instanci třídy. Například (pro
výše uvedenou třídu)::

   x = MyClass()

vytvoří novou *instanci* třídy a přiřadí tento objekt lokální proměnné ``x``.

Operace vytvoření instance („volání“ objektu třídy) vytvoří prázdný objekt.
Mnoho tříd chce vytvářet instance přizpůsobené určitému počátečnímu stavu.
Třída proto může definovat speciální metodu :meth:`~object.__init__`, například::

   def __init__(self):
       self.data = []

Definuje-li třída metodu :meth:`~object.__init__`, vytvoření instance
automaticky zavolá :meth:`!__init__` pro nově vytvořenou instanci. V tomto
příkladu tedy novou inicializovanou instanci získáme pomocí::

   x = MyClass()

Metoda :meth:`~object.__init__` může samozřejmě pro větší flexibilitu přijímat
argumenty. Argumenty předané při vytváření instance se v takovém případě
předají metodě :meth:`!__init__`. Například::

   >>> class Complex:
   ...     def __init__(self, realpart, imagpart):
   ...         self.r = realpart
   ...         self.i = imagpart
   ...
   >>> x = Complex(3.0, -4.5)
   >>> x.r, x.i
   (3.0, -4.5)


.. _tut-instanceobjects:

Objekty instancí
----------------

Co lze s objekty instancí dělat? Jediné operace, kterým rozumějí, jsou odkazy na
atributy. Existují dva druhy platných názvů atributů: datové atributy a metody.

*Datové atributy* odpovídají „instančním proměnným“ ve Smalltalku a „datovým
členům“ v C++. Nemusejí se deklarovat; podobně jako lokální proměnné vzniknou
při prvním přiřazení. Je-li například ``x`` výše vytvořenou instancí
:class:`!MyClass`, následující kód vypíše hodnotu ``16`` a nezanechá po sobě
žádnou stopu::

   x.counter = 1
   while x.counter < 10:
       x.counter = x.counter * 2
   print(x.counter)
   del x.counter

Druhým typem odkazu na atribut instance je *metoda*. Metoda je funkce, která
„patří“ objektu.

.. index:: pair: object; method

Platné názvy metod objektu instance závisejí na jeho třídě. Každý atribut třídy,
který je objektem funkce, z definice určuje odpovídající metodu jejích instancí.
V našem příkladu je tedy ``x.f`` platným odkazem na metodu, protože ``MyClass.f``
je funkce, ale ``x.i`` nikoli, protože ``MyClass.i`` funkcí není. ``x.f`` však
není totéž co ``MyClass.f`` --- jde o *objekt metody*, nikoli objekt funkce.


.. _tut-methodobjects:

Objekty metod
--------------

Metoda se obvykle volá bezprostředně po svém navázání::

   x.f()

Je-li ``x = MyClass()`` jako výše, vrátí se řetězec ``'hello world'``. Metodu
však není nutné volat ihned: ``x.f`` je objekt metody, který lze uložit a
zavolat později. Například::

   xf = x.f
   while True:
       print(xf())

bude vypisovat ``hello world`` až do skonání věků.

Co přesně se stane při volání metody? Možná jste si všimli, že ``x.f()`` bylo
výše zavoláno bez argumentu, přestože definice funkce :meth:`!f` argument uvádí.
Kam se argument poděl? Python přece vyvolá výjimku, pokud je funkce vyžadující
argument zavolána bez něj --- i když jej ve skutečnosti nepoužívá...

Odpověď jste možná uhodli: zvláštností metod je, že se objekt instance předává
jako první argument funkce. V našem příkladu je volání ``x.f()`` přesně
ekvivalentní ``MyClass.f(x)``. Obecně je volání metody se seznamem *n* argumentů
ekvivalentní volání odpovídající funkce se seznamem argumentů, před který je
vložen objekt instance dané metody.

Metody obecně fungují následovně. Při odkazu na nedatový atribut instance se
prohledá její třída. Označuje-li název platný atribut třídy, který je objektem
funkce, odkazy na objekt instance a objekt funkce se společně zabalí do objektu
metody. Při zavolání objektu metody se z objektu instance a seznamu argumentů
vytvoří nový seznam argumentů a s ním se zavolá objekt funkce.


.. _tut-class-and-instance-variables:

Třídní a instanční proměnné
----------------------------

Obecně platí, že instanční proměnné slouží pro data jedinečná pro jednotlivé
instance, zatímco třídní proměnné slouží pro atributy a metody sdílené všemi
instancemi třídy::

    class Dog:

        kind = 'canine'         # class variable shared by all instances

        def __init__(self, name):
            self.name = name    # instance variable unique to each instance

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.kind                  # shared by all dogs
    'canine'
    >>> e.kind                  # shared by all dogs
    'canine'
    >>> d.name                  # unique to d
    'Fido'
    >>> e.name                  # unique to e
    'Buddy'

Jak bylo uvedeno v části :ref:`tut-object`, sdílená data mohou mít u
:term:`měnitelných <mutable>` objektů, jako jsou seznamy a slovníky, překvapivé
důsledky. Seznam *tricks* v následujícím kódu by například neměl být třídní
proměnnou, protože by všechny instance *Dog* sdílely jediný seznam::

    class Dog:

        tricks = []             # mistaken use of a class variable

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks                # unexpectedly shared by all dogs
    ['roll over', 'play dead']

Správný návrh třídy má místo toho použít instanční proměnnou::

    class Dog:

        def __init__(self, name):
            self.name = name
            self.tricks = []    # creates a new empty list for each dog

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks
    ['roll over']
    >>> e.tricks
    ['play dead']


.. _tut-remarks:

Různé poznámky
==============

.. These should perhaps be placed more carefully...

Pokud se stejný název atributu vyskytuje v instanci i ve třídě, má při
vyhledávání atributu přednost instance::

    >>> class Warehouse:
    ...    purpose = 'storage'
    ...    region = 'west'
    ...
    >>> w1 = Warehouse()
    >>> print(w1.purpose, w1.region)
    storage west
    >>> w2 = Warehouse()
    >>> w2.region = 'east'
    >>> print(w2.purpose, w2.region)
    storage east

Na datové atributy mohou odkazovat metody i běžní uživatelé („klienti“)
objektu. Třídy tedy nelze použít k implementaci čistě abstraktních datových
typů. Python ve skutečnosti neposkytuje nic, čím by bylo možné vynutit skrývání
dat --- vše je založeno na konvencích. (Implementace Pythonu napsaná v C však v
případě potřeby může zcela skrýt podrobnosti implementace a řídit přístup k
objektu; toho mohou využívat rozšíření Pythonu napsaná v C.)

Klienti by měli datové atributy používat opatrně --- jejich přepsáním mohou
porušit invarianty udržované metodami. Klienti mohou k objektu instance přidávat
vlastní datové atributy, aniž ovlivní správnost metod, pokud se vyhnou konfliktům
názvů. I zde může vhodná konvence pojmenování ušetřit mnoho potíží.

Pro odkazy na datové atributy (ani jiné metody) zevnitř metod neexistuje
zkrácený zápis. To ve skutečnosti zvyšuje čitelnost metod: při jejich procházení
nelze zaměnit lokální a instanční proměnné.

První argument metody se často nazývá ``self``. Jde pouze o konvenci: název
``self`` nemá pro Python žádný zvláštní význam. Nedodržení této konvence však
může snížit čitelnost kódu pro ostatní programátory a také je možné, že na ní
bude záviset nějaký program pro procházení tříd.

Každý objekt funkce, který je atributem třídy, definuje metodu jejích instancí.
Definice funkce nemusí být textově uzavřena v definici třídy: přípustné je také
přiřadit objekt funkce lokální proměnné ve třídě. Například::

   # Function defined outside the class
   def f1(self, x, y):
       return min(x, x+y)

   class C:
       f = f1

       def g(self):
           return 'hello world'

       h = g

``f``, ``g`` a ``h`` jsou nyní atributy třídy :class:`!C`, které odkazují na
objekty funkcí, a jsou proto metodami instancí :class:`!C`; ``h`` je přitom zcela
ekvivalentní ``g``. Tento postup obvykle pouze mate čtenáře programu.

Metody mohou volat jiné metody prostřednictvím atributů argumentu ``self``::

   class Bag:
       def __init__(self):
           self.data = []

       def add(self, x):
           self.data.append(x)

       def addtwice(self, x):
           self.add(x)
           self.add(x)

Metody mohou odkazovat na globální názvy stejně jako běžné funkce. Globálním
oborem spojeným s metodou je modul obsahující její definici. (Třída se jako
globální obor nikdy nepoužívá.) Dobrý důvod k použití globálních dat v metodě se
najde zřídka, globální obor má však mnoho oprávněných využití: metody mohou
například používat funkce a moduly importované do globálního oboru i funkce a
třídy v něm definované. V tomto globálním oboru je obvykle definována i třída
obsahující metodu a v následující části uvidíme, proč může metoda chtít odkazovat
na vlastní třídu.

Každá hodnota je objekt, a má proto *třídu* (označovanou také jako *typ*).
Ta je uložena jako ``object.__class__``.


.. _tut-inheritance:

Dědičnost
===========

Jazyková vlastnost by si samozřejmě nezasloužila název „třída“, kdyby
nepodporovala dědičnost. Syntaxe definice odvozené třídy vypadá takto::

   class DerivedClassName(BaseClassName):
       <statement-1>
       .
       .
       .
       <statement-N>

Název :class:`!BaseClassName` musí být definován ve jmenném prostoru přístupném
z oboru obsahujícího definici odvozené třídy. Místo názvu základní třídy jsou
povoleny také jiné libovolné výrazy. To se hodí například tehdy, když je
základní třída definována v jiném modulu::

   class DerivedClassName(modname.BaseClassName):

Definice odvozené třídy se provádí stejně jako definice základní třídy. Při
konstrukci objektu třídy se základní třída zapamatuje. Používá se při
rozlišování odkazů na atributy: pokud požadovaný atribut není nalezen ve třídě,
hledání pokračuje v základní třídě. Je-li základní třída sama odvozena od jiné
třídy, uplatní se toto pravidlo rekurzivně.

Na vytváření instancí odvozených tříd není nic zvláštního:
``DerivedClassName()`` vytvoří novou instanci třídy. Odkazy na metody se
rozlišují vyhledáním odpovídajícího atributu třídy a v případě potřeby postupem
po řetězci základních tříd. Odkaz na metodu je platný, pokud se tak nalezne
objekt funkce.

Odvozené třídy mohou překrývat metody svých základních tříd. Protože metody při
volání jiných metod stejného objektu nemají žádná zvláštní oprávnění, může
metoda základní třídy volající jinou metodu definovanou v téže třídě nakonec
zavolat metodu odvozené třídy, která ji překrývá. (Pro programátory v C++: všechny
metody v Pythonu jsou v podstatě ``virtual``.)

Překrývající metoda v odvozené třídě může chtít stejnojmennou metodu základní
třídy rozšířit, nikoli pouze nahradit. Základní metodu lze jednoduše zavolat
přímo pomocí ``BaseClassName.methodname(self, arguments)``. To může být občas
užitečné i pro klienty. (Funguje to pouze tehdy, je-li základní třída dostupná
pod názvem ``BaseClassName`` v globálním oboru.)

Python nabízí dvě vestavěné funkce pracující s dědičností:

* Funkce :func:`isinstance` ověřuje typ instance: ``isinstance(obj, int)`` bude
  ``True`` pouze tehdy, je-li ``obj.__class__`` třída :class:`int` nebo třída od
  ní odvozená.

* Funkce :func:`issubclass` ověřuje dědičnost tříd: ``issubclass(bool, int)`` je
  ``True``, protože :class:`bool` je podtřídou :class:`int`. Naproti tomu
  ``issubclass(float, int)`` je ``False``, protože :class:`float` podtřídou
  :class:`int` není.



.. _tut-multiple:

Vícenásobná dědičnost
---------------------

Python podporuje také vícenásobnou dědičnost. Definice třídy s více základními
třídami vypadá takto::

   class DerivedClassName(Base1, Base2, Base3):
       <statement-1>
       .
       .
       .
       <statement-N>

Ve většině jednoduchých případů si lze hledání atributů zděděných z rodičovské
třídy představit jako průchod do hloubky zleva doprava, který při překryvu v
hierarchii neprohledává tutéž třídu dvakrát. Pokud tedy atribut není nalezen v
:class:`!DerivedClassName`, hledá se v :class:`!Base1`, poté rekurzivně v jejích
základních třídách, a není-li nalezen ani tam, v :class:`!Base2` a tak dále.

Ve skutečnosti je situace o něco složitější: pořadí rozlišování metod se
dynamicky mění, aby podporovalo kooperativní volání :func:`super`. V některých
jiných jazycích s vícenásobnou dědičností se tento přístup nazývá
call-next-method a je výkonnější než volání super v jazycích s jednoduchou
dědičností.

Dynamické pořadí je nutné, protože každá vícenásobná dědičnost obsahuje jeden
nebo více diamantových vztahů, v nichž je alespoň jedna rodičovská třída
dosažitelná z nejnižší třídy více cestami. Všechny třídy například dědí z
:class:`object`, takže při vícenásobné dědičnosti k ní vždy vede více než jedna
cesta. Dynamický algoritmus proto linearizuje pořadí hledání tak, aby zachoval
pořadí zleva doprava určené v každé třídě, navštívil každého rodiče jen jednou a
byl monotónní (odvození podtřídy nezmění pořadí přednosti jejích rodičů). Tyto
vlastnosti společně umožňují navrhovat spolehlivé a rozšiřitelné třídy s
vícenásobnou dědičností. Podrobnosti viz :ref:`python_2.3_mro`.


.. _tut-private:

Privátní proměnné
=================

„Privátní“ instanční proměnné přístupné pouze zevnitř objektu v Pythonu
neexistují. Většina kódu však dodržuje konvenci, podle níž má být název s
počátečním podtržítkem (např. ``_spam``) považován za neveřejnou část API, ať už
jde o funkci, metodu nebo datový člen. Jde o detail implementace, který se může
bez upozornění změnit.

.. index::
   pair: name; mangling

Protože členy privátní pro třídu mají oprávněné využití (brání konfliktům s
názvy definovanými podtřídami), existuje omezená podpora mechanismu nazývaného
:dfn:`komolení názvů <name mangling>`. Každý identifikátor ve tvaru ``__spam``
(nejméně dvě úvodní a nejvýše jedno koncové podtržítko) se textově nahradí
``_classname__spam``, kde ``classname`` je název aktuální třídy bez úvodních
podtržítek. Komolení proběhne bez ohledu na syntaktickou pozici identifikátoru,
pokud se nachází v definici třídy.

.. seealso::

   Podrobnosti a zvláštní případy obsahuje :ref:`specifikace komolení privátních
   názvů <private-name-mangling>`.

Komolení názvů umožňuje podtřídám překrývat metody bez narušení volání metod
uvnitř třídy. Například::

   class Mapping:
       def __init__(self, iterable):
           self.items_list = []
           self.__update(iterable)

       def update(self, iterable):
           for item in iterable:
               self.items_list.append(item)

       __update = update   # private copy of original update() method

   class MappingSubclass(Mapping):

       def update(self, keys, values):
           # provides new signature for update()
           # but does not break __init__()
           for item in zip(keys, values):
               self.items_list.append(item)

Příklad by fungoval, i kdyby ``MappingSubclass`` zavedla identifikátor
``__update``, protože ve třídě ``Mapping`` se nahradí ``_Mapping__update`` a ve
třídě ``MappingSubclass`` názvem ``_MappingSubclass__update``.

Pravidla komolení jsou určena především k zabránění nehodám; k proměnné
považované za privátní lze stále přistupovat a měnit ji. Ve zvláštních
okolnostech, například v ladicím programu, to může být dokonce užitečné.

Kód předaný funkcím ``exec()`` nebo ``eval()`` nepovažuje název volající třídy
za aktuální třídu. Podobá se to účinku příkazu ``global``, který je rovněž
omezen na společně zkompilovaný bajtkód. Stejné omezení platí pro ``getattr()``,
``setattr()`` a ``delattr()`` i pro přímé odkazy na ``__dict__``.


.. _tut-odds:

Další poznámky
===============

Někdy je užitečné mít datový typ podobný „záznamu“ v Pascalu nebo „struktuře“ v
C, který sdružuje několik pojmenovaných datových položek. Idiomatickým řešením
je použít modul :mod:`dataclasses`::

    from dataclasses import dataclass

    @dataclass
    class Employee:
        name: str
        dept: str
        salary: int

::

    >>> john = Employee('john', 'computer lab', 1000)
    >>> john.dept
    'computer lab'
    >>> john.salary
    1000

Kódu v Pythonu, který očekává určitý abstraktní datový typ, lze často předat
třídu napodobující metody tohoto typu. Máte-li například funkci formátující data
ze souborového objektu, můžete definovat třídu s metodami
:meth:`~io.TextIOBase.read` a :meth:`~io.TextIOBase.readline`, které data místo
toho získávají z vyrovnávací paměti řetězce, a předat ji jako argument.

.. (Unfortunately, this technique has its limitations: a class can't define
   operations that are accessed by special syntax such as sequence subscripting
   or arithmetic operators, and assigning such a "pseudo-file" to sys.stdin will
   not cause the interpreter to read further input from it.)

Také :ref:`objekty instančních metod <instance-methods>` mají atributy:
:attr:`m.__self__ <method.__self__>` je objekt instance s metodou :meth:`!m` a
:attr:`m.__func__ <method.__func__>` je :ref:`objekt funkce
<user-defined-funcs>` odpovídající této metodě.


.. _tut-iterators:

Iterátory
=========

Pravděpodobně jste si již všimli, že většinu kontejnerových objektů lze
procházet pomocí příkazu :keyword:`for`::

   for element in [1, 2, 3]:
       print(element)
   for element in (1, 2, 3):
       print(element)
   for key in {'one':1, 'two':2}:
       print(key)
   for char in "123":
       print(char)
   for line in open("myfile.txt"):
       print(line, end='')

Tento způsob přístupu je jasný, stručný a pohodlný. Iterátory prostupují
Pythonem a sjednocují jej. Příkaz :keyword:`for` na pozadí zavolá pro
kontejnerový objekt funkci :func:`iter`. Ta vrátí objekt iterátoru definující
metodu :meth:`~iterator.__next__`, která postupně přistupuje k jednotlivým
prvkům kontejneru. Jakmile žádné další prvky nezbývají, metoda
:meth:`~iterator.__next__` vyvolá výjimku :exc:`StopIteration`, která cyklu
:keyword:`!for` oznámí, že má skončit. Metodu :meth:`~iterator.__next__` lze
volat vestavěnou funkcí :func:`next`; následující příklad ukazuje celý postup::

   >>> s = 'abc'
   >>> it = iter(s)
   >>> it
   <str_iterator object at 0x10c90e650>
   >>> next(it)
   'a'
   >>> next(it)
   'b'
   >>> next(it)
   'c'
   >>> next(it)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       next(it)
   StopIteration

Když znáte mechanismus protokolu iterátoru, můžete snadno přidat chování
iterátoru vlastním třídám. Definujte metodu :meth:`~container.__iter__`, která
vrací objekt s metodou :meth:`~iterator.__next__`. Definuje-li třída
:meth:`!__next__`, může :meth:`!__iter__` jednoduše vracet ``self``::

   class Reverse:
       """Iterator for looping over a sequence backwards."""
       def __init__(self, data):
           self.data = data
           self.index = len(data)

       def __iter__(self):
           return self

       def __next__(self):
           if self.index == 0:
               raise StopIteration
           self.index = self.index - 1
           return self.data[self.index]

::

   >>> rev = Reverse('spam')
   >>> iter(rev)
   <__main__.Reverse object at 0x00A1DB50>
   >>> for char in rev:
   ...     print(char)
   ...
   m
   a
   p
   s


.. _tut-generators:

Generátory
==========

:term:`Generátory <generator>` jsou jednoduchým a účinným nástrojem pro
vytváření iterátorů. Zapisují se jako běžné funkce, ale při vracení dat používají
příkaz :keyword:`yield`. Při každém volání :func:`next` pokračuje generátor tam,
kde skončil (pamatuje si všechny hodnoty dat i naposledy provedený příkaz).
Příklad ukazuje, jak snadné může být generátor vytvořit::

   def reverse(data):
       for index in range(len(data)-1, -1, -1):
           yield data[index]

::

   >>> for char in reverse('golf'):
   ...     print(char)
   ...
   f
   l
   o
   g

Vše, co lze provést generátory, lze provést také iterátory založenými na třídách
popsanými v předchozí části. Generátory jsou tak stručné proto, že se metody
:meth:`~iterator.__iter__` a :meth:`~generator.__next__` vytvářejí automaticky.

Další klíčovou vlastností je automatické uchovávání lokálních proměnných a stavu
provádění mezi voláními. Funkce se díky tomu píše snadněji a je mnohem
čitelnější než řešení s instančními proměnnými jako ``self.index`` a
``self.data``.

Kromě automatického vytváření metod a uchovávání stavu programu generátory při
ukončení automaticky vyvolají :exc:`StopIteration`. Tyto vlastnosti společně
umožňují vytvářet iterátory stejně snadno jako běžné funkce.


.. _tut-genexps:

Generátorové výrazy
=====================

Některé jednoduché generátory lze stručně zapsat jako výrazy se syntaxí
podobnou generátorové notaci seznamu, ale s kulatými namísto hranatých závorek.
Tyto výrazy jsou určeny pro situace, kdy generátor okamžitě použije obklopující
funkce. Generátorové výrazy jsou stručnější, ale méně všestranné než úplné
definice generátorů a bývají paměťově úspornější než odpovídající generátorové
notace seznamů.

Příklady::

   >>> sum(i*i for i in range(10))                 # sum of squares
   285

   >>> xvec = [10, 20, 30]
   >>> yvec = [7, 5, 3]
   >>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
   260

   >>> unique_words = set(word for line in page  for word in line.split())

   >>> valedictorian = max((student.gpa, student.name) for student in graduates)

   >>> data = 'golf'
   >>> list(data[i] for i in range(len(data)-1, -1, -1))
   ['f', 'l', 'o', 'g']



.. rubric:: Poznámky pod čarou

.. [#] S jedinou výjimkou. Objekty modulů mají skrytý atribut pouze pro čtení
   :attr:`~object.__dict__`, který vrací slovník použitý k implementaci jmenného
   prostoru modulu. Název ``__dict__`` je atribut, ale nikoli globální název.
   Jeho použití zjevně porušuje abstrakci implementace jmenného prostoru, a mělo
   by proto být omezeno například na ladění programu po jeho pádu.
