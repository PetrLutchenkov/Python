# Реализовать метакласс.
# позволяющий создавать всегда один и тот же объект класса
class MyMetaClass(type):
    a = None

    def __init__(self, *args):
        self.__a = []

    def __call__(self, *args):
        if self.__a is None:
            self.a = super().__call__()
        return self.a


class MyClass(metaclass=MyMetaClass):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
print(obj_1 is obj_2)
