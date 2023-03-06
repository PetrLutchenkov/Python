"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess_number(num, attempt):
    if attempt > 0:
        inp_num = int(input('Введите число от 0 до 100: '))
        if inp_num == num:
            print(f'Число отгадано верно: {inp_num}')
        else:
            if inp_num < num:
                print('Число меньше загаданного')
            else:
                print('Число больше загаданного')
            guess_number(num, attempt - 1)
    else:
        print(f'Загаданное число: {num}.')


hidden_number = random.randint(0, 100)
guess_number(hidden_number, 10)