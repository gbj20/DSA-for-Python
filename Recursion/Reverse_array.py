class Solution:
    def reverseSubArray(self, arr, l, r):

        if l >= r:
            return arr
        arr[l], arr[r] = arr[r], arr[l]
        return self.reverseSubArray(arr, l + 1, r - 1)


arr = [1, 2, 3, 4, 5, 6, 7]
sol = Solution()
print(sol.reverseSubArray(arr, 2, 5))
