from PIL import Image, ImageFilter, ImageFont, ImageDraw
image = Image.open("1.jpg")

resized = image.resize((image.width // 3, image.height // 3))
resized.save("resized_image.jpg")

horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal.save("horizontal_flip.jpg")

vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical.save("vertical_flip.jpg")

resized.show()
horizontal.show()
vertical.show()