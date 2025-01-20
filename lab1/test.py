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