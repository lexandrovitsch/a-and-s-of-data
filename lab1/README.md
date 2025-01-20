# Задание 1
> Написать на Python генератор нулевой матрицы.

Реализация:

> Листинг 1 - _Исходный код генератора пустой матрицы_
```Python
# Функция генерации пустой матрицы
def generate_empty_matrix(size):
    matrix = []

    for i in range(size):
        matrix.append([False] * size)
    
    return matrix

size = int(input('Укажите размер матрицы >> '))

matrix = generate_empty_matrix(size)

# Конвертация матрицы из boolean в int
for i in range(size):
    for j in range(size):
        matrix[i][j] = int(matrix[i][j])

# Построчный вывод матрицы
for _ in range(size):
    print(matrix[_])

```

# Задание 2
> Модифицировать программу, добавив возможность заполнять единицами выбранную пользователем четверть.

Реализация:

> Листинг 2 - _Исходный код программы, которая заполняет выбранную четверть матрицы единицами_
```Python
# Функция генерации пустой матрицы
def generate_empty_matrix(size):
    matrix = []

    for i in range(size):
        matrix.append([False] * size)
    
    return matrix


def replace_quarter(matrix, quarter):
    if quarter == 0:
        return matrix
    
    elif quarter % 4 == 1:  # Верхняя левая четверть
        k = size
        for i in range(k):
            for j in range(k):
                matrix[i][j] = not(matrix[i][j])
                if k == 0:
                    break
            k -= 1
    
    elif quarter % 4 == 2:  # Верхняя правая четверть
        k = size
        for i in range(k):
            for j in range(size - k, size):
                matrix[i][j] = not(matrix[i][j])
            k -= 1
    
    elif quarter % 4 == 3:  # Нижняя левая четверть
        k = size
        for i in range(size - 1, -1, -1):
            for j in range(k):
                matrix[i][j] = not(matrix[i][j])
            k -= 1
    
    elif quarter % 4 == 0:  # Нижняя правая четверть
        k = size
        for i in range(size - 1, -1, -1):
            for j in range(size - k, size):
                matrix[i][j] = not(matrix[i][j])
            k -= 1

    return matrix


size = int(input('Укажите размер матрицы >> '))
quarter = int(input('Укажите четверть >> '))

matrix = generate_empty_matrix(size)
matrix = replace_quarter(matrix, quarter)

# Конвертация матрицы из boolean в int
for i in range(size):
    for j in range(size):
        matrix[i][j] = int(matrix[i][j])

# Построчный вывод матрицы
for _ in range(size):
    print(matrix[_])

```

# Задание 3
> Написать на Python генератор матрицы Адамара без использования посторонних библиотек (_Бонус, если генератор написан через рекурсию_).

Реализация:

> Листинг 3 - _Исходный код генератора матрицы Адамара с рекурсией_
```Python
def generate_hadamard(n):
    if n == 1:
        return [[False]]
    
    # Рекурсивно обращаемся к generate_hadamard с 1/2 размером (четверть требуемой матрицы)
    quarter_matrix = generate_hadamard(n // 2)
    
    # Составляем верхнюю часть матрицы из двух четвертей
    upper = [line + line for line in quarter_matrix]
    
    # Составляем нижнюю часть матрицы из двух четвертей, половину инвертируем
    lower = [line + [(not x) for x in line] for line in quarter_matrix]
    
    return upper + lower
    
    
n = (int((input('Введите степень двойки для размера матрицы >> ')))) ** 2

result = generate_hadamard(n)

# Конвертируем все boolean в int
for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = int(result[i][j])

# Выводим матрицу
for i in result:
    print(i)

```
# Задание 4
> Модифицировать программу из _задания 3_ так, чтобы вместо **списков** использовалась структура данных **matrix** из **numpy**.

Реализация:

> Листинг 4 - _Исходный код генератора матрицы Адамара с рекурсией с использованием numpy_
```Python
import numpy as np

def generate_hadamard(n):
    if n == 1:
        return np.array([[False]])
    
    # Рекурсивно обращаемся к generate_hadamard с 1/2 размером (четверть требуемой матрицы)
    quarter_matrix = generate_hadamard(n // 2)
    
    # Составляем верхнюю и нижнюю части матрицы
    upper = np.block([[quarter_matrix, quarter_matrix]])
    lower = np.block([[quarter_matrix, np.logical_not(quarter_matrix)]])
    
    return np.block([[upper], [lower]])
    
def main():    
    n = (int((input('Введите степень двойки для размера матрицы >> ')))) ** 2
    print(generate_hadamard(n).astype(int))

if __name__ == '__main__':
    main()

```

# Задание 5
> Модифицировать программу из _задания 4_ так, чтобы она искала в строках матрицы Адамара вейвлеты Хаара. Выводить соответствующие строки на экран.

Реализация:

> Листинг 5 - _Исходный код программы поиска вейвлетов Хаара внутри матрицы Адамара_
```Python
from my_hadamard_numpy import generate_hadamard

def is_haar_row(row):
    middle = len(row) // 2
    half_1 = row[:middle]
    half_2 = row[middle:]

    for i in range(middle):
        if (half_1[i] == False and half_2[i] != True) or (half_1[i] == True and half_2.all() != False):
            return False
    
    return True

def count_haar_rows(rows):
    counter = 0
    matches = []
    for row in rows:
        if is_haar_row(row):
            matches.append(row)
            counter += 1
    
    return matches, counter

n = (int((input('Введите степень двойки для размера матрицы >> ')))) ** 2

hadamard = generate_hadamard(n)
matches, count = count_haar_rows(hadamard)

print(f'Количество совпадений: {count}\n')

print('Совпадения:')
for i in matches:
    print(i.astype(int))

```

# Задание 6
> Добавить в программу из _задания 4_ фреймворк **pytest**, он должен сверять самописную матрицу с матрицей из библиотеки **scipy**

Реализация:

> Листинг 6 - _Исходный код программы, использующей pytest для сравнения самописной матрицы с матрицей из scipy_
```Python
import numpy as np
import scipy.linalg as sp
import pytest

from my_hadamard_numpy import generate_hadamard
from scipy_hadamard import sci_hadamard

@pytest.mark.parametrize('n', [2, 4, 8, 16, 32])
def test_hadamard(n):
    matrix1 = generate_hadamard(n).astype(int)
    matrix2 = sci_hadamard(n)

    assert np.array_equal(matrix1, matrix2)
    f'Не совпадают при n = {n}'

```
