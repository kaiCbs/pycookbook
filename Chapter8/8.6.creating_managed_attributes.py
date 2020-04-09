class Student:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    @property
    def first_name(self):
        return self.__first

    @property
    def last_name(self):
        return self.__last

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self.__first = value

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self.__last = value


if __name__ == "__main__":
    a = Student("James", "Harden")
    print(a.first_name)
    a.first_name = "Mike"
    print(a.first_name)
    # a.first_name = 007
    # Raise TypeError: Expected a string


# Properties can also be defined for existing get and set methods. For example:

# class Person:
#     def __init__(self, first_name):
#         self.set_first_name(first_name)

#     def get_first_name(self):
#         return self._first_name

#     def set_first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Expected a string")
#         self._first_name = value

#     def del_first_name(self):
#         raise AttributeError("Can't delete attribute")

#     name = property(get_first_name, set_first_name, del_first_name)
