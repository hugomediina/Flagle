Este proyecto se realizó con la necesidad de crear un juego utilizable de forma constante, el código que leerás a continuación es correspondiente mi primera toma de contacto con Flask y la biblioteca PIL.
Está basado en la página web "https://flagle-game.com/" con la misma temática.

Para la realización de este proyecto se utilizarón para las fuentes de banderas y codes.json, la siguiente página web: "https://www.banderas-mundo.es/descargar"
Además, se utilizarón tanto la biblioteca PIL, para el tratamiento de imágenes, como Flask, para la conexión entre las vistas y el código principal
Antes de explicar el código se ha de comentar que para que hubiera un correcto funcionamiento del programa, se realizó un programa que cambia de tamaño la resolución de estas para que todas tengan una similar o igual.

El código funciona de la siguiente manera:

Primero se crea una imagen en blanco con la resolución de todas las banderas.
Tras esto se escoge un país dentro de todos los disponibles.
Una vez creado esto se realiza una matriz con la imagen del pais escogido y otra con la seleccionada por el usuario.
Se realiza una intersección y si existia un elemento anterior se realiza una union con la actual, hecho esto.
Se pide al usuario añadir más opciones hasta que esta sea correcta.

Gracias por leer y disfruta del código :D