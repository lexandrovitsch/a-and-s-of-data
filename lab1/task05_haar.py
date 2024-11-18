import numpy as np

def generate_hadamard(n):
    # Рекурсивное построение матрицы Адамара
    if n == 1:
        return np.matrix([[False]], dtype=int)

    quarter_matrix = generate_hadamard(n // 2)
    upper = np.bmat([[quarter_matrix, quarter_matrix]])
    lower = np.bmat([[quarter_matrix, ~quarter_matrix]])
    return np.bmat([[upper], [lower]])

def haar_wavelet_structure_binary(n):
    """Создает список строк, соответствующих бинарным базисам вейвлетов Хаара."""
    haar_basis = []
    for i in range(n // 2):
        base = np.zeros(n, dtype=int)
        base[i] = 1  # Первая часть "включена"
        base[i + n // 2] = 1  # Вторая часть "включена"
        haar_basis.append(base)
    return haar_basis

def find_haar_wavelets(hadamard_matrix):
    """Ищет строки матрицы Адамара, соответствующие бинарным базисам вейвлетов Хаара."""
    n = hadamard_matrix.shape[1]
    haar_basis = haar_wavelet_structure_binary(n)
    matching_rows = []

    for i, row in enumerate(hadamard_matrix):
        for haar_row in haar_basis:
            if np.array_equal(row, haar_row):
                matching_rows.append((i, row))
    return matching_rows

# Ввод размера матрицы
n = 2 ** int(input('Введите степень двойки для размера матрицы >> '))

# Генерация и конвертация матрицы Адамара в целые числа
hadamard_matrix = generate_hadamard(n).astype(int)

# Нахождение вейвлетов Хаара
matching_rows = find_haar_wavelets(hadamard_matrix)

# Вывод строк, соответствующих бинарным вейвлетам Хаара
if matching_rows:
    print("Найдены строки, соответствующие бинарным вейвлетам Хаара:")
    for index, row in matching_rows:
        print(f"Строка {index}: {row.tolist()}")
else:
    print("Бинарные вейвлеты Хаара не найдены в матрице.")
