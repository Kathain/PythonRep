
# ооп в питоне
# ооп - это обьекты и классы (в классах создаются обеькты)
# с ооп программа более читабельна, более структурирована, и больще людей над ней могут работать
# важнейшие моменты ооп - Наследование, инкапсуляция, полиморфизм
# инкапсуляция - это защита данных (ограничение доступа к полям или методам) _name нужно использовать нижнее подчеркивание
# __два нижних подчеркивания это как private
# полиморфизм - это когда мы можем использовать один и тот метод но по разному в разных классах

class Person:
    name = "Ivan"
    age = 10

    def __init__(self, name, age):   #тут создали конструктор
        self.name = name
        self.age = age

    def set(self, name, age):     # создаем функцию (method)
        self.name = name
        self.age = age

class Student(Person):  # тут создали наследованиие другого класса
    cource = 1

igor = Student("vova",12)
# igor.set("Loli",19)
print(igor.name)






vlad = Person()  # тут создали обьект
vlad.name = "Vlad"
vlad.age = 45
print(vlad.name)
print(vlad.age)

kola = Person()
kola.name = "Kola"
print(kola.name)

mimi = Person()   #тут используем именно созданный метод
#mimi.set("Мими", 25)
print(mimi.name + " " + str(mimi.age))

print(2 + 2)