.. highlight:: rest

.. _flujo_de_estado_transcodedeamon:

Flujos de Trabajos
------------------

Por defecto, los productos de multimedia de la fundación Cenditel no posee su propio flujo de trabajo al estilo de Plone.

cenditel.transcodedeamon
""""""""""""""""""""""""

Este producto posee su propio flujo de trabajo que se basa en teoría de colas,
usa la disciplina primero en entrar, primero en salir (FIFO). El flujo de trabajo, se encuentra
estrechamente relacionado a los productos cenditel.audio y cenditel.video en los métodos
de PlayingAudioType and PlayingVideoType de los modulos audioview.py y videoview.py de los paquetes browser.

De manera general, los métodos mencionados anteriormente obtienen una serie de configuraciones del
panel de control de la aplicación los modifica parcialmente en caso de ser necesario eliminando los simbolos ``/``
sobrantes, realizando concatenaciones entre las configuraciones, URL del sitio, y la porción de URL que sera utilizada
por los nuevos archivos codificados en formatos libres.

Origen de los datos
^^^^^^^^^^^^^^^^^^^

En el caso del producto cenditel.audio, el método ``PlayingAudioType`` que pertenece a la clase ``audioView`` del modulo ``audioview.py`` en el paquete browser,
es el encargado de obtener los datos que serán manipulados por ``cenditel.transcodedeamon``. A continuación se desglosa
dicho método.

