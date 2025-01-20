students = []  # Список студентов: [Фамилия, Имя, Отчество, Год рождения, Группа, Средний балл]

# Функция, добавляющая запись в базу данных
def add_entry(last_name, first_name, middle_name, birth_year, group, average_score):
    students.append([last_name, first_name, middle_name, int(birth_year), group, float(average_score)])

# Функция поиска по определённому полю
def search_by(field_index, search_value):
    results = []
    for student in students:
        if str(search_value).lower() in str(student[field_index]).lower():
            results.append(student)
    if results:
        print("Найдено:")
        for result in results:
            print(result)
    else:
        print("Записей не найдено.")

# Функция редактирования записи
def edit_entry(entry_index, new_entry):
    if 0 <= entry_index < len(students):
        students[entry_index] = new_entry
        print("Запись обновлена.")
    else:
        print("Некорректный индекс записи.")

# Функция сортировки базы данных
def sort_by(field_index):
    global students
    students.sort(key=lambda x: x[field_index])
    print("База данных отсортирована.")

# Функция удаления записи
def delete_entry(entry_index):
    if 0 <= entry_index < len(students):
        removed = students.pop(entry_index)
        print(f"Запись удалена: {removed}")
    else:
        print("Некорректный индекс записи.")

# Главная программа
def main():
    is_running = True
    while is_running:
        print("\nМеню:")
        print("1) Добавить запись")
        print("2) Искать запись")
        print("3) Редактировать запись")
        print("4) Удалить запись")
        print("5) Сортировать базу данных")
        print("6) Показать все записи")
        print("7) Выход")
        choice = input("Выбор >> ")

        if choice == '1':
            input_entry = input("Введите через пробел: Фамилия Имя Отчество Год_рождения Группа Средний_балл >> ").split()
            if len(input_entry) == 6:
                add_entry(input_entry[0], input_entry[1], input_entry[2], input_entry[3], input_entry[4], input_entry[5])
                print("Запись добавлена.")
            else:
                print("Ошибка: неверное количество данных.")
        
        elif choice == '2':
            search_by_x = int(input("Выберите поле для поиска (0-Фамилия, 1-Имя, 2-Отчество, 3-Год, 4-Группа, 5-Средний балл) >> "))
            search_string = input("Введите строку для поиска >> ")
            if 0 <= search_by_x <= 5:
                search_by(search_by_x, search_string)
            else:
                print("Некорректный выбор поля.")
        
        elif choice == '3':
            try:
                entry_index = int(input("Введите индекс записи для редактирования >> "))
                new_entry = input("Введите новую запись через пробел (Фамилия Имя Отчество Год_рождения Группа Средний_балл) >> ").split()
                if len(new_entry) == 6:
                    edit_entry(entry_index, [new_entry[0], new_entry[1], new_entry[2], int(new_entry[3]), new_entry[4], float(new_entry[5])])
                else:
                    print("Ошибка: неверное количество данных.")
            except ValueError:
                print("Ошибка: индекс или данные неверны.")
        
        elif choice == '4':
            try:
                entry_index = int(input("Введите индекс записи для удаления >> "))
                delete_entry(entry_index)
            except ValueError:
                print("Ошибка: некорректный индекс.")
        
        elif choice == '5':
            sort_by_x = int(input("Выберите поле для сортировки (0-Фамилия, 1-Имя, 2-Отчество, 3-Год, 4-Группа, 5-Средний балл) >> "))
            if 0 <= sort_by_x <= 5:
                sort_by(sort_by_x)
            else:
                print("Некорректный выбор поля.")
        
        elif choice == '6':
            print("Все записи:")
            for i, student in enumerate(students):
                print(f"{i}: {student}")
        
        elif choice == '7':
            is_running = False
            print("Выход из программы.")
        
        else:
            print("Некорректный выбор.")

# Запуск программы
if __name__ == "__main__":
    main()