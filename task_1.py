class Prossesor:

    def __init__(self, architecture: str, core: int, clock: float):

        """
            Инициализация экземпляра класса, который хранит в себе общие сведения про котов и кошек:
            :param clock: частота
            :param architecture: архитектура
            :param core: количество ядер
        """
        self.architecture = architecture
        self.core = core
        self.clock = clock

    def __str__(self):
        """
            Используем метод __str__
            чтобы оформить табличку
        """
        return f"\n Архитектура: {self.architecture}" \
               f"\n Количество ядер: {self.core}" \
               f"\n Частота: {self.clock}" \
               "\n (str)"

    def __repr__(self):
        """
            Используем  метод __repr__
            чтобы оформить табличку

        """
        return f"\n Архитектура: {self.architecture}, Ядро: {self.core}, Частота: {self.clock} (repr)"


class Intel(Prossesor):
    """
        Первый класс, в котором используется наследование из класса Prosseror
        Класс будет создавать процессоры
    """

    def __init__(self, name: str, architecture, core, clock):
        """
            Такие параметры, как:
                :param clock: частота
                :param architecture: архитектура
                :param core: количество ядер
                :param vendor: производитель (Этот параметр будет иметь фиксированное значение - Intel)
        """

        super().__init__(architecture, core, clock)
        self.vendor = "Intel"
        self.name = name

    def __str__(self):
        """
            Используем метод __str__  чтобы оформить карточку
            Часть карточки мы наследуем из оригинального класса.
        """
        return f"Характеристики процессора с индексом: {self.name}" \
               f"\n Производитель: {self.vendor} {super().__str__()}"

    def __repr__(self):
        """
            Используем  метод __repr__
        """
        return f"\n Производитель: {self.vendor} {super().__repr__()}"


class AMD(Prossesor):
    """
        Второй класс, в котором используется наследование из класса Prosseror
        Класс будет создавать процессоры
    """

    def __init__(self, name: str, architecture, core, clock):
        """
            Такие параметры, как:
                :param clock: частота
                :param architecture: архитектура
                :param core: количество ядер
                :param vendor: устройство (Этот параметр будет иметь фиксированное значение - AMD)
        """

        super().__init__(architecture, core, clock)
        self.vendor = "AMD"
        self.name = name

    def __str__(self):
        """
            Используем метод __str__  чтобы оформить карточку
            Часть карточки мы наследуем из оригинального класса.
        """
        return f"Характеристики процессора с индексом: {self.name}" \
               f"\n Производитель: {self.vendor} {super().__str__()}"

    def __repr__(self):
        """
            Используем  метод __repr__
        """
        return f"\n Производитель: {self.vendor} {super().__repr__()}"


if __name__ == "__main__":
    """
        В консоли мы увидим аккуратные таблички квадратики (str), 
        а в режиме отладки, если написать котика самому, можем увидеть красивые строчки (repr)
    """
    in1 = Intel("Core 9 285K", "x86", 24, 3.7)
    am1 = AMD("Ryzen 9 9950X", "AMD64", 16, 4.3)
    print(in1)
    print(am1)
    pass
