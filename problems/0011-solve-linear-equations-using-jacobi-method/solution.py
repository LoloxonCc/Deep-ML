import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = [0.0 for i in range(len(b))]
	for _ in range(n):
		x_new = [0.0 for i in range(len(b))]
		for i in range(len(b)):
			s = sum(A[i][j] * x[j] for j in range(len(b)) if j != i)
			x_new[i] = (b[i] - s) / A[i][i] 
		x = x_new
	return [round(val, 4) for val in x]