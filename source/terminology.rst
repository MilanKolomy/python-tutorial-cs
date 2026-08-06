Terminologický slovník
======================

Slovník určuje preferované překlady opakujících se odborných termínů.
Anglický termín lze při prvním důležitém výskytu uvést v závorce.

.. list-table::
   :header-rows: 1
   :widths: 28 28 44

   * - Anglicky
     - Preferovaný český termín
     - Poznámka
   * - argument
     - argument
     - Hodnota předaná při volání funkce.
   * - annotation
     - anotace
     - Nepovinné metadatové informace, například anotace parametrů a návratové hodnoty.
   * - attribute
     - atribut
     - Ponechat názvy konkrétních atributů beze změny.
   * - built-in
     - vestavěný
     - Například „vestavěná funkce“ nebo „vestavěný typ“.
   * - class
     - třída
     - 
   * - command-line option
     - volba příkazového řádku
     - Samotný zápis volby, například ``-i``, se nemění.
   * - concatenation
     - zřetězení
     - Spojení řetězců nebo sekvencí.
   * - dictionary comprehension
     - generátorová notace slovníku
     - Stručný zápis pro vytvoření slovníku.
   * - dictionary
     - slovník
     - Datový typ ``dict``; nezaměňovat s tímto terminologickým slovníkem.
   * - exception
     - výjimka
     - 
   * - exception chaining
     - řetězení výjimek
     - Vazba mezi původní a následně vyvolanou výjimkou pomocí ``raise ... from``.
   * - exception group
     - skupina výjimek
     - Objekt ``ExceptionGroup`` sdružující více výjimek.
   * - exception handler
     - obsluha výjimky
     - Kód v klauzuli ``except``; podle kontextu také „obsluha výjimek“.
   * - file object
     - souborový objekt
     - Objekt poskytující rozhraní pro čtení ze souboru a zápis do něj.
   * - formatted string literal / f-string
     - formátovaný řetězcový literál / f-řetězec
     - Prefix ``f`` nebo ``F`` a výrazy ve složených závorkách.
   * - expression
     - výraz
     - 
   * - floor division
     - celočíselné dělení
     - Operátor ``//``; výsledek se zaokrouhluje směrem dolů.
   * - floating-point number / arithmetic
     - číslo / aritmetika s plovoucí řádovou čárkou
     - Technický typ ``float`` a konkrétní číselné zápisy se nemění.
   * - function
     - funkce
     - 
   * - garbage collection
     - automatický úklid paměti
     - Automatické vyhledávání a uvolňování již nedosažitelných objektů.
   * - guard
     - stráž
     - Podmínka ``if`` připojená ke vzoru příkazu ``match``.
   * - indentation
     - odsazení
     - V Pythonu určuje strukturu bloků příkazů.
   * - inheritance
     - dědičnost
     - ``multiple inheritance`` překládat jako „vícenásobná dědičnost“.
   * - instance
     - instance
     - Konkrétní objekt vytvořený z třídy.
   * - indexing
     - indexování
     - Přístup k prvku pomocí indexu.
   * - immutable
     - neměnný
     - O objektu, jehož hodnotu nelze po vytvoření změnit.
   * - interpreter
     - interpret
     - „Interpret Pythonu“, nikoli „interpreter“.
   * - iterable
     - iterovatelný objekt
     - Objekt, jehož prvky lze postupně procházet.
   * - iterator / generator
     - iterátor / generátor
     - Iterátor poskytuje postupný přístup k prvkům; generátor jej vytváří pomocí ``yield``.
   * - keyword argument
     - argument klíčového slova
     - Argument předaný ve tvaru ``name=value``.
   * - list
     - seznam
     - Datový typ ``list``.
   * - list comprehension
     - generátorová notace seznamu
     - Při prvním důležitém výskytu uvést anglické „list comprehension“.
   * - logging
     - protokolování
     - Záznam provozních, informačních a chybových zpráv aplikace.
   * - literal
     - literál
     - Hodnota zapsaná přímo ve zdrojovém kódu.
   * - method
     - metoda
     - 
   * - name mangling
     - komolení názvů
     - Mechanismus převodu názvů s dvojitým úvodním podtržítkem ve třídách.
   * - module
     - modul
     - 
   * - module search path
     - vyhledávací cesta modulů
     - Posloupnost umístění, ve kterých Python hledá importované moduly.
   * - mutable
     - měnitelný
     - O objektu, který lze po vytvoření měnit.
   * - namespace
     - jmenný prostor
     - Mapování názvů na objekty; ``namespace package`` překládat jako „jmenný balíček“.
   * - object
     - objekt
     - 
   * - package / subpackage
     - balíček / podbalíček
     - Adresářová struktura sdružující moduly; názvy konkrétních balíčků se nemění.
   * - parameter
     - parametr
     - Název v definici funkce; odlišovat od argumentu při volání.
   * - pattern matching
     - porovnávání vzorů
     - Mechanismus příkazu ``match`` a bloků ``case``.
   * - positional-only / keyword-only parameter
     - pouze poziční / pouze klíčový parametr
     - Druh parametru vyznačený v definici funkce pomocí ``/`` nebo ``*``.
   * - primary/secondary prompt
     - primární/sekundární výzva
     - Výzvy interpretu ``>>>`` a ``...``.
   * - raw string
     - surový řetězec
     - Při prvním výskytu uvést anglické „raw string“; zapisuje se s prefixem ``r``.
   * - regular expression
     - regulární výraz
     - Konkrétní vzory a syntaxe regulárních výrazů se nemění.
   * - representation error
     - chyba reprezentace
     - Nepřesnost vznikající při převodu hodnoty do dostupné číselné reprezentace.
   * - relative / absolute import
     - relativní / absolutní import
     - Relativní import používá úvodní tečky; zápis příkazu se nemění.
   * - scope
     - obor platnosti
     - Kontext, ve kterém je název přímo dostupný.
   * - sequence
     - sekvence
     - 
   * - serialization / deserialization
     - serializace / deserializace
     - Převod objektu na přenositelnou reprezentaci a její zpětné načtení.
   * - set
     - množina
     - Datový typ ``set``; neuspořádaná kolekce bez duplicit.
   * - slice, slicing
     - výřez, vytváření výřezu
     - Při prvním důležitém výskytu lze uvést anglické „slicing“.
   * - source code
     - zdrojový kód
     - 
   * - stack / queue
     - zásobník / fronta
     - Zásobník používá LIFO, fronta FIFO.
   * - statement
     - příkaz
     - 
   * - standard library
     - standardní knihovna
     - Soubor modulů a balíčků dodávaných s Pythonem.
   * - syntax error
     - syntaktická chyba
     - Výjimka ``SyntaxError``; výpis a technický název se nemění.
   * - string
     - řetězec
     - Datový typ ``str``; při potřebě upřesnit „textový řetězec“.
   * - traceback
     - výpis zásobníku volání
     - Při prvním výskytu lze doplnit anglické ``traceback``.
   * - thread / multi-threading
     - vlákno / vícevláknové zpracování
     - Termíny pro souběžné provádění v rámci procesu.
   * - text mode / binary mode
     - textový režim / binární režim
     - Režim otevření souboru; konkrétní hodnoty argumentu ``mode`` se nemění.
   * - tuple
     - n-tice
     - 
   * - virtual environment
     - virtuální prostředí
     - 
   * - weak reference
     - slabá reference
     - Reference, která sama nebrání uvolnění objektu z paměti.
   * - wildcard
     - žolík
     - V porovnávání vzorů například ``_``; při prvním výskytu uvést „wildcard“.
