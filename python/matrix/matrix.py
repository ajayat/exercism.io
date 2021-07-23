class Matrix:
    def __init__(self, matrix_string: str):
        self._matrix = [row.split() for row in matrix_string.split("\n")]
        self._transposed = tuple(zip(*self._matrix))

    def row(self, index: int) -> list:
        return list(map(int, self._matrix[index-1]))

    def column(self, index: int) -> str:
        return list(map(int, self._transposed[index-1]))
