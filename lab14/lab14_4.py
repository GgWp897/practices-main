import random
import csv

def process_tuple():
    original_tuple = tuple(random.randint(1, 128) for _ in range(10))
    new_tuple = tuple(0 if x % 5 == 0 else x for x in original_tuple)

    with open("lab14_4.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Исходный кортеж"] + list(original_tuple))
        writer.writerow(["Новый кортеж"] + list(new_tuple))
    
    with open("lab14_4.csv", "r", newline='', encoding="utf-8") as f:
        data = csv.reader(f)
        for row in data:
            print(row)

process_tuple()
