from PIL import Image, ImageDraw, ImageFont
def add_congrats(image_path, name):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arialbd.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    text = f"{name}, поздравляю!"


    text_width = draw.textlength(text, font=font)
    x = (img.width - text_width) // 2
    y = img.height - 70

    draw.text((x, y), text, font=font, fill="red")

    img.save(f"congrats_{image_path}", "PNG")

add_congrats("нг.jpg", "Анна")