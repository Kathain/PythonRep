a = {32, 45, 43.23, 76}
x = 45
print(x in a) # тут проверяется если ли такое значение как x (а точнее 45) в переменной ] a
print(len(a))  # показывет количество элементов в нашем множестве

b = {32, 45, 43.23, 76}
z = {67, 12, 90}
print(b.isdisjoint(z))  # эта функция возвращает тру - если нет в переменных ничего одинакового (цифры разные например)

l = {32, 48, 12, 76}
g = {12, 19, 13, 66}
print (l == g) #тут проверяется равны ли они

v = {32, 45, 43.23, 76}
n = {67, 12, 90}
v.update(n)  #она будет обьеденять несколько множеств
print(v)

ko = {32, 45, 43.23, 76}
la = {67, 12, 90, 76}
ko.intersection_update(la)  #она показывает есть ли одинаковые значения , и если да - то выводит само значение на экран
print(ko)

j = {32, 45, 43.23, 76}
m = {67, 12, 90, 76}
j.difference_update(m) # показывает пересечение, показывает например каких из чисел в j нет в m - 32, 45, 43.23
print(j)

pu = {32, 45, 43.23, 76}
hu = {67, 12, 90, 76}
pu.symmetric_difference_update(hu) # множество из элементов встречабщихся в одной но не встречающихся в обеих
print(pu)
pu.remove(43.23)   # удаляет число в множестве
print(pu)

hu.pop()  #функция удаляет рандомный элемент
print(hu)

hu.clear() #очищает множество