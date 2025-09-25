from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break


nums = [1, 0, 1, 0, 3, 0, 56]
sol = Solution()
sol.moveZeroes(nums)
print(nums)
