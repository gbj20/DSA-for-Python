from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(0, n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(0, n):
            matrix[i].reverse()

matrix = [
    [19, 10, 11],
    [21, 20, 14],
    [31, 13, 15]
]

Solution().rotate(matrix)
print(matrix)
