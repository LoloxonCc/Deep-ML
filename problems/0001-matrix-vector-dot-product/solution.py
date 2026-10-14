def dot_product(vec1, vec2):
	return sum(x * y for x, y in zip(vec1, vec2))

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	return [dot_product(x, b) for x in a]