class FactorialMeta(type):
    def __new__(cls, name, bases, dct):

        def factorial(self, n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(self, n - 1)
        dct['factorial'] = factorial
        return super().__new__(cls, name, bases, dct)

for i in range(1, 11):
    class_name = f'Номер класса {i}'
    class_vars = {}
    NumberClass = FactorialMeta(class_name, (), class_vars)
    globals()[class_name] = NumberClass

for i in range(1, 11):
    class_name = f'Номер класса {i}'
    num_instance = globals()[class_name]()
    result = num_instance.factorial(5) 
    print(f"{class_name}: Факториал 5: {result}")
