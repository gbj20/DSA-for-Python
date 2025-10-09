from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)

    def binary_search(self, nums, low, high, target):
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, high, target)
        else:
            return self.binary_search(nums, low, mid - 1, target)


obj = Solution()
print(obj.search([1, 3, 5, 7, 9], 7))  # Output: 3
print(obj.search([1, 3, 5, 7, 9], 2))  # Output: -1
