class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expect an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    _x = Integer("x")
    _y = Integer("y")

    def __init__(self, x, y):
        self._x = x
        self._y = y


if __name__ == "__main__":
    p = Point(2, 3)
    print("Point({0.x}, {0.y})".format(p))
    # p = Point(2, 3.1)
    # raise TypeError("Expect an int")
