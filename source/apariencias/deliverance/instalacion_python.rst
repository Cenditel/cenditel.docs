.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _instalacion_python:

Instalación de Python mediante zc.buildout
==========================================

A continuación se explicara como realizar una instalación de un interprete python2.4 mediante mecanismos de configuración zc.buildout

El primer paso seria crear una carpeta y acceder a ella

.. code-block:: console
 
    $ cd $HOME ; mkdir ./python2.4 ; cd ./python2.4 
    $ svn co http://svn.plone.org/svn/collective/buildout/python/src buildout.python
    $ cd buildout.python

Iniciar construcción del proyecto

.. code-block:: console
  
    $ python bootstrap.py

Luego de haber realizado este paso es recomendable hacerle las modificaciones correspondientes al buildout, para este ejemplo se realizo una instalación de un python2.4, si usted necesita hacer una instalación de este tipo verificar que su buildout este igual al que se presenta a continuación:

.. code-block:: cfg

    # This is here just for backward compatibility
    [buildout]
    extends =
        src/base.cfg
        src/readline.cfg
        src/libjpeg.cfg
        src/python24.cfg
    #    src/python25.cfg
    #    src/python26.cfg
    #    src/python27.cfg
    #    src/python32.cfg
        src/links.cfg

    parts =
        ${buildout:base-parts}
        ${buildout:readline-parts}
        ${buildout:libjpeg-parts}
        ${buildout:python24-parts}
    #    ${buildout:python25-parts}
    #    ${buildout:python26-parts}
    #    ${buildout:python27-parts}
    #    ${buildout:python32-parts}
        ${buildout:links-parts}

    python-buildout-root = ${buildout:directory}/src

    # we want our own eggs directory and nothing shared from a
    # ~/.buildout/default.cfg to prevent any errors and interference
    eggs-directory = eggs


    extra_options_py24 = --with-threads --enable-unicode=ucs4
    #extra_options_py24 = --with-threads --enable-unicode=ucs4 --with-readline

    [install-links]
    prefix = /opt/local

Luego de haberle aplicado los cambios respectivos a su buildout ejecutar el siguiente comando

.. code-block:: console

    $ ./bin/buildout -vN

A este punto ya la instalación debe haberse realizado correctamente y se debe poder activar el entorno virtual sin ningún problema.

.. code-block:: console

    $ source $HOME/python2.4/bin/activate 

.. _Deliverance: https://pypi.org/project/Deliverance
.. _DeliveranceDemo: http://svn.plone.org/svn/collective/deliverancedemo/trunk/
