# исключения в языке питон

x = int(input("Введи число "))
y = int(input("Введи второе число "))

try:
    res = x / y
except ZeroDivisionError:  #есть разные кода ошибок - это одна из них
    print("Вы ввели 0")
    res = 0
print(res)
