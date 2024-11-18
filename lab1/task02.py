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
