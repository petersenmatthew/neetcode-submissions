class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            # output[i] becomes the product of everything before it
            output[i] = nums[i - 1] * output[i - 1]
            
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output