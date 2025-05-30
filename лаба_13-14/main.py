#
# class Restaurant:
#     def init(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.rating = 0
#
#     def describe_restaurant(self):
#         print(f"Название: {self.restaurant_name}")
#         print(f"Тип кухни: {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"Ресторан '{self.restaurant_name}' открыт!")
#
#     def update_rating(self, new_rating):
#         self.rating = new_rating
#         print(f"Рейтинг обновлен: {self.rating}")
#
#
# newRestaurant = Restaurant("Гурман", "Французская")
#
#
# print(newRestaurant.restaurant_name)
# print(newRestaurant.cuisine_type)
# newRestaurant.describe_restaurant()
# newRestaurant.open_restaurant()
#
#
#
# restaurant1 = Restaurant("Суши-бар", "Японская")
# restaurant2 = Restaurant("Печка", "Русская")
# restaurant3 = Restaurant("Бургер Кинг", "Американская")
#
#
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
#
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().init(restaurant_name, cuisine_type)
#         self.flavors = flavors
#
#     def show_flavors(self):
#         print("Сорта мороженого:")
#         for flavor in self.flavors:
#             print(f"- {flavor}")
#
# # Создание экземпляра
# ice_cream_stand = IceCreamStand("Сладкоежка", "Кафе-мороженое", ["Ванильное", "Шоколадное", "Клубничное"])
# ice_cream_stand.show_flavors()
#
# class IceCreamStand(Restaurant):
#     def init(self, restaurant_name, cuisine_type, flavors, location, working_hours):
#         super().init(restaurant_name, cuisine_type)
#         self.flavors = flavors
#         self.location = location
#         self.working_hours = working_hours
#         self.ice_cream_types = {"на палочке": [], "мягкое": [], "фруктовый лед": []}
#
#     def add_flavor(self, flavor):
#         self.flavors.append(flavor)
#         print(f"Добавлен сорт: {flavor}")
#
#     def remove_flavor(self, flavor):
#         if flavor in self.flavors:
#             self.flavors.remove(flavor)
#             print(f"Удален сорт: {flavor}")
#         else:
#             print("Такого сорта нет в списке!")
#
#     def check_flavor(self, flavor):
#         return flavor in self.flavors
#
#     def add_ice_cream_to_type(self, ice_cream_type, flavor):
#         if ice_cream_type in self.ice_cream_types:
#             self.ice_cream_types[ice_cream_type].append(flavor)
#             print(f"Добавлено {flavor} в {ice_cream_type}")
#         else:
#             print("Неизвестный тип мороженого!")
#
#
# stand = IceCreamStand(
#     "Морожко",
#     "Кафе-мороженое",
#     ["Фисташковое"],
#     "ул. Ленина, 10",
#     "10:00–22:00"
# )
#
# stand.add_flavor("Мятное")
# stand.add_ice_cream_to_type("на палочке", "Эскимо")
# print(stand.check_flavor("Фисташковое"))  # True
#
#
# import tkinter as tk
#
# class IceCreamStandGUI:
#     def init(self, master):
#         self.master = master
#         master.title("Кафе-мороженое")
#
#
#         self.stand = IceCreamStand(
#             "Сладкий уголок",
#             "Кафе-мороженое",
#             ["Ванильное", "Карамельное"],
#             "Центральный парк",
#             "09:00–23:00"
#         )
#
#
#         self.label = tk.Label(master, text="Добро пожаловать в кафе-мороженое!")
#         self.label.pack()
#
#         self.flavors_button = tk.Button(master, text="Показать сорта", command=self.show_flavors)
#         self.flavors_button.pack()
#
#         self.add_button = tk.Button(master, text="Добавить сорт", command=self.add_flavor)
#         self.add_button.pack()
#
#     def show_flavors(self):
#         flavors_window = tk.Toplevel(self.master)
#         flavors_window.title("Сорта мороженого")
#         for flavor in self.stand.flavors:
#             tk.Label(flavors_window, text=flavor).pack()
#
#
# def add_flavor(self):
#     add_window = tk.Toplevel(self.master)
#     tk.Label(add_window, text="Введите новый сорт:").pack()
#     self.new_flavor_entry = tk.Entry(add_window)
#     self.new_flavor_entry.pack()
#     tk.Button(add_window, text="Добавить", command=self.save_flavor).pack()
#
# def save_flavor(self):
#     new_flavor = self.new_flavor_entry.get()
#     self.stand.add_flavor(new_flavor)
#     self.new_flavor_entry.delete(0, tk.END)
#
#
#
# root = tk.Tk()
# app = IceCreamStandGUI(root)
# root.mainloop()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):  # Исправлено на __init__
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг обновлен: {self.rating}")


