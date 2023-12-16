class ChangeMethodMeta(type):
    def __new__(cls, name, bases, dct):
        new_method = dct.get('new_method')

        if new_method:
            original_method = dct.get('original_method')

            def wrapper(self, *args, **kwargs):
                return new_method(self, *args, **kwargs)

            dct['original_method'] = wrapper

        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=ChangeMethodMeta):
    def original_method(self):
        return "Это оригинальный метод"

    def new_method(self):
        return "Это новый метод"

obj = MyClass()

print(obj.original_method())  
