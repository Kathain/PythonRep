# конструкторы в классах и переопределение методов в классаъ


class Cars:
    wheels = 0
    marka = ""

    def __init__(self, wheels, marka):
        self.wheels = wheels
        self.marka = marka


bmw = Cars(4, "X3")  # Сразу добавили характеристики
print(bmw.wheels)  # Результат - 4