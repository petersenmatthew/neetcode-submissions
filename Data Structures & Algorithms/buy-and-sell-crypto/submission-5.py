class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 0
        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit < 0:
                left = right
            else:
                max_profit = max(profit, max_profit)
            right +=1
        return max_profit