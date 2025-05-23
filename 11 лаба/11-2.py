from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os

def process_image(file_path):

    try:
        image = Image.open(file_path)
        image.show()
        print(f"Файл: {file_path}")
        print(f"Размер изображения: {image.size}")
        print(f"Формат: {image.format}")
        print(f"Цветовая модель: {image.mode}\n")
    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}\n")

folder_path = "."

supported_formats = ('.jpg', '.jpeg', '.png')

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if filename.lower().endswith(supported_formats):
        print(f"Найдено изображение: {filename}")
        process_image(file_path)
    else:
        print(f"Пропущен файл (не изображение): {filename}")