class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end=' ')
        self.printNos(n-1)  # head Recursion


sol = Solution()
sol.printNos(10)
