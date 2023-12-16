class sayHello(type):
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    def __call__(self, *args, **kwargs):
        cls = type.__call__(self, *args, **kwargs)

        setattr(cls, "hello", self.hello )

        return cls
    
class TryHello(object, metaclass=sayHello):  
    def greet(self):
        self.hello()

greeter = TryHello()  
greeter.greet()