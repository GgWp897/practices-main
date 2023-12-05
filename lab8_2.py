import random

def MyNewFunction(original_tuple, index=0):
    if index == len(original_tuple):
        return () 
    new_tuple = MyNewFunction(original_tuple, index + 1)
    return (0 if (current_value:=original_tuple[index]) % 5 == 0 else current_value,) + new_tuple
original_tuple = tuple(random.randint(1, 128) for _ in range(10)) 
print("Исходный кортеж: ", original_tuple)
new_tuple = MyNewFunction(original_tuple)
print("Новый кортеж с заменой чисел, кратных 5, на 0: ", new_tuple)