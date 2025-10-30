from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def backtrack(row):
            # Base case: all queens placed
            if row == n:
                solution = ["".join(r) for r in board]
                result.append(solution)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Backtrack
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result


obj = Solution()
for sol in obj.solveNQueens(4):
    for row in sol:
        print(row)
    print()
