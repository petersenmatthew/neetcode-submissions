import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -max_heap[0] # x is heaviest stone
            heapq.heappop(max_heap)
            y = -max_heap[0] # y is second heaviest stone

            heapq.heappop(max_heap)
            # y will also be <= x
            if x != y:
                heapq.heappush(max_heap, -(x - y))
            
        
        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]