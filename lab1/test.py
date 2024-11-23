import pytest, numpy as np, scipy_hadamard
from my_hadamard_numpy import generate_hadamard

@pytest.mark.parametrize("n", [2, 4, 8, 16])
def test_hadamard(n):
    m1 = generate_hadamard(n).astype(int)
    m2 = scipy_hadamard(n)

    assert np.array_equal(m1, m2), f'Матрицы не совпадают для n={n}'
