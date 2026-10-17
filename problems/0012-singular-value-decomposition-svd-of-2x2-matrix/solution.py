import numpy as np
import math 

def delta(a, b, c):
	return b ** 2 - 4 * a * c

def quadratic_roots(a, b, c):
	if delta(a, b, c) < 0:
		return []
	x_1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
	x_2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
	return [x_1, x_2]

def tr(matrix):
	return sum(matrix[i][i] for i in range(len(matrix)))  

def det(matrix):
	return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	return quadratic_roots(1, -tr(matrix), det(matrix))

def formSymmetricMatrix(A: np.ndarray) -> np.ndarray:
    return np.transpose(A) @ A

def optimalAngle(A: np.ndarray) -> float:
    if A[0][0] == A[1][1]:
        return np.pi / 4
    return 0.5 * np.arctan2(2 * A[0][1], (A[0][0] - A[1][1]))

def jacobiRotation(A: np.ndarray) -> np.ndarray:
    thetha = optimalAngle(A)
    return np.array([[np.cos(thetha), - np.sin(thetha)], [np.sin(thetha), np.cos(thetha)]])

def sigmaInverse(sigma1, sigma2) -> np.ndarray:
    return np.array([[1 / sigma1, 0], [0, 1/sigma2]])

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    B = formSymmetricMatrix(A)
    V = jacobiRotation(B)
    lambda1, lambda2 = calculate_eigenvalues(V.T @ B @ V)
    sigma1, sigma2 = np.sqrt(lambda1), np.sqrt(lambda2)
    if sigma1 < sigma2:
        sigma1, sigma2 = sigma1, sigma2
    U = A @ V @ sigmaInverse(sigma1, sigma2)
    return U, np.array([sigma1, sigma2]), V.T