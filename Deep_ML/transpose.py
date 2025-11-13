# https://www.deep-ml.com/problems/2

import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    mat = np.array(a)
    b = mat.T.tolist()
	return b