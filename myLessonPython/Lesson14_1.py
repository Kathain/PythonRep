# мои пробы связанные с созданием обьектов в питоне

class Animals:
    type_cat = "Cat"
    type_dog = "Dog"

    def set(self, type_cat, type_dog):
        self.type_cat = type_cat
        self.type_dog = type_dog

        if input("Myau"):
            print(self.type_cat)
        elif input("Wouw"):
            print(self.type_dog)
        else:
            print("You entered the wrong animal sound")

        type_cat = Animals()
        type_cat.set("Moew", "Wouw")
        print(type_cat, type_dog)

