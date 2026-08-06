
.. _tut-venv:

*********************************
Virtuální prostředí a balíčky
*********************************

Úvod
============

Aplikace v Pythonu často používají balíčky a moduly, které nejsou součástí
standardní knihovny. Někdy potřebují určitou verzi knihovny, protože vyžadují
opravu konkrétní chyby nebo byly napsány pro zastaralou verzi jejího rozhraní.

Jedna instalace Pythonu proto nemusí být schopna splnit požadavky všech
aplikací. Pokud aplikace A potřebuje verzi 1.0 určitého modulu, ale aplikace B
potřebuje verzi 2.0, jsou jejich požadavky v konfliktu a po instalaci kterékoli
z těchto verzí nebude možné jednu z aplikací spustit.

Řešením je vytvořit :term:`virtuální prostředí <virtual environment>`, tedy
samostatný adresářový strom obsahující instalaci určité verze Pythonu a několik
dalších balíčků.

Různé aplikace pak mohou používat různá virtuální prostředí. V předchozím
příkladu konfliktních požadavků může mít aplikace A vlastní virtuální prostředí
s verzí 1.0 a aplikace B jiné prostředí s verzí 2.0. Pokud aplikace B vyžaduje
aktualizaci knihovny na verzi 3.0, prostředí aplikace A to neovlivní.


Vytváření virtuálních prostředí
===============================

Modul pro vytváření a správu virtuálních prostředí se nazývá :mod:`venv`.
:mod:`venv` nainstaluje verzi Pythonu, ze které byl příkaz spuštěn (jak ji uvádí
volba :option:`--version`). Spuštění příkazu pomocí ``python3.12`` například
nainstaluje verzi 3.12.

Chcete-li vytvořit virtuální prostředí, zvolte adresář, do kterého je chcete
umístit, a spusťte modul :mod:`venv` jako skript s cestou k tomuto adresáři::

   python -m venv tutorial-env

Tím se vytvoří adresář ``tutorial-env``, pokud dosud neexistuje, a uvnitř něj
adresáře obsahující kopii interpretu Pythonu a různé podpůrné soubory.

Běžným názvem adresáře virtuálního prostředí je ``.venv``. Tento název adresář
v shellu zpravidla skryje, takže nepřekáží, a zároveň vysvětluje jeho účel.
Zabraňuje také konfliktu se soubory ``.env`` pro definice proměnných prostředí,
které podporují některé nástroje.

Po vytvoření můžete virtuální prostředí aktivovat.

Ve Windows spusťte::

  tutorial-env\Scripts\activate

V Unixu nebo macOS spusťte::

  source tutorial-env/bin/activate

(Tento skript je napsán pro shell bash. Používáte-li shell :program:`csh` nebo
:program:`fish`, použijte místo něj odpovídající skript ``activate.csh`` nebo
``activate.fish``.)

Aktivace virtuálního prostředí změní výzvu shellu tak, aby ukazovala používané
prostředí, a upraví prostředí tak, že příkaz ``python`` spustí právě danou verzi
a instalaci Pythonu. Například:

.. code-block:: console

  $ source ~/envs/tutorial-env/bin/activate
  (tutorial-env) $ python
  Python 3.5.1 (default, May  6 2016, 10:59:36)
    ...
  >>> import sys
  >>> sys.path
  ['', '/usr/local/lib/python35.zip', ...,
  '~/envs/tutorial-env/lib/python3.5/site-packages']
  >>>

Virtuální prostředí deaktivujete zadáním::

    deactivate

do terminálu.

Správa balíčků pomocí pip
==========================

Balíčky lze instalovat, aktualizovat a odstraňovat programem :program:`pip`.
Ve výchozím nastavení ``pip`` instaluje balíčky z `Python Package Index
<https://pypi.org>`_. Jeho obsah můžete procházet ve webovém prohlížeči.

``pip`` má řadu dílčích příkazů: "install", "uninstall", "freeze" atd. (Úplnou
dokumentaci nástroje ``pip`` naleznete v příručce :ref:`installing-index`.)

Nejnovější verzi balíčku nainstalujete zadáním jeho názvu:

.. code-block:: console

  (tutorial-env) $ python -m pip install novas
  Collecting novas
    Downloading novas-3.1.1.3.tar.gz (136kB)
  Installing collected packages: novas
    Running setup.py install for novas
  Successfully installed novas-3.1.1.3

Určitou verzi balíčku lze nainstalovat také uvedením názvu balíčku následovaného
``==`` a číslem verze:

.. code-block:: console

  (tutorial-env) $ python -m pip install requests==2.6.0
  Collecting requests==2.6.0
    Using cached requests-2.6.0-py2.py3-none-any.whl
  Installing collected packages: requests
  Successfully installed requests-2.6.0

Spustíte-li tento příkaz znovu, ``pip`` zjistí, že je požadovaná verze již
nainstalována, a nic neprovede. Můžete zadat jiné číslo verze, nebo balíček
aktualizovat na nejnovější verzi příkazem ``python -m pip install --upgrade``:

.. code-block:: console

  (tutorial-env) $ python -m pip install --upgrade requests
  Collecting requests
  Installing collected packages: requests
    Found existing installation: requests 2.6.0
      Uninstalling requests-2.6.0:
        Successfully uninstalled requests-2.6.0
  Successfully installed requests-2.7.0

``python -m pip uninstall`` následovaný jedním či více názvy balíčků odstraní
tyto balíčky z virtuálního prostředí.

``python -m pip show`` zobrazí informace o konkrétním balíčku:

.. code-block:: console

  (tutorial-env) $ python -m pip show requests
  ---
  Metadata-Version: 2.0
  Name: requests
  Version: 2.7.0
  Summary: Python HTTP for Humans.
  Home-page: http://python-requests.org
  Author: Kenneth Reitz
  Author-email: me@kennethreitz.com
  License: Apache 2.0
  Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
  Requires:

``python -m pip list`` zobrazí všechny balíčky nainstalované ve virtuálním
prostředí:

.. code-block:: console

  (tutorial-env) $ python -m pip list
  novas (3.1.1.3)
  numpy (1.9.2)
  pip (7.0.3)
  requests (2.7.0)
  setuptools (16.0)

``python -m pip freeze`` vytvoří podobný seznam nainstalovaných balíčků, jeho
výstup však používá formát očekávaný příkazem ``python -m pip install``. Tento
seznam se běžně ukládá do souboru ``requirements.txt``:

.. code-block:: console

  (tutorial-env) $ python -m pip freeze > requirements.txt
  (tutorial-env) $ cat requirements.txt
  novas==3.1.1.3
  numpy==1.9.2
  requests==2.7.0

Soubor ``requirements.txt`` lze následně zařadit do správy verzí a distribuovat
jako součást aplikace. Uživatelé pak mohou všechny potřebné balíčky nainstalovat
pomocí ``install -r``:

.. code-block:: console

  (tutorial-env) $ python -m pip install -r requirements.txt
  Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
    ...
  Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
    ...
  Collecting requests==2.7.0 (from -r requirements.txt (line 3))
    ...
  Installing collected packages: novas, numpy, requests
    Running setup.py install for novas
  Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

``pip`` nabízí mnoho dalších voleb. Úplnou dokumentaci naleznete v příručce
:ref:`installing-index`. Pokud jste vytvořili balíček a chcete jej zpřístupnit
v Python Package Index, přečtěte si `uživatelskou příručku pro balíčkování v
Pythonu <Python packaging user guide>`_.

.. _Python Packaging User Guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/
