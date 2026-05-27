class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # inputs:
        # nums : list[]
        # k : int

        # output:
        # return the top k most frequent elements
        # list of size k

        hash_map = {}
        # key : value
        # num : frequency
        nums.sort()

        for num in nums: #(O (n))
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        sorted_hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        print(sorted_hash_map)
        sorted_keys = list(sorted_hash_map.keys())
        print(sorted_keys)
        result = []
        for i in range(k):
            result.append(sorted_keys[i])

        return result
