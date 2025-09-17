class Solution:
    def printNos(self, n):
        if n == 0:
            return
        self.printNos(n-1) ##tail Recursion
        print(n, end=' ')
        


sol = Solution()
sol.printNos(10)
