# словари
# в словарях вместо индексов - используют ключи

# 1 способ
# словари только в фигурных скобках
# 'test': 1  где 'test' это имея а 1 это значение

d = {'test': 1, 'test_2': "teST"}
print(d['test_2'])

# 2 способ

ko = dict(short='dict', longer='dictionary')
ko['short'] = '234' # тут меняем значение у short
print(ko)


# 23 это ключ - 34 это значение
ra = dict([(23, 34), (56, 87)])
print(ra)

# 3 способ

g = dict.fromkeys(['a', 'b']) # с помощью fromkeys мы можем создать много клюяей без значений
print(g)

ga = dict.fromkeys(['a', 'b'], 1) # для всех ключей будет значение 1
print(ga)

# 4 способ

ji = {a: a ** 2 for a in range(7)}
print(ji)

person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'}, 'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'], 'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}
print(person['name']['first_name'])
print(person.values()) #values возвращает все значения в словае




