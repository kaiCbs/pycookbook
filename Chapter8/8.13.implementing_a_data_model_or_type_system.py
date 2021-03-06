class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, val in opts.items():
            setattr(self, key, val)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("expected", self.expected_type)
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError("size must be <", str(self.size))
        super().__set__(instance, value)


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class UnsignedInteger(Integer, Unsigned):
    ...


class SizedString(String, MaxSized):
    ...


class UnsignedFloat(Float, Unsigned):
    ...


class Stock:
    name = SizedString("name", size=8)
    shares = UnsignedInteger("shares")
    price = UnsignedInteger("price")

    def __init__(self, name, shares, prices):
        self.name = name
        self.shares = shares
        self.price = prices


s = Stock("Apple", 50, 201)

print(s.name, s.shares, s.price)

# s.shares = -1
# raise ValueError("Expected >= 0")


# class decorator
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate
