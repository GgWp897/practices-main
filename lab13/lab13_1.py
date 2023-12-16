class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f'Создание нового класса {name}')
        return super().__new__(cls, name, bases, dct)
    
class FirstClass(metaclass = MyMeta):
    pass

class SecondClass(metaclass = MyMeta):
    pass