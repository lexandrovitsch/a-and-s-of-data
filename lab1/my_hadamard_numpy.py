import numpy as np

def generate_hadamard(n):
    if n == 1:
        return np.matrix([[False]])
    
    # Рекурсивно обращаемся к generate_hadamard с 1/2 размером (четверть требуемой матрицы)
    quarter_matrix = generate_hadamard(n // 2)
    
    # Составляем верхнюю и нижнюю части матрицы
    upper = np.bmat([[quarter_matrix, quarter_matrix]])
    lower = np.bmat([[quarter_matrix, ~quarter_matrix]])
    
    return np.bmat([[upper], [lower]])
    
def main():    
    n = (int((input('Введите степень двойки для размера матрицы >> ')))) ** 2
    result = generate_hadamard(n)
    print(generate_hadamard(n).astype(int))

if __name__ == '__main__':
    main()
