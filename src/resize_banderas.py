from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file in files:
        if file.lower().endswith('.jpg'):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            image = Image.open(input_path)
            resized_image = image.resize(new_size)

            resized_image.save(output_path)
            print(f"Imagen {file} redimensionada y guardada en {output_path}")

input_folder = '../img/original_flags'
output_folder = '../img/all_flags'

new_size = (640, 488)
resize_images(input_folder, output_folder, new_size)
