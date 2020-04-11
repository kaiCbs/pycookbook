import math


class Lazy:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.r = radius

    @Lazy
    def area(self):
        print("Computing area")
        return math.pi * self.r ** 2

    @Lazy
    def perimeter(self):
        print("Computing perimeter")
        return math.pi * self.r * 2


if __name__ == "__main__":
    c = Circle(5)
    print(c.r)
    print(c.area)
    print(c.perimeter)
