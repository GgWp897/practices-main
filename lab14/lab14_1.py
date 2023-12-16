import random

def process_tuple():
    original_tuple = tuple(random.randint(1, 128) for _ in range(10))
    new_tuple = tuple(0 if x % 5 == 0 else x for x in original_tuple)

    with open("lab14_1.txt", "w", encoding="utf-8") as file:
        file.write("Исходный кортеж: {}\n".format(original_tuple))
        file.write("Новый кортеж: {}\n".format(new_tuple))

    with open("lab14_1.txt", "r", encoding="utf-8") as file:
        my_tuples = file.read()
        print(my_tuples)

process_tuple()