# декораторы - это обертка для функций

# тут создаем функцию декоратор
def decorator (func):
    def wrapper():
        print("Код до выполнения функции")
        func()
        print("Код который сработал после функции")
    return wrapper

# тут создаем саму функцию

@decorator      # через собаку можно сразу вызвать декоратор к этой функции через название декоратора
def show():
    print("Я обычная функция")

#show = decorator(show)
show()


#show()
#dec = decorator(show)
#dec()