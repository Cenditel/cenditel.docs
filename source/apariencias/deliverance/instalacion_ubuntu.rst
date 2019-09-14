.. -*- coding: utf-8 -*-

.. highlight:: rest

.. _instalacion_ubuntu:

Ubuntu 11.04 Natty Narwhal
==========================
Instalar dependencias de sistema

.. code-block:: console
 
    # sudo apt-get install python python-dev python-imaging python-profiler python-setuptools libc6-dev subversion git-core build-essential

Instalar entorno virtual

.. code-block:: console
 
    # easy_install-2.6 virtualenv

Cerrar sesión del usuario root 

.. code-block:: console

    # exit

Preparar entorno de trabajo

.. code-block:: console
 
    $ cd $HOME ; mkdir ./virtualenv ; cd ./virtualenv

.. note: 
    Debido a los cambios de versiones algunas distros ya no vienen con un ``python2.4`` nativo en el sistema tal es el caso de la versión de ``Ubuntu`` de la 10.04  en adelante por lo que se hace necesario descargar un instalador unificado de Plone 4.x que posee un ``python2.6`` listo para su uso se puede descargar desde https://pypi.org/project/python-ldap/2.4.4. Descomprimimos el ``.tar.gz`` dentro de la carpeta que acabamos de crear y para la instalación del `"Virtualenv" <https://plone-spanish-docs.readthedocs.io/es/latest/python/creacion_entornos_virtuales.html>`_ le apuntamos esa dirección quedaria algo asi: 

.. code-block:: console

    $ virtualenv --no-site-packages --python=/home/usr/virtualenv/bin/python2.6 python2.6 

Nota: /usr se refiere al usuario del sistema el nombre de usuario que usted tenga en el sistema

Activamos el entorno virtual recién creado y seguimos con la instalación, para mas información consultar https://plone-spanish-docs.readthedocs.io/es/latest/python/creacion_entornos_virtuales.html

.. code-block:: console

    $ source $HOME/virtualenv/python2.6/bin/activate 
    $ cd $HOME ; mkdir ./proyectos ; cd ./proyectos 
    $ svn co http://svn.plone.org/svn/collective/deliverancedemo/trunk/ deliverancedemo

Iniciar construcción del proyecto

.. code-block:: console
 
    $ cd ./deliverancedemo 
    $ python bootstrap.py

(Nota antes de seguir al siguiente paso se aconseja modificar el ``buildout`` por el proporcionado acá para evitar errores de instalación, se han proporcionado 2 uno para instalación del servicio de ``Deliverance`` y otro de instalación de ``Deliverance`` con ``Plone``, modificarlo por el que este acorde a sus preferencias)

.. code-block:: console

    $ ./bin/buildout -vN

Usted debería ver algo como esto:

.. code-block:: console
 
    Generated script '/home/user/deliverancedemo/bin/paster'.
    Generated script '/home/user/deliverancedemo/bin/deliverance-proxy'/.
    Generated interpreter '/home/user/deliverancedemo/deliverancedemo/bin/py'.

Y por ultimo debe iniciar el servidor proxy Deliverance, con el siguiente comando:

.. code-block:: console

    $ ./bin/deliverance-proxy ./rules.xml
    To see logging, visit http://localhost:5000/.deliverance/login
        after login go to http://localhost:5000/?deliv_log
    serving on http://localhost:5000

Como puede ver le esta indicando que Deliverance esta siendo servido por la dirección URL http://localhost:5000/ aplicando su estilo y tema HTML al contenido como se define en la archivo deliverance.xml

Para acceder a la consola depuración de iniciar sesión por la dirección URL http://localhost:5000/.deliverance/login y luego acceder a la dirección URL http://localhost:5000/?deliv_log


Entonces la instalación fue realizada correctamente.

.. _Deliverance: https://pypi.org/project/Deliverance
.. _DeliveranceDemo: http://svn.plone.org/svn/collective/deliverancedemo/trunk/
