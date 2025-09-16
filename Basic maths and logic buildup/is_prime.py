# class Solution:
#     def isPrime(self, n):
#         if n <= 1:
#             return False
#         count = 0
#         for i in range(1, n + 1):
#             if n % i == 0:
#                 count += 1
#         return count == 2


from math import sqrt

class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        count = 0
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:  
                    count += 1

        return count == 2   
sol = Solution()
print(sol.isPrime(25))  
print(sol.isPrime(7))  
