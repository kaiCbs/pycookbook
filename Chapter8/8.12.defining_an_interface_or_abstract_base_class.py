import io
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# A central feature of an abstract base class is that it cannot be instantiated
# directly. Instead, an abstract base class is meant to be used as a base class
# for other classes that   are expected to implement the required methods.


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        ...

    def write(self, data):
        ...


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError("Expected an IStream")


IStream.register(io.IOBase)
f = open("temp.txt", "w")
print(isinstance(f, IStream))
