def dot_product(vec1, vec2):
	return sum(x * y for x, y in zip(vec1, vec2))

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    flat = [dot_product(row, col) for row in a for col in zip(*b)]
    return [flat[i * len(b[0]):(i + 1) * len(b[0])] for i in range(len(a))]