def mean(vector: list[float]) -> float:
	return sum(x for x in vector) / len(vector)

def covariance(vec1: list[float], vec2: list[float()]) -> float:
	mean1, mean2 = mean(vec1), mean(vec2)
	return sum((x - mean1) * (y - mean2) / (len(vec1) - 1) for x, y in zip(vec1, vec2))

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	flat = [covariance(i, j) for i in vectors for j in vectors]
	return [flat[i * len(vectors):(i + 1) * len(vectors)] for i in range(len(vectors))]