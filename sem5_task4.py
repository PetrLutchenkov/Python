"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтись без создания массива!
"""


def sum_row(n, res):
    if n == 1:
        return res
    else:
        return res + sum_row(n - 1, res / -2)


count = int(input('Введите количество элементов: '))
print(f'Количество элементов: {count} , их сумма: {sum_row(count, 1)}')
