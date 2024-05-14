# Типы
# print(f'Hi, Vlad')
# print(f'Vlad, type {type("Vlad")}')
# print(f'{1}, type {type(1)}')
# print(f'{True}, type {type(True)}')
# print(f'{[1, "abc", True]}, type {type([1, "abc", True])}')
# print(f'{{"int": 1, "string": "abc", "boolean": True}}, type {type({"int": 1, "string": "abc", "boolean": True})}')

# Трюки с строками
# n: int = 1_000_000_000
# print(n)
# n: int = 1000000000 #только такие сепараторы , _ другие работать не будут
# print(f'{n:,}')
# print(f'{n:_}')
# var: str = 'var'  # Добавить пробелы
# print(f'{var:<20}:')
# print(f'{var:>20}:')
# print(f'{var:^20}:')
# print(f'{var:_^20}:')
# print(f'{var:.<20}:')
# Полезные трюки
# Модель соединения
# Запустим модель от сюда
# from hacks import connect
#
# connect()  # Мы увидим что соединение идет циклично, что же делать, идем в модуль

# from datetime import datetime
# now: datetime = datetime.now()
# print(f'{now:%d.%m.%y (%H:%M:%S)}')  # own format date
# print(f'{now:%c}')  # local version date
# print(f'{now:%I%p}')  # local version date

# f: float = 1234.56789
# print(f'{f:.2f}') # round to 2 after dote
# print(f'{f:.0f}') # round to 0 after dote
# print(f'{f:,.3f}') # round to 3 after dote + separator

# a: int = 5
# b: int = 10
# var: str = 'Text'
# print(f'a + b = {a + b}')
# print(f'{a + b = }')  # shorter to write
# print(f'{bool(a) = }')
# print(f'{var = }')

# Встроенные функции
# print type id len sum input round min max int str bool ... etc
# print(print)
# name = input("Enter you name: ")
# print(name)
# name = 'Vlad'
# print(dir(name))  # dir отображает имена всех атрибутов объекта
# print(name.__doc__)

# # К примеру в списке есть lower
# print(name.lower())
# print(name.upper())

# Свои функции
# def my_fn(a, b):
#     a = a + 1
#     c = a + b
#     return c
#
#
# print(my_fn(1, 2))

# print(dir(__builtins__)) # Список всех строенных функций в python к примеру print

# name = input("Enter you name: ")
# # print(dir(name))
# age = input("Enter you age: ")
# male = input("Enter you male: ")
#
# print(f'Your name: {name.capitalize()}, age: {age}, male: {male.upper()}')

# my_list = [1, 2, 3]
# print(my_list)

# def hello():
#     print('Hello world!')
#
# def hello(name):
#     print('Hello world!', name)
#
#
# hello('Vlad')

# def sum_numbs(a, b):
#     sum = a + b
#     # print(sum)
#     return sum
#
#
# res1 = sum_numbs(10, 5)
# print(res1)
# res2 = sum_numbs(50.5, 29)
# print(res2)

# Результат выполнения функции/действия называют Выражением

# print(10 + 5)

# Не знаю почему, но он условия выполнения кода назвал Инструкцией

# name = 'Vlad'  # присвоение значения

# Условная инструкция
# if name:
#     print(name.upper())

# Импортирования модуля
# import datetime
#
# print(datetime.MAXYEAR)

# Переменные/функции/методы/модули пример snake_case
# Классы PascalCase
# Пакеты или наборы модулей my-package
# Константы DB_USER

# Все в python являються объектами, что имеется в виду.
# Каждый символ занимает место в ячейки памяти компьютера/сервера и они являються объектами.
# Есть два типа объектов мутационные и не мутационные, что дальше назвем изменяемые и не изменяемые объекты.
# Основные типы не изменяемых: string, boolean, integer, float, tuple(Картежи), None (Ничто).
# Основные типы изменяемых: list(список), dict(словарь), set(набор), пользовательские какие либо

# Переменные по сути своей ссылка на объект в памяти пк
# функция id(имя переменной) адрес объекта или переменной в памяти
# К примеру почему переменная является ссылкой name = 'Vlad', new_name = name, old_name = name.
# Мы не создаем новый объект в памяти, а копируем адрес объекта.

# name = 'Vlad'
# print(id(name))
# new_name = name
# print(id(new_name))
# old_name = name
# print(id(old_name))

# Ctrl + right or left перемещение по тексту лево/право
# ALT + up or down перемещение вверх/вниз
# Ctrl + Shift перемещение строки вверх/вниз

# long_str = '''This
# is a very
# long string'''
# print(long_str)
# print(type(long_str))  # Тип
# print(id(long_str))  # Его адрес в памяти
# print(len(long_str))  # длина строки
# print(long_str[5:15])  # получение конкретного диапазона
# print(long_str.upper())
# print(long_str.count('is'))
# print(long_str.index('is'))
# print(long_str.capitalize())
# print(long_str.lower())
# print(long_str.replace('very', 'much')) # Методы не заменяют оригинальную переменную.
# Он только преобразует ответ. Можна записать в новую переменную или заменить

# my_comment = 'This is my short comment'
# print(len(my_comment))

# friends_qty = 50
# print(friends_qty)
# print(type(friends_qty))
#
# any_num = input('Enter any number')
# print(any_num)
# print(type(any_num))
#
# user_number = input('Enter any number')
# any_num = int(user_number)
# print(any_num)
# print(type(any_num))
#
# any_num = int(input('Enter any number'))
# print(any_num)
# print(type(any_num))

# Возведение в степень
# base = 5
# power = 3
# my_pow = pow(base, power)
# print(my_pow)
# print(type(my_pow))

# # Для удобства чтения кода можно разделять числа _
# one_million = 1_000_000
# print(one_million)
# my_number = 3_427
# print(my_number)

# input_str = input('Enter any number: ')
# input_int = int(input_str)
# print(input_str)
# print(type(input_str))
# print(input_int)
# print(type(input_int))

# Float Десятичные

# average_price = 17.25
# print(average_price)
# print(type(average_price))

# average_price = 28.75
# price = int(average_price)
# print(price)
# print(type(price))
# print(round(average_price))
# str_tmp = '14.5'
# temp = float(str_tmp)
# print(temp)
# print(type(temp))

# Комплексные числа
# complex_a = 3+5j
# complex_b = 4+7j
# sum_complex = complex_a + complex_b
# print(sum_complex)
# print(type(sum_complex))

# Логические True or False
# is_auth = True
# print(is_auth)
# print(type(is_auth))
# print(100 > 24)  # True
# print(-5 > 0)  # False
# print('Long string' > 'Long')  # True сравнивает по количеству символов
# print([1, 2, 3] == [1, 2, 3])  # True
# bool(10)
# bool('10')
# bool([])
# bool([1,2])
# bool(None)
# print({'a': 3} == {'a': 5})

# Конвертация типов
# Python не выполняет неявную конвертацию типов значений
# str(), float(), int(), tuple(), list(), set(), dict() ...

