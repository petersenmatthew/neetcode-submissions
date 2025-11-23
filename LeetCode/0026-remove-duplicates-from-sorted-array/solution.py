class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] in nums[0:i]:
                del nums[i]
            else:
                i += 1
        return len(nums)
