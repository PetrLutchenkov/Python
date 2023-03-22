# Реализовать дескрипторы для любых двух классов
# 1:
class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _road_len = 5000
    _road_width = 20
    weight_1qc = NonNegative()
    thickness = NonNegative()

    def __init__(self, weight_1qc, thickness):
        self.weight_1qc = weight_1qc
        self.thickness = thickness

    def asphalt_mass(self):
        weight = self._road_len * self._road_width * self.weight_1qc * \
                 self.thickness
        print(
            f'{self._road_width}м*{self._road_len}м*{self.weight_1qc}кг*'
            f'{self.thickness}м = {round(weight)} кг = '
            f'{round(weight / 1000)} т')


road = Road(25, 0.05)
road.asphalt_mass()


# 2:
class NonStr:
    def __init__(self, name, type_name, default=None):
        self.name = "_" + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Значение должно быть типа %s" % self.type)
        instance.__dict__[self.name] = value


class Worker:
    name = NonStr('name', str)

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def __str__(self):
        return f'{self.name} {self.surname} {self.position}'


worker = Worker('Иван', 'Петров', "Сторож")
print(worker)
