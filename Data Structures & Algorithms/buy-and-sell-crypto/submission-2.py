class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find a pair b, s where you maximize prices[s]] - prices[b] , s > b
        # profit = prices[s] - prices[b]
        l = 0
        if len(prices) == 1:
            return 0
        r = 1
        best = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            best = max(profit, best)
            if prices[l] > prices[r]: # move l up 1 and reset r if net loss
                l = r
                r = l + 1
            else:
                r+=1
        return best