.. code-block:: python
    
    def PlayingAudioType(self):
            """
            Primero vamos  a obtener la configuracion desde el panel de control:
            para eso, aplicamos la documentacion de Plone.app.registry
            que puede ser vista en http://pypi.python.org/pypi/plone.app.registry
            
                >>> registry = getUtility(IRegistry)
                >>> settings = registry.forInterface(ITranscodeSetings)
                >>> self.SERVER = self.RemoveSlash(settings.adress_of_streaming_server)
                >>> VIDEO_PARAMETRES_TRANSCODE = settings.ffmpeg_parameters_video_line
                >>> AUDIO_PARAMETRES_TRANSCODE = settings.ffmpeg_parameters_audio_line
                >>> audio_content_types=settings.audio_valid_content_types
                >>> video_content_types=settings.video_valid_content_types
                
            De esta manera, hacemos un llamado a los distintos registros almacenados
            por el panel de configuración que nos serán útiles en este caso.
            Ahora, se declaran variables que son de interés para entender el contexto de la aplicación:
            
               >>> self.MyTitle = self.context.Title()
               >>> idvideo=self.context.getId()
               >>> self.MyTitleWhitOutSpace = MFNI.DeleteSpaceinNameOfFolderFile(MFNI.TitleDeleteSpace(self.MyTitle))
               >>> url = self.context.absolute_url()
               >>> self.PathOfFile = MFNI.ReturnPathOfFile(url)
               >>>virtualobject=self.context.getVideo()
               >>>self.filenamesaved=virtualobject.filename
               >>> self.extension=MTDI.CheckExtension(self.filenamesaved)
            
            Para entender de mejor manera el código. Verifique la documentación de los métodos en el los script asociados a ellos.
            Las importaciones e instancias se encuentran en el modulo videoview.py.
            A continuación, se verifica si el archivo que fue cargado por el usuario tiene extensión ogg la cual corresponde
            a formatos de archivo basados en estandares libres.
            
                >>> if self.extension=="ogg":
                     ... self.folderfileOGG=self.PathOfFile+'/' + quote(self.filenamesaved)
                     ... self.prefiletranscoded=self.STORAGE+self.PathOfFile+'/'+self.filenamesaved
                     
            En caso de cumplirse la condición, se crea una nueva variable llamada FolderFile que posee parte de la URL del servidor de streaming,
            y otra variable que por su nombre indica que el archivo ha sido precodificado por el usuario desde antes de ser cargado al servidor.
            A continuación se verifica si ese archivo existe, y en caso de ser verdad, revisa si no existe en la lista de archivos disponibles, de ser así
            se agrega a dicha lista, en caso contrario se completa la ejecución del método y por tanto el flujo del transcode ya que no fue necesario convertir el archivo
            y por tanto puede ser publicado inmediatamente.
            
                >>> if path.isfile(self.prefiletranscoded)==True:
                        ... self.StatusOfFile=ServiceList.available(idvideo,self.prefiletranscoded)
                        ... if self.StatusOfFile == False:
                        ....... ServiceList.AddReadyElement(idaudio,self.prefiletranscoded)
                        ....... self.StatusOfFile=True
                        ....... ServiceList.SaveInZODB()
                        ....... self.AbsoluteServerPath = self.SERVER + self.folderfileOGG
                        ... else:
                        ....... self.AbsoluteServerPath = self.SERVER + self.folderfileOGG
                    
            En caso contrario a que la extesión del archivo subido por el usuario sea ogg, se dispara la ejecución de un método que se encargará de
            registrar el archivo en lista de espera y almacenar en cenditelmultimedia.fs datos que no son accesibles desde el panel
            de control que pueden ser usados por el convertidor de formatos. También se declaran otras variables que son utilizadas a nivel de vista
            de usuario para la presentación del contenido, para información acerca de los métodos revise la documentación de los mismos en el código
            correspondiente.
            
            >>> else:
                newtrans_init_(self.STORAGE,
                               self.PathOfFile,
                               self.filenamesaved,
                               idvideo,
                               VIDEO_PARAMETRES_TRANSCODE,
                               AUDIO_PARAMETRES_TRANSCODE,
                               audio_content_types,
                               video_content_types)
                self.folderfileOGG=MTDI.newname(self.PathOfFile+'/' + self.filenamesaved)
                self.AbsoluteServerPath = self.SERVER + MTDI.nginxpath(self.folderfileOGG)
                self.newfiletranscoded=MTDI.nginxpath(self.STORAGE+self.folderfileOGG)
                self.StatusOfFile = ServiceList.available(idvideo, self.newfiletranscoded)
                
            La ultima sección del método, verifica el valor de una variable bandera que revisa si el archivo se encuentra disponible. En
            caso contrario devuelve un error. 
                >>> if self.StatusOfFile == True:
                    ... self.newfilename=MTDI.newname(self.filenamesaved)
                ... else:
                    ... self.newfilename=_('The file is not ready yet, please contact site administration')
            """
            registry = getUtility(IRegistry)
            settings = registry.forInterface(ITranscodeSetings)
            self.SERVER = self.RemoveSlash(settings.adress_of_streaming_server)
            VIDEO_PARAMETRES_TRANSCODE = settings.ffmpeg_parameters_video_line
            AUDIO_PARAMETRES_TRANSCODE = settings.ffmpeg_parameters_audio_line
            audio_content_types=settings.audio_valid_content_types
            video_content_types=settings.video_valid_content_types
            self.STORAGE = self.RemoveSlash(settings.mount_point_fss)
            self.MyTitle = self.context.Title()
            idvideo=self.context.getId()
            self.MyTitleWhitOutSpace = MFNI.DeleteSpaceinNameOfFolderFile(MFNI.TitleDeleteSpace(self.MyTitle))
            url = self.context.absolute_url()
            self.PathOfFile = MFNI.ReturnPathOfFile(url)
            virtualobject=self.context.getVideo()
            self.filenamesaved=virtualobject.filename
            self.extension=MTDI.CheckExtension(self.filenamesaved)
            if self.extension=="ogg":
                self.folderfileOGG=self.PathOfFile+'/' + quote(self.filenamesaved)
                self.prefiletranscoded=self.STORAGE+self.PathOfFile+'/'+self.filenamesaved
                if path.isfile(self.prefiletranscoded)==True:
                    self.StatusOfFile=ServiceList.available(idvideo,self.prefiletranscoded)
                    if self.StatusOfFile == False:
                        ServiceList.AddReadyElement(idaudio,self.prefiletranscoded)
                        ServiceList.SaveInZODB()
                        self.AbsoluteServerPath = self.SERVER + self.folderfileOGG
                    else:
                        self.AbsoluteServerPath = self.SERVER + self.folderfileOGG
                else:
                    print _("File not found "+self.prefiletranscoded)
                    self.Error=True
                    self.ErrorSituation()
            else:
                newtrans_init_(self.STORAGE,
                               self.PathOfFile,
                               self.filenamesaved,
                               idvideo,
                               VIDEO_PARAMETRES_TRANSCODE,
                               AUDIO_PARAMETRES_TRANSCODE,
                               audio_content_types,
                               video_content_types)
                self.folderfileOGG=MTDI.newname(self.PathOfFile+'/' + self.filenamesaved)
                self.AbsoluteServerPath = self.SERVER + MTDI.nginxpath(self.folderfileOGG)
                self.newfiletranscoded=MTDI.nginxpath(self.STORAGE+self.folderfileOGG)
                self.StatusOfFile = ServiceList.available(idvideo, self.newfiletranscoded)
                #print "El STATUS OF FILE IN THE VIEW "+ str(self.StatusOfFile)
                if self.StatusOfFile == True:
                    self.newfilename=MTDI.newname(self.filenamesaved)
                else:
                    self.newfilename=_('The file is not ready yet, please contact site administration')
            return

