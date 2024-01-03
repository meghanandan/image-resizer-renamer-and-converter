import os
from PIL import Image

def resize_image(input_path, output_path, target_width):
    original_image = Image.open(input_path)
    aspect_ratio = original_image.width / original_image.height
    target_height = int(target_width / aspect_ratio)
    resized_image = original_image.resize((target_width, target_height))
    resized_image.save(output_path)

def resize_and_convert(input_folder, output_folder, target_width, new_extension='.webp'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_folder, file)
            filename, extension = os.path.splitext(file)
            new_filename = f'{filename}_movie-poster_cc{new_extension}'
            output_path = os.path.join(output_folder, new_filename)
            resize_image(input_path, output_path, target_width)

# Example usage
input_folder = r'C:\Users\Administrator\Pictures\pics'
output_folder = r'C:\Users\Administrator\Pictures\pics'
target_width = 300
new_extension = '.webp'

resize_and_convert(input_folder, output_folder, target_width, new_extension)
