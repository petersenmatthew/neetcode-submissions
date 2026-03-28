class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find a pair b, s where you maximize prices[s]] - prices[b] , s > b
        # profit = prices[s] - prices[b]
        l, r, best = 0, 1 ,0
        while r < len(prices):
            best = max(prices[r] - prices[l], best)
            if prices[l] > prices[r]: # move l up 1 and reset r if net loss
                l += 1
                r = l + 1
            else:
                r+=1
        return best
