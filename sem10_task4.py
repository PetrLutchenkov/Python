"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
my_list = ['разработка', 'администрирование', 'protocol', 'standard']

my_byte_list = []
for el in my_list:
    my_byte_list.append(el.encode())
print(my_byte_list)

my_revers_list = []
for el in my_byte_list:
    my_revers_list.append(el.decode())
print(my_revers_list)
