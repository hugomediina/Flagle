
Flagle En Español

Este proyecto fue creado con la intención de desarrollar un juego reutilizable. El código que encontrarás a continuación representa mi primera incursión en Flask y la biblioteca PIL. Está inspirado en el sitio web "https://flagle-game.com/" con una temática similar.

Para este proyecto, se utilizaron como fuentes de banderas y codes.json el sitio web "https://www.banderas-mundo.es/descargar". Además, se emplearon las bibliotecas PIL para el procesamiento de imágenes y Flask para la conexión entre las vistas y el código principal. Es importante mencionar que, para garantizar el correcto funcionamiento del programa, se creó un script que ajusta la resolución de todas las imágenes para que sean similares o iguales.

El funcionamiento del código es el siguiente:

Se crea una imagen en blanco con la resolución de todas las banderas disponibles.
Se elige aleatoriamente un país entre todos los disponibles.
Se crea una matriz con la imagen del país seleccionado y otra con la imagen seleccionada por el usuario.
Se realiza una intersección y, si ya existe un elemento anterior, se realiza una unión con la matriz actual.
Se solicita al usuario que agregue más opciones hasta que la selección sea correcta.
¡Gracias por leer y disfruta del código! 😄
