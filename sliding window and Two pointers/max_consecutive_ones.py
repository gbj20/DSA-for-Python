from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        right = 0
        zeros = 0
        n = len(nums)
        while right<n:
            if nums[right] ==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            if zeros<=right:
                maxi = max(maxi,right-left+1)
            right+=1
        return maxi
obj = Solution()
print(obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
