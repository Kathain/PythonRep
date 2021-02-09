# тут учим функции

# функции это подпрограмма которую мы можем вызывать через под

def func(x, a):
    return x + a

print(func(23, 12))


# вариант 2


def func1(x1, a1):
    res = x1 + a1
    return res

print(func1(23, 12))

# вариант 3

def olk(m):
    def add(o):
        return m + o
    return add

test = olk(100)
print(test(200))

# вариант когда функция ничего не возвращает

def kaki():
    x = 34
    y = 45
    pass

print(kaki())

# вариант передачи аргумента по умолчанию

def olli(r, w, y = 2):
    ses = r + w
    ses *= y
    return ses
print(olli(2,4,3))

# вариант если не знаем сколько хотим передать параметров

def olli(*q):
    return q
print(olli(2,4,3))  # создается по факту обычный кортеж

# вариант если хотим выводить в виде словаря

def olli(**q):
    return q
print(olli(a=23, n=56, o=90))  # создается словарь

# вариант с функцией LAMBDA

add = lambda x, y: x * y
print(add(2,5))
print(add('q',2))

print((lambda x, y: x * y)(2, 6)) #еще один вариант ламбды

fun = lambda *args: args  #еще один варитант
print(fun(2, 56, 78.56))