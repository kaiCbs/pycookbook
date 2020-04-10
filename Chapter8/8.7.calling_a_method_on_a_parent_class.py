class Person:
    def __init__(self, name):
        self.name = name

    def who(self):
        return self.name


class Student(Person):
    def __init__(self, name, class_):
        self.name = name
        self.class_ = class_

    def who(self):
        return "{0.name} at Class {0.class_}".format(self)

    def who_par(self):
        return super().who()


if __name__ == "__main__":
    a = Student("Bob", "A")
    print(a.who_par())
    print(a.who())


# A very common use of super() is in the handling of the __init__() method to
# make sure that parents are properly initialized


class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


# Another common use of super() is in code that overrides any of Python’s
# special methods.


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


if __name__ == "__main__":
    a = Person("Mike")
    p = Proxy(a)
    print(getattr(p, "name"))
    setattr(p, "classLetter", "A")
    print(getattr(p, "classLetter"))
    setattr(p, "_classLetter", "B")
    print(getattr(p, "_classLetter"))
