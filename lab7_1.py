import random
def process_tuple():
    original_tuple = tuple(random.randint(1, 128) for _ in range(10))
    print("Исходный кортеж: ", original_tuple)
    new_tuple = tuple(0 if x % 5 == 0 else x for x in original_tuple)
    print("Новый кортеж с заменой чисел, кратных 5, на 0: ", new_tuple)
process_tuple()