# Задание No1
# 📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт
# целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.


def get_number():
    num: int
    while True:
        try:
            num = int(input('Input integer or floating point number: '))
        except ValueError as error:
            print('Input was not an integer or floating point.')
        else:
            return num


number = get_number()
print(f'Number entered {number}')