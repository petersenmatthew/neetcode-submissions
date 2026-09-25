import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        ## how to calculate eating time, given k?
        def getEatingTime(k):
            time = 0
            for pile in piles: # O(n)
                pile_time = math.ceil(pile/k)
                time += pile_time
            return time
        
        # ok but we want to find hte lowest k that statisfies time <= h

        # binary search for k
        # what are the mins / max? 
        # min : 1, max : Biggest pile #
        min_k = 1
        max_k = max(piles)

        best_k = max_k
        
        # could make a list of ints from min_k to max_k?
        # maybe not needed?
        while min_k <= max_k:
            mid = (min_k + max_k) // 2
            time = getEatingTime(mid)
            if time > h: ## took too long, need faster eating speed
                min_k = mid + 1
            else: ## good! lets try and then store smthn slower even
                best_k = min(best_k, mid)
                max_k = mid - 1

        return best_k

