.. highlight:: rest

.. _instalación:

Instalación
-----------


PPM (Portafolio Project Manamegent), es un producto para Plone
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
permitirá configurar un sitio.

Para realizar la descarga proceda en un terminal con los siguientes comandos:

.. code-block:: console

    $ mkdir buildouts ; cd buildouts
    $ svn co http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/renasen/cenditel.ppm/buildouts/plone3/ ppm.buildout
    $ cd ppm.buildout ; ls -p
    00-varibles.cfg        02-mrdeveloper.cfg  bootstrap.py  cenditel.ppm.cfg     etc/           products/  templates/
    01-dumpedversions.cfg  03-mountpoint.cfg   buildout.cfg  dumped-versions.cfg  plonesite.cfg  src/       versions.cfg
    
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

Archivo de configuración que posee las características necesarias para la construcción
de un sitio Web basado básico en el sistema manejador de contenidos Plone.

cenditel.ppm.cfg:
"""""""""""""""""

Contiene las configuraciones del Producto y productos adicionales que necesita PPM para poder instalarlo


Instale una jaula de python2.4 en su sistema para evitar daños a su sistema operativo.
Proceda como se señala a continuación.

.. code-block:: console

    $ sudo aptitude install python2.4 python2.4-minimal python2.4-dev python-virtualenv python-setuptools 
    $ virtualenv -p python2.4 python2.4/
    $ cd python2.4/
    $ source bin/activate
    (python2.4)$ cd $HOME/buildouts/ppm.buildout
    (python2.4)$ python bootstrap.py

El primer comando, instala las dependencias python en el sistema operativo. Si
usted se encuentra bajo el sistema operativo Debian Lenny o Ubuntu Karmic Koala,
no tendrá problemas de dependencias. El segundo comando, crea una jaula virtual
de python en su directorio de usuario llamada python2.4, con el tercer comando entramos a ella,
para activarla usamos el cuarto comando, los siguientes comandos nos llevan al
entorno de desarrollo allí llamamos al interprete de python para que ejecute al
archivo bootstrap.py; el cual nos dará una salida como:


Segundo Paso:
^^^^^^^^^^^^^

A continuación, podemos proceder a realizar la instalación del sitio.
Para eso, ejecutaremos el siguiente comando.

.. code-block:: console

    (python2.4)$ ./bin/buildout -vNc cenditel.ppm.cfg
    
Este comando descarga automáticamente todas las dependencias de PPM y las pone en los
lugares correspondientes e instala Plone 3.3


Tercer Paso:
^^^^^^^^^^^^

Ya con Plone instalado y descargado los productos necesarios solo queda subir la instancia de plone, ir a agregar
Productos e instalar Project Portfolio Management Framework NG y sus dependencias 


Dependencias
------------

- **DataGridField**, es un componente de entrada de la tabla para `Plone <http://plone.org/>`_. Utiliza Javascript para hacer la introducción de datos tabulares más de proceso de usuario amigable - no hay ida y vuelta peticiones HTTP al servidor al insertar o eliminar filas. Más información consulte la pagina de proyecto de `datagridfield <http://plone.org/products/datagridfield>`_. 

- **Poi**, es un producto de seguimiento de incidencias para Plone. su objetivo es ser sencillo y atractivo, proporcionando la cuestiones más necesarias para el seguimiento de funcionalidades. Más información consulte la pagina de proyecto de `poi <http://plone.org/products/poi>`_.
 
- **Quills:** es un `weblog <http://es.wikipedia.org/wiki/Weblog>`_  para `Plone <http://plone.org/>`_. Se ha diseñado desde cero para trabajar bien y ofrecer funciones especializadas para una multi-blog, el medio ambiente multi-usuario. Más información consulte la pagina de proyecto de `quills <http://plone.org/products/quills>`_.

- **Ploneboard:** es un producto para `Plone <http://plone.org/>`_ su objetivo es poner el comportamiento de un foro de debate en un sitio Plone. Más información consulte la pagina de proyecto de `ploneboard <http://plone.org/products/ploneboard>`_.

- **CPFCKTemplates:** es un producto con el que usted puede agregar una plantilla para el editor `FCKeditor <http://plone.org/products/fckeditor/>`_ como un contenido de Plone. Cada usuario verá el "habilitado " las plantillas que se encuentran en el catálogo, es decir, sólo las plantillas que el usuario tiene permiso para ver. Más información consulte su `manual de uso <http://translate.google.com/translate?sl=fr&tl=es&js=n&prev=_t&hl=es&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fwww.communesplone.org%2Fsupport%2Fdocumentation%2Fmanual%2Fproduit-de-gestion-des-modeles-fckeditor%2Freferencemanual-all-pages>`_ del producto. 
