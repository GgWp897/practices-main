students = [
    {
        "Фамилия": "Иванов",
        "Имя": "Петр",
        "Пол": "М",
        "Возраст": 20,
        "Группа": "Группа A",
        "Оценка по математике": 4,
        "Оценка по физике": 4,
        "Оценка по химии": 5
    },
    {
        "Фамилия": "Петрова",
        "Имя": "Мария",
        "Пол": "Ж",
        "Возраст": 19,
        "Группа": "Группа B",
        "Оценка по математике": 3,
        "Оценка по физике": 2,
        "Оценка по химии": 4
    },
    {
        "Фамилия": "Сидоров",
        "Имя": "Алексей",
        "Пол": "М",
        "Возраст": 21,
        "Группа": "Группа A",
        "Оценка по математике": 5,
        "Оценка по физике": 4,
        "Оценка по химии": 3
    }
]

# Выводим студентов, у которых есть хотя бы одна тройка или двойка
for student in students:
    if 2 in [student["Оценка по математике"], student["Оценка по физике"], student["Оценка по химии"]] or  3 in [student["Оценка по математике"], student["Оценка по физике"], student["Оценка по химии"]]:
        print(f"{student['Фамилия']} {student['Имя']} ({student['Группа']}): "f"Математика - {student['Оценка по математике']}, "f"Физика - {student['Оценка по физике']}, "f"Химия - {student['Оценка по химии']}")
