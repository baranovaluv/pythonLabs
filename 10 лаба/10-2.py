from PIL import Image
holidays = {
    "Новый год": "нг.jpg",
    "8 марта": "весна.jpg",
    "День рождения": "др.jpg"
}
user_holiday = input("К какому празднику нужна открытка? ").strip().lower()
matched = False
for holiday, filename in holidays.items():
    if user_holiday in holiday.lower():
        Image.open(filename).show()
        matched = True
        break

if not matched:
    print("Открытка не найдена!")