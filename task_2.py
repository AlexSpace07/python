# TODO импортировать необходимые молули

# Импорт модулей

import csv
import json

# Имя входного csv файла
INPUT_FILENAME = "input.csv"

# Имя выходного json файла
OUTPUT_FILENAME = "output.json"


# Конвертация содержимого csv файла в json файл
def task() -> None:

    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as file:
        lines_ = [line for line in csv.DictReader(file)]
    # Преобразование строки в список

    # Открываю json файл для записи и сохраняю туда данные с отступами для читаемости
    with open(OUTPUT_FILENAME, "w") as file:

        # TODO Сериализовать в файл с отступами равными 4
        json.dump(lines_, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Вывод содержимого
    with open(OUTPUT_FILENAME) as output_file:
        for line in output_file:
            print(line, end="")
