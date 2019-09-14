.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _deliverance_instalacion:

===========
Instalación
===========

Para instalar ``Deliverance``, usted podría instalar la distribución de `Deliverance`_  de PyPI.

.. note::

    El paquete ``Deliverance`` sólo se requiere para obtener el comando para manipular el `servidor proxy`_ Deliverance.

Usted puede instalar la distribución de `Deliverance`_ usando `easy_install`_, `pip`_ o `zc.buildout`_. Por ejemplo, usando ``easy_install`` (sería ideal si se ejecuta dentro de un `entorno virtual`_ Python):

.. code-block:: console

    $ easy_install -U Deliverance

Usted también puede instalar con la herramienta ``pip`` si es su preferencia, puede realizarlo con el siguiente comando:

.. code-block:: console

    $ pip install Deliverance


Modos de instalación
====================

Para este caso se instalara el ejemplo de instalación llamado `DeliveranceDemo`_

.. toctree::
   :maxdepth: 2

   instalacion_buildout
   instalacion_wsgi


Instalación en diversas plataformas
===================================

A continuación se ofrece una serie de recetas de como instalar ``Deliverance`` en varios sistemas operativos:

.. toctree::
   :maxdepth: 2

   instalacion_debian
   instalacion_ubuntu
   instalacion_python


.. _Deliverance: https://pypi.org/project/Deliverance/
.. _easy_install: https://plone-spanish-docs.readthedocs.io/es/latest/python/setuptools.html
.. _pip: https://plone-spanish-docs.readthedocs.io/es/latest/python/distribute_pip.html
.. _zc.buildout: https://plone-spanish-docs.readthedocs.io/es/latest/buildout/replicacion_proyectos_python.html
.. _entorno virtual: https://plone-spanish-docs.readthedocs.io/es/latest/python/creacion_entornos_virtuales.html
.. _middleware WSGI: https://en.wikipedia.org/wiki/Python_Paste#WSGI_middleware
.. _DeliveranceDemo: http://svn.plone.org/svn/collective/deliverancedemo/trunk/
.. _servidor proxy: https://es.wikipedia.org/wiki/Servidor_proxy

