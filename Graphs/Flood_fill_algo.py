from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        # If the starting pixel already has the target color, no change is needed
        if original_color == color:
            return image

        def dfs(r, c):
            # Base case: Out of bounds or different color
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
            image[r][c] = color  # Change color

            # Explore all 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image


image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
color = 2

print(Solution().floodFill(image, sr, sc, color))
