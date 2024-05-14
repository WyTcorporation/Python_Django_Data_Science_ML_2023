# # Life hacks
# 1
# import time
# def connect() -> None:
#     print('Connecting to internet')
#     time.sleep(5)
#     print('You ara connected!')
#
#
# # Если запустить этот файл, то отработает один раз, но если вызвать в main оно стало цикличным
# # connect()
#
# # Таким образом мы жестко задали один раз вызывать функцию
# if __name__ == '__main__':
#     connect()

# 2

# def green() -> None:
#     print('Hello world!')
#
#
# def bue() -> None:
#     print('Bye, world!')

# Все это можно было прописать в if, но таким способом код становиться более чистым
# А так же эта функция есть в автозаполнении
# def main() -> None:
#     green()
#     bue()
#
# if __name__ == '__main__':
#     main()

# 3 Совет выносить все проверки в функции для дальнейшего использования, пример

# def is_an_adult(age: int, has_id: bool) -> bool:
#     return age >= 21 and has_id
#
#
# def is_bob(name: str) -> bool:
#     return name.lower() == 'bob'
#
#
# def enter_club(name: str, age: int, has_id: bool) -> None:
#     if is_bob(name):
#         print('Get out og here Bob, we don\'t want no trouble')
#
#     if is_an_adult(age, has_id):
#         print('You may enter the club')
#     else:
#         print('You nay not enter the club')
#
#         # if name.lower() == 'bob':
#     #     print('Get out og here Bob, we don\'t want no trouble')
#     #
#     # if age >= 21 and has_id:
#     #     print('You may enter the club')
#     # else:
#     #     print('You nay not enter the club')
#
#
# def main() -> None:
#     enter_club('Bob', 29, has_id=True)
#     enter_club('James', 29, has_id=True)
#     enter_club('Sandra', 29, has_id=False)
#     enter_club('Mario', 20, has_id=True)
#
#
# main()

# 4
# Подпись типа значения, то что меня удивило с начала
# n: int = 1_000_000_000  # Задание переменной типа значения,
# в дальнейшем это значение нельзя будет перевести к примеру в str

# Простая функция, но если в списке будут int то программа остановиться с ошибкой
# def my_func(elements):
#     return [element.upper() for element in elements]
# Когда мы задай конкретный список и ответ то ошибки станут очевидны при написании кода,
# а так же упростит дебаг самой программы
# def my_func(elements: list[str]) -> list[str]:
#     return [element.upper() for element in elements]
#
#
# load_list1: list[str] = my_func(['Maria', 'Bob', 'James'])
# load_list2: list[int] = my_func([1, 2, 3])
# print(load_list1)
# print(load_list2)

# pip install mypy
# sample: list[int] = [1, 'a', 2, 'b']

# 5 Сокращенное написание функций
# people: list[str] = ['James', 'Charlotte', 'Stephany', 'Mario', 'Sandra']
# Скажем нам надо получить список имен свыше 7 букв
# long_name: list[str] = []
# for person in people:
#     if len(person) > 7:
#         long_name.append(person)
# print(long_name)

# long_name: list[str] = [p for p in people if len(p) > 7]
# print(long_name)

# 6
# import sys
#
# a = [val for val in range(100_000)]
# print(f'{sum(a)=}')
# print(f'{sys.getsizeof(a)=}\n')
# b = (val for val in range(100_000))  # Взамен списка использовать картеж
# print(f'{sum(b)=}')
# print(f'{sys.getsizeof(b)=}\n')

# 7
# Рассмотреть самому F строки, много фишек

# 8 Асинхронные запросы
# import requests
# from requests import Response

# Так мы получим один запрос
# response: Response = requests.get('')
# response.json()
# но что если нам надо получить много запросов
# Мульти запросы, для этого нам и надо асинхронные запросы

# import asyncio
# from asyncio import Task
#
#
# async def fetch_status(url: str) -> dict:
#     print(f'Fetching status for: {url}')
#     response: Response = await asyncio.to_thread(requests.get, url, None)  # None тут параметры запроса
#     print('Done!')
#     return {'status': response.status_code, 'url': url}
#
#
# async def main() -> None:
#     apple_task: Task[dict] = asyncio.create_task(fetch_status('https://www.apple.com/ua/'))
#     apple_status: dict = await apple_task
#     print(apple_status)
#
# if __name__ == '__main__':
#     asyncio.run(main=main())

# 9 Словари
# users: dict = {
#     0: 'Mario',
#     1: 'Luigi',
#     2: 'James'
# }
# print(users.values())
# print(users.keys())
# popped: str = users.pop(2)
# print(users)
# print(popped)
# users.popitem()
# print(users)
# print(users.get(1))
# print(users.get(999))
# print(users.get(999, 'Missing!'))
# print(users.setdefault(0, '&&&'))
# print(users.setdefault(999, '???'))  # Если он не найдет такого он его добавит
# print(users)
# users.clear()
# print(users)
# sample_dict: dict = {
#     0: ['a', 'b'],
#     1: ['c', 'd']
# }
# my_copy: dict = sample_dict.copy()
# print(id(sample_dict))
# print(id(my_copy))
# my_copy[0][0] = '!!!'
# print(sample_dict)
# print(my_copy)
# people: list[str] = ['Mario', 'Luigi', 'James']
# users: dict = dict.fromkeys(people)
# print(users)
# users: dict = dict.fromkeys(people, 'Unknown')
# print(users)
# users: dict = {
#     0: 'Mario',
#     1: 'Luigi',
#     2: 'James'
# }
# print(users.items())
# for k, v in users.items():
#     print(k, v)
#
# users.update({2: 'Bob', 3: 'Jame\'s sister'})
# print(users)
# users |= {10: 'Spam', 11: 'Eggs'}
# # var: dict = users | {10: 'Spam', 11: 'Eggs'}
# print(users)

# 10 staticmethod и classmethod
# from typing import Self
# from datetime import date
#
#
# class Comment:
#     # Если мы вызываем Comment(со скобками), то вызывается  __init__
#     def __init__(self, text: str) -> None:
#         self.text = text
#         self.qty = 0
#
#     @staticmethod
#     def upvote(*numbs: int) -> int:
#         return sum(numbs)
#
#     @classmethod
#     def upvote2(cls, text: str) -> Self:
#         return cls(text)
#
#
# # Ты превращаешь модель в статический метод который можно вызывать без вызова отдельно Comment()
# print(Comment.upvote(10, 20, 30))
# # Тут мы обозначаем сразу параметры функции и сразу вызываем метод
# test: Comment = Comment.upvote2('Vlad')
# print(test.text)

# 11 Learn Python's AsyncIO in 15 minutes
# import asyncio
# import asyncio_api


# async def send_data(to: str):
#     print(f'Sending data to {to}...')
#     await asyncio.sleep(2)
#     print(f'Data send to {to}!')
#
#
# async def main():
#     data = await asyncio_api.fetch_data()
#     print('Data:', data)
#     # await send_data('Mario')  # Так нам придеться отсылать каждому с задержкой
#     await asyncio.gather(send_data('Mario'),
#                          send_data('Vlad'),
#                          send_data('Luigi'))  # А так мы отправляем сразу одновременно несколько запросов


# async def kill_time(num):
#     print('Running:', num)
#     await asyncio.sleep(2)
#     print('Finished:', num)
#
#
# async def main():
#     print('Started!')
#     list_of_tasks = []
#     for i in range(1, 1000 + 1):
#         list_of_tasks.append(kill_time(i))
#
#     await asyncio.sleep(2)
#     await asyncio.gather(*list_of_tasks)  # Запуск 1000 функций одновременно )))
#     print('Done!')

# async def main():
#     task = asyncio.create_task(
#         asyncio_api.fetch_data()
#     )
#     # task.cancel()  # Отмена задания
#     #
#     # await asyncio.sleep(0.5)
#     # if task.cancelled():  # Проверка на отмену
#     #     print(task.cancelled())
#
#     try:
#         # result = await task
#         # print(result)
#         # if task.done(): # Не успевает отработать, потому мало ефективно или делать сон
#         #     print(task.result())
#         await asyncio.wait_for(task, timeout=3)  # Задача с ограничением времени
#         print(task.result())
#     except asyncio.CancelledError:
#         print('CANCELLED: Request was canceled...')
#     except asyncio.TimeoutError:
#         print('Timeout: Request was to long...')
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
# 12
# text: str = 'This is a very long sentence.'
#
# info: dict = {
#     'words': (words := text.split()),
#     'characters': (chars := len(''.join(words))),
#     'avg_char_per_word': round(chars / len(words), 2)
# }
# print(info)
#
# name: str = 'Mario'
# empty_name: str = ''
# if temp_name := empty_name or name:
#     print(temp_name)

# 13 (5 Useful Python Decorators) Смотри декораторы
# import time
# from decorators.retry import retry
#
#
# @retry(retries=3, delay=1)
# def connect() -> None:
#     time.sleep(1)
#     raise Exception('Could not connect to internet...')
#
# def main() -> None:
#     connect()
#
#
# if __name__ == '__main__':
#     main()

# 14
# from typing import TypedDict, NotRequired, Required

# 1 Вар
# class Coordinate(TypedDict):
#     x: Required[float]
#     y: Required[float]
#     label: NotRequired[str]
#     category: NotRequired[str]
#
#
# coordinate: Coordinate = {'x': 10, 'y': 10, 'label': 'Profit',
#                           'category': 'Car'}  # Появляется автозаполнение ключей и их типов, это круто

# 2 Вар То же самое
# validation = TypedDict('validation', {'x': int, 'y': int, 'label': str}, total=True)

# coordinate: validation = {'x': 10, 'y': 10, 'label': 'Profit',
#                           'category': 'Car'} # Лишний параметр

# coordinate: validation = {'x': 10, 'y': 10, 'label': 'Profit'}  # Валидно, но сам валидатор выключен в total=False
# coordinate: validation = {'x': 10, 'y': 10, 'label': 1}  # Не Валидно total=True

# validation = TypedDict('validation', {'x': int, 'y': Required[int], 'label': NotRequired[str]}, total=False)
# coordinate: validation = {'x': 10, 'y': 10, 'label': 1}  # Не Валидно total=False

# 15 F str
# big_number = 1_650_000_000
# print(f'{big_number:.2e}')

# from datetime import datetime, date
#
# now: datetime = datetime.now()
# print(f'{now:%d.%m.%y}')
# date_format: str = '%d.%m.%y'
# print(f'{now:date_format}')
# print(f'{now:{date_format}}')

# path: str = '\User\Vlad\somefile.jpg'  # \екранирует пути, что же делать
# path: str = r'\User\Vlad\somefile.jpg'
# path: str = fr'\User\Vlad\somefile.jpg'  # F  + R str

# a: float = 0.1
# b: float = 0.2
#
# print(f'{a + b = :.1f}')
# name: str = 'Vlad'
# print(f'{name = !s}')

# banana:str = '🍌'
# name:str = 'Vlad'
# today: date = datetime.now().date()
#
# print(f'[{today!s}] {name!s} says: {banana!s}')
# print(f'[{today!r}] {name!r} says: {banana!r}')
# print(f'[{today!a}] {name!a} says: {banana!a}')

# 16 Nesting “If Else”

connection = True
paid = True
internet = True
online = True


# Плохой пример
def go_online_if():
    if connection:
        if paid:
            if internet:
                if online:
                    print('You ara online')
                else:
                    print('You ara offline')
            else:
                print('No internet...')
        else:
            print('User has not paid...')
    else:
        print('No connection')


# Хорошее решение
def go_online():
    if not connection:
        print('No connection')
        return
    if not paid:
        print('User has not paid...')
        return
    if not internet:
        print('No internet...')
        return
    if not online:
        print('You ara offline')
        return
    print('You ara offline')
