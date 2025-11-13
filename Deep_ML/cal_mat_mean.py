# https://www.deep-ml.com/problems/4

import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	mat = np.array(matrix)
	
	if mode == 'row':
		means = np.mean(mat, axis=1).tolist()
	else:
		means = np.mean(mat, axis=0).tolist()

	return means