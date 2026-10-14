def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	flat = [scalar * a for row in matrix for a in row]
	return [flat[i * len(matrix[0]):(i + 1) * len(matrix[0])] for i in range(len(matrix))]