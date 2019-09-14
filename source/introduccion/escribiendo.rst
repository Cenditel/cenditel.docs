.. -*- coding: utf-8 -*-

===========================================
 Escribiendo y actualizando este documento
===========================================

.. contents :: :local: 

.. admonition:: Descripción

        Como escribir y enviar mejoras al Manual de Productos Plone en la Fundación Cenditel.

Obtener y compilar la documentación
===================================

El almacenamiento de este material está disponible en el servidor de Subversion
`"Plataforma colaborativa" <http://plataforma.cenditel.gob.ve/svn/plataforma/>`_ de los contribuyentes a 
Plone. Si usted tiene una credenciales en este servidor y desea convertirse en 
un colaborador ejecute el siguiente comando:

.. code-block:: sh

  $ svn co http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/renasen/cenditel.documentation/buildout cenditel-docs

Si usted no tiene las credenciales de acceso al repositorio SVN 
`"Plataforma colaborativa" <http://plataforma.cenditel.gob.ve/svn/plataforma/>`_ 
de Plone o simplemente solo desea obtener y compilar esta documentación ejecute 
el siguiente comando:

.. code-block:: sh

  $ svn export http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/renasen/cenditel.documentation/buildout cenditel-docs

Crear entorno virtual de Python para reconstruir este proyecto:

.. code-block:: sh

  # aptitude install python-setuptools subversion
  # easy_install virtualenv
  # exit
  $ cd $HOME ; mkdir $HOME/virtualenv ; cd $HOME/virtualenv
  $ virtualenv --no-site-packages --python=/usr/bin/python sphinx
  $ cd -

Ahora puede generar la documentación de HTML, con los siguiente comandos:

.. code-block:: sh

  $ source virtualenv/sphinx/bin/activate
  (sphinx)$ cd cenditel-docs/
  (sphinx)$ python bootstrap.py
  (sphinx)$ ./bin/buildout -vN
  (sphinx)$ ./bin/sphinx

Ahora se puede abrir ``cenditel-docs/build/html/index.html`` desde 
su navegador Web favorito.

Para obtener la documentación en PDF:

.. code-block:: sh

  $ source virtualenv/sphinx/bin/activate
  (sphinx)$ cd ./cenditel-docs/build
  (sphinx)$ make latex
  (sphinx)$ cd ./latex
  (sphinx)$ make all-pdf

Ahora se puede abrir ``cenditel-docs/sphinx/build/latex/DocumentacionEspanolPlone.pdf`` 
con sus programas de visor de PDF favorito (Evince, Acrobat Reader, ...)


Reglas de redacción
===================

En primer lugar, debe aprender los `fundamentos de Sphinx
<http://www.sphinx-doc.org/en/master/>`_ que es un reStructuredText extendido.


Codificación de caracteres
==========================

Su editor debe codificar el texto en **utf-8** si le gusta lo que está leyendo. 
Si su editor de texto favorito no reconoce esta codificación 
(en la actualidad, eso es bien extraño), entonces cambie de editor de texto.

.. admonition::
   Truco

   Para ``vi``, ``emacs`` y algunos otros editores de texto soportan
   utf-8 de forma automática al abrir un archivo de Sphinx, el lugar en
   primera línea de la siguiente marca (como en este archivo)::

     .. -*- coding: utf-8 -*-


Desplazamientos y indentaciones
===============================

El uso del carácter de tabulación en el texto fuente para las distintas
desplazamientos y indentaciones está **estrictamente prohibido**. Utilice siempre
espacios para este fin. Todos los editores de texto ofrecen opciones avanzadas
para insertar espacios al pulsar la tecla TAB. No tiene
excusa si es necesario.

Estilos de subrayado
====================

Sphinx y ReStructuredText no imponer estilo de subrayado para
diferentes niveles de secciones de un documento. Todo se deja a la discreción
editores. Para mantener la coherencia nosotros adoptamos la siguiente convención: ::

  ==============================================
  Titulo de capitulo (uno solo por cada archivo)
  ==============================================
  ...
  Sección del nivel 1
  ===================
  ...
  Sección del nivel 2
  -------------------
  ...
  Sección del nivel 3
  ...................
  ...
  Sección del nivel 4
  ~~~~~~~~~~~~~~~~~~~

No es necesario ni deseable ir más allá del nivel 4. Cuando la generación del 
documento allá completado, el nivel de las secciones básicas de un archivo
depende del nivel de anidamiento del archivo en la estructura general de
documento. Para generar el HTML, no es un problema, pero en LaTeX limita
la superposición de las secciones a 6 niveles.

Contribuciones SVN
==================

Wow, estás contento con tu excelente trabajo. Y le gustaría compartirlo con
todo el mundo. Al igual que cuando "contribuidor" de código fuente, las pruebas
unitarias no deben mostrar ningún error, compruebe en primer lugar:

* Que el comando ``make html`` no genere ningún error o advertencia.
* Que su redacción no posea ningún error de ortografía.
* Los enlaces de hipertexto que se ha agregado o cambiado (glosario, enlaces
  externos explícitos, referencias a las secciones, ...) funcionan correctamente.

Imágenes
========

Aparte de las capturas de pantalla - ¡Uy, lo siento - las capturas de pantalla!, 
las imágenes Sphinx se inserta en el documento debe ir acompañada de su versión
"Fuente" en un formato público interoperables, y para que el editor pueda abrir
el archivo fuente que este disponible. Las imágenes deben estar preferentemente en el formato
PNG.

Además, durante cada inserción o cambio de imagen, usted **debe**
verificar y ajustar si es necesario la representación PDF, a sabiendas de las limitaciones
la imagen a tamaño del papel final.

**Ejemplo :** ::

   .. gs-map.mm: imagen de mapa mental de los servicios de GenericSetup. Creado con FreeMind

   .. image:: gs-map.png

**Aplicaciones gráficas recomendadas**

Diagramas : `Graphviz <http://www.graphviz.org/>`_


Algunas de las herramientas recomendadas
========================================

Emacs: usted puede agregar a emacs el módulo `rst.el
<http://docutils.sourceforge.net/tools/editors/emacs/rst.el>`_
que añade un par de comandos y la sintaxis de la documentación a los escritores 
simpatizantes de Sphinx y reStructuredText.


FAQ
===

**Pregunta :** He añadido una entrada del índice o un nuevo término en el glosario y
no se actualiza cuando compilo el documento.

**Respuesta :** El índice de Sphinx es a veces es desorientado y la gestión de la dependencia
a veces, mejor. Por lo tanto, todo se debe reiniciar ejecutando el comando ``make clean`` 
dentro del directorio ``cenditel-docs/sphinx/build/``.
