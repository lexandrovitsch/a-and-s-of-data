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
