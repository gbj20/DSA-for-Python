from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        queue = deque()

        # Step 1: Add all 0s to the queue and mark their distance as 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        # Step 2: Directions → up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 3: BFS traversal
        while queue:
            i, j = queue.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))

        return dist


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(Solution().updateMatrix(mat))
