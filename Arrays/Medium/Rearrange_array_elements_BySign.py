from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        n = len(nums)
        for i in range(0, n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        print(pos)
        print(neg)
        for i in range(0, len(pos)):
            nums[2*i] = pos[i]
            nums[(2*i)+1] = neg[i]
        return nums


nums = [3, 1, -2, -5, 2, -4]
sol = Solution()
print(sol.rearrangeArray(nums))
