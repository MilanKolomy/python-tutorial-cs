.. testsetup::

    import math
    from fractions import Fraction

.. _tut-fp-issues:

********************************************************
Aritmetika s plovoucí řádovou čárkou: problémy a omezení
********************************************************

.. sectionauthor:: Tim Peters <tim_one@users.sourceforge.net>
.. sectionauthor:: Raymond Hettinger <python at rcn dot com>


Čísla s plovoucí řádovou čárkou jsou v počítačovém hardwaru reprezentována jako
zlomky o základu 2 (binární). Například **desetinný** zlomek ``0.625`` má
hodnotu 6/10 + 2/100 + 5/1000 a obdobně **binární** zlomek ``0.101`` má hodnotu
1/2 + 0/4 + 1/8. Oba zlomky mají stejnou hodnotu; jediným skutečným rozdílem je,
že první je zapsán zlomkovou notací o základu 10 a druhý o základu 2.

Většinu desetinných zlomků bohužel nelze přesně reprezentovat jako binární
zlomky. Zadaná desetinná čísla s plovoucí řádovou čárkou jsou proto obecně jen
přibližně nahrazena binárními čísly, která počítač skutečně ukládá.

Problém je zpočátku snazší pochopit v soustavě o základu 10. Uvažujme zlomek
1/3. Jako desetinný zlomek jej lze přibližně vyjádřit::

   0.3

nebo lépe::

   0.33

nebo ještě lépe::

   0.333

a tak dále. Bez ohledu na počet zapsaných číslic nebude výsledek nikdy přesně
1/3, ale bude jej stále lépe aproximovat.

Stejně tak nelze desetinnou hodnotu 0.1 přesně vyjádřit jako binární zlomek bez
ohledu na počet použitých binárních číslic. V soustavě o základu 2 je 1/10
nekonečně se opakující zlomek::

   0.0001100110011001100110011001100110011001100110011...

Při zastavení na libovolném konečném počtu bitů získáte aproximaci. Na většině
dnešních počítačů se hodnoty float aproximují binárním zlomkem, jehož čitatel
používá prvních 53 bitů od nejvýznamnějšího bitu a jmenovatel je mocninou dvou.
Pro 1/10 je tímto zlomkem ``3602879701896397 / 2 ** 55``, který je skutečné
hodnotě 1/10 blízký, ale není jí přesně roven.

Mnoho uživatelů si aproximaci neuvědomuje kvůli způsobu zobrazování hodnot.
Python vypisuje pouze desetinnou aproximaci skutečné desetinné hodnoty binární
aproximace uložené v počítači. Kdyby měl na většině počítačů vypsat skutečnou
desetinnou hodnotu binární aproximace uložené pro 0.1, musel by zobrazit::

   >>> 0.1
   0.1000000000000000055511151231257827021181583404541015625

To je více číslic, než většina lidí považuje za užitečné, a proto Python místo
toho zobrazí zaokrouhlenou hodnotu s přijatelným počtem číslic:

.. doctest::

   >>> 1 / 10
   0.1

Pamatujte, že ačkoli vypsaný výsledek vypadá jako přesná hodnota 1/10, skutečně
uloženou hodnotou je nejbližší reprezentovatelný binární zlomek.

Je zajímavé, že mnoho různých desetinných čísel sdílí stejnou nejbližší binární
aproximaci. Čísla ``0.1``, ``0.10000000000000001`` a
``0.1000000000000000055511151231257827021181583404541015625`` jsou například
všechna aproximována zlomkem ``3602879701896397 / 2 ** 55``. Protože sdílejí
stejnou aproximaci, lze zobrazit kterékoli z nich a stále zachovat invariant
``eval(repr(x)) == x``.

Výzva Pythonu a vestavěná funkce :func:`repr` historicky vybíraly variantu se 17
platnými číslicemi, ``0.10000000000000001``. Od Pythonu 3.1 dokáže Python na
většině systémů vybrat nejkratší z nich a zobrazit jednoduše ``0.1``.

Jde o samotnou podstatu binárních čísel s plovoucí řádovou čárkou: není to chyba
Pythonu ani vašeho kódu. Stejný jev uvidíte ve všech jazycích podporujících
hardwarovou aritmetiku s plovoucí řádovou čárkou (některé jazyky však rozdíl ve
výchozím nastavení nebo ve všech režimech výstupu nemusejí *zobrazit*).

Pro příjemnější výstup můžete pomocí formátování řetězců omezit počet platných
číslic:

.. doctest::

   >>> format(math.pi, '.12g')  # give 12 significant digits
   '3.14159265359'

   >>> format(math.pi, '.2f')   # give 2 digits after the point
   '3.14'

   >>> repr(math.pi)
   '3.141592653589793'

Je důležité si uvědomit, že jde v pravém slova smyslu o iluzi: zaokrouhlujete
pouze *zobrazení* skutečné strojové hodnoty.

