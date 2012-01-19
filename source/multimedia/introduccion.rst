.. highlight:: rest

.. _introduccion_multimedia:

============
Introducción
============

Esta es la documentación del producto ``cenditel.multimedia`` para el sistema
manejador de contenidos Plone. En las siguientes paginas encontrará material
referente al su proceso de instalación usando la herramienta ``buildout``,
la instalación y configuración de sus dependencias tanto en el sistema manejador
de contenidos Plone y la suite de participación Web cyn.in. En todos los casos,
presentados en el siguiente manual, se entiende que usted esta corriendo una
versión de python 2.4 en un sistema operativo Debian Lenny o Ubuntu 9.10 Karmic Koala.


Componentes
-----------

Los productos multimedia de Cenditel se componente en los siguientes módulos:

cenditel.audio
""""""""""""""

Este producto proporciona un tipo de contenido para que archivos de audio
puedan ser agregados al Sistema Manejador de contenidos Plone permitiendo su
streaming a través de la Web previa reconversión a formatos libres.

cenditel.video
""""""""""""""

Este producto proporciona un tipo de contenido para que archivos de vídeo
puedan ser agregados al Sistema Manejador de contenidos Plone permitiendo su
streaming a través de la Web previa reconversión a formatos libres.

cenditel.multimediaplayertheme
""""""""""""""""""""""""""""""

Este producto proporciona un piel para el reproductor html5 por defecto de los
navegadores permitiendo una vista standart para cada uno de ellos. Se basa en la
libreria javascript jMediaElement de Alexader Farkas disponible en:
`http://www.protofunc.com/jme/ <http://www.protofunc.com/jme/>`_

cenditel.transcodedeamon
""""""""""""""""""""""""

Este producto proporciona un panel de configuración para los productos cenditel.video
y cenditel.audio, además permite configurar la códificación de archivos a formatos libres
prestando el servicio de codificación mediante una cola que sigue la disciplina
primero en entrar, primero en salir. 




