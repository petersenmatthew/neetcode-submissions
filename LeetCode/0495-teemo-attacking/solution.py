class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        poison_end = 0
        
        for t in timeSeries:
            if t >= poison_end:
                # no overlap
                total += duration
            else:
                # overlap: only add the extended portion
                total += (t + duration - poison_end)
            
            poison_end = t + duration
        
        return total

# ex: timeSeires = [1,2,4,5,10]
