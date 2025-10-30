class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        ans = [-1] * n
        stack = []   

        for i in range(n - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) != 0:
                ans[i] = stack[-1]
            stack.append(arr[i])
        return ans


arr = [6, 8, 0, 1, 3]
obj = Solution()
print(obj.nextLargerElement(arr))
