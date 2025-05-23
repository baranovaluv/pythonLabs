from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

input_folder = "images"
output_folder = "processed"

os.makedirs(output_folder, exist_ok=True)

def add_watermark(input_path, output_path, text="©12f"):

    try:
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
    except Exception as e:
        print(f"Ошибка при добавлении водяного знака: {e}")


for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)

        try:
            img = Image.open(input_path)
            filtered_img = img.filter(ImageFilter.EMBOSS)

            filtered_path = os.path.join(output_folder, f"filtered_{filename}")
            filtered_img.save(filtered_path)

            watermarked_path = os.path.join(output_folder, f"watermarked_{filename}")
            add_watermark(input_path, watermarked_path, "©12f")

            print(f"Обработано: {filename}")
        except Exception as e:
            print(f"Ошибка при обработке {filename}: {e}")

print("Обработка завершена!")