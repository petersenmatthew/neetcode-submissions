class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return the top k most frequent elements
        # DS: 
        # Map? With key: value = num : frequency
        # 3: 2, 4: 1, 5: 3
        # sort it?  n log n 
        # array where the index is the frequency, and the array[i] = num

        # 1) make frequency map
        frequency_map = {}
        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1;
            else:
                frequency_map[num] = 1
        
        frequency_array = [[] for _ in range(len(nums) + 1)]

        # wqhat if two nums share a frequency??
        for num in frequency_map.keys():
            frequency_array[frequency_map[num]].append(num)
        

        output = []
        nums_added = 0
        i = len(frequency_array) - 1
        # frequency_array = [[], [1], [2], [3, 4]]
        while nums_added < k:
            for num in frequency_array[i]:
                output.append(num)
                nums_added += 1
            i -=1
        print(frequency_map)
        print(frequency_array)
        return output