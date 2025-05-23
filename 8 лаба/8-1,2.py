countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Япония": "Токио",
    "Германия": "Берлин",
    "Италия": "Рим"
}

print("Все страны и столицы:")
for country, capital in countries.items():
    print(f"{country} — {capital}")

country_to_find = "Япония"
print(f"\nСтолица страны {country_to_find}: {countries.get(country_to_find)}")

print("\nСортированный список стран и столиц:")
for country in sorted(countries):
    print(f"{country} — {countries[country]}")


points = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

letter_scores = {}
for point, letters in points.items():
    for letter in letters:
        letter_scores[letter] = point

word = input("Введите слово: ").upper()
score = sum(letter_scores.get(letter, 0) for letter in word)
print(f"Стоимость слова «{word}» — {score} очков.")