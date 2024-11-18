students = [] # Ф, И, О, год рождения, группа, средний балл

# Функция, добавляющая запись в базу данных
def add_entry(last_name, first_name, middle_name, birth_year, group, average_score):
    students.append([[first_name], [last_name], [middle_name], [birth_year], [group], [average_score]])

# Функция вывода всей базы данных на экран (лучше переделать!)
def to_string_all():
    for i in students:
        print(i)


# Функция поиска по определённому полю
def search_by(by, string):
    for i in students:
        if string in i[by]:
            print(f'Найдено: {i}')


def edit_entry(entry_index, replacement):
    students[entry_index] = replacement


# def sort_by():

is_running = True
while is_running:
    choice = input('Выберите режим: 1) - Добавить запись;\n2) - Искать\nВыбор >> ')

    if choice == '1':
        input_entry = input('Введите, разделяя пробелами: Ф, И, О, год рождения, группа, средний балл >> ').split()
        add_entry(input_entry[0], input_entry[1], input_entry[2], input_entry[3], input_entry[4], input_entry[5])
        print('Запись добавлена')
    elif choice == '2':
        search_by_x = int(input('Выберите поле для поиска. 1, 2, 3 - Ф, И, О 4 - Год, 5 - Группа, 6 - Средний балл >> '))
        search_string = input('Введите строку для поиска >> ')

        search_by(search_by_x, search_string)
    else:
        is_running = False
