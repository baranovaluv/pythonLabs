def create_ru_en_dictionary(input_file, output_file):

    ru_en_dict = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ' - ' not in line:
                continue

            en_word, ru_translations = line.split(' - ', 1)
            en_word = en_word.strip()

            for ru_word in [x.strip() for x in ru_translations.split(',')]:
                if ru_word not in ru_en_dict:
                    ru_en_dict[ru_word] = set()
                ru_en_dict[ru_word].add(en_word)

    sorted_ru_words = sorted(ru_en_dict.keys(), key=lambda x: x.lower())

    with open(output_file, 'w', encoding='utf-8') as f:
        for ru_word in sorted_ru_words:
            en_words = sorted(ru_en_dict[ru_word])
            f.write(f"{ru_word} - {', '.join(en_words)}\n")



input_filename = 'en-ru.txt'
output_filename = 'ru-en.txt'
create_ru_en_dictionary(input_filename, output_filename)

print(f"Русско-английский словарь успешно создан и сохранен в файл {output_filename}")