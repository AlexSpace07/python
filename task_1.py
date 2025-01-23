# TODO Написать 2 класса с документацией и аннотацией типов


# Класс №1 - Ноутбук

class Laptop:
    """
    Класс, описывающий ноутбук.
    >>> laptop = Laptop("ASUS", 50)
    >>> laptop.charge(30)
    80
    >>> laptop.power_on()
    >>> laptop.is_on
    True
    >>> laptop.power_off()
    >>> laptop.is_on
    False
    """

    def __init__(self, brand: str, battery_capacity: int):
        """
        Создаёт объект ноутбука.
        :param brand: Производитель ноутбука.
        :param battery_capacity: Ёмкость батареи (в %). Должна быть от 0 до 100.
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой.")
        if not (0 <= battery_capacity <= 100):
            raise ValueError("Ёмкость батареи должна быть в диапазоне от 0 до 100.")

        self.brand = brand
        self.battery_capacity = battery_capacity
        self.is_on = False  # Состояние ноутбука

    def power_on(self) -> None:
        """Включает ноутбук."""
        if self.battery_capacity == 0:
            raise ValueError("Невозможно включить ноутбук: батарея разряжена.")
        self.is_on = True

    def power_off(self) -> None:
        """Выключает ноутбук."""
        self.is_on = False

    def charge(self, amount: int = 10) -> int:
        """
        Заряжает ноутбук.
        :param amount: Процент заряда (по умолчанию 10%). Должен быть положительным.
        :return: Текущий уровень заряда батареи.
        """
        if amount <= 0:
            raise ValueError("Зарядка должна быть положительным числом.")
        self.battery_capacity = min(self.battery_capacity + amount, 100)
        return self.battery_capacity

# Класс №2 - Чайник


class Kettle:
    """
    Класс, описывающий чайник.
    >>> kettle = Kettle("Xiaomi", 1)
    >>> kettle.refuel(1)
    2
    >>> kettle.power_on()
    >>> kettle.is_on
    True
    >>> kettle.power_off()
    >>> kettle.is_on
    False
    """

    def __init__(self, brand: str, water_capacity: int):
        """
        Создаёт объект чайник.
        :param brand: Производитель чайника.
        :param water_capacity: Ёмкость воды (в %). Должна быть от 0 до 100.
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой.")
        if not (0 <= water_capacity <= 100):
            raise ValueError("Ёмкость воды должна быть в диапазоне от 0 до 100.")

        self.brand = brand
        self.water_capacity = water_capacity
        self.is_on = False  # Состояние чайника

    def power_on(self) -> None:
        """Включает чайник."""
        if self.water_capacity == 0:
            raise ValueError("Невозможно включить чайник")
        self.is_on = True

    def power_off(self) -> None:
        """Выключает чайник."""
        self.is_on = False

    def refuel(self, amount: int = 10) -> int:
        """
        Наполнение чайника
        :param amount: Процент воды (по умолчанию 10%). Должен быть положительным.
        :return: Текущий уровень жидкости в процентах.
        """
        if amount <= 0:
            raise ValueError("Емкость должна быть положительным числом.")
        self.water_capacity = min(self.water_capacity + amount, 100)
        return self.water_capacity

# TODO работоспособность экземпляров класса проверить с помощью doctest


import doctest

if __name__ == "__main__":
    doctest.testmod()

# Тестирование примеров, которые находятся в документации

    laptop = Laptop("ASUS", 50)
    kettle = Kettle("Xiaomi", 1)


# Тестирование методов классов с корректными аргументами

    print(laptop.charge(30))    # Ожидается: 80
    laptop.power_on()   # Ноутбук включен
    print(laptop.is_on)     # Ожидается: True
    laptop.power_off()     # Ноутбук выключен
    print(laptop.is_on)     # Ожидается: False

    print(kettle.refuel(1))     # Ожидается: 2
    kettle.power_on()       # Чайник включен
    print(kettle.is_on)     # Ожидается: True
    kettle.power_off()       # Чайник выключен
    print(kettle.is_on)     # Ожидается: False


# Проверка обработки ошибок через try...except

    try:
        laptop.charge(-20)  # Некорректное количество заряда
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        laptop.power_on()  # Попытка включить ноутбук с разряженной батареей
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

    try:
        kettle.refuel(-2)  # Некорректное количество воды
    except ValueError as e:
        print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке

        try:
            kettle.power_on()  # Попытка включить чайник с некорректным значением жидкости
        except ValueError as e:
            print(f"Ошибка: {e}")  # Ожидается сообщение об ошибке