# '10' + 2 # TypeError: can only concatenate str (not "int") to str
# 5 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# int_num = 5
# float_num = 4.5
# print(int_num + float_num)
# print(int_num.__add__(float_num)) # __add__ (магический метод добавления int) = int_num + float_num
# NotImplemented = означает что добавление не реализовано, потому что разные типы данных it and float
# print(float_num.__radd__(int_num)) # __radd__ (магический метод добавления float) = int_num + float_num но отличия от
# add он рассчитан на целые числа и потому ошибок не будет

# магический методы примеры (можна посмотреть через dir)
# int_num = 50
# float_num = 7.5
# print(int_num + float_num)
# print(int_num * float_num)
# print(int_num.__mul__(float_num))
# print(float_num.__rmul__(int_num))
# print(float_num.__rsub__(int_num))
# print(float_num.__rmod__(int_num))
# print(float_num.__rfloordiv__(int_num))
# print(float_num.__rtruediv__(int_num))
# print(help([].__eq__)) # Вызвать подсказки, что бы понимать как работает метод

# Списки
# my_fruits = ['apple', 'banana', 'lime']
# posts_ids = [151, 245, 762, 167]
# user_inputs = [True, 'Hi!', "👉", 10.5]
# print(len(my_fruits))
# print(posts_ids[0])
# print(user_inputs)
# user_inputs[0] = False
# user_inputs[3] = 11.5
# print(user_inputs)
# del posts_ids[2]
# print(posts_ids)
# Не забываем что можна комбинировать,
# часто используется список словарей
# users = [
#     {
#         'user_id': 1,
#         'user_name': 'Alice'
#     },
#     {
#         'user_id': 2,
#         'user_name': 'Maks'
#     }
# ]
# print(len(users))
# print(users[0]['user_id'])
# apple = 'apple'
# banana = 'banana'
# lime = 'lime'
# all_fruits = [apple, banana, lime]
# print(all_fruits)
# posts_ids = [151, 245, 762, 167]
# print(posts_ids[10])  # IndexError: list index out of range Такого елемента нет в списке

# Методы для списков

# append(добавить в конец),
# pop(удалить последний елемент или заданный),
# remove,
# insert,
# sort(), sort(reverse=True) сортировка по порядку и обратно
# index,
# clear,
# copy,
# extend,
# reverse,
# count

# Конвертация в список

# hi = 'Hello from Python'
# letters = list(hi)
# print(letters)
# my_dict = {'a': 10, 'b': 90}
# dict_keys = list(my_dict)
# print(dict_keys)
# rating = [2.5, 5.0, 4.3, 3.7]
# print(min(rating))
# print(max(rating))
# print(sum(rating))
# print(sum(rating) / len(rating))

# Копируем списки
# my_fruits = ['apple', 'banana', 'lime']
# copied_cars1 = my_fruits[:]
# copied_cars2 = my_fruits.copy()
# copied_cars3 = list(my_fruits)

# Задание
# my_nums = [10, 50, 0, 5, 100]
# # print(dir(my_nums))
# del my_nums[2]
# # or
# # my_nums.pop(2)
# print(len(my_nums))
# my_nums.sort()
# # or
# # my_nums.reverse()
# my_new_list = [2, 12]
# my_nums.extend(my_new_list)
# print(my_nums)

# Задание 2
# l1 = [1, 2, 3, 4, 5]
# l2 = [5, 4, 3, 2, 1]
# l3 = l1 + l2
# l4 = l1.__add__(l2)
# print(l3)
# print(l4)

# Словари dict {'key':'value'}

# my_bike = {
#     'brand': 'Ducati',
#     'price': 2500,
#     'engine_vol': 1.2
# }
# print(dir(my_bike))
# my_dict = {}
# print(my_dict.__doc__)
# print(my_bike['brand'])
# print(my_bike['price'])
# my_bike['price'] = 2000
# print(my_bike['price'])
# my_bike['is_new'] = True
# print(my_bike)
# del my_bike['engine_vol']
# print(my_bike)
# # пример ключей с базы
# key_name = 'engine_vol'
# my_bike[key_name] = 1.5
# print(my_bike)
# my_bike['price_info'] = {}
# my_bike['price_info']['price'] = my_bike['price']
# del my_bike['price']
# print(my_bike)
# print(len(my_bike))
# # print(my_bike['model']) # Ошибка и программа закончиться
# print(my_bike.get('model'))
# print(my_bike.get('model', 'No models'))
# print(my_bike.get('brand'))


# print(id(my_bike))
# print(type(my_bike))
# print(my_bike.__doc__)
# print(my_bike.items())
# print(type(my_bike.items()))
# print(my_bike.keys())
# print(list(my_bike.keys()))
# print(my_bike.popitem())  # Удалил последний елемент (не рекомендуют)
# new_bike = my_bike.copy()
# new_bike['type'] = 'elect'
# print(new_bike)

# Конвертация списка или кортежа в словарь
# my_list = [0, True, 'abc']
# my_dict = dict(my_list)
# print(my_dict)
# my_list = [['first', 0], ['second', True]]  # Словарь
# my_list = [('first', 0), ('second', True)]  # Картеж
# my_dict = dict(my_list)
# print(my_dict)

# Задача
# my_dict = {}
# key1 = input('Key 1:')
# value1 = input('Value 1:')
# my_dict[key1] = value1
# key2 = input('Key 2:')
# value2 = input('Value 2:')
# my_dict[key2] = value2
# key3 = input('Key 3:')
# value3 = input('Value 3:')
# my_dict[key3] = value3
# print(my_dict)

# Кортежи - упорядоченная последовательность элементов
# По сути тот же список, но кортеж НЕ изменяемые (удали, добавить и т.д. НЕЛЬЗЯ)
# my_tuple = ('a', 2, True, '🔥')
# my_tuple = ('a', 2, True, '🔥')

# Наборы - НЕ упорядоченная последовательность элементов
# Тот же словарь, но без ключей
# users_inputs = {'a', 2, True, '🔥'}
# users_inputs_dict = {'str': 'a', 'int': 2, 'bool': True, 'random': '🔥'}
# print(type(users_inputs))
# print(type(users_inputs_dict))
# # Зачем он нужен, что бы убрать дубликаты при создании, добавлении елементов, порядок не важен
# ids: set[int] = {1, 2, 3, 4, 1, 3, 5}
# ids.add(6)
# ids.add(7)
# ids.add(7)
# print(type(ids))
# print(ids)

# Методы набора, за счет их это становиться мощным инструментом
# add, union, remove, difference, intersection (пересечение),
# discard, clear, copy, update, issubset (входит ли один набор в другой), issuperset, pop
# photo_size: set[str] = {'1920x1080', '800x600'}
# photo_size.add('1024x768')
# print(photo_size)
# other_sizes: set[str] = {'800x600', '1024x628'}
# all_sizes: set[str] = photo_size.union(other_sizes)
# print(all_sizes)
# common_s: set[str] = photo_size.intersection(other_sizes)
# print(common_s)