Registro en espera
^^^^^^^^^^^^^^^^^^
Como se mencionó en la sección anterior, cuando un archivo subido no corresponde
a un archivo ogg dicho archivo es registrado en espera para posteriormente ser codificado
según la pocisión en la cola. En otras palabras, imagine la cola de un banco, donde usted
entra y espera su turno, luego es atendido, y posteriormente sale del banco. El sistema de conversión funciona de igual manera.

Ahora se va a analizar, el método ``newtrans_init_`` que es el encargado de registrar los elementos en la lista de espera.

.. code-block:: python

    """
    Como se puede observar a continuación el método recibe los siguientes parámetros:
    
    * STORAGE: Es la URL al directorio raíz del elemento.
    * path: Corresponde a la URL del elemento y es donde se guarda el archivo original en el disco duro del
    servidor.
    * filenamesaved: Nombre del archivo guardado originalmente.
    * idfile: Identificador del Elemento en el sitio Plone
    * VIDEO_PARAMETRES_TRANSCODE: Los datos de configuración del elemento video en el panel de control.
    * AUDIO_PARAMETRES_TRANSCODE: Los datos de configuración del elemento video el panel de control.
    * audio_content_types: Corresponde a los mimetypes para archivos de audio validos en el panel de control.
    * video_content_types: Corresponde a los mimetypes para archivos de vídeo validos en el panel de control.
    La primera linea, crea una variable que concatena los valores especificados anteriormente luego, esta es modificada por un método
    para entender el funcionamiento de este, vea la documentación respectiva en el código fuente del respectivo paquete.
    >>> PathToOriginalFile = STORAGE + path +'/'+ filenamesaved
    >>> newfolderfile=MTD.nginxpath(PathToOriginalFile)
    
    Las siguientes lineas, verifican si el valor de las variables en el panel de control corresponden
    a las variables almacenadas en la Base de Datos orientada a objetos del producto, y en caso de no
    ser de esa manera, cambian el valor almacenado.
    
    La siguiente linea, verifica si el archivo no esta en la lista de espera (resultado del método uploaded) y no se encuentra
    tampoco en la lista de archivos disponibles (resultado del método available) y no se encuentra siendo codificado en el momento
    (resultado del método transcoding)y en el caso de ser negativas todas las condiciones se el archivo se registrá en la lista de espera.
    
    >>> if ServiceList.uploaded(idfile, PathToOriginalFile)== False and ServiceList.available(idfile, newfolderfile)== False\
    and ServiceList.transcoding(PathToOriginalFile)== False:
        ... ServiceList.RegisterWaitingFile(idfile, PathToOriginalFile)

    La ultima seccion de codigo de este metodo, se encarga de disparar un sub proceso basado en programación multihilos
    que se ejecutará siempre que no se este convirtiendo ningun archivo en el momento.
    
    >>> import threading
    >>> if ServiceList.CurrentTranscoding()=="":
        ... class MyThread(threading.Thread):
        ... def run(self):
               transcodedaemon()
               MyThread().start()
    >>> return  
    """
    def newtrans_init_(STORAGE, path, filenamesaved,\
                       idfile, VIDEO_PARAMETRES_TRANSCODE,\
                       AUDIO_PARAMETRES_TRANSCODE,\
                       audio_content_types, video_content_types):
            PathToOriginalFile = STORAGE + path +'/'+ filenamesaved
            newfolderfile=MTD.nginxpath(PathToOriginalFile)
            if ServiceList.CheckItemZODB('waiting')==False:
                    ServiceList.AddObjectZODB('waiting',[])
            if ServiceList.CheckItemZODB('current')==False:
                    ServiceList.AddObjectZODB('current','')
                    ServiceList.SaveInZODB()
            if ServiceList.CheckItemZODB('ready')==False:
                    ServiceList.AddObjectZODB('ready',[])
                    ServiceList.SaveInZODB()
            if ServiceList.CheckItemZODB('Video_Parameters')==False:
                    ServiceList.AddObjectZODB('Video_Parameters', VIDEO_PARAMETRES_TRANSCODE)
                    ServiceList.SaveInZODB()
            if ServiceList.CheckItemZODB('Audio_Parameters')==False:
                    ServiceList.AddObjectZODB('Audio_Parameters', AUDIO_PARAMETRES_TRANSCODE)
                    ServiceList.SaveInZODB()
            
            if ServiceList.CheckItemZODB('Video_ContentTypes')==False:
                    ServiceList.AddObjectZODB('Video_ContentTypes', video_content_types)
                    ServiceList.SaveInZODB()
            if ServiceList.CheckItemZODB('Audio_ContentTypes')==False:
                    ServiceList.AddObjectZODB('Audio_ContentTypes', audio_content_types)
                    ServiceList.SaveInZODB()
    
            if ServiceList.root['Audio_Parameters']!=AUDIO_PARAMETRES_TRANSCODE:
                    ServiceList.root['Audio_Parameters']=AUDIO_PARAMETRES_TRANSCODE
                    ServiceList.SaveInZODB()
            if ServiceList.root['Video_Parameters']!=VIDEO_PARAMETRES_TRANSCODE:
                    ServiceList.root['Video_Parameters']=VIDEO_PARAMETRES_TRANSCODE
                    ServiceList.SaveInZODB()
    
            if ServiceList.root['Video_ContentTypes']!=video_content_types:
                    ServiceList.root['Video_ContentTypes']=video_content_types
                    ServiceList.SaveInZODB()
            
            if ServiceList.root['Audio_ContentTypes']!=audio_content_types:
                    ServiceList.root['Audio_ContentTypes']=audio_content_types
                    ServiceList.SaveInZODB()
    
            if ServiceList.uploaded(idfile, PathToOriginalFile)== False and ServiceList.available(idfile, newfolderfile)== False and ServiceList.transcoding(PathToOriginalFile)== False:
                    ServiceList.RegisterWaitingFile(idfile, PathToOriginalFile)
            import threading
            if ServiceList.CurrentTranscoding()=="":
                    class MyThread(threading.Thread):
                            def run(self):
                                    transcodedaemon()
                    MyThread().start()
            return  
    
