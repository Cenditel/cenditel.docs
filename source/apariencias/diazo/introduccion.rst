.. highlight:: rest

.. _diazo_instroduccion:

===========
XDV / Diazo
===========

El paquete `diazo`_ implementa un lenguaje como `Deliverance`_ usando un puro motor `XSLT`_. Con Diazo, usted "compila" el tema y el conjunto de reglas (ruleset) en un solo paso, entonces usa una súper / simple transformación en cada solicitud adicional. Por otra parte, usted puede compilar el tema durante el desarrollo, protegerlo dentro de un repositorio de control de versiones Subversion o Git, y no tocar Diazo durante la implementación.

Este le permite aplicar un tema incluido en una página web `HTML`_ estática a un sitio web creado de manera dinámica utilizando cualquier tecnología del lado del servidor. Con Diazo, usted puede tomar una diagramación de un diseño `HTML`_ creado por un diseñador de páginas web y convertirlo en un tema para su favorito de la CMS, el rediseño de la interfaz de usuario de una aplicación web operativa sin ni siquiera tener acceso al código fuente original, o crear una experiencia de usuario unificada a través de múltiples sistemas dispares, todo en cuestión de horas, no semanas.

Cuando se utiliza Diazo, tendrá que trabajar con la sintaxis y conceptos familiares al trabajar con `HTML`_ y `CSS`_. Y por lo que le permite integrar sin problemas los archivos `XSLT`_ en su regla, Diazo hace que en los casos más simple y complejos comunes las exigencias sean posibles.

Para obtener documentación detallada, consulte `diazo.org`_.

.. _diazo: https://pypi.org/project/diazo
.. _Deliverance: https://pypi.org/project/Deliverance
.. _XSLT: https://es.wikipedia.org/wiki/XSLT
.. _HTML: https://es.wikipedia.org/wiki/HTML
.. _CSS: https://es.wikipedia.org/wiki/Hojas_de_estilo_en_cascada
.. _diazo.org: http://docs.diazo.org/en/latest/
