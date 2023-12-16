import random
from openpyxl import Workbook

def process_tuple():
    original_tuple = tuple(random.randint(1, 128) for _ in range(10))
    new_tuple = tuple(0 if x % 5 == 0 else x for x in original_tuple)

    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["Исходный кортеж"] + list(original_tuple))
    sheet.append(["Новый кортеж"] + list(new_tuple))

    workbook.save("lab14_5.xlsx")

process_tuple()