"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class Traffic_Lights:

    def __init__(self, color=""):
        __color = color

    def running(self, red=7, yellow=2, green=4):
        self.__color = 'Красный'
        print(self.__color)
        time.sleep(red)
        self.__color = 'Жёлтый'
        print(self.__color)
        time.sleep(yellow)
        self.__color = 'Зелёный'
        print(self.__color)
        time.sleep(green)


traffic_lights = Traffic_Lights()
traffic_lights.running()
