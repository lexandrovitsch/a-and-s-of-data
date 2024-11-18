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
