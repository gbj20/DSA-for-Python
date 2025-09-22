class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                return False
        return True


arr = [10, 0, 30, 40]
sol = Solution()
print(sol.isSorted(arr))
