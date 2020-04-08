class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


if __name__ == "__main__":
    p = Point(3, 4)
    print('p is {0!r}'.format(p))
    print('p is {}'.format(p))