# Создание и тестирование ресторанов
newRestaurant = Restaurant("Гурман", "Французская")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

restaurant1 = Restaurant("Суши-бар", "Японская")
restaurant2 = Restaurant("Печка", "Русская")
restaurant3 = Restaurant("Бургер Кинг", "Американская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location=None, working_hours=None):
        super().__init__(restaurant_name, cuisine_type)  # Исправлено на __init__
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
        self.ice_cream_types = {"на палочке": [], "мягкое": [], "фруктовый лед": []}

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Добавлен сорт: {flavor}")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Удален сорт: {flavor}")
        else:
            print("Такого сорта нет в списке!")

    def check_flavor(self, flavor):
        return flavor in self.flavors

    def add_ice_cream_to_type(self, ice_cream_type, flavor):
        if ice_cream_type in self.ice_cream_types:
            self.ice_cream_types[ice_cream_type].append(flavor)
            print(f"Добавлено {flavor} в {ice_cream_type}")
        else:
            print("Неизвестный тип мороженого!")


# Создание экземпляра IceCreamStand
ice_cream_stand = IceCreamStand("Сладкоежка", "Кафе-мороженое", ["Ванильное", "Шоколадное", "Клубничное"])
ice_cream_stand.show_flavors()

stand = IceCreamStand(
    "Морожко",
    "Кафе-мороженое",
    ["Фисташковое"],
    "ул. Ленина, 10",
    "10:00–22:00"
)

stand.add_flavor("Мятное")
stand.add_ice_cream_to_type("на палочке", "Эскимо")
print(stand.check_flavor("Фисташковое"))  # True


import tkinter as tk

class IceCreamStandGUI:
    def __init__(self, master):  # Исправлено на __init__
        self.master = master
        master.title("Кафе-мороженое")

        self.stand = IceCreamStand(
            "Сладкий уголок",
            "Кафе-мороженое",
            ["Ванильное", "Карамельное"],
            "Центральный парк",
            "09:00–23:00"
        )

        self.label = tk.Label(master, text="Добро пожаловать в кафе-мороженое!")
        self.label.pack()

        self.flavors_button = tk.Button(master, text="Показать сорта", command=self.show_flavors)
        self.flavors_button.pack()

        self.add_button = tk.Button(master, text="Добавить сорт", command=self.add_flavor)
        self.add_button.pack()

    def show_flavors(self):
        flavors_window = tk.Toplevel(self.master)
        flavors_window.title("Сорта мороженого")
        for flavor in self.stand.flavors:
            tk.Label(flavors_window, text=flavor).pack()

    def add_flavor(self):
        add_window = tk.Toplevel(self.master)
        tk.Label(add_window, text="Введите новый сорт:").pack()
        self.new_flavor_entry = tk.Entry(add_window)
        self.new_flavor_entry.pack()
        tk.Button(add_window, text="Добавить", command=self.save_flavor).pack()

    def save_flavor(self):
        new_flavor = self.new_flavor_entry.get()
        self.stand.add_flavor(new_flavor)
        self.new_flavor_entry.delete(0, tk.END)


root = tk.Tk()
app = IceCreamStandGUI(root)
root.mainloop()