Jedna iluze může vést k další. Protože například 0.1 není přesně 1/10, nemusí
ani součet tří hodnot 0.1 dát přesně 0.3:

.. doctest::

   >>> 0.1 + 0.1 + 0.1 == 0.3
   False

Protože se 0.1 nemůže více přiblížit přesné hodnotě 1/10 a 0.3 přesné hodnotě
3/10, nepomůže ani předběžné zaokrouhlení funkcí :func:`round`:

.. doctest::

   >>> round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)
   False

Přestože čísla nelze více přiblížit jejich zamýšleným přesným hodnotám, pro
porovnání nepřesných hodnot může být užitečná funkce :func:`math.isclose`:

.. doctest::

   >>> math.isclose(0.1 + 0.1 + 0.1, 0.3)
   True

K porovnání hrubých aproximací lze alternativně použít funkci :func:`round`:

.. doctest::

   >>> round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
   True

Binární aritmetika s plovoucí řádovou čárkou skrývá mnoho podobných překvapení.
Problém s hodnotou „0.1“ je podrobně vysvětlen níže v části „Chyba
reprezentace“. Příjemné shrnutí fungování binárních čísel s plovoucí řádovou
čárkou a problémů běžných v praxi nabízí `Examples of Floating Point Problems
<https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/>`_.
Úplnější přehled dalších častých překvapení naleznete také v `The Perils of
Floating Point <http://www.indowsway.com/floatingpoint.htm>`_.

Jak se ke konci uvedeného textu píše, „jednoduché odpovědi neexistují“.
Nenechte se však čísly s plovoucí řádovou čárkou zbytečně odradit. Chyby operací
s typem float v Pythonu pocházejí z hardwaru a na většině počítačů nepřesahují
řádově jednu část z 2\*\*53 na operaci. To je pro většinu úloh více než
dostatečné, je však třeba pamatovat, že nejde o desetinnou aritmetiku a každá
operace s float může přinést novou chybu zaokrouhlení.

Patologické případy sice existují, při většině běžných použití aritmetiky s
plovoucí řádovou čárkou však získáte očekávaný výsledek, pokud zobrazení
konečných výsledků zaokrouhlíte na požadovaný počet desetinných číslic. Obvykle
postačí :func:`str`; jemnější řízení umožňují specifikátory metody
:meth:`str.format` popsané v části :ref:`formatstrings`.

Pro případy vyžadující přesnou desetinnou reprezentaci zkuste modul
:mod:`decimal`, který implementuje desetinnou aritmetiku vhodnou pro účetní
aplikace a aplikace s vysokou přesností.

Jinou podobu přesné aritmetiky podporuje modul :mod:`fractions`, který
implementuje aritmetiku založenou na racionálních číslech (takže lze přesně
reprezentovat například 1/3).

Pokud operace s plovoucí řádovou čárkou používáte intenzivně, prohlédněte si
balíček NumPy a mnoho dalších balíčků pro matematické a statistické operace z
projektu SciPy. Viz <https://scipy.org>.

Python poskytuje nástroje pro vzácné situace, kdy *opravdu* chcete znát přesnou
hodnotu float. Metoda :meth:`float.as_integer_ratio` vyjádří hodnotu float jako
zlomek:

.. doctest::

   >>> x = 3.14159
   >>> x.as_integer_ratio()
   (3537115888337719, 1125899906842624)

Protože je poměr přesný, lze z něj beze ztráty obnovit původní hodnotu:

.. doctest::

    >>> x == 3537115888337719 / 1125899906842624
    True

Metoda :meth:`float.hex` vyjádří float šestnáctkově (v soustavě o základu 16),
a opět tak poskytne přesnou hodnotu uloženou počítačem:

.. doctest::

   >>> x.hex()
   '0x1.921f9f01b866ep+1'

Z této přesné šestnáctkové reprezentace lze hodnotu float přesně obnovit:

.. doctest::

    >>> x == float.fromhex('0x1.921f9f01b866ep+1')
    True

Přesná reprezentace je užitečná pro spolehlivý přenos hodnot mezi různými
verzemi Pythonu (nezávisle na platformě) a výměnu dat s jinými jazyky
podporujícími stejný formát, například Java a C99.

Dalším užitečným nástrojem je funkce :func:`sum`, která pomáhá omezit ztrátu
přesnosti při sčítání. Pro mezikroky zaokrouhlování při přidávání hodnot k
průběžnému součtu používá rozšířenou přesnost. Tím může zlepšit celkovou přesnost
a zabránit nahromadění chyb, které by ovlivnily konečný součet:

.. doctest::

   >>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
   False
   >>> sum([0.1] * 10) == 1.0
   True

:func:`math.fsum` jde ještě dále a při přidávání hodnot k průběžnému součtu
sleduje všechny „ztracené číslice“, takže se výsledek zaokrouhlí pouze jednou.
Je pomalejší než :func:`sum`, ale přesnější v neobvyklých případech, kdy se
vstupy s velkou absolutní hodnotou navzájem téměř vyruší a konečný součet je
blízký nule:

