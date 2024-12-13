import scipy.linalg as sp
import numpy as np

def sci_hadamard(n):
    matrix = sp.hadamard(n, dtype=int)
    matrix[matrix == -1] = 0
    matrix = np.logical_not(matrix)
    return matrix

def main():
    n = (int((input('Введите степень двойки для размера матрицы >> ')))) ** 2
    print(sci_hadamard(n).astype(int))

if __name__ == '__main__':
    main()
