class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                return i


nums = [0, 1, 3, 4, 2]
sol = Solution()
print(sol.missingNumber(nums))