# nums: set[int] = {10, 5, 35}
# other_nums: set[int] = {20, 5, 12, 10, 35}
# res: bool = nums.issubset(other_nums)
# print(res)

# Практика
# my_set: set[str] = {'abc', 'd', 'f', 'y'}
# other_set: set[str] = {'a', 'f', 'd'}
# print(my_set.intersection(other_set))
# print(other_set.intersection(my_set))
# print(my_set.intersection('abc'))
# print(my_set.intersection('abcd') == my_set.intersection(['a', 'b', 'c', 'd']))
# print(my_set.union(other_set))
# print(my_set.issubset(other_set))
# print(my_set.issuperset({'f', 'd'}))
# print(other_set.issubset(my_set))
# print(my_set.difference(other_set))
# my_set.discard('abc')
# print(my_set)
# my_set.discard('def')
# print(my_set)
# # my_set.remove('def') #Будет ошибка в отличии от discard
# # print(my_set)
# new_set:set[str] = my_set.copy()
# new_set.add('t')
# print(new_set)
# print(my_set.symmetric_difference(new_set))

# Задача
# my_set: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# my_set.add(10)
# other_set: set[int] = {2, 12, 3, 23, 56, 7}
# new_set: list[int] = list(my_set.intersection(other_set))
# print(type(new_set))
# print(new_set)

# Диапазоны - упорядоченная НЕ изменяемая последовательность элементов.
# Используются в циклах

# my_range = range(7)
# print(type(my_range))
# print(my_range)
# print(list(my_range))

# my_range = range(10, 20, 3)  # 10 - 20 диапазон и шаг 3
# print(type(my_range))
# print(my_range)
# print(list(my_range))
# print(my_range[1])
# Использование в цикле
# for n in my_range:
#     print(n)


# Практика
# my_range = range(5)
# print(type(my_range))
# print(my_range)
# # print(my_range[-1])
# for n in my_range:
#     print(n)
# print(my_range.count(10))
# print(my_range.start)
# print(my_range.stop)
# print(my_range.step)
# print(my_range.index(2))

# Сравнение типов ❌ ✅
# Тип  изменения порядок одинаковые эелементы  рекомендация данных
# list    ✅       ✅       ✅                  Упорядоченная последовательность
# tuple   ❌       ✅       ✅                  Нельзя изменять элементы
# set     ✅       ❌       ❌                  Уникальность
# range   ❌       ✅       ❌                  Н раз действия
# dict    ✅       ❌       ❌                  Спряденные данные и большие
# str     ❌       ✅       ✅


# Встроенная функция ZIP (объединение объектов)
# fruits = ['apple', 'banana', 'lime']
# quantities = [100, 70, 50]
# sailed = (True, False, True)
# # fruit_qty_zip = zip(fruits, quantities, sailed)
# fruit_qty_zip = zip(fruits, quantities)
# print(fruit_qty_zip)
# # fruit_qty_list = list(fruit_qty_zip)
# # print(fruit_qty_list)
# # Поскольку зип храниться в паяти,
# # мы его преобразовали в лист и дикт не отработал
# fruit_qty_dict = dict(fruit_qty_zip)
# print(fruit_qty_dict)

# Изменение объектов
# Это касается НЕ изменяемых объектов
# number_1 = 10
# number_2 = 10
# number_3 = 10
# print(id(number_1))
# print(id(number_2))
# print(id(number_3))
# Суть такая что python проверяет нет ли такого же
# объекта в памяти и если существует, то присваивает один и тот же адрес

# Это касается изменяемых объектов
# my_list_1 = [1, 2, 3]
# my_list_2 = [1, 2, 3]
# print(id(my_list_1))
# print(id(my_list_2))
# my_list_3 = my_list_1
# print(id(my_list_1))
# print(id(my_list_3))
# my_list_3.append(4)
# print(my_list_1)
# print(my_list_3)
# Суть такая, что если вы присваете новой переменной
# значения другой переменной изменяемых объектов (НЕ copy),
# то они будут изменяться все одновременно.

# Как избежать изменения копий
# info = {
#     'name': 'Bob',
#     'is': True,
#     'reviews': []
# }
# info_copy = info.copy()
# info_copy['reviews'].append('Great course!')
# print(info)
# print(info_copy)
# Как видишь если в словаре есть список, словарь
# или что-то изменяемое второго прядка reviews,
# то оно присваивает адрес в ячейки первого и изменяет оба объекта

# Как скопировать так что бы избежать такого
# from copy import deepcopy
# info_copy_deepcopy = deepcopy(info)
# info_copy_deepcopy['reviews'].append('Great course!')
# print(info)
# print(info_copy_deepcopy)

# Функции
# def sum_numb(a: int, b: int) -> int:
#     return a + b
#
#
# a: int = 5
# b: int = 10
# print(sum_numb(a, b))

# def my_func():
#     ...
#
# def my_func_2():
#     pass
#
# print(my_func())
# print(my_func_2())

# Передача изменяемых объектов
# def person_age(person: dict) -> dict:
#     person['age'] += 1
#     return person
#
#
# person_one: dict = {
#     'name': 'Bob',
#     'age': 21
# }
#
# person_age(person_one)
# print(person_one)

# Homework
# def merge_lists_to_dict(a: list[str], b: list) -> dict:
#     # if len(a) != len(b):
#     #     print('Lists length not same, please check it!')
#     #     return {}
#     # Вызвать ошибку руками ))) Полезно
#     assert len(a) == len(b), "Lists must be of the same length"
#     return dict(zip(a, b))
#
#
# l1 = ['one', 'two', 'three']
# l2 = [1, 2, 3]
# dict1: dict = merge_lists_to_dict(l1, l2)
# print(dict1)


# Объединение аргументов в tuple(кортеж)
# def sum_numbs(*args):
#     print(args)
#     print(type(args))
#     return sum(args)
#
#
# print(sum_numbs(1, 2, 6, 7, 9))


# def my_func(name: str, age: int) -> None:
#     print(f'Name {name}, age: {age}')
#
#
# my_func(name='Vlad', age=36)


# Для читабельности часто прописывают ключи параметров,
# если прописаны ключи, то порядок не важен,
# но лучше что бы соответствовал

# Объединение аргументов в dict(словарь)
# def get_person(**person) -> dict:
#     # print(person)
#     # print(type(person))
#     # print(person['name'])
#     # print(person['age'])
#     return person
#
#
# info: dict = get_person(name='Vlad', age=36)
# print(info)

# Задача
# def merge_lists_to_dict(a: list[str], b: list) -> dict:
#     assert len(a) == len(b), "Lists must be of the same length"
#     return dict(zip(a, b))
#
#
# l1 = ['one', 'two', 'three']
# l2 = [1, 2, 3]
# dict1: dict = merge_lists_to_dict(a=l1, b=l2)
# print(dict1)
#
#
# def update_car_info(**car) -> dict:
#     car['is_available'] = True
#     return car
#
#
# print(update_car_info(brand='BMW', price=1200))

# Значения параметров по умолчанию

