from typing import List


class Solution:
    def subsetSums(self, arr: List[int]) -> List[int]:
        result = []

        def backtrack(index, current_sum):
            # Base case: reached end of array
            if index == len(arr):
                result.append(current_sum)
                return

            # Include current element
            backtrack(index + 1, current_sum + arr[index])

            # Exclude current element
            backtrack(index + 1, current_sum)

        backtrack(0, 0)
        return result


obj = Solution()
print(obj.subsetSums([2, 3]))
