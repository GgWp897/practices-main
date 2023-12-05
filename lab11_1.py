class Human:
    def __init__(self, name, age, gender, ssn):
        self.name = name
        self.age = age
        self.gender = gender
        self.__ssn = ssn 

    def introduce(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет, и я {self.gender}."

    def get_ssn(self):
        return self.__ssn

    @staticmethod
    def is_adult(age):
        return age >= 18  

person1 = Human("Иван", 25, "мужчина", "123-45-6789")
person2 = Human("Мария", 16, "женщина", "987-65-4321")

print(person1.gender)  
print(person1.introduce())  
print(person1.get_ssn())
print(person1.is_adult(person1))  
print(Human.is_adult(person2.age))  
