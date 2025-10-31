from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(0,len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i+nums[i])
        return True
nums = [2,3,1,1,4]
sol = Solution()
print(sol.canJump(nums))