
class Car:
    color = "Black"
    model = "HG56"
    year = 2007
    price = 7000

    def set(self, color, model, year, price):
        self.color = color
        self.model = model
        self.year = year
        self.price = price

car1 = Car()
car1.set("Red", "KLL86", "1995", "4000")
print("Цвет машины - " + car1.color + " " + "Модель машины - " + car1.model + " " + "Год машины - " + car1.year + " " + "Цена машины - " + car1.price)
