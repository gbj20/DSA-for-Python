from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            # Base case: valid combination
            if len(path) == k and total == n:
                result.append(path.copy())
                return
            # Prune invalid paths
            if total > n or len(path) > k:
                return

            for num in range(start, 10):  # numbers 1–9
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()  # backtrack

        backtrack(1, [], 0)
        return result


obj = Solution()
print(obj.combinationSum3(3, 7))
