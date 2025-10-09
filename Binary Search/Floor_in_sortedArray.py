class Solution:
    def findFloor(self, arr, x):
        n = len(arr)
        ans = -1  # default if no floor exists
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


obj = Solution()
print(obj.findFloor([1, 3, 5, 7, 9], 7))
print(obj.findFloor([1, 3, 5, 7, 9], 2))
