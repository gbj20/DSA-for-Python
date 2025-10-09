from typing import List

class Solution:
    def lowerBound(self, arr: List[int], x: int) -> int:
        n = len(arr)
        lower_bound = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        return lower_bound

    def upperBound(self, arr: List[int], x: int) -> int:
        n = len(arr)
        upper_bound = n
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > x:
                upper_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        return upper_bound

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)

        # Check if target exists
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
obj = Solution()
print(obj.searchRange(nums, target))  # Output: [3, 4]
