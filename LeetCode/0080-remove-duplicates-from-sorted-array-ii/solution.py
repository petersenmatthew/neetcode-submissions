class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 2, 2
        while r < len(nums):
            # If current element is different from the one 
            # placed two positions ago, it's valid.
            if nums[r] != nums[l - 2]:
                nums[l] = nums[r]
                l += 1
            r+=1
        return l if len(nums) > 2 else len(nums)