# def my_func(a: int, b: int = 1) -> int:
#     return a + b
#
#
# print(my_func(1, 2))
# print(my_func(1))

# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_post(post, weekday=get_weekday()):
#     post['created_at'] = weekday
#     return post
#
#
# post = {
#     'id': 1,
#     'author': 'Vlad'
# }
#
# print(create_post(post))

# Колбэк функции

# def func():
#     pass
#
#
# def main_func(callback_func): # Если мы передаем ф-цию как параметр ОБЕЗАТЕЛЬНО её переименуем
#     callback_func()
#
#
# main_func(func)

# Пример 1
# def print_number(num: int) -> None:
#     if (num % 2) == 0:
#         print('Number is even')
#     else:
#         print('Number is odd')
#
#
# def process_number(num: int, callback_fn):
#     callback_fn(num)
#
#
# number: int = 7
#
# process_number(number, print_number)

# Правила для функций
# 1. Называть функции исходя из выполнения
# 2. Название функции начинать с глагола
# 3. Одна функция одно действие/задача
# 4. Не рекомендуется изменять внешние относительно функции переменные

# Документация функции/классов/модулей и т.д. (docstring)
# def mult_by_factor(a:int, b:int)->int:
#     """Multiplies numbers by multiplicator"""
#     return a * b
#
#
# mult_by_factor(1, 2)

# def print_numbers_info(num: int) -> None:
#     """
#     Prints whether number is event or odd
#     :param num: (int) Number to be evaluated
#     :return: None
#     """
#     if (num % 2) == 0:
#         print('Num is event')
#     else:
#         print('Num is odd')
#
#
# print_numbers_info(10)

# Область видимости определяет границы действия переменной
# Все что вне функции являються глобальной,
# что внутри функции локальной

# a = 10  # Глобальная (будет жить до конца выполнения программы)
#
#
# def my_func():
#     a = True  # Локальная (будет жить до конца выполнении функции)
#     print(a)
#
#
# print(a)

# Так же можна создать глобальную переменную внутри функции
# Но так делать не рекомендуется
# def my_func():
#     global a
#     a = True
#
#
# my_func()
# print(a)

# Операторы
# a = 10  # Присвоение =
# Операнд Оператор Операнд -> a = 10
# Арифметические
# + - * /
# Сравнения
# == != < >
# Логические
# not or and
# Текстовые
# is is not in not in
# a = [1, 2]
# b = [1, 2]
# print(a == b)
# print(a.__eq__(b))

# Унарные и бинарные операторы
# Унарные операторы всегда имеют один операнд
# -my_number
# +my_number
# not is_activated
# my_number = 10
# print(+my_number)
# print(not my_number)  # Потому что не 0 будет False
# my_bool = False
# print(+my_bool)
# Инфиксная запись
# Когда Операторы между оператоми
# a = 5
# a + b
# a += 5 # Увеличить на 5
# a == b
# a and b
# Операторы in not in
# my_car: dict = {
#     'brand': 'Toyota',
#     'price': 150
# }
# print('brand' in my_car)
# print('year' in my_car)
# print('year' not in my_car)

# Задача

# my_numbs_1: set = {1, 2, 3, 4, 5}
# my_numbs_2: set = {1, 2, 3, 4, 5}
# print(my_numbs_1 == my_numbs_2)
# print(my_numbs_1.__eq__(my_numbs_2))
# print(my_numbs_1 is my_numbs_2)
# print(list(my_numbs_1)[0] in my_numbs_2)

# Ложные значения
# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(False))
# print(bool(None))
# print(bool({}))
# print(bool([]))
# print(bool(()))
# print(bool(set()))
# print(bool(range(0)))
# print(bool(''))
# print({})
# print(not {})
# print(not not {})

# Логические операторы
# not and or
# print(not 0)
# print(not 1)
# print(10 == 10 and 11 == 11)
# print(10 == 11 and 11 == 12)
# print(10 == 11 or 11 == 11)
# print(10 == 10 or 11 == 12)
# print(10 == 11 or 11 == 12)

# Операторы**
# button: dict = {
#     'width': 200,
#     'text': 'Buy'
# }
#
# red_button: dict = {
#     **button,
#     'color': 'red'
# }
# print(button)
# print(red_button)
#
# grey_button: dict = {
#     'width': 200,
#     'text': 'Buy',
#     'color': 'grey'
# }
# blue_button: dict = {
#     **grey_button,
#     'color': 'blue'
# }
# print(grey_button)
# print(blue_button)

# button_default: dict = {
#     'text': 'Ok',
#     'width': 0,
#     'height': 0,
#     'color': 'black'
# }
# button_style: dict = {
#     'width': 200,
#     'height': 200,
#     'color': 'grey'
# }
# # Вариант 1
# # button: dict = {
# #     **button_default,
# #     **button_style
# # }
# # Вариант 2
# button: dict = button_default | button_style
#
# print(button)

# Соединение строк
# line: str = 'Hello ' + 'Python'
# print(line)
# hello: str = 'Hello'
# world: str = 'world'
# greeting: str = hello + ' ' + world
# print(greeting)

# Форматирование строк f-strings
# hello: str = 'Hello'
# world: str = 'world'
# greeting: str = f'{hello} {world}'
# print(greeting)

# lambda функции - Они всегда анонимные
# lambda parameters: expression
# Пример сравнения
# def mult(a: int, b: int) -> int:
#     return a * b
#
# lambda a, b: a * b

# Использование lambda функций

# def greeting(greet):
#     return lambda name: f'{greet}, {name}'
#
#
# morning_greeting = greeting('Good Morning')
# print(morning_greeting('Vlad'))
#
# evening_greeting = greeting('Good Evening')
# print(evening_greeting('Vlad'))

# Обработка ошибок

# print(10 / 0)

# try:
#     # Выполнение блока кода
#     pass
# except ErrorType:
#     # Этот блок выполняется в случае возникновения ошибок в блоке try
#     pass

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print('Error - Division by zero')
#
# print('Continue...')


# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(type(e))
#     print(e)
#     print(dir(e))
#     print(e.__str__())
#
# print('Continue...')

# try:
#     print('10' / 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
#
# print('Continue...')


# try:
#     print(10 / 5)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print('There was no error')  # Блок выполнения после удачной обработки
# finally:
#     print('Continue...')  # Блок выполнения не зависимости от результата

# Об роботка общим классом/все ошибки если не знаем какая может быть конкретно
# try:
#     print(10 / 0)
# except Exception as e: # Универсальный метод
#     print(e)
#
# # OR
#
# try:
#     print(10 / 0)
# except: # Не Рекомендуют
#     print('Some error occurred')

# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)
#     print(isinstance(e, str))
#     print(isinstance(e, ZeroDivisionError))
#     print(isinstance(e, Exception))
#
# print('Continue...')

# def divide_nums(a: int, b: int) -> float:
#     if b == 0:
#         raise TypeError('Second argument can\'t be 0')
#     return a / b
#
#
# try:
#     divide_nums(10, 0)
# except Exception as e:
#     print(e)

