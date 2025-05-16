from PIL import Image, ImageFilter, ImageFont, ImageDraw
image = Image.open("2.jpg")
image.show()
print(f"Размер изображения: {image.size}")
print(f"Формат: {image.format}")
print(f"Цветовая модель: {image.mode}")
