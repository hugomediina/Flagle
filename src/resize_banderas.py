from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Listar archivos en la carpeta de entrada
    files = os.listdir(input_folder)

    for file in files:
        # Verificar si es un archivo jpg
        if file.lower().endswith('.jpg'):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            # Abrir la imagen
            image = Image.open(input_path)

            # Cambiar el tamaño
            resized_image = image.resize(new_size)

            # Guardar la imagen en la carpeta de salida
            resized_image.save(output_path)
            print(f"Imagen {file} redimensionada y guardada en {output_path}")

# Carpeta de entrada y salida
input_folder = '../img/original_flags'
output_folder = '../img/all_flags'

# Tamaño deseado para las imágenes (ancho, alto)
new_size = (640, 488)

# Llamar a la función para redimensionar las imágenes
resize_images(input_folder, output_folder, new_size)
