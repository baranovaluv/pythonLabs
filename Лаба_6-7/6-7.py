def x (number):
    return number % 3 == 0
n = int(input("Введите число: "))
print(x(n))



def y ():
    try:
        user_input = float(input("Введите число для деления 100: "))
        result = 100 / user_input
        print(f"Результат деления 100 на {user_input} = {result}")
    except ValueError:
        print("Ошибка: введено некорректное значение. Пожалуйста, введите число.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
y()


def d (day, month, year):
    return day * month == year % 100


day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
print(d(day, month, year))


def t (ticket_number):
    half_length = len(ticket_number) // 2
    first_half_sum = sum(int(digit) for digit in ticket_number[:half_length])
    second_half_sum = sum(int(digit) for digit in ticket_number[half_length:])
    return first_half_sum == second_half_sum


ticket_number = input("Введите номер билет (чётное количество цифр): ")
if len(ticket_number) % 2 == 0:
    print(t(ticket_number))
else:
    print("Ошибка: номер билета должен содержать чётное количество цифр.")


import random
def guess_the_number():
    numbers = random.sample(range(1, 50), 5)
    user_number = int(input("Введите число: "))
    print("Исходный список:", numbers)
    print("Вы ввели число:", user_number)
    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
guess_the_number()



random_list = [1, 2, 3, 4, 5, 2, 5, 7, 3]
duplicates = set([x for x in random_list if random_list.count(x) > 1])
if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет")


days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
holidays = int(input("Сколько выходных на неделе Вы хотите? "))
print("Ваши выходные дни:", days[-holidays:])
print("Ваши рабочие дни:", days[:-holidays])


import random
group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Смирнов",
          "Попов", "Васильев", "Михайлов", "Федоров", "Алексеев"]
group2 = ["Григорьев", "Орлов", "Никитин", "Захаров", "Соловьев",
          "Борисов", "Титов", "Кудрявцев", "Матвеев", "Жуков"]
team = tuple(random.sample(group1, 5) + random.sample(group2, 5))
print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", team)
print("Длина кортежа:", len(team))
print("Отсортированная команда:", sorted(team))

ivanov_count = team.count("Иванов")
if "Иванов" in team:
    print("Фамилия Иванов входит в команду.")
else:
    print("Фамилии Иванов нет в команде.")
print("Фамилия Иванов встречается", ivanov_count, "раз(а).")