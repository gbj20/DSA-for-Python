from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, path, total):
            # If target is reached, add combination
            if total == target:
                result.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicate values at same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose current number and move to next
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], 0)
        return result


obj = Solution()
print(obj.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
