class MedianFinder:

    def __init__(self):
        # keep a heap
        # on find median, make a deep copy of the heap and then pop len / 2 times to get median

        self.min_heap = [] # upper half
        self.max_heap = [] # lower half

    def addNum(self, num: int) -> None:
        # all nums in min_heap must be greater than max_heap
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        
        if self.max_heap and -self.max_heap[0] < num: # push to min_heap
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        # balance them
        if len(self.min_heap) - len(self.max_heap) > 1: # upper half heavy
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        # if its odd, one heap will be bigger
        # return that 
        if (len(self.min_heap) + len(self.max_heap)) % 2 != 0:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        
        # even, return both the tops mean
        else:
            return ((-self.max_heap[0] + self.min_heap[0]) / 2)

