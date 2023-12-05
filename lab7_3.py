def xz():
    input_str = input("Введите строку из трех слов: ")
    input_str = input_str.lower()
    words = input_str.split()
    while True:
        if len(words) != 3:
            print('больше 3 слов')
            return False           
        letter_set = set(words[0])
        for word in words[1:]:
            if set(word) != letter_set:
                print("Для записи всех трех слов использован разный набор букв.")  
                return False 
        print("Для записи всех трех слов использован одинаковый набор букв.")  
        return False         
xz()