# TODO решите задачу

# Импорт модуля для работы с json данными
import json


# Возвращение числа с плавающей запятой
def task() -> float:
    file = "input.json"

# Загрузка содержимого из файла
    with open(file) as file:
        json_data = json.load(file)

    # Вычислениесуммы произведений
    sumv = sum([item["score"] * item["weight"] for item in json_data])

    # Округление результата до трех знаков после запятой
    return round(sumv, 3)


print(task())
