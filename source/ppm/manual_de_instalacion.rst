.. highlight:: rest

.. _instalación:

Manual de Instalación
---------------------


PPM (Portafolio Project Manamegent) Es un producto para Plone
el cual ayuda a determinar la combinación óptima y la secuencia
de los proyectos propuestos para lograr los mejores objetivos
y así describir los métodos para el análisis y la gestión
colectiva de un grupo de proyectos

Para instalar el producto es necesario Un sitio Plone 3

A continuación veremos los pasos para replicar
el ambiente de desarrollo:


Primer Paso:
^^^^^^^^^^^^
Descargar de la pagina Web del Proyecto el script de instalación buildout que le
permitira configurar un sitio.

Para realizar la descarga proceda en un terminal con los siguientes comandos:

.. code-block:: console

    usuario@equipo:~$ mkdir buildouts
    usuario@equipo:~$ cd buildouts
    usuario@equipo:~/buildouts$ svn co http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/eGov/ppm/buildout/plone/3.3 PPM
    usuario@equipo:~/buildouts$ cd PPM
    usuario@equipo:~/buildouts/PPM ls
    bootstrap.py  buildout.cfg  ppm.cfg
    
El primer comando es el encargado de crear un directorio para nuestros proyectos
buildout, el segundo comando abre dicho directorio , el tercero es el encargado de descargar del repositorio
lo necesario para instalar nuestro producto

Para saber un poco más acerca de scripts listados, serán explicados a continuación.

bootstrap.py:
"""""""""""""

Es un script python, encargado de realizar la descarga y construcción de un
ambiente de desarrollo buildout para sitios Web basados en Zope/Plone

buildout.cfg:
"""""""""""""

Archivo de configuración que posee las caracteristicas necesarias para la construcción
de un sitio Web basado basíco en el sistema manejador de contenidos Plone.

ppm.cfg:
""""""""

Contiene las configuraciónes del Producto y productos adicionales que necesita PPM para poder instalarlo


Instale una jaula de python2.4 en su sistema para evitar daños a su sistema operativo.
Proceda como se señala a continuación.

.. code-block:: console

    usuario@equipo:~$ sudo aptitude install python2.4 python2.4-minimal python2.4-dev python-virtualenv python-setuptools 
    usuario@equipo:~$ virtualenv -p python2.4 py2.4/
    usuario@equipo:~$ cd py2.4/
    usuario@equipo:~/py2.4$ source bin/activate
    usuario@equipo:~/py2.4$ cd
    usuario@equipo:~$ cd buildouts/PPM
    usuario@equipo:~/buildouts/PPM$ python bootstrap.py

El primer comando, instala las dependencias python en el sistema operativo. Si
usted se encuentra bajo el sistema operativo Debian Lenny o Ubuntu Karmic Koala,
no tendrá problemas de dependencias. El segundo comando, crea una jaula virtual
de python en su directorio de usuario llamada py2.4, con el tercer comando entramos a ella,
para activarla usamos el cuarto comando, los siguientes comandos nos llevan al
entorno de desarrollo allí llamamos al interprete de python para que ejecute al
archivo bootstrap.py; el cual nos dará una salida como:


Segundo Paso:
^^^^^^^^^^^^^

A continuación, podemos proceder a realizar la instalación del sitio.
Para eso, ejecutaremos el siguiente comando.

.. code-block:: console

    usuario@equipo:~/buildouts/PPM$ ./bin/buildout -vc ppm.cfg
    
Este comando descarga automáticamente todas las dependencias de PPM y las pone en los
lugares correspondientes e instala Plone 3.3


Tercer Paso:
^^^^^^^^^^^^

Ya con Plone instalado y descargado los productos necesarios solo queda subir la instancia de plone, ir a agregar
Productos e instalar ppm y sus dependencias 



Dependencias que usa PPM
------------------------

DataGridField
=============

Un componente de entrada de la tabla para Plone. Utiliza
Javascript para hacer la introducción de datos tabulares
más de proceso de usuario amigable - no hay ida y vuelta
peticiones HTTP al servidor al insertar o eliminar filas.

http://plone.org/products/datagridfield

Poi
===

Poi es un producto de seguimiento de incidencias para Plone.

su objetivo es ser sencillo y atractivo, proporcionando
la cuestiónes más necesarias para el seguimiento de funcionalidades.
 
http://plone.org/products/poi


Quills:
=======

Quills es un weblog para Plone. Se ha diseñado desde cero para trabajar
bien y ofrecer funciones especializadas para una multi-blog, el medio
ambiente multi-usuario.

http://plone.org/products/quills


Ploneboard:
===========

Ploneboard es un producto para Plone su objetivo es poner el comportamiento de
un foro de debate en un sitio Plone.

http://plone.org/products/ploneboard


CPFCKTemplates:
===============

Con el producto CPFCKTemplates, puede agregar una plantilla FCKeditor como un contenido de
Plone. Cada usuario verá el "habilitado " las plantillas que se encuentran en el catálogo,
es decir, sólo las plantillas que el usuario tiene permiso para ver.

http://www.communesplone.org/support/documentation/manual/produit-de-gestion-des-modeles-fckeditor/referencemanual-all-pages
