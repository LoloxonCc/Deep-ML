def average(tab: list[float]):
	return sum(x for x in tab) / len(tab)

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		means = [average(row) for row in matrix]
	else:
		means = [average(col) for col in zip(*matrix)]
	return means