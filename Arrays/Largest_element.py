class Solution:
    def largest(self, arr):
        n = len(arr)
        largest = arr[0]
        for i in range(0, n):
            largest = max(largest, arr[i])
        return largest


arr = [10, 50, 60, 5, 90]
sol = Solution()
print(sol.largest(arr))
