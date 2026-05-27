class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Create buckets (index = frequency)
        # We need len(nums) + 1 buckets to handle 0 to n frequencies
        buckets = [[] for _ in range(len(nums) + 1)]        

        for num, freq in count.items():
            # 2. Use .append() to keep ALL numbers with this frequency
            buckets[freq].append(num)
            
        result = []
        i = len(buckets) - 1
        
        # 3. Use the while loop safely
        while i > 0 and len(result) < k:
            # Check if the bucket has numbers (is not empty)
            if buckets[i]: 
                # Since buckets[i] is a list, we must add its contents
                for val in buckets[i]:
                    result.append(val)
                    if len(result) == k:
                        return result
            i -= 1
