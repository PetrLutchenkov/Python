"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    _road_len = 5000
    _road_width = 20

    def __init__(self, weight_1qc, thickness):
        self.weight_1qc = weight_1qc
        self.thickness = thickness

    def asphalt_mass(self):
        weight = self._road_len * self._road_width * self.weight_1qc * \
                 self.thickness
        print(
            f'{self._road_width}м*{self._road_len}м*{self.weight_1qc}кг*'
            f'{self.thickness}м = {round(weight)} кг = {round(weight / 1000)} т')


road = Road(25, 0.05)
road.asphalt_mass()
