import csv
total = 0
print("Нужно купить:")

with open('products.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row['Продукт']
        quantity = row['Количество']
        price = row['Цена']
        cost = int(quantity) * int(price)
        total += cost
        print(f"{product} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {total} руб.")