.. highlight:: rest

.. _integracion_con_cynin:

Integración con cyn.in
----------------------

Primer Paso
^^^^^^^^^^^
Descargar de la pagina Web del Proyecto el script de instalación buildout que le permitirá configurar un sitio demostrativo.
Para realizar la descarga proceda en un terminal con los siguientes comandos:

.. code-block:: console

    $ mkdir buildouts
    $ cd buildouts
    $ svn co http://plataforma.cenditel.gob.ve/svn/plataforma/proyectosInstitucionales/
    renasen/cenditel.multimedia/buildout/cynin313 cenditelmultimedia
    $ cd cenditelmultimedia
    $ ls -p
    00-varibles.cfg           06-contenttypes.cfg     plonesite.cfg
    01-dumpedversions.cfg     bootstrap.py            products/
    02-mrdeveloper.cfg        buildout.cfg            src/
    03-prerequemients.cfg     cenditelmultimedia.cfg  templates/
    04-mountpoint.cfg         dumped-versions.cfg     versions.cfg
    05-mediafilesstorage.cfg  etc/                    user.cfg

Segundo paso
^^^^^^^^^^^^

Instale una jaula de ``python2.4`` en su sistema para evitar daños a su sistema operativo.
Proceda como se señala a continuación.

.. code-block:: console

    $ sudo aptitude install python2.4 python2.4-minimal python2.4-dev
    python-virtualenv python-setuptools 
    $ virtualenv -p python2.4 python2.4/
    $ cd python2.4/
    $ source bin/activate
    (python2.4)$ cd $HOME/buildouts/cenditelmultimedia
    (python2.4)$ python bootstrap.py
    (python2.4)$ pip install ZopeSkel lxml python-ldap
    (python2.4)$ easy_install-2.4 -i http://dist.serverzen.com/pypi/simple PILwoTk

Tercer Paso
^^^^^^^^^^^
Edite el archivo ``user.cfg`` y cambie la variable ``effective-user`` de manera que el
valor corresponda con el nombre de usuario de su sesión Unix. 

.. code-block:: console

    (python2.4)$ ./bin/buildout -vNc cenditelmultimedia.cfg

Al realizar esto, buildout ejecutará las configuraciones necesarias en la instancia
para instalar los productos. Una vez finalizado, se debe iniciar la instancia para
crear un sitio nuevo de demostración.

Iniciando la Instancia en Cyn.in 3.1.3:
"""""""""""""""""""""""""""""""""""""""

A continuación usted debe proceder a iniciar la instancia del mismo:

.. code-block:: console

    (python2.4)$ ./bin/instance fg

Dirijase a la interfaz administrativa de Zope a través de `http://localhost:8080/manage <http://localhost:8080/manage>`_
El nombre de usuario por defecto es ``admin`` y la contraseña es ``secret``. En la parte superior derecha,
se observa un menú desplegable. Haga clic en él y seleccione la opción que dice: ``Plone site``

En la siguiente ventana, agregue un identificador en minúsculas para el sitio,
dadas la configuraciones que realizo buildout en la etapa anterior, debe colocar
en esta casilla el valor ``demo``. Luego haga clic en aceptar. Como podrá observar
ahora posee un sitio Plone básico, para continuar proceda a volver a la interfaz
administrativa `http://localhost:8080/manage <http://localhost:8080/manage>`_.
Haga clic en elemento demo a mano derecha, la ventana se actualizará.
Luego debe ir a la opción ``portal_quick_instaler`` y seleccionar para instalación
el producto ubify.sitepolicy. Haga clic en install y espere unos segundos.

Tras esto, ya debe de poseer un sitio basico con el sistema cyn.in. Vaya a
`http://localhost:8080/demo <http://localhost:8080/demo>`_

Luego, detenga su instancia usando ``Ctrl+C`` en la ventana donde ejecuto.

.. code-block:: console

    (python2.4)$ ./bin/instance fg

Proceda a editar el archivo: src/ubify.policy/ubify/policy/config.py

Cambie las variables ``spacesdefaultaddablenonfolderishtypes`` y  ``PRODUCT_DEPENDENCIES``
como se muestra a continuación:

.. code-block:: python
    
    spacesdefaultaddablenonfolderishtypes = ('Document',
                                             'Event',
                                             'File',
                                             'Image',
                                             'Link',
                                             'Blog Entry',
                                             'Discussion',
                                             'audio',
                                             'video',
                                            )   

    PRODUCT_DEPENDENCIES = ('Calendaring',
                            'plone.app.iterate',
                            'Marshall',
                            'CMFPlacefulWorkflow',
                            'CMFNotification',
                            'ZipFileTransport',
                            'Scrawl',
                            'ubify.coretypes',
                            'ubify.smartview',
                            'ubify.spaces',
                            'ubify.viewlets',
                            'ubify.cyninv2theme',
                            'ubify.recyclebin',
                            'ubify.xmlrpc',
                            'Products.OpenXml',
                            'ATRatings',
                            'ubify.ffxmpp',
                            'cenditel.audio',
                            'cenditel.video',
                            )

A continuación modifique los siguientes valores a los archivos de configuración
xml en ``ubify.coretypes/ubify/coretypes/profiles/default/ContentSpace``
y ``ubify.coretypes/ubify/coretypes/profiles/default/ContentRoot``.

.. code-block:: xml

    <property name="allowed_content_types">
      <element value="Document"/>
      <element value="Event"/>
      <element value="File"/>
      <element value="Image"/>
      <element value="Link"/>
      <element value="Blog Entry"/>
      <element value="ContentSpace"/>
      <element value="Video"/>
      <element value="Discussion"/>
      <element value="Audio"/>
      <element value="audio"/>
      <element value="video"/>
     </property>
 
Vuelva a la zona donde esta el script buildout y ejecute el mismo de nuevo.

.. code-block:: console
 
    (python2.4)$ cd $HOME/buildouts/cenditelmultimedia
    (python2.4)$ ./bin/buildout -vNc cenditelmultimedia.cfg

Al finalizar ejecute nuevamente la instancia.

.. code-block:: console

    (python2.4)$ ./bin/instance fg

Luego, diríjase a `http://localhost:8080/manage <http://localhost:8080/manage>`_
diríjase nuevamente a ``portal_quick_installer`` y marque la casilla ubisite.policy
presione reinstall.

Al terminar vuelva a `http://localhost:8080/demo <http://localhost:8080/demo>`_
y presione el botón nuevo. Debería de poder agregar tipos de contenido de audio y vídeo usando html5.