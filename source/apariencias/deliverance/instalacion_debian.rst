.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _instalacion_debian:

Debian GNU/Linux Lenny
======================

Requerimientos previos
----------------------

Iniciar sesión con el usuario root, con el siguiente comando: 

.. code-block:: console

    $ su -

Instalar dependencias de sistema, con el siguiente comando:

.. code-block:: console
 
    # aptitude install python2.4 python2.4-dev python2.4-imaging python-profiler python2.4-setuptools libc6-dev subversion git-core

Instalar el paquete para entorno virtual Python, con el siguiente comando:

.. code-block:: console
 
    # easy_install-2.4 virtualenv

Cerrar sesión del usuario root, con el siguiente comando:

.. code-block:: console
 
    # exit

Entornos virtual Python
-----------------------

Preparar entorno de trabajo, con los siguientes comandos:

.. code-block:: console
 
    $ cd $HOME ; mkdir ./virtualenv ; cd ./virtualenv
    $ virtualenv --no-site-packages --python=/usr/bin/python2.4 python2.4

Activamos el entorno virtual recién creado, para mas información consultar `aquí`_.

.. code-block:: console

    $ source $HOME/virtualenv/python2.4/bin/activate 

Descargar código de ejemplo
---------------------------

Para esto debe preparar el directorio destino de la descaga y realizar la descarga propiamente dicha, para esto ejecute los siguientes comandos:

.. code-block:: console

    $ source $HOME/virtualenv/python2.4/bin/activate 
    $ cd $HOME ; mkdir ./proyectos ; cd ./proyectos 
    $ svn co http://svn.plone.org/svn/collective/deliverancedemo/trunk/ deliverancedemo

Iniciar construcción del proyecto, con los siguientes comandos:

.. code-block:: console
 
    $ cd ./deliverancedemo 
    $ python bootstrap.py

(Nota antes de seguir al siguiente paso se aconseja modificar el ``buildout`` por el proporcionado acá para evitar errores de instalación, se han proporcionado 2 uno para instalación del servicio de ``Deliverance`` y otro de instalación de ``Deliverance`` con ``Plone``, modificarlo por el que este acorde a sus preferencias)

.. code-block:: console

    $ ./bin/buildout -vN

Usted debería ver algo como esto:

.. code-block:: console
 
    Generated script '/home/user/deliverancedemo/bin/paster'.
    Generated script '/home/user/deliverancedemo/bin/deliverance-proxy'.
    Generated interpreter '/home/user/deliverancedemo/deliverancedemo/bin/py'.   

Usted debe iniciar la instancia Zope, con el siguiente comando:

.. code-block:: console

    $ ./bin/instance start

Y por ultimo debe iniciar el servidor proxy Deliverance, con el siguiente comando:

.. code-block:: console

    $ ./bin/deliverance-proxy ./rules.xml
    To see logging, visit http://localhost:5000/.deliverance/login
        after login go to http://localhost:5000/?deliv_log
    serving on http://localhost:5000

Como puede ver le esta indicando que Deliverance esta siendo servido por la dirección URL http://localhost:5000/ aplicando su estilo y tema HTML al contenido como se define en la archivo deliverance.xml

Para acceder a la consola depuración de iniciar sesión por la dirección URL http://localhost:5000/.deliverance/login y luego acceder a la dirección URL http://localhost:5000/?deliv_log


Entonces la instalación fue realizada correctamente.

.. _Deliverance: http://pypi.python.org/pypi/Deliverance
.. _DeliveranceDemo: http://svn.plone.org/svn/collective/deliverancedemo/trunk/
.. _aquí: http://readthedocs.org/docs/plone-spanish-docs/en/latest/python/creacion-de-entornos-virtuales-python.html
