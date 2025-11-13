# https://www.deep-ml.com/problems/1

import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

    a = np.array(a)
    b = np.array(b)

    shape_a = a.shape

    if shape_a[1] != b.size:
        return -1
    
    dot = np.dot(a, b).tolist()

	return dot