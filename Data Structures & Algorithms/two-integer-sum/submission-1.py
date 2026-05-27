class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        # value / num : index

        # input array of nums:
        # return: indices of i and j that add up to target

        for index, num in enumerate(nums):
            difference = target - num
            if difference in hash_map:
                return [hash_map[difference], index]
            else:
                hash_map[num] = index