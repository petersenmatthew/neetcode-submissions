class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make an array of tuples:
        # ((pointx, point y), distance)

        # max heap it
        # make a max heap of only k elements
        # -> do this by popping while len(max_heap) > k
        max_heap = []

        for point in points:
            distance = (point[0]**2) + (point[1]**2) # square root or not doesnt matter 
            heapq.heappush(max_heap, (-distance, (point[0], point[1])))
            if len(max_heap) > k:
                    heapq.heappop(max_heap)            
        
        output = [[tup[1][0], tup[1][1]] for tup in max_heap]
        return output

