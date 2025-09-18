
class Solution:
    def func(self, s, l, r):
        n = len(s)
        l = 0
        r = n-1
        if s[l] >= s[r]:
            return True
        if s[l] != s[r]:
            return False


sol = Solution()
print(sol.func("MADAM", 0, 5))
