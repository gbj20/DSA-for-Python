class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num = abs(x)
        result = 0
        while num > 0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num // 10
        return x==result


s = Solution()
print(s.isPalindrome(121))        
print(s.isPalindrome(-121))      
print(s.isPalindrome(10)) 