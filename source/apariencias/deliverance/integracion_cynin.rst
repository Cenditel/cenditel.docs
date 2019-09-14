.. highlight:: rest

.. _deliverance_integración_cynin:

======================
Integración con cyn.in
======================

Se realizo una integración de ``Deliverance`` para el portal de comunidades en Cenditel que esta basado en la plataforma ``cyn.in`` versión 3.1.3 el cual esta basado en una versión de ``Plone`` 3.3.1

Para el levantamiento de información sobre los cambios que se realizarían se levanto una reunión con algunos de los usuarios del portal de comunidades con los cuales se llegaron a los siguientes acuerdos.

* La creación del botón principios políticos de la fundación Cenditel.
* La creación del botón colectivos comunitarios el cual unificaría los espacios actuales creados como lo son, Medios de comunicación popular liberadora, Renasen y proyectos comunitarios.
* El portal de comunidades en Cenditel esta basado actualmente en la plataforma Cynin, dicha plataforma contiene portlets en la cual se pueden ver las etiquetas de las publicaciones, comentarios recientes, usuarios conectados entre otros, dichos portlets serán quitados.
* Actualmente en el portal de comunidades en Cenditel se pueden agregar muchos contenidos sin embargo a petición de los usuarios se llego al acuerdo de que solo se podrán publicar, imágenes, archivos, wikis, audio y vídeo.
* En la plataforma actual la manera de agregar contenidos ya sean imágenes, archivos, vídeos, audios entre otros, es dando clic al botón Nuevo el cual se encuentra en la parte superior izquierda del portal, agregar contenidos de esta forma causa confusión a los usuarios dificultándole en ocasiones no encontrar la forma de agregar contenidos, por ende la manera de agregar imágenes, vídeos, wikis, audios y archivos serán colocadas en un menú lateral.
* Se pidió la creación de un cintillo institucional de color representativo de la misma en el cual se vea reflejado el logo de la institución.
* Bajo el cintillo institucional se quiere un menú horizontal negra la cual despliegue contenidos de forma vertical, las secciones de este menú desplegable serán: Contenidos y metodologías, Audios y vídeos, Colectivos comunitarios, Articulación y Reflexión.
* Los contenidos del espacio que actualmente es llamado Ayuda, pasaran a ser parte del espacio Contenidos y metodologías.
* Se pidió quitar las vistas de aplicación.
* Se pidió la creación de 4 cajas de texto en la cual se mostrarían las noticias más relevantes.
* Se pidió la creación de un banner o deslizador de imágenes.
* Se desea visualizar imágenes de los colectivos comunitarios que trabajan actualmente con la fundación Cenditel.

También se realizo una encuesta que serviría para evaluar algunos puntos que pudieran haber quedado fuera de discusión en la reunión.
   
.. centered:: **Encuesta Realizada a Juan Lenzo**

..
  .. figure:: ../_static/apariencia_encuesta1.png
     :align:   center
     :alt: encuesta

   **Encuesta Realizada a Ernesto Crespo**

..
  .. figure:: ../_static/apariencia_encuesta2.png
     :align:   center
     :alt: encuesta

   **Encuesta Realizada a Yuleici Verdi**

..
  .. figure:: ../_static/apariencia_encuesta3.png
     :align:   center
     :alt: encuesta

Experiencias con la Integración
===============================

Para el cumplimiento de los requerimientos hablados en la reunión se realizaron 2 diseños, la pagina de inicio, la cual contiene cintillo institucional rojo con el logo de la fundación, menú horizontal negro con contenidos desplegables en forma vertical, menú lateral el cual contiene las formas de ingresar contenidos, los principios políticos de la fundación, un deslizador de imágenes, las 4 cajas de texto con la información mas relevante y una pequeña animación en ``javascript`` la cual cambia cada 3 segundos, en ella se ven reflejados los distintos colectivos comunitarios que trabajan con la fundación.

Se realizo también un segundo diseño, destinado a mostrar los contenidos, el cual contiene cintillo institucional con logo de la institución y menú horizontal, en este diseño se incorporara por medio del servicio de ``Deliverance`` la columna 3 de la plataforma ``cyn.in`` (la columna3 de la plataforma cyn.in es aquella en la cual se muestran y se crean todos los contenidos). 

.. centered:: **Columna 3 de la plataforma cyn.in**

..
  .. figure:: ../_static/apariencia_col3.png
     :align:   center
     :alt: columna 3 de la plataforma cyn.in

Este segundo diseño se usara para añadir contenidos y mostrar información de la plataforma de comunidades en Cenditel, se decidió incorporar solo la columna3 de la plataforma actual ya que dicha columna se encuentra presente en todas las secciones de la plataforma de comunidades y se aplicaría a todas las pantallas que fueran necesarias.

**Evolución de los diseños**

Durante la fase de programación a medida que se empezó a avanzar los diseños, empezaron a evolucionar pasando por tres cambios siendo el tercer cambio el definitivo.

.. centered:: **Primer diseño realizado**

..
  .. image:: ../_static/apariencia_evolucion.png
     :align:   center
     :alt: evolucion de los diseños

.. centered:: **Segundo diseño realizado**

..
  .. image:: ../_static/apariencia_evolucion2.png
     :align:   center
     :alt: evolucion de los diseños

.. centered:: **Diseño final**

..
  .. image:: ../_static/apariencia_evolucion3.png
     :align:   center
     :alt: evolucion de los diseños

.. centered:: **Maquetación en CSS de la pagina de inicio**

..
  .. image:: ../_static/apariencia_diagramacion1.png
     :align:   center
     :alt: maquetación en CSS

**Fase de pruebas**

Durante la fase de prueba surgieron problemas con la pagina de inicio los cuales se mencionan a continuación:

* No incorporaba elementos dinámicos de la plataforma de comunidades en Cenditel.
* Era un ``HTML`` completamente estático y para su modificación había que ir directamente a modificar el código fuente del archivo lo cual no era la idea principal.
* El menú lateral daba problemas de usabilidad y accesibilidad debido a la gran cantidad de contenidos que desplegaba.
* Las 4 cajas de texto no se modificarían a menos que el administrador de la plataforma modificara el código ``HTML`` del tema.
* El programa ``Javascript`` del deslizador de imágenes daba problemas de compatibilidad con los programas de inicio del servicio de ``Deliverance`` haciendo que este no iniciara correctamente.


.. centered:: **Problema de usabilidad y accesibilidad del menú lateral**

..
  .. image:: ../_static/apariencia_problema.png
     :align:   center
     :alt: problema de usabilidad y accesibilidad

En la fase de pruebas se decidió descartar el primer diseño y se le aplicaron los cambios pertinentes al segundo diseño y al menú lateral, este menú ya no desplegara contenidos de forma horizontal y sera agregado al segundo diseño. Se decidió utilizar solo el segundo diseño para todo el contenido, como se menciono anteriormente este incorpora la columna 3 de la plataforma de comunidades la cual esta presente en todas las secciones y esta columna incorpora los elementos dinámicos necesarios para su funcionamiento tales como títulos, menús de navegación y contenidos. También incorpora el portal-breadcrumbs el cual es un elemento que permite al usuario orientarse sobre su ubicación dentro de la plataforma de comunidades.

.. centered:: **Portal Breadcrumbs**

..
  .. image:: ../_static/apariencia_breadcrumbs.png
     :align:   center
     :alt: portal bread-crumbs

.. centered:: **Diseño final**

..
  .. image:: ../_static/apariencia_disfinal.png
     :align:   center
     :alt: diseño final

.. centered:: **Maquetación en CSS del diseño final**

..
  .. image:: ../_static/apariencia_diagramacion.png
     :align:   center
     :alt: maquetación en CSS del diseño final

A continuación se explicara un poco sobre la diagramacion en CSS

* logo: Corresponde al logotipo de la institución.
* children:#usuario: Corresponde a la sección para iniciar sesión.
* children:#navegacion: Corresponde a la sección del menú horizontal la cual contendrá los botones, ayuda, colectivos comunitarios entre otros.
* #sidebar: Corresponde al menú lateral en el cual se podrán agregar los distintos contenidos.
* children:#heading: Este identificador sera reemplazado por el portal-breadcrumbs de la plataforma de comunidades, el portal-breadcrumbs es una barra de ubicación.
* children:#bodytext: Este identificador sera reemplazado por la columna3 de la plataforma de comunidades, la columna3 es el elemento en el cual son mostrados y agregados todos los contenidos del portal.
* #rotator: Es una pequeña animación en javascript la cual cambiara cada 3 segundos y en ella se verán visualizados los distintos colectivos comunitarios que trabajan con la fundación.
* #footer: Corresponde al pie de pagina de la plataforma de comunidades. 

.. centered:: **Menú Horizontal**

..
  .. image:: ../_static/apariencia_menu.png
     :align:   center
     :alt: menú horizontal

.. centered:: **Div id="Rotator"**

cada imagen puede tener un link que redireccione al portal o Web del colectivo comunitario.

..
  .. image:: ../_static/apariencia_sidebar.png
     :align:   center
     :alt: rotator animación en Javascript

.. code-block:: html

    <div id="rotator"> <!-- Mini Slide-->
    <a href="http://localhost:5000/cynin/home/colectivos-comunitarios/lapiz-    rebelde/mas-de-100000-visitas"><img src="images/02.jpg" alt="" /></a>
    <a href="http://localhost:5000/cynin/home/colectivos-comunitarios/    investarte/una-botella-menos-en-nuestro-paisaje"><img src="images/04.jpg"     alt="" /></a>  
    <!-- Podemos poner todas las imágenes que queramos, siempre metidas entre el div rotator--><!--fin rotator--></div>


Implementacion
==============

**Primer paso**

Activar un entorno virtual de python2.4 como se explico anteriormente en la sección de instalación

.. code-block:: console

    $ source virtualenv/python2.4/./bin/activate

**Segundo paso**

Iniciar la instancia en cyn.in como se explico anteriormente en la sección de instalación

.. code-block:: console

    (python2.4)$ ./bin/instance fg

**Tercer Paso**

