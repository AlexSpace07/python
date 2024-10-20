numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

missing_item = 4

# Расчет суммы чисел
summa = sum(numbers[:missing_item]) + sum(numbers[missing_item+1:])

# Количество чисел в списке
count = len(numbers)

# Среднее арифметическое чисел
average = summa / count

# Замена пропущенного элемента на среднее арифметическое
numbers[missing_item] = average

# Вывод изменненого списка
print("Измененный список:", numbers)
