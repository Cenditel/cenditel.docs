.. highlight:: rest

.. _diazo_instalacion:

===========
Instalación
===========

Para instalar Diazo, usted podría instalar la distribución de `diazo`_  de PyPI

.. note::

    El paquete Diazo sólo se requiere para obtener el compilador Diazo y herramientas de desarrollo. Si se implementa el tema Diazo en un servidor web, no es necesario la distribución `diazo`_  en ese servidor.

Usted puede instalar la distribución de `diazo`_ usando `easy_install`_, `pip`_ o `zc.buildout`_. Por ejemplo, usando easy_install (sería ideal si se ejecuta dentro de un `entorno virtual`_ Python):

.. code-block:: console

    $ easy_install -U diazo


Opcionalmente, si estas usando zc.buildout, usted puede usar la siguiente configuración buildout.cfg como punto de arranque. Este asegura que los scripts de consola estén instalados, lo cual es importante si usted necesita ejecutar manualmente el compilador Diazo:

.. code-block:: cfg

    [buildout]
    parts =
       diazo

    [diazo]
    recipe = zc.recipe.egg
    eggs = diazo

En algunos sistemas operativos, en particular, Mac OS X la instalación de un "buen" paquete (Python egg) de ``lxml`` puede ser problemático, debido a una falta de coincidencia en las versiones del sistema operativo de las librerías ``lxml`` con respecto a la ``libxml2`` y ``libxslt``. Para resolver esto, se puede compilar un ``lxml`` estático de paquete egg usando la siguiente receta buildout:

.. code-block:: cfg

    [buildout]
    # lxml debería estar de primero en la lista ``parts``
    parts =
       lxml
       diazo

    [lxml]
    recipe = z3c.recipe.staticlxml
    egg = lxml

    [diazo]
    recipe = zc.recipe.egg
    eggs = diazo


Entonces usted tiene que comenzar de arranque:

.. code-block:: console

    $ python bootstrap.py

Luego ejecute la construcción de su configuración zc.buildout, con el siguiente comando:

.. code-block:: console

    $ ./bin/buildout -vN


.. note::

    Note que el paquete lxml es una dependencia de diazo, usted podría necesitar instalar los paquetes de desarrollo de libxml2 y libxslt para poder construir esta configuración zc.buildout. En Debian/Ubuntu Linux usted puede ejecutar:

.. code-block:: console

    # sudo apt-get install build-essential python2.6-dev libxml2-dev libxslt1-dev

Una ves instalado, usted debería buscar los scripts ``diazocompiler`` y ``diazorun`` en su directorio ``bin``.

Si usted quiere usar el filtro `middleware WSGI`_, usted debería usar el parámetro extra [wsgi] cuando se instale el paquete egg Diazo, a continuación un ejemplo:

.. code-block:: cfg

    [buildout]
    extends = http://good-py.appspot.com/release/diazo/1.0b1
    versions = versions
    parts =
        diazo

    [diazo]
    recipe = zc.recipe.egg
    eggs =
        diazo [wsgi]
        PasteScript

    [lxml]
    recipe = z3c.recipe.staticlxml
    egg = lxml

Entonces usted tiene que comenzar de arranque:

.. code-block:: console

    $ python bootstrap.py

Luego ejecute la construcción de su configuración zc.buildout, con el siguiente comando:

.. code-block:: console

    $ ./bin/buildout -vN

Al finalizar la construcción zc.buildout más archivos se añaden a la lista scripts disponibles en el directorio ``bin/``, incluyendo ``bin/paster``, ``bin/diazocompiler`` o ``bin/diazorun``. 

Ahora puede crear una carpeta que contiene diversos recursos para nuestro tema.

.. code-block:: console

    $ mkdir mitema

A continuación, crea el archivo ``proxy.ini`` en el directorio de su proyecto zc.buidlout:

.. code-block:: ini

    [server:main]
    use = egg:Paste#http
    host = 0.0.0.0
    port = 5000

    [composite:main]
    use = egg:Paste#urlmap
    /static = static
    / = default

    [app:static]
    use = egg:Paste#static
    document_root = %(here)s/theme

    [pipeline:default]
    pipeline = theme
               content

    [filter:theme]
    use = egg:diazo
    rules = %(here)s/rules.xml
    prefix = /static
    debug = true

    # Proxy: por ejemplo, Plone, cuyo nombre es MiSitio en 127.0.0.1:8080.
    [app:content]
    use = egg:Paste#proxy
    address = http://127.0.0.1:8080/VirtualHostBase/http/127.0.0.1:5000/MiSitio

Uno sólo tiene que lanzar el proxy con el siguiente comando:

.. code-block:: console

    $ bin/paster serve --reload proxy.ini

A continuación, puede tener acceso a nuestra página en http://127.0.0.1:5000 .

.. _diazo: http://pypi.python.org/pypi/diazo
.. _easy_install: http://plone-spanish-docs.readthedocs.org/en/latest/python/setuptools.html
.. _pip: http://plone-spanish-docs.readthedocs.org/en/latest/python/distribute-y-pip.html
.. _zc.buildout: http://plone-spanish-docs.readthedocs.org/en/latest/buildout/replicacion-de-proyectos-python.html#que-es-zc-buildout
.. _entorno virtual: http://plone-spanish-docs.readthedocs.org/en/latest/python/creacion-de-entornos-virtuales-python.html
.. _middleware WSGI: http://en.wikipedia.org/wiki/Python_Paste#WSGI_middleware
