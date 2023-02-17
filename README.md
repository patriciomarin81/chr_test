# chr_test
Test Práctico Developer

Se creó una app llamada GestionDatos donde se generaron los modelos para utilizar en las tareas (models.py).

Tarea 1:
- Con la libreria "requests" se obtiene el contenido entregado por la API y transforma en texto.
- Se utliza json.loads() para poder obtener la información de todos los campos del JSON, los cuales se almacenan en la base de datos Postgresql.
- Se ejecuta python "manage.py runserver localhost:xxxx" (xxxx: puerto) para correr el servidor.
- Por medio de la URL http://localhost:xxxx/BikeSantiago, la aplicación borra la información existente en la base de datos y la vuelve a cargar leyendo la API.

Tarea 2:
- Con la libreria "beautifulsoap4" se obtiene el contenido entregado por la URL. Navega todas las páginas y se construye un script para obtener la data.
- Se ejecuta python "manage.py runserver localhost:xxxx" (xxxx: puerto) para correr el servidor.
- Por medio de la URL http://localhost:xxxx/ServicioEvaluacionAmbiental, la aplicación borra la información existente en la base de datos y la vuelve a cargar leyendo la API. Además desplegará el JSON con toda la información obtenida.
