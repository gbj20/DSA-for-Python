class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        num = abs(x)
        result = 0
        while num > 0:
            last_digit = num % 10
            result = (result * 10) + last_digit
            num = num // 10

        result = sign * result

        #Check 32-bit signed integer range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result


s = Solution()
print(s.reverse(123))        
print(s.reverse(-123))      
print(s.reverse(1534236469)) 
