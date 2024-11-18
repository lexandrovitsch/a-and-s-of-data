from scipy.linalg import hadamard

def generate_hadamard(n):
    matrix = hadamard(n, int)
    print(len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix
    
    return matrix

n = (int(input("Введите степень двойки для размера матрицы >> "))) ** 2
print(generate_hadamard(n))