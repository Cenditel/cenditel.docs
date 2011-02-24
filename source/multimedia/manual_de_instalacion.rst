.. highlight:: rest

.. _ManualdeInstalacion:

Manual de Instalación:
----------------------

Para instalar el producto cenditel.multimedia usted necesita solventar las
siguientes dependencias en su instancia Plone/Zope:

* Un sitio Plone 3.3.5 configurado con el producto File System Storage usando la estrategia de almacenamiento "site2".
* Un servidor web nginx, con una configuración especifica en mimetypes, que permitirá el streaming a partir de este.

A continuación veremos los pasos necesarios para replicar el ambiente de desarrollo:


Primer Paso:
^^^^^^^^^^^^
Descargar de la pagina Web del Proyecto el script de instalación buildout que le permitirá configurar un sitio demostrativo.
Para realizar la descarga proceda en un terminal con los siguientes comandos:

.. code-block:: console

    usuario@equipo:~$ mkdir buildouts
    usuario@equipo:~$ cd buildouts
    usuario@equipo:~/buildouts$ svn co http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/renasen/cenditel.multimedia/buildout/plone/3.3/ cenditelmultimedia
    usuario@equipo:~/buildouts$ cd cenditelmultimedia
    usuario@equipo:~/buildouts/cenditelmultimedia$ ls 
    bootstrap.py  buildout.cfg  cenditelmultimedia.cfg  contenttypes.cfg  dumped-versions.cfg  dumpedversions.cfg  prerequemients.cfg  versions.cfg

El primer comando es el encargado de crear un directorio para nuestros proyectos
buildout, el segundo comando abre dicho directorio pero la magia realmente se encuentra
en el tercero, el cual es el encargado de descargar del repositorio `subversion`_
los scripts listados por el cuarto comando.

.. _subversion: http://subversion.apache.org/

Para saber un poco más acerca de scripts listados, seran explicados a continuación.

bootstrap.py:
"""""""""""""

Es un script python, encargado de realizar la descarga y construcción de un
ambiente de desarrollo buildout para sitios Web basados en Zope/Plone

buildout.cfg:
"""""""""""""

Archivo de configuración que posee las características necesarias para la construcción
de un sitio Web basado basíco en el sistema manejador de contenidos Plone.

cenditelmultimedia.cfg:
"""""""""""""""""""""""

Posee las configuraciones del Producto File System Storage para Plone, usando
el recipe de configuración `iw.recipe.ffs <http://pypi.python.org/pypi/iw.recipe.fss>`_, para un sitio llamado ``justvideos``
que es creado en otra sección usando el recipe `collective.recipe.plonesite <http://pypi.python.org/pypi/collective.recipe.plonesite>`_  el cual instala
los productos vinculados al desarrollo que serán mencionados más adelante

contenttypes.cfg:
"""""""""""""""""
Utiliza el recipe buildout `plone.recipe.atcontenttypes <http://pypi.python.org/pypi/plone.recipe.atcontenttypes>`_ para limitar el tamaño máximo
de los tipos de contenido ATImage, ATFile y ATNewsItem; además de la calidad de imagen de los ATImage.

dumped-versions.cfg:
""""""""""""""""""""
Recibe los valores de versión de las dependencias instaladas por los distintos recipes.
Es creado usando el recipe ``buildout.dumppickedversions``

dumpedversions.cfg:
"""""""""""""""""""
Contiene el recipe `buildout.dumppickedversions <http://pypi.python.org/pypi/buildout.dumppickedversions>`_ el cual crea al archivo dumped-versions.cfg

prerequemients.cfg:
"""""""""""""""""""
Usa al recipe `plone.recipe.command <http://pypi.python.org/pypi/plone.recipe.command>`_ para crear directorios necesarios para el producto `File Sistem Storage <http://plone.org/products/filesystemstorage>`_ 

versions.cfg:
"""""""""""""


Segundo paso:
^^^^^^^^^^^^^

Instale una jaula de python2.4 en su sistema para evitar daños a su sistema operativo.
Proceda como se señala a continuación.

.. code-block:: console

    usuario@equipo:~$ sudo aptitude install python2.4 python2.4-minimal python2.4-dev python-virtualenv python-setuptools 
    usuario@equipo:~$ virtualenv -p python2.4 py2.4/
    usuario@equipo:~$ cd py2.4/
    usuario@equipo:~/py2.4$ source bin/activate
    usuario@equipo:~/py2.4$ cd
    usuario@equipo:~$ cd buildouts/cenditelmultimedia
    usuario@equipo:~/buildouts/cenditelmultimedia$ python bootstrap.py
    
El primer comando, instala las dependencias python en el sistema operativo. Si
usted se encuentra bajo el sistema operativo Debian Lenny o Ubuntu Karmic Koala,
no tendrá problemas de dependencias. El segundo comando, crea una jaula virtual
de python en su directorio de usuario llamada py2.4, con el tercer comando entramos a ella,
para activarla usamos el cuarto comando, los siguientes comandos nos llevan al
entorno de desarrollo allí llamamos al interprete de python para que ejecute al
archivo bootstrap.py; el cual nos dará una salida como:

.. code-block:: console

    Downloading http://pypi.python.org/packages/source/d/distribute/distribute-0.6.14.tar.gz
    Extracting in /tmp/tmpIUY_yz
    Now working in /tmp/tmpIUY_yz/distribute-0.6.14
    Building a Distribute egg in /tmp/tmptWrUVV
    /tmp/tmptWrUVV/distribute-0.6.14-py2.4.egg
    Creating directory '/home/victor/buildouts/tutorial/bin'.
    Creating directory '/home/victor/buildouts/tutorial/parts'.
    Creating directory '/home/victor/buildouts/tutorial/eggs'.
    Creating directory '/home/victor/buildouts/tutorial/develop-eggs'.
    Getting distribution for 'zc.buildout==1.4.3'.
    Got zc.buildout 1.4.3.
    Generated script '/home/victor/buildouts/tutorial/bin/buildout'.

Tercer Paso:
^^^^^^^^^^^^
Luego, nos dirigimos al directorio src que acaba de ser creado, y realizamos la
descarga de los productos que serán utilizados usando los siguientes comandos:

.. code-block:: console

    usuario@equipo:~/buildouts$ svn co http://plataforma.cenditel.gob.ve/browser/proyectosInstitucionales/renasen/cenditel.multimedia/trunk cenditel.multimedia
    usuario@equipo:~/buildouts$ svn co http://plataforma.cenditel.gob.ve/browser/proyectosInstitucionales/renasen/cenditel.multimediapanel/trunk cenditel.multimediapanel
    usuario@equipo:~/buildouts$ svn co http://plataforma.cenditel.gob.ve/browser/proyectosInstitucionales/renasen/cenditel.multimediaplayertheme/trunk cenditel.multimediaplayertheme

A continuación, podemos proceder a realizar la instalación del sitio de demostración.
Para eso, ejecutaremos el siguiente comando.

.. code-block:: console

    usuario@equipo:~/buildouts/cenditelmultimedia$ ./bin/buildout -vc cenditelmultimedia.cfg

El comando, lee el archivo de configuración ``cenditelmultimedia.cfg``, que se puede leer a continuación:

.. code-block:: console
    
    # Buildout Configuration File for cenditel.multimedia 
    [buildout]
    
    extends = contenttypes.cfg
    parts +=
        plonesite
        fss        
    
    
    ############################################
    # Eggs
    #
    eggs += cenditel.multimedia
            cenditel.multimediapanel
            cenditel.multimediaplayertheme
          
    
    zcml += 
    
    ############################################
    # Development Eggs
    #
    develop += src/cenditel.multimedia
               src/cenditel.multimediapanel
               src/cenditel.multimediaplayertheme
    
    [instance]
    eggs +=
        iw.fss
        collective.monkeypatcher
    
    #effective-user = victor
    Plone-user=victor
    
    # This recipe is to create and update a plone site.
    # For options see http://pypi.python.org/pypi/collective.recipe.plonesite
    [plonesite]
    recipe = collective.recipe.plonesite
    
    # id for a Plone site
    site-id = justvideos
    
     
    instance = instance
    
    # 
    #profiles-initial = my.package:initial
    profiles =
         iw.fss:default
         cenditel.multimedia:default
         cenditel.multimediapanel:default
         cenditel.multimediatheme:default
         
    #post-extras =
    #    ${buildout:directory}/my_script.py
    #
    #pre-extras =
    #    ${buildout:directory}/my_other_script.py

    # This recipe to configure File System Storage.
    # For options see http://pypi.python.org/pypi/iw.recipe.fss

    [fss]
    recipe = iw.recipe.fss
    # Filesystem path for the configuration file. Need the complete path to the file.
    #conf = ${zopeinstance:location}/etc/plone-filesystemstorage.conf
    
    # List of filesystem paths for standalone zope instances or ZEO client instances. One path by line.
    zope-instances=
        ${instance:location}
    
    # List of FSS configurations for your buildout.
    # The first line is for the global configuration.
    # Following lines are by zope path specific configurations.
    storages =
        global / flat
    
    # Para cynin
    #    pone_flat /cynin site2 /home/${instance:effective-user}/public_html/
    #    other_site /cynapse site2 /home/${instance:effective-user}/public_html/filesystemstorage
    
    # Para Plone 3.3.5
        plone_flat /justvideos site2 /home/${instance:Plone-user}/justvideos

El archivo de configuración, se divide en las siguientes secciones:

Instance:
"""""""""
En esta sección se declaran las variables de configuración ``extends``, ``parts``, ``eggs`` y ``develop`` que explicaremos a continuación:

* ``extends`` : Apunta al archivo de configuración que presede al archivo actual cenditelmultimedia.cfg, para mayor información revise la documentación de buildout.
* ``parts`` : En esta sección se declaran las otras secciones que serán parte del documento.
* ``eggs`` : Son los paquetes python que se instalaran en el servidor Zope/Plone al ser ejecutado el script buildout.
* ``develop`` : apunta al directorio y nombre de paquete que deben ser desarrollados por buildout.


Plonesite:
""""""""""
Esta sección usa al recipe `collective.recipe.plonesite <http://pypi.python.org/pypi/collective.recipe.plonesite>`_
para crear un sitio Plone básico. La variable ``site-id`` es el identificador del
sitio creado, la variable ``instance`` le indica al recipe la instancia Zope/Plone
que debe utilizar, la variable ``profiles`` indica al servidor que al momento de
crear el sitio instale los paquetes señalados usando el perfil de GenericSetup especificado.
Para mayor información acerca de las variable y configuraciones que adminte el recipe,
visite la pagina de documentación oficial en `pypi <http://pypi.python.org/pypi/collective.recipe.plonesite>`_


FSS:
""""