Prestación del servicio
^^^^^^^^^^^^^^^^^^^^^^^
Una vez que el archivo cliente ha sido registrado en la lista de espera, y no existe
ningún elemento siendo codificado en el momento, se dispara el siguiente método que
es el encargado de extraer los archivos en espera y pasar la URL en el disco duro a una
instancia de ffmpeg que se encargará de crear un archivo de salida con un nuevo formato
libre que permita su utilización usando html5.

.. code-block:: python
 
    def transcodedaemon():
        """
        
        La primera linea, obtiene la cantidad de registros en espera.
        Si la cantidad es mayor a 0.
        
        >>> while(ServiceList.FileWaitings()>0):
        
        Las siguientes lineas extraen la dirección del primer archivo 
        
            ... element=ServiceList.WaitingElement()
	    ... listpath=element.values()
	    ... PathToOriginalFile=listpath[0]
            
        Por otro lado, reseteando la variable se extrae el identificador del archivo.
        
	    ... listpath=''
	    ... listpath=element.keys()
	    ... idfile=listpath[0]
            
        A continuación se verifica si el archivo existe, de ser así se elimina el elemento
        de la lista de espera, se agrega la url del a una variable que controla el flujo en el
        codificador se dispara el método ``transcode`` que recibe una serie de parámetros
        que serán explicados a continuación.
        
        >>> if os.path.isfile(PathToOriginalFile):
        
                    ... ServiceList.DeleteElement(idfile, PathToOriginalFile)
		    ... ServiceList.AddActiveTranscoding(PathToOriginalFile)
		    ... PathToTranscodedFile = MTD.transcode(PathToOriginalFile,
						     ServiceList.root['Video_Parameters'],
						     ServiceList.root['Audio_Parameters'],
						     ServiceList.root['Video_ContentTypes'],
						     ServiceList.root['Audio_ContentTypes'],)
       
        * ServiceList.root['Video_Parameters']: Parámetros de codificación de archivos de vídeo.
        * ServiceList.root['Audio_Parameters']: Parámetros de codificación de archivos de audio.
        * ServiceList.root['Video_ContentTypes']: Tipos de contenido de vídeo validos.
	* ServiceList.root['Audio_ContentTypes']: Tipos de contenido de audio validos.
       
       Luego, es eliminado el elemento de la variable de control de codificación y luego
       es pasada a una lista de elementos guardados y se guarda la información en la base de
       datos del producto.
        
        >>> ServiceList.RemoveActiveTranscoding()
	>>> ServiceList.AddReadyElement(idfile, PathToTranscodedFile)
	>>> ServiceList.SaveInZODB()
        
        En caso de que la condición de existencia del archivo no se cumpla,
        Se elimina el elemento de la lista de espera y se manda un log de elemento no encontrado.
        
        ... else:
            ... ServiceList.DeleteElement(idfile, PathToOriginalFile)
	    ... print "NOT FOUND "+ PathToOriginalFile
	    ... ServiceList.SaveInZODB()
        """
        while(ServiceList.FileWaitings()>0):
		element=ServiceList.WaitingElement()
		listpath=element.values()
		PathToOriginalFile=listpath[0]
		listpath=''
		listpath=element.keys()
		idfile=listpath[0]
		if os.path.isfile(PathToOriginalFile):
			ServiceList.DeleteElement(idfile, PathToOriginalFile)
			ServiceList.AddActiveTranscoding(PathToOriginalFile)
			PathToTranscodedFile = MTD.transcode(PathToOriginalFile,
						     ServiceList.root['Video_Parameters'],
						     ServiceList.root['Audio_Parameters'],
						     ServiceList.root['Video_ContentTypes'],
						     ServiceList.root['Audio_ContentTypes'],)
			ServiceList.RemoveActiveTranscoding()
			ServiceList.AddReadyElement(idfile, PathToTranscodedFile)
			ServiceList.SaveInZODB()
		else:
			ServiceList.DeleteElement(idfile, PathToOriginalFile)
			print "NOT FOUND "+ PathToOriginalFile
			ServiceList.SaveInZODB()
	print "Daemon is waiting for File"
	return

Una vez finalizado los procesos, el archivo queda disponible para streaming. Ya
sea en el caso de los archivos de audio o de los archivos de vídeo. 