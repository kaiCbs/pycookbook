class Encap:
    def __init__(self):
        self.__private = 0
        self._private = 1
        self.public = 2


# However we still have way to access the private attribute
if __name__ == "__main__":
    a = Encap()
    print(a._Encap__private)
    print(a._private)
