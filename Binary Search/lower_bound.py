class Solution:
    def lowerBound(self, arr, x):
        n = len(arr)
        lower_bound = n
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                lower_bound = mid  # possible answer
                high = mid - 1     # search for smaller index
            else:
                low = mid + 1
        return lower_bound


obj = Solution()
print(obj.lowerBound([1, 3, 5, 7, 9], 7))
print(obj.lowerBound([1, 3, 5, 7, 9], 2))
