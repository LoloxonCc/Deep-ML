def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    d = det(matrix)
    if d == 0:
        return None
    return [[matrix[1][1] / d, -matrix[0][1]/d], [-matrix[1][0]/d, matrix[0][0]/d]]