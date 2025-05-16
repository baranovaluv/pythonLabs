from PIL import Image, ImageFilter, ImageFont, ImageDraw
import os

output_dir = "RJNS"
os.makedirs(output_dir, exist_ok=True)
for i in range(1, 6):
    try:
        img = Image.open(f"{i}.jpg")
        filtered = img.filter(ImageFilter.EMBOSS)
        filtered.save(f"{output_dir}/filtered_{i}.jpg")
    except FileNotFoundError:
        print(f"Файл {i}.jpg не найден!")
def add_watermark(input_path, output_path, text):
    img = Image.open(input_path).convert("RGBA")
    watermark = Image.new("RGBA", img.size)
    draw = ImageDraw.Draw(watermark)

    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font = ImageFont.load_default()

    x = img.width - 200
    y = img.height - 100

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

    combined = Image.alpha_composite(img, watermark)
    combined.convert("RGB").save(output_path)

for i in range(1, 3):
    add_watermark(f"{i}.jpg", f"watermarked_{i}.jpg", "©1231")