.. doctest::

   >>> arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
   ...        -143401161400469.7, 266262841.31058735, -0.003244936839808227]
   >>> float(sum(map(Fraction, arr)))   # Exact summation with single rounding
   8.042173697819788e-13
   >>> math.fsum(arr)                   # Single rounding
   8.042173697819788e-13
   >>> sum(arr)                         # Multiple roundings in extended precision
   8.042178034628478e-13
   >>> total = 0.0
   >>> for x in arr:
   ...     total += x                   # Multiple roundings in standard precision
   ...
   >>> total                            # Straight addition has no correct digits!
   -0.0051575902860057365


.. _tut-fp-error:

Chyba reprezentace
====================

Tato část podrobně vysvětluje příklad „0.1“ a ukazuje, jak lze podobné případy
přesně analyzovat. Předpokládá základní znalost binární reprezentace čísel s
plovoucí řádovou čárkou.

:dfn:`Chyba reprezentace <Representation error>` označuje skutečnost, že některé
(ve skutečnosti většinu) desetinné zlomky nelze přesně reprezentovat jako
binární zlomky o základu 2. To je hlavní důvod, proč Python (stejně jako Perl,
C, C++, Java, Fortran a mnoho dalších jazyků) často nezobrazí přesné desetinné
číslo, které očekáváte.

Proč tomu tak je? Hodnotu 1/10 nelze přesně reprezentovat jako binární zlomek.
Přinejmenším od roku 2000 téměř všechny počítače používají binární aritmetiku s
plovoucí řádovou čárkou IEEE 754 a téměř všechny platformy mapují hodnoty float
Pythonu na 64bitové hodnoty IEEE 754 binary64 s „dvojitou přesností“. Ty
obsahují 53 bitů přesnosti, takže se počítač při vstupu snaží převést 0.1 na
nejbližší možný zlomek tvaru *J*/2**\ *N*, kde *J* je celé číslo obsahující
přesně 53 bitů. Přepišme
::

   1 / 10 ~= J / (2**N)

jako::

   J ~= 2**N / 10

a připomeňme, že *J* má přesně 53 bitů (je ``>= 2**52`` a ``< 2**53``).
Nejlepší hodnota *N* je pak 56:

.. doctest::

    >>> 2**52 <=  2**56 // 10  < 2**53
    True

Hodnota 56 je tedy jedinou hodnotou *N*, při níž má *J* přesně 53 bitů. Nejlepší
možnou hodnotou *J* je potom zaokrouhlený podíl:

.. doctest::

   >>> q, r = divmod(2**56, 10)
   >>> r
   6

Protože je zbytek větší než polovina z 10, nejlepší aproximaci získáme
zaokrouhlením nahoru:

.. doctest::



   >>> q+1
   7205759403792794

Nejlepší možná aproximace 1/10 ve dvojité přesnosti IEEE 754 je tedy::

   7205759403792794 / 2 ** 56

Vydělením čitatele i jmenovatele dvěma zlomek zkrátíme na::

   3602879701896397 / 2 ** 55

Protože jsme zaokrouhlili nahoru, je výsledek ve skutečnosti o něco větší než
1/10. Bez zaokrouhlení nahoru by byl podíl o něco menší než 1/10. V žádném
případě však nemůže být *přesně* 1/10!

Počítač tedy nikdy „nevidí“ 1/10; vidí přesný zlomek uvedený výše, nejlepší
dostupnou aproximaci v dvojité přesnosti IEEE 754:

.. doctest::

   >>> 0.1 * 2 ** 55
   3602879701896397.0

Vynásobením tohoto zlomku 10\*\*55 můžeme zobrazit hodnotu na 55 desetinných
číslic:

.. doctest::

   >>> 3602879701896397 * 10 ** 55 // 2 ** 55
   1000000000000000055511151231257827021181583404541015625

To znamená, že přesné číslo uložené v počítači se rovná desetinné hodnotě
0.1000000000000000055511151231257827021181583404541015625. Mnoho jazyků
(včetně starších verzí Pythonu) namísto zobrazení celé desetinné hodnoty
zaokrouhlí výsledek na 17 platných číslic:

.. doctest::

   >>> format(0.1, '.17f')
   '0.10000000000000001'

Moduly :mod:`fractions` a :mod:`decimal` tyto výpočty usnadňují:

.. doctest::

   >>> from decimal import Decimal
   >>> from fractions import Fraction

   >>> Fraction.from_float(0.1)
   Fraction(3602879701896397, 36028797018963968)

   >>> (0.1).as_integer_ratio()
   (3602879701896397, 36028797018963968)

   >>> Decimal.from_float(0.1)
   Decimal('0.1000000000000000055511151231257827021181583404541015625')

   >>> format(Decimal.from_float(0.1), '.17')
   '0.10000000000000001'
