class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0

        # hash map of each task and its frequency?

        # algo:
        # choose the task to process
        # one with highest reamining frequency
        # set a cooldown for that task
        # try to find another task to process 
        # if no other, then just idle for that cycle
        # go back to cooldowned task (if existing cycles to go)
        hash_map = {}
        for task in tasks:
            if task not in hash_map:
                hash_map[task] = 1
            else:   
                hash_map[task] += 1
        
        # create max heap with (-frequency, task)

        max_heap = []
        for task in hash_map:
            heapq.heappush(max_heap, (-hash_map[task], task))
        # cooldown_queue (remaining_frequency, task, available_at)

        cooldown_queue = deque()
        while len(max_heap) > 0 or len(cooldown_queue) > 0:
            if cooldown_queue and cooldown_queue[0][2] <= cycles:
                freq, task, available_at = cooldown_queue.popleft()
                heapq.heappush(max_heap, (-freq, task))
            
            if max_heap:
                # process it and then add to cooldown if still remaning
                freq, task = heapq.heappop(max_heap)
                freq = -freq
                if freq > 1:
                    cooldown_queue.append((freq - 1, task, cycles + n + 1))
                

            cycles += 1
        
        return cycles