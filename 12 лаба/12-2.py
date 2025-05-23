import json
import os

def load_products(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):

        return {"products": []}


def save_products(filename, data):

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def get_valid_input(prompt, input_type=str, validation=None):

    while True:
        try:
            value = input(prompt)
            if input_type == int:
                value = int(value)
                if value <= 0:
                    raise ValueError("Значение должно быть положительным")
            elif input_type == bool:
                value = value.lower() in ['да', 'yes', '1', 'true']
            if validation and not validation(value):
                raise ValueError("Некорректное значение")
            return value
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, попробуйте еще раз.")


def add_product(data):

    print("\nДобавление нового продукта:")

    name = get_valid_input("Название: ", validation=lambda x: len(x.strip()) > 0)
    price = get_valid_input("Цена: ", int)
    available = get_valid_input("В наличии (да/нет): ", bool)
    weight = get_valid_input("Вес (в граммах): ", int)

    new_product = {
        "name": name.strip(),
        "price": price,
        "available": available,
        "weight": weight,
        "added_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data['products'].append(new_product)
    print(f"\nПродукт '{name}' успешно добавлен!")


def display_products(data):

    if not data['products']:
        print("\nСписок продуктов пуст.")
        return

    print("\nТекущий список продуктов:")
    for i, product in enumerate(data['products'], 1):
        print(f"\n#{i}")
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']} руб.")
        print(f"Вес: {product['weight']} г")
        print(f"В наличии: {'Да' if product['available'] else 'Нет'}")
        if 'added_date' in product:
            print(f"Дата добавления: {product['added_date']}")


def main():
    filename = 'products.json'


    data = load_products(filename)


    display_products(data)


    while True:
        answer = input("\nХотите добавить продукт? (да/нет): ").lower()
        if answer not in ['да', 'yes', 'д', 'y']:
            break
        add_product(data)
        save_products(filename, data)


    print("\nИтоговый список продуктов:")
    display_products(data)


if __name__ == "__main__":
    import datetime

    main()