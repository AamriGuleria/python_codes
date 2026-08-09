# brute force solution
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]-prices[i] > max_profit:
                    max_profit = prices[j]-prices[i]

        return max_profit

# Improved O(N) approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_buy_price=prices[0]
        max_profit=0
        n = len(prices)
        for i in range(n):
            max_profit = max(max_profit,prices[i]-minimum_buy_price)
            if prices[i]<minimum_buy_price:
                minimum_buy_price = prices[i]
        return max_profit