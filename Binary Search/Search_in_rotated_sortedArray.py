from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 5
obj = Solution()
print(obj.search(nums, target))
