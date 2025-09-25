#Brute force solution

# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         n = len(nums)
#         freq_map = {}
#         for i in range(0,n):
#             freq_map[nums[i]]=0
#         j = 0
#         for k in freq_map:
#             nums[j] = k
#             j+=1
#         return j

# nums = [1, 1, 1, 2, 3, 5, 56]
# sol = Solution()
# print(sol.removeDuplicates(nums))


#optimal Solution
class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        i = 0
        j = i+1
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j+=1
        return i+1


nums = [1, 1, 1, 2, 3, 5, 56]
sol = Solution()
print(sol.removeDuplicates(nums))