# Задача
# def image_info(args: dict) -> None:
#     if ('image_id' not in args) or ('image_title' not in args):
#         raise TypeError('You don\'t have image_id or image_title')
#     print(f'Image {args["image_title"]} has id {args["image_id"]}')
#
#
# try:
#     image_info({
#         'image_id': 5136,
#         # 'image_title': 'My cat'
#     })
# except TypeError as e:
#     print(e)


# Распаковка - Извлечение значений и присвоение их переменным

# Распаковка списка и кортежа
# # my_fruits: list = ['apple', 'banana', 'lime']
# my_fruits: tuple = ('apple', 'banana', 'lime')
# # apple: str = my_fruits[0] # по элементная распаковка
# # apple, banana, lime = my_fruits
# # print(apple)
# apple, *other = my_fruits
# print(other)

# Распаковка словаря
# user_profile: dict = {
#     'name': 'Vlad',
#     'qty': 23
# }
#
#
# def user_info(name: str, qty: int = 0) -> str:
#     if not qty:
#         return f'{name} has no comments'
#
#     return f'{name} has {qty} comments'
#
#
# print(user_info(**user_profile))
# name, qty = user_profile
# print(name)

# Условные инструкции
# if
# if...else
# if elif else
# тернарные оператор

# Суть if если не ложное выполняется код
# Ложные значения
# {}, [], set(), range(0), "" (str), 0, 0.0, 0j, False, None
# numb = 10
# if numb > 0:
#     print('True')
#
# info: dict = {
#     'age': 10
# }
#
# if not info.get('name'):
#     print('Name is absent')
# elif info.get('name'):
#     print(f'Your name is {info.get("name")}')
# else:
#     print('Some Error')

# Задача
# info: dict = {
#     # 'distance': 10,
#     # 'speed': 100,
#     # 'time': 10
# }
#
#
# def route_info(args: dict) -> str:
#     # if args.get('distance') and not args.get('distance') % 2:
#     #     return f"Distance to your destination is {args.get('distance')}"
#     # elif args.get('speed') and args.get('time'):
#     #     return f"Distance to your destination is {args.get('speed') * args.get('time')}"
#     # else:
#     #     return f"No distance info is available"
#
#     # Ответ, мой мне нравиться больше стилистически, но тут есть сравнение по типу
#     if ('distance' in args) and (type(args['distance']) == int):
#         return f"Distance to your destination is {args['distance']}"
#     if ('speed' in args) and ('time' in args):
#         return f"Distance to your destination is {args['speed'] * args['time']}"
#     else:
#         return f"No distance info is available"
#
#
# print(route_info(info))

# Тернарный оператор (условные выражения)
# Выражение_1 if Условие else Выражение_2

# Примеры
# numb: int = 20.5
# print('is int') if type(numb) is int else print('is not int')

# qty = 10
#
# print('in stock' if qty > 0 else 'out of stock')
#
# temp = +23
# weather = 'hot' if temp > 18 else 'cold'
# print(weather)

# Циклы используются для перебора элементов последовательностей (dict, list, tuple, set, range,str)
# for ... in ...
# while

# for элемент (свое название) in последовательность (dict, list, tuple, set, range,str)
#    Действие

# my_list: list = [True, 10, 'abc', {}]  # Список
# for elem in my_list:
#     print(elem)

# my_list: set = {True, 10, 'abc', {}}  # set Error!
# for elem in my_list:
#     print(elem)

# my_list: dict = {0: True, 1: 10, 2: 'abc', 3: {}}  # Словарь set
# for key in my_list:
#     print(key, my_list[key])
#
# my_list: tuple = (True, 10, 'abc', {})  # Картеж tuple
# for elem in my_list:
#     print(elem)

# Items

# my_object: dict = {
#     'x': 10, 'y': True
# }
#
# for item in my_object.items():
#     key, val = item
#     print(key, val)

# Filter

# def filter_list(list_to_filter, value_type):
#     # def check_element_type(elem):
#     #     # return isinstance(elem, value_type) # или что и лучше
#     #     return type(elem) is value_type
#     # # filter(функция проверки, список что. надо проверить)
#     # return list(filter(check_element_type, list_to_filter))
#     # Сократим код)))
#     return list(filter(lambda elem: type(elem) is value_type, list_to_filter))
#
#
# # Ищем в списке все int
# res = filter_list([1, 10, 'abc', 5.5, True], int)
# print(res)

# While

# i = 10
# while i < 50:
#     print(i)
#     i += 10  # Изменения значения переменной внутри цикла!

# while True:  # Без конечный цикл !!!ТАК ДЕЛАТЬ НЕЛЬЗЯ И ЗАПРЕЩЕНО!!! Без условий остановки цикла
#     print('Infinite loop')
# Пример с условиями безконечного цикла
# while True:
#     answer = input('Enter yes or no: ')
#     if answer == 'no':
#         break

# import random
#
# random_num = random.randint(1, 5) # от 1 до 5
#
# while True:
#     num = int(input('1 to 5: '))
#     if num != random_num:
#         print('Try again... )))')
#         continue
#
#     print('Congratulations!)))', random_num)
#     break

# Сокращенный цикл for in list, dict, tuple, set
# Выражение for элемент in Последовательность if Условия

# all_numbs: list = [-2, 1, 0, 10, -2, 5]
# # absolute_numbs:list = []
# # for num in all_numbs:
# #     absolute_numbs.append(abs(num))
# # print(absolute_numbs)
# # print(all_numbs)
#
# # absolute_numbs:list = [abs(num) for num in all_numbs]
# absolute_numbs:list = [abs(num) for num in all_numbs if num > 0]
#
# print(absolute_numbs)

# my_set: set = {1, 10, 15}
#
# new_set:set = {val * val for val in my_set}
# print(new_set)

# my_scores: dict = {
#     'a': 10,
#     'b': 7,
#     'c': 14
# }
#
# scores: dict = {key: val * 10 for key, val in my_scores.items()}
# print(scores)

# Генераторы в сокращенном for in

# numbs = (3, 5, 10)
# sqr = list((num * num for num in numbs))
# print(sqr)

# sqr = tuple((num * num for num in range(6)))
# print(sqr)


# Давайте посмотрим разницу)))

# from sys import getsizeof
#
# my_list = (num * num for num in range(100_000_000))  # generator
# print(getsizeof(my_list))
# print(type(my_list))
# # 200
# my_tuple = [num * num for num in range(100_000_000)]  # list
# # 835128600
# print(getsizeof(my_tuple))
# print(type(my_tuple))
# # Суть такая что generator занимает меньше памяти PC

# Class and Objects
# Классы это шаблоны для объектов 170
# class Car:
#     def move(self):
#         print('Car is moving')
#
#     def stop(self):
#         print('Car is stop')
#
#
# my_car = Car()
# print(type(my_car))
# print(isinstance(my_car, Car))
# print(dir(my_car))
# my_car.stop()
# my_car.move()
# print(my_car.__dict__)
#
# my_second_car = Car()
#
# print(my_car == my_second_car)
# print(id(my_car), id(my_second_car))

# Метод __init__

# class Comment:
#     # Если мы вызываем Comment(со скобками), то вызывается  __init__
#     def __init__(self, text: str) -> None:
#         self.text = text
#         self.qty = 0
#
#     def upvote(self) -> None:
#         self.qty += 1
#
#
# first_comment = Comment('First Comment')
# print(first_comment.__dict__)
# print(first_comment.text)
# print(first_comment.qty)
# first_comment.upvote()
# print(first_comment.qty)

# Задача
# class Image:
#     def __init__(self, resolution: str, title: str, extension: str) -> None:
#         self.resolution = resolution
#         self.title = title
#         self.extension = extension
#
#     def resize(self, resol) -> None:
#         self.resolution = resol
#
#     # Преобразуем ответ обращения в строку, а не в объект print(img)
#     def __str__(self):
#         return self.title + '.' + self.extension
#
#
# img: Image = Image('1900x600', 'My image', 'png')
# print(img.__dict__)
# img.resize('800x600')
# print(img.__dict__)
# print(img)

# @staticmethod
# class Comment:
#     def __init__(self, text: str) -> None:
#         self.text = text
#
#     @staticmethod
#     def merge_comments(first: str, second: str) -> str:
#         return f"{first} {second}"
#
#
# comment: Comment = Comment('My comment')
#
# new_comment: str = comment.merge_comments('First', 'Second')  # Атрибут екземпляра класса
# print(new_comment)
# new_comment2: str = Comment.merge_comments('First', 'Second')  # Атрибут класса
# print(new_comment2)

# Атрибут класса
# class Comment:
#     total_comments = 0
#
#     def __init__(self, text: str) -> None:
#         self.text = text
#         self.qty = 0
#         Comment.total_comments += 1
#
#
# print(Comment.total_comments)
# comment1: Comment = Comment('My comment1')
# print(Comment.total_comments)
# comment2: Comment = Comment('My comment2')
# print(Comment.total_comments)

# Магические методы в Классах
# class Comment:
#     def __init__(self, text: str) -> None:
#         self.text = text
#         self.qty = 0
#
#     def upvote(self) -> None:
#         self.qty += 1
#
#     def __add__(self, other) -> tuple:
#         return (f'{self.text} {other.text}',
#                 self.qty + other.qty)
#
#
# comment1: Comment = Comment('My comment1')
# comment1.upvote()
# comment2: Comment = Comment('My comment2')
# comment2.upvote()
# print(comment1 + comment2)
# # Они не плюсуються,
# # а нам надо их прибавить. Добавим маг метод __add__,
# # в нем опишем как нам нравиться

# Наследование из других классов или подклассы (по сути класс без ничего как я понял)
# class ExtendedList(list):
#     def print_list_info(self):
#         print(f'List has {len(self)} elements')
#
#
# custom_list: ExtendedList = ExtendedList([3, 4, 5, 6])
#
# custom_list.print_list_info()

# ДЕКОРАТОРЫ
# Декораторы - спец функции которые выполняют Ваши функции
# К примеру мы хотим что-то вызвать перед нашей ф-цией и после ее выполнения
# def decoration_func(original_function):
#     def wrapper(*args, **kwargs):
#         # Действие перед выполнением оригинальной функции
#         print('Executed before function')
#         result = original_function(*args, **kwargs)
#         # Действия после выполнение оригинальной функции
#         print('Function result:', result)
#         print('Executed after function')
#         return result
#
#     return wrapper
#
#
# @decoration_func
# def my_func(a, b):
#     print('This is my function')
#     return a, b
#
#
# res = my_func(100, 50)
# print(res)
# Пример декоратора - Логирование данных

# def logs_fn(fn):
#     def wrapper(*args, **kwargs):
#         print(f'Function name: {fn.__name__}')
#         print(f'Function arguments: {args}, {kwargs}')
#         result = fn(*args, **kwargs)
#         print(f'Function result: {result}')
#         return result
#
#     return wrapper
#
#
# @logs_fn
# def mult(a: int, b: int) -> int:
#     return a * b
#
#
# print(mult(2, 5))
#
#
# @logs_fn
# def sum(a: int, b: int) -> int:
#     return a + b
#
#
# print(sum(2, 5))

# Пример валидация аргументов функции

# def validate_args(fn):
#     def wrapper(*args, **kwargs):
#         # for arg in args:
#         #     if not isinstance(arg, int) and not isinstance(arg, float):
#         #         raise ValueError(f'Type of the {arg} is {type(arg)}',
#         #                          'All arguments must be int or float!')
#         for arg in [*args, *kwargs.values()]:  # Более универсальный метод
#             if not isinstance(arg, int) and not isinstance(arg, float):
#                 raise ValueError(f'Type of the {arg} is {type(arg)}',
#                                  'All arguments must be int or float!')
#         result = fn(*args, **kwargs)
#         return result
#
#     return wrapper
#
#
# @validate_args
# def sum_nums(a, b):
#     return a + b
#
#
# try:
#     print(sum_nums(7, 2))
#     print(sum_nums(10.5, 2.3))
#     # print(sum_nums(10.5, '2.3'))
#     # print(sum_nums(a=10.5, b='2.3'))  # таким образом мы попадаем уже не в *args, а в **kwargs
#     print(sum_nums([1, 2.2, 3], b='2.3'))  # таким образом мы попадаем уже не в *args, а в **kwargs
# except ValueError as e:
#     print(e)

# Пример Аутентификации пользователя

# def is_user_auth():
#     return True
#
#
# def check_user_auth(fn):
#     def wrapper(*args, **kwargs):
#         if is_user_auth():
#             return fn(*args, **kwargs)
#         else:
#             raise Exception('User is NOT auth')
#
#     return wrapper
#
#
# @check_user_auth
# def do_sensitive_job():
#     # Do something if usr auth
#     print('Results of some sensitive tasks')
#
#
# try:
#     do_sensitive_job()
# except Exception as e:
#     print(e)


# МОДУЛИ

# Модули - позволяют вас структурировать код и импортировать его
# import hacks
# import hacks as hack
# from hacks import connect
# from hacks import connect as con
# from hacks import *

# print(dir(hack))
# print(hack.connect())
# print(connect())
# print(con())

# Что такое __name__ и __main__
# print(dir())
# print(__name__)
# print(type(__name__))
# print(__name__ == '__main__')

# Встроенные модули
# Примеры
# os - Работа с файлами
# smtplib - Почта
# pprint - Форматировать вывод данных в консоль
# time - Действия со временем
# zipfile - Архивы
# calendar - С датами
# sys - Системные функции
# csv - CSV
# regex - Регулярные выражения
# math - Математические операции
# statistics - Статистические расчеты
# random - Генерация случайных чисел

# help('modules')  # Список всех доступных модулей
# help('pprint')  # Читаем про конкретный модуль

# Применение встроенных модулей
# import math
# print(math.pi)

# Создание пакетов
# import pack.pack as hacks
#
# hacks.connect()

# Json - Javascript object notation
# Формат обмена данными или формат хранения данными (похож на словарь)
# {
#     "id": 1,
#     "brand": "Nike",
#     "qty":84,
#     "status":{
#         "isForSale": true
#     }
# }

# import json
#
# json_str = '{"id":1,"brand":"Nike","qty":84,"status": {"isForSale":true}}'
# sneakers = json.loads(json_str)  # Из json в словарь
# print(type(sneakers))
# print(sneakers)
# to_json = json.dumps(sneakers)  # Из словаря в json
# print(type(to_json))
# print(to_json)
# to_json = json.dumps(sneakers, indent=1)  # Из словаря в json в красивом формате для файлов
# print(type(to_json))
# print(to_json)

# Работа с файлами
# os(функциональный подход) or pathlib(ООП подход к работе с файлами)
# Сравним

# from os import path
# from pathlib import Path
#
# print(path.abspath('.'))
# print(type(path))
# print(Path('.').absolute())
# print(type(Path))
#
# print(path.abspath('/'))
# print(Path('/').absolute())

# from pathlib import Path

# print(Path.cwd())  # Путь к текущей папке
# Формировать новые пути
# print(Path('usr').joinpath('local').joinpath('bin'))
# print(Path('usr') / 'local' / 'bin')

# print(Path('main.py').exists())
# print(Path('E:\\Projects\\Python\\Python_Django_Data_Science_ML_2023\\basic_knowledge\\main.py').exists())
# print(Path('main.py').is_dir())
# print(Path('main.py').is_file())

# Список файлов и папок

# for f in Path('.').iterdir():
#     print(f)

# from os import path
#
# print(path.curdir)
# print(path.abspath('.'))

# from pathlib import Path
#
# cmd = Path('django')
# if not cmd.exists():
#     cmd.mkdir()
#
# print(cmd.exists())
#
# if cmd.exists():
#     cmd.rmdir()

# Чтение файлов
# with open('test.txt') as test_file:
#     print(test_file.read())
#
# with open('test.txt') as test_file:
#     print(test_file.readlines())  # Получим список, построково

# и запись файлов
# with open('new.txt', 'w') as test_file:
#     print(test_file.write('First line in the new file\n'))  # Перезапись файла с 0
#
# with open('new.txt', 'a') as test_file:
#     print(test_file.write('Second line in the new file\n'))  # Дописать в файла

# Удалить файл

# from pathlib import Path
# Path('new.txt').unlink()

# test_file = open('test2.txt', 'w') # Создаст или опустошит файл
# # test_file = open('test2.txt', 'a')  # До записи файла
# # print(type(test_file))
# # print(test_file)
# test_file.write('First line in the new file\n')
# test_file.write('Second line in the new file\n')
#
# # print(test_file.read()) # Не можем прочесть в режиме записи
#
# test_file.close()
#
# # Обязательно закрыть и заново открыть
# test_file = open('test2.txt')
# print(test_file.read())

# То же самое что до открытия в чтение (Скажем так краткая запись)
# with open('test2.txt', 'w') as test_file:
#     test_file.write('First line in the new file\n')
#     test_file.write('Second line in the new file\n')

# Создание и распаковка zip архивов 207
# from zipfile import ZipFile
# from pathlib import Path
#
# # if not Path('my-files').exists():
# #     Path('my-files').mkdir()
# #
# # with open('my-files/first.txt', 'w') as my_file:
# #     my_file.write('This is first file')
# #
# # with open('my-files/second.txt', 'w') as my_file:
# #     my_file.write('This is second file')
# # Запись в файл зип
# # with ZipFile('my-files.zip', mode='w') as my_zip:
# #     # print(my_zip)
# #     for file in Path('my-files').iterdir():
# #         # print(file)
# #         my_zip.write(file)
#
# with ZipFile('my-files.zip', mode='r') as my_zip:
#     print(my_zip.infolist())
#     print(my_zip.filename)
#     print(my_zip.filelist)
#     # my_zip.extractall(path='my-files-unzip')

# CSV
# import csv

# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([1, 'Vlad', 10])
#     writer.writerow([2, 'Viktor', 1])
#     writer.writerow([1, 'Oksana', 15])

# with open('test.csv', ) as csv_file:
#     reader = csv.reader(csv_file)  # вызвать можно только один раз
#     # print(type(reader))
#     # print(reader)
#     # for line in reader:
#     #     print(line)
#     csv_list = list(reader)
#     print(csv_list)
#     print(reader.line_num)

# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=';')
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([1, 'Vlad', 10])
#     writer.writerow([2, 'Viktor', 1])
#     writer.writerow([1, 'Oksana', 15])

# Datetime

# from datetime import date, time, datetime, timedelta

# my_date = date(2100, 4, 15)
# print(my_date)
# print(my_date.day)
# print(my_date.weekday())
# print(my_date.year)
# print(my_date.month)
# print(my_date.isocalendar())

# my_time = time(18, 10, 45)
# print(my_time)
# print(my_time.hour)
# print(my_time.isoformat())

# my_datetime = datetime(2024,3,8,18,10,15)
# print(my_datetime)
# print(my_datetime.now())
# print(my_datetime.isoformat())
# print(my_datetime.strftime('%d/%m/%Y'))
# print(my_datetime.strftime('%d-%m/-%Y %H:%M:%S'))

# date_str = '08/03/2024'
# converted_date = datetime.strptime(date_str,'%d/%m/%Y')
# print(converted_date)

# print(timedelta)
# my_datetime = datetime(2024, 3, 8, 18, 10, 15)
# print(my_datetime + timedelta(days=100))  # + сто дней
# print(my_datetime + timedelta(minutes=10))  # + 10 минут
# print(my_datetime - timedelta(minutes=10))  # - 10 минут

# Time
# import time
#
# print(time.time())
# print(time.ctime(time.time()))
# start = time.time()
# print(start)
# time.sleep(2.5)
# # Или к примеру надо не слип,
# # а отследить сколько идет обработка
# end = time.time()
# print('Total duration:', end - start)

# Random
# import random
#
# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(random.choice('abcd'))
# print(random.choices('abcd', k=2))
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# random.shuffle(my_list)
# print(my_list)
#
# # Пример генерации пароля простого
# print(''.join(random.choices('0123456789', k=8)))

# Secrets - Пароли
# import secrets
# import string
#
# # print(string.ascii_letters)
# # print(string.digits)
# # print(string.punctuation)
# # print(string.printable)
# # print(string.hexdigits)
#
# all_chars = string.ascii_letters + string.digits + string.punctuation
# # print(all_chars)
# # password = secrets.choice(all_chars)
# # print(password)
# password = ''.join(secrets.choice(all_chars) for i in range(8))
# print(password)

# Math
# import math
# print(math.pi)
# print(math.e)
# print(math.sqrt(25))
# print(math.log(100))  # логарифм
# print(math.factorial(10))  # факториал

# Рекурсивная ф-ция
# def calc_factorial(num: int) -> int:
#     if num <= 0:
#         raise ValueError('Number must be positive')
#     elif num == 1:
#         return 1
#     return calc_factorial(num - 1) * num
#
#
# print(calc_factorial(10))  # 10*9*8*7*6...
# print(math.factorial(10))

# Re - модуль для регулярных выражений
# import re

# my_str = 'My name is Vlad.'
# res = re.search('Vlad', my_str)
# print(res)
# res = re.search('V..d', my_str) # . заменяет любой символ
# print(res)
# res = re.search('V..d$', my_str)  # . заменяет любой символ и в конце строки
# print(res)
# res = re.search('^M.*name', my_str)  # Начинается на М и заканчивается на name
# print(res)
# res = re.search(r'V..d\.$', my_str)  # Ище с точкой, поскольку оно зарезервировано то экранируем
# print(res)
# print(r'V..d\.$')  # r строки, тогда они не форматируються
# print(res.span())
# print(res.start())
# print(res.end())
# my_pattern = re.compile(r'V..d\.$') # Создаем патерн
# print(my_pattern)
# print(my_pattern.search(my_str))
# my_pattern = re.compile(r'^My.*\.') # Создаем патерн
# print(my_pattern)
# print(my_pattern.search(my_str))
# print(my_pattern.match(my_str))

# Проверка email
# email_regexp = r'[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
#
# email_check_pattern = re.compile(email_regexp)  # Создаем патерн
#
# print(email_check_pattern.fullmatch('bs@gmail.com'))
# print(email_check_pattern.fullmatch('bsgmail.com'))
# print(email_check_pattern.fullmatch('bs-@gmail.com'))
# print(email_check_pattern.fullmatch('bs_@gmail.com'))

# Задача
# import re
#
# def check_password(password: str) -> tuple:
#     length_pattern = re.compile(r'^.*\S{8,}.*$')
#     lowercase_pattern = re.compile(r'^.*[a-z]+.*$')
#     uppercase_pattern = re.compile(r'^.*[A-Z]+.*$')
#     number_pattern = re.compile(r'^.*[0-9]+.*$')
#     special_symbol_pattern = re.compile(r'^.*[@%#!&*^]+.*$')
#     no_white_spaces = re.compile(r'^\S*$')
#     if not re.fullmatch(length_pattern, password):
#         return False, 'Password must have at least 8 symbols'
#     elif not re.fullmatch(lowercase_pattern, password):
#         return False, 'Password must have at least one lowercase letter'
#     elif not re.fullmatch(uppercase_pattern, password):
#         return False, 'Password must have at least one uppercase letter'
#     elif not re.fullmatch(number_pattern, password):
#         return False, 'Password must have at least one number'
#     elif not re.fullmatch(special_symbol_pattern, password):
#         return False, 'Password must have at least one special symbol like @%#!&*^'
#     elif not re.fullmatch(no_white_spaces, password):
#         return False, 'Password must`t have  white spaces'
#     else:
#         return True, 'Password ia valid'
#
#
# print(check_password('1234567'))
# print(check_password('12345678'))
# print(check_password('12345678l'))
# print(check_password('12345678Fl'))
# print(check_password('12345678 Fl!'))
# print(check_password('12345678Fl!'))

# SMTPLIB - рассылка email
# from email.message import EmailMessage
# import smtplib
# from string import Template
# from pathlib import Path
#
# html_tmpl = Template(Path('tmpl/email/index.html').read_text())
# html_content = html_tmpl.substitute({'name': 'Vlad', 'date': '10.10.2024'})
#
# my_email = EmailMessage()
# my_email['from'] = 'Vlad'
# my_email['to'] = 'test@gmail.com'
# my_email['subject'] = 'Hello from Python'
# # my_email.set_content('Hey? How are you doing?')
# my_email.set_content(html_content, 'html')
#
# with open('images/photo.jpg', 'rb') as img:
#     image_data = img.read()
#     my_email.add_attachment(image_data, maintype='image', subtype='jpg', filename='email.jpg')
#
# with smtplib.SMTP(host='192.168.2.1', port=2525) as smtp_server:
#     smtp_server.ehlo()
#     smtp_server.starttls()
#     smtp_server.login('user', 'password')
#     smtp_server.send_message(my_email)

# Sqlite3
# import sqlite3

# DB_NAME = 'sqlite.db'

# courses: list = [
#     (2, 'Java course', 10, 3),
#     (3, 'JavaScript course', 10, 3),
#     (4, 'Php course', 10, 3),
#     (5, 'C++ course', 10, 3),
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     # print(sqlite_conn)
#     # print(sqlite3.sqlite_version)
#
#     # sql_request = """CREATE TABLE IF NOT EXISTS courses(
#     # id integer  PRIMARY KEY,
#     # title text NOT NULL,
#     # student_qty integer,
#     # reviews_qty integer
#     # );"""
#     # sqlite_conn.execute(sql_request)
#
#     # sql_request = "INSERT INTO courses VALUES (?,?,?,?)"
#     # sqlite_conn.execute(sql_request, (1, 'Python course', 100, 30))
#     # sqlite_conn.commit()
#
#     # sql_request = "INSERT INTO courses VALUES (?,?,?,?)"
#     # for course in courses:
#     #     sqlite_conn.execute(sql_request, course)
#     # sqlite_conn.commit()
#
#     # sql_request = "SELECT * FROM courses"
#     # result_cursor = sqlite_conn.execute(sql_request)
#     #
#     # # for record in result_cursor: # Не забываем что два раза вызывать нельзя
#     # #     print(record)
#     # #     print(record[1])
#     #
#     # records = result_cursor.fetchall()
#     # print(records)
#
#     # sql_request = "SELECT * FROM courses WHERE reviews_qty>=10"
#     # result_cursor = sqlite_conn.execute(sql_request)
#     # records = result_cursor.fetchall()
#     # print(records)

# Array
# from array import array
#
# my_array: array = array('i', [4, 10, 5, 7, 5, 15, 7])
# # print(my_array)
# # my_array.append(15)
# # # my_array.append('1')
# # print(my_array)
# # print(my_array.count(5))
# # my_array.pop()
# # print(my_array)
# # for el in my_array:
# #     print(el)
#
# with open('my_array.bin','wb') as my_file:
#     my_array.tofile(my_file)

# Sys
# import sys
#
# print(sys.argv)
# # python basic_knowledge\main.py test first argument
#
# if len(sys.argv) < 3:
#     raise IOError('You must provide 3 arguments')
#
# print(sys.argv[1])

# Webbrowser
# import webbrowser
#
# webbrowser.open('https://www.facebook.com/')

# PIP
# pip3 --version
# pip3 list

# Виртуальная среда разработки с помощью Pipenv
# pip install -user pipenv

# .venv создаем папку
# python pipenv install requests

# import requests
# res = requests.get('https://www.facebook.com/')
# print(res)
# print(res.status_code)
# print(res.text)

# Django
# Model View Controller (MVC)
# Model Template View (в Django MVC->MTV)
# python -m django startproject base . - installation
