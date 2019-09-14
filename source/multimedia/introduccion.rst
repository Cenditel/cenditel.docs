.. highlight:: rest

.. _introduccion_multimedia:

============
Introducción
============

Esta es la documentación de los productos multimedia de 
la fundación Cenditel para el sistema administración de 
contenidos Plone. 

En las siguientes páginas encontrará material referente al 
su proceso de instalación usando la herramienta ``buildout``,
la instalación y configuración de sus dependencias tanto en 
el sistema administración de contenidos Plone y la herramienta 
cyn.in. En todos los casos, presentados en el siguiente manual, 
se entiende que usted esta corriendo una versión de Python 2.4 
en un sistema operativo Debian Lenny, en su defecto en una 
distribución basada en esta.


Componentes
-----------

Los productos multimedia de Cenditel se componente en los 
siguientes módulos:

cenditel.audio
""""""""""""""

Este producto proporciona un tipo de contenido para que archivos 
de audio puedan ser agregados al sistema administración de contenidos 
Plone permitiendo su Streaming a través de la Web previa conversión 
a formatos libres.

cenditel.video
""""""""""""""

Este producto proporciona un tipo de contenido para que archivos 
de vídeo puedan ser agregados al sistema administración de contenidos 
Plone permitiendo su Streaming a través de la Web previa conversión 
a formatos libres.

cenditel.transcodedaemon
""""""""""""""""""""""""

Este producto proporciona un panel de configuración de servicio de 
conversión de formatos multimedia para los productos ``cenditel.video`` 
y ``cenditel.audio``, en el cual se permite definir los parámetros de 
conversión que usa la herramienta FFMPEG. Prestando el servicio de 
conversión mediante una cola que sigue la disciplina primero en entrar, 
primero en salir. 

cenditel.multimediaplayertheme
""""""""""""""""""""""""""""""

Este producto proporciona un piel para el reproductor HTML5 por defecto 
de los navegadores permitiendo una vista entandar para cada uno de ellos. 
Se basa en la librería javascript `jMediaElement <http://protofunc.com/jme/>`_ 
de *Alexader Farkas*.
