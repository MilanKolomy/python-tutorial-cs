.. _tut-intro:

********************
Pro povzbuzení chuti
********************

Pokud s počítači pracujete často, dříve či později narazíte na úlohu, kterou
byste chtěli automatizovat. Můžete například potřebovat vyhledat a nahradit text
ve velkém množství textových souborů nebo složitým způsobem přejmenovat
a uspořádat mnoho fotografií. Možná byste chtěli napsat malou databázi na míru,
specializovanou aplikaci s grafickým uživatelským rozhraním nebo jednoduchou
hru.

Jste-li profesionální vývojář softwaru, možná musíte pracovat s několika
knihovnami v C/C++/Javě, ale obvyklý cyklus zápis/překlad/testování/opětovný
překlad vám připadá příliš pomalý. Třeba pro takovou knihovnu píšete sadu testů
a tvorba testovacího kódu je pro vás únavná. Nebo jste možná napsali program,
kterému by prospěl rozšiřující jazyk, a nechcete pro svou aplikaci navrhovat
a implementovat úplně nový jazyk.

Python je právě ten jazyk, který hledáte.

Pro některé z těchto úloh byste mohli napsat skript unixového shellu nebo
dávkový soubor Windows. Shellové skripty se však nejlépe hodí k přesouvání
souborů a úpravám textových dat, nikoli k tvorbě aplikací s grafickým rozhraním
nebo her. Mohli byste napsat program v C/C++/Javě, ale i vytvoření prvního návrhu
může zabrat mnoho času. Python se používá jednodušeji, je dostupný v systémech
Windows, macOS i Unix a pomůže vám práci dokončit rychleji.

Python se používá snadno, je to však skutečný programovací jazyk, který velkým
programům poskytuje mnohem více struktury a podpory než shellové skripty či
dávkové soubory. Zároveň nabízí podstatně více kontroly chyb než C, a protože je
to *jazyk velmi vysoké úrovně*, má vestavěné vysokoúrovňové datové typy, jako
jsou pružná pole a slovníky. Díky obecnějším datovým typům lze Python použít
v mnohem širší oblasti problémů než Awk nebo dokonce Perl, přesto je v něm řada
věcí přinejmenším stejně snadná jako v těchto jazycích.

Python umožňuje rozdělit program do modulů, které lze opakovaně použít v jiných
programech v Pythonu. Dodává se s rozsáhlou sbírkou standardních modulů, které
můžete použít jako základ svých programů --- nebo jako příklady, na nichž se
začnete učit programovat v Pythonu. Některé z těchto modulů poskytují například
vstup a výstup souborů, systémová volání, sokety, a dokonce rozhraní k sadám
nástrojů pro grafické uživatelské rozhraní, jako je Tk.

Python je interpretovaný jazyk, což může při vývoji programů ušetřit mnoho času,
protože není potřeba překlad ani sestavování odkazů. Interpret lze používat
interaktivně, takže se snadno experimentuje s vlastnostmi jazyka, píší jednorázové
programy nebo testují funkce při vývoji programu zdola nahoru. Poslouží také jako
praktická stolní kalkulačka.

Python umožňuje psát programy stručně a čitelně. Programy napsané v Pythonu jsou
obvykle mnohem kratší než odpovídající programy v C, C++ nebo Javě, a to
z několika důvodů:

* vysokoúrovňové datové typy umožňují vyjádřit složité operace jediným
  příkazem;

* příkazy se seskupují odsazením namísto počátečních a koncových závorek;

* není nutné deklarovat proměnné ani argumenty.

Python je *rozšiřitelný*: umíte-li programovat v C, můžete do interpretu snadno
přidat novou vestavěnou funkci nebo modul, ať už pro provádění kritických operací
maximální rychlostí, nebo pro propojení programů v Pythonu s knihovnami, které
mohou být dostupné pouze v binární podobě (například s grafickou knihovnou
konkrétního dodavatele). Až si Python skutečně oblíbíte, můžete jeho interpret
vložit do aplikace napsané v C a použít jej jako rozšiřující nebo příkazový jazyk
této aplikace.

Mimochodem, jazyk je pojmenován podle pořadu BBC „Monty Python's Flying Circus“
a s plazy nemá nic společného. Odkazy na skeče Monty Python v dokumentaci jsou
nejen povolené, ale přímo vítané!

Teď, když vás Python nadchl, jej budete chtít prozkoumat podrobněji. Nejlépe se
jazyk naučíte jeho používáním, a proto vás tutorial vybízí, abyste si při čtení
hráli s interpretem Pythonu.

Následující kapitola vysvětluje praktické používání interpretu. Jde o poměrně
všední informace, jsou však nezbytné pro zkoušení příkladů uvedených dále.

Zbytek tutorialu představuje na příkladech různé vlastnosti jazyka a systému
Python: začíná jednoduchými výrazy, příkazy a datovými typy, pokračuje funkcemi
a moduly a nakonec se dotkne pokročilých konceptů, jako jsou výjimky a uživatelem
definované třídy.
