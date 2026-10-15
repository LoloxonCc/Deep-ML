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