import random
import json

def process_tuple():
    original_tuple = tuple(random.randint(1, 128) for _ in range(10))
    new_tuple = tuple(0 if x % 5 == 0 else x for x in original_tuple)

    data = {
        "Исходный кортеж": original_tuple,
        "Новый кортеж": new_tuple
    }

    with open("lab14_2.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False))

    with open("lab14_2.json", encoding="utf-8") as file:
        xxx = file.read()
        loaded_data = json.loads(xxx)
        print(loaded_data["Новый кортеж"])

process_tuple()
