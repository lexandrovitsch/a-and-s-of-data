import scipy.linalg as sp

def sci_hadamard(n):
    matrix = sp.hadamard(n, int)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix
