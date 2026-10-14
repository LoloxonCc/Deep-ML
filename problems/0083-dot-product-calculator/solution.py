import numpy as np

def calculate_dot_product(vec1, vec2):
	return sum(x * y for x, y in zip(vec1, vec2))