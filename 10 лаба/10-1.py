from PIL import Image
img = Image.open("нг.jpg")
cropped = img.crop((100, 50, 400, 300))
cropped.save("cropped_postcard.jpg")