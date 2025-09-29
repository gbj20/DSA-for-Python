class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        for i in range(0, n):
            if nums[i]+nums[i+1] == target:
                return [i, i+1]


 
nums = [1, 2, 3, 6]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
