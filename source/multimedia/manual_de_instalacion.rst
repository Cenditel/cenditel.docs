.. highlight:: rest

.. _ManualdeInstalacion:

===========
Instalación
===========

El manual de Instalación de los productos cenditel.audio y cenditel.video cuenta básicamente con dos partes:

* Instalación en Instancias Zope Plone 3.3.5
* Instalación en Instancias Cyn.in 3.1.3


Primera Parte Instalación en Instancias Zope Plone 3.3.5
========================================================

Para instalar el producto cenditel.multimedia usted necesita solventar las
siguientes dependencias en su instancia Plone/Zope

* Un sitio Plone 3.3.5 configurado con el producto File System Storage usando la estrategia de almacenamiento "site2".
* Un servidor web nginx, con una configuración especifica en mimetypes, que permitirá el streaming a partir de este.

A continuación veremos los pasos necesarios para replicar el ambiente de desarrollo:

Primer Paso
-----------

Descargar de la pagina Web del Proyecto el script de instalación buildout que le permitirá configurar un sitio demostrativo.
Para realizar la descarga proceda en un terminal con los siguientes comandos:

.. code-block:: console

    $ mkdir buildouts
    $ cd buildouts
    $ svn co http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/renasen/cenditel.multimedia/buildout/plone/3.3/ cenditelmultimedia
    $ cd cenditelmultimedia
    $ ls -p
    00-varibles.cfg           06-contenttypes.cfg     plonesite.cfg
    01-dumpedversions.cfg     bootstrap.py            products/
    02-mrdeveloper.cfg        buildout.cfg            src/
    03-prerequemients.cfg     cenditelmultimedia.cfg  templates/
    04-mountpoint.cfg         dumped-versions.cfg     versions.cfg
    05-mediafilesstorage.cfg  etc/

El primer comando es el encargado de crear un directorio para nuestros proyectos
buildout, el segundo comando abre dicho directorio pero la magia realmente se encuentra
en el tercero, el cual es el encargado de descargar del repositorio `subversion`_
los scripts listados por el cuarto comando.

.. _subversion: http://subversion.apache.org/

Para saber un poco más acerca de scripts listados, serán explicados a continuación.

bootstrap.py
^^^^^^^^^^^^

Es un script python, encargado de realizar la descarga y construcción de un
ambiente de desarrollo buildout para sitios Web basados en Zope/Plone

buildout.cfg
^^^^^^^^^^^^

Archivo de configuración que posee las características necesarias para la construcción
de un sitio Web basado básico en el sistema manejador de contenidos Plone.

00-varibles.cfg
^^^^^^^^^^^^^^^

Como su nombre lo indica, contiene las variables a ser utilizadas por el sistema
de instalación buildout para la reconstrucción del sitio de pruebas.

Se divide en cuatro partes:

* buildout: Posee la definición de las variables de extensión del producto al momento de ser ejecutado el script, es decir indica el orden de ejecución, para eso usa la variable ``extends=``, además declara la variable ``site-id`` con un nombre de sitio que va a ser usado más adelante.

* zopeserver: Contiene configuraciones referentes al servidor de aplicaciones Zope.
    * La primera variable de esta parte es la variable ``user`` que indica el nombre de usuario y contraseña del usuario admin del servidor con las configuraciones por defecto.
    * La segunda variable ``effective-user`` corresponde al usuario Unix del servidor.
    * La tercera variable ``host`` es una variable correspondiente a la dirección IP del servidor Web.
    * La cuarta variable ``debug-mode`` indica si el servidor se encuentra en modo de depuración, por defecto se encuentra en off.
    * La quinta variable, ``verbose-security`` indica si se presentan informes detallados de la seguridad, por defecto se encuentra en off.
    
* hosts: Contiene las distintas variables de conexión al servidor de producción.
    * Variable ``http-address``, corresponde a la dirección del Servidor Web Zope.
    * Variable ``ftp-address``, corresponde a la dirección del Servidor FTP de Zope.
    * Variable ``webdav-address``, corresponde a la dirección del Servidor WebDav de Zope
    * Variable ``dns``, nombre del dominio producción o la dirección IP
    * Variable ``user``, corresponde al usuario de servicios ssh que se conectara al Hosting del servidor.
    * Variable ``password``, corresponde a la contraseña del servicio ssh para conectarse al Hosting de servidor
    
* ports: Contiene las variable de los distintos puertos para los diferentes servicios.
    * Variable ``http-address``, contiene el puerto de entrada a la aplicación http.
    * Variable ``ftp-address``, contiene el puerto de entrada a la aplicación mediante ftp.
    * Variable ``webdav-address``, contiene el puerto de entrada a la aplicación mediante servicios WebDAV.

01-dumpedversions.cfg
^^^^^^^^^^^^^^^^^^^^^

Contiene el récipe `buildout.dumppickedversions <http://pypi.python.org/pypi/buildout.dumppickedversions>`_ el cual crea al archivo dumped-versions.cfg
que contiene la lista de productos instalados y sus respectivas versiones. Se actualiza cada vez que se ejecuta buildout.

02-mrdeveloper.cfg
^^^^^^^^^^^^^^^^^^

Consta de la sección buildout y la sección sources, en la primera es declarada la variable ``extends`` que
permite la extensión de las configuraciones a partir del archivo 01-dumpedversions.cfg. Por otro lado
agrega la extensión para buildout `mr.developer <http://pypi.python.org/pypi/mr.developer>`_ 

El récipe mr.developer admite las siguientes variables de configuración:

* sources-dir: Indica el directorio donde serán descargados los distintos productos, por defecto es ``src``.
* sources: Indica el nombre de la sección donde serán indicados los paquetes a descargar.
* always-check: Especifica el nombre de los archivos a los cuales siempre que buildout se ejecute se le realizará check out.
* auto-checkout: Especifica el nombre de los archivos a los cuales siempre que buildout se ejecute se le realizará check out.

Por otro lado, la sección sources se encuentra vacía porque aún no es necesaria su utilización.

03-prerequemients.cfg
^^^^^^^^^^^^^^^^^^^^^

Este Script cuenta de las siguientes partes: pre-requemients, make-fss-directory, vhost-nginx, mime-types-nginx, config-nginx.

* pre-requemients: Usa el recipe `plone.recipe.command <http://pypi.python.org/pypi/plone.recipe.command>`_ el cual es utilizado para lanzar el comando de instalación necesario para instalar nginx y ffmpeg, mediante la variable ``command``. 
* make-fss-directory: Usa el recipe `plone.recipe.command <http://pypi.python.org/pypi/plone.recipe.command>`_ , con el cual se crean los directorios necesarios para el producto `File Sistem Storage <http://plone.org/products/filesystemstorage>`_ y para la creación de archivos de configuración del servidor nginx. Además de los comandos lanzados con ``command`` utiliza las siguientes variables:
    * update-command: Esta variable, es utilizada cuando buildout es ejecutado pero la parte no ha sido alterada.
    * stop-on-error: Cuando el valor es yes, no o true. Buildout detiene su ejecución si un comando recibe un valor de salida cero.
* vhost-nginx: Usa el recipe `collective.recipe.template <http://pypi.python.org/pypi/collective.recipe.template>`_, mediante este, se crea una template de ejemplo que va a ser utilizada por el servidor nginx para realizar el servicio de streaming.
* mime-types-nginx: Usa el recipe `collective.recipe.template <http://pypi.python.org/pypi/collective.recipe.template>`_ para crear un archivo de configuración de mimetypes para el servidor web nginx.
* config-nginx: Usa el recipe `plone.recipe.command <http://pypi.python.org/pypi/plone.recipe.command>`_ y con los comandos, crea enlaces simbólicos, verifica la configuración del servidor web nginx y además recarga la configuración.
    * update-command: Esta variable, es utilizada cuando buildout es ejecutado pero la parte no ha sido alterada.
    * stop-on-error: Cuando el valor es yes, no o true. Buildout detiene su ejecución si un comando recibe un valor de salida cero.

04-mountpoint.cfg
^^^^^^^^^^^^^^^^^

Este archivo de configuración, crea punto de montaje en la para un sitio web basado en Plone de manera tal,
que se permitan Bases de Datos separadas para cada sitio Plone. Para mayor información puede visitar este `link <http://plone.org/documentation/kb/multiple-plone-sites-per-zope-instance-using-separate-data-fs-files-for-each-one>`_


05-mediafilestorage.cfg
^^^^^^^^^^^^^^^^^^^^^^^

Este script tiene las configuraciones necesarias para el manejo de los archivos de audio y vídeo, a
nivel del disco duro. Consta de cuatro secciones:

* buildout: Se declara la variable extends, y se indica que este script continua con las configuraciones a partir del archivo 04-mountpoint.cfg. Y se declara la adición de la parte fss.

* instance: agrega eggs python necesarios para la configuración del servidor Zope de manera que este use el sistema de archivos.

* fss: Utiliza el recipe `iw.recipe.ffs <http://pypi.python.org/pypi/iw.recipe.fss>`_, el récipe consta de las siguientes variables:
    * zope-instances: Por defecto tiene asignado el valor ``${instance:location}``
    * storage: En esta variable se indica los lugares donde serán colocados los distintos archivos, consiste en tres configuraciones:
        * global: Explica el tipo de almacenamiento global para todos los sitios.
        * Almacenamiento específico para cada sitio: Después de la linea global se pueden declarar estrategias de almacenamiento específicas para cada sitio. Para ello se sigue la sintaxis:

             plone_flat /sitename site2 path/to/storage
             
             donde:
             
             * plone_flat: es un alias para la configuración.
             * sitename: Es el nombre de un sitio que se encuentra en el root de la ZMI
             * site2: Es la configuración de almacenamiento para el sitio.
             * path/to/storage: Es el sitio en el disco duro donde iw.fss colocará los archivos que vienen de la ZODB.

* versions: Especifica versiones especificas que son necesarias para la instalación del sistema.

06-contenttypes.cfg
^^^^^^^^^^^^^^^^^^^

Extiende del archivo de configuración 05-mediafilestorage.cfg, además en este archivo es declarada una parte llamada ``contenttypes-conf``
que utiliza el recipe `plone.recipe.atcontenttypes <http://pypi.python.org/pypi/plone.recipe.atcontenttypes>`_ en esta configuración
la variable ``max-file-size`` especifica el tamaño máximo que los tipos de contenido  pueden tener dentro de los sitios plone, la variable ``max-image-dimension``
específica la resolución máxima en pixeles, para las imágenes de los contenidos de noticias y para las imágenes. Por ultimo,
la variable ``pil-quality`` señala, la calidad con que serán guardadas las imágenes.

cenditelmultimedia.cfg
^^^^^^^^^^^^^^^^^^^^^^

Extiende del archivo de configuración 06-contenttypes.cfg, posee las siguientes variables:

* auto-checkout: Declara los eggs a los cuales el recipe mr.developer mencionado previamente realizará un check out.
* eggs: Indica al script buildout cuales paquetes de tipo huevo python debe descargar para instalación.
* zcml: Indica a buildout, cuales paquetes de tipo huevo python deben ser configurados en base a archivos de configuración zcml.

Además contiene la parte de la declaración de los paquetes a los cuales se les realizará un check out para la instalación de los mismos
en la instancia Zope, es decir la parte sources que fue previamente mencionada en el archivo 02-mrdeveloper.cfg.

plonesite.cfg
^^^^^^^^^^^^^

Extiende del archivo de configuración cenditelmultimedia.cfg. Utiliza el récipe `collective.recipe.plonesite <http://pypi.python.org/pypi/collective.recipe.plonesite>`_
aceptando las siguientes variables de configuración:

* site-id: Nombre del sitio de ejemplo creado con el récipe.
* intance: Corresponde al nombre de la instancia que esta corriendo el script, por defecto ``instance``.
* profiles: Corresponde a una lista de perfiles de GenericSetup que se ejecutaran cada vez que se ejecute el script buildout.

templates
^^^^^^^^^

Este directorio contiene modelos de archivos de configuración que son modificados en base
a las variables declaradas en el archivo 00-variables.cfg, permitiendo replicar configuraciones para el servidor nginx.

products
^^^^^^^^

Corresponde al directorio **products** creado por bootstrap.py.

src
^^^

Es el directorio de instalación donde serán colocados los archivos en desarrollo. En este caso, el récipe
mr.developer coloca aquí dichos archivos. 

etc
^^^

En este directorio, son colocados los archivos de salida generados a partir del récipe de `collective.recipe.template <http://pypi.python.org/pypi/collective.recipe.template>`_

Segundo paso
------------

Instale una jaula de python2.4 en su sistema para evitar daños a su sistema operativo.
Proceda como se señala a continuación.

.. code-block:: console

    $ sudo aptitude install python2.4 python2.4-minimal python2.4-dev python-virtualenv python-setuptools 
    $ virtualenv -p python2.4 python2.4/
    $ cd python2.4/
    $ source bin/activate
    (python2.4)$ cd $HOME/buildouts/cenditelmultimedia
    (python2.4)$ python bootstrap.py
    
El primer comando, instala las dependencias python en el sistema operativo. Si
usted se encuentra bajo el sistema operativo Debian Lenny o Ubuntu Karmic Koala,
no tendrá problemas de dependencias. El segundo comando, crea una jaula virtual
de python en su directorio de usuario llamada python2.4, con el tercer comando entramos a ella,
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

Tercer Paso
-----------

.. code-block:: console

    (python2.4)$ ./bin/buildout -vNc plonesite.cfg

Al realizar esto, buildout ejecutará las configuraciones necesarias en el sitio para instalar los productos. A continuación vamos a ver
como configurar el resto de la aplicación. 