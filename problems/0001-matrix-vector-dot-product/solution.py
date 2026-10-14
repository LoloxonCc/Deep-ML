import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1;
	return (np.matmul(a, b)).tolist()