"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

arg = (['ping', 'yandex.ru'], ['ping', 'youtube.com'],)

for el in arg:
    ping = subprocess.Popen(el, stdout=subprocess.PIPE)
    for site in ping.stdout:
        res = chardet.detect(site)
        print(site.decode(res['encoding']).encode('utf-8').decode('utf-8'))
