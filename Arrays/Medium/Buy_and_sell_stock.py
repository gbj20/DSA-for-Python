from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float("inf")
        n = len(prices)
        for i in range(0,n):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit,prices[i]-min_price)
        return max_profit
prices =[7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))