from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Helper DFS function to mark boundary-connected land
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 0  # mark visited (convert land to sea)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # Step 1: Remove all land cells (1s) connected to the boundary
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][n-1] == 1:
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[m-1][j] == 1:
                dfs(m-1, j)

        # Step 2: Count remaining land cells (enclaves)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count


grid = [[0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]

result = Solution().numEnclaves(grid)
print("Number of Enclaves:", result)
