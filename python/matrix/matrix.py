import numpy as np


class ListView(list):
    def __init__(self, arr: np.array):
        super().__init__(arr)
        self._arr = arr

    def __setitem__(self, index: int, value: int) -> None:
        self._arr[index] = value


class Matrix:
    def __init__(self, matrix_string: str):
        self._matrix = np.asarray([
            [int(n) for n in row.split()] for row in matrix_string.splitlines()
        ])

    def row(self, index: int) -> list[int]:
        return ListView(self._matrix[index - 1])

    def column(self, index: int) -> list[int]:
        return ListView(self._matrix[:, index - 1])


matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
matrix.row(1)[0] = 10
print(matrix.column(1))
