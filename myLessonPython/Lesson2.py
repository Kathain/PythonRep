# В этом уроке изучаем Если - то

num = input("Введите ваше имя: ")

if num == "Test" :
    print("True\n")
    print("All is OK")


num2 = input("Введите число : ")

if int(num2) > 0:
    print("Вы ввели число больше нуля")
    print("All is OK")
    if int(num2) > 50:
        print("Вы ввели число больше 50")

elif int(num2) < -10:
    print("Вы ввели число меньше -10")
else:
    print("Вы ввели число меньше нуля но больше 10")

name = input()
A = 'Yes' if name != "Test" else 'No'

print(A)