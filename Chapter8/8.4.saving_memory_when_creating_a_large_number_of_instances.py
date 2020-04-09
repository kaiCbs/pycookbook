# When you define __slots__ , Python uses a much more compact internal
# representation for instances. Instead of each instance consisting of a
# dictionary, instances are built around a small fixed-sized array, much like a
# tuple or list.


class Date:
    __slots__ = ["year", "month", "day"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        # self.name = "unknown"
        # Raise AttributeError: 'Date' object has no attribute 'name'


if __name__ == "__main__":
    d = Date(2020, 4, 2)
