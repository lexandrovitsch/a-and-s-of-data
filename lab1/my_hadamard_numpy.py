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
