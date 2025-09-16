"""
You're given an array (arr)
Return the frequency of element x in the given array
"""


class Solution:
    def findFrequency(self, arr, x):
        hash_map = {}
        n = len(arr)
        for i in range(n):
            hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1

        return hash_map.get(x, 0)


arr = [1, 2, 4, 1, 2, 4]
x = 2
sol = Solution()
print(sol.findFrequency(arr, x))
