from openpyxl import load_workbook

def read_and_process_excel_file(file_name):
    workbook = load_workbook(file_name)
    
    sheet = workbook.active

    original_tuple = tuple(sheet[1][i].value for i in range(1, 11))
    new_tuple = tuple(sheet[2][i].value for i in range(1, 11))

    print("Исходный кортеж:", original_tuple)
    print("Новый кортеж:", new_tuple)

read_and_process_excel_file("lab14_5.xlsx")
