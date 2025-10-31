class Solution:
    def findMin(self, n):
        coins = [10, 5, 2, 1]  
        count = 0               

        for coin in coins:
            if n >= coin:
                count += n // coin   
                n = n % coin         
            if n == 0:
                break

        return count
print(Solution().findMin(39))
