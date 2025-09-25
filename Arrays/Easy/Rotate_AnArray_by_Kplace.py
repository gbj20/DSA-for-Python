from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n   
        temp = nums[n-k:]   

        for i in range(n-k-1, -1, -1):  
            nums[i+k] = nums[i]

        nums[:k] = temp  
nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
print(nums)
