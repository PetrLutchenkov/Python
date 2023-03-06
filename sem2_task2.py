"""
Задание 2.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
x = int(input('Введите целое положительное число: '))
maximal = 0
while x > 0:
    i = x % 10
    if i > maximal:
        maximal = i
    x //= 10
print(maximal)