Editar el archivo de reglas. Para este ejemplo la integración de Deliverance con Cynin en base a los requerimientos de los usuarios fueron necesarias las siguientes reglas:


.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <ruleset>
    <server-settings>
    <server>localhost:5000</server>
    <execute-pyref>true</execute-pyref>
    <dev-allow>localhost</dev-allow>
    <dev-user username="guest" password="guest" />
    </server-settings>  

    <proxy path="/static" class="static" editable="1">
    <dest href="{here}/static/" />
    </proxy>

    <proxy path="/" class="plone">
    <dest href="http://localhost:8081/cynin/" />
    <response rewrite-links="1" />
    </proxy>

    <rule class="static" />
    <rule class="plone" suppress-standard="1">

    <!-- Theme -->

    <theme href="/static/index.html" />

    <!-- Reglas -->

    <prepend content='/html/head/base' theme='children:/html/head' />   

    <!-- Agregar los CSS y Javascript de la plataforma al tema -->

    <append content='/html/head/meta' theme='/html/head' />
 
    <append content='/html/head/link' theme='/html/head' />

    <append content='/html/head/style' theme='/html/head' />

    <append content='/html/head/script' theme='/html/head' />

    <!--append theme="//head" content="//head/meta" nocontent="ignore" /-->

    <!--Reemplazar titulo del contenido al tema estatico-->

    <replace content='/html/head/title' theme='/html/head/title' />  

    <!-- Agregar los Ids y Clases de la plataforma cynin a la sección body del tema -->

    <append content="attributes(id,class):/html/body" theme="attributes:/html/body" /> 

    <!-- Reemplazar descripción del contenido  -->

    <drop theme='children:#bodytext' />

    <replace content='#col3_content' theme='children:#description' />

    <!-- Reemplazar titulo del texto por Ubicación -->

    <replace content='#portal-breadcrumbs' theme='children:#heading' nocontent="ignore"/>    

    <!--Reemplazar barra de Usuario-->

    <replace content='.myareanotloggedin' theme='children:#usuario'/>

    </rule>   

    </ruleset>


**Cuarto Paso**

Iniciar el Servicio de Deliverance

.. code-block:: console

    (python2.4)$ ./bin/deliverance-proxy rules.xml

A continuación unas capturas sobre como las reglas presentadas anteriormente hacen que el servicio de Deliverance cambie la apariencia por defecto del portal de comunidades.

.. centered:: **Portal de comunidades en Cenditel**

..
  .. image:: ../_static/apariencia_layoutcynin.png
     :align:   center

.. centered:: **Portal de comunidades en Cenditel con el servicio de Deliverance**

..
  .. image:: ../_static/apariencia_layouttema.png
     :align:   center
     :alt: integración del portal de comunidades con el tema

Como se pudo ver en las imágenes anteriores la columna 3 de la plataforma de comunidades y el portal-breadcrumbs se integraron correctamente en el tema, se pueden agregar contenidos, todas las vistas de aplicación funcionan. Sin embargo dicho tema es recomendable realizarle los cambios que se mencionan a continuación:

* El menú horizontal despliega contenidos, pero estos contenidos no son traídos de forma dinámica desde la plataforma de comunidades estos están debidamente enlazados, se realizo de esta manera debido a que la estructura de carpetas actual de la plataforma de comunidades no se encuentra distribuida de la manera como sus usuarios lo desean, para esto hay que aplicar cambios a la estructura de contenidos actual del CMS. Es importante realizar este cambio ya que momentáneamente los usuarios de la plataforma pueden agregar contenidos pero estos no se verán visualizados en los menús hasta que el administrador de la plataforma no modifique el código ``HTML`` del tema.

* Para agregar contenidos se limito en el diseño del tema a que los usuarios solo puedan agregar wikis, imágenes, archivos y audios, debido a que son estos los contenidos que comúnmente agregan, sin embargo no se debería limitar en esta medida a todos los usuarios, es decir, la plataforma ofrece un panel de configuración dentro de cada espacio de comunidad donde se pueden definir que tipos de contenidos se pueden seleccionar para ser agregados por los usuarios y adicionalmente desde el panel de administración se pueden agregar permisos en los cuales se especifican que clase de contenido se puede agregar a cada sección, haciéndolo de esta forma se podría usar el menú lateral para incorporar otro elemento.

* Se decidió dejar las vistas de aplicación de la plataforma cyn.in ya que remover estas quitarían completamente la usabilidad del portal de comunidades.

* A petición de los usuarios del portal de comunidades no se agrego el portlet de usuario, sin embargo es recomendable agregar este debido a que sin este elemento dificultara a los mismos usuarios cerrar su sesión. 

* A petición de los usuarios del portal de comunidades se realizaron los menús desplegables, pero basándose en la experiencia obtenida en la implementación estos menús dan problemas de accesibilidad y usabilidad, en ocasiones no se integran debidamente como corresponde, para futuros cambios es recomendable cambiar al menos el menú lateral por lo que actualmente se conoce como acordeón de botones. Para mas información en esta web se pueden ver algunos ejemplos http://www.celulaweb.net/2008/10/13/30-menús-basados-en-tabs-y-acordeon/

