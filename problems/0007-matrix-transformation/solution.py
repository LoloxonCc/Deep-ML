import numpy as np

def isInvertible(matrix):
	return np.linalg.det(matrix) != 0.0

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if not isInvertible(T) or not isInvertible(S):
		return -1
	return np.matmul(np.linalg.inv(T), np.matmul(A, S))