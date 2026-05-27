class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l = 0 # buy day idx
       r = 0 # sell day idx
       best = 0
       while r < len(prices):
            profit = prices[r] - prices[l]
            best = max(profit, best)
            if profit < 0:
                l = r
            r+=1
       return best
