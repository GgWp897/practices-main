class MyMeta(type):
    registry = {}

    def __new__ (cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        cls.registry[name] = new_class
        return new_class
    
class Base(metaclass = MyMeta):
    pass

class First(Base):
    pass

class Second(Base):
    pass

print(MyMeta.registry)