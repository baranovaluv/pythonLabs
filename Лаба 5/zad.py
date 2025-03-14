def concatenate_words():
#     words = []
#     n = int(input("Введите количество слов: "))
#
#     for _ in range(n):
#         word = input("Введите слово: ")
#         words.append(word)
#
#     result = " ".join(words)
#     return result
#
# concatenated_string = concatenate_words()
# print("Результирующая строка:", concatenated_string)



# def concatenate_words():
#     words = []
#
#     while True:
#         word = input("Введите слово (или 'stop' для завершения): ")
#         if word.lower() == "stop":
#             break
#         words.append(word)
#
#     result = " ".join(words)
#     return result
#
# concatenated_string = concatenate_words()
# print("Результирующая строка:", concatenated_string)


# def check_rare_word():
#     while True:
#         word = input("Введите слово (или 'stop' для завершения): ")
#         if word.lower() == "stop":
#             break
#
#         if 'ф' in word:
#             print("Ого! Это редкое слово!")
#         else:
#             print("Эх, это не очень редкое слово...")
#
# check_rare_word()


import random



import random

def game():
    err = 0
    correct = 0

    while err < 3:
        x, y = random.randint(1, 10), random.randint(1, 10)
        ans = x + y

        try:
            user_input = int(input(f"{x} + {y} = "))
            if user_input == ans:
                print("Правильно!")
                correct += 1
            else:
                print("Ответ неверный.")
                err += 1
        except ValueError:
            print("Пожалуйста, введите число.")
            err += 1

    print(f"Игра окончена. Правильных ответов: {correct}")

game()