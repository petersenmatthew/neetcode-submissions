class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        for i in range(len(nums)):
            num1 = nums[i]
            for i2 in range(i + 1, len(nums)):
                num2 = nums[i2]

                if num1 + num2 == target:
                    return [i, i2]
