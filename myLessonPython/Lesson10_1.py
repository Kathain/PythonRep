# исключения в языке питон

try:
    x = int(input())
except ValueError:  #есть разные кода ошибок - это одна из них проверка на число
    print("Вы ввели не число")
    x = 0
try:
    y = int(input())
except ValueError:
    print("Вы ввели не число")
    y = 0
else:        #выполянется тогда - когда у нас нет ошибки
    print("Все верно")
finally:  #конструкция которая выполняется всегда 100 процентов
        print("100 процентов верно")
try:
    res = x / y
except ZeroDivisionError:
    print("Вы ввели ноль")
    res = 0
print(res)




