class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Выполняется декоратор до вызова функции")
        
        result = self.func(*args, **kwargs)
        
        print("Выполняется декоратор после вызова функции")
        
        return result

@MyDecorator
def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Макс")
