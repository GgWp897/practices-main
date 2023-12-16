class MetaClass(type):
    def __new__(cls, name, bases, dct):
        dct['custom_attribute'] = 'Added by metaclass'
        new_class = super().__new__(cls, name, bases, dct)
        return new_class

def create_classes(num_classes):
    classes = []
    for i in range(num_classes):
        name = f'DynamicClass {i}'
        dct = {'dynamic_attribute': f'Value{i}'}


        dynamic_class = MetaClass(name, (), dct)
        classes.append(dynamic_class)

    return classes

generated_classes = create_classes(10)


for class_item in generated_classes:
    print(f"Имя класса: {class_item.__name__}")
    print(f"Аттрибуты класса: {class_item.__dict__}")
    print()