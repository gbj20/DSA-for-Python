class Solution:
    def search(self, arr, x):
        n = len(arr)
        for i in range(0, n):
            if arr[i] == x:
                return i
            
        return -1


arr = [1, 12, 33, 4]
sol = Solution()
print(sol.search(arr, 3))
