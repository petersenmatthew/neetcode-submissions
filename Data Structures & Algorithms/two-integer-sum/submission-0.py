class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #1st solution (bad)
        # Can brute force it with two nested for loops
        # Outer loop iterates over all numbers.
        # Inner loop iterates over all numbers except that current number. 
        # If match returns the index of both loops. 

         # O(n) x O(n) = O(n^2)

        #2nd solution (better)


        hash_map = {}
        # value : index
        for index, value in enumerate(nums):
            print(hash_map)
            num = nums[index]
            difference = target - num
            if difference in hash_map:
                # return [index, differenceindex]
                return [hash_map[difference], index]
            else:
                hash_map[num] = index
        return False
    