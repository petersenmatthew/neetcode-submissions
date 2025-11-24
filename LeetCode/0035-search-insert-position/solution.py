class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            # num should be at start:
            elif (i == 0 and target <= nums[0]):
                return 0
            elif (i > 0 and target <= nums[i] and target >= nums[i-1]):
                return i 
            # num at end
            elif (i == len(nums) - 1 and target >= nums[len(nums) - 1]):
                return len(nums)
            
