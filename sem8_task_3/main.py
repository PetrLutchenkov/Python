"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

lib_to_write = {
    'items': [
        'computer',
        'printer',
        'scanner',
        'mouse',
    ],
    'count': 4,
    'price': {
        'computer': '500-4000€',
        'printer': '100-500€',
        'scanner': '50-300€',
        'mouse': '5-80€',
    }
}

with open('my_file.yaml', 'w') as file:
    yaml.dump(lib_to_write, file, default_flow_style=False, allow_unicode=True)

with open('my_file.yaml', encoding='windows-1251') as file:
    print(file.read())
