# def get(text: str = None) -> int:
#     data = input(text)
#     num = int(data)
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')
#############################################################################################
# def get(text: str = None) -> int:
#     data = input(text)
#     num = int(data)
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')
#############################################################################################
# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#         num = 1
#         print(f'Будем считать результатом ввода число {num}')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')
#############################################################################################
# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                   f'Попробуйте снова')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')
#############################################################################################
# def hundred_div_num(text: str = None) -> tuple[int, float]:
#     while True:
#         try:
#             num = int(input(text))
#             div = 100 / num
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                   f'Попробуйте снова')
#         except ZeroDivisionError as e:
#             div = float('inf')
#             break
#     return num, div
#
#
# if __name__ == '__main__':
#     n, d = hundred_div_num('Введите целый делитель: ')
#     print(f'Результат операции: "100 / {n} = {d}"')
#############################################################################################
# MAX_COUNT = 5
#
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         result = 100 / num
#         break
# print(f'{result = }')
#############################################################################################
# MAX_COUNT = 5
#
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         try:
#             result = 100 / num
#         except ZeroDivisionError as e:
#             result = float('inf')
#             break
#
# print(f'{result = }')
#############################################################################################
# def get(text: str = None) -> int:
#     num = None
#     try:
#         num = int(input(text))
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#     finally:
#         return num if isinstance(num, int) else 1
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     try:
#         print(f'100 / {number} = {100 / number}')
#     except ZeroDivisionError as e:
#         print(f'На ноль делить нельзя. Получим {e}')
#############################################################################################
# file = open('text.txt', 'r', encoding='utf-8')
# try:
#     data = file.read().split()
#     print(data[len(data)])
# finally:
#     print('Закрываю файл')
#     file.close()
#############################################################################################
# def add_key(dct, key, value):
#     if key in dct:
#         raise KeyError(f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
#     dct[key] = value
#     return dct
#
#
# data = {'one': 1, 'two': 2}
# print(add_key(data, 'three', 3))
# print(add_key(data, 'three', 3))
#############################################################################################
# class User:
#     def __init__(self, name, age):
#         if 6 < len(name) < 30:
#             self.name = name
#         else:
#             raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
#         if not isinstance(age, (int, float)):
#             raise TypeError(f'Возраст должен быть числом. Используйте int или float. {type(age) = }')
#         elif age < 0:
#             raise ValueError(f'Возраст должен быть положительным.{age = }')
#         else:
#             self.age = age
#
#
# user = User('Яков', '-12')
#############################################################################################
# from error import UserNameError, UserAgeError
#
#
# class User:
#     MIN_LEN = 6
#     MAX_LEN = 30
#
#     def __init__(self, name, age):
#         if self.MIN_LEN < len(name) < self.MAX_LEN:
#             self.name = name
#         else:
#             raise UserNameError
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError
#         else:
#             self.age = age
#
#
# user = User('Яков', '-12')
#############################################################################################
class UserException(Exception):
    pass


class UserAgeError(UserException):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return f'Возраст пользователя должен быть целым int() или вещественным float() больше нуля.\n' \
               f'У вас тип {type(self.value)}, а значение {self.value}'


class UserNameError(UserException):
    def __init__(self, name, lower, upper):
        self.name = name
        self.lower = lower
        self.upper = upper

    def __str__(self):
        text = 'попадает в'
        if len(self.name) < self.lower:
            text = 'меньше нижней'
        elif len(self.name) > self.lower:
            text = 'больше верхней'
            return f'Имя пользователя {self.name} содержит {len(self.name)} символа(ов).\n' \
                    f'Это {text} границы. Попадите в диапазон ({self.lower}, {self.upper}).'